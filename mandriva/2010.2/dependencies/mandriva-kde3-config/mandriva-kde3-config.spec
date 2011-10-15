%define epoch_kdelibs 30000000
%define oname mandriva-kde-config

Name: mandriva-kde3-config
Summary: Mandriva KDE configuration
Version: 2010.2
Release: %mkrel 1
URL: http://www.mandriva.com
Group: Graphical desktop/KDE3
BuildRoot: %_tmppath/%name-buildroot
BuildRequires: kde3-macros
Source0: %{oname}-%{version}.tar.bz2
# OpenOffice.org icons. Should be in a separate package
# in the future, since they're shared between kde, OOo
# and maybe others
Source1: ooo-icons.tar.bz2
Source2: opendocument-mime.tar.bz2
Patch0: fix_kdmtheme.patch
License: GPL
BuildArch: noarch
Obsoletes: %{name} < %version-%release
Obsoletes: mandriva-kde-config
Provides: mandriva-kde-config = %version-%release


%description
This package regroups all specific Mandriva config file for KDE.
(kicker config etc.)

#--------------------------------------------------------------------

%package common
Group: Graphical desktop/KDE3
Summary: Common configs used for Mandriva theme
Requires(pre): update-alternatives
Requires: urw-fonts
Obsoletes: %{name}-common < %version-%release
Obsoletes: mandriva-kde-config-common
Provides: mandriva-kde-config-common = %version-%release

%description common
common configs used for Mandriva theme

%post common
update-alternatives --install /etc/kderc kde-config %_localstatedir/lib/mandriva/kde-profiles/common/upstream-kde-config 9

