#
# spec file for package dbus-tqt (version 3.5.13-SRU)
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

%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define libdbus %{_lib}dbus
%else
%define libdbus libdbus
%endif


Name:		trinity-dbus-tqt
Epoch:		%{tde_epoch}
Version:	0.63
Release:	%{?!preversion:2}%{?preversion:1_%{preversion}}%{?dist}%{?_variant}
Summary:	Simple inter-process messaging system
Group:		System/Libraries
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		/usr
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

# [dbus-tqt] Fix build on RHEL 4
Patch1:		dbus-tqt-3.5.13-fix_old_dbus_types.patch

BuildRequires:	libtqt4-devel >= %{tde_epoch}:4.2.0

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

This package provides the TQt-based shared library for applications using the
Qt interface to D-BUS.

See the dbus description for more information about D-BUS in general.

##########

%package -n %{libdbus}-tqt-1-0
Summary:		Simple inter-process messaging system (TQt-based shared library)
Group:			System/Libraries
Provides:		libdbus-tqt-1-0 = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:		trinity-dbus-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-dbus-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libdbus}-tqt-1-0
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides the TQt-based shared library for applications using the
Qt interface to D-BUS.

See the dbus description for more information about D-BUS in general.

%post -n %{libdbus}-tqt-1-0
/sbin/ldconfig || :

%postun -n %{libdbus}-tqt-1-0
/sbin/ldconfig || :

%files -n %{libdbus}-tqt-1-0
%defattr(-,root,root,-)
%{_libdir}/libdbus-tqt-1.so.0
%{_libdir}/libdbus-tqt-1.so.0.0.0

##########

%package -n %{libdbus}-tqt-1-devel
Summary:		Simple inter-process messaging system (TQt interface)
Group:			Development/Libraries/C and C++
Provides:		libdbus-tqt-1-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{libdbus}-tqt-1-0 = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:		trinity-dbus-tqt-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-dbus-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libdbus}-tqt-1-devel
D-BUS is a message bus, used for sending messages between applications.
Conceptually, it fits somewhere in between raw sockets and CORBA in
terms of complexity.

This package provides the TQt-based shared library for applications using the
Qt interface to D-BUS.

See the dbus description for more information about D-BUS in general.

%post -n %{libdbus}-tqt-1-devel
/sbin/ldconfig || :

%postun -n %{libdbus}-tqt-1-devel
/sbin/ldconfig || :

%files -n %{libdbus}-tqt-1-devel
%defattr(-,root,root,-)
%{_includedir}/dbus-1.0/*
%{_libdir}/libdbus-tqt-1.so
%{_libdir}/libdbus-tqt-1.la
%{_libdir}/pkgconfig/dbus-tqt.pc

##########

%if 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%if 0%{?rhel} == 4
%patch1 -p1 -b .dbustypes
%endif


%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh

%if 0%{?rhel} == 4
export CXXFLAGS="-DDBUS_API_SUBJECT_TO_CHANGE ${CXXFLAGS}"
%endif

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
  \
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
* Sat Oct 11 2014 Francois Andriot <francois.andriot@free.fr> - 1:0.63-2
- Rename package to 'libdbus-tqt-1'

* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1:0.63-1
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2
