
%define branch 0
%define oname kdesdk
%define lib_name_orig lib%{oname}
%define lib_oldname %mklibname %{oname} %lib_major
%define lib_major 1
%define lib_name %mklibname %{name} %lib_major

Name:		kde3-%{oname}
Summary:	K Desktop Environment - Software Development Kit
Version:	3.5.12
Release:	%mkrel 1
Epoch:		1
License:	GPL
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
#Patch1:		kdesdk-3.5.9-fix-underlinking.patch
#Patch2:		kdesdk-3.5.10-antlr.patch
Patch3:		kde-3.5.10-acinclude.patch
#Patch4:		fix_autotools.patch
Patch5:         kdebase-3.5.12-move-xdg-menu-dir.patch
Patch6:         kdebase-3.5.12-config.patch
Group:		Graphical desktop/KDE3
BuildRoot: 	%_tmppath/%name-%version-%release-root

Provides:	%{oname}3 = %epoch:%version-%release
Provides:	%{oname} = %epoch:%version-%release
Obsoletes:	%{oname}3
Obsoletes:	%{oname}
Requires:	automake >= 1.8
Requires:	autoconf >= 1:2.59
BuildRequires:	db4-devel 
BuildRequires:	freetype2-devel
BuildRequires:	kdelibs-devel 
BuildRequires:	bzip2-devel 
BuildRequires:	jpeg-devel 
BuildRequires:	lcms-devel 
BuildRequires:	mng-devel 
BuildRequires:	png-devel 
BuildRequires:	qt3-devel
BuildRequires:	zlib-devel
%if %mdkversion < 201000
BuildRequires:	autoconf <= 1:2.63
%endif
BuildRequires:	autoconf >= 1:2.65
BuildRequires:	automake >= 1.7
BuildRequires:	kde3-macros
BuildRequires:	flex
BuildRequires:	binutils-devel
BuildRequires:	subversion-devel
BuildRequires:	libxslt-devel
BuildRequires:	mesaglut-devel 
BuildRequires:	libx11-devel 

%description
Software Development Kit for the K Desktop Environment.

