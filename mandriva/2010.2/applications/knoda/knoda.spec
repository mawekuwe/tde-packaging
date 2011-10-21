# THIS PACKAGE IS HOSTED AT MANDRIVA SVN
# PLEASE DO NOT UPLOAD DIRECTLY BEFORE COMMIT

%define LIBMAJ 0
%define libname %mklibname %name %LIBMAJ
%define develname %mklibname %name -d

%define name knoda
%define version 0.8.3
%define hk_version 0.8.3
%define release %mkrel 10

Summary:	Database frontend for KDE
Name:		%{name}
Version:        %{version}
Release:        %{release}
License:	GPL
Group:		Databases

Source:		http://hk-classes.sourceforge.net/%{name}-%{version}.tar.bz2
Source1:	http://hk-classes.sourceforge.net/%{name}python.tar.bz2
Source2:	lo48-app-knoda.png
Patch0:		knoda-0.8.3-remove-fr-comment.patch
Patch1:		knoda-0.8.3-fix-icon-ext.patch
Url:		http://www.knoda.org
BuildRoot:	%_tmppath/%name-%version-root

BuildRequires:	hk_classes-devel = %{hk_version} 
BuildRequires:	kdelibs-devel 
BuildRequires:  python-devel
BuildRequires:	desktop-file-utils

Requires: 	hk_classes = %{hk_version} 
Obsoletes:      %{libname}

%description
Knoda is a database frontend for KDE. It is based on hk_classes.
Knoda allows you to:

 * define and delete databases;
 * create, alter and delete tables and indices;
 * add, change and delete data in tables;
 * define, execute and store sql queries;
 * import and export CSV data;
 * define and use forms; and
 * define and print reports

Its driver concept allows a uniform connection to different database 
servers.

Note: If you've used knoda 0.6, you'll probably want to delete 
~/.hk_classes/preferences, as the driver paths have changed.

%package devel
Summary:        Headers for hk_kdeclasses application development
Group:          Development/Databases
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{libname}-devel
Obsoletes:	%{develname}

%description devel
Hk_kdeclasses headers for application development


%prep
%setup -q -a 1 -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
%configure_kde3 --disable-final \
  --with-hk_classes-dir=%{_libdir}/hk_classes \
  --with-hk_classes-incdir=%{_includedir}/hk_classes
%make 

%install
rm -rf %{buildroot}
%makeinstall_std

# (sb) get rid of CVS in python docs
rm -rf %{name}python/common/CVS

mkdir -p $RPM_BUILD_ROOT%{_kde3_datadir}/applications/kde
desktop-file-install --vendor="" --delete-original \
	--dir $RPM_BUILD_ROOT%{_kde3_datadir}/applications/kde \
	$RPM_BUILD_ROOT%{_kde3_datadir}/applnk/Office/%{name}.desktop

%find_lang %name --with-html

%if %mdkversion < 200900
%post
%update_menus
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%{update_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
rm -fr %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc ChangeLog COPYING NEWS INSTALL README
%doc %{name}python/*
%{_kde3_bindir}/*
%{_kde3_datadir}/applications/kde/%{name}.desktop
%{_kde3_datadir}/apps/hk_kdeclasses
%{_kde3_datadir}/apps/%{name}
%{_kde3_datadir}/config/magic/*.magic
%{_kde3_datadir}/mimelnk/application/*.desktop
%{_kde3_iconsdir}/*/*/apps/*.png
%{_kde3_datadir}/services/hk_kde*.desktop
%{_kde3_libdir}/*

%files devel
%defattr(-,root,root)
%{_kde3_includedir}/*


%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 0.8.3-9mdv2010.2
+ Rebuild for Trinity

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 0.8.3-9mdv2010.1
+ Rebuild for MDV 2010.1

* Tue Nov 24 2009 Tim Williams <tim@my-place.org.uk> 0.8.3-8mdv2010.0
+ Rebuild for MDV 2010.0

* Thu Jul 31 2008 Funda Wang <fundawang@mandriva.org> 0.8.3-7mdv2009.0
+ Revision: 257899
- switch to /opt

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.8.3-5mdv2008.1
+ Revision: 170929
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Oct 23 2007 Funda Wang <fundawang@mandriva.org> 0.8.3-4mdv2008.1
+ Revision: 101432
- cleanup spec file
- fix desktop file icon ext
- drop libpackage as it is wrongly introduced.

* Sat Sep 01 2007 Funda Wang <fundawang@mandriva.org> 0.8.3-3mdv2008.0
+ Revision: 77297
- Remove invalid fr comment of menu entry

* Fri Aug 10 2007 Funda Wang <fundawang@mandriva.org> 0.8.3-2mdv2008.0
+ Revision: 61513
- don't use chrpath

* Tue Jun 26 2007 Funda Wang <fundawang@mandriva.org> 0.8.3-1mdv2008.0
+ Revision: 44338
- new develpackage policy
  drop old menu

  + Per Ã˜yvind Karlsen <peroyvind@mandriva.org>
    - update to 0.8.3
    - wipe out buildroot before install


* Mon Jan 15 2007 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.8.2-1mdv2007.0
+ Revision: 109306

  + Lenny Cartier <lenny@mandriva.com>
    - Update to 0.8.2

* Mon Jul 10 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.8.1-1mdv2007.0
+ Revision: 38589
- Fix xdg menu
- right require on hk_version
- 0.8.1
- Fix Menu for xdg
- Use macros
- Increase release
- Fix menu
- Use macros
- import knoda-0.8-1mdk

* Sun Dec 11 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.8-1mdk
- 0.8
- fix build on x86_64

* Wed Oct 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.4-6mdk
- Rebuild

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.4-5mdk
- BuildRequires fix

* Sun Sep 18 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.4-4mdk
- Fix Requires

* Wed Jul 13 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.4-3mdk
- Rebuild for new hk_classes

* Tue Jul 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.4-2mdk
- Remove conflict : i suxx

* Sat Jul 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.4-1mdk
- 0.7.4
- Fix conflicts with mandrake-mime BR: 16672

* Sat Apr 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7.4-0.test1.1mdk
- New release 0.7.4-test1

* Mon Feb 07 2005 Stew Benedict <sbenedict@mandrakesoft.com> 0.7.2-2mdk
- rebuild for new python

* Tue Nov 30 2004 Stew Benedict <sbenedict@mandrakesoft.com> 0.7.2-1mdk
- 0.7.2, make sure it requires hk_classes with the same version
- roll python-knoda into the main package, since it's just docs

* Sat Oct 02 2004 Stew Benedict <sbenedict@mandrakesoft.com> 0.7.1-2mdk
- fix crash bug (missing /usr/lib/kde3/libhk*.la files - #11863)

* Fri Sep 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.7.1-1mdk
- 0.7.1

* Thu Jun 17 2004 Stew Benedict <sbenedict@mandrakesoft.com> 0.6.3-2mdk
- rebuild, patch to build with gcc-3.4.1 (patch0, extra ";"s)
- some rpmlint fixes

* Thu Apr 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.3-1mdk
- 0.6.3

