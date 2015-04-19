#
# spec file for package konversation (version R14.0.0)
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
%define tde_pkg konversation
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
Version:	1.1
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:	user friendly Internet Relay Chat (IRC) client for TDE [Trinity]
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

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

# XSLT support
BuildRequires:	libxslt-devel
%if 0%{?suse_version}
BuildRequires:	docbook-xsl-stylesheets
%else
BuildRequires:	docbook-style-xsl
%endif

# LIBXI support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}xi-devel
%endif
%if 0%{?rhel} >= 5|| 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libXi-devel
%endif
%if 0%{?suse_version} == 1140
BuildRequires:	libXi6-devel
%endif

%description
Konversation is a client for the Internet Relay Chat (IRC) protocol.
It is easy to use and well-suited for novice IRC users, but novice
and experienced users alike will appreciate its many features:

 * Standard IRC features
 * Easy to use graphical interface
 * Multiple server and channel tabs in a single window
 * IRC color support
 * Pattern-based message highlighting and OnScreen Display
 * Multiple identities for different servers
 * Multi-language scripting support (with DCOP)
 * Customizable command aliases
 * NickServ-aware log-on (for registered nicknames)
 * Smart logging
 * Traditional or enhanced-shell-style nick completion
 * DCC file transfer with resume support



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
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/konversation
%{tde_tdeappdir}/konversation.desktop
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-appearance.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-colorcodes.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-colors.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-custombrowser.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-notifylists.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-sortorder.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.19-tabplacement.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.20-customfonts.pl
%{tde_datadir}/apps/tdeconf_update/konversation-0.20-quickbuttons.pl
%{tde_datadir}/apps/tdeconf_update/konversation.upd
%{tde_datadir}/apps/konversation/
%{tde_datadir}/config.kcfg/konversation.kcfg
%{tde_datadir}/services/konvirc.protocol
%{tde_datadir}/services/konvirc6.protocol
%{tde_tdedocdir}/HTML/*/konversation/
%{tde_datadir}/icons/crystalsvg/*/actions/tdeimproxyaway.png
%{tde_datadir}/icons/crystalsvg/*/actions/tdeimproxyoffline.png
%{tde_datadir}/icons/crystalsvg/*/actions/tdeimproxyonline.png
%{tde_datadir}/icons/crystalsvg/*/actions/char.png
%{tde_datadir}/icons/crystalsvg/*/actions/konv_message.png
%{tde_datadir}/icons/crystalsvg/scalable/actions/tdeimproxyaway.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/tdeimproxyoffline.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/tdeimproxyonline.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/konv_message.svgz
%{tde_datadir}/icons/hicolor/*/apps/konversation.png
%{tde_datadir}/icons/hicolor/scalable/apps/konversation.svgz


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2:1.1-1
- Initial release for TDE 14.0.0
