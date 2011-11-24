# Default version for this component
%if "%{?version}" == ""
%define version 3.5.12
%endif
%define release 12

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_libdir %{_libdir}/kde3

# Older RHEL/Fedora versions use packages named "qt", "qt-devel", ..
# whereas newer versions use "qt3", "qt3-devel" ...
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 8
%define _qt_suffix 3
%endif


Name:		trinity-kdebase
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}
License:	GPL
Summary:	Trinity KDE Base Programs
Group:		User Interface/Desktops

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kdebase-%{version}.tar.gz

# Wrapper script to prevent Plasma launch at Trinity Startup
Source1:	plasma-desktop

# Pam configuration files for RHEL / Fedora
Source2:	pamd.kdm-trinity%{?dist}
Source3:	pamd.kdm-trinity-np%{?dist}
Source4:	pamd.kcheckpass-trinity%{?dist}
Source5:	pamd.kscreensaver-trinity%{?dist}

# TDE Official patches (from SVN), unmodified
# [kdebase/kcontrol] fix for openssl 1.0 
Patch1:		http://www.trinitydesktop.org/patches/r1201523.diff
# [kdebase/kcontrol] make it compatible with openssl < 1.0 
Patch2:		http://www.trinitydesktop.org/patches/r1201705.diff
# Fix My Documents shortcut on desktop
Patch4:		http://www.trinitydesktop.org/patches/r1182808.diff
# [kdebase] fixed an incompatibility with gcc 4.5 
Patch8:		http://www.trinitydesktop.org/patches/r1221326.diff

# TDE Official patches (from SVN), modified
# [kdebase/ksmserver/shutdowndlg.cpp] Fixed invalid constructor per GCC 4.5.2
Patch12:	kdebase-3.5.12-r1220975.patch
# [kdebase] Another invalid constructor per gcc 4.5
Patch9:		kdebase-3.5.12-r1220927.patch

# TDE for RHEL/Fedora specific patches
## [kdebase/kdesu] Remove 'ignore' button on 'kdesu' dialog box
Patch3:		kdebase-3.5.12-kdesu-noignorebutton.patch
## [kdebase/kdesktop] Modifies "open terminal here" on desktop
Patch5:		kdebase-3.5.12-desktop-openterminalhere.patch
## [kdebase/kioslave] Forces HAL backend to use HAL mount options
Patch6:		kdebase-3.5.12-halmountoptions.patch
## [kdebase/kdm/kfrontend] Global Xsession file is '/etc/X11/xinit/Xsession'
Patch7:		kdebase-3.5.13-genkdmconf_Xsession_location.patch
## [kdebase/startkde] Sets default Start Icon in 'kickerrc'
Patch11:	kdebase-3.5.13-startkde_icon.patch

# TDE 3.5.12 patches
# Fix for DBUS include files in RHEL6
Patch0:		kdebase-3.5.12-shutdowndlg-dbus-include.patch
# [kdebase/kcontrol]: disable components that depends of krandr (old distros)
Patch100:	kdebase-3.5.12-disable-krandr.patch


# Fedora 15 Theme: "Lovelock"
%if 0%{?fedora} == 15
Requires:	lovelock-backgrounds-single
%define tde_bg /usr/share/backgrounds/lovelock/default/standard/lovelock.png
%endif

# Fedora 16 Theme: "Verne"
%if 0%{?fedora} == 16
Requires:	verne-backgrounds-single
%define tde_bg /usr/share/backgrounds/verne/default/standard/verne.png
%endif

# RHEL 5 Theme
%if 0%{?rhel} == 5
Requires:	desktop-backgrounds-basic
%define tde_bg /usr/share/backgrounds/images/default.jpg
%endif

