# Default version for this component
%if "%{?version}" == ""
%define version 3.5.12
%endif
%define release 9

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific variables
BuildRequires:	autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_libdir %{_libdir}/kde3

# Older RHEL/Fedora versions use packages named "qt", "qt-devel", ..
# whereas newer versions use "qt3", "qt3-devel" ...
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 8
%define _qt_suffix 3
%endif


Name:		trinity-kdelibs
Version:	%{version}
Release:	%{?release}%{?dist}%{?_variant}
License:	GPL
Summary:	TDE Libraries
Group:		System Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kdelibs-%{version}.tar.gz
Patch0:		kdelibs-3.5.13-maxlinelength.patch

BuildRequires:	libtool
BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	avahi-devel
BuildRequires:	lua-devel
BuildRequires:	krb5-devel libxslt-devel cups-devel libart_lgpl-devel pcre-devel
BuildRequires:	libutempter-devel
BuildRequires:	bzip2-devel
BuildRequires:	openssl-devel
BuildRequires:	gcc-c++
BuildRequires:	alsa-lib-devel
BuildRequires:	libidn-devel
BuildRequires:	qt%{?_qt_suffix}-devel
BuildRequires:	avahi-qt3-devel
BuildRequires:	jasper-devel
BuildRequires:	libtiff-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:	glib2-devel

Requires:		tqtinterface
Requires:		trinity-arts
Requires:		avahi
Requires:		qt%{?_qt_suffix}
Requires:		avahi-qt3


Provides:	kdelibs%{?_qt_suffix} = %{version}
%if "%{?_prefix}" == "/usr"
Obsoletes:		kdelibs%{?_qt_suffix} <= 3.5.10
%endif

%description
Libraries for the Trinity Desktop Environment:
KDE Libraries included: kdecore (KDE core library), kdeui (user interface),
kfm (file manager), khtmlw (HTML widget), kio (Input/Output, networking),
kspell (spelling checker), jscript (javascript), kab (addressbook),
kimgio (image manipulation).


%package devel
Summary:	%{name} - Development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	kdelibs%{?_qt_suffix}-devel = %{version}
%if "%{?_prefix}" == "/usr"
Obsoletes:	kdelibs%{?_qt_suffix}-devel <= 3.5.10
%endif

%description devel
This package includes the header files you will need to compile
applications for TDE.

%package apidocs
Group:		Development/Libraries
Summary:	%{name} - API documentation
Requires:	%{name} = %{version}-%{release}
Provides:	kdelibs%{?_qt_suffix}-apidocs = %{version}
%if "%{?_prefix}" == "/usr"
Obsoletes:	kdelibs%{?_qt_suffix}-apidocs <= 3.5.10
%endif

%description apidocs
This package includes the TDE API documentation in HTML
format for easy browsing


%prep
%setup -q -n kdelibs
%patch0 -p1

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LD_LIBRARY_PATH="%{_libdir}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

# On older RHEL, libXrandr is too old so krandr cannot be compiled.
# Kspell2 does not compile either.
%if 0%{?rhel} && 0%{?rhel} < 6
export DO_NOT_COMPILE="krandr"
%endif

%configure \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-dependency-tracking \
  --disable-debug --disable-warnings --enable-final \
  --disable-fast-malloc \
  --enable-cups \
  --enable-mitshm \
  --enable-pie \
  --enable-sendfile \
  --with-distribution="$(cat /etc/redhat-release 2>/dev/null)" \
  --with-alsa \
  --without-aspell \
  --without-hspell \
  --disable-libfam \
  --enable-dnotify \
  --enable-inotify \
  --with-utempter \
  --with-jasper \
  --with-openexr \
  --with-xinerama \
  --enable-closure \
  --with-extra-includes=%{_includedir}/tqt
  
# Do NOT use %{?_smp_mflags} for this package, or it will fail to build !
%__make


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot}

%__mkdir_p %{?buildroot}%{_sysconfdir}/ld.so.conf.d
cat <<EOF >%{?buildroot}%{_sysconfdir}/ld.so.conf.d/trinity.conf
%if "%{?_prefix}" != "/usr"
%{_libdir}
%endif
%{tde_libdir}
EOF

# Moves the XDG configuration files to TDE directory
%if "%{_prefix}" != "/usr"
%__install -p -D -m644 \
	"%{?buildroot}%{_sysconfdir}/xdg/menus/applications.menu" \
	"%{?buildroot}%{_prefix}/etc/xdg/menus/kde-applications.menu"
%__rm -rf "%{?buildroot}%{_sysconfdir}/xdg"
%else
%__mv -f "%{?buildroot}%{_sysconfdir}/xdg/menus/applications.menu" "%{?buildroot}%{_sysconfdir}/xdg/menus/kde-applications.menu"
%endif


