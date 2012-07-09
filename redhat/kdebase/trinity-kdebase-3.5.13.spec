# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
%define tde_appdir %{_datadir}/applications/kde
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity

# Older RHEL/Fedora versions use packages named "qt", "qt-devel", ..
# whereas newer versions use "qt3", "qt3-devel" ...
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 8
%define _qt_suffix 3
%endif


Name:		trinity-tdebase
Version:	3.5.13
Release:	25%{?release}%{?dist}%{?_variant}
License:	GPL
Summary:	Trinity Base Programs
Group:		User Interface/Desktops

Obsoletes:	trinity-kdebase < %{version}-%{release}
Provides:	trinity-kdebase = %{version}-%{release}
Obsoletes:	trinity-kdebase-libs < %{version}-%{release}
Obsoletes:	trinity-kdebase-extras < %{version}-%{release}
Provides:	trinity-kdebase-extras = %{version}-%{release}
Obsoletes:	tdebase < %{version}-%{release}
Provides:	tdebase = %{version}-%{release}


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
## [kdebase/kioslave] Forces HAL backend to use HAL mount options [Bug #986]
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
Patch45:	kdebase-3.5.13-fix_kxdglauncher_document.patch
## [kdebase/kioslave] Fix sftp failure on newer systems [Bug #897]
Patch46:	kdebase-3.5.13-fix_kio_sftp.patch
## [kdebase/kicker] Fix compilation with GCC 4.7 [Bug #958]
Patch47:	kdebase-3.5.13-kicker-easyvector.patch
## [kdebase/kioslave] Fix sftp when nonstandard port is specified in ssh config [Bug #897]
Patch48:	kdebase-3.5.13-fix_kio_sftp_nonstandard_ports.patch
## [kdebase/kdm] Start minimal dcop system to support twin in tdm [Commit #66a19439]
Patch49:	kdebase-3.5.13-start_dcop_in_tdm.patch
## [kdebase/kdesktop/lock] Update lock process to engage the lock in near real time [Commit #8d521d0b]
Patch50:	kdebase-3.5.13-engage_lock_in_near_real_time.patch
## [kdebase/kdesktop/lock] Commit the rest of 8d521d0b, not merged due to GIT glitch [Commit #49526413]
Patch51:	kdebase-3.5.13-engage_lock_in_near_real_time_continued.patch
## [kdebase/kdesktop/lock] Fix desktop lock failure due to race condition within signal handler between qt and xcb [Commit #67a3a8f3]
Patch52:	kdebase-3.5.13-fix_lock_failure.patch
## [kdebase/kioslave] Temporary fix for a probable race condition on some systems. [Bug #760] [Commit #d41f5217]
Patch53:	kdebase-3.5.13-fix_race_condition.patch
## [kdebase] Adds USB default mount options in control panel [Bug #986]
Patch54:	kdebase-3.5.13-add_usbstorage_panel.patch
## [tdebase] Add the ability to reorder documents in kate [Commit #46a657f7]
Patch55:	kdebase-3.5.13-add_reorder_documents_in_kate.patch
## [tdebase] Add drag and drop to kate file list in manual mode [Commit #b0fa10df]
Patch56:	kdebase-3.5.13-add_drag_drop_to_kate_file_list.patch
## [tdebase] Disable keyboard shortcuts for file location moving, as they did not work properly 
##  and have very little practical use [Commit #9a948c1a]
Patch57:	kdebase-3.5.13-disable_keyboard_shortcuts_for_file_location_moving.patch
## [tdebase] Fix KHTML smooth scrolling control center option [Bug #1001] [Commit #b45b4bd7]
Patch58:	kdebase-3.5.13-fix_khtml_smooth_scrolling.patch
## [tdebase] Fix fancy logout not allowing interaction with save dialogs [Bug #922]
##   Fix desktop wallpaper export failing when triggered by krootbacking or ksmserver and konsole or kdesktop_lock not previously loaded [Commit #d2f8fca9]
Patch59:	kdebase-3.5.13-fix_fancy_logout.patch
## [tdebase] Update default konqueror maximum image preview size to 10MB. [Commit #03e19305]
Patch60:	kdebase-3.5.13-update_default_konq_max_image_prev_size.patch
## [tdebase] Fix menu crash with disabled search field [Bug #1081] [Commit #0afb2d8a]
Patch61:	kdebase-3.5.13-fix_menu_crash_with_disabled_search.patch

### FEDORA / RHEL distribution-specific settings ###

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

# Fedora 17 Theme: "Beefy Miracle"
%if 0%{?fedora} == 17
Requires:	beefy-miracle-backgrounds-single
%define tde_bg /usr/share/backgrounds/beefy-miracle/default/standard/beefy-miracle.png

Requires:	fedora-release-notes
%define tde_aboutlabel Fedora 17
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


BuildRequires:	cmake >= 2.8
BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	gcc-c++ make
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
BuildRequires:	pcre-devel

%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
BuildRequires:	libudev-devel
%endif

%if 0%{?fedora} >= 17
BuildRequires:	perl-Digest-MD5
%endif

# tdebase is a metapackage that installs all sub-packages
Requires: %{name}-runtime-data-common = %{version}-%{release}
Requires: %{name}-data = %{version}-%{release}
Requires: %{name}-bin = %{version}-%{release}
Requires: %{name}-kio-plugins = %{version}-%{release}
Requires: %{name}-kio-pim-plugins = %{version}-%{release}
Requires: trinity-kappfinder = %{version}-%{release}
Requires: trinity-kate = %{version}-%{release}
Requires: trinity-kwrite = %{version}-%{release}
Requires: trinity-kcontrol = %{version}-%{release}
Requires: trinity-kdepasswd = %{version}-%{release}
Requires: trinity-tdeprint = %{version}-%{release}
Requires: trinity-kdesktop = %{version}-%{release}
Requires: trinity-tdm = %{version}-%{release}
Requires: trinity-kfind = %{version}-%{release}
Requires: trinity-khelpcenter = %{version}-%{release}
Requires: trinity-kicker = %{version}-%{release}
Requires: trinity-klipper = %{version}-%{release}
Requires: trinity-kmenuedit = %{version}-%{release}
Requires: trinity-konqueror = %{version}-%{release}
Requires: trinity-konqueror-nsplugins = %{version}-%{release}
Requires: trinity-konsole = %{version}-%{release}
Requires: trinity-kpager = %{version}-%{release}
Requires: trinity-kpersonalizer = %{version}-%{release}
Requires: trinity-ksmserver = %{version}-%{release}
Requires: trinity-ksplash = %{version}-%{release}
Requires: trinity-ksysguard = %{version}-%{release}
Requires: trinity-ksysguardd = %{version}-%{release}
Requires: trinity-ktip = %{version}-%{release}
Requires: trinity-twin = %{version}-%{release}
Requires: trinity-libkonq = %{version}-%{release}
Requires: %{name}-libtqt3-integration = %{version}-%{release}
 
Requires:	tqtinterface
Requires:	trinity-arts
Requires:	trinity-kdelibs
Requires:	qt%{?_qt_suffix}
Requires:	openssl
Requires:	avahi avahi-qt3
Requires:	dbus-tqt

# RHEL 6 Configuration files are provided in separate packages
%if "%{?_prefix}" == "/usr"
Requires:	kde-settings-kdm
%endif
Requires:	redhat-menus


%description
TDE (the Trinity Desktop Environment) is a powerful Open Source graphical
desktop environment for Unix workstations. It combines ease of use,
contemporary functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

This metapackage includes the nucleus of TDE, namely the minimal package
set necessary to run TDE as a desktop environment. This includes the
window manager, taskbar, control center, a text editor, file manager,
web browser, X terminal emulator, and many other programs and components.


##########

%package devel
Summary:	%{summary} - Development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	trinity-kdelibs-devel

Requires:	%{name}-bin-devel = %{version}-%{release}
Requires:	trinity-kate-devel = %{version}-%{release}
Requires:	trinity-kcontrol-devel = %{version}-%{release}
Requires:	trinity-kdesktop-devel = %{version}-%{release}
Requires:	trinity-kicker-devel = %{version}-%{release}
Requires:	trinity-konqueror-devel = %{version}-%{release}
Requires:	trinity-ksplash-devel = %{version}-%{release}
Requires:	trinity-ksysguard-devel = %{version}-%{release}
Requires:	trinity-libkonq-devel = %{version}-%{release}
Requires:	trinity-tdm-devel = %{version}-%{release}
Requires:	trinity-twin-devel = %{version}-%{release}

Provides:	trinity-kdebase-devel = %{version}-%{release}
Obsoletes:	trinity-kdebase-devel < %{version}-%{release}
Provides:	tdebase-devel = %{version}-%{release}
Obsoletes:	tdebase-devel < %{version}-%{release}

Obsoletes:	trinity-kdebase-cmake < %{version}-%{release}
Obsoletes:	tdebase-cmake < %{version}-%{release}

%description devel
This is a meta-package that installs all tdebase development packages.

Header files for developing applications using %{name}.
Install tdebase-devel if you want to develop or compile Konqueror,
Kate plugins or KWin styles.

%files devel
%{_datadir}/cmake/*.cmake

##########

%package kio-pim-plugins
Summary:	PIM KIOslaves from %{name}
Group:		Environment/Libraries

Provides:	trinity-kdebase-pim-ioslaves = %{version}-%{release}
Obsoletes:	trinity-kdebase-pim-ioslaves < %{version}-%{release}
Provides:	tdebase-kio-pim-plugins = %{version}-%{release}
Obsoletes:	tdebase-kio-pim-plugins < %{version}-%{release}

%description kio-pim-plugins
Protocol handlers (KIOslaves) for personal information management, including:
 * kio_ldap
 * kio_nntp
 * kio_pop3
 * kio_smtp

%files kio-pim-plugins
%defattr(-,root,root,-)
%{tde_libdir}/kio_ldap.la
%{tde_libdir}/kio_ldap.so
%{tde_libdir}/kio_nntp.la
%{tde_libdir}/kio_nntp.so
%{tde_libdir}/kio_pop3.la
%{tde_libdir}/kio_pop3.so
%{tde_libdir}/kio_smtp.la
%{tde_libdir}/kio_smtp.so
%{_datadir}/services/ldap.protocol
%{_datadir}/services/ldaps.protocol
%{_datadir}/services/nntp.protocol
%{_datadir}/services/nntps.protocol
%{_datadir}/services/pop3.protocol
%{_datadir}/services/pop3s.protocol
%{_datadir}/services/smtp.protocol
%{_datadir}/services/smtps.protocol

##########

%package runtime-data-common
Summary:	Shared common files for Trinity and KDE4
Group:		Environment/Libraries

Provides:	tdebase-runtime-data-common = %{version}-%{release}
Obsoletes:	tdebase-runtime-data-common < %{version}-%{release}

%description runtime-data-common
Shared common files for both Trinity and KDE4
Such as the desktop right-click-"Create New" list

%files runtime-data-common
%defattr(-,root,root,-)
%{_datadir}/autostart/khotkeys.desktop
%{_datadir}/desktop-directories/*
%{_datadir}/icons/hicolor/*/apps/kxkb.png
%{_datadir}/icons/hicolor/*/apps/knetattach.*
%{_datadir}/icons/hicolor/*/apps/khotkeys.png
%{_datadir}/icons/hicolor/*/apps/kmenuedit.png
%{_datadir}/icons/hicolor/*/apps/ksplash.png
%{_datadir}/locale/en_US/entry.desktop
%{_datadir}/locale/l10n/*.desktop
%{_datadir}/locale/l10n/*/entry.desktop
%{_datadir}/locale/l10n/*/flag.png
%{_datadir}/sounds/pop.wav
%{_datadir}/templates

%post runtime-data-common
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

%postun runtime-data-common
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-kappfinder
Summary:	non-KDE application finder for KDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-kappfinder
kappfinder searches your workstation for many common applications and
creates menu entries for them.

%files -n trinity-kappfinder
%defattr(-,root,root,-)
%{_bindir}/kappfinder
%{tde_appdir}/kappfinder.desktop
%{_datadir}/applnk/System/kappfinder.desktop
%{_datadir}/apps/kappfinder
%{_datadir}/icons/hicolor/*/apps/kappfinder.png

%post -n trinity-kappfinder
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun -n trinity-kappfinder
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database %{tde_appdir} 2> /dev/null || : 

##########

%package -n trinity-libkateinterfaces
Summary:	Common libraries used by kwrite and kate
Group:		Environment/Libraries

%description -n trinity-libkateinterfaces
%{summary}

%files -n trinity-libkateinterfaces
%{_libdir}/libkateinterfaces.so.*

##########

%package -n trinity-kate
Summary:	advanced text editor for TDE
Group:		Applications/Text
Requires:	%{name}-data = %{version}-%{release}
Requires:	trinity-kwrite = %{version}-%{release}
Requires:	trinity-libkateinterfaces = %{version}-%{release}

%description -n trinity-kate
Kate is a multi document editor, based on a rewritten version of the kwrite
editing widget of TDE.

