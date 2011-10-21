%define effect_version 0.1
Summary:    Default Mandriva Linux screensaver for KDE
Name:       krozat
Version:    2008.1.6
Release:    %mkrel 8
Epoch:      2
License:    GPL
URL:        http://www.mandrivalinux.com/

# get the source from our cvs repository (see
# http://qa.mandriva.com/twiki/bin/view/Main/CvsGuide)
# no extra source or patch are allowed here.
Source:     krozat-%{version}.tar.bz2
Source1:    krozat-effect-%{effect_version}.tar.bz2
Patch0 :    krozat-printf.patch
Patch1:     krozat-trinity.patch

BuildRoot:      %_tmppath/%name-%version-%release-root
BuildRequires:  X11-devel
BuildRequires:  arts-devel
BuildRequires:  fam-devel
BuildRequires:  kdelibs-devel
BuildRequires:  libart_lgpl-devel
BuildRequires:  jpeg-devel
BuildRequires:  png-devel
BuildRequires:  qt3-devel
BuildRequires:  zlib-devel
BuildRequires:  intltool
# requires qt4 for the effect generation tool
BuildRequires:  qt4-devel

Summary:    Default Mandriva Linux screensaver for KDE
Group:      Graphical desktop/KDE3
Requires:   kdebase-progs
Requires:   mandriva-theme-screensaver

%description
This package contains the default Mandriva Linux screensaver for KDE.

%prep

%setup -q -a 1
%patch0 -p0
find . -type 'd' -name 'CVS' | xargs rm -fr
%patch1 -p0

%build
%configure_kde3

%make

pushd krozat-effect-%{effect_version}
   qmake
   make
popd

%install
rm -rf %buildroot

%makeinstall_std
%find_lang krozat

pushd krozat-effect-%{effect_version}
   mkdir -p %buildroot%_kde3_bindir
   cp krozat-effect %buildroot%_kde3_bindir
popd

%clean
rm -fr %buildroot

%files -f krozat.lang 
%defattr(-,root,root)
#
%_kde3_bindir/krozat.kss
%_kde3_bindir/krozat-effect
#
#
%dir %_kde3_datadir/applnk/System/
%dir %_kde3_datadir/applnk/System/ScreenSavers/
%_kde3_datadir/applnk/System/ScreenSavers/*.desktop


%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 2:2008.1.6-8mvt2010.2
+ Rebuild for Trinity

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 2:2008.1.6-7mvt2010.0
+ Rebuild for MDV 2010.1

* Sun Jan 17 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 2:2008.1.6-6mvt2010.0
+ Fix group in specfile

* Tue Nov 17 2009 Tim Williams <tim@my-place.org.uk> 2:2008.1.6-5mdv2010.0
+ Rebuild for MDV 2010.0

* Sat Nov 08 2008 Oden Eriksson <oeriksson@mandriva.com> 2:2008.1.6-4mdv2009.1
+ Revision: 301006
- rebuilt against new libxcb

* Tue Jun 17 2008 Thierry Vignaud <tvignaud@mandriva.com> 2:2008.1.6-3mdv2009.0
+ Revision: 221993
- rebuild

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 2:2008.1.6-2mdv2009.0
+ Revision: 204750
- Move to /opt

* Wed Mar 26 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:2008.1.6-1mdv2008.1
+ Revision: 190515
- New release fixing a string message in the config dialog (#38644)

* Tue Mar 11 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:2008.1.5-1mdv2008.1
+ Revision: 186866
- New release adding a fake desktop fading effect

* Wed Mar 05 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:2008.1.4-1mdv2008.1
+ Revision: 180184
- New release changing only the time the screensaver will wait on each image
  and the transition speed.

* Tue Mar 04 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:2008.1.3-1mdv2008.1
+ Revision: 178440
- New release enabling the setup option of the screensaver

* Tue Mar 04 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:2008.1.2-3mdv2008.1
+ Revision: 178432
- Add a effect generation tool to help users creating their own themes for the
  screensaver

* Thu Feb 28 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:2008.1.2-2mdv2008.1
+ Revision: 176403
- new release (2008.1.2) adding support for extra slideshow themes

* Mon Feb 18 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:2008.1.1-1mdv2008.1
+ Revision: 171922
- new release improving the crossfade effect

* Thu Feb 14 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:2008.1.0-1mdv2008.1
+ Revision: 167780
- new release adding the crossfade effect for the machines that are able to
  use it. For machines that don't have 2D acceleration, the screensaver will
  revert its behavior to the previous one.

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 2:2008.0.1-2mdv2008.1
+ Revision: 141740
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot
    - buildrequires X11-devel instead of XFree86-devel

* Wed Sep 26 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:2008.0.1-1mdv2008.0
+ Revision: 93139
- new release fixing image downscaling.

* Mon Sep 24 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:2008.0-1mdv2008.0
+ Revision: 92499
- New release including a fix from Neoclust for the desktop file

* Fri Sep 21 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:2008-1mdv2008.0
+ Revision: 92021
- new version fixing it for 2008.0
- spec cleanup

  + Anssi Hannula <anssi@mandriva.org>
    - Import krozat




* Sat Sep 16 2006 Laurent MONTEL <lmontel@mandriva.com> 2007-4
- Fix requires

* Fri Sep 15 2006 Laurent MONTEL <lmontel@mandriva.com> 2007-3
- Only show krozat in kde

* Wed May 10 2006 Laurent MONTEL <lmontel@mandriva.com> 2007-1mdk
- Rebuild to generate category

* Tue Aug 30 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-4mdk
- Fix other color

* Tue Aug 30 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-3mdk
- Adapt background color to distro

* Tue Aug 16 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-2mdk
- Rebuild

* Mon Aug 15 2005 Laurent MONTEL <lmontel@mandriva.com> 2006-1mdk
- Rebuild

* Wed Oct 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.1-3mdk
- Fix translation pb (bug found by Gwenole)

* Wed Oct 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.1-2mdk
- Updtae po

* Tue Aug 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.1-1mdk
- Update po file

* Mon Jun 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-7mdk
- Update version

* Mon Jun 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-6mdk
- Rebuild with new gcc
- Fix automake/autoconf
- use %%mdkversion

* Fri Feb 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-6mdk
- Update po file

* Fri Jan 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-5mdk
- Fix requires (found by vdanen)

* Thu Jan 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-4mdk
- Fix other mem leak

* Thu Jan 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-3mdk
- Rebuild
- update po file
- Fix make clean
- Fix mem leak

* Thu Dec 04 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-2mdk
- Translate po file

* Tue Dec 02 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 10.0-1mdk
- Add po file

* Tue Sep 02 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 9.1-4mdk
- Fix build

* Thu Jul 17 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 9.1-3mdk
- Rebuild

* Tue Dec 24 2002 Stefan van der Eijk <stefan@eijk.nu. 9.1-2mdk
- BuildRequires: libart_lgpl2-devel


* Tue Dec 17 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 9.1-1mdk
- 9.1

* Fri Oct 18 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 9.0-7mdk
- Rebuild

* Sat Aug 31 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 9.0-6mdk
- Fix about dialogbox

* Fri Aug 23 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 9.0-5mdk
- Fix MDK copyright.

* Wed Aug 14 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 9.0-4mdk
- Rebuild against new gcc-3.2

* Fri Aug  9 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 9.0-3mdk
- lib64 fixes, again. They were split to nihil when mandrake_desk was split

* Thu Aug  8 2002 Stefan van der Eijk <stefan@eijk.nu> 9.0-2mdk
- BuildRequires

* Fri Aug 02 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 9.0-1mdk
- Initial package
