%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define oname kdeadmin
%define lib_name_orig %mklibname kdeadmin
%define lib_major 1
%define lib_name %lib_name_orig%lib_major

Name: kde3-%{oname}
Version: 3.5.12
Release: %mkrel 1
Group: Graphical desktop/KDE3
Summary: K Desktop Environment - Adminstrative Tools
URL: ftp://ftp.kde.org/pub/kde/stable/%version/src/
Epoch: 2
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
Source1: kpackage.pamd
Patch0: kdeadmin-post-3.5.8-add-mandriva-support.patch
Patch1: kde-3.5.10-acinclude.patch
#Patch2: fix_autotools.patch
Patch3: kdebase-3.5.12-move-xdg-menu-dir.patch
BuildRoot:	%_tmppath/%name-%version-%release-root
License:	GPL
Provides:	kdeadmin3 = %epoch:%version-%release
Provides: 	%{oname} = %epoch:%version-%release
Obsoletes:	%{oname}
Obsoletes:	kdeadmin3
Obsoletes:	%lib_name < 2:3.5.9
Requires:	pciutils
BuildRequires: X11-devel 
BuildRequires: freetype2-devel 
BuildRequires: kdelibs-devel >= 3.2-13mdk
BuildRequires: bzip2-devel 
BuildRequires: jpeg-devel 
BuildRequires: lcms-devel 
BuildRequires: mng-devel
BuildRequires: png-devel 
BuildRequires: qt3-devel
BuildRequires: kde3-macros
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%endif
BuildRequires: autoconf >= 1:2.65
BuildRequires: automake > 1.5
BuildRequires: rpm-devel libz-devel
BuildRequires: pam-devel
# createmdkmenu
BuildRequires:	kdelibs-common >= 3.1.93-5mdk
%ifarch %{ix86} x86_64
BuildRequires:	lilo
%endif

%description
The kdeadmin package contains packages that usually only a system
administrator might need:
	- kcmlinuz
    	Linux Kernel configurator
	- kcron
    	Editor for the cron command scheduler.
	- kdat
   		Tape backup tool.
	- kfile-plugins
    	Make Konquerer display additional info on about *.dep and *.rpm files.
	- ksysv
    	An editor for System V startup schemes.
	- kuser
   		An user manager.
	- kwuftpd
   		Front end to the wu-ftpd FTP daemon.
	- lilo-config
    	A plugin for KControl to manage the Linux boot loader LILO.
	- secpolicy
    	A program to display PAM security policies.

