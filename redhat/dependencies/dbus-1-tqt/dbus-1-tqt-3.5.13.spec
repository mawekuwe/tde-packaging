# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
BuildRequires:	qt3-devel >= 3.3.8d
Requires:	qt3 >= 3.3.8d


Name:		dbus-1-tqt
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}
License:	GPL
Summary:	Dbus TQT Interface
Group:		System Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}.tar.gz

# Fix for a nasty memleak in knetworkmanager
Patch0:		dbus1tqt-3.5.13-memory_leak.patch

BuildRequires:	gcc-c++
BuildRequires:	dbus-devel
BuildRequires:	tqtinterface-devel

%description
Dbus TQT Interface


%package devel
Requires:	%{name}
Summary:	%{name} - Development files
Group:		Development/Libraries

%description devel
Development files for %{name}


%prep
%setup -q -n dependencies/%{name}
#patch0 -p1

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh

%__mkdir build
cd build
%cmake ..
%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__mkdir_p %{?buildroot}%{_includedir}
%__make install DESTDIR=%{?buildroot} -C build

%clean
%__rm -rf %{?buildroot}

%files
%{_bindir}/dbusxml2qt3
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Nov 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5, Fedora 15 and Fedora 16

