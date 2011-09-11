# Default version for this component
%if "%{?version}" == ""
%define version 3.5.12
%define release 5
%endif

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_libdir %{_libdir}/kde3


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

# TDE official patches from SVN, unmodified
# Attempt to fix a kdepim FTBFS based on a missing stdc header #include
Patch0:		http://www.trinitydesktop.org/patches/r1228885.diff

BuildRequires:	tqtinterface
BuildRequires:	trinity-arts
BuildRequires:	trinity-kdelibs
BuildRequires:	gpgme-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	flex
BuildRequires:	libical-devel
BuildRequires:	gnokii-devel

%if 0%{?fedora} >= 15
BuildRequires:	flex-static
%endif

Requires:	trinity-kdelibs

%description
PIM (Personal Information Manager) applications.


%package devel
Requires:	%{name}
Summary:	%{name} - Development files
%description devel
Development files for %{name}.


%prep
%setup -q -n kdepim
%patch0 -p1

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-dependency-tracking \
  --disable-debug --disable-warnings --enable-final \
  --with-extra-includes=%{_includedir}/tqt

# Do NOT use %{?_smp_mflags} for this package, or it will fail to build !
%__make

%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{?buildroot}
%make_install

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
%{_datadir}/services/*
%{_datadir}/mimelnk/application/*
%{_datadir}/config.kcfg/*
%{_libdir}/lib*.so.*
%{tde_libdir}/*.so
%{tde_libdir}/*.so.*
%{tde_libdir}/plugins/designer/*.so
%{_datadir}/servicetypes/*
%{_libdir}/kconf_update_bin/*
%{_libdir}/libakregatorprivate.so
%{_libdir}/libkmailprivate.so
%{tde_docdir}/HTML/en/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{tde_libdir}/*.la
%{tde_libdir}/plugins/designer/*.la
%exclude %{_libdir}/libakregatorprivate.so
%exclude %{_libdir}/libkmailprivate.so

%changelog
* Mon Sep 05 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-5
- Import to GIT

* Tue Aug 23 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-4
- Correct (again) macro to install under "/opt", if desired
- Add missing BuildRequires
- Add 'patch0' to allow compilation with GCC >= 4.5

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-3
- Correct macro to install under "/opt", if desired

* Sun Dec 19 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-2
- Rebuilt

* Fri Dec 17 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-1
- Add macro _kde3_prefix to define custom installation prefix (ex: /opt/kde3)
- Add '--with-extra-includes=%{_includedir}/tqt'

* Wed Dec 15 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-0
- Initial version

