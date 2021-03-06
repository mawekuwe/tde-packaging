#!/bin/bash

PKGNAME="$1"
TDE_VERSION="${2:-14.0.0}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1

RPM=$(get_latest_built_package_filename.sh "${PKGNAME}" ${TDE_VERSION})

[ ! -r "${RPM}" ] && echo "No package found for '${PKGNAME}' !" && exit 2

VERSION=$(rpm -qp --qf "%{version}-%{release}" "${RPM}")
VERSION=${VERSION%.opt}
VERSION=${VERSION%.[a-z]*}
VERSION=${VERSION/-*_/\~}


echo $VERSION
