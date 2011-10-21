Name: task-kde3
Version: 3.5.12
Release: %mkrel 4
Summary: Metapackage for KDE
Group: Graphical desktop/KDE
License: GPL
Requires: %{name}-minimal
Requires: kde3-kdepim-kontact
Requires: kde3-kdeaddons-akregator
Requires: kdeutils-kwalletmanager
Requires: kdenetwork3-kopete
Requires: aspell
Requires: kdenetwork3-kget
Suggests: kde3-amarok
Suggests: kde3-kaffeine
Suggests: kde3-k3b
Suggests: kde3-konversation
Suggests: kde3-kdegraphics
Suggests: kde3-kdeaddons-metabar
Suggests: kde3-kdeaddons-kfile-plugins
Suggests: kde3-kdeaddons-kicker-applets
Suggests: kde3-kdeaddons-konqimagegallery
Suggests: kde3-kdeaddons-renamedlg
Suggests: kde3-kdeaddons-kaddressbook-plugins
Suggests: kde3-kdeaddons-knewsticker
Suggests: kde3-kdeaddons-atlantik
Suggests: kde3-kdeaddons-searchbar
Suggests: kde3-kdegraphics-ksvg
Suggests: kdeutils-kmilo
Suggests: kde-config-file 
Suggests: kdeutils-ark


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the K Desktop Environment.

%files
%defattr(-,root,root-)

#--------------------------------------------------------------------

%package devel
Summary: Metapackage for KDE development
Group: Development/KDE and Qt
Requires: kdelibs3-devel
Requires: libkde3core4-devel
Requires: libcups-devel
Requires: e2fsprogs-devel
Requires: libltdl-devel
Requires: libtiff-devel
Requires: libxml2-devel
Requires: libxslt-devel
Requires: taglib-devel
Requires: gcc-c++
Requires: automake
Requires: autoconf
Requires: gettext

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for installing a KDE development environment.

%files devel
%defattr(-,root,root-)

#--------------------------------------------------------------------

%package minimal
Summary: Metapackage for minimal KDE3
Group: Graphical desktop/KDE
Requires: arts3
Requires: kde3-kdebase-progs
Requires: kde3-style-ia-ora
Requires: kde3-kdebase-kmenuedit
Requires: krozat
Requires: xsettings-kde
Requires: kde3-kdebase-servicemenu
Requires: kde3-kdeaddons-konq-plugins
Requires: kde3-kdegraphics-common
Requires: kde3-kdebase-konsole
Requires: fonts-ttf-dejavu
Requires: fonts-ttf-liberation
Requires: kde3-kdebase-kdm
Suggests: kde3-kdebase-nsplugins
Suggests: preload
Suggests: readahead
Suggests: kde3-kdebase-kmenuedit
Suggests: task-pulseaudio
Suggests: kde3-kdemultimedia-kmix


%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running the K Desktop Environment.

%files minimal
%defattr(-,root,root-)

#--------------------------------------------------------------------

%package all
Summary: Metapackage for all KDE3
Group: Graphical desktop/KDE
Requires: %{name}-minimal
Requires: aspell
#Requires: kde3-gwenview
Requires: kde3-amarok
Requires: kde3-kdebase-kmenuedit
Requires: kde3-i18n-en_GB
Requires: kde3-i18n-de
Requires: kde3-i18n-fr
Requires: kde3-i18n-es
Requires: kde3-i18n-tr
Requires: kde3-k3b
Requires: kde3-kaffeine
Requires: kde3-kdegraphics
Requires: kde3-kdemultimedia
Requires: kde3-kdemultimedia
Requires: kdeutils
Requires: kdenetwork3
Requires: kde3-kdeaddons
Requires: kde3-kdepim
Requires: kde3-kdmtheme
Requires: kde3-kickoff-i18n
Requires: kde3-kio-sysinfo
Requires: kdeartwork
#Requires: kde-icons-tulliana
Suggests: kde3-amarok-engine-xine
Suggests: kde3-amarok-engine-yauap
#Suggests: kde3-digikam
Suggests: kde3-gtk-qt-engine
Suggests: kde3-kicker-backgrounds
Suggests: kde3-ktorrent
Suggests: kde3-mplayerthumbs
Suggests: kde3-servicemenu-mountiso
Suggests: kde3-servicemenu-rootactions
#Suggests: kde3-servicemenu-rpmxdgtool
#Suggests: kde3-style-domino
Suggests: kde3-style-ia-ora
#Suggests: kde3-style-metal4kde
Suggests: kde3-style-QtCurve
Suggests: kde3-style-serenity
#Suggests: kde3-yakuake
#Suggests: kde-icons-os-k
#Suggests: kde-icons-oxygen
#Suggests: kde-style-baghira
#Suggests: kde-style-lipstik
Suggests: kmetabar
#Suggests: kwinstyle-suse
#Suggests: kwin-style-powder
#Suggests: kwin-style-crystal
Suggests: ksmoothdock
#Suggests: kde3-gwenview-i18n
Suggests: kde3-kaffeine-engine-gstreamer
Suggests: kde3-kaffeine-engine-xine
Suggests: kde3-kdebase

%description all
This package is a meta-package, meaning that its purpose is to contain
all packages for running the K Desktop Environment.

%files all
%defattr(-,root,root-)


%changelog
* Tue Jul 26 2011 Tim Williams <tim@my-place.org.uk> 3.5.12-4mvt2010.2
- Fix devel dependencies again

