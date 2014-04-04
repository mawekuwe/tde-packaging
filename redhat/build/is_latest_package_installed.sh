#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-14.0.0}"

INSTALLED=$(get_installed_package_version.sh ${PKGNAME} ${TDE_VERSION})
TARBALL=$(get_latest_tarball_version.sh ${PKGNAME} ${TDE_VERSION})
SPEC=$(get_spec_version.sh ${PKGNAME} ${TDE_VERSION})

# Package containing "~" (e.g. R14 preversion tarballs):
if [ "${INSTALLED/\~/}" != "${INSTALLED}" ]; then
  if [ "${INSTALLED#*\~}" = "${TARBALL#*\~}" ]; then
    echo "Latest package '${PKGNAME}' version '${TARBALL}' is already built and installed."
    exit 0
  fi
else
  # Other package (e.g. akode)
  if [ "${INSTALLED%-*}" = "${TARBALL%-*}" ]; then
    echo "Latest package '${PKGNAME}' version '${INSTALLED}' is already built and installed."
    exit 0
  fi
  
  # Other package (e.g. QT3)
  if [ "${INSTALLED}" = "${SPEC}" ]; then
    echo "Latest package '${PKGNAME}' version '${INSTALLED}' is already built and installed."
    exit 0
  fi
fi

exit 1
