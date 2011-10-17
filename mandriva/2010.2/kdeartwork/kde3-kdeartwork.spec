%define oname kdeartwork

Name: kde3-%{oname}
Version: 3.5.12
Release: %mkrel 1
Group: Graphical desktop/KDE3
Summary: Kdeartwork
URL: http://www.kde.org
License: GPL
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
Patch1:	kdeartwork-3.5.4-fix-screensaver-only-showin-kde.patch
Patch2:	kdeartwork-3.5.5-fix-default-inherits-theme.patch
#Patch3:	kdeartwork-3.5.6-fix-screensaver-nodisplay.patch
Patch4: kde-3.5.10-acinclude.patch
#Patch5: fix_autotools.patch

BuildRoot: %_tmppath/%name-%version-%release-root

BuildRequires: kde3-macros
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%endif
BuildRequires: autoconf >= 1:2.65
BuildRequires: automake > 1.5
BuildRequires: X11-devel 
BuildRequires: freetype2-devel
BuildRequires: kdebase3-devel 
BuildRequires: kdelibs-devel >= 3.2-13mdk 
BuildRequires: bzip2-devel 
BuildRequires: libintl 
BuildRequires: jpeg-devel 
BuildRequires: lcms-devel 
BuildRequires: mng-devel
BuildRequires: png-devel 
BuildRequires: qt3-devel
BuildRequires: libz-devel 
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-gl
BuildRequires: mesaglut-devel
BuildRequires: mesaglu-devel
BuildRequires: GL-devel
Requires: kdebase-progs >= 1:3.2
Requires: kdeartwork-screensavers
Provides: kdeartwork3 = %version-%release
Provides: %{oname} = %version-%release
Provides: kde-style-phase 
Provides: kde-theme-phase
Provides: kwin-style-smoothblend
Obsoletes: kdemoreartwork-plastik < 3.5.3
Obsoletes: kde-style-phase kde-theme-phase
Obsoletes: kwin-style-smoothblend
Obsoletes: kdeartwork3
Obsoletes: %{oname}
Conflicts: kdebase <= 2.2.2-93mdk
Conflicts: libkdebase4 <= 1:3.4.2-56mdk 
Conflicts: kdebase-common <= 1:3.4.2-56mdk

%description
Additional artwork (themes, sound themes, icons,etc...) for KDE.

