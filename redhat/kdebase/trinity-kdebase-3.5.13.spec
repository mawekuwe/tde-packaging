# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 18

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}/kde
%define tde_libdir %{_libdir}/trinity

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

# [kdebase] Fix corrupted PNG images [Bug #298]
Source6:	tiles-fixed-png-images.tar.gz

# TDE 3.5.13 patches
## [kdebase/kdm] adds gcrypt support [Bug #624]
Patch7:		kdebase-3.5.13-kdm-crypt.patch
## [kdebase/kioslave/media/mediamanager] FTBFS missing dbus-tqt includes [RHEL/Fedora]
Patch8:		kdebase-3.5.13-mediamanager_ftbfs.patch
## [kdebase/startkde] Hardcoded path '/usr/lib/xxx' in startkde, not suitable for x86_64 [RHEL/Fedora]
Patch9:		kdebase-3.5.13-startkde_ldpreload.patch
## [kdebase/kdesu] Remove 'ignore' button on 'kdesu' dialog box [RHEL/Fedora]
Patch10:	kdebase-3.5.13-kdesu-noignorebutton.patch
## [kdebase/kdesktop] Modifies 'open terminal here' on desktop [RHEL/Fedora]
Patch11:	kdebase-3.5.12-desktop-openterminalhere.patch
## [kdebase/kioslave] Forces HAL backend to use HAL mount options [RHEL/Fedora]
Patch12:	kdebase-3.5.12-halmountoptions.patch
## [kdebase/kdm/kfrontend] Global Xsession file is '/etc/X11/xinit/Xsession' [RHEL/Fedora]
Patch13:	kdebase-3.5.13-genkdmconf_Xsession_location.patch
## [kdebase/kicker/kicker/ui] Fix kickoff menu issues [Bug #508]
Patch14:	kdebase-3.5.13-kickoff_unstable.patch
## [kdebase/startkde] Sets default Start Icon in 'kickerrc' [RHEL/Fedora]
Patch15:	kdebase-3.5.13-startkde_icon.patch
## [kdebase/startkde] Fixes duplicate and incorrect TDE directories location [Bug #741]
Patch16:	kdebase-3.5.13-startkde_directories.patch
## [kdebase/kate] Restores the 'number of files' and sorting widgets to the Kate configuration [Bug #244]
Patch20:	kdebase-3.5.13-kate_mru.patch
## [kdebase/kioslave/man] Fix kio_man for older distros without 'man-db' [Bug #714]
Patch21:	kdebase-3.5.13-kio_man_utf8.patch
## [kdebase/konqueror] Re-enable 'open tab in background' [Bug #245]
Patch22:	kdebase-3.5.13-konq_menu_tab_background.patch
## [kdebase/konqueror/sidebar] Fix error message on documents parent folder [Bug #723]
Patch23:	kdebase-3.5.13-konqsidebar_documents.patch
## [kdebase/konqueror/listview] Konqueror Icon Activation Effect [Bug #335]
Patch24:	kdebase-3.5.13-konq_icon_effect.patch
## [kdebase/kdesu] Restores the "Keep password" check box to the kdesu dialog box [Bug #388]
Patch25:	kdebase-3.5.13-kdesu_showkeeppassword.patch
## [kdebase/kpersonalizer] Repair KPersonalizer settings to match system defaults [Bug #759]
Patch26:	kdebase-3.5.13-kpersonalizer_default_doubleclick.patch
## [kdebase/kicker] Restores the original KDE3 clock [Bug #387]
Patch27:	kdebase-3.5.13-restore_kde3_clock.patch
## [kdebase/kcontrol/randr] Implement X11 event merging in krandrtray [Bug #758]
Patch28:	kdebase-3.5.13-randrtray_merge_x11_reconfig_requests.patch
## [kdebase/kdesktop/lock] Fix multihead screen locking [Bug #669]
Patch29:	kdebase-3.5.13-fix_multihead_desktop_lock.patch
## [kdebase/kdm/kfrontend] Allows to hide KDM menu button [RHEL/Fedora]
Patch30:	kdebase-3.5.12-kdm_hide_menu_button.patch
## [kdebase/kxkb] Enables xtest support
Patch31:	kdebase-3.5.13-enable_xtest_support.patch
## [kdebase/kdm/kfrontend] fix KDM high CPU usage when inactive [Bug #690]
Patch32:	kdebase-3.5.13-fix_kdm_cpu_usage.patch
## [kdebase/tsak] Add keyboard hotplug (add/remove) support to tsak [Bug #587]
Patch33:	kdebase-3.5.13-tsak_keyboard_hotplug.patch
## [kdebase/tsak] Replicate LED status from virtual keyboards to physical keyboards [Bug #561]
Patch34:	kdebase-3.5.13-replicate_led_status_on_virtual_keyboard.patch
## [kdebase/kwin] do not show hostname in titlebar if it's FQDN of localhost [Bug #889]
Patch35:	kdebase-3.5.13-fix_fqdn_in_title.patch
## [kdebase/kicker/applets] Adds option to disable desktop switch on mouse wheel cycling [Bug #908]
Patch36:	kdebase-3.5.13-option_to_disable_scroll_desktop.patch
## [kdebase] Fix Keramik window decoration in KWIN [Bug #905]
Patch37:	kdebase-3.5.13-kwin-keramic-pics-emb.patch
## [kdebase/kdesktop] Fix device icon placement on desktop [Bug #392]
Patch38:	kdebase-3.5.13-fix_device_icon_placement.patch
## [kdebase/kdesktop/lock] Fix security hole in kdesktop_lock
Patch39:	kdebase-3.5.13-fix_kdesktop_lock_security_issue.patch
## [kdebase/kdesktop/lock] Allow minimal managed window interaction inside the lock process [Bug #810]
Patch40:	kdebase-3.5.13-allow_minimal_window_interaction_inside_lock_process.patch
## [kdebase/kwin] Corrects a potential ABI compat problem
Patch41:	kdebase-3.5.13-fix_potential_ABI_compat_problem.patch
## [kdebase] Fix kdebase translations in desktop files - part 2 [Bug #890]
Patch42:	kdebase-3.5.13-fix_translations_in_desktop_files.patch
## [kdebase/kate] Kate: fix focus broken when using the --use parameter [Bug #692]
Patch43:	kdebase-3.5.13-kate_focus_fix.patch
## [kdebase/kicker] Ensures that 'pagersettings.kcfg' is installed [Bug #908, Commit bd9c1479]
Patch44:	kdebase-3.5.13-ensure_pagersettings_is_installed.patch
## [kdebase] Fix "Malformed URL $( kxdglauncher --getpath xdgname DOCUMENTS )" error dialog.
Patch45:	1333232616:f752bcbf6585c61f414963ad83e1300a1da08504.diff
## [kdebase/kioslave] Fix sftp failure on newer systems [Bug #897]
Patch46:	1335166907:e72f4926c094b2bd94501518fbcd2a3e66a74f6a.diff

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
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	qt%{?_qt_suffix}-devel
BuildRequires:	openssl-devel
BuildRequires:	avahi-devel avahi-qt3-devel
BuildRequires:	imake
BuildRequires:	xorg-x11-proto-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-tqt-devel
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
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	nas-devel

