# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific variables
%define tde_docdir %{_docdir}/kde
%define tde_libdir %{_libdir}/trinity

# Older RHEL/Fedora versions use packages named "qt", "qt-devel", ..
# whereas newer versions use "qt3", "qt3-devel" ...
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 8
%define _qt_suffix 3
%endif


Name:		tdelibs
Version:	3.5.13
Release:	9%{?dist}%{?_variant}
License:	GPL
Summary:	TDE Libraries
Group:		System Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kdelibs-%{version}.tar.gz

Obsoletes:	trinity-kdelibs < %{version}-%{release}
Provides:	trinity-kdelibs = %{version}-%{release}
Obsoletes:	trinity-kdelibs-apidocs < %{version}-%{release}
Provides:	trinity-kdelibs-apidocs = %{version}-%{release}

## [kdelibs/kio] Disable 'max line length' detection [Bug #656]
Patch10:	kdelibs-3.5.13-maxlinelength.patch
## [kdelibs/kjs] Enable pcre support in kdelibs [Bug #569]
Patch11:	kdelibs-3.5.13-enable_pcre.patch
## [kdelibs/kate] Updated syntax highlighting files [Bug #764]
Patch12:	kdelibs-3.5.13-kate_syntax.patch.gz
## [kdelibs] Adds Inotify support (backport commit 24f144fa)
Patch13:	kdelibs-3.5.13-add_inotify_support.patch
## [kdelibs] Add fam/gamin support to tdelibs CMake (backport commit 2b035349)
Patch14:	kdelibs-3.5.13-enable_fam_gamin.patch
## [kdelibs/kioslave/http] Fix UTF8 Encoding for WebDAV directories [Bug #766] [Commit #e131f10b]
Patch15:	kdelibs-3.5.13-fix_UTF8_encoding_for_WebDAV_directories.patch
## [kdelibs/kdeprint] Fix add printer [Bug #383]
Patch16:	kdelibs-3.5.13-fix_add_printer.patch
## [kdelibs/kio/kdirwatch] Fix "Konqueror: Does not update file pane with file changes" [Bug #756]
Patch17:	kdelibs-3.5.13-fix_kdirwatch.patch
## [kdelibs/dcop] Fix 'dcoptypes.h' for compilation with GCC 4.7
Patch18:	kdelibs-3.5.13-fix_dcoptypes_h.patch
## [tdelibs] Fix konq filter in list view mode. [Commit #06b51484]
Patch19:	kdelibs-3.5.13-fix_konq_filter.patch
## [tdelibs] Fix tdesu internal pathing [Bug #766] [Commit #e131f10b]
Patch20:	kdelibs-3.5.13-fix_tdesu_internal_pathing.patch
## [tdelibs] Fix slider drawing on external paint devices [Commit #a1c30c14]
Patch21:	kdelibs-3.5.13-fix_slide_drawing.patch
## [tdelibs] Reduce "More Applications" and extra koffice items from TDE menu. [Commit #1c06ae32]
Patch22:	kdelibs-3.5.13-reduce_more_applications.patch
## [tdelibs] Fix creation of profile directory in system root [Bug #293] [Commit #049525ee]
Patch23:	kdelibs-3.5.13-fix_creation_of_profile_directory.patch
## [tdelibs] Initialize X11 threading when kinit is used to launch a program [Bug #812] [Commit #6c806af1]
Patch24:	kdelibs-3.5.13-fix_x11_threading_when_kinit_is_used.patch
## [tdelibs] Fix composition extension detection [Commit #41ea89f7]
Patch25:	kdelibs-3.5.13-fix_composition_extension_detection.patch
## [tdelibs] Fix KTempFile not obeying special bits on file creation [Bug #349] [Commit #9068fffd]
Patch26:	kdelibs-3.5.13-fix_ktempfile_special_bits.patch
## [tdelibs] Add dynamic label support to kpassworddialog [Commit #3c752316]
Patch27:	kdelibs-3.5.13-add_dynamic_label_to_kpassword.patch
## [tdelibs] Fix FTBFS - incomplete build kspell2 [Bug #657] [Commit #3e284fad]
Patch28:	kdelibs-3.5.13-fix_build_kspell2.patch


BuildRequires:	cmake >= 2.8
BuildRequires:	libtool
BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	avahi-devel
#BuildRequires:	lua-devel
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
BuildRequires:	gamin-devel
BuildRequires:	xorg-x11-proto-devel
BuildRequires:	libXcomposite-devel

Requires:		tqtinterface
Requires:		trinity-arts
Requires:		avahi
Requires:		qt%{?_qt_suffix}
Requires:		avahi-qt3

%description
Libraries for the Trinity Desktop Environment:
TDE Libraries included: tdecore (TDE core library), kdeui (user interface),
kfm (file manager), khtmlw (HTML widget), kio (Input/Output, networking),
kspell (spelling checker), jscript (javascript), kab (addressbook),
kimgio (image manipulation).

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING-DOCS COPYING.LIB README TODO
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
%{_libdir}/lib[kt]deinit_*.la
%{_libdir}/lib[kt]deinit_*.so
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
%{_sysconfdir}/ld.so.conf.d/trinity.conf
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