# RHEL 6 Theme
%if 0%{?rhel} == 6
Requires:	redhat-logos
%define tde_bg /usr/share/backgrounds/default.png
%endif

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	qt%{?_qt_suffix}-devel
BuildRequires:	openssl-devel
BuildRequires:	avahi-devel avahi-qt3-devel
BuildRequires:	imake
BuildRequires:	xorg-x11-proto-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-qt-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	libfontenc-devel
BuildRequires:	hal-devel
BuildRequires:	audiofile-devel alsa-lib-devel
BuildRequires:	libraw1394-devel
BuildRequires:	openldap-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pam-devel
BuildRequires:	libXdmcp-devel
BuildRequires:	libxkbfile-devel
BuildRequires:	libusb-devel
BuildRequires:	esound-devel
BuildRequires:	glib2-devel
BuildRequires:	libXcomposite-devel
BuildRequires:	libXtst-devel
BuildRequires:	libXdamage-devel
BuildRequires:	xorg-x11-font-utils

# These dependancies are not met in RHEL
%if 0%{?fedora}
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	nas-devel
%endif
 
Requires:	tqtinterface
Requires:	trinity-arts
Requires:	trinity-kdelibs
Requires:	qt%{?_qt_suffix}
Requires:	openssl
Requires:	avahi avahi-qt3
Requires:	dbus-qt
# Provides the global Xsession script (/etc/X11/xinit/Xsession)
Requires:	xorg-x11-xinit


# RHEL 6 Configuration files are provided in separate packages
%if "%{?_prefix}" == "/usr"
Requires:	kde-settings-kdm
%endif
Requires:	redhat-menus

Provides:	kdebase%{?_qt_suffix} = %{version}
%if "%{?_prefix}" == "/usr"
Obsoletes:		kdebase%{?_qt_suffix} <= 3.5.10
%endif


# Required for Fedora LiveCD
Provides:	service(graphical-login)


%description
Core applications for the Trinity K Desktop Environment.  Included are: kdm
(replacement for xdm), kwin (window manager), konqueror (filemanager,
web browser, ftp client, ...), konsole (xterm replacement), kpanel
(application starter and desktop pager), kaudio (audio server),
kdehelp (viewer for kde help files, info and man pages), kthememgr
(system for managing alternate theme packages) plus other KDE
components (kcheckpass, kikbd, kscreensaver, kcontrol, kfind,
kfontmanager, kmenuedit).


%package devel
Requires:	%{name}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	trinity-kdelibs-devel
Summary:	%{summary} - Development files
Provides:	kdebase%{?_qt_suffix}-devel = %{version}
%if "%{?_prefix}" == "/usr"
Obsoletes:		kdebase%{?_qt_suffix}-devel <= 3.5.10
%endif

Group:		Development/Libraries
%description devel
Header files for developing applications using %{name}.
Install kdebase-devel if you want to develop or compile Konqueror,
Kate plugins or KWin styles.


%package extras
Summary: Extra applications from %{name}
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides:	kdebase%{?_qt_suffix}-extras = %{version}
%if "%{?_prefix}" == "/usr"
Obsoletes: kdebase%{?_qt_suffix}-extras <= 3.5.10
%endif
%description extras
%{summary}, including:
 * kappfinder
 * kpager
 * ktip
 * kpersonalizer


%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-kdelibs
Provides:	kdebase%{?_qt_suffix}-libs = %{version}
%if "%{?_prefix}" == "/usr"
Obsoletes: kdebase%{?_qt_suffix}-libs <= 3.5.10
%endif
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}


%package pim-ioslaves
Summary: PIM KIOslaves from %{name}
Group: System Environment/Libraries
Provides:	kdebase%{?_qt_suffix}-pim-ioslaves = %{version}
%if "%{?_prefix}" == "/usr"
Obsoletes: kdebase%{?_qt_suffix}-pim-ioslaves <= 3.5.10
%endif
%description pim-ioslaves
Protocol handlers (KIOslaves) for personal information management, including:
 * kio_ldap
 * kio_nntp
 * kio_pop3
 * kio_smtp


%prep
%setup -q -n kdebase
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch11 -p1
%patch12 -p1
%if 0%{?rhel} && 0%{?rhel} < 6
%patch100 -p1
%endif

# Applies an optional distro-specific graphical theme
%if "%{?tde_bg}" != ""
# KDM Background
%__sed -i "kdm/kfrontend/genkdmconf.c" \
	-e 's,"Wallpaper=isadora.png\n","Wallpaper=%{tde_bg}\n",'
	
