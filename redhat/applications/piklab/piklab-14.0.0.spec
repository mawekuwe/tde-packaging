#
# spec file for package piklab (version R14.0.0)
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
%define tde_pkg piklab
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
Version:	0.15.2
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:	IDE for PIC-microcontroller development [Trinity]
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

# READLINE support
BuildRequires:	readline-devel

# LIBUSB support
%if 0%{?mageia} || 0%{?mandriva} || 0%{?pclinuxos}
BuildRequires:  %{_lib}usb1.0-devel
BuildRequires:  %{_lib}usb-compat0.1-devel
%else
BuildRequires:  libusb-devel
%endif


%description
Piklab is an integrated development environment for applications based on
Microchip PIC and dsPIC microcontrollers similar to the MPLAB environment.

Support for several compiler and assembler toolchains is integrated. The
GPSim simulator, the ICD1 programmer, the ICD2 debugger, the PICkit1 and
PICkit2 programmers, the PicStart+ programmer, and most direct programmers
are supported. A command-line programmer and debugger are also available.


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
  --disable-final \
  --enable-new-ldflags \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Incorrect extension on manpage
%__mv -f %{buildroot}%{tde_mandir}/man1/piklab.1x %{buildroot}%{tde_mandir}/man1/piklab.1

%find_lang %{tde_pkg}

%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_tdeappdir} > /dev/null
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
update-desktop-database %{tde_tdeappdir} > /dev/null
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/piklab
%{tde_bindir}/piklab-coff
%{tde_bindir}/piklab-hex
%{tde_bindir}/piklab-prog
%{tde_tdeappdir}/piklab.desktop
%{tde_datadir}/apps/katepart/syntax/asm-pic.xml
%{tde_datadir}/apps/katepart/syntax/coff-c-pic.xml
%{tde_datadir}/apps/katepart/syntax/coff-pic.xml
%{tde_datadir}/apps/katepart/syntax/jal-pic.xml
%{tde_datadir}/apps/piklab
%{tde_tdedocdir}/HTML/en/piklab
%{tde_datadir}/icons/hicolor/*/*/*.png
%{tde_datadir}/mimelnk/application/x-piklab.desktop
%{tde_mandir}/man1/piklab-coff.1
%{tde_mandir}/man1/piklab-hex.1
%{tde_mandir}/man1/piklab-prog.1
%{tde_mandir}/man1/piklab.1


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2:0.15.2-1
- Initial release for TDE 14.0.0
