#
# spec file for package kdebase3
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

%if %suse_version < 1210 || 0%{?is_kde_kde3} > 0
%define with_hal 1
%else
%define with_hal 0
%endif

Name:           kdebase3
BuildRequires:  OpenEXR-devel cups-devel db-devel doxygen graphviz kdelibs3-devel krb5-devel libsmbclient-devel mDNSResponder-devel openldap2 openldap2-devel openmotif openmotif-devel openslp-devel openssh pam-devel pcsc-lite-devel qt3-devel-doc samba-client utempter xorg-x11
BuildRequires:  unsermake xorg-x11-libfontenc-devel
BuildRequires:  liblazy-devel 
%if %suse_version >= 1130
BuildRequires:  libusb-compat-devel
%endif
%if 0%{?with_hal} > 0
BuildRequires:  hal-devel
Provides:       kdebase3-with-hal-enabled
%endif
BuildRequires:  fdupes libbz2-devel
%ifnarch s390 s390x
BuildRequires:  libsensors4-devel
%endif
%define qt_path    /usr/lib/qt3
%define kde_path   /opt/kde3
Provides:       windowmanager kfontinst kdebase3-konqueror kdebase3-khotkeys
Obsoletes:      kfontinst kdebase3-konqueror kdebase3-khotkeys
# bug437293
%ifarch ppc64
Obsoletes:      kdebase3-64bit
%endif
#
Requires:       kdelibs3 >= %( echo `rpm -q --queryformat '%{VERSION}' kdelibs3`)
Requires:       xorg-x11 misc-console-font
Recommends:     kdelibs3_doc
Recommends:     gdb
PreReq:         fileshareset
%define	fileshare_prefix	%{_prefix}
Conflicts:      kdebase3-SuSE <= 9.0
PreReq:         /bin/sh fileutils permissions
%if %suse_version < 1120
Requires:       kdebase3-apps kdebase3-workspace
%endif
%if %suse_version > 1130
Provides:       kdebase3-beagle = 3.5.10
Obsoletes:      kdebase3-beagle <= 3.5.10
%endif
License:        GPLv2+
Group:          System/GUI/KDE
Summary:        The KDE Core Components
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://www.kde.org/
Version:        3.5.10.1
Release:        17
%define	kde_version	3.5.10
Requires:       kdebase3-runtime == %{version}
Source0:        kdebase-%{kde_version}.tar.bz2
Source1:        baselibs.conf
Source3:        startkde.suse.sh
Source4:        kdebase3.fillup
Source6:        ksysguardd.init
# we append this file for older dist verions
Source8:        mp3-info.tar.bz2
Source9:        wizard_small.png
# kicker gets messed up, if it got deinstalled
Source11:       kickerrc
# from HEAD/3.2:
Source12:       console8x16.pcf.gz
Source13:       fileshareset2.tar.bz2
Source914:      kdm-pam-np-legacy
Source15:       ksysguardd.reg
Source16:       stopkde.suse.sh
Source17:       zh_TW.flag.png
Source18:       fileshareset.8.gz
Source19:       kcheckpass.8.gz
Source20:       kickoff-data.tar.bz2
Source21:       kcheckpass-pam-11.1
Source921:      kcheckpass-pam-11.0
Source9921:     kcheckpass-pam-legacy
Source22:       bnc.desktop
Source23:       sourceforge.desktop
Source24:       devmon-automounter.sh
Patch0:         3_5_BRANCH.diff
Patch3:         startkde.diff
Patch5:         media-iPod.diff
Patch6:         ksysguardd-openslp.diff
Patch7:         fix-kio-smb-auth.diff
Patch8:         konsole_keytab.diff
Patch10:        kdesud-security.diff
Patch11:        clock-applet-style.diff
Patch12:        dont-always-start-kaccess.diff
Patch14:        autorun.patch
Patch15:        artwork.diff
# TODO
Patch16:        kfontinst.diff
Patch17:        nsplugin-Preference.diff
Patch20:        ksplashml.patch
Patch21:        media_suse.diff
Patch22:        libkonq-kdemm.diff
Patch39:        kdesktop_icons.diff
Patch40:        suse_default_move.diff
Patch44:        clock-suse-integrate.diff
Patch45:        klipperrc.diff
Patch46:        lock-xvkbd.diff
Patch51:        kcontrol.diff
Patch60:        short-menus.diff
# from http://fred.hexbox.de/kde_patches/kmenu-search-fs20050503.diff 
Patch61:        kmenu-search-fs20050503-fixed.diff
Patch62:        fix-kcontrol-yast.diff
Patch63:        quick_browser_menu.diff
Patch64:        default_fonts.diff
#kdm
Patch69:        kdm-cope-with-new-grub.diff
Patch70:        kdm-aliasing.diff
Patch71:        kdm-mark_autologin.diff
Patch72:        kdm-all-users-nopass.diff
Patch74:        kdm-sysconfig-values.diff
# svn diff $BASE/branches/KDE/3.5/kdebase/kdm@599257 $BASE/branches/work/coolos_kdm | sed -e "s,^+++ ,+++ kdm/,"
Patch75:        kdm-make_it_cool.diff
Patch76:        kdm-admin-mode.diff
Patch77:        kdm-suspend-hal.diff
Patch78:        kdm-relaxed-auth.diff
Patch79:        kdm-wordbreak.diff
Patch80:        non-fast-malloc.diff
Patch81:        ksmserver-defaulttohalt.diff
Patch82:        fix-lockup-from-gnome-apps.diff
Patch83:        ksmserver-suspend.diff
Patch84:        default-kdeprintfax.diff
Patch85:        ksmserver-tooltips.diff
Patch88:        hide-only-showin-entries.diff
Patch92:        kcminit-ignore-arts.diff
Patch94:        mach_blass.diff
Patch96:        khelpcenter-gnome-support.patch
Patch996:       khelpcenter-gnome-support-legacy.patch
Patch98:        workaround-pdf-on64bit-nsplugin-bug.diff
Patch99:        xcursor.diff
Patch100:       ksysguard-slp-ratelimit.diff
Patch104:       locale-dont-show-flag.diff
Patch105:       kscreensaver-random-NG.diff
Patch111:       fix_default_theme_reset.diff
Patch114:       improve-panelservicemenu-geticonset.diff
Patch116:       teach-minicli-lock.diff
Patch117:       access.diff
Patch120:       kmenu-search-slowdown-fix.diff
Patch123:       less_verbal_kdesu.patch
Patch125:       kicker-defaults.diff
Patch126:       kdebase_khc_rellinks.diff
Patch127:       khelpcenter-use-suseconfig-indexer.diff
Patch131:       background_default.diff
Patch141:       khelpcenter-use-susehelp.diff
Patch144:       make-wallpapers-hideable.diff
Patch145:       kdebase_networkstatus_branch.diff
Patch149:       kdeeject.diff
Patch155:       use-full-hinting-by-default.diff
Patch156:       kcmshell_use_kde-sound.diff
Patch157:       kcmsamba_log.diff
Patch160:       khelpcenter-localindices.patch
Patch161:       applet-lock-logout.diff
# svn diff $BASE/branches/KDE/3.5/kdebase/kicker@849788 $BASE/branches/work/suse_kickoff_qstyle/kicker | clean_patch
Patch162:       kickoff.diff
Patch1629:      kickoff-beagle.diff
# svn diff $BASE/branches/KDE/3.5/kdebase/kcontrol/kicker@755866 $BASE/branches/work/suse_kickoff_qstyle/kcontrol/kicker
Patch158:       kickoff-kcm.diff
# svn diff -r 551296:HEAD khelpcenter
Patch159:       khelpcenter-beagle.diff
Patch163:       xinerama.patch
Patch165:       optional-compmgr.diff
Patch166:       lowdiskspace.patch
Patch167:       ksmserver-timed.diff
Patch169:       systray_order.diff
Patch170:       khotkeys-multimedia-action.diff
Patch171:       khotkeys-multimedia-action2.diff
Patch172:       select-wm-gui.diff
Patch173:       suspend-unmount.diff
Patch174:       ksmserver-kdeinit.diff
Patch177:       kio-media-errorhandling.diff
Patch179:       restore-description-parens.diff
Patch180:       kompmgr_use_defaults.diff
Patch189:       runupdater.patch
Patch190:       kcontrol-energy.diff
Patch195:       ioslaveinfo-icon.diff
Patch197:       rotate-wacom-pointers.diff
Patch198:       konsole-schema-update.diff
Patch199:       media-cryptosupport.diff
Patch200:       kdm-use-rpmoptflags.diff
Patch203:       show-konqueror-in-menu.diff
Patch204:       fix-desktop-icons.diff
Patch205:       kcmkdm-default-grub.diff
Patch206:       simplify-randr-settings.diff
Patch207:       spellcheck-default-utf8.diff
Patch208:       kdm-audit-log.diff
Patch209:       kwinbindings.diff
Patch211:       konq-combo-editor.diff
Patch212:       minicli-combo-editor.diff
Patch214:       kdm-color-scheme.diff
Patch215:       kdm-consolekit.diff
Patch216:       krandr-0.5.2.1.diff.bz2
Patch217:       kickoff-install-software.diff
Patch218:       kdm-align-userlist-labels.diff
Patch219:       kxkb-include-latin-layout.diff
Patch220:       mediamanager-mount-point-utf8.diff
Patch222:       khelpcenter-delayed-indexcheck.cpp
Patch225:       system-folder_man.diff
Patch227:       arts-start-on-demand.diff
Patch228:       media-teardown_crypto.diff
Patch229:       beagle-0.3.diff
Patch230:       remove-beagle-stuff.diff
Patch231:       kde3-session.diff
Patch232:       kde3-session-restore.diff
Patch233:       uninit.diff
Patch234:       kpamgreeter.diff
Patch235:       use-pam-before-classic.diff
Patch236:       kdesu-remember-keep-password.diff
Patch237:       suspend-kpowersave.diff
Patch238:       knetattach-show.diff
Patch239:       gcc44.diff
Patch240:       bnc584223.diff
Patch241:       openssl1.patch
Patch242:       nsplugin-init-gtk.diff
Patch243:       taskbar.patch
Patch244:       mtab-reenable.patch

%description
This package contains kdebase, one of the basic packages of the K
Desktop Environment. It contains, among others, kwin (the KDE window
manager), Konqueror (the KDE Web browser), and KControl (the
configuration program)

This package is needed if you want to use the KDE Desktop. It is not
needed if you only want to start some KDE applications.



Authors:
--------
    The KDE Team <kde@kde.org>

