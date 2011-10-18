%define oname kdewebdev
%define lib_name_orig lib%oname
%define lib_major 0
%define lib_name %mklibname %name %lib_major
%define lib_oldname %mklibname %oname %lib_major

%define oldname quanta
%define oldlib_name %mklibname %oldname %lib_major

%define obsolete_numver 3.2.3-30mdk

%define unstable 0
%{?_unstable: %{expand: %%global unstable 1}}

%if %unstable
%define dont_strip 1
%endif

Name:	          kde3-%{oname}
Version:          3.5.12
Release:          %mkrel 1
License:          GPL
Summary:          A web editor for the KDE Desktop Environment
Epoch:            1
URL:              http://www.kde.org
Source:           ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
Source1:          css.tar.bz2
Source2:          html.tar.bz2
Source3:          javascript.tar.bz2
Source4:          mysql5-quanta-doc-20051117.tar.bz2
Source5:          php.tar.bz2
Patch0:           kde-3.5.10-acinclude.patch
#Patch1:           fix_autotools.patch
Patch2:           kdebase-3.5.12-move-xdg-menu-dir.patch
Patch3:           kdebase-3.5.12-config.patch
Group:            Graphical desktop/KDE3
BuildRoot:        %_tmppath/%name-%version-%release-root
BuildRequires:    pam
BuildRequires:    diffutils
BuildRequires:    texinfo gettext 
BuildRequires:    jpeg-devel
BuildRequires:    png-devel
BuildRequires:    arts-devel
BuildRequires:    libxml2-devel
BuildRequires:    libxslt-devel
BuildRequires:    automake >= 1.8
%if %mdkversion < 201000
BuildRequires:    autoconf <= 1:2.63
%endif
BuildRequires:    autoconf >= 1:2.65
BuildRequires:    kdelibs-devel  
BuildRequires:    freetype2 
BuildRequires:    kde3-macros
Requires:         tidy
Requires:         %{name}-kommander
Requires:         %{name}-kfilereplace
Requires(post):   desktop-file-utils
Requires(postun): desktop-file-utils
Conflicts:        quanta <= %epoch:%obsolete_numver
Obsoletes:        %oldname <= %epoch:%obsolete_numver
Provides:         %oldname = %epoch:%version-%release
Provides:         %oldname = %epoch:%version-%release
Obsoletes:        %oname
Conflicts:        kdewebdev-kommander <= 3.5.5

%description
A html editor for the K Desktop Environment.

%post
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor
%endif

%postun
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor
%endif

