%define _requires_exceptions perl\(.*\)\\|devel\(linux-gate\)\\|devel\(libdns_sd\(.*\)\\|devel\(libdns_sd\)

%define _disable_ld_no_undefined 1

%define use_hspell_plugins 1

%define compile_apidox 0
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define use_kickoff_menu 1
%{?_no_kickoff_menu: %{expand: %%global use_kickoff_menu 0}}

%define lib_major 4
%define lib_name_orig libkde3core
%define lib_name %mklibname kde3core %{lib_major}
%define libqt %mklibname qt 3

%define lib_name_orig_kdepim %mklibname kdepim
%define lib_major_kdepim 2
%define lib_name_kdepim %lib_name_orig_kdepim%lib_major_kdepim

%define lib_name_orig_kdebase libkdebase
%define lib_major 4
%define lib_name_kdebase %mklibname kdebase %lib_major

%define epoch_kdelibs 30000000
%define epoch_arts 30000001

%define oname kdelibs

Name: kdelibs3
Summary: K Desktop Environment - Libraries
Version: 3.5.12
Release: %mkrel 4
Epoch: %epoch_kdelibs
Group: Graphical desktop/KDE
License: LGPL_V2
BuildRoot: %_tmppath/%name-%version-%release-root
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
Source1: kdelibs-3.5.9-mandriva-mimetypes.tar.bz2
Source2: verisign-class-3-secure-server-ca.pem
Source3: kde3lib.filter
Source4: kde3lib.script
Patch2:	kdelibs-3.3.2-fix-kurlbar-global.patch
Patch3:	kdelibs-3.5.3-fix-enable-dialogbox.patch
Patch4: kdelibs-3.5.7-cups-1.3-conf.patch
Patch10: kdelibs-3.5.2-move-xdg-menu-dir.patch
Patch11: kdelibs-3.5.7-add-extra-catalogs.patch
Patch15: kdelibs-3.5.9-kio-kfile-grouplist.patch
Patch22: kdelibs-3.5.10-ktip-on-kde4.patch
Patch26: kdelibs-3.5.10-LDFLAG_fix-1.patch
Patch29: ac264.patch
Patch30: kdelibs-dcopobject-destruct-crash.patch
# Kickoff related patches 
Patch204: kdelibs-3.5.8-add-bookmark-dialog.patch
Obsoletes: kdelibs-static-devel
Obsoletes: kdelibs3.0
Obsoletes: kde3-kdelibs
Requires: kde-l10n
Conflicts: kdepim-korganizer <= 3.2.3-100mdk
BuildRequires: kde3-macros
BuildRequires: aspell-devel
BuildRequires: lua-devel
BuildRequires: avahi-compat-libdns_sd-devel 
BuildRequires: avahi-qt3-devel 
BuildRequires: avahi-client-devel
BuildRequires: qt3-devel >= 3.3.6
BuildRequires: libxslt-devel
BuildRequires: libxml2 >= 2.4.11
BuildRequires: openssl-devel
BuildRequires: cups-devel >= 1.2
BuildRequires: pcre-devel
BuildRequires: fam-devel
BuildRequires: libarts-devel
BuildRequires: bzip2-devel
BuildRequires: libart_lgpl-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libsasl-devel
BuildRequires: libtiff-devel
BuildRequires: libvorbis-devel
BuildRequires: pam-devel
BuildRequires: X11-devel
BuildRequires: libalsa-devel
BuildRequires: libmad-devel
BuildRequires: gdbm-devel
BuildRequires: jasper-devel
BuildRequires: OpenEXR-devel
BuildRequires: libacl-devel
BuildRequires: krb5-devel
BuildRequires: autoconf >= 1:2.59
BuildRequires: automake > 1.5
BuildRequires: libldap-devel
BuildRequires: idn-devel
BuildRequires: lzma-devel
%if %use_hspell_plugins
BuildRequires:	hspell-devel
%endif
BuildRequires:  liblzmadec-devel

%description 
Libraries for the K Desktop Environment.

%files
%defattr(-,root,root,-)

#--------------------------------------------------------------

%package -n %lib_name
Group:      Development/KDE and Qt
Summary:    Core libraries for KDE
Obsoletes: kdetrayproxy 
Obsoletes: kdelibs-arts
Obsoletes: libkdecore4 < 4.0.0
Provides: kdelibs = %{epoch_kdelibs}:%version-%release
Provides: %lib_name_orig = %{epoch_kdelibs}:%version-%release
Requires: kdelibs3-common = %{epoch_kdelibs}:%version-%release
Requires: %{libqt} >= 3.2.2
Requires: nss_mdns
Conflicts: %lib_name < 3.1.91, libkdebase4 < 3.1.91
Conflicts: kmplayer <= 0.8.4
Conflicts: krusader <= 1.29-1mdk
Conflicts: %lib_name_kdebase <= 1:3.3.2
Conflicts: %lib_name_kdepim-korganizer <= 1:3.3.0-30mdk
Obsoletes: kde3-kdepim-common < 3.5.12
Requires: libtqtinterface >= 3.5.12-1

%description -n %lib_name
Libraries for the K Desktop Environment.

%files -n %{lib_name}
%defattr(-,root,root,-)
%_sysconfdir/ld.so.conf.d/*
%_kde3_libdir/libkdeinit_*
%_kde3_libdir/libkdefakes_nonpic.a
%_kde3_libdir/libDCOP.la
%_kde3_libdir/libkdecore.la
%_kde3_libdir/libkdefakes.la
%_kde3_libdir/libkdefx.la
%_kde3_libdir/libkdeprint.la
%_kde3_libdir/libkdeprint_management.la
%_kde3_libdir/libkdesu.la
%_kde3_libdir/libkdeui.la
%_kde3_libdir/libkhtml.la
%_kde3_libdir/libkio.la
%_kde3_libdir/libkjs.la
%_kde3_libdir/libkmid.la
%_kde3_libdir/libkparts.la
%_kde3_libdir/libkscreensaver.la
%_kde3_libdir/libkspell.la
%_kde3_libdir/libktexteditor.la
%_kde3_libdir/libkdesasl.la
%_kde3_libdir/libkscript.la
%_kde3_libdir/libkatepartinterfaces.la
%_kde3_libdir/libkabc.la
%_kde3_libdir/libartskde.la
%_kde3_libdir/libkmediaplayer.la
%_kde3_libdir/libkutils.la
%_kde3_libdir/libkjava.la
%_kde3_libdir/libkabc_dir.la
%_kde3_libdir/libkabc_file.la
%_kde3_libdir/libkabc_ldapkio.la
%_kde3_libdir/libkmdi.la
%_kde3_libdir/libkresources.la
%_kde3_libdir/libkwalletbackend.la
%_kde3_libdir/libkwalletclient.la
%_kde3_libdir/libvcard.la
%_kde3_libdir/libartskde.so.*
%_kde3_libdir/libDCOP.so.*
%_kde3_libdir/libkdecore.so.*
%_kde3_libdir/libkdefakes.so.*
%_kde3_libdir/libkdefx.so.*
%_kde3_libdir/libkdeprint.so.*
%_kde3_libdir/libkdeprint_management.so.*
%_kde3_libdir/libkdesu.so.*
%_kde3_libdir/libkdeui.so.*
%_kde3_libdir/libkhtml.so.*
%_kde3_libdir/libkio.so.*
%_kde3_libdir/libkjs.so.*
%_kde3_libdir/libkmid.so.*
%_kde3_libdir/libkparts.so.*
%_kde3_libdir/libkscreensaver.so.*
%_kde3_libdir/libkspell.so.*
%_kde3_libdir/libktexteditor.so.*
%_kde3_libdir/libkdesasl.so.*
%_kde3_libdir/libkscript.so.*
%_kde3_libdir/libkatepartinterfaces.so.*
%_kde3_libdir/libkabc.so.*
%_kde3_libdir/libkmediaplayer.so.*
%_kde3_libdir/libkutils.so.*
%_kde3_libdir/libkjava.so.*
%_kde3_libdir/libkabc_dir.so.*
%_kde3_libdir/libkabc_file.so.*
%_kde3_libdir/libkabc_ldapkio.so.*
%_kde3_libdir/libkmdi.so.*
%_kde3_libdir/libkresources.so.*
%_kde3_libdir/libkwalletbackend.so.*
%_kde3_libdir/libkwalletclient.so.*
%_kde3_libdir/libvcard.so.*
%_kde3_libdir/libkimproxy.la
%_kde3_libdir/libkimproxy.so.*
%_kde3_libdir/libknewstuff.la
%_kde3_libdir/libknewstuff.so.*
%_kde3_libdir/libkspell2.la
%_kde3_libdir/libkspell2.so.*
%_kde3_libdir/libkdnssd.la
%_kde3_libdir/libkdnssd.so.*
%_kde3_libdir/libkmdi2.la
%_kde3_libdir/libkmdi2.so.*
%_kde3_libdir/libkntlm.la
%_kde3_libdir/libkntlm.so.*
%_kde3_libdir/libkunittest.la
%_kde3_libdir/libkunittest.so.*
%_kde3_libdir/libconnectionmanager.la
%_kde3_libdir/libconnectionmanager.so.*
%_kde3_libdir/libkabc_net.la
%_kde3_libdir/libkabc_net.so.*
%_kde3_libdir/libkdefakes_pic.a
%_kde3_libdir/libkrandr.la
%_kde3_libdir/libkrandr.so.*
%_kde3_libdir/libnetworkstatus.la
%_kde3_libdir/libnetworkstatus.so.*
%dir %_kde3_libdir/kde3
%_kde3_libdir/kde3/*.la
%_kde3_libdir/kde3/*.so
%dir %_kde3_libdir/kde3/plugins/
%dir %_kde3_libdir/kde3/plugins/designer/
%_kde3_libdir/kde3/plugins/designer/*.so
%_kde3_libdir/kde3/plugins/designer/*.la
%dir %_kde3_libdir/kde3/plugins/styles/
%_kde3_libdir/kde3/plugins/styles/*.la
%_kde3_libdir/kde3/plugins/styles/*.so
%{_var}/lib/rpm/filetriggers/kde3lib.*


#--------------------------------------------------------------

%package -n %lib_name-devel
Group:		Development/KDE and Qt
Summary:	Header files and documentation for compiling KDE applications
Obsoletes:  kdelibs-devel
Obsoletes: libkdecore4-devel < 4.0.0
Provides:	kdelibs-devel = %{epoch_kdelibs}:%version-%release
Provides:   kdelibs3-devel = %{epoch_kdelibs}:%version-%release
Conflicts:	kdebase-devel <= 3.1.91mdk 
Requires:	%lib_name = %{epoch_kdelibs}:%version-%release
Requires:	acl-devel
Requires:	qt3-devel >= 3.3.6
Requires:   kde3-macros
Requires:   libtqtinterface-devel >= 3.5.12-1
Conflicts:  kmplayer <= 0.8.4
Conflicts:  kdelibs-devel < 3.1.91
Conflicts:  krusader <= 1.29-1mdk
Conflicts:  %lib_name_kdepim-korganizer-devel <= 1:3.3.0-30mdk

%description -n %lib_name-devel
This package includes the header files you will need to compile applications 
for KDE. Also included is the KDE API documentation in HTML format for easy 
browsing.

%files -n %lib_name-devel
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/kspell
%_kde3_includedir/*
%_kde3_libdir/libartskde.so
%_kde3_libdir/libDCOP.so
%_kde3_libdir/libkabc_dir.so
%_kde3_libdir/libkabc_file.so
%_kde3_libdir/libkabc_ldapkio.so
%_kde3_libdir/libkabc.so
%_kde3_libdir/libkdecore.so
%_kde3_libdir/libkdefakes.so
%_kde3_libdir/libkdefx.so
%_kde3_libdir/libkdeprint.so
%_kde3_libdir/libkdeprint_management.so
%_kde3_libdir/libkdesu.so
%_kde3_libdir/libkdeui.so
%_kde3_libdir/libkhtml.so
%_kde3_libdir/libkio.so
%_kde3_libdir/libkjs.so
%_kde3_libdir/libkmid.so
%_kde3_libdir/libkparts.so
%_kde3_libdir/libkscreensaver.so
%_kde3_libdir/libkspell.so
%_kde3_libdir/libktexteditor.so
%_kde3_libdir/libkdesasl.so
%_kde3_libdir/libkscript.so
%_kde3_libdir/libkatepartinterfaces.so
%_kde3_libdir/libkmediaplayer.so
%_kde3_libdir/libkutils.so
%_kde3_libdir/libkjava.so
%_kde3_libdir/libkresources.so
%_kde3_libdir/libkwalletclient.so
%_kde3_libdir/libkwalletbackend.so
%_kde3_libdir/libkmdi.so
%_kde3_libdir/libvcard.so
%_kde3_libdir/libkimproxy.so
%_kde3_libdir/libknewstuff.so
%_kde3_libdir/libkspell2.so
%_kde3_libdir/libkdnssd.so
%_kde3_libdir/libkmdi2.so
%_kde3_libdir/libkntlm.so
%_kde3_libdir/libkunittest.so
%_kde3_libdir/libconnectionmanager.so
%_kde3_libdir/libkabc_net.so
%_kde3_libdir/libkrandr.so
%_kde3_libdir/libnetworkstatus.so

#--------------------------------------------------------------

%package    common
Group:      Development/KDE and Qt
Summary:    Config file and icons file for %name
Requires(pre):   %lib_name = %{epoch_kdelibs}:%version-%release
Requires: kde-config-file
Conflicts:   kdelibs-common < 0.8.4-0.rc5.1mdk
Conflicts:	kmplayer <= 0.8.4
Conflicts:	krusader <= 1.29-1mdk
Conflicts:      koffice <= 1.3-0.beta3.6mdk
Conflicts:	kdesdk <= 3.1-9mdk
Conflicts:  kdebase-progs <= 3.1.3-79mdk
Conflicts:	%lib_name_kdepim-korganizer <= 1:3.3.0-30mdk
Conflicts:	kjsembed <= 3.3.0
Conflicts:	kmplayer <= 0.8.4
Conflicts:	kdeadmin <= 2:3.3.2-6mdk 
Conflicts:	kdevelop <= 3:3.2.2-3mdk
Conflicts:	mandrake-mime <= 0.4
Requires(post): 	kde-custom-icons
Requires:	desktop-common-data
Obsoletes:	mandrake-menu-directory
Obsoletes:      kde3-kdelibs-common
Obsoletes: kde3-kdepim-common < 3.5.12
Requires:   hicolor-icon-theme
Requires:  libxml2-utils
Conflicts: kdepim =< 2.2.2-5
Conflicts: kdeartwork =< 2.2.2-3mdk
Conflicts: koffice =< 1.1.1-14mdk
Conflicts: kdelibs-sound =< 2.2.2-48mdk
Conflicts: kdebase =< 2.2.2-93mdk
Conflicts: kdelibs < 3.1.91
Conflicts: kdebase < 3.1.91
Conflicts: k3b <= 0.9-15mdk
Conflicts: kdesdk <= 3.1.3-9mdk
Conflicts: koffice <= 1.3-0.beta3.6mdk
Conflicts: %lib_name < 3.2.3-19mdk
Conflicts: kdebase-progs <= 1:3.3.2
Conflicts: kttsd <= 0.3.0
Conflicts: kdeaddons <= 1:3.3.2
Provides:  %oname-common = %{epoch_kdelibs}:%version-%release
Requires: libtqtinterface >= 3.5.12-1

%description common
This packages contains all icons, config file etc...

%files common
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/common
%dir %_kde3_configdir/
%config(noreplace) %_kde3_configdir/kdebug.areas
%config(noreplace) %_kde3_configdir/kdebugrc
%config(noreplace) %_kde3_configdir/ksslcalist
%config(noreplace) %_kde3_configdir/language.codes
%config(noreplace) %_kde3_configdir/kthemestylerc
%config(noreplace) %_kde3_configdir/khotnewstuffrc
%config(noreplace) %_kde3_configdir/katefiletyperc
%config(noreplace) %_kde3_configdir/ui/ui_standards.rc
%config(noreplace) %_kde3_configdir/ui/kprintpreviewui.rc
%config(noreplace) %_kde3_configdir/kdeprintrc
%config(noreplace) %_kde3_configdir/katesyntaxhighlightingrc
%config(noreplace) %_kde3_configdir/kio_isorc
%dir %_kde3_configdir/colors/
%dir %_kde3_configdir/ui/
%_kde3_configdir/colors/*
%_kde3_configdir/ipv6blacklist
%doc %_kde3_appsdir/LICENSES
%dir %_kde3_appsdir/kdewidgets
%_kde3_appsdir/kdewidgets/*
%dir %_kde3_appsdir/knewstuff
%_kde3_appsdir/knewstuff/*
%dir %_kde3_appsdir/ktexteditor_docwordcompletion/
%_kde3_appsdir/ktexteditor_docwordcompletion/*
%attr(0755,root,root) %_sysconfdir/profile.d/*
%_kde3_bindir/lnusertemp
%_kde3_bindir/start_kdeinit
%_kde3_bindir/ktradertest
%_kde3_bindir/kfmexec
%_kde3_bindir/kioexec
%_kde3_bindir/artsmessage
%_kde3_bindir/checkXML
%_kde3_bindir/cupsdconf
%_kde3_bindir/cupsdoprint
%_kde3_bindir/dcop
%_kde3_bindir/dcopidl
%_kde3_bindir/dcopidl2cpp
%_kde3_bindir/dcopserver
%_kde3_bindir/imagetops
%_kde3_bindir/kbuildsycoca
%_kde3_bindir/kconf_update
%_kde3_bindir/kcookiejar
%_kde3_bindir/kde-config
%_kde3_bindir/kded
%_kde3_bindir/kdeinit
%_kde3_bindir/kdeinit_shutdown
%_kde3_bindir/kdeinit_wrapper
%_kde3_bindir/kdesu_stub
%_kde3_bindir/kio_http_cache_cleaner
%_kde3_bindir/kio_uiserver
%_kde3_bindir/klauncher
%_kde3_bindir/kmailservice
%attr(4755, root, root) %_kde3_bindir/kpac_dhcp_helper
%_kde3_bindir/ksendbugmail
%_kde3_bindir/kshell
%_kde3_bindir/kwrapper
%_kde3_bindir/make_driver_db_cups
%_kde3_bindir/meinproc
%_kde3_bindir/preparetips
%_kde3_bindir/kdontchangethehostname
%_kde3_bindir/kfile
%_kde3_bindir/kconfig_compiler
%_kde3_bindir/kde-menu
%_kde3_bindir/kcmshell
%_kde3_bindir/dcopclient
%_kde3_bindir/dcopfind
%_kde3_bindir/dcopobject
%_kde3_bindir/dcopref
%_kde3_bindir/dcopserver_shutdown
%_kde3_bindir/dcopstart
%_kde3_bindir/kab2kabc
%_kde3_bindir/kaddprinterwizard
%_kde3_bindir/ktelnetservice
%_kde3_bindir/make_driver_db_lpr
%_kde3_bindir/kinstalltheme
%_kde3_bindir/kioslave
%_kde3_bindir/ksvgtopng
%_kde3_bindir/dcopidlng
%_kde3_bindir/dcopquit
%attr(4755,root, root) %_kde3_bindir/kgrantpty
%_kde3_bindir/kdostartupconfig
%_kde3_bindir/kstartupconfig
%_kde3_bindir/kunittestmodrunner
%_kde3_bindir/khotnewstuff
%_kde3_bindir/makekdewidgets
%_kde3_bindir/start_kdeinit_wrapper
%_kde3_bindir/kmimelist
%_kde3_bindir/networkstatustestservice
%dir %_kde3_datadir/applications/kde/
%_kde3_datadir/applications/kde/kresources.desktop
%dir %_kde3_appsdir/kabc/
%_kde3_appsdir/kabc/*
%dir %_kde3_appsdir/kconf_update/
%_kde3_appsdir/kconf_update/*
%dir %_kde3_appsdir/dcopidlng
%_kde3_appsdir/dcopidlng/*
%dir %_kde3_appsdir/kdeprint
%_kde3_appsdir/kdeprint/*
%dir %_kde3_appsdir/kdeui
%_kde3_appsdir/kdeui/*
%dir %_kde3_appsdir/khtml
%_kde3_appsdir/khtml/*
%dir %_kde3_appsdir/kio_uiserver
%_kde3_appsdir/kio_uiserver/*
%dir %_kde3_appsdir/proxyscout
%_kde3_appsdir/proxyscout/*
%dir %_kde3_appsdir/kjava/
%_kde3_appsdir/kjava/*
%dir %_kde3_appsdir/knotify
%_kde3_appsdir/knotify/*
%dir %_kde3_appsdir/ksgmltools2
%_kde3_appsdir/ksgmltools2/*
%dir %_kde3_appsdir/kssl
%_kde3_appsdir/kssl/*
%dir %_kde3_appsdir/kstyle
%_kde3_appsdir/kstyle/*
%dir %_kde3_appsdir/kcertpart
%_kde3_appsdir/kcertpart/*
%dir %_kde3_appsdir/katepart
%_kde3_appsdir/katepart/*
%dir %_kde3_appsdir/kcm_componentchooser
%_kde3_appsdir/kcm_componentchooser/*
%dir %_kde3_appsdir/ktexteditor_insertfile
%_kde3_appsdir/ktexteditor_insertfile/*
%dir %_kde3_appsdir/ktexteditor_isearch/
%_kde3_appsdir/ktexteditor_isearch/*
%dir %_kde3_appsdir/ktexteditor_kdatatool/
%_kde3_appsdir/ktexteditor_kdatatool/*
%dir %_kde3_autostart/
%_kde3_autostart/*.desktop
%_kde3_iconsdir/*
%dir %_kde3_datadir/mimelnk
%_kde3_datadir/mimelnk/*
%dir %_kde3_datadir/emoticons
%_kde3_datadir/emoticons/*
%_kde3_datadir/locale/*
%dir %_kde3_datadir/services/
%_kde3_datadir/services/*
%dir %_kde3_datadir/servicetypes/
%_kde3_datadir/servicetypes/*
%_sysconfdir/xdg/kde/menus/*
%dir %_kde3_datadir/apps/konqueror/servicemenus/
%_kde3_datadir/apps/konqueror/servicemenus/*
%dir %_kde3_datadir/applnk/
%_kde3_datadir/applnk/*
# Not ship this files
%exclude %_kde3_bindir/filesharelist
%exclude %_kde3_bindir/fileshareset

#--------------------------------------------------------------
%if %compile_apidox
%package devel-doc
Group: Development/KDE and Qt
Summary: Development documentation for %name
Requires: qt3-doc
BuildRequires:	doxygen
BuildRequires:  graphviz
BuildRequires:	qt3-doc

%description devel-doc
This packages contains all development documentation for kdelibs

%files devel-doc
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/kdelibs-apidocs
%endif


%prep
%setup -q  -n %oname-%version
%patch2 -p1 -b .add_kfile_item_in_global
%patch3 -p1 -b .fix_disable_button
%patch10 -p1 -b .move_xdg_menu_dir
%patch11 -p0 -b .catalogs
%patch15 -p1 -b .kio_kfile
%patch22 -p1 -b .ktiponkde4
%patch26 -p1 -b .ldflags
%patch29 -p1 -b .ac
%patch30 -p1 -b .dcopcrash
%patch204 -p0 -b .post358

# Cert
cp %SOURCE2 kio/kssl/kssl
echo "verisign-class-3-secure-server-ca.pem" >> kio/kssl/kssl/localcerts

%build
# This step is needed mostly because avahi patch
# Until better solution is find, do not remove the build
# regenerate step
make -f admin/Makefile.common cvs

QTDIR=%qt3dir ; export QTDIR;
PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export xdg_menudir=%_sysconfdir/xdg/kde/menus
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/

%configure_kde3 \
	--disable-arts-gsl \
	--enable-cups \
	--with-qt-libraries=%qt3lib \
%if %use_hspell_plugins	
	--with-hspell \
%else
	--without-hspell \
%endif
%if "%{_lib}" != "lib"
	--enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
%endif
	--with-extra-includes=/usr/include/avahi-compat-libdns_sd/:/opt/kde3/include/tqt \
	
make -C dnssd mocs

%make

%if %compile_apidox
make apidox
%endif


%install
rm -fr %buildroot

make DESTDIR=%buildroot install

# Lets push an stable mimlnk source tree, instead of dealing with patches
pushd  %buildroot/%_kde3_datadir/
    rm -rf mimelnk
    tar xfj %SOURCE1
popd

%if %compile_apidox
make install-apidox DESTDIR=%buildroot/
%endif

install -d %buildroot/%_sysconfdir/profile.d
cat > %buildroot/%_sysconfdir/profile.d/91kde3.sh <<EOF

if [ -z "\$PATH" ]; then
    PATH=%{_bindir}:/bin:%{_kde3_bindir}
else
    if [ -z \$(echo \$PATH | grep %{_kde3_bindir}) ]; then
    	PATH=\$PATH:%{_bindir}:%{_kde3_bindir}
		export PATH
	fi
fi

if [ -z "\$XDG_DATA_DIRS" ]; then
    XDG_DATA_DIRS=%{_datadir}:%{_kde3_datadir}
	export XDG_DATA_DIRS
else
    if [ -z \$(echo \$XDG_DATA_DIRS | grep %{_kde3_datadir}) ]; then
		XDG_DATA_DIRS=\$XDG_DATA_DIRS:%{_datadir}:%{_kde3_datadir}
		export XDG_DATA_DIRS
	fi
fi


EOF

install -d %buildroot/%_sysconfdir/ld.so.conf.d
cat > %buildroot/%_sysconfdir/ld.so.conf.d/%lib_name.conf <<EOF
%_kde3_libdir
EOF

mkdir %buildroot/var
mkdir %buildroot/var/lib
mkdir %buildroot/var/lib/rpm
mkdir %buildroot/var/lib/rpm/filetriggers
install -m 0644 %SOURCE3 %buildroot/var/lib/rpm/filetriggers
install -m 0755 %SOURCE4 %buildroot/var/lib/rpm/filetriggers

%clean
rm -fr %buildroot



%changelog
* Mon Jul 26 2011 Tim Williams <tim@my-place.org.uk> 30000000:3.5.12-4mvf2010.2
+ Fix kde3-kdepim-common conflict

* Mon Jul 26 2011 Tim Williams <tim@my-place.org.uk> 30000000:3.5.12-3mvf2010.2
+ Restore package name to libkde3core4 for main library
+ Add obsoletes libkdecore4 to libkde3core and libkde3core-devel package to solve upgrade conflit

* Mon Jul 18 2011 Tim Williams <tim@my-place.org.uk> 30000000:3.5.12-2mdv2010.2
+ Add new filetrigger filters

* Thu Feb 3 2011  Tim Williams <tim@my-place.org.uk> 30000000:3.5.12-1mdv2010.2
+ Added trinity KDE 3.5.12 sources
+ Added the following trinity patches
  kdelibs-r1184225.diff
+ Fix the following patches which wouldn't apply due to code changes:
  kdelibs-3.5.3-fix-enable-dialogbox.patch
  kdelibs-3.5.7-add-extra-catalogs.patch
  kdelibs-3.5.9-kio-kfile-grouplist.patch
  kdelibs-3.5.10-ktip-on-kde4.patch
- Removed the following patches which no longer seem to be necessary. In most cases the core code now contains the
  necessary functionality:
  kdelibs-3.5.7-speedbar-xdg-user-dirs.patch 
  kdelibs-3.5.7-xdg-dirs-document-path.patch
  kdelibs-3.5.4-dcop_wrong_reply.patch
  kdelibs-3.5.8-smooth-scrolling.patch
  kdelibs-3.5.0-rubberband-selection.patch
  kdelibs-3.5.6-add-dnssd-avahi-support.patch
  kdelibs-3.5.4-fix-translate-menu.patch
  kdelibs-3.5.4-fix-translate-desktopfile.patch
  kdelibs-3.5.5-ldap-kconfig.patch
  kdelibs-3.5.10-kfile-beagle.patch
  kdelibs-3.5.8-lzma_support.patch
  kdelibs-3.5.8-cups_by_default.patch
  kdelibs-3.5.10-glibc-inotify.patch
  kdelibs-3.5.10-gcc44.patch
  kdelibs-3.5.10-ossl-1.x.patch
  kdelibs-3.5.10-gcc_4.4-2.patch
  kde-am.patch
  kickoff-drop-shadow.diff
  clever-menu.diff
  kdelibs-3.5.4-fix-https-loop.patch
+ Add unpackaged files to the files lists of the relevant packages
  

* Wed May 19 2010 Tim Williams <tim@my-place.org.uk> 30000000:3.5.10-13mdv2010.1
+ Added kdelibs-3.5.10-gcc_4.4-2.patch, kdelibs-3.5.10-LDFLAG_fix-1.patch, kdelibs-3.5.10-ossl-1.x.patch
  kde-am.patch, ac264.patch, kdelibs-dcopobject-destruct-crash.patch
+ Rebuild for MDV 2010.1

* Fri Nov 13 2009 Tim Williams <tim@my-place.org.uk> 30000000:3.5.10-12mdv2010.0
+ Rebuild for MDV 2010.0
+ Add kdelibs-3.5.10-gcc44.patch

* Mon Mar 30 2009 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.10-11mdv2009.1
+ Revision: 362451
- Rebuild to get rid of old libxcb references

* Wed Mar 18 2009 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.10-10mdv2009.1
+ Revision: 357134
- Some Provides/Obsoletes Fixes

* Tue Mar 17 2009 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.10-9mdv2009.1
+ Revision: 356571
- Add provide on kdelibs-common

* Mon Mar 16 2009 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.10-8mdv2009.1
+ Revision: 355784
- Fix Requires

* Sun Mar 15 2009 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.10-7mdv2009.1
+ Revision: 355410
- Do not build apidox for now
- Fix BuildRequires
- fix for new package  name
- Change kdelibs to kdelibs3 ( kde3 reintroduction step 2 )

* Sat Nov 08 2008 Adam Williamson <awilliamson@mandriva.org> 30000000:3.5.10-5mdv2009.1
+ Revision: 300983
- rebuild for xcb changes

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add icon for powerpoint files

* Sun Sep 28 2008 Anssi Hannula <anssi@mandriva.org> 30000000:3.5.10-4mdv2009.0
+ Revision: 289032
- prefer the glibc header for inotify (fixes build with current
  kernel-headers, r858854+859451 from KDE SVN)
- rename /etc/ld.so.conf.d/kde3.conf to %%lib_name.conf to avoid conflicts
  on biarch systems

* Mon Sep 01 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.10-3mdv2009.0
+ Revision: 278570
- Ktip is not enabled on kde 3 and kde 4

* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.10-2mdv2009.0
+ Revision: 277335
- ktip should not appears on kde4. This is an exception on kde3 autostart services

* Tue Aug 26 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.10-1mdv2009.0
+ Revision: 276217
- Update for probably the last upstream kdelibs from kde3

* Thu Aug 07 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-25mdv2009.0
+ Revision: 266500
- Fix expanding test issue

* Thu Aug 07 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-24mdv2009.0
+ Revision: 266223
- Fix profile

* Thu Jul 03 2008 Olivier Blin <oblin@mandriva.com> 30000000:3.5.9-23mdv2009.0
+ Revision: 230927
- rebuild (the build system ate the previous package)

* Wed Jul 02 2008 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.9-22mdv2009.0
+ Revision: 230631
- Fix  test on $PATH
- Revert: misunderstanding
- More fix on PATH :/

* Wed Jul 02 2008 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.9-21mdv2009.0
+ Revision: 230598
- Fix $PATH

* Sun Jun 29 2008 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.9-20mdv2009.0
+ Revision: 230057
- Add missing dir on 91kde3.sh

  + Helio Chissini de Castro <helio@mandriva.com>
    - Added new profile to solve issues of XDG

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 30 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-19mdv2009.0
+ Revision: 213552
- Configure was wrong during the transition...

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Revert XDG_DATA_DIRS workaround this breaks other DM (gnome fox ex

* Tue May 27 2008 Funda Wang <fundawang@mandriva.org> 30000000:3.5.9-17mdv2009.0
+ Revision: 211521
- rebuild for new qt3

* Mon May 26 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-16mdv2009.0
+ Revision: 211426
- Added recent branch patchs ( Description inlcuded in patches )
- Added collin suggestion for XDG_DATA_DIR even not becoming final solution. will solve pontual issues users
  are having with kde3 + modules

* Fri May 09 2008 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.9-15mdv2009.0
+ Revision: 205309
- Fix macros for cache image

* Sun May 04 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-14mdv2009.0
+ Revision: 201205
- Invalid requires for libarts giving us headaches

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add kde3-macros as Requires for kdelibs-devel

* Sun May 04 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-12mdv2009.0
+ Revision: 200807
- Branch patches are provided with full changelog now
- kde 3 now seats under /opt

* Thu Mar 20 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-10mdv2008.1
+ Revision: 189192
- khtml fixes from kde branch

* Mon Mar 17 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-9mdv2008.1
+ Revision: 188277
- Patch from branch to fix skipped lat icon on set

* Fri Mar 14 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-8mdv2008.1
+ Revision: 187983
- Dcopserver shutdown fix from kde branch

* Thu Mar 13 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-7mdv2008.1
+ Revision: 187696
- Closing bug https://qa.mandriva.com/show_bug.cgi?id=29797
- Added latest branch post 3.5.9 bugfixes. ( kdeinit with --new-startup )

* Thu Mar 06 2008 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.9-6mdv2008.1
+ Revision: 180266
- Add mandriva-kde-translation catalogs support (thanks Helio)
- [BUGFIX] Fix mimetype for svg (Bug #35301)

  + Helio Chissini de Castro <helio@mandriva.com>
    - kfilegroup info patch to redice pooling time under the network using proper glibc calls. Thanks to Andreas Hasenack

* Wed Feb 20 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-4mdv2008.1
+ Revision: 173307
- Proper fix of kate line position issue. We need wake up some packagers :-/

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] Fix encoding of x-bzeps.desktop in french (Bug #32764)

* Thu Feb 14 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-2mdv2008.1
+ Revision: 168139
- Revert the Makefile.am changes to allow header proper install
- Revert the Makefile.am changes to allow header proper install

* Thu Feb 14 2008 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.9-1mdv2008.1
+ Revision: 167794
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches intregrated
- Fixed dnnsd patch and added a workaround on spec to not brask nrproc compilations

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - fix breakage with tar.bz2 archives (modifies P18, fixes #37194)

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [FEATURE] Add back bookmark dialog (Bug #31933)

* Wed Jan 16 2008 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.8-9mdv2008.1
+ Revision: 153911
- [BUGFIX] Fix embedding started from outside by reparenting inside to QXEmbed. (Bug #36478)

* Wed Jan 09 2008 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.8-8mdv2008.1
+ Revision: 146989
- [BUGFIX] Fix tests on %%post (Bug #32974)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - regenerate lzma patch (P18)

* Sat Dec 22 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.8-7mdv2008.1
+ Revision: 136741
- Updated to branch, with officil qxembed/flash fixes
- Fixed ldap patch
- Disabled lzma for now since it's not applying with current base

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 17 2007 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 30000000:3.5.8-6mdv2008.1
+ Revision: 122429
- Add a patch to detect cups every time.
  If user force the choice, autodetect will be stoped.

  + Helio Chissini de Castro <helio@mandriva.com>
    - Fixed qxembed and flash novell patches to compile
    - Added current qxembed patch from suse
    - Fix smooth scrooling patch, based on suse current patch
    - Remove old qxembed patch. not valid for current status and superseded by flash test patch
    - Added Lubos kdelibs part test patch for flash plugin issues

* Thu Dec 06 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 30000000:3.5.8-3mdv2008.1
+ Revision: 115892
- Requires nss_mdns so that zeroconf works. (#21010)

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Fix Build as we have now qt4 as default

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - fix lzma filter bug, fixes reading of >8KB man pages (fixes #34294)

* Mon Nov 05 2007 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.8-2mdv2008.1
+ Revision: 106219
- [BUGFIX] Fix encoding of control panel and main menu (Bug #27478)

* Wed Oct 24 2007 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.8-1mdv2008.1
+ Revision: 101837
- Fix File list
- Remove patch 247 ( merged upstream )
- Kde 3.5.8
- Remove upstream merged patches
- [BUGFIX] Fix avahi support (Bug #26154)

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-ended-with-dot

* Mon Oct 01 2007 Frederic Crozat <fcrozat@mandriva.com> 30000000:3.5.7-43mdv2008.0
+ Revision: 94112
- Add conflicts on mandrake-mime for update from 2007.0

* Fri Sep 28 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 30000000:3.5.7-42mdv2008.0
+ Revision: 93438
- Fix xdg-user-dir usage in KDE on non-utf8 locales (#33973)
- Removed obsolete document path patch

* Fri Sep 21 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-41mdv2008.0
+ Revision: 92016
- Fixed pdf2ps on the fly conversion in kdeprint. Thanks to Ademar Reis to dig, catch and provide
  the fix

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] Add mimetype for *.m2t files (Bug #27589)

* Fri Sep 14 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-40mdv2008.0
+ Revision: 85681
- Latest updated on libltdl and khtml rendering

* Thu Sep 13 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 30000000:3.5.7-39mdv2008.0
+ Revision: 85316
- Add lzma support (#32877)

* Wed Sep 12 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-38mdv2008.0
+ Revision: 84624
- Updated cve-4224-4225-3820
- kurl patches
- xhtml fixes
- Add pdf2ps converdion as a kprinter filter. Thanks to Ademar found the bug

* Mon Sep 10 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-36mdv2008.0
+ Revision: 84149
- Fixed latest cookie jar patches. Neoclust modified the flaw patch for kopete crash. Need be
  remember that the change was done directly on old patch, instead of follow correct mandriva
  procedure of add proper new patch branch revision. In the future, people that touch in kdelibs
  should avoid enter same patch again.

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Make patches back as the one making kopete crash is fixed now

* Thu Sep 06 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-35mdv2008.0
+ Revision: 81097
- Application requesting mime from mdkonline without require the packge itselfr leas developers to make errors on fixing mimetypes

* Wed Sep 05 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-34mdv2008.0
+ Revision: 80379
- Latest mimetypes
- Disable http patches that breaks kopete msn http login

* Mon Sep 03 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-32mdv2008.0
+ Revision: 78603
- Added lates patches from branch

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Another mimetype fix for 32764
    - [BUGFIX] -Fix french comment of image/x-bzeps.desktop (#32764)

* Sat Sep 01 2007 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.7-31mdv2008.0
+ Revision: 77709
- Fix some mimetypes
  		- Remove x-mdv-exec
  		- add 2 pdf mimetypes

* Thu Aug 30 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-30mdv2008.0
+ Revision: 76328
- Boiko's patch to fix svn rendering and including embed images
- More patches from upstream branch

* Wed Aug 29 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-29mdv2008.0
+ Revision: 74689
- Last mimetypes, m3u recursion fix
- Cups 1.3 now fully functional
- Mimetype tree is provided in a separate tarball instead of multiple patches.
  The intention is to make easy to fix all missing ones, as reported by kbuildsyscoca.
  Almost all video, audio and image mimetypes are solved now, some application/ still to be solved,
  mostly due to gnome apps requires.
- This patch is uselles, as problem happens before reach proper test
- Start to fix the remaining mime issues

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - add upstream patch from BRANCH (patch 252)
    - Add 2 upstream patches from 3.5.x BRANCH

* Fri Aug 24 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-27mdv2008.0
+ Revision: 70874
- Added remaining patches on branch tree
- Fixed build with cups 1.3, updated with no advise :-/
- Added last remaining patches for xdg user dirs
- Added XDG USER DIRS spec.
- Removed old invalid patchs
- Removed support for legacy icons
- Added XDG USER DIRS catalog as standard
- Remove the recursive mimetype. Previous workaround to real fix. This not prevents happens in the
  future in a new mime addition, but solves current 100%% cpu usage in mime calls. Need run
  kbuildsyscoca again for be effective in already running installs

* Wed Aug 15 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-23mdv2008.0
+ Revision: 63782
- On the fly per-app language change....

* Wed Aug 15 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-22mdv2008.0
+ Revision: 63689
- Sec. fix CVE-2007-4224, CVE-2007-3820, CVE-2007-4225

* Tue Aug 14 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-21mdv2008.0
+ Revision: 63408
- Added another patch from upstream branch
- Fixed file conflicts. New urpmi/rpm is doing a great job to fix our ancient problems

* Mon Aug 13 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-20mdv2008.0
+ Revision: 62659
- Rename patch for proper name
- Submit package, which for some reason aren't submitted before. Should solve Mdv bug
  http://qa.mandriva.com/show_bug.cgi?id=32488

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add patch 227 : Better consolekit support
    - add some missing Excel mimetypes

  + Funda Wang <fundawang@mandriva.org>
    - meinproc requires xmllint

* Fri Jul 27 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-19mdv2008.0
+ Revision: 56129
- Removing invalid patch for share dialog disable. Was in same pack as kickoff old patches and was applied by mistake
- Changing to one license only

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - add missing mimetype

* Wed Jul 25 2007 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.7-17mdv2008.0
+ Revision: 55210
- Remove non-existant mimetypes from Makefile

* Tue Jul 24 2007 David Walluck <walluck@mandriva.org> 30000000:3.5.7-16mdv2008.0
+ Revision: 55073
- fix release
- move binaries in libkdecore to common in order to allow parallel lib installs

* Thu Jul 19 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-15mdv2008.0
+ Revision: 53378
- Fix kde bug #130104

* Mon Jul 16 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-14mdv2008.0
+ Revision: 52656
- Update latest bugfixes from upstream branch

* Mon Jul 16 2007 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.7-13mdv2008.0
+ Revision: 52529
- Do not add x-fli file

* Mon Jul 16 2007 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.7-12mdv2008.0
+ Revision: 52399
- Add  Mimetypes for video/
- Add Mimetypes for image/
- Add Mimetypes for text/
- Fix install of x-zip-compressed

  + Anssi Hannula <anssi@mandriva.org>
    - drop requires on aspell from kdelibs-common (users should be free to remove
      aspell if they do not use it for spell-checking)

* Mon Jul 09 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 30000000:3.5.7-11mdv2008.0
+ Revision: 50637
- Remove the build requirement for the mandriva menu category script
- Remove mandriva specific categories script
- Fix the fix-document-path patch which was not using readlink in the right way

* Thu Jun 14 2007 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.7-10mdv2008.0
+ Revision: 39756
- Add mimetype for flv files (bug #31285)

* Wed Jun 13 2007 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.7-9mdv2008.0
+ Revision: 38993
- Own %%_libdir/kde3 directory

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 30000000:3.5.7-8mdv2008.0
+ Revision: 36178
- rebuild with correct optflags

  + Helio Chissini de Castro <helio@mandriva.com>
    - Added latest relevant patches from branch

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add patch202 from kde bugzilla ( bug #52151 )

* Fri Jun 01 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-5mdv2008.0
+ Revision: 34251
- Added post 3.5.7 gmail backport

* Fri Jun 01 2007 Nicolas Lécureuil <neoclust@mandriva.org> 30000000:3.5.7-4mdv2008.0
+ Revision: 34037
- Remove mandriva-create-kde-mdk-menu Requires
- First patch to add new mimetypes ( excel related )

  + Anssi Hannula <anssi@mandriva.org>
    - Add missing buildrequires for idn-devel

* Thu May 17 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-3mdv2008.0
+ Revision: 27591
- Minor update in official tarball from kde.org

* Wed May 16 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-2mdv2008.0
+ Revision: 27434
- 3.5.7 release
- Added extrea catalog for kickoff translations

* Thu May 10 2007 Helio Chissini de Castro <helio@mandriva.com> 30000000:3.5.7-0.6mdv2008.0
+ Revision: 26175
- Updated for branch revision 663293
- Fixed apidocs install

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Change Requires to use new script and do not generated %%_menudir file anymore
    - Add back mandriva categories on .desktop file

