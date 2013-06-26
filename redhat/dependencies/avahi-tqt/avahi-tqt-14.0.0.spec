# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_libdir %{tde_prefix}/%{_lib}


Name:		trinity-avahi-tqt
Version:	14.0.0
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:	GPL
Summary:	Avahi TQT Interface
Group:		System Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake >= 2.8
BuildRequires:	trinity-tqt3-devel >= %{version}
BuildRequires:	trinity-tqtinterface-devel >= %{version}
BuildRequires:	gettext-devel
BuildRequires:	libtool
%if 0%{?suse_version}
BuildRequires:	dbus-1-devel
%else
BuildRequires:	dbus-devel
%endif

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}avahi-client-devel
%if 0%{?pclinuxos}
BuildRequires:	libexpat-devel
%else
# On Mageia 2, package is 'lib64expat1-devel', but on Mandriva, 'lib64expat-devel'
BuildRequires:	%{_lib}expat%{?mgaversion:1}-devel
%endif
Provides:		%{_lib}avahi-qt3
%else
BuildRequires:	avahi-devel
%if 0%{?suse_version}
BuildRequires:	libexpat-devel
%else
BuildRequires:	expat-devel
%endif
%endif

Requires:		trinity-tqt3 >= %{version}
Requires:		trinity-tqtinterface >= %{version}

Obsoletes:		avahi-tqt < %{version}-%{release}
Provides:		avahi-tqt = %{version}-%{release}


%description
Avahi TQT Interface


%package devel
Requires:	%{name}
Summary:	%{name} - Development files
Group:		Development/Libraries

%if 0%{?mgaversion} || 0%{?mdkversion}
Provides:		%{_lib}avahi-qt3-devel
%endif

Obsoletes:		avahi-tqt-devel < %{version}-%{release}
Provides:		avahi-tqt-devel = %{version}-%{release}

%description devel
Development files for %{name}


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}


%build
unset QTDIR
./autogen.sh

%configure \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --docdir=%{tde_docdir} \
  --includedir=%{tde_includedir} \
  --libdir=%{tde_libdir} \
  --enable-compat-libdns_sd \
  --with-systemdsystemunitdir=/lib/systemd/system \
  --disable-static

%__make %{?_smp_mflags}

%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot}


%clean
%__rm -rf %{?buildroot}

%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

%files
%defattr(-,root,root,-)
%{tde_libdir}/libavahi-tqt.so.1
%{tde_libdir}/libavahi-tqt.so.1.0.0

%files devel
%defattr(-,root,root,-)
%{tde_includedir}/avahi-tqt/
%{tde_libdir}/libavahi-tqt.so
%{tde_libdir}/libavahi-tqt.la
%{tde_libdir}/pkgconfig/avahi-tqt.pc

%changelog
* Thu Feb 16 2012 Francois Andriot <francois.andriot@free.fr> - 14.0.0-1
- Initial build for TDE R14, using 'tqt3' instead of 'qt3'
