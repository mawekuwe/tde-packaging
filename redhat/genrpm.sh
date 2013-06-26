#!/bin/bash

cd "$( dirname "$0" )"
ARGS=""

#eval TARBALLS_DIR=~/tde/tde-tarballs/3.5.13.2
eval TARBALLS_DIR=~/tde/tde-tarballs/14.0.0
DIST="$(rpmdist.sh --dist)"

# CCACHE related stuff
if [ ! -d /var/cache/ccache ]; then
  [ -z "${DIST}" ] && DIST="$(rpm -E "%{dist}")"
  if [ -n "${DIST}" ]; then
    export CCACHE_DIR=~/.ccache${DIST}.$(uname -m)
  fi
fi

while [ $# -gt 0 ]; do
  case "$1" in
    "--auto"|"-a") AUTO=1;;
    "--version"|"-v") REQVERSION="$2"; shift;;
    "--"*) ARGS="${ARGS} $1";;
    *) COMP="${1%%/}";;
  esac
  shift
done

clear
cat <<EOF
$(< /etc/redhat-release) [$(uname -m)]
This script generates RPM of TDE from source tarball.

EOF

# Checks RPMBUILD environment
RHEL="$( rpm -E "%{rhel}" )"
FEDORA="$( rpm -E "%{fedora}" )"
SUSE="$( rpm -E "%{suse_version}" )"
PCLINUXOS="$( rpm -E "%{pclinuxos}" )"
MGAVERSION="$( rpm -E "%{mgaversion}" )"
if [ "${RHEL}" = "%{rhel}" ] && [ "${FEDORA}" = "%{fedora}" ] && [ "${SUSE}" = "%{suse_version}" ] && [ "${PCLINUXOS}" = "%{pclinuxos}" ] && [ "${MGAVERSION}" = "%{mgaversion}" ] ; then
  cat <<EOF
Error: RPM macro %rhel or %fedora must be set to the distribution version to build !
E.g:
  %rhel 6 
or:
  %fedora 15
EOF
  exit 1
fi

# Checks TDE version to use
#if [ -z "${REQVERSION}" ]; then
#	REQVERSION="3.5.13"
#fi

if [ -z "${COMP}" ]; then
  select COMP in $( cut -f1 "components.txt" | grep -v "^#" ) ; do break; done
fi

# Gets package version from 'components.txt' file
VERSION=$( awk '{ if ($1 == "'${COMP}'") { print $2; } }' components.txt )
	
# If no version is set in text file, get version number from source tarball name
COMPNAME="${COMP##*/}"
if [ -z "${VERSION}" ]; then
  for d in "${TARBALLS_DIR}/main/${COMP%/*}" "${TARBALLS_DIR}/main/" "${PWD}/main/${COMP}/"; do
    for n in "trinity-${COMPNAME}-${REQVERSION:-*}.tar.gz" "trinity-${COMPNAME}?-${REQVERSION:-*}.tar.gz" "trinity-${COMPNAME/kde/tde}-${REQVERSION:-*}.tar.gz"  "trinity-${COMPNAME/kde/tde}-${REQVERSION:-*}*.tar.gz"; do
