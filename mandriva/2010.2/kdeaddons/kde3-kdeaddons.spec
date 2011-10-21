%define oldname kdeaddons
%define lib_name_orig lib%oldname
%define lib_major 1
%define lib_name %mklibname %oldname %lib_major

Name: kde3-%{oldname}
Summary: Kdeaddons
Group: Graphical desktop/KDE3
Version: 3.5.12
Release: %mkrel 1
Epoch: 1
License: GPL
URL: http://www.kde.org
Source: http://download.kde.org/stable/3.5.10/src/%oldname-%version.tar.bz2
Patch0:	kdeaddons-3.2.3-call-drakclock.patch
Patch1: kde-3.5.10-acinclude.patch
#Patch2: fix_autotools.patch
#Patch3: 01_searchbar-google-suggest.patch
Patch4: kdebase-3.5.12-move-xdg-menu-dir.patch
Patch5: kdebase-3.5.12-config.patch
BuildRoot: %_tmppath/%name-%version-%release-root
Provides: kdeaddons3 = %epoch:%version-%release
Requires: %{name}-kfile-plugins = %epoch:%version-%release
Requires: %{name}-kicker-applets = %epoch:%version-%release
Requires: %{name}-konqimagegallery = %epoch:%version-%release
Requires: %{name}-renamedlg = %epoch:%version-%release
Requires: %{name}-konq-plugins = %epoch:%version-%release
Requires: %{name}-kaddressbook-plugins = %epoch:%version-%release
Requires: %{name}-knewsticker = %epoch:%version-%release
Requires: ksig = %epoch:%version-%release
Requires: %{name}-atlantik = %epoch:%version-%release
Requires: %{name}-searchbar = %epoch:%version-%release
Requires: %{name}-akregator = %epoch:%version-%release
Requires: %{name}-metabar = %epoch:%version-%release
Suggests: %{name}-kate = %epoch:%version-%release
Obsoletes: %lib_name
Obsoletes: %lib_name-devel 
Obsoletes: %{oldname}
Provides: %{oldname} = %epoch:%version-%release
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%endif
BuildRequires: autoconf >= 1:2.65
BuildRequires: automake > 1.5
BuildRequires: X11-devel
BuildRequires: freetype2-devel
BuildRequires: libkde3base4-devel 
BuildRequires: libkde3-kdegames1-devel
BuildRequires: libkdecore4-devel >= 3.2.12-1mvf
BuildRequires: libSDL-devel 
BuildRequires: alsa-lib-devel
BuildRequires: libaudiofile-devel 
BuildRequires: bzip2-devel
BuildRequires: esound-devel 
BuildRequires: jpeg-devel 
BuildRequires: lcms-devel 
BuildRequires: mng-devel
BuildRequires: png-devel 
BuildRequires: qt3-devel 
BuildRequires: kde3-kdepim-devel
BuildRequires: openssl-devel
BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: mesaglu-devel
BuildRequires: gpm-devel

%description
Plugins for some KDE applications: kdeaddons extends the functionality
of Konqueror, kate (text editor), kicker (some applets)
and knewsticker.

%files

#-----------------------------------------------------------------------------------

%package kfile-plugins
Summary: Kfile-plugins addons
Group: Graphical desktop/KDE3
Conflicts: kdeaddons < 1:3.5.7-4
Obsoletes: kdeaddons-noatun
Obsoletes: %{oldname}-kfile-plugins
Provides: %{oldname}-kfile-plugins = %epoch:%version

%description kfile-plugins
Kfile-plugins addons.

%files kfile-plugins
%defattr(-,root,root)
%_kde3_bindir/lnkforward
%_kde3_libdir/kde3/kfile_*
%_kde3_datadir/mimelnk/application/x-win-lnk.desktop
%_kde3_datadir/applnk/.hidden/lnkforward.desktop
%_kde3_datadir/services/kfile_*

#-----------------------------------------------------------------------------------

%package kicker-applets
Summary: Kicker-applets addons
Group: Graphical desktop/KDE3
Requires: kdebase3-progs 
Conflicts: kdeaddons < 1:3.5.7-4
Obsoletes: kdeaddons-noatun
Obsoletes: %{oldname}-kicker-applets

