#
# spec file for package tqca (version 3.5.13-SRU)
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
# Please submit bugfixes or comments via http:/www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 1
%define tde_version 3.5.13.2
%define tde_pkg tqca
%define tde_prefix /opt/trinity
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define libtqca %{_lib}tqca
%else
%define libtqca libtqca
%endif


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.0
Release:	%{?!preversion:4}%{?preversion:3_%{preversion}}%{?dist}%{?_variant}
Summary:	TQt Cryptographic Architecture
Group:		Development/Libraries/C and C++
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        tqca-3.5.13.2.tar.gz
Source1:		%{name}-rpmlintrc

BuildRequires:  libtqt4-devel >= %{tde_epoch}:4.2.0
BuildRequires:	gcc-c++

%description
Taking a hint from the similarly-named Java Cryptography Architecture,
TQCA aims to provide a straightforward and cross-platform crypto API,
using TQt datatypes and conventions. TQCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
application!

##########

%package -n %{libtqca}1
Summary:	TQt Cryptographic Architecture
Group:		Development/Libraries/C and C++

Obsoletes:	trinity-libtqca < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-libtqca = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	libtqca = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	libtqca1 = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libtqca}1
Taking a hint from the similarly-named Java Cryptography Architecture,
TQCA aims to provide a straightforward and cross-platform crypto API,
using TQt datatypes and conventions. TQCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
application!

%post -n %{libtqca}1
/sbin/ldconfig

%postun -n %{libtqca}1
/sbin/ldconfig

%files -n %{libtqca}1
%defattr(-,root,root,-)
%doc COPYING README TODO
%{_libdir}/libqca.so.1
%{_libdir}/libqca.so.1.0
%{_libdir}/libqca.so.1.0.0

##########

%package -n %{libtqca}-devel
Summary:	TQt Cryptographic Architecture development files
Group:		Development/Libraries/C and C++
Requires:	%{libtqca}1 = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-libtqca-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-libtqca-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	libtqca-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libtqca}-devel
This packages contains the development files for TQCA

%post -n %{libtqca}-devel
/sbin/ldconfig

%postun -n %{libtqca}-devel
/sbin/ldconfig

%files -n %{libtqca}-devel
%defattr(-,root,root,-)
%{_includedir}/qca.h
%{_libdir}/libqca.so

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n tqca-3.5.13.2

# Fix 'lib64' library directory
perl -pi -e 's,target\.path=\$PREFIX/lib,target.path=\$PREFIX/%{_lib},g' qcextra


%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh

./configure \
  --prefix=%{_prefix} \
  --qtdir=${QTDIR} \
  --debug

%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install INSTALL_ROOT=$RPM_BUILD_ROOT


%clean
%__rm -rf $RPM_BUILD_ROOT


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-3
- Build for Fedora 19

* Thu Jun 27 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-2
- Renames TQCA to QCA in source code

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-1
- Initial release for TDE 3.5.13.2
