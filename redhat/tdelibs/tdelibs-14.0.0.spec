# Remove qt-devel and qt3-devel and any kde*-devel that may interfere !!!

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_version 14.0.0

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
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:		GPL
Summary:		TDE Libraries
Group:			Environment/Libraries

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz

# Patches from Mandriva
Patch101:		tdelibs-14.0.0-xdg_dirs_set_path.patch
Patch102:		tdelibs-14.0.0-cups_by_default.patch

Obsoletes:		tdelibs < %{version}-%{release}
Provides:		tdelibs = %{version}-%{release}
Obsoletes:		trinity-kdelibs < %{version}-%{release}
Provides:		trinity-kdelibs = %{version}-%{release}
Obsoletes:		trinity-kdelibs-apidocs < %{version}-%{release}
Provides:		trinity-kdelibs-apidocs = %{version}-%{release}


BuildRequires:	cmake >= 2.8
BuildRequires:	libtool
BuildRequires:	trinity-tqt3-devel >= 3.5.0
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-dbus-1-tqt-devel >= 1:0.9
BuildRequires:	trinity-dbus-tqt-devel >= 1:0.63
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
BuildRequires:	trinity-libart-lgpl-devel

# ELFICON support
#  It's an Ubuntu gadget, not useful for us.
%if 0
%define with_elficon 1
BuildRequires:	libr-devel
%endif

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

# UDEV support
%if 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version} || 0%{?rhel} >= 6
%define with_tdehwlib 1
BuildRequires:	libudev-devel
%endif

# HAL support
%if 0%{?rhel} == 5
%define with_hal 1
%endif

# UDISKS support
%if 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version} || 0%{?rhel} >= 6
%define with_udisks 1
BuildRequires:	udisks-devel
Requires:		udisks
%endif

# PMOUNT support
#Requires:		pmount

# UDISKS2 support
%if 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
%define with_udisks2 1
BuildRequires:	udisks2-devel
Requires:		udisks2
%endif

# DEVICEKIT POWER support
%if 0%{?rhel} >= 6
%define with_devkitpower 1
Requires:		DeviceKit-power
%endif

# UPOWER support
%if 0%{?fedora} || 0%{?suse_version} || 0%{?mdkversion} || 0%{?mgaversion}
%define with_upower 1
Requires:		upower
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

# NETWORKMANAGER support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?suse_version}
%define with_nm 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}nm-util-devel
%endif
%if 0%{?rhel} >= 6 || 0%{?fedora}
BuildRequires:	NetworkManager-glib-devel
%endif
%if 0%{?suse_version}
BuildRequires:	NetworkManager-devel
%endif
%endif

# Certificates support
%if 0%{?rhel} || 0%{?fedora}
%define	cacert %{_sysconfdir}/ssl/certs/ca-certificates.crt
Requires:		ca-certificates
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
%define	cacert %{_sysconfdir}/ssl/certs/ca-bundle.crt
Requires:		openssl
%endif

