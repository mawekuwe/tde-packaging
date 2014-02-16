# Default version for this component
%define tde_pkg kcmldap
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

%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		Kerberos control module for the TDE control center
Version:		0.5
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext
BuildRequires:	trinity-libtdeldap-devel >= 0.5

Requires:		trinity-tde-ldap-cert-updater = %{version}-%{release}
Requires:		trinity-kcontrol-ldap-bonding = %{version}-%{release}

%description
This is a meta-package that installs all kcmldap related packages.

%files

##########

%package -n trinity-kcontrol-ldap-bonding
Summary:		Kerberos control module for the TDE control center
Group:			Applications/Utilities
Requires:		trinity-tde-ldap-cert-updater = %{version}-%{release}

%description -n trinity-kcontrol-ldap-bonding
This is a TDE control center module to manage TDE connections to Kerberos realms.

%post -n trinity-kcontrol-ldap-bonding
touch --no-create %{tde_datadir}/icons/hicolor || :

%postun -n trinity-kcontrol-ldap-bonding
touch --no-create %{tde_datadir}/icons/hicolor || :

%files -n trinity-kcontrol-ldap-bonding
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING
%{tde_bindir}/tdeldapbonding
%{tde_tdelibdir}/kcm_ldapbonding.la
%{tde_tdelibdir}/kcm_ldapbonding.so
%{tde_tdeappdir}/ldapbonding.desktop
%{tde_datadir}/pixmaps/kcmldapbonding_step1.png
%{tde_datadir}/pixmaps/kcmldapbonding_step3.png

##########

%package -n trinity-tde-ldap-cert-updater
Summary:		Service to keep LDAP certificates up-to-date
Group:			Applications/Utilities
Requires:		trinity-kcontrol-ldap-bonding = %{version}-%{release}

%description -n trinity-tde-ldap-cert-updater
This is a small daemon which keeps the LDAP root certificate up to date with the LDAP server

%post -n trinity-tde-ldap-cert-updater
touch --no-create %{tde_datadir}/icons/hicolor || :

%postun -n trinity-tde-ldap-cert-updater
touch --no-create %{tde_datadir}/icons/hicolor || :

%files -n trinity-tde-ldap-cert-updater
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING
%{tde_bindir}/tdeldapcertupdater

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
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
  --includedir=%{tde_tdeincludedir} \
  --docdir=%{tde_tdedocdir} \
  --libdir=%{tde_libdir} \
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


%clean
%__rm -rf %{buildroot}


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.5-1
- Initial release for TDE 14.0.0
