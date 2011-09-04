# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%endif

# TQT include files may conflict with QT4 includes, so we move them to a subdirectory.
# Later compiled Trinity products should be aware of that !
%define _includedir %{_prefix}/include/tqt

# Currently we build with (RHEL 6):
#  automake-1.11.1-1.2.el6.noarch
#  autoconf-2.63-5.1.el6.noarch
#  libtool-2.2.6-15.5.el6.x86_64
#  m4-1.4.13-5.el6.x86_64

# Currently we build with (Fedora 15):
#  automake-1.11.1-5.fc14.noarch
#  autoconf-2.63-5.1.f15.noarch (backport from EL6)
#  libtool-2.2.6-15.5.f15.x86_64 (backport from EL6)
#  m4-1.4.13-5.f15.x86_64 (backport from EL6)

Name:		tqtinterface
Version:	3.5.12
Release:	7%{?dist}%{?_variant}
License:	GPL
Summary:	Trinity QT Interface
Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
Source0:	http://mirror3.tokra.lv/releases/3.5.12/dependencies/tqtinterface-3.5.12.tar.gz

BuildRequires:	autoconf automake libtool m4
BuildRequires:	qt3-devel >= 3.3.8b
BuildRequires:	gcc-c++
BuildRequires:	libXi-devel
BuildRequires:	pth-devel

Requires:	qt3 >= 3.3.8b

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

