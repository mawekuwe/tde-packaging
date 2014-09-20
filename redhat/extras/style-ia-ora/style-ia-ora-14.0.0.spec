# Default version for this component
%define tde_pkg style-ia-ora
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
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:        Mandriva theme for TDE - Widget design
Version:        1.0.8
Release:		%{?!preversion:4}%{?preversion:3_%{preversion}}%{?dist}%{?_variant}

License:        GPL
Group:          Environment/Desktop
URL:            http://www.mandrivalinux.com/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        %{tde_pkg}-%{tde_version}.tar.gz

Prefix:		%{_prefix}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}

Requires:	trinity-twin

%description
Mandriva theme for Trinity

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n ia_ora-kde-%{version}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --libdir=%{tde_libdir} \
  \
  --enable-rpath \
  --enable-closure \
  --disable-dependency-tracking \
  --enable-new-ldflags \
  --enable-final \
  --enable-shared \
  --disable-static

%__make %{?_smp_mflags}


%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{?buildroot}

# Removes useless files
%__rm -f %{?buildroot}%{tde_tdelibdir}/*.a
%__rm -f %{?buildroot}%{tde_tdelibdir}/plugins/styles/*.a


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{tde_tdelibdir}/twin3_iaora.la
%{tde_tdelibdir}/twin3_iaora.so
%{tde_tdelibdir}/twin_iaora_config.la
%{tde_tdelibdir}/twin_iaora_config.so
%{tde_tdelibdir}/plugins/styles/ia_ora.la
%{tde_tdelibdir}/plugins/styles/ia_ora.so
%{tde_datadir}/apps/kstyle/themes/ia_ora.themerc
%{tde_datadir}/apps/twin/iaora.desktop




%changelog
* Sat Jan 19 2013 Francois Andriot <francois.andriot@free.fr> - 1.0.8-4
- Initial release for TDE 14.0.0
