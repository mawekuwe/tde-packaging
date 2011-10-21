Name: kde3-macros
Version: 3.5.12
Release: %mkrel 1
Group: Development/KDE and Qt
Summary: Base install macros for kde 3
Source: kde3.macros
URL: http://www.mandriva.com
License: GPL
BuildArch: noarch
Requires: rpm-manbo-setup-build >= 2-7
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Base install macros for kde 3

%files 
%defattr(-,root,root)
%_sysconfdir/rpm/macros.d/kde3.macros

%install
rm -rf %buildroot
install -d -m 755 %buildroot%_sysconfdir/rpm/macros.d
install -m 644 %SOURCE0 %buildroot%_sysconfdir/rpm/macros.d/

%clean
rm -rf %buildroot




%changelog
* Thu Feb 16 2011 Tim Williams <tim@my-place.org.uk> 3.5.12-1mvt2010.1
+ Rebuild for Trinity 3.5.12
+ Add extra-libs and extra-includes so build can find tqtinterface
+ Add --enable-closure

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 3.5.10-5mvt2010.1
+ Rebuild for MDV 2010.1

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 3.5.10-4mdv2010.0
+ Rebuild for MDV 2010.0

* Mon Oct 27 2008 Funda Wang <fundawang@mandriva.org> 3.5.10-3mdv2009.1
+ Revision: 297523
- specify qt3 dir

* Wed Sep 24 2008 Funda Wang <fundawang@mandriva.org> 3.5.10-2mdv2009.0
+ Revision: 287688
- add libdir to pkgconfig dir

* Tue Sep 16 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.10-1mdv2009.0
+ Revision: 285306
- Update version and fix bug 43876 - /etc/profile.d/91kde3.sh should contain redefination of PKG_CONFIG_PATH

* Wed Aug 06 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.5.9-15mdv2009.0
+ Revision: 264759
- rebuild early 2009.0 package (before pixel changes)

* Fri Jun 06 2008 Funda Wang <fundawang@mandriva.org> 3.5.9-14mdv2009.0
+ Revision: 216405
- Requires rpm-manbo-setup-build for %%before_configure

* Thu Jun 05 2008 Funda Wang <fundawang@mandriva.org> 3.5.9-13mdv2009.0
+ Revision: 215104
- change configure_kde3 to use %%before_configure

* Fri May 30 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.9-12mdv2009.0
+ Revision: 213551
- Proper new qtdir libraries

* Wed May 28 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.9-11mdv2009.0
+ Revision: 212725
- Revert of the previous commit

* Wed May 28 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.9-10mdv2009.0
+ Revision: 212717
- Fix macros

* Fri May 09 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.9-9mdv2009.0
+ Revision: 205308
- Fix typo

* Thu May 08 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.9-8mdv2009.0
+ Revision: 204698
- Add clean_kde3_icon_cache and update_kde3_icon_cache macros

* Sat May 03 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.9-7mdv2009.0
+ Revision: 200791
- Yes, we need a copy. Sometimes we loose a lot of time that we don't have
  because some nitpicking pointing.

* Sat May 03 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.9-6mdv2009.0
+ Revision: 200553
- Using again configure2_5x. Some impatient people can't wait some work in progress...

* Sat May 03 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.9-4mdv2009.0
+ Revision: 200535
- Added xinerama and alsa

* Sat May 03 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.9-3mdv2009.0
+ Revision: 200534
- Added mitshm and enable-libfam

* Fri May 02 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.9-2mdv2009.0
+ Revision: 200518
- Created configure_kde macro to make kde3 build easier too like kde4 and make transition to /opt less painfull. Thanks to Blino for the help.
  There's no need anymore add all define switches, even for libsuffix detection, so if you want:
- Disable enable-final: use --define _disable_final=1
- Compile with debug full: use --define _unstable=1
- Compile in non 32bits arch: No need add the usual lib test

* Sun Apr 13 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.9-1mdv2009.0
+ Revision: 192655
- import kde3-macros


