# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE specific variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}/trinity
%define tde_libdir %{_libdir}/trinity

# Older RHEL/Fedora versions use packages named "qt", "qt-devel", ..
# whereas newer versions use "qt3", "qt3-devel" ...
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 8
%define _qt_suffix 3
%endif


Name:		tdebase
Version:	r14
Release:	1%{?dist}%{?_variant}
License:	GPL
Summary:	Trinity Base Programs
Group:		User Interface/Desktops

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	tdebase-%{version}.tar.gz

# Wrapper script to prevent Plasma launch at Trinity Startup
Source1:	plasma-desktop

# Pam configuration files for RHEL / Fedora
Source2:	pamd.kdm-trinity%{?dist}
Source3:	pamd.kdm-trinity-np%{?dist}
Source4:	pamd.kcheckpass-trinity%{?dist}
Source5:	pamd.kscreensaver-trinity%{?dist}

# TDE unofficial patches, fixing FTBFS

# TDE for RHEL/Fedora specific patches
## [kdebase/kdesktop] Modifies 'open terminal here' on desktop
Patch11:	kdebase-3.5.12-desktop-openterminalhere.patch
## [kdebase/kioslave] Forces HAL backend to use HAL mount options
Patch12:	kdebase-3.5.12-halmountoptions.patch

# TDE unofficial patches for enhanced features or bugfixes.
## [kdebase/kioslave/man] Fix kio_man for older distros without 'man-db' [Bug #714]
Patch21:	kdebase-3.5.13-kio_man_utf8.patch
## [kdebase/konqueror] Re-enable 'open tab in background' [Bug #245]
Patch22:	kdebase-3.5.13-konq_menu_tab_background.patch
## [kdebase/kicker] Restores the original KDE3 clock [Bug #387]
Patch27:	kdebase-3.5.13-restore_kde3_clock.patch

# Fedora 15 Theme: "Lovelock"
%if 0%{?fedora} == 15
Requires:	lovelock-backgrounds-single
%define tde_bg /usr/share/backgrounds/lovelock/default/standard/lovelock.png

Requires:	fedora-release-notes
%define tde_aboutlabel Fedora 15
%define tde_aboutpage /usr/share/doc/HTML/fedora-release-notes/index.html
%endif

# Fedora 16 Theme: "Verne"
%if 0%{?fedora} == 16
Requires:	verne-backgrounds-single
%define tde_bg /usr/share/backgrounds/verne/default/standard/verne.png

Requires:	fedora-release-notes
%define tde_aboutlabel Fedora 16
%define tde_aboutpage /usr/share/doc/HTML/fedora-release-notes/index.html
%endif

# RHEL 5 Theme
%if 0%{?rhel} == 5
Requires:	desktop-backgrounds-basic
%define tde_bg /usr/share/backgrounds/images/default.jpg

Requires:	indexhtml
%define tde_aboutlabel Enterprise Linux 5
%define tde_aboutpage /usr/share/doc/HTML/index.html
%endif

# RHEL 6 Theme
%if 0%{?rhel} == 6
Requires:	redhat-logos
%define tde_bg /usr/share/backgrounds/default.png

Requires:	redhat-indexhtml
%define tde_aboutlabel Enterprise Linux 6
%define tde_aboutpage /usr/share/doc/HTML/index.html
%endif

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	tdelibs-devel >= %{version}
BuildRequires:	tqt3-devel >= 3.4.0
BuildRequires:	openssl-devel
BuildRequires:	avahi-devel
BuildRequires:	avahi-tqt-devel
BuildRequires:	imake
BuildRequires:	xorg-x11-proto-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-tqt-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	libfontenc-devel
BuildRequires:	hal-devel
BuildRequires:	audiofile-devel
BuildRequires:	alsa-lib-devel
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
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	nas-devel

%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
BuildRequires:	libudev-devel
%endif
 
Requires:	tqtinterface >= %{version}
Requires:	trinity-arts
Requires:	tdelibs >= %{version}
Requires:	tqt3 >= 3.4.0
Requires:	openssl
Requires:	avahi
Requires:	avahi-tqt
Requires:	dbus-tqt
# Provides the global Xsession script (/etc/X11/xinit/Xsession)
Requires:	xorg-x11-xinit


# RHEL 6 Configuration files are provided in separate packages
%if "%{?_prefix}" == "/usr"
Requires:	kde-settings-kdm
%endif
Requires:	redhat-menus

#Provides:	kdebase%{?_qt_suffix} = %{version}
%if "%{?_prefix}" == "/usr"
Provides:		kdebase%{?_qt_suffix} = %{version}
Obsoletes:		kdebase%{?_qt_suffix} <= 3.5.10
%endif


# Required for Fedora LiveCD
Provides:	service(graphical-login)

Obsoletes:		trinity-kdebase <= 3.5.13


