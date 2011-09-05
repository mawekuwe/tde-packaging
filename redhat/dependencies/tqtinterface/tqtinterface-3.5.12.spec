# Default version for this component
%if "%{?version}" == ""
%define version 3.5.12
%endif
%define release 7

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%endif

# TQT include files may conflict with QT4 includes, so we move them to a subdirectory.
# Later compiled Trinity products should be aware of that !
%define _includedir %{_prefix}/include/tqt

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
BuildRequires:	qt3-devel >= 3.3.8b
Requires:	qt3 >= 3.3.8b


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

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f admin/Makefile.common

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
CFLAGS=$( pkg-config --libs qt-mt )
%configure \
  --enable-new-ldflags \
  --disable-dependency-tracking \
  --disable-debug --disable-warnings --enable-final

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__mkdir_p %{?buildroot}%{_includedir}
%make_install

%clean
%__rm -rf %{?buildroot}

%files
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%{_includedir}
%{_libdir}/*.so
%{_libdir}/*.la


%changelog
* Sun Sep 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-7
- Import to GIT
- Removes cmake stuff, build with autotools only

* Thu Aug 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-6
- Use '/etc/profile.d/qt.sh' to source QT environment

* Tue Aug 23 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-5
- Add missing BuildRequires

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-4
- Correct macro to install under "/opt", if desired

* Wed Dec 22 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-3
- Re-add '.la' files, needed for kdelibs compilation

* Sat Dec 18 2010  Francois Andriot <francois.andriot@free.fr> - 3.5.12-2
- Add cmake support
- Removes '.la' files

* Fri Dec 17 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-1
- Add macro _trinity_prefix to define custom installation prefix (ex: /opt/trinity)
- Move TQT includes into 'tqt' subdirectory to avoid conflict with 'qt-devel' package (from KDE4)

* Tue Dec 07 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-0
- Initial version

