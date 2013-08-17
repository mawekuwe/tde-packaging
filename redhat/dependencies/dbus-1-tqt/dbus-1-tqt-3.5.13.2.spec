# TDE specific building variables
%define tde_version 3.5.13.2
%define tde_prefix /usr
%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

Name:		trinity-dbus-1-tqt
Epoch:		1
Version:	0.9
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:	GPL
Summary:	Dbus TQT Interface
Group:		System Environment/Libraries

Obsoletes:		dbus-1-tqt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		dbus-1-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	gcc-c++
%if 0%{?suse_version}
BuildRequires:	dbus-1-devel
%else
BuildRequires:	dbus-devel
%endif

BuildRequires:	cmake >= 2.8
BuildRequires:	qt3-devel >= 3.3.8d
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
Requires:		qt3 >= 3.3.8d


%description
Dbus TQT Interface

%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

%files
%defattr(-,root,root,-)
%{tde_bindir}/dbusxml2qt3
%{tde_libdir}/libdbus-1-tqt.so.0
%{tde_libdir}/libdbus-1-tqt.so.0.0.0

##########

%package devel
Requires:	%{name}
Summary:	%{name} - Development files
Group:		Development/Libraries

Obsoletes:		dbus-1-tqt-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		dbus-1-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Development files for %{name}

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

%files devel
%defattr(-,root,root,-)
%{tde_includedir}/*.h
%{tde_libdir}/libdbus-1-tqt.so
%{tde_libdir}/libdbus-1-tqt.la
%{tde_libdir}/pkgconfig/*.pc

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR || : ; . /etc/profile.d/qt?.sh
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%__mkdir_p build
cd build
%endif

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_includedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  ..

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build


%clean
%__rm -rf %{?buildroot}


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1:0.9-1
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2
