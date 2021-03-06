#
# spec file for package tdebase (version 3.5.13-SRU)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 1
%define tde_version 3.5.13.2
%define tde_pkg tdebase
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define tdm kdm
%define tdm_datadir %{tde_datadir}/apps/%{tdm}
%define starttde startkde

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif


Name:			trinity-%{tde_pkg}
Version:		%{tde_version}
Release:		%{?!preversion:5}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:		Trinity Base Programs
Group:			System/GUI/Other
URL:			http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:		GPL-2.0+
%else
License:		GPLv2+
%endif

#Vendor:			Trinity Desktop
#Packager:		Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Source1:		trinity-tdebase-rpmlintrc

# Pam configuration files for RHEL / Fedora
%if 0%{?suse_version} == 0
Source2:		pamd.kdm-trinity%{?dist}
Source3:		pamd.kdm-trinity-np%{?dist}
Source4:		pamd.kcheckpass-trinity%{?dist}
Source5:		pamd.kscreensaver-trinity%{?dist}
%endif

# openSUSE: configuration file for TDM
Source6:		suse-displaymanagers-tdm

# Fedora 18: use SYSTEMD for TDM startup
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
Source7:		tdm.service%{?dist}
%endif

# openSUSE 11.4: overwrite distribution-provided '/etc/init.d/xdm' !!!
%if 0%{?suse_version} == 1140
Source7:		xdm.oss114
%endif

# Fedora >= 17: special selinux policy required for TDM
#  If login through TDM takes ages, then look at '/var/log/audit/audit.log'.
#  Locate the line containing 'USER_AVC' and dbus stuff.
#  Put this line into a temporary file, then (e.g for Fedora 17):
#   audit2allow -i /tmp/file -m tdm.fc17 >tdm.fc17.te
#   audit2allow -i /tmp/file -M tdm.fc17

%if 0%{?fedora} >= 17 || 0%{?rhel} >= 6
%define with_selinux_policy 1
Source8:	tdm%{?dist}.pp
%endif

%if 0%{?mgaversion} >= 3
Source9:	mgabutton.svg
%endif

%{?tde_patch:Patch1:			%{tde_pkg}-%{tde_version}.patch}

Obsoletes:	trinity-kdebase < %{version}-%{release}
Provides:	trinity-kdebase = %{version}-%{release}
Obsoletes:	trinity-kdebase-libs < %{version}-%{release}
Provides:	trinity-kdebase-libs = %{version}-%{release}
Obsoletes:	trinity-kdebase-extras < %{version}-%{release}
Provides:	trinity-kdebase-extras = %{version}-%{release}
Obsoletes:	tdebase < %{version}-%{release}
Provides:	tdebase = %{version}-%{release}

# for set_permissions macro
%if 0%{?suse_version}
PreReq: permissions
%endif

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

### Distribution-specific settings ###

# Fedora 15 Theme: "Lovelock"
%if 0%{?fedora} == 15
Requires:	lovelock-backgrounds-single
%define tde_bg /usr/share/backgrounds/lovelock/default/standard/lovelock.png
%define tde_starticon /usr/share/icons/hicolor/96x96/apps/fedora-logo-icon.png

Requires:	fedora-release-notes
%define tde_aboutlabel Fedora 15
%define tde_aboutpage /usr/share/doc/HTML/fedora-release-notes/index.html
%endif

# Fedora 16 Theme: "Verne"
%if 0%{?fedora} == 16
Requires:	verne-backgrounds-single
%define tde_bg /usr/share/backgrounds/verne/default/standard/verne.png
%define tde_starticon /usr/share/icons/hicolor/96x96/apps/fedora-logo-icon.png

Requires:	fedora-release-notes
%define tde_aboutlabel Fedora 16
%define tde_aboutpage /usr/share/doc/HTML/fedora-release-notes/index.html
%endif

# Fedora 17 Theme: "Beefy Miracle"
%if 0%{?fedora} == 17
Requires:	beefy-miracle-backgrounds-single
%define tde_bg /usr/share/backgrounds/beefy-miracle/default/standard/beefy-miracle.png
%define tde_starticon /usr/share/icons/hicolor/96x96/apps/fedora-logo-icon.png

Requires:	fedora-release-notes
%define tde_aboutlabel Fedora 17
%define tde_aboutpage /usr/share/doc/HTML/fedora-release-notes/index.html
%endif

# Fedora 18 Theme: "Spherical Cow"
%if 0%{?fedora} == 18
Requires:	spherical-cow-backgrounds-single
%define tde_bg /usr/share/backgrounds/spherical-cow/default/standard/spherical-cow.png
Requires:	fedora-logos
%define tde_starticon /usr/share/icons/hicolor/96x96/apps/fedora-logo-icon.png

Requires:	fedora-release-notes
%define tde_aboutlabel Fedora 18
%define tde_aboutpage /usr/share/doc/HTML/fedora-release-notes/index.html
%endif

# Fedora 19 Theme: "Schroedinger's cat"
%if 0%{?fedora} == 19
Requires:	schroedinger-cat-backgrounds-base
%define tde_bg /usr/share/backgrounds/schroedinger-cat/default/standard/schroedinger-cat.jpg
Requires:	fedora-logos
%define tde_starticon /usr/share/icons/hicolor/96x96/apps/fedora-logo-icon.png

Requires:	fedora-release-notes
%define tde_aboutlabel Fedora 19
%define tde_aboutpage /usr/share/doc/fedora-release-notes-19/index.html
%endif

# Fedora 20 Theme: "Heisenbug"
%if 0%{?fedora} == 20
Requires:	heisenbug-backgrounds-base
%define tde_bg /usr/share/backgrounds/heisenbug/default/standard/heisenbug.png
Requires:	fedora-logos
%define tde_starticon /usr/share/icons/hicolor/96x96/apps/fedora-logo-icon.png

Requires:	fedora-release-notes
%define tde_aboutlabel Fedora 20
%define tde_aboutpage /usr/share/doc/fedora-release-notes/index.html
%endif

# RHEL 4 Theme
%if 0%{?rhel} == 4
Requires:	desktop-backgrounds-basic
%define tde_bg /usr/share/backgrounds/images/default.png
Requires:	redhat-logos
%define tde_starticon /usr/share/pixmaps/redhat/rpmlogo-64.xpm

Requires:	indexhtml
%define tde_aboutlabel Enterprise Linux 4
%define tde_aboutpage /usr/share/doc/HTML/index.html
%endif

# RHEL 5 Theme
%if 0%{?rhel} == 5
Requires:	desktop-backgrounds-basic
%define tde_bg /usr/share/backgrounds/images/default.jpg
%define tde_starticon /usr/share/pixmaps/redhat-starthere.png

Requires:	indexhtml
%define tde_aboutlabel Enterprise Linux 5
%define tde_aboutpage /usr/share/doc/HTML/index.html
%endif

# RHEL 6 Theme
%if 0%{?rhel} == 6
Requires:	redhat-logos
%define tde_bg /usr/share/backgrounds/default.png
%define tde_starticon /usr/share/icons/hicolor/96x96/apps/system-logo-icon.png

Requires:	redhat-indexhtml
%define tde_aboutlabel Enterprise Linux 6
%define tde_aboutpage /usr/share/doc/HTML/index.html
%endif

# RHEL 7 Theme
%if 0%{?rhel} == 7
Requires:	redhat-logos
%define tde_bg /usr/share/backgrounds/day.jpg
%define tde_starticon /usr/share/icons/hicolor/96x96/apps/system-logo-icon.png

Requires:	redhat-indexhtml
%define tde_aboutlabel Enterprise Linux 7
%define tde_aboutpage /usr/share/doc/HTML/index.html
%endif

# Mageia 2 Theme
%if 0%{?mgaversion} == 2
Requires:	mageia-theme-Default
%define tde_bg /usr/share/mga/backgrounds/default.jpg
%define tde_starticon /usr/share/icons/hicolor/scalable/apps/mageia-menu.svg

Requires:	indexhtml
%define tde_aboutlabel Mageia 2
%define tde_aboutpage /usr/share/mga/about/index.html
%endif

# Mageia 3 Theme
%if 0%{?mgaversion} == 3
Requires:	mageia-theme-Default
%define tde_bg /usr/share/mga/backgrounds/default.jpg
%define tde_starticon %{tde_datadir}/oxygen/scalable/mgabutton.svg

Requires:	indexhtml
%define tde_aboutlabel Mageia 3
%define tde_aboutpage /usr/share/mga/about/index.html
%endif

# Mageia 4 Theme
%if 0%{?mgaversion} == 4
Requires:	mageia-theme-Default
%define tde_bg /usr/share/mga/backgrounds/default.jpg
%define tde_starticon %{tde_datadir}/oxygen/scalable/mgabutton.svg

Requires:	indexhtml
%define tde_aboutlabel Mageia 4
%define tde_aboutpage /usr/share/mga/about/index.html
%endif

# Mandriva 2011 Theme: "rosa"
%if "%{distribution}" == "Mandriva Linux" && "%{?mdkversion}" == "201100"
Requires:	mandriva-theme
%define tde_bg /usr/share/mdk/backgrounds/default.jpg
%define tde_starticon /usr/share/icons/mandriva.png

Requires:	indexhtml
%define tde_aboutlabel Mandriva 2011
%define tde_aboutpage /usr/share/mdk/about/index.html
%endif

# PCLINUXOS
%if 0%{?pclinuxos}
Requires:	desktop-common-data
%define tde_starticon /usr/share/icons/pclinuxos.png

Requires:	indexhtml
%define tde_aboutlabel PCLinuxOS
%define tde_aboutpage /usr/share/mdk/about/index.html
%endif

# OpenSuse 11.4 Theme
%if "%{?suse_version}" == "1140"
Requires:	hicolor-icon-theme-branding = 11.4
%define tde_starticon /usr/share/icons/hicolor/scalable/apps/distributor.svg

Requires:	opensuse-manuals_en
%define tde_aboutlabel OpenSuse 11.4
%define tde_aboutpage /usr/share/doc/manual/opensuse-manuals_en/manual/book.opensuse.startup.html
%endif

# OpenSuse 12.2 Theme
%if "%{?suse_version}" == "1220"
Requires:	wallpaper-branding = 12.2
%define tde_bg /usr/share/wallpapers/openSUSEdefault/contents/images/1600x1200.jpg
Requires:	hicolor-icon-theme-branding = 12.2
%define tde_starticon /usr/share/icons/hicolor/scalable/apps/distributor.svg

Requires:	opensuse-manuals_en
%define tde_aboutlabel OpenSuse 12.2
%define tde_aboutpage /usr/share/doc/manual/opensuse-manuals_en/book.opensuse.startup.html
%endif

# OpenSuse 12.3 Theme
%if "%{?suse_version}" == "1230"
Requires:	wallpaper-branding = 12.3
%define tde_bg /usr/share/wallpapers/openSUSEdefault/contents/images/1600x1200.jpg
Requires:	hicolor-icon-theme-branding
%define tde_starticon /usr/share/icons/hicolor/scalable/apps/distributor.svg

Requires:	opensuse-manuals_en
%define tde_aboutlabel OpenSuse 12.3
%define tde_aboutpage /usr/share/doc/manual/opensuse-manuals_en/book.opensuse.startup.html
%endif

# OpenSuse 13.1 Theme
%if "%{?suse_version}" == "1310"
Requires:	wallpaper-branding = 13.1
%define tde_bg /usr/share/wallpapers/openSUSEdefault/contents/images/1600x1200.jpg
Requires:	hicolor-icon-theme-branding = 13.1
%define tde_starticon /usr/share/icons/hicolor/scalable/apps/distributor.svg

Requires:	opensuse-manuals_en
%define tde_aboutlabel OpenSuse 13.1
%define tde_aboutpage /usr/share/do%endif
%endif

# OpenSuse 13.2 Theme
%if "%{?suse_version}" == "1320"
Requires:	wallpaper-branding = 13.2
%define tde_bg /usr/share/wallpapers/openSUSEdefault/contents/images/1600x1200.jpg
Requires:	hicolor-icon-theme-branding
%define tde_starticon /usr/share/icons/hicolor/scalable/apps/distributor.svg

Requires:	release-notes-openSUSE
%define tde_aboutlabel OpenSuse 13.2
%define tde_aboutpage /usr/share/doc/release-notes/openSUSE/RELEASE-NOTES.en.html
%endif

BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	cmake >= 2.8
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	fdupes

# HTDIG support
BuildRequires:	htdig

# OPENSSL support
BuildRequires:	openssl-devel

# AUDIOFILE support
BuildRequires:	audiofile-devel

# ALSA supportl
BuildRequires:	alsa-lib-devel

# RAW1394 support
BuildRequires:	libraw1394-devel

# VORBIS support
BuildRequires:	libvorbis-devel

# GLIB2 support
BuildRequires:	glib2-devel

# PCRE support
BuildRequires:	pcre-devel

# SASL support
%if 0%{?mageia} || 0%{?mandriva} || 0%{?pclinuxos}
BuildRequires:	%{_lib}sasl2-devel
%endif
%if 0%{?suse_version}
BuildRequires:	cyrus-sasl-devel
%endif

# LIBUSB support
BuildRequires:	pam-devel
%if 0%{?mageia} || 0%{?mandriva} || 0%{?pclinuxos}
BuildRequires:	%{_lib}usb1.0-devel
BuildRequires:	%{_lib}usb-compat0.1-devel
%else
BuildRequires:	libusb-devel
%endif

# ESOUND support
%if 0%{?rhel} || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
%define with_esound 1
BuildRequires:	esound-devel
%endif

# IDN support
BuildRequires:	libidn-devel

# GAMIN support
#  Not on openSUSE.
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:	gamin-devel
%endif

# OPENLDAP support
%if 0%{?suse_version}
BuildRequires:	openldap2-devel
%else
BuildRequires:	openldap-devel
%endif

# SENSORS support
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel}
BuildRequires:	lm_sensors-devel
%endif
%if 0%{?suse_version}
BuildRequires:	libsensors4-devel
%endif

# TSAK support (requires libudev-devel)
#  On RHEL5, udev is built statically, so TSAK cannot build.
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 6 || 0%{?suse_version}
BuildRequires:	libudev-devel
%define with_tsak 1
%endif

# XRANDR support
#  On RHEL5, xrandr library is too old.
%if 0%{?fedora} >= 15 || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 6 || 0%{?suse_version}
%define with_xrandr 1
%endif

# XTEST support
#  On RHEL4, xtest library is too old.
%if 0%{?fedora} >= 15 || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?suse_version}
%define with_xtest 1
%endif

# HAL support
#  On RHEL4, we do not use HAL (too old)
%if 0%{?fedora} >= 15 || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?suse_version}
%define with_hal 1
BuildRequires:	hal-devel >= 0.5
%endif

# OPENEXR support
#  Disabled on RHEL4
%if 0%{?fedora} >= 15 || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?suse_version}
%define with_exr 1
BuildRequires:	OpenEXR-devel
%endif

# XSCREENSAVER support
%if 0%{?fedora} >= 15 || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?suse_version} || 0%{?with_xscreensaver}
%define with_xscreensaver 1
%if 0%{?fedora} || 0%{?rhel} >= 5 || 0%{?suse_version}
BuildRequires:	libXScrnSaver-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mgaversion} >= 4
BuildRequires:	%{_lib}xscrnsaver-devel
%else
BuildRequires:	%{_lib}xscrnsaver%{?mgaversion:1}-devel
%endif
%endif
%endif

# AVAHI support
#  Disabled on RHEL4 and RHEL5
%if 0%{?fedora} >= 15 || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 6 || 0%{?suse_version}
BuildRequires:	libavahi-tqt-devel
%endif

# MESA support
%if 0%{?rhel} || 0%{?fedora}
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: mesaglu-devel
%endif
%if 0%{?suse_version}
BuildRequires: Mesa-libGL-devel
BuildRequires: Mesa-libGLU-devel
%endif

# NAS support
# (what is nas btw ?)
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	nas-devel
%endif

# DBUS support
#  TQT bindings not available for RHEL4
%if 0%{?rhel} == 4
# Dbus bindings were rebuilt with Qt support
BuildRequires:	dbus-devel >= 0.22-12.EL.9p1
Requires:		dbus-qt >= 0.22-12.EL.9p1
%else
BuildRequires:	libdbus-tqt-1-devel >= %{tde_epoch}:0.63
BuildRequires:	libdbus-1-tqt-devel >= %{tde_epoch}:0.9
Requires:		libdbus-tqt-1-0 >= %{tde_epoch}:0.63
%endif

%if 0%{?fedora} >= 17
BuildRequires:	perl-Digest-MD5
%endif

# LIBART_LGPL support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version} || 0%{?fedora} || 0%{?rhel} >= 5
%define with_libart 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}art_lgpl-devel
%endif
%if 0%{?suse_version} || 0%{?fedora} || 0%{?rhel}
BuildRequires:	libart_lgpl-devel
%endif
%endif

# SAMBA support
%if 0%{?rhel} == 4
BuildRequires:	samba-common
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
BuildRequires:	libsmbclient-devel
%endif

# IMAKE
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version} >= 1220
BuildRequires:	imake
%endif

# XKB support
%if 0%{?suse_version} == 1140
BuildRequires:	xorg-x11-libxkbfile-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version} >= 1210
BuildRequires:	libxkbfile-devel
%endif

# XDMCP support
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mgaversion} >= 4
BuildRequires:	%{_lib}xdmcp-devel
%else
BuildRequires:	%{_lib}xdmcp%{?mgaversion:6}-devel
%endif
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libXdmcp-devel
%endif

# XTST support
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?mgaversion} >= 4
%define xtst_devel %{_lib}xtst-devel
%else
%define xtst_devel %{_lib}xtst%{?mgaversion:6}-devel
%endif
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
%define xtst_devel libXtst-devel
%endif
%{?xtst_devel:BuildRequires: %{xtst_devel}}

# XDAMAGE support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}xdamage-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libXdamage-devel
%endif

# Requires 'usb.ids'
BuildRequires:	usbutils

# LIBFONTENC support
%if 0%{?suse_version} == 1140
BuildRequires:	xorg-x11-libfontenc-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version} >= 1220
BuildRequires:	libfontenc-devel
%endif

# Other X11 stuff ...
%if 0%{?rhel} == 4
BuildRequires:	xorg-x11-devel
%endif

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	x11-font-util
BuildRequires:	x11-proto-devel
%endif

%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	xorg-x11-proto-devel
%endif

%if 0%{?rhel} >= 5 || 0%{?fedora}
BuildRequires:	xorg-x11-font-utils
%endif

%if 0%{?suse_version} >= 1220
BuildRequires:	font-util
BuildRequires:	bdftopcf
%endif

