# Always build under "/usr"
%define _prefix /usr


Name:		avahi-tqt
Version:	r14
Release:	1%{?dist}
License:	GPL
Summary:	Avahi TQT Interface
Group:		System Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}.tar.gz

# Allows building with TQT3 instead of QT3
Patch1:		avahi-tqt-moc-tqt3.patch

BuildRequires:	gcc-c++
BuildRequires:	avahi-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	tqt3-devel >= 3.4.0
BuildRequires:	tqtinterface-devel
Requires:		tqt3 >= 3.4.0
Requires:		tqtinterface

%description
Avahi TQT Interface


%package devel
Requires:	%{name}
Summary:	%{name} - Development files
Group:		Development/Libraries


%description devel
Development files for %{name}


%prep
%setup -q -n dependencies/%{name}
%patch1 -p1

%build
./autogen.sh
%configure \
	--enable-compat-libdns_sd \
	--with-systemdsystemunitdir=/lib/systemd/system

%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot}

%clean
%__rm -rf %{?buildroot}


%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/libavahi-tqt.a

%changelog
* Thu Feb 16 2012 Francois Andriot <francois.andriot@free.fr> - r14-1
- Initial build for TDE R14, using 'tqt3' instead of 'qt3'
