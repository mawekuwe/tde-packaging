%define lib_name_orig %mklibname %name
%define lib_major 0
%define lib_name %mklibname %name %lib_major
%define develname %mklibname -d %name

Name: kmymoney2
Version: 1.0.2
Release: %mkrel 3
Summary: Kmymoney2 The Personal Finances Manager for kde3 
Source0: http://kent.dl.sourceforge.net/sourceforge/kmymoney2/%{name}-%{version}.tar.bz2
Source1: kmymoney2.desktop
Url: http://kmymoney2.sourceforge.net/
License: GPLv2+
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: kdelibs-devel
BuildRequires: jpeg-devel mng-devel png-devel qt3-devel
BuildRequires: aqhbci-devel > 0.3.0
BuildRequires: OpenSP-devel libofx-devel
Requires: %lib_name = %version-%release
Patch0: kmymoney-0.8.2-disable-visibility.patch

%description
The Personal Finances Manager for KDE 3.

%files -f %name.lang
%defattr(-,root,root)
%_kde3_bindir/*
%_kde3_datadir/apps/%name
%_kde3_iconsdir/*/*/*/*
%_kde3_datadir/applications/kde/*.desktop
%_kde3_datadir/services/*.desktop
%_kde3_datadir/servicetypes/*.desktop
%_kde3_datadir/apps/kmm_ofximport
%_kde3_datadir/config.kcfg/kmymoney2.kcfg
%_mandir/man1/*
%_kde3_datadir/mimelnk/application/*.desktop
%_kde3_datadir/icons/Tango/scalable/*
%_kde3_datadir/icons/oxygen/scalable/*

#--------------------------------------------------------------------

%package -n %lib_name
Group:      Development/KDE and Qt
Summary:    Libraries for %name

%description -n %lib_name
Librairie for %name

%if %mdkversion < 200900
%post -n %lib_name -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name -p /sbin/ldconfig
%endif

%files -n %lib_name
%defattr(-,root,root,-)
%_kde3_libdir/kde3/kmm_ofximport.la
%_kde3_libdir/kde3/kmm_ofximport.so
%_kde3_libdir/libkmm_mymoney.la
%_kde3_libdir/libkmm_mymoney.so.*
%_kde3_libdir/libkmm_plugin.la
%_kde3_libdir/libkmm_plugin.so.*
%_kde3_libdir/libkmm_kdchart.so.*
#--------------------------------------------------------------------

%package -n %develname
Group:      Development/KDE and Qt
Summary:    Devel files for %name
Requires:   %lib_name = %{version}-%{release}
Obsoletes:  %lib_name-devel

%description -n %develname
Devel file for %name

%files -n %develname
%defattr(-,root,root,-)
%dir %_kde3_includedir/kmymoney/
%_kde3_includedir/kmymoney/*.h
%_kde3_libdir/libkmm_mymoney.so
%_kde3_libdir/libkmm_plugin.so
%_kde3_libdir/libkmm_kdchart.la
%_kde3_libdir/libkmm_kdchart.so

#--------------------------------------------------------------------

%prep

%setup -q
#%patch0 -p1 -b .disable_visibility

%build
%define _disable_ld_no_undefined 1
%configure_kde3 \
	--enable-ofxplugin \
    --enable-ofxbanking --disable-final --disable-sqlite3
#necessary to remove old files
make clean

%make

%install
%makeinstall_std

# Translation team modified desktop file
cp -f %SOURCE1  %buildroot/%_kde3_datadir/applications/kde/

%find_lang %name --with-html

%clean
rm -fr %buildroot



%changelog
* Tue Jul 26 2011 Tim Williams <tim@my-place.org.uk> 1.0.2-3mdv2010.2
+ rebuild for Trinity

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 1.0.2-2mdv2010.1
+ rebuild for MDV 2010.1

* Thu Nov 19 2009 Tim Williams <tim@my-place.org.uk> 1.0.2-1mdv2010.0
+ Update source to 1.0.2
+ rebuild for MDV 2010.0

* Wed Mar 04 2009 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.3-1mdv2009.1
+ Revision: 348190
- Update to 0.9.3
  Disable sqlite3 support for now, the build must be fixed before

* Sat Nov 08 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.9-5mdv2009.1
+ Revision: 301009
- rebuilt against new libxcb

  + Helio Chissini de Castro <helio@mandriva.com>
    - Updated desktop file as requested by translation team

* Sat Jul 26 2008 Nicolas Lécureuil <neoclust@mandriva.org> 0.8.9-3mdv2009.0
+ Revision: 250088
- Disable enable final
- Fix typo
- Fix specfile layout
- Rebuild because BS failure
- Move to /opt
  Move Kmoney2 out of "More"

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Apr 17 2008 Funda Wang <fundawang@mandriva.org> 0.8.9-1mdv2009.0
+ Revision: 195065
- disable kbanking as it does not exist any more
- Bump requires on aqbanking
- New version 0.8.9

* Sat Mar 08 2008 Funda Wang <fundawang@mandriva.org> 0.8.8-2mdv2008.1
+ Revision: 182081
- cleanup spec file

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 21 2007 Funda Wang <fundawang@mandriva.org> 0.8.8-1mdv2008.1
+ Revision: 136311
- New version 0.8.8

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - replace %%_datadir/man by %%_mandir!

* Mon Jul 23 2007 Funda Wang <fundawang@mandriva.org> 0.8.7-1mdv2008.0
+ Revision: 54782
- New version

* Fri Jul 13 2007 Funda Wang <fundawang@mandriva.org> 0.8.6-2mdv2008.0
+ Revision: 51845
- New develpackage policy


* Sat Mar 10 2007 Laurent Montel <lmontel@mandriva.com> 0.8.6-1mdv2007.1
+ Revision: 140315
- 0.8.6
- Rebuild
- Import kmymoney2

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Fix BuildRequires

* Fri Sep 01 2006 Laurent MONTEL <lmontel@mandriva.com> 0.8.5-1
- 0.8.5

* Mon Jun 19 2006 Laurent MONTEL <lmontel@mandriva.com> 0.8.4-2mdk
- Fix missing build requires

* Sun May 21 2006 Laurent MONTEL <lmontel@mandriva.com> 0.8.4-1mdk
- 0.8.4

* Thu Apr 20 2006 Laurent MONTEL <lmontel@mandriva.com> 0.8.3-4mdk
- Fix requires

* Thu Apr 20 2006 Laurent MONTEL <lmontel@mandriva.com> 0.8.3-3mdk
- Rebuild

* Mon Feb 27 2006 Laurent MONTEL <lmontel@mandriva.com> 0.8.3-2mdk
- Fix build kbanking plugins

* Mon Feb 27 2006 Laurent MONTEL <lmontel@mandriva.com> 0.8.3-1mdk
- 0.8.3

* Tue Jan 03 2006 Laurent MONTEL <lmontel@mandriva.com> 0.8.2-2mdk
- Fix compile under x86_64

* Mon Jan 02 2006 Laurent MONTEL <lmontel@mandriva.com> 0.8.2-1mdk
- 0.8.2

* Sun Nov 06 2005 Laurent MONTEL <lmontel@mandriva.com> 0.8.1-1mdk
- 0.8.1

* Sun Aug 14 2005 Laurent MONTEL <lmontel@mandriva.com> 0.8.0-1mdk
- 0.8.0

* Sun Jul 31 2005 Laurent MONTEL <lmontel@mandriva.com> 0.7.5-1mdk
- 0.7.5

* Tue Jul 19 2005 Laurent MONTEL <lmontel@mandriva.com> 0.7.4-1mdk
- 0.7.4

* Sat Jul 09 2005 Laurent MONTEL <lmontel@mandriva.com> 0.7.3-1mdk
- 0.7.3

* Wed Jun 01 2005 Laurent MONTEL <lmontel@mandriva.com> 0.7.2-1mdk
- 0.7.2

* Tue May 24 2005 Laurent MONTEL <lmontel@mandriva.com> 0.7.1-2mdk
- Add --enable-ofxplugin

* Sun May 22 2005 Laurent MONTEL <lmontel@mandriva.com> 0.7.1-1mdk
- 0.7.1

* Fri May 20 2005 Laurent MONTEL <lmontel@mandriva.com> 0.7.0-2mdk
- Enable --enable-kbanking

* Sun May 15 2005 Laurent MONTEL <lmontel@mandriva.com> 0.7.0-1mdk
- 0.7.0

* Sat May 07 2005 Laurent MONTEL <lmontel@mandriva.com> 0.6.4-3mdk
- fix build on x86_64

* Thu Dec 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.4-2mdk
- Fix menu

* Thu Nov 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.4-1mdk
- 06.4

* Mon Nov 01 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.3-1mdk
- 0.6.3

* Thu Sep 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.2-2mdk
- kde2 -> kde3 thanks (Eskild Hustvedt <eskild@mandrakehelp.com>)
- clean spec file

* Sat Sep 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.2-1mdk
- New version

* Sat Aug 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.1-2mdk
- Rebuild with new menu translation table

* Wed Jul 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.1-1mdk
- 0.6.1

* Tue Jun 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6-1mdk
- 0.6

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.5.1-4mdk
- Rebuild

