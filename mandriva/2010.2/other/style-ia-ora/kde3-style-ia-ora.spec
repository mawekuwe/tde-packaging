%define shortname 	ia_ora-kde
Summary:        Mandriva theme for KDE - Widget design
Name:           kde3-style-ia-ora
Version:        1.0.8
Release:        %mkrel 10
License:        GPL
Group:          Graphical desktop/KDE3
URL:            http://www.mandrivalinux.com/
BuildRequires:  kdelibs-devel
BuildRequires:  kdebase-devel >= 3.1.94-11mdk
Source0:        %{shortname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mandriva theme for KDE

%prep
%setup -q -n %{shortname}-%{version}

%build
%configure_kde3

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%_kde3_libdir/kde3/kwin3_iaora.la
%_kde3_libdir/kde3/kwin3_iaora.so
%_kde3_libdir/kde3/kwin_iaora_config.la
%_kde3_libdir/kde3/kwin_iaora_config.so
%_kde3_appsdir/kwin/iaora.desktop
%_kde3_libdir/kde3/plugins/styles/ia_ora.la
%_kde3_libdir/kde3/plugins/styles/ia_ora.so
%_kde3_appsdir/kstyle/themes/ia_ora.themerc





%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 1.0.8-10mvt2010.2
+ Rebuild for Trinity

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 1.0.8-9mvt2010.0
+ Rebuild for MDV 2010.1

* Sun Nov 22 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1.0.8-8mvt2010.0
- Rename package to avoid unwanted KDE4 upgrade
- Merge packages in one kde-style package
- Fix package group in spec file

* Tue Nov 17 2009 Tim Williams <tim@my-place.org.uk> 1.0.8-7mdv2010.0
+ Rebuild for MDV 2010.0

* Thu Mar 26 2009 Helio Chissini de Castro <helio@mandriva.com> 1.0.8-6mdv2009.1
+ Revision: 361404
- Bump to rebuild against cooker

* Tue Nov 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.8-5mdv2009.1
+ Revision: 304189
- rebuild for new xcb

* Wed Aug 06 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.8-4mdv2009.0
+ Revision: 264680
- rebuild early 2009.0 package (before pixel changes)

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 1.0.8-2mdv2009.0
+ Revision: 204689
- Move to /opt

* Wed Feb 27 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.8-1mdv2008.1
+ Revision: 175799
- New release (1.0.8):
   * Fix drawing of buttons when using mandriva color schemes
   * Update color scheme names to match the new ones

* Tue Feb 19 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.7-1mdv2008.1
+ Revision: 173100
- new release (1.0.7) fixing some drawing issues on applications that don't use
  standard background colors (#33502)

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-2mdv2008.1
+ Revision: 141786
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 12 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.6-1mdv2008.0
+ Revision: 84626
- new release: 1.0.6:
   * Use the right color for the bottom line of menubar
   * Remove some lines that were causing double borders at menubar and toolbar
     ends
   * Fix the bottom of toolbars: it was being drawn using the wrong color
   * Use a flat background for status bars
   * Add a minimum size for the scrollbar handle
- new release: 1.0.5
   * Use the widget style in all separators (#33260)
   * Fixed popup menu item drawing on menus that have titles (#33287)

* Thu Sep 06 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.4-1mdv2008.0
+ Revision: 81272
- new version: 1.0.4
   * Restore the old color themes (as they will be kept as alternatives)
   * Properly mask the rounded borders and properly draw the region previously
     masked
   * Create fake rounded corners on menu items
   * Reduced the button margin to get normal sized buttons (not giant ones)
   * Make it possible to resize windows by the top border
------------------------------------------------------------------------
  r227235 | boiko | 2007-09-06 13:58:18 -0300 (Qui, 06 Set 2007) | 3 lines

* Wed Sep 05 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.3-1mdv2008.0
+ Revision: 80378
- new release: 1.0.3
   * Implement highligh on hovering controls
   * Threat scrollbar buttons as buttons (showing them lowered when the button
     is pressed for example)
   * Show the combo box button as pressed when the list is opened
   * Removed Powerpack+ colors
   * Changed Discovery/One to just One and adjusted colors
   * Used more sane values when using ia_ora together with other KDE color
     schemes
- new release:
   * fix gradient colors of menus (thanks Frederic Crozat for pointing that)
   * implement correctly the combo box drawing according to the ia_ora spec
   * Fix the text color of menubar items

* Thu Aug 23 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.1-1mdv2008.0
+ Revision: 70685
- new version: 1.0.1
   * Replace the gradient code by the Plastik one (it is better written)
   * Fix drawing of menubar items and popupmenu items (#30659)

* Mon Jun 11 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1.0-18mdv2008.0
+ Revision: 38004
- REBUILD


* Thu Mar 22 2007 Laurent Montel <lmontel@mandriva.com> 1.0-17mdv2007.1
+ Revision: 147929
- Fix theme

* Mon Mar 19 2007 Laurent Montel <lmontel@mandriva.com> 1.0-16mdv2007.1
+ Revision: 146479
- Fix progressbar text color

* Wed Mar 07 2007 Laurent Montel <lmontel@mandriva.com> 1.0-15mdv2007.1
+ Revision: 134563
- Fix style

* Tue Mar 06 2007 Laurent Montel <lmontel@mandriva.com> 1.0-14mdv2007.1
+ Revision: 133854
- New update

* Wed Feb 28 2007 Laurent Montel <lmontel@mandriva.com> 1.0-13mdv2007.1
+ Revision: 127097
- New update

* Wed Jan 24 2007 Laurent Montel <lmontel@mandriva.com> 1.0-12mdv2007.1
+ Revision: 112737
- Fix theme

* Tue Jan 02 2007 Laurent Montel <lmontel@mandriva.com> 1.0-11mdv2007.1
+ Revision: 103350
- Update tarball

* Mon Dec 11 2006 Laurent Montel <lmontel@mandriva.com> 1.0-10mdv2007.1
+ Revision: 94696
- Rename spec file name too
- Rename ia_ora to ia_ora-kde
  Fix a lot of bug
- Import ia_ora-kde

* Sat Sep 16 2006 Laurent MONTEL <lmontel@mandriva.com> 1.0-9
- Fix title bar

* Thu Sep 14 2006 Laurent MONTEL <lmontel@mandriva.com> 1.0-8
- Fix handle

* Thu Sep 14 2006 Laurent MONTEL <lmontel@mandriva.com> 1.0-7
- Fix toolbar color

* Thu Sep 14 2006 Laurent MONTEL <lmontel@mandriva.com> 1.0-6
- Fix Combobox/Scrollbar/Checkbox and bidi mode

* Tue Sep 12 2006 Laurent MONTEL <lmontel@mandriva.com> 1.0-5
- Fix tabbar

* Tue Sep 12 2006 Laurent MONTEL <lmontel@mandriva.com> 1.0-4
- Fix scrollbar

* Sun Sep 10 2006 Laurent MONTEL <lmontel@mandriva.com> 1.0-3
- Improve style

* Fri Sep 08 2006 Laurent MONTEL <lmontel@mandriva.com> 1.0-2
- Some fixes

* Tue Sep 05 2006 Laurent MONTEL <lmontel@mandriva.com> 1.0-1
- Initial package

