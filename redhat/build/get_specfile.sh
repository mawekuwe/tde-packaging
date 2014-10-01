#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-14.0.0}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1

[ -d "${PACKAGING_DIR}" ] || PACKAGING_DIR=~/tde/tde-packaging
[ -d "${DIST_PACKAGING_DIR}" ] || DIST_PACKAGING_DIR=${PACKAGING_DIR}/redhat

# Special case for QT3
if [ "${PKGNAME}" = "qt3" ]; then
  case "$(rpmdist.sh --dist)" in
    .oss*) DIST_PACKAGING_DIR=${PACKAGING_DIR}/opensuse ;;
    .mga*|.mdk*|.pclos*) DIST_PACKAGING_DIR=${PACKAGING_DIR}/mageia ;;
  esac
fi

SPECFILE=$(find "${DIST_PACKAGING_DIR}" -name "${PKGNAME}-${TDE_VERSION}.spec")
if [ ! -r "${SPECFILE}" ]; then
  SPECFILE=$(find "${DIST_PACKAGING_DIR}" -name "${PKGNAME}.spec")
  if [ ! -r "${SPECFILE}" ]; then
    SPECFILE=$(find "${DIST_PACKAGING_DIR}" -name "trinity-${PKGNAME}-${TDE_VERSION}.spec")
    if [ ! -r "${SPECFILE}" ]; then
      SPECFILE=$(find "${DIST_PACKAGING_DIR}" -name "trinity-${PKGNAME}.spec")
    fi
  fi
fi

echo ${SPECFILE}
