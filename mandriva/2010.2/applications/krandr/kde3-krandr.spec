%define oname krandr
Name: kde3-%{oname}
Summary: Applet for configuring screen size and rotation
Version: 0.5.2.1
Release: %mkrel 19
License: GPL
Group: Graphical desktop/KDE3
URL: http://git.mandriva.com/?p=projects/%{oname}.git
Source0:  %{oname}-%{version}.tar.gz
Patch0: %{oname}-0.5.2.1-legacy_randr_on_single_output.patch
Patch1: %{oname}-0.5.2-display_switch.patch
Patch2: %{oname}-0.5.2.1-fix_rrate_display.patch
Patch3: %{oname}-0.5.2.1-fix_autostart.patch
Patch4: %{oname}-0.5.2.1-add-mandriva-translations.patch
Patch5: %{oname}-0.5.2.1-change_the_way_crtcs_are_set.patch
Patch6: %{oname}-0.5.2.1-grab_server_avoiding_crashes.patch
Patch7: %{oname}-0.5.2.1-flush_after_ungrab.patch
Patch8: kde-3.5.10-acinclude.patch
Patch9: fix_autotools.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: kde3-macros
BuildRequires: automake >= 1.6.1
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%else
BuildRequires: autoconf >= 1:2.65
%endif
BuildRequires: qt3-devel >= 3.3.3
BuildRequires: kdelibs-devel
BuildRequires: kde3-macros
Conflicts: kdebase-common <= 1:3.5.7-18mdv2008.0
Conflicts: libkdebase4 <= 1:3.5.7-20mdv2008.0
Provides: %{oname} = %version-%release
Obsoletes: %{oname}

%description
KRandr is an applet for configuring screen size and rotation through the XRandR
extension.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1 -b .legacyrandr
%patch1 -p1 -b .displayswitch
%patch2 -p1 -b .rrate_display
%patch3 -p1 -b .fix_autostart
%patch4 -p1 -b .test_translations
%patch5 -p1 -b .crtc_set
%patch6 -p1 -b .grab_server
%patch7 -p1 -b .flush_after_ungrab
%if %mdkversion >= 201000
%patch8 -p1
%patch9 -p1
%endif

%build
%define _disable_ld_no_undefined 1
make -f admin/Makefile.common cvs
%configure_kde3
%make

%install
rm -rf %buildroot
%makeinstall_std

# install %{oname}tray in kde autostart
install -d -m 0755 %{buildroot}%{_kde3_datadir}/autostart
cp -f %{buildroot}%{_kde3_datadir}/applications/kde/%{oname}tray.desktop %{buildroot}%{_kde3_datadir}/autostart/

%files
%defattr(-,root,root)
%{_kde3_bindir}/%{oname}tray
%{_kde3_libdir}/kde3/kcm_randr.*
%{_kde3_datadir}/applications/kde/%{oname}tray.desktop
%{_kde3_datadir}/applnk/.hidden/randr.desktop
%{_kde3_datadir}/autostart/%{oname}tray.desktop
# remove the non wanted files
%exclude %{_kde3_datadir}/doc/HTML/en/%{oname}
%exclude %{_kde3_datadir}/locale/*/LC_MESSAGES/%{oname}.mo


%changelog
* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 0.5.2.1-19mdv2010.1
+ Rebuild for MDV 2010.2/Trinity

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 0.5.2.1-18mdv2010.1
+ Rebuild for MDV 2010.1

* Fri Feb 12 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.5.2.1-17mdv2010.0
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65
- Rename package name and group to avoid possible future kde4 conflicts

* Fri Nov 13 2009 Tim Williams <tim@my-place.org.uk> 0.5.2.1-16mdv2010.0
+ Rebuild for MDV 2010.0

* Tue Jul 22 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.2.1-15mdv2009.0
+ Revision: 240518
- Flush the X calls after calling XUngrabServer to avoid deadlocks

* Sat Jun 14 2008 Anssi Hannula <anssi@mandriva.org> 0.5.2.1-14mdv2009.0
+ Revision: 219126
- rebuild to get higher evr than 2008.1 updates (needed for kde4 conflicts)

* Mon May 05 2008 Helio Chissini de Castro <helio@mandriva.com> 0.5.2.1-13mdv2009.0
+ Revision: 201520
- Update %{oname} to new build of moved kde3

* Mon Mar 31 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.2.1-12mdv2008.1
+ Revision: 191318
- Grab the X server in order for the changes to be atomic

* Fri Mar 28 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.2.1-11mdv2008.1
+ Revision: 190977
- Fix the way the screen are upper-sized when the resolution of the CRTC is
  changed. This avoids kicker and kwin getting lost on parsing X events.

* Mon Mar 10 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.5.2.1-10mdv2008.1
+ Revision: 183618
- fix description

* Mon Mar 10 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.2.1-9mdv2008.1
+ Revision: 183512
- Use the correct autostart condition so that it is actually started (#38455)

* Fri Feb 22 2008 Nicolas Lécureuil <neoclust@mandriva.org> 0.5.2.1-8mdv2008.1
+ Revision: 174021
- Add translations for mandriva strings

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5.2.1-7mdv2008.1
+ Revision: 141739
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 03 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.2.1-6mdv2008.0
+ Revision: 94865
- Make it possible to disable %{oname} autostart (#34378)

* Fri Sep 28 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.2.1-5mdv2008.0
+ Revision: 93579
- Make %{oname} start at session startup (#34047)
- Remove the dummy documentation files

* Mon Sep 17 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.2.1-4mdv2008.0
+ Revision: 89338
- Fix displaying of refresh rates (#33710)

* Thu Sep 13 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.2.1-3mdv2008.0
+ Revision: 85303
- add a display switch shortcut
- add proper conflicts to libkdebase4 (#32957)

* Wed Sep 12 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.2.1-2mdv2008.0
+ Revision: 84651
- Use the legacy randr interface when there is only one output available
  (mostly drivers that do not support RandR1.2 yet)

* Tue Aug 28 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.5.2.1-1mdv2008.0
+ Revision: 72849
- Fix group and point the URL to the git repository of %{oname}
- Import %{oname}

