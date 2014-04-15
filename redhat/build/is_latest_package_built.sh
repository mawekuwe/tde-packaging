#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-14.0.0}"

BUILT=$(get_latest_built_package_version.sh ${PKGNAME} ${TDE_VERSION})
TARBALL=$(get_latest_tarball_version.sh ${PKGNAME} ${TDE_VERSION})
RPM_PKGNAME="$(get_rpm_package_name.sh ${PKGNAME})"

# If package version contains a "~": it's a pre-release
if [ "${BUILT/\~/}" != "${BUILT}" ]; then
  if [ "${BUILT#*\~}" = "${TARBALL#*\~}" ]; then
    echo "Latest package '${PKGNAME}' version '${BUILT}' is already built."
    exit 0
  fi
# Nominal case: no "~" caracter
else
  if [ "${TARBALL%-*}" = "${BUILT%-*}" ]; then
    echo "Latest package '${PKGNAME}' version '${BUILT}' is already built."
    exit 0
  fi
fi

exit 1