%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
BuildRequires:	libudev-devel
%endif
 
Requires:	tqtinterface
Requires:	trinity-arts
Requires:	trinity-kdelibs
Requires:	qt%{?_qt_suffix}
Requires:	openssl
Requires:	avahi avahi-qt3
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
%if "%{?_prefix}" == "/usr"
Provides:		kdebase%{?_qt_suffix}-devel = %{version}
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
%if "%{?_prefix}" == "/usr"
Provides:	kdebase%{?_qt_suffix}-extras = %{version}
Obsoletes:	kdebase%{?_qt_suffix}-extras <= 3.5.10
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
%if "%{?_prefix}" == "/usr"
Provides:	kdebase%{?_qt_suffix}-libs = %{version}
Obsoletes:	kdebase%{?_qt_suffix}-libs <= 3.5.10
%endif
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}


%package pim-ioslaves
Summary: PIM KIOslaves from %{name}
Group: System Environment/Libraries
%if "%{?_prefix}" == "/usr"
Provides:	kdebase%{?_qt_suffix}-pim-ioslaves = %{version}
Obsoletes:	kdebase%{?_qt_suffix}-pim-ioslaves <= 3.5.10
%endif
%description pim-ioslaves
Protocol handlers (KIOslaves) for personal information management, including:
 * kio_ldap
 * kio_nntp
 * kio_pop3
 * kio_smtp


%prep
%setup -q -n kdebase
%__tar xfz %{SOURCE6} -C kicker/data/tiles

%patch7 -p1
%patch8 -p1
%patch9 -p1

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%patch20 -p4
%if 0%{?rhel} > 0
%patch21 -p1
%endif
%patch22 -p1
%patch23 -p1
%patch24 -p4
%patch25 -p1
%patch26 -p1
%patch27 -p0
%patch28 -p0
%patch29 -p0
%patch30 -p1
%patch31 -p1
%patch32 -p1
%if 0%{?fedora} >= 15
%patch33 -p1
%patch34 -p1
%endif
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1

# Applies an optional distro-specific graphical theme
%if "%{?tde_bg}" != ""
# KDM Background
%__sed -i "kdm/kfrontend/genkdmconf.c" \
	-e 's|"Wallpaper=isadora.png\n"|"Wallpaper=%{tde_bg}\n"|'

# TDE user default background
%__sed -i "kpersonalizer/keyecandypage.cpp" \
	-e 's|#define DEFAULT_WALLPAPER "isadora.png"|#define DEFAULT_WALLPAPER "%{tde_bg}"|'
%__sed -i "startkde" \
	-e 's|/usr/share/wallpapers/isadora.png.desktop|%{tde_bg}|' \
	-e 's|Wallpaper=isadora.png|Wallpaper=%{tde_bg}|'
%endif