# TDE user default background
%__sed -i "kpersonalizer/keyecandypage.cpp" \
	-e 's,#define DEFAULT_WALLPAPER "isadora.png",#define DEFAULT_WALLPAPER "%{tde_bg}",'

%__sed -i "startkde" \
	-e 's,/usr/share/wallpapers/isadora.png.desktop,%{tde_bg},' \
	-e 's,Wallpaper=isadora.png,Wallpaper=%{tde_bg},'
%endif

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"
export IMAKEINCLUDE="-I/usr/share/X11/config"

%configure  \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-dependency-tracking \
  --disable-debug --disable-warnings --enable-final \
  --with-pam=yes \
  --with-kdm-pam=kdm-trinity \
  --with-kcp-pam=kcheckpass-trinity \
  --with-kss-pam=kscreensaver-trinity \
  --with-libraw1394 \
  --with-openexr \
  --with-samba \
  --with-xinerama \
  --with-xscreensaver \
  --without-shadow \
  --enable-closure \
  --with-extra-includes=%{_includedir}/tqt

# Do NOT use %{?_smp_mflags} for this package, or it will fail to build !
%__make

%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot}

# Adds a GDM/KDM/XDM session called 'TDE'
%__install -D -m 644 \
	"%{?buildroot}%{_datadir}/apps/kdm/sessions/kde.desktop" \
	"%{?buildroot}%{_usr}/share/xsessions/tde.desktop"

# Force session name to be 'TDE'
%__sed -i "%{?buildroot}%{_usr}/share/xsessions/tde.desktop" \
	-e "s,^Name=.*,Name=TDE,"

# Modifies 'startkde' to set KDEDIR and KDEHOME hardcoded specific for TDE
%__sed -i "%{?buildroot}%{_bindir}/startkde" \
  -e '/^echo "\[startkde\] Starting startkde.".*/ s,$,\nexport KDEDIR=%{_prefix}\nexport KDEHOME=~/.trinity,'

# Renames '/etc/ksysguarddrc' to avoid conflict with KDE4 'ksysguard'
%__mv -f %{?buildroot}%{_sysconfdir}/ksysguarddrc %{?buildroot}%{_sysconfdir}/ksysguarddrc.tde

# TDE 3.5.12: add script "plasma-desktop" to avoid conflict with KDE4
%if "%{?_prefix}" != "/usr"
%__install -m 755 "%{SOURCE1}" "%{?buildroot}%{_bindir}"
%endif

# PAM configuration files
%__mkdir_p "%{?buildroot}%{_sysconfdir}/pam.d"
%__install -m 644 "%{SOURCE2}" "%{?buildroot}%{_sysconfdir}/pam.d/kdm-trinity"
%__install -m 644 "%{SOURCE3}" "%{?buildroot}%{_sysconfdir}/pam.d/kdm-trinity-np"
%__install -m 644 "%{SOURCE4}" "%{?buildroot}%{_sysconfdir}/pam.d/kcheckpass-trinity"
%__install -m 644 "%{SOURCE5}" "%{?buildroot}%{_sysconfdir}/pam.d/kscreensaver-trinity"

# KDM configuration for RHEL/Fedora
%__sed -i "%{?buildroot}%{_datadir}/config/kdm/kdmrc" \
%if 0%{?fedora} >= 16
	-e "s/^#*MinShowUID=.*/MinShowUID=1000/"
%else
	-e "s/^#*MinShowUID=.*/MinShowUID=500/"
%endif

# Moves the XDG configuration files to TDE directory
%if "%{_prefix}" != "/usr"
%__mkdir_p "%{?buildroot}%{_prefix}/etc"
%__mv -f "%{?buildroot}%{_sysconfdir}/xdg" "%{?buildroot}%{_prefix}/etc"
%endif

%clean
%__rm -rf %{?buildroot}


