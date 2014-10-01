#
# spec file for package dbus-1-tqt
#
# Copyright (c) 2014 François Andriot <francois.andriot@free.fr>
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

# TDE specific building variables
%define tde_version 14.0.0


Name:		trinity-dbus-1-tqt
Epoch:		2
Version:	0.9
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:	dbus bindings for the Trinity Qt [TQt] interface
Group:		System/Libraries

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	libtqt3-mt-devel >= 3.5.0
BuildRequires:	libtqt4-devel >= 1:4.2.0

BuildRequires:	cmake >= 2.8
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

# DBUS support
%if 0%{?suse_version}
BuildRequires:	dbus-1-devel
%else
BuildRequires:	dbus-devel
%endif

%description
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides bindings for the Trinity Qt TQt interface.

See the dbus description for more information about D-BUS in general.

###########

%package -n libdbus-1-tqt
Summary:		dbus bindings for the Trinity Qt [TQt] interface
Group:			System/Libraries

Obsoletes:		trinity-dbus-1-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-dbus-1-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libdbus-1-tqt
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides bindings for the Trinity Qt TQt interface.

See the dbus description for more information about D-BUS in general.

%post -n libdbus-1-tqt
/sbin/ldconfig || :

%postun -n libdbus-1-tqt
/sbin/ldconfig || :

%files -n libdbus-1-tqt
%defattr(-,root,root,-)
%{_libdir}/libdbus-1-tqt.so.0
%{_libdir}/libdbus-1-tqt.so.0.0.0

##########

%package -n libdbus-1-tqt-devel
Summary:		dbus bindings for the Trinity Qt [TQt] interface (Development Files)
Group:			Development/Libraries
Requires:		libdbus-1-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:		trinity-dbus-1-tqt-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-dbus-1-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libdbus-1-tqt-devel
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides bindings for the Trinity Qt TQt interface.

See the dbus description for more information about D-BUS in general.

%post -n libdbus-1-tqt-devel
/sbin/ldconfig || :

%postun -n libdbus-1-tqt-devel
/sbin/ldconfig || :

%files -n libdbus-1-tqt-devel
%defattr(-,root,root,-)
%{_bindir}/dbusxml2qt3
%{_includedir}/*.h
%{_libdir}/libdbus-1-tqt.so
%{_libdir}/libdbus-1-tqt.la
%{_libdir}/pkgconfig/*.pc

##########

%if 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB

if ! rpm -E %%cmake|grep -q "cd build"; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DBIN_INSTALL_DIR=%{_bindir} \
  -DINCLUDE_INSTALL_DIR=%{_includedir} \
  -DLIB_INSTALL_DIR=%{_libdir} \
  ..

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build


%clean
%__rm -rf %{?buildroot}


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2:0.9-1
- Initial release for TDE R14.0.0