%post
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kcron
%doc %_kde3_docdir/HTML/en/kuser
%doc %_kde3_docdir/HTML/en/kdat
%_kde3_datadir/applications/kde/kcron.desktop
%_kde3_datadir/applications/kde/kdat.desktop
%_kde3_datadir/applications/kde/kuser.desktop
%_kde3_bindir/kcron
%_kde3_bindir/kuser
%_kde3_bindir/secpolicy
%_kde3_bindir/kdat
%dir %_kde3_appsdir/kcron
%_kde3_appsdir/kcron/*
%dir %_kde3_appsdir/kuser/
%_kde3_appsdir/kuser/*
%dir %_kde3_appsdir/kdat
%_kde3_appsdir/kdat/*
%dir %_kde3_appsdir/knetworkconf/
%_kde3_appsdir/knetworkconf/*
%_kde3_datadir/config.kcfg/kuser.kcfg
%_kde3_datadir/services/*.desktop
%_kde3_datadir/applications/kde/kcm_knetworkconfmodule.desktop
%_kde3_libdir/kde3/kfile_*.*
%_kde3_libdir/pkgconfig/system-tools-backends.pc
%_kde3_libdir/kde3/kcm_knetworkconfmodule*
%doc %_kde3_docdir/HTML/en/knetworkconf/*.png
%doc %_kde3_docdir/HTML/en/knetworkconf/common
%doc %_kde3_docdir/HTML/en/knetworkconf/index.cache.bz2
%doc %_kde3_docdir/HTML/en/knetworkconf/index.docbook
%_kde3_iconsdir/*/*/*/*
%exclude %_kde3_iconsdir/*/*/*/ksysv.png

#------------------------------------------------------------------------	

%package -n %{name}-kpackage
Group:      Graphical desktop/KDE3
Summary:    Manager for DEB, RPM
Requires:   kde3-kdeadmin = %epoch:%version-%release
Obsoletes:  kpackage < 2:3.4.3 
Provides:   kde3-kpackage = %epoch:%version-%release
Provides:   kdeadmin3-kpackage = %epoch:%version-%release
Provides:   %{oname}-kpackage = %epoch:%version-%release
Obsoletes:  %{oname}-kpackage
Obsoletes:  kdeadmin3-kpackage


%description -n %{name}-kpackage
Kpackage is a package manager that is integrated into the K Desktop 
Environemnt.  It works with the KDE File Manager to manage DEB, RPM 
and Slackware tgz software packages.

%if %mdkversion < 200900
%post -n %{name}-kpackage
%update_menus
%endif

%if %mdkversion < 200900
%postun -n %{name}-kpackage
%clean_menus
%endif

%files -n %{name}-kpackage
%defattr(-,root,root)
%_kde3_bindir/kpackage
%dir %_sysconfdir/pam.d/
%config(noreplace) %_sysconfdir/pam.d/kpackage
%doc %_kde3_docdir/HTML/en/kpackage
%_kde3_iconsdir/*/*/*/kpackage.png
%_kde3_datadir/applications/kde/kpackage.desktop
%dir %_kde3_appsdir/kpackage
%_kde3_appsdir/kpackage/*

#------------------------------------------------------------------------	

%package -n %{name}-ksysv
Group:      Graphical desktop/KDE3
Summary:    Edit your SysV-style init configuration
Provides:   kde3-ksysv = %epoch:%version-%release
Provides:   kdeadmin3-ksysv = %epoch:%version-%release
Provides:   %{oname}-ksysv = %epoch:%version-%release
Obsoletes:  %{oname}-ksysv
Obsoletes:  kdeadmin3-ksysv


%description -n %{name}-ksysv
SysV-Init Editor lets you edit your SysV-style init configuration
using drag'n'drop.

%if %mdkversion < 200900
%post -n %{name}-ksysv
%update_menus
%endif

%if %mdkversion < 200900
%postun -n %{name}-ksysv
%clean_menus
%endif

%files -n %{name}-ksysv
%defattr(-,root,root)
%_kde3_bindir/ksysv
%dir %_kde3_appsdir/ksysv/
%_kde3_appsdir/ksysv/*
%_kde3_datadir/applications/kde/ksysv.desktop
%_kde3_appsdir/ksysv/*.rc
%_kde3_iconsdir/*/*/*/ksysv.png
%doc %_kde3_docdir/HTML/en/ksysv
%_kde3_datadir/mimelnk/application/x-ksysv.desktop
%_kde3_datadir/mimelnk/text/x-ksysv-log.desktop

#------------------------------------------------------------------------	

%ifnarch ppc
%package    lilo
Group:      Graphical desktop/KDE3
Summary:    Configure lilo
Requires:   kde3-kdeadmin = %epoch:%version-%release
Provides:   kdeadmin3-lilo = %epoch:%version-%release
Provides:   %{oname}-lilo = %epoch:%version-%release
Obsoletes:  %{oname}-lilo
Obsoletes:  kdeadmin3-lilo

%description lilo
lilo-config is a kcontrol plugin for configuring LILO, the most commonly
used Linux boot loader.

%if %mdkversion < 200900
%post lilo
%update_menus
%endif

%if %mdkversion < 200900
%postun lilo
%clean_menus
%endif

%files lilo
%defattr(-,root,root)
%_kde3_datadir/applications/kde/lilo.desktop
%doc %_kde3_docdir/HTML/en/lilo-config
%_kde3_libdir/kde3/kcm_lilo.*

%endif

#------------------------------------------------------------------------	

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p0
%if %mdkversion >= 201000
%patch1 -p1
#%patch2 -p1
%endif

%build
export QTDIR=%_prefix/lib/qt3

PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/
export xdg_menudir=%_sysconfdir/xdg/kde/menus

make -f admin/Makefile.common cvs

%configure_kde3 \
   --with-rpm \
   --with-pam=kde \
   --with-quota \
   --with-nis \
   --with-homeprefix=/home \
   --with-private-groups

%make


%install
rm -fr %buildroot

make install DESTDIR=%buildroot

# Install kdebase pam configuration file
install -d %buildroot/%_sysconfdir/pam.d
install -m644 %SOURCE1 %buildroot/%_sysconfdir/pam.d/kpackage

rm -rf %buildroot/%_kde3_datadir/applnk/Settings/Peripherals/

%ifarch ppc
rm -rf %buildroot/%_kde3_docdir/HTML/en/lilo-config
%endif

%clean
rm -fr %buildroot






%changelog

* Wed Jul 20 2011 Tim Williams <tim@my-place.org.uk> 2:3.5.12-1mvt2010.2
+ Update sources for Trinity
+ Add kdebase-3.5.12-move-xdg-menu-dir.patch
- Remove fix_autotools.patch

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 2:3.5.10-4mvt2010.1
+ Rebuild for MDV 2010.1

* Sun Jan 17 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 2:3.5.10-3mvt2010.0
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65:patch1
+ Fix automake 1.11 issue:patch2

* Fri Nov 13 2009 Tim Williams <tim@my-place.org.uk> 2:3.5.10-2mdv2010.0
+ Rebuild for MDV 2010.0
+ kdeadmin-post-3.5.8-add-mandriva-support.patch was failing - remade and fixed

* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 2:3.5.10-1mdv2009.0
+ Revision: 277481
- Update for last kde3 updates

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 2:3.5.9-5mdv2009.0
+ Revision: 267767
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 08 2008 Funda Wang <fundawang@mandriva.org> 2:3.5.9-4mdv2009.0
+ Revision: 216910
- Rebuild for new ldflags

* Mon May 19 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 2:3.5.9-3mdv2009.0
+ Revision: 209004
- User versioned obsoletes

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 2:3.5.9-2mdv2009.0
+ Revision: 204575
- Move to /opt

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 2:3.5.9-1mdv2008.1
+ Revision: 168995
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches integrated

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 31 2007 Oden Eriksson <oeriksson@mandriva.com> 2:3.5.8-2mdv2008.1
+ Revision: 139861
- rebuilt against openldap-2.4.7 libs

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add patch0 : it added the support of mandriva 2008.0
      and the upcoming 2008.1 in knetworkconf

* Wed Oct 24 2007 Nicolas Lécureuil <neoclust@mandriva.org> 2:3.5.8-1mdv2008.1
+ Revision: 101713
- Kde 3.5.8

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-ended-with-dot

* Thu Sep 20 2007 Nicolas Lécureuil <neoclust@mandriva.org> 2:3.5.7-3mdv2008.0
+ Revision: 91480
- Rebuild because of missing packages

* Wed Aug 08 2007 Funda Wang <fundawang@mandriva.org> 2:3.5.7-2mdv2008.0
+ Revision: 60515
- drop old menu

* Wed May 16 2007 Helio Chissini de Castro <helio@mandriva.com> 2:3.5.7-1mdv2008.0
+ Revision: 27453
- 3.5.7 release


* Thu Feb 01 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-1mdv2007.0
+ Revision: 115846
- 3.5.6

* Wed Jan 24 2007 Laurent Montel <lmontel@mandriva.com> 2:3.5.5-5mdv2007.1
+ Revision: 112738
- Not necessary
- Rebuild against new python

* Fri Nov 03 2006 Laurent Montel <lmontel@mandriva.com> 2:3.5.5-3mdv2007.1
+ Revision: 76120
- Add knetworkconf 2007.1 support
  (Bug found by Nicolas Chipaux)

* Fri Oct 20 2006 Laurent Montel <lmontel@mandriva.com> 2:3.5.5-2mdv2007.0
+ Revision: 71233
- 3.5.5
- Revert: "it's new lilo is supported by ppc ?????"

  + Helio Chissini de Castro <helio@mandriva.com>
    - Back to use branch tarballs. Now using post 3.5.5
    - Fixed cross compiling when using no-enable-final

* Sat Aug 12 2006 Laurent Montel <lmontel@mandriva.com> 2:3.5.4-3mdv2007.0
+ Revision: 55570
- New package (2006/08/11 3.5.4-3mdv)
  Add patch to fix knetworkconf signal/slot conflict

* Fri Aug 11 2006 Laurent Montel <lmontel@mandriva.com> 2:3.5.4-2mdv2007.0
+ Revision: 55299
- New package (2006/08/10 - 3.5.4-2mdv)
  knetworkconf: add support for Mandriva 2007
- 3.5.4
  New release (2006/08/02 3.5.4-1mdv)
--enable-new-ldflags doesn't work on x86_64
- 3.5.3
  Fix pamd files
- Rebuild for generate category in menu
- 3.5.2
- Fix build on ppc but reported by Christiaan Welvaart
- 3.5.1
- Enable debug only cooker
  MDK9.2 is obsolete now
- Real kde 3.5
- Complet fix of patch
- Fix kdenetwork conf to detect mandriva
- 3.5.0
- 3.4.92
- Fix build on x86_64 (gb patch)
- Rebuild
  Use %%mkrel
- Fix email
- Rebuild
- Remove debug
  Sync with kde 3.4.2 branch
- Rebuild for missing package
- 3.4.2

  + Helio Chissini de Castro <helio@mandriva.com>
    - Cleaned spec
    - Added tarball from kde branch as discussed on meeting in 28/06
    - Removed rpath and added configure macro invalidating libtoolize
    - We are Mandriva now
    - Uploading package ./kdeadmin

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 05 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-3mdk
- Rebuild with new GCC

* Tue Apr 12 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-2mdk
- Enable debug
- Use --enable-new-ldflags 
- Remove old patch

* Tue Apr 05 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0

* Thu Feb 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-6mdk
- Disable debug

* Fri Jan 28 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-5mdk
- Fix generated menu entry

* Mon Jan 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-4mdk
- Fix buildrequires for ppc

* Fri Dec 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-3mdk
- Fix category

* Wed Dec 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-2mdk
- Fix menu

* Fri Dec 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Wed Oct 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-3mdk
- Delete %%buildfor

* Wed Oct 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-2mdk
- Deprecated mdk < 9.2

* Fri Oct 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-1mdk
- 3.3.1

* Fri Oct 01 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-2mdk
- Add buildrequires lilo

* Fri Sep 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-1mdk
- 3.3.0

* Thu Aug 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-6mdk
- Fix spec file

* Tue Aug 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-5mdk
- Remove debug

* Wed Aug 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-4mdk
- Fix spec file

* Thu Jul 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-3mdk
- Add patch15: fix remove rpath (patch from gb)

* Tue Jun 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-2mdk
- Fix buildrequires

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-4mdk
- Rebuild

* Thu Jun 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-3mdk
- Rebuild with debug

* Fri May 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-2mdk
- Rebuild again qt 3.3.2

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-2mdk
- Fix spec file for using rpmbuildupdate

* Sat Apr 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

* Thu Feb 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-5mdk
- Fix buildrequires for gb

* Fri Feb 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-4mdk
- Split ksysv
- Fix menu entry

* Mon Feb 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-3mdk
- Rebuild with good kdedesktop2mdkmenu.pl

* Mon Feb 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-2mdk
- Sync with CVS

* Tue Feb 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-1mdk
- 3.2

