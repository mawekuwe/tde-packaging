#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-14.0.0}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1

[ -d "${PACKAGING_DIR}" ] || PACKAGING_DIR=~/tde/tde-packaging/redhat

# Special case for QT3
if [ "${PKGNAME}" = "qt3" ]; then
  case "$(rpmdist.sh --dist)" in
    .oss*) PACKAGING_DIR=~/tde/tde-packaging/opensuse ;;
    .mga*|.mdk*|.pclos*) PACKAGING_DIR=~/tde/tde-packaging/mageia ;;
  esac
fi

SPECFILE=$(find "${PACKAGING_DIR}" -name "${PKGNAME}-${TDE_VERSION}.spec")
if [ ! -r "${SPECFILE}" ]; then
  SPECFILE=$(find "${PACKAGING_DIR}" -name "${PKGNAME}.spec")
  if [ ! -r "${SPECFILE}" ]; then
    SPECFILE=$(find "${PACKAGING_DIR}" -name "trinity-${PKGNAME}-${TDE_VERSION}.spec")
    if [ ! -r "${SPECFILE}" ]; then
      SPECFILE=$(find "${PACKAGING_DIR}" -name "trinity-${PKGNAME}.spec")
    fi
  fi
fi

echo ${SPECFILE}
