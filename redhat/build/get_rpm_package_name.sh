#!/bin/bash

# Gets the RPM package name from the component name.
# This is useful because some RPM packages do not have prefix "trinity"
# while others do.
#
# E.g :
#  trinity-qt3 => qt3
#  trinity-tdelibs => trinity-tdelibs


PKGCATEGORY="${1%%/*}"
PKGNAME="${1##*/}"
DEVEL="$2"

# Language package: install only French language package
case "${PKGNAME}" in
  "k3b-i18n"|"koffice-i18n"|"tde-i18n") PKGNAME="${PKGNAME}-French";;
  "koffice") PKGNAME="${PKGNAME}-suite";;
esac

# Use the Trinity Prefix, or not.
case "${PKGNAME}" in
  "trinity-"*|"qt3"|"python-qt3"|"esound") PREFIX="";;
  "autoconf"|"automake"|"cmake"|"gnuchess"|"htdig"|"imlib1"|"libotr3"|"libtool"|"lilypond"|"m4"|"mftrace"|"pcsc-perl"|"torsocks"|"wv2") PREFIX="";;
  "curl") PREFIX="trinity-lib";;
  *) PREFIX="trinity-";;
esac

echo "${PREFIX}${PKGNAME}"

if [ -n "${DEVEL}" ]; then
  # Check if development package is required.
  # Applications do NOT have development packages, except K3B
  case "${PKGCATEGORY}" in
    "applications") if [ "${PKGNAME}" != "k3b" ]; then exit 0; fi;;
  esac
  # Other packags NOT having development package
  case "${PKGNAME}" in
    "hal-info"|"lilypond"|"mftrace"|"pcsc-perl"|"torsocks") exit 0;;
    "tqca-tls"|"tdeadmin"|"tdetoys"|"tde-i18n"*|"tdeaddons"|"tdeartwork"|"libtqt-perl") exit 0;;
  esac
  
  echo "${PREFIX}${PKGNAME}-devel"
fi

