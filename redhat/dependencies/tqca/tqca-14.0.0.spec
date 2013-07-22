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


Name:           trinity-tqca
Version:        1.0
Release:		%{?!preversion:3}%{?preversion:2_%{preversion}}%{?dist}%{?_variant}

Summary:        TQt Cryptographic Architecture

Group:          System Environment/Libraries
License:        LGPLv2+

Vendor:			Trinity Project
URL:			http://www.trinitydesktop.org/
Packager:		Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:  trinity-tqt3-devel >= 3.5.0
BuildRequires:  trinity-tqtinterface-devel >= %{tde_version}


%description
Taking a hint from the similarly-named Java Cryptography Architecture,
TQCA aims to provide a straightforward and cross-platform crypto API,
using TQt datatypes and conventions. TQCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
application!

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README TODO
%{tde_libdir}/libqca.so.*

##########

%package        devel
Summary:        TQt Cryptographic Architecture development files
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
This packages contains the development files for TQCA

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%{tde_includedir}/qca.h
%{tde_libdir}/libqca.so

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

# Fix 'lib64' library directory
perl -pi -e 's,target\.path=\$PREFIX/lib,target.path=\$PREFIX/%{_lib},g' qcextra


%build
unset QTDIR
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

./configure \
  --prefix=%{tde_prefix} \
  --qtdir=/usr \
  --debug

%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install INSTALL_ROOT=$RPM_BUILD_ROOT


%clean
%__rm -rf $RPM_BUILD_ROOT



%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-3
- Initial release for TDE 14.0.0
