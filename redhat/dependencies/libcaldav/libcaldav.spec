# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_datadir %{_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{_prefix}/include
%define tde_libdir %{_prefix}/%{_lib}

Name:		trinity-libcaldav
Version:	0.6.5
Release:	3%{?dist}%{?_variant}

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

License:	GPL
Group:		System Environment/Libraries
Summary:	A client library that adds support for the CalDAV protocol (rfc4791).

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	libcaldav_0.6.5-2debian2.tar.gz

BuildRequires:	libtool
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
BuildRequires:	make

Obsoletes:	libcaldav < %{version}-%{release}
Provides:	libcaldav = %{version}-%{release}

%if 0%{?fedora} || 0%{?rhel} >= 6
BuildRequires:	libcurl-devel
%else
%if 0%{?mgaversion}
BuildRequires:	%{_lib}curl-devel
%else
# Specific CURL version for TDE on RHEL 5 (and older)
BuildRequires:	trinity-libcurl-devel
%endif
%endif

%description
libcaldev is a client library that adds support for the CalDAV protocol (rfc4791).
The object is to have a library which fully implements the protocol so that it is
easy to integrate CalDAV support into any PIM application.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libcaldav-devel < %{version}-%{release}
Provides:	libcaldav-devel = %{version}-%{release}

%description devel
%{summary}


%prep
%setup -q -n libcaldav-%{version}

%build
autoreconf --force --install --symlink
%configure \
  --docdir=%{tde_docdir}/libcaldav \
  --includedir=%{tde_includedir} \
  --libdir=%{tde_libdir} \
  
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# The include files do not go in the correct directory
%__mv -f %{buildroot}%{tde_includedir}/libcaldav-0.6.2/*.h %{buildroot}%{tde_includedir}
%__rm -rf %{buildroot}%{tde_includedir}/libcaldav-0.6.2

%clean
%__rm -rf %{buildroot}


%files
%{tde_libdir}/*.so.*
%{tde_docdir}/libcaldav

%files devel
%{tde_includedir}/*.h
%{tde_libdir}/*.a
%{tde_libdir}/*.la
%{tde_libdir}/*.so
%{tde_libdir}/pkgconfig/libcaldav.pc


%Changelog
* Sun Jul 28 2012 Francois Andriot <francois.andriot@free.fr> - 0.6.5-3
- Renames to 'trinity-libcaldav'
- Build on MGA2

* Thu Nov 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.6.5-2debian2.2
- Add missing BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.6.5-2debian2.1
- Initial build for RHEL 6, RHEL 5, and Fedora 15
