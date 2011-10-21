%define oname kdebluetooth
%define _requires_exceptions devel\(libbluetooth\)\||devel\(libGLcore\)\||devel\(libGL\)

%define _disable_ld_no_undefined 1

%define major 0
%define libname %mklibname %name %major
%define liboldname %mklibname %oname %major
%define develname %mklibname %name -d
%define develoldname %mklibname %oname -d
%define svn_rev svn697456
%define beta beta8

Name: kde3-%{oname}
Summary: Access and control bluetooth devices in KDE
Version: 1.0
Epoch: 1
Release: %mkrel -c %beta 14
Source: %{oname}-%{version}_%beta.tar.bz2
Patch0: kdebluetooth-1.0_beta8-compile.patch
URL: http://bluetooth.kmobiletools.org
License: GPL
Group: System/Configuration/Hardware
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: pkgconfig 
BuildRequires: arts-devel
BuildRequires: qt3-devel >= 3.3.6-15mdv2007.0
BuildRequires: kdelibs-devel 
BuildRequires: dbus-devel
BuildRequires: libdbus-qt-1-devel
BuildRequires: hal-devel
BuildRequires: openobex-devel >= 1.2 
BuildRequires: kdepim-devel
BuildRequires: bluez-devel
BuildRequires: bluez-sdp-devel 
BuildRequires: libxml2-utils
BuildRequires: obexftp-devel
BuildConflicts: xmms-devel
Requires: bluez-utils 
Requires: bluez-sdp
Provides: bluez-pin
Obsoletes: kdebluetooth-pin
Provides: %{oname} = %epoch:%version-%release
Obsoletes: %{oname}

