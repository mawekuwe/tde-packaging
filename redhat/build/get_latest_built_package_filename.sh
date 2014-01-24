#!/bin/bash

PKGNAME="$1"
[ -z "${PKGNAME}" ] && echo "You must specify a package name !" && exit 1

RPMDIR=$(rpm -E %_rpmdir)

RPM=$(find ${RPMDIR} -name "trinity-${PKGNAME}-[0-9]*.rpm" | sort -n | tail -n 1)

if [ ! -r "${RPM}" ]; then
  RPM=$(find ${RPMDIR} -name "${PKGNAME}-[0-9]*.rpm" | sort -n | tail -n 1)
  if [ ! -r "${RPM}" ]; then
    echo "Error, cannot find any package for '${PKGNAME}' !"
    exit 1
  fi
fi

echo $RPM
