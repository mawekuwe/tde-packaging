#
# spec file for package trinity-filesystem
#
# Copyright (c) 2014 François Andriot <francois.andriot@free.fr>
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

# TDE variables
%define tde_version 14.0.0
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define _docdir %{tde_docdir}
%define tde_docdir %{tde_datadir}/doc
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_includedir %{tde_prefix}/include
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_tdelibdir %{tde_libdir}/trinity



Name:		trinity-filesystem
Version:	%{tde_version}
Release:	1%{?dist}
Summary:	Trinity Directory Layout
Group:		System/Fhs
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		/usr
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch


%description
This package installs the Trinity directory structure.


%files
%dir %{tde_prefix}

%dir %{tde_bindir}

%dir %{tde_datadir}
%dir %{tde_datadir}/config

%dir %{tde_docdir}
%dir %{tde_tdedocdir}
%dir %{tde_tdedocdir}/HTML
%dir %{tde_tdedocdir}/HTML/en
%dir %{tde_tdedocdir}/HTML/en/common

%dir %{tde_includedir}
%dir %{tde_tdeincludedir}

%dir %{tde_libdir}
%dir %{tde_libdir}/pkgconfig
%dir %{tde_tdelibdir}

%dir %{tde_datadir}/applications
%dir %{tde_datadir}/applications/tde
%dir %{tde_datadir}/applnk
%dir %{tde_datadir}/apps
%dir %{tde_datadir}/config.kcfg
%dir %{tde_datadir}/autostart
%dir %{tde_datadir}/emoticons
%dir %{tde_datadir}/icons
%dir %{tde_datadir}/icons/crystalsvg
%dir %{tde_datadir}/icons/hicolor
%dir %{tde_datadir}/locale
%dir %{tde_datadir}/mimelnk
%dir %{tde_datadir}/services
%dir %{tde_datadir}/servicetypes

%dir %{_sysconfdir}/trinity

##########

%prep

%build

%install
%__install -d -m 755 %{?buildroot}%{tde_prefix}

%__install -d -m 755 %{?buildroot}%{tde_bindir}

%__install -d -m 755 %{?buildroot}%{tde_datadir}
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applications
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applications/tde
%__install -d -m 755 %{?buildroot}%{tde_datadir}/applnk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/apps
%__install -d -m 755 %{?buildroot}%{tde_datadir}/autostart
%__install -d -m 755 %{?buildroot}%{tde_datadir}/config
%__install -d -m 755 %{?buildroot}%{tde_datadir}/config.kcfg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/emoticons
%__install -d -m 755 %{?buildroot}%{tde_datadir}/icons
%__install -d -m 755 %{?buildroot}%{tde_datadir}/icons/crystalsvg
%__install -d -m 755 %{?buildroot}%{tde_datadir}/icons/hicolor
%__install -d -m 755 %{?buildroot}%{tde_datadir}/locale
%__install -d -m 755 %{?buildroot}%{tde_datadir}/mimelnk
%__install -d -m 755 %{?buildroot}%{tde_datadir}/services
%__install -d -m 755 %{?buildroot}%{tde_datadir}/servicetypes

%__install -d -m 755 %{?buildroot}%{tde_docdir}
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/en
%__install -d -m 755 %{?buildroot}%{tde_tdedocdir}/HTML/en/common

%__install -d -m 755 %{?buildroot}%{tde_includedir}
%__install -d -m 755 %{?buildroot}%{tde_tdeincludedir}

%__install -d -m 755 %{?buildroot}%{tde_libdir}
%__install -d -m 755 %{?buildroot}%{tde_libdir}/pkgconfig
%__install -d -m 755 %{?buildroot}%{tde_tdelibdir}

%__install -d -m 755 %{?buildroot}%{_datadir}/icons/hicolor
%__install -d -m 755 %{?buildroot}%{_datadir}/icons/hicolor/32x32
%__install -d -m 755 %{?buildroot}%{_datadir}/icons/hicolor/32x32/apps

%__install -d -m 755 %{?buildroot}%{_sysconfdir}/trinity

%changelog
* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 14.0.0-1
- Initial build for TDE R14
