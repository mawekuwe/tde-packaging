%define __libtoolize    /bin/true
%define oname kdmtheme
%define name kde3-%{oname}

Name:           %{name}
Summary:        Kdmtheme allow to change kdm theme
Version:        1.2.2
Release:        %mkrel 4
Source:         http://beta.smileaf.org/files/kdmtheme/%{oname}-%{version}.tar.bz2
URL:           	http://smileaf.org/
Group:		Graphical desktop/KDE3
BuildRoot:      %_tmppath/%oname-buildroot
License:	GPLv2+
BuildRequires:	kde3-macros
BuildRequires:	kdelibs-devel
BuildRequires:	desktop-file-utils
Requires:       kdebase-session-plugins
Patch0:		kdmtheme-0.8.2-use-kdesu.patch
Patch1:		kde-3.5.10-acinclude.patch
Patch2:		kdmtheme-1.2.2-new-autotools.patch

%description
Kdmtheme allow to change theme in kdm when we used gdm theme

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1 -b .fix_use_kdmtheme
%patch1 -p1
%patch2 -p1 -b .autotools

%build
make -f Makefile.cvs
%configure_kde3

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

desktop-file-install --vendor='' \
	--dir %buildroot%_kde3_datadir/applications/kde/ \
	--remove-key='Encoding' \
	--add-category='DesktopSettings;Settings' \
	%buildroot%_kde3_datadir/applications/kde/*.desktop

%find_lang %oname --with-html

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%{update_menus}

%postun
%{clean_menus}
%endif

%files -f %oname.lang
%defattr(-,root,root,0755)
%_kde3_libdir/kde3/kcm_kdmtheme.la
%_kde3_libdir/kde3/kcm_kdmtheme.so
%_kde3_datadir/applications/kde/*


%changelog
* Wed Jul 18 2011 Tim Williams <tim@my-place.org.uk> 1.2.2-3mvt2010.2
+ Rebuild for Trinity

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 1.2.2-3mvt2010.0
+ Repackage for MDV 2010.1

* Tue Feb 09 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1.2.2-2mvt2010.0
- Fix built with autoconf 2.65 and automake 1.11
- Fix SPEC according to filetriggers policy
- Change package group

* Fri Nov 20 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1.2.2-1mvt2010.0
+ Rebuild for 2010.0

* Fri Feb 08 2008 Funda Wang <fundawang@mandriva.org> 1.2.2-1mdv2008.1
+ Revision: 163969
- add more categories for desktop entry
- New version 1.2.

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 07 2007 Laurent Montel <lmontel@mandriva.org> 1.1.3-1mdv2008.0
+ Revision: 23970
- 1.1.3


* Wed Jan 17 2007 Laurent Montel <lmontel@mandriva.com> 1.1.2-2mdv2007.0
+ Revision: 109749
- Fix autoconf detect
- Fix requires
- Import kdmtheme

* Sat Jun 24 2006 Laurent MONTEL <lmontel@mandriva.com> 1.1.2-1mdk
- 1.1.2

* Tue May 09 2006 Laurent MONTEL <lmontel@mandriva.com> 1.1-2mdk
- Rebuild to generate category

* Fri Mar 24 2006 Laurent MONTEL <lmontel@mandriva.com> 1.1-1mdk
- 1.1

* Tue Jan 31 2006 Laurent MONTEL <lmontel@mandriva.com> 1.0.1-1mdk
- 1.0.1

* Fri Dec 30 2005 Laurent MONTEL <lmontel@mandriva.com> 0.9.2-1mdk
- 0.9.2

* Thu Jul 21 2005 Laurent MONTEL <lmontel@mandriva.com> 0.9.1-1mdk
- 0.9.1

* Sat Jul 09 2005 Laurent MONTEL <lmontel@mandriva.com> 0.9-4mdk
- Rebuild

* Fri Apr 08 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9-3mdk
- Fix compile on x86_64 (copy/paste is bad !!!)

* Thu Apr 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9-2mdk
- Add patch2: fix disable widget

* Thu Apr 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9-1mdk
- 0.9

* Tue Apr 05 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.2-3mdk
- Patch1: Fix use kdesu

* Fri Mar 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.2-2mdk
- Fix build on x86_64

* Fri Mar 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.2-1mdk
- 0.8.2

* Thu Mar 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6-1mdk
- 0.6
- Integrate my other patchs

* Wed Mar 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.5-1mdk
- 0.5
- Remove all my patch (all was add into release 0.5)

* Wed Mar 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.3-7mdk
- Add patch7: disable action when is not root

* Wed Mar 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.3-6mdk
- Add patch6: fix rootonly

* Wed Mar 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.3-5mdk
- Fix menu entry

* Wed Mar 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.3-4mdk
- Add patch5: fix reference

* Wed Mar 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.3-3mdk
- Add patch4: fix crash when "themes" doesn't exist

* Wed Mar 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.3-2mdk
- Add patch3: fix mem leak
- Fix url

* Wed Mar 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.3-1mdk
- First package

