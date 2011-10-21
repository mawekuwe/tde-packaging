%define lib_name_orig %mklibname kdeaccessibility
%define lib_major 1
%define lib_name %lib_name_orig%lib_major

%define lib_name_orig_kttsd %mklibname kttsd
%define lib_major_kttsd 0
%define lib_name_kttsd %lib_name_orig_kttsd%lib_major_kttsd

%define oname kdeaccessibility
%define rname %{oname}3

Name:		kde3-%{oname}
Version:        3.5.12
Release:        %mkrel 1
Epoch:		1
Group:		Graphical desktop/KDE3
Summary:	K Desktop Environment - Accessibility program
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
Patch0:		kde-3.5.10-acinclude.patch
#Patch1:		fix_autotools.patch
Patch2:         kdebase-3.5.12-move-xdg-menu-dir.patch
Patch3:         kdebase-3.5.12-config.patch

BuildRoot:	%_tmppath/%name-%version-%release-root
License:	GPL
BuildRequires:  X11-devel
BuildRequires:  kdelibs3-devel
BuildRequires:  qt3-devel
BuildRequires:	kde3-macros
%if %mdkversion < 201000
BuildRequires:	autoconf <= 1:2.63
%endif
BuildRequires:	autoconf >= 1:2.65
BuildRequires:	automake > 1.5
BuildRequires:	akode-devel
Conflicts:      %oname < 1:3.5.10-2
Conflicts:      %rname < 1:3.5.10-3
Provides:       %oname = %epoch:%version-%release
Provides:       %rname = %epoch:%version-%release
Obsoletes:      %oname
Obsoletes:      %rname
Obsoletes:	kmag < %epoch:%version
Provides:	kde3-kmag = %epoch:%version-%release

%description
KDE Accessibility Aids:
- kmag, a screen magnifier,
- kmousetool, a program for people whom it hurts to click the mouse
- KMouth, a program that allows people who have lost their voice to let 
  their computer speak for them.

