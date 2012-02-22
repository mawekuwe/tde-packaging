# Always build under "/usr"
%define _prefix /usr


Name:		dbus-tqt
Version:	r14
Release:	1%{?dist}
License:	GPL
Summary:	Dbus TQT Interface
Group:		System Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	dbus-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	tqt3-devel >= 3.4.0
BuildRequires:	tqtinterface-devel
Requires:		tqt3 >= 3.4.0
Requires:		tqtinterface

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

%build
%__mkdir build
cd build
%cmake ..

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

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
* Thu Feb 16 2012 Francois Andriot <francois.andriot@free.fr> - r14-1
- Initial build for TDE R14, using 'tqt3' instead of 'qt3'