%files
%defattr(-,root,root,-)
%_kde3_libdir/kde3/*
%_kde3_appsdir/kstyle
%_kde3_appsdir/kwin
%_kde3_appsdir/kworldclock
%_kde3_datadir/emoticons/*
%_kde3_datadir/wallpapers/*
%_kde3_datadir/sounds/*

#-------------------------------------------------------------------------

%package icons-theme-kdeclassic
Summary:  Default Icons from kde3.0 
Group: Graphical desktop/KDE3
Obsoletes: kdeartwork-kde-classic
Provides: %{oname}-icons-theme-kdeclassic = %version-%release
Obsoletes: %{oname}-icons-theme-kdeclassic

%description icons-theme-kdeclassic
Default Icons from kde3.0.

%files icons-theme-kdeclassic
%defattr(-,root,root,-)
%dir %_kde3_iconsdir/kdeclassic/
%_kde3_iconsdir/kdeclassic/*

#-------------------------------------------------------------------------

%package icons-theme-Locolor
Summary:  Default Icons from kde3.0 
Group: Graphical desktop/KDE3
Provides: %{oname}-icons-theme-Locolor = %version-%release
Obsoletes: %{oname}-icons-theme-Locolor

%description icons-theme-Locolor
Locolor icons theme

%files icons-theme-Locolor
%defattr(-,root,root,-)
%dir %_kde3_iconsdir/Locolor/
%_kde3_iconsdir/Locolor/*

#-------------------------------------------------------------------------

%package icons-theme-ikons
Summary:  Default Icons from kde3.0 
Group: Graphical desktop/KDE3
Provides: %{oname}-icons-theme-ikons = %version-%release
Obsoletes: %{oname}-icons-theme-ikons

%description icons-theme-ikons
ikons icons theme

%files icons-theme-ikons
%defattr(-,root,root,-)
%dir %_kde3_iconsdir/ikons/
%_kde3_iconsdir/ikons/*

#-------------------------------------------------------------------------

%package icons-theme-kids
Summary:  Default Icons from kde3.0 
Group: Graphical desktop/KDE3
Provides: %{oname}-icons-theme-kids = %version-%release
Obsoletes: %{oname}-icons-theme-kids

%description icons-theme-kids
kids icons theme

%files icons-theme-kids
%defattr(-,root,root,-)
%dir %_kde3_iconsdir/kids/
%_kde3_iconsdir/kids/*

#-------------------------------------------------------------------------

%package icons-theme-slick
Summary:  Default Icons from kde3.0 
Group: Graphical desktop/KDE3
Provides: %{oname}-icons-theme-slick = %version-%release
Obsoletes: %{oname}-icons-theme-slick

%description icons-theme-slick
Slick icons theme

%files icons-theme-slick
%defattr(-,root,root,-)
%dir %_kde3_iconsdir/slick/
%_kde3_iconsdir/slick/*

#-------------------------------------------------------------------------

%package screensavers
Summary: Screensaver using OpenGL 
Group: Graphical desktop/KDE3
Requires: kdebase-progs >= 3.2
Obsoletes: kdeartwork <= 3.5.7-%mkrel 2
Provides: %{oname}-screensavers = %version-%release
Obsoletes: %{oname}-screensavers

%description screensavers
Screensaver using OpenGL.

%files screensavers -f savers.files
%defattr(-,root,root,-)
%_kde3_appsdir/kfiresaver
%_kde3_appsdir/kscreensaver

#-------------------------------------------------------------------------

%package screensavers-gl
Summary: Screensaver using OpenGL 
Group: Graphical desktop/KDE3
Requires: kdebase-progs >= 3.2
Requires: %name-screensavers
Requires: xscreensaver-gl
Obsoletes: kdeartwork <= 3.5.7-%mkrel 2
Obsoletes: kdeartwork-screensaver-gl
Provides: %{oname}-screensavers-gl = %version-%release
Obsoletes: %{oname}-screensavers-gl

%description screensavers-gl
Screensaver using OpenGL.

%files screensavers-gl -f glsavers.files
%defattr(-,root,root,-)

#-------------------------------------------------------------------------

%prep
%setup  -q -n %{oname}-%{version}
%patch1 -p1 -b .fix_screensaver_onlyshowinkde
%patch2 -p1 -b .fix_inherit_theme
#%patch3 -p1 -b .fix_screensaver_nodisplay
%if %mdkversion >= 201000
%patch4 -p1
#%patch5 -p1
%endif

%build
make -f admin/Makefile.common cvs

PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/

%configure_kde3

%make


%install
rm -fr %buildroot

make install DESTDIR=%buildroot

install -d %buildroot/%_menudir/

export PATH=%_kde3_bindir:$PATH

# Legal issues ?
rm -f %buildroot/%_kde3_bindir/kmatrix.kss
rm -f %buildroot/%_kde3_datadir/applnk/System/ScreenSavers/KMatrix.desktop
rm -f %buildroot/%_kde3_datadir/applnk/System/ScreenSavers/glmatrix.desktop
rm -f %buildroot/%_kde3_datadir/applnk/System/ScreenSavers/xmatrix.desktop

# Screensaver list
rm -f glsavers.files savers.files
for name in `find %buildroot -type f |grep ScreenSaver`; do
     if grep -qs "Type=OpenGL" $name; then 
        echo $name | sed -e "s,%buildroot%_kde3_datadir,%_kde3_datadir,g" >> glsavers.files
        if ! grep -qs "TryExec=xscreensaver" $name; then
            grep Exec= $name | grep -v TryExec | head -1 | sed -e "s,Exec=,%_kde3_bindir/,g" -e "s, .*,,g" >> glsavers.files
        fi
     else
        echo $name | sed -e "s,%buildroot%_kde3_datadir,%_kde3_datadir,g" >> savers.files
        if ! grep -qs "TryExec=xscreensaver" $name; then
            if ! grep -qs "fiberlamp" $name; then
            grep Exec= $name | grep -v TryExec | head -1 | sed -e "s,Exec=,%_kde3_bindir/,g" -e "s, .*,,g" >> savers.files
            fi
        fi
    fi 
done

%clean
rm -fr %buildroot



%changelog

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 3.5.12-1mvf2010.2
+ Rebuild for MDV 2010.2/Trinity
+ Added KDE/Trinity 3.5.12 sources
- Remove fix_autotools.patch, kdeartwork-3.5.6-fix-screensaver-nodisplay.patch

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 3.5.10-4mvt2010.1
+ Rebuild for MDV 2010.1

* Sun Jan 17 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 3.5.10-3mvt2010.0
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65:patch4
+ Fix automake 1.11 issue:patch5
+ Rename package to avoid KDE4 conflicts

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 3.5.10-1mdv2010.0
+ Add kde 3.5.10 sources package
+ Fix kdeartwork-3.5.4-fix-screensaver-only-showin-kde.patch
+ Fix kdeartwork-3.5.6-fix-screensaver-nodisplay.patch

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.5.9-6mdv2009.0
+ Revision: 267768
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 11 2008 Funda Wang <fundawang@mandriva.org> 3.5.9-5mdv2009.0
+ Revision: 217839
- rebuid for new rpm binary payload

* Sun Jun 08 2008 Funda Wang <fundawang@mandriva.org> 3.5.9-4mdv2009.0
+ Revision: 216918
- rebuild for new ldflags

* Wed May 07 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.9-3mdv2009.0
+ Revision: 203697
- Move to /opt

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Rebuild for backports

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.9-1mdv2008.1
+ Revision: 169159
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches integrated

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-not-capitalized

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 31 2007 Oden Eriksson <oeriksson@mandriva.com> 3.5.8-2mdv2008.1
+ Revision: 139862
- rebuilt against openldap-2.4.7 libs

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add usptream 3.5.9 branch patches
      	- Be more random with the slideshow screensaver.
      	- Handle properly display height/width ratio.

* Sun Oct 28 2007 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.8-1mdv2008.1
+ Revision: 102776
- Kde 3.5.8

* Sat Jun 09 2007 Helio Chissini de Castro <helio@mandriva.com> 3.5.7-3mdv2008.0
+ Revision: 37629
- Split packages
- Remove broken changelog on spec
- Separate screensaver and icon packages properly

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add a Obsoletes for kwin-style-smoothblend (bug #25452)

* Wed May 16 2007 Helio Chissini de Castro <helio@mandriva.com> 3.5.7-1mdv2008.0
+ Revision: 27459
- 3.5.7 release


* Sat Mar 31 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-2mdv2007.1
+ Revision: 149988
- don't display screensaver
- 3.5.6
- Use iconsdir macro
- Fix inherite theme

* Wed Oct 18 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-1mdv2007.1
+ Revision: 65948
- 3.5.5

* Sat Sep 16 2006 Laurent Montel <lmontel@mandriva.com> 3.5.4-3mdv2007.0
+ Revision: 61557
- New package(2006-09-15 3mdv)
  Fix only show screensaver into kde

* Fri Sep 01 2006 Laurent Montel <lmontel@mandriva.com> 3.5.4-2mdv2007.0
+ Revision: 58952
- Fix upgrade
- New package (2006/08/04 3.5.4-1mdv)
- don't requires on metapackage
- Fix compile on mdk2006
- 3.5.3
- Rebuild against new xorg
- Rebuild to generate category
- Fix spec file
- 3.5.2
- Fix spec file
- Fix spec file
- 3.5.1
- Enable debug for cooker
  MDK9.2 is obsolete now
- Fix conflict with mdk2006
- Fix compile on mdk <2006
- Fix file list for mdk 2006
- Fix spec file
- real 3.5.0
- 3.5.0
- Rebuild with new qt3.3.5
- Add conflict with kdebase
- 3.4.92
- Fix build on x86_64
- Rebuild
- Obsolete/provides kde-style-phase kde-theme-phase
  Patch from neoclust
- 3.4.2

  + Helio Chissini de Castro <helio@mandriva.com>
    - Cleaned spec
    - Added tarball from kde branch as discussed on meeting in 28/06
    - Removed rpath and added configure macro invalidating libtoolize
    - We are Mandriva now
    - Uploading package ./kdeartwork

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 05 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-4mdk
- Rebuild

* Wed Apr 20 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-3mdk
- Add BuildREquires on xscreensaver-gl (reported by Arnaud de Lorbeau )

* Sat Apr 16 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-2mdk
- Change email
- Activate debug
- Active -fvisibility same as for ppc
- Use --enable-new-ldflags

* Thu Apr 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0

* Mon Mar 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-14mdk
- Rebuild

* Mon Feb 28 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-13mdk
- Add patch10: fix other plastik ininitialise variable

* Fri Feb 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-12mdk
- Add patch9: fix plastik initial variable

* Thu Feb 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-11mdk
- Disable debug

* Thu Jan 27 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-10mdk
- Fix screensaver (use directly screensaver into applnk, it's hidden by default and it fixed all bug with new xdg menu (for screensaver))

* Mon Jan 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-9mdk
- Fix plastik kde bug #97681
- Don't use -fvisibility for ppc

* Sat Jan 15 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-8mdk
- Add patch7: allow to disable visibility

* Sat Jan 15 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-7mdk
- Add patch6: fix plastik kde bug #73873

* Mon Jan 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-6mdk
- Now plastik style

* Mon Jan 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-5mdk
- Fix other kde_export

* Sat Jan 08 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-4mdk
- Fix export into plastik style

* Fri Jan 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-3mdk
- Use -fvisibility

* Wed Dec 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-2mdk
- Fix menu

* Thu Dec 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Thu Oct 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-3mdk
- Bye-bye %%buildfor

* Wed Oct 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-2mdk
- Deprecated mdk < 9.2

* Sat Oct 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-1mdk
- 3.3.1

* Sat Oct 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-5mdk
- Sync with CVS

* Fri Oct 01 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-4mdk
- Fix menu entry

* Sat Sep 11 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-3mdk
- Remove dependance on xscreensaver

* Thu Sep 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-2mdk
- Sync with CVS

* Fri Sep 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-1mdk
- 3.3.0

* Wed Sep 01 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-10mdk
- Add patch7: fix kde bug #83406 "kslideshow screensaver does not start nor
					configure when images directory does not exist anymore"

* Fri Aug 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-9mdk
- Remove explicite requires just for icons

* Tue Aug 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-8mdk
- Disable debug

* Thu Aug 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-7mdk
- Add patch6: fix kde1 style kde bug #73592

* Fri Jul 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-6mdk
- fix spec file

* Thu Jul 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-5mdk
- Remove rpath

* Thu Jul 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-4mdk
- Create package for opengl screensaver

* Wed Jul 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-3mdk
- Rebuild with new kdedesktop2mdkmenu.pl

* Tue Jul 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-2mdk
- Create screensaver from xscreensaver

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Sat Jun 05 2004 Montel Laurent <lmontel@mandrakesoft.com> 3.2.2-5mdk
- Rebuild

* Wed Jun 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-4mdk
- Rebuild with debug

* Fri May 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-3mdk
- Rebuild against qt 3.3.2

* Thu Apr 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-2mdk
- Fix twice 64x64 directory bug reported by Pascal BILLERY-SCHNEIDER <pascal.billery-schneider@bluewin.ch>

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-2mdk
- Fix spec file to using rpmbuildupdate

* Sat Apr 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