%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	drakconf
%endif

# tdebase is a metapackage that installs all sub-packages
Requires: %{name}-runtime-data-common = %{version}-%{release}
Requires: %{name}-data = %{version}-%{release}
Requires: %{name}-bin = %{version}-%{release}
Requires: %{name}-tdeio-plugins = %{version}-%{release}
Requires: %{name}-tdeio-pim-plugins = %{version}-%{release}
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
Requires: %{name}-tdeio-smb-plugin = %{version}-%{release}
 
Requires:	trinity-arts >= %{tde_epoch}:1.5.10
Requires:	trinity-tdelibs >= %{tde_version}
Requires:	openssl


# RHEL 6 Configuration files are provided in separate packages
%if 0%{?rhel} || 0%{?fedora}
Requires:	redhat-menus
%endif

%if 0%{?suse_version}
Requires:	desktop-data-openSUSE
%endif

%description
TDE (the Trinity Desktop Environment) is a powerful Open Source graphical
desktop environment for Unix workstations. It combines ease of use,
contemporary functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

This metapackage includes the nucleus of TDE, namely the minimal package
set necessary to run TDE as a desktop environment. This includes the
window manager, taskbar, control center, a text editor, file manager,
web browser, X terminal emulator, and many other programs and components.

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING-DOCS README README.pam

##########

%package devel
Summary:	%{summary} - Development files
Group:		Development/Libraries/Other
Requires:	%{name} = %{version}-%{release}
Requires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
Requires:	trinity-tdelibs-devel >= %{tde_version}

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
Kate plugins or TWin styles.

%files devel
%defattr(-,root,root,-)
%{tde_datadir}/cmake/*.cmake

##########

%package tdeio-pim-plugins
Summary:	PIM TDEIOslaves from %{name}
Group:		System/GUI/Other

Provides:	trinity-kdebase-pim-ioslaves = %{version}-%{release}
Obsoletes:	trinity-kdebase-pim-ioslaves < %{version}-%{release}
Provides:	tdebase-kio-pim-plugins = %{version}-%{release}
Obsoletes:	tdebase-kio-pim-plugins < %{version}-%{release}
Provides:	trinity-tdebase-kio-pim-plugins = %{version}-%{release}
Obsoletes:	trinity-tdebase-kio-pim-plugins < %{version}-%{release}

%description tdeio-pim-plugins
Protocol handlers (TDEIOslaves) for personal information management, including:
 * tdeio_ldap
 * tdeio_nntp
 * tdeio_pop3
 * tdeio_smtp

%files tdeio-pim-plugins
%defattr(-,root,root,-)
%{tde_tdelibdir}/kio_ldap.la
%{tde_tdelibdir}/kio_ldap.so
%{tde_tdelibdir}/kio_nntp.la
%{tde_tdelibdir}/kio_nntp.so
%{tde_tdelibdir}/kio_pop3.la
%{tde_tdelibdir}/kio_pop3.so
%{tde_tdelibdir}/kio_smtp.la
%{tde_tdelibdir}/kio_smtp.so
%{tde_datadir}/services/ldap.protocol
%{tde_datadir}/services/ldaps.protocol
%{tde_datadir}/services/nntp.protocol
%{tde_datadir}/services/nntps.protocol
%{tde_datadir}/services/pop3.protocol
%{tde_datadir}/services/pop3s.protocol
%{tde_datadir}/services/smtp.protocol
%{tde_datadir}/services/smtps.protocol

##########

%package runtime-data-common
Summary:	Shared common files for Trinity and KDE4
Group:		System/GUI/Other

Provides:	tdebase-runtime-data-common = %{version}-%{release}
Obsoletes:	tdebase-runtime-data-common < %{version}-%{release}

%description runtime-data-common
Shared common files for both Trinity and KDE4
Such as the desktop right-click-"Create New" list

%files runtime-data-common
%defattr(-,root,root,-)
%{tde_datadir}/autostart/khotkeys.desktop
%{tde_datadir}/desktop-directories/
%{tde_datadir}/icons/hicolor/*/apps/kxkb.png
%{tde_datadir}/icons/hicolor/*/apps/knetattach.*
%{tde_datadir}/icons/hicolor/*/apps/khotkeys.png
%{tde_datadir}/icons/hicolor/*/apps/kmenuedit.png
%{tde_datadir}/icons/hicolor/*/apps/ksplash.png
%{tde_datadir}/locale/en_US/entry.desktop
%{tde_datadir}/locale/l10n/*.desktop
%{tde_datadir}/locale/l10n/*/entry.desktop
%{tde_datadir}/locale/l10n/*/flag.png
%{tde_datadir}/sounds/pop.wav
%{tde_datadir}/templates/

%post runtime-data-common
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

%postun runtime-data-common
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-kappfinder
Summary:	Non-TDE application finder for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-kappfinder
kappfinder searches your workstation for many common applications and
creates menu entries for them.

%files -n trinity-kappfinder
%defattr(-,root,root,-)
%{tde_bindir}/kappfinder
%{tde_tdeappdir}/kappfinder.desktop
%{tde_datadir}/applnk/System/kappfinder.desktop
%{tde_datadir}/apps/kappfinder
%{tde_datadir}/icons/hicolor/*/apps/kappfinder.png

%post -n trinity-kappfinder
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun -n trinity-kappfinder
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database %{tde_appdir} 2> /dev/null || : 

##########

%package -n trinity-libkateinterfaces
Summary:	Common libraries used by kwrite and kate
Group:		System/GUI/Other

%description -n trinity-libkateinterfaces
This package contains the kateinterface library.

%files -n trinity-libkateinterfaces
%defattr(-,root,root,-)
%{tde_libdir}/libkateinterfaces.so.*

%post -n trinity-libkateinterfaces
/sbin/ldconfig || :

%postun -n trinity-libkateinterfaces
/sbin/ldconfig || :

##########

%package -n trinity-kate
Summary:	Advanced text editor for TDE
Group:		System/GUI/Other
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
%{tde_bindir}/kate
%{tde_tdelibdir}/kate.la
%{tde_tdelibdir}/kate.so
%{tde_libdir}/libkateutils.so.*
%{tde_libdir}/libkdeinit_kate.la
%{tde_libdir}/libkdeinit_kate.so
%{tde_tdeappdir}/kate.desktop
%{tde_datadir}/apps/kate/
%{tde_datadir}/apps/kconf_update/kate-2.4.upd
%config(noreplace) %{_sysconfdir}/trinity/katerc
%{tde_datadir}/icons/hicolor/*/apps/kate.png
%{tde_datadir}/icons/hicolor/*/apps/kate2.svgz
%{tde_datadir}/servicetypes/kateplugin.desktop
%{tde_tdedocdir}/HTML/en/kate/

%post -n trinity-kate
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database %{tde_appdir} 2> /dev/null || : 
/sbin/ldconfig || :

%postun -n trinity-kate
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database %{tde_appdir} 2> /dev/null || : 
/sbin/ldconfig || :

##########

%package -n trinity-kate-devel
Summary:	Development files for kate
Group:		Development/Libraries/Other
Requires:	trinity-kate = %{version}-%{release}

%description -n trinity-kate-devel
This package contains the development files fare Kate.

%files -n trinity-kate-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kate/
%{tde_libdir}/libkateutils.so
%{tde_libdir}/libkateutils.la
%{tde_libdir}/libkateinterfaces.so
%{tde_libdir}/libkateinterfaces.la

%post -n trinity-kate-devel
/sbin/ldconfig || :

%postun -n trinity-kate-devel
/sbin/ldconfig || :

##########

%package -n trinity-kwrite
Summary:	Advanced text editor for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}
Requires:	trinity-libkateinterfaces = %{version}-%{release}

%description -n trinity-kwrite
Kwrite is an advanced text editor for TDE.

%files -n trinity-kwrite
%defattr(-,root,root,-)
%{tde_bindir}/kwrite
%{tde_tdelibdir}/kwrite.la
%{tde_tdelibdir}/kwrite.so
%{tde_libdir}/libkdeinit_kwrite.la
%{tde_libdir}/libkdeinit_kwrite.so
%{tde_tdeappdir}/kwrite.desktop
%{tde_datadir}/apps/kwrite/
%{tde_datadir}/icons/hicolor/*/apps/kwrite.png
%{tde_datadir}/icons/hicolor/*/apps/kwrite2.svgz
%{tde_tdedocdir}/HTML/en/kwrite/


%post -n trinity-kwrite
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun -n trinity-kwrite
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database %{tde_appdir} 2> /dev/null || : 

##########

%package -n trinity-kcontrol
Summary:	Control center for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

# Requires 'usb.ids'
Requires:	usbutils
%if 0%{?suse_version} == 0
Requires:	hwdata
%endif

%description -n trinity-kcontrol
The Trinity Control Center provides you with a centralized and convenient
way to configure all of your TDE settings.

It is made up of multiple modules. Each module is a separate application,
but the control center organizes all of these programs into a convenient
location.

In combination with udev KControl supports the advanced
configuration of Logitech mice, though the user must be a member of the
plugdev group.

