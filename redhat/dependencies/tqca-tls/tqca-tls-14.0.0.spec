# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_version 14.0.0

%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_datadir %{tde_prefix}/share

%define tde_tdeincludedir %{tde_includedir}/tde

%define _docdir %{tde_datadir}/doc

Name:			trinity-tqca-tls
Version:		1.0
Release:		%{?!preversion:4}%{?preversion:3_%{preversion}}%{?dist}%{?_variant}

Summary:		TLS plugin for the TQt Cryptographic Architecture
License:		LGPLv2+
Group:			Applications/Internet

URL:			http://delta.affinix.com/qca/
Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:  libtqt4-devel >= 2:4.2.0
BuildRequires:	trinity-tqca-devel >= 1.0
BuildRequires:	openssl-devel >= 0.9.8


%description
This is a plugin to provide SSL/TLS capability to programs that use the TQt
Cryptographic Architecture (TQCA).  TQCA is a library providing an easy API
for several cryptographic algorithms to TQt programs.  This package only
contains the TLS plugin.

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

./configure \
  --qtdir=/usr

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__make install INSTALL_ROOT=%{?buildroot}


%clean
%__rm -rf %{?buildroot}


%files
%defattr(0644,root,root,0755)
%doc README COPYING
%{_libdir}/tqt3/plugins/crypto/libtqca-tls.so


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-3
- Initial release for TDE 14.0.0