# Trinity dependencies
Requires:		trinity-tqt3 >= 3.5.0
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
%{tde_bindir}/tdeab2tdeabc
%{tde_bindir}/kaddprinterwizard
%{tde_bindir}/tdebuildsycoca
%{tde_bindir}/tdecmshell
%{tde_bindir}/tdeconf_update
%{tde_bindir}/kcookiejar
%{tde_bindir}/tde-config
%{tde_bindir}/tde-menu
%{tde_bindir}/kded
%{tde_bindir}/tdeinit
%{tde_bindir}/tdeinit_shutdown
%{tde_bindir}/tdeinit_wrapper
%{tde_bindir}/tdesu_stub
%{tde_bindir}/kdetcompmgr
%{tde_bindir}/kdontchangethehostname
%{tde_bindir}/tdedostartupconfig
%{tde_bindir}/tdefile
%{tde_bindir}/kfmexec
%{tde_bindir}/tdehotnewstuff
%{tde_bindir}/kinstalltheme
%{tde_bindir}/tdeio_http_cache_cleaner
%{tde_bindir}/tdeio_uiserver
%{tde_bindir}/tdeioexec
%{tde_bindir}/tdeioslave
%{tde_bindir}/tdeiso_info
%{tde_bindir}/tdelauncher
%if 0%{?with_elficon}
%{tde_bindir}/tdelfeditor
%endif
%{tde_bindir}/tdemailservice
%{tde_bindir}/tdemimelist
%attr(4755,root,root) %{tde_bindir}/kpac_dhcp_helper
%{tde_bindir}/tdesendbugmail
%{tde_bindir}/kshell
%{tde_bindir}/tdestartupconfig
%{tde_bindir}/tdetelnetservice
%{tde_bindir}/tdetradertest
%{tde_bindir}/kwrapper
%{tde_bindir}/lnusertemp
%{tde_bindir}/make_driver_db_cups
%{tde_bindir}/make_driver_db_lpr
%{tde_bindir}/meinproc
%{tde_bindir}/networkstatustestservice
%{tde_bindir}/start_tdeinit
%{tde_bindir}/start_tdeinit_wrapper
%attr(4755,root,root) %{tde_bindir}/kgrantpty
%{tde_bindir}/tde_dbus_hardwarecontrol
%{tde_bindir}/checkXML
%{tde_bindir}/ksvgtopng
%{tde_bindir}/tdeunittestmodrunner
%{tde_bindir}/preparetips
%{tde_tdelibdir}/*
%{tde_libdir}/lib*.so.*
%{tde_libdir}/libtdeinit_*.la
%{tde_libdir}/libtdeinit_*.so
%{tde_datadir}/applications/tde/*.desktop
%{tde_datadir}/autostart/tdeab2tdeabc.desktop
%{tde_datadir}/applnk/tdeio_iso.desktop
%{tde_datadir}/apps/*
%exclude %{tde_datadir}/apps/ksgmltools2/
%config(noreplace) %{tde_datadir}/config/*
%{tde_datadir}/emoticons/*
%{tde_datadir}/icons/crystalsvg/
%{tde_datadir}/icons/default.tde
%{tde_datadir}/icons/hicolor/index.theme
%{tde_datadir}/locale/all_languages
%{tde_datadir}/mimelnk/magic
%{tde_datadir}/mimelnk/*/*.desktop
%{tde_datadir}/services/*
%{tde_datadir}/servicetypes/*
%{tde_tdedocdir}/HTML/en/common/*
%{tde_tdedocdir}/HTML/en/tdespell/

%{_sysconfdir}/xdg/menus/tde-applications.menu
%{_sysconfdir}/xdg/menus/tde-applications.menu-no-kde
%{_sysconfdir}/dbus-1/system.d/org.trinitydesktop.hardwarecontrol.conf
%{_datadir}/dbus-1/system-services/org.trinitydesktop.hardwarecontrol.service

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
%{tde_bindir}/*config_compiler
%{tde_bindir}/maketdewidgets
%{tde_datadir}/apps/ksgmltools2/
%{tde_tdeincludedir}/*
%{tde_libdir}/*.la
%{tde_libdir}/*.so
%{tde_libdir}/*.a
%exclude %{tde_libdir}/libtdeinit_*.la
%exclude %{tde_libdir}/libtdeinit_*.so
%{tde_datadir}/cmake/tdelibs.cmake
%{tde_libdir}/pkgconfig/tdelibs.pc

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

%patch101 -p1 -b .xdg_path
%patch102 -p1 -b .cups_by_default


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

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
  -DWITH_GCC_VISIBILITY=ON \
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
  %{?!with_jasper:-DWITH_JASPER=OFF} \
  %{?!with_openexr:-DWITH_OPENEXR=OFF} \
  -DWITH_UTEMPTER=ON \
  %{?!with_elficon:-DWITH_ELFICON=OFF} \
  %{?!with_avahi:-DWITH_AVAHI=OFF} \
  %{?!with_pcre:-DWITH_PCRE=OFF} \
  %{?!with_inotify:-DWITH_INOTIFY=OFF} \
  %{?!with_gamin:-DWITH_GAMIN=OFF} \
  -DWITH_TDEHWLIB_DAEMONS=ON \
  %{?with_hal:-DWITH_HAL=ON} \
  %{?with_devkitpower:-DWITH_DEVKITPOWER=ON} \
  %{?!with_upower:-DWITH_UPOWER=OFF} \
  %{?!with_udisks:-DWITH_UDISKS=OFF} \
  %{?!with_udisks2:-DWITH_UDISKS2=OFF} \
  -DWITH_CONSOLEKIT=ON \
  %{?with_nm:-DWITH_NETWORK_MANAGER_BACKEND=ON} \
  -DWITH_SUDO_TDESU_BACKEND=OFF \
  -DWITH_OLD_XDG_STD=OFF \
  %{?!with_lzma:-DWITH_LZMA=OFF} \
  -DWITH_LIBBFD=OFF \
  -DWITH_KDE4_MENU_SUFFIX=OFF \
  -DWITH_ASPELL=ON \
  %{?!with_hspell:-DWITH_HSPELL=OFF} \
  -DWITH_TDEICONLOADER_DEBUG=OFF \
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
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 14.0.0-1
- Initial release for TDE 14.0.0
