#!/bin/bash

tdp='cd ~/tde/tde-packaging/redhat'
#grp='tdp; ./genrpm.sh -v 3.5.13.2 -a'
grp='tdp; ./genrpm.sh -v 14.0.0 -a'

BUILDDIR="/dev/shm/BUILD${DIST}.$(uname -i)"
BUILDROOTDIR="/dev/shm/BUILDROOT${DIST}.$(uname -i)"

if [ -x /usr/sbin/urpmi ]; then
  PKGMGR="urpmi"
  PKGINST='sudo urpmi --auto --no-verify-rpm'
  PKGDEL='sudo urpme --auto'
  REPOUPDATE='(cd $(rpm -E %{_rpmdir}); genhdlist2 --clean --allow-empty noarch; genhdlist2 --clean --allow-empty $(uname -i); sudo urpmi.update rpmbuild.$(uname -i) rpmbuild.noarch)'
elif [ -x /usr/bin/zypper ]; then
  PKGMGR="zypper"
  PKGINST="zypper install -y"
  PKGDEL="zypper remove -y"
elif [ -x /usr/bin/yum ]; then
  PKGMGR="yum"
  PKGINST='sudo yum install -y'
  PKGDEL='sudo yum remove -y'
  REPOUPDATE='(cd $(rpm -E %{_rpmdir}); createrepo $(uname -i); createrepo noarch; sudo yum clean all --disablerepo="*" --enablerepo="rpmbuild*")'
fi

BUILDDIR=$(rpm -E "%{_builddir}")

echo "Package Manager is '${PKGMGR}'"

pkg_listlocal() {
  rpm -qa --qf "%{name} %{buildhost}\n" | while read a b; do case "$b" in *.vtf) echo $a;; esac;done
}

pkg_delall() {
  PKGDEL $(pkg_listlocal)
}

is_installed() {
  rpm -q "$1" &>/dev/null
  return $?
}

# Build package if not already installed
grpi() {
  if ! is_installed "${1##*/}" && ! is_installed trinity-"${1##*/}"; then
    eval ${grp} ${1}
    RET=$?
    if [ $RET -gt 0 ]; then
      echo "ERROR $RET !!!"
      exit $RET
    fi
  fi
}
# Build package if not already installed, then update repo
grpiu() {
  if ! is_installed "${1##*/}" && ! is_installed trinity-"${1##*/}"; then
    grpi "$1"
    eval ${REPOUPDATE}
  fi
}
# Build package if not already installed, then update repo, then install package
grpiui() {
  if ! is_installed "${1##*/}" && ! is_installed trinity-"${1##*/}"; then
    grpiu "$1"
    eval ${PKGINST} "trinity-${1##*/}"
  fi
}
# Build package if not already installed, then update repo, then install -devel package
grpiud() {
  if ! is_installed "${1##*/}" && ! is_installed trinity-"${1##*/}"; then
    grpiu "$1"
    eval ${PKGINST} "trinity-${1##*/}"
    eval ${PKGINST} "trinity-${1##*/}-devel"
  fi
}

# Build dependencies
rm -rf "${BUILDDIR}" "${BUILDROOTDIR}"
#if ! rpm -q libqt3-devel && ! rpm -q lib64qt3-devel && ! rpm -q qt3-devel; then
#  grpiu dependencies/qt3
#  eval ${PKGINST} qt3-devel
#fi
grpiud dependencies/tqt3
grpiud dependencies/tqtinterface
grpi dependencies/arts
grpi dependencies/avahi-tqt
grpi dependencies/dbus-1-tqt
grpi dependencies/dbus-tqt
grpi dependencies/libcaldav
grpi dependencies/libcarddav
grpiud dependencies/tqca
grpiu dependencies/tqca-tls
eval ${PKGINST} trinity-tqca-tls trinity-dbus-1-tqt-devel

# Build main
# basic packages
rm -rf "${BUILDDIR}" "${BUILDROOTDIR}"
eval ${PKGINST} trinity-arts-devel trinity-avahi-tqt-devel trinity-dbus-tqt-devel
grpiud tdelibs
grpiud tdebase
# packages which are required by others
rm -rf "${BUILDDIR}" "${BUILDROOTDIR}"
eval ${PKGINST} trinity-libcaldav-devel trinity-libcarddav-devel
grpiud tdepim
grpiu extras/akode
eval ${PKGINST} trinity-akode-libmad trinity-akode-devel
grpiud tdemultimedia
grpiud tdegames
grpiud tdebindings
grpiud tdegraphics
grpiud tdenetwork
# other packages
rm -rf "${BUILDDIR}" "${BUILDROOTDIR}"
grpiui tdeaccessibility
grpiui tdeaddons
grpiui tdeadmin
grpiui tdeartwork
grpiui tdeedu
grpiui tdetoys
grpiui tdeutils
grpiu extras/trinity-desktop
eval ${PKGINST} trinity-desktop
# devel packages
grpiud tdesdk
grpiui tdevelop
grpiui tdewebdev
eval ${PKGINST} trinity-desktop-devel

