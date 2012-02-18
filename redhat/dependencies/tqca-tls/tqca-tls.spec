%define _prefix /usr

Name:		tqca-tls
Version:	r14
Release:	1%{?dist}

Summary:	TLS plugin for the Qt Cryptographic Architecture
License:	LGPLv2+
Group:		Applications/Internet

URL:		http://delta.affinix.com/qca/
Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Source0:	%{name}-%{version}.tar.gz

# Fix build in mach for QT apps
Patch0:		qca-tls-1.0-mach.patch
# Missing ifdefs for openssl 0.9.8
Patch1:     qca-tls-1.0-ossl098.patch
# Build with openssl 1.0.0
Patch2:     qca-tls-1.0-ossl10.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch10:	tqca-tls-qmake-tqt3.patch

BuildRequires:	tqt3-devel >= 3.4.0
# To build with openssl 0.9.7, disable patch1
BuildRequires:	openssl-devel >= 0.9.8


%description
This is a plugin to provide SSL/TLS capability to programs that use the TQt
Cryptographic Architecture (TQCA).  TQCA is a library providing an easy API
for several cryptographic algorithms to TQt programs.  This package only
contains the TLS plugin.

%prep
%setup -q -n dependencies/%{name}
%patch0 -p0 -b .mach
#patch1 -p0 -b .ossl098
%patch2 -p1 -b .ossl10
%patch10 -p1

%build
./configure \
  --qtdir=/usr
%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__mkdir -p %{?buildroot}%{_libdir}/tqt3/plugins/crypto
%__make install INSTALL_ROOT=%{?buildroot}


%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc README COPYING
%attr(755,root,root) %{_libdir}/tqt3/plugins/crypto


%changelog
* Sat Feb 18 2012 Francois Andriot <francois.andriot@free.fr> - r14-1
- Initial build for TDE R14
- Spec file based on Fedora 12 'qca-tls-1.0-18'