%package -n misc-console-font
License:        GPLv2+
Group:          System/GUI/KDE
Summary:        A font for terminal usage

%description -n misc-console-font
This package contains the Misc Console font as shipped with KDE.



Authors:
--------
    The KDE Team <kde@kde.org>

%package runtime
License:        GPLv2+
Summary:        Runtime Dependencies of KDE3 Applications
Group:          System/GUI/KDE
Provides:       kio_fish
Obsoletes:      kio_fish
Provides:       kdebase3:/opt/kde3/%_lib/libkonq.so.4

%description runtime
This package contains runtime dependencies of KDE3 applications like
KIO-slaves.



Authors:
--------
    The KDE Team <kde@kde.org>

%package workspace
License:        GPLv2+
Summary:        Workspace Components of KDE3 Desktop
Group:          System/GUI/KDE
Requires:       kdebase3 == %{version}
Provides:       kdebase3:/opt/kde3/bin/kicker
Recommends:     kdebase3-ksysguardd == %{version}
%if 0%{?with_hal} > 0
Recommends:       kdebase3-with-hal-enabled
%endif

%description workspace
This package contains the wrkspace components of kdebase3 like
kdesktop, kicker and kwin.


Authors:
--------
    The KDE Team <kde@kde.org>

%package apps
License:        GPLv2+
Summary:        Major Applications KDE3 Desktop
Group:          System/GUI/KDE
Requires:       kdebase3 == %{version}
Provides:       kdebase3:/opt/kde3/bin/konsole

%description apps
This package contains the major applications kdebase3 like
Kate, Konqueror and KWrite.


Authors:
--------
    The KDE Team <kde@kde.org>

%package devel
License:        GPLv2+
Requires:       kdelibs3-devel kdebase3 = %version kdebase3-apps = %version kdebase3-runtime = %version kdebase3-workspace = %version
Summary:        KDE Base Package: Base, Build Environment
Group:          System/GUI/KDE

%description devel
This package contains KDEbase, one of the basic packages of the K
Desktop Environment. It contains, among other things, KWIN, the KDE
window manager; Konqueror, the KDE web and file browser; and KControl,
the KDE configuration program.

This package is not needed if you do not want to compile high level KDE
applications.



Authors:
--------
    The KDE Team <kde@kde.org>

%package kdm
License:        GPLv2+
# usesubdirs kdm
Summary:        The KDE login and display manager
Provides:       kdebase3:/opt/kde3/bin/kdm
Provides:       kdebase:/opt/kde2/bin/kdm
Provides:       kdebase3-kdm-SLD:/opt/kde3/bin/kdm
Requires:       xorg-x11
Requires:       kdebase3-runtime >= %version
Group:          System/GUI/KDE
PreReq:         %fillup_prereq /bin/grep

%description kdm
This package contains kdm, the login and session manager for KDE.



Authors:
--------
    The KDE Team <kde@kde.org>

%package samba
License:        GPLv2+
# usesubdirs kioslave/smb kcontrol/samba
Summary:        KDE Base package: Windows Connection Module
Group:          System/GUI/KDE

%description samba
This package provides the "smb://" protocol, to connect to and from
Windows and Samba shares.



Authors:
--------
    The KDE Team <kde@kde.org>

%package extra
License:        GPLv2+
# usesubdirs kpersonalizer kcontrol/thememgr
Summary:        KDE Base package: Extra Applications
Group:          System/GUI/KDE

%description extra
This package contains applications which are usually not needed on
SUSE.

- kpersonalizer - sets different settings

- khotkeys aRts support - for voice triggered shortcuts



Authors:
--------
    The KDE Team <kde@kde.org>

%package nsplugin
License:        GPLv2+
%ifarch x86_64 ppc64 s390x ia64
Requires:       nspluginwrapper
%endif
Supplements:    kdebase3 >= %version
Requires:       kdebase3 = %version
Summary:        Netscape plugin support for KDE
Group:          System/GUI/KDE

%description nsplugin
This package contains support for Netscape plug-ins in konqueror. You
have to enable JavaScript for this.



Authors:
--------
    The KDE Team <kde@kde.org>


%package ksysguardd
License:        GPLv2+
PreReq:         %insserv_prereq %fillup_prereq aaa_base
Summary:        KDE base package: ksysguard daemon
Group:          System/GUI/KDE
Provides:       kdebase4-workspace-ksysguardd

%description ksysguardd
This package contains the ksysguard daemon. It is needed for ksysguard.

This package can be installed on servers without any other KDE packages
to guard the system from remote computers.



Authors:
--------
    The KDE Team <kde@kde.org>


%package session
License:        GPLv2+
Summary:        The KDE Session
Group:          System/GUI/KDE
Provides:       kdebase3:/usr/bin/kde
Requires:       kdebase3-workspace

%description session
This package contains the startup scripts necessary to start a KDE
session from kdm.



Authors:
--------
    The KDE Team <kde@kde.org>

%if %suse_version < 1140

%package beagle
License:        GPLv2+
Summary:        Beagle dependent plugins for KDE desktop
Group:          System/GUI/KDE
Requires:       beagle >= 0.3.0
Requires:       kdebase3-workspace = %version
Supplements:    packageand(kdebase3-session:beagle)
BuildRequires:  libbeagle-devel

%description beagle
This package contains kdebase plugins which provide additional search
functionality via Beagle.



Authors:
--------
    The KDE Team <kde@kde.org>

%endif

%package -n fileshareset
License:        GPLv2+
Summary:        Set and list fileshares
Group:          System/Management
Version:        2.0
Release:        578

%description -n fileshareset
This package contains the the fileshareset utility to allow users to
add or remove file shares.  It's also possible to list currently shared
locations. /etc/security/fileshare.conf is the main configuration file.



Authors:
--------
    Uwe Gansert <uwe.gansert at SuSE dot de>

%define sysconfdir /etc

%prep
%setup -q -b 8 -b 13 -n kdebase-%{kde_version}
%patch0
%patch3
%patch5
# causes hangs (bnc#158239)
#%patch6
#%patch100
%patch7
%patch8
%patch10
%patch11
%patch12
%patch14
# do we really still need it ?
#%patch16
%patch15
%patch17
%patch20
%patch21
%patch85
%patch39
%patch40
%patch44
%patch45
%patch46
%patch51
%patch63
%patch60
%patch64
%patch94
%patch98
# all the kdm changes
%patch75
%patch70
%patch71
%patch72
%patch74
%patch76
%patch78
%patch79
# default-to-halt
%patch81
%patch82
%if %suse_version > 1010
%patch83
%patch77
%endif 
%patch200
%patch215
%patch84
%patch61
%patch120
%patch22
%patch92
%patch88
%if %suse_version > 1020
%patch96
%else
%patch996
%endif
# xcursor
%patch99
%ifnarch %ix86 x86_64
%patch80
%endif
%patch62
%patch69
%patch104
%patch105
%patch111
%patch114
%patch116
%patch117
%patch123
%patch126
%patch131
%patch141 -p1
%patch127
%patch144
%patch145
%patch149
%patch155
%patch156
%patch157
%patch160
%if %suse_version > 1010
%patch161
pushd kicker
%patch162
pushd ../kcontrol/kicker
%patch158
popd
popd
%if %suse_version > 1010
%if %suse_version < 1140
%patch159
%endif
%endif
%patch165
%patch166
%patch167
tar xvfj %SOURCE20
%endif
%patch163
%patch125
%patch169
%patch170
%patch171
%patch172
%patch173
%patch174
%patch177
%patch179
%patch180
%if %suse_version > 1010
%patch189
%endif
%patch190
%patch195
%if %suse_version > 1020
%patch198
%patch199
%endif
%patch203
%patch204
%patch205
%patch207
%patch208
%patch209
%patch211
%patch212
%patch214
pushd kcontrol
%patch216
popd
%patch217
%patch218
%patch219
%patch220
%patch222
%patch225
%patch197
%patch206
%patch227
%patch228
%if %suse_version > 1030
%if %suse_version < 1140
pushd kicker
%patch1629
popd
%patch229
%patch230
%endif
%endif
%patch231
%patch232
%patch233
%patch234
%patch235
%patch236
%if %suse_version > 1010
%patch237
%endif
%patch238
%patch239
%patch240 -p1
%patch241 -p0
%patch242 -p0
%patch243
%patch244 -p1

rm -rf kappfinder
rm pics/crystalsvg/cr??-*emacs.png
cp %SOURCE17 l10n/tw/flag.png
. /etc/opt/kde3/common_options
cd ../fileshareset2
aclocal
autoconf
automake -a -c 
cd ../kdebase-%{kde_version}
update_admin

%build
. /etc/opt/kde3/common_options
DEBUG="--disable-debug"
FINAL="--enable-final"
PARANOIA=""
%ifnarch s390
PARANOIA="--with-cdparanoia"
%endif
  LDAP="--with-ldap"
%if %suse_version > 1010
  MOTIF_INCLUDE="/usr/include"
X_SERVER=/usr/bin/X RUN_KAPPFINDER=no \
%else
  MOTIF_INCLUDE="/usr/X11R6/include"
X_SERVER=/usr/X11R6/bin/X RUN_KAPPFINDER=no \
%endif
./configure \
  $configkde \
  $PARANOIA \
  $LDAP \
  $FLAGS \
  $XINERAMA \
%if %suse_version > 1010
  --with-motif-libraries=/usr/%{_lib}/ \
%else
  --with-motif-libraries=/usr/X11R6/%{_lib}/ \
%endif
  --with-motif-includes=$MOTIF_INCLUDE \
  --with-samba-libs \
  --with-pam=xdm \
  --with-kdm-xconsole \
  --with-kdm-pam=xdm \
  --with-kcp-pam=kcheckpass \
  --with-kss-pam=kcheckpass
  do_make %{?_smp_mflags}
cd ../fileshareset2
  ./configure --prefix=%{fileshare_prefix}
  make %{?_smp_mflags}