* Tue Jul 26 2011 Tim Williams <tim@my-place.org.uk> 3.5.12-3mvt2010.2
+ Fix kde3-addons dependency in all package
- Remove dependencies from all package: gwenview, digikam, kde-icons-tulliana, kde3-style-domino, kde3-style-kde4metal
  kde3-servicemenu-rpmxdgtool, kwinstyle-suse, kwinstyle-powder, kwin-style-crystal, kde3-yakuake
  kde-icons-os-k, kde-icons-oxygen, dde-style-baghira, kde-style-lipstik

* Wed Jul 21 2011 Tim Williams <tim@my-place.org.uk> 3.5.12-1mvt2010.2
+ Fix depency issue in devel

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 3.5.12-1mvt2010.2
+ Rebuild for Trinity KDE 3.5.12

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 3.5.10-10mvt2010.0
+ Rebuild for MDV 2010.1

* Sat Jan 02 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 3.5.10-9mvt2010.0
+ Added task-kde3-all package

* Tue Nov 17 2009 Tim Williams <tim@my-place.org.uk> 3.5.10-8mdv2010.0
+ Rebuild for MDV 2010.0
+ Change kdepim3-kontact dependency to kde3-kdepim-kontact
+ Remove konversation
+ kdegames now kdegames3
- Remove mandriva-galaxy dependency

* Wed Apr 22 2009 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.10-4mdv2009.1
+ Revision: 368611
- Fix Requires

* Wed Apr 01 2009 Helio Chissini de Castro <helio@mandriva.com> 3.5.10-3mdv2009.1
+ Revision: 363358
- Solve dependencies

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Fix Require for new arts package name

* Mon Sep 29 2008 Frederic Crozat <fcrozat@mandriva.com> 3.5.10-2mdv2009.0
+ Revision: 289370
- Add readahead as suggests

* Thu Sep 25 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.10-1mdv2009.0
+ Revision: 288170
- Suggests preload

* Sat Sep 20 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.9-10mdv2009.0
+ Revision: 286171
- Add ark and kmix as Suggests (Bug #41877 #41876)

* Fri Jul 18 2008 Olivier Blin <oblin@mandriva.com> 3.5.9-9mdv2009.0
+ Revision: 238157
- do not suggest digikam anymore, it is a kde4 application

* Mon Jun 02 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 3.5.9-7mdv2009.0
+ Revision: 214312
- Changed kde3-kdeaddons-metabar from Required to Suggested package.

* Mon May 19 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.9-6mdv2009.0
+ Revision: 209222
- Fix package name
- Fix Spec file name
- Order spec file sections
  Fix Requires
- Add obsoletes
- Fix some Requires
- Rename to show which kde it is

* Thu Apr 03 2008 Anne Nicolas <anne.nicolas@mandriva.com> 3.5.9-5mdv2008.1
+ Revision: 192170
- Add kde-config-file suggest to fix #39724 (neoclust)

* Wed Mar 26 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 3.5.9-4mdv2008.1
+ Revision: 190372
- Requires gcc-c++, not gcc-g++

* Sat Mar 15 2008 Olivier Blin <oblin@mandriva.com> 3.5.9-3mdv2008.1
+ Revision: 188069
- only suggest konversation so that it can be skipped in One
  (kopete is already required)

* Wed Mar 05 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.9-2mdv2008.1
+ Revision: 179452
- Add task-pulseaudio as Suggests
- New version 3.5.9

* Sun Jan 27 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.8-1mdv2008.1
+ Revision: 158801
- Suggest kmilo
- [BUGFIX] Add missing requires on task-kde-devel (Bug #35101)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 17 2007 Pixel <pixel@mandriva.com> 3.5.7-12mdv2008.1
+ Revision: 121622
- rebuild for new "Suggests" rpm format

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [FEATURE] Add kdegraphics-ksvg as Suggest (Bug #35321)

* Fri Oct 05 2007 Anne Nicolas <anne.nicolas@mandriva.com> 3.5.7-11mdv2008.0
+ Revision: 95548
- add mandriva-galaxy

* Thu Oct 04 2007 Anne Nicolas <anne.nicolas@mandriva.com> 3.5.7-10mdv2008.0
+ Revision: 95317
- fix suggests

* Fri Sep 28 2007 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.7-9mdv2008.0
+ Revision: 93620
- Add kdenetwork-kget as Require

* Fri Sep 21 2007 Adam Williamson <awilliamson@mandriva.org> 3.5.7-8mdv2008.0
+ Revision: 92068
- okay, require krozat again, since boiko fixed it, and for safety

* Fri Sep 21 2007 Adam Williamson <awilliamson@mandriva.org> 3.5.7-7mdv2008.0
+ Revision: 91999
- don't require krozat

* Wed Sep 19 2007 Olivier Blin <oblin@mandriva.com> 3.5.7-6mdv2008.0
+ Revision: 90814
- suggest kerry instead of requiring it (so that it can be skipped on live systems)

* Fri Sep 14 2007 Helio Chissini de Castro <helio@mandriva.com> 3.5.7-5mdv2008.0
+ Revision: 85689
- Suggests kaffeine instead of kmplayer

* Thu Aug 30 2007 Helio Chissini de Castro <helio@mandriva.com> 3.5.7-4mdv2008.0
+ Revision: 76262
- Added konversation, kopete and standard fonts
- Update task kde for new kde3-kdeaddons
- Update to add konsole as default
- Remove Mandriva galaxy as standard install

  + Anssi Hannula <anssi@mandriva.org>
    - add dependency on aspell, moved from kdelibs-common

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - New KDE version 3.5.7