# Avoid conflict with 'redhat-menus' package
%if "%{_prefix}" == "/usr"
%{_sysconfdir}/xdg/menus/kde-applications.menu
%else
%{_prefix}/etc/xdg/menus/kde-applications.menu
%endif

# New in TDE 3.5.13
%{_bindir}/kdetcompmgr

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

##########

%package devel
Summary:	%{name} - Development files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

Obsoletes:	trinity-kdelibs-devel < %{version}-%{release}
Provides:	trinity-kdelibs-devel = %{version}-%{release}

%description devel
This package includes the header files you will need to compile
applications for TDE.

%files devel
%defattr(-,root,root,-)
%{_bindir}/dcopidl*
%{_bindir}/kconfig_compiler
%{_bindir}/makekdewidgets
%{_datadir}/apps/ksgmltools2/
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/*.a
%exclude %{_libdir}/libkdeinit_*.la
%exclude %{_libdir}/libkdeinit_*.so

# New in TDE 3.5.13
%{_datadir}/cmake/kdelibs.cmake

%post devel -p /sbin/ldconfig

%postun devel -p /sbin/ldconfig

##########

%if 0
%package apidocs
Group:		Development/Libraries
Summary:	%{name} - API documentation
Requires:	%{name} = %{version}-%{release}

Obsoletes:	trinity-kdelibs-devel < %{version}-%{release}
Provides:	trinity-kdelibs-devel = %{version}-%{release}

%description apidocs
This package includes the TDE API documentation in HTML
format for easy browsing

%files apidocs
%defattr(-,root,root,-)
#%{tde_docdir}/HTML/en/kdelibs*
%endif

##########

%prep
%setup -q -n kdelibs
%patch10 -p1
%patch11 -p0
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LD_LIBRARY_PATH="%{_libdir}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"

%__mkdir build
cd build
%cmake \
  -DWITH_ARTS=ON \
  -DWITH_ALSA=ON \
  -DWITH_LIBART=ON \
  -DWITH_LIBIDN=OFF \
  -DWITH_SSL=ON \
  -DWITH_CUPS=ON \
  -DWITH_LUA=OFF \
  -DWITH_TIFF=ON \
  -DWITH_JASPER=ON \
  -DWITH_OPENEXR=ON \
  -DWITH_UTEMPTER=ON \
  -DWITH_AVAHI=ON \
  -DWITH_ASPELL=OFF \
  -DWITH_HSPELL=OFF \
  -DWITH_PCRE=ON \
  -DWITH_INOTIFY=ON \
  -DWITH_GAMIN=ON \
  ..

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

%if "%{?_prefix}" != "/usr"
%__mkdir_p %{?buildroot}%{_sysconfdir}/ld.so.conf.d
cat <<EOF >%{?buildroot}%{_sysconfdir}/ld.so.conf.d/trinity.conf
%{_libdir}
EOF
%endif

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


%changelog
* Tue Jun 19 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-9
- Renames to 'tdelib'
- Fix 'ld.so.conf' file
- Fix konq filter in list view mode. [Commit #06b51484]
- Fix tdesu internal pathing [Bug #766] [Commit #e131f10b]
- Fix slider drawing on external paint devices [Commit #a1c30c14]
- Reduce "More Applications" and extra koffice items from TDE menu. [Commit #1c06ae32]
- Fix creation of profile directory in system root [Bug #293] [Commit #049525ee]
- Initialize X11 threading when kinit is used to launch a program [Bug #812] [Commit #6c806af1]
- Fix composition extension detection [Commit #41ea89f7]
- Fix KTempFile not obeying special bits on file creation [Bug #349] [Commit #9068fffd]
- Add dynamic label support to kpassworddialog [Commit #3c752316]
- Fix FTBFS - incomplete build kspell2 [Bug #657] [Commit #3e284fad]

* Tue Apr 24 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-8
- Fix "Konqueror: Does not update file pane with file changes" [Bug #756] 
- Fix compilation with GCC 4.7

* Sat Jan 21 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-7
- Fix UTF8 Encoding for WebDAV directories
- Fix hardcoded path in 'add printer' [Bug #383]

* Mon Jan 16 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-6
- Adds 'fam' and 'gamin' support

* Sat Jan 14 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-5
- Adds 'inotify' support

* Sat Dec 31 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Enable pcre support in kdelibs [Bug #569]
- Updated Kate syntax highlighting files [Bug #764]
- Disable 'max line length' detection [Bug #656]
- Add 'Provides: kdelibs3' to avoid installing distro-provided KDE3 libraries

* Sat Nov 12 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Moves XDG files in TDE prefix to avoid conflict with distro-provided KDE

* Thu Nov 03 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Add missing BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Wed Sep 02 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
