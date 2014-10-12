#!/bin/bash

PKGNAME="$1"
[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1
TDE_VERSION="${2:-14.0.0}"

RPMDIR="$(rpm -E %{_rpmdir}.tde-${TDE_VERSION})"
RPMDIR_ARCH="${RPMDIR}/$(rpm -E %_target_cpu)"
RPMDIR_NOARCH="${RPMDIR}/noarch"
RPMDIRS="${RPMDIR_ARCH} ${RPMDIR_NOARCH}"

case "${PKGNAME##*/}" in
  "tqt3") PKGNAME="libtqt3-mt";;
  "tqtinterface") PKGNAME="libtqt4";;
  "koffice") PKGNAME="koffice-suite";;
  "tde-i18n") PKGNAME="tde-i18n-French";;
esac

RPM=$(find ${RPMDIRS} -name "trinity-${PKGNAME##*/}-[0-9]*.rpm" | sort -n | tail -n 1)

if [ ! -r "${RPM}" ]; then
  RPM=$(find ${RPMDIRS} -name "${PKGNAME##*/}-[0-9]*.rpm" | sort -n | tail -n 1)
  if [ ! -r "${RPM}" ]; then
    echo "Error, cannot find any package for '${PKGNAME}' !"
    exit 1
  fi
fi

echo $RPM