%clean
%__rm -rf %{?buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README
%doc COPYING.LIB
%{_bindir}/artsmessage
%{_bindir}/cupsdconf
%{_bindir}/cupsdoprint
%{_bindir}/dcop
%{_bindir}/dcopclient
%{_bindir}/dcopfind
%{_bindir}/dcopobject
%{_bindir}/dcopquit
%{_bindir}/dcopref
%{_bindir}/dcopserver
%{_bindir}/dcopserver_shutdown
%{_bindir}/dcopstart
%{_bindir}/filesharelist
%{_bindir}/fileshareset
%{_bindir}/imagetops
%{_bindir}/kab2kabc
%{_bindir}/kaddprinterwizard
%{_bindir}/kbuildsycoca
%{_bindir}/kcmshell
%{_bindir}/kconf_update
%{_bindir}/kcookiejar
%{_bindir}/kde-config
%{_bindir}/kde-menu
%{_bindir}/kded
%{_bindir}/kdeinit
%{_bindir}/kdeinit_shutdown
%{_bindir}/kdeinit_wrapper
%{_bindir}/kdesu_stub
%{_bindir}/kdontchangethehostname
%{_bindir}/kdostartupconfig
%{_bindir}/kfile
%{_bindir}/kfmexec
%{_bindir}/khotnewstuff
%{_bindir}/kinstalltheme
%{_bindir}/kio_http_cache_cleaner
%{_bindir}/kio_uiserver
%{_bindir}/kioexec
%{_bindir}/kioslave
%{_bindir}/klauncher
%{_bindir}/kmailservice
%{_bindir}/kmimelist
%attr(4755,root,root) %{_bindir}/kpac_dhcp_helper
%{_bindir}/ksendbugmail
%{_bindir}/kshell
%{_bindir}/kstartupconfig
%{_bindir}/ktelnetservice
%{_bindir}/ktradertest
%{_bindir}/kwrapper
%{_bindir}/lnusertemp
%{_bindir}/make_driver_db_cups
%{_bindir}/make_driver_db_lpr
%{_bindir}/meinproc
%{_bindir}/networkstatustestservice
%{_bindir}/start_kdeinit
%{_bindir}/start_kdeinit_wrapper
%attr(4755,root,root) %{_bindir}/kgrantpty
%{_libdir}/lib*.so.*
%{_libdir}/libkdeinit_*.so
%{_libdir}/lib*.la
%{tde_libdir}/
%{_datadir}/applications/kde/*.desktop
%{_datadir}/autostart/kab2kabc.desktop
%{_datadir}/applnk/kio_iso.desktop
%{_datadir}/apps/*
%exclude %{_datadir}/apps/ksgmltools2/
%config(noreplace) %{_datadir}/config/*
%{_datadir}/emoticons/*
%{_datadir}/icons/default.kde
%{_datadir}/mimelnk/magic
%{_datadir}/mimelnk/*/*.desktop
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/icons/crystalsvg/
%{tde_docdir}/HTML/en/kspell
# remove conflicts with kdelibs-4
%if "%{?_prefix}" != "/usr"
%{_bindir}/checkXML
%{_bindir}/ksvgtopng
%{_bindir}/kunittestmodrunner
%{_bindir}/preparetips
%{_datadir}/icons/hicolor/index.theme
%{_datadir}/locale/all_languages
%{tde_docdir}/HTML/en/common/*
%else
%exclude %{_bindir}/checkXML
%exclude %{_bindir}/ksvgtopng
%exclude %{_bindir}/kunittestmodrunner
%exclude %{_bindir}/preparetips
%exclude %{_datadir}/config/colors
%exclude %{_datadir}/config/kdebug.areas
%exclude %{_datadir}/config/kdebugrc
%exclude %{_datadir}/config/ksslcalist
%exclude %{_datadir}/config/ui/ui_standards.rc
%exclude %{_datadir}/icons/hicolor/index.theme
%exclude %{_datadir}/locale/all_languages
%exclude %{tde_docdir}/HTML/en/common/*
%endif
%{_sysconfdir}/ld.so.conf.d/trinity.conf

# Avoid conflict with 'redhat-menus' package
%if "%{_prefix}" == "/usr"
%{_sysconfdir}/xdg/menus/kde-applications.menu
%else
%{_prefix}/etc/xdg/menus/kde-applications.menu
%endif

%files devel
%defattr(-,root,root,-)
%{_bindir}/dcopidl*
%{_bindir}/kconfig_compiler
%{_bindir}/makekdewidgets
%{_datadir}/apps/ksgmltools2/
%{_includedir}/
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%exclude %{_libdir}/libkdeinit_*.so

%files apidocs
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}/
%{tde_docdir}/HTML/en/kdelibs*


%changelog
* Sun Nov 29 2911 Francois Andriot <francois.andriot@free.fr> - 3.5.12-9
- Moves XDG files in TDE prefix to avoid conflict with distro-provided KDE
- Disable 'max line length' detection
- Add missing BuildRequires
- Disable 'max line length' detection

* Fri Sep 16 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-8
- Add support for RHEL 5.

* Thu Sep 15 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-7
- Add missings 'BuildRequires'
- Re-add lost 'ld.so.conf' file

* Mon Sep 12 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-6
- Add "Group" field

* Sun Sep 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-5
- Import to GIT
- Removes cmake stuff, build with autotools only

* Tue Aug 23 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-4
- Add missing BuildRequires

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-3
- Correct macro to install under "/opt", if desired

* Sun Dec 19 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-2
- Rebuilt 

* Fri Dec 17 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-1
- Add macro _kde3_prefix to define custom installation prefix (ex: /opt/trinity)
- Add '--with-extra-includes=%{_includedir}/tqt'

* Wed Dec 14 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-0
- Initial version

