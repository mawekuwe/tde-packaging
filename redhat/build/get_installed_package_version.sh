#!/bin/bash

# Sample package name: trinity-tdelibs-14.0.0-0_pre727+6be06b3d.mga3.opt

PKGNAME="${1##*/}"
[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1

# Language package: install only French language package
case ${PKGNAME} in
  "k3b-i18n"|"koffice-i18n"|"tde-i18n") PKGNAME="${PKGNAME}-French";;
  "koffice") PKGNAME="${PKGNAME}-suite";;
  "trinity-"*) PKGNAME="${PKGNAME#trinity-}";;
  "qt3") [ -r /etc/mandriva-release ] && PKGNAME="qt3-common";;
  "curl") PKGNAME="trinity-libcurl";;
esac

VERSION=$(LC_ALL=C rpm -q --qf "%{version}-%{release}" trinity-${PKGNAME} 2>/dev/null)
if [ -z "${VERSION}" ] || [[ "${VERSION}" =~ "not installed" ]]; then
	VERSION=$(LC_ALL=C rpm -q --qf "%{version}-%{release}" ${PKGNAME})
fi

VERSION=${VERSION/-*_/\~}
VERSION=${VERSION%-[0-9]}
VERSION=${VERSION%.opt}
VERSION=${VERSION%.*}

echo $VERSION