%files -n trinity-kcontrol
%defattr(-,root,root,-)
%{tde_bindir}/kaccess
%{tde_bindir}/kcontrol
%{tde_bindir}/kdeinstallktheme
%{tde_bindir}/keditfiletype
%{tde_bindir}/kfontinst
%{tde_bindir}/kfontview
%{tde_bindir}/kinfocenter
%{tde_bindir}/klocaldomainurifilterhelper
%{tde_bindir}/krdb
%{tde_tdelibdir}/fontthumbnail.la
%{tde_tdelibdir}/fontthumbnail.so
%{tde_tdelibdir}/kaccess.la
%{tde_tdelibdir}/kaccess.so
%{tde_tdelibdir}/kcm_access.la
%{tde_tdelibdir}/kcm_access.so
%{tde_tdelibdir}/kcm_arts.la
%{tde_tdelibdir}/kcm_arts.so
%{tde_tdelibdir}/kcm_background.la
%{tde_tdelibdir}/kcm_background.so
%{tde_tdelibdir}/kcm_bell.la
%{tde_tdelibdir}/kcm_bell.so
%{tde_tdelibdir}/kcm_clock.la
%{tde_tdelibdir}/kcm_clock.so
%{tde_tdelibdir}/kcm_colors.la
%{tde_tdelibdir}/kcm_colors.so
%{tde_tdelibdir}/kcm_componentchooser.la
%{tde_tdelibdir}/kcm_componentchooser.so
%{tde_tdelibdir}/kcm_crypto.la
%{tde_tdelibdir}/kcm_crypto.so
%{tde_tdelibdir}/kcm_css.la
%{tde_tdelibdir}/kcm_css.so
%{tde_tdelibdir}/kcm_display.la
%{tde_tdelibdir}/kcm_display.so
%{tde_tdelibdir}/kcm_energy.la
%{tde_tdelibdir}/kcm_energy.so
%{tde_tdelibdir}/kcm_filetypes.la
%{tde_tdelibdir}/kcm_filetypes.so
%{tde_tdelibdir}/kcm_fontinst.la
%{tde_tdelibdir}/kcm_fontinst.so
%{tde_tdelibdir}/kcm_fonts.la
%{tde_tdelibdir}/kcm_fonts.so
%{tde_tdelibdir}/kcm_icons.la
%{tde_tdelibdir}/kcm_icons.so
%{tde_tdelibdir}/kcm_info.la
%{tde_tdelibdir}/kcm_info.so
%{tde_tdelibdir}/kcm_input.la
%{tde_tdelibdir}/kcm_input.so
%{tde_tdelibdir}/kcm_ioslaveinfo.la
%{tde_tdelibdir}/kcm_ioslaveinfo.so
%{tde_tdelibdir}/kcm_joystick.la
%{tde_tdelibdir}/kcm_joystick.so
%{tde_tdelibdir}/kcm_kded.la
%{tde_tdelibdir}/kcm_kded.so
%{tde_tdelibdir}/kcm_%{tdm}.la
%{tde_tdelibdir}/kcm_%{tdm}.so
%{tde_tdelibdir}/kcm_kdnssd.so
%{tde_tdelibdir}/kcm_kdnssd.la
%{tde_tdelibdir}/kcm_keys.la
%{tde_tdelibdir}/kcm_keys.so
%{tde_tdelibdir}/kcm_kicker.la
%{tde_tdelibdir}/kcm_kicker.so
%{tde_tdelibdir}/kcm_kio.la
%{tde_tdelibdir}/kcm_kio.so
%{tde_tdelibdir}/kcm_knotify.la
%{tde_tdelibdir}/kcm_knotify.so
%{tde_tdelibdir}/kcm_konqhtml.la
%{tde_tdelibdir}/kcm_konqhtml.so
%{tde_tdelibdir}/kcm_konq.la
%{tde_tdelibdir}/kcm_konq.so
%{tde_tdelibdir}/kcm_kthememanager.la
%{tde_tdelibdir}/kcm_kthememanager.so
%{tde_tdelibdir}/kcm_kurifilt.la
%{tde_tdelibdir}/kcm_kurifilt.so
%{tde_tdelibdir}/kcm_launch.la
%{tde_tdelibdir}/kcm_launch.so
%{tde_tdelibdir}/kcm_locale.la
%{tde_tdelibdir}/kcm_locale.so
%{tde_tdelibdir}/kcm_nic.la
%{tde_tdelibdir}/kcm_nic.so
%{tde_tdelibdir}/kcm_performance.la
%{tde_tdelibdir}/kcm_performance.so
%{tde_tdelibdir}/kcm_privacy.la
%{tde_tdelibdir}/kcm_privacy.so
%{tde_tdelibdir}/kcm_screensaver.la
%{tde_tdelibdir}/kcm_screensaver.so
%{tde_tdelibdir}/kcm_smserver.la
%{tde_tdelibdir}/kcm_smserver.so
%{tde_tdelibdir}/kcm_spellchecking.la
%{tde_tdelibdir}/kcm_spellchecking.so
%{tde_tdelibdir}/kcm_style.la
%{tde_tdelibdir}/kcm_style.so
%{tde_tdelibdir}/kcm_taskbar.la
%{tde_tdelibdir}/kcm_taskbar.so
%{tde_tdelibdir}/kcm_usb.la
%{tde_tdelibdir}/kcm_usb.so
%{tde_tdelibdir}/kcm_view1394.la
%{tde_tdelibdir}/kcm_view1394.so
%{tde_tdelibdir}/kcm_xinerama.la
%{tde_tdelibdir}/kcm_xinerama.so
%{tde_tdelibdir}/kcontrol.la
%{tde_tdelibdir}/kcontrol.so
%{tde_tdelibdir}/kfile_font.la
%{tde_tdelibdir}/kfile_font.so
%{tde_tdelibdir}/kio_fonts.la
%{tde_tdelibdir}/kio_fonts.so
%{tde_tdelibdir}/kstyle_keramik_config.la
%{tde_tdelibdir}/kstyle_keramik_config.so
%{tde_tdelibdir}/libkfontviewpart.la
%{tde_tdelibdir}/libkfontviewpart.so
%{tde_tdelibdir}/libkshorturifilter.la
%{tde_tdelibdir}/libkshorturifilter.so
%{tde_tdelibdir}/libkuriikwsfilter.la
%{tde_tdelibdir}/libkuriikwsfilter.so
%{tde_tdelibdir}/libkurisearchfilter.la
%{tde_tdelibdir}/libkurisearchfilter.so
%{tde_tdelibdir}/liblocaldomainurifilter.la
%{tde_tdelibdir}/liblocaldomainurifilter.so
%{tde_libdir}/libkdeinit_kaccess.la
%{tde_libdir}/libkdeinit_kaccess.so
%{tde_libdir}/libkdeinit_kcontrol.la
%{tde_libdir}/libkdeinit_kcontrol.so
%{tde_libdir}/libkfontinst.so.*
%{tde_tdeappdir}/arts.desktop
%{tde_tdeappdir}/background.desktop
%{tde_tdeappdir}/bell.desktop
%{tde_tdeappdir}/cache.desktop
%{tde_tdeappdir}/cdinfo.desktop
%{tde_tdeappdir}/clock.desktop
%{tde_tdeappdir}/colors.desktop
%{tde_tdeappdir}/componentchooser.desktop
%{tde_tdeappdir}/cookies.desktop
%{tde_tdeappdir}/crypto.desktop
%{tde_tdeappdir}/desktopbehavior.desktop
%{tde_tdeappdir}/desktop.desktop
%{tde_tdeappdir}/desktoppath.desktop
%{tde_tdeappdir}/devices.desktop
%{tde_tdeappdir}/display.desktop
%{tde_tdeappdir}/dma.desktop
%{tde_tdeappdir}/ebrowsing.desktop
%{tde_tdeappdir}/filebrowser.desktop
%{tde_tdeappdir}/filetypes.desktop
%{tde_tdeappdir}/fonts.desktop
%{tde_tdeappdir}/icons.desktop
%{tde_tdeappdir}/installktheme.desktop
%{tde_tdeappdir}/interrupts.desktop
%{tde_tdeappdir}/ioports.desktop
%{tde_tdeappdir}/ioslaveinfo.desktop
%{tde_tdeappdir}/joystick.desktop
%{tde_tdeappdir}/kcm_kdnssd.desktop
%{tde_tdeappdir}/kcmaccess.desktop
%{tde_tdeappdir}/kcmcss.desktop
%{tde_tdeappdir}/kcmfontinst.desktop
%{tde_tdeappdir}/kcmkded.desktop
%{tde_tdeappdir}/kcmlaunch.desktop
%{tde_tdeappdir}/kcmnotify.desktop
%{tde_tdeappdir}/kcmperformance.desktop
%{tde_tdeappdir}/kcmsmserver.desktop
%{tde_tdeappdir}/kcmtaskbar.desktop
%{tde_tdeappdir}/kcmusb.desktop
%{tde_tdeappdir}/kcmview1394.desktop
%{tde_tdeappdir}/KControl.desktop
%{tde_tdeappdir}/%{tdm}.desktop
%{tde_tdeappdir}/keys.desktop
%{tde_tdeappdir}/kfontview.desktop
%{tde_tdeappdir}/khtml_behavior.desktop
%{tde_tdeappdir}/khtml_fonts.desktop
%{tde_tdeappdir}/khtml_java_js.desktop
%{tde_tdeappdir}/kinfocenter.desktop
%{tde_tdeappdir}/kthememanager.desktop
%{tde_tdeappdir}/lanbrowser.desktop
%{tde_tdeappdir}/language.desktop
%{tde_tdeappdir}/media.desktop
%{tde_tdeappdir}/memory.desktop
%{tde_tdeappdir}/mouse.desktop
%{tde_tdeappdir}/netpref.desktop
%{tde_tdeappdir}/nic.desktop
%{tde_tdeappdir}/opengl.desktop
%{tde_tdeappdir}/panel_appearance.desktop
%{tde_tdeappdir}/panel.desktop
%{tde_tdeappdir}/partitions.desktop
%{tde_tdeappdir}/pci.desktop
%{tde_tdeappdir}/privacy.desktop
%{tde_tdeappdir}/processor.desktop
%{tde_tdeappdir}/proxy.desktop
%{tde_tdeappdir}/screensaver.desktop
%{tde_tdeappdir}/scsi.desktop
%{tde_tdeappdir}/smbstatus.desktop
%{tde_tdeappdir}/sound.desktop
%{tde_tdeappdir}/spellchecking.desktop
%{tde_tdeappdir}/style.desktop
%{tde_tdeappdir}/useragent.desktop
%{tde_tdeappdir}/xserver.desktop
%{tde_datadir}/applnk/.hidden/energy.desktop
%{tde_datadir}/applnk/.hidden/fileappearance.desktop
%{tde_datadir}/applnk/.hidden/filebehavior.desktop
%{tde_datadir}/applnk/.hidden/filepreviews.desktop
%{tde_datadir}/applnk/.hidden/kcmkonqyperformance.desktop
%{tde_datadir}/applnk/.hidden/kicker_config_appearance.desktop
%{tde_datadir}/applnk/.hidden/kicker_config.desktop
%{tde_datadir}/applnk/.hidden/smb.desktop
%{tde_datadir}/applnk/.hidden/xinerama.desktop
%{tde_datadir}/applnk/Settings/LookNFeel/
%{tde_datadir}/applnk/Settings/WebBrowsing/khtml_appearance.desktop
%{tde_datadir}/applnk/Settings/WebBrowsing/nsplugin.desktop
%{tde_datadir}/applnk/Settings/WebBrowsing/smb.desktop
%{tde_datadir}/apps/kcm_componentchooser/kcm_browser.desktop
%{tde_datadir}/apps/kcm_componentchooser/kcm_kemail.desktop
%{tde_datadir}/apps/kcm_componentchooser/kcm_terminal.desktop
%{tde_datadir}/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%{tde_datadir}/apps/konqueror/servicemenus/installfont.desktop
%{tde_datadir}/mimelnk/application/x-ktheme.desktop
%{tde_datadir}/mimelnk/fonts/folder.desktop
%{tde_datadir}/mimelnk/fonts/package.desktop
%{tde_datadir}/mimelnk/fonts/system-folder.desktop
%{tde_datadir}/services/fonts.protocol
%{tde_datadir}/services/fontthumbnail.desktop
%{tde_datadir}/services/kaccess.desktop
%{tde_datadir}/services/kfile_font.desktop
%{tde_datadir}/services/kfontviewpart.desktop
%{tde_datadir}/services/kshorturifilter.desktop
%{tde_datadir}/services/kuriikwsfilter.desktop
%{tde_datadir}/services/kurisearchfilter.desktop
%{tde_datadir}/services/localdomainurifilter.desktop
%{tde_datadir}/icons/hicolor/*/apps/kcmcolors.png
%{tde_datadir}/icons/hicolor/*/apps/kcmcomponentchooser.png
%{tde_datadir}/icons/hicolor/*/apps/kcmdesktop.png
%{tde_datadir}/icons/hicolor/*/apps/kcmdesktopbehavior.png
%{tde_datadir}/icons/hicolor/*/apps/kcmkdnssd.png
%{tde_datadir}/icons/hicolor/*/apps/kcmlaunch.png
%{tde_datadir}/icons/hicolor/*/apps/kcmmedia.png
%{tde_datadir}/icons/hicolor/*/apps/kcmmouse.png
%{tde_datadir}/icons/hicolor/*/apps/kcmnetpref.png
%{tde_datadir}/icons/hicolor/*/apps/kcmnic.png
%{tde_datadir}/icons/hicolor/*/apps/kcmperformance.png
%{tde_datadir}/icons/hicolor/*/apps/kcmprivacy.png
%{tde_datadir}/icons/hicolor/*/apps/kcmtaskbar.png
%{tde_datadir}/icons/hicolor/*/apps/kcmcgi.png
%{tde_datadir}/icons/hicolor/*/apps/kcmcrypto.png
%{tde_datadir}/icons/hicolor/*/apps/kcmhistory.png
%{tde_datadir}/icons/hicolor/*/apps/kcmjoystick.png
%{tde_datadir}/icons/hicolor/*/apps/kcmkded.png
%{tde_datadir}/icons/hicolor/*/apps/kcmkhtml_filter.png
%{tde_datadir}/icons/hicolor/*/apps/kcmsmserver.png
%{tde_datadir}/icons/hicolor/*/apps/kcmspellchecking.png

%{tde_datadir}/apps/usb.ids
%{tde_datadir}/apps/kcmview1394/

# The following features are not compiled under RHEL 5 and older
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15 || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
%{tde_bindir}/krandrtray
%{tde_tdelibdir}/kcm_displayconfig.la
%{tde_tdelibdir}/kcm_displayconfig.so
%{tde_tdelibdir}/kcm_iccconfig.la
%{tde_tdelibdir}/kcm_iccconfig.so
%{tde_tdelibdir}/kcm_randr.la
%{tde_tdelibdir}/kcm_randr.so
%{tde_tdeappdir}/displayconfig.desktop
%{tde_tdeappdir}/iccconfig.desktop
%{tde_tdeappdir}/krandrtray.desktop
%{tde_datadir}/applnk/.hidden/randr.desktop
%{tde_datadir}/autostart/krandrtray-autostart.desktop
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
Group:		Development/Languages/Other
Requires:	trinity-kcontrol = %{version}-%{release}

%description -n trinity-kcontrol-devel
This package contains the development files for Kcontrol.

%files -n trinity-kcontrol-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkfontinst.la
%{tde_libdir}/libkfontinst.so

%post -n trinity-kcontrol-devel
/sbin/ldconfig || :

%postun -n trinity-kcontrol-devel
/sbin/ldconfig || :

##########

%package bin
Summary:	Core binaries for the TDE base module
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}
Requires:	pam
%if 0%{?rhel} >= 7
Requires:	xorg-x11-server-Xorg
Requires:	xorg-x11-drv-evdev
Requires:	dejavu-sans-fonts
%endif

Provides:	tdebase-bin = %{version}-%{release}
Obsoletes:	tdebase-bin < %{version}-%{release}

%description bin
This package contains miscellaneous programs needed by other
TDE applications, particularly those in the TDE base module.

%files bin
%defattr(-,root,root,-)
%{tde_bindir}/krootbacking
%if 0%{?with_tsak}
%{tde_bindir}/tsak
%endif
%{tde_bindir}/kdebugdialog
%{tde_bindir}/kreadconfig
%{tde_bindir}/kwriteconfig
%{tde_bindir}/kstart
%config(noreplace) %{_sysconfdir}/trinity/kxkb_groups
%{tde_bindir}/drkonqi
%{tde_bindir}/crashtest
%{tde_bindir}/kapplymousetheme
%{tde_bindir}/kblankscrn.kss
%{tde_bindir}/kcminit
%{tde_bindir}/kcminit_startup
%{tde_bindir}/kdcop
%{tde_bindir}/kdesu
%attr(0755,root,root) %{tde_bindir}/kdesud
%{tde_bindir}/kdialog
%{tde_bindir}/khotkeys
%{tde_bindir}/knetattach
%{tde_bindir}/krandom.kss
%{tde_bindir}/ksystraycmd
%{tde_bindir}/kxkb
%dir %{tde_libdir}/kconf_update_bin
%{tde_libdir}/kconf_update_bin/khotkeys_update
%{tde_tdelibdir}/kcminit.la
%{tde_tdelibdir}/kcminit.so
%{tde_tdelibdir}/kcminit_startup.la
%{tde_tdelibdir}/kcminit_startup.so
%{tde_tdelibdir}/kcm_keyboard.la
%{tde_tdelibdir}/kcm_keyboard.so
%{tde_tdelibdir}/kcm_khotkeys_init.la
%{tde_tdelibdir}/kcm_khotkeys_init.so
%{tde_tdelibdir}/kcm_khotkeys.la
%{tde_tdelibdir}/kcm_khotkeys.so
%{tde_tdelibdir}/kded_khotkeys.la
%{tde_tdelibdir}/kded_khotkeys.so
%{tde_tdelibdir}/kgreet_classic.la
%{tde_tdelibdir}/kgreet_classic.so
%{tde_tdelibdir}/kgreet_winbind.la
%{tde_tdelibdir}/kgreet_winbind.so
%{tde_tdelibdir}/khotkeys.la
%{tde_tdelibdir}/khotkeys.so
%{tde_tdelibdir}/khotkeys_arts.la
%{tde_tdelibdir}/khotkeys_arts.so
%{tde_tdelibdir}/kxkb.la
%{tde_tdelibdir}/kxkb.so
%{tde_libdir}/libkdeinit_kcminit.la
%{tde_libdir}/libkdeinit_kcminit.so
%{tde_libdir}/libkdeinit_kcminit_startup.la
%{tde_libdir}/libkdeinit_kcminit_startup.so
%{tde_libdir}/libkdeinit_khotkeys.la
%{tde_libdir}/libkdeinit_khotkeys.so
%{tde_libdir}/libkdeinit_kxkb.la
%{tde_libdir}/libkdeinit_kxkb.so
%{tde_libdir}/libkhotkeys_shared.so.*
%{tde_tdeappdir}/keyboard.desktop
%{tde_tdeappdir}/keyboard_layout.desktop
%{tde_tdeappdir}/khotkeys.desktop
%{tde_tdeappdir}/knetattach.desktop
%{tde_datadir}/applnk/System/ScreenSavers/
%{tde_datadir}/apps/drkonqi/
%{tde_datadir}/apps/kconf_update/khotkeys_32b1_update.upd
%{tde_datadir}/apps/kconf_update/khotkeys_printscreen.upd
%{tde_datadir}/apps/kconf_update/konqueror_gestures_trinity21_update.upd
%{tde_datadir}/apps/kdcop/
%{tde_datadir}/apps/khotkeys/
%{tde_datadir}/services/kded/khotkeys.desktop
%{tde_datadir}/services/kxkb.desktop
%if 0%{?suse_version} == 0
%config(noreplace) %{_sysconfdir}/pam.d/kcheckpass-trinity
%config(noreplace) %{_sysconfdir}/pam.d/tdescreensaver-trinity
%endif
%{tde_tdedocdir}/HTML/en/kdcop/
%{tde_tdedocdir}/HTML/en/kdebugdialog//
%{tde_tdedocdir}/HTML/en/kdesu/
%{tde_tdedocdir}/HTML/en/knetattach/
%{tde_tdedocdir}/HTML/en/kxkb/

# SETUID binaries
# Some setuid binaries need special care
%if 0%{?suse_version}
%if 0%{?with_tsak}
%verify(not mode) %{tde_bindir}/%{tdm}tsak
%endif
%verify(not mode) %{tde_bindir}/kcheckpass
%else
%if 0%{?with_tsak}
%attr(4511,root,root) %{tde_bindir}/%{tdm}tsak
%endif
%attr(4755,root,root) %{tde_bindir}/kcheckpass
%endif

%post bin
/sbin/ldconfig || :
update-desktop-database %{tde_appdir} 2> /dev/null || : 
# Sets permissions on setuid files (openSUSE specific)
%if 0%{?suse_version}
%if 0%{?with_tsak}
%set_permissions %{tde_bindir}/%{tdm}tsak
%endif
%set_permissions %{tde_bindir}/kcheckpass
%endif

%postun bin
/sbin/ldconfig || :
update-desktop-database %{tde_appdir} 2> /dev/null || : 

##########

%package bin-devel
Summary:	Development files for core binaries for the TDE base module
Group:		Development/Libraries/Other
Requires:	%{name}-bin = %{version}-%{release}
%{?xtst_devel:Requires: %{xtst_devel}}

Obsoletes:	tdebase-bin-devel < %{version}-%{release}
Provides:	tdebase-bin-devel = %{version}-%{release}

%description bin-devel
This package contains the development files for core binaries for 
the TDE base module

%files bin-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkhotkeys_shared.la
%{tde_libdir}/libkhotkeys_shared.so

%post bin-devel
/sbin/ldconfig || :

%postun bin-devel
/sbin/ldconfig || :

##########

%package data
Summary:	Shared data files for the TDE base module
Group:		System/GUI/Other
Requires:	%{name}-runtime-data-common = %{version}-%{release}

Obsoletes:	tdebase-data < %{version}-%{release}
Provides:	tdebase-data = %{version}-%{release}

%description data
This package contains the architecture-independent shared data files
needed for a basic TDE desktop installation.

%files data
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/kshorturifilterrc
%{tde_datadir}/applnk/.hidden/battery.desktop
%{tde_datadir}/applnk/.hidden/bwarning.desktop
%{tde_datadir}/applnk/.hidden/cwarning.desktop
%{tde_datadir}/applnk/.hidden/.directory
%{tde_datadir}/applnk/.hidden/email.desktop
%{tde_datadir}/applnk/.hidden/kcmkonq.desktop
%{tde_datadir}/applnk/.hidden/kcmkxmlrpcd.desktop
%{tde_datadir}/applnk/.hidden/konqhtml.desktop
%{tde_datadir}/applnk/.hidden/passwords.desktop
%{tde_datadir}/applnk/.hidden/power.desktop
%{tde_datadir}/applnk/.hidden/socks.desktop
%{tde_datadir}/applnk/.hidden/userinfo.desktop
%{tde_datadir}/applnk/.hidden/virtualdesktops.desktop
%{tde_datadir}/apps/kaccess/
%{tde_datadir}/apps/kcmcss/
%{tde_datadir}/apps/kcminput/
%{tde_datadir}/apps/kcmkeys/
%{tde_datadir}/apps/kcmlocale/
%{tde_datadir}/apps/kconf_update/convertShortcuts.pl
%{tde_datadir}/apps/kconf_update/kaccel.upd
%{tde_datadir}/apps/kconf_update/kcmdisplayrc.upd
%{tde_datadir}/apps/kconf_update/kuriikwsfilter.upd
%{tde_datadir}/apps/kconf_update/mouse_cursor_theme.upd
%{tde_datadir}/apps/kconf_update/socks.upd
%{tde_datadir}/apps/kcontrol/
%{tde_datadir}/apps/kdisplay/
%{tde_datadir}/apps/kfontview/
%{tde_datadir}/apps/kinfocenter/
%{tde_datadir}/apps/kthememanager/
%{tde_datadir}/icons/crystalsvg/*/apps/access.png
%{tde_datadir}/icons/crystalsvg/*/apps/acroread.png
%{tde_datadir}/icons/crystalsvg/*/apps/applixware.png
%{tde_datadir}/icons/crystalsvg/*/apps/arts.png
%{tde_datadir}/icons/crystalsvg/*/apps/background.png
%{tde_datadir}/icons/crystalsvg/*/apps/bell.png
%{tde_datadir}/icons/crystalsvg/*/apps/cache.png
%{tde_datadir}/icons/crystalsvg/*/apps/clanbomber.png
%{tde_datadir}/icons/crystalsvg/*/apps/clock.png
%{tde_datadir}/icons/crystalsvg/*/apps/colors.png
%{tde_datadir}/icons/crystalsvg/*/apps/date.png
%{tde_datadir}/icons/crystalsvg/*/apps/email.png
%{tde_datadir}/icons/crystalsvg/*/apps/energy.png
%{tde_datadir}/icons/crystalsvg/*/apps/energy_star.png
%{tde_datadir}/icons/crystalsvg/*/apps/filetypes.png
%{tde_datadir}/icons/crystalsvg/*/apps/fonts.png
%{tde_datadir}/icons/crystalsvg/*/apps/gimp.png
%{tde_datadir}/icons/crystalsvg/*/apps/help_index.png
%{tde_datadir}/icons/crystalsvg/*/apps/hwinfo.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmdevices.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmdf.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmkwm.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmmemory.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmpartitions.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmpci.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcontrol.png
%{tde_datadir}/icons/crystalsvg/*/apps/%{tdm}config.png
%{tde_datadir}/icons/crystalsvg/*/apps/key_bindings.png
%{tde_datadir}/icons/crystalsvg/*/apps/kfm_home.png
%{tde_datadir}/icons/crystalsvg/*/apps/kscreensaver.png
%{tde_datadir}/icons/crystalsvg/*/apps/kthememgr.png
%{tde_datadir}/icons/crystalsvg/*/apps/licq.png
%{tde_datadir}/icons/crystalsvg/*/apps/linuxconf.png
%{tde_datadir}/icons/crystalsvg/*/apps/locale.png
%{tde_datadir}/icons/crystalsvg/*/apps/looknfeel.png
%{tde_datadir}/icons/crystalsvg/*/apps/multimedia.png
%{tde_datadir}/icons/crystalsvg/*/apps/netscape.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_applications.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_development.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_favourite.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_games.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_games_kids.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_multimedia.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_network.png
%{tde_datadir}/icons/crystalsvg/*/apps/package.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_settings.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_toys.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_utilities.png
%{tde_datadir}/icons/crystalsvg/*/apps/penguin.png
%{tde_datadir}/icons/crystalsvg/*/apps/personal.png
%{tde_datadir}/icons/crystalsvg/*/apps/phppg.png
%{tde_datadir}/icons/crystalsvg/*/apps/proxy.png
%{tde_datadir}/icons/crystalsvg/*/apps/pysol.png
%{tde_datadir}/icons/crystalsvg/*/apps/randr.png
%{tde_datadir}/icons/crystalsvg/*/apps/samba.png
%{tde_datadir}/icons/crystalsvg/*/apps/staroffice.png
%{tde_datadir}/icons/crystalsvg/*/apps/stylesheet.png
%{tde_datadir}/icons/crystalsvg/*/apps/terminal.png
%{tde_datadir}/icons/crystalsvg/*/apps/tux.png
%{tde_datadir}/icons/crystalsvg/*/apps/wp.png
%{tde_datadir}/icons/crystalsvg/*/apps/xclock.png
%{tde_datadir}/icons/crystalsvg/*/apps/xfmail.png
%{tde_datadir}/icons/crystalsvg/*/apps/xmag.png
%{tde_datadir}/icons/crystalsvg/*/apps/xpaint.png
%{tde_datadir}/icons/crystalsvg/scalable/apps/access.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/acroread.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/aim.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/aktion.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/antivirus.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/applixware.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/arts.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/background.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/bell.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/browser.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/cache.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/camera.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/clanbomber.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/clock.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/colors.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/core.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/date.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/display.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/download_manager.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/email.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/energy.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/error.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/fifteenpieces.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/filetypes.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/fonts.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/galeon.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/gnome_apps.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/hardware.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/hwinfo.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/ieee1394.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/kcmdevices.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/kcmkwm.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/kcmx.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/locale.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/my_mac.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/netscape.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/openoffice.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/package_development.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/package_games_kids.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/package_toys.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/penguin.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/personal.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/quicktime.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/realplayer.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/samba.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/shell.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/staroffice.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/stylesheet.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/terminal.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/tux.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/wine.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/x.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/xapp.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/xcalc.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/xchat.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/xclock.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/xeyes.svgz
%{tde_datadir}/icons/crystalsvg/scalable/apps/xpaint.svgz
%{tde_datadir}/icons/crystalsvg/*/devices/laptop.png
%{tde_datadir}/icons/crystalsvg/*/devices/laptop.svgz
%{tde_datadir}/icons/crystalsvg/*/actions/newfont.png
%{tde_datadir}/icons/crystalsvg/*/apps/abiword.png
%{tde_datadir}/icons/crystalsvg/*/apps/agent.png
%{tde_datadir}/icons/crystalsvg/*/apps/alevt.png
%{tde_datadir}/icons/crystalsvg/*/apps/assistant.png
%{tde_datadir}/icons/crystalsvg/*/apps/blender.png
%{tde_datadir}/icons/crystalsvg/*/apps/bluefish.png
%{tde_datadir}/icons/crystalsvg/*/apps/cookie.png
%{tde_datadir}/icons/crystalsvg/*/apps/designer.png
%{tde_datadir}/icons/crystalsvg/*/apps/dia.png
%{tde_datadir}/icons/crystalsvg/*/apps/dlgedit.png
%{tde_datadir}/icons/crystalsvg/*/apps/eclipse.png
%{tde_datadir}/icons/crystalsvg/*/apps/edu_languages.png
%{tde_datadir}/icons/crystalsvg/*/apps/edu_mathematics.png
%{tde_datadir}/icons/crystalsvg/*/apps/edu_miscellaneous.png
%{tde_datadir}/icons/crystalsvg/*/apps/edu_science.png
%{tde_datadir}/icons/crystalsvg/*/apps/emacs.png
%{tde_datadir}/icons/crystalsvg/*/apps/enhanced_browsing.png
%{tde_datadir}/icons/crystalsvg/*/apps/evolution.png
%{tde_datadir}/icons/crystalsvg/*/apps/fifteenpieces.png
%{tde_datadir}/icons/crystalsvg/*/apps/gabber.png
%{tde_datadir}/icons/crystalsvg/*/apps/gaim.png
%{tde_datadir}/icons/crystalsvg/*/apps/gnome_apps.png
%{tde_datadir}/icons/crystalsvg/*/apps/gnomemeeting.png
%{tde_datadir}/icons/crystalsvg/*/apps/gnucash.png
%{tde_datadir}/icons/crystalsvg/*/apps/gnumeric.png
%{tde_datadir}/icons/crystalsvg/*/apps/gv.png
%{tde_datadir}/icons/crystalsvg/*/apps/gvim.png
%{tde_datadir}/icons/crystalsvg/*/apps/icons.png
%{tde_datadir}/icons/crystalsvg/*/apps/iconthemes.png
%{tde_datadir}/icons/crystalsvg/*/apps/ieee1394.png
%{tde_datadir}/icons/crystalsvg/*/apps/input_devices_settings.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmkicker.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmmidi.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmprocessor.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmscsi.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmsound.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmsystem.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmx.png
%{tde_datadir}/icons/crystalsvg/*/apps/keyboard.png
%{tde_datadir}/icons/crystalsvg/*/apps/keyboard_layout.png
%{tde_datadir}/icons/crystalsvg/*/apps/knotify.png
%{tde_datadir}/icons/crystalsvg/*/apps/kvirc.png
%{tde_datadir}/icons/crystalsvg/*/apps/linguist.png
%{tde_datadir}/icons/crystalsvg/*/apps/lyx.png
%{tde_datadir}/icons/crystalsvg/*/apps/mac.png
%{tde_datadir}/icons/crystalsvg/*/apps/mathematica.png
%{tde_datadir}/icons/crystalsvg/*/apps/nedit.png
%{tde_datadir}/icons/crystalsvg/*/apps/opera.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_application.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_editors.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_edutainment.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_games_arcade.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_games_board.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_games_card.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_games_strategy.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_graphics.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_system.png
%{tde_datadir}/icons/crystalsvg/*/apps/package_wordprocessing.png
%{tde_datadir}/icons/crystalsvg/*/apps/pan.png
%{tde_datadir}/icons/crystalsvg/*/apps/panel_settings.png
%{tde_datadir}/icons/crystalsvg/*/apps/plan.png
%{tde_datadir}/icons/crystalsvg/*/apps/planner.png
%{tde_datadir}/icons/crystalsvg/*/apps/pybliographic.png
%{tde_datadir}/icons/crystalsvg/*/apps/realplayer.png
%{tde_datadir}/icons/crystalsvg/*/apps/remote.png
%{tde_datadir}/icons/crystalsvg/*/apps/scribus.png
%{tde_datadir}/icons/crystalsvg/*/apps/sodipodi.png
%{tde_datadir}/icons/crystalsvg/*/apps/style.png
%{tde_datadir}/icons/crystalsvg/*/apps/usb.png
%{tde_datadir}/icons/crystalsvg/*/apps/vnc.png
%{tde_datadir}/icons/crystalsvg/*/apps/wabi.png
%{tde_datadir}/icons/crystalsvg/*/apps/wine.png
%{tde_datadir}/icons/crystalsvg/*/apps/xcalc.png
%{tde_datadir}/icons/crystalsvg/*/apps/xchat.png
%{tde_datadir}/icons/crystalsvg/*/apps/xclipboard.png
%{tde_datadir}/icons/crystalsvg/*/apps/xconsole.png
%{tde_datadir}/icons/crystalsvg/*/apps/xedit.png
%{tde_datadir}/icons/crystalsvg/*/apps/xemacs.png
%{tde_datadir}/icons/crystalsvg/*/apps/xeyes.png
%{tde_datadir}/icons/crystalsvg/*/apps/xfig.png
%{tde_datadir}/icons/crystalsvg/*/apps/xload.png
%{tde_datadir}/icons/crystalsvg/*/apps/xmms.png
%{tde_datadir}/icons/crystalsvg/*/apps/xosview.png
%{tde_datadir}/icons/crystalsvg/*/apps/xv.png
%{tde_datadir}/icons/crystalsvg/*/apps/galeon.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmdrkonqi.png
%{tde_datadir}/icons/crystalsvg/*/apps/pinguin.png
%{tde_datadir}/icons/crystalsvg/*/apps/x.png
%{tde_datadir}/icons/crystalsvg/*/apps/xapp.png
%{tde_datadir}/icons/crystalsvg/*/apps/xawtv.png
%{tde_datadir}/icons/crystalsvg/*/apps/kcmopengl.png
%{tde_datadir}/icons/crystalsvg/*/apps/wmaker_apps.png
%{tde_datadir}/icons/crystalsvg/*/apps/qtella.png
%{tde_datadir}/services/searchproviders
%{tde_datadir}/services/useragentstrings/
%{tde_datadir}/servicetypes/searchprovider.desktop
%{tde_datadir}/servicetypes/uasprovider.desktop
%exclude %{tde_datadir}/sounds/pop.wav
%{tde_datadir}/sounds/
%{tde_datadir}/wallpapers/*

# XDG directories information
%dir %{_sysconfdir}/xdg/menus/applications-merged
%config(noreplace) %{_sysconfdir}/xdg/menus/applications-merged/tde-essential.menu
%config(noreplace) %{_sysconfdir}/xdg/menus/tde-information.menu
%config(noreplace) %{_sysconfdir}/xdg/menus/tde-screensavers.menu
%config(noreplace) %{_sysconfdir}/xdg/menus/tde-settings.menu

%{tde_tdedocdir}/HTML/en/kcontrol/
%exclude %{tde_tdedocdir}/HTML/en/kcontrol/kcmkonsole/
%{tde_tdedocdir}/HTML/en/kinfocenter/

%post data
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

%if "%{distribution}" == "Mandriva Linux"
# Mandriva-specific: we have to choose a background for current distribution variant (Free, One, Powerpack, ...)
# First, we read the "product" key in /etc/product.id
eval $(tr "," ";" </etc/product.id) 2>/dev/null
# Then, we create a symbolic link to the corresponding background
if [ -r "%{_datadir}/mdk/backgrounds/Mandriva-${product:-Free}-1280x1024-1300.jpg" "%{tde_bg}" ]; then
  ln -sf "%{_datadir}/mdk/backgrounds/Mandriva-${product:-Free}-1280x1024-1300.jpg" "%{tde_bg}"
fi
%endif

%if "%{distribution}" == "Mageia"
if [ ! -r "%{tde_bg}" ] && [ -r "%{_datadir}/mga/backgrounds/Mageia-Default-1920x1440.png" ]; then
  ln -sf "%{_datadir}/mga/backgrounds/Mageia-Default-1920x1440.png" "%{tde_bg}"
fi
%endif

%postun data
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package tdeio-plugins
Summary:	Core I/O slaves for TDE
Group:		System/GUI/Other
Requires:	trinity-kdesktop = %{version}-%{release}
Requires:	cyrus-sasl
Requires:	psmisc
%if 0%{?with_hal}
Requires:	hal >= 0.4.8
%endif
%if 0%{?rhel} == 4 || 0%{?suse_version}
Requires:	cryptsetup
%else
Requires:	cryptsetup-luks
%endif

Obsoletes:	tdebase-kio-plugins < %{version}-%{release}
Provides:	tdebase-kio-plugins = %{version}-%{release}
Obsoletes:	trinity-tdebase-kio-plugins < %{version}-%{release}
Provides:	trinity-tdebase-kio-plugins = %{version}-%{release}

%description tdeio-plugins
This package includes the base tdeioslaves. They include, amongst many
others, file, http, and ftp.

It also includes the media tdeioslave, which handles removable devices,
and which works best with hal (and therefore udev) and pmount. Media
also extends the functionality of many other tdeioslaves. To use this
service, please make sure that your user is a member of the plugdev
group.

%files tdeio-plugins
%defattr(-,root,root,-)
%{tde_bindir}/kio_media_mounthelper
%{tde_bindir}/ktrash
%{tde_tdelibdir}/cursorthumbnail.la
%{tde_tdelibdir}/cursorthumbnail.so
%{tde_tdelibdir}/djvuthumbnail.la
%{tde_tdelibdir}/djvuthumbnail.so
%{tde_tdelibdir}/htmlthumbnail.la
%{tde_tdelibdir}/htmlthumbnail.so
%{tde_tdelibdir}/imagethumbnail.la
%{tde_tdelibdir}/imagethumbnail.so
%{tde_tdelibdir}/kcm_cgi.la
%{tde_tdelibdir}/kcm_cgi.so
%{tde_tdelibdir}/kcm_media.la
%{tde_tdelibdir}/kcm_media.so
%{tde_tdelibdir}/kded_homedirnotify.la
%{tde_tdelibdir}/kded_homedirnotify.so
%{tde_tdelibdir}/kded_mediamanager.la
%{tde_tdelibdir}/kded_mediamanager.so
%{tde_tdelibdir}/kded_medianotifier.la
%{tde_tdelibdir}/kded_medianotifier.so
%{tde_tdelibdir}/kded_remotedirnotify.la
%{tde_tdelibdir}/kded_remotedirnotify.so
%{tde_tdelibdir}/kded_systemdirnotify.la
%{tde_tdelibdir}/kded_systemdirnotify.so
%{tde_tdelibdir}/kfile_media.la
%{tde_tdelibdir}/kfile_media.so
%{tde_tdelibdir}/kfile_trash.la
%{tde_tdelibdir}/kfile_trash.so
%{tde_tdelibdir}/kio_about.la
%{tde_tdelibdir}/kio_about.so
%{tde_tdelibdir}/kio_cgi.la
%{tde_tdelibdir}/kio_cgi.so
%{tde_tdelibdir}/kio_filter.la
%{tde_tdelibdir}/kio_filter.so
%{tde_tdelibdir}/kio_finger.la
%{tde_tdelibdir}/kio_finger.so
%{tde_tdelibdir}/kio_fish.la
%{tde_tdelibdir}/kio_fish.so
%{tde_tdelibdir}/kio_floppy.la
%{tde_tdelibdir}/kio_floppy.so
%{tde_tdelibdir}/kio_home.la
%{tde_tdelibdir}/kio_home.so
%{tde_tdelibdir}/kio_info.la
%{tde_tdelibdir}/kio_info.so
%{tde_tdelibdir}/kio_mac.la
%{tde_tdelibdir}/kio_mac.so
%{tde_tdelibdir}/kio_man.la
%{tde_tdelibdir}/kio_man.so
%{tde_tdelibdir}/kio_media.la
%{tde_tdelibdir}/kio_media.so
%{tde_tdelibdir}/kio_nfs.la
%{tde_tdelibdir}/kio_nfs.so
%{tde_tdelibdir}/kio_remote.la
%{tde_tdelibdir}/kio_remote.so
%{tde_tdelibdir}/kio_settings.la
%{tde_tdelibdir}/kio_settings.so
%{tde_tdelibdir}/kio_sftp.la
%{tde_tdelibdir}/kio_sftp.so
%{tde_tdelibdir}/kio_system.la
%{tde_tdelibdir}/kio_system.so
%{tde_tdelibdir}/kio_tar.la
%{tde_tdelibdir}/kio_tar.so
%{tde_tdelibdir}/kio_thumbnail.la
%{tde_tdelibdir}/kio_thumbnail.so
%{tde_tdelibdir}/kio_trash.la
%{tde_tdelibdir}/kio_trash.so
%{tde_tdelibdir}/libkmanpart.la
%{tde_tdelibdir}/libkmanpart.so
%{tde_tdelibdir}/textthumbnail.la
%{tde_tdelibdir}/textthumbnail.so
%{tde_tdeappdir}/kcmcgi.desktop
%{tde_datadir}/apps/kio_finger/
%{tde_datadir}/apps/kio_info/
%{tde_datadir}/apps/kio_man/
%{tde_datadir}/apps/systemview/
%{tde_datadir}/config.kcfg/mediamanagersettings.kcfg
%{tde_datadir}/mimelnk/application/x-smb-server.desktop
%{tde_datadir}/mimelnk/inode/system_directory.desktop
%{tde_datadir}/mimelnk/media/*.desktop
%{tde_datadir}/services/about.protocol
%{tde_datadir}/services/applications.protocol
%{tde_datadir}/services/ar.protocol
%{tde_datadir}/services/bzip.protocol
%{tde_datadir}/services/bzip2.protocol
%{tde_datadir}/services/cgi.protocol
%{tde_datadir}/services/cursorthumbnail.desktop
%{tde_datadir}/services/djvuthumbnail.desktop
%{tde_datadir}/services/finger.protocol
%{tde_datadir}/services/fish.protocol
%{tde_datadir}/services/floppy.protocol
%{tde_datadir}/services/gzip.protocol
%{tde_datadir}/services/home.protocol
%{tde_datadir}/services/htmlthumbnail.desktop
%{tde_datadir}/services/imagethumbnail.desktop
%{tde_datadir}/services/info.protocol
%{tde_datadir}/services/kded/homedirnotify.desktop
%{tde_datadir}/services/kded/mediamanager.desktop
%{tde_datadir}/services/kded/medianotifier.desktop
%{tde_datadir}/services/kded/remotedirnotify.desktop
%{tde_datadir}/services/kded/systemdirnotify.desktop
%{tde_datadir}/services/kfile_media.desktop
%{tde_datadir}/services/kfile_trash_system.desktop
%{tde_datadir}/services/lzma.protocol
%{tde_datadir}/services/kmanpart.desktop
%{tde_datadir}/services/mac.protocol
%{tde_datadir}/services/man.protocol
%{tde_datadir}/services/media.protocol
%{tde_datadir}/services/nfs.protocol
%{tde_datadir}/services/nxfish.protocol
%{tde_datadir}/services/programs.protocol
%{tde_datadir}/services/remote.protocol
%{tde_datadir}/services/settings.protocol
%{tde_datadir}/services/sftp.protocol
%{tde_datadir}/services/system.protocol
%{tde_datadir}/services/tar.protocol
%{tde_datadir}/services/textthumbnail.desktop
%{tde_datadir}/services/thumbnail.protocol
%{tde_datadir}/services/trash.protocol
%{tde_datadir}/services/xz.protocol
%{tde_datadir}/services/zip.protocol
%{tde_datadir}/servicetypes/thumbcreator.desktop
%{tde_datadir}/services/kfile_trash.desktop
%{tde_tdedocdir}/HTML/en/kioslave/
%if 0%{?with_exr}
%{tde_tdelibdir}/exrthumbnail.la
%{tde_tdelibdir}/exrthumbnail.so
%{tde_datadir}/services/exrthumbnail.desktop
%endif
%if 0%{?with_hal}
%{tde_tdelibdir}/media_propsdlgplugin.la
%{tde_tdelibdir}/media_propsdlgplugin.so
%{tde_datadir}/services/media_propsdlgplugin.desktop
%endif

%post tdeio-plugins
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun tdeio-plugins
update-desktop-database %{tde_appdir} 2> /dev/null || : 

##########

%package -n trinity-tdepasswd
Summary:	Password changer for TDE
Group:		System/GUI/Other

Obsoletes:	trinity-kdepasswd < %{version}-%{release}
Provides:	trinity-kdepasswd = %{version}-%{release}

%description -n trinity-tdepasswd
This is a simple application which allows users to change their
system passwords.

%files -n trinity-tdepasswd
%defattr(-,root,root,-)
%{tde_bindir}/kdepasswd
%{tde_tdelibdir}/kcm_useraccount.la
%{tde_tdelibdir}/kcm_useraccount.so
%{tde_tdeappdir}/kcm_useraccount.desktop
%{tde_tdeappdir}/kdepasswd.desktop
%{tde_datadir}/config.kcfg/kcm_useraccount.kcfg
%{tde_datadir}/config.kcfg/kcm_useraccount_pass.kcfg
%{_datadir}/faces/Apple.png
%{_datadir}/faces/BeachBall.png
%{_datadir}/faces/Blowfish.png
%{_datadir}/faces/Bug.png
%{_datadir}/faces/Butterfly.png
%{_datadir}/faces/Car.png
%{_datadir}/faces/Cow.png 
%{_datadir}/faces/Daemon.png
%{_datadir}/faces/Dog.png
%{_datadir}/faces/Elephant.png
%{_datadir}/faces/Flower.png
%{_datadir}/faces/Frog.png
%{_datadir}/faces/Ghost.png
%{_datadir}/faces/Guitar.png
%{_datadir}/faces/Heart.png
%{_datadir}/faces/Konqui.png
%{_datadir}/faces/Lion.png
%{_datadir}/faces/Monkey.png
%{_datadir}/faces/Penguin.png
%{_datadir}/faces/Pig.png
%{_datadir}/faces/Rabbit.png
%{_datadir}/faces/Ring.png
%{_datadir}/faces/Scream.png
%{_datadir}/faces/Shark.png
%{_datadir}/faces/Splash.png
%{_datadir}/faces/Star.png
%{_datadir}/faces/Teddybear.png
%{_datadir}/faces/Turtle.png

%post -n trinity-tdepasswd
update-desktop-database %{tde_tdeappdir} 2> /dev/null || : 

%postun -n trinity-tdepasswd
update-desktop-database %{tde_tdeappdir} 2> /dev/null || : 

##########

%package -n trinity-tdeprint
Summary:	Print system for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}
Requires:	psutils

%description -n trinity-tdeprint
This package contains the TDE printing subsystem. It can use CUPS,
lpd-ng or the traditional lpd. It also includes support for fax and
pdf printing.

Installation of smbclient will make you able to use smb shared printers.

%files -n trinity-tdeprint
%defattr(-,root,root,-)
%{tde_bindir}/kdeprintfax
%{tde_bindir}/kjobviewer
%{tde_bindir}/kprinter
%{tde_tdelibdir}/kcm_printmgr.la
%{tde_tdelibdir}/kcm_printmgr.so
%{tde_tdelibdir}/kio_print.la
%{tde_tdelibdir}/kio_print.so
%{tde_tdelibdir}/kjobviewer.la
%{tde_tdelibdir}/kjobviewer.so
%{tde_tdelibdir}/kprinter.la
%{tde_tdelibdir}/kprinter.so
%{tde_tdelibdir}/libkdeprint_part.la
%{tde_tdelibdir}/libkdeprint_part.so
%{tde_libdir}/libkdeinit_kjobviewer.la
%{tde_libdir}/libkdeinit_kjobviewer.so
%{tde_libdir}/libkdeinit_kprinter.la
%{tde_libdir}/libkdeinit_kprinter.so
%{tde_tdeappdir}/kdeprintfax.desktop
%{tde_tdeappdir}/kjobviewer.desktop
%{tde_tdeappdir}/printers.desktop
%{tde_datadir}/apps/kdeprint/
%{tde_datadir}/apps/kdeprintfax/
%{tde_datadir}/apps/kjobviewer/
%{tde_datadir}/apps/kdeprint_part/
%{tde_datadir}/icons/hicolor/*/apps/kdeprintfax.png
%{tde_datadir}/icons/hicolor/*/apps/kjobviewer.png
%{tde_datadir}/icons/hicolor/*/apps/printmgr.png
%{tde_datadir}/icons/hicolor/scalable/apps/kdeprintfax.svgz
%{tde_datadir}/icons/hicolor/scalable/apps/kjobviewer.svgz
%{tde_datadir}/icons/hicolor/scalable/apps/printmgr.svgz
%{tde_datadir}/mimelnk/print/class.desktop
%{tde_datadir}/mimelnk/print/driver.desktop
%{tde_datadir}/mimelnk/print/folder.desktop
%{tde_datadir}/mimelnk/print/jobs.desktop
%{tde_datadir}/mimelnk/print/manager.desktop
%{tde_datadir}/mimelnk/print/printer.desktop
%{tde_datadir}/mimelnk/print/printermodel.desktop
%{tde_datadir}/services/kdeprint_part.desktop
%{tde_datadir}/services/print.protocol
%{tde_datadir}/services/printdb.protocol
%{tde_tdedocdir}/HTML/en/kdeprint/

