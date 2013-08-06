# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_version 14.0.0

%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

Name:		trinity-libcarddav
Version:	0.6.2
Release:	%{?!preversion:4}%{?preversion:3_%{preversion}}%{?dist}%{?_variant}

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

License:	GPL
Group:		System Environment/Libraries
Summary:	A portable CardDAV client implementation originally developed for the Trinity PIM suite.

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

# CURL support
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

%if 0%{?rhel} == 4
BuildRequires:	evolution28-gtk2-devel
%else
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
%endif
BuildRequires:	make

Obsoletes:	libcarddav < %{version}-%{release}
Provides:	libcarddav = %{version}-%{release}

%description
Libcarddav is a portable CardDAV client implementation originally developed for the Trinity PIM suite. 
It incorporates full list, get, add, modify, and delete functionality per the latest CardDAV standards. 
Build dependencies are minimal, requiring only libcurl.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

Obsoletes:	libcarddav-devel < %{version}-%{release}
Provides:	libcarddav-devel = %{version}-%{release}

%description devel
%{summary}

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
# Fix empty ChangeLog cause invalid macro in 'configure.ac'
echo "%{name} (%{version})" >ChangeLog
./autogen.sh


%build
unset QTDIR QTINC QTLIB

# CFLAGS required if CURL is installed on /opt/trinity, e.g. RHEL 5
export CFLAGS="-I%{tde_includedir} -L%{tde_libdir} ${RPM_OPT_FLAGS}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

# RHEL4 stuff
if [ -d /usr/evolution28 ]; then
  export PKG_CONFIG_PATH="/usr/evolution28/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"
fi

%configure \
  --includedir=%{tde_includedir} \
  --libdir=%{tde_libdir} \
  \
  --disable-dependency-tracking

%__make %{?_smp_mflags}


%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} LIBTOOL=$(which libtool)

%__rm -f %{buildroot}%{tde_libdir}/libcarddav.a


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{tde_libdir}/libcarddav.so.*

%files devel
%defattr(-,root,root,-)
%{tde_includedir}/libcarddav/
%{tde_libdir}/libcarddav.la
%{tde_libdir}/libcarddav.so
%{tde_libdir}/pkgconfig/libcarddav.pc

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig


%Changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.6.2-4
- Initial release for TDE R14.0.0

* Sat Jul 28 2012 Francois Andriot <francois.andriot@free.fr> - 0.6.2-3
- Renames to 'trinity-libcarddav'
- Build on MGA2

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.6.2-2
- Initial release for RHEL 6, RHEL 5, and Fedora 15
