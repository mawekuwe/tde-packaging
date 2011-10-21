%define libname_orig libamarok
%define libname %mklibname kde3amarok 0
%define develname %mklibname -d kde3amarok 0
%define develscripts %mklibname -d kde3amarok-scripts

%define _disable_final 1

#Add MySQL support
%define build_mysql 1
%{?_with_mysql: %global build_mysql 1}

#Add PostgreSQL support
%define build_postgresql 1
%{?_with_postgresql: %global build_postgresql 1}

Summary:        A powerful media player for Kde
Name:           kde3-amarok
Version:        3.5.12
Release:        %mkrel 1
Epoch:          1
License:        GPLv2+
Url:            http://amarok.kde.org/
Group:          Sound
Source0:        amarok-%{version}.tar.bz2
# fwang: add lyric script for Chinese songs
# http://www.kde-apps.org/content/show.php/Lyrics_CN?content=50120
Source1:	Lyrics_CN-0.5.3.tar.bz2
Patch0:         amarok-1.4.1-fix-initial-preference.patch
Patch1:         amarok-1.3-fix-default-config.patch
Patch2:         amarok-1.2-fix-config.patch
Patch3:         amarok-1.4-beta2-add-multimedia-shortcut.patch
#(nl): Disable for the moment as it had been reported that this patch is broken.
Patch4:         amarok-1.4.0-use-mandriva-directory.patch
Patch6:         amarok-add-radios.patch
#Patch8:		amarok-1.4.9.1-libmtp-0.3.0-build-fix.patch
#Patch9:         wikipedia-lookup.patch
#Patch10:        amarok-1.4.10-gcc44.patch
Patch11:	kde-3.5.10-acinclude.patch
#Patch12:	fix_autotools.patch
Patch13:	fix-ifpdevice-build.patch
Patch14:         kdebase-3.5.12-move-xdg-menu-dir.patch
Patch15:         kdebase-3.5.12-config.patch
##########################################################

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  kde3-macros
%if %mdkversion < 201000
BuildRequires:  autoconf <= 2.63
%else
BuildRequires:  autoconf >= 2.65
%endif
BuildRequires:  automake >= 1.9
BuildRequires:  taglib-devel >= 1.4 
BuildRequires:  kdemultimedia-devel
BuildRequires:  libxine-devel 
BuildRequires:  libvisual-devel >= 0.4.0
BuildRequires:  libtunepimp-devel >= 1:0.4.2  
BuildRequires:  kdebase3-devel 
BuildRequires:  libxml2-utils
BuildRequires:  kde3-k3b-devel
BuildRequires:  libifp-devel
BuildRequires:  SDL-devel
BuildRequires:  libgpod-devel <= 0.7.93
BuildRequires:  libnjb-devel
BuildRequires:  sqlite3-devel
BuildRequires:  libmtp-devel >= 0.3.0
%if %build_mysql
BuildRequires:  mysql-devel
%endif
%if %build_postgresql
BuildRequires:  postgresql-devel
%endif
BuildRequires:  mesaglut-devel
BuildRequires:  libgpod-devel
BuildRequires:  ruby-devel
BuildRequires:  gpm-devel
BuildRequires:	tcl-devel
BuildRequires:	libkarma-devel
BuildRequires:  musicbrainz-devel
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires:       kde3-amarok-engine
Requires:       kde3-amarok-scripts
Requires:       %{libname} = %epoch:%{version}
Requires:       tunepimp-plugins 
Suggests:	moodbar
Requires:       libvisual-plugins >= 0.4.0
Suggests:       transkode
Conflicts :     amarok-engine-arts
Conflicts :     amarok-engine-gstreamer
Conflicts :     amarok-engine-akode
Conflicts :     amarok-engine-gstreamer0.10
 
%description
Feature Overview 
 