%post -n trinity-tdeprint
/sbin/ldconfig || :
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

%postun -n trinity-tdeprint
/sbin/ldconfig || :
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-kdesktop
Summary:	Miscellaneous binaries and files for the TDE desktop
Group:		System/GUI/Other
Requires:	%{name}-bin = %{version}-%{release}
Requires:	%{name}-data = %{version}-%{release}
Requires:	trinity-libkonq = %{version}-%{release}
Requires:	eject
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
Requires:	xdg-utils
%endif

%description -n trinity-kdesktop
This package contains miscellaneous binaries and files integral to
the TDE desktop.

%files -n trinity-kdesktop
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/kdesktop_custom_menu1
%config(noreplace) %{_sysconfdir}/trinity/kdesktop_custom_menu2
%{tde_bindir}/kcheckrunning
%{tde_bindir}/kxdglauncher
%{tde_bindir}/kdeeject
%{tde_bindir}/kdesktop
%{tde_bindir}/kdesktop_lock
%{tde_bindir}/kwebdesktop
%{tde_tdelibdir}/kdesktop.la
%{tde_tdelibdir}/kdesktop.so
%{tde_libdir}/libkdeinit_kdesktop.la
%{tde_libdir}/libkdeinit_kdesktop.so
%{tde_datadir}/apps/kdesktop/
%{tde_datadir}/apps/konqueror/servicemenus/kdesktopSetAsBackground.desktop
%{tde_datadir}/autostart/kdesktop.desktop
%{tde_datadir}/config.kcfg/kdesktop.kcfg
%{tde_datadir}/config.kcfg/klaunch.kcfg
%{tde_datadir}/config.kcfg/kwebdesktop.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/error.png

