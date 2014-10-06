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

# Some RPM packages have different name than the source tarball.

# Some runtime packages are prefixed with 'trinity-', some are not.
case "${PKGNAME}" in
  "trinity-"*|"qt3"|"tqt3"|"tqtinterface"|"python-qt3"|"esound"|"avahi-tqt"|"dbus-tqt"|"dbus-1-tqt"|"libart-lgpl"|"fileshareset") PREFIX="";;
  "autoconf"|"automake"|"cmake"|"gnuchess"|"htdig"|"imlib1"|"libotr3"|"libtool"|"lilypond"|"m4"|"mftrace"|"pcsc-perl"|"torsocks"|"wv2") PREFIX="";;
  "curl") PREFIX="trinity-lib";;
  *) PREFIX="trinity-";;
esac

# Runtime packages
lib=$(rpm -E %_lib)
case "${PKGNAME}" in
  # Some packages have different runtime name than source package.
  "avahi-tqt") PKGRUNTIME="${lib}avahi-tqt1";;
  "dbus-tqt") PKGRUNTIME="${lib}dbus-tqt-1-0";;
  "dbus-1-tqt") PKGRUNTIME="${lib}dbus-1-tqt0";;
  "esound") PKGRUNTIME="esound-libs";;
  "koffice") PKGRUNTIME="trinity-koffice-suite";;
  "libart-lgpl") PKGRUNTIME="${lib}art_lgpl_2-2";;
  "tqt3") PKGRUNTIME="${lib}tqt3-mt";;
  "tqtinterface") PKGRUNTIME="${lib}tqt4";;
  # Language package: install only French language package
  "k3b-i18n"|"koffice-i18n"|"tde-i18n") PKGRUNTIME="${PKGNAME}-French";;
  # Default case: runtime package has same name as source package
  *) PKGRUNTIME="${PKGNAME}";;
esac

# Finally, display the runtime package name.
echo "${PREFIX}${PKGRUNTIME}"

# Development package.
if [ -n "${DEVEL}" ]; then
  # Check if development package is required.
  case "${PKGCATEGORY}" in
    # Applications do NOT have 'devel' package, except K3B.
    "applications") if [ "${PKGNAME}" != "k3b" ]; then exit 0; fi;;
    # Extras packages do NOT have 'devel' package, except Akode
    "extras") if [ "${PKGNAME}" != "akode" ]; then exit 0; fi;;
  esac
  
  # Some other packags NOT having development package
  case "${PKGNAME}" in
    "hal-info"|"lilypond"|"mftrace"|"pcsc-perl"|"torsocks") exit 0;;
    "tqca-tls"|"tdeadmin"|"tdetoys"|"tde-i18n"*|"tdeaddons"|"tdeartwork"|"libtqt-perl") exit 0;;
  esac

  # Some package have specific development package.
  case "${PKGNAME}" in
    "avahi-tqt") PKGDEVEL="libavahi-tqt-devel";;
    "dbus-tqt") PKGDEVEL="libdbus-tqt-1-devel";;
    "dbus-1-tqt") PKGDEVEL="libdbus-1-tqt-devel";;
    "esound") PKGDEVEL="esound-devel";;
    "libart-lgpl") PKGDEVEL="libart_lgpl-devel";;
    "tqt3") PKGDEVEL="tqt3-dev-tools tqt3-apps-devel";;
    # Default case: development package has same name as runtime package, plus '-devel' suffix.
    *) PKGDEVEL="${PKGRUNTIME}-devel";;
  esac

  # Finally, other packages do have a '-devel'
  echo "${PREFIX}${PKGDEVEL}"
fi

