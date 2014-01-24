#!/bin/bash

PKGCATEGORY="${1%%/*}"
PKGNAME="${1##*/}"

if [ -x /usr/sbin/urpmi ]; then
  PKGINST='sudo urpmi --auto --no-verify-rpm'
elif [ -x /usr/bin/zypper ]; then
  PKGINST="sudo zypper install -y"
elif [ -x /usr/bin/yum ]; then
  PKGINST='sudo yum install -y'
elif [ -x /usr/bin/apt-get ]; then
  PKGINST='sudo apt-get install -y'
fi

# Language package: install only French language package
case "${PKGNAME}" in
  "k3b-i18n"|"koffice-i18n"|"tde-i18n") PKGNAME="${PKGNAME}-French";;
  "koffice") PKGNAME="${PKGNAME}-suite";;
esac

# Trinity Prefix, or not.
case "${PKGNAME}" in
  "trinity-"*|"qt3"|"python-qt3") PREFIX="";;
  "gnuchess"|"imlib1"|"lilypond"|"mftrace"|"pcsc-perl"|"torsocks"|"wv2") PREFIX="";;
  "curl") PREFIX="trinity-lib";;
  *) PREFIX="trinity-";;
esac

# Installing main package
eval ${PKGINST} "${PREFIX}${PKGNAME}" || exit 1

# Installing development package

# Applications do NOT have development packages
case "${PKGCATEGORY}" in
  "applications") if [ "${PKGNAME}" != "k3b" ]; then exit 0; fi;;
esac
# Other packags NOT having development package
case "${PKGNAME}" in
  "hal-info"|"lilypond"|"mftrace"|"pcsc-perl"|"torsocks") exit 0;;
  "tqca-tls"|"tdeadmin"|"tdetoys"|"tde-i18n"*|"tdeaddons"|"tdeartwork"|"libtqt-perl") exit 0;;
esac

eval ${PKGINST} "${PREFIX}${PKGNAME}-devel"