%post -n trinity-kdesktop
/sbin/ldconfig || :
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

%postun -n trinity-kdesktop
/sbin/ldconfig || :
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-kdesktop-devel
Summary:	Development files for kdesktop
Group:		Development/Libraries/Other
Requires:	trinity-kdesktop = %{version}-%{release}

%description -n trinity-kdesktop-devel
This package contains the development files for kdesktop.

%files -n trinity-kdesktop-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/KBackgroundIface.h
%{tde_tdeincludedir}/KDesktopIface.h
%{tde_tdeincludedir}/KScreensaverIface.h

##########

%package -n trinity-tdm
Summary:	X Display manager for TDE
Group:		System/GUI/Other
Requires:	%{name}-bin = %{version}-%{release}
Requires:	%{name}-data = %{version}-%{release}
Requires:	pam
Requires:	logrotate

# Provides the global Xsession script (/etc/X11/xinit/Xsession or /etc/X11/Xsession)
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} == 4
Requires:	xinitrc
%endif
%if 0%{?suse_version} == 1140
Requires:	xorg-x11
%endif
%if 0%{?suse_version} >= 1220
Requires:	xdm
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora}
Requires:	xorg-x11-xinit
%endif

# Required for Fedora LiveCD
%if 0%{?rhel} || 0%{?fedora}
Provides:	service(graphical-login)
%endif
# Required for Mandriva's installer
%if 0%{?mgaversion} || 0%{?mdkversion}
Provides:	dm
Provides:	%{tdm}
%endif

%description -n trinity-tdm
TDM manages a collection of X servers, which may be on the local host or
remote machines. It provides services similar to those provided by init,
getty, and login on character-based terminals: prompting for login name and
password, authenticating the user, and running a session. tdm supports XDMCP
(X Display Manager Control Protocol) and can also be used to run a chooser
process which presents the user with a menu of possible hosts that offer
XDMCP display management.

A collection of icons to associate with individual users is included with
TDE, but as part of the tdepasswd package.

The menu package will help to provide TDM with a list of window managers
that can be launched, if the window manager does not register with TDM
already. Most users won't need this.

%files -n trinity-tdm
%defattr(-,root,root,-)
%{tde_tdelibdir}/kgreet_pam.la
%{tde_tdelibdir}/kgreet_pam.so
%{tde_bindir}/gen%{tdm}conf
%{tde_bindir}/%{tdm}
%{tde_bindir}/%{tdm}_config
%{tde_bindir}/%{tdm}ctl
%{tde_bindir}/%{tdm}_greet
%{tde_bindir}/krootimage
%dir %{tdm_datadir}
%dir %{tdm_datadir}/pics
%{tdm_datadir}/pics/kdelogo.png
%{tdm_datadir}/pics/kdelogo-crystal.png
%{tdm_datadir}/pics/shutdown.jpg
%{tdm_datadir}/pics/users
%dir %{tdm_datadir}/sessions
%{tdm_datadir}/sessions/*.desktop
%{tdm_datadir}/themes/
%{tde_datadir}/config/%{tdm}
%dir %{_sysconfdir}/trinity/%{tdm}
%if 0%{?with_selinux_policy}
%exclude %{?_sysconfdir}/trinity/%{tdm}/tdm.pp
%endif
%config(noreplace) %{_sysconfdir}/trinity/%{tdm}/*
%{tde_tdedocdir}/HTML/en/%{tdm}/
%if 0%{?suse_version} == 0
%config(noreplace) %{_sysconfdir}/pam.d/tdm-trinity
%config(noreplace) %{_sysconfdir}/pam.d/tdm-trinity-np
%endif

# XDG user faces
%dir %{_datadir}/faces
%{_datadir}/faces/default1.png
%{_datadir}/faces/default2.png
%{_datadir}/faces/default3.png
%{_datadir}/faces/root1.png

# Distribution specific stuff
%if 0%{?suse_version} == 1140
%{_sysconfdir}/init.d/xdm.tde
%endif
%if 0%{?suse_version} >= 1210
/usr/lib/X11/displaymanagers/tdm
%endif
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
/usr/lib/systemd/system/tdm.service
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%{_datadir}/xsessions/tde.desktop
%endif

# https://wiki.mageia.org/en/How_to_add_a_new_Window_Manager_or_Display_Manager
%if 0%{?mgaversion} || 0%{?mdkversion}
%{_sysconfdir}/X11/wmsession.d/45TDE
%{_datadir}/X11/dm.d/45TDE.conf
%endif

# SELINUX policy
%if 0%{?with_selinux_policy}
%{?_sysconfdir}/trinity/%{tdm}/tdm.pp
%endif

# Logrotate configuration
%config %{_sysconfdir}/logrotate.d/trinity-tdm

%pre -n trinity-tdm
# Make sure that TDM configuration files are now under '/etc/trinity/tdm'
if [ -d "%{tde_datadir}/config/%{tdm}" ] && [ ! -L "%{tde_datadir}/config/%{tdm}" ]; then
  if [ -d "%{_sysconfdir}/trinity/%{tdm}" ]; then
    # If there is already something under '/etc/trinity/tdm', simply delete old configuration
    echo "Deleting TDM configuration under '%{tde_datadir}/config/%{tdm}'"
    rm -rf "%{tde_datadir}/config/%{tdm}"
  else
    # Else, move '/opt/trinity/share/config/tdm' to '/etc/trinity/tdm'
    if [ ! -d "%{_sysconfdir}/trinity" ]; then
      mkdir -p "%{_sysconfdir}/trinity"
    fi
    echo "Migrating TDM configuration from '%{tde_datadir}/config/%{tdm}' to '%{_sysconfdir}/trinity/%{tdm}'"
    mv -f "%{tde_datadir}/config/%{tdm}" "%{_sysconfdir}/trinity/%{tdm}.migr"
  fi
fi

# Remove actual directory before creating a symlink
if [ ! -L "%{tdm_datadir}/pics/users" ]; then
  [ -d "%{_datadir}/faces" ] || mkdir -p "%{_datadir}/faces"
  cp -f "%{tdm_datadir}/pics/users/"* "%{_datadir}/faces"
  rm -rf "%{tdm_datadir}/pics/users"
fi

%post -n trinity-tdm
%if 0%{?mgaversion} || 0%{?mdkversion}
%make_session
%endif
%if 0%{?with_selinux_policy}
/usr/sbin/semodule -i "%{?_sysconfdir}/trinity/%{tdm}/tdm.pp"
%endif

# Sets default user icon in TDM
if [ ! -r "%{tdm_datadir}/faces/.default.face.icon" ]; then
  [ -d "%{tdm_datadir}/faces" ] || mkdir -p "%{tdm_datadir}/faces"
  cp -f "%{tdm_datadir}/pics/users/default2.png" "%{tdm_datadir}/faces/.default.face.icon"
fi

# Sets default language for TDM
if [ "$1" = "1" ]; then
  if [ -n "${LANG}" ] && [ "${LANG}" != "C" ]; then
    sed -i "%{_sysconfdir}/trinity/%{tdm}/%{tdm}rc" -e "s|^#*Language=.*|Language=${LANG}|"
  fi
fi

# openSUSE 11.4 tdm's startup script
if [ -r "%{_sysconfdir}/init.d/xdm.tde" ]; then
  cat "%{_sysconfdir}/init.d/xdm.tde" >"%{_sysconfdir}/init.d/xdm"
fi


%posttrans -n trinity-tdm
# Make sure that TDM configuration files are now under '/etc/trinity/tdm'
if [ -d "%{_sysconfdir}/trinity/%{tdm}.migr" ] && [ -d "%{_sysconfdir}/trinity/%{tdm}" ]; then
  mv -f "%{_sysconfdir}/trinity/%{tdm}.migr/"* "%{_sysconfdir}/trinity/%{tdm}/"
  rmdir "%{_sysconfdir}/trinity/%{tdm}.migr/"
fi

%postun -n trinity-tdm
%if 0%{?mgaversion} || 0%{?mdkversion}
%make_session
%endif

##########

%package -n trinity-tdm-devel
Summary:	Development files for tdm
Group:		Development/Libraries/Other
Requires:	trinity-tdm = %{version}-%{release}
%{?xtst_devel:Requires: %{xtst_devel}}

%description -n trinity-tdm-devel
This package contains the development files for TDM.

%files -n trinity-tdm-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kgreeterplugin.h

##########

%package -n trinity-kfind
Summary:	File-find utility for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-kfind
kfind can be used to find files and directories on your
workstations.

%files -n trinity-kfind
%defattr(-,root,root,-)
%{tde_bindir}/kfind
%{tde_tdelibdir}/libkfindpart.la
%{tde_tdelibdir}/libkfindpart.so
%{tde_tdeappdir}/Kfind.desktop
%{tde_datadir}/apps/kfindpart/
%{tde_datadir}/icons/hicolor/*/apps/kfind.png
%{tde_datadir}/services/kfindpart.desktop
%{tde_datadir}/servicetypes/findpart.desktop
%{tde_tdedocdir}/HTML/en/kfind/

%post -n trinity-kfind
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

%postun -n trinity-kfind
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-khelpcenter
Summary:	Help center for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}
Requires:	htdig

%description -n trinity-khelpcenter
The TDE Help Center provides documentation on how to use the TDE desktop.

The htdig package is needed to build a searchable archive of TDE
documentation.

%files -n trinity-khelpcenter
%defattr(-,root,root,-)
%{tde_bindir}/khc_docbookdig.pl
%{tde_bindir}/khc_htdig.pl
%{tde_bindir}/khc_htsearch.pl
%{tde_bindir}/khc_indexbuilder
%{tde_bindir}/khc_mansearch.pl
%{tde_bindir}/khelpcenter
%{tde_tdelibdir}/khelpcenter.la
%{tde_tdelibdir}/khelpcenter.so
%{tde_libdir}/libkdeinit_khelpcenter.la
%{tde_libdir}/libkdeinit_khelpcenter.so
%{tde_tdeappdir}/Help.desktop
%{tde_datadir}/apps/khelpcenter/
%{tde_datadir}/config.kcfg/khelpcenter.kcfg
%{tde_datadir}/icons/hicolor/*/apps/khelpcenter.*
%{tde_datadir}/services/khelpcenter.desktop
%{tde_tdedocdir}/HTML/en/khelpcenter/

%post -n trinity-khelpcenter
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%postun -n trinity-khelpcenter
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

##########

%package -n trinity-kicker
Summary:	Desktop panel for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-kicker
Kicker provides the TDE panel on you desktop. It can be used as a
program launcher and can load plugins to provide additional
functionality.

%files -n trinity-kicker
%defattr(-,root,root,-)
%{tde_bindir}/appletproxy
%{tde_bindir}/extensionproxy
%{tde_bindir}/kasbar
%{tde_bindir}/kicker
%{tde_libdir}/kconf_update_bin/kicker-3.4-reverseLayout
%{tde_tdelibdir}/appletproxy.la
%{tde_tdelibdir}/appletproxy.so
%{tde_tdelibdir}/clock_panelapplet.la
%{tde_tdelibdir}/clock_panelapplet.so
%{tde_tdelibdir}/dockbar_panelextension.la
%{tde_tdelibdir}/dockbar_panelextension.so
%{tde_tdelibdir}/extensionproxy.la
%{tde_tdelibdir}/extensionproxy.so
%{tde_tdelibdir}/kasbar_panelextension.la
%{tde_tdelibdir}/kasbar_panelextension.so
%{tde_tdelibdir}/kicker.la
%{tde_tdelibdir}/kickermenu_find.la
%{tde_tdelibdir}/kickermenu_find.so
%{tde_tdelibdir}/kickermenu_kate.so
%{tde_tdelibdir}/kickermenu_kate.la
%{tde_tdelibdir}/kickermenu_kdeprint.la
%{tde_tdelibdir}/kickermenu_kdeprint.so
%{tde_tdelibdir}/kickermenu_konqueror.la
%{tde_tdelibdir}/kickermenu_konqueror.so
%{tde_tdelibdir}/kickermenu_konsole.la
%{tde_tdelibdir}/kickermenu_konsole.so
%{tde_tdelibdir}/kickermenu_prefmenu.la
%{tde_tdelibdir}/kickermenu_prefmenu.so
%{tde_tdelibdir}/kickermenu_recentdocs.la
%{tde_tdelibdir}/kickermenu_recentdocs.so
%{tde_tdelibdir}/kickermenu_remotemenu.la
%{tde_tdelibdir}/kickermenu_remotemenu.so
%{tde_tdelibdir}/kickermenu_systemmenu.la
%{tde_tdelibdir}/kickermenu_systemmenu.so
%{tde_tdelibdir}/kicker.so
%{tde_tdelibdir}/launcher_panelapplet.la
%{tde_tdelibdir}/launcher_panelapplet.so
%{tde_tdelibdir}/lockout_panelapplet.la
%{tde_tdelibdir}/lockout_panelapplet.so
%{tde_tdelibdir}/media_panelapplet.la
%{tde_tdelibdir}/media_panelapplet.so
%{tde_tdelibdir}/menu_panelapplet.la
%{tde_tdelibdir}/menu_panelapplet.so
%{tde_tdelibdir}/minipager_panelapplet.la
%{tde_tdelibdir}/minipager_panelapplet.so
%{tde_tdelibdir}/naughty_panelapplet.la
%{tde_tdelibdir}/naughty_panelapplet.so
%{tde_tdelibdir}/run_panelapplet.la
%{tde_tdelibdir}/run_panelapplet.so
%{tde_tdelibdir}/sidebar_panelextension.la
%{tde_tdelibdir}/sidebar_panelextension.so
%{tde_tdelibdir}/systemtray_panelapplet.la
%{tde_tdelibdir}/systemtray_panelapplet.so
%{tde_tdelibdir}/taskbar_panelapplet.la
%{tde_tdelibdir}/taskbar_panelapplet.so
%{tde_tdelibdir}/taskbar_panelextension.la
%{tde_tdelibdir}/taskbar_panelextension.so
%{tde_tdelibdir}/trash_panelapplet.la
%{tde_tdelibdir}/trash_panelapplet.so
%{tde_libdir}/libkasbar.so.*
%{tde_libdir}/libkdeinit_appletproxy.la
%{tde_libdir}/libkdeinit_appletproxy.so
%{tde_libdir}/libkdeinit_extensionproxy.la
%{tde_libdir}/libkdeinit_extensionproxy.so
%{tde_libdir}/libkdeinit_kicker.la
%{tde_libdir}/libkdeinit_kicker.so
%{tde_libdir}/libkickermain.so.*
%{tde_libdir}/libtaskbar.so.*
%{tde_libdir}/libtaskmanager.so.*
%{tde_libdir}/libkickoffsearch_interfaces.so.*
%{tde_tdeappdir}/kcmkicker.desktop
%{tde_datadir}/applnk/.hidden/kicker_config_arrangement.desktop
%{tde_datadir}/applnk/.hidden/kicker_config_hiding.desktop
%{tde_datadir}/applnk/.hidden/kicker_config_menus.desktop
%{tde_datadir}/apps/clockapplet/
%{tde_datadir}/apps/kconf_update/kicker-3.1-properSizeSetting.pl
%{tde_datadir}/apps/kconf_update/kicker-3.5-kconfigXTize.pl
%{tde_datadir}/apps/kconf_update/kicker-3.5-taskbarEnums.pl
%{tde_datadir}/apps/kconf_update/kickerrc.upd
%{tde_datadir}/apps/kicker/
%exclude %{tde_datadir}/apps/kicker/applets/klipper.desktop
%exclude %{tde_datadir}/apps/kicker/applets/ksysguardapplet.desktop
%{tde_datadir}/apps/naughtyapplet/
%{tde_datadir}/autostart/panel.desktop
%{tde_datadir}/config.kcfg/kickerSettings.kcfg
%{tde_datadir}/config.kcfg/launcherapplet.kcfg
%{tde_datadir}/config.kcfg/pagersettings.kcfg
%{tde_datadir}/config.kcfg/taskbar.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/systemtray.png
%{tde_datadir}/icons/crystalsvg/*/apps/taskbar.png
%{tde_datadir}/icons/crystalsvg/*/apps/kbinaryclock.png
%{tde_datadir}/icons/crystalsvg/*/apps/kdisknav.png
%{tde_datadir}/icons/crystalsvg/*/apps/kicker.png
%{tde_datadir}/icons/crystalsvg/*/apps/panel.png
%{tde_datadir}/icons/crystalsvg/*/apps/runprocesscatcher.png
%{tde_datadir}/icons/crystalsvg/*/apps/window_list.png
%{tde_datadir}/icons/crystalsvg/*/apps/kbinaryclock.svgz
%{tde_datadir}/icons/crystalsvg/*/apps/systemtray.svgz
%{tde_datadir}/servicetypes/kickoffsearchplugin.desktop
%{tde_tdedocdir}/HTML/en/kicker/
%if 0%{?mgaversion} >= 3
%{tde_datadir}/oxygen/scalable/mgabutton.svg
%endif

