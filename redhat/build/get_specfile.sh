#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-14.0.0}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1

[ -d "${TDE_SPECDIR}" ] || TDE_SPECDIR=~/tde/tde-packaging/redhat

# Special case for QT3
if [ "${PKGNAME}" = "qt3" ]; then
  case "$(rpmdist.sh --dist)" in
    .oss*) TDE_SPECDIR=~/tde/tde-packaging/opensuse ;;
    .mga*|.mdk*|.pclos*) TDE_SPECDIR=~/tde/tde-packaging/mageia ;;
  esac
fi

SPECFILE=$(find "${TDE_SPECDIR}" -name "${PKGNAME}-${TDE_VERSION}.spec")
if [ ! -r "${SPECFILE}" ]; then
  SPECFILE=$(find "${TDE_SPECDIR}" -name "${PKGNAME}.spec")
  if [ ! -r "${SPECFILE}" ]; then
    SPECFILE=$(find "${TDE_SPECDIR}" -name "trinity-${PKGNAME}-${TDE_VERSION}.spec")
    if [ ! -r "${SPECFILE}" ]; then
      SPECFILE=$(find "${TDE_SPECDIR}" -name "trinity-${PKGNAME}.spec")
    fi
  fi
fi

echo ${SPECFILE}
