%define name    ksmoothdock
%define version 4.5
%define release %mkrel 8
%define _liconsdir %_kde3_iconsdir/large
%define _miconsdir %_kde3_iconsdir/mini

Summary:       Desktop panel for KDE3
Name:          %{name}
Version:       %{version}
Release:       %{release}
License:       GPL
Url:           http://ksmoothdock.sourceforge.net/
Group:         Graphical desktop/KDE3
Source:        %{name}-%{version}_automake-1.9.tar.bz2
BuildRoot:     %{_tmppath}/%{name}-%{version}
BuildRequires: kdebase3-devel
BuildRequires: chrpath
Patch0: ksmoothdock-4.5-compile.patch

%description
KSmoothDock is a cool desktop panel (like KDE's kicker) for KDE 3.2 with 
smooth zooming (2 modes: normal & parabolic). Its aim is to provide 
a cool alternative/complement to kicker. As it is intended for KDE/Linux,
its behaviour will be like that of kicker. 

%prep
%setup -q -n %{name}
%patch0 -p0

%build
%configure_kde3

%make

%install
rm -Rf %{buildroot}
%makeinstall_std

desktop-file-install --vendor="" \
  --add-category="KDE" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --add-only-show-in="KDE" \
  --dir %{buildroot}%{_kde3_datadir}/applications %{buildroot}%{_kde3_datadir}/applnk/Utilities/*


mkdir -p %{buildroot}/{%_kde3_iconsdir,%{_miconsdir},%{_liconsdir}}
ln -s ../hicolor/16x16/apps/%{name}.png %{buildroot}/%{_miconsdir}
ln -s ../hicolor/32x32/apps/%{name}.png %{buildroot}/%{_liconsdir}
ln -s hicolor/32x32/apps/%{name}.png %{buildroot}/%_kde3_iconsdir


%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%_kde3_iconsdir/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_kde3_bindir}/%{name}
%{_kde3_datadir}/applications/ksmoothdock.desktop
%{_kde3_datadir}/applnk/Utilities/ksmoothdock.desktop
%{_kde3_datadir}/apps/ksmoothdock/ksmoothdockui.rc
%dir %{_kde3_docdir}/HTML/en/ksmoothdock
%{_kde3_docdir}/HTML/en/ksmoothdock/common
%{_kde3_docdir}/HTML/en/ksmoothdock/index.cache.bz2
%{_kde3_docdir}/HTML/en/ksmoothdock/index.docbook
%{_kde3_iconsdir}/hicolor/16x16/apps/ksmoothdock.png
%{_kde3_iconsdir}/hicolor/32x32/apps/ksmoothdock.png


%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 4.5-8mvt2010.0
+ Rebuild for Trinity

* Fri Jul 23 2010 Tim Williams <tim@my-place.org.uk> 4.5-7mvt2010.0
+ Rebuild for MDV 2010.1

* Sun Jan 17 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 4.5-6mvt2010.0
+ Fix spec file

* Fri Dec 25 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 4.5-5mvt2010.0
+ Rebuild

* Thu Mar 26 2009 Helio Chissini de Castro <helio@mandriva.com> 4.5-4mdv2009.1
+ Revision: 361356
- Bump to rebuild against cooker

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 4.5-1mdv2008.1
+ Revision: 140918
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jun 14 2007 Emmanuel Blindauer <blindauer@mandriva.org> 4.5-1mdv2008.0
+ Revision: 39330
- 4.5 version and xdg menu


* Wed Mar 14 2007 Emmanuel Blindauer <blindauer@mandriva.org> 4.3-1mdv2007.1
+ Revision: 143848
- try to fix x86_64 compilation
- new version
- Import ksmoothdock

* Mon Aug 14 2006 Emmanuel Blindauer <blindauer@mandriva.org> 3.6.1-3mdv2007.0
- correct some rpmlint warning and errors

* Sat May 20 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 3.6.1-2mdk
- build with automake1.8

* Sat Feb 11 2006 Nicolas L�cureuil <neoclust@mandriva.org> 3.6.1-1mdk
- New release 3.6.1
- Rediff patch 1, 2

* Mon Dec 26 2005 Nicolas L�cureuil <neoclust@mandriva.org> 3.5.1-4mdk
- Fix Build
- use mkrel

* Fri Feb 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.5.1-3mdk
- Add patch2: fix mem leak

* Fri Feb 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.5.1-2mdk
- Add patch1: fix includemoc

* Fri Feb 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.5.1-1mdk
- 3.5.1

* Tue Feb 22 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3-3mdk
- Fix build on 64_x86

* Fri Jul 23 2004 Michael Scherer <misc@mandrake.org> 3.3-2mdk 
- rebuild for new gcc
- remove libtool hack
- add description

* Sat May 29 2004 Buchan Milne <bgmilne@linux-mandrake.com> 3.3-1mdk
- first package