It is a multi-view editor that lets you view several instances of the same
document with all instances being synced, or view more files at the same
time for easy reference or simultaneous editing. The terminal emulation
and sidebar are docked windows that can be plugged out of the main window,
or replaced therein according to your preference.

Some random features:
* Editing of big files
* Extensible syntax highlighting
* Folding
* Dynamic word wrap
* Selectable encoding
* Filter command
* Global grep dialog

%files -n trinity-kate
%defattr(-,root,root,-)
%{_bindir}/kate
%{tde_libdir}/kate.la
%{tde_libdir}/kate.so
%{_libdir}/libkateutils.so.*
%{_libdir}/lib[kt]deinit_kate.la
%{_libdir}/lib[kt]deinit_kate.so
%{tde_appdir}/kate.desktop
%{_datadir}/apps/kate/
%{_datadir}/apps/kconf_update/kate-2.4.upd
%{_datadir}/config/katerc
%{_datadir}/icons/hicolor/*/apps/kate.png
%{_datadir}/icons/hicolor/*/apps/kate2.svgz
%{_datadir}/servicetypes/kateplugin.desktop
%{tde_docdir}/HTML/en/kate/

%post -n trinity-kate
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database %{tde_appdir} 2> /dev/null || : 
/sbin/ldconfig || :

%postun -n trinity-kate
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database %{tde_appdir} 2> /dev/null || : 
/sbin/ldconfig || :

##########

%package -n trinity-kate-devel
Summary:	Development files for kate
Group:		Development/Libraries
Requires:	trinity-kate = %{version}-%{release}

%description -n trinity-kate-devel
%{summary}

%files -n trinity-kate-devel
%{_includedir}/kate/
%{_libdir}/libkateutils.so
%{_libdir}/libkateutils.la
%{_libdir}/libkateinterfaces.so
%{_libdir}/libkateinterfaces.la

%post -n trinity-kate-devel
/sbin/ldconfig || :

%postun -n trinity-kate-devel
/sbin/ldconfig || :

##########

%package -n trinity-kwrite
Summary:	advanced text editor for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}
Requires:	trinity-libkateinterfaces = %{version}-%{release}

%description -n trinity-kwrite
Kwrite is a text editor for TDE.

%files -n trinity-kwrite
%defattr(-,root,root,-)
%{_bindir}/kwrite
%{tde_libdir}/kwrite.la
%{tde_libdir}/kwrite.so
%{_libdir}/lib[kt]deinit_kwrite.la
%{_libdir}/lib[kt]deinit_kwrite.so
%{tde_appdir}/kwrite.desktop
%{_datadir}/apps/kwrite/kwriteui.rc
%{_datadir}/icons/hicolor/*/apps/kwrite.png
%{_datadir}/icons/hicolor/*/apps/kwrite2.svgz
%{tde_docdir}/HTML/en/kwrite/


%post -n trinity-kwrite
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun -n trinity-kwrite
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database %{tde_appdir} 2> /dev/null || : 

##########

%package -n trinity-kcontrol
Summary:	control center for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}
Requires:	hwdata
Requires:	usbutils

%description -n trinity-kcontrol
The TDE Control Center provides you with a centralized and convenient
way to configure all of your TDE settings.

It is made up of multiple modules. Each module is a separate application,
but the control center organizes all of these programs into a convenient
location.

In combination with udev KControl supports the advanced
configuration of Logitech mice, though the user must be a member of the
plugdev group.

%files -n trinity-kcontrol
%defattr(-,root,root,-)
%{_bindir}/kaccess
%{_bindir}/kcontrol
%{_bindir}/kdeinstallktheme
%{_bindir}/keditfiletype
%{_bindir}/kfontinst
%{_bindir}/kfontview
%{_bindir}/kinfocenter
%{_bindir}/klocaldomainurifilterhelper
%{_bindir}/krdb
%{tde_libdir}/fontthumbnail.la
%{tde_libdir}/fontthumbnail.so
%{tde_libdir}/kaccess.la
%{tde_libdir}/kaccess.so
%{tde_libdir}/kcm_access.la
%{tde_libdir}/kcm_access.so
%{tde_libdir}/kcm_arts.la
%{tde_libdir}/kcm_arts.so
%{tde_libdir}/kcm_background.la
%{tde_libdir}/kcm_background.so
%{tde_libdir}/kcm_bell.la
%{tde_libdir}/kcm_bell.so
%{tde_libdir}/kcm_clock.la
%{tde_libdir}/kcm_clock.so
%{tde_libdir}/kcm_colors.la
%{tde_libdir}/kcm_colors.so
%{tde_libdir}/kcm_componentchooser.la
%{tde_libdir}/kcm_componentchooser.so
%{tde_libdir}/kcm_crypto.la
%{tde_libdir}/kcm_crypto.so
%{tde_libdir}/kcm_css.la
%{tde_libdir}/kcm_css.so
%{tde_libdir}/kcm_display.la
%{tde_libdir}/kcm_display.so
%{tde_libdir}/kcm_energy.la
%{tde_libdir}/kcm_energy.so
%{tde_libdir}/kcm_filetypes.la
%{tde_libdir}/kcm_filetypes.so
%{tde_libdir}/kcm_fontinst.la
%{tde_libdir}/kcm_fontinst.so
%{tde_libdir}/kcm_fonts.la
%{tde_libdir}/kcm_fonts.so
#%{tde_libdir}/kcm_hwmanager.la
#%{tde_libdir}/kcm_hwmanager.so
%{tde_libdir}/kcm_icons.la
%{tde_libdir}/kcm_icons.so
%{tde_libdir}/kcm_info.la
%{tde_libdir}/kcm_info.so
%{tde_libdir}/kcm_input.la
%{tde_libdir}/kcm_input.so
%{tde_libdir}/kcm_ioslaveinfo.la
%{tde_libdir}/kcm_ioslaveinfo.so
%{tde_libdir}/kcm_joystick.la
%{tde_libdir}/kcm_joystick.so
%{tde_libdir}/kcm_kded.la
%{tde_libdir}/kcm_kded.so
%{tde_libdir}/kcm_[kt]dm.la
%{tde_libdir}/kcm_[kt]dm.so
%{tde_libdir}/kcm_kdnssd.so
%{tde_libdir}/kcm_kdnssd.la
%{tde_libdir}/kcm_keys.la
%{tde_libdir}/kcm_keys.so
%{tde_libdir}/kcm_kicker.la
%{tde_libdir}/kcm_kicker.so
%{tde_libdir}/kcm_kio.la
%{tde_libdir}/kcm_kio.so
%{tde_libdir}/kcm_knotify.la
%{tde_libdir}/kcm_knotify.so
%{tde_libdir}/kcm_konqhtml.la
%{tde_libdir}/kcm_konqhtml.so
%{tde_libdir}/kcm_konq.la
%{tde_libdir}/kcm_konq.so
%{tde_libdir}/kcm_kthememanager.la
%{tde_libdir}/kcm_kthememanager.so
%{tde_libdir}/kcm_kurifilt.la
%{tde_libdir}/kcm_kurifilt.so
%{tde_libdir}/kcm_launch.la
%{tde_libdir}/kcm_launch.so
%{tde_libdir}/kcm_locale.la
%{tde_libdir}/kcm_locale.so
%{tde_libdir}/kcm_nic.la
%{tde_libdir}/kcm_nic.so
%{tde_libdir}/kcm_performance.la
%{tde_libdir}/kcm_performance.so
%{tde_libdir}/kcm_privacy.la
%{tde_libdir}/kcm_privacy.so
%{tde_libdir}/kcm_samba.la
%{tde_libdir}/kcm_samba.so
%{tde_libdir}/kcm_screensaver.la
%{tde_libdir}/kcm_screensaver.so
%{tde_libdir}/kcm_smserver.la
%{tde_libdir}/kcm_smserver.so
%{tde_libdir}/kcm_spellchecking.la
%{tde_libdir}/kcm_spellchecking.so
%{tde_libdir}/kcm_style.la
%{tde_libdir}/kcm_style.so
%{tde_libdir}/kcm_taskbar.la
%{tde_libdir}/kcm_taskbar.so
%{tde_libdir}/kcm_usb.la
%{tde_libdir}/kcm_usb.so
%{tde_libdir}/kcm_view1394.la
%{tde_libdir}/kcm_view1394.so
%{tde_libdir}/kcm_xinerama.la
%{tde_libdir}/kcm_xinerama.so
%{tde_libdir}/kcontrol.la
%{tde_libdir}/kcontrol.so
%{tde_libdir}/kfile_font.la
%{tde_libdir}/kfile_font.so
%{tde_libdir}/kio_fonts.la
%{tde_libdir}/kio_fonts.so
%{tde_libdir}/kstyle_keramik_config.la
%{tde_libdir}/kstyle_keramik_config.so
%{tde_libdir}/libkfontviewpart.la
%{tde_libdir}/libkfontviewpart.so
%{tde_libdir}/libkshorturifilter.la
%{tde_libdir}/libkshorturifilter.so
%{tde_libdir}/libkuriikwsfilter.la
%{tde_libdir}/libkuriikwsfilter.so
%{tde_libdir}/libkurisearchfilter.la
%{tde_libdir}/libkurisearchfilter.so
%{tde_libdir}/liblocaldomainurifilter.la
%{tde_libdir}/liblocaldomainurifilter.so
%{_libdir}/lib[kt]deinit_kaccess.la
%{_libdir}/lib[kt]deinit_kaccess.so
%{_libdir}/lib[kt]deinit_kcontrol.la
%{_libdir}/lib[kt]deinit_kcontrol.so
%{_libdir}/libkfontinst.so.*
%{tde_appdir}/arts.desktop
%{tde_appdir}/background.desktop
%{tde_appdir}/bell.desktop
%{tde_appdir}/cache.desktop
%{tde_appdir}/cdinfo.desktop
%{tde_appdir}/clock.desktop
%{tde_appdir}/colors.desktop
%{tde_appdir}/componentchooser.desktop
%{tde_appdir}/cookies.desktop
%{tde_appdir}/crypto.desktop
%{tde_appdir}/desktopbehavior.desktop
%{tde_appdir}/desktop.desktop
%{tde_appdir}/desktoppath.desktop
%{tde_appdir}/devices.desktop
%{tde_appdir}/display.desktop
%{tde_appdir}/dma.desktop
%{tde_appdir}/ebrowsing.desktop
%{tde_appdir}/filebrowser.desktop
%{tde_appdir}/filetypes.desktop
%{tde_appdir}/fonts.desktop
#%{tde_appdir}/hwmanager.desktop
%{tde_appdir}/icons.desktop
%{tde_appdir}/installktheme.desktop
%{tde_appdir}/interrupts.desktop
%{tde_appdir}/ioports.desktop
%{tde_appdir}/ioslaveinfo.desktop
%{tde_appdir}/joystick.desktop
%{tde_appdir}/kcm_kdnssd.desktop
%{tde_appdir}/kcmaccess.desktop
%{tde_appdir}/kcmcss.desktop
%{tde_appdir}/kcmfontinst.desktop
%{tde_appdir}/kcmkded.desktop
%{tde_appdir}/kcmlaunch.desktop
%{tde_appdir}/kcmnotify.desktop
%{tde_appdir}/kcmperformance.desktop
%{tde_appdir}/kcmsmserver.desktop
%{tde_appdir}/kcmtaskbar.desktop
%{tde_appdir}/kcmusb.desktop
%{tde_appdir}/kcmview1394.desktop
%{tde_appdir}/KControl.desktop
%{tde_appdir}/[kt]dm.desktop
%{tde_appdir}/keys.desktop
%{tde_appdir}/kfontview.desktop
%{tde_appdir}/khtml_behavior.desktop
%{tde_appdir}/khtml_fonts.desktop
%{tde_appdir}/khtml_java_js.desktop
%{tde_appdir}/kinfocenter.desktop
%{tde_appdir}/kthememanager.desktop
%{tde_appdir}/lanbrowser.desktop
%{tde_appdir}/language.desktop
%{tde_appdir}/media.desktop
%{tde_appdir}/memory.desktop
%{tde_appdir}/mouse.desktop
%{tde_appdir}/netpref.desktop
%{tde_appdir}/nic.desktop
%{tde_appdir}/opengl.desktop
%{tde_appdir}/panel_appearance.desktop
%{tde_appdir}/panel.desktop
%{tde_appdir}/partitions.desktop
%{tde_appdir}/pci.desktop
%{tde_appdir}/privacy.desktop
%{tde_appdir}/processor.desktop
%{tde_appdir}/proxy.desktop
%{tde_appdir}/screensaver.desktop
%{tde_appdir}/scsi.desktop
%{tde_appdir}/smbstatus.desktop
%{tde_appdir}/sound.desktop
%{tde_appdir}/spellchecking.desktop
%{tde_appdir}/style.desktop
%{tde_appdir}/useragent.desktop
%{tde_appdir}/xserver.desktop
%{_datadir}/applnk/.hidden/energy.desktop
%{_datadir}/applnk/.hidden/fileappearance.desktop
%{_datadir}/applnk/.hidden/filebehavior.desktop
%{_datadir}/applnk/.hidden/filepreviews.desktop
%{_datadir}/applnk/.hidden/kcmkonqyperformance.desktop
%{_datadir}/applnk/.hidden/kicker_config_appearance.desktop
%{_datadir}/applnk/.hidden/kicker_config.desktop
%{_datadir}/applnk/.hidden/smb.desktop
%{_datadir}/applnk/.hidden/xinerama.desktop
%{_datadir}/applnk/Settings/LookNFeel/
%{_datadir}/applnk/Settings/WebBrowsing/khtml_appearance.desktop
%{_datadir}/applnk/Settings/WebBrowsing/nsplugin.desktop
%{_datadir}/applnk/Settings/WebBrowsing/smb.desktop
%{_datadir}/apps/kcm_componentchooser/kcm_browser.desktop
%{_datadir}/apps/kcm_componentchooser/kcm_kemail.desktop
%{_datadir}/apps/kcm_componentchooser/kcm_terminal.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/apps/konqueror/servicemenus/installfont.desktop
%{_datadir}/mimelnk/application/x-ktheme.desktop
%{_datadir}/mimelnk/fonts/folder.desktop
%{_datadir}/mimelnk/fonts/package.desktop
%{_datadir}/mimelnk/fonts/system-folder.desktop
%{_datadir}/services/fonts.protocol
%{_datadir}/services/fontthumbnail.desktop
%{_datadir}/services/kaccess.desktop
%{_datadir}/services/kfile_font.desktop
%{_datadir}/services/kfontviewpart.desktop
%{_datadir}/services/kshorturifilter.desktop
%{_datadir}/services/kuriikwsfilter.desktop
%{_datadir}/services/kurisearchfilter.desktop
%{_datadir}/services/localdomainurifilter.desktop

