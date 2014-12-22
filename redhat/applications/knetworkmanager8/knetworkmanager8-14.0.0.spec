#
# spec file for package knetworkmanager8 (version R14.0.0)
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
# Please submit bugfixes or comments via http:/www.trinitydesktop.org/
#

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%define tde_version 14.0.0
%define tde_pkg knetworkmanager
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_prefix}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif


Name:			trinity-%{tde_pkg}8
Epoch:			%{tde_epoch}
Version:		0.8
Summary:		Trinity applet for Network Manager
Release:		%{?!preversion:6}%{?preversion:5_%{preversion}}%{?dist}%{?_variant}
Group:			Applications/Internet
URL:			http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

#Requires:       kde-filesystem
BuildRequires:	desktop-file-utils

%if 0%{?rhel} || 0%{?fedora}
Requires:		NetworkManager-gnome
%else
Requires:		networkmanager
%endif

BuildRequires:	trinity-dbus-1-tqt-devel >= 1:0.9
BuildRequires:	trinity-dbus-tqt-devel >= 1:0.63
BuildRequires:	NetworkManager-glib-devel

Obsoletes:		trinity-knetworkmanager < %{version}-%{release}
Provides:		trinity-knetworkmanager = %{version}-%{release}

%description
KNetworkManager is a system tray applet for controlling network
connections on systems that use the NetworkManager daemon.


%package devel
Summary:		Common data shared among the MySQL GUI Suites
Group:			Development/Libraries
Requires:		%{name} = %{version}-%{release}

Obsoletes:		trinity-knetworkmanager-devel < %{version}-%{release}
Provides:		trinity-knetworkmanager-devel = %{version}-%{release}

%description devel
Development headers for knetworkmanager


%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif


%prep 
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

# Warning: --enable-final causes FTBFS
%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --disable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility \
  \
  --with-openvpn \
  --with-vpnc \
  --with-pptp

# Does not support parallel build
%__make


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=%{?buildroot}
%find_lang knetworkmanager


%clean
%__rm -rf $RPM_BUILD_ROOT


%post
update-desktop-database %{tde_appdir} > /dev/null
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%postun
update-desktop-database %{tde_appdir} > /dev/null
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%post devel
/sbin/ldconfig


%postun devel
/sbin/ldconfig


%files -f knetworkmanager.lang
%defattr(-,root,root,-)
%{tde_bindir}/knetworkmanager
%{tde_libdir}/*.la
%{tde_libdir}/*.so
%{tde_tdelibdir}/knetworkmanager_openvpn.so.*
%{tde_tdelibdir}/knetworkmanager_pptp.so.*
%{tde_tdelibdir}/knetworkmanager_vpnc.so.*
%{_sysconfdir}/dbus-1/system.d/knetworkmanager.conf
%{tde_tdeappdir}/knetworkmanager.desktop
%{tde_datadir}/apps/knetworkmanager
%{tde_datadir}/icons/hicolor/*/apps/knetworkmanager*
%{tde_datadir}/servicetypes/knetworkmanager_plugin.desktop
%{tde_datadir}/servicetypes/knetworkmanager_vpnplugin.desktop
%{tde_datadir}/services/knetworkmanager_openvpn.desktop
%{tde_datadir}/services/knetworkmanager_pptp.desktop
%{tde_datadir}/services/knetworkmanager_vpnc.desktop

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/*.h
%{tde_tdelibdir}/*.la
%{tde_tdelibdir}/*.so

%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.8-6
- Initial release for TDE 14.0.0
