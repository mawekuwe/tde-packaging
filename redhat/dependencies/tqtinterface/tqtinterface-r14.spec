# Always build under "/usr"
%define _prefix /usr
%define cmake_modules_dir %{_datadir}/cmake/Modules

Name:		tqtinterface
Version:	r14
Release:	1%{?dist}
License:	GPL
Summary:	Trinity QT Interface
Group:		System Environment/Libraries

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	%{name}-%{version}.tar.gz


BuildRequires:	cmake >= 2.8
BuildRequires:	tqt3-devel >= 3.4.0
BuildRequires:	gcc-c++
BuildRequires:	libXi-devel
BuildRequires:	pth-devel

Requires:		tqt3 >= 3.4.0

%description
Trinity QT Interface

%package devel
Group:		Development/Libraries
Summary:	%{name} - Development files
Requires:	%{name} = %{version}-%{release}
Requires:	tqt3-devel >= 3.4.0

%description devel
Development files for %{name}

%prep
%setup -q -n dependencies/%{name}

%build
%__mkdir build
cd build
%cmake \
  -DQT_VERSION=3 \
  -DINCLUDE_INSTALL_DIR=%{_includedir}/tqt \
  -DMOC_EXECUTABLE=/usr/bin/moc-tqt3 \
  -DUIC_EXECUTABLE=/usr/bin/uic-tqt3 \
  ..

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
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
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/tqt/
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{cmake_modules_dir}/*.cmake


%changelog
* Tue Feb 14 2012 Francois Andriot <francois.andriot@free.fr> - r14-1
- Initial build for TDE R14, using 'tqt3' instead of 'qt3'