%files
%defattr(-,root,root)
%_kde3_bindir/quanta
%_kde3_bindir/kxsldbg
%_kde3_bindir/kimagemapeditor
%_kde3_bindir/klinkstatus
%doc %_kde3_docdir/HTML/en/xsldbg
%dir %_kde3_datadir/apps/quanta
%_kde3_datadir/apps/quanta/*
%dir %_kde3_datadir/apps/kimagemapeditor/
%_kde3_datadir/apps/kimagemapeditor/*
%_kde3_iconsdir/*/*/*/kimagemap*
%_kde3_datadir/services/kimagemapeditorpart.desktop
%_kde3_libdir/kde3/libkimagemapeditor.*
%_kde3_datadir/applications/kde/kimagemapeditor.desktop
%_kde3_datadir/applications/kde/klinkstatus.desktop
%_kde3_datadir/applications/kde/kxsldbg.desktop
%_kde3_datadir/applications/kde/quanta.desktop
%_kde3_datadir/services/klinkstatus_part.desktop
%dir %_kde3_datadir/apps/klinkstatus
%_kde3_datadir/apps/klinkstatus/*
%dir %_kde3_datadir/apps/klinkstatuspart/
%_kde3_datadir/apps/klinkstatuspart/*.rc
%dir %_kde3_datadir/apps/klinkstatuspart/pics/
%_kde3_datadir/apps/klinkstatuspart/pics/*.png
%_kde3_datadir/config.kcfg/klinkstatus.kcfg
%doc %_kde3_docdir/HTML/en/klinkstatus
%_kde3_libdir/kde3/libklinkstatuspart.*
%_kde3_iconsdir/*/*/*/klinkstat*
%_kde3_iconsdir/*/*/actions/*
%_kde3_iconsdir/*/*/*/quanta*
%_kde3_datadir/mimelnk/application/x-webprj.desktop
%_kde3_datadir/servicetypes/quantadebugger.desktop
%dir %_kde3_datadir/apps/kxsldbg/
%_kde3_datadir/apps/kxsldbg/*
%dir %_kde3_datadir/apps/kxsldbgpart/
%_kde3_datadir/apps/kxsldbgpart/*
%dir %_kde3_datadir/apps/kafkapart/
%_kde3_datadir/apps/kafkapart/*
%_kde3_libdir/kde3/libkxsldbgpart.*
%_kde3_libdir/kde3/quantadebugger*.*
%_kde3_datadir/services/kxsldbg_part.desktop
%_kde3_datadir/services/quanta_preview_config.desktop
%_kde3_datadir/services/quantadebuggerdbgp.desktop
%_kde3_datadir/services/quantadebuggergubed.desktop
%doc %_kde3_docdir/HTML/en/quanta
%doc %_kde3_docdir/HTML/en/kxsldbg

#--------------------------------------------------------------------------

%package        quanta-doc
Summary:        Documentation about Quanta
Group:          Books/Computer books
Provides:       kde3-quanta-doc = %epoch:%version-%release
Provides:	%oname-quanta-doc = %epoch:%version-%release
Obsoletes:      %oname-quanta-doc

%description    quanta-doc
Documentation for Quanta

%files quanta-doc
%dir %_kde3_docdir/quanta
%dir %_kde3_docdir/quanta/css
%doc %_kde3_docdir/quanta/css/*
%dir %_kde3_docdir/quanta/html
%doc %_kde3_docdir/quanta/html/*
%dir %_kde3_docdir/quanta/javascript
%doc %_kde3_docdir/quanta/javascript/*
%dir %_kde3_docdir/quanta/mysql5
%doc %_kde3_docdir/quanta/mysql5/*
%dir %_kde3_docdir/quanta/php
%doc %_kde3_docdir/quanta/php/*

#--------------------------------------------------------------------------

%package kfilereplace
Summary:	Kfilereplace
Group:		Graphical desktop/KDE3
Obsoletes:	kfilereplace <= 0.7.1-1mdk
Provides:	kde3-kfilereplace = %epoch:%version-%release
Conflicts:	quanta <= %epoch:%obsolete_numver
Obsoletes:      %oldname-kfilereplace <= %epoch:%obsolete_numver
Provides:       %oldname-kfilereplace = %epoch:%version-%release
Obsoletes:      %lib_name-kfilereplace < 1:3.5.9
Provides:	%oname-kfilereplace = %epoch:%version-%release
Obsoletes:      %oname-kfilereplace

%description kfilereplace
Kfilereplace program

%if %mdkversion < 200900
%post kfilereplace
%update_menus
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun kfilereplace
%clean_menus
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor
%endif

%files kfilereplace
%defattr(-,root,root)
%_kde3_bindir/kfilereplace
%dir %_kde3_datadir/apps/kfilereplacepart
%_kde3_datadir/apps/kfilereplacepart/*
%dir %_kde3_datadir/apps/kfilereplace/
%_kde3_datadir/apps/kfilereplace/*
%_kde3_datadir/services/kfilereplacepart.desktop
%doc %_kde3_docdir/HTML/en/kfilereplace
%_kde3_datadir/applications/kde/kfilereplace.desktop
%_kde3_libdir/kde3/libkfilereplacepart.*
%_kde3_iconsdir/*/*/*/kfilerep*

#--------------------------------------------------------------------------

%package kommander
Summary:	Kommander
Group:		Graphical desktop/KDE3
Provides:	kde3-kommander = %epoch:%version-%release
Requires:	%lib_name-kommander = %epoch:%version-%release
Conflicts:	quanta <= %epoch:%obsolete_numver
Conflicts:      %name  < 3.5.4-4
Obsoletes:      %oldname-kommander <= %epoch:%obsolete_numver
Provides:       %oldname-kommander = %epoch:%version-%release
Provides:	%oname-kommander = %epoch:%version-%release
Obsoletes:      %oname-kommander
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description kommander
Kommander program

%if %mdkversion < 200900
%post kommander
%update_menus
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun kommander
%clean_menus
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor
%endif

%files kommander
%defattr(-,root,root)
%_kde3_bindir/kmdr-executor
%_kde3_bindir/kmdr-plugins
%_kde3_bindir/kmdr-editor
%_kde3_bindir/xsldbg
%_kde3_bindir/extractkmdr
%_kde3_bindir/kmdr2po
%_kde3_datadir/mimelnk/application/x-kommander.desktop
%doc %_kde3_docdir/HTML/en/kommander
%_kde3_datadir/applnk/.hidden/kmdr-executor.desktop
%_kde3_datadir/applications/kde/kmdr-editor.desktop
%_kde3_iconsdir/*/*/*/kommand*
%_kde3_datadir/apps/kommander
%_kde3_datadir/apps/kmdr-editor
%_kde3_datadir/apps/katepart/syntax/kommand*
%_kde3_datadir/apps/kdevappwizard/templates/kommander*
%_kde3_datadir/apps/kdevappwizard/kommander*
%_kde3_datadir/services/kommander_part.desktop
%_kde3_libdir/kde3/libkommander_part.*

#--------------------------------------------------------------------------

%package -n %lib_name-kommander
Summary:    Library for Kommander
Group:	    System/Libraries	
Conflicts:  quanta <= %epoch:%obsolete_numver
Provides:   %oldlib_name-kommander = %epoch:%version-%release
Provides:   %lib_oldname-kommander = %epoch:%version-%release
Obsoletes:  %lib_oldname-kommander
Obsoletes:  %oldlib_name-kommander
Conflicts:  quanta <= 3.2-9mdk

%description -n %lib_name-kommander
Kommander program

%if %mdkversion < 200900
%post -n %lib_name-kommander -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name-kommander -p /sbin/ldconfig
%endif

%files -n %lib_name-kommander
%defattr(-,root,root)
%_kde3_libdir/libkommanderwidgets.la
%_kde3_libdir/libkommanderwidgets.so.*
%_kde3_libdir/libkommanderplugin.la
%_kde3_libdir/libkommanderplugin.so.*
%_kde3_libdir/libkommanderwidget.la
%_kde3_libdir/libkommanderwidget.so.*

#--------------------------------------------------------------------------

%package -n %lib_name
Summary:    Library for kdewebdev
Group:      System/Libraries
Provides:   %lib_name_orig = %epoch:%version-%release
Provides:   quanta-devel = %epoch:%version-%release
Conflicts:  quanta <= %epoch:%obsolete_numver
Obsoletes:  %oldlib_name <= %epoch:%obsolete_numver
Provides:   %oldlib_name = %epoch:%version-%release
Provides:   %lib_oldname = %epoch:%version-%release
Obsoletes:  %lib_oldname


%description -n %lib_name
Library files for kdewebdev.

%files -n %lib_name
%defattr(-,root,root)

#--------------------------------------------------------------------------

%package devel
Summary:    Development library for kdewebdev
Group:      Development/KDE and Qt
Requires:   %lib_name-kommander = %epoch:%version
Requires:   %lib_name = %epoch:%version
Obsoletes:  %oldlib_name-devel <= %epoch:%obsolete_numver
Provides:   %oldlib_name-devel = %epoch:%version-%release
Obsoletes:  %lib_name-devel < 1:3.5.9
Provides:   %lib_name-devel = %epoch:%version-%release
Obsoletes:  quanta-devel < 1:3.5.9
Provides:   kde3-quanta-devel = %epoch:%version-%release
Provides:   %{lib_name_orig}-devel = %epoch:%version-%release
Conflicts:  quanta <= %epoch:%obsolete_numver
Obsoletes:  %lib_name-kommander-devel < 1:3.5.9
Provides:   %lib_name-kommander-devel = %epoch:%version
Provides:   %lib_oldname-devel = %epoch:%version-%release
Obsoletes:  %lib_oldname-devel

%description devel
Development library files for quanta.

%files devel
%defattr(-,root,root)
%_kde3_includedir/*.h
%_kde3_libdir/libkommanderwidgets.so
%_kde3_libdir/libkommanderplugin.so
%_kde3_libdir/libkommanderwidget.so

#--------------------------------------------------------------------------

%prep

%setup -q -n %oname-%version -a 1 -a 2 -a 3 -a 4 -a 5
%if %mdkversion >= 201000
%patch0 -p1
#%patch1 -p1
%endif
%patch2 -p0
%patch3 -p0

%build
export QTDIR=%qt3dir
PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/
export xdg_menudir=%_sysconfdir/xdg/kde/menus

make -f admin/Makefile.common cvs

%configure_kde3

%make

%install
rm -fr %buildroot

make install DESTDIR=%buildroot

cp kommander/working/extractkmdr   %buildroot/%_kde3_bindir/
cp kommander/working/kmdr2po %buildroot/%_kde3_bindir/

%__mkdir -p %buildroot%_kde3_datadir/doc/quanta
cp -r css/ %buildroot%_kde3_datadir/doc/quanta
cp -r html/ %buildroot%_kde3_datadir/doc/quanta
cp -r javascript/ %buildroot%_kde3_datadir/doc/quanta
cp -r mysql5/ %buildroot%_kde3_datadir/doc/quanta
cp -r php/ %buildroot%_kde3_datadir/doc/quanta
%clean
rm -rf $RPM_BUILD_ROOT





%changelog

* Mon Jul 25 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-1mvt2010.2
- Remove fix_autotools.patch
+ Add kdebase-3.5.12-move-xdg-menu-dir.patch, kdebase-3.5.12-config.patch

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 1:3.5.10-3mvt2010.0
- Rebuild for MDV 2010.1

* Mon Jan 18 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-2mvt2010.0
- Rebuild for 2010.0
- Change package name to avoid KDE4 upgrade
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65:patch0
+ Fix automake 1.11 issue:patch1

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 1:3.5.10-1mdv2010.0
+ rebuild for MDV 2010.0

* Sun Apr 19 2009 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-1mdv2009.1
+ Revision: 368024
- New version 3.5.10

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:3.5.9-6mdv2009.0
+ Revision: 267782
- rebuild early 2009.0 package (before pixel changes)

* Fri Jun 13 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.9-5mdv2009.0
+ Revision: 218660
- rebuild for new ldflags

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 20 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 1:3.5.9-4mdv2009.0
+ Revision: 209431
- Use versioned obsoletes

* Thu May 08 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-3mdv2009.0
+ Revision: 204587
- Fix Build ( thanks to helio)
- Move to /opt/kde3

* Sat Mar 22 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-2mdv2008.1
+ Revision: 189497
- Fix groups ( tks to pterjan)

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-1mdv2008.1
+ Revision: 169024
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches integrated
- Obsolete worng lib devel packages to one devel package to rule then all

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix spacing at top of description

* Sun Dec 30 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.8-3mdv2008.1
+ Revision: 139415
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 02 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-1mdv2008.1
+ Revision: 105097
- Kde 3.5.8

* Thu Oct 04 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-3mdv2008.0
+ Revision: 95305
- Fix upgrade from 2007.0

  + Anssi Hannula <anssi@mandriva.org>
    - remove hardcoded packager tag

* Sat Jun 23 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-2mdv2008.0
+ Revision: 43460
- [FEATURE] Add documentation for Quanta (bug #10091)'

* Thu May 17 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-1mdv2008.0
+ Revision: 27534
- 3.5.7 release

  + Laurent Montel <lmontel@mandriva.org>
    - Fix conflict


* Thu Feb 01 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-1mdv2007.0
+ Revision: 115858
- 3.5.6

* Wed Oct 18 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-2mdv2007.0
+ Revision: 65944
- Use packager tag
- Use official tarball

  + Helio Chissini de Castro <helio@mandriva.com>
    - Back to use branch tarballs. Now using post 3.5.5
    - Updated spec. The spec layout was too old and not match with current kde specs
      on mandriva

* Sun Sep 03 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-4mdv2007.0
+ Revision: 59594
- New package (3.5.4-4mdv 2006-09-02)
  Fix crash into css editor

* Tue Aug 15 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-3mdv2007.0
+ Revision: 55872
- New package (2006/08/14 3.5.4-3mdv)
  Be sure to obsolete old package (migrate pb)

* Sat Aug 12 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-2mdv2007.0
+ Revision: 55626
- New package (2006/08/11 3.5.4-2mdv)
  Fix icon into menu
- New package (2006/08/04 3.5.4-1mdv)

* Wed Jul 19 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.3-3mdv2007.0
+ Revision: 41548
- Fix install files
- fix compile under x86_64
- 3.5.3
- Rebuild to generate category
- Fix file list
- 3.5.2
- 3.5.1
- Activate debug for cooker only
  MDK9.2 is obsolete now
- Fix kfilereplace.desktop pos
- Real kde3.5.0
- 3.5.0
- Fix typo
  * Wed Nov 02 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.5-3mdk
- Rebuild with new mysql
  * Thu Oct 27 2005 Helio Chissini de Castro <helio@mandriva.com> 3.3.5-2mdk
- New immodule patch
- 3.4.92
- Rebuild
- Requires tidy not all component otherwise it's not necessary to split it
- New sync
- Fix icons into kommander
- Remove debug
  Sync with kde 3.4.2 branch
- Oops
- Add missing patch
- 3.4.2

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Helio Chissini de Castro <helio@mandriva.com>
    - Uploading package ./kdewebdev

* Thu May 05 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-3mdk
- Rebuild

* Tue Apr 12 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-2mdk
- Fix spec
- Reenable debug
- Use --enable-new-ldflags
- Recreate menu entry

* Tue Apr 05 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0

* Wed Mar 30 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-11mdk
- Try to fix install

* Fri Mar 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-10mdk
- Fix update from 10.1

* Wed Feb 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-9mdk
- Fix MDK bug #13914

* Thu Feb 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-8mdk
- Disable debug

* Sat Jan 29 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-7mdk
- Fix generate menu

* Tue Jan 18 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-6mdk
- Fix menu entry

* Sat Jan 15 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-5mdk
- Rebuild

* Fri Dec 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-4mdk
- Fix menu

* Thu Dec 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-3mdk
- Remove direct requires on kommander

* Wed Dec 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-2mdk
- Fix menu

* Tue Nov 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Thu Nov 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-6mdk
- Generate menu

* Tue Nov 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-5mdk
- Sync with CVS

* Wed Nov 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-4mdk
- Fix spec

* Thu Oct 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-3mdk
- bye-bye %%buildfor

* Wed Oct 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-3mdk
- Sync with CVS

* Tue Oct 12 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-2mdk
- Deprecated mdk < 9.2

* Sat Oct 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-1mdk
- 3.3.1

* Wed Sep 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-4mdk
- Fix conflict from MDK 10.0

* Thu Sep 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-3mdk
- Update from kde3.3.0

* Fri Sep 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-2mdk
- Rebuild without debug

* Fri Sep 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-2mdk
- Fix conflict

* Sat Sep 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-1mdk
- kde 3.3.0

* Mon Aug 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3-0.rc1.1mdk
- 3.3 rc1

* Fri Jul 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.92-1mdk
- Rename quanta to kdewebdev
- TODO fix conflict/Obsoletes

* Thu Jul 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-6mdk
- Add patch2: fix kde bug #82984: "grey==gray"

* Tue Jul 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-5mdk
- Sync with CVS

* Thu Jul 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-4mdk
- Fix remove rpath

* Wed Jul 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-3mdk
- Sync with CVS

* Wed Jul 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-2mdk
- Rebuild with new kdelibs

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Sat Jun 05 2004 <lmontel@mandrakesoft.com> 3.2.2-3mdk
- Rebuild

* Wed Jun 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-2mdk
- Rebuild with debug

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Thu Apr 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-5mdk
- Add patch from gbeauchesne@mandrakesoft.com fix amd64 build (thanks a lot)

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-3mdk
- Fix spec file to using rpmbuildupdate

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-2mdk
- Fix requires

* Sat Apr 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

* Wed Mar 31 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-10mdk
- Use %%configure
- Use mdkversion
- Add requires on quanta-kommander

* Thu Mar 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-9mdk
- Fix group
- Add patch1: fix treeview crash
- Add patch2: "Make removal of new top folders pointing to the non-local root directory (e.g ftp://someserver/) possible [#76573]."
- Add patch3: "Fix opening of documentation pages with references [#70345]"
- Add patch4: fix quanta crash with bookmark

* Fri Feb 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-8mdk
- Sync

* Thu Feb 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-7mdk
- Fix some bugs into quanta

* Fri Feb 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-6mdk
- Fix menu entry

* Fri Feb 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-5mdk
- Fix epoch

* Mon Feb 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-4mdk
- Sync with CVS
- Fix distlint
- Fix buildrequires kdelibs >=3.2-13mdk (pb kdedesktop2mdkmenu)

* Thu Feb 12 2004 David Baudens <baudens@mandrakesoft.com> 3.2-3mdk
- Fix menu

* Fri Feb 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-2mdk
- Sync with CVS
- Fix menu entry (icons/position)

* Tue Feb 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-1mdk
- 3.2

* Mon Feb 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-0.2mdk
- Sync with CVS