%description
Core applications for the Trinity Desktop Environment.  Included are: kdm
(replacement for xdm), twin (window manager), konqueror (filemanager,
web browser, ftp client, ...), konsole (xterm replacement), kpanel
(application starter and desktop pager), kaudio (audio server),
kdehelp (viewer for kde help files, info and man pages), kthememgr
(system for managing alternate theme packages) plus other KDE
components (kcheckpass, kikbd, kscreensaver, kcontrol, kfind,
kfontmanager, kmenuedit).


%package devel
Requires:	%{name}
Requires:	%{name}-libs = %{version}-%{release}
Requires:	tdelibs-devel >= %{version}
Summary:	%{summary} - Development files
%if "%{?_prefix}" == "/usr"
Provides:		kdebase%{?_qt_suffix}-devel = %{version}
Obsoletes:		kdebase%{?_qt_suffix}-devel <= 3.5.10
%endif
Obsoletes:		trinity-kdebase-devel <= 3.5.13

Group:		Development/Libraries
%description devel
Header files for developing applications using %{name}.
Install kdebase-devel if you want to develop or compile Konqueror,
Kate plugins or TWin styles.


%package extras
Summary: Extra applications from %{name}
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
%if "%{?_prefix}" == "/usr"
Provides:	kdebase%{?_qt_suffix}-extras = %{version}
Obsoletes:	kdebase%{?_qt_suffix}-extras <= 3.5.10
%endif
Obsoletes:		trinity-kdebase-extras <= 3.5.13
%description extras
%{summary}, including:
 * kappfinder
 * kpager
 * ktip
 * kpersonalizer


%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: tdelibs >= %{version}
%if "%{?_prefix}" == "/usr"
Provides:	kdebase%{?_qt_suffix}-libs = %{version}
Obsoletes:	kdebase%{?_qt_suffix}-libs <= 3.5.10
%endif
Requires: %{name} = %{version}-%{release}
Obsoletes:		trinity-kdebase-libs <= 3.5.13
%description libs
%{summary}


%package pim-ioslaves
Summary: PIM KIOslaves from %{name}
Group: System Environment/Libraries
%if "%{?_prefix}" == "/usr"
Provides:	kdebase%{?_qt_suffix}-pim-ioslaves = %{version}
Obsoletes:	kdebase%{?_qt_suffix}-pim-ioslaves <= 3.5.10
%endif
Obsoletes:		trinity-kdebase-pim-ioslaves <= 3.5.13
%description pim-ioslaves
Protocol handlers (KIOslaves) for personal information management, including:
 * kio_ldap
 * kio_nntp
 * kio_pop3
 * kio_smtp


%prep
%setup -q -n %{name}

%patch11 -p1
%patch12 -p1

%if 0%{?rhel} > 0
%patch21 -p1
%endif
%patch22 -p1
%patch27 -p0

# Applies an optional distro-specific graphical theme
%if "%{?tde_bg}" != ""
# TDM Background
%__sed -i "tdm/kfrontend/gentdmconf.c" \
	-e 's|"Wallpaper=isadora.png\n"|"Wallpaper=%{tde_bg}\n"|'

# TDE user default background
%__sed -i "kpersonalizer/keyecandypage.cpp" \
	-e 's|#define DEFAULT_WALLPAPER "isadora.png"|#define DEFAULT_WALLPAPER "%{tde_bg}"|'
%__sed -i "starttde" \
	-e 's|/usr/share/wallpapers/isadora.png.desktop|%{tde_bg}|' \
	-e 's|Wallpaper=isadora.png|Wallpaper=%{tde_bg}|'
%endif

# TDE branding: removes KUbuntu references [Bug #617]
%__sed -i "kcontrol/tdm/tdm-appear.cpp" \
	-e "s|Welcome to Kubuntu |Welcome to %{tde_aboutlabel} |"
%__sed -i "konqueror/about/konq_aboutpage.cc" \
	-e "s|About Kubuntu|About %{tde_aboutlabel}|" \
	-e "s|help:/kubuntu/|%{tde_aboutpage}|" \
	-e "s|Kubuntu Documentation|%{tde_aboutlabel} Documentation|"
%__sed -i "konqueror/about/launch.html" \
	-e "s|help:/kubuntu/about-kubuntu/index.html|%{tde_aboutpage}|"
%__sed -i "tdm/config.def" \
	-e "s|Welcome to Trinity |Welcome to %{tde_aboutlabel} |"

# TDE default directory in 'starttde' script (TDEDIR)
%__sed -i "starttde" \
	-e "s|/opt/trinity|%{_prefix}|g"

%build
export PATH="%{_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"
export LD_LIBRARY_PATH="%{_libdir}"

%__mkdir build
cd build
%cmake \
  -DHAVE_REAL_TQT=ON \
  -DHTML_INSTALL_DIR=%{tde_docdir}/HTML \
  -DWITH_SASL=ON \
  -DWITH_LDAP=ON \
  -DWITH_SAMBA=ON \
  -DWITH_OPENEXR=ON \
  -DWITH_XCOMPOSITE=ON \
  -DWITH_XCURSOR=ON \
  -DWITH_XFIXES=ON \
