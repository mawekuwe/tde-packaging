Name:		libcaldav
Version:	0.6.5
Release:	2debian2%{?dist}

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

License:	GPL
Group:		System Environment/Libraries
Summary:	A client library that adds support for the CalDAV protocol (rfc4791).

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	libcaldav_0.6.5-2debian2.tar.gz

%if 0%{?fedora} || 0%{?rhel} >= 6
BuildRequires:	libcurl-devel
%else
BuildRequires:	trinity-libcurl-devel
%endif

%description
libcaldev is a client library that adds support for the CalDAV protocol (rfc4791).
The object is to have a library which fully implements the protocol so that it is
easy to integrate CalDAV support into any PIM application.

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

# The include files do not go in the correct directory
%__mv -f %{buildroot}%{_includedir}/%{name}-0.6.2/*.h %{buildroot}%{_includedir}
%__rm -rf %{buildroot}%{_includedir}/%{name}-0.6.2

%clean
%__rm -rf %{buildroot}


%files
%{_libdir}/*.so.*
%{_datadir}/doc/%{name}

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc


%Changelog
* Fri Oct 21 2011 Francois Andriot <francois.andriot@free.fr> - 0.6.5-2debian2 
- Initial build for RHEL 6.0
