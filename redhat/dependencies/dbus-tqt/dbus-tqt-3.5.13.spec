# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _libdir %{_prefix}/lib
%endif

Name:		dbus-tqt
Version:	%{?version}
Release:	0%{?dist}%{?_variant}
License:	GPL
Summary:	Dbus TQT Interface
Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	qt3-devel >= 3.3.8d
BuildRequires:	gcc-c++
BuildRequires:	dbus-qt-devel
BuildRequires:	tqtinterface-devel
BuildRequires:	cmake >= 2.8

Requires:	qt3 >= 3.3.8d

%description
Dbus TQT Interface

%package devel
Requires:	%{name}
Summary:	%{name} - Development files

%description devel
Development files for %{name}

%prep
%setup -q -n dependencies/%{name}

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh

%__mkdir build
cd build
%cmake ..

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__mkdir_p %{?buildroot}%{_includedir}
%make_install -C build

%clean
%__rm -rf %{?buildroot}

%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/dbus-1.0/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

%changelog
* Sun Sep 02 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13pre-0
- Import to GIT
- Built with future TDE version (3.5.13 + cmake + QT3.3.8d)