%if 0%{?fedora} || 0%{?rhel} >= 6
  -DWITH_XRANDR=ON \
%else
  -DWITH_XRANDR=OFF \
%endif
  -DWITH_XRENDER=ON \
  -DWITH_XDAMAGE=ON \
  -DWITH_XEXT=ON \
  -DWITH_XTEST=ON \
  -DWITH_LIBUSB=ON \
  -DWITH_LIBRAW1394=ON \
  -DWITH_PAM=ON \
  -DWITH_SHADOW=OFF \
  -DWITH_XDMCP=ON \
  -DWITH_XINERAMA=ON \
  -DWITH_ARTS=ON \
  -DWITH_I8K=OFF \
  -DWITH_HAL=ON \
  -DBUILD_ALL=ON \
  -DKCHECKPASS_PAM_SERVICE="kcheckpass-trinity" \
  -DKDM_PAM_SERVICE="kdm-trinity" \
  -DKSCREENSAVER_PAM_SERVICE="kscreensaver-trinity" \
  ..

%__make %{?_smp_mflags} 

%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

# Adds a GDM/KDM/TDM/XDM session called 'TDE'
%__install -D -m 644 \
	"%{?buildroot}%{_datadir}/apps/tdm/sessions/tde.desktop" \
	"%{?buildroot}%{_usr}/share/xsessions/tde.desktop"

# Renames '/etc/ksysguarddrc' to avoid conflict with KDE4 'ksysguard'
%__mv -f \
	%{?buildroot}%{_sysconfdir}/ksysguarddrc \
	%{?buildroot}%{_sysconfdir}/ksysguarddrc.tde

# TDE 3.5.12: add script "plasma-desktop" to avoid conflict with KDE4
%if "%{?_prefix}" != "/usr"
%__install -m 755 "%{SOURCE1}" "%{?buildroot}%{_bindir}"
%endif

# PAM configuration files
%__install -D -m 644 "%{SOURCE2}" "%{?buildroot}%{_sysconfdir}/pam.d/kdm-trinity"
%__install -D -m 644 "%{SOURCE3}" "%{?buildroot}%{_sysconfdir}/pam.d/kdm-trinity-np"
%__install -D -m 644 "%{SOURCE4}" "%{?buildroot}%{_sysconfdir}/pam.d/kcheckpass-trinity"
%__install -D -m 644 "%{SOURCE5}" "%{?buildroot}%{_sysconfdir}/pam.d/kscreensaver-trinity"

# KDM configuration for RHEL/Fedora
%__sed -i "%{?buildroot}%{_datadir}/config/tdm/tdmrc" \
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
[ -r "%{_sysconfdir}/ksysguarddrc" ] || cp -f "%{_sysconfdir}/ksysguarddrc.tde" "%{_sysconfdir}/ksysguarddrc"

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

%doc AUTHORS COPYING COPYING-DOCS README README.pam
%{tde_docdir}/HTML/en/*
%config(noreplace) %{_sysconfdir}/ksysguarddrc.tde
%{_bindir}/gentdmconf
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
%{_bindir}/tdesu
%attr(0755,root,root) %{_bindir}/tdesud
%{_bindir}/kdialog
%{_bindir}/tdm
%{_bindir}/tdmctl
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
%{_bindir}/twin
%{_bindir}/twin_killer_helper
%{_bindir}/twin_rules_dialog
%{_bindir}/kwrite
%{_bindir}/kwriteconfig
%{_bindir}/kxkb
%{_bindir}/nspluginscan
%{_bindir}/nspluginviewer
%{_bindir}/starttde
%{_bindir}/kcheckrunning
%{_bindir}/kdesktop
%{_bindir}/kdesktop_lock
%{_bindir}/tdm_config
%{_bindir}/tdm_greet
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
%{_bindir}/tdeprintfax
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
%{_libdir}/libtdeinit_*.*
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

# New in TDE 3.5.13
%{_bindir}/krootbacking
%{_bindir}/tsak
%attr(4511,root,root) %{_bindir}/tdmtsak

# New in TDE R14
%{_bindir}/crashtest
%{_bindir}/tdeinit_phase1
%{_bindir}/twin_resumer_helper


%files libs
%defattr(-,root,root,-)
%exclude %{_libdir}/libtdeinit_*.*
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
%dir %{_includedir}/twin
%{_includedir}/twin/*
%dir %{_includedir}/ksgrd
%{_includedir}/ksgrd/*
%dir %{_includedir}/ksplash
%{_includedir}/ksplash/*
%{_libdir}/lib*.so
%exclude %{_libdir}/libtdeinit_*.*
# New in TDE 3.5.13
%{_datadir}/cmake/*.cmake

%changelog
* Sun Mar 04 2012 Francois Andriot <francois.andriot@free.fr> - r14-1
- Initial build for TDE R14, using 'tqt3' instead of 'qt3'
