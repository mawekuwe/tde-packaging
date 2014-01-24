#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-14.0.0}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1

TARBALL=$(get_latest_tarball_filename.sh "${PKGNAME}" ${TDE_VERSION})

[ ! -r "${TARBALL}" ] && echo "No tarball found for '${PKGNAME}' !" && exit 2

VERSION=${TARBALL##*/}
VERSION=${VERSION#trinity-}
VERSION=${VERSION#${PKGNAME}-}
VERSION=${VERSION#*-}
VERSION=${VERSION%.tar.gz}
VERSION=${VERSION%.tar.bz2}
echo "$VERSION"