%{_datadir}/apps/usb.ids
%{_datadir}/apps/kcmview1394/oui.db

# The following features are not compiled under RHEL 5
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
%{_bindir}/krandrtray
%{tde_libdir}/kcm_displayconfig.la
%{tde_libdir}/kcm_displayconfig.so
%{tde_libdir}/kcm_iccconfig.la
%{tde_libdir}/kcm_iccconfig.so
%{tde_libdir}/kcm_randr.la
%{tde_libdir}/kcm_randr.so
%{tde_appdir}/displayconfig.desktop
%{tde_appdir}/iccconfig.desktop
%{tde_appdir}/krandrtray.desktop
%{_datadir}/applnk/.hidden/randr.desktop
%{_datadir}/autostart/krandrtray-autostart.desktop
%endif

%post -n trinity-kcontrol
/sbin/ldconfig || :
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun -n trinity-kcontrol
/sbin/ldconfig || :
update-desktop-database %{tde_appdir} 2> /dev/null || : 

##########

%package -n trinity-kcontrol-devel
Summary:	Development files for kcontrol
Group:		Development/Libraries
Requires:	trinity-kcontrol = %{version}-%{release}

%description -n trinity-kcontrol-devel
%{summary}

%files -n trinity-kcontrol-devel
%{_libdir}/libkfontinst.la
%{_libdir}/libkfontinst.so

%post -n trinity-kcontrol-devel
/sbin/ldconfig || :

%postun -n trinity-kcontrol-devel
/sbin/ldconfig || :

##########

%package bin
Summary:	core binaries for the TDE base module
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}
Requires:	pam

Provides:	tdebase-bin = %{version}-%{release}
Obsoletes:	tdebase-bin < %{version}-%{release}

%description bin
This package contains miscellaneous programs needed by other
TDE applications, particularly those in the TDE base module.

%files bin
%defattr(-,root,root,-)
%{_bindir}/krootbacking
#%{_bindir}/tdeinit_phase1
%attr(4511,root,root) %{_bindir}/[kt]dmtsak
%{_bindir}/tsak
%{_bindir}/kdebugdialog
%{_bindir}/kreadconfig
%{_bindir}/kwriteconfig
%{_bindir}/kstart
%{_datadir}/config/kxkb_groups
%{_bindir}/drkonqi
%{_bindir}/kapplymousetheme
%{_bindir}/kblankscrn.kss
%attr(4755,root,root) %{_bindir}/kcheckpass
%{_bindir}/kcminit
%{_bindir}/kcminit_startup
%{_bindir}/kdcop
%{_bindir}/[kt]desu
%attr(0755,root,root) %{_bindir}/[kt]desud
%{_bindir}/kdialog
%{_bindir}/khotkeys
%{_bindir}/knetattach
%{_bindir}/krandom.kss
%{_bindir}/ksystraycmd
%{_bindir}/kxkb
%{_libdir}/kconf_update_bin/khotkeys_update
%{tde_libdir}/kcminit.la
%{tde_libdir}/kcminit.so
%{tde_libdir}/kcminit_startup.la
%{tde_libdir}/kcminit_startup.so
%{tde_libdir}/kcm_keyboard.la
%{tde_libdir}/kcm_keyboard.so
%{tde_libdir}/kcm_khotkeys_init.la
%{tde_libdir}/kcm_khotkeys_init.so
%{tde_libdir}/kcm_khotkeys.la
%{tde_libdir}/kcm_khotkeys.so
%{tde_libdir}/kded_khotkeys.la
%{tde_libdir}/kded_khotkeys.so
%{tde_libdir}/kgreet_classic.la
%{tde_libdir}/kgreet_classic.so
%{tde_libdir}/kgreet_winbind.la
%{tde_libdir}/kgreet_winbind.so
%{tde_libdir}/khotkeys.la
%{tde_libdir}/khotkeys.so
%{tde_libdir}/khotkeys_arts.la
%{tde_libdir}/khotkeys_arts.so
%{tde_libdir}/kxkb.la
%{tde_libdir}/kxkb.so
%{_libdir}/lib[kt]deinit_kcminit.la
%{_libdir}/lib[kt]deinit_kcminit.so
%{_libdir}/lib[kt]deinit_kcminit_startup.la
%{_libdir}/lib[kt]deinit_kcminit_startup.so
%{_libdir}/lib[kt]deinit_khotkeys.la
%{_libdir}/lib[kt]deinit_khotkeys.so
%{_libdir}/lib[kt]deinit_kxkb.la
%{_libdir}/lib[kt]deinit_kxkb.so
%{_libdir}/libkhotkeys_shared.so.*
%{tde_appdir}/keyboard.desktop
%{tde_appdir}/keyboard_layout.desktop
%{tde_appdir}/khotkeys.desktop
%{tde_appdir}/knetattach.desktop
%{_datadir}/applnk/System/ScreenSavers/
%{_datadir}/apps/drkonqi/
%{_datadir}/apps/kconf_update/khotkeys_32b1_update.upd
%{_datadir}/apps/kconf_update/khotkeys_printscreen.upd
%{_datadir}/apps/kconf_update/konqueror_gestures_trinity21_update.upd
%{_datadir}/apps/kdcop/kdcopui.rc
%{_datadir}/apps/khotkeys/
%{_datadir}/services/kded/khotkeys.desktop
%{_datadir}/services/kxkb.desktop
%{_sysconfdir}/pam.d/kcheckpass-trinity
%{_sysconfdir}/pam.d/kscreensaver-trinity
%{tde_docdir}/HTML/en/kdcop/
%{tde_docdir}/HTML/en/kdebugdialog//
%{tde_docdir}/HTML/en/[kt]desu/
%{tde_docdir}/HTML/en/knetattach/
%{tde_docdir}/HTML/en/kxkb/

%post bin
/sbin/ldconfig || :
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun bin
/sbin/ldconfig || :
update-desktop-database %{tde_appdir} 2> /dev/null || : 

##########

%package bin-devel
Summary:	Development files for core binaries for the TDE base module
Group:		Development/Libraries
Requires:	%{name}-bin = %{version}-%{release}

Obsoletes:	tdebase-bin-devel < %{version}-%{release}
Provides:	tdebase-bin-devel = %{version}-%{release}

%description bin-devel
%{summary}

%files bin-devel
%{_libdir}/libkhotkeys_shared.la
%{_libdir}/libkhotkeys_shared.so

%post bin-devel
/sbin/ldconfig || :

%postun bin-devel
/sbin/ldconfig || :

##########

%package data
Summary:	shared data files for the TDE base module
Group:		Environment/Libraries
Requires:	%{name}-runtime-data-common = %{version}-%{release}

Obsoletes:	tdebase-data < %{version}-%{release}
Provides:	tdebase-data = %{version}-%{release}

%description data
This package contains the architecture-independent shared data files
needed for a basic TDE desktop installation.

