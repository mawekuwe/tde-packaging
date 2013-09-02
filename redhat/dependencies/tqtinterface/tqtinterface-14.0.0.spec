# TDE specific building variables
%define tde_version 14.0.0
%define tde_prefix /usr
%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define cmake_modules_dir %{_datadir}/cmake/Modules

Name:		trinity-tqtinterface
Version:	%{tde_version}
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:	GPL
Summary:	Trinity QT Interface
Group:		System Environment/Libraries

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	cmake >= 2.8
BuildRequires:	trinity-tqt3-devel >= 3.5.0
Requires:		trinity-tqt3 >= 3.5.0

BuildRequires:	gcc-c++

# PTHREAD support
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
BuildRequires:	pth-devel
%endif

# X11 libraries
%if 0%{?rhel} == 4
BuildRequires:	xorg-x11-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}xi-devel
%endif
%if 0%{?suse_version} >= 1220 || 0%{?rhel} >= 5 || 0%{?fedora}
BuildRequires:	libXi-devel
%endif
%if 0%{?suse_version} == 1140
BuildRequires:	libXi6-devel
%endif

Obsoletes:	tqtinterface < %{version}-%{release}
Provides:	tqtinterface = %{version}-%{release}


%description
Trinity QT Interface


%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

%files
%defattr(-,root,root,-)
%{tde_bindir}/convert_qt_tqt1
%{tde_bindir}/convert_qt_tqt2
%{tde_bindir}/convert_qt_tqt3
%{tde_bindir}/dcopidl-tqt
%{tde_bindir}/dcopidl2cpp-tqt
%{tde_bindir}/dcopidlng-tqt
%{tde_bindir}/mcopidl-tqt
%{tde_bindir}/moc-tqt
%{tde_bindir}/tmoc
%{tde_bindir}/tqt-replace
%{tde_bindir}/tqt-replace-stream
%{tde_bindir}/uic-tqt
%{tde_libdir}/libtqassistantclient.so.4
%{tde_libdir}/libtqassistantclient.so.4.2.0
%{tde_libdir}/libtqt.so.4
%{tde_libdir}/libtqt.so.4.2.0

##########

%package devel
Group:		Development/Libraries
Summary:	%{name} - Development files
Requires:	%{name} = %{version}-%{release}
Requires:	trinity-tqt3-devel >= 3.5.0

Obsoletes:	tqtinterface-devel < %{version}-%{release}
Provides:	tqtinterface-devel = %{version}-%{release}

%description devel
Development files for %{name}

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

%files devel
%defattr(-,root,root,-)
%{tde_includedir}/tqt/
%{tde_libdir}/libtqassistantclient.la
%{tde_libdir}/libtqassistantclient.so
%{tde_libdir}/libtqt.la
%{tde_libdir}/libtqt.so
%{tde_libdir}/pkgconfig/tqt.pc
%{tde_libdir}/pkgconfig/tqtqui.pc
%{cmake_modules_dir}/*.cmake

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}

%build
unset QTDIR QTINC QTLIB

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
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DQTDIR="%{tde_datadir}/tqt3" \
  -DQT_INCLUDE_DIRS="%{tde_includedir}/tqt3" \
  -DQT_LIBRARY_DIRS="%{tde_libdir}" \
  \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  -DINCLUDE_INSTALL_DIR=%{tde_includedir}/tqt \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
\
  -DCMAKE_LIBRARY_PATH="%{tde_libdir}" \
  -DCMAKE_INCLUDE_PATH="%{tde_includedir}" \
  \
  -DWITH_QT3="ON" \
  -DBUILD_ALL="ON" \
  -DUSE_QT3="ON" \
  ..

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

# RHEL 5: add newline at end of include files to avoid warnings
%if 0%{?rhel} && 0%{?rhel} <= 5
for i in %{?buildroot}%{tde_includedir}/tqt/*.h; do
  echo "" >>${i}
done
%endif

# Install 'cmake' modules for development use
%__mkdir_p %{?buildroot}%{cmake_modules_dir}
for i in cmake/modules/*.cmake; do
  %__install -m 644 $i %{?buildroot}%{cmake_modules_dir}
done


%clean
%__rm -rf %{?buildroot}


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 14.0.0-1
- Initial release for TDE 14.0.0
