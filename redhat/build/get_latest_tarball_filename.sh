#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-14.0.0}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1
[ -d "${TARBALLS_DIR}" ] || TARBALLS_DIR=~/tde/tde-tarballs/${TDE_VERSION}/
[ -d "${PACKAGING_DIR}" ] || PACKAGING_DIR=~/tde/tde-packaging/redhat/

RET=$(find "${TARBALLS_DIR}" -name "trinity-${PKGNAME}-[0-9]*.tar.gz" | sort -n | tail -n 1)
if [ ! -r "${RET}" ]; then
	# Retry without 'trinity-*', and allow any TAR extension.
	RET=$(find "${PACKAGING_DIR}" -name "${PKGNAME}-[0-9]*.tar*" | sort -n | tail -n 1)
	if [ ! -r "${RET}" ]; then
		# Retry by removing numbers in package name, e.g "imlib1" => "imlib"
		RET=$(find "${PACKAGING_DIR}" -name "$(tr -d "[0-9]" <<< ${PKGNAME})-[0-9]*.tar*" | sort -n | tail -n 1)
	fi
fi

[ -z "${RET}" ] && exit 2

echo "${RET}"
exit 0