%files data
%defattr(-,root,root,-)
%{_datadir}/config/kshorturifilterrc
%{_datadir}/applnk/.hidden/battery.desktop
%{_datadir}/applnk/.hidden/bwarning.desktop
%{_datadir}/applnk/.hidden/cwarning.desktop
%{_datadir}/applnk/.hidden/.directory
%{_datadir}/applnk/.hidden/email.desktop
%{_datadir}/applnk/.hidden/kcmkonq.desktop
%{_datadir}/applnk/.hidden/kcmkxmlrpcd.desktop
%{_datadir}/applnk/.hidden/konqhtml.desktop
%{_datadir}/applnk/.hidden/passwords.desktop
%{_datadir}/applnk/.hidden/power.desktop
%{_datadir}/applnk/.hidden/socks.desktop
%{_datadir}/applnk/.hidden/userinfo.desktop
%{_datadir}/applnk/.hidden/virtualdesktops.desktop
%{_datadir}/apps/kaccess/eventsrc
%{_datadir}/apps/kcmcss/template.css
%{_datadir}/apps/kcminput/
%{_datadir}/apps/kcmkeys/
%{_datadir}/apps/kcmlocale/pics/background.png
%{_datadir}/apps/kconf_update/convertShortcuts.pl
%{_datadir}/apps/kconf_update/kaccel.upd
%{_datadir}/apps/kconf_update/kcmdisplayrc.upd
%{_datadir}/apps/kconf_update/kuriikwsfilter.upd
%{_datadir}/apps/kconf_update/mouse_cursor_theme.upd
%{_datadir}/apps/kconf_update/socks.upd
%{_datadir}/apps/kcontrol/
%{_datadir}/apps/kdisplay/
%{_datadir}/apps/kfontview/
%{_datadir}/apps/kinfocenter/kinfocenterui.rc
%{_datadir}/apps/kthememanager/themes/*
%{_datadir}/icons/crystalsvg/*/apps/access.png
%{_datadir}/icons/crystalsvg/*/apps/acroread.png
%{_datadir}/icons/crystalsvg/*/apps/applixware.png
%{_datadir}/icons/crystalsvg/*/apps/arts.png
%{_datadir}/icons/crystalsvg/*/apps/background.png
%{_datadir}/icons/crystalsvg/*/apps/bell.png
%{_datadir}/icons/crystalsvg/*/apps/cache.png
%{_datadir}/icons/crystalsvg/*/apps/clanbomber.png
%{_datadir}/icons/crystalsvg/*/apps/clock.png
%{_datadir}/icons/crystalsvg/*/apps/colors.png
%{_datadir}/icons/crystalsvg/*/apps/date.png
%{_datadir}/icons/crystalsvg/*/apps/email.png
%{_datadir}/icons/crystalsvg/*/apps/energy.png
%{_datadir}/icons/crystalsvg/*/apps/energy_star.png
%{_datadir}/icons/crystalsvg/*/apps/filetypes.png
%{_datadir}/icons/crystalsvg/*/apps/fonts.png
%{_datadir}/icons/crystalsvg/*/apps/gimp.png
%{_datadir}/icons/crystalsvg/*/apps/help_index.png
%{_datadir}/icons/crystalsvg/*/apps/hwinfo.png
%{_datadir}/icons/crystalsvg/*/apps/kcmdevices.png
%{_datadir}/icons/crystalsvg/*/apps/kcmdf.png
%{_datadir}/icons/crystalsvg/*/apps/kcmkwm.png
%{_datadir}/icons/crystalsvg/*/apps/kcmmemory.png
%{_datadir}/icons/crystalsvg/*/apps/kcmpartitions.png
%{_datadir}/icons/crystalsvg/*/apps/kcmpci.png
%{_datadir}/icons/crystalsvg/*/apps/kcontrol.png
%{_datadir}/icons/crystalsvg/*/apps/[kt]dmconfig.png
%{_datadir}/icons/crystalsvg/*/apps/key_bindings.png
%{_datadir}/icons/crystalsvg/*/apps/kfm_home.png
%{_datadir}/icons/crystalsvg/*/apps/kscreensaver.png
%{_datadir}/icons/crystalsvg/*/apps/kthememgr.png
%{_datadir}/icons/crystalsvg/*/apps/licq.png
%{_datadir}/icons/crystalsvg/*/apps/linuxconf.png
%{_datadir}/icons/crystalsvg/*/apps/locale.png
%{_datadir}/icons/crystalsvg/*/apps/looknfeel.png
%{_datadir}/icons/crystalsvg/*/apps/multimedia.png
%{_datadir}/icons/crystalsvg/*/apps/netscape.png
%{_datadir}/icons/crystalsvg/*/apps/package_applications.png
%{_datadir}/icons/crystalsvg/*/apps/package_development.png
%{_datadir}/icons/crystalsvg/*/apps/package_favourite.png
%{_datadir}/icons/crystalsvg/*/apps/package_games.png
%{_datadir}/icons/crystalsvg/*/apps/package_multimedia.png
%{_datadir}/icons/crystalsvg/*/apps/package_network.png
%{_datadir}/icons/crystalsvg/*/apps/package.png
%{_datadir}/icons/crystalsvg/*/apps/package_settings.png
%{_datadir}/icons/crystalsvg/*/apps/package_toys.png
%{_datadir}/icons/crystalsvg/*/apps/package_utilities.png
%{_datadir}/icons/crystalsvg/*/apps/penguin.png
%{_datadir}/icons/crystalsvg/*/apps/personal.png
%{_datadir}/icons/crystalsvg/*/apps/phppg.png
%{_datadir}/icons/crystalsvg/*/apps/proxy.png
%{_datadir}/icons/crystalsvg/*/apps/pysol.png
%{_datadir}/icons/crystalsvg/*/apps/randr.png
%{_datadir}/icons/crystalsvg/*/apps/samba.png
%{_datadir}/icons/crystalsvg/*/apps/staroffice.png
%{_datadir}/icons/crystalsvg/*/apps/stylesheet.png
%{_datadir}/icons/crystalsvg/*/apps/terminal.png
%{_datadir}/icons/crystalsvg/*/apps/tux.png
%{_datadir}/icons/crystalsvg/*/apps/wp.png
%{_datadir}/icons/crystalsvg/*/apps/xclock.png
%{_datadir}/icons/crystalsvg/*/apps/xfmail.png
%{_datadir}/icons/crystalsvg/*/apps/xmag.png
%{_datadir}/icons/crystalsvg/*/apps/xpaint.png
%{_datadir}/icons/crystalsvg/scalable/apps/access.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/acroread.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/aim.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/aktion.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/antivirus.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/applixware.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/arts.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/background.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/bell.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/browser.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/cache.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/camera.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/clanbomber.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/clock.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/colors.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/core.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/date.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/display.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/download_manager.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/email.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/energy.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/error.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/fifteenpieces.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/filetypes.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/fonts.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/galeon.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/gnome_apps.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/hardware.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/hwinfo.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/ieee1394.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/kcmdevices.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/kcmkwm.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/kcmx.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/locale.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/my_mac.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/netscape.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/openoffice.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/package_development.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/package_toys.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/penguin.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/personal.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/quicktime.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/realplayer.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/samba.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/shell.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/staroffice.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/stylesheet.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/terminal.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/tux.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/wine.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/x.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/xapp.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/xcalc.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/xchat.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/xclock.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/xeyes.svgz
%{_datadir}/icons/crystalsvg/scalable/apps/xpaint.svgz
%{_datadir}/icons/crystalsvg/*/devices/laptop.png
%{_datadir}/icons/crystalsvg/*/devices/laptop.svgz
%{_datadir}/icons/crystalsvg/*/actions/newfont.png
%{_datadir}/icons/crystalsvg/*/apps/abiword.png
%{_datadir}/icons/crystalsvg/*/apps/agent.png
%{_datadir}/icons/crystalsvg/*/apps/alevt.png
%{_datadir}/icons/crystalsvg/*/apps/assistant.png
%{_datadir}/icons/crystalsvg/*/apps/blender.png
%{_datadir}/icons/crystalsvg/*/apps/bluefish.png
%{_datadir}/icons/crystalsvg/*/apps/cookie.png
%{_datadir}/icons/crystalsvg/*/apps/designer.png
%{_datadir}/icons/crystalsvg/*/apps/dia.png
%{_datadir}/icons/crystalsvg/*/apps/dlgedit.png
%{_datadir}/icons/crystalsvg/*/apps/eclipse.png
%{_datadir}/icons/crystalsvg/*/apps/edu_languages.png
%{_datadir}/icons/crystalsvg/*/apps/edu_mathematics.png
%{_datadir}/icons/crystalsvg/*/apps/edu_miscellaneous.png
%{_datadir}/icons/crystalsvg/*/apps/edu_science.png
%{_datadir}/icons/crystalsvg/*/apps/emacs.png
%{_datadir}/icons/crystalsvg/*/apps/enhanced_browsing.png
%{_datadir}/icons/crystalsvg/*/apps/evolution.png
%{_datadir}/icons/crystalsvg/*/apps/fifteenpieces.png
%{_datadir}/icons/crystalsvg/*/apps/gabber.png
%{_datadir}/icons/crystalsvg/*/apps/gaim.png
%{_datadir}/icons/crystalsvg/*/apps/gnome_apps.png
%{_datadir}/icons/crystalsvg/*/apps/gnomemeeting.png
%{_datadir}/icons/crystalsvg/*/apps/gnucash.png
%{_datadir}/icons/crystalsvg/*/apps/gnumeric.png
%{_datadir}/icons/crystalsvg/*/apps/gv.png
%{_datadir}/icons/crystalsvg/*/apps/gvim.png
%{_datadir}/icons/crystalsvg/*/apps/icons.png
%{_datadir}/icons/crystalsvg/*/apps/iconthemes.png
%{_datadir}/icons/crystalsvg/*/apps/ieee1394.png
%{_datadir}/icons/crystalsvg/*/apps/input_devices_settings.png
%{_datadir}/icons/crystalsvg/*/apps/kcmkicker.png
%{_datadir}/icons/crystalsvg/*/apps/kcmmidi.png
%{_datadir}/icons/crystalsvg/*/apps/kcmprocessor.png
%{_datadir}/icons/crystalsvg/*/apps/kcmscsi.png
%{_datadir}/icons/crystalsvg/*/apps/kcmsound.png
%{_datadir}/icons/crystalsvg/*/apps/kcmsystem.png
%{_datadir}/icons/crystalsvg/*/apps/kcmx.png
%{_datadir}/icons/crystalsvg/*/apps/keyboard.png
%{_datadir}/icons/crystalsvg/*/apps/keyboard_layout.png
%{_datadir}/icons/crystalsvg/*/apps/knotify.png
%{_datadir}/icons/crystalsvg/*/apps/kvirc.png
%{_datadir}/icons/crystalsvg/*/apps/linguist.png
%{_datadir}/icons/crystalsvg/*/apps/lyx.png
%{_datadir}/icons/crystalsvg/*/apps/mac.png
%{_datadir}/icons/crystalsvg/*/apps/mathematica.png
%{_datadir}/icons/crystalsvg/*/apps/nedit.png
%{_datadir}/icons/crystalsvg/*/apps/opera.png
%{_datadir}/icons/crystalsvg/*/apps/package_application.png
%{_datadir}/icons/crystalsvg/*/apps/package_editors.png
%{_datadir}/icons/crystalsvg/*/apps/package_edutainment.png
%{_datadir}/icons/crystalsvg/*/apps/package_games_arcade.png
%{_datadir}/icons/crystalsvg/*/apps/package_games_board.png
%{_datadir}/icons/crystalsvg/*/apps/package_games_card.png
%{_datadir}/icons/crystalsvg/*/apps/package_games_strategy.png
%{_datadir}/icons/crystalsvg/*/apps/package_graphics.png
%{_datadir}/icons/crystalsvg/*/apps/package_system.png
%{_datadir}/icons/crystalsvg/*/apps/package_wordprocessing.png
%{_datadir}/icons/crystalsvg/*/apps/pan.png
%{_datadir}/icons/crystalsvg/*/apps/panel_settings.png
%{_datadir}/icons/crystalsvg/*/apps/plan.png
%{_datadir}/icons/crystalsvg/*/apps/planner.png
%{_datadir}/icons/crystalsvg/*/apps/pybliographic.png
%{_datadir}/icons/crystalsvg/*/apps/realplayer.png
%{_datadir}/icons/crystalsvg/*/apps/remote.png
%{_datadir}/icons/crystalsvg/*/apps/scribus.png
%{_datadir}/icons/crystalsvg/*/apps/sodipodi.png
%{_datadir}/icons/crystalsvg/*/apps/style.png
%{_datadir}/icons/crystalsvg/*/apps/usb.png
%{_datadir}/icons/crystalsvg/*/apps/vnc.png
%{_datadir}/icons/crystalsvg/*/apps/wabi.png
%{_datadir}/icons/crystalsvg/*/apps/wine.png
%{_datadir}/icons/crystalsvg/*/apps/xcalc.png
%{_datadir}/icons/crystalsvg/*/apps/xchat.png
%{_datadir}/icons/crystalsvg/*/apps/xclipboard.png
%{_datadir}/icons/crystalsvg/*/apps/xconsole.png
%{_datadir}/icons/crystalsvg/*/apps/xedit.png
%{_datadir}/icons/crystalsvg/*/apps/xemacs.png
%{_datadir}/icons/crystalsvg/*/apps/xeyes.png
%{_datadir}/icons/crystalsvg/*/apps/xfig.png
%{_datadir}/icons/crystalsvg/*/apps/xload.png
%{_datadir}/icons/crystalsvg/*/apps/xmms.png
%{_datadir}/icons/crystalsvg/*/apps/xosview.png
%{_datadir}/icons/crystalsvg/*/apps/xv.png
%{_datadir}/icons/crystalsvg/*/apps/galeon.png
%{_datadir}/icons/crystalsvg/*/apps/kcmdrkonqi.png
%{_datadir}/icons/crystalsvg/*/apps/pinguin.png
%{_datadir}/icons/crystalsvg/*/apps/x.png
%{_datadir}/icons/crystalsvg/*/apps/xapp.png
%{_datadir}/icons/crystalsvg/*/apps/xawtv.png
%{_datadir}/icons/crystalsvg/*/apps/kcmopengl.png
%{_datadir}/icons/crystalsvg/*/apps/wmaker_apps.png
%{_datadir}/icons/crystalsvg/*/apps/qtella.png
%{_datadir}/services/searchproviders
%{_datadir}/services/useragentstrings/*.desktop
%{_datadir}/servicetypes/searchprovider.desktop
%{_datadir}/servicetypes/uasprovider.desktop
%exclude %{_datadir}/sounds/pop.wav
%{_datadir}/sounds/
%{_datadir}/wallpapers/*

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

%exclude %{tde_docdir}/HTML/en/kcontrol/kcmkonsole/
%{tde_docdir}/HTML/en/kcontrol/
%{tde_docdir}/HTML/en/kinfocenter/

%post data
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

%postun data
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package kio-plugins
Summary:	core I/O slaves for TDE
Group:		Applications/Utilities
Requires:	trinity-kdesktop = %{version}-%{release}
Requires:	cyrus-sasl
Requires:	psmisc
Requires:	cryptsetup-luks

Obsoletes:	tdebase-kio-plugins < %{version}-%{release}
Provides:	tdebase-kio-plugins = %{version}-%{release}

%description kio-plugins
This package includes the base kioslaves. They include, amongst many
others, file, http, and ftp.

It also includes the media kioslave, which handles removable devices,
and which works best with hal (and therefore udev) and pmount. Media
also extends the functionality of many other kioslaves. To use this
service, please make sure that your user is a member of the plugdev
group.

%files kio-plugins
%defattr(-,root,root,-)
%{_bindir}/kio_media_mounthelper
%{_bindir}/ktrash
%{tde_libdir}/cursorthumbnail.la
%{tde_libdir}/cursorthumbnail.so
%{tde_libdir}/djvuthumbnail.la
%{tde_libdir}/djvuthumbnail.so
%{tde_libdir}/exrthumbnail.la
%{tde_libdir}/exrthumbnail.so
%{tde_libdir}/htmlthumbnail.la
%{tde_libdir}/htmlthumbnail.so
%{tde_libdir}/imagethumbnail.la
%{tde_libdir}/imagethumbnail.so
%{tde_libdir}/kcm_cgi.la
%{tde_libdir}/kcm_cgi.so
%{tde_libdir}/kcm_media.la
%{tde_libdir}/kcm_media.so
%{tde_libdir}/kded_homedirnotify.la
%{tde_libdir}/kded_homedirnotify.so
%{tde_libdir}/kded_mediamanager.la
%{tde_libdir}/kded_mediamanager.so
%{tde_libdir}/kded_medianotifier.la
%{tde_libdir}/kded_medianotifier.so
%{tde_libdir}/kded_remotedirnotify.la
%{tde_libdir}/kded_remotedirnotify.so
%{tde_libdir}/kded_systemdirnotify.la
%{tde_libdir}/kded_systemdirnotify.so
%{tde_libdir}/kfile_media.la
%{tde_libdir}/kfile_media.so
%{tde_libdir}/kfile_trash.la
%{tde_libdir}/kfile_trash.so
%{tde_libdir}/kio_about.la
%{tde_libdir}/kio_about.so
%{tde_libdir}/kio_cgi.la
%{tde_libdir}/kio_cgi.so
%{tde_libdir}/kio_filter.la
%{tde_libdir}/kio_filter.so
%{tde_libdir}/kio_finger.la
%{tde_libdir}/kio_finger.so
%{tde_libdir}/kio_fish.la
%{tde_libdir}/kio_fish.so
%{tde_libdir}/kio_floppy.la
%{tde_libdir}/kio_floppy.so
%{tde_libdir}/kio_home.la
%{tde_libdir}/kio_home.so
%{tde_libdir}/kio_info.la
%{tde_libdir}/kio_info.so
%{tde_libdir}/kio_mac.la
%{tde_libdir}/kio_mac.so
%{tde_libdir}/kio_man.la
%{tde_libdir}/kio_man.so
%{tde_libdir}/kio_media.la
%{tde_libdir}/kio_media.so
%{tde_libdir}/kio_nfs.la
%{tde_libdir}/kio_nfs.so
%{tde_libdir}/kio_remote.la
%{tde_libdir}/kio_remote.so
%{tde_libdir}/kio_settings.la
%{tde_libdir}/kio_settings.so
%{tde_libdir}/kio_sftp.la
%{tde_libdir}/kio_sftp.so
%{tde_libdir}/kio_smb.la
%{tde_libdir}/kio_smb.so
%{tde_libdir}/kio_system.la
%{tde_libdir}/kio_system.so
%{tde_libdir}/kio_tar.la
%{tde_libdir}/kio_tar.so
%{tde_libdir}/kio_thumbnail.la
%{tde_libdir}/kio_thumbnail.so
%{tde_libdir}/kio_trash.la
%{tde_libdir}/kio_trash.so
%{tde_libdir}/libkmanpart.la
%{tde_libdir}/libkmanpart.so
%{tde_libdir}/media_propsdlgplugin.la
%{tde_libdir}/media_propsdlgplugin.so
%{tde_libdir}/textthumbnail.la
%{tde_libdir}/textthumbnail.so
%{tde_appdir}/kcmcgi.desktop
%{_datadir}/apps/kio_finger/kio_finger.css
%{_datadir}/apps/kio_finger/kio_finger.pl
%{_datadir}/apps/kio_info/kde-info2html
%{_datadir}/apps/kio_info/kde-info2html.conf
%{_datadir}/apps/kio_man/kio_man.css
%{_datadir}/apps/konqueror/dirtree/remote/smb-network.desktop
%{_datadir}/apps/remoteview/smb-network.desktop
%{_datadir}/apps/systemview/*.desktop
%{_datadir}/config.kcfg/mediamanagersettings.kcfg
%{_datadir}/mimelnk/application/x-smb-server.desktop
%{_datadir}/mimelnk/application/x-smb-workgroup.desktop
%{_datadir}/mimelnk/inode/system_directory.desktop
%{_datadir}/mimelnk/media/*.desktop
%{_datadir}/services/about.protocol
%{_datadir}/services/applications.protocol
%{_datadir}/services/ar.protocol
%{_datadir}/services/bzip.protocol
%{_datadir}/services/bzip2.protocol
%{_datadir}/services/cgi.protocol
%{_datadir}/services/cursorthumbnail.desktop
%{_datadir}/services/djvuthumbnail.desktop
%{_datadir}/services/exrthumbnail.desktop
%{_datadir}/services/finger.protocol
%{_datadir}/services/fish.protocol
%{_datadir}/services/floppy.protocol
%{_datadir}/services/gzip.protocol
%{_datadir}/services/home.protocol
%{_datadir}/services/htmlthumbnail.desktop
%{_datadir}/services/imagethumbnail.desktop
%{_datadir}/services/info.protocol
%{_datadir}/services/kded/homedirnotify.desktop
%{_datadir}/services/kded/mediamanager.desktop
%{_datadir}/services/kded/medianotifier.desktop
%{_datadir}/services/kded/remotedirnotify.desktop
%{_datadir}/services/kded/systemdirnotify.desktop
%{_datadir}/services/kfile_media.desktop
%{_datadir}/services/kfile_trash_system.desktop
%{_datadir}/services/kmanpart.desktop
%{_datadir}/services/mac.protocol
%{_datadir}/services/man.protocol
%{_datadir}/services/media.protocol
%{_datadir}/services/media_propsdlgplugin.desktop
%{_datadir}/services/nfs.protocol
%{_datadir}/services/nxfish.protocol
%{_datadir}/services/programs.protocol
%{_datadir}/services/remote.protocol
%{_datadir}/services/settings.protocol
%{_datadir}/services/sftp.protocol
%{_datadir}/services/smb.protocol
%{_datadir}/services/system.protocol
%{_datadir}/services/tar.protocol
%{_datadir}/services/textthumbnail.desktop
%{_datadir}/services/thumbnail.protocol
%{_datadir}/services/trash.protocol
%{_datadir}/services/zip.protocol
%{_datadir}/servicetypes/thumbcreator.desktop
%{_datadir}/services/kfile_trash.desktop
%{tde_docdir}/HTML/en/kioslave/

%post kio-plugins
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun kio-plugins
update-desktop-database %{tde_appdir} 2> /dev/null || : 


##########

%package -n trinity-kdepasswd
Summary:	password changer for TDE
Group:		Applications/Utilities

%description -n trinity-kdepasswd
This is a simple application which allows users to change their
system passwords.

%files -n trinity-kdepasswd
%defattr(-,root,root,-)
%{_bindir}/kdepasswd
%{tde_libdir}/kcm_useraccount.la
%{tde_libdir}/kcm_useraccount.so
%{tde_appdir}/kcm_useraccount.desktop
%{tde_appdir}/kdepasswd.desktop
%exclude %{_datadir}/apps/[kt]dm/pics/users/default1.png
%exclude %{_datadir}/apps/[kt]dm/pics/users/default2.png
%exclude %{_datadir}/apps/[kt]dm/pics/users/default3.png
%exclude %{_datadir}/apps/[kt]dm/pics/users/root1.png
%{_datadir}/apps/[kt]dm/pics/users/*.png
%{_datadir}/config.kcfg/kcm_useraccount.kcfg
%{_datadir}/config.kcfg/kcm_useraccount_pass.kcfg

%post -n trinity-kdepasswd
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun -n trinity-kdepasswd
update-desktop-database %{tde_appdir} 2> /dev/null || : 

##########

%package -n trinity-tdeprint
Summary:	print system for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}
Requires:	psutils

%description -n trinity-tdeprint
This package contains the TDE printing subsystem. It can use CUPS,
lpd-ng or the traditional lpd. It also includes support for fax and
pdf printing.

Installation of smbclient will make you able to use smb shared printers.

%files -n trinity-tdeprint
%defattr(-,root,root,-)
%{_bindir}/[kt]deprintfax
%{_bindir}/kjobviewer
%{_bindir}/kprinter
%{tde_libdir}/kcm_printmgr.la
%{tde_libdir}/kcm_printmgr.so
%{tde_libdir}/kio_print.la
%{tde_libdir}/kio_print.so
%{tde_libdir}/kjobviewer.la
%{tde_libdir}/kjobviewer.so
%{tde_libdir}/kprinter.la
%{tde_libdir}/kprinter.so
%{tde_libdir}/lib[kt]deprint_part.la
%{tde_libdir}/lib[kt]deprint_part.so
%{_libdir}/lib[kt]deinit_kjobviewer.la
%{_libdir}/lib[kt]deinit_kjobviewer.so
%{_libdir}/lib[kt]deinit_kprinter.la
%{_libdir}/lib[kt]deinit_kprinter.so
%{tde_appdir}/[kt]deprintfax.desktop
%{tde_appdir}/kjobviewer.desktop
%{tde_appdir}/printers.desktop
%{_datadir}/apps/[kt]deprintfax/
%{_datadir}/apps/[kt]deprint_part/[kt]deprint_part.rc
%{_datadir}/apps/[kt]deprint/
%{_datadir}/apps/kjobviewer/kjobviewerui.rc
%{_datadir}/icons/hicolor/*/apps/[kt]deprintfax.png
%{_datadir}/icons/hicolor/*/apps/kjobviewer.png
%{_datadir}/icons/hicolor/*/apps/printmgr.png
%{_datadir}/icons/hicolor/*/apps/[kt]deprintfax.svgz
%{_datadir}/icons/hicolor/*/apps/kjobviewer.svgz
%{_datadir}/icons/hicolor/*/apps/printmgr.svgz
%{_datadir}/mimelnk/print
%{_datadir}/services/[kt]deprint_part.desktop
%{_datadir}/services/printdb.protocol
%{_datadir}/services/print.protocol
%{tde_docdir}/HTML/en/[kt]deprint/

%post -n trinity-tdeprint
/sbin/ldconfig || :
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

%postun -n trinity-tdeprint
/sbin/ldconfig || :
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-kdesktop
Summary:	miscellaneous binaries and files for the TDE desktop
Group:		Applications/Utilities
Requires:	%{name}-bin = %{version}-%{release}
Requires:	%{name}-data = %{version}-%{release}
Requires:	trinity-libkonq = %{version}-%{release}
Requires:	eject
Requires:	xdg-utils

%description -n trinity-kdesktop
This package contains miscellaneous binaries and files integral to
the TDE desktop.

%files -n trinity-kdesktop
%defattr(-,root,root,-)
%{_datadir}/config/kdesktop_custom_menu1
%{_datadir}/config/kdesktop_custom_menu2
%{_bindir}/kcheckrunning
%{_bindir}/kxdglauncher
%{_bindir}/kdeeject
%{_bindir}/kdesktop
%{_bindir}/kdesktop_lock
%{_bindir}/kwebdesktop
%{tde_libdir}/kdesktop.la
%{tde_libdir}/kdesktop.so
%{_libdir}/lib[kt]deinit_kdesktop.la
%{_libdir}/lib[kt]deinit_kdesktop.so
%{_datadir}/apps/kdesktop/
%{_datadir}/apps/konqueror/servicemenus/kdesktopSetAsBackground.desktop
%{_datadir}/autostart/kdesktop.desktop
%{_datadir}/config.kcfg/kdesktop.kcfg
%{_datadir}/config.kcfg/klaunch.kcfg
%{_datadir}/config.kcfg/kwebdesktop.kcfg
%{_datadir}/icons/crystalsvg/*/apps/error.png

