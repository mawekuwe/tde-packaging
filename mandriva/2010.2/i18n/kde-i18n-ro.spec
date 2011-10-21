%define oname kde-i18n-ro

Name: kde3-i18n-ro
Summary: Romanian language support for KDE3
Version:  3.5.10
Release: %mkrel 5
Group: System/Internationalization
License: GPL
URL: http://www.kde.org/
Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/kde-i18n/%oname-%version.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
Requires: locales-ro
BuildArch: noarch
BuildRequires: freetype2 
BuildRequires: gettext 
BuildRequires: kdelibs3-devel kde3-macros 
BuildRequires: texinfo
Obsoletes: kde-i18n-ro3
Provides: kde-i18n-ro = %version-%release
Provides: kde-i18n-ro3
Provides: kde-l10n = %version
Obsoletes: kde-i18n-ro
Provides: kde-i18n-ro = %version-%release

%description
Romanian language support for KDE3.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure_kde3

make clean
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -fr %buildroot

%files
%defattr(-,root,root,-)
%_kde3_datadir/locale/*/LC_MESSAGES/*
%_kde3_datadir/locale/*/flag.png
%_kde3_datadir/locale/*/charset
%_kde3_datadir/locale/*/entry.desktop
%_kde3_appsdir/*
%doc %_kde3_docdir/HTML/*/*


%changelog
* Wed Jul 21 2011 Tim Williams <tim@my-place.org.uk> 3.5.10-5mvt2010.2
+ Repackage for Trinity

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 3.5.10-4mvt2010.1
+ Repackage for MDV 2010.1

* Mon Feb 22 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 3.5.10-3mvt2010.0
+ Packaged for mdv 2010.0
- Change package name to avoid future KDE4 conflicts

* Fri Sep 05 2008 Funda Wang <fundawang@mandriva.org> 3.5.10-2mdv2009.0
+ Revision: 281432
- versioned provides

* Thu Sep 04 2008 Funda Wang <fundawang@mandriva.org> 3.5.10-1mdv2009.0
+ Revision: 280080
- New version 3.5.10

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.5.9-6mdv2009.0
+ Revision: 267662
- rebuild early 2009.0 package (before pixel changes)

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.9-5mdv2009.0
+ Revision: 204024
- Move to /opt

* Sat Feb 16 2008 Olivier Blin <oblin@mandriva.com> 3.5.9-1mdv2008.1
+ Revision: 169181
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 17 2007 Funda Wang <fundawang@mandriva.org> 3.5.8-1mdv2008.1
+ Revision: 99687
- New version 3.5.8

* Fri May 18 2007 Helio Chissini de Castro <helio@mandriva.com> 3.5.7-5mdv2008.0
+ Revision: 27751
- KDE i18n packages should not own whole i18n subsystem and kde apps data dirs. Thanks to Olivier Blin by report this one.
- Update for forthcoming 3.5.7


* Fri Jan 26 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-1mdv2007.0
+ Revision: 113664
- 3.5.6

* Thu Nov 02 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-1mdv2007.1
+ Revision: 75238
- 3.5.5
- Import kde-i18n-ro

* Fri Aug 04 2006 Laurent MONTEL <lmontel@mandriva.com> 3.5.4-1
- 3.5.4

* Fri Jun 02 2006 Laurent MONTEL <lmontel@mandriva.com> 3.5.3-1
- 3.5.3

* Sun May 28 2006 Laurent MONTEL <lmontel@mandriva.com> 3.5.2-3
- Use %%mkrel

* Tue Apr 18 2006 Laurent MONTEL <lmontel@mandriva.com> 3.5.2-1mdk
- 3.5.2

* Wed Feb 01 2006 Laurent MONTEL <lmontel@mandriva.com> 3.5.1-1mdk
- 3.5.1

* Tue Nov 29 2005 Laurent MONTEL <lmontel@mandriva.com> 3.5.0-10mdk
- Real kde-3.5.0

* Mon Nov 14 2005 Laurent MONTEL <lmontel@mandriva.com> 3.5.0-1mdk
- 3.5.0 (named rc1)

* Tue Oct 18 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.92-1mdk
- 3.5beta2

* Fri Jul 29 2005 Laurent MONTEL <lmontel@mandriva.com> 10mdk
- Fix provides kde-l10n

* Sat Jul 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.2-1mdk
- 3.4.2

* Fri Jun 10 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.1-1mdk
- 3.4.1

* Wed Mar 30 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0

* Tue Mar 22 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-30mdk
- Update translate

* Thu Feb 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-20mdk
- update from translation

* Fri Feb 04 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-10mdk
- Update from CVS and add kpdf translate from CVS

* Tue Nov 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Fri Sep 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-3mdk
- Add kdepim kde3.3 translation

* Fri Aug 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-2mdk
- Sync with CVS

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Sun Apr 18 2004 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 3.2.1-2mdk
- fix buildrequires
- fix obsoletes-not-provided
- spec cosmetics

* Sat Apr 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

* Thu Mar 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.0-4mdk
- Tarball was bad generated, it removed all kdevelop files

* Thu Feb 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.0-2mdk
- Sync with CVS

* Tue Feb 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.0-1mdk
- 3.2

* Fri Jan 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-0.1mdk
- Fix for package freeze

