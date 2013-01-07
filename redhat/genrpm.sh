#!/bin/bash

cd "$( dirname "$0" )"
ARGS=""

eval TARBALLS_DIR=~/tde/3.5.13.1

if [ ! -d /var/cache/ccache ]; then
  DIST="$(rpmdist.sh --dist)"
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
Please choose a TDE component to build.

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
if [ -z "${VERSION}" ]; then
	if [ -n "${REQVERSION}" ]; then
		set $( cd "${TARBALLS_DIR}"; echo ${COMP##*/}*-${REQVERSION%-sru}*.tar.gz)
	else
		set $( cd "${TARBALLS_DIR}"; echo ${COMP##*/}*.tar.* )
	fi
	if [ $# -gt 1 ]; then
		select VERSION in $*; do break; done
	elif [ -r "${TARBALLS_DIR}/$1" ]; then
		VERSION="$1"
	elif [ "${COMP}" = "trinity-live" ]; then
		VERSION="3.5.13"
	else
		echo "No source tarball found for '${COMP}' !"
		exit 0
	fi
	VERSION="${VERSION##${COMP##*/}-}"
	VERSION="${VERSION%%.tar.gz}"
	VERSION="${VERSION%%.tar.bz2}"
# If version is defined in spec file: appends the date
else
	VERSION="${VERSION}.$(date +%Y%m%d)"
fi
	
# Chooses a spec file (if many)
set $( cd "${COMP}"; echo *.spec )
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
	exit 2
fi
	
cat <<EOF

About to build '${COMP}':
  Version: '${VERSION}'
  Spec file: '${SPEC}'

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
cp -rf "${PWD}/${COMP}/"* "${SOURCEDIR}"
# Puts the TARBALL in SOURCEDIR
cp -f "${TARBALLS_DIR}/${COMP}-"*.tar* "${SOURCEDIR}"

BUILDDIR="/dev/shm/BUILD${DIST}.$(uname -i)"
BUILDROOTDIR="/dev/shm/BUILDROOT${DIST}.$(uname -i)"

set -x
(
rpmbuild -ba \
	${ARGS} \
	--define "_sourcedir ${SOURCEDIR}" \
    --define "_builddir ${BUILDDIR}" \
    --define "_buildrootdir ${BUILDROOTDIR}" \
	--define "tde_prefix ${PREFIX:-/opt/trinity}" \
	--define "version ${VERSION:-3.5.13}" \
	${COMP}/${SPEC} || exit 1
) 2>&1 | tee ${LOGFILE}
RET=$?
set +x

if [ ${RET} -gt 0 ]; then
	exit ${RET}
fi

if grep -q "error: Failed build dependencies:" ${LOGFILE}; then
#	DEPS=$( sed -n -e "/.* is needed by .*/ s/^[ \t]*\([a-zA-Z2-9_-]*\) .*/\1/p" ${LOGFILE} )
	set $( grep " is needed by " ${LOGFILE} | cut -d " " -f1 )
	exit 2
fi

rm -rf "${SOURCEDIR}"
