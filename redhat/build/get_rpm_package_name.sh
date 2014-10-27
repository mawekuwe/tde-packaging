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
  # In case prefix is already there, don't add it again.
  "trinity-"*) PREFIX="";;
  # Most TDE dependencies have no prefix
  "avahi-tqt"|"dbus-tqt"|"dbus-1-tqt"|"libart-lgpl"|"libcarddav"|"libcaldav"|"python-tqt"|"sip4-tqt"|"qt3"|"tqscintilla"|"tqt3"|"tqtinterface") PREFIX="";;
  # 3rd party dependencies
  "esound"|"fileshareset"|"hk_classes"|"python-qt3") PREFIX="";;
  # Extra build stuff
  "autoconf"|"automake"|"cmake"|"gnuchess"|"htdig"|"imlib1"|"libconfig"|"libotr3"|"libtool"|"lilypond"|"m4"|"mftrace"|"pan"|"pcsc-perl"|"torsocks"|"wv2") PREFIX="";;
  # Other
  "curl") PREFIX="trinity-lib";;
  # Default case: add prefix
  *) PREFIX="trinity-";;
esac

# Runtime packages
if [ -r /etc/mandriva-release ]; then
  lib=$(rpm -E %_lib)
else
  lib="lib"
fi

case "${PKGNAME}" in
  # Some packages have different runtime name than source package.
  "avahi-tqt") PKGRUNTIME="${lib}avahi-tqt1";;
  "dbus-tqt") PKGRUNTIME="${lib}dbus-tqt-1-0";;
  "dbus-1-tqt") PKGRUNTIME="${lib}dbus-1-tqt0";;
  "esound") PKGRUNTIME="esound-libs";;
  "koffice") PKGRUNTIME="koffice-suite";;
  "libart-lgpl") PKGRUNTIME="${lib}art_lgpl_2-2";;
  "libcaldav") PKGRUNTIME="${lib}caldav0";;
  "libcarddav") PKGRUNTIME="${lib}carddav0";;
  "tqscintilla") PKGRUNTIME="${lib}tqscintilla7";;
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
    "extras") if [ "${PKGNAME}" != "akode" ] && [ "${PKGNAME}" != "hk_classes" ]; then exit 0; fi;;
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
    "pan") PKGDEVEL="uulib-devel";;
    "libart-lgpl") PKGDEVEL="libart_lgpl-devel";;
    "libcaldav") PKGDEVEL="${lib}caldav-devel";;
    "libcarddav") PKGDEVEL="${lib}carddav-devel";;
    "tqscintilla") PKGDEVEL="${lib}tqscintilla-devel";;
    "tqt3") PKGDEVEL="tqt3-dev-tools tqt3-apps-devel tqt3-compat-headers";;
    # Default case: development package has same name as runtime package, plus '-devel' suffix.
    *) PKGDEVEL="${PKGRUNTIME}-devel";;
  esac

  # Finally, other packages do have a '-devel'
  echo "${PREFIX}${PKGDEVEL}"
fi

