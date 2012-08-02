# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific variables
%define tde_bindir %{_prefix}/bin
%define tde_datadir %{_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{_prefix}/include
%define tde_libdir %{_prefix}/%{_lib}

%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:		trinity-tdelibs
Version:	3.5.13
Release:	11%{?dist}%{?_variant}
License:	GPL
Summary:	TDE Libraries
Group:		Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kdelibs-%{version}.tar.gz

Obsoletes:	tdelibs < %{version}-%{release}
Provides:	tdelibs = %{version}-%{release}
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
## [tdelibs] Export kdemain symbol in iso kioslave [Bug #465] [Commit #0536f0b7]
Patch29:	kdelibs-3.5.13-fix_iso_kioslave.patch
## [tdelibs] Fix iso kioslave not parsing large images properly [Commit #b4bba7b5]
Patch30:	kdelibs-3.5.13-fix_iso_kioslave_not_parsing_large_image_properly.patch
## [tdelibs] Add ability to set KLed off color [Commit #513ffc6e]
Patch31:	kdelibs-3.5.13-add_ability_to_set_kled_off_color.patch
## [tdelibs] Fix spinbox text entry when base is not 10 [Commit #d1c71f69]
Patch32:	kdelibs-3.5.13-fix_spinbox_text_entry_when_base_not_10.patch
## [tdelibs] Update iso kioslave to better handle large images [Commit #dca4c677]
Patch33:	kdelibs-3.5.13-update_iso_kioslave_better_handle_large_image.patch
## [tdelibs] Restore tdesu dialog "Keep password" check box default to disabled/unchecked. [Commit #87363770]
Patch34:	kdelibs-3.5.13-restore_tdesu_keeppassword_default_disabled.patch

BuildRequires:	cmake >= 2.8
BuildRequires:	libtool
BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	krb5-devel libxslt-devel cups-devel libart_lgpl-devel pcre-devel
BuildRequires:	libutempter-devel
BuildRequires:	bzip2-devel
BuildRequires:	openssl-devel
BuildRequires:	gcc-c++
BuildRequires:	alsa-lib-devel
BuildRequires:	libidn-devel
BuildRequires:	qt3-devel
BuildRequires:	jasper-devel
BuildRequires:	libtiff-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	glib2-devel
BuildRequires:	gamin-devel
BuildRequires:	aspell-devel
BuildRequires:	hspell-devel
BuildRequires:	avahi-tqt-devel >= 3.5.13
# LUA support are not ready yet
#BuildRequires:	lua-devel

%if 0%{?mgaversion}
BuildRequires:	%{_lib}avahi-client-devel
BuildRequires:	%{_lib}ltdl-devel
BuildRequires:	x11-proto-devel
BuildRequires:	%{_lib}xcomposite1-devel
Requires:		%{_lib}avahi-client3
%else
BuildRequires:	avahi-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:	xorg-x11-proto-devel
BuildRequires:	libXcomposite-devel
%endif

Requires:		tqtinterface >= 3.5.13
Requires:		trinity-arts >= 3.5.13
Requires:		avahi
Requires:		qt3 >= 3.3.8.d

%description
Libraries for the Trinity Desktop Environment:
TDE Libraries included: tdecore (TDE core library), kdeui (user interface),
kfm (file manager), khtmlw (HTML widget), kio (Input/Output, networking),
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
%{tde_tdelibdir}/*
%{tde_libdir}/lib*.so.*
%{tde_libdir}/lib[kt]deinit_*.la
%{tde_libdir}/lib[kt]deinit_*.so
%{tde_datadir}/applications/kde/*.desktop
%{tde_datadir}/autostart/kab2kabc.desktop
%{tde_datadir}/applnk/kio_iso.desktop
%{tde_datadir}/apps/*
%exclude %{tde_datadir}/apps/ksgmltools2/
%config(noreplace) %{tde_datadir}/config/*
%{tde_datadir}/emoticons/*
%{tde_datadir}/icons/default.kde
%{tde_datadir}/mimelnk/magic
%{tde_datadir}/mimelnk/*/*.desktop
%{tde_datadir}/services/*
%{tde_datadir}/servicetypes/*
%{tde_datadir}/icons/crystalsvg/
%{tde_tdedocdir}/HTML/en/kspell/
# remove conflicts with kdelibs-4
%if "%{?_prefix}" != "/usr"
%{tde_bindir}/checkXML
%{tde_bindir}/ksvgtopng
%{tde_bindir}/kunittestmodrunner
%{tde_bindir}/preparetips
%{tde_datadir}/icons/hicolor/index.theme
%{tde_datadir}/locale/all_languages
%{tde_tdedocdir}/HTML/en/common/*
%{_sysconfdir}/ld.so.conf.d/trinity.conf
%else
%exclude %{tde_bindir}/checkXML
%exclude %{tde_bindir}/ksvgtopng
%exclude %{tde_bindir}/kunittestmodrunner
%exclude %{tde_bindir}/preparetips
%exclude %{tde_datadir}/config/colors
%exclude %{tde_datadir}/config/kdebug.areas
%exclude %{tde_datadir}/config/kdebugrc
%exclude %{tde_datadir}/config/ksslcalist
%exclude %{tde_datadir}/config/ui/ui_standards.rc
%exclude %{tde_datadir}/icons/hicolor/index.theme
%exclude %{tde_datadir}/locale/all_languages
%exclude %{tde_tdedocdir}/HTML/en/common/*
%endif

# Avoid conflict with 'redhat-menus' package
%if "%{_prefix}" == "/usr"
%{_sysconfdir}/xdg/menus/kde-applications.menu
%else
%{_prefix}/etc/xdg/menus/kde-applications.menu
%endif

# New in TDE 3.5.13
%{tde_bindir}/kdetcompmgr

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
%{tde_includedir}/*
%{tde_libdir}/*.la
%{tde_libdir}/*.so
%{tde_libdir}/*.a
%exclude %{tde_libdir}/libkdeinit_*.la
%exclude %{tde_libdir}/libkdeinit_*.so

# New in TDE 3.5.13
%{tde_datadir}/cmake/kdelibs.cmake

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

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
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${QTDIR}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{tde_includedir}:%{tde_includedir}/tqt"

# We need LD_LIBRARY_PATH here because ld.so.conf file has not been written yet
export LD_LIBRARY_PATH="%{tde_libdir}"


%{?!mgaversion:%__mkdir build; cd build}
%cmake \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DDOC_INSTALL_DIR=%{tde_docdir} \
  -DINCLUDE_INSTALL_DIR=%{tde_includedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DPKGCONFIG_INSTALL_DIR=%{tde_libdir}/pkgconfig \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DCMAKE_SKIP_RPATH="OFF" \
  -DWITH_ARTS=ON \
  -DWITH_ALSA=ON \
  -DWITH_LIBART=ON \
  -DWITH_LIBIDN=ON \
  -DWITH_SSL=ON \
  -DWITH_CUPS=ON \
  -DWITH_LUA=OFF \
  -DWITH_TIFF=ON \
  -DWITH_JASPER=ON \
  -DWITH_OPENEXR=ON \
  -DWITH_UTEMPTER=ON \
  -DWITH_AVAHI=ON \
  -DWITH_ASPELL=ON \
  -DWITH_HSPELL=ON \
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
%{tde_libdir}
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
* Sun Jul 22 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-11
- Fix iso kioslave not parsing large images properly [Commit #b4bba7b5]
- Add ability to set KLed off color [Commit #513ffc6e]
- Fix spinbox text entry when base is not 10 [Commit #d1c71f69]
- Update iso kioslave to better handle large images [Commit #dca4c677]
- Restore tdesu dialog "Keep password" check box default to disabled/unchecked. [Commit #87363770]

* Tue Jun 26 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-10
- Renames to 'trinity-tdelibs'
- Enable 'aspell', 'hspell' and 'libidn'
- Export kdemain symbol in iso kioslave [Bug #465] [Commit #0536f0b7]

* Tue Jun 19 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-9
- Renames to 'tdelibs'
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
