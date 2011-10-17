%define oname kdetoys
%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define lib_name_orig %mklibname kde3-kdetoys
%define lib_major 1
%define lib_name %lib_name_orig%lib_major
%define lib_name_old %mklibname kdetoys
%define lib_oldname %lib_name_old%lib_major

Name: kde3-%{oname}
Summary: K Desktop Environment - Toys and Amusements
Version: 3.5.12
Release: %mkrel 1
Epoch: 1
URL:		http://www.kde.org
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
Patch0: kdetoys-3.5.6-fix-screensaver-nodisplay.patch
Patch1:		kde-3.5.10-acinclude.patch
#Patch2:		fix_autotools.patch
Group: Graphical desktop/KDE3
BuildRoot: %_tmppath/%name-%version-%release-root
License: GPL
Provides: kteatime3
Provides: kde3-kteatime
Obsoletes: kdetoys3.0 
Obsoletes: kdetoys3
Provides: kdetoys3 = %epoch:%version-%release
Provides:	%{oname}3 = %epoch:%version-%release
Provides:	%{oname} = %epoch:%version-%release
Obsoletes:	%{oname}3
Obsoletes:	%{oname}
Obsoletes: %lib_name
BuildRequires: X11-devel 
BuildRequires: kdelibs-devel
BuildRequires: qt3-devel
BuildRequires:	kde3-macros
%if %mdkversion < 201000
BuildRequires:	autoconf <= 1:2.63
%endif
BuildRequires:	autoconf >= 1:2.65
BuildRequires:	automake >= 1.7

%description
Toys for the K Desktop Environment.

Software included in this package are:
	- amor: Amusing Misuse Of Resources put's comic figures above your windows
	- eyesapplet: a kicker applet similar to XEyes
	- fifteenapplet: kicker applet, order 15 pieces in a 4x4 square by moving them
	- kmoon: system tray applet showing the moon phase
	- kodo: mouse movement meter
	- kscore: kicker applet with a sports ticker
	- kteatime: system tray applet that makes sure your tea doesn't get too strong
	- ktux: Tux-in-a-Spaceship screen saver
	- kweather: kicker applet that will display the current weather outside
	- kworldwatch: application and kicker applet showing daylight area on the
	  world globe


%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files
%defattr(-,root,root)
%_kde3_bindir/amor
%_kde3_bindir/kodo
%_kde3_bindir/kteatime
%_kde3_bindir/ktux
%_kde3_bindir/kworldclock

%_kde3_datadir/applications/kde/amor.desktop
%_kde3_datadir/applications/kde/kodo.desktop
%_kde3_datadir/applications/kde/kteatime.desktop
%_kde3_datadir/applications/kde/kworldclock.desktop

%_kde3_datadir/applnk/System/ScreenSavers/ktux.desktop
%_kde3_appsdir/kdesktop/programs/kdeworld.desktop
%_kde3_appsdir/kicker/applets/eyesapplet.desktop
%_kde3_appsdir/kicker/applets/kfifteenapplet.desktop
%_kde3_appsdir/kicker/applets/kmoonapplet.desktop
%_kde3_appsdir/kicker/applets/kwwapplet.desktop

%_kde3_appsdir/kmoon
%_kde3_appsdir/ktux
%_kde3_appsdir/kteatime
%_kde3_appsdir/kworldclock
%_kde3_appsdir/amor
%_kde3_appsdir/kodo

%_kde3_libdir/kde3/eyes_panelapplet.*
%_kde3_libdir/kde3/fifteen_panelapplet.*
%_kde3_libdir/kde3/kmoon_panelapplet.*
%_kde3_libdir/kde3/ww_panelapplet.*

%_kde3_iconsdir/hicolor/*/apps/amor.png
%_kde3_iconsdir/hicolor/*/apps/kmoon.png
%_kde3_iconsdir/hicolor/*/apps/kodo.png
%_kde3_iconsdir/hicolor/*/apps/kteatime.png
%_kde3_iconsdir/hicolor/*/apps/kworldclock.png
%_kde3_iconsdir/hicolor/*/apps/ktux.png

%doc %_kde3_docdir/HTML/en/amor
%doc %_kde3_docdir/HTML/en/kmoon
%doc %_kde3_docdir/HTML/en/kodo
%doc %_kde3_docdir/HTML/en/kteatime
%doc %_kde3_docdir/HTML/en/kworldclock


