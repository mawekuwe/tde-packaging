#!/bin/bash

# Sample package name: trinity-tdelibs-14.0.0-0_pre727+6be06b3d.mga3.opt

PKGNAME="${1##*/}"
[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1

# Language package: install only French language package
PKGNAME="$(get_rpm_package_name.sh ${PKGNAME})"

VERSION=$(LC_ALL=C rpm -q --qf "%{version}-%{release}" trinity-${PKGNAME} 2>/dev/null)
if [ -z "${VERSION}" ] || [[ "${VERSION}" =~ "not installed" ]]; then
	VERSION=$(LC_ALL=C rpm -q --qf "%{version}-%{release}" ${PKGNAME})
fi

VERSION=${VERSION/-*_/\~}
#VERSION=${VERSION%-[0-9]}
VERSION=${VERSION%.opt}
VERSION=${VERSION%.[a-z]*}

echo $VERSION
