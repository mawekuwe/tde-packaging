# Default version for this component
%if "%{?version}" == ""
%define version 3.5.12
%endif
%define release 9

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%endif

# Older RHEL/Fedora versions use packages named "qt", "qt-devel", ..
# whereas newer versions use "qt3", "qt3-devel" ...
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 8
%define _qt_suffix 3
%endif


# TQT include files may conflict with QT4 includes, so we move them to a subdirectory.
# Later compiled Trinity products should be aware of that !
%define _includedir %{_prefix}/include/tqt

# TDE 3.5.12 specific building variables
BuildRequires:	autoconf automake libtool m4
BuildRequires:	qt%{?_qt_suffix}-devel >= 3.3.8b
Requires:		qt%{?_qt_suffix} >= 3.3.8b


Name:		tqtinterface
Version:	%{version}
Release:	%{release}%{?dist}%{?_variant}
License:	GPL
Summary:	Trinity QT Interface
Group:		System Environment/Libraries

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:	%{name}-%{version}.tar.gz

Patch0:		tqtinterface-3.5.12-qtinterface-makefile.patch

BuildRequires:	gcc-c++
BuildRequires:	libXi-devel
BuildRequires:	pth-devel


%description
Trinity QT Interface

%package devel
Group:		Development/Libraries
Summary:	%{name} - Development files
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for %{name}

%prep
%setup -q -n dependencies/%{name}
%patch0 -p1

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"

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
%__make install DESTDIR=%{?buildroot}

# RHEL 5: add newline at end of include files
%if 0%{?rhel} && 0%{?rhel} <= 5
for i in %{?buildroot}%{_includedir}/*.h; do
  echo "" >>${i}
done
%endif

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
* Fri Sep 16 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-9
- Add support for RHEL 5.

* Mon Sep 12 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-8
- Add "Group"

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