%description kicker-applets
Kicker-applets addons.

%files kicker-applets
%defattr(-,root,root)
%_kde3_appsdir/mediacontrol
%_kde3_iconsdir/*/*/*/ktimemon.png
%_kde3_appsdir/kicker
%_kde3_datadir/config.kcfg/kbinaryclock.kcfg
%_kde3_docdir/HTML/en/kicker-applets
%_kde3_libdir/kde3/*_panelapplet.*

#-----------------------------------------------------------------------------------

%package konqimagegallery
Summary: Konqimagegallery addon
Group: Graphical desktop/KDE3
Conflicts: kdeaddons < 1:3.5.7-4
Obsoletes: kdeaddons-noatun
Obsoletes: %{oldname}-konqimagegallery


%description konqimagegallery
Konqimagegallery addons.

%files konqimagegallery
%defattr(-,root,root)
%_kde3_iconsdir/*/*/*/imagegallery.png
%_kde3_libdir/kde3/libkimgallery.*
%_kde3_datadir/applnk/.hidden/kimgalleryplugin.desktop
%_kde3_appsdir/konqiconview/kpartplugins/kimgalleryplugin.rc

#-----------------------------------------------------------------------------------

%package renamedlg
Summary: Renamedlg addons
Group: Graphical desktop/KDE3
Conflicts: kdeaddons < 1:3.5.7-4
Obsoletes: kdeaddons-noatun
Obsoletes: %{oldname}-renamedlg
Provides: %{oldname}-renamedlg = %epoch:%version


%description renamedlg
Plugins for the KDE file rename dialog.

%files renamedlg
%defattr(-,root,root)
%_kde3_libdir/kde3/librenaudioplugin.*
%_kde3_libdir/kde3/librenimageplugin.*
%_kde3_datadir/services/renaudiodlg.desktop
%_kde3_datadir/services/renimagedlg.desktop

#-----------------------------------------------------------------------------------

%package konq-plugins
Summary: Konq-plugins addons
Group: Graphical desktop/KDE3
Requires: kdebase3-progs
Conflicts: kdeaddons < 1:3.5.7-4
Obsoletes: kdeaddons-noatun
Obsoletes: %{oldname}-konq-plugins
Provides: %{oldname}-konq-plugins = %epoch:%version


%description konq-plugins
Konq-plugins addons.

%files konq-plugins
%defattr(-,root,root)
%_kde3_bindir/kio_media_realfolder
%_kde3_bindir/fsview
%_kde3_bindir/jpegorient
%_kde3_libdir/kde3/libarkplugin.*
%_kde3_libdir/kde3/kcm_kuick.*
%_kde3_libdir/kde3/libkuickplugin.*
%_kde3_libdir/kde3/libcrashesplugin.*
%_kde3_libdir/kde3/webarchivethumbnail.*
%_kde3_libdir/kde3/konq_sidebarnews.*
%_kde3_libdir/kde3/libbabelfishplugin.*
%_kde3_libdir/kde3/libkhtmlsettingsplugin.*
%_kde3_libdir/kde3/libminitoolsplugin.*
%_kde3_libdir/kde3/libfsviewpart.*
%_kde3_libdir/kde3/libdomtreeviewerplugin.*
%_kde3_libdir/kde3/konqsidebar_delicious.*
%_kde3_libdir/kde3/librellinksplugin.*
%_kde3_libdir/kde3/libdirfilterplugin.*
%_kde3_libdir/kde3/libautorefresh.*
%_kde3_libdir/kde3/libwebarchiverplugin.*
%_kde3_libdir/kde3/libmfkonqmficon.*
%_kde3_libdir/kde3/libvalidatorsplugin.*
%_kde3_libdir/kde3/libuachangerplugin.*
%_kde3_libdir/kde3/libadblock.*
%_kde3_libdir/kde3/librsyncplugin.*
%_kde3_appsdir/khtml
%_kde3_appsdir/domtreeviewer
%_kde3_appsdir/microformat
%_kde3_appsdir/fsview
%_kde3_appsdir/konqsidebartng
%_kde3_appsdir/konqlistview
%_kde3_appsdir/konqiconview
%_kde3_appsdir/konqueror
%_kde3_appsdir/imagerotation
%_kde3_iconsdir/*/*/*/fsview.png
%_kde3_iconsdir/*/*/*/konqside*
%_kde3_iconsdir/*/*/*/autorefresh*
%_kde3_iconsdir/*/*/*/htmlvalidator.png
%_kde3_iconsdir/*/*/*/minitools.png
%_kde3_iconsdir/*/*/*/webarchiver.png
%_kde3_iconsdir/*/*/*/domtreeviewer.png
%_kde3_iconsdir/*/*/*/cssvalidator.png
%_kde3_iconsdir/*/*/*/babelfish.png
%_kde3_iconsdir/*/*/*/validators.png
%_kde3_datadir/applnk/.hidden/plugin_domtreeviewer.desktop
%_kde3_datadir/applnk/.hidden/fsview.desktop
%_kde3_datadir/applnk/.hidden/kcmkuick.desktop
%_kde3_datadir/applnk/.hidden/khtmlsettingsplugin.desktop
%_kde3_datadir/applnk/.hidden/plugin_babelfish.desktop
%_kde3_datadir/applnk/.hidden/plugin_validators.desktop
%_kde3_datadir/applnk/.hidden/kuickplugin.desktop
%_kde3_datadir/applnk/.hidden/dirfilterplugin.desktop
%_kde3_datadir/applnk/.hidden/uachangerplugin.desktop
%_kde3_datadir/applnk/.hidden/crashesplugin.desktop
%_kde3_datadir/applnk/.hidden/arkplugin.desktop
%_kde3_datadir/applnk/.hidden/plugin_webarchiver.desktop
%_kde3_datadir/applnk/.hidden/rsyncplugin.desktop
%_kde3_datadir/config/translaterc
%_kde3_datadir/config.kcfg/konq_sidebarnews.kcfg
%_kde3_datadir/services/webarchivethumbnail.desktop
%_kde3_datadir/services/ark_plugin.desktop
%_kde3_datadir/services/fsview_part.desktop
%_kde3_datadir/services/kuick_plugin.desktop
%_kde3_datadir/icons/crystalsvg/16x16/actions/remotesync.png
%_kde3_datadir/icons/crystalsvg/16x16/actions/remotesyncconfig.png
%_kde3_datadir/icons/crystalsvg/22x22/actions/remotesync.png
%_kde3_datadir/icons/crystalsvg/22x22/actions/remotesyncconfig.png
%_kde3_docdir/HTML/en/konq-plugins
%exclude %_kde3_appsdir/konqiconview/kpartplugins/kimgalleryplugin.rc
%exclude %_kde3_appsdir/konqueror/kpartplugins/searchbar*
%exclude %_kde3_appsdir/khtml/kpartplugins/akregator*
%exclude %_kde3_appsdir/konqsidebartng/entries/metabar.desktop
%exclude %_kde3_appsdir/konqsidebartng/add/metabar_add.desktop
%exclude %_kde3_appsdir/konqueror/icons/crystalsvg/16x16/actions/google*

#-----------------------------------------------------------------------------------

%package kaddressbook-plugins
Summary: Kaddressbook-plugins addons
Group: Graphical desktop/KDE3
Conflicts: kdeaddons < 1:3.5.7-4
Obsoletes: kdeaddons-noatun
Obsoletes: %{oldname}-kaddressbook-plugins
Provides: %{oldname}-kaddressbook-plugins = %epoch:%version


%description kaddressbook-plugins
Kaddressbook-plugins addons.

%files kaddressbook-plugins
%defattr(-,root,root)
%_kde3_libdir/kde3/libkaddrbk_geo_xxport.*
%_kde3_libdir/kde3/libkaddrbk_gmx_xxport.*
%_kde3_appsdir/kaddressbook
%_kde3_datadir/services/kaddressbook/gmx_xxport.desktop
%_kde3_datadir/services/kaddressbook/geo_xxport.desktop

#-----------------------------------------------------------------------------------

%package knewsticker
Summary: Knewsticker addons
Group: Graphical desktop/KDE3
Requires: kdenetwork3-knewsticker
Conflicts: kdeaddons < 1:3.5.7-4
Obsoletes: kdeaddons-noatun
Obsoletes: %{oldname}-knewsticker
Provides: %{oldname}-knewsticker = %epoch:%version


%description knewsticker
knewsticker addons

%files knewsticker
%defattr(-,root,root)
%_kde3_appsdir/knewsticker

#-----------------------------------------------------------------------------------

%package kate
Summary: Kate addons
Group: Graphical desktop/KDE3
Requires: kdebase3-kate
Conflicts: kdeaddons < 1:3.5.7-4
Obsoletes: kdeaddons-noatun
Obsoletes: %{oldname}-kate
Provides: %{oldname}-kate = %epoch:%version


%description kate
Kate addons.

%files kate
%defattr(-,root,root)
%_kde3_libdir/kde3/kate*
%_kde3_libdir/kde3/libkate*
%_kde3_appsdir/kat*
%_kde3_datadir/applnk/.hidden/kate*
%_kde3_docdir/HTML/en/kate-plugins
%_kde3_datadir/services/kate*

#-----------------------------------------------------------------------------------

%package -n kde3-ksig
Summary: Signature generator
Group: Graphical desktop/KDE3
Conflicts: kdeaddons < 1:3.5.7-4
Obsoletes: kdeaddons-noatun
Obsoletes: ksig
Provides: ksig = %epoch:%version


%description -n kde3-ksig
Signature generator.

%if %mdkversion < 200900
%post -n kde3-ksig
%update_menus
%endif

%if %mdkversion < 200900
%postun -n kde3-ksig
%clean_menus
%endif

%files -n kde3-ksig
%defattr(-,root,root)
%_kde3_iconsdir/*/*/*/ksig.png
%_kde3_datadir/applications/kde/ksig.desktop
%_kde3_appsdir/ksig
%_kde3_bindir/ksig
%_kde3_docdir/HTML/en/ksig

#-----------------------------------------------------------------------------------

%package atlantik
Summary: Atlantik map generator
Group: Graphical desktop/KDE3
Requires: kdegames3
Obsoletes: kdeaddons-noatun
Obsoletes: %{oldname}-atlantik
Provides: %{oldname}-atlantik = %epoch:%version


%description atlantik
Map generator for atlantik game

%if %mdkversion < 200900
%post atlantik
%update_menus
%endif

%if %mdkversion < 200900
%postun atlantik
%clean_menus
%endif

%files atlantik
%defattr(-,root,root)
%_kde3_bindir/atlantikdesigner
%dir %_kde3_appsdir/atlantikdesigner/
%_kde3_appsdir/atlantikdesigner/*
%_kde3_datadir/applications/kde/atlantikdesigner.desktop
%_kde3_iconsdir/*/*/*/atlantikdesigner.*

#-----------------------------------------------------------------------------------

%package searchbar
Summary: Searchbar
Group: Graphical desktop/KDE3
Conflicts: kdeaddons < 1:3.5.5
Conflicts: kdeaddons-konq-plugins < 1:3.5.7-8
Obsoletes: kdeaddons-noatun
Obsoletes: %{oldname}-searchbar
Provides: %{oldname}-searchbar = %epoch:%version


%description searchbar
Search bar for konqueror

%files searchbar
%defattr(-,root,root)
%_kde3_libdir/kde3/libsearchbarplugin.*
%_kde3_appsdir/konqueror/kpartplugins/searchbar*
%_kde3_appsdir/konqueror/icons/crystalsvg/16x16/actions/google*

#-----------------------------------------------------------------------------------

%package akregator
Summary: Akregator plugins
Group: Graphical desktop/KDE3
Requires: kde3-kdepim-akregator
Conflicts: kdeaddons < 1:3.5.5
Conflicts: kdeaddons-konq-plugins < 1:3.5.7-7
Obsoletes: kdeaddons-noatun
Obsoletes: %{oldname}-akregator
Provides: %{oldname}-akregator = %epoch:%version


%description akregator
Akregator plugins.

%files akregator
%defattr(-,root,root)
%_kde3_libdir/kde3/libakregatorkonqfeedicon.*
%_kde3_libdir/kde3/libakregatorkonqplugin.*
%_kde3_appsdir/akregator/*
%_kde3_appsdir/khtml/kpartplugins/akregator*
%_kde3_datadir/services/akregator_konqplugin.desktop

#-----------------------------------------------------------------------------------

%package metabar
Summary: A sidebar plugin for KDE's Konqueror
Group: Graphical desktop/KDE3
Requires: kdebase3-progs >= 3.2
Conflicts: metabar <= 0.8-5mdk
Conflicts: kdeaddons < 1:3.5.5
Conflicts: kdeaddons-konq-plugins < 1:3.5.7-8
Obsoletes: metabar <= 0.8-5mdk
Provides: metabar = %version-%release
Obsoletes: kdeaddons-noatun
Obsoletes: %{oldname}-metabar
Provides: %{oldname}-metabar = %epoch:%version

%description metabar
A sidebar plugin for KDE's Konqueror which shows information and actions for
selected files and directories.

%files metabar
%defattr(-,root,root,-)
%{_kde3_libdir}/kde3/konqsidebar_metabar.*
%dir %{_kde3_appsdir}/metabar
%{_kde3_appsdir}/metabar/*
%_kde3_appsdir/konqsidebartng/entries/metabar.desktop
%_kde3_iconsdir/*/*/*/metabar*
%_kde3_appsdir/konqsidebartng/add/metabar_add.desktop

#-----------------------------------------------------------------------------------

%prep

%setup  -q -n %{oldname}-%{version}
%patch0 -p1 -b .fix_call_drakclock
%if %mdkversion >= 201000
%patch1 -p1
#%patch2 -p1
%endif
#%patch3 -p1
%patch4 -p0
%patch5 -p0

%build
export QTDIR=%qt3dir

export xdg_menudir=%_sysconfdir/xdg/kde/menus
make -f admin/Makefile.common cvs

PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/

%configure_kde3 \
	--without-arts

%make


%install
rm -fr %buildroot

%makeinstall_std


%clean
rm -fr %buildroot



%changelog
* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 1:3.5.12-1mvt2010.2
+ Update to Trinity 3.5.12 sources
- Remove fix-autotools.patch
+ Add xdg dirs patch
+ Add kdebase-3.5.12-config.patch
+ Fix kdeaddons-3.2.3-call-drakclock.patch
- Remove 01_searchbar-google-suggest.patch, no longer needed

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 1:3.5.10-9mvt2010.0
+ rebuild for MDV 2010.1

* Sun Jan 17 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-8mvt2010.0
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65
+ Add patch from Chakra Linux to provide google search suggestions
  on searchbar

* Fri Dec 08 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-7mvt2010.0
+ New package name to avoid possible&unwanted KDE4 conflict
+ Rename kdepim and kdepim-devel
+ Fix automake 1.11 issue (still needed autoconf 2.63)

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 1:3.5.10-6mdv2010.0
+ kdepim3 dependency changed to kdepim for akregator

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 1:3.5.10-5mdv2010.0
+ Rebuild for MDV 2010.0
+ kdepim3-devel changed to kdepim-devel

* Fri Apr 03 2009 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-4mdv2009.1
+ Revision: 363639
- New requires

* Tue Mar 31 2009 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-3mdv2009.1
+ Revision: 363014
- Fix references to kdepim

* Sun Mar 22 2009 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-2mdv2009.1
+ Revision: 360344
- Fix Requires

* Tue Oct 14 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.10-1mdv2009.1
+ Revision: 293490
- New version 3.5.10

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:3.5.9-4mdv2009.0
+ Revision: 267766
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 11 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.9-3mdv2009.0
+ Revision: 218110
- bump release for rebuild for new ldflags
- fix br

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-2mdv2009.0
+ Revision: 204687
- Move to /opt and kill uselless and problematic noatun plugins

* Sat Feb 16 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-1mdv2008.1
+ Revision: 169177
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches integrated

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-not-capitalized

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 31 2007 Oden Eriksson <oeriksson@mandriva.com> 1:3.5.8-3mdv2008.1
+ Revision: 139860
- rebuilt against openldap-2.4.7 libs

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add usptream 3.5.9 branch patches
      	- Fix compilation with gcc 4.3

* Wed Oct 24 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-1mdv2008.1
+ Revision: 101692
- Kde 3.5.8

* Wed Oct 03 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-12mdv2008.0
+ Revision: 94970
- Suggests kdeaddons-kate and kdeaddons-noatun (thanks Anssi for pointing that)

* Wed Oct 03 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-11mdv2008.0
+ Revision: 94869
- Do not require kdeaddons-kate by default

* Sun Sep 30 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-9mdv2008.0
+ Revision: 94046
- Do not require kdeaddons-noatun by default

* Sat Aug 18 2007 Anssi Hannula <anssi@mandriva.org> 1:3.5.7-8mdv2008.0
+ Revision: 65551
- fix file conflicts between kdeaddons-konq-plugins and
  kdeaddons-searchbar
  kdeaddons-metabar
- add conflicts on old kdeaddons-konq-plugins to kdeaddons-akregator
  to ensure smooth upgrade

* Thu Aug 16 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-7mdv2008.0
+ Revision: 64329
- Remove conflicts

* Mon Aug 13 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-6mdv2008.0
+ Revision: 62678
- Fix conflicts.

* Wed Jun 20 2007 Anssi Hannula <anssi@mandriva.org> 1:3.5.7-5mdv2008.0
+ Revision: 41876
- fix conflicts

* Sat Jun 09 2007 Anssi Hannula <anssi@mandriva.org> 1:3.5.7-4mdv2008.0
+ Revision: 37719
- provide a kdeaddons metapackage which requires all subpackages
- drop duplicate searchbar.desktop from main package

  + Helio Chissini de Castro <helio@mandriva.com>
    - Split split split .... Closing bug #17000

* Sat May 26 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.7-2mdv2008.0
+ Revision: 31402
- Rebuild for directfb 1.0

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update kdeaddons for 3.5.7


* Fri Mar 02 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-3mdv2007.0
+ Revision: 131499
- Fix conflicts

* Fri Mar 02 2007 Laurent Montel <lmontel@mandriva.com> 1:3.5.6-2mdv2007.1
+ Revision: 131103
- Rebuild
- 3.5.6
- Fix spec file
- Fix konq quick browser icon

* Thu Oct 26 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-3mdv2007.1
+ Revision: 72719
- Increase release
- Fix conflict
- Fix epoch

* Wed Oct 25 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-2mdv2007.1
+ Revision: 72320
- Install akregator files into kdeaddons-akregator
  => fix display akregator into konqueror
- 3.5.5
- Fix metabar

* Thu Sep 07 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-3mdv2007.0
+ Revision: 60239
- New package (3.5.4-mdv 2006-09-06)
  Obsolete devel package too

* Wed Aug 09 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-2mdv2007.0
+ Revision: 54423
- Fix conflict
- New package (2006/08/04 3.5.4-1mdv)

  + Helio Chissini de Castro <helio@mandriva.com>
    - Updated for latest official kde 3.5.4 release

* Mon Jul 24 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.3-7mdv2007.0
+ Revision: 41935
- Remove debug
- Don't requires kdebase metapackage but kdebase-progs (need by kdeaddons)
- 3.5.3
- Rebuild against new xorg
- Rebuild to generate category
- Fix file list
- 3.5.2
- Fix conflict with metabar (Patch from neoclust)
- Fix buildrequires
- 3.5.1
- Fix enable debug for cooker
  MDK9.2 is obsolete now
- Add patch (and improve) from Neoclust to split metabar plugins
  Sync with kde3.5 branch
- Add patch (and improve) from Neoclust to split metabar plugins
- real kde3.5
- 3.5.0
- Rebuild for missing package
- Fix typo
  * Wed Nov 02 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.5-3mdk
- Rebuild with new mysql
  * Thu Oct 27 2005 Helio Chissini de Castro <helio@mandriva.com> 3.3.5-2mdk
- New immodule patch
- Obsolete metabar
- 3.4.92
- Fix package
- Rebuild
- Fix akregator bug
- Fix rebuild
- Rebuild
- Fix conflict
- Rebuild
- Fix conflict (update from MDK10.1)
- Update from svn
- New release for missing package
- 3.4.2

  + Helio Chissini de Castro <helio@mandriva.com>
    - Fix search plugin. Invalid file list
    - Added tarball from kde branch as discussed on meeting in 28/06
    - Removed rpath and added configure macro invalidating libtoolize
    - Cleanup to get rid of all library packages ( no libraries at all, just modules )
    - We are Mandriva now
    - Uploading package ./kdeaddons

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 17 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-6mdk
- Fix MDK bug #15477

* Tue May 03 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-5mdk
- Add missing build requires found by Christiaan Welvaart <cjw@daneel.dyndns.org>

* Sat Apr 23 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-4mdk
- Reactivate -fvisibility

* Fri Apr 15 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-3mdk
- Fix email
- Fix spec

* Tue Apr 12 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-2mdk
- Reactivate debug
- Clean spec
- Readd noatun file
- Use --enable-new-ldflags

* Thu Apr 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0

* Tue Mar 08 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-14mdk
- Add patch4: fix xmms applet

* Wed Feb 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-13mdk
- Fix MDK bug #13915

* Tue Feb 22 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-12mdk
- Patch10: Disable relational bar

* Fri Feb 11 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-11mdk
- Fix conflict found by Frank Griffin

* Thu Feb 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-10mdk
- Disable debug

* Mon Jan 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-9mdk
- Disable visibility for ppc

* Fri Jan 21 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-8mdk
- Fix spec file

* Fri Jan 21 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-7mdk
- Fix compile for atlantik designer

* Thu Jan 20 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-6mdk
- Add patch9: fix konq-plugins rellink 
- Disable atlantik-designer there is a bug when I try to compile it

* Tue Jan 18 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-5mdk
- Fix menu entry

* Mon Jan 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-4mdk
- Rebuild

* Fri Jan 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-3mdk
- Add -fvisibility

* Wed Dec 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-2mdk
- Fix menu

* Tue Nov 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Tue Nov 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-6mdk
- Sync with CVS

* Mon Nov 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-5mdk
- Add requires on arts

* Thu Oct 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-4mdk
- bye-bye %%buildfor

* Wed Oct 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-3mdk
- Sync with CVS

* Wed Oct 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-2mdk
- Deprecated mdk < 9.2
- Remove search bar code

* Sat Oct 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-1mdk
- 3.3.1

* Thu Sep 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-2mdk
- Sync with CVS

* Sat Sep 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-1mdk
- 3.3.0

* Sat Sep 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-14mdk
- Add patch7: fix "Squeeze the urls"

* Tue Aug 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-13mdk
- Add patch6: fix xmlcheck kde bug #82560

* Fri Aug 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-12mdk
- Add patch5: call drakclock mdk bug #10742

* Tue Aug 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-11mdk
- Disable debug

* Fri Jul 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-10mdk
- Try to fix bad dependancy

* Fri Jul 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-9mdk
- Fix spec file

* Thu Jul 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-8mdk
- Remove rpath

* Wed Jul 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-7mdk
- Rebuild with new kdelibs

* Tue Jul 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-6mdk
- Fix requires for jpegtran (necessary to rotate jpeg image)

* Fri Jul 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-5mdk
- Sync with CVS
- fix flicking into searchbar

* Thu Jul 01 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-4mdk
- Fix requires for konqueror-servicemenu

* Fri Jun 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-3mdk
- Fix search bar.

* Thu Jun 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-2mdk
- Fix some bugs into search google bar from kde 3.3

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Thu Jun 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-2mdk
- Rebuild with debug

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Fri Apr 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-3mdk
- Apply patch from gbeauchesne@mandrakesoft.com fix deps (Thanks a lot)

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-2mdk
- Fix spec file to using rpmbuildupdate

* Sat Apr 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

* Wed Mar 31 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-16mdk
- use %%configure
- use mdkversion

* Mon Mar 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-15mdk
- Fix bug #8348 don't install kdegames when we want just UA

* Fri Mar 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-14mdk
- Fix group