%post
touch --no-create %{_datadir}/icons/crystalsvg 2> /dev/null || :
gtk-update-icon-cache --quiet %{_datadir}/icons/crystalsvg  2> /dev/null || :
update-desktop-database 2> /dev/null || : 
# Dirty hack to install '/etc/ksysguardrc' alongside with KDE4
[ -r %{_sysconfdir}/ksysguarddrc ] || cp -f %{_sysconfdir}/ksysguarddrc.tde %{_sysconfdir}/ksysguarddrc

%postun
touch --no-create %{_datadir}/icons/crystalsvg 2> /dev/null || :
gtk-update-icon-cache --quiet %{_datadir}/icons/crystalsvg  2> /dev/null || :
update-desktop-database 2> /dev/null || : 


%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post extras
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun extras
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :


%files extras
%defattr(-,root,root,-)
# kappfinder
%{_bindir}/kappfinder
%{_datadir}/applications/kde/kappfinder.desktop
%{_datadir}/applnk/System/kappfinder.desktop
%{_datadir}/apps/kappfinder/
%{_datadir}/icons/hicolor/*/apps/kappfinder.png
# ktip
%{_bindir}/ktip
%{_datadir}/applications/kde/ktip.desktop
%{_datadir}/applnk/Toys/ktip.desktop
%{_datadir}/apps/kdewizard
%{_datadir}/autostart/ktip.desktop
%{_datadir}/icons/hicolor/*/apps/ktip*
# kpersonalizer
%{_bindir}/kpersonalizer
%{_datadir}/applications/kde/kpersonalizer.desktop
%{_datadir}/applnk/System/kpersonalizer.desktop
%{_datadir}/apps/kpersonalizer/
%{_datadir}/icons/crystalsvg/*/apps/kpersonalizer.png
# kpager
%{_bindir}/kpager
%{_datadir}/applications/kde/kpager.desktop
%{_datadir}/applnk/Utilities/kpager.desktop
%{_datadir}/icons/hicolor/*/apps/kpager.png


%files
%defattr(-,root,root,-)
# kappfinder
%exclude %{_datadir}/applications/kde/kappfinder.desktop
%exclude %{_datadir}/applnk/System/kappfinder.desktop
%exclude %{_datadir}/apps/kappfinder/
%exclude %{_datadir}/icons/hicolor/*/apps/kappfinder.png
# ktip
%exclude %{_datadir}/applications/kde/ktip.desktop
%exclude %{_datadir}/applnk/Toys/ktip.desktop
%exclude %{_datadir}/apps/kdewizard
%exclude %{_datadir}/autostart/ktip.desktop
%exclude %{_datadir}/icons/hicolor/*/apps/ktip*
# kpersonalizer
%exclude %{_datadir}/applications/kde/kpersonalizer.desktop
%exclude %{_datadir}/applnk/System/kpersonalizer.desktop
%exclude %{_datadir}/apps/kpersonalizer/
%exclude %{_datadir}/icons/crystalsvg/*/apps/kpersonalizer.png
# kpager
%exclude %{_datadir}/applications/kde/kpager.desktop
%exclude %{_datadir}/applnk/Utilities/kpager.desktop
%exclude %{_datadir}/icons/hicolor/*/apps/kpager.png