#      echo $d/$n
      set $d/$n
      if [ $# -eq 0 ]; then
        echo "No tarball found !"
        exit 1
      elif [ $# -eq 1 ] && [ -r "$1" ]; then
        TARBALL=$1
      elif [ $# -gt 1 ]; then
        select TARBALL in $*; do break; done
      fi
    done
  done

  echo "TARBALL is ${TARBALL##*/}"
fi

# Checks for version
if [ -z "${VERSION}" ] && [ -n "${REQVERSION}" ]; then
  VERSION="${REQVERSION}"
fi

# Checks for preversion (non-final)
if [ "${TARBALL}" != "${TARBALL%%~pre*}" ]; then
  PREVERSION="${TARBALL##*~}"
  PREVERSION="${PREVERSION%.tar*}"
fi
	
# Chooses a spec file (if many)
set $( cd "${COMP}"; echo *${COMP##*/}*.spec )
if [ $# -gt 1 ]; then
	if [ -n "${REQVERSION}" ]; then
		set $( cd "${COMP}"; echo *-${REQVERSION}.spec )
		SPEC="$1"
	else
		select SPEC in $*; do break; done
	fi
elif [ -r "${COMP}/$1" ]; then
	SPEC="$1"
else
	echo "Fatal: no spec file found !"
	echo $1
	exit 2
fi
	
cat <<EOF

About to build '${COMP}':
  Version: '${VERSION}'
  Preversion: '${PREVERSION}'
  Spec file: '${SPEC}'
  Tarball: '${TARBALL}'

CCACHE_DIR='${CCACHE_DIR}'

Press ENTER to build, or CTRL+C to abort.
EOF
[ -z "${AUTO}" ] && read rep
	
# Specific prefix for installation of some components
case "${COMP##*/}" in
	"qt3") PREFIX="/usr";;
esac
	
# Determines if we are running an i386 or x86_64 distro
if [ "$(rpm -q --qf '%{arch}\n' kernel | tail -n 1)" = "i686" ]; then
	ARGS="${ARGS} --target=i686"
fi

LOGFILE=/tmp/log.${COMP##*/}

SOURCEDIR="$(mktemp -d)"
# Puts the GIT files in SOURCEDIR
#rsync -rLv "${PWD}/${COMP}/" "${SOURCEDIR}/"
while read a b; do
  case "${a}" in
    "Source"*|"Patch"*)
      b=$(rpm -E "${b##*/}")
      [ -r "${COMP}/${b}" ] && cp -fv "${COMP}/${b}" "${SOURCEDIR}"
    ;;
  esac
done < "${COMP}/${SPEC}"

# Copies the SPEC file
cp -f "${COMP}/${SPEC}" "${SOURCEDIR}"

# Puts the TARBALL in SOURCEDIR
#cp -f "${TARBALLS_DIR}/${COMP}-"*.tar* "${SOURCEDIR}"
echo "Copying TARBALL ..."
cp -fv "${TARBALL}" "${SOURCEDIR}"

if [ $(hostname) = "aria.vtf" ]; then
	BUILDDIR="$HOME/rpmbuild/BUILD/BUILD${DIST}.$(uname -i)"
	BUILDROOTDIR="$HOME/rpmbuild/BUILDROOT/BUILDROOT${DIST}.$(uname -i)"
else
	BUILDDIR="/dev/shm/BUILD${DIST}.$(uname -i)"
	BUILDROOTDIR="/dev/shm/BUILDROOT${DIST}.$(uname -i)"
fi

TOPSRCRPMDIR="$(rpm -E %_srcrpmdir)"
TOPRPMDIR="$(rpm -E %_rpmdir)"
SUBDIR="${COMP%/*}"
if [ "${SUBDIR}" = "${COMP}" ]; then
	SUBDIR="main"
fi
RPMDIR="${TOPRPMDIR}/${SUBDIR}"
SRCRPMDIR="${TOPSRCRPMDIR}/${SUBDIR}"

[ -d "${BUILDDIR}" ] || mkdir "${BUILDDIR}"
[ -d "${BUILDROOTDIR}" ] || mkdir "${BUILDROOTDIR}"

set -x
(
rpmbuild -ba \
	${ARGS} \
	--define "_specdir ${SOURCEDIR}" \
	--define "_sourcedir ${SOURCEDIR}" \
	--define "_builddir ${BUILDDIR}" \
	--define "_buildrootdir ${BUILDROOTDIR}" \
	--define "tde_prefix ${PREFIX:-/opt/trinity}" \
	--define "version ${VERSION:-3.5.13.2}" \
	--define "preversion ${PREVERSION}" \
	${SOURCEDIR}/${SPEC}
	echo "RET=$?"
) 2>&1 | tee ${LOGFILE}
eval "$(grep ^RET= ${LOGFILE})"
set +x

if [ "${RET}" -gt 0 ]; then
	exit ${RET}
fi

if grep -q "error: Failed build dependencies:" ${LOGFILE}; then
#	DEPS=$( sed -n -e "/.* is needed by .*/ s/^[ \t]*\([a-zA-Z2-9_-]*\) .*/\1/p" ${LOGFILE} )
	set $( grep " is needed by " ${LOGFILE} | cut -d " " -f1 )
	exit 2
fi

set -x
rm -rf "${SOURCEDIR}"
#rm -rf "${BUILDDIR}/"*${COMP}-${VERSION}*
