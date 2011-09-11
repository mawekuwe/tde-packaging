# Default version for this component
%if "%{?version}" == ""
%define version 3.5.12
%endif
%define release 5

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific variables
BuildRequires:	autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_libdir %{_libdir}/kde3


Name:		trinity-kdelibs
Version:	%{version}
Release:	%{?release}%{?dist}%{?_variant}
License:	GPL
Summary:	Trinity KDE Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Source0:	kdelibs-%{version}.tar.gz
Prefix:		%{_prefix}

BuildRequires:	libtool
BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	qt3-devel
BuildRequires:	avahi-devel avahi-qt3-devel
BuildRequires:	lua-devel
BuildRequires:	krb5-devel libxslt-devel cups-devel libart_lgpl-devel pcre-devel
BuildRequires:	libutempter-devel
BuildRequires:	bzip2-devel
BuildRequires:	openssl-devel

Requires:	tqtinterface
Requires:	trinity-arts
Requires:	qt3
Requires:	avahi avahi-qt3

%if "%{?_prefix}" == "/usr"
Obsoletes:	kdelibs3
%endif

%description
Libraries for the Trinity K Desktop Environment

%package devel
Requires:	%{name}
Summary:	%{name} - Development files
%if "%{?_prefix}" == "/usr"
Obsoletes:	kdelibs3-devel
%endif

%description devel
Development files for %{name}

%package apidocs
Requires:	%{name}
Summary:	%{name} - API documentation

%description apidocs
This package includes the KDE 3 API documentation in HTML
format for easy browsing

%prep
%setup -q -n kdelibs

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LD_LIBRARY_PATH="%{_libdir}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

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
  --with-extra-includes=%{_includedir}/tqt
  
# Do NOT use %{?_smp_mflags} for this package, or it will fail to build !
%__make


%install
%__rm -rf %{?buildroot}
%__mkdir_p %{?buildroot}
%make_install


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

# Provided by 'redhat-menus' package
%exclude %{_sysconfdir}/xdg/menus/applications.menu

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