%post -n trinity-kdesktop
/sbin/ldconfig || :
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

%postun -n trinity-kdesktop
/sbin/ldconfig || :
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-kdesktop-devel
Summary:	Development files for kdesktop
Group:		Development/Libraries
Requires:	trinity-kdesktop = %{version}-%{release}

%description -n trinity-kdesktop-devel
%{summary}

%files -n trinity-kdesktop-devel
%{_includedir}/KBackgroundIface.h
%{_includedir}/KDesktopIface.h
%{_includedir}/KScreensaverIface.h

##########

%package -n trinity-tdm
Summary:	X Display manager for TDE
Group:		Applications/Utilities
Requires:	%{name}-bin = %{version}-%{release}
Requires:	%{name}-data = %{version}-%{release}
Requires:	pam

# Provides the global Xsession script (/etc/X11/xinit/Xsession)
Requires:	xorg-x11-xinit

# Required for Fedora LiveCD
Provides:	service(graphical-login)

%description -n trinity-tdm
tdm manages a collection of X servers, which may be on the local host or
remote machines. It provides services similar to those provided by init,
getty, and login on character-based terminals: prompting for login name and
password, authenticating the user, and running a session. tdm supports XDMCP
(X Display Manager Control Protocol) and can also be used to run a chooser
process which presents the user with a menu of possible hosts that offer
XDMCP display management.

A collection of icons to associate with individual users is included with
TDE, but as part of the kdepasswd package.

The menu package will help to provide TDM with a list of window managers
that can be launched, if the window manager does not register with TDM
already. Most users won't need this.

%files -n trinity-tdm
%defattr(-,root,root,-)
%{tde_libdir}/kgreet_pam.la
%{tde_libdir}/kgreet_pam.so
%{_bindir}/gen[kt]dmconf
%{_bindir}/[kt]dm
%{_bindir}/[kt]dm_config
%{_bindir}/[kt]dmctl
%{_bindir}/[kt]dm_greet
%{_bindir}/krootimage
%{_datadir}/apps/[kt]dm/pics/kdelogo.png
%{_datadir}/apps/[kt]dm/pics/kdelogo-crystal.png
%{_datadir}/apps/[kt]dm/pics/shutdown.jpg
%{_datadir}/apps/[kt]dm/pics/users/default1.png
%{_datadir}/apps/[kt]dm/pics/users/default2.png
%{_datadir}/apps/[kt]dm/pics/users/default3.png
%{_datadir}/apps/[kt]dm/pics/users/root1.png
%{_datadir}/apps/[kt]dm/sessions/*.desktop
%{_datadir}/apps/[kt]dm/themes/
%{_datadir}/config/[kt]dm/
%{tde_docdir}/HTML/en/[kt]dm/

# RHEL/Fedora specific
/usr/share/xsessions/*.desktop
%{_sysconfdir}/pam.d/kdm-trinity
%{_sysconfdir}/pam.d/kdm-trinity-np

##########

%package -n trinity-tdm-devel
Summary:	Development files for tdm
Group:		Development/Libraries
Requires:	trinity-tdm = %{version}-%{release}

%description -n trinity-tdm-devel
%{summary}

%files -n trinity-tdm-devel
%{_includedir}/kgreeterplugin.h

##########

%package -n trinity-kfind
Summary:	file-find utility for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-kfind
kfind can be used to find files and directories on your
workstations.

%files -n trinity-kfind
%defattr(-,root,root,-)
%{_bindir}/kfind
%{tde_libdir}/libkfindpart.la
%{tde_libdir}/libkfindpart.so
%{tde_appdir}/Kfind.desktop
%{_datadir}/apps/kfindpart/
%{_datadir}/icons/hicolor/*/apps/kfind.png
%{_datadir}/services/kfindpart.desktop
%{_datadir}/servicetypes/findpart.desktop
%{tde_docdir}/HTML/en/kfind/