%files 
%defattr(-,root,root)
%_kde3_bindir/kmag
%_kde3_bindir/kmousetool
%_kde3_bindir/kmouth
%_kde3_libdir/kde3/kbstate_*
%dir %_kde3_appsdir/kbstateapplet/
%_kde3_appsdir/kbstateapplet/*
%_kde3_appsdir/kicker/applets/kbstateapplet.desktop
%_kde3_datadir/applnk/Applications/kmag.desktop
%_kde3_datadir/applnk/Applications/kmousetool.desktop
%_kde3_datadir/applnk/Applications/kmouth.desktop
%_kde3_datadir/applications/kde/kmag.desktop
%_kde3_datadir/applications/kde/kmousetool.desktop
%_kde3_datadir/applications/kde/kmouth.desktop
%dir %_kde3_appsdir/kmag/
%_kde3_appsdir/kmag/*
%dir %_kde3_appsdir/kmousetool/
%_kde3_appsdir/kmousetool/*
%dir %_kde3_appsdir/kmouth/
%_kde3_appsdir/kmouth/*


%doc %_kde3_docdir/HTML/en/kmag
%doc %_kde3_docdir/HTML/en/kmousetool
%doc %_kde3_docdir/HTML/en/kmouth
%_kde3_iconsdir/*/*/apps/*.png
%dir %_kde3_datadir/icons/mono
%_kde3_datadir/icons/mono/*

# To be moved for config package
%_kde3_datadir/config/kmouthrc

#--------------------------------------------------------------------

%package kttsd
Group:		Development/KDE and Qt
Summary:	KDE Text-to-Speech
Obsoletes:	kttsd <= 0.3.0
Provides:	kttsd3 >= %epoch:3.4.0
Provides:	kde3-kttsd >= %epoch:3.4.0
Requires:	%{lib_name}-kttsd = %epoch:%version-%release
Obsoletes:	%oname-kttsd-gstreamer
Provides:	%oname-kttsd = %epoch:%version-%release
Provides:	%rname-kttsd = %epoch:%version-%release
Obsoletes:	%oname-kttsd
Obsoletes:	%rname-kttsd

%description kttsd
KTTS -- KDE Text-to-Speech -- is a subsystem within the KDE desktop for 
conversion of text to audible speech. KTTS is currently under development 
and aims to become the standard subsystem for all KDE applications 
to provide speech output.
User Features:
 _ Speak any text from the KDE clipboard.
 _ Speak any plain text file.
 _ Speak all or any portion of a text file from Kate.
 _ Speak all or any portion of an HTML page from Konqueror.
 _ Use as the speech backend for KMouth and KSayIt.
 _ Speak KDE notifications (KNotify).
 _ Long text is parsed into sentences. User may backup by sentence or 
	paragraph, replay, pause, and stop playing.

%files kttsd
%defattr(-,root,root,0755)
%_kde3_bindir/ksayit
%_kde3_bindir/kttsd
%_kde3_bindir/kttsmgr
%_kde3_datadir/applications/kde/ksayit.desktop
%_kde3_datadir/services/ktexteditor_kttsd.desktop
%_kde3_datadir/services/kttsjobmgr.desktop
%_kde3_datadir/services/kttsd*
%_kde3_datadir/servicetypes/*.desktop
%_kde3_datadir/applications/kde/kcmkttsd.desktop
%_kde3_datadir/applications/kde/kttsmgr.desktop
%dir %_kde3_appsdir/ksayit
%_kde3_appsdir/ksayit/*
%dir %_kde3_appsdir/kttsd
%_kde3_appsdir/kttsd/*
%dir %_kde3_appsdir/ktexteditor_kttsd
%_kde3_appsdir/ktexteditor_kttsd/*
%_kde3_iconsdir/*/*/actions/*
%doc %_kde3_docdir/HTML/en/kttsd

#--------------------------------------------------------------------

%package    kttsd-akode
Group:		Development/KDE and Qt
Summary:	Akode plugins
Requires:	%name-kttsd >= %epoch:%version-%release
Obsoletes:	%{lib_name}-kttsd-akode
Provides:	%oname-kttsd-akode = %epoch:%version-%release
Provides:	%rname-kttsd-akode = %epoch:%version-%release
Obsoletes:	%oname-kttsd-akode
Obsoletes:	%rname-kttsd-akode

%description    kttsd-akode
Plugins for akode

%files    kttsd-akode
%defattr(-,root,root)
%_kde3_datadir/services/*akodeplugin.desktop
%_kde3_libdir/kde3/*akodeplugin.la
%_kde3_libdir/kde3/*akodeplugin.so

#--------------------------------------------------------------------

%package -n	%{lib_name}-kttsd
Group:		Development/KDE and Qt
Summary:	Library files for Kttsd
Obsoletes:  %{lib_name_kttsd} <= 0.3.0
Provides:   %{lib_name_kttsd} >= %epoch:3.4.0


%description -n	%{lib_name}-kttsd
Libraries file for Ktts

%files -n %lib_name-kttsd
%defattr(-,root,root)
%_kde3_libdir/kde3/kcm_kttsd.*
%_kde3_libdir/kde3/ktexteditor_kttsd.*
%_kde3_libdir/kde3/libkttsd*
%_kde3_libdir/kde3/libkttsjobmgrpart.*
%_kde3_libdir/libkttsd.so.*
%_kde3_libdir/libkttsd.la
%_kde3_libdir/libKTTSD_Lib.so.*
%_kde3_libdir/libKTTSD_Lib.la

#--------------------------------------------------------------------

%package -n	%{lib_name}-kttsd-devel
Group:		Development/KDE and Qt
Summary:	Header files for developing ktts
Requires:	%{lib_name}-kttsd = %epoch:%{version}-%{release}
Obsoletes:  %{lib_name_kttsd}-devel <= 0.3.0
Provides:   %{lib_name_kttsd}-devel >= %epoch:3.4.0

%description -n	%{lib_name}-kttsd-devel
Header files needed for developing ktts applications.

%files -n %lib_name-kttsd-devel
%defattr(-,root,root)
%_kde3_includedir/*.h
%_kde3_libdir/libkttsd.so
%_kde3_libdir/libKTTSD_Lib.so

#--------------------------------------------------------------------

%prep
%setup -q -n %oname-%version
%if %mdkversion >= 201000
%patch0 -p1
#%patch1 -p1
%endif
%patch2 -p0
%patch3 -p0

%build

export QTDIR=%_prefix/%_lib/qt3
export KDEDIR=%_prefix

PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/
export xdg_menudir=%_sysconfdir/xdg/kde/menus

make -f admin/Makefile.common cvs

%configure_kde3 \
	--with-akode \
	--without-gstreamer \
	--disable-embedded \
	--disable-palmtop \
	--disable-kttsd-gstreamer \
	--with-xinerama

%make

%install
rm -fr %buildroot
export PATH=%_kde3_bindir:$PATH

make install DESTDIR=%buildroot

# Vfolder directory
install -d %buildroot/%_kde3_datadir/applications/kde/
cp %buildroot/%_kde3_datadir/applnk/Applications/kmag.desktop %buildroot/%_kde3_datadir/applications/kde/kmag.desktop
cp %buildroot/%_kde3_datadir/applnk/Applications/kmousetool.desktop %buildroot/%_kde3_datadir/applications/kde/kmousetool.desktop
cp %buildroot/%_kde3_datadir/applnk/Applications/kmouth.desktop %buildroot/%_kde3_datadir/applications/kde/kmouth.desktop

%clean
rm -fr %buildroot


%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-1mdv2010.2
- Update to Trinity 3.5.12 sources
- Add xdg and build process patches

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 1:3.5.10-5mdv2010.1
- Rebuild for MDV 2010.1

* Sun Jan 17 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-4mvt2010.0
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65:patch0
+ Fix automake 1.11 issue:patch1
+ Change package name to avoid KDE4 conflicts, add kde3 prefix
+ Fix BuildRequirers, add kde3-macros

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 1:3.5.10-3mdv2010.0
- Rebuild for MDV 2010.0

* Mon Mar 23 2009 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-2mdv2009.1
+ Revision: 360612
- Change spec file name
  Fix spec file for new name
  Remove unused macros
  Add conflicts to ease upgrade to kde4

* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-1mdv2009.0
+ Revision: 277479
- Update for last kde3 updates

* Wed Jun 25 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-5mdv2009.0
+ Revision: 228960
- Fix Provides

* Thu Jun 12 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.9-4mdv2009.0
+ Revision: 218493
- rebuild for new ldflag

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 01 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.9-3mdv2009.0
+ Revision: 213980
- should provides kde3-kmag
- do not obsoletes kmag 4

* Thu May 08 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-2mdv2009.0
+ Revision: 204594
- Fix macros
- Move to /opt

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-1mdv2008.1
+ Revision: 169026
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches integrated

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Funda Wang <fundawang@mandriva.org>
    - fix duplicate mono dir

* Sat Dec 29 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.8-3mdv2008.1
+ Revision: 139064
- rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add usptream 3.5.9 branch patches
      	- Fix handling positions with Xinerama

* Wed Oct 24 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-1mdv2008.1
+ Revision: 101691
- Kde 3.5.8

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-ended-with-dot

* Wed Sep 05 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-5mdv2008.0
+ Revision: 80183
- Disable old gstreamer

* Thu Aug 23 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.7-4mdv2008.0
+ Revision: 69377
- fix kmag desktop file also

* Thu Aug 23 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.7-3mdv2008.0
+ Revision: 69365
- fix invalid kmouth desktop file

* Fri Aug 10 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-2mdv2008.0
+ Revision: 61653
- Fix menu categories and OnlyShowIn ( Bug #32470)

* Thu May 17 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-1mdv2008.0
+ Revision: 27530
- 3.5.7 release

