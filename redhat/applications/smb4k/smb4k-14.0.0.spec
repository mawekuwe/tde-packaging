#
# spec file for package smb4k (version R14.0.0)
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
%define tde_pkg smb4k
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
Version:	0.9.4
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:	A Samba (SMB) share advanced browser for Trinity
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org

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
BuildRequires:	gettext

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


%description
Smb4K is a SMB (Windows) share browser for TDE. It uses the Samba software 
suite to access the SMB shares of the local network neighborhood. Its purpose
is to provide a program that's easy to use and has as many features as 
possible.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/smb4k
%{tde_bindir}/smb4k_cat
%{tde_bindir}/smb4k_kill
%{tde_bindir}/smb4k_mount
%{tde_bindir}/smb4k_mv
%{tde_bindir}/smb4k_umount
%{tde_libdir}/libsmb4kcore.so.2
%{tde_libdir}/libsmb4kcore.so.2.0.0
%{tde_libdir}/libsmb4kdialogs.la
%{tde_libdir}/libsmb4kdialogs.so
%{tde_tdelibdir}/konqsidebar_smb4k.la
%{tde_tdelibdir}/konqsidebar_smb4k.so
%{tde_tdelibdir}/libsmb4tdeconfigdialog.la
%{tde_tdelibdir}/libsmb4tdeconfigdialog.so
%{tde_tdelibdir}/libsmb4knetworkbrowser.la
%{tde_tdelibdir}/libsmb4knetworkbrowser.so
%{tde_tdelibdir}/libsmb4ksearchdialog.la
%{tde_tdelibdir}/libsmb4ksearchdialog.so
%{tde_tdelibdir}/libsmb4ksharesiconview.la
%{tde_tdelibdir}/libsmb4ksharesiconview.so
%{tde_tdelibdir}/libsmb4kshareslistview.la
%{tde_tdelibdir}/libsmb4kshareslistview.so
%{tde_tdeappdir}/smb4k.desktop
%{tde_datadir}/apps/konqsidebartng/add/smb4k_add.desktop
%{tde_datadir}/apps/smb4k/
%{tde_datadir}/apps/smb4knetworkbrowserpart/
%{tde_datadir}/apps/smb4ksharesiconviewpart/
%{tde_datadir}/apps/smb4kshareslistviewpart/
%{tde_datadir}/config.kcfg/smb4k.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/smb4k.png
%{tde_tdedocdir}/HTML/en/smb4k/

%post
update-desktop-database %{tde_tdeappdir} > /dev/null
touch --no-create %{tde_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/crystalsvg || :
/sbin/ldconfig || :

%postun
update-desktop-database %{tde_tdeappdir} > /dev/null
touch --no-create %{tde_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/crystalsvg || :
/sbin/ldconfig || :

##########

%package devel
Summary:		Development files for %{name}
Group:			Development/Libraries
Requires:		%{name} = %{version}-%{release}

%description devel
%{summary}

%files devel
%{tde_tdeincludedir}/*.h
%{tde_libdir}/libsmb4kcore.la
%{tde_libdir}/libsmb4kcore.so

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

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
  --enable-final \
  --enable-new-ldflags \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}

# Updates applications categories for openSUSE
%if 0%{?suse_version}
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/%{tde_pkg}.desktop"
%suse_update_desktop_file -r %{tde_pkg} System Network
%endif

# Removes duplicate files
%fdupes -s %buildroot


%clean
%__rm -rf %{buildroot}


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2:0.9.4-1
- Initial release for TDE 14.0.0