%install
. /etc/opt/kde3/common_options
# relabel smb icon
grep -v ^Icon= kioslave/smb/smb-network.desktop | grep -v ^Name > w
mv w kioslave/smb/smb-network.desktop
echo "Icon=samba" >> kioslave/smb/smb-network.desktop
echo "Name=SMB Shares" >> kioslave/smb/smb-network.desktop
# install
do_make DESTDIR=$RPM_BUILD_ROOT $INSTALL_TARGET
rm $RPM_BUILD_ROOT/opt/kde3/share/applnk/System/kmenuedit.desktop
rm $RPM_BUILD_ROOT/opt/kde3/share/applnk/System/kpersonalizer.desktop
rm $RPM_BUILD_ROOT/opt/kde3/share/applnk/Utilities/kpager.desktop
rm $RPM_BUILD_ROOT/opt/kde3/share/applnk/Internet/keditbookmarks.desktop
rm $RPM_BUILD_ROOT/opt/kde3/share/applnk/Toys/ktip.desktop
install -m 0644 %SOURCE12 $RPM_BUILD_ROOT/opt/kde3/share/fonts/
%if %suse_version > 1100
install -D -m 0644 %SOURCE21 $RPM_BUILD_ROOT/etc/pam.d/kcheckpass
%else
%if %suse_version > 1010
install -D -m 0644 %SOURCE921 $RPM_BUILD_ROOT/etc/pam.d/kcheckpass
%else
install -D -m 0644 %SOURCE914 $RPM_BUILD_ROOT/etc/pam.d/xdm-np
install -D -m 0644 %SOURCE9921 $RPM_BUILD_ROOT/etc/pam.d/kcheckpass
%endif
%endif
install -m 0644 %SOURCE22 $RPM_BUILD_ROOT/opt/kde3/share/services/searchproviders/
install -m 0644 %SOURCE23 $RPM_BUILD_ROOT/opt/kde3/share/services/searchproviders/
%if %suse_version < 1011
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
%endif
mkdir -p ${RPM_BUILD_ROOT}/usr/bin \
         ${RPM_BUILD_ROOT}/usr/sbin \
         ${RPM_BUILD_ROOT}/var/run/xdmctl
%if %suse_version > 1010
  ln -fs /opt/kde3/bin/startkde $RPM_BUILD_ROOT/usr/bin/kde
  ln -fs /opt/kde3/bin/startkde $RPM_BUILD_ROOT/usr/bin/startkde3
%else
  ln -fs /opt/kde3/bin/startkde $RPM_BUILD_ROOT/usr/X11R6/bin/kde
%endif
ln -sf rcxdm ${RPM_BUILD_ROOT}/usr/sbin/rckdm
#%if %suse_version > 1020
#rm ${RPM_BUILD_ROOT}/opt/kde3/bin/ksysguardd
#rm ${RPM_BUILD_ROOT}/etc/ksysguarddrc
#%else
mv ${RPM_BUILD_ROOT}/opt/kde3/bin/ksysguardd ${RPM_BUILD_ROOT}/usr/bin/ksysguardd
ln -sf /usr/bin/ksysguardd ${RPM_BUILD_ROOT}/opt/kde3/bin/ksysguardd
#%endif
install -d ${RPM_BUILD_ROOT}/opt/kde3/env
%if %suse_version < 1001
install -m 0755 %SOURCE3 ${RPM_BUILD_ROOT}/opt/kde3/env
%endif
install -D -m 0755 %SOURCE16 ${RPM_BUILD_ROOT}/opt/kde3/shutdown/stopkde.suse.sh
mkdir -p "${RPM_BUILD_ROOT}"/etc/security/
echo "RESTRICT=yes" > "${RPM_BUILD_ROOT}"/etc/security/fileshare.conf
#
# install pixmaps and configuration
#
mkdir -p $RPM_BUILD_ROOT/var/adm/fillup-templates
mkdir -p $RPM_BUILD_ROOT/etc/init.d/
install -m 0644 %SOURCE9 ${RPM_BUILD_ROOT}/opt/kde3/share/apps/kdewizard/pics/wizard_small.png
#%if %suse_version < 1031
install -m 0744 %SOURCE6 $RPM_BUILD_ROOT/etc/init.d/ksysguardd
#%endif
mkdir -p $RPM_BUILD_ROOT/opt/kde3/share/apps/kdm/faces/
ln -s ../pics/users/root1.png $RPM_BUILD_ROOT/opt/kde3/share/apps/kdm/faces/root.face.icon
ln -s ../pics/users/default2.png $RPM_BUILD_ROOT/opt/kde3/share/apps/kdm/faces/.default.face.icon
#%if %suse_version < 1031
ln -sf /etc/init.d/ksysguardd  $RPM_BUILD_ROOT/usr/sbin/rcksysguardd
install -D -m 644 %SOURCE15 $RPM_BUILD_ROOT/etc/slp.reg.d/ksysguardd.reg
#%endif
# even if we use smbro
install -D -m 644 kioslave/smb/smb-network.desktop $RPM_BUILD_ROOT/opt/kde3/share/apps/konqueror/dirtree/remote/smb-network.desktop
#
# install kde session file
#
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/xsessions/
mv $RPM_BUILD_ROOT/opt/kde3/share/apps/kdm/sessions/kde.desktop $RPM_BUILD_ROOT/usr/share/xsessions/
# for those we have a package for remove the backup and rely on the package
for wm in gnome xfce4 xfce wmaker blackbox fvwm95 fvwm icewm enlightenment; do
  rm -f $RPM_BUILD_ROOT/opt/kde3/share/apps/kdm/sessions/$wm.desktop
