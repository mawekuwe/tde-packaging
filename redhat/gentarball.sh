#!/bin/bash

cd "$( dirname "$0" )"

# Default TDE version (if unspecified in 'components.txt')
DEFAULT_VERSION="3.5.12.99"

clear
cat <<EOF
This script generates a source tarball of TDE from the SVN/GIT repository.
Please choose a TDE component to archive or build.

EOF


##### CHOOSE A TDE COMPONENT #####
PS3="Enter number: "
select COMP in $( cut -f1 components.txt ) ; do
	ARCHIVEDIR="${PWD}/${COMP}"
	[ -d "${ARCHIVEDIR}" ] || mkdir -p "${ARCHIVEDIR}"

	VERSION=$( awk '{ if ($1 == "'${COMP}'") { print $2; } }' components.txt )
	if [ -z "${VERSION}" ]; then VERSION=${DEFAULT_VERSION}; fi

	# List existing tarballs
	if ls ${ARCHIVEDIR}/${COMP##*/}*.tar.gz >/dev/null 2>&1; then
		echo
		echo "You currently have the following tarball(s): "
		for i in ${ARCHIVEDIR}/${COMP##*/}*.tar.gz; do echo "  ${i##*/}"; done
	fi
	
	# Checks latest SVN revision
	SVNREV=$( LANG=C svn info svn://anonsvn.kde.org/home/kde/branches/trinity/dependencies/tqtinterface|sed -n "/^Revision: / s,.* \(.*\),\1,p" )
	ARCHIVENAME=${COMP##*/}-${VERSION}.${SVNREV}.tar.gz

	if [ -r ${ARCHIVEDIR}/${ARCHIVENAME} ]; then
		echo "You already have the latest revision (${SVNREV})";
	fi
	
	echo
	echo "Press ENTER to download a new version, or CTRL+C to abort."
	read rep

	TMPDIRTDE=$(mktemp -d)
	pushd "${TMPDIRTDE}" >/dev/null
	mkdir -p "${TMPDIRTDE}/${COMP}"
	pushd "${COMP}/.." >/dev/null
	echo "Extracting '${COMP}' from SVN ..."
	case "${COMP##*/}" in
		"qt3") git clone http://scm.trinitydesktop.org/scm/git/tde; mv tde/main/dependencies/qt3 . ;;
		*) svn export --force --quiet svn://anonsvn.kde.org/home/kde/branches/trinity/${COMP} ;;
	esac
	popd >/dev/null

	echo "Creating archive '${ARCHIVENAME}' ..."
	tar cfz ${ARCHIVEDIR}/${ARCHIVENAME} ${COMP}
	popd >/dev/null
	echo "Cleaning temporary directory ..."
	rm -rf "${TMPDIRTDE}"
	cat <<EOF

Resulting archive:
EOF
	\ls -l ${ARCHIVEDIR}/${ARCHIVENAME}
	echo
	echo "Have a nice day !"
	break
done