%post -n trinity-kfind
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

%postun -n trinity-kfind
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-khelpcenter
Summary:	help center for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}
Requires:	htdig

%description -n trinity-khelpcenter
The TDE Help Center provides documentation on how to use the KDE desktop.

The htdig package is needed to build a searchable archive of TDE
documentation.

%files -n trinity-khelpcenter
%defattr(-,root,root,-)
%{_bindir}/khc_beagle_index.pl
%{_bindir}/khc_beagle_search.pl
%{_bindir}/khc_docbookdig.pl
%{_bindir}/khc_htdig.pl
%{_bindir}/khc_htsearch.pl
%{_bindir}/khc_indexbuilder
%{_bindir}/khc_mansearch.pl
%{_bindir}/khelpcenter
%{tde_libdir}/khelpcenter.la
%{tde_libdir}/khelpcenter.so
%{_libdir}/lib[kt]deinit_khelpcenter.la
%{_libdir}/lib[kt]deinit_khelpcenter.so
%{tde_appdir}/Help.desktop
%{_datadir}/apps/khelpcenter/
%{_datadir}/config.kcfg/khelpcenter.kcfg
%{_datadir}/icons/hicolor/*/apps/khelpcenter.*
%{_datadir}/services/khelpcenter.desktop
%{tde_docdir}/HTML/en/khelpcenter/

%post -n trinity-khelpcenter
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%postun -n trinity-khelpcenter
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

##########

%package -n trinity-kicker
Summary:	desktop panel for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-kicker
Kicker provides the TDE panel on you desktop. It can be used as a
program launcher and can load plugins to provide additional
functionality.

%files -n trinity-kicker
%defattr(-,root,root,-)
%{_bindir}/appletproxy
%{_bindir}/extensionproxy
%{_bindir}/kasbar
%{_bindir}/kicker
%{_libdir}/kconf_update_bin/kicker-3.4-reverseLayout
%{tde_libdir}/appletproxy.la
%{tde_libdir}/appletproxy.so
%{tde_libdir}/clock_panelapplet.la
%{tde_libdir}/clock_panelapplet.so
%{tde_libdir}/dockbar_panelextension.la
%{tde_libdir}/dockbar_panelextension.so
%{tde_libdir}/extensionproxy.la
%{tde_libdir}/extensionproxy.so
%{tde_libdir}/kasbar_panelextension.la
%{tde_libdir}/kasbar_panelextension.so
%{tde_libdir}/kicker.la
%{tde_libdir}/kickermenu_find.la
%{tde_libdir}/kickermenu_find.so
%{tde_libdir}/kickermenu_kate.so
%{tde_libdir}/kickermenu_kate.la
%{tde_libdir}/kickermenu_[kt]deprint.la
%{tde_libdir}/kickermenu_[kt]deprint.so
%{tde_libdir}/kickermenu_konqueror.la
%{tde_libdir}/kickermenu_konqueror.so
%{tde_libdir}/kickermenu_konsole.la
%{tde_libdir}/kickermenu_konsole.so
%{tde_libdir}/kickermenu_prefmenu.la
%{tde_libdir}/kickermenu_prefmenu.so
%{tde_libdir}/kickermenu_recentdocs.la
%{tde_libdir}/kickermenu_recentdocs.so
%{tde_libdir}/kickermenu_remotemenu.la
%{tde_libdir}/kickermenu_remotemenu.so
%{tde_libdir}/kickermenu_systemmenu.la
%{tde_libdir}/kickermenu_systemmenu.so
%{tde_libdir}/kicker.so
%{tde_libdir}/launcher_panelapplet.la
%{tde_libdir}/launcher_panelapplet.so
%{tde_libdir}/lockout_panelapplet.la
%{tde_libdir}/lockout_panelapplet.so
%{tde_libdir}/media_panelapplet.la
%{tde_libdir}/media_panelapplet.so
%{tde_libdir}/menu_panelapplet.la
%{tde_libdir}/menu_panelapplet.so
%{tde_libdir}/minipager_panelapplet.la
%{tde_libdir}/minipager_panelapplet.so
%{tde_libdir}/naughty_panelapplet.la
%{tde_libdir}/naughty_panelapplet.so
%{tde_libdir}/run_panelapplet.la
%{tde_libdir}/run_panelapplet.so
%{tde_libdir}/sidebar_panelextension.la
%{tde_libdir}/sidebar_panelextension.so
%{tde_libdir}/systemtray_panelapplet.la
%{tde_libdir}/systemtray_panelapplet.so
%{tde_libdir}/taskbar_panelapplet.la
%{tde_libdir}/taskbar_panelapplet.so
%{tde_libdir}/taskbar_panelextension.la
%{tde_libdir}/taskbar_panelextension.so
%{tde_libdir}/trash_panelapplet.la
%{tde_libdir}/trash_panelapplet.so
%{_libdir}/libkasbar.so.*
%{_libdir}/lib[kt]deinit_appletproxy.la
%{_libdir}/lib[kt]deinit_appletproxy.so
%{_libdir}/lib[kt]deinit_extensionproxy.la
%{_libdir}/lib[kt]deinit_extensionproxy.so
%{_libdir}/lib[kt]deinit_kicker.la
%{_libdir}/lib[kt]deinit_kicker.so
%{_libdir}/libkickermain.so.*
%{_libdir}/libtaskbar.so.*
%{_libdir}/libtaskmanager.so.*
%{_libdir}/libkickoffsearch_interfaces.so.*
%{tde_appdir}/kcmkicker.desktop
%{_datadir}/applnk/.hidden/kicker_config_arrangement.desktop
%{_datadir}/applnk/.hidden/kicker_config_hiding.desktop
%{_datadir}/applnk/.hidden/kicker_config_menus.desktop
%{_datadir}/apps/clockapplet/pics/lcd.png
%{_datadir}/apps/kconf_update/kicker-3.1-properSizeSetting.pl
%{_datadir}/apps/kconf_update/kicker-3.5-kconfigXTize.pl
%{_datadir}/apps/kconf_update/kicker-3.5-taskbarEnums.pl
%{_datadir}/apps/kconf_update/kickerrc.upd
%{_datadir}/apps/kicker
%{_datadir}/apps/naughtyapplet/pics/naughty-happy.png
%{_datadir}/apps/naughtyapplet/pics/naughty-sad.png
%{_datadir}/autostart/panel.desktop
%{_datadir}/config.kcfg/kickerSettings.kcfg
%{_datadir}/config.kcfg/launcherapplet.kcfg
%{_datadir}/config.kcfg/pagersettings.kcfg
%{_datadir}/config.kcfg/taskbar.kcfg
%{_datadir}/icons/crystalsvg/*/apps/systemtray.png
%{_datadir}/icons/crystalsvg/*/apps/taskbar.png
%{_datadir}/icons/crystalsvg/*/apps/kbinaryclock.png
%{_datadir}/icons/crystalsvg/*/apps/kdisknav.png
%{_datadir}/icons/crystalsvg/*/apps/kicker.png
%{_datadir}/icons/crystalsvg/*/apps/panel.png
%{_datadir}/icons/crystalsvg/*/apps/runprocesscatcher.png
%{_datadir}/icons/crystalsvg/*/apps/window_list.png
%{_datadir}/icons/crystalsvg/*/apps/kbinaryclock.svgz
%{_datadir}/icons/crystalsvg/*/apps/systemtray.svgz
%{_datadir}/servicetypes/kickoffsearchplugin.desktop
%{tde_docdir}/HTML/en/kicker/

%post -n trinity-kicker
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%postun -n trinity-kicker
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

##########

%package -n trinity-kicker-devel
Summary:	Development files for kicker
Group:		Development/Libraries
Requires:	trinity-kicker = %{version}-%{release}

%description -n trinity-kicker-devel
%{summary}

%files -n trinity-kicker-devel
%{_includedir}/kickoff-search-plugin.h
%{_includedir}/kickoffsearchinterface.h
%{_libdir}/libkasbar.la
%{_libdir}/libkasbar.so
%{_libdir}/libkickermain.la
%{_libdir}/libkickermain.so
%{_libdir}/libkickoffsearch_interfaces.la
%{_libdir}/libkickoffsearch_interfaces.so
%{_libdir}/libtaskbar.la
%{_libdir}/libtaskbar.so
%{_libdir}/libtaskmanager.la
%{_libdir}/libtaskmanager.so

%post -n trinity-kicker-devel
/sbin/ldconfig || :

%postun -n trinity-kicker-devel
/sbin/ldconfig || :

##########

%package -n trinity-klipper
Summary:	clipboard utility for Trinity
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-klipper
klipper provides standard clipboard functions (cut and paste, history
saving) plus additional features, like the ability to offer actions to 
take dependent on the clipboard contents. For example, it can launch a 
web browser if the clipboard contains a URL.

%files -n trinity-klipper
%defattr(-,root,root,-)
%{_bindir}/klipper
%{_datadir}/config/klipperrc
%{tde_libdir}/klipper.la
%{tde_libdir}/klipper.so
%{tde_libdir}/klipper_panelapplet.la
%{tde_libdir}/klipper_panelapplet.so
%{_libdir}/lib[kt]deinit_klipper.la
%{_libdir}/lib[kt]deinit_klipper.so
%{tde_appdir}/klipper.desktop
%{_datadir}/apps/kconf_update/klipper-1-2.pl
%{_datadir}/apps/kconf_update/klipper-trinity1.sh
%{_datadir}/apps/kconf_update/klipperrc.upd
%{_datadir}/apps/kconf_update/klippershortcuts.upd
%{_datadir}/apps/kicker/applets/klipper.desktop
%{_datadir}/autostart/klipper.desktop
%{_datadir}/icons/hicolor/*/apps/klipper.*
%{tde_docdir}/HTML/en/klipper/

%post -n trinity-klipper
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%postun -n trinity-klipper
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

##########

%package -n trinity-kmenuedit
Summary:	menu editor for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-kmenuedit
The TDE menu editor allows you to make customisations to the KDE menu
structure.

%files -n trinity-kmenuedit
%defattr(-,root,root,-)
%{_bindir}/kcontroledit
%{_bindir}/kmenuedit
%{tde_libdir}/kcontroledit.la
%{tde_libdir}/kcontroledit.so
%{tde_libdir}/kmenuedit.la
%{tde_libdir}/kmenuedit.so
%{_libdir}/lib[kt]deinit_kcontroledit.la
%{_libdir}/lib[kt]deinit_kcontroledit.so
%{_libdir}/lib[kt]deinit_kmenuedit.la
%{_libdir}/lib[kt]deinit_kmenuedit.so
%{tde_appdir}/kmenuedit.desktop
%{_datadir}/applnk/System/kmenuedit.desktop
%{_datadir}/apps/kcontroledit/
%{_datadir}/apps/kmenuedit/
%{tde_docdir}/HTML/en/kmenuedit/

%post -n trinity-kmenuedit
update-desktop-database %{tde_appdir} 2> /dev/null || : 
/sbin/ldconfig || :

%postun -n trinity-kmenuedit
update-desktop-database %{tde_appdir} 2> /dev/null || : 
/sbin/ldconfig || :

##########

%package -n trinity-konqueror
Summary:	TDE's advanced file manager, web browser and document viewer
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}
Requires:	trinity-kcontrol = %{version}-%{release}
Requires:	%{name}-kio-plugins = %{version}-%{release}
Requires:	trinity-kdesktop = %{version}-%{release}
Requires:	trinity-kfind = %{version}-%{release}
Requires:	trinity-konqueror-nsplugins = %{version}-%{release}
Requires:	trinity-libkonq = %{version}-%{release}

%description -n trinity-konqueror
Konqueror is the file manager for the Trinity Desktop Environment.
It supports basic file management on local UNIX filesystems,
from simple cut/copy and paste operations to advanced remote
and local network file browsing.

It is also the canvas for all the latest TDE technology,
from KIO slaves (which provide mechanisms for file access) to
component embedding via the KParts object interface, and it
is one of the most customizable applications available.

Konqueror is an Open Source web browser with HTML4.0 compliance,
supporting Java applets, JavaScript, CSS1 and (partially) CSS2,
as well as Netscape plugins (for example, Flash or RealVideo plugins).

It is a universal viewing application, capable of embedding
read-only viewing components in itself to view documents without
ever launching another application.