%postun common
if ! [ -e /var/lib/mandriva/kde-profiles/common/upstream-kde-config ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/common/upstream-kde-config
fi

%files common
%defattr(0644,root,root,755)
%dir %_localstatedir/lib/mandriva/
%dir %_localstatedir/lib/mandriva/kde-profiles/common
%_localstatedir/lib/mandriva/kde-profiles/common/*

#--------------------------------------------------------------------

%package -n powerpack-kde3-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE3
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: desktop-common-data
Requires(pre): mandriva-kde-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Obsoletes: powerpackplus-kde-config < 2008.0 
Provides: powerpack-kde-config = %version-%release
Provides: powerpackplus-kde-config = %version-%release
Obsoletes: powerpack-kde-config
Requires(preun): mandriva-kde3-config-common
Obsoletes: powerpack-kde3-config < %version-%release

%pre -n powerpack-kde3-config
if [ "$1" = "2" ]; then
	[ ! -h %_sysconfdir/kderc ] && rm -f %_sysconfdir/kderc ]
fi
if [ -d %_localstatedir/lib/mandriva/kde-profiles/powerpack/share/apps/kdesktop/Desktop ]; then
  rm -rf %_localstatedir/lib/mandriva/kde-profiles/powerpack/share/apps/kdesktop/Desktop
fi

%post -n powerpack-kde3-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/lib/mandriva/kde-profiles/powerpack/kderc 10

%postun -n powerpack-kde3-config
if ! [ -e /var/lib/mandriva/kde-profiles/powerpack/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/powerpack/kderc
fi

%description -n powerpack-kde3-config
This package regroups all specific Mandriva config file for KDE.

%files -n powerpack-kde3-config
%defattr(0644,root,root,755)
%dir %_localstatedir/lib/mandriva/kde-profiles/powerpack
%_localstatedir/lib/mandriva/kde-profiles/powerpack/*

#--------------------------------------------------------------------

%package -n one-kde3-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE3
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: desktop-common-data
Requires(pre): mandriva-kde3-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Provides: one-kde-config = %version-%release
Obsoletes: one-kde-config
Requires(preun): mandriva-kde3-config-common
Obsoletes: one-kde3-config < %version-%release

%description -n one-kde3-config
This package regroups all specific Mandriva config file for KDE.

%pre -n one-kde3-config
if [ "$1" = "2" ]; then
	[ ! -h %_sysconfdir/kderc ] && rm -f %_sysconfdir/kderc ]
fi
if [ -d %_localstatedir/lib/mandriva/kde-profiles/one/share/apps/kdesktop/Desktop ]; then
  rm -rf %_localstatedir/lib/mandriva/kde-profiles/one/share/apps/kdesktop/Desktop
fi

%post -n one-kde3-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/lib/mandriva/kde-profiles/one/kderc 10

%postun -n one-kde3-config
if ! [ -e /var/lib/mandriva/kde-profiles/one/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/one/kderc
fi

%files -n one-kde3-config
%defattr(0644,root,root,755)
%dir %_localstatedir/lib/mandriva/kde-profiles/one
%_localstatedir/lib/mandriva/kde-profiles/one/*


#--------------------------------------------------------------------

%package -n flash-kde3-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE3
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: desktop-common-data
Requires(pre): mandriva-kde3-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Provides: flash-kde-config = %version-%release
Obsoletes: flash-kde-config
Requires(preun): mandriva-kde3-config-common
Obsoletes: flash-kde3-config < %version-%release

%description -n flash-kde3-config
This package regroups all specific Mandriva config file for KDE.

%pre -n flash-kde3-config
if [ "$1" = "2" ]; then
	[ ! -h %_sysconfdir/kderc ] && rm -f %_sysconfdir/kderc ]
fi
if [ -d %_localstatedir/lib/mandriva/kde-profiles/flash/share/apps/kdesktop/Desktop ]; then
  rm -rf %_localstatedir/lib/mandriva/kde-profiles/flash/share/apps/kdesktop/Desktop
fi

%post -n flash-kde3-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/lib/mandriva/kde-profiles/flash/kderc 10

%postun -n flash-kde3-config
if ! [ -e /var/lib/mandriva/kde-profiles/flash/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/flash/kderc
fi

%files -n flash-kde3-config
%defattr(0644,root,root,755)
%dir %_localstatedir/lib/mandriva/kde-profiles/flash
%_localstatedir/lib/mandriva/kde-profiles/flash/*


#--------------------------------------------------------------------

%package -n free-kde3-config
Summary: Mandriva KDE configuration 
Group: Graphical desktop/KDE3
Provides: kde-config-file = %version-%release
Requires: mandriva-theme
Requires: qt4-style-iaora
Requires: desktop-common-data
Requires(pre): mandriva-kde3-config-common = %version-%release
Conflicts: kdelibs-common < %epoch_kdelibs:3.5.1
Conflicts: kdebase-common < 1:3.5.2-10.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Requires(preun): mandriva-kde3-config-common
Obsoletes: download-kde-config-2007 < 2008.0 
Provides:	download-kde-config-2007
Obsoletes: discovery-kde-config < 2008.0
Provides: discovery-kde-config = %version-%release
Provides: free-kde-config = %version-%release
Obsoletes: free-kde-config
Obsoletes: free-kde3-config < %version-%release

%description -n free-kde3-config
This package regroups all specific Mandriva config file for KDE.

%pre -n free-kde3-config
if [ "$1" = "2" ]; then
	[ ! -h %_sysconfdir/kderc ] && rm -f %_sysconfdir/kderc ]
fi
if [ -d %_localstatedir/lib/mandriva/kde-profiles/free/share/apps/kdesktop/Desktop ]; then
  rm -rf %_localstatedir/lib/mandriva/kde-profiles/free/share/apps/kdesktop/Desktop
fi

%post -n free-kde3-config
update-alternatives --install /etc/kderc kde-config %_localstatedir/lib/mandriva/kde-profiles/free/kderc 10

%postun -n free-kde3-config
if ! [ -e /var/lib/mandriva/kde-profiles/free/kderc ]; then
  update-alternatives --remove kde-config /var/lib/mandriva/kde-profiles/free/kderc
fi

%files -n free-kde3-config
%defattr(0644,root,root,755)
%dir %_localstatedir/lib/mandriva/kde-profiles/free
%_localstatedir/lib/mandriva/kde-profiles/free/*


#--------------------------------------------------------------------
# KDM

%package -n mandriva-kdm3-config
Summary: Mandriva KDM config file
Group: Graphical desktop/KDE3
Obsoletes: kdebase-kdm-config-file < 2008.0
Provides: kdm-config-file = %version-%release
# For upgrade 
Provides: kdebase-kdm-config-file = 2:%version 
Conflicts: kdebase-progs <= 3.5.1-15.1.20060mdk
Obsoletes: mandriva-kde-config-file < 2008.0
Requires(post): perl-MDK-Common
Obsoletes: mandriva-kdm-config
Provides: mandriva-kdm-config = %version-%release


%description -n mandriva-kdm3-config
Mandriva KDM config file

%trigger -n mandriva-kdm3-config -- kdebase-kdm-config-file 
perl -MMDK::Common -e 'update_gnomekderc("%{_kde3_configdir}/kdm/kdmrc", "General", "ConsoleTTYs", "tty1,tty2,tty3,tty4,tty5,tty6", "ServerVTs", "-7")'

%files -n mandriva-kdm3-config
%defattr(0644,root,root,0755)
%config(noreplace) %_kde3_configdir/kdm/backgroundrc
%config(noreplace) %_kde3_configdir/kdm/kdmrc
%_kde3_configdir/kdm/themes

#---------------------------------------

%prep
%setup -q -n %{oname}-%{version} -a 1 -a 2
%patch0 -p1

%install
rm -rf %buildroot
# Create profile dirs
mkdir -p %buildroot/%{_kde3_configdir}
mkdir -p %buildroot/%_localstatedir/lib/mandriva

mv kde-profiles %buildroot/%_localstatedir/lib/mandriva
mv kdm %buildroot/%{_kde3_configdir}

# openoffice icons, see #26311
mkdir -p %buildroot/%_localstatedir/lib/mandriva/kde-profiles/common/share/icons/
cp -a ooo-icons/hicolor %buildroot/%_localstatedir/lib/mandriva/kde-profiles/common/share/icons/

# openoffice mimetypes, see #26311
mkdir -p %buildroot/%_localstatedir/lib/mandriva/kde-profiles/common/share/mimelnk/application
cp -a opendocument-mime/* %buildroot/%_localstatedir/lib/mandriva/kde-profiles/common/share/mimelnk/application
# XXX we have to rename them to the same name provided by kdelibs-common, otherwise the
# global ones are used.
pushd %buildroot/%_localstatedir/lib/mandriva/kde-profiles/common/share/mimelnk/application
    mv openoffice.org2.4-oasis-drawing.desktop vnd.oasis.opendocument.graphics.desktop
    mv openoffice.org2.4-oasis-drawing-template.desktop vnd.oasis.opendocument.graphics-template.desktop
    mv openoffice.org2.4-oasis-master-document.desktop vnd.oasis.opendocument.text-master.desktop
    mv openoffice.org2.4-oasis-formula.desktop vnd.oasis.opendocument.formula.desktop
    mv openoffice.org2.4-oasis-spreadsheet.desktop vnd.oasis.opendocument.spreadsheet.desktop
    mv openoffice.org2.4-oasis-spreadsheet-template.desktop vnd.oasis.opendocument.spreadsheet-template.desktop
    mv openoffice.org2.4-oasis-text.desktop vnd.oasis.opendocument.text.desktop
    mv openoffice.org2.4-oasis-text-template.desktop vnd.oasis.opendocument.text-template.desktop
    mv openoffice.org2.4-oasis-web-template.desktop vnd.oasis.opendocument.text-web.desktop
    mv openoffice.org2.4-oasis-presentation.desktop vnd.oasis.opendocument.presentation.desktop
    mv openoffice.org2.4-oasis-presentation-template.desktop vnd.oasis.opendocument.presentation-template.desktop
    mv openoffice.org2.4-spreadsheet.desktop vnd.sun.xml.calc.desktop
    mv openoffice.org2.4-spreadsheet-template.desktop vnd.sun.xml.calc.template.desktop
    mv openoffice.org2.4-presentation.desktop vnd.sun.xml.impress.desktop
    mv openoffice.org2.4-presentation-template.desktop vnd.sun.xml.impress.template.desktop
    mv openoffice.org2.4-drawing.desktop  vnd.sun.xml.draw.desktop
    mv openoffice.org2.4-drawing-template.desktop vnd.sun.xml.draw.template.desktop
    mv openoffice.org2.4-text.desktop vnd.sun.xml.writer.desktop
    mv openoffice.org2.4-text-template.desktop vnd.sun.xml.writer.template.desktop
    mv openoffice.org2.4-master-document.desktop vnd.sun.xml.writer.master.desktop
    mv openoffice.org2.4-formula.desktop vnd.sun.xml.math.desktop
popd


for name in flash free one powerpack; do
    echo "[Directories-default]" > %buildroot%_localstatedir/lib/mandriva/kde-profiles/$name/kderc
    echo "prefixes=/var/lib/mandriva/kde-profiles/common,%_localstatedir/lib/mandriva/kde-profiles/$name" >> %buildroot%_localstatedir/lib/mandriva/kde-profiles/$name/kderc
	# create the symlink to the desktop data
    mkdir -p %buildroot%_localstatedir/lib/mandriva/kde-profiles/$name/share/apps/kdesktop
    ln -s %_datadir/mdk/desktop/$name %buildroot%_localstatedir/lib/mandriva/kde-profiles/$name/share/apps/kdesktop/DesktopLinks
done

# Upstream
echo "[Directories-default]" > %buildroot%_localstatedir/lib/mandriva/kde-profiles/common/upstream-kde-config
echo "prefixes=%{_kde3_prefix}" >> %buildroot%_localstatedir/lib/mandriva/kde-profiles/common/upstream-kde-config

# Bookmarks
mkdir -p %buildroot%_localstatedir/lib/mandriva/kde-profiles/{free,flash,one,powerpack}/share/apps/konqueror/
ln -s %_datadir/mdk/bookmarks/konqueror/bookmarks-download.xml %buildroot%_localstatedir/lib/mandriva/kde-profiles/free/share/apps/konqueror/bookmarks.xml
ln -s %_datadir/mdk/bookmarks/konqueror/bookmarks-one.xml %buildroot%_localstatedir/lib/mandriva/kde-profiles/one/share/apps/konqueror/bookmarks.xml
ln -s %_datadir/mdk/bookmarks/konqueror/bookmarks-one.xml %buildroot%_localstatedir/lib/mandriva/kde-profiles/flash/share/apps/konqueror/bookmarks.xml
ln -s %_datadir/mdk/bookmarks/konqueror/bookmarks-powerpack.xml %buildroot%_localstatedir/lib/mandriva/kde-profiles/powerpack/share/apps/konqueror/bookmarks.xml

%clean
rm -rf %buildroot


%changelog
* Fri Feb 4 2011 Tim Williams <tim@my-place.org.uk> 2010.2-1mvt2010.2
+ Rebuild for 2010.2

* Fri Jul 16 2010 Tim Williams <tim@my-place.org.uk> 2010.1-1mvt2010.1
+ Rebuild for 2010.1

* Sun Feb 07 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 2010.0-3mvt2010.0
+ Prevent to install old 2009.0 packages
+ Change mandriva-kdm-config package name to mandriva-kdm3-config to avoid possible future
conflicts. (Mandriva developer may decide to change mandriva-kdm4-config to this one)

* Tue Jan 12 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 2010.0-2mvt2010.0
+ Fix ksplash and wallpaper issues

* Fri Jan 08 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 2010.0-1mvt2010.0
+ Rebuild source for 2010.0
  - Mandriva 2010.0 KDM theme added
  - Mandriva 2010.0 KSplash theme added

* Sun Nov 22 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 2009.0-11mvt2010.0
+ Fixed pacakge name to avoid old official Mandriva package upgrade

* Wed Nov 18 2009 Tim Williams <tim@my-place.org.uk> 2009.0-10mdv2010.0
+ Add konq-home.patch. Changes default start page to avoid crash when viewing the default /usr/share/doc/HTML/index.html

* Tue Nov 17 2009 Tim Williams <tim@my-place.org.uk> 2009.0-9mdv2010.0
+ Rebuild for MDV 2010.0

* Fri Sep 19 2008 Helio Chissini de Castro <helio@mandriva.com> 2009.0-8mdv2009.0
+ Revision: 285971
- Mandriva simple splash for kde3

* Tue Sep 16 2008 Helio Chissini de Castro <helio@mandriva.com> 2009.0-7mdv2009.0
+ Revision: 285202
- Update Mandriva Simple kde3 splash

* Mon Sep 01 2008 Helio Chissini de Castro <helio@mandriva.com> 2009.0-6mdv2009.0
+ Revision: 278597
- Fix profilerc due new .desktop files

* Thu Aug 07 2008 Helio Chissini de Castro <helio@mandriva.com> 2009.0-5mdv2009.0
+ Revision: 265832
- Start to disable basic services of kde3. kde4 runs kded daemon from kde3 to enable easy way to run kde3 applications. We don't want duplicate media notifiers, writed and other similar daemons.

* Mon Jul 28 2008 Anne Nicolas <anne.nicolas@mandriva.com> 2009.0-4mdv2009.0
+ Revision: 251563
- add qt4-style-iaora require

* Mon Jun 23 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 2009.0-3mdv2009.0
+ Revision: 228397
- Changing X11* references in kdmrc to /usr/share/X11...

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Wed May 14 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2009.0-2mdv2009.0
+ Revision: 207234
- Update Flash design

* Tue May 06 2008 Helio Chissini de Castro <helio@mandriva.com> 2009.0-1mdv2009.0
+ Revision: 201967
- Fixed kdm position of new config file. Bye bye /etc/kde

* Wed Apr 02 2008 Helio Chissini de Castro <helio@mandriva.com> 2008.1-27mdv2008.1
+ Revision: 191678
- Kmenu font size

* Tue Apr 01 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 2008.1-26mdv2008.1
+ Revision: 191389
- I've commited this file with a wrong dir path. Fixed now...
- Adding support to Mentor Office Keyboard again, with VolumeKeys disabled, because
  it's a kmilo function

* Fri Mar 28 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2008.1-25mdv2008.1
+ Revision: 190961
- add openoffice icons and openoffice mimetypes so that
  opendocuments use the latest iconset from openoffice.org.
  Closes: #26311

* Thu Mar 27 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 2008.1-24mdv2008.1
+ Revision: 190675
- Fixing Multimedia keyboard pb, by removing Mentor Office Wireless Keyboard shortcuts

* Fri Mar 14 2008 Helio Chissini de Castro <helio@mandriva.com> 2008.1-23mdv2008.1
+ Revision: 187866
- Fix https://qa.mandriva.com/show_bug.cgi?id=37109
- Line up icons by default on desktop

* Wed Mar 12 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 2008.1-22mdv2008.1
+ Revision: 187106
- Fixing minipager issue, by adding a default config file acording to
  https://qa.mandriva.com/show_bug.cgi?id=37796

* Mon Mar 10 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 2008.1-21mdv2008.1
+ Revision: 183669
- Fixing lockout-buttons in kicker to save their configurations affter logout.

* Fri Mar 07 2008 Helio Chissini de Castro <helio@mandriva.com> 2008.1-20mdv2008.1
+ Revision: 181604
- Bookmarking made easy...

* Thu Mar 06 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.1-19mdv2008.1
+ Revision: 181059
- Use the right color scheme for KDM greeter
- Add the config for the default wallpaper for 2008.1

* Wed Mar 05 2008 Helio Chissini de Castro <helio@mandriva.com> 2008.1-18mdv2008.1
+ Revision: 180241
- Houston, we're out of space icons...

* Mon Mar 03 2008 Helio Chissini de Castro <helio@mandriva.com> 2008.1-17mdv2008.1
+ Revision: 177993
- Updated with transparent buttons
- Removed scaled allowing button getting good sizing and centerd position

* Fri Feb 29 2008 Helio Chissini de Castro <helio@mandriva.com> 2008.1-16mdv2008.1
+ Revision: 176912
- Fix shutdown kfm image

* Fri Feb 29 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.1-15mdv2008.1
+ Revision: 176750
- Make sure the right colors are used

* Wed Feb 27 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.1-14mdv2008.1
+ Revision: 175931
- New release containing:
   * Fixed default colors for the kde profiles
   * Removed shadows from the status labels of splash themes
   * Updated kmenu icons
   * Updated metabar images

* Wed Feb 27 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.1-13mdv2008.1
+ Revision: 175813
- New release updating splash themes and color schemes for 2008.1

* Mon Feb 25 2008 Helio Chissini de Castro <helio@mandriva.com> 2008.1-12mdv2008.1
+ Revision: 175126
- Proper faces dir for kdm

* Fri Feb 22 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.1-11mdv2008.1
+ Revision: 173976
- Add a simple splash screen for the ones who don't like the full screen splash

* Tue Feb 19 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.1-10mdv2008.1
+ Revision: 173041
- Fix the button background colors

* Fri Feb 15 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 2008.1-9mdv2008.1
+ Revision: 169003
- Add a default configuration file to minipagerapplet

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 2008.1-8mdv2008.1
+ Revision: 168879
- No use of external player as standard

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-not-capitalized

* Fri Feb 01 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.1-7mdv2008.1
+ Revision: 161221
- Change the kside top images to match the new layout

* Wed Jan 09 2008 Helio Chissini de Castro <helio@mandriva.com> 2008.1-6mdv2008.1
+ Revision: 147151
- Make standard menu default again

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 21 2007 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 2008.1-5mdv2008.1
+ Revision: 136414
- Kicker's clockapplet was not saving their options
  when exits only one clock on kicker. Now its working.

* Tue Dec 18 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.1-4mdv2008.1
+ Revision: 132432
- Added media applet in kicker by default

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - do not hardcode man pages extension

* Thu Dec 13 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.1-3mdv2008.1
+ Revision: 119505
- Fix upgrade from non alternatives /etc/kderc
- Moved common kdeglobal settings for kdeglobals in common and removed the duplicated in the profiles
- Set kspell default encoding for UTF8

* Thu Nov 22 2007 Thierry Vignaud <tvignaud@mandriva.com> 2008.1-2mdv2008.1
+ Revision: 111300
- reupload (missing on x86_64)

* Fri Oct 26 2007 Nicolas Lécureuil <neoclust@mandriva.org> 2008.1-1mdv2008.1
+ Revision: 102378
- Update tarball with merged patches

* Fri Oct 26 2007 Nicolas Lécureuil <neoclust@mandriva.org> 2008.0-31mdv2008.1
+ Revision: 102229
- Add patch to activate klipper

* Tue Oct 23 2007 Olivier Blin <oblin@mandriva.com> 2008.0-30mdv2008.1
+ Revision: 101644
- update Flash splash (from Helio)

* Thu Oct 18 2007 Olivier Blin <oblin@mandriva.com> 2008.0-29mdv2008.1
+ Revision: 100018
- add flash-kde-config

* Tue Oct 02 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.0-28mdv2008.0
+ Revision: 94768
- Make the Mandriva theme select the proper components (#33822)

* Mon Oct 01 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.0-27mdv2008.0
+ Revision: 94151
- Use the ia_ora style and colors in kdm

* Fri Sep 28 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.0-26mdv2008.0
+ Revision: 93584
- Restore kicker pager
- Use official preview for moodin theme
- Use sound notification only for session start and stop
- Properly obsolete the discovery and powerpackplus kde config packages
- Make all obsoletes tags versioned

* Wed Sep 26 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.0-24mdv2008.0
+ Revision: 93095
- Use DesktopLinks instead of Desktop to put icons on desktop (this way they get
  copied to the user home dir (#33204)

* Tue Sep 25 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.0-23mdv2008.0
+ Revision: 92891
- Enforce kaffeine as the default player for One and Free

  + Helio Chissini de Castro <helio@mandriva.com>
    - Flatten people image on powerpack images

* Fri Sep 21 2007 Anne Nicolas <anne.nicolas@mandriva.com> 2008.0-21mdv2008.0
+ Revision: 91776
- update sources
- add metabar themes

* Wed Sep 19 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.0-20mdv2008.0
+ Revision: 91199
- Add squared icons for the K menu

* Wed Sep 19 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.0-19mdv2008.0
+ Revision: 91017
- Fix One color scheme

* Tue Sep 18 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.0-18mdv2008.0
+ Revision: 89764
- Define totem as the default player for powerpack

* Mon Sep 17 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 2008.0-17mdv2008.0
+ Revision: 89272
- Use the desktop icons from desktop-common-data so that they are proper
  translated

* Sat Sep 15 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-16mdv2008.0
+ Revision: 85869
- Multimedia direction change

* Sat Sep 15 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-15mdv2008.0
+ Revision: 85852
- Fix kickoff button

* Fri Sep 14 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-14mdv2008.0
+ Revision: 85758
- KDM changes
- Sound changes

* Wed Sep 12 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-13mdv2008.0
+ Revision: 84580
- Fixed clock position
- Fixed "fat" menu letters
- Fixed spacing on itens

* Mon Sep 10 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-12mdv2008.0
+ Revision: 84142
- ksmserver image change
- kdm call grub instead of lilo
- Proper naming

* Thu Sep 06 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-11mdv2008.0
+ Revision: 81020
- Font and config
- kdm, kicker and Free splash update

* Wed Sep 05 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-9mdv2008.0
+ Revision: 80365
- Position text
- New kicker buttons
- No kdm userlist
- New ia_ora one scheme

* Tue Sep 04 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-8mdv2008.0
+ Revision: 79481
- Updated themes

* Tue Sep 04 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-7mdv2008.0
+ Revision: 78913
- Starting migrate kde theme for 2008.0

* Mon Aug 06 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-5mdv2008.0
+ Revision: 59467
- Restore original images lost on svn crash

* Thu Aug 02 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-4mdv2008.0
+ Revision: 58316
- Fixed splash, removing Galaxy at last !
- Removed wallpaper patch, commited on svn
- Fixed Discovery theme

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] change wallpaper link to more userfriendly one (bug #10638)'

* Fri Jun 08 2007 Anssi Hannula <anssi@mandriva.org> 2008.0-3mdv2008.0
+ Revision: 37525
- do not remove profile alternatives when upgrading package

* Fri Jun 08 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-2mdv2008.0
+ Revision: 37505
- Added possibility to change to upstream kde config, as requested by Anssi

* Mon Jun 04 2007 Helio Chissini de Castro <helio@mandriva.com> 2008.0-1mdv2008.0
+ Revision: 35211
- Removed old faulty updatekdeprofiles for a solution based on update-alternatives. Simple, using
  cascade for common avoiding symlinks, and letting have one profile read instead of a list of
  profiles that never keep same order
- Added hardcoded files present before on kdebase package
- Changed konsole config for Linux schema, instead of white one


* Fri Apr 06 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-25mdv2007.1
+ Revision: 150809
- Fix nsplugins config

* Wed Mar 28 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-24mdv2007.1
+ Revision: 149172
- Fix kicker default icon

* Tue Mar 27 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-23mdv2007.1
+ Revision: 149058
- Fix kdesktop icon order

* Thu Mar 22 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-22mdv2007.1
+ Revision: 148090
- Fix windows key

* Wed Mar 21 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-21mdv2007.1
+ Revision: 147454
- Fix konsole default config

* Wed Mar 21 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-20mdv2007.1
+ Revision: 147276
- don't autostart klipper

* Mon Mar 19 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-19mdv2007.1
+ Revision: 146426
- Fix selected text color

* Thu Mar 15 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-18mdv2007.1
+ Revision: 144247
- Fix title text color

* Wed Mar 14 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-17mdv2007.1
+ Revision: 143441
- Fix kicker top
  Fix kdesktop icons order

* Mon Mar 12 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-16mdv2007.1
+ Revision: 141633
- Update kside top

* Sat Mar 10 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-15mdv2007.1
+ Revision: 140413
- Add jam search engine

* Wed Mar 07 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-14mdv2007.1
+ Revision: 134313
- Add specific desktop file

* Tue Mar 06 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-13mdv2007.1
+ Revision: 134007
- Fix free color

* Mon Mar 05 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-12mdv2007.1
+ Revision: 133018
- Minor fix

* Fri Mar 02 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-10mdv2007.1
+ Revision: 130993
- Update preview

* Thu Mar 01 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-9mdv2007.1
+ Revision: 130605
- Update moodin picture

* Tue Feb 27 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-8mdv2007.1
+ Revision: 126305
- Fix kicker config

* Fri Feb 16 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-7mdv2007.1
+ Revision: 121648
- Fix kicker config

* Fri Feb 16 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-6mdv2007.1
+ Revision: 121631
- New kside

* Fri Feb 16 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-5mdv2007.1
+ Revision: 121620
- Fix version
- Add kicker 16x16 icons

* Wed Feb 14 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-4mdv2007.1
+ Revision: 121083
- Add kside

* Wed Feb 14 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-3mdv2007.1
+ Revision: 121080
- New update

* Wed Feb 14 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-2mdv2007.1
+ Revision: 121001
- Fix icons pos

* Wed Feb 14 2007 Laurent Montel <lmontel@mandriva.com> 2007.1-1mdv2007.1
+ Revision: 120949
- New version
- New source

* Thu Nov 16 2006 Helio Chissini de Castro <helio@mandriva.com> 2007-29mdv2007.1
+ Revision: 85037
- Touch default kdmrc to been able to provide userlist

  + Laurent Montel <lmontel@mandriva.com>
    - New package (2006-09-22 28mdv)
      Fix kmplayer backend
    - New package (2006-09-20 27mdv)
      Fix migrate kdm from 2006 (thanks Pixel)
    - New package (26mdv 2006-09-19)
      Only description into menu for one/discovery

* Tue Sep 19 2006 Laurent Montel <lmontel@mandriva.com> 2007-25mdv2007.0
+ Revision: 61919
- New package( 2006-09-18 25mdv)
  Fix wav encodage

* Sat Sep 16 2006 Laurent Montel <lmontel@mandriva.com> 2007-24mdv2007.0
+ Revision: 61581
- New sound

* Sat Sep 16 2006 Laurent Montel <lmontel@mandriva.com> 2007-23mdv2007.0
+ Revision: 61570
- New package (2006-09-15 23mdv)
  Add new mdk statup function

* Sat Sep 16 2006 Laurent Montel <lmontel@mandriva.com> 2007-22mdv2007.0
+ Revision: 61542
- New package (2006-09-15 22mdv)
  Add default sounds

* Fri Sep 15 2006 Laurent Montel <lmontel@mandriva.com> 2007-21mdv2007.0
+ Revision: 61458
- New package (2006-09-14 21mdv)
  Use double click

* Fri Sep 15 2006 Laurent Montel <lmontel@mandriva.com> 2007-20mdv2007.0
+ Revision: 61419
- New version
  Fix kicker right button

* Wed Sep 13 2006 Laurent Montel <lmontel@mandriva.com> 2007-19mdv2007.0
+ Revision: 61072
- New package (2006-09-12 19mdv)
  Rename download->free
  Fix typo
- Add missing test

* Tue Sep 12 2006 Laurent Montel <lmontel@mandriva.com> 2007-18mdv2007.0
+ Revision: 60840
- New package (2006-09-11 18mdv)
  Workaround for Requires(preun) which doesn't work

* Tue Sep 12 2006 Laurent Montel <lmontel@mandriva.com> 2007-17mdv2007.0
+ Revision: 60830
- New package (2006-09-11 16mdv)
  Fix device on desktop

* Tue Sep 12 2006 Laurent Montel <lmontel@mandriva.com> 2007-16mdv2007.0
+ Revision: 60764
- New package (2006-09-11 16mdv)
  Fix default color, don't display tooltip by default

* Tue Sep 12 2006 Laurent Montel <lmontel@mandriva.com> 2007-15mdv2007.0
+ Revision: 60757
- New package (2006-09-11 15mdv)
  Fix kicker default apps

* Sat Sep 09 2006 Laurent Montel <lmontel@mandriva.com> 2007-14mdv2007.0
+ Revision: 60598
- New package (2006-09-08 14mdv)
  Use by default ia_ora-kde theme

* Thu Sep 07 2006 Laurent Montel <lmontel@mandriva.com> 2007-13mdv2007.0
+ Revision: 60211
- New package (2006/09/06 -13mdv)
  /var/lib/mandriva now is owned by this package
  Add requires postun (need to uninstall package)

* Wed Sep 06 2006 Helio Chissini de Castro <helio@mandriva.com> 2007-12mdv2007.0
+ Revision: 60141
- Added new configuration for kscd

* Wed Sep 06 2006 Laurent Montel <lmontel@mandriva.com> 2007-11mdv2007.0
+ Revision: 60084
- New package (2006-09-05 2007-10mdv)
  Now each distro load correct scheme files
- Fix typo

* Fri Sep 01 2006 Helio Chissini de Castro <helio@mandriva.com> 2007-10mdv2007.0
+ Revision: 59028
- Xdmcp back to disabled due popular demand.
- Fixed post update of profile ( Thanks to Nanar )

* Thu Aug 31 2006 Laurent Montel <lmontel@mandriva.com> 2007-9mdv2007.0
+ Revision: 58847
- Fix kside

  + Helio Chissini de Castro <helio@mandriva.com>
    - Fixed background defaults. Thanks to Laurent Montel
    - Moved configs for a non versionated directories. Requested by Pixel and Laurent
    - Fixed the clean generation if /etc/kderc.
    - Fixed kcookiejar config, which for some reason is making some people getting
      the cookies ask dialog back

* Tue Aug 29 2006 Helio Chissini de Castro <helio@mandriva.com> 2007-7mdv2007.0
+ Revision: 58364
- Fix install for directories with space ( Galaxy )
- Use the right tarball
- Return to old Galaxy name for ksplash. Keep Mandriva2007 for "in the middel of
  cooker" upgrade
- Fixed invalid resources
- Set 2 desktops for discovery

* Fri Aug 25 2006 Helio Chissini de Castro <helio@mandriva.com> 2007-6mdv2007.0
+ Revision: 57975
- Moved terminal from rxvt to xterm in failsafe session of kdm. rxvt not support
  utf-8 and most installations are using this by default
- Fixed bug http://qa.mandriva.com/show_bug.cgi?id=24690 ( Wrong X path )
- enabled xdmcp by default. System listen just locally.

* Fri Aug 25 2006 Helio Chissini de Castro <helio@mandriva.com> 2007-5mdv2007.0
+ Revision: 57956
- Fixed type on ksplash theme rc
- Fixed kdm postinstall

* Thu Aug 24 2006 Helio Chissini de Castro <helio@mandriva.com> 2007-4mdv2007.0
+ Revision: 57753
- Fixed updatekdeprofile by Nanar ( thanks )
- Fixed config paths
- Fixed upgrade of kdm config
- Uploaded Mandriva configs for svn on soft
- Added kside images ( depends on remove switch patch on kdebase )
- Added new ksplash theme ( will have different color ones ones ? )
- First fully operational package. Thanks to Nanar for all help
- import mandriva-kde-config-2007-1mdv2007.0

  + Olivier Thauvin <nanardon@mandriva.org>
    - preserv order of value
    - the regexp need an eol marker
    - no space around the ,