%post -n trinity-kicker
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%postun -n trinity-kicker
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

##########

%package -n trinity-kicker-devel
Summary:	Development files for kicker
Group:		Development/Libraries/Other
Requires:	trinity-kicker = %{version}-%{release}
%{?xtst_devel:Requires: %{xtst_devel}}

%description -n trinity-kicker-devel
This package contains the development files for kicker.

%files -n trinity-kicker-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kickoff-search-plugin.h
%{tde_tdeincludedir}/kickoffsearchinterface.h
%{tde_libdir}/libkasbar.la
%{tde_libdir}/libkasbar.so
%{tde_libdir}/libkickermain.la
%{tde_libdir}/libkickermain.so
%{tde_libdir}/libkickoffsearch_interfaces.la
%{tde_libdir}/libkickoffsearch_interfaces.so
%{tde_libdir}/libtaskbar.la
%{tde_libdir}/libtaskbar.so
%{tde_libdir}/libtaskmanager.la
%{tde_libdir}/libtaskmanager.so

%post -n trinity-kicker-devel
/sbin/ldconfig || :

%postun -n trinity-kicker-devel
/sbin/ldconfig || :

##########

%package -n trinity-klipper
Summary:	Clipboard utility for Trinity
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-klipper
klipper provides standard clipboard functions (cut and paste, history
saving) plus additional features, like the ability to offer actions to 
take dependent on the clipboard contents. For example, it can launch a 
web browser if the clipboard contains a URL.

%files -n trinity-klipper
%defattr(-,root,root,-)
%{tde_bindir}/klipper
%config(noreplace) %{_sysconfdir}/trinity/klipperrc
%{tde_tdelibdir}/klipper.la
%{tde_tdelibdir}/klipper.so
%{tde_tdelibdir}/klipper_panelapplet.la
%{tde_tdelibdir}/klipper_panelapplet.so
%{tde_libdir}/libkdeinit_klipper.la
%{tde_libdir}/libkdeinit_klipper.so
%{tde_tdeappdir}/klipper.desktop
%{tde_datadir}/apps/kconf_update/klipper-1-2.pl
%{tde_datadir}/apps/kconf_update/klipper-trinity1.sh
%{tde_datadir}/apps/kconf_update/klipperrc.upd
%{tde_datadir}/apps/kconf_update/klippershortcuts.upd
%{tde_datadir}/apps/kicker/applets/klipper.desktop
%{tde_datadir}/autostart/klipper.desktop
%{tde_datadir}/icons/hicolor/*/apps/klipper.*
%{tde_tdedocdir}/HTML/en/klipper/

%post -n trinity-klipper
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%postun -n trinity-klipper
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

##########

%package -n trinity-kmenuedit
Summary:	Menu editor for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-kmenuedit
The TDE menu editor allows you to make customisations to the TDE menu
structure.

%files -n trinity-kmenuedit
%defattr(-,root,root,-)
%{tde_bindir}/kcontroledit
%{tde_bindir}/kmenuedit
%{tde_tdelibdir}/kcontroledit.la
%{tde_tdelibdir}/kcontroledit.so
%{tde_tdelibdir}/kmenuedit.la
%{tde_tdelibdir}/kmenuedit.so
%{tde_libdir}/libkdeinit_kcontroledit.la
%{tde_libdir}/libkdeinit_kcontroledit.so
%{tde_libdir}/libkdeinit_kmenuedit.la
%{tde_libdir}/libkdeinit_kmenuedit.so
%{tde_tdeappdir}/kmenuedit.desktop
%{tde_datadir}/applnk/System/kmenuedit.desktop
%{tde_datadir}/apps/kcontroledit/
%{tde_datadir}/apps/kmenuedit/
%{tde_tdedocdir}/HTML/en/kmenuedit/

%post -n trinity-kmenuedit
update-desktop-database %{tde_appdir} 2> /dev/null || : 
/sbin/ldconfig || :

%postun -n trinity-kmenuedit
update-desktop-database %{tde_appdir} 2> /dev/null || : 
/sbin/ldconfig || :

##########

%package -n trinity-konqueror
Summary:	TDE's advanced file manager, web browser and document viewer
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}
Requires:	trinity-kcontrol = %{version}-%{release}
Requires:	%{name}-tdeio-plugins = %{version}-%{release}
Requires:	trinity-kdesktop = %{version}-%{release}
Requires:	trinity-kfind = %{version}-%{release}
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
%config(noreplace) %{_sysconfdir}/trinity/konqsidebartng.rc
%{tde_bindir}/kbookmarkmerger
%{tde_bindir}/keditbookmarks
%{tde_bindir}/kfmclient
%{tde_bindir}/konqueror
%{tde_tdelibdir}/kcm_history.la
%{tde_tdelibdir}/kcm_history.so
%{tde_tdelibdir}/kded_konqy_preloader.la
%{tde_tdelibdir}/kded_konqy_preloader.so
%{tde_tdelibdir}/keditbookmarks.la
%{tde_tdelibdir}/keditbookmarks.so
%{tde_tdelibdir}/kfmclient.la
%{tde_tdelibdir}/kfmclient.so
%{tde_tdelibdir}/konq_aboutpage.la
%{tde_tdelibdir}/konq_aboutpage.so
%{tde_tdelibdir}/konq_iconview.la
%{tde_tdelibdir}/konq_iconview.so
%{tde_tdelibdir}/konq_listview.la
%{tde_tdelibdir}/konq_listview.so
%{tde_tdelibdir}/konq_remoteencoding.la
%{tde_tdelibdir}/konq_remoteencoding.so
%{tde_tdelibdir}/konq_shellcmdplugin.la
%{tde_tdelibdir}/konq_shellcmdplugin.so
%{tde_tdelibdir}/konq_sidebar.la
%{tde_tdelibdir}/konq_sidebar.so
%{tde_tdelibdir}/konq_sidebartree_bookmarks.la
%{tde_tdelibdir}/konq_sidebartree_bookmarks.so
%{tde_tdelibdir}/konq_sidebartree_dirtree.la
%{tde_tdelibdir}/konq_sidebartree_dirtree.so
%{tde_tdelibdir}/konq_sidebartree_history.la
%{tde_tdelibdir}/konq_sidebartree_history.so
%{tde_tdelibdir}/konqsidebar_tree.la
%{tde_tdelibdir}/konqsidebar_tree.so
%{tde_tdelibdir}/konqsidebar_web.la
%{tde_tdelibdir}/konqsidebar_web.so
%{tde_tdelibdir}/konqueror.la
%{tde_tdelibdir}/konqueror.so
%{tde_tdelibdir}/libkhtmlkttsdplugin.la
%{tde_tdelibdir}/libkhtmlkttsdplugin.so
%{tde_libdir}/libkdeinit_keditbookmarks.la
%{tde_libdir}/libkdeinit_keditbookmarks.so
%{tde_libdir}/libkdeinit_kfmclient.la
%{tde_libdir}/libkdeinit_kfmclient.so
%{tde_libdir}/libkdeinit_konqueror.la
%{tde_libdir}/libkdeinit_konqueror.so
%{tde_libdir}/libkonqsidebarplugin.so.*
%{tde_tdeappdir}/Home.desktop
%{tde_tdeappdir}/kcmhistory.desktop
%{tde_tdeappdir}/kfmclient.desktop
%{tde_tdeappdir}/kfmclient_dir.desktop
%{tde_tdeappdir}/kfmclient_html.desktop
%{tde_tdeappdir}/kfmclient_war.desktop
%{tde_tdeappdir}/khtml_filter.desktop
%{tde_tdeappdir}/konqbrowser.desktop
%{tde_tdeappdir}/konquerorsu.desktop
%{tde_datadir}/applnk/.hidden/konqfilemgr.desktop
%{tde_datadir}/applnk/Internet/keditbookmarks.desktop
%{tde_datadir}/applnk/konqueror.desktop
%{tde_datadir}/apps/kconf_update/kfmclient_3_2.upd
%{tde_datadir}/apps/kconf_update/kfmclient_3_2_update.sh
%{tde_datadir}/apps/kconf_update/konqsidebartng.upd
%{tde_datadir}/apps/kconf_update/move_konqsidebartng_entries.sh
%{tde_datadir}/apps/keditbookmarks/
%{tde_datadir}/apps/khtml/kpartplugins/
%{tde_datadir}/apps/konqiconview/
%{tde_datadir}/apps/konqlistview/
%exclude %{tde_datadir}/apps/konqsidebartng/virtual_folders/services/fonts.desktop
%{tde_datadir}/apps/konqsidebartng/
%{tde_datadir}/apps/konqueror/about/
%dir %{tde_datadir}/apps/konqueror/dirtree
%dir %{tde_datadir}/apps/konqueror/dirtree/remote
%{tde_datadir}/apps/konqueror/icons/
%{tde_datadir}/apps/konqueror/konq-simplebrowser.rc
%{tde_datadir}/apps/konqueror/konqueror.rc
%{tde_datadir}/apps/konqueror/pics/indicator_connect.png
%{tde_datadir}/apps/konqueror/pics/indicator_empty.png
%{tde_datadir}/apps/konqueror/pics/indicator_noconnect.png
%{tde_datadir}/apps/konqueror/pics/indicator_viewactive.png
%{tde_datadir}/apps/konqueror/profiles/
%exclude %{tde_datadir}/apps/konqueror/servicemenus/kdesktopSetAsBackground.desktop
%exclude %{tde_datadir}/apps/konqueror/servicemenus/konsolehere.desktop
%exclude %{tde_datadir}/apps/konqueror/servicemenus/installfont.desktop
%{tde_datadir}/apps/konqueror/servicemenus/*.desktop
%ghost %{_sysconfdir}/alternatives/media_safelyremove.desktop
%{tde_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase
%{tde_datadir}/apps/konqueror/tiles/
%{tde_datadir}/autostart/konqy_preload.desktop
%{tde_datadir}/config.kcfg/keditbookmarks.kcfg
%{tde_datadir}/config.kcfg/konq_listview.kcfg
%{tde_datadir}/config.kcfg/konqueror.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/keditbookmarks.png
%{tde_datadir}/icons/crystalsvg/*/apps/kfm_home.svgz
%{tde_datadir}/icons/hicolor/*/apps/kfm.png
%{tde_datadir}/icons/hicolor/*/apps/konqueror.*
%{tde_datadir}/services/kded/konqy_preloader.desktop
%{tde_datadir}/services/konq_*.desktop
%{tde_datadir}/servicetypes/konqaboutpage.desktop
%{tde_tdedocdir}/HTML/en/konqueror/