done
%suse_update_desktop_file $RPM_BUILD_ROOT/usr/share/xsessions/kde.desktop
#
# delete unwanted/double files
#
rm $RPM_BUILD_ROOT/opt/kde3/share/apps/kdesktop/DesktopLinks/Home.desktop
rm $RPM_BUILD_ROOT/opt/kde3/share/apps/kdesktop/DesktopLinks/System.desktop
rm $RPM_BUILD_ROOT/opt/kde3/share/icons/*/*/apps/kvirc.*
mkdir -p $RPM_BUILD_ROOT/usr/share
mv $RPM_BUILD_ROOT/opt/kde3/share/wallpapers $RPM_BUILD_ROOT/usr/share
cd ../fileshareset2/src
rm -f $RPM_BUILD_ROOT/opt/kde3/bin/fileshare{set,list}
make DESTDIR=$RPM_BUILD_ROOT install
chmod 0755 $RPM_BUILD_ROOT/%{fileshare_prefix}/bin/fileshareset
cd ..
FILLUP_DIR=$RPM_BUILD_ROOT/var/adm/fillup-templates
install -m 644 -D  %SOURCE4 $FILLUP_DIR/sysconfig.windowmanager-kdebase3
mkdir -p $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/{16x16,22x22,32x32,48x48,64x64,128x128}/apps/
for i in {16,32,48,64,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/mimetypes/misc.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmcomponentchooser.png;done
for i in {16,22,32,48,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/actions/launch.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmperformance.png;done
cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/16x16/actions/services.png $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/16x16/apps/kcmkded.png
for i in {16,22,32,48}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/actions/exit.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmsmserver.png;done
for i in {16,22,32}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/actions/spellcheck.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmspellchecking.png;done
for i in {16,22,32,48,64,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/filesystems/desktop.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmdesktopbehavior.png;done
for i in {16,22,32,48,64,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/filesystems/desktop.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmdesktop.png;done
for i in {16,22,32,48,64,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/apps/kmenu.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmtaskbar.png;done
for i in {16,22,32,48,64,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/mimetypes/colorscm.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmcolors.png;done
for i in {16,22,32,48,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/actions/launch.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmlaunch.png;done
for i in {16,22,32}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/actions/filter.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmkhtml_filter.png;done
for i in {16,22,32}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/actions/run.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmcgi.png;done
for i in {16,22}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/actions/history.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmhistory.png;done
for i in {16,22,32,48,64,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/filesystems/network.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmnetpref.png;done
for i in {16,32,48,64,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/devices/blockdevice.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmkdnssd.png;done
for i in {16,22,32,48,64}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/devices/joystick.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmjoystick.png;done
for i in {16,32,48,64,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/devices/mouse.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmmouse.png;done
for i in {16,22,32,48,64,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/devices/system.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmmedia.png;done
for i in {16,22,32}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/actions/encrypted.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmcrypto.png;done
for i in {16,22,32,48,64,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/filesystems/trashcan_empty.png  $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmprivacy.png;done
for i in {16,22,32,48,64,128}; do cp $BUILD_ROOT/opt/kde3/share/icons/crystalsvg/"$i"x"$i"/filesystems/network.png $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/"$i"x"$i"/apps/kcmnic.png;done
#
# solve file conflicts with theme packages ...
#
mv $RPM_BUILD_ROOT/opt/kde3/share/apps/ksplash/pics $RPM_BUILD_ROOT/opt/kde3/share/apps/ksplash/pics-default
ln -s pics-default $RPM_BUILD_ROOT/opt/kde3/share/apps/ksplash/pics
chmod 0755 $RPM_BUILD_ROOT/%{fileshare_prefix}/bin/fileshareset
%suse_update_desktop_file kate             TextEditor
%suse_update_desktop_file kwrite        TextEditor
%suse_update_desktop_file Help             Documentation Viewer
%suse_update_desktop_file Home             System FileManager core
%suse_update_desktop_file KControl         X-SuSE-core
%suse_update_desktop_file konqbrowser      WebBrowser
%suse_update_desktop_file Kfind            System Filesystem core
%suse_update_desktop_file kinfocenter      System Monitor
%suse_update_desktop_file kmenuedit        Core-Configuration
%suse_update_desktop_file konsole          TerminalEmulator
%suse_update_desktop_file konsolesu        TerminalEmulator
%suse_update_desktop_file ksysguard        System Monitor
%suse_update_desktop_file -r klipper          System TrayIcon
%suse_update_desktop_file kpager           Utility  DesktopUtility
%suse_update_desktop_file -u ktip          System Utility
%suse_update_desktop_file konqfilemgr      System FileManager
%suse_update_desktop_file konquerorsu      System FileManager
%suse_update_desktop_file kdeprintfax      PrintingUtility
%suse_update_desktop_file kjobviewer       PrintingUtility
%suse_update_desktop_file kpersonalizer    DesktopUtility
%suse_update_desktop_file kcmkicker        X-KDE-settings-desktop
%suse_update_desktop_file knetattach       System Network
%suse_update_desktop_file -r kfontview     Graphics Viewer
%suse_update_desktop_file -r krandrtray    Applet X-KDE-settings-desktop
%suse_update_desktop_file $RPM_BUILD_ROOT/opt/kde3/share/apps/remoteview/smb-network.desktop
for i in $RPM_BUILD_ROOT/opt/kde3/share/applnk/System/ScreenSavers/*.desktop ; do
  sed -e '/^\[Desktop Entry\]/a\
Categories=Screensaver;' $i > ${i}_
  mv ${i}_ $i
  %suse_update_desktop_file "$i"
done
install -d $RPM_BUILD_ROOT/opt/kde3/share/applnk/apps
ln -sf /opt/kde3/share/applnk/System/ScreenSavers $RPM_BUILD_ROOT/opt/kde3/share/applnk/apps/ScreenSavers

for i in $RPM_BUILD_ROOT/opt/kde3/share/applications/kde/*.desktop \
	 $RPM_BUILD_ROOT/opt/kde3/share/apps/konqueror/servicemenus/*.desktop \
	 $RPM_BUILD_ROOT/opt/kde3/share/apps/kicker/*/*.desktop \
	 $RPM_BUILD_ROOT/opt/kde3/share/apps/kicker/*/*/*.desktop \
         $RPM_BUILD_ROOT/opt/kde3/share/apps/kicker/*/*/*.desktop \
         $RPM_BUILD_ROOT/usr/share/wallpapers/*.desktop \
	 $RPM_BUILD_ROOT/opt/kde3/share/apps/konqsidebartng/virtual_folders/services/*.desktop; do
  [ "`sed -n '/^\[Desktop Entry\]/,/^\[/ s,NoDisplay=\(.*\),\1,p' "$i"`" = "true" ] && continue
  [ "`sed -n '/^\[Desktop Entry\]/,/^\[/ s,Hidden=\(.*\),\1,p' "$i"`" = "true" ] && continue
  grep -q X-SuSE-translate "$i" && continue
  %suse_update_desktop_file "$i"
done
rm -f $RPM_BUILD_ROOT/opt/kde3/share/config/kdm/README
rm -f $RPM_BUILD_ROOT/opt/kde3/share/apps/kdm/sessions/icewm.desktop
#
# gimp 2.0 does have a different named icon
#
for i in $RPM_BUILD_ROOT//opt/kde3/share/icons/*/*/apps/gimp.png; do
  ln "$i" "${i%/*}/wilber-icon.png"
done
mkdir -p -m 755 $RPM_BUILD_ROOT/%_mandir/man8
cp %SOURCE18 $RPM_BUILD_ROOT/%_mandir/man8
cp %SOURCE19 $RPM_BUILD_ROOT/%_mandir/man8
# don't conflict with man pages from KDE4 packages
rm $RPM_BUILD_ROOT/%_mandir/man1/kate.*
rm $RPM_BUILD_ROOT/%_mandir/man1/kdesu.*
rm $RPM_BUILD_ROOT/%_mandir/man1/kbookmarkmerger.*
rm $RPM_BUILD_ROOT/%_mandir/man1/kfind.*
kde_post_install
%if %suse_version > 1020
%fdupes $RPM_BUILD_ROOT/opt/kde3/share
%endif
# move konqueror.desktop back to old position (#281572)
mv $RPM_BUILD_ROOT/opt/kde3/share/applications/kde/konqueror.desktop $RPM_BUILD_ROOT/opt/kde3/share/applnk/konqueror.desktop

%if 0%{?with_hal} == 0
cp -f %{SOURCE24} $RPM_BUILD_ROOT/opt/kde3/bin
chmod +x $RPM_BUILD_ROOT/opt/kde3/bin/devmon-automounter.sh
sed -i 5i\ '/opt/kde3/bin/devmon-automounter.sh &' $RPM_BUILD_ROOT/opt/kde3/bin/startkde
%endif

%pre
# we have this as link
if test -e opt/kde3/share/apps/ksplash/pics -a ! -L opt/kde3/share/apps/ksplash/pics ;
 then
  if test -e opt/kde3/share/apps/ksplash/pics-default; then
     rm -rf opt/kde3/share/apps/ksplash/pics
  else
     mv opt/kde3/share/apps/ksplash/pics opt/kde3/share/apps/ksplash/pics-default
  fi
fi
kdmrc=/opt/kde3/share/config/kdm/kdmrc
# if the /opt/kde3 one is obviously wrong and we have one in /etc we move that one over to 
# avoid confusion on update what's the right kdmrc
if test -f $kdmrc && grep -q "Session=/opt/kde3/share/config/kdm/Xsession" $kdmrc && test -f /etc$kdmrc; then
   mv /etc$kdmrc $kdmrc
fi

%post
/sbin/ldconfig
%run_permissions

%post kdm
%{fillup_only -an windowmanager-kdebase3}
/opt/kde3/bin/genkdmconf
if test -f /etc/sysconfig/displaymanager ; then
  . /etc/sysconfig/displaymanager
fi
%{fillup_only -n displaymanager -s kdebase3-SuSE}
%{remove_and_set -n displaymanager KDM_SHUTDOWN}
if test -n "$KDM_SHUTDOWN" -a "$KDM_SHUTDOWN" != "no"; then
  if test "$KDM_SHUTDOWN" = "local" ; then
    KDM_SHUTDOWN=all
  fi
  case "$KDM_SHUTDOWN" in
  "auto" | "none" | "root")
    sed -i -e "s/^DISPLAYMANAGER_SHUTDOWN=.*/DISPLAYMANAGER_SHUTDOWN=\"$KDM_SHUTDOWN\"/" /etc/sysconfig/displaymanager
    ;;
  esac
fi

%post -n fileshareset
%run_permissions

%postun kdm
%insserv_cleanup

%postun
%insserv_cleanup
/sbin/ldconfig
%if %suse_version < 1031

%post ksysguardd
%{fillup_and_insserv -sn kdebase3-ksysguardd ksysguardd RUN_KSYSGUARDD}
%verifyscript
%verify_permissions -e /opt/kde3/bin/kcheckpass
%verify_permissions -e /opt/kde3/bin/kdesud
%verify_permissions -e /opt/kde3/bin/khc_indexbuilder

%postun ksysguardd
%restart_on_update ksysguardd
%insserv_cleanup

%preun ksysguardd
%stop_on_removal ksysguardd
%endif

%post runtime -p /sbin/ldconfig

%postun runtime -p /sbin/ldconfig

%post workspace -p /sbin/ldconfig
%if %suse_version > 1110 && 0%{?with_hal} > 0
chkconfig haldaemon on
%endif

%postun workspace -p /sbin/ldconfig

%post apps -p /sbin/ldconfig

%postun apps -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n misc-console-font
%defattr(-,root,root)
%doc COPYING
/opt/kde3/share/fonts/console8x16.pcf.gz

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README README.pam ../lame.spec ../README.mp3
%exclude /opt/kde3/share/fonts/console8x16.pcf.gz
%dir /opt/kde3/share/icons/hicolor/*
%dir /opt/kde3/%_lib/kconf_update_bin
%dir /opt/kde3/share/apps/plugin
%dir /opt/kde3/share/applnk/
%dir /opt/kde3/share/applnk/Settings
%dir /opt/kde3/share/applnk/Settings/WebBrowsing
%dir /opt/kde3/share/applnk/System/ScreenSavers
%dir /opt/kde3/share/applnk/apps
/opt/kde3/share/applnk/apps/ScreenSavers
/etc/xdg/menus/*.menu
/etc/xdg/menus/applications-merged
%verify(not mode) %attr(2755,root,nogroup) /opt/kde3/bin/kdesud
%verify(not mode) %attr(0755,root,man) /opt/kde3/bin/khc_indexbuilder
/opt/kde3/env
/opt/kde3/bin/arts-start
/opt/kde3/bin/drkonqi
/opt/kde3/bin/kaccess
/opt/kde3/bin/kblankscrn.kss
/opt/kde3/bin/kbookmarkmerger
/opt/kde3/bin/kcminit
/opt/kde3/bin/kcminit_startup
/opt/kde3/%_lib/kde3/kcminit_startup.*
/opt/kde3/bin/kcontrol*
/opt/kde3/bin/kdeinstallktheme
/opt/kde3/bin/kdepasswd
/opt/kde3/bin/kdcop
/opt/kde3/bin/kdebugdialog
/opt/kde3/bin/kdeeject
/opt/kde3/bin/kdeprintfax
/opt/kde3/bin/keditfiletype
/opt/kde3/bin/khelpcenter
/opt/kde3/bin/kjobviewer
/opt/kde3/bin/kcheckrunning
/opt/kde3/bin/kpm
/opt/kde3/bin/krandom.kss
/opt/kde3/bin/krdb
/opt/kde3/bin/kxkb
/opt/kde3/bin/kdialog
/opt/kde3/bin/klocaldomainurifilterhelper
/opt/kde3/bin/kio_media_mounthelper
/opt/kde3/bin/knetattach
/opt/kde3/bin/ktrash
/opt/kde3/bin/khc_docbookdig.pl
/opt/kde3/bin/khc_mansearch.pl
/opt/kde3/bin/khc_htdig.pl
/opt/kde3/bin/khc_htsearch.pl
/opt/kde3/bin/kapplymousetheme
/opt/kde3/bin/kio_system_documenthelper
%if %suse_version > 1010
/opt/kde3/bin/runupdater
%endif
/opt/kde3/bin/kstart                      
/opt/kde3/bin/ksystraycmd
/opt/kde3/%_lib/kde3/cursorthumbnail.*
/opt/kde3/%_lib/kde3/htmlthumbnail.*
/opt/kde3/%_lib/kde3/imagethumbnail.*
/opt/kde3/%_lib/kde3/kcm_a*
/opt/kde3/%_lib/kde3/kcm_bell*
/opt/kde3/%_lib/kde3/kcm_keyboard*
/opt/kde3/%_lib/kde3/kcm_c*
/opt/kde3/%_lib/kde3/kcm_d*
/opt/kde3/%_lib/kde3/kcm_e*
/opt/kde3/%_lib/kde3/kcm_f*
/opt/kde3/%_lib/kde3/kcm_h*
/opt/kde3/%_lib/kde3/kcm_i*
/opt/kde3/%_lib/kde3/kcm_l*
/opt/kde3/%_lib/kde3/kcm_nic.*
/opt/kde3/%_lib/kde3/kcm_p*
/opt/kde3/%_lib/kde3/kcm_smserver.*
/opt/kde3/%_lib/kde3/kcm_spellchecking.*
/opt/kde3/%_lib/kde3/kcm_style.*
/opt/kde3/%_lib/kde3/kcm_usb.*
/opt/kde3/%_lib/kde3/khelpcenter.*
/opt/kde3/%_lib/kde3/kcm_xinerama.*
/opt/kde3/%_lib/kde3/kxkb.*
/opt/kde3/%_lib/kde3/djvuthumbnail.*
/opt/kde3/%_lib/kde3/kaccess.*
/opt/kde3/%_lib/kde3/kcminit.*
/opt/kde3/%_lib/kde3/kcm_nsplugins.*
/opt/kde3/%_lib/kde3/kcontrol.*
/opt/kde3/%_lib/kde3/keditbookmarks.*
/opt/kde3/%_lib/kde3/kfmclient.*
/opt/kde3/%_lib/kde3/kjobviewer.*
/opt/kde3/%_lib/kde3/kprinter.*
/opt/kde3/%_lib/kde3/libkdeprint_part.*
/opt/kde3/%_lib/kde3/libkshorturifilter.*
/opt/kde3/%_lib/kde3/libkuri*
/opt/kde3/%_lib/kde3/libkonsolepart.*
/opt/kde3/%_lib/kde3/textthumbnail.*
/opt/kde3/%_lib/kde3/kcm_joystick.*
/opt/kde3/%_lib/kde3/kcm_useraccount.*
/opt/kde3/%_lib/kde3/kcontroledit.*
/opt/kde3/%_lib/kde3/kded_kwrited.*
/opt/kde3/%_lib/kde3/kstyle_keramik_config.*
/opt/kde3/%_lib/kde3/libkmanpart.*
/opt/kde3/%_lib/kde3/liblocaldomainurifilter.*
%if %suse_version > 1010
/opt/kde3/%_lib/kde3/runupdater.*
/opt/kde3/%_lib/libkdeinit_runupdater.so
%endif
/opt/kde3/%_lib/libkdeinit_kaccess.so
/opt/kde3/%_lib/libkdeinit_kcminit.so
/opt/kde3/%_lib/libkdeinit_kcminit_startup.so
/opt/kde3/%_lib/libkdeinit_kcontrol.so
/opt/kde3/%_lib/libkdeinit_kcontroledit.so
/opt/kde3/%_lib/libkdeinit_keditbookmarks.so
/opt/kde3/%_lib/libkdeinit_kfmclient.so
/opt/kde3/%_lib/libkdeinit_khelpcenter.so
/opt/kde3/%_lib/libkdeinit_kjobviewer.so
/opt/kde3/%_lib/libkdeinit_kxkb.so
/opt/kde3/%_lib/kde3/libnsplugin.*
/opt/kde3/%_lib/kde3/kded_remotedirnotify.*
/opt/kde3/%_lib/kde3/kded_systemdirnotify.*
/opt/kde3/%_lib/kde3/libkhtmlkttsdplugin.*
/opt/kde3/%_lib/kde3/kcm_media.la
/opt/kde3/%_lib/kde3/kcm_media.so
/opt/kde3/%_lib/kde3/kded_homedirnotify.la
/opt/kde3/%_lib/kde3/kded_homedirnotify.so
/opt/kde3/%_lib/kde3/kded_medianotifier.la
/opt/kde3/%_lib/kde3/kded_medianotifier.so
%if 0%{?with_hal} > 0
/opt/kde3/%_lib/kde3/media_propsdlgplugin.*
%endif
/opt/kde3/%_lib/kde3/kcm_kded.*
/opt/kde3/%_lib/kde3/kcm_kdnssd.*
/opt/kde3/%_lib/kde3/kcm_keyboard.*
/opt/kde3/%_lib/kde3/kcm_keys.*
/opt/kde3/%_lib/kde3/kcm_kio.*
/opt/kde3/%_lib/kde3/kcm_knotify.*
/opt/kde3/%_lib/kde3/kcm_konq.*
/opt/kde3/%_lib/kde3/kcm_konqhtml.*
/opt/kde3/%_lib/kde3/kcm_kthememanager.*
/opt/kde3/%_lib/kde3/kcm_kurifilt.*
/opt/kde3/share/applications/kde/khtml_filter.desktop
/opt/kde3/share/applications/kde/media.desktop
/opt/kde3/share/applications/kde/joystick.desktop
/opt/kde3/share/applications/kde/kcm_useraccount.desktop
/opt/kde3/share/applications/kde/kdepasswd.desktop
/opt/kde3/share/applications/kde/kthememanager.desktop
/opt/kde3/share/applications/kde/Help.desktop
/opt/kde3/share/applications/kde/KControl.desktop
/opt/kde3/share/applications/kde/arts.desktop
/opt/kde3/share/applications/kde/bell.desktop
/opt/kde3/share/applications/kde/cache.desktop
/opt/kde3/share/applications/kde/colors.desktop
/opt/kde3/share/applications/kde/componentchooser.desktop
/opt/kde3/share/applications/kde/cookies.desktop
/opt/kde3/share/applications/kde/crypto.desktop
/opt/kde3/share/applications/kde/display.desktop
/opt/kde3/share/applications/kde/dma.desktop
/opt/kde3/share/applications/kde/ebrowsing.desktop
/opt/kde3/share/applications/kde/filebrowser.desktop
/opt/kde3/share/applications/kde/filetypes.desktop
/opt/kde3/share/applications/kde/fonts.desktop
/opt/kde3/share/applications/kde/clock.desktop
/opt/kde3/share/applications/kde/icons.desktop
/opt/kde3/share/applications/kde/interrupts.desktop
/opt/kde3/share/applications/kde/installktheme.desktop
/opt/kde3/share/applications/kde/ioports.desktop
/opt/kde3/share/applications/kde/ioslaveinfo.desktop
/opt/kde3/share/applications/kde/kcmaccess.desktop
/opt/kde3/share/applications/kde/kcmcgi.desktop
/opt/kde3/share/applications/kde/kcmcss.desktop
/opt/kde3/share/applications/kde/kcmhistory.desktop
/opt/kde3/share/applications/kde/kcmkded.desktop
/opt/kde3/share/applications/kde/kcmlaunch.desktop
/opt/kde3/share/applications/kde/kcm_kdnssd.desktop
/opt/kde3/share/applications/kde/kcmnotify.desktop
/opt/kde3/share/applications/kde/kcmperformance.desktop
/opt/kde3/share/applications/kde/kcmusb.desktop
/opt/kde3/share/applications/kde/kdeprintfax.desktop
/opt/kde3/share/applications/kde/keyboard.desktop
/opt/kde3/share/applications/kde/keyboard_layout.desktop
/opt/kde3/share/applications/kde/keys.desktop
/opt/kde3/share/applications/kde/kfmclient.desktop
/opt/kde3/share/applications/kde/kfmclient_dir.desktop
/opt/kde3/share/applications/kde/kfmclient_html.desktop
/opt/kde3/share/applications/kde/kfmclient_war.desktop
/opt/kde3/share/applications/kde/khtml_behavior.desktop
/opt/kde3/share/applications/kde/khtml_fonts.desktop
/opt/kde3/share/applications/kde/khtml_java_js.desktop
/opt/kde3/share/applications/kde/khtml_plugins.desktop
/opt/kde3/share/applications/kde/kjobviewer.desktop
/opt/kde3/share/applications/kde/lanbrowser.desktop
/opt/kde3/share/applications/kde/language.desktop
/opt/kde3/share/applications/kde/memory.desktop
/opt/kde3/share/applications/kde/mouse.desktop
/opt/kde3/share/applications/kde/netpref.desktop
/opt/kde3/share/applications/kde/nic.desktop
/opt/kde3/share/applications/kde/partitions.desktop
/opt/kde3/share/applications/kde/pci.desktop
/opt/kde3/share/applications/kde/printers.desktop
/opt/kde3/share/applications/kde/privacy.desktop
/opt/kde3/share/applications/kde/processor.desktop
/opt/kde3/share/applications/kde/proxy.desktop
/opt/kde3/share/applications/kde/scsi.desktop
/opt/kde3/share/applications/kde/smbstatus.desktop
/opt/kde3/share/applications/kde/sound.desktop
/opt/kde3/share/applications/kde/spellchecking.desktop
/opt/kde3/share/applications/kde/style.desktop
/opt/kde3/share/applications/kde/useragent.desktop
/opt/kde3/share/applications/kde/xserver.desktop
/opt/kde3/share/applications/kde/cdinfo.desktop
/opt/kde3/share/applnk/.hidden
/opt/kde3/share/applnk/Settings/Information
/opt/kde3/share/applnk/Settings/LookNFeel
/opt/kde3/share/applnk/Settings/WebBrowsing/khtml_appearance.desktop
/opt/kde3/share/applnk/Settings/WebBrowsing/smb.desktop
/opt/kde3/share/apps/drkonqi
/opt/kde3/share/apps/kc*
/opt/kde3/share/apps/kdcop
/opt/kde3/share/apps/kdeprint*
/opt/kde3/share/apps/kdewizard
/opt/kde3/share/apps/kdisplay
/opt/kde3/share/apps/khelpcenter/searchhandlers/docbook.desktop
/opt/kde3/share/apps/khelpcenter
/opt/kde3/share/apps/kio*
/opt/kde3/share/apps/kjobviewer
/opt/kde3/share/apps/konsole
/opt/kde3/share/apps/khtml/kpartplugins
/opt/kde3/share/apps/kthememanager
/opt/kde3/share/apps/remoteview
/opt/kde3/share/apps/systemview
/opt/kde3/share/apps/kaccess
/opt/kde3/share/config.kcfg/klaunch.kcfg
/opt/kde3/share/config.kcfg/khelpcenter.kcfg
/opt/kde3/share/config.kcfg/keditbookmarks.kcfg
/opt/kde3/share/config.kcfg/launcherapplet.kcfg
/opt/kde3/share/config.kcfg/mediamanagersettings.kcfg
/opt/kde3/share/mimelnk/inode/system_directory.desktop
/opt/kde3/share/services/kded/remotedirnotify.desktop
/opt/kde3/share/services/kded/systemdirnotify.desktop
%if 0%{?with_hal} > 0
/opt/kde3/share/services/media_propsdlgplugin.desktop

%endif
%config(noreplace) /opt/kde3/share/config/kshorturifilterrc
%config(noreplace) /opt/kde3/share/config/kxkb_groups
/opt/kde3/share/desktop-directories
%exclude /opt/kde3/share/doc/HTML/en/kioslave
%dir /opt/kde3/share/fonts
%dir /opt/kde3/share/fonts/override
%verify(not md5 size mtime) /opt/kde3/share/fonts/override/fonts.dir
%dir /opt/kde3/share/icons/*/*/*
/opt/kde3/share/config.kcfg/kcm_useraccount.kcfg
/opt/kde3/share/config.kcfg/kcm_useraccount_pass.kcfg
%exclude /opt/kde3/share/icons/*/*/*/style.*
%exclude /opt/kde3/share/icons/*/*/*/looknfeel.*
%exclude /opt/kde3/share/icons/*/*/*/energy.*
%exclude /opt/kde3/share/icons/*/*/*/date.*
%exclude /opt/kde3/share/icons/*/*/*/filetypes.*
%exclude /opt/kde3/share/icons/*/*/*/personal.*
/opt/kde3/share/icons/*/*/*/a*.*
/opt/kde3/share/icons/*/*/*/b*.*
/opt/kde3/share/icons/*/*/*/c*.*
/opt/kde3/share/icons/*/*/*/d*.*
/opt/kde3/share/icons/*/*/*/f*.*
/opt/kde3/share/icons/*/*/*/g*.*
/opt/kde3/share/icons/*/*/*/help_index.*
/opt/kde3/share/icons/*/*/*/icons.*
/opt/kde3/share/icons/*/*/*/input_devices_settings.*
/opt/kde3/share/icons/*/*/*/kcmx.*
/opt/kde3/share/icons/*/*/*/kcmdf.*
/opt/kde3/share/icons/*/*/*/kbinaryclock.*
/opt/kde3/share/icons/*/*/apps/kcmcgi.*
/opt/kde3/share/icons/*/*/apps/kcmcolors.*
/opt/kde3/share/icons/*/*/apps/kcmcomponentchooser.*
/opt/kde3/share/icons/*/*/apps/kcmcrypto.*
/opt/kde3/share/icons/*/*/apps/kcmhistory.*
/opt/kde3/share/icons/*/*/apps/kcmjoystick.*
/opt/kde3/share/icons/*/*/apps/kcmkded.*
/opt/kde3/share/icons/*/*/apps/kcmkdnssd.*
/opt/kde3/share/icons/*/*/apps/kcmkhtml_filter.*
/opt/kde3/share/icons/*/*/apps/kcmlaunch.*
/opt/kde3/share/icons/*/*/apps/kcmmedia.*
/opt/kde3/share/icons/*/*/apps/kcmmouse.*
/opt/kde3/share/icons/*/*/apps/kcmnetpref.*
/opt/kde3/share/icons/*/*/apps/kcmnic.*
/opt/kde3/share/icons/*/*/apps/kcmperformance.*
/opt/kde3/share/icons/*/*/apps/kcmprivacy.*
/opt/kde3/share/icons/*/*/apps/kcmspellchecking.*
/opt/kde3/share/icons/*/*/*/ieee1394.*
/opt/kde3/share/icons/*/*/*/kdeprintfax.*
/opt/kde3/share/icons/*/*/*/kdisknav.*
/opt/kde3/share/icons/*/*/*/knetattach.*
/opt/kde3/share/icons/*/*/*/key_bindings.*
/opt/kde3/share/icons/*/*/*/keyboard_layout.*
/opt/kde3/share/icons/*/*/*/kfm_home.*
/opt/kde3/share/icons/*/*/*/khelpcenter.*
/opt/kde3/share/icons/*/*/*/kjobviewer.*
/opt/kde3/share/icons/*/*/*/konsole.*
/opt/kde3/share/icons/*/*/*/l*.*
/opt/kde3/share/icons/*/*/*/m*.*
/opt/kde3/share/icons/*/*/*/ne*.*
/opt/kde3/share/icons/*/*/*/opera.*
/opt/kde3/share/icons/*/*/*/r*.*
/opt/kde3/share/icons/*/*/*/s*.*
/opt/kde3/share/icons/*/*/*/usb.*
/opt/kde3/share/icons/*/*/*/vnc.*
/opt/kde3/share/icons/*/*/*/w*.*
/opt/kde3/share/icons/*/*/*/e*.*
/opt/kde3/share/icons/*/*/*/kcmdevices.*
/opt/kde3/share/icons/*/*/*/kcmdrkonqi.*
/opt/kde3/share/icons/*/*/*/kcmmemory.*
/opt/kde3/share/icons/*/*/*/kcmmidi.*
/opt/kde3/share/icons/*/*/*/kcmpartitions.*
/opt/kde3/share/icons/*/*/*/kcmpci.*
/opt/kde3/share/icons/*/*/*/kcmprocessor.*
/opt/kde3/share/icons/*/*/*/kcmscsi.*
/opt/kde3/share/icons/*/*/*/kthememgr.*
/opt/kde3/share/icons/*/*/*/kcontrol.*
/opt/kde3/share/icons/*/*/*/kxkb.*
/opt/kde3/share/icons/*/*/*/p*.*
/opt/kde3/share/icons/*/*/*/t*.*
/opt/kde3/share/icons/*/*/*/qtella.*
/opt/kde3/share/icons/*/*/*/x*.*
# these have no PNG
/opt/kde3/share/icons/*/scalable/apps/hardware.svgz
/opt/kde3/share/icons/*/scalable/apps/kate2.svgz
/opt/kde3/share/icons/*/scalable/apps/kwrite2.svgz
/opt/kde3/share/icons/*/scalable/apps/openoffice.svgz
/opt/kde3/share/icons/*/scalable/apps/quicktime.svgz
/opt/kde3/share/locale
/opt/kde3/share/mimelnk/application/x-konsole.desktop
/opt/kde3/share/mimelnk/application/x-ktheme.desktop
/opt/kde3/share/mimelnk/application/x-smb-server.desktop
/opt/kde3/share/mimelnk/print
/opt/kde3/share/services/textthumbnail.desktop
/opt/kde3/share/services/htmlthumbnail.desktop
/opt/kde3/share/services/ka*.desktop
/opt/kde3/share/services/kdeprint_part.desktop
/opt/kde3/share/services/konsolepart.desktop
/opt/kde3/share/services/konsole-script.desktop
/opt/kde3/share/services/kshorturifilter.desktop
/opt/kde3/share/services/ku*.desktop
/opt/kde3/share/services/searchproviders
/opt/kde3/share/services/useragentstrings
/opt/kde3/share/services/imagethumbnail.desktop
/opt/kde3/share/services/kxkb.desktop
/opt/kde3/share/services/kmanpart.desktop
/opt/kde3/share/services/localdomainurifilter.desktop
/opt/kde3/share/services/kwrited.desktop
/opt/kde3/share/services/djvuthumbnail.desktop
/opt/kde3/share/services/kded/kwrited.desktop
/opt/kde3/share/servicetypes/terminalemulator.desktop
/opt/kde3/share/servicetypes/kateplugin.desktop
/opt/kde3/share/servicetypes/findpart.desktop
/opt/kde3/share/servicetypes/searchprovider.desktop
/opt/kde3/share/servicetypes/thumbcreator.desktop
/opt/kde3/share/servicetypes/uasprovider.desktop
%exclude /opt/kde3/share/sounds/KDE_Close_Window*
%exclude /opt/kde3/share/sounds/KDE_Dialog*
%exclude /opt/kde3/share/sounds/KDE_Desktop*
%exclude /opt/kde3/share/sounds/KDE_Logout*
%exclude /opt/kde3/share/sounds/KDE_Startup*
%exclude /opt/kde3/share/sounds/KDE_Window*
/opt/kde3/share/sounds
/opt/kde3/share/templates
/opt/kde3/share/services/khelpcenter.desktop
/opt/kde3/bin/keditbookmarks
/opt/kde3/bin/kfm*
/opt/kde3/share/apps/kbookmark
/opt/kde3/share/apps/keditbookmarks
/opt/kde3/share/icons/*/*/*/keditbookmarks.*
/opt/kde3/share/icons/*/*/*/kfm.*
/opt/kde3/share/icons/*/*/*/konqueror.*
/opt/kde3/share/services/konq*
/opt/kde3/share/servicetypes/konq*
/opt/kde3/share/services/cursorthumbnail.desktop
/opt/kde3/%_lib/kde3/kcm_randr.*
/opt/kde3/bin/krandrtray
/opt/kde3/share/applications/kde/krandrtray.desktop
/opt/kde3/%_lib/kde3/kded_mediamanager.*
/opt/kde3/%_lib/kde3/kfile_media.*
/opt/kde3/%_lib/kde3/kfile_trash.*
/opt/kde3/share/applications/kde/devices.desktop
/opt/kde3/share/applications/kde/knetattach.desktop
/opt/kde3/share/applications/kde/opengl.desktop
/opt/kde3/share/icons/*/*/*/kcmopengl.*
/opt/kde3/share/mimelnk/media
/opt/kde3/share/services/kded/mediamanager.desktop
/opt/kde3/share/services/kded/homedirnotify.desktop
/opt/kde3/share/services/kded/medianotifier.desktop
/opt/kde3/share/services/kfile_media.desktop
/opt/kde3/share/services/kfile_trash.desktop
/opt/kde3/share/services/kfile_trash_system.desktop
/opt/kde3/share/mimelnk/fonts/package.desktop
/opt/kde3/%_lib/kde3/exrthumbnail.*
/opt/kde3/share/services/exrthumbnail.desktop
%dir /opt/kde3/share/mimelnk/fonts
/opt/kde3/bin/kfontinst
/opt/kde3/%_lib/kde3/fontthumbnail.*
/opt/kde3/%_lib/kde3/kfile_font.*
/opt/kde3/%_lib/kde3/libkfontviewpart.*
%dir /opt/kde3/share/apps/kfontview
/opt/kde3/share/apps/kfontview/kfontviewpart.rc
/opt/kde3/share/applications/kde/kcmfontinst.desktop
/opt/kde3/share/mimelnk/fonts/folder.desktop
/opt/kde3/share/mimelnk/fonts/system-folder.desktop
/opt/kde3/share/services/fontthumbnail.desktop
/opt/kde3/share/services/kfile_font.desktop
/opt/kde3/share/services/kfontviewpart.desktop
%_mandir/man1/*
%if %suse_version < 1001
%config(noreplace) /etc/security/fileshare.conf
/opt/kde3/bin/filesharelist
%verify(not mode) /opt/kde3/bin/fileshareset
%endif
%{_mandir}/man8/kcheckpass.8.gz
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kcontrol
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kdcop
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kdebugdialog
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kdeprint
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kdesu
%exclude /opt/kde3/share/doc/HTML/en/khelpcenter/userguide
%exclude /opt/kde3/share/doc/HTML/en/khelpcenter/visualdict
%doc %lang(en) /opt/kde3/share/doc/HTML/en/khelpcenter
%doc %lang(en) /opt/kde3/share/doc/HTML/en/knetattach
/opt/kde3/share/applications/kde/desktoppath.desktop

%files samba
%defattr(-,root,root)
/opt/kde3/%_lib/kde3/kcm_samba.*
/opt/kde3/%_lib/kde3/kio_smb.*
/opt/kde3/share/services/smb.protocol
%dir /opt/kde3/share/apps/konqueror/dirtree
%dir /opt/kde3/share/apps/konqueror/dirtree/remote
/opt/kde3/share/apps/konqueror/dirtree/remote/smb-network.desktop
/opt/kde3/share/mimelnk/application/x-smb-workgroup.desktop

%files kdm
%defattr(-,root,root)
%dir /opt/kde3/share/doc/kdm
/opt/kde3/bin/genkdmconf
/opt/kde3/bin/kdm*
/opt/kde3/bin/krootimage
/opt/kde3/share/apps/kdm
/opt/kde3/%_lib/kde3/kgreet_pam.*
%doc /opt/kde3/share/doc/kdm/README
%if %suse_version < 1020
%config /etc/pam.d/xdm-np
%endif
%dir /opt/kde3/share/config/kdm
%config(noreplace) /opt/kde3/share/config/kdm/kdmrc
%config(noreplace) /opt/kde3/share/config/kdm/backgroundrc
%if %suse_version < 1010
%config /opt/kde3/share/config/kdm/Xaccess
%config /opt/kde3/share/config/kdm/Xreset
%config /opt/kde3/share/config/kdm/Xresources
%config /opt/kde3/share/config/kdm/Xsession
%config /opt/kde3/share/config/kdm/Xsetup
%config /opt/kde3/share/config/kdm/Xstartup
%config /opt/kde3/share/config/kdm/Xwilling
%endif
%ghost /var/run/xdmctl
/usr/sbin/rckdm
/opt/kde3/share/applications/kde/kdm.desktop
/opt/kde3/share/icons/*/*/*/kdmconfig.*
/opt/kde3/%_lib/kde3/kcm_kdm.*
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kdm

%files session
%defattr(-,root,root)
%if %suse_version > 1010
/usr/bin/kde
/usr/bin/startkde3
%else
/usr/X11R6/bin/kde
%endif
%if %suse_version < 1030
%dir /usr/share/xsessions
%endif
/usr/share/xsessions/kde.desktop

%files extra
%defattr(-,root,root)
/opt/kde3/bin/kpersonalizer
/opt/kde3/share/applications/kde/kpersonalizer.desktop
/opt/kde3/share/apps/kpersonalizer
/opt/kde3/share/icons/*/*/*/kpersonalizer.*
/opt/kde3/bin/kfontview
/opt/kde3/share/applications/kde/kfontview.desktop
/opt/kde3/share/apps/kfontview/kfontviewui.rc
/opt/kde3/%_lib/kde3/khotkeys_arts.*

%files nsplugin
%defattr(-,root,root)
/opt/kde3/bin/nsplugin*
/opt/kde3/share/apps/plugin/nspluginpart.rc
%dir /opt/kde3/share/applnk/Settings/WebBrowsing
/opt/kde3/share/applnk/Settings/WebBrowsing/nsplugin.desktop

%files devel
%defattr(-,root,root)
/opt/kde3/include/*
/opt/kde3/%_lib/libkonq.so
/opt/kde3/%_lib/libkdecorations.so
/opt/kde3/%_lib/libkonqsidebarplugin.so
/opt/kde3/%_lib/libkickermain.so
/opt/kde3/%_lib/libtask*.so
/opt/kde3/%_lib/libksgrd.so
%if %suse_version > 1010
/opt/kde3/%_lib/libkickoffsearch_interfaces.so
/opt/kde3/%_lib/libkickoffsearch_interfaces.la
%endif
/opt/kde3/%_lib/libksplashthemes.so
/opt/kde3/%_lib/libkateinterfaces.so
/opt/kde3/%_lib/libkateutils.so
/opt/kde3/%_lib/libkhotkeys_shared.so
/opt/kde3/%_lib/libkateinterfaces.la
/opt/kde3/%_lib/libkateutils.la
/opt/kde3/%_lib/libkdecorations.la
/opt/kde3/%_lib/libkfontinst.la
/opt/kde3/%_lib/libkfontinst.so
/opt/kde3/%_lib/libkhotkeys_shared.la
/opt/kde3/%_lib/libkickermain.la
/opt/kde3/%_lib/libkonq.la
/opt/kde3/%_lib/libkonqsidebarplugin.la
/opt/kde3/%_lib/libksgrd.la
/opt/kde3/%_lib/libksplashthemes.la
/opt/kde3/%_lib/libtaskbar.la
/opt/kde3/%_lib/libtaskmanager.la
/opt/kde3/%_lib/libkasbar.so
/opt/kde3/%_lib/libkasbar.la

%files ksysguardd
%defattr(-,root,root)
%dir /etc/slp.reg.d
#%if %suse_version < 1020
/usr/bin/ksysguardd
/opt/kde3/bin/ksysguardd
%config(noreplace) /etc/ksysguarddrc
#%endif
#%if %suse_version > 1030
#/usr/bin/ksysguardd
#%config(noreplace) /etc/ksysguarddrc
#%endif
/etc/init.d/ksysguardd
/usr/sbin/rcksysguardd
%config(noreplace) /etc/slp.reg.d/*

%if %suse_version > 1010
%if %suse_version < 1140

%files beagle
%defattr(-,root,root)
/opt/kde3/bin/khc_beagle_search.pl
/opt/kde3/bin/khc_beagle_index.pl
/opt/kde3/share/apps/khelpcenter/searchhandlers/docbook.desktop
/opt/kde3/%_lib/kde3/kickoffsearch_beagle.*
/opt/kde3/share/services/kickoffsearch_beagle.desktop
%endif
%endif

%files -n fileshareset
%defattr(-,root,root)
%config(noreplace) /etc/security/fileshare.conf
%{_bindir}/filesharelist
%verify(not mode) %{_bindir}/fileshareset
%{_mandir}/man8/fileshareset.8.gz

%files apps
%defattr(-,root,root)
/opt/kde3/bin/konsole*
/opt/kde3/%_lib/kde3/konsole.*
/opt/kde3/%_lib/kde3/kcm_konsole.*
/opt/kde3/%_lib/libkdeinit_konsole.so
/opt/kde3/share/applications/kde/konsole.desktop
/opt/kde3/share/applications/kde/konsolesu.desktop
%doc %lang(en) /opt/kde3/share/doc/HTML/en/konsole
/opt/kde3/share/applications/kde/Home.desktop
/opt/kde3/%_lib/libkdeinit_konqueror.so
/opt/kde3/share/apps/konqueror/konq-simplebrowser.rc
/opt/kde3/share/applications/kde/konquerorsu.desktop
/opt/kde3/share/applnk/konqueror.desktop
%doc %lang(en) /opt/kde3/share/doc/HTML/en/konqueror
/opt/kde3/share/config.kcfg/konqueror.kcfg
/opt/kde3/bin/konqueror
/opt/kde3/%_lib/kde3/konq*.so
/opt/kde3/%_lib/kde3/konq*.la
%dir /opt/kde3/share/apps/konqueror
/opt/kde3/share/apps/konqueror/tiles
/opt/kde3/share/apps/konqueror/about
/opt/kde3/share/apps/konqueror/icons
/opt/kde3/share/apps/konqueror/konqueror.rc
/opt/kde3/share/apps/konqueror/p*
/opt/kde3/share/apps/konqueror/servicemenus
/opt/kde3/%_lib/kde3/konqueror.*
/opt/kde3/share/apps/konqiconview
/opt/kde3/share/apps/konqlistview
/opt/kde3/share/apps/konqsidebartng
/opt/kde3/%_lib/kde3/kded_konqy_preloader.*
/opt/kde3/share/services/kded/konqy_preloader.desktop
/opt/kde3/share/applications/kde/konqbrowser.desktop
/opt/kde3/share/applications/kde/konqfilemgr.desktop
/opt/kde3/share/config.kcfg/konq_listview.kcfg
%config(noreplace) /opt/kde3/share/config/konqsidebartng.rc
/opt/kde3/bin/kfind
/opt/kde3/%_lib/kde3/libkfindpart.*
/opt/kde3/share/applications/kde/Kfind.desktop
/opt/kde3/share/apps/kfindpart
/opt/kde3/share/icons/*/*/*/kfind.*
/opt/kde3/share/services/kfindpart.desktop
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kfind
/opt/kde3/bin/kwrite
/opt/kde3/%_lib/kde3/kwrite.*
/opt/kde3/%_lib/libkdeinit_kwrite.so
/opt/kde3/share/applications/kde/kwrite.desktop
/opt/kde3/share/apps/kwrite
/opt/kde3/share/icons/*/*/*/kwrite.*
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kwrite
/opt/kde3/bin/kate
/opt/kde3/%_lib/kde3/kate.*
/opt/kde3/%_lib/libkateinterfaces.so.*
/opt/kde3/%_lib/libkateutils.so.*
/opt/kde3/%_lib/libkdeinit_kate.so
/opt/kde3/share/applications/kde/kate.desktop
/opt/kde3/share/apps/kate
/opt/kde3/share/config/katerc
/opt/kde3/share/icons/*/*/*/kate.*
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kate

%files workspace
%defattr(-,root,root)
%exclude /usr/share/wallpapers/default_blue.*
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kicker
/usr/share/wallpapers
/opt/kde3/bin/startkde
/opt/kde3/bin/kdesktop
/opt/kde3/bin/kdesktop_lock
/opt/kde3/bin/ksmserver
/opt/kde3/%_lib/libkdeinit_ksmserver.so
/opt/kde3/bin/ksplash                     
/opt/kde3/bin/ksplashsimple
/opt/kde3/%_lib/kde3/kdesktop.*
/opt/kde3/share/apps/kdesktop
/opt/kde3/share/config.kcfg/kdesktop.kcfg
%config(noreplace) /opt/kde3/share/config/kdesktop_custom_menu*
/opt/kde3/bin/kicker
/opt/kde3/%_lib/kde3/kicker*
/opt/kde3/%_lib/kde3/kcm_kicker*
/opt/kde3/%_lib/libkickermain.so.*
/opt/kde3/share/applications/kde/kcmkicker.desktop
/opt/kde3/share/apps/kicker
/opt/kde3/share/config.kcfg/kickerSettings.kcfg
/opt/kde3/share/icons/*/*/*/kcmkicker.*
/opt/kde3/share/icons/*/*/*/kicker.*
/opt/kde3/%_lib/kconf_update_bin/kicker-3.4-reverseLayout
/opt/kde3/bin/kwin
/opt/kde3/bin/kwin_killer_helper
/opt/kde3/bin/kwin_rules_dialog
/opt/kde3/%_lib/kde3/kwin_*
/opt/kde3/share/apps/kwin
/opt/kde3/%_lib/kde3/kwin.*
/opt/kde3/%_lib/kde3/kwin3_*
/opt/kde3/%_lib/kconf_update_bin/kwin_update_default_rules
/opt/kde3/%_lib/kconf_update_bin/kwin_update_window_settings
/opt/kde3/share/applications/kde/kwinrules.desktop
/opt/kde3/share/applications/kde/kwindecoration.desktop
/opt/kde3/share/applications/kde/kwinoptions.desktop
/opt/kde3/share/config.kcfg/kwin.kcfg
/opt/kde3/share/icons/*/*/*/kwin.*
/var/adm/fillup-templates/sysconfig.windowmanager-kdebase3
/opt/kde3/share/apps/ksplash
/opt/kde3/share/services/ksplash.desktop
/opt/kde3/share/services/ksplashdefault.desktop
/opt/kde3/share/services/ksplashredmond.desktop
/opt/kde3/share/services/ksplashstandard.desktop
/opt/kde3/share/servicetypes/ksplashplugins.desktop
/opt/kde3/share/icons/*/*/*/ksplash.*
/opt/kde3/%_lib/kde3/ksplash*
/opt/kde3/%_lib/libksplashthemes.so.*
/opt/kde3/share/icons/*/*/apps/kcmsmserver.*
/opt/kde3/share/applications/kde/kcmsmserver.desktop
/opt/kde3/%_lib/kde3/ksmserver.*
/opt/kde3/share/apps/ksmserver
/opt/kde3/%_lib/kde3/clock_panelapplet.*
/opt/kde3/%_lib/kde3/dockbar_panelextension.*
/opt/kde3/%_lib/kde3/kasbar_panelextension.*
/opt/kde3/%_lib/kde3/menu_panelapplet.*
/opt/kde3/%_lib/kde3/klipper_panelapplet.*
/opt/kde3/%_lib/kde3/launcher_panelapplet.*
/opt/kde3/%_lib/kde3/lockout_panelapplet.*
/opt/kde3/%_lib/kde3/minipager_panelapplet.*
/opt/kde3/%_lib/kde3/naughty_panelapplet.*
/opt/kde3/%_lib/kde3/run_panelapplet.*
/opt/kde3/%_lib/kde3/sidebar_panelextension.*
/opt/kde3/share/applications/kde/panel.desktop
/opt/kde3/share/applications/kde/panel_appearance.desktop
/opt/kde3/%_lib/kde3/media_panelapplet.*
/opt/kde3/%_lib/kde3/kcm_taskbar.*
/opt/kde3/share/applications/kde/kcmtaskbar.desktop
/opt/kde3/share/config.kcfg/taskbar.kcfg
/opt/kde3/share/icons/*/*/apps/kcmtaskbar.*
/opt/kde3/%_lib/kde3/kcm_screensaver.*
/opt/kde3/share/applications/kde/screensaver.desktop
/opt/kde3/share/applnk/System/ScreenSavers/KBlankscreen.desktop
/opt/kde3/share/applnk/System/ScreenSavers/KRandom.desktop
/opt/kde3/bin/kwebdesktop
/opt/kde3/share/config.kcfg/kwebdesktop.kcfg
/opt/kde3/share/applications/kde/background.desktop
/opt/kde3/%_lib/kde3/kcm_background*
/opt/kde3/bin/default_desktop_aligning
/opt/kde3/share/applications/kde/desktop.desktop
/opt/kde3/share/applications/kde/desktopbehavior.desktop
/opt/kde3/share/applications/kde/ksplashthememgr.desktop
/opt/kde3/share/icons/*/*/apps/kcmdesktop.*
/opt/kde3/share/icons/*/*/apps/kcmdesktopbehavior.*
/opt/kde3/%_lib/kde3/kcm_ksplashthemes.*
/opt/kde3/%_lib/kde3/kcm_kwindecoration.*
/opt/kde3/%_lib/kde3/kcm_kwinoptions.*
/opt/kde3/%_lib/kde3/kcm_kwinrules.*
%doc %lang(en) /opt/kde3/share/doc/HTML/en/ksplashml
/opt/kde3/shutdown
%if %suse_version > 1010
/opt/kde3/%_lib/libkickoffsearch_interfaces.so.*
/opt/kde3/share/servicetypes/kickoffsearchplugin.desktop
%endif
/opt/kde3/share/autostart/*
/opt/kde3/share/apps/naughtyapplet
/opt/kde3/%_lib/libtask*.so.*
/opt/kde3/bin/extensionproxy
/opt/kde3/bin/appletproxy
/opt/kde3/%_lib/kde3/appletproxy.*
/opt/kde3/%_lib/kde3/extensionproxy.*
/opt/kde3/%_lib/kde3/taskbar*
/opt/kde3/%_lib/kde3/trash_panelapplet*
/opt/kde3/%_lib/kde3/sys*
/opt/kde3/share/apps/clockapplet
/opt/kde3/bin/kasbar
/opt/kde3/%_lib/libkasbar.so.*
/opt/kde3/%_lib/libkdeinit_kicker.so
/opt/kde3/%_lib/libkdeinit_appletproxy.so
/opt/kde3/%_lib/libkdeinit_extensionproxy.so
/opt/kde3/%_lib/libkdeinit_kdesktop.so
/opt/kde3/%_lib/libkdeinit_kwin.so
/opt/kde3/%_lib/libkdeinit_kwin_rules_dialog.so
/opt/kde3/bin/ktip
/opt/kde3/share/appl*/*/ktip.desktop
/opt/kde3/share/icons/*/*/*/ktip.*
/opt/kde3/bin/kpager
/opt/kde3/share/appl*/*/kpager.desktop
/opt/kde3/share/icons/*/*/*/kpager.*
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kpager
/opt/kde3/bin/klipper
/opt/kde3/%_lib/kde3/klipper.*
/opt/kde3/%_lib/libkdeinit_klipper.so
/opt/kde3/share/applications/kde/klipper.desktop
%config(noreplace) /opt/kde3/share/config/klipperrc
/opt/kde3/share/icons/*/*/*/klipper.*
%doc %lang(en) /opt/kde3/share/doc/HTML/en/klipper
/opt/kde3/share/applications/kde/kmenuedit.desktop
/opt/kde3/share/apps/kmenuedit
/opt/kde3/share/icons/*/*/*/kmenuedit.*
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kmenuedit
/opt/kde3/bin/kmenuedit
/opt/kde3/%_lib/kde3/kmenuedit.*
/opt/kde3/%_lib/libkdeinit_kmenuedit.so
/opt/kde3/bin/kinfocenter
/opt/kde3/share/applications/kde/kinfocenter.desktop
/opt/kde3/share/apps/kinfocenter
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kinfocenter
%doc %lang(en) /opt/kde3/share/doc/HTML/en/khelpcenter/userguide
%doc %lang(en) /opt/kde3/share/doc/HTML/en/khelpcenter/visualdict
/opt/kde3/share/sounds/KDE_Close_Window*
/opt/kde3/share/sounds/KDE_Dialog*
/opt/kde3/share/sounds/KDE_Desktop*
/opt/kde3/share/sounds/KDE_Logout*
/opt/kde3/share/sounds/KDE_Startup*
/opt/kde3/share/sounds/KDE_Window*
/opt/kde3/%_lib/libkdeinit_khotkeys.so
/opt/kde3/%_lib/kde3/kcm_khotkeys.*
/opt/kde3/%_lib/kde3/kcm_khotkeys_init.*
/opt/kde3/share/icons/*/*/*/khotkeys.*
/opt/kde3/bin/khotkeys
/opt/kde3/%_lib/kconf_update_bin/khotkeys_update
/opt/kde3/%_lib/kde3/khotkeys.*
/opt/kde3/%_lib/kde3/kded_khotkeys.*
/opt/kde3/%_lib/libkhotkeys_shared.so.*
/opt/kde3/share/applications/kde/khotkeys.desktop
/opt/kde3/share/apps/khotkeys
/opt/kde3/share/services/kded/khotkeys.desktop
/opt/kde3/bin/ksysguard
/opt/kde3/share/applications/kde/ksysguard.desktop
/opt/kde3/share/apps/ksysguard
/opt/kde3/share/icons/*/*/*/ksysguard.*
/opt/kde3/share/mimelnk/application/x-ksysguard.desktop
%doc %lang(en) /opt/kde3/share/doc/HTML/en/ksysguard
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kxkb
/opt/kde3/%_lib/libksgrd.so.*
/opt/kde3/bin/kompmgr
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kompmgr
%if 0%{?with_hal} == 0
/opt/kde3/bin/devmon-automounter.sh
%endif

%files runtime
%defattr(-,root,root)
%doc %lang(en) /opt/kde3/share/doc/HTML/en/kioslave
%exclude /opt/kde3/%_lib/kde3/kio_smb.*
%exclude /opt/kde3/share/services/smb.protocol
/opt/kde3/bin/kde3
/opt/kde3/bin/kreadconfig
/opt/kde3/bin/kwriteconfig
/opt/kde3/bin/kprinter
/opt/kde3/%_lib/libkdeinit_kprinter.so
/opt/kde3/bin/kdesu
/opt/kde3/%_lib/kde3/kio_*
/opt/kde3/%_lib/libkfontinst.so.*
/opt/kde3/share/services/*.protocol
/opt/kde3/%_lib/libkonq.so.*
/opt/kde3/%_lib/libkonqsidebarplugin.so.*
/opt/kde3/%_lib/kde3/kded_favicons.*
/opt/kde3/share/services/kded/favicons.desktop
/opt/kde3/%_lib/libkdecorations.so.*
/opt/kde3/%_lib/kde3/kgreet_winbind.*
/opt/kde3/%_lib/kde3/kgreet_classic.*
%config /etc/pam.d/kcheckpass
%verify(not mode) %attr(4755,root,shadow) /opt/kde3/bin/kcheckpass
/opt/kde3/share/icons/*/*/*/knotify.*
/opt/kde3/share/icons/*/*/*/kscreensaver.*
/opt/kde3/share/icons/*/*/*/style.*
/opt/kde3/share/icons/*/*/*/looknfeel.*
/opt/kde3/share/icons/*/*/*/iconthemes.*
/opt/kde3/share/icons/*/*/*/keyboard.*
/opt/kde3/share/icons/*/*/*/kcmsound.*
/opt/kde3/share/icons/*/*/*/energy.*
/opt/kde3/share/icons/*/*/*/kcmkwm.*
/opt/kde3/share/icons/*/*/*/hwinfo.*
/opt/kde3/share/icons/*/*/*/date.*
/opt/kde3/share/icons/*/*/*/filetypes.*
/opt/kde3/share/icons/*/*/*/kcmsystem.*
/opt/kde3/share/icons/*/*/*/personal.*

%changelog
