# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_version 14.0.0

%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

Name:		trinity-libcaldav
Version:	0.6.5
Release:	%{?!preversion:4}%{?preversion:3_%{preversion}}%{?dist}%{?_variant}

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

License:	GPL
Group:		System Environment/Libraries
Summary:	A client library that adds support for the CalDAV protocol (rfc4791).

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	libtool
%if 0%{?rhel} == 4
BuildRequires:	evolution28-gtk2-devel
%else
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
%endif
BuildRequires:	make

Obsoletes:	libcaldav < %{version}-%{release}
Provides:	libcaldav = %{version}-%{release}

%if 0%{?fedora} || 0%{?rhel} >= 6 || 0%{?suse_version}
BuildRequires:	libcurl-devel
%else
%if 0%{?mgaversion} || 0%{?mdkversion}
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

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
./autogen.sh


%build
# CFLAGS required if CURL is installed on /opt/trinity, e.g. RHEL 5
export CFLAGS="-I%{tde_includedir} -L%{tde_libdir} ${CFLAGS}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

if [ -d /usr/evolution28 ]; then
  export PKG_CONFIG_PATH="/usr/evolution28/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"
fi

%configure \
  --docdir=%{tde_docdir}/libcaldav \
  --includedir=%{tde_includedir} \
  --libdir=%{tde_libdir} \
  
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%__rm -f %{buildroot}%{tde_libdir}/*.a

%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{tde_libdir}/libcaldav.so.*
%{tde_docdir}/libcaldav/

%files devel
%defattr(-,root,root,-)
%{tde_includedir}/libcaldav/caldav.h
%{tde_libdir}/libcaldav.la
%{tde_libdir}/libcaldav.so
%{tde_libdir}/pkgconfig/libcaldav.pc

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig


%Changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.6.5-4
- Initial release for TDE R14.0.0

* Sun Jul 28 2012 Francois Andriot <francois.andriot@free.fr> - 0.6.5-3
- Renames to 'trinity-libcaldav'
- Build on MGA2

* Thu Nov 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.6.5-2debian2.2
- Add missing BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.6.5-2debian2.1
- Initial release for RHEL 6, RHEL 5, and Fedora 15