%description
The aim of this project is a tight and easy to use integration of Bluetooth
into the KDE desktop. You can manage your local Bluetooth devices and services
with it, browse your Bluetooth neighbourhood with konqueror and send and
receive files with just a few clicks. And that's not all you can do with it...

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %oname.lang
%defattr(-,root,root)
%{_kde3_bindir}/kbluelock
%{_kde3_bindir}/kbluemon
%{_kde3_bindir}/kbluetooth
%{_kde3_bindir}/kinputwizard
%{_kde3_bindir}/kbtobexclient
%{_kde3_bindir}/kioobex_start
%{_kde3_libdir}/kde3/kcm_btpaired.*
%{_kde3_libdir}/kde3/kio_bluetooth.*
%{_kde3_libdir}/kde3/kio_obex.*
%{_kde3_libdir}/kde3/kio_sdp.*
%{_kde3_libdir}/kdebluetooth/servers/kbtobexsrv
%{_kde3_appsdir}/kdebluetooth/dunhandler/dunhandler
%{_kde3_appsdir}/kdebluetooth/faxhandler/faxhandler
%{_kde3_appsdir}/kdebluetooth/faxhandler/kbtfax
%{_kde3_appsdir}/kdebluetooth/eventsrc
%{_kde3_appsdir}/kbtobexclient/kbtobexclientui.rc
%{_kde3_appsdir}/konqsidebartng/virtual_folders/services/bluetooth_sidebarentry.desktop
%{_kde3_appsdir}/konqueror/servicemenus/kbtobexclient_sendfile.desktop
%{_kde3_iconsdir}/*/*/*/kdebluetooth.*
%dir %{_kde3_datadir}/mimelnk/bluetooth/
%{_kde3_datadir}/mimelnk/bluetooth/*.desktop
%{_kde3_datadir}/applnk/Settings/Network/Bluetooth
%_kde3_datadir/applnk/Utilities/dunhandler.desktop
%_kde3_datadir/applnk/Utilities/faxhandler.desktop
%_kde3_datadir/applnk/.hidden/kioobex_start.desktop
%{_kde3_datadir}/servicetypes/*
%{_kde3_datadir}/services/*
%{_kde3_datadir}/autostart/*
%dir %{_kde3_datadir}/desktop-directories
%{_kde3_datadir}/desktop-directories/*
%{_kde3_datadir}/applications/kde/*.desktop
%{_kde3_iconsdir}/hicolor/*/apps/kbluetooth.png
%{_kde3_iconsdir}/hicolor/*/apps/kbluelock.png

#--------------------------------------------------------------------------

%package -n %develname
%define _requires_exceptions devel\(libbluetooth\)
Group:   Development/KDE and Qt
Summary: Development for KDE Bluetooth
Requires: %libname = %epoch:%version-%release
Provides: kdebluetooth-devel = %epoch:%{version}-%{release}
Obsoletes: %libname-devel
Provides: %{develoldname} = %epoch:%version-%release
Obsoletes: %{develoldname}


%description -n %develname
The aim of this project is a tight and easy to use integration of Bluetooth
into the KDE desktop. You can manage your local Bluetooth devices and services
with it, browse your Bluetooth neighbourhood with konqueror and send and
receive files with just a few clicks. And that's not all you can do with it...

%files -n %develname
%defattr(-,root,root)
%{_kde3_includedir}/*
%{_kde3_libdir}/*.la
%{_kde3_libdir}/*.so

#--------------------------------------------------------------------------

%package -n %libname
Group: System/Configuration/Hardware
Summary: Development for KDE Bluetooth
Provides: %{liboldname} = %epoch:%version-%release
Obsoletes: %{liboldname}

%description -n %libname
The aim of this project is a tight and easy to use integration of Bluetooth
into the KDE desktop. You can manage your local Bluetooth devices and services
with it, browse your Bluetooth neighbourhood with konqueror and send and
receive files with just a few clicks. And that's not all you can do with it...

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%{_kde3_libdir}/*.so.*

#--------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}_%beta
%patch0 -p0

%build

%configure_kde3 \
   --without-xmms


%make

%install
rm -rf %buildroot

%makeinstall_std

%find_lang %{oname} --with-html

%clean
rm -rf %buildroot





%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 1:1.0-0.beta8.14mvt2010.2
+ Rebuild for Trinity

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 1:1.0-0.beta8.13mvt2010.1
+ Rebuild for MDV 2010.1

* Tue Jan 19 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:1.0-0.beta8.12mvt2010.0
- Rebuild for 2010.0
- Change package name to avoid KDE4 upgrade

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 1:1.0-0.beta8.11mdv2010.0
+ Rebuild for MDV 2010.0

* Wed Mar 25 2009 Helio Chissini de Castro <helio@mandriva.com> 1:1.0-0.beta8.10mdv2009.1
+ Revision: 361207
- Bump release, fix build to recompile

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 1:1.0-0.beta8.8mdv2009.0
+ Revision: 204662
- Move to /opt

* Sun Feb 24 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.0-0.beta8.8mdv2008.1
+ Revision: 174146
- Rebuild

* Thu Feb 07 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.0-0.beta8.7mdv2008.1
+ Revision: 163348
- Rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 31 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-0.beta8.6mdv2008.1
+ Revision: 139863
- rebuilt against openldap-2.4.7 libs

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 20 2007 Anssi Hannula <anssi@mandriva.org> 1:1.0-0.beta8.5mdv2008.0
+ Revision: 91632
- remove broken workaround for find-lang.pl bug that prevented
  installation, the bug is properly fixed in rpm-mandriva-setup-build 1.60

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - update to version 1.0_beta8:
      * back to kbluetoothd kio_obex module (Novell #310145)
      * added wrapper classes for new obex-data-server
      * fixed config file to fix wrong autostart settings

* Tue Sep 18 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.0-0.beta7.3mdv2008.0
+ Revision: 89735
- upload again because of HD failure

* Mon Sep 17 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.0-0.beta7.2mdv2008.0
+ Revision: 89249
- Fix File list
- Fix File list
- Use new tarball fixing some bugs

* Mon Sep 03 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.0-0.beta7.1mdv2008.0
+ Revision: 78718
- Fix file list
- New upstream beta => beta7

* Wed Aug 08 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:1.0-0.beta5.1mdv2008.0
+ Revision: 60183
- New release 1.0 Beta5

* Thu Aug 02 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:1.0-0.beta3.4mdv2008.0
+ Revision: 58254
- Rebuild against latest bluez-utils to fix a crash in the passkey agent

* Wed Jun 20 2007 Helio Chissini de Castro <helio@mandriva.com> 1:1.0-0.beta3.3mdv2008.0
+ Revision: 41730
- Missig build requires
- New devel library policy
- Added new kdebluetooth branch based on standard dbus calls.

  + Funda Wang <fundawang@mandriva.org>
    - Remove unwanted obsoletes

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Obsoletes bluez-pin as it is gone
    - New version Beta3
    - Fix Group

* Mon May 21 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1.0-1.beta2.13mdv2008.0
+ Revision: 29096
- Add BuildRequire
- Fix File list
- Remove old menu entries
- Add menu macros needed for non XDG-Compliant WM
- Rebuild


* Sat Mar 31 2007 Laurent Montel <lmontel@mandriva.com> 1.0-1.beta2.12mdv2007.1
+ Revision: 150049
- fix menu

* Thu Feb 22 2007 Olivier Blin <oblin@mandriva.com> 1.0-1.beta2.11mdv2007.1
+ Revision: 124768
- try current user before relying on the "who" command (#28448)

* Mon Feb 05 2007 Laurent Montel <lmontel@mandriva.com> 1.0-1.beta2.10mdv2007.1
+ Revision: 116277
- Use kwrite by default into template

* Wed Jan 17 2007 Laurent Montel <lmontel@mandriva.com> 1.0-1.beta2.9mdv2007.1
+ Revision: 109783
- I don't understand... a beta2 called beta1...
- Fix message
- Fix crash
- Add missing menu

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream version ( 1.0 beta2 )

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - added a patch fixing directory mimetype when using ObexFTP
    - cosmetic changes on spec file

* Wed Sep 13 2006 Helio Chissini de Castro <helio@mandriva.com> 1.0-0.beta1.8mdv2007.0
+ Revision: 61111
- Added new revision with obex 1.2 compliance ( fix openobex detection and
  compilation )
- Adde kdebluetooth-pin package ( for pin_helper )
- Pin helper separated to make easy access to backward auth patch on bluez-utils
- BuildConflicts on xmms-devel
- Fixed kdebluetooth pin alternatives
- import kdebluetooth-1.0-0.beta1.5mdv2007.0

* Wed May 25 2005 Nicolas L�cureuil <neoclust@mandriva.org> 1.0-0.beta1.2mdk
- Drop Patch 0, 1, 2, 3 ( Merged Upstream )
- Fix files permissions
- Fix doc section

* Wed May 25 2005 Laurent MONTEL <lmontel@mandriva.com> 1.0-0.beta1.1
- 1.0beta1

* Wed Mar 09 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.0.cvs20041202-5mdk
- amarok support for kbemusedsrv (P1 from cvs)
- fix build with recent bluez libs (P2 from CVS)

* Tue Dec 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.0.cvs20041202-4mdk
- Fix install script bug found by Arnaud

* Tue Dec 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.0.cvs20041202-3mdk
- Fix obsolete

* Tue Dec 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.0.cvs20041202-2mdk
- Fix requires

* Thu Dec 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.0.cvs20041202-1mdk
- Update code from CVS

* Thu Dec 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.0.cvs20040914-3mdk
- Fix spec file

* Tue Oct 19 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.0.cvs20040914-2mdk
- fix build

* Wed Sep 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.0.cvs20040914-1mdk
- cvs 20040914

* Tue Aug 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.0.cvs20040718-3mdk
- Rebuild with new menu

* Fri Jul 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.0.cvs20040718-2mdk
- Fix tarball (add admin directory into package)

* Mon Jul 19 2004 Austin Acton <austin@mandrake.org> 0.0.cvs20040718-1mdk
- cvs 20040718
- configure 2.5
- disable-rpath

* Sat Jun 19 2004 Austin Acton <austin@mandrake.org> 0.0.cvs20040618-1mdk
- cvs 20040618

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.0.cvs20040302-5mdk
- Rebuild

