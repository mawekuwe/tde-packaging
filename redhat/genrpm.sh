#!/bin/bash

cd "$( dirname "$0" )"
ARGS=""

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
if [ "${RHEL}" = "%{rhel}" ] && [ "${FEDORA}" = "%{fedora}" ]; then
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
		set $( cd "${COMP}"; echo ${COMP##*/}*-${REQVERSION}.tar.gz)
	else
		set $( cd "${COMP}"; echo ${COMP##*/}*.tar.* )
	fi
	if [ $# -gt 1 ]; then
		select VERSION in $*; do break; done
	elif [ -r "${COMP}/$1" ]; then
		VERSION="$1"
	elif [ "${COMP}" = "trinity-live" ]; then
		VERSION="3.5.13"
	else
		echo "No source tarball found for '${COMP}' !"
		exit 0
	fi
	VERSION="${VERSION##${COMP##*/}-}"
	VERSION="${VERSION%%.tar.gz}"
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

Press ENTER to build, or CTRL+C to abort.
EOF
[ -z "${AUTO}" ] && read rep
	
# Specific prefix for installation of some components
case "${COMP##*/}" in
	"qt3"|"libkarma") PREFIX="/usr";;
esac
	
# Determines if we are running an i386 or x86_64 distro
if [ "$(rpm -q --qf '%{arch}\n' kernel | tail -n 1)" = "i686" ]; then
	ARGS="${ARGS} --target=i686"
fi

LOGFILE=/tmp/log.${COMP##*/}

set -x
(
rpmbuild -ba \
	${ARGS} \
	--define "_sourcedir ${PWD}/${COMP}" \
	--define "_prefix ${PREFIX:-/opt/trinity}" \
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
