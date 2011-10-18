%define oname kde-i18n-es

Name: kde3-i18n-es
Summary: Spanish language support for KDE3
Version:  3.5.10
Release: %mkrel 5
Group: System/Internationalization
License: GPL
URL: http://www.kde.org
Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/kde-i18n/%oname-%version.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
Requires: locales-es
BuildArch: noarch
BuildRequires: freetype2 
BuildRequires: gettext 
BuildRequires: kdelibs-devel kde3-macros 
BuildRequires: texinfo
Obsoletes: kde-i18n-es3
Provides: kde-i18n-es = %version-%release
Provides: kde-i18n-es3
Provides: kde-l10n = %version
Obsoletes: kde-i18n-es
Provides: kde-i18n-es = %version-%release

%description
Spanish language support for KDE3.

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
* Mon Jul 18 2011 Tim Williams <tim@my-place.org.uk> 3.5.10-5mvt2010.2
+ Repackage for Trinity

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 3.5.10-4mvt2010.0
+ Repackage for MDV 2010.1

* Mon Feb 22 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 3.5.10-3mvt2010.0
+ Packaged for mdv 2010.0
- Change package name to avoid future KDE4 conflicts

* Fri Sep 05 2008 Funda Wang <fundawang@mandriva.org> 3.5.10-2mdv2009.0
+ Revision: 281405
- versioned provides

* Wed Sep 03 2008 Funda Wang <fundawang@mandriva.org> 3.5.10-1mdv2009.0
+ Revision: 279502
- New version 3.5.10

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.5.9-6mdv2009.0
+ Revision: 267460
- rebuild early 2009.0 package (before pixel changes)

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.9-5mdv2009.0
+ Revision: 203879
- Move to /opt

* Fri Feb 15 2008 Olivier Blin <oblin@mandriva.com> 3.5.9-1mdv2008.1
+ Revision: 169037
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Funda Wang <fundawang@mandriva.org> 3.5.8-1mdv2008.1
+ Revision: 98995
- New version 3.5.8

* Fri May 18 2007 Helio Chissini de Castro <helio@mandriva.com> 3.5.7-5mdv2008.0
+ Revision: 27716
- KDE i18n packages should not own whole i18n subsystem and kde apps data dirs. Thanks to Olivier Blin by report this one.

* Thu May 17 2007 Helio Chissini de Castro <helio@mandriva.com> 3.5.7-4mdv2008.0
+ Revision: 27666
- Fixed spec using sane file list and correct name from tarball
- Update for forthcoming 3.5.7


* Mon Feb 05 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-2mdv2007.0
+ Revision: 116203
- Fix spec file
- 3.5.6

* Mon Nov 06 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-2mdv2007.0
+ Revision: 76978
- Fix file list
- 3.5.5
- Import kde-i18n-es

* Fri Aug 04 2006 Laurent MONTEL <lmontel@mandriva.com> 3.5.4-1
- 3.5.4

* Fri Jun 02 2006 Laurent MONTEL <lmontel@mandriva.com> 3.5.3-1
- 3.5.3

* Sun May 28 2006 Laurent MONTEL <lmontel@mandriva.com> 3.5.2-3
- Use %%mkrel

* Tue Apr 18 2006 Laurent MONTEL <lmontel@mandriva.com> 3.5.2-1mdk
- 3.5.2

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

* Thu Jun 02 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.1-1mdk
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

* Thu Oct 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-2mdk
- Update from CVS

* Fri Sep 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-1mdk
- KDE 3.3.0

* Fri Aug 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-2mdk
- Sync with CVS

* Thu Jun 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Sun Apr 18 2004 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 3.2.0-5mdk
- fix buildrequires
- fix obsoletes-not-provided
- spec cosmetics

* Thu Mar 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.0-4mdk
- Tarball was bad generated, it removed all kdevelop files

* Thu Feb 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.0-2mdk
- Sync with CVS