%files -n trinity-konqueror
%defattr(-,root,root,-)
%{_datadir}/config/konqsidebartng.rc
%{_bindir}/kbookmarkmerger
%{_bindir}/keditbookmarks
%{_bindir}/kfmclient
%{_bindir}/konqueror
%{tde_libdir}/kcm_history.la
%{tde_libdir}/kcm_history.so
%{tde_libdir}/kded_konqy_preloader.la
%{tde_libdir}/kded_konqy_preloader.so
%{tde_libdir}/keditbookmarks.la
%{tde_libdir}/keditbookmarks.so
%{tde_libdir}/kfmclient.la
%{tde_libdir}/kfmclient.so
%{tde_libdir}/konq_aboutpage.la
%{tde_libdir}/konq_aboutpage.so
%{tde_libdir}/konq_iconview.la
%{tde_libdir}/konq_iconview.so
%{tde_libdir}/konq_listview.la
%{tde_libdir}/konq_listview.so
%{tde_libdir}/konq_remoteencoding.la
%{tde_libdir}/konq_remoteencoding.so
%{tde_libdir}/konq_shellcmdplugin.la
%{tde_libdir}/konq_shellcmdplugin.so
%{tde_libdir}/konq_sidebar.la
%{tde_libdir}/konq_sidebar.so
%{tde_libdir}/konq_sidebartree_bookmarks.la
%{tde_libdir}/konq_sidebartree_bookmarks.so
%{tde_libdir}/konq_sidebartree_dirtree.la
%{tde_libdir}/konq_sidebartree_dirtree.so
%{tde_libdir}/konq_sidebartree_history.la
%{tde_libdir}/konq_sidebartree_history.so
%{tde_libdir}/konqsidebar_tree.la
%{tde_libdir}/konqsidebar_tree.so
%{tde_libdir}/konqsidebar_web.la
%{tde_libdir}/konqsidebar_web.so
%{tde_libdir}/konqueror.la
%{tde_libdir}/konqueror.so
%{tde_libdir}/libkhtmlkttsdplugin.la
%{tde_libdir}/libkhtmlkttsdplugin.so
%{_libdir}/lib[kt]deinit_keditbookmarks.la
%{_libdir}/lib[kt]deinit_keditbookmarks.so
%{_libdir}/lib[kt]deinit_kfmclient.la
%{_libdir}/lib[kt]deinit_kfmclient.so
%{_libdir}/lib[kt]deinit_konqueror.la
%{_libdir}/lib[kt]deinit_konqueror.so
%{_libdir}/libkonqsidebarplugin.so.*
%{tde_appdir}/Home.desktop
%{tde_appdir}/kcmhistory.desktop
%{tde_appdir}/kfmclient.desktop
%{tde_appdir}/kfmclient_dir.desktop
%{tde_appdir}/kfmclient_html.desktop
%{tde_appdir}/kfmclient_war.desktop
%{tde_appdir}/khtml_filter.desktop
%{tde_appdir}/konqbrowser.desktop
%{tde_appdir}/konquerorsu.desktop
%{_datadir}/applnk/.hidden/konqfilemgr.desktop
%{_datadir}/applnk/Internet/keditbookmarks.desktop
%{_datadir}/applnk/konqueror.desktop
%{_datadir}/apps/kconf_update/kfmclient_3_2.upd
%{_datadir}/apps/kconf_update/kfmclient_3_2_update.sh
%{_datadir}/apps/kconf_update/konqsidebartng.upd
%{_datadir}/apps/kconf_update/move_konqsidebartng_entries.sh
%{_datadir}/apps/keditbookmarks/keditbookmarks-genui.rc
%{_datadir}/apps/keditbookmarks/keditbookmarksui.rc
%{_datadir}/apps/khtml/kpartplugins/khtmlkttsd.desktop
%{_datadir}/apps/khtml/kpartplugins/khtmlkttsd.rc
%{_datadir}/apps/konqiconview/
%{_datadir}/apps/konqlistview/
%exclude %{_datadir}/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/apps/konqsidebartng/
%{_datadir}/apps/konqueror/about/
%{_datadir}/apps/konqueror/icons/
%{_datadir}/apps/konqueror/konq-simplebrowser.rc
%{_datadir}/apps/konqueror/konqueror.rc
%{_datadir}/apps/konqueror/pics/indicator_connect.png
%{_datadir}/apps/konqueror/pics/indicator_empty.png
%{_datadir}/apps/konqueror/pics/indicator_noconnect.png
%{_datadir}/apps/konqueror/pics/indicator_viewactive.png
%{_datadir}/apps/konqueror/profiles/
%exclude %{_datadir}/apps/konqueror/servicemenus/kdesktopSetAsBackground.desktop
%exclude %{_datadir}/apps/konqueror/servicemenus/konsolehere.desktop
%exclude %{_datadir}/apps/konqueror/servicemenus/installfont.desktop
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase
%{_datadir}/apps/konqueror/tiles/*.png
%{_datadir}/autostart/konqy_preload.desktop
%{_datadir}/config.kcfg/keditbookmarks.kcfg
%{_datadir}/config.kcfg/konq_listview.kcfg
%{_datadir}/config.kcfg/konqueror.kcfg
%{_datadir}/icons/crystalsvg/*/apps/keditbookmarks.png
%{_datadir}/icons/crystalsvg/*/apps/kfm_home.svgz
%{_datadir}/icons/hicolor/*/apps/kfm.png
%{_datadir}/icons/hicolor/*/apps/konqueror.*
%{_datadir}/services/kded/konqy_preloader.desktop
%{_datadir}/services/konq_*.desktop
%{_datadir}/servicetypes/konqaboutpage.desktop
%{tde_docdir}/HTML/en/konqueror/

%post -n trinity-konqueror
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :
alternatives --install \
  %{_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop \
  media_safelyremove.desktop_konqueror \
  %{_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase \
  10

%postun -n trinity-konqueror
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :
if [ $1 -eq 0 ]; then
  alternatives --remove \
    media_safelyremove.desktop_konqueror
    %{_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase
fi

##########

%package -n trinity-konqueror-devel
Summary:	Development files for konqueror
Group:		Development/Libraries
Requires:	trinity-konqueror = %{version}-%{release}

%description -n trinity-konqueror-devel
%{summary}

%files -n trinity-konqueror-devel
%{_includedir}/konqsidebarplugin.h
%{_includedir}/KonquerorIface.h
%{_libdir}/libkonqsidebarplugin.la
%{_libdir}/libkonqsidebarplugin.so

%post -n trinity-konqueror-devel
/sbin/ldconfig || :

%postun -n trinity-konqueror-devel
/sbin/ldconfig || :

##########

%package -n trinity-konqueror-nsplugins
Summary:	Netscape plugin support for Konqueror
Group:		Applications/Utilities
Requires:	trinity-konqueror = %{version}-%{release}

%description -n trinity-konqueror-nsplugins
This package includes support for Netscape plugins in Konqueror.

%files -n trinity-konqueror-nsplugins
%defattr(-,root,root,-)
%{_bindir}/nspluginscan
%{_bindir}/nspluginviewer
%{tde_libdir}/kcm_nsplugins.la
%{tde_libdir}/kcm_nsplugins.so
%{tde_libdir}/libnsplugin.la
%{tde_libdir}/libnsplugin.so
%{tde_appdir}/khtml_plugins.desktop
%{_datadir}/apps/plugin/nspluginpart.rc

%post -n trinity-konqueror-nsplugins
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun -n trinity-konqueror-nsplugins
update-desktop-database %{tde_appdir} 2> /dev/null || : 

##########

%package -n trinity-konsole
Summary:	X terminal emulator for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-konsole
Konsole is an X terminal emulation which provides a command-line interface
(CLI) while using the graphical K Desktop Environment. Konsole helps to
better organize user's desktop by containing multiple sessions in a single
window (a less cluttered desktop).

Its advanced features include a simple configuration and the ability to use
multiple terminal shells in a single window

Using Konsole, a user can open:
* Linux console sessions
* Midnight Commander file manager sessions
* Shell sessions
* Root consoles sessions

%files -n trinity-konsole
%defattr(-,root,root,-)
%{_bindir}/konsole
%{tde_libdir}/kcm_konsole.la
%{tde_libdir}/kcm_konsole.so
%{tde_libdir}/kded_kwrited.la
%{tde_libdir}/kded_kwrited.so
%{tde_libdir}/konsole.la
%{tde_libdir}/konsole.so
%{tde_libdir}/libkonsolepart.la
%{tde_libdir}/libkonsolepart.so
%{_libdir}/lib[kt]deinit_konsole.la
%{_libdir}/lib[kt]deinit_konsole.so
%{tde_appdir}/konsole.desktop
%{tde_appdir}/konsolesu.desktop
%{_datadir}/applnk/.hidden/kcmkonsole.desktop
%{_datadir}/apps/kconf_update/konsole.upd
%{_datadir}/apps/kconf_update/schemaStrip.pl
%{_datadir}/apps/konqueror/servicemenus/konsolehere.desktop
%{_datadir}/apps/konsole/
%{_datadir}/icons/hicolor/*/apps/konsole.*
%{_datadir}/mimelnk/application/x-konsole.desktop
%{_datadir}/services/kded/kwrited.desktop
%{_datadir}/services/konsolepart.desktop
%{_datadir}/services/konsole-script.desktop
%{_datadir}/services/kwrited.desktop
%{_datadir}/servicetypes/terminalemulator.desktop
%exclude %{tde_docdir}/HTML/en/kcontrol/kcmkonsole/
%{tde_docdir}/HTML/en/konsole/

%post -n trinity-konsole
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%postun -n trinity-konsole
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

##########

%package -n trinity-kpager
Summary:	desktop pager for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-kpager
This package contains TDE's desktop pager, which displays your virtual
desktops iconically in a window, along with icons of any running
applications. It is used to switch between applications or desktops.

%files -n trinity-kpager
%defattr(-,root,root,-)
%{_bindir}/kpager
%{tde_appdir}/kpager.desktop
%{_datadir}/applnk/Utilities/kpager.desktop
%{_datadir}/icons/hicolor/*/apps/kpager.png
%{tde_docdir}/HTML/en/kpager/

%post -n trinity-kpager
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

%postun -n trinity-kpager
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-kpersonalizer
Summary:	installation personalizer for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-kpersonalizer
TDE Personalizer is the application that configures the TDE desktop for you.
It's a very useful wizard that allows you to quickly change the TDE desktop to
suit your own needs. When you run TDE for the first time, KPersonalizer is
automatically started. KPersonalizer can also be called later.

%files -n trinity-kpersonalizer
%defattr(-,root,root,-)
%{_bindir}/kpersonalizer
%{tde_appdir}/kpersonalizer.desktop
%{_datadir}/applnk/System/kpersonalizer.desktop
%{_datadir}/apps/kpersonalizer/
%{_datadir}/icons/crystalsvg/*/apps/kpersonalizer.png

%post -n trinity-kpersonalizer
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

%postun -n trinity-kpersonalizer
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-ksmserver
Summary:	session manager for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}
Requires:	trinity-twin = %{version}-%{release}

%description -n trinity-ksmserver
This package contains the KDE session manager. It is responsible for
restoring your TDE session on login. It is also needed to properly
start a KDE session. It registers KDE with X display managers, and
provides the 'starttde' command, for starting an X session with KDE
from the console.

If you are running TDE for the first time for a certain user,
kpersonalizer is used to help with setup. If it is not present,
KDE will start, but many good defaults will not be set.

%files -n trinity-ksmserver
%defattr(-,root,root,-)
%{_bindir}/ksmserver
%{_bindir}/start[kt]de
%{tde_libdir}/ksmserver.la
%{tde_libdir}/ksmserver.so
%{_libdir}/lib[kt]deinit_ksmserver.la
%{_libdir}/lib[kt]deinit_ksmserver.so
%{_datadir}/apps/kconf_update/ksmserver.upd
%{_datadir}/apps/kconf_update/move_session_config.sh
%{_datadir}/apps/ksmserver/pics/shutdownkonq.png

# Remove conflicts with redhat-menus
%if "%{?_prefix}" != "/usr"
%{_bindir}/plasma-desktop
%endif

##########

%package -n trinity-ksplash
Summary:	the TDE splash screen
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-ksplash
This package includes the TDE Splash screen, which is seen when
a TDE session is launched.

%files -n trinity-ksplash
%defattr(-,root,root,-)
%{_bindir}/ksplash
%{_bindir}/ksplashsimple
%{tde_libdir}/kcm_ksplashthemes.la
%{tde_libdir}/kcm_ksplashthemes.so
%{tde_libdir}/ksplashdefault.la
%{tde_libdir}/ksplashdefault.so
%{tde_libdir}/ksplashunified.la
%{tde_libdir}/ksplashunified.so
%{tde_libdir}/ksplashredmond.la
%{tde_libdir}/ksplashredmond.so
%{tde_libdir}/ksplashstandard.la
%{tde_libdir}/ksplashstandard.so
%{_libdir}/libksplashthemes.so.*
%{tde_appdir}/ksplashthememgr.desktop
%{_datadir}/apps/ksplash
%{_datadir}/services/ksplashdefault.desktop
%{_datadir}/services/ksplash.desktop
%{_datadir}/services/ksplashunified.desktop
%{_datadir}/services/ksplashredmond.desktop
%{_datadir}/services/ksplashstandard.desktop
%{_datadir}/servicetypes/ksplashplugins.desktop
%{tde_docdir}/HTML/en/ksplashml/

