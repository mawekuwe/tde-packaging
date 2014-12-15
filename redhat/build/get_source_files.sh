#!/bin/bash

PKGNAME="${1##*/}"
TDE_VERSION="${2:-14.0.0}"

[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1
SPECFILE=$(get_specfile.sh ${PKGNAME} ${TDE_VERSION})
SPECDIR="${SPECFILE%/*}"

[ ! -r "${SPECFILE}" ] && exit 2

while read var val; do
  case "${var}" in
    Version:*) VERSION="${val}";;
    Source[0-9]*:|Source:|Patch[0-9]*:)
      FILE=$(rpm --define "tde_pkg ${PKGNAME}" --define "tde_version ${TDE_VERSION}" --define "name ${PKGNAME}" --define "version ${VERSION}" -E "${SPECDIR}/${val##*/}")
      if [ -r "${FILE}" ]; then
        echo "${FILE}"
      else
        echo "Warning: cannot find '${FILE}'" >&2
      fi
    ;;
  esac
done < "${SPECFILE}"