# Pam configuration
%{_sysconfdir}/pam.d/*

%doc AUTHORS COPYING README
%{tde_docdir}/HTML/en/*
%config(noreplace) %{_sysconfdir}/ksysguarddrc.tde
%{_bindir}/genkdmconf
%{_bindir}/kaccess
%{_bindir}/kapplymousetheme
%{_bindir}/kate
%{_bindir}/kblankscrn.kss
%{_bindir}/kbookmarkmerger
%{_bindir}/kcminit
%{_bindir}/kcminit_startup
%{_bindir}/kcontrol
%{_bindir}/kcontroledit
%{_bindir}/kdebugdialog
%{_bindir}/kdeinstallktheme
%{_bindir}/kdepasswd
%{_bindir}/kdesu
%attr(0755,root,root) %{_bindir}/kdesud
%{_bindir}/kdialog
%{_bindir}/kdm
%{_bindir}/kdmctl
%{_bindir}/keditbookmarks
%{_bindir}/keditfiletype
%{_bindir}/kfind
%{_bindir}/kfmclient
%{_bindir}/khelpcenter
%{_bindir}/khotkeys
%{_bindir}/kinfocenter
%{_bindir}/klipper
%{_bindir}/kmenuedit
%{_bindir}/konqueror
%{_bindir}/konsole
%{_bindir}/krandom.kss
%{_bindir}/krdb
%{_bindir}/kreadconfig
%{_bindir}/ksmserver
%{_bindir}/ksplashsimple
%{_bindir}/kstart
%{_bindir}/ksysguard
%{_bindir}/ksysguardd
%{_bindir}/ksystraycmd
%{_bindir}/ktrash
%{_bindir}/kwin
%{_bindir}/kwin_killer_helper
%{_bindir}/kwin_rules_dialog
%{_bindir}/kwrite
%{_bindir}/kwriteconfig
%{_bindir}/kxkb
%{_bindir}/nspluginscan
%{_bindir}/nspluginviewer
%{_bindir}/startkde
%{_bindir}/kcheckrunning
%{_bindir}/kdesktop
%{_bindir}/kdesktop_lock
%{_bindir}/kdm_config
%{_bindir}/kdm_greet
%{_bindir}/kfontinst
%{_bindir}/kfontview
%{_bindir}/krootimage
%{_bindir}/kwebdesktop
%{_datadir}/autostart/*
%{_datadir}/desktop-directories/*
%{_datadir}/locale/*/entry.desktop
%{_datadir}/locale/l10n
%{_datadir}/templates/*
%{_datadir}/templates/.source/*
%{_datadir}/wallpapers/*
%{_bindir}/appletproxy
%{_bindir}/drkonqi
%{_bindir}/extensionproxy
%{_bindir}/kasbar
%attr(4755,root,root) %{_bindir}/kcheckpass
%{_bindir}/kdeeject
%{_bindir}/khc_docbookdig.pl
%{_bindir}/khc_htdig.pl
%{_bindir}/khc_htsearch.pl
%{_bindir}/khc_indexbuilder
%{_bindir}/khc_mansearch.pl
%{_bindir}/kicker
%{_bindir}/knetattach
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
%{_bindir}/krandrtray
%endif
%{_bindir}/kompmgr
%{_bindir}/kpm
%{_bindir}/ksplash
%{_libdir}/kconf_update_bin
%{_datadir}/applnk/*.desktop
%{_datadir}/applnk/*/*
%{_datadir}/applnk/.hidden/*
%exclude %{_datadir}/applnk/.hidden/.directory
%{_datadir}/config.kcfg/*
%{_bindir}/kio_media_mounthelper
%{_bindir}/kdcop
%{_bindir}/kdeprintfax
%{_bindir}/khc_beagle_index.pl
%{_bindir}/khc_beagle_search.pl
%{_bindir}/kxdglauncher
%{_bindir}/kjobviewer
%{_bindir}/klocaldomainurifilterhelper
%{_bindir}/kprinter
%{_datadir}/applications/*/*
%{_datadir}/apps/*
%{_datadir}/icons/*color/*/*/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/mimelnk/*/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/sounds/*
%{tde_libdir}/*
%{_libdir}/libkdeinit_*.*
%if "%{_prefix}" != "/usr"
%{_prefix}/etc/xdg/menus/applications-merged/kde-essential.menu
%{_prefix}/etc/xdg/menus/kde-information.menu
%{_prefix}/etc/xdg/menus/kde-screensavers.menu
%{_prefix}/etc/xdg/menus/kde-settings.menu
%else
%{_sysconfdir}/xdg/menus/applications-merged/kde-essential.menu
%{_sysconfdir}/xdg/menus/kde-information.menu
%{_sysconfdir}/xdg/menus/kde-screensavers.menu
%{_sysconfdir}/xdg/menus/kde-settings.menu
%endif
/usr/share/xsessions/*.desktop
# Remove conflicts with redhat-menus
%if "%{?_prefix}" != "/usr"
%{_bindir}/plasma-desktop
%config(noreplace) %{_datadir}/config/*
%else
%exclude %{_datadir}/config
%endif
# exclude pim-ioslaves files from main package
%exclude %{tde_libdir}/kio_ldap.*
%exclude %{tde_libdir}/kio_nntp.*
%exclude %{tde_libdir}/kio_pop3.*
%exclude %{tde_libdir}/kio_smtp.*
%exclude %{_datadir}/services/ldap*.protocol
%exclude %{_datadir}/services/nntp*.protocol
%exclude %{_datadir}/services/pop3*.protocol
%exclude %{_datadir}/services/smtp*.protocol

# TDE 3.5.12 specific
%{_bindir}/kde3
%exclude %{_datadir}/applications/kde/display.desktop
%exclude %{_datadir}/fonts/override/fonts.dir
%{_docdir}/kdm/README

%files libs
%defattr(-,root,root,-)
%exclude %{_libdir}/libkdeinit_*.*
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la

%files pim-ioslaves
%defattr(-,root,root,-)
%{tde_libdir}/kio_ldap.*
%{tde_libdir}/kio_nntp.*
%{tde_libdir}/kio_pop3.*
%{tde_libdir}/kio_smtp.*
%{_datadir}/services/ldap*.protocol
%{_datadir}/services/nntp*.protocol
%{_datadir}/services/pop3*.protocol
%{_datadir}/services/smtp*.protocol

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%dir %{_includedir}/kate
%{_includedir}/kate/*
%dir %{_includedir}/kwin
%{_includedir}/kwin/*
%dir %{_includedir}/ksgrd
%{_includedir}/ksgrd/*
%dir %{_includedir}/ksplash
%{_includedir}/ksplash/*
%{_libdir}/lib*.so
%exclude %{_libdir}/libkdeinit_*.*

%changelog
* Sun Nov 20 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-12
- Updates Kickoff menu Fix [TDE Bugs #281, #508]
- Add distribution-specific start button icon
- Add graphical theme for RHEL 5, RHEL 6, Fedora 15, Fedora 16
- Moves XDG files in TDE prefix to avoid conflict with distro-provided KDE
- Add "service(graphical-login)"
- kdmrc: sets "MinShowUID=500"
- Add missing BuildRequires

* Fri Sep 16 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-11
- Add support for RHEL 5.
- Remove file conflicts with KDE 4.6.5 under Fedora 15

* Mon Sep 12 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-10
- Add "Group" field

* Sun Sep 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-9
- Import to GIT

* Tue Aug 23 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-8
- Add missing BuildRequires
- Add Patch7, Patch8, Patch9 to allow compilation under GCC >= 4.5.2

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-7
- Correct macro to install under "/opt", if desired

* Wed Jul 20 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-6
- Add patch to force halbackend to use HAL-provided mount options

* Wed Jul 20 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-5
- Add patch to modify "Open terminal here" shortcut (now opens in home directory)

* Tue Jul 19 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-4
- Add 'BuildRequires: dbus-qt' to enable HAL support

* Wed Jun 22 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-3
- Adds setuid bit on '/usr/bin/kcheckpass'
- Removes '/usr/share/applications/kde/display.desktop' (does not work on RHEL 6.0)

* Mon Dec 20 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-2
- Add missing Requires
- Rename 'kde3.desktop' to 'kde.desktop' in case of default prefix

* Fri Dec 17 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-1
- Add macro _kde3_prefix to define custom installation prefix (ex: /opt/kde3)
- Add '--with-extra-includes=%{_includedir}/tqt'
- Add 'patch3' to remove ignore button on kdesu dialog box
- Add 'patch4' r1182808.diff : Fix My Documents shortcut on desktop

* Wed Dec 14 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-0
- Initial version
- Add script 'plasma-desktop' to prevent KDE4 plasma automatic startup
- Add 'patch0' to fix for DBUS include files in RHEL6
- Add 'patch1' r1201523.diff : [kdebase/kcontrol] fix for openssl 1.0 
- Add 'patch2' r1201705.diff : [kdebase/kcontrol] make it compatible with openssl < 1.0 

