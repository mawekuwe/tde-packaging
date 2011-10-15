Name: pinentry
Version: 0.8.0
Release: %mkrel 7
Summary: Collection of simple PIN or passphrase entry dialogs
Source0: ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.gz
Source1: %{SOURCE0}.sig
Source2: pinentry-wrapper
Patch0:  0001-Fix-pinentry-gtk-2-SIGSEGV-when-unfocusing-with-g-ar.patch
Patch1:  0002-Fix-sigabrt-on-fail-grab-r229.patch
Patch2:  0003-pinentry-gtk-x11-race.patch  
Patch3:  0004-Fix-qt4-pinentry-window-created-in-the-background.patch
License: GPLv2+
Group: System/Kernel and hardware
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.gnupg.org/
Requires(post): info-install
Requires(preun):info-install
BuildRequires: libgtk+2.0-devel
BuildRequires: libcap-devel
BuildRequires: ncurses-devel
BuildRequires: qt4-devel
BuildRequires: gettext-devel
Obsoletes:     %name-curses < 0.8.0-2

%description 
%{name} is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project.

%pre
%{_sbindir}/update-alternatives --remove pinentry %{_bindir}/pinentry-curses ||:
%{_sbindir}/update-alternatives --remove pinentry %{_bindir}/pinentry-gtk ||:
%{_sbindir}/update-alternatives --remove pinentry %{_bindir}/pinentry-qt ||:
%{_sbindir}/update-alternatives --remove pinentry %{_bindir}/pinentry-qt4 ||:

