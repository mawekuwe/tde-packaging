# Default version for this component
%define tde_pkg kima
%define tde_version 3.5.13.2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		kicker monitoring applet [Trinity]
Version:		0.7.3.2
Release:		%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.elliptique.net/~ken/kima/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

# HAL support
#  On RHEL4, we do not use HAL (too old)
%if 0%{?fedora} >= 15 || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?suse_version}
%define with_hal 1
BuildRequires:	hal-devel >= 0.4.8
%endif


%description
This applet monitors various temperature,
frequency and fan sources in your kicker
panel.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%find_lang %{tde_pkg}



%clean
%__rm -rf %{buildroot}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_tdelibdir}/libkima.la
%{tde_tdelibdir}/libkima.so
%{tde_datadir}/apps/kicker/applets/kima.desktop
%{tde_tdedocdir}/HTML/en/kima/


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 0.7.3.2-5
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.7.3.2-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.7.3.2-3
- Initial release for TDE 3.5.13.1

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.7.3.2-2
- Rebuilt for Fedora 17
- Fix post and postun

* Wed Nov 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.7.3.2-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
