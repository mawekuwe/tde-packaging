%define _requires_exceptions devel\(libdns_sd\(.*\)\\|devel\(libdns_sd\)

%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define lib_major 1
%define lib_name_orig libkdegames
%define lib_name %mklibname kde3-kdegames %{lib_major}
%define lib_oname %mklibname kdegames %{lib_major}
%define oname kdegames
%define rname kdegames3

Name:                   kde3-%{oname}
Summary:                KDE3 - Games
Version:                3.5.12
Release:                %mkrel 1
Epoch:                  1
Group:                  Graphical desktop/KDE3
License:                GPL
URL:                    http://www.kde.org
Source:                 %{oname}-%version.tar.bz2
Patch0:                 kdegames-3.5.8-add-support-avahi.patch
Patch1:                 kde-3.5.10-acinclude.patch
#Patch2:                 fix_autotools.patch
Patch3: 		kdebase-3.5.12-move-xdg-menu-dir.patch
Patch4: 		kdebase-3.5.12-config.patch

BuildRequires:          kde3-macros
BuildRequires:          X11-devel
BuildRequires:          freetype2-devel
BuildRequires:          kdelibs3-devel
BuildRequires:          alsa-lib-devel
BuildRequires:          arts3-devel
BuildRequires:          audiofile-devel
BuildRequires:          bzip2-devel
BuildRequires:          jpeg-devel
BuildRequires:          lcms-devel
BuildRequires:          mng-devel
BuildRequires:          png-devel
BuildRequires:          qt3-devel
BuildRequires:          libz-devel
%if %mdkversion < 201000
BuildRequires:          autoconf <= 1:2.63
BuildRequires:          automake >= 1.7
%else
BuildRequires:          autoconf >= 1:2.65
BuildRequires:          automake >= 1.11
%endif
BuildRequires:          qt3-doc
BuildRequires:          avahi-compat-libdns_sd-devel
BuildRequires:          mesaglu-devel
BuildRequires:          libx11-devel
%if %compile_apidox
BuildRequires:          doxygen
BuildRequires:          graphviz
%endif
Requires:               %{lib_name} = %epoch:%version-%release
Suggests:               %name-atlantik
Suggests:               %name-kasteroids
Suggests:               %name-katomic
Suggests:               %name-kbackgammon
Suggests:               %name-kbattleship
Suggests:               %name-kblackbox
Suggests:               %name-kbounce
Suggests:               %name-kenolaba
Suggests:               %name-kfouleggs
Suggests:               %name-kgoldrunner
Suggests:               %name-kjumpingcube
Suggests:               %name-klickety
Suggests:               %name-klines
Suggests:               %name-kmahjongg
Suggests:               %name-kmines
Suggests:               %name-knetwalk
Suggests:               %name-kolf
Suggests:               %name-konquest
Suggests:               %name-kpat
Suggests:               %name-kpoker
Suggests:               %name-kreversi
Suggests:               %name-ksame
Suggests:               %name-kshisen
Suggests:               %name-ksirtet
Suggests:               %name-ksmiletris
Suggests:               %name-ksnake
Suggests:               %name-ksokoban
Suggests:               %name-kspaceduel
Suggests:               %name-ktron
Suggests:               %name-ktuberling
Suggests:               %name-kwin4
Suggests:               %name-libs
Suggests:               %name-lskat
%if %mdkversion < 200900
Requires(post):         desktop-file-utils
Requires(postun):       desktop-file-utils
%endif
Obsoletes:              ktron < 1:3.5.9
Obsoletes:              kjumpingcube < 1:3.5.9
Provides:               %{oname} = %epoch:%version-%release
Obsoletes:              %{oname}
Provides:               %{rname} = %epoch:%version-%release
Obsoletes:              %{rname}
BuildRoot:              %_tmppath/%name-%version-%release-root

%description
Games for the K Desktop Environment.
This is a compilation of various games for KDE project
	- atlantik: Monopoly-like board games
	- kabalone: board game: move 6 pieces from your opponent over the edge
	- kasteroids: shoot at those nasty asteroids
	- katomic: build complex atoms with a minimal amount of moves
	- kbackgammon: play backgammon against a local human player, via a
               game server or against GNU Backgammon (not included)
	- kbattleship: battleship game with built-in game server
	- kblackbox: find atoms in a grid by shooting electrons
	- kfouleggs: a famous japanese game known as puyo-puyo
	- kbounce: claim areas and don't get disturbed
	- kjumpingcube: a tactical game for number-crunchers
	- klines: place 5 equal pieces together, but wait, there are 3 new ones
	- mahjongg: a tile laying patience
	- kmines: the classical mine sweeper
	- kolf: a golf game
	- konquest: conquer the planets of your enemy
	- kpat: several patience card games
	- kpoker: the game of poker
	- kreversi: the old reversi board game, also known as othello
	- ksame: collect pieces of the same color
	- kshisen: patience game where you take away all pieces
	- ksirtet: very known if spelt this backwards
	- ksmiletris: another Tetris-like game
	- ksnake: don't bite yourself, eat apples!
	- ksokoban: move all storage boxes into the cabinet
	- kspaceduel: two player game with shooting spaceships flying around a sun
	- ktron: like ksnake, but without fruits
	- ktuberling: kids game: make your own potato (NO french fries!)
	- kwin4: place 4 pieces in a row
	- libkdegames: KDE game library used by many of these programs
	- lskat: lieutnant skat
	- megami: blackjack card game

%if %mdkversion < 200900
%post
%update_menus
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor
%endif

%files 
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/*/*
%exclude %_kde3_docdir/HTML/en/kdegames-%version-apidocs
%attr(0755,root,root) %_kde3_bindir/*
%dir %_kde3_datadir/applications/kde/
%_kde3_datadir/applications/kde/*.desktop
%_kde3_appsdir/*/*
%dir %_kde3_datadir/mimelnk/application/
%_kde3_datadir/mimelnk/application/*.desktop
%dir %_kde3_datadir/services/
%_kde3_datadir/services/*.protocol
%dir %_kde3_datadir/config/magic
%_kde3_datadir/config/magic/*.magic
%_kde3_iconsdir/*/*/*/*
%dir %_kde3_datadir/config.kcfg/
%_kde3_datadir/config.kcfg/*.kcfg

#---------------------------------------------------------------------------

%package -n %lib_name-devel
Summary:	Headers files for kdegames
Group:		Development/KDE and Qt
Requires:	%lib_name = %epoch:%version-%release

Obsoletes:  kdegames3-devel < 1:3.5.9
Provides:   kde3-kdegames3-devel = %epoch:%version-%release

Obsoletes:  kdegames-devel < 1:3.5.9
Provides:   kde3-kdegames-devel = %epoch:%version-%release
Provides:   %lib_name_orig-devel = %epoch:%version-%release

%description -n %lib_name-devel
Headers files needed to build applications based on kdegames applications.

%files -n %lib_name-devel
%defattr(-,root,root,-)
%_kde3_includedir/*
%_kde3_libdir/*.so
%_kde3_libdir/*.la
%if %compile_apidox
%doc %_kde3_docdir/HTML/en/kdegames-%version-apidocs/*
%endif
%exclude %_kde3_libdir/libkdeinit_*.so

#---------------------------------------------------------------------------

%package -n %lib_name
Group:      System/Libraries
Summary:    Libraries for kdegame
Provides:   %lib_name_orig = %epoch:%version-%release
Conflicts:	kdegames <= 3.1-11mdk

%if %mdkversion < 200900
%post -n %lib_name -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name -p /sbin/ldconfig
%endif

%description -n %lib_name
Libraries for the K Desktop Environment.

%files -n %lib_name
%defattr(-,root,root,-)
%_kde3_libdir/*.la
%_kde3_libdir/*.so.*
%_kde3_libdir/libkdeinit_*.so
%_kde3_libdir/kde3/*

#---------------------------------------------------------------------------

%prep
%setup -q -n kdegames-%version
%patch0 -p0 -b .add_avahi_support
%patch3 -p0
%patch4 -p0

%build
PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/
export xdg_menudir=%_sysconfdir/xdg/kde/menus

make -f admin/Makefile.common cvs

%configure_kde3 \
    --with-extra-includes=/usr/include/avahi-compat-libdns_sd/:/opt/kde3/include/tqt \
    --with-extra-libs=/opt/kde3/lib
%make

%if %compile_apidox
make apidox
%endif


%install
rm -fr %buildroot

%makeinstall_std

%clean
rm -fr %buildroot






%changelog
* Thu Jul 21 2011 Tim Williams <tim@my-place.org.uk> 3.5.12-1mvt2010.2
+ Update to use Trinity sources
+ Add xdg dirs patch
+ Add kdebase-3.5.12-config.patch

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 3.5.10-6mvt2010.0
+ Rebuild for MDV 2010.1
+ Add patches from Atilla ÖNTAŞ <atilla_ontas@mandriva.org> branch (this 
  refused to work due to packaging errors, reverting to the original 
  packaging structure)
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65:patch4
+ Fix automake 1.11 issue:patch5
+ Rename package to avoid KDE4 conflicts

* Fri Nov 13 2009 Tim Williams <tim@my-place.org.uk> 1:3.5.10-3mdv2010.0
+ Rebuild for MDV 2010.0

* Thu Apr 02 2009 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-2mdv2009.1
+ Revision: 363578
- Bump release
- Pushing back kde3 kdegames :-/


* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-1mdv2009.0
+ Revision: 277475
- Update for last kde3 updates

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:3.5.9-7mdv2009.0
+ Revision: 267777
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 11 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.9-6mdv2009.0
+ Revision: 218010
- rebuild for new ldflags

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon May 19 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 1:3.5.9-5mdv2009.0
+ Revision: 209007
- User versioned obsoletes

* Wed May 07 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-4mdv2009.0
+ Revision: 202889
- Move for /opt

* Sat Mar 22 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-2mdv2008.1
+ Revision: 189493
- Fix groups ( tks to pterjan)

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-1mdv2008.1
+ Revision: 169010
- Get away from branches. Last KDE 3 arriving !!

* Wed Feb 13 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.8-5mdv2008.1
+ Revision: 167148
- Removing knetwalk doc files, cause it was added in the wrong place.

* Wed Feb 13 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.8-4mdv2008.1
+ Revision: 167134
- Adding pt_BR docbook

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 29 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.8-3mdv2008.1
+ Revision: 139068
- rebuild

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [FEATURE] Show kdegames in other WM than KDE ( Bug #35868)

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 28 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-1mdv2008.1
+ Revision: 102782
- Kde 3.5.8
  Rediff patches

* Fri Aug 10 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-3mdv2008.0
+ Revision: 61629
- Fix categories and add some OnlyShowIn

* Mon May 21 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-2mdv2008.0
+ Revision: 29259
- kdeinit libraries are modules, not development libraries. Moving for proper package

* Wed May 16 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-1mdv2008.0
+ Revision: 27454
- 3.5.7 release
- Removed old related icons to debian like menu


* Thu Feb 01 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-1mdv2007.0
+ Revision: 115845
- 3.5.6

* Thu Dec 21 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-5mdv2007.1
+ Revision: 100932
- Fix typo found by Blino
- Fix spec file

* Fri Nov 03 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-3mdv2007.1
+ Revision: 76072
- Rebuild

* Thu Oct 26 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-2mdv2007.1
+ Revision: 72785
- Rebuild
- 3.5.5
- New version (2006/08/03 3.5.4-1mdv)
- compile under x86_64
- Use macro
- 3.5.3
- Rebuild against new xorg
- Rebuild to generate category
- 3.5.2
- Fix build on mdk <=2006
- Fix spec file
  Fix avahi support
- kde3.5.1
- MDK9.2 is obsolete now
- Fix spec file (bug found by nicolas Chipaux)
- Add support for avahi
- Fix twice kgoldrunner bug found by Nicolas Chipaux
- Use avahi
- Fix spec file
- Real 3.5.0
- 3.5.0 (named rc1)
- Fix spec file
- 3.4.92
- Rebuild
- New sync to fix kmines program
  Clean spec file
  Use --libsuffix
- Forgot to increase version number
- Add diff
  Use %%mkrel
  Fix attribute
- Fix attribute of file
  TODO search why it's suid by default
- Fix group
- 3.4.2

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Helio Chissini de Castro <helio@mandriva.com>
    - We are Mandriva now
    - Increase release number
    - Fixed klickety bug http://qa.mandriva.com/show_bug.cgi?id=17295. No bindir files must be suid root.
    - Uploading package ./kdegames

* Tue May 17 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-6mdk
- Rebuild for missing package

* Sat May 07 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-5mdk
- Sync with CVS

* Fri May 06 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-4mdk
- Rebuild

* Mon Apr 18 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-3mdk
- Fix depend

* Sat Apr 16 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-2mdk
- Use --enable-new-ldflags 
- Reactivate debug
- Change email
- Reactivate -fvisibility same as for ppc

* Tue Apr 05 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0

* Mon Feb 21 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-8mdk
- Add patch4: fix kbounce kde bug #96841

* Fri Feb 18 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-7mdk
- Fix export

* Thu Feb 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-6mdk
- Disable debug

* Fri Jan 28 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-5mdk
- Add patch3: fix atlantik url

* Mon Jan 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-4mdk
- Disable visibility for ppc

* Tue Jan 11 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-3mdk
- Use -f visibility

* Thu Dec 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-2mdk
- Fix menu

* Tue Nov 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Mon Nov 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-6mdk
- Requires arts

* Thu Oct 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-5mdk
- Bye-bye %%buildfor

* Wed Oct 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-4mdk
- Sync with CVS

* Sat Oct 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-3mdk
- Fix spec file

* Tue Oct 12 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-2mdk
- Deprecated mdk < 9.2

* Sat Oct 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-1mdk
- 3.3.1

* Fri Sep 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-1mdk
- 3.3..0

* Sat Aug 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-9mdk
- Rebuild for new menu translation tabl

* Sat Aug 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-8mdk
- Remove debug

* Wed Aug 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-7mdk
- Fix spec file

* Thu Jul 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-5mdk
- Fix remove rpath

* Sat Jul 10 2004 Laurent Montel <lmontel@mandrakesoft.com> 3.2.3-4mdk
- generate doc

* Wed Jul 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-3mdk
- Rebuild with new kdelibs

* Wed Jun 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-2mdk
- Sync with CVS

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-4mdk
- Rebuild

* Wed Jun 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-3mdk
- rebuild with debug

* Fri May 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-2mdk
- Rebuild again qt 3.3.2

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-2mdk
- Fix spec file for using rpmbuildupdate

* Sat Apr 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

* Wed Mar 31 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-10mdk
- Use %%configure
- Use mdkversion

* Thu Mar 11 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-9mdk
- Fix bug #77170

* Fri Mar 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-8mdk
- Fix Group
- Fix epoch

* Mon Feb 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-7mdk
- Sync with CVS

* Mon Feb 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-6mdk
- Fix katomic bug

* Mon Feb 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-5mdk
- Rebuild with good kdedesktop2mdkmenu.pl

* Thu Feb 12 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-4mdk
- Sync with CVS

* Tue Feb 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-3mdk
- Sync with CVS

* Mon Feb 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-2mdk
- Fix pb into spec file (distint)

* Tue Feb 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-1mdk
- 3.2

* Mon Feb 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-0.2mdk
- Sync with CVS

