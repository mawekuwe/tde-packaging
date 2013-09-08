# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_version 3.5.13.2

# TDE specific variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:			trinity-tdelibs
Version:		%{tde_version}
Release:		%{?!preversion:3}%{?preversion:2_%{preversion}}%{?dist}%{?_variant}
License:		GPL
Summary:		TDE Libraries
Group:			Environment/Libraries

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz

# Fix categories in T-menu
Patch1:			tdelibs-3.5.13.2-fix_xdg_menu.patch
# Fix startup of KDE4 applications
Patch2:			tdelibs-3.5.13.2-fix-starting-kde4-applications.patch

# Patches from Mandriva
Patch101:		tdelibs-3.5.13.2-xdg_dirs_set_path.patch
Patch102:		tdelibs-3.5.13.2-cups_by_default.patch

Obsoletes:		tdelibs < %{version}-%{release}
Provides:		tdelibs = %{version}-%{release}
Obsoletes:		trinity-kdelibs < %{version}-%{release}
Provides:		trinity-kdelibs = %{version}-%{release}
Obsoletes:		trinity-kdelibs-apidocs < %{version}-%{release}
Provides:		trinity-kdelibs-apidocs = %{version}-%{release}


BuildRequires:	cmake >= 2.8
BuildRequires:	libtool
BuildRequires:	qt3-devel >= 3.3.8.d
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	krb5-devel
BuildRequires:	libxslt-devel
BuildRequires:	cups-devel
BuildRequires:	openssl-devel
BuildRequires:	gcc-c++
BuildRequires:	alsa-lib-devel
BuildRequires:	libidn-devel
BuildRequires:	libtiff-devel
BuildRequires:	glib2-devel
# LUA support are not ready yet
#BuildRequires:	lua-devel

# LIBART_LGPL support
BuildRequires:	libart_lgpl-devel

# ASPELL support
BuildRequires:	aspell
BuildRequires:	aspell-devel

# GAMIN support
#  Not on openSUSE.
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:	gamin-devel
%endif

# PCRE support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_pcre 1
BuildRequires:	pcre-devel
%endif

# INOTIFY support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_inotify 1
%endif

# BZIP2 support
%if 0%{?suse_version}
BuildRequires:	libbz2-devel
%else
BuildRequires:	bzip2-devel
%endif

# UTEMPTER support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	libutempter-devel
%endif
%if 0%{?rhel} == 4
BuildRequires:	utempter
%endif
%if 0%{?suse_version}
BuildRequires:	utempter-devel
%endif

# HSPELL support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_hspell 1
BuildRequires:	hspell-devel
%endif

# JASPER support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_jasper 1
%if 0%{?suse_version}
BuildRequires:	libjasper-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}jasper-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	jasper-devel
%endif
%endif

# AVAHI support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_avahi 1
BuildRequires:	trinity-avahi-tqt-devel >= 1:0.6.30
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}avahi-client-devel
Requires:		%{_lib}avahi-client3
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	avahi-devel
Requires:		avahi
%endif
%endif

# OPENEXR support
%if 0%{?rhel} >=5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_openexr 1
BuildRequires:	OpenEXR-devel
%endif

# LIBTOOL
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}ltdl-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libtool-ltdl-devel
%endif
%if 0%{?rhel} == 4 || 0%{?suse_version} == 1140
BuildRequires:	libtool
%endif

# X11 support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	x11-proto-devel
BuildRequires:	%{_lib}xcomposite%{?mgaversion:1}-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	xorg-x11-proto-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libXcomposite-devel
%endif
%if 0%{?rhel} == 4
BuildRequires:	xorg-x11-devel
%endif

# ICEAUTH
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version} >= 1220
Requires:		iceauth
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora}
Requires:		xorg-x11-server-utils
%endif
%if 0%{?rhel} == 4 || 0%{?suse_version}
Requires:		xorg-x11
%endif

# XZ support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
%define with_lzma 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}lzma-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	xz-devel
%endif
%endif

# Certificates support
%if 0%{?rhel} >= 6 || 0%{?fedora}
%define	cacert	%{_sysconfdir}/ssl/certs/ca-certificates.crt
Requires:		ca-certificates
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
%define	cacert	%{_sysconfdir}/ssl/certs/ca-bundle.crt
Requires:		openssl
%endif
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
%define	cacert	%{_sysconfdir}/pki/tls/certs/ca-bundle.crt
Requires:		openssl
%endif

