# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}/kde
%define tde_libdir %{_libdir}/trinity


Name:    trinity-kdesdk
Summary: The KDE Software Development Kit (SDK)
Version: %{?version}
Release: %{?release}%{?dist}%{?_variant}

License: GPLv2
Group: User Interface/Desktops
URL:		http://www.trinitydesktop.org/
Vendor: Trinity Project
Packager: Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source: kdesdk-%{version}.tar.gz

# RedHat Legacy patches
Patch1: kdesdk-3.5.7-subversion.patch

Provides: kdesdk3 = %{version}-%{release}

Requires: %{name}-libs = %{version}-%{release}

BuildRequires: libtool
BuildRequires: tqtinterface-devel
BuildRequires: pcre-devel
BuildRequires: trinity-kdelibs-devel
# for kbugbuster/libkcal
BuildRequires: trinity-kdepim-devel
BuildRequires: db4-devel
BuildRequires: desktop-file-utils
# kbabel,  F-7+: flex >= 2.5.33-9
BuildRequires: flex
# umbrello
BuildRequires: libxslt-devel libxml2-devel
%if 0%{?fedora} > 5 || 0%{?rhel} > 4
BuildRequires: binutils-devel
%endif
BuildRequires: perl
BuildRequires: subversion-devel neon-devel

# Obsoletes/Provides
%define cervisia_ver 2.4.7
Provides: cervisia = %{cervisia_ver}-%{release}

%define umbrello_ver 1.5.7
Obsoletes: umbrello < %{umbrello_ver}-%{release}
Provides:  umbrello = %{umbrello_ver}-%{release}


%description
A collection of applications and tools used by developers, including:
* cervisia: a CVS frontend
* kbabel: PO file management
* kbugbuster: a tool to manage the KDE bug report system
* kcachegrind: a browser for data produced by profiling tools (e.g. cachegrind)
* kompare: diff tool
* kuiviewer: displays designer's UI files
* umbrello: UML modeller and UML diagram tool

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Provides: trinity-kdesdk-devel = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Requires: trinity-kdelibs-devel
%description devel
%{summary}.

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-kdelibs
# helps multilib upgrades
Obsoletes: %{name} < %{version}-%{release}
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%setup -q -n kdesdk
%patch1 -p1 -b .subversion


%build
unset QTDIR || :; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LD_LIBRARY_PATH="%{_libdir}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"

%__mkdir build
cd build
%cmake \
  -DWITH_DBSEARCHENGINE=OFF \
  -DBUILD_ALL=ON \
  ..

# Do not use %{?_smp_mflags} !
%__make


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot} 

%__make install DESTDIR=%{?buildroot} -C build

desktop-file-install --vendor "" \
  --dir %{buildroot}%{_datadir}/applications/kde \
  %{buildroot}%{_datadir}/applications/kde/*.desktop \

# make symlinks relative
if [ -d %{buildroot}%{tde_docdir}/HTML/en ]; then
  pushd %{buildroot}%{tde_docdir}/HTML/en
  for i in *; do
     if [ -d $i -a -L $i/common ]; then
        rm -f $i/common
        ln -nfs ../common $i
     fi
  done
  popd
fi

%__rm -f %{buildroot}/%{_datadir}/apps/kapptemplate/admin/Makefile \
      %{buildroot}/%{_datadir}/apps/kapptemplate/admin/Makefile.in


%clean
%__rm -rf %{buildroot}


# trick to replace a dir by a symlink -- Rex
%pre
if [ $1 -gt 0 -a ! -L  %{_docdir}/HTML/en/cervisia/common ]; then 
  rm -rf %{tde_docdir}/HTML/en/cervisia/common ||:
fi

%post
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{tde_docdir}/HTML/en/*
%{_datadir}/apps/*
#%{_datadir}/mimelnk/application/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*
%{_datadir}/applications/kde/*
%{_datadir}/config.kcfg/*
%{tde_libdir}/*
%{_libdir}/libkdeinit_*.so
#%{_mandir}/man1/*

# Removes conflict with package 'rpmdevtool' on RHEL 6
%if "%{_prefix}" == "/usr"
%exclude %{_bindir}/licensecheck
%endif

%files libs
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_includedir}/kbabel
%{_libdir}/lib*.so
%exclude %{_libdir}/libkdeinit_*.so
#%{_libdir}/kmtrace/*
%{_datadir}/cmake/*.cmake


%changelog
* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Mon Sep 05 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
