Name:		libcarddav
Version:	0.6.2
Release:	2debian2%{?dist}

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

License:	GPL
Group:		System Environment/Libraries
Summary:	Libcarddav is a portable CardDAV client implementation.

Source0:	libcarddav_0.6.2-2debian2.tar.gz

%description
Libcarddav is a portable CardDAV client implementation originally developed for the Trinity PIM suite. 
It incorporates full list, get, add, modify, and delete functionality per the latest CardDAV standards. 
Build dependencies are minimal, requiring only libcurl.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name}

%description devel
%{summary}


%prep
%setup -q

%build
autoreconf --force --install --symlink
%configure
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%clean
%__rm -rf %{buildroot}


%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}-0.6.1
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%Changelog
* Fri Oct 21 2011 Francois Andriot <francois.andriot@free.fr> - 0.6.5-2debian2 
- Initial build for RHEL 6.0