#--------------------------------------------------------------------

%package -n %lib_name-devel
Summary:	Headers files for kdetoys
Group:		Development/KDE and Qt

Provides:	kdetoys-devel = %epoch:%version-%release
Obsoletes:	kdetoys-devel	


Obsoletes:  kdetoys3-devel
Provides:   kdetoys3-devel = %epoch:%name-%version
Provides:	%lib_name_orig-devel = %epoch:%version-%release
Obsoletes:	%lib_name_orig-devel
Provides:	%lib_oldname-devel = %epoch:%version-%release
Obsoletes:	%lib_oldname	

Provides:	%lib_name_orig-devel = %epoch:%version-%release

%description -n %lib_name-devel
Headers files for kdetoys.


%files -n %lib_name-devel
%defattr(-,root,root,-)
%_kde3_includedir/*.h

#--------------------------------------------------------------------

%package kweather
Group:      Graphical desktop/KDE3
Summary:    Applet displaying the current weather
Conflicts:  kdetoys < 1:3.5.8-1
Conflicts:  %lib_name-kweather <= 3.2.3-1mdk
Provides:   kweather3
Provides:   kde3-kweather
Provides:	%{oname}-kweather = %epoch:%version-%release
Obsoletes:	%{oname}-kweather
Requires:   %lib_name-kweather = %epoch:%version-%release

%description kweather
kicker applet that will display the current weather outside

%files kweather
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/kweather
%_kde3_bindir/kweather*
%_kde3_appsdir/kicker/applets/kweather.desktop
%_kde3_appsdir/kweather*
%_kde3_datadir/services/kcmweather.desktop
%_kde3_datadir/services/kweatherservice.desktop
%_kde3_datadir/services/kcmweatherservice.desktop
%_kde3_libdir/kde3/*weather*
%_kde3_iconsdir/hicolor/*/*/kweat*

#--------------------------------------------------------------------

%package -n %lib_name-kweather
Group:      Development/KDE and Qt
Summary:    Libraries for kdetoys
Conflicts:  kdetoys < 3.5.8-5
Conflicts: %lib_name <= 3.2.3-11mdk
Provides:	%{lib_oldname}-kweather = %epoch:%version-%release
Obsoletes:	%{lib_oldname}-kweather

%description -n %lib_name-kweather
kicker applet that will display the current weather outside

%if %mdkversion < 200900
%post -n %lib_name-kweather -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name-kweather -p /sbin/ldconfig
%endif

%files -n %lib_name-kweather
%defattr(-,root,root,-)
%_kde3_libdir/libkdeinit_kweatherreport.*

#--------------------------------------------------------------------

%prep

%setup -q -n %{oname}-%{version}
%patch0 -p1 -b .fix_screensaver_nodisplay
%if %mdkversion >= 201000
%patch1 -p1
#%patch2 -p1
%endif

%build
export QTDIR=%{qt3dir}

make -f admin/Makefile.common cvs

PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/

%configure_kde3 \
  --with-extra-includes=/usr/include/avahi-compat-libdns_sd:/opt/kde3/include/tqt \
  --with-extra-libs=/opt/kde3/lib
%make


%install
rm -fr %buildroot
make install DESTDIR=%buildroot

%clean
rm -fr %buildroot


%changelog
* Mon Jul 18 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-1mvt2010.2
+ Update sources and rebuild for Trinity 3.5.12
- remove fix-autotools.patch

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 1:3.5.10-2mvt2010.1
+ Rebuild for MDV 2010.1

* Tue Jan 19 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-2mvt2010.0
- Rebuild for 2010.0
- Change package name to avoid KDE4 upgrade
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65:patch3
+ Fix automake 1.11 issue:patch4