# TDE branding: removes KUbuntu references [Bug #617]
%__sed -i "kcontrol/kdm/kdm-appear.cpp" \
	-e "s|Welcome to Kubuntu |Welcome to %{tde_aboutlabel} |"
%__sed -i "konqueror/about/konq_aboutpage.cc" \
	-e "s|About Kubuntu|About %{tde_aboutlabel}|" \
	-e "s|help:/kubuntu/|%{tde_aboutpage}|" \
	-e "s|Kubuntu Documentation|%{tde_aboutlabel} Documentation|"
%__sed -i "konqueror/about/launch.html" \
	-e "s|help:/kubuntu/about-kubuntu/index.html|%{tde_aboutpage}|"
%__sed -i "kdm/config.def" \
	-e "s|Welcome to Trinity |Welcome to %{tde_aboutlabel} |"

# TDE default directory in 'startkde' script (KDEDIR)
%__sed -i "startkde" \
	-e "s|/opt/trinity|%{_prefix}|g"

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"
export LD_LIBRARY_PATH="%{_libdir}"

%__mkdir build
cd build
%cmake \
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

# Adds a GDM/KDM/XDM session called 'TDE'
%__install -D -m 644 \
	"%{?buildroot}%{_datadir}/apps/kdm/sessions/tde.desktop" \
	"%{?buildroot}%{_usr}/share/xsessions/tde.desktop"

# Force session name to be 'TDE'
%__sed -i "%{?buildroot}%{_usr}/share/xsessions/tde.desktop" \
	-e "s,^Name=.*,Name=TDE,"

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

# New in TDE 3.5.13
%{_bindir}/krootbacking
%{_bindir}/tsak
%attr(4511,root,root) %{_bindir}/kdmtsak

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
# New in TDE 3.5.13
%{_datadir}/cmake/*.cmake

%changelog
* Mon Apr 23 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-18
- Ensures that 'pagersettings.kcfg' is installed [Bug #908, Commit bd9c1479]
- Fix "Malformed URL $( kxdglauncher --getpath xdgname DOCUMENTS )" error dialog.
- Fix sftp failure on newer systems [Bug #897]

* Sun Apr 01 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-17
- do not show hostname in titlebar if it's FQDN of localhost [Bug #889]
- Adds option to disable desktop switch on mouse wheel cycling [Bug #908]
- Fix Keramik window decoration in KWIN [Bug #905]
- Fix device icon placement on desktop [Bug #392]
- Fix security hole in kdesktop_lock
- Allow minimal managed window interaction inside the lock process [Bug #810]
- Corrects a potential ABI compat problem
- Fix kdebase translations in desktop files - part 2 [Bug #890]
- Kate: fix focus broken when using the --use parameter [Bug #692]
   
* Sat Jan 21 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-16
- Fix KDM high CPU usage when inactive [Bug #690]
- Add keyboard hotplug (add/remove) support to tsak [Bug #587]
- Replicate LED status from virtual keyboards to physical keyboards [Bug #561]

* Thu Jan 05 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-15
- Add a KDM option to hide 'Menu' button on login prompt
- Fix corrupted PNG tiles [Bug #298]
- Adds 'xtest' support

* Mon Jan 02 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-14
- Fix Konqueror Icon Activation Effect [Bug #335]
- Restores the "Keep password" check box to the kdesu dialog box [Bug #388]
- Repair KPersonalizer settings to match system defaults [Bug #759]
- Restores the original KDE3 clock [Bug #387]
- Implement X11 event merging in krandrtray [Bug #758]
- Fix multihead screen locking [Bug #669]

* Mon Dec 12 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-13
- Fix variables (again)

* Sun Dec 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-12
- Fix KDEDIRS and other variables in 'startkde', that messes up translations. [Bug  #741]

* Sat Dec 10 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-11
- Fix error message 'cannot find parent folder' on konqueror sidebar. [Bug #723]

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-10
- Removes Kubuntu branding [Bug #449]
- Re-enables 'open tab in background' konqueror feature [Bug #245]

* Wed Nov 29 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-9
- Fix 'kio_man' on RHEL 5 and RHEL 6 [Bug #714]
- Restores the 'number of files' and sorting widgets to the Kate configuration [Bug #244]

* Fri Nov 18 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-8
- Updates Kickoff menu Fix [Bugs #281, #508]
- Adds KDM gcrypt dependency

* Sun Nov 13 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-7
- Add distribution-specific start button icon

* Sat Nov 12 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-6
- Add graphical theme for RHEL 5, RHEL 6, Fedora 15, Fedora 16
- Moves XDG files in TDE prefix to avoid conflict with distro-provided KDE

* Fri Nov 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-5
- Add "service(graphical-login)"
- Add kickoff menu fix [Bug #508]
- kdmrc: sets "MinShowUID=500"

* Tue Nov 08 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Fix FTBFS with dbus-tqt

* Thu Nov 03 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Add missing BuildRequires

* Tue Nov 01 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Add 'patch8' to fix LD_PRELOAD variable set by 'startkde' under x86_64

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sat Sep 03 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
- Use TDE 3.5.13, cmake, QT3.3.3.8d