%files 
%defattr(-,root,root)
%doc README TODO ChangeLog NEWS AUTHORS THANKS
%{_bindir}/pinentry
%{_bindir}/pinentry-curses
%{_infodir}/*.info*

#-----------------------------------------------------------------------------------------

%package gtk2
Summary: GTK+ interface of pinentry
Group: System/Kernel and hardware
Provides: %{name}-gui = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Obsoletes: pinentry-gtk

%description gtk2
%{name} is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project.

This package provides GTK+ interface of the dialog.

%files gtk2
%defattr(-,root,root)
%_bindir/pinentry-gtk-2

#-----------------------------------------------------------------------------------------

%package qt4
Summary: QT4 interface of pinentry
Group: System/Kernel and hardware
Provides: %{name}-gui = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Obsoletes: %name-qt < 0.7.6-3

%description qt4
%{name} is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project.

This package provides QT4 interface of the dialog.

%files qt4
%defattr(-,root,root)
%{_bindir}/pinentry-qt*


#-----------------------------------------------------------------------------------------
%package qt3
Summary: QT3 interface of pinentry
Group: System/Kernel and hardware
Provides: %{name} = %{version}-%{release}
Provides: %{name}-qt = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
BuildRequires: qt3-devel

%description qt3
%{name} is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project.

This package provides QT3 interface of the dialog.

%post qt3
update-alternatives --install /usr/bin/pinentry pinentry /usr/bin/pinentry-qt 1
 --slave /usr/bin/pinentry-qt pinentry-qt /usr/bin/pinentry-qt

%postun qt3
if [ "$1" = "0" ]; then
   update-alternatives --remove pinentry /usr/bin/pinentry-qt3
fi

%files qt3
%defattr(-,root,root)
%{_bindir}/pinentry-qt

#-----------------------------------------------------------------------------------------

%prep
%setup -q 
%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p1

%build
./autogen.sh

%configure2_5x \
	--disable-pinentry-gtk \
        --enable-pinentry-qt \
        --with-qt-dir=%qt3dir \
	--enable-pinentry-qt4 \
	--enable-pinentry-gtk2 \
    --with-qt4-dir=%qt4dir \
	--disable-rpath

%make
%install
rm -rf %{buildroot}
%makeinstall_std

#Remove link we will use update alternative
rm -f %{buildroot}%{_bindir}/pinentry

install -p -m755 -D %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/pinentry 

pushd $RPM_BUILD_ROOT%{_bindir}
#ln -s pinentry-qt4 pinentry-qt
popd

%clean
rm -rf %{buildroot}




%changelog
* Mon Jul 28 2011 Tim Williams <tim@my-place.org.uk> 0.8.0-7mdv2010.2
+ Rebuild for Trinity repo

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 0.8.0-6mdv2010.1
+ Restore qt3 package due to KDE3 sanity...

* Thu May 13 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.8.0-5mdv2010.1
+ Revision: 544667
- Add fedora patches fixing segfault in the gtk pinentry
- Fix pinentry-qt4 showing in background

* Wed Mar 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.8.0-3mdv2010.1
+ Revision: 530268
- Add a symlink for pinentry-qt ( Bug #58457 )
- Remove qt3 support

* Fri Mar 05 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.8.0-2mdv2010.1
+ Revision: 514581
- Use patch from fedora to handle no display settings (Bug #46841 )
  Add a pinentry-gui provide to qt4 qt and gtk2 subpackages

* Wed Mar 03 2010 Frederik Himpe <fhimpe@mandriva.org> 0.8.0-1mdv2010.1
+ Revision: 513991
- Update to new version 0.8.0
- Remove patch to build with QT 4.5: integrated upstream

* Thu Sep 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.7.6-3mdv2010.0
+ Revision: 444182
- Obsolete qt3 packages

* Tue Sep 15 2009 Helio Chissini de Castro <helio@mandriva.com> 0.7.6-2mdv2010.0
+ Revision: 443111
- Make teuf happy. ( And obsoletes pinentry-qt )

* Tue Jul 14 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.6-1mdv2010.0
+ Revision: 395922
- Update to new version 0.7.6
- Remove patches integrated upstream
- Add moc patch to fix build with QT 4.5

* Thu Mar 26 2009 Frederic Crozat <fcrozat@mandriva.com> 0.7.5-7mdv2009.1
+ Revision: 361357
- Add missing buildrequires on gettext-devel

  + Helio Chissini de Castro <helio@mandriva.com>
    - Restore qt3 package due t kde3 insanity...
    - Fixed last bit of curses fallback on pinentry-qt4 dialog
    - Make qt4 pinentry dialog automake complaint, avoiding duplicate os secdring code and allowing to fallback on curses
      if no display is available, like their counterparts.

* Wed Jan 07 2009 Helio Chissini de Castro <helio@mandriva.com> 0.7.5-4mdv2009.1
+ Revision: 326682
- We should made old binary names available in case user decided put the explicit binary name in their gpg.conf,
  pointing to pinentry-qt and pinentry-gtk instead of have it clean allowing gpg-agent programs like use the
  standard /usr/bin/pinentry ( which is handled by alternatives in Mandriva ).
  Since new packages obsolete old ones, is possible to add a slave for the alternatives rule linking old names, solving the upgrade path issue.

* Mon Jan 05 2009 Helio Chissini de Castro <helio@mandriva.com> 0.7.5-3mdv2009.1
+ Revision: 325155
- Rediff gtk transient patch
- Disable qt3 vuild
- Added pinentry qt4 from kde playground svn. Dialog ui need some love.
- Move name gtk to gtk2 and obsolete old pinentry-gtk ( was gtk2 already )
- qt4 package obsoletes old pinentry-qt

* Mon Jul 07 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.5-2mdv2009.0
+ Revision: 232371
- rebuilt against new libcap

* Mon Mar 17 2008 Olivier Blin <oblin@mandriva.com> 0.7.5-1mdv2008.1
+ Revision: 188312
- do not remove alternatives in postun if the package is not removed
- move pinentry-curses in a new pinentry-curses package to make
  pinentry a virtual package (so that qt/gtk versions can be selected
  when pinentry is required)
- realize the window as transient if keyboard is grabbed (from upstream SVN)
- fix keyboard grab (from Gentoo)
- fix build with latest glib that broke g_malloc API (from upstream ML)
- restore BuildRoot

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - drop not applied patch
    - set buildrequires on libcap-devel
    - new version
    - new license policy

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 11 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.4-1mdv2008.1
+ Revision: 117509
- new version

* Mon Sep 10 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.7.3-2mdv2008.0
+ Revision: 84038
- fix broken info entry (P0, should fix #32534)
- $QTLIB is already set by /etc/profile.d/qt3.sh, so don't set it in spec

* Thu Jul 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.3-1mdv2008.0
+ Revision: 55628
- correct configure options
- nuke rpath
- update to the latest version
- Import pinentry



* Mon Sep 18 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.7.2-6mdv2007.0
- Rebuild

* Fri Jul 28 2006 Laurent MONTEL <lmontel@mandriva.com> 0.7.2-5
- Add patch to disable gtk-1.2 support

* Mon Jun 19 2006 Laurent MONTEL <lmontel@mandriva.com> 0.7.2-4
- Add patch from Rapha�l Gertz to use update-alternative 

* Fri Feb 24 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.7.2-3mdk
- Add Requires(post|preun): fix ticket #17416
- use mkrel

* Sat May 28 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.7.2-2mdk
- add BuildRequires: libgtk+2.0-devel

* Tue May 17 2005 Laurent MONTEL <lmontel@mandriva.com> 0.7.2-1mdk
- 0.7.2

* Mon Mar 14 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.7.1-4mdk
- fix build on lib64 platforms

* Tue Mar 08 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.7.1-3mdk
- Rebuild

* Sat Jun 19 2004 Abel Cheung <deaddog@deaddog.org> 0.7.1-2mdk
- Rebuild with new gcc

* Thu May 20 2004 Abel Cheung <deaddog@deaddog.org> 0.7.1-1mdk
- New version
- Don't build against libcap

* Sat Jan 24 2004 Abel Cheung <deaddog@deaddog.org> 0.7.0-1mdk
- New version
- Enable all interfaces

* Fri Nov 14 2003 Florin <florin@mandrakesoft.com> 0.6.9-2mdk
- rebuild

* Wed Apr 30 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.9-1mdk
- Update version

* Tue Feb 18 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.8-1mdk
- Update and fix spec file thanks to <fabrice-marie-sec@ifrance.com>

* Tue Jan 28 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.6-2mdk
- Fix link as report Jason Straight <jason@JeetKuneDoMaster.net>

* Wed Dec 11 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.6-1mdk
- update spec file from Fabrice MARIE <fabrice-marie-sec@ifrance.com>

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.5-1mdk
- Initial package
