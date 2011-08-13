#
# spec file for package libdbus-1-tqt-0
#
# Copyright (c) 2011 the Trinity Project (opensuse).
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
  
# Please submit bugfixes or comments via http://bugs.trinitydesktop.org/
#

# norootforbuild


Name:           libdbus-1-tqt-0
Url:            http://www.freedesktop.org/wiki/Software/DBusBindings
%define appname libdbus-1-tqt
BuildRequires:  dbus-1-devel libtqt4-devel
License:        GPL v2 or later
Group:          Development/Libraries/C and C++
AutoReqProv:    on
Version:        0.8.1
Release:        1
Summary:        TQt DBus Bindings
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{appname}-%{version}.tar.bz2
Patch1:         fix_ifdef.patch
Patch2:         r785103.patch
Patch3:         r795238.patch
Patch4:         fix_circular_destructor.patch

%description
This library provides TQt-classes for accessing the DBus



Authors:
--------
    Kevin Krammer <kevin.krammer@gmx.at>

%package devel
License:        GPL v2 or later
Summary:        Development files for libdbus-1-tqt
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       dbus-1-devel libtqt4-devel

%description devel
This library provides TQt-classes for accessing the DBus.

This package holds the development files for libdbus-1-tqt.



Authors:
--------
    Kevin Krammer <kevin.krammer@gmx.at>

%package -n dbusxml2tqt
License:        GPL v2 or later
Summary:        Generate TQt-classes from DBus-introspection data
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}

%description -n dbusxml2tqt
dbusxml2tqt allows to generate TQt-classes from DBus-introspection data



Authors:
--------
    Kevin Krammer <kevin.krammer@gmx.at>

%prep
%setup -n %{appname}-%{version} -q
%patch1
%patch2 -p1
%patch3 -p0
%patch4 -p0

%build
mkdir build
cd build
cmake ../
%{__make} %{?jobs:-j%jobs}

%install
make install DESTDIR=$RPM_BUILD_ROOT
#install -D -m 0755 ./tools/dbusxml2qt3/dbusxml2qt3 $RPM_BUILD_ROOT%{_bindir}/dbusxml2tqt
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog COPYING INSTALL
%{_libdir}/libdbus-1-tqt.so.0
%{_libdir}/libdbus-1-tqt.so.0.8.1

%files devel
%defattr(-,root,root)
%{_libdir}/libdbus-1-tqt.so
%dir %{_includedir}/dbus-1.0/tqt
%dir %{_includedir}/dbus-1.0/tqt/dbus
%{_includedir}/dbus-1.0/tqt/dbus/tqdbusconnection.h
%{_includedir}/dbus-1.0/tqt/dbus/tqdbusdata.h
%{_includedir}/dbus-1.0/tqt/dbus/tqdbusdataconverter.h
%{_includedir}/dbus-1.0/tqt/dbus/tqdbusdatalist.h
%{_includedir}/dbus-1.0/tqt/dbus/tqdbusdatamap.h
%{_includedir}/dbus-1.0/tqt/dbus/tqdbuserror.h
%{_includedir}/dbus-1.0/tqt/dbus/tqdbusmacros.h
%{_includedir}/dbus-1.0/tqt/dbus/tqdbusmessage.h
%{_includedir}/dbus-1.0/tqt/dbus/tqdbusobject.h
%{_includedir}/dbus-1.0/tqt/dbus/tqdbusobjectpath.h
%{_includedir}/dbus-1.0/tqt/dbus/tqdbusproxy.h
%{_includedir}/dbus-1.0/tqt/dbus/tqdbusvariant.h
%{_libdir}/pkgconfig/dbus-1-tqt.pc

%files -n dbusxml2tqt
%defattr(-,root,root)
%{_bindir}/dbusxml2tqt

%changelog