* Music Collection:
You have a huge music library and want to locate tracks quickly? Let amaroK's
powerful Collection take care of that! It's a database powered music store, 
which keeps track of your complete music library, allowing you to find any 
title in a matter of seconds. 
 
* Intuitive User Interface:
You will be amazed to see how easy amaroK is to use! Simply drag-and-drop files
into the playlist. No hassle with complicated  buttons or tangled menus. 
Listening to music has never been easier! 
 
* Streaming Radio:
Web streams take radio to the next level: Listen to thousands of great radio
stations on the internet, for free! amaroK provides excellent streaming
support, with advanced features, such as displaying titles of the currently
playing songs. 
 
* Context Browser:
This tool provides useful information on the music you are currently listening
to, and can make listening suggestions, based on your personal music taste. An
innovate and unique feature. 
 
* Visualizations:
amaroK is compatible with XMMS visualization plugins. Allows you to use the
great number of stunning visualizations available on the net. 3d visualizations
with OpenGL are a great way to enhance your music experience. 

%if %mdkversion < 200900
%post
%update_menus
%{update_desktop_database}
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%{clean_desktop_database}
%endif

%files 
%defattr(-,root,root)
%doc README AUTHORS COPYING ChangeLog
%{_kde3_bindir}/*
%{_kde3_appsdir}/konqueror/servicemenus/amarok_*
%{_kde3_datadir}/locale/*/*/*
%{_kde3_docdir}/*/*/amarok
%{_kde3_datadir}/applications/kde/amarok.desktop
%{_kde3_datadir}/servicetypes/amarok_*
%{_kde3_datadir}/services/amarok_daap-mediadevice.desktop
%{_kde3_datadir}/services/amarok_generic-mediadevice.desktop
%{_kde3_datadir}/services/amarok_ifp-mediadevice.desktop
%{_kde3_datadir}/services/amarok_ipod-mediadevice.desktop
%{_kde3_datadir}/services/amarok_massstorage-device.desktop
%{_kde3_datadir}/services/amarok_mtp-mediadevice.desktop
%{_kde3_datadir}/services/amarok_nfs-device.desktop
%{_kde3_datadir}/services/amarok_njb-mediadevice.desktop
%{_kde3_datadir}/services/amarok_smb-device.desktop
%{_kde3_datadir}/services/amarok_riokarma-mediadevice.desktop
%{_kde3_datadir}/services/amarokitpc.protocol
%{_kde3_datadir}/services/amaroklastfm.protocol
%{_kde3_datadir}/services/amarokpcast.protocol
%dir %{_kde3_appsdir}/amarok
%{_kde3_appsdir}/amarok/amarokui.rc
%dir %{_kde3_appsdir}/amarok/data
%{_kde3_appsdir}/amarok/ruby_lib
%{_kde3_appsdir}/amarok/themes
%{_kde3_appsdir}/amarok/data/*
%{_kde3_appsdir}/amarok/icons/*/*/*/*
%{_kde3_iconsdir}/*/*/*/*
%{_kde3_appsdir}/amarok/images/*
%{_kde3_appsdir}/profiles/amarok.profile.xml
%{_kde3_datadir}/config/amarokrc
%{_kde3_datadir}/config.kcfg/amarok.kcfg
%{_kde3_appsdir}/konqsidebartng/*

#--------------------------------------------------------------------

%package scripts
Summary:        Scripts for amarok
Group:          Graphical desktop/KDE3
Requires:       %name = %epoch:%version-%release
URL:            http://amarok.kde.org/
Requires:       kde3-kjsembed
Requires:       ruby
Requires:       python
# (Anssi 05/2008) ruby_lib moved; the package was obsoleted by amarok-scripts:
Conflicts:	%{_lib}amarok0-scripts < 1:1.4.9.1-3

%description scripts
This package includes python scripts for amarok.

%files scripts
%defattr(-,root,root)
%dir %{_kde3_appsdir}/amarok/scripts/
%{_kde3_appsdir}/amarok/scripts/*
%_kde3_libdir/ruby_lib/http11.rb
%_kde3_libdir/ruby_lib/*.la
%_kde3_libdir/ruby_lib/*.so.*

#--------------------------------------------------------------------

%package -n %{develscripts}
Summary:        Library scripts for amarok
Group:          Graphical desktop/KDE3
Requires:       %{name}-scripts = %epoch:%{version}
URL:            http://amarok.kde.org/
Requires:       ruby
Obsoletes:	%{libname}-devel-scripts
Provides:	%{libname}-devel-scripts

%description -n %{develscripts}
This package includes devel for scripts for amarok.

%files -n %{develscripts}
%defattr(-,root,root)
%_kde3_libdir/ruby_lib/*.so

#------------------------------------------------------------------

%package engine-xine
Summary:        Amarok xine engine
Group:          Graphical desktop/KDE3
Provides:       kde3-amarok-engine
URL:            http://amarok.kde.org/
Requires:       xine-lib
Requires:       xine-plugins
Requires:       %name = %epoch:%version-%release

%description engine-xine
This package includes xine engine for amarok.

%files  engine-xine
%defattr(-,root,root)
%{_kde3_libdir}/kde3/libamarok_xine-engine.*
%{_kde3_datadir}/services/amarok_xine-engine.desktop
%{_kde3_datadir}/config.kcfg/xinecfg.kcfg

#--------------------------------------------------------------------

%package engine-yauap
Summary:        Amarok yauap engine
Group:          Graphical desktop/KDE3
URL:            http://amarok.kde.org/
Requires:       %name = %epoch:%version-%release
Conflicts:      %name < 1:1.4.8-1

%description engine-yauap
This package includes yauap engine for amarok.

%files  engine-yauap
%defattr(-,root,root)
%{_kde3_libdir}/kde3/libamarok_yauap-engine_plugin.*
%{_kde3_datadir}/services/amarok_yauap-engine_plugin.desktop

#--------------------------------------------------------------------

%package engine-void
Summary:        Amarok void engine
Group:          Graphical desktop/KDE3
URL:            http://amarok.kde.org/
Requires:       %name = %epoch:%version-%release
Conflicts:      %name < 1:1.4.8-4

%description engine-void
This package includes void engine for amarok.

%files  engine-void
%defattr(-,root,root)
%{_kde3_libdir}/kde3/libamarok_void-engine_plugin.*
%{_kde3_datadir}/services/amarok_void-engine_plugin.desktop

#--------------------------------------------------------------------

%package -n %{libname}
Summary:        Amarok  library
Group:          Graphical desktop/KDE3
Provides:       %{libname_orig} = %epoch:%{version}-%{release}

%description -n %{libname}
Library for Amarok

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_kde3_libdir}/libamarok.so.*
%{_kde3_libdir}/kde3/konqsidebar_universalamarok.*
%{_kde3_libdir}/kde3/libamarok_daap-mediadevice.*
%{_kde3_libdir}/kde3/libamarok_generic-mediadevice.*
%{_kde3_libdir}/kde3/libamarok_ifp-mediadevice.*
%{_kde3_libdir}/kde3/libamarok_ipod-mediadevice.*
%{_kde3_libdir}/kde3/libamarok_massstorage-device.*
%{_kde3_libdir}/kde3/libamarok_mtp-mediadevice.*
%{_kde3_libdir}/kde3/libamarok_nfs-device.*
%{_kde3_libdir}/kde3/libamarok_njb-mediadevice.*
%{_kde3_libdir}/kde3/libamarok_smb-device.*
%{_kde3_libdir}/kde3/libamarok_riokarma-mediadevice.*

#--------------------------------------------------------------------

%package -n %{develname}
Summary:        Headers of %name for development
Group:          Development/C
Requires:       %{libname} = %epoch:%{version}
Provides:       %{name}-devel = %epoch:%{version}-%{release}
Provides:       amarok0-devel = %epoch:%{version}-%{release}
# (Anssi 05/2008) Wrong package name:
Conflicts:	%{_lib}amarok-devel < 1:1.4.9.1-3

%description -n %{develname}
Headers of %{name} for development.

%files -n %{develname}
%defattr(-,root,root)
%{_kde3_libdir}/libamarok.la
%{_kde3_libdir}/libamarok.so

#--------------------------------------------------------------------

%prep
%setup -q -n amarok-%version -a 1
%patch0  -p1 -b .fix_amarok_initial_preference
%patch1  -p0 -b .fix_amarok_default_config_file
%patch3  -p1 -b .fix_add_multimedia_shortcut
%patch6  -p1 -b .add_some_radios
#%patch8 -p0
#%patch9 -p1
#%patch10 -p1
%if %mdkversion >= 201000
%patch11 -p1
#%patch12 -p1
%patch13 -p1
%endif
%patch14 -p0
%patch15 -p0

%build
PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/
export xdg_menudir=%_sysconfdir/xdg/kde/menus

make -f admin/Makefile.common cvs
export QTDIR=%qt3dir

%configure_kde3 --docdir=%_kde3_docdir\
   --with-xine \
   --with-yauap \
   --without-included-sqlite \
   --with-libgpod \
   --without-helix \
   --without-xmms \
   --with-libmtp \
   --with-libkarma \
   --with-ifp \
%if %build_mysql
   --enable-mysql \
%endif
%if %build_postgresql
   --enable-postgresql \
%endif

%make

%install
rm -rf %buildroot

%{makeinstall_std}

# install source1
mkdir -p %{buildroot}/%{_kde3_appsdir}/amarok/scripts/lyrics_cn/dict
pushd Lyrics_CN
cp -a * %{buildroot}/%{_kde3_appsdir}/amarok/scripts/lyrics_cn
find %{buildroot}/%{_kde3_appsdir}/amarok/scripts/lyrics_cn/ -type f | xargs chmod 0644
chmod 0755 %{buildroot}/%{_kde3_appsdir}/amarok/scripts/lyrics_cn/Lyrics_CN
popd

#correct wrong script encoding file
perl -pi -e 's/\015$//' %{buildroot}/%{_kde3_appsdir}/amarok/data/Cool-Streams.xml
perl -pi -e 's/\015$//' %{buildroot}/%{_kde3_appsdir}/amarok/scripts/playlist2html/README
perl -pi -e 's/\015$//' %{buildroot}/%{_kde3_appsdir}/amarok/scripts/webcontrol/README


%clean
rm -rf %buildroot



%changelog

* Mon Jul 25 2011 Tim Williams <tim@my-place.org.uk> 3.5.12-1mvt2010.2
+ Update to Trinity sources
- Remove amarok-1.4.10-gcc44.patch, fix_autotools.patch, amarok-1.4.9.1-fix-underlinking.patch, amarok-1.4.9.1-libmtp-0.3.0-build-fix.patch
+ Add kdebase-3.5.12-move-xdg-menu-dir.patch, kdebase-3.5.12-config.patch
- Remove wikipedia-lookup.patch

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 1:1.4.10-5mvt2010.1
+ Rebuild for MDV 2010.1
+ change required version of libgpod to match MDV 2010.1 packages

* Wed Dec 23 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:1.4.10-4mvt2010.0
- Use upper release number to avoid unwanted KDE4 upgrade
- Fix automake 1.11 and autoconf 2.65 build issues
- Fix ifp build for compability autoconf changes
- Change package group

* Sun Dec 20 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:1.4.10-3mvt2010.0
+ Last KDE3 verison
+ Built for 2010.0 release
+ Added gcc4 patch
+ Fix wikipedia lookup patch
+ Fix karma service built

* Tue Sep 02 2008 Helio Chissini de Castro <helio@mandriva.com> 1:1.4.10-2mdv2009.0
+ Revision: 278767
- Fix kjsembed and k3b-devel requires

* Thu Aug 14 2008 Funda Wang <fundawang@mandriva.org> 1:1.4.10-1mdv2009.0
+ Revision: 271697
- New version 1.4.10

* Fri Jul 18 2008 Funda Wang <fundawang@mandriva.org> 1:1.4.9.1-9mdv2009.0
+ Revision: 238331
- add patch to build against libmtp 0.3.0

* Thu Jul 03 2008 Adam Williamson <awilliamson@mandriva.com> 1:1.4.9.1-8mdv2009.0
+ Revision: 231371
- drop exscalibar (build)requires: moodbar was rewritten not to need exscalibar
  in august 2006

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 11 2008 Funda Wang <fundawang@mandriva.org> 1:1.4.9.1-7mdv2009.0
+ Revision: 218132
- add patch to fix underlink
- rebuild for new configure_kde3

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jun 04 2008 Funda Wang <fundawang@mandriva.org> 1:1.4.9.1-6mdv2009.0
+ Revision: 214923
- BR tcl
- rebuild for new directfb

* Tue May 20 2008 Anssi Hannula <anssi@mandriva.org> 1:1.4.9.1-5mdv2009.0
+ Revision: 209512
- change the libamarok0-scripts obsoletes back to conflict to avoid
  multiple packages obsoleting the same one
- do not require kde3-amarok in libamarok0 (avoids upgrading users
  getting both kde3-amarok and amarok)

  + Funda Wang <fundawang@mandriva.org>
    - libscripts should be obsoleted rather than conflicts

* Tue May 13 2008 Anssi Hannula <anssi@mandriva.org> 1:1.4.9.1-3mdv2009.0
+ Revision: 206809
- rename libamarok-devel to libamarok0-devel to avoid conflicts with
  main amarok package
- drop libamarok0-scripts and move the contents to amarok-scripts

* Mon May 12 2008 Anssi Hannula <anssi@mandriva.org> 1:1.4.9.1-2mdv2009.0
+ Revision: 206473
- drop obsoletes that belong to amarok package
- do not provide libamarok-devel, it conflicts with main amarok devel pkg

  + Funda Wang <fundawang@mandriva.org>
    - should be kde3-k3b

* Fri May 09 2008 Funda Wang <fundawang@mandriva.org> 1:1.4.9.1-1mdv2009.0
+ Revision: 204803
- New version of lyrics_cn plugin
- New version 1.4.9.1

* Fri May 09 2008 Helio Chissini de Castro <helio@mandriva.com> 1:1.4.8-11mdv2009.0
+ Revision: 204753
- Return of kde3 amarok in new /opt path
- We need old amarok for kde3

* Sat Mar 08 2008 Funda Wang <fundawang@mandriva.org> 1:1.4.8-8mdv2008.1
+ Revision: 182085
- New license policy
- fix lyrics_cn file permission

* Tue Mar 04 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.4.8-7mdv2008.1
+ Revision: 179228
- Add support for the new amazon web API
- Remove condition for unsupported version

* Thu Feb 28 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.4.8-6mdv2008.1
+ Revision: 176529
- Add transkode as suggest as requested by colin

* Thu Feb 21 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.4.8-5mdv2008.1
+ Revision: 173486
- Only provide amarok-engine on working engines (Bug #37800)
- Package void engine in its own package (Bug #37797)

* Sun Feb 10 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.4.8-3mdv2008.1
+ Revision: 164737
- [FEATURE] Enable mysql and postgresql support (Bug #36392)
  Add upstream patch to fix some pbs on the dynamic mode
- Move yauap in its own engine package

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1:1.4.8-1mdv2008.1
+ Revision: 135819
- restore BuildRoot

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - New version 1.4.8

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 14 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.7-14mdv2008.1
+ Revision: 108663
- rebuild for new libgpod

* Wed Oct 31 2007 Thierry Vignaud <tvignaud@mandriva.com> 1:1.4.7-12mdv2008.1
+ Revision: 104176
- really rebuild for new libmtp

* Sun Oct 28 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.7-11mdv2008.1
+ Revision: 102710
- fix startup of lyrics_CN script

* Sat Oct 27 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.7-10mdv2008.1
+ Revision: 102620
- Rebuild for new libmtp
- New version of Lyrics_CN plugin
- suggests moodbar

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add patch from upstream stable branch (patch 16)
      Add support for other engines and hardware (WIP)

* Mon Sep 03 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.7-9mdv2008.0
+ Revision: 78441
- New version of Lyrics_CN plugin

* Fri Aug 31 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.4.7-8mdv2008.0
+ Revision: 76978
- Add upstream patch: amarok freezes when trying to play mp3 files without mp3 support
- Add upstream patch that fix a crash with mysql
- Fix post/postun
- Add new upstream patches from BRANCH

* Mon Aug 27 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:1.4.7-7mdv2008.0
+ Revision: 72238
- Rebuild for locale dir fix

* Sun Aug 26 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.4.7-6mdv2008.0
+ Revision: 71488
- Add upstream patches from upcoming 1.4.8 release

* Sat Aug 25 2007 Anssi Hannula <anssi@mandriva.org> 1:1.4.7-5mdv2008.0
+ Revision: 71349
- rebuild with new rpm-mandriva-setup for find_lang fixes

* Fri Aug 24 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.7-4mdv2008.0
+ Revision: 70748
- fix install of lyric_cn script
- New version of Lyrics_CN

* Sat Aug 18 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.7-3mdv2008.0
+ Revision: 65550
- New devel policy for scripts-devel

* Sat Aug 18 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.7-2mdv2008.0
+ Revision: 65423
- New devel package policy

* Thu Aug 16 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.7-1mdv2008.0
+ Revision: 64501
- New verison 1.4.7

* Fri Aug 10 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.6-5mdv2008.0
+ Revision: 61071
- finally fix lyric_cn permission

* Sun Aug 05 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.6-4mdv2008.0
+ Revision: 59036
- Rebuild against latest libmtp

* Wed Jun 27 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.6-3mdv2008.0
+ Revision: 44942
- Rebuild against k3b 1.0.2
- fix permission

* Fri Jun 22 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.6-2mdv2008.0
+ Revision: 42938
- Renew SOURCE1
  fix executive permission

* Wed Jun 20 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.4.6-1mdv2008.0
+ Revision: 41932
- Remove desktop-file-utils require as categories have been merged upstream

  + Funda Wang <fundawang@mandriva.org>
    - Kill patch21, merged upstream
    - kill patch 7, merged upstream
    - New upstream version

* Wed Jun 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.4.5-15mdv2008.0
+ Revision: 38603
- rebuild for expat

* Fri Jun 01 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:1.4.5-14mdv2008.0
+ Revision: 34341
- Rebuild with libslang2.

  + Nicolas Lécureuil <neoclust@mandriva.org>
    -Add only needed categories

* Sat May 26 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.5-13mdv2008.0
+ Revision: 31411
- Rebuild for directfb 1.0

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add patch21 from upstream (rev: 667738 )

* Wed May 09 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.4.5-12mdv2008.0
+ Revision: 25817
- Rebuild
- Fix breakage because of wrongly removed macros

  + Funda Wang <fundawang@mandriva.org>
    - install with correct permission

* Sat May 05 2007 Funda Wang <fundawang@mandriva.org> 1:1.4.5-10mdv2008.0
+ Revision: 22912
- Added lyrics_cn script for Chinese songs.

* Mon Apr 16 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.4.5-9mdv2008.0
+ Revision: 13504
- Bump release

