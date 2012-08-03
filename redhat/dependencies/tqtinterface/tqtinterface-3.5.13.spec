# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%define cmake_modules_dir %{tde_prefix}/share/cmake
%else
%define cmake_modules_dir %{_datadir}/cmake/Modules
%endif

# TQT include files may conflict with QT4 includes, so we move them to a subdirectory.
# Later compiled Trinity products should be aware of that !
%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

Name:		tqtinterface
Version:	3.5.13
Release:	3%{?dist}%{?_variant}
License:	GPL
Summary:	Trinity QT Interface
Group:		System Environment/Libraries

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	%{name}-%{version}.tar.gz

# [tqtinterface] Add missing endian-ness defines [Bug #727] [Commit #458e74a6]
Patch1:		tqtinterface-3.5.13-add_missing_endianness_defines.patch

# TDE 3.5.13 specific building variables
BuildRequires:	cmake >= 2.8
BuildRequires:	qt3-devel >= 3.3.8.d
Requires:		qt3 >= 3.3.8.d

BuildRequires:	gcc-c++
BuildRequires:	pth-devel
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}xi-devel
%else
BuildRequires:	libXi-devel
%endif


%description
Trinity QT Interface

%package devel
Group:		Development/Libraries
Summary:	%{name} - Development files
Requires:	%{name} = %{version}-%{release}
Requires:	qt3-devel >= 3.3.8.d

%description devel
Development files for %{name}

%prep
%setup -q -n dependencies/%{name}
%patch1 -p1

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh

%if 0%{?rhel} || 0%{?fedora}
%__mkdir_p build
cd build
%endif

%cmake \
  -DQT_PREFIX_DIR=${QTDIR} \
  -DQT_VERSION=3 \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DINCLUDE_INSTALL_DIR=%{tde_includedir}/tqt \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DPKGCONFIG_INSTALL_DIR=%{tde_libdir}/pkgconfig \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  ..

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__mkdir_p %{?buildroot}%{_includedir}
%__make install DESTDIR=%{?buildroot} -C build

# RHEL 5: add newline at end of include files to avoid warnings
%if 0%{?rhel} && 0%{?rhel} <= 5
for i in %{?buildroot}%{_includedir}/*.h; do
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

%files
%{tde_bindir}/*
%{tde_libdir}/*.so.*

%files devel
%{tde_includedir}/tqt
%{tde_libdir}/*.so
%{tde_libdir}/*.la
%{tde_libdir}/pkgconfig/*.pc
%{cmake_modules_dir}/*.cmake


%changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Rebuilt for Fedora 17
- Add missing endian-ness defines [Bug #727] [Commit #458e74a6]

* Sun Nov 06 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Add missing Requires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sun Aug 28 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
- Built with future TDE version (3.5.13 + cmake + QT3.3.8d)
