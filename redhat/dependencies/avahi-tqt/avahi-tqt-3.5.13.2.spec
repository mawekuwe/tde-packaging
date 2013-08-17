# TDE specific building variables
%define tde_version 3.5.13.2
%define tde_prefix /usr
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}


Name:		trinity-avahi-tqt
Epoch:		1
Version:	0.6.30
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:	GPL
Summary:	Avahi TQT Interface
Group:		System Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	qt3-devel >= 3.3.8d
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	gettext-devel
BuildRequires:	libtool
%if 0%{?suse_version}
BuildRequires:	dbus-1-devel
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	dbus-devel
%endif

# AVAHI support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}avahi-client-devel
Provides:		%{_lib}avahi-qt3
%endif
%if 0%{?suse_version} || 0%{?rhel} || 0%{?fedora}
BuildRequires:	avahi-devel
%endif

# EXPAT support
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	expat-devel
%endif
%if 0%{?suse_version} || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	libexpat-devel
%endif

Requires:		qt3 >= 3.3.8d
Requires:		trinity-tqtinterface >= %{tde_version}

Obsoletes:		avahi-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		avahi-tqt = %{?epoch:%{epoch}:}%{version}-%{release}


%description
Avahi TQT Interface


%package devel
Summary:	%{name} - Development files
Group:		Development/Libraries
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?mgaversion} || 0%{?mdkversion}
Provides:		%{_lib}avahi-qt3-devel
%endif

Obsoletes:		avahi-tqt-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		avahi-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Development files for %{name}


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
./autogen.sh


%build
unset QTDIR || : ; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --exec-prefix=%{tde_prefix} \
  --includedir=%{tde_includedir} \
  --libdir=%{tde_libdir} \
  \
  --disable-static \
  --disable-dependency-tracking \
  \
  --enable-compat-libdns_sd \
  --with-systemdsystemunitdir=/lib/systemd/system

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
* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2