%files
%defattr(-,root,root)
%_kde3_bindir/*
%doc %_kde3_docdir/HTML/en/kbugbuster
%doc %_kde3_docdir/HTML/en/kdesvn-build
%_kde3_iconsdir/*/*/*/kuiviewer*
%_kde3_iconsdir/*/*/*/kbugbuster*
%_kde3_appsdir/katepart/syntax/kdesvn-buildrc.xml
%_kde3_libdir/kde3/*
%_mandir/man1/kde-build*
%_mandir/man1/includemocs*
%_mandir/man1/kdesvn-build*
%_kde3_appsdir/kstyle/*
%_kde3_datadir/applications/kde/kbugbuster.desktop
%_kde3_datadir/applications/kde/kuiviewer.desktop
%dir %_kde3_appsdir/kbugbuster
%_kde3_appsdir/kbugbuster/*
%dir %_kde3_appsdir/kapptemplate/
%_kde3_appsdir/kapptemplate/*
%dir %_kde3_appsdir/kuiviewer/
%_kde3_appsdir/kuiviewer/*
%dir %_kde3_appsdir/kuiviewerpart/
%_kde3_appsdir/kuiviewerpart/*
%_kde3_datadir/servicetypes/*
%_kde3_appsdir/kmtrace/kde.excludes
%_kde3_appsdir/kabc/*
%_kde3_datadir/services/*
%exclude %_kde3_bindir/kbabel
%exclude %_kde3_bindir/kbabeldict
%exclude %_kde3_bindir/catalogmanager
%exclude %_kde3_bindir/kcachegrind
%exclude %_kde3_bindir/po2xml
%exclude %_kde3_bindir/split2po
%exclude %_kde3_bindir/swappo
%exclude %_kde3_bindir/transxx
%exclude %_kde3_bindir/xml2pot
%exclude %_kde3_libdir/kde3/kbabel*
%exclude %_kde3_libdir/kde3/kfile_po*
%exclude %_kde3_libdir/kde3/pothumbnail*
%exclude %_kde3_bindir/cervisia
%exclude %_kde3_bindir/cvsaskpass
%exclude %_kde3_bindir/cvsservice
%exclude %_kde3_bindir/umbrello
%exclude %_kde3_bindir/kompare
%exclude %_kde3_datadir/services/cvsservice.desktop
%exclude %_kde3_datadir/services/kbabel_*.desktop
%exclude %_kde3_datadir/services/po*.desktop
%exclude %_kde3_datadir/services/dbsea*.desktop
%exclude %_kde3_datadir/services/kfile_po.desktop
%exclude %_kde3_datadir/services/tmx*.desktop
%exclude %_kde3_datadir/services/kompare*
%exclude %_kde3_datadir/servicetypes/kbabel*.desktop
%exclude %_kde3_datadir/servicetypes/kompareviewpart.desktop
%exclude %_kde3_datadir/servicetypes/komparenavigationpart.desktop
%exclude %_kde3_libdir/kde3/libcervisiapart.*
%exclude %_kde3_libdir/kde3/cervisia.*
%exclude %_kde3_libdir/kde3/cvsaskpass.*
%exclude %_kde3_libdir/kde3/cvsservice.*
%exclude %_kde3_libdir/kde3/libkompare*
%exclude %_kde3_libdir/libkdeinit_cervisia.*
%exclude %_kde3_libdir/libkdeinit_cvsaskpass.*
%exclude %_kde3_libdir/libkdeinit_cvsservice.*

#---------------------------------------------------------------

%package -n %lib_name
Summary:        Lib files for kdesdk
Group:		System/Libraries
Conflicts:	kdesdk <= 3.1.94-13mdk
Conflicts:      %lib_name-kbabel <= 3.3.2-1mdk
Provides:	%lib_name_orig = %epoch:%version-%release
Provides:	%lib_oldname = %epoch:%version-%release
Obsoletes:	%lib_name_orig
Obsoletes:	%lib_oldname
 
%description -n %lib_name
Lib files for kdesdk

%if %mdkversion < 200900
%post -n %lib_name -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name -p /sbin/ldconfig
%endif

%files -n %lib_name
%defattr(-,root,root,-)
%_kde3_libdir/libkompareinterface.la
%_kde3_libdir/libkompareinterface.so.*
%_kde3_libdir/libkspy.so.*
%_kde3_libdir/libkspy.la
%_kde3_libdir/kmtrace/libktrace.la
%_kde3_libdir/kmtrace/libktrace.so
%_kde3_libdir/kmtrace/libktrace_s.a
%_kde3_libdir/libkunittestgui.so.*
%_kde3_libdir/libkunittestgui.la

#---------------------------------------------------------------

%package umbrello
Summary:	UML Modeller
Group:		Graphical desktop/KDE3
Provides:	umbrello3 = %epoch:%version-%release
Provides:	kde3-umbrello = %epoch:%version-%release
Provides:	%{oname}-umbrello = %epoch:%version-%release
Obsoletes:	%{oname}-umbrello
Conflicts:	kdesdk <= 3.1.94-13mdk

%description umbrello
Umbrello UML Modeller is a UML diagramming tool for KDE.

%if %mdkversion < 200900
%post  umbrello
%update_menus
%endif

%if %mdkversion < 200900
%postun  umbrello
%clean_menus
%endif

%files umbrello
%defattr(-,root,root,-)
%_kde3_bindir/umbrello
%_kde3_datadir/applications/kde/umbrello.desktop
%doc %_kde3_docdir/HTML/en/umbrello
%dir %_kde3_appsdir/umbrello/
%_kde3_appsdir/umbrello/*
%_kde3_iconsdir/*/*/*/umbrello*
%_kde3_datadir/mimelnk/application/x-umbrello.desktop

#---------------------------------------------------------------

%package cervisia
Summary:	CVS client part
Group:		Graphical desktop/KDE3
Requires:	cvs
Requires:	%lib_name-cervisia = %epoch:%version-%release
Provides:	cervisia3 = %epoch:%version-%release
Provides:	kde3-cervisia = %epoch:%version-%release
Provides:	%{oname}-cervisia = %epoch:%version-%release
Obsoletes:	%{oname}-cervisia
Conflicts:	kdesdk <= 3.1.94-13mdk


%description cervisia
CVS client part.

%if %mdkversion < 200900
%post  cervisia
%update_menus
%endif

%if %mdkversion < 200900
%postun  cervisia
%clean_menus
%endif

%files cervisia
%defattr(-,root,root,-)
%_kde3_bindir/cervisia
%_kde3_bindir/cvsaskpass
%_kde3_bindir/cvsservice
%_kde3_appsdir/kconf_update/cervisia-change_repos_list.pl
%_kde3_appsdir/kconf_update/cervisia-normalize_cvsroot.pl
%_kde3_iconsdir/*/*/*/cervisia*
%_kde3_iconsdir/*/*/*/vcs*
%_kde3_iconsdir/*/*/*/svn*
%_kde3_appsdir/konqueror/servicemenus/subversion*
%_mandir/man1/cervisia*
%_mandir/man1/cvs*
%_mandir/man1/noncvslist*
%_kde3_datadir/config.kcfg/cervisiapart.kcfg
%dir %_kde3_appsdir/cervisia/
%_kde3_appsdir/cervisia/*
%_kde3_datadir/applications/kde/cervisia.desktop
%doc %_kde3_docdir/HTML/en/cervisia
%dir %_kde3_appsdir/cervisiapart/
%_kde3_appsdir/cervisiapart/*
%_kde3_appsdir/kconf_update/cervisia.upd  
%_kde3_appsdir/kconf_update/change_colors.pl  
%_kde3_appsdir/kconf_update/move_repositories.pl
%_kde3_datadir/services/cvsservice.desktop
%_kde3_libdir/kde3/libcervisiapart.*
%_kde3_libdir/kde3/cervisia.*
%_kde3_libdir/kde3/cvsaskpass.*
%_kde3_libdir/kde3/cvsservice.*
%_kde3_libdir/libkdeinit_cervisia.*
%_kde3_libdir/libkdeinit_cvsaskpass.*
%_kde3_libdir/libkdeinit_cvsservice.*

#---------------------------------------------------------------

%package kompare
Summary:	KDE diff graphic tool
Group:		Graphical desktop/KDE3
Provides:	kompare3 = %epoch:%version-%release
Provides:	kde3-kompare = %epoch:%version-%release
Provides:	%{oname}-kompare = %epoch:%version-%release
Obsoletes:	%{oname}-kompare
Conflicts:	kdesdk < 3.5.9-2

%description kompare
kompare is a KDE diff graphic tool

%if %mdkversion < 200900
%post kompare
%update_menus
%endif

%if %mdkversion < 200900
%postun kompare
%clean_menus
%endif

%files kompare
%defattr(-,root,root,-)
%_kde3_bindir/kompare
%doc %_kde3_docdir/HTML/en/kompare
%_kde3_datadir/applications/kde/kompare.desktop
%_kde3_datadir/servicetypes/kompareviewpart.desktop
%_kde3_libdir/kde3/libkomparenavtreepart.la
%_kde3_libdir/kde3/libkomparenavtreepart.so
%_kde3_libdir/kde3/libkomparepart.la
%_kde3_libdir/kde3/libkomparepart.so
%_kde3_datadir/services/komparenavtreepart.desktop
%_kde3_datadir/services/komparepart.desktop
%_kde3_datadir/servicetypes/komparenavigationpart.desktop
%dir %_kde3_appsdir/kompare/
%_kde3_appsdir/kompare/*
%_kde3_iconsdir/*/*/*/kompare*

#---------------------------------------------------------------

%package kcachegrind
Summary:	KCachegrind
Group:		Graphical desktop/KDE3
Requires:	valgrind
Provides:	kcachegrind3 = %epoch:%version-%release
Provides:	kde3-kcachegrind = %epoch:%version-%release
Provides:	%{oname}-kcachegrind = %epoch:%version-%release
Obsoletes:	%{oname}-kcachegrind
Conflicts:	kdesdk <= 3.1.94-13mdk

%description kcachegrind
KCachegrind is a visualisation tool for the profiling data generated by 
Cachegrind and Calltree (they profile data file format is upwards compatible).
Calltree extends Cachegrind, which is part of Valgrind.

%if %mdkversion < 200900
%post  kcachegrind
%update_menus
%endif

%if %mdkversion < 200900
%postun  kcachegrind
%clean_menus
%endif

%files kcachegrind
%defattr(-,root,root,-)
%_kde3_bindir/kcachegrind
%doc %_kde3_docdir/HTML/en/kcachegrind
%_kde3_iconsdir/*/*/*/kcachegrind*
%dir %_kde3_appsdir/kcachegrind/
%_kde3_appsdir/kcachegrind/*
%_kde3_datadir/mimelnk/application/x-kcachegrind.desktop
%_kde3_datadir/applications/kde/kcachegrind.desktop

#---------------------------------------------------------------

%package po2xml
Summary:	Xml2po and vice versa converters
Group:		Graphical desktop/KDE3
Provides:	kde3-po2xml = %epoch:%version-%release
Provides:	%{oname}-xml2pot = %epoch:%version-%release
Provides:	%{oname}-po2xml = %epoch:%version-%release
Obsoletes:	%{oname}-po2xml
Conflicts:	kdesdk <= 3.5.6-4mdk

%description po2xml
An xml2po and vice versa converters.

%files po2xml
%defattr(-,root,root,-)
%_kde3_bindir/po2xml
%_kde3_bindir/split2po
%_kde3_bindir/swappo
%_kde3_bindir/transxx
%_kde3_bindir/xml2pot

#---------------------------------------------------------------

%package kbabel
Summary:	Set of tools for editing and managing gettext PO files
Group:		Graphical desktop/KDE3
Requires:	%lib_name-kbabel = %epoch:%version-%release
Requires:	gettext
Provides:	kbabel3 = %epoch:%version-%release
Provides:	kde3-kbabel = %epoch:%version-%release
Provides:	%{oname}-kbabel = %epoch:%version-%release
Obsoletes:	%{oname}-kbabel
Conflicts:	kdesdk <= 3.1.94-13mdk

%description kbabel
KBabel is a set of tools for editing and managing gettext PO files. 
Main part is a powerful and comfortable PO file editor which features 
full navigation capabilities, full editing functionality, possibility 
to search for translations in different dictionaries, spell and 
syntax checking, showing diffs and many more. Also included is a 
"Catalog Manager", a file manager view which helps keeping an overview 
of PO files. Last but not least it includes a standalone 
dictionary application as an additional possibility to access KBabel's 
powerful dictionaries. 
KBabel will help you to translate fast and also keep consistent translations.

%if %mdkversion < 200900
%post  kbabel
%update_menus
%endif

%if %mdkversion < 200900
%postun  kbabel
%clean_menus
%endif

%files kbabel
%defattr(-,root,root,-)
%_kde3_bindir/kbabel
%_kde3_bindir/kbabeldict
%_kde3_bindir/catalogmanager
%_kde3_datadir/applications/kde/kbabel.desktop
%_kde3_datadir/applications/kde/kbabeldict.desktop
%_kde3_datadir/applications/kde/catalogmanager.desktop
%_kde3_iconsdir/*/*/*/catalogmanager*
%_kde3_iconsdir/*/*/*/kbabel*
%dir %_kde3_appsdir/kbabel
%_kde3_appsdir/kbabel/*
%_kde3_appsdir/kconf_update/kbabel-difftoproject.upd
%_kde3_appsdir/kconf_update/kbabel-project.upd
%_kde3_appsdir/kconf_update/kbabel-projectrename.upd
%_kde3_datadir/config.kcfg/kbabel.kcfg
%_kde3_datadir/config.kcfg/kbprojectsettings.kcfg
%dir %_kde3_appsdir/catalogmanager
%_kde3_appsdir/catalogmanager/*
%doc %_kde3_docdir/HTML/en/kbabel
%_kde3_datadir/services/kbabel_*.desktop
%_kde3_datadir/services/po*.desktop
%_kde3_datadir/services/dbsea*.desktop
%_kde3_datadir/services/kfile_po.desktop
%_kde3_datadir/services/tmx*.desktop
%_kde3_datadir/servicetypes/kbabel*.desktop

#---------------------------------------------------------------

%package -n %lib_name-kbabel
Summary:	Library files for KBabel
Group:		System/Libraries
Provides:	%lib_oldname-kbabel = %epoch:%version-%release
Obsoletes:	%lib_oldname-kbabel
Conflicts:	kdesdk <= 3.1.94-13mdk

%description -n %lib_name-kbabel
Library files for KBabel.

%files -n %lib_name-kbabel
%defattr(-,root,root,-)
%_kde3_libdir/libkbabelcommon.so.*
%_kde3_libdir/libkbabelcommon.la
%_kde3_libdir/libkbabeldictplugin.la
%_kde3_libdir/libkbabeldictplugin.so.*
%_kde3_libdir/kde3/kbabel*.so
%_kde3_libdir/kde3/kbabel*.la
%_kde3_libdir/kde3/kfile_po.so
%_kde3_libdir/kde3/kfile_po.la
%_kde3_libdir/kde3/pothumbnail.so
%_kde3_libdir/kde3/pothumbnail.la

#---------------------------------------------------------------

%package -n %lib_name-cervisia
Summary:	Library for CVS client part
Group:		System/Libraries
Conflicts:	kdesdk <= 3.1.94-13mdk
Provides:	%lib_name_orig-cervisia = %epoch:%version-%release
Provides:	%lib_oldname-cervisia = %epoch:%version-%release
Obsoletes:	%lib_oldname-cervisia

%description -n %lib_name-cervisia
Library for CVS client part.

%if %mdkversion < 200900
%post -n %lib_name-cervisia -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name-cervisia -p /sbin/ldconfig
%endif

%files -n %lib_name-cervisia
%defattr(-,root,root,-)
%_kde3_libdir/libcvsservice.la
%_kde3_libdir/libcvsservice.so.*

#---------------------------------------------------------------

%package devel
Summary:	Devel files for kdesdk
Group:		Development/KDE and Qt
Requires:	%lib_name-cervisia = %epoch:%version-%release
Conflicts: 	kdesdk <= 3.1.94-13mdk
Obsoletes:	%lib_name-cervisia-devel < 1:3.5.9
Provides:	%lib_name-cervisia-devel = %epoch:%version
Obsoletes:	%lib_name-kbabel-devel < 1:3.5.9
Provides:	%lib_name-kbabel-devel = %epoch:%version
Obsoletes:	%lib_name-devel < 1:3.5.9
Provides:	%lib_name-devel = %epoch:%version
Provides:	%lib_oldname-devel = %epoch:%version-%release
Obsoletes:	%lib_oldname-devel

%description devel
Devel files for kdesdk.

%files devel
%defattr(-,root,root,-)
%_kde3_includedir/*
%_kde3_libdir/libcvsservice.so
%_kde3_libdir/libkbabelcommon.so
%_kde3_libdir/libkbabeldictplugin.so
%_kde3_libdir/libkompareinterface.so
%_kde3_libdir/libkspy.so
%_kde3_libdir/libkunittestgui.so

#---------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
#%patch1 -p0 -b .underlinking
#%patch2 -p1
%if %mdkversion >= 201000
%patch3 -p1
#%patch4 -p1
%patch5 -p0
%patch6 -p0
%endif

%build
export QTDIR=%qt3dir

PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/
export xdg_menudir=%_sysconfdir/xdg/kde/menus

make -f admin/Makefile.common cvs

%configure_kde3 \
   --with-apr-config=%_bindir/apr-1-config \
   --with-apu-config=%_bindir/apu-1-config \
   --with-svn-include=%_includedir

%make

%install
rm -fr %buildroot

make install DESTDIR=%buildroot

rm -f %buildroot/%_kde3_docdir/HTML/en/kbabel/TODO

%clean
rm -fr %buildroot


%changelog

* Mon Jul 25 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-1mvt2010.2
+ Update to trinity 2.5.12 sources
- Remove fix_autotools.patch, kdesdk-3.5.9-fix-underlinking.patch, kdesdk-3.5.10-antlr.patch
+ Add kdebase-3.5.12-move-xdg-menu-dir.patch, kdebase-3.5.12-config.patch

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 1:3.5.10-4mvt2010.0
+ Rebuild for MDV 2010.1

* Mon Jan 18 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-3mvt2010.0
- Rebuild for 2010.0
- Change package name to avoid KDE4 upgrade
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65:patch3
+ Fix automake 1.11 issue:patch4

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 1:3.5.10-2mdv2010.0
+ Rebuild for MDV 2010.0

* Thu Aug 28 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-1mdv2009.0
+ Revision: 277089
- remove spurious build requires on kdepim-devel
- Latest kde 3 upstream package

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:3.5.9-8mdv2009.0
+ Revision: 267779
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jun 07 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.9-7mdv2009.0
+ Revision: 216755
- readd svn plugin
- fix svn include dir
- add underlinking patch
- rebuild for new qt3 libdir

* Mon May 19 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 1:3.5.9-6mdv2009.0
+ Revision: 209006
- User versioned obsoletes

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-5mdv2009.0
+ Revision: 204009
- Move to /opt

* Sat Mar 22 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-4mdv2008.1
+ Revision: 189496
- Fix groups ( tks to pterjan)

* Mon Mar 03 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-3mdv2008.1
+ Revision: 177822
- Fix file list

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:3.5.9-2mdv2008.1
+ Revision: 170922
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-1mdv2008.1
+ Revision: 169004
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches integrated
- Obsolete worng lib devel packages to one devel package to rule then all

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-not-capitalized

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Fix file list for kompare

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 26 2007 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.8-3mdv2008.1
+ Revision: 137902
- Changing the release to rebuild this package

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.8-2mdv2008.1
+ Revision: 109225
- rebuild for new lzma

* Sun Oct 28 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-1mdv2008.1
+ Revision: 102855
- Kde 3.5.8
  Remove merged patch

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-ended-with-dot

* Thu Sep 13 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-3mdv2008.0
+ Revision: 85381
- [BUGFIX] Apply upstream patch to handle correclty CVS in cervisia (BUG #30497)'
  Remove Hardcoded Packager Tag

  + Funda Wang <fundawang@mandriva.org>
    - Remove 2006 conditions
    - More provides for po2xml

* Wed May 16 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-1mdv2008.0
+ Revision: 27458
- 3.5.7 release

* Wed May 16 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.6-4mdv2008.0
+ Revision: 27249
- split po2xml tools.
- Remove changelog entries.


* Mon Mar 05 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-3mdv2007.0
+ Revision: 133246
- Just cervisia needs cvs

* Thu Mar 01 2007 Laurent Montel <lmontel@mandriva.com> 1:3.5.6-2mdv2007.1
+ Revision: 130569
- Fix kbugbuster mandriva address
- 3.5.6
- Fix spec file

* Mon Oct 30 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-5mdv2007.1
+ Revision: 73733
- Subversion -1.4 doesn't have svn-config program
  => check into kdesdk doesn't work (for the moment)
  => disable it
- Fix buildrequires
- Rebuild
- Rebuild
- New release (2006/08/02 -3.5.4-mdv)
--enable-new-ldflags doesn't work on x86_64
- Rebuild for x86_64
- Fix with new valgrind
- 3.5.33.5.33.5.3
- Rebuild against new xorg
- Rebuild to generate new category
- 3.5.2
- Fix man page
- 3.5.1
- Real kde3.5
- 3.5.0 (named rc1)
- Fix typo
  * Wed Nov 02 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.5-3mdk
- Rebuild with new mysql
  * Thu Oct 27 2005 Helio Chissini de Castro <helio@mandriva.com> 3.3.5-2mdk
- New immodule patch
- 3.4.92
- Rebuild
- Now it's necessary to use --libsuffix
- Add patch from neoclust (without remove xfree bugzilla) fix kde bug #102873
- Remove debug
  Add diff
- 3.4.2

  + Helio Chissini de Castro <helio@mandriva.com>
    - Back to use branch tarballs. Now using post 3.5.5
    - Updated spec. The spec layout was too old and not match with current kde specs
      on mandriva
    - Added missing subveriosn support on cervisia
    - We are Mandriva now
    - Uploading package ./kdesdk

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Wed May 18 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-6mdk
- Fix requires on automake1.7 for kdeapptemplate (bug found by qa)

* Thu May 05 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-5mdk
- Rebuild with new gcc

* Sat Apr 23 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-4mdk
- Fix debug flag

* Sun Apr 17 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-4mdk
- Activate visibility same as for ppc
- Add comment to remove patch for kde 3.5 (patch commited into kde head)

* Wed Apr 13 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-3mdk
- Reapply patch4: fix compile on x86_64

* Tue Apr 12 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-2mdk
- Reactivate debug
- Change email
- Use --enable-new-ldflags

* Thu Apr 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0

* Mon Feb 14 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.3.2-11mdk
- fix build on x86_64

* Fri Feb 11 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-10mdk
- Fix build on x86_64 (can't compile kmtrace and co)

* Thu Feb 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-9mdk
- Disable debug

* Fri Jan 28 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-8mdk
- Fix menu entry

* Mon Jan 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-7mdk
- Disable visibility for ppc

* Wed Jan 19 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-6mdk
- Requires on valgrind plugins MDK bug #13096

* Thu Jan 13 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-5mdk
- Use -fvisibility

* Tue Dec 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-4mdk
- Sync with CVS

* Tue Dec 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-3mdk
- Fix conflict

* Wed Dec 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-2mdk
- Fix menu

* Tue Nov 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Fri Oct 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-4mdk
- Requires gettext for kbabel fix MDK kde bug #12156

* Thu Oct 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-3mdk
- bye-bye %%buildfor

* Tue Oct 12 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-2mdk
- Deprecated mdk < 9.2

* Sat Oct 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-1mdk
- 3.3.1

* Thu Sep 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-2mdk
- Sync with kde 3.3 brnach

* Fri Sep 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-1mdk
- 3.3.0

* Thu Aug 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-12mdk
- Add patch4: fix kbabel mem leak

* Tue Aug 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-11mdk
- Add patch3: fix kompare

* Sat Aug 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-10mdk
- Rebuild for new menu translation table

* Tue Aug 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-9mdk
- Remove debug

* Fri Jul 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-8mdk
- Sync with CVS

* Sat Jul 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-7mdk
- Fix spec file

* Thu Jul 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-6mdk
- Fix remove rpath

* Fri Jul 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-5mdk
- Add patch1: fix kde bug #83018 
	"Disable 'Diff' button until the dialog appears so the user doesn't
	 accidentilly opens the same diff several times."

* Wed Jul 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-4mdk
- Rebuild with new kdelibs

* Tue Jul 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-3mdk
- Remove patch3 not necessary (break build under MDK10.0)

* Tue Jun 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-2mdk
- Fix build requires

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-7mdk
- Rebuild

* Wed Jun 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-6mdk
- Rebuild with debug

* Sat May 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-5mdk
- Add buildrequires

* Thu May 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-4mdk
- kcachgrind can read also gprof file => change requires on valgrind to 
specific ix86

* Wed May 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-3mdk
- Merge Gb amd64 fix (kcachegrind is ix86 specific)

* Fri May 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-2mdk
- Fix some rpmlint error

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-2mdk
- Fix spec file for using rpmbuildupdate

* Fri Apr 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

* Wed Mar 31 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-12mdk
- use mdkverion
- use %%configure

* Wed Mar 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-11mdk
- Fix compile under amd64 (patch gb)