# Build libraries
rm -rf "${BUILDDIR}" "${BUILDROOTDIR}"
grpiud libraries/libkdcraw
grpiud libraries/libkexiv2
grpiud libraries/libkipi
grpiud libraries/libksquirrel
grpiud libraries/python-trinity
grpiu libraries/pytdeextensions
eval ${PKGINST} trinity-libpythonize0-devel trinity-pytdeextensions

# Build applications
rm -rf "${BUILDDIR}" "${BUILDROOTDIR}"
grpiud applications/k3b
grpiui applications/abakus
#grpiui applications/adept
grpiui applications/amarok
grpiui applications/basket
grpiui applications/bibletime
#grpiui applications/compizconfig-backend-kconfig
grpiui applications/digikam
grpiui applications/dolphin
grpiui applications/filelight
#grpiui applications/filelight-l10n
#grpiui applications/fusion-icon
grpiui applications/gtk-qt-engine
grpiui applications/gwenview
grpiui applications/gwenview-i18n
#grpiui applications/k3b
if ! is_installed trinity-k3b-i18n-fr; then
  grpiu applications/k3b-i18n
  eval ${PKGINST} trinity-k3b-i18n-fr
fi
grpiui applications/k9copy
grpiui applications/kaffeine
grpiui applications/kaffeine-mozilla
grpiui applications/katapult
grpiui applications/kbarcode
grpiui applications/kbfx
grpiui applications/kbookreader
grpiui applications/kchmviewer
grpiui applications/kcpuload
grpiui applications/kdbusnotification
grpiui applications/kdiff3
grpiui applications/kdirstat
grpiui applications/keep
#grpiui applications/kerry
#grpiui applications/kgtk-qt3
grpiui applications/kile
grpiui applications/kima
grpiui applications/kiosktool
grpiui applications/kmplayer
grpiui applications/kmyfirewall
grpiui applications/kmymoney
grpiui applications/knemo
grpiui applications/knetload
grpiui applications/knetstats
#grpiui applications/knetworkmanager
grpiui applications/knights
grpiui applications/knowit
grpiui applications/knutclient
if ! is_installed trinity-koffice-suite; then
  grpiu applications/koffice
  eval ${PKGINST} trinity-koffice-suite
fi
if ! is_installed trinity-koffice-i18n-French; then
  grpiu applications/koffice-i18n
  eval ${PKGINST} trinity-koffice-i18n-French
fi
grpiui applications/konversation
grpiui applications/kopete-otr
grpiui applications/kpicosim
grpiui applications/kpilot
grpiui applications/kpowersave
grpiui applications/krename
grpiui applications/krusader
grpiui applications/ksplash-engine-moodin
grpiui applications/ksquirrel
grpiui applications/kstreamripper
grpiui applications/ksystemlog
grpiui applications/ktechlab
grpiui applications/ktorrent
grpiui applications/kuickshow
grpiui applications/kvirc
grpiui applications/kvkbd
#grpiui applications/kvpnc
grpiui applications/piklab
grpiui applications/potracegui
grpiui applications/rosegarden
grpiui applications/smartcardauth
grpiui applications/smb4k
grpiui applications/soundkonverter
grpiui applications/tde-guidance
grpiui applications/tdeio-apt
grpiui applications/tdeio-locate
grpiui applications/tdeio-umountwrapper
grpiui applications/tderadio
grpiui applications/tde-style-lipstik
grpiui applications/tde-style-qtcurve
grpiui applications/tdesudo
grpiui applications/tdesvn
grpiui applications/tde-systemsettings
grpiui applications/tdmtheme
grpiui applications/tellico
grpiui applications/twin-style-crystal
grpiui applications/wlassistant
grpiui applications/yakuake
eval ${PKGINST} trinity-desktop-applications

# Build extra packages
grpiui extras/icons-crystalsvg-updated
grpiui extras/icons-kfaenza
grpiui extras/icons-oxygen
grpiui extras/kasablanca
grpiui extras/kbibtex
grpiui extras/kbiff
#grpiui extras/kcheckgmail
grpiui extras/kcmautostart
#grpiui extras/kdebluetooth
grpiui extras/kftpgrabber
grpiui extras/kickoff-i18n
grpiui extras/knmap
#grpiui extras/knoda
grpiui extras/ksensors
grpiui extras/kshowmail
grpiui extras/mplayerthumbs
grpiui extras/style-ia-ora
if ! is_installed trinity-tdeio-ftps-plugin; then
  grpiu extras/tdeio-ftps
  eval ${PKGINST} trinity-tdeio-ftps-plugin
fi
#grpiui extras/tdeio-sysinfo
grpiui extras/theme-baghira
grpiu 3rdparty/torsocks
eval ${PKGINST} torsocks
grpiui extras/tork
#grpiui extras/trinity-desktop
#grpiui extras/trinity-live
grpiui extras/twinkle
eval ${PKGINST} trinity-desktop-extras

eval ${PKGINST} trinity-desktop-all
