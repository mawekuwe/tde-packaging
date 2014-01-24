#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-14.0.0}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1
SPECFILE=$(get_specfile.sh ${PKGNAME} ${TDE_VERSION})
SPECDIR="${SPECFILE%/*}"

[ ! -r "${SPECFILE}" ] && exit 2

while read var val; do
  case "${var}" in
    Source[0-9]*:|Source:|Patch[0-9]*:)
      FILE=$(rpm -E "${SPECDIR}/${val##*/}")
      if [ -r "${FILE}" ]; then
        echo "${FILE}"
      fi
    ;;
  esac
done < "${SPECFILE}"