%post -n trinity-konqueror
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :
if [ $1 -eq 1 ]; then
  update-alternatives --install \
    %{tde_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop \
    media_safelyremove.desktop_konqueror \
    %{tde_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase \
    10 || :
fi

%postun -n trinity-konqueror
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%preun -n trinity-konqueror
if [ $1 -eq 0 ]; then
  update-alternatives --remove \
    media_safelyremove.desktop_konqueror \
    %{tde_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase || :
fi

##########

%package -n trinity-konqueror-devel
Summary:	Development files for konqueror
Group:		Development/Libraries/Other
Requires:	trinity-konqueror = %{version}-%{release}

%description -n trinity-konqueror-devel
This package contains the development files for konqueror.

%files -n trinity-konqueror-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/konqsidebarplugin.h
%{tde_tdeincludedir}/KonquerorIface.h
%{tde_libdir}/libkonqsidebarplugin.la
%{tde_libdir}/libkonqsidebarplugin.so

%post -n trinity-konqueror-devel
/sbin/ldconfig || :

%postun -n trinity-konqueror-devel
/sbin/ldconfig || :

##########

%package -n trinity-konqueror-nsplugins
Summary:	Netscape plugin support for Konqueror
Group:		System/GUI/Other
Requires:	trinity-konqueror = %{version}-%{release}

%description -n trinity-konqueror-nsplugins
This package includes support for Netscape plugins in Konqueror.

%files -n trinity-konqueror-nsplugins
%defattr(-,root,root,-)
%{tde_bindir}/nspluginscan
%{tde_bindir}/nspluginviewer
%{tde_tdelibdir}/kcm_nsplugins.la
%{tde_tdelibdir}/kcm_nsplugins.so
%{tde_tdelibdir}/libnsplugin.la
%{tde_tdelibdir}/libnsplugin.so
%{tde_tdeappdir}/khtml_plugins.desktop
%{tde_datadir}/apps/plugin/nspluginpart.rc

%post -n trinity-konqueror-nsplugins
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun -n trinity-konqueror-nsplugins
update-desktop-database %{tde_appdir} 2> /dev/null || : 

##########

%package -n trinity-konsole
Summary:	X terminal emulator for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-konsole
Konsole is an X terminal emulation which provides a command-line interface
(CLI) while using the graphical Trinity Desktop Environment. Konsole helps to
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
%{tde_bindir}/konsole
%{tde_tdelibdir}/kcm_konsole.la
%{tde_tdelibdir}/kcm_konsole.so
%{tde_tdelibdir}/kded_kwrited.la
%{tde_tdelibdir}/kded_kwrited.so
%{tde_tdelibdir}/konsole.la
%{tde_tdelibdir}/konsole.so
%{tde_tdelibdir}/libkonsolepart.la
%{tde_tdelibdir}/libkonsolepart.so
%{tde_libdir}/libkdeinit_konsole.la
%{tde_libdir}/libkdeinit_konsole.so
%{tde_tdeappdir}/konsole.desktop
%{tde_tdeappdir}/konsolesu.desktop
%{tde_datadir}/applnk/.hidden/kcmkonsole.desktop
%{tde_datadir}/apps/kconf_update/konsole.upd
%{tde_datadir}/apps/kconf_update/schemaStrip.pl
%{tde_datadir}/apps/konqueror/servicemenus/konsolehere.desktop
%{tde_datadir}/apps/konsole/
%{tde_datadir}/icons/hicolor/*/apps/konsole.*
%{tde_datadir}/mimelnk/application/x-konsole.desktop
%{tde_datadir}/services/kded/kwrited.desktop
%{tde_datadir}/services/konsolepart.desktop
%{tde_datadir}/services/konsole-script.desktop
%{tde_datadir}/services/kwrited.desktop
%{tde_datadir}/servicetypes/terminalemulator.desktop
%{tde_tdedocdir}/HTML/en/konsole/
%{tde_tdedocdir}/HTML/en/kcontrol/kcmkonsole/
%config %{_sysconfdir}/fonts/conf.d/99-konsole.conf

%post -n trinity-konsole
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%postun -n trinity-konsole
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

##########

%package -n trinity-kpager
Summary:	Desktop pager for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-kpager
This package contains TDE's desktop pager, which displays your virtual
desktops iconically in a window, along with icons of any running
applications. It is used to switch between applications or desktops.

%files -n trinity-kpager
%defattr(-,root,root,-)
%{tde_bindir}/kpager
%{tde_tdeappdir}/kpager.desktop
%{tde_datadir}/applnk/Utilities/kpager.desktop
%{tde_datadir}/icons/hicolor/*/apps/kpager.png
%{tde_tdedocdir}/HTML/en/kpager/

%post -n trinity-kpager
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

%postun -n trinity-kpager
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-kpersonalizer
Summary:	Installation personalizer for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-kpersonalizer
TDE Personalizer is the application that configures the TDE desktop for you.
It's a very useful wizard that allows you to quickly change the TDE desktop to
suit your own needs. When you run TDE for the first time, KPersonalizer is
automatically started. KPersonalizer can also be called later.

%files -n trinity-kpersonalizer
%defattr(-,root,root,-)
%{tde_bindir}/kpersonalizer
%{tde_tdeappdir}/kpersonalizer.desktop
%{tde_datadir}/applnk/System/kpersonalizer.desktop
%{tde_datadir}/apps/kpersonalizer/
%{tde_datadir}/icons/crystalsvg/*/apps/kpersonalizer.png

%post -n trinity-kpersonalizer
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

%postun -n trinity-kpersonalizer
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-ksmserver
Summary:	Session manager for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}
Requires:	trinity-twin = %{version}-%{release}

%description -n trinity-ksmserver
This package contains the TDE session manager. It is responsible for
restoring your TDE session on login. It is also needed to properly
start a TDE session. It registers TDE with X display managers, and
provides the 'starttde' command, for starting an X session with TDE
from the console.

If you are running TDE for the first time for a certain user,
kpersonalizer is used to help with setup. If it is not present,
TDE will start, but many good defaults will not be set.

%files -n trinity-ksmserver
%defattr(-,root,root,-)
%{tde_bindir}/ksmserver
%{tde_bindir}/%{starttde}
%{tde_bindir}/migratekde3
%{tde_tdelibdir}/ksmserver.la
%{tde_tdelibdir}/ksmserver.so
%{tde_libdir}/libkdeinit_ksmserver.la
%{tde_libdir}/libkdeinit_ksmserver.so
%{tde_datadir}/apps/kconf_update/ksmserver.upd
%{tde_datadir}/apps/kconf_update/move_session_config.sh
%{tde_datadir}/apps/ksmserver/

# Workaround conflict with KDE4
%if "%{?tde_prefix}" != "/usr"
%{tde_bindir}/plasma-desktop
%endif

%post -n trinity-ksmserver
/sbin/ldconfig || :
%if 0%{?mdkversion} || 0%{?mgaversion}
fndSession
%endif

%postun -n trinity-ksmserver
/sbin/ldconfig || :
%if 0%{?mdkversion} || 0%{?mgaversion}
fndSession
%endif

##########

%package -n trinity-ksplash
Summary:	The TDE splash screen
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-ksplash
This package includes the TDE Splash screen, which is seen when
a TDE session is launched.

%files -n trinity-ksplash
%defattr(-,root,root,-)
%{tde_bindir}/ksplash
%{tde_bindir}/ksplashsimple
%{tde_tdelibdir}/kcm_ksplashthemes.la
%{tde_tdelibdir}/kcm_ksplashthemes.so
%{tde_tdelibdir}/ksplashdefault.la
%{tde_tdelibdir}/ksplashdefault.so
%{tde_tdelibdir}/ksplashunified.la
%{tde_tdelibdir}/ksplashunified.so
%{tde_tdelibdir}/ksplashredmond.la
%{tde_tdelibdir}/ksplashredmond.so
%{tde_tdelibdir}/ksplashstandard.la
%{tde_tdelibdir}/ksplashstandard.so
%{tde_libdir}/libksplashthemes.so.*
%{tde_tdeappdir}/ksplashthememgr.desktop
%{tde_datadir}/apps/ksplash
%{tde_datadir}/services/ksplashdefault.desktop
%{tde_datadir}/services/ksplash.desktop
%{tde_datadir}/services/ksplashunified.desktop
%{tde_datadir}/services/ksplashredmond.desktop
%{tde_datadir}/services/ksplashstandard.desktop
%{tde_datadir}/servicetypes/ksplashplugins.desktop
%{tde_tdedocdir}/HTML/en/ksplashml/

%post -n trinity-ksplash
update-desktop-database %{tde_appdir} 2> /dev/null || : 
/sbin/ldconfig || :

%postun -n trinity-ksplash
update-desktop-database %{tde_appdir} 2> /dev/null || : 
/sbin/ldconfig || :

##########

%package -n trinity-ksplash-devel
Summary:	Development files for ksplash
Group:		Development/Libraries/Other
Requires:	trinity-ksplash = %{version}-%{release}

%description -n trinity-ksplash-devel
This package contains the development files for ksplash.

%files -n trinity-ksplash-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/ksplash/
%{tde_libdir}/libksplashthemes.la
%{tde_libdir}/libksplashthemes.so

%post -n trinity-ksplash-devel
/sbin/ldconfig || :

%postun -n trinity-ksplash-devel
/sbin/ldconfig || :

##########

%package -n trinity-ksysguard
Summary:	System guard for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}
Requires:	trinity-ksysguardd = %{version}-%{release}

%description -n trinity-ksysguard
TDE System Guard allows you to monitor various statistics about your
computer.

%files -n trinity-ksysguard
%defattr(-,root,root,-)
%{tde_bindir}/kpm
%{tde_bindir}/ksysguard
%{tde_tdelibdir}/sysguard_panelapplet.la
%{tde_tdelibdir}/sysguard_panelapplet.so
%{tde_libdir}/libksgrd.so.*
%{tde_tdeappdir}/ksysguard.desktop
%{tde_datadir}/apps/kicker/applets/ksysguardapplet.desktop
%{tde_datadir}/apps/ksysguard/
%{tde_datadir}/icons/crystalsvg/*/apps/ksysguard.png
%{tde_datadir}/mimelnk/application/x-ksysguard.desktop
%{tde_tdedocdir}/HTML/en/ksysguard/

%post -n trinity-ksysguard
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%postun -n trinity-ksysguard
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

##########

%package -n trinity-ksysguard-devel
Summary:	Development files for ksysguard
Group:		Development/Libraries/Other
Requires:	trinity-ksysguard = %{version}-%{release}

%description -n trinity-ksysguard-devel
This package contains the development files for ksysguard.

%files -n trinity-ksysguard-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/ksgrd/
%{tde_libdir}/libksgrd.la
%{tde_libdir}/libksgrd.so

%post -n trinity-ksysguard-devel
/sbin/ldconfig || :

%postun -n trinity-ksysguard-devel
/sbin/ldconfig || :

##########

%package -n trinity-ksysguardd
Summary:	System guard daemon for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-ksysguardd
TDE System Guard Daemon is the daemon part of ksysguard. The daemon can
be installed on a remote machine to enable ksysguard on another machine
to monitor it through the daemon running there.

%files -n trinity-ksysguardd
%defattr(-,root,root,-)
%{tde_bindir}/ksysguardd
%config(noreplace) %{_sysconfdir}/trinity/ksysguarddrc

##########

%package -n trinity-ktip
Summary:	Useful tips for TDE
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-ktip
ktip provides many useful tips on using TDE when you log in.

%files -n trinity-ktip
%defattr(-,root,root,-)
%{tde_bindir}/ktip
%{tde_tdeappdir}/ktip.desktop
%{tde_datadir}/applnk/Toys/ktip.desktop
%{tde_datadir}/apps/kdewizard/
%{tde_datadir}/autostart/ktip.desktop
%{tde_datadir}/icons/hicolor/*/apps/ktip.*

%post -n trinity-ktip
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

%postun -n trinity-ktip
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

##########

%package -n trinity-twin
Summary:	The TDE window manager
Group:		System/GUI/Other
Requires:	%{name}-data = %{version}-%{release}

%description -n trinity-twin
This package contains the default X window manager for TDE.

%files -n trinity-twin
%defattr(-,root,root,-)
%{tde_bindir}/kompmgr
%{tde_bindir}/kwin
%{tde_bindir}/kwin_killer_helper
%{tde_bindir}/kwin_rules_dialog
%{tde_libdir}/kconf_update_bin/kwin_update_default_rules
%{tde_libdir}/kconf_update_bin/kwin_update_window_settings
%{tde_tdelibdir}/kcm_kwin*.la
%{tde_tdelibdir}/kcm_kwin*.so
%{tde_tdelibdir}/kwin*.la
%{tde_tdelibdir}/kwin*.so
%{tde_libdir}/libkdecorations.so.*
%{tde_libdir}/libkdeinit_kwin_rules_dialog.la
%{tde_libdir}/libkdeinit_kwin_rules_dialog.so
%{tde_libdir}/libkdeinit_kwin.la
%{tde_libdir}/libkdeinit_kwin.so
%{tde_tdeappdir}/showdesktop.desktop
%{tde_tdeappdir}/kwindecoration.desktop
%{tde_tdeappdir}/kwinoptions.desktop
%{tde_tdeappdir}/kwinrules.desktop
%{tde_datadir}/applnk/.hidden/kwinactions.desktop
%{tde_datadir}/applnk/.hidden/kwinadvanced.desktop
%{tde_datadir}/applnk/.hidden/kwinfocus.desktop
%{tde_datadir}/applnk/.hidden/kwinmoving.desktop
%{tde_datadir}/applnk/.hidden/kwintranslucency.desktop
%{tde_datadir}/apps/kconf_update/kwin3_plugin.pl
%{tde_datadir}/apps/kconf_update/kwin3_plugin.upd
%{tde_datadir}/apps/kconf_update/kwin_focus1.sh
%{tde_datadir}/apps/kconf_update/kwin_focus1.upd
%{tde_datadir}/apps/kconf_update/kwin_focus2.sh
%{tde_datadir}/apps/kconf_update/kwin_focus2.upd
%{tde_datadir}/apps/kconf_update/kwin_fsp_workarounds_1.upd
%{tde_datadir}/apps/kconf_update/kwiniconify.upd
%{tde_datadir}/apps/kconf_update/kwinsticky.upd
%{tde_datadir}/apps/kconf_update/kwin.upd
%{tde_datadir}/apps/kconf_update/kwinupdatewindowsettings.upd
%{tde_datadir}/apps/kconf_update/pluginlibFix.pl
%{tde_datadir}/apps/kwin/
%{tde_datadir}/config.kcfg/kwin.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/kwin.png
%{tde_tdedocdir}/HTML/en/kompmgr/

%post -n trinity-twin
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

%postun -n trinity-twin
update-desktop-database %{tde_appdir} 2> /dev/null || : 
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done
/sbin/ldconfig || :

##########

%package -n trinity-twin-devel
Summary:	Development files for twin
Group:		Development/Libraries/Other
Requires:	trinity-twin = %{version}-%{release}

%description -n trinity-twin-devel
This package contains the development files for twin.

%files -n trinity-twin-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kwin/
%{tde_tdeincludedir}/kcommondecoration.h
%{tde_tdeincludedir}/kdecoration.h
%{tde_tdeincludedir}/kdecoration_p.h
%{tde_tdeincludedir}/kdecoration_plugins_p.h
%{tde_tdeincludedir}/kdecorationfactory.h
%{tde_tdeincludedir}/KWinInterface.h
%{tde_libdir}/libkdecorations.la
%{tde_libdir}/libkdecorations.so

%post -n trinity-twin-devel
/sbin/ldconfig || :

%postun -n trinity-twin-devel
/sbin/ldconfig || :

##########

%package -n trinity-libkonq
Summary:	Core libraries for Konqueror
Group:		System/GUI/Other

%description -n trinity-libkonq
These libraries are used by several TDE applications, most notably
Konqueror and the kdesktop package.

%files -n trinity-libkonq
%defattr(-,root,root,-)
%{tde_tdelibdir}/kded_favicons.la
%{tde_tdelibdir}/kded_favicons.so
%{tde_tdelibdir}/konq_sound.la
%{tde_tdelibdir}/konq_sound.so
%{tde_libdir}/libkonq.so.*
%{tde_datadir}/apps/kbookmark/
%{tde_datadir}/apps/kconf_update/favicons.upd
%{tde_datadir}/apps/kconf_update/move_favicons.sh
%dir %{tde_datadir}/apps/konqueror/pics
%{tde_datadir}/apps/konqueror/pics/arrow_bottomleft.png
%{tde_datadir}/apps/konqueror/pics/arrow_bottomright.png
%{tde_datadir}/apps/konqueror/pics/arrow_topleft.png
%{tde_datadir}/apps/konqueror/pics/arrow_topright.png
%{tde_datadir}/apps/konqueror/pics/thumbnailfont_7x4.png
%{tde_datadir}/services/kded/favicons.desktop
%{tde_datadir}/servicetypes/konqpopupmenuplugin.desktop

%post -n trinity-libkonq
/sbin/ldconfig || :

%postun -n trinity-libkonq
/sbin/ldconfig || :

##########

%package libtqt3-integration
Summary:	Integration library between TQt3 and TDE
Group:		System/GUI/Other

Obsoletes:	tdebase-libtqt3-integration < %{version}-%{release}
Provides:	tdebase-libtqt3-integration = %{version}-%{release}

%description libtqt3-integration
These libraries allow you to use TDE dialogs in native TQt3 applications.

%files libtqt3-integration
%defattr(-,root,root,-)
%dir %{tde_tdelibdir}/plugins/integration
%{tde_tdelibdir}/plugins/integration/libqtkde.la
%{tde_tdelibdir}/plugins/integration/libqtkde.so
%{tde_tdelibdir}/plugins/integration/libqtkde.so.*
%{tde_tdelibdir}/kded_kdeintegration.la
%{tde_tdelibdir}/kded_kdeintegration.so
%{tde_datadir}/services/kded/kdeintegration.desktop

##########

%package -n trinity-libkonq-devel
Summary:	Development files for Konqueror's core libraries
Group:		Development/Libraries/Other
Requires:	trinity-libkonq = %{version}-%{release}
%{?xtst_devel:Requires: %{xtst_devel}}

%description -n trinity-libkonq-devel
This package contains headers and other development files for the core
Konqueror libraries.

%files -n trinity-libkonq-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kfileivi.h
%{tde_tdeincludedir}/kivdirectoryoverlay.h
%{tde_tdeincludedir}/knewmenu.h
%{tde_tdeincludedir}/konqbookmarkmanager.h
%{tde_tdeincludedir}/konq_*.h
%{tde_tdeincludedir}/libkonq_export.h
%{tde_libdir}/libkonq.la
%{tde_libdir}/libkonq.so

%post -n trinity-libkonq-devel
/sbin/ldconfig || :

%postun -n trinity-libkonq-devel
/sbin/ldconfig || :

##########

%package tdeio-smb-plugin
Summary:	Windows Connection Module for TDE
Group:		System/GUI/Other

%description tdeio-smb-plugin
This package provides the "smb://" protocol, to connect to and from
Windows and Samba shares.

%files tdeio-smb-plugin
%defattr(-,root,root)
%{tde_tdelibdir}/kcm_samba.la
%{tde_tdelibdir}/kcm_samba.so
%{tde_tdelibdir}/kio_smb.la
%{tde_tdelibdir}/kio_smb.so
%{tde_datadir}/services/smb.protocol
%{tde_datadir}/apps/konqueror/dirtree/remote/smb-network.desktop
%dir %{tde_datadir}/apps/remoteview
%{tde_datadir}/apps/remoteview/smb-network.desktop
%{tde_datadir}/mimelnk/application/x-smb-workgroup.desktop

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}
%{?tde_patch:%patch1 -p1}

# Applies an optional distro-specific graphical theme
%if "%{?tde_bg}" != ""
# TDM Background
%__sed -i "%{tdm}/kfrontend/gen%{tdm}conf.c" \
	-e 's|"Wallpaper=isadora.png\n"|"Wallpaper=%{tde_bg}\n"|'

# TDE user default background
%__sed -i "kpersonalizer/keyecandypage.cpp" \
	-e 's|#define DEFAULT_WALLPAPER "isadora.png"|#define DEFAULT_WALLPAPER "%{tde_bg}"|'
%__sed -i "%{starttde}" \
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

# TDE default directory and icon in startup script
%__sed -i "%{starttde}" \
	-e "s|/opt/trinity|%{tde_prefix}|g"

# Sets default TDE menu icon
%if "%{tde_starticon}" != ""
%__sed -i "kicker/libkicker/kickerSettings.kcfg" \
	-e "s|QString(\"kmenu\")|QString(\"%{tde_starticon}\")|"
%endif

# Xsession script location may vary on some distro
%if 0%{?rhel} || 0%{?fedora}
%__sed -i "%{tdm}/kfrontend/gen%{tdm}conf.c" -e "s|/etc/X11/Xsession|/etc/X11/xinit/Xsession|"
%endif
%if 0%{?suse_version}
%__sed -i "%{tdm}/kfrontend/gen%{tdm}conf.c" -e "s|/etc/X11/Xsession|/etc/X11/xdm/Xsession|"
%endif

# Reboot command location may vary on some distributions
if [ -x "/usr/bin/reboot" ]; then
  POWEROFF="/usr/bin/poweroff"
  REBOOT="/usr/bin/reboot"
fi
if [ -n "${REBOOT}" ]; then
  %__sed -i \
    "doc/%{tdm}/%{tdm}rc-ref.docbook" \
    "kcontrol/%{tdm}/%{tdm}-shut.cpp" \
    "%{tdm}/config.def" \
  -e "s|/sbin/poweroff|${POWEROFF}|g" \
  -e "s|/sbin/reboot|${REBOOT}|g"
fi

# Update icons for some control center modules
%__sed -i "kcontrol/componentchooser/componentchooser.desktop"        -e "s|^Icon=.*|Icon=kcmcomponentchooser|"
%__sed -i "kcontrol/taskbar/kcmtaskbar.desktop"                       -e "s|^Icon=.*|Icon=kcmtaskbar|"
%__sed -i "kcontrol/nics/nic.desktop"                                 -e "s|^Icon=.*|Icon=kcmnic|"
%__sed -i "kcontrol/input/mouse.desktop"                              -e "s|^Icon=.*|Icon=kcmmouse|"
%__sed -i "kcontrol/smserver/kcmsmserver.desktop"                     -e "s|^Icon=.*|Icon=kcmsmserver|"
%__sed -i "kcontrol/kded/kcmkded.desktop"                             -e "s|^Icon=.*|Icon=kcmkded|"
%__sed -i "kcontrol/konq/desktop.desktop"                             -e "s|^Icon=.*|Icon=kcmdesktop|"
%__sed -i "kcontrol/konq/desktopbehavior.desktop"                     -e "s|^Icon=.*|Icon=kcmdesktopbehavior|"
%__sed -i "kcontrol/privacy/privacy.desktop"                          -e "s|^Icon=.*|Icon=kcmprivacy|"
%__sed -i "kcontrol/crypto/crypto.desktop"                            -e "s|^Icon=.*|Icon=kcmcrypto|"
%__sed -i "kcontrol/kio/netpref.desktop"                              -e "s|^Icon=.*|Icon=kcmnetpref|"
%__sed -i "kcontrol/konqhtml/khtml_filter.desktop"                    -e "s|^Icon=.*|Icon=kcmkhtml_filter|"
%__sed -i "kcontrol/joystick/joystick.desktop"                        -e "s|^Icon=.*|Icon=kcmjoystick|"
%__sed -i "kcontrol/colors/colors.desktop"                            -e "s|^Icon=.*|Icon=kcmcolors|"
%__sed -i "kcontrol/performance/kcmperformance.desktop"               -e "s|^Icon=.*|Icon=kcmperformance|"
%__sed -i "kcontrol/launch/kcmlaunch.desktop"                         -e "s|^Icon=.*|Icon=kcmlaunch|"
%__sed -i "kcontrol/dnssd/kcm_kdnssd.desktop"                         -e "s|^Icon=.*|Icon=kcmkdnssd|"
%__sed -i "kcontrol/spellchecking/spellchecking.desktop"              -e "s|^Icon=.*|Icon=kcmspellchecking|"
%__sed -i "konqueror/sidebar/trees/history_module/kcmhistory.desktop" -e "s|^Icon=.*|Icon=kcmhistory|"
%__sed -i "kioslave/cgi/kcmcgi/kcmcgi.desktop"                        -e "s|^Icon=.*|Icon=kcmcgi|"
%__sed -i "kioslave/media/kcmodule/media.desktop"                     -e "s|^Icon=.*|Icon=kcmmedia|" 


%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"
export KDEDIR=%{tde_prefix}

# Shitty hack for RHEL4 ...
if [ -d "/usr/X11R6" ]; then
  export CMAKE_INCLUDE_PATH="${CMAKE_INCLUDE_PATH}:/usr/X11R6/include:/usr/X11R6/%{_lib}"
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

# Samba 4.0 includes (Fedora 18)
if [ -d "/usr/include/samba-4.0" ]; then
  export CMAKE_INCLUDE_PATH="${CMAKE_INCLUDE_PATH}:/usr/include/samba-4.0"
fi

if ! rpm -E %%cmake|grep -q "cd build"; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_NO_BUILTIN_CHRPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  \
  -DBIN_INSTALL_DIR="%{tde_bindir}" \
  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  -DCONFIG_INSTALL_DIR="%{_sysconfdir}/trinity" \
  -DSYSCONF_INSTALL_DIR="%{_sysconfdir}/trinity" \
  -DXDG_MENU_INSTALL_DIR="%{_sysconfdir}/xdg/menus" \
  \
  -DWITH_SASL=ON \
  -DWITH_LDAP=ON \
  -DWITH_SAMBA=ON \
  %{?with_exr:-DWITH_OPENEXR=ON} \
  -DWITH_XCOMPOSITE=ON \
  -DWITH_XCURSOR=ON \
  -DWITH_XFIXES=ON \
  %{?with_xrandr:-DWITH_XRANDR=ON} \
  -DWITH_XRENDER=ON \
  -DWITH_XDAMAGE=ON \
  -DWITH_XEXT=ON \
  %{?with_xtest:-DWITH_XTEST=ON} \
  %{?with_xscreensaver:-DWITH_XSCREENSAVER=ON} \
  %{?with_libart:-DWITH_LIBART=ON} \
  -DWITH_LIBUSB=ON \
  -DWITH_LIBRAW1394=ON \
  -DWITH_SUDO_KDESU_BACKEND=OFF \
  -DWITH_PAM=ON \
  -DWITH_SHADOW=ON \
  -DWITH_XDMCP=ON \
  -DWITH_XINERAMA=ON \
  -DWITH_ARTS=ON \
  -DWITH_I8K=ON \
  %{?with_hal:-DWITH_HAL=ON} \
  -DWITH_KDESKTOP_LOCK_BACKTRACE=OFF \
  -DBUILD_ALL=ON \
%if 0%{?suse_version}
  -DKCHECKPASS_PAM_SERVICE="xdm" \
  -DKDM_PAM_SERVICE="xdm" \
  -DKSCREENSAVER_PAM_SERVICE="xdm" \
%else
  -DKCHECKPASS_PAM_SERVICE="kcheckpass-trinity" \
  -DKDM_PAM_SERVICE="tdm-trinity" \
  -DKSCREENSAVER_PAM_SERVICE="tdescreensaver-trinity" \
%endif
  %{!?with_tsak:-DBUILD_TSAK=OFF} \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

# Removes obsolete Beagle-related files
%__rm -f %{?buildroot}%{tde_bindir}/khc_beagle_index.pl
%__rm -f %{?buildroot}%{tde_bindir}/khc_beagle_search.pl

# Adds a GDM/KDM/XDM session called 'TDE'

# Under RHEL/Fedora/Suse, static 'xsessions' files go to '/usr/share/xsessions'.
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%__install -D -m 644 \
	"%{?buildroot}%{tdm_datadir}/sessions/tde.desktop" \
	"%{?buildroot}%{_datadir}/xsessions/tde.desktop"

# Force session name to be 'TDE'
%__sed -i "%{?buildroot}%{_datadir}/xsessions/tde.desktop" \
	-e "s,^Name=.*,Name=TDE,"
%endif

# Mageia/Mandriva/PCLinuxOS stores its session file in different folder than RHEL/Fedora
# Generated files for TDM/KDM4 go to '/usr/share/apps/kdm/sessions'
%if 0%{?mgaversion} || 0%{?mdkversion}
%__install -d -m 755 %{?buildroot}%{_sysconfdir}/X11/wmsession.d
cat <<EOF >"%{?buildroot}%{_sysconfdir}/X11/wmsession.d/45TDE"
NAME=TDE
ICON=kde-wmsession.xpm
DESC=The Trinity Desktop Environment
EXEC=%{tde_bindir}/%{starttde}
SCRIPT:
exec %{tde_bindir}/%{starttde}
EOF

%__install -d -m 755 %{?buildroot}%{_datadir}/X11/dm.d
cat <<EOF >"%{?buildroot}%{_datadir}/X11/dm.d/45TDE.conf"
NAME=TDM
DESCRIPTION=TDM (Trinity Display Manager)
PACKAGE=trinity-tdm
EXEC=%{tde_bindir}/%{tdm}
%if 0%{?pclinuxos}
FNDSESSION_EXEC="/usr/sbin/chksession -k"
%else
FNDSESSION_EXEC="/usr/sbin/chksession --generate=/usr/share/xsessions"
%endif
EOF
%endif

# TDE 3.5.12: add script "plasma-desktop" to avoid conflict with KDE4
%if "%{?tde_prefix}" != "/usr"
cat <<EOF >"%{?buildroot}%{tde_bindir}/plasma-desktop"
#!/bin/sh

# This stupid scripts prevent the launch of 'plasma-desktop'
# (from KDE4) alongside with TDE.

case "\${DESKTOP_SESSION}" in
        "kde3"|"trinity"|"TDE") exit 0;;
        *) exec /usr/bin/plasma-desktop;;
esac
EOF
chmod 755 "%{?buildroot}%{tde_bindir}/plasma-desktop"
%endif

# PAM configuration files (except openSUSE)
%if 0%{?suse_version} == 0
%__install -D -m 644 "%{SOURCE2}" "%{?buildroot}%{_sysconfdir}/pam.d/tdm-trinity"
%__install -D -m 644 "%{SOURCE3}" "%{?buildroot}%{_sysconfdir}/pam.d/tdm-trinity-np"
%__install -D -m 644 "%{SOURCE4}" "%{?buildroot}%{_sysconfdir}/pam.d/kcheckpass-trinity"
%__install -D -m 644 "%{SOURCE5}" "%{?buildroot}%{_sysconfdir}/pam.d/tdescreensaver-trinity"
%endif

# TDM configuration
%__sed -i "%{?buildroot}%{_sysconfdir}/trinity/%{tdm}/%{tdm}rc" \
%if 0%{?fedora} >= 16 || 0%{?suse_version} >= 1210 || 0%{?rhel} >= 7
	-e "s/^#*MinShowUID=.*/MinShowUID=1000/"
%else
	-e "s/^#*MinShowUID=.*/MinShowUID=500/"
%endif

# Symlinks 'usb.ids' (Use system-provided version, not TDE provided version)
%__rm -f "%{?buildroot}%{tde_datadir}/apps/usb.ids"
%if 0%{?suse_version} || 0%{?mgaversion} >= 4
%__ln_s -f "/usr/share/usb.ids" "%{?buildroot}%{tde_datadir}/apps/usb.ids"
%else
%__ln_s -f "/usr/share/hwdata/usb.ids" "%{?buildroot}%{tde_datadir}/apps/usb.ids"
%endif

# Makes 'media_safelyremove.desktop' an alternative.
# This allows the use of 'tdeio-umountwrapper' package.
%__mv -f "%{buildroot}%{tde_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop" "%{buildroot}%{tde_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_tdebase"
%__mkdir_p "%{buildroot}%{_sysconfdir}/alternatives"
%__ln_s "media_safelyremove.desktop_tdebase" "%{buildroot}%{_sysconfdir}/alternatives/media_safelyremove.desktop"

# SUSE >= 12 : creates DM config file, used by '/etc/init.d/xdm'
#  You must set 'DISPLAYMANAGER=tdm' in '/etc/sysconfig/displaymanager'
%if 0%{?suse_version} >= 1210
%__install -D -m 644 "%{SOURCE6}" "%{?buildroot}/usr/lib/X11/displaymanagers/tdm"
%__sed -i "%{?buildroot}/usr/lib/X11/displaymanagers/tdm" -e "s|/opt/trinity/bin|%{tde_bindir}|g"
%endif

# Fedora 18 / RHEL 7: no more SYSV init script, we have to use systemd to launch TDM.
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
%__install -D -m 644 "%{SOURCE7}" "%{?buildroot}/usr/lib/systemd/system/tdm.service"
%endif

# Symlink TDM configuration
%__mkdir_p "%{?buildroot}%{tde_datadir}/config"
%__ln_s "%{_sysconfdir}/trinity/%{tdm}" "%{?buildroot}%{tde_datadir}/config/%{tdm}"

# SELINUX policy for RHEL / Fedora
%if 0%{?with_selinux_policy}
%__install -D -m 644 "%{SOURCE8}" "%{?buildroot}%{?_sysconfdir}/trinity/%{tdm}/tdm.pp"
%endif

# Mageia icon for TDE menu
%if 0%{?mgaversion} >= 3
%__install -D -m 644 "%{SOURCE9}" "%{?buildroot}%{tde_datadir}/oxygen/scalable/mgabutton.svg"
%endif

# openSUSE 11.4: tdm startup script
%if 0%{?suse_version} == 1140
%__install -D -m 755 "%{SOURCE7}" "%{?buildroot}%{?_sysconfdir}/init.d/xdm.tde"
%endif

# Console font to fontconfig
%__mkdir_p "%{buildroot}%{_sysconfdir}/fonts/conf.d"
cat <<EOF >"%{buildroot}%{_sysconfdir}/fonts/conf.d/99-konsole.conf"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <!-- Font directory list -->
  <dir>%{tde_datadir}/apps/konsole/fonts</dir>
</fontconfig>
EOF

# logrotate configuration
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cat << EOF > "%{buildroot}%{_sysconfdir}/logrotate.d/trinity-tdm"
/var/log/tdm.log {
    weekly
    notifempty
    missingok
    nocompress
}
EOF

# Move faces icon to XDG directory '/usr/share/faces'
if [ ! -d "%{?buildroot}%{_datadir}/faces" ]; then
  %__mkdir_p "%{?buildroot}%{_datadir}/faces"
  %__mv -f "%{?buildroot}%{tdm_datadir}/pics/users/"* "%{?buildroot}%{_datadir}/faces"
  rmdir "%{?buildroot}%{tdm_datadir}/pics/users"
fi
%__ln_s "%{_datadir}/faces" "%{?buildroot}%{tdm_datadir}/pics/users"

# Adds missing icons in 'hicolor' theme
# These icons are copied from 'crystalsvg' theme, provided by 'tdelibs'.
%__mkdir_p "%{?buildroot}%{tde_datadir}/icons/hicolor/"{16x16,22x22,32x32,48x48,64x64,128x128}"/apps/"
pushd "%{?buildroot}%{tde_datadir}/icons"
for i in {16,32,48,64,128};    do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/mimetypes/misc.png                      hicolor/"$i"x"$i"/apps/kcmcomponentchooser.png  ;done
for i in {16,22,32,48,128};    do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/actions/launch.png                      hicolor/"$i"x"$i"/apps/kcmperformance.png       ;done
for i in 16;                   do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/actions/services.png                    hicolor/"$i"x"$i"/apps/kcmkded.png              ;done
for i in {16,22,32,48};        do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/actions/exit.png                        hicolor/"$i"x"$i"/apps/kcmsmserver.png          ;done
for i in {16,22,32};           do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/actions/spellcheck.png                  hicolor/"$i"x"$i"/apps/kcmspellchecking.png     ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/filesystems/desktop.png                 hicolor/"$i"x"$i"/apps/kcmdesktopbehavior.png   ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/filesystems/desktop.png                 hicolor/"$i"x"$i"/apps/kcmdesktop.png           ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/apps/kmenu.png                          hicolor/"$i"x"$i"/apps/kcmtaskbar.png           ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/mimetypes/colorscm.png                  hicolor/"$i"x"$i"/apps/kcmcolors.png            ;done
for i in {16,22,32,48,128};    do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/actions/launch.png                      hicolor/"$i"x"$i"/apps/kcmlaunch.png            ;done
for i in {16,22,32};           do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/actions/filter.png                      hicolor/"$i"x"$i"/apps/kcmkhtml_filter.png      ;done
for i in {16,22,32};           do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/actions/run.png                         hicolor/"$i"x"$i"/apps/kcmcgi.png               ;done
for i in {16,22};              do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/actions/history.png                     hicolor/"$i"x"$i"/apps/kcmhistory.png           ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/filesystems/network.png                 hicolor/"$i"x"$i"/apps/kcmnetpref.png           ;done
for i in {16,32,48,64,128};    do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/devices/blockdevice.png                 hicolor/"$i"x"$i"/apps/kcmkdnssd.png            ;done
for i in {16,22,32,48,64};     do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/devices/joystick.png                    hicolor/"$i"x"$i"/apps/kcmjoystick.png          ;done
for i in {16,32,48,64,128};    do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/devices/mouse.png                       hicolor/"$i"x"$i"/apps/kcmmouse.png             ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/devices/system.png                      hicolor/"$i"x"$i"/apps/kcmmedia.png             ;done
for i in {16,22,32};           do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/actions/encrypted.png                   hicolor/"$i"x"$i"/apps/kcmcrypto.png            ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/filesystems/trashcan_empty.png          hicolor/"$i"x"$i"/apps/kcmprivacy.png           ;done
for i in {16,22,32,48,64,128}; do %__cp %{tde_datadir}/icons/crystalsvg/"$i"x"$i"/filesystems/network.png                 hicolor/"$i"x"$i"/apps/kcmnic.png               ;done
popd

# Updates applications categories for openSUSE
%if 0%{?suse_version}
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/Help.desktop                       Documentation Viewer
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/Home.desktop                       System FileManager core
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kate.desktop                       TextEditor
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/KControl.desktop                   X-SuSE-core
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/Kfind.desktop                      System Filesystem core
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kjobviewer.desktop                 PrintingUtility
%suse_update_desktop_file -r %{?buildroot}%{tde_tdeappdir}/klipper.desktop                    System TrayIcon
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kmenuedit.desktop                  Core-Configuration
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/knetattach.desktop                 System Network
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/konqbrowser.desktop                WebBrowser
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/konquerorsu.desktop                System FileManager
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/konsole.desktop                    TerminalEmulator
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/konsolesu.desktop                  TerminalEmulator
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kpager.desktop                     Utility  DesktopUtility
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kpersonalizer.desktop              DesktopUtility
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/ksysguard.desktop                  System Monitor
%suse_update_desktop_file -u %{?buildroot}%{tde_tdeappdir}/ktip.desktop                       System Utility
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kwrite.desktop                     TextEditor
%suse_update_desktop_file    %{?buildroot}%{tde_tdeappdir}/kdeprintfax.desktop                PrintingUtility
%suse_update_desktop_file -r %{?buildroot}%{tde_tdeappdir}/kfontview.desktop                  Graphics Viewer
%suse_update_desktop_file -r %{?buildroot}%{tde_tdeappdir}/krandrtray.desktop                 Applet X-KDE-settings-desktop
%suse_update_desktop_file    %{?buildroot}%{tde_datadir}/applnk/.hidden/konqfilemgr.desktop   System FileManager
%endif

# Icons from TDE Control Center should only be displayed in TDE
for i in %{?buildroot}%{tde_tdeappdir}/*.desktop ; do
  if grep -q "^Categories=.*X-KDE-settings" "${i}"; then
    if ! grep -q "OnlyShowIn=KDE" "${i}" ; then
      echo "OnlyShowIn=KDE;" >>"${i}"
    fi
  fi
done

# Other apps that should stay in TDE
for i in ksysguard kfontview showdesktop; do
  echo "OnlyShowIn=KDE;" >>"%{?buildroot}%{tde_tdeappdir}/${i}.desktop"
done

# Remove setuid bit on some binaries.
%if 0%{?with_tsak}
chmod 0511 "%{?buildroot}%{tde_bindir}/%{tdm}tsak"
%endif
chmod 0755 "%{?buildroot}%{tde_bindir}/kcheckpass"

# Fix permissions on shell scripts
chmod 0755 "%{?buildroot}%{tde_datadir}/apps/kconf_update/move_session_config.sh"
chmod 0755 "%{?buildroot}%{tde_tdedocdir}/HTML/en/khelpcenter/glossary/checkxrefs"

# Links duplicate files
%fdupes "%{?buildroot}%{tde_datadir}"


%clean
%__rm -rf %{?buildroot}


%if 0%{?suse_version}
# Check permissions on setuid files (openSUSE specific)
%verifyscript
%if 0%{?with_tsak}
%verify_permissions -e %{tde_bindir}/%{tdm}tsak
%endif
%verify_permissions -e %{tde_bindir}/kcheckpass
%endif


%changelog
* Sat Oct 11 2014 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-5
- Add logrotate configuration file.
- Add font configuration file.
- Install missing icons.

* Sun May 18 2014 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-4
- Fix Fedora 20 theme
- Fix some Mageia 4 path problems
- Forward port KDE SVN r803253 to fix potential security hole [Commit #c383da9d]

* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-3
- Build for Fedora 19

* Sun Jul 28 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-2
- Rebuild with NDEBUG option
- Fix XDG menu
- Fix Mageia/Mandriva specific icons

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2
