# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_version 3.5.13.2

%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_datadir %{tde_prefix}/share

%define tde_tdeincludedir %{tde_includedir}/tde

%define _docdir %{tde_datadir}/doc

Name:			trinity-tqca-tls
Version:		1.0
Release:		%{?!preversion:3}%{?preversion:2_%{preversion}}%{?dist}%{?_variant}

Summary:		TLS plugin for the TQt Cryptographic Architecture
License:		LGPLv2+
Group:			Applications/Internet

URL:			http://delta.affinix.com/qca/
Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		tqca-tls-master.tar.gz

# Fix build in mach for QT apps
Patch0:		qca-tls-1.0-mach.patch
# Build with openssl 1.0.0
Patch2:     qca-tls-1.0-ossl10.patch
# Allows building with TQT3 from TDE
Patch10:	tqca-tls-qt3.patch

BuildRequires:	qt3-devel >= 3.3.8.d
BuildRequires:  trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tqca-devel >= 1.0
BuildRequires:	openssl-devel >= 0.9.8


%description
This is a plugin to provide SSL/TLS capability to programs that use the TQt
Cryptographic Architecture (TQCA).  TQCA is a library providing an easy API
for several cryptographic algorithms to TQt programs.  This package only
contains the TLS plugin.

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n tqca-tls-master
%patch0 -p0 -b .mach
%patch2 -p1 -b .ossl10
%patch10 -p1 -b .qt

# Revert TQCA to QCA
%__sed -i * -e "s|TQCA|QCA|g"


%build
unset QTDIR || : ; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

./configure
%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__make install INSTALL_ROOT=%{?buildroot}


%clean
%__rm -rf %{?buildroot}


%files
%defattr(0644,root,root,0755)
%doc README COPYING
%if 0%{?mgaversion} || 0%{?mdkversion}
%{_libdir}/qt3/plugins/crypto/libqca-tls.so
%endif
%if 0%{?suse_version}
%{_usr}/lib/qt3/plugins/crypto/libqca-tls.so
%endif
%if 0%{?rhel} || 0%{?fedora}
%{_libdir}/qt-3.3/plugins/crypto/libqca-tls.so
%endif


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-3
- Build for Fedora 19

* Thu Jun 27 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-2
- Renames TQCA to QCA in source code

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-1
- Initial release for TDE 3.5.13.2
