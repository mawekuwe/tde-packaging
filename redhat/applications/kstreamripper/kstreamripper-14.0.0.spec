#
# spec file for package kstreamripper (version R14.0.0)
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
%define tde_epoch 2
%define tde_version 14.0.0
%define tde_pkg kstreamripper
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.3.4
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:	TDE frontend for streamripper
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	autoconf automake libtool m4
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	fdupes

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

BuildRequires:	scons


%description
KStreamRipper is a small frontend for the streamripper command
line utility. Streamripper captures internet shoutcast radio streams
on your harddisk and splits them up in mp3 files. KStreamRipper helps
you with managing/ripping your preferred streams.


##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

export QTDIR=/usr
scons -Q -j4


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Move desktop file to XDG folder
%__mkdir_p "%{?buildroot}%{tde_tdeappdir}"
%__mv -f "%{?buildroot}%{tde_datadir}/applnk/"*"/%{tde_pkg}.desktop" "%{?buildroot}%{tde_tdeappdir}"

# Missing icon file will make this fail.
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/%{tde_pkg}.desktop"


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{tde_bindir}/kstreamripper
%{tde_tdeappdir}/kstreamripper.desktop
%{tde_datadir}/apps/kstreamripper/
%{tde_tdedocdir}/HTML/en/kstreamripper/



%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2:0.3.4-1
- Initial release for TDE 14.0.0
