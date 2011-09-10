# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 0

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define cmake_modules_dir %{_datadir}/cmake
%else
%define cmake_modules_dir %{_datadir}/cmake/Modules
%endif

# TQT include files may conflict with QT4 includes, so we move them to a subdirectory.
# Later compiled Trinity products should be aware of that !
%define _includedir %{_prefix}/include/tqt

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
BuildRequires:	qt3-devel >= 3.3.8d
Requires:	qt3 >= 3.3.8d


Name:		tqtinterface
Version:	%{version}
Release:	%{release}%{?dist}%{?_variant}
License:	GPL
Summary:	Trinity QT Interface
Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
Source0:	%{name}-%{version}.tar.gz


BuildRequires:	gcc-c++
BuildRequires:	libXi-devel
BuildRequires:	pth-devel


%description
Trinity QT Interface

%package devel
Requires:	%{name}
Summary:	%{name} - Development files

%description devel
Development files for %{name}

%prep
%setup -q -n dependencies/%{name}

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh

%__mkdir build
cd build
%__cmake \
  -DQT_PREFIX_DIR=${QTDIR} \
  -DQT_VERSION=3 \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DPKGCONFIG_INSTALL_DIR=%{_libdir}/pkgconfig \
  -DBIN_INSTALL_DIR=%{_bindir} \
  -DINCLUDE_INSTALL_DIR=%{_includedir} \
  -DLIB_INSTALL_DIR=%{_libdir} \
  ..

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__mkdir_p %{?buildroot}%{_includedir}
%make_install -C build

# Fix 'tqt.pc': UIC executable is not correct
sed -i %{?buildroot}%{_libdir}/pkgconfig/tqt.pc \
  -e '/^uic_executable=.*/ s,^\(uic_executable=\).*,\1%{_bindir}/uic-tqt,'

# Install 'cmake' modules for a specific package (for later use)
%__mkdir_p %{?buildroot}%{cmake_modules_dir}
for i in cmake/modules/*.cmake; do
  install -m 644 $i %{?buildroot}%{cmake_modules_dir}
done

%clean
%__rm -rf %{?buildroot}

%files
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{cmake_modules_dir}/*.cmake


%changelog
* Sun Aug 28 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
- Built with future TDE version (3.5.13 + cmake + QT3.3.8d)
