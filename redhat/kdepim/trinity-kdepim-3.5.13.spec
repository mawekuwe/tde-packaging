# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 3

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}/kde
%define tde_libdir %{_libdir}/trinity

# KDEPIM specific features
%if 0%{?fedora}
%define with_gnokii 1
%else
%define with_gnokii 0
%endif


Name:		trinity-kdepim
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}
License:	GPL
Group:		Applications/Productivity

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
Summary:	PIM (Personal Information Manager) applications

Prefix:		%{_prefix}

Source0:	kdepim-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	gpgme-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	flex
BuildRequires:	libical-devel
BuildRequires:	boost-devel
BuildRequires:	curl-devel

BuildRequires:	libcaldav-devel
BuildRequires:	libcarddav-devel

%if 0%{?with_gnokii}
BuildRequires:	gnokii-devel
%endif

%if 0%{?fedora} >= 15
BuildRequires:	flex-static
%else
%if 0%{?rhel} <= 5
BuildRequires:	trinity-libcurl-devel
%endif
%endif

Requires:	trinity-kdelibs
Requires:	libcaldav
Requires:	libcarddav

%description
PIM (Personal Information Manager) applications.


%package devel
Requires:	%{name}
Summary:	%{name} - Development files
Group: Development/Libraries
%description devel
Development files for %{name}.


%prep
%setup -q -n kdepim


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"
export LD_LIBRARY_PATH="%{_libdir}"

%__mkdir build
cd build
%cmake \
  -DWITH_ARTS=ON \
  -DWITH_SASL=ON \
  -DWITH_NEWDISTRLISTS=ON  \
%if 0%{?with_gnokii}
  -DWITH_GNOKII=ON \
%else
  -DWITH_GNOKII=OFF \
%endif
  -DWITH_EXCHANGE=ON \
  -DWITH_EGROUPWARE=ON \
  -DWITH_KOLAB=ON \
  -DWITH_SLOX=ON \
  -DWITH_GROUPWISE=ON \
  -DWITH_FEATUREPLAN=ON \
  -DWITH_GROUPDAV=ON \
  -DWITH_BIRTHDAYS=ON \
  -DWITH_NEWEXCHANGE=ON \
  -DWITH_SCALIX=ON \
  -DWITH_CALDAV=ON \
  -DWITH_CARDDAV=ON \
  -DWITH_INDEXLIB=ON \
  -DBUILD_ALL=ON \
  ..

# Do not use %{?_smp_mflags} !
%__make 

%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

%clean
%__rm -rf %{?buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/applnk/.hidden/*
%{_datadir}/applnk/*/*
%{_datadir}/apps/*
%{_datadir}/autostart/*.desktop
%{_datadir}/config/*
%{_datadir}/icons/*
%exclude %{_datadir}/icons/default.kde
%{_datadir}/services/*
%{_datadir}/mimelnk/application/*
%{_datadir}/config.kcfg/*
%{_libdir}/lib*.so.*
%{tde_libdir}/*.so
%{tde_libdir}/*.la
%{tde_libdir}/plugins/designer/*.so
%{tde_libdir}/plugins/designer/*.la
%{_datadir}/servicetypes/*
%{_libdir}/kconf_update_bin/*
%{_libdir}/libakregatorprivate.so
%{_libdir}/libkmailprivate.so
%{_libdir}/libkmobiledevice.so
%{tde_docdir}/HTML/en/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%exclude %{_libdir}/libakregatorprivate.so
%exclude %{_libdir}/libkmailprivate.so
%exclude %{_libdir}/libkmobiledevice.so
%{_datadir}/cmake/*.cmake

%changelog
* Sun Nov 27 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Add missing files '*.la'

* Fri Nov 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Updates BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Mon Sep 05 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-0
- Import to GIT