# Trinity dependencies
Requires:		qt3 >= 3.3.8.d
Requires:		trinity-tqtinterface >= %{tde_version}
Requires:		trinity-arts >= 1:1.5.10


%description
Libraries for the Trinity Desktop Environment:
TDE Libraries included: tdecore (TDE core library), kdeui (user interface),
kfm (file manager), khtmlw (HTML widget), tdeio (Input/Output, networking),
kspell (spelling checker), jscript (javascript), kab (addressbook),
kimgio (image manipulation).

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING-DOCS COPYING.LIB README TODO
%{tde_bindir}/artsmessage
%{tde_bindir}/cupsdconf
%{tde_bindir}/cupsdoprint
%{tde_bindir}/dcop
%{tde_bindir}/dcopclient
%{tde_bindir}/dcopfind
%{tde_bindir}/dcopobject
%{tde_bindir}/dcopquit
%{tde_bindir}/dcopref
%{tde_bindir}/dcopserver
%{tde_bindir}/dcopserver_shutdown
%{tde_bindir}/dcopstart
%{tde_bindir}/filesharelist
%{tde_bindir}/fileshareset
%{tde_bindir}/imagetops
%{tde_bindir}/kab2kabc
%{tde_bindir}/kaddprinterwizard
%{tde_bindir}/kbuildsycoca
%{tde_bindir}/kcmshell
%{tde_bindir}/kconf_update
%{tde_bindir}/kcookiejar
%{tde_bindir}/kde-config
%{tde_bindir}/kde-menu
%{tde_bindir}/kded
%{tde_bindir}/kdeinit
%{tde_bindir}/kdeinit_shutdown
%{tde_bindir}/kdeinit_wrapper
%{tde_bindir}/kdesu_stub
%{tde_bindir}/kdetcompmgr
%{tde_bindir}/kdontchangethehostname
%{tde_bindir}/kdostartupconfig
%{tde_bindir}/kfile
%{tde_bindir}/kfmexec
%{tde_bindir}/khotnewstuff
%{tde_bindir}/kinstalltheme
%{tde_bindir}/kio_http_cache_cleaner
%{tde_bindir}/kio_uiserver
%{tde_bindir}/kioexec
%{tde_bindir}/kioslave
%{tde_bindir}/klauncher
%{tde_bindir}/kmailservice
%{tde_bindir}/kmimelist
%attr(4755,root,root) %{tde_bindir}/kpac_dhcp_helper
%{tde_bindir}/ksendbugmail
%{tde_bindir}/kshell
%{tde_bindir}/kstartupconfig
%{tde_bindir}/ktelnetservice
%{tde_bindir}/ktradertest
%{tde_bindir}/kwrapper
%{tde_bindir}/lnusertemp
%{tde_bindir}/make_driver_db_cups
%{tde_bindir}/make_driver_db_lpr
%{tde_bindir}/meinproc
%{tde_bindir}/networkstatustestservice
%{tde_bindir}/start_kdeinit
%{tde_bindir}/start_kdeinit_wrapper
%attr(4755,root,root) %{tde_bindir}/kgrantpty
%{tde_bindir}/checkXML
%{tde_bindir}/ksvgtopng
%{tde_bindir}/kunittestmodrunner
%{tde_bindir}/preparetips
%{tde_tdelibdir}/*
%{tde_libdir}/lib*.so.*
%{tde_libdir}/libkdeinit_*.la
%{tde_libdir}/libkdeinit_*.so
%{tde_datadir}/applications/kde/*.desktop
%{tde_datadir}/autostart/kab2kabc.desktop
%{tde_datadir}/applnk/kio_iso.desktop
%{tde_datadir}/apps/*
%exclude %{tde_datadir}/apps/ksgmltools2/
%config(noreplace) %{tde_datadir}/config/*
%{tde_datadir}/emoticons/*
%{tde_datadir}/icons/crystalsvg/
%{tde_datadir}/icons/default.kde
%{tde_datadir}/icons/hicolor/index.theme
%{tde_datadir}/locale/all_languages
%{tde_datadir}/mimelnk/magic
%{tde_datadir}/mimelnk/*/*.desktop
%{tde_datadir}/services/*
%{tde_datadir}/servicetypes/*
%{tde_tdedocdir}/HTML/en/common/*
%{tde_tdedocdir}/HTML/en/kspell/

%{_sysconfdir}/xdg/menus/tde-applications.menu

%pre
# TDE Bug #1074
if [ -d "%{tde_datadir}/locale/all_languages" ]; then
  rm -rf "%{tde_datadir}/locale/all_languages"
fi

%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

##########

%package devel
Summary:	%{name} - Development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

Obsoletes:	tdelibs-devel < %{version}-%{release}
Provides:	tdelibs-devel = %{version}-%{release}
Obsoletes:	trinity-kdelibs-devel < %{version}-%{release}
Provides:	trinity-kdelibs-devel = %{version}-%{release}

%description devel
This package includes the header files you will need to compile
applications for TDE.

%files devel
%defattr(-,root,root,-)
%{tde_bindir}/dcopidl*
%{tde_bindir}/kconfig_compiler
%{tde_bindir}/makekdewidgets
%{tde_datadir}/apps/ksgmltools2/
%{tde_tdeincludedir}/*
%{tde_libdir}/*.la
%{tde_libdir}/*.so
%{tde_libdir}/*.a
%exclude %{tde_libdir}/libkdeinit_*.la
%exclude %{tde_libdir}/libkdeinit_*.so
%{tde_datadir}/cmake/kdelibs.cmake

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}
%patch1 -p1 -b .xdg
%patch2 -p1 -b .kde4
%patch101 -p1 -b .xdg_path
%patch102 -p1 -b .cups_by_default


%build
unset QTDIR; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${QTDIR}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{tde_includedir}:%{tde_includedir}/tqt"

# We need LD_LIBRARY_PATH here because ld.so.conf file has not been written yet
export LD_LIBRARY_PATH="%{tde_libdir}"

export KDEDIR="%{tde_prefix}"

if [ -d "/usr/X11R6" ]; then
  export CXXFLAGS="${RPM_OPT_FLAGS} -L/usr/X11R6/%{_lib} -I/usr/X11R6/include"
fi


%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%__mkdir_p build
cd build
%endif

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DBIN_INSTALL_DIR="%{tde_bindir}" \
  -DDOC_INSTALL_DIR="%{tde_docdir}" \
  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  \
  -DWITH_ALL_OPTIONS=ON \
  -DWITH_ARTS=ON \
  -DWITH_ALSA=ON \
  -DWITH_LIBART=ON \
  -DWITH_LIBIDN=ON \
  -DWITH_SSL=ON \
  -DWITH_CUPS=ON \
  -DWITH_LUA=OFF \
  -DWITH_TIFF=ON \
  %{?with_jasper:-DWITH_JASPER=ON} \
  %{?with_openexr:-DWITH_OPENEXR=ON} \
  -DWITH_UTEMPTER=ON \
  %{?with_avahi:-DWITH_AVAHI=ON} \
  %{?!with_pcre:-DWITH_PCRE=OFF} \
  %{?!with_inotify:-DWITH_INOTIFY=OFF} \
  %{?!with_gamin:-DWITH_GAMIN=OFF} \
  -DWITH_SUDO_KDESU_BACKEND=OFF \
  %{?!with_lzma:-DWITH_LZMA=OFF} \
  -DWITH_ASPELL=ON \
  %{?!with_hspell:-DWITH_HSPELL=OFF} \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf "%{?buildroot}"
%__make install DESTDIR="%{?buildroot}" -C build

# Use system-wide CA certificate
%if "%{?cacert}" != ""
%__rm -f "%{?buildroot}%{tde_datadir}/apps/kssl/ca-bundle.crt"
%__ln_s "%{cacert}" "%{?buildroot}%{tde_datadir}/apps/kssl/ca-bundle.crt"
%endif


%clean
%__rm -rf "%{?buildroot}"


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-3
- Build for Fedora 19

* Sun Jul 28 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-2
- Rebuild with NDEBUG option
- Fix XDG menu

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2
