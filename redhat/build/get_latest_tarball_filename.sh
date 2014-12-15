#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-14.0.0}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1
[ -d "${TARBALLS_DIR}" ] || TARBALLS_DIR=~/tde/tde-tarballs/${TDE_VERSION}/
[ -d "${TDE_PACKAGING_DIR}" ] || TDE_PACKAGING_DIR=~/tde/tde-packaging
[ -d "${DIST_PACKAGING_DIR}" ] || DIST_PACKAGING_DIR=${TDE_PACKAGING_DIR}/redhat/

EXTRA_DIR="$(cd ${TARBALLS_DIR}/../extras/; pwd)"

RET=$(find "${TARBALLS_DIR}" -name "trinity-${PKGNAME}-${TDE_VERSION}*.tar.gz" | sort -n | tail -n 1)
[ -r "${RET}" ] && echo "${RET}" && exit 0

RET=$(find "${TARBALLS_DIR}" "${EXTRA_DIR}" -name "${PKGNAME}-${TDE_VERSION}*.tar.gz" | sort -n | tail -n 1)
[ -r "${RET}" ] && echo "${RET}" && exit 0

RET=$(find "${TARBALLS_DIR}" -name "trinity-${PKGNAME}-[0-9]*.tar.gz" | sort -n | tail -n 1)
[ -r "${RET}" ] && echo "${RET}" && exit 0

RET=$(find "${EXTRA_DIR}" -name "${PKGNAME}[-_][0-9]*.tar.*" | sort -n | tail -n 1)
[ -r "${RET}" ] && echo "${RET}" && exit 0

# Now look in the 'tde-packaging' directory
RET=$(find "${DIST_PACKAGING_DIR}" -name "${PKGNAME}-[0-9]*.tar*" | sort -n | tail -n 1)
[ -r "${RET}" ] && echo "${RET}" && exit 0

# Retry without 'trinity-*', and allow any TAR extension.
RET=$(find "${DIST_PACKAGING_DIR}" -name "${PKGNAME}-[0-9]*.tar*" | sort -n | tail -n 1)
[ -r "${RET}" ] && echo "${RET}" && exit 0

# Retry without 'trinity-*', and allow any TAR extension.
RET=$(find "${DIST_PACKAGING_DIR}" -name "${PKGNAME}-[0-9]*.tar*" | sort -n | tail -n 1)
[ -r "${RET}" ] && echo "${RET}" && exit 0

# Retry by removing numbers in package name, e.g "imlib1" => "imlib"
RET=$(find "${DIST_PACKAGING_DIR}" -name "$(tr -d "[0-9]" <<< ${PKGNAME})-[0-9]*.tar*" | sort -n | tail -n 1)
[ -r "${RET}" ] && echo "${RET}" && exit 0


exit 0
