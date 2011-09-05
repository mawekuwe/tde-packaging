#!/bin/bash

cd "$( dirname "$0" )"

clear
cat <<EOF
This script generates RPM of TDE from source tarball.
Please choose a TDE component to build.

EOF

# Checks RPMBUILD environment
if [ $( rpm -E "%{rhel}" ) = "%{rhel}" ] && [ $( rpm -E "%{fedora}" ) = "%{fedora}" ]; then
	cat <<EOF
Error: RPM macro %rhel or %fedora must be set to the distribution version to build !
E.g:
%rhel 6 
or
%fedora 15
EOF
	exit 1
fi

select COMP in $( cut -f1 "components.txt" ) ; do
	# Gets package version from 'components.txt' file
	VERSION=$( awk '{ if ($1 == "'${COMP}'") { print $2; } }' components.txt )
	
	# If no version is set in text file, get version number from source tarball name
	if [ -z "${VERSION}" ]; then
		set $( cd "${COMP}"; echo ${COMP##*/}*.tar.gz)
		if [ $# -gt 1 ]; then
			select VERSION in $*; do break; done
		elif [ -r "${COMP}/$1" ]; then
			VERSION="$1"
		else
			echo "No source tarball found for '${COMP}' !"
			continue
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
		select SPEC in $*; do break; done
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
	read rep
	
	# Specific prefix for installation of some components
	case "${COMP##*/}" in
		"qt3") PREFIX="/usr";;
	esac
	
	set -x
	rpmbuild -ba \
		--define "_sourcedir ${PWD}/${COMP}" \
		--define "_prefix ${PREFIX:-/opt/trinity}" \
		--define "version ${VERSION:-3.5.13}" \
		${COMP}/${SPEC} || exit 1
	set +x
done