%post -n trinity-ksplash
update-desktop-database %{tde_appdir} 2> /dev/null || : 
/sbin/ldconfig || :

%postun -n trinity-ksplash
update-desktop-database %{tde_appdir} 2> /dev/null || : 
/sbin/ldconfig || :

##########

%package -n trinity-ksplash-devel
Summary:	Development files for ksplash
Group:		Development/Libraries
Requires:	trinity-ksplash = %{version}-%{release}

%description -n trinity-ksplash-devel
%{summary}

%files -n trinity-ksplash-devel
%{_includedir}/ksplash/*
%{_libdir}/libksplashthemes.la
%{_libdir}/libksplashthemes.so

%post -n trinity-ksplash-devel
/sbin/ldconfig || :

%postun -n trinity-ksplash-devel
/sbin/ldconfig || :

##########

%package -n trinity-ksysguard
Summary:	system guard for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}
Requires:	trinity-ksysguardd = %{version}-%{release}

%description -n trinity-ksysguard
TDE System Guard allows you to monitor various statistics about your
computer.

%files -n trinity-ksysguard
%defattr(-,root,root,-)
%{_bindir}/kpm
%{_bindir}/ksysguard
%{tde_libdir}/sysguard_panelapplet.la
%{tde_libdir}/sysguard_panelapplet.so
%{_libdir}/libksgrd.so.*
%{tde_appdir}/ksysguard.desktop
%{_datadir}/apps/kicker/applets/ksysguardapplet.desktop
%{_datadir}/apps/ksysguard/
%{_datadir}/icons/crystalsvg/*/apps/ksysguard.png
%{_datadir}/mimelnk/application/x-ksysguard.desktop
%{tde_docdir}/HTML/en/ksysguard/

%post -n trinity-ksysguard
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%postun -n trinity-ksysguard
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

##########

%package -n trinity-ksysguard-devel
Summary:	Development files for ksysguard
Group:		Development/Libraries
Requires:	trinity-ksysguard = %{version}-%{release}

%description -n trinity-ksysguard-devel
%{summary}

%files -n trinity-ksysguard-devel
%{_includedir}/ksgrd/*
%{_libdir}/libksgrd.la
%{_libdir}/libksgrd.so

%post -n trinity-ksysguard-devel
/sbin/ldconfig || :

%postun -n trinity-ksysguard-devel
/sbin/ldconfig || :

##########

%package -n trinity-ksysguardd
Summary:	system guard daemon for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-ksysguardd
TDE System Guard Daemon is the daemon part of ksysguard. The daemon can
be installed on a remote machine to enable ksysguard on another machine
to monitor it through the daemon running there.

%files -n trinity-ksysguardd
%defattr(-,root,root,-)
%{_bindir}/ksysguardd
%config(noreplace) %{_sysconfdir}/ksysguarddrc.tde

%post -n trinity-ksysguardd
# Dirty hack to install '/etc/ksysguarddrc' alongside with KDE4
[ -r "%{_sysconfdir}/ksysguarddrc" ] || cp -f "%{_sysconfdir}/ksysguarddrc.tde" "%{_sysconfdir}/ksysguarddrc"

##########

%package -n trinity-ktip
Summary:	useful tips for TDE
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-ktip
ktip provides many useful tips on using KDE when you log in.

%files -n trinity-ktip
%defattr(-,root,root,-)
%{_bindir}/ktip
%{tde_appdir}/ktip.desktop
%{_datadir}/applnk/Toys/ktip.desktop
%{_datadir}/apps/kdewizard/pics/wizard_small.png
%{_datadir}/apps/kdewizard/tips/
%{_datadir}/autostart/ktip.desktop
%{_datadir}/icons/hicolor/*/apps/ktip.*

%post -n trinity-ktip
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

%postun -n trinity-ktip
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-twin
Summary:	the TDE window manager
Group:		Applications/Utilities
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-twin
This package contains the default X window manager for KDE.

%files -n trinity-twin
%defattr(-,root,root,-)
%{_bindir}/kompmgr
%{_bindir}/[kt]win
%{_bindir}/[kt]win_killer_helper
#%{_bindir}/[kt]win_resumer_helper
%{_bindir}/[kt]win_rules_dialog
%{_libdir}/kconf_update_bin/[kt]win_update_default_rules
%{_libdir}/kconf_update_bin/[kt]win_update_window_settings
%{tde_libdir}/kcm_[kt]win*.la
%{tde_libdir}/kcm_[kt]win*.so
%{tde_libdir}/[kt]win*.la
%{tde_libdir}/[kt]win*.so
%{_libdir}/lib[kt]decorations.so.*
%{_libdir}/lib[kt]deinit_[kt]win_rules_dialog.la
%{_libdir}/lib[kt]deinit_[kt]win_rules_dialog.so
%{_libdir}/lib[kt]deinit_[kt]win.la
%{_libdir}/lib[kt]deinit_[kt]win.so
%{tde_appdir}/showdesktop.desktop
%{tde_appdir}/[kt]windecoration.desktop
%{tde_appdir}/[kt]winoptions.desktop
%{tde_appdir}/[kt]winrules.desktop
%{_datadir}/applnk/.hidden/[kt]winactions.desktop
%{_datadir}/applnk/.hidden/[kt]winadvanced.desktop
%{_datadir}/applnk/.hidden/[kt]winfocus.desktop
%{_datadir}/applnk/.hidden/[kt]winmoving.desktop
%{_datadir}/applnk/.hidden/[kt]wintranslucency.desktop
%{_datadir}/apps/kconf_update/[kt]win3_plugin.pl
%{_datadir}/apps/kconf_update/[kt]win3_plugin.upd
%{_datadir}/apps/kconf_update/[kt]win_focus1.sh
%{_datadir}/apps/kconf_update/[kt]win_focus1.upd
%{_datadir}/apps/kconf_update/[kt]win_focus2.sh
%{_datadir}/apps/kconf_update/[kt]win_focus2.upd
%{_datadir}/apps/kconf_update/[kt]win_fsp_workarounds_1.upd
%{_datadir}/apps/kconf_update/[kt]winiconify.upd
%{_datadir}/apps/kconf_update/[kt]winsticky.upd
%{_datadir}/apps/kconf_update/[kt]win.upd
%{_datadir}/apps/kconf_update/[kt]winupdatewindowsettings.upd
%{_datadir}/apps/kconf_update/pluginlibFix.pl
%{_datadir}/apps/[kt]win/
%{_datadir}/config.kcfg/[kt]win.kcfg
%{_datadir}/icons/crystalsvg/*/apps/[kt]win.png
%{tde_docdir}/HTML/en/kompmgr/

%post -n trinity-twin
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%postun -n trinity-twin
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

##########

%package -n trinity-twin-devel
Summary:	Development files for twin
Group:		Development/Libraries
Requires:	trinity-twin = %{version}-%{release}

%description -n trinity-twin-devel
%{summary}

%files -n trinity-twin-devel
%{_includedir}/[kt]win/
%{_includedir}/kcommondecoration.h
%{_includedir}/kdecoration.h
%{_includedir}/kdecoration_p.h
%{_includedir}/kdecoration_plugins_p.h
%{_includedir}/kdecorationfactory.h
%{_includedir}/KWinInterface.h
%{_libdir}/libkdecorations.la
%{_libdir}/libkdecorations.so

%post -n trinity-twin-devel
/sbin/ldconfig || :

%postun -n trinity-twin-devel
/sbin/ldconfig || :

##########

%package -n trinity-libkonq
Summary:	core libraries for Konqueror
Group:		Environment/Libraries

%description -n trinity-libkonq
These libraries are used by several TDE applications, most notably
Konqueror and the kdesktop package.

%files -n trinity-libkonq
%defattr(-,root,root,-)
%{tde_libdir}/kded_favicons.la
%{tde_libdir}/kded_favicons.so
%{tde_libdir}/konq_sound.la
%{tde_libdir}/konq_sound.so
%{_libdir}/libkonq.so.*
%{_datadir}/apps/kbookmark/directory_bookmarkbar.desktop
%{_datadir}/apps/kconf_update/favicons.upd
%{_datadir}/apps/kconf_update/move_favicons.sh
%{_datadir}/apps/konqueror/pics/arrow_bottomleft.png
%{_datadir}/apps/konqueror/pics/arrow_bottomright.png
%{_datadir}/apps/konqueror/pics/arrow_topleft.png
%{_datadir}/apps/konqueror/pics/arrow_topright.png
%{_datadir}/apps/konqueror/pics/thumbnailfont_7x4.png
%{_datadir}/services/kded/favicons.desktop
%{_datadir}/servicetypes/konqpopupmenuplugin.desktop

%post -n trinity-libkonq
/sbin/ldconfig || :

%postun -n trinity-libkonq
/sbin/ldconfig || :

##########

%package libtqt3-integration
Summary:	Integration library between TQt3 and TDE
Group:		Environment/Libraries

Obsoletes:	tdebase-libtqt3-integration < %{version}-%{release}
Provides:	tdebase-libtqt3-integration = %{version}-%{release}

%description libtqt3-integration
These libraries allow you to use TDE dialogs in native TQt3 applications.

%files libtqt3-integration
%defattr(-,root,root,-)
%{tde_libdir}/plugins/integration/libqtkde.la
%{tde_libdir}/plugins/integration/libqtkde.so
%{tde_libdir}/plugins/integration/libqtkde.so.*
%{tde_libdir}/kded_kdeintegration.la
%{tde_libdir}/kded_kdeintegration.so
%{_datadir}/services/kded/kdeintegration.desktop

##########

%package -n trinity-libkonq-devel
Summary:	development files for Konqueror's core libraries
Group:		Development/Libraries
Requires:	trinity-libkonq = %{version}-%{release}

%description -n trinity-libkonq-devel
This package contains headers and other development files for the core
Konqueror libraries.

%files -n trinity-libkonq-devel
%defattr(-,root,root,-)
%{_includedir}/kfileivi.h
%{_includedir}/kivdirectoryoverlay.h
%{_includedir}/knewmenu.h
%{_includedir}/konqbookmarkmanager.h
%{_includedir}/konq_*.h
%{_includedir}/libkonq_export.h
%{_libdir}/libkonq.la
%{_libdir}/libkonq.so

%post -n trinity-libkonq-devel
/sbin/ldconfig || :

%postun -n trinity-libkonq-devel
/sbin/ldconfig || :

##########

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
%patch47 -p0
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1

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

# Symlinks 'usb.ids'
%__rm -f "%{?buildroot}%{_datadir}/apps/usb.ids"
%__ln_s -f "/usr/share/hwdata/usb.ids" "%{?buildroot}%{_datadir}/apps/usb.ids"

# Makes 'media_safelyremove.desktop' an alternative
%__mv -f %{buildroot}%{_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop %{buildroot}%{_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase
%__ln_s /etc/alternatives/media_safelyremove.desktop_tdebase %{buildroot}%{_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop


%clean
%__rm -rf %{?buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING-DOCS README README.pam


%changelog
* Sun Jul 08 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-25
- Fix menu crash with disabled search field [Bug #1081] [Commit #0afb2d8a]
- Makes 'media_safelyremove.desktop' an alternative

* Sun Jul 01 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-24
- Renames 'tdebase' to 'trinity-tdebase'
- Update default konqueror maximum image preview size to 10MB. [Commit #03e19305]

* Sun Jun 17 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-23
- Renames 'trinity-kdebase' to 'tdebase'
- Split into several packages

* Sat May 05 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-22
- Adds panel to choose default mounting options for removable storage [Bug #986]
- Add the ability to reorder documents in kate [Commit #46a657f7]
- Add drag and drop to kate file list in manual mode [Commit #b0fa10df]
- Disable keyboard shortcuts for file location moving, as they did not work properly 
  and have very little practical use [Commit #9a948c1a]
- Fix KHTML smooth scrolling control center option [Bug #1001] [Commit #b45b4bd7]
- Fix fancy logout not allowing interaction with save dialogs [Bug #922]
  Fix desktop wallpaper export failing when triggered by krootbacking or ksmserver and konsole or 
  kdesktop_lock not previously loaded [Commit #d2f8fca9]

* Mon Apr 30 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-21
- Commit the rest of 8d521d0b, not merged due to GIT glitch [Commit #49526413]

* Fri Apr 27 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-20
- Fix sftp when nonstandard port is specified in ssh config [Bug #897]
- Start minimal dcop system to support twin in tdm [Commit #66a19439]
- Update lock process to engage the lock in near real time [Commit #8d521d0b]
- Fix desktop lock failure due to race condition within signal handler between qt and xcb [Commit #67a3a8f3]
- Temporary fix for a probable race condition on some systems. [Bug #760] [Commit #d41f5217]

* Tue Apr 24 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-19
- Build for Fedora 17
- Fix compilation with GCC 4.7 [Bug #958]

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