* Tue Oct 14 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.10-1mdv2009.1
+ Revision: 293470
- New version 3.5.10
- drop upstream patch

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:3.5.9-4mdv2009.0
+ Revision: 267780
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 11 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.9-3mdv2009.0
+ Revision: 217989
- Rebuild for new ldflags

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 07 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-2mdv2009.0
+ Revision: 203741
- Move to /opt

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-1mdv2008.1
+ Revision: 169163
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches integrated

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-not-capitalized
    - fix description-line-too-long

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Fix Nantes location
    - [FEATURE] Add some stations on Kweather (Bug #35562)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 31 2007 Oden Eriksson <oeriksson@mandriva.com> 1:3.5.8-8mdv2008.1
+ Revision: 139865
- rebuilt against openldap-2.4.7 libs

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 08 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-7mdv2008.1
+ Revision: 116559
- Use icons macros  for kweather package too
  Use rpms macros for icons
- Clean spec file

* Fri Dec 07 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-6mdv2008.1
+ Revision: 116129
- Only package kweather stuffs on kweather packages

* Fri Dec 07 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-5mdv2008.1
+ Revision: 116095
- Fix conflicts between kdetoys and libkdetoys-kweather

* Mon Nov 19 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-4mdv2008.1
+ Revision: 110493
- Add conflicts to allow smooth upgrades
- File File list ( Fix the fact that kweather do not work )

* Sun Oct 28 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-1mdv2008.1
+ Revision: 102857
- KDE 3.5.8

* Thu May 17 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-1mdv2008.0
+ Revision: 27531
- 3.5.7 release


* Sat Mar 31 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-6mdv2007.1
+ Revision: 149992
- Only display it under kde
- Fix screensaver nodisplay

* Tue Mar 06 2007 Laurent Montel <lmontel@mandriva.com> 1:3.5.6-4mdv2007.1
+ Revision: 133944
- Fix specification

* Mon Feb 05 2007 Laurent Montel <lmontel@mandriva.com> 1:3.5.6-3mdv2007.1
+ Revision: 116381
- Remove non existing requires
- 3.5.6

* Fri Dec 22 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-2mdv2007.1
+ Revision: 101414
- Fix spec file

* Wed Oct 18 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-1mdv2007.1
+ Revision: 65909
- 3.5.5
- New release (2006/08/03 3.5.4-1mdv)
- Use macro
- 3.5.3
- Rebuild
- Rebuild for generate category
- 3.5.2
- 3.5.1
- MDK9.2 is obsolete now
- Enable debug for cooker
- toto
- real kde3.5
- 3.5.0 (named rc1)
- 3.4.92
- Rebuild
- Use --libsuffix
  use %%qtdir
- Fix error
- Remove debug
  Add diff from svn kde 3.4.2 branch
- 3.4.2

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Helio Chissini de Castro <helio@mandriva.com>
    - We are Mandriva now
    - Uploading package ./kdetoys

* Thu May 05 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-5mdk
- Rebuild

* Sat Apr 23 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-4mdk
- Reactivate -fvisibility same as for ppc ask by Christiaan Welvaart <cjw@daneel.dyndns.org>

* Tue Apr 12 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-3mdk
- Fix requires (bug found by Nicolas Chipaux)

* Tue Apr 12 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-2mdk
- Use --enable-new-ldflags
- change email

* Thu Apr 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0

* Thu Feb 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-6mdk
- Disable debug

* Fri Jan 28 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-4mdk
- Fix generated menu
- Don't generate menu entry for ktux screensaver use applnk default directory which is hidden by default

* Mon Jan 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-4mdk
- Disable visibility for ppc

* Fri Jan 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-3mdk
- Use -fvisibility

* Thu Dec 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-2mdk
- Fix menu

* Tue Nov 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Thu Oct 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-3mdk
- Bye-bye %%buildfor

* Tue Oct 12 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-2mdk
- Deprecated mdk < 9.2

* Fri Oct 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-1mdk
- 3.3.1

* Thu Sep 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-4mdk
- Fix conflict

* Wed Sep 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-3mdk
- Fix conflict from MDK10.0

* Wed Sep 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-2mdk
- Fix conflict

* Sat Sep 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-1mdk
- 3.3.0

* Tue Aug 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-10mdk
- add patch2: fix kweather rtl

* Sat Aug 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-9mdk
- Rebuild for missing package

* Tue Aug 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-8mdk
- Remove debug

* Thu Aug 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-7mdk
- Fix conflict

* Wed Aug 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-6mdk
- Fix spec file

* Fri Jul 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-5mdk
- Fix remove rpath

* Wed Jul 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-4mdk
- Rebuild to new kdelibs

* Tue Jul 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-3mdk
- Fix conflict
- Remove libkdetoys it's empty

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Sat Jun 05 2004 <lmontel@n2.mandrakesoft.com> 3.2.2-4mdk
- Rebuild

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-3mdk
- Fix conflict

* Wed Jun 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-2mdk
- Rebuild with debug

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-2mdk
- Fix spec file for using rpmbuildupdate

* Sat Apr 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

