# Default version for this component
%define tdecomp libtqt-perl
%define tde_version 14.0.0

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
%define tde_appdir %{tde_datadsir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-%{tdecomp}
Summary:	Perl bindings for the TQt library
Version:	14.0.0
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Patch0:		libtqt-perl-14.0.0-ftbfs.patch

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-libsmokeqt-devel

%description
This module lets you use the TQt library from Perl.
It provides an object-oriented interface and is easy to use.


%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

%files
%defattr(-,root,root,-)
%{tde_bindir}/puic
%{tde_mandir}/man1/puic.1*
%{_bindir}/pqtapi
%{_bindir}/pqtsh
%{perl_vendorarch}/TQt.pm
%{perl_vendorarch}/TQt.pod
%{perl_vendorarch}/TQt/GlobalSpace.pm
%{perl_vendorarch}/TQt/attributes.pm
%{perl_vendorarch}/TQt/constants.pm
%{perl_vendorarch}/TQt/debug.pm
%{perl_vendorarch}/TQt/enumerations.pm
%{perl_vendorarch}/TQt/isa.pm
%{perl_vendorarch}/TQt/properties.pm
%{perl_vendorarch}/TQt/signals.pm
%{perl_vendorarch}/TQt/slots.pm
%{perl_vendorarch}/auto/TQt/TQt.so
%{_mandir}/man3/TQt.3pm.*

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}
%patch0 -p1 -b .ftbfs

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  --disable-rpath

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%clean
%__rm -rf %{buildroot}


%Changelog
* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 14.0.0-1
- Initial build for TDE 14.0.0
