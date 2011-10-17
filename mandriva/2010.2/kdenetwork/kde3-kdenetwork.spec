%define _requires_exceptions devel\(linux-gate\)

%define lib_name_orig lib%{name}
%define lib_major 2
%define lib_name %mklibname kdenetwork %lib_major
%define oname kdenetwork3

Name: kde3-kdenetwork
Version: 3.5.12
Release: %mkrel 1
Epoch: 2
Group: Graphical desktop/KDE3
Summary: K Desktop Environment - Network Applications
License: GPL
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdenetwork-%version.tar.bz2
Source1:  %{oname}-kppp.pamd
Source2:  kdenetwork-lisa
Patch1: kdenetwork-3.5.7-add-slovenian-provider.patch
Patch2: kdenetwork-3.5.7-fix-kdebug-120625.patch
#Patch3: kdenetwork-3.5.8-fix-desktop-files.patch
#Patch4: kdenetwork-3.5.9-fix-underlinking.patch
Patch5: kdenetwork-3.5.10-wformat.patch
#Patch6: kdenetwork-3.5.10-gcc44.patch
#Patch7: kdenetwork-3.5.10-kopete_fix_yahoo.patch
Patch8: kde-3.5.10-acinclude.patch
#Patch9: fix_autotools.patch
Patch10: kdebase-3.5.12-move-xdg-menu-dir.patch
Patch11: kdebase-3.5.12-config.patch
BuildRoot:	%_tmppath/%name-%version-%release-root
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%else
BuildRequires: autoconf >= 1:2.65
%endif
BuildRequires: automake > 1.5
BuildRequires: arts3-devel
BuildRequires: freetype2-devel
BuildRequires: kde3-macros
BuildRequires: gettext
BuildRequires: kdelibs-devel
BuildRequires: kdelibs-common >= 3.1.93-5mdk
BuildRequires: bzip2-devel
BuildRequires: jpeg-devel
BuildRequires: lcms-devel
BuildRequires: mng-devel
BuildRequires: png-devel
BuildRequires: wireless-tools
BuildRequires: avahi-compat-libdns_sd-devel  
BuildRequires: avahi-client-devel
BuildRequires: mesaglut-devel
BuildRequires: X11-devel
BuildRequires: expat-devel
BuildRequires: speex-devel
BuildRequires: ortp-devel
BuildRequires: meanwhile-devel
BuildRequires: gadu-devel
BuildRequires: libopenssl-devel
BuildRequires: libopenslp-devel
BuildRequires: libaudiofile-devel
BuildRequires: libz-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: libiw-devel
BuildRequires: qca2-devel
BuildRequires: libidn-devel
BuildRequires: libgsmlib-devel
BuildRequires: libxtst-devel
Requires: %{name}-kdict = %epoch:%version-%release	
Requires: %{name}-kget = %epoch:%version-%release
Requires: %{name}-ksirc = %epoch:%version-%release
Requires: %{name}-ktalk = %epoch:%version-%release
Requires: %{name}-krfb = %epoch:%version-%release
Requires: %{name}-kopete = %epoch:%version-%release
Requires: %{name}-knewsticker = %epoch:%version-%release
Obsoletes: %{name}-kxmlrpcd
Obsoletes: %lib_name-kxmlrpcd
Obsoletes: kdenetwork_kroupware
Obsoletes: kdenetwork_kroupware-kppp
Obsoletes: libkdenetwork_kroupware2
Obsoletes: libkdenetwork_kroupware2-devel
Obsoletes: kit
Obsoletes: kdenetwork-kmail < 3.1.6
Obsoletes: kdenetwork-knode < 3.1.6
Obsoletes: kdenetwork-korn < 3.1.6
Obsoletes: kdenetwork <= 2:3.5.10
Obsoletes: %{oname}-kget
Obsoletes: %{oname}-ksirc
Obsoletes: %{oname}-ktalk
Obsoletes: %{oname}-krfb
Obsoletes: %{oname}-kopete
Obsoletes: %{oname}-knewsticker
Provides: %{oname} = %epoch:%version-%release


%description
Networking applications for the K Desktop Environment.

- kdict: graphical client for the DICT protocol.
- kit: AOL instant messenger client, using the TOC protocol
- knewsticker: RDF newsticker applet
- kpf: public fileserver applet
- ksirc: IRC client
- ktalkd: talk daemon
- lanbrowsing: lan browsing kio slave
- krfb: Desktop Sharing server, allow others to access your desktop via VNC
- krdc: a client for Desktop Sharing and other VNC servers

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files

#-----------------------------------------------------------

%package common
Summary:	Common files for kdenetwork
Group:		Graphical desktop/KDE3

Requires: kdebase3-progs >= 3.1
Requires: kdelibs3 >= 3.1.1-15mdk
Requires: %lib_name-common = %epoch:%version-%release
Obsoletes: %{name} < 2:3.5.9
Obsoletes: kdenetwork-kxmlrpcd < 2:3.5.9
Obsoletes: %lib_name-kxmlrpcd < 2:3.5.9
Obsoletes: kdenetwork-common
Obsoletes: kdenetwork3-common
Provides: kdenetwork-common = %epoch:%version-%release
Provides: kdenetwork3-common = %epoch:%version-%release

%description common
Common files for kdenetwork

%files common
%defattr(-,root,root,-)
%_kde3_libdir/kde3/kfile_torrent.*
%_kde3_libdir/kde3/kio_zeroconf.*
%_kde3_datadir/services/emailwindow.desktop
%_kde3_datadir/services/kfile_torrent.desktop
%_kde3_bindir/feedbrowser
%_kde3_bindir/rssclient
%_kde3_bindir/rssservice

%_kde3_datadir/services/kntsrcfilepropsdlg.desktop
%_kde3_appsdir/remoteview/*

%dir %_kde3_appsdir/zeroconf/
%_kde3_appsdir/zeroconf/*
%_kde3_datadir/services/kded/dnssdwatcher.desktop
%_kde3_libdir/kde3/kded_dnssdwatcher.*
%_kde3_datadir/services/zeroconf.protocol

# KPF
%dir %_kde3_docdir/HTML/en/kpf/
%doc %_kde3_docdir/HTML/en/kpf/*
%_kde3_appsdir/kicker/applets/kpfapplet.desktop
%_kde3_datadir/icons/*/*/*/kpf.png
%_kde3_libdir/kde3/kpf_panelapplet.*
%_kde3_libdir/kde3/kpfpropertiesdialog.*
%_kde3_datadir/services/kpfpropertiesdialogplugin.desktop

#-----------------------------------------------------------

%package -n %lib_name-common
Group:      System/Libraries
Summary:    Libraries for kdenetwork
Obsoletes:  %lib_name < 2:3.5.9
Provides:   %lib_name = %epoch:%version-%release
Conflicts:	kdenetwork <= 3.1-31mdk
Conflicts:  kdepim <= 3.1.92
Obsoletes:  kdenetwork-kxmlrpcd < 2:3.5.9
Obsoletes:  %lib_name-kxmlrpcd < 2:3.5.9

%description -n %lib_name-common
Libraries for kdenetwork.

%if %mdkversion < 200900
%post -n %lib_name-common -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name-common -p /sbin/ldconfig
%endif

%files -n %lib_name-common
%defattr(-,root,root,-)
%_kde3_libdir/librss.la
%_kde3_libdir/librss.so.*

#-----------------------------------------------------------

%package devel
Summary: Header files for kdenetwork
Group: Development/KDE and Qt
Obsoletes: %lib_name-kopete-devel < 2:3.5.7-%mkrel 4
Obsoletes: %lib_name-common-devel < 2:3.5.7-%mkrel 4
Obsoletes: %lib_name-devel < 2:3.5.7-%mkrel 4
Provides: %lib_name-kopete-devel = %epoch:%version
Provides: %lib_name-common-devel = %epoch:%version
Provides: %lib_name-devel = %epoch:%version
Requires: %lib_name-common = %epoch:%version
Requires: %lib_name-kopete = %epoch:%version
Conflicts: kdenetwork <= 3.1-31mdk
Conflicts: kdepim <= 3.1.92
Conflicts: kdenetwork-common <= 3.1.3-37mdk
Obsoletes: kdenetwork-devel <= 2:3.5.10
Obsoletes: kdenetwork-devel
Obsoletes: kdenetwork3-devel
Provides: kdenetwork-devel = %epoch:%version-%release
Provides: kdenetwork3-devel = %epoch:%version-%release

%description devel
Header files for kdenetwork.

%files devel
%defattr(-,root,root,-)
%_kde3_libdir/*.so
%_kde3_includedir/*
%exclude %_kde3_libdir/libkdeinit_*
%exclude %_kde3_libdir/libkwireless.*

#-----------------------------------------------------------

%package kopete
Group: Graphical desktop/KDE3
Summary: Kopete
Requires: %{name}-common >= %epoch:%version-%release
Requires: %lib_name-kopete >= %epoch:%version-%release
Provides: kopete3
Provides: kde3-kopete
Obsoletes: kopete <= 0.7.1-7mdk
Obsoletes: kopete = %epoch:%version-%release
Obsoletes: kdenetwork-kopete-nowlistening < %epoch:3.5.4
Conflicts: kdenetwork-common <= 3.1.3-37mdk
Obsoletes: kdenetwork-kopete
Obsoletes: kdenetwork3-kopete
Provides: kdenetwork-kopete = %epoch:%version-%release
Provides: kdenetwork3-kopete = %epoch:%version-%release
Conflicts: lisa < 1:3.4.2-11mdk

BuildConflicts: xmms-devel
#Need for yahoo webcam
Requires:	jasper

%description kopete
Kopete is a flexible and extendable multiple protocol instant messaging
system designed as a plugin-based system.

All protocols are plugins and allow modular installment, configuration,
and usage without the main application knowing anything about the plugin 
being loaded.

The goal of Kopete is to provide users with a standard and easy to use 
interface between all of their instant messaging systems, but at the same
time also providing developers with the ease of writing plugins to support
a new protocol.

The core Kopete development team provides a handful of plugins that most
users can use, in addition to templates for new developers to base a 
plugin off of.

%post kopete
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun kopete
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files kopete
%defattr(-,root,root,-)
%_kde3_bindir/kopete
%_kde3_bindir/winpopup-*
%_kde3_libdir/kconf_update_bin/kopete-nameTracking-kconf_update
%dir %_kde3_docdir/HTML/en/kopete
%doc %_kde3_docdir/HTML/en/kopete/*
%_kde3_appsdir/kopete*
%_kde3_appsdir/kconf_update/kopete-*
%_kde3_datadir/applications/kde/kopete.desktop
%_kde3_libdir/kde3/kopete_*
%_kde3_libdir/kde3/kcm_kopete_*
%_kde3_libdir/kde3/libkrichtexteditpart.*
%_kde3_datadir/services/kconfiguredialog/kopete_*
%_kde3_datadir/sounds/*.ogg
%_kde3_datadir/servicetypes/kopete*.desktop
%_kde3_datadir/services/kopete*.desktop
%_kde3_datadir/mimelnk/application/x-icq.desktop
%_kde3_datadir/mimelnk/application/x-kopete-emoticons.desktop
%dir %_kde3_datadir/config.kcfg/
%_kde3_datadir/config.kcfg/historyconfig.kcfg
%_kde3_datadir/services/chatwindow.desktop
%_kde3_datadir/services/rdp.protocol
%_kde3_datadir/services/rssservice.desktop
%_kde3_datadir/services/aim.protocol
%_kde3_datadir/services/irc.protocol
%_kde3_iconsdir/*/*/*/kopete*
%_kde3_iconsdir/*/*/*/jabber*
%_kde3_iconsdir/*/*/*/webcam*
%_kde3_iconsdir/*/*/*/*_user*
%_kde3_iconsdir/*/*/*/*_offliners*
%_kde3_iconsdir/*/*/*/voice*
%_kde3_iconsdir/*/*/*/meta*
%_kde3_iconsdir/*/*/*/account*
%_kde3_iconsdir/*/*/*/emotico*
%_kde3_iconsdir/*/*/*/new*
%_kde3_iconsdir/*/*/*/contact*
%_kde3_iconsdir/*/*/*/status*
%_kde3_datadir/config.kcfg/kopete.kcfg
%_kde3_datadir/config.kcfg/kopeteidentityconfigpreferences.kcfg
%_kde3_datadir/services/invitation.protocol
%_kde3_datadir/services/jabberdisco.protocol
%exclude %_kde3_libdir/kde3/kcm_kopete_latex.*
%exclude %_kde3_libdir/kde3/kopete_latex.*
%exclude %_kde3_datadir/services/kopete_latex.desktop
%exclude %_kde3_datadir/services/kconfiguredialog/kopete_latex_config.desktop
%exclude %_kde3_appsdir/kopete/icons/crystalsvg/32x32/apps/latex.png
%exclude %_kde3_datadir/config.kcfg/nowlisteningconfig.kcfg

#-----------------------------------------------------------

%package  kopete-latex
Group: Graphical desktop/KDE3
Summary: Kopete latex plugin for write andd read mesages in latex
Requires: %{name}-kopete
Requires: ImageMagick	
Obsoletes: kdenetwork-kopete-latex
Obsoletes: kdenetwork3-kopete-latex
Provides: kdenetwork-kopete-latex = %epoch:%version-%release
Provides: kdenetwork3-kopete-latex = %epoch:%version-%release

%description kopete-latex
Kopete latex plugin for write andd read mesages in latexinder

%files kopete-latex
%defattr(-,root,root,-)
%_kde3_libdir/kde3/kcm_kopete_latex.*
%_kde3_libdir/kde3/kopete_latex.*
%_kde3_datadir/services/kopete_latex.desktop
%_kde3_datadir/config.kcfg/latexconfig.kcfg
%_kde3_bindir/kopete_latexconvert.sh
%_kde3_datadir/services/kconfiguredialog/kopete_latex_config.desktop
%_kde3_appsdir/kopete/icons/crystalsvg/32x32/apps/latex.png

#-----------------------------------------------------------

%package -n %lib_name-kopete
Summary: Multi-protocol plugin-based instant messenger
Group: 		System/Libraries
Obsoletes:	libkopete1 < 2:3.5.9
Provides:	libkopete1 = %epoch:%version-%release
Conflicts:	libkopete1 <= 0.7.1-7mdk
Conflicts:  kdepim <= 3.1.92
Conflicts:  kdenetwork-common <= 3.1.3-37mdk

%description -n %lib_name-kopete
Kopete is a flexible and extendable multiple protocol instant messaging
system designed as a plugin-based system.

All protocols are plugins and allow modular installment, configuration,
and usage without the main application knowing anything about the plugin
being loaded.

The goal of Kopete is to provide users with a standard and easy to use
interface between all of their instant messaging systems, but at the same
time also providing developers with the ease of writing plugins to support
a new protocol.

The core Kopete development team provides a handful of plugins that most
users can use, in addition to templates for new developers to base a
plugin off of.

%if %mdkversion < 200900
%post -n %lib_name-kopete -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name-kopete -p /sbin/ldconfig
%endif

%files -n %lib_name-kopete
%defattr(-, root, root)
%_kde3_libdir/libkopete*.so.*
%_kde3_libdir/libkopete*.la
%_kde3_libdir/kconf_update_bin/kopete-account-kconf_update
%_kde3_libdir/kconf_update_bin/kopete-pluginloader2-kconf_update

#-----------------------------------------------------------

%package -n lisa
Group: Graphical desktop/KDE3
Summary: Lisa server
Requires: %{name}-common >= %{epoch}:%version-%release
Obsoletes: ksambaplugin <= 0.5
Obsoletes: %{name}-lisa <= 2:3.5.10
Conflicts: kdenetwork-common < 1:3.4.2-11mdk
Conflicts: kdenetwork-kopete < 1:3.4.2-11mdk


%description -n lisa
LISa is intended to provide a kind of "network neighbourhood" but only
relying on the TCP/IP protocol stack, no smb or whatever.

%post -n lisa
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif
%_post_service lisa

%preun -n lisa
%_preun_service lisa

%postun -n lisa
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files -n lisa
%defattr(-,root,root)
%_kde3_bindir/lisa
%_kde3_bindir/reslisa
%dir %_kde3_datadir/applnk/.hidden/
%_kde3_datadir/applnk/.hidden/kcmkiolan.desktop
%_kde3_datadir/applnk/.hidden/kcmlisa.desktop
%_kde3_datadir/applnk/.hidden/kcmreslisa.desktop
%dir %_kde3_docdir/HTML/en/kcontrol/lanbrowser/
%doc %_kde3_docdir/HTML/en/kcontrol/lanbrowser/*
%_kde3_datadir/services/fileshare_propsdlgplugin.desktop
%_kde3_iconsdir/*/*/*/kcmsambaconf.png
%_kde3_datadir/applications/kde/fileshare.desktop
%_kde3_datadir/applications/kde/kcmsambaconf.desktop
%_kde3_appsdir/konqueror/dirtree/remote/lan.desktop
%_kde3_libdir/kde3/kio_lan.*
%_kde3_libdir/kde3/kcm_lanbrowser.*
%_kde3_libdir/kde3/fileshare_propsdlgplugin.*
%_kde3_libdir/kde3/kcm_fileshare.*
%_kde3_libdir/kde3/kcm_kcmsambaconf.*
%_kde3_appsdir/konqsidebartng/virtual_folders/services/lisa.desktop
%_kde3_appsdir/konqueror/servicemenus/smb2rdc.desktop
%dir %_kde3_datadir/services/
%_kde3_datadir/services/lan.protocol
%_kde3_datadir/services/rlan.protocol
%dir %_kde3_appsdir/lisa/
%_kde3_appsdir/lisa/README
%dir %_kde3_docdir/HTML/en/lisa
%doc %_kde3_docdir/HTML/en/lisa/*
%config(noreplace) /etc/rc.d/init.d/lisa

#-----------------------------------------------------------

%package ktalk 
Group: Graphical desktop/KDE3
Summary: Ktalk program
Provides: ktalk3
Provides: kde3-ktalk
Conflicts: kdenetwork <= 3.1-31mdk
Conflicts: kdepim <= 3.1.92
Conflicts: kdenetwork-common <= 3.1.3-37mdk
Conflicts: kdenetwork-ktalk  < 2:3.5.9-4
Obsoletes: kdenetwork-ktalk 
Obsoletes: kdenetwork3-ktalk 
Provides: kdenetwork-ktalk = %epoch:%version-%release
Provides: kdenetwork3-ktalk = %epoch:%version-%release

%description ktalk
ktalk is a graphical talk client capable of multiple connections. It contains 
an addressbook and provides word-wrap, copy and paste, configurable fonts, 
ping, and file transfer. 

%post ktalk
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun ktalk
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files ktalk
%defattr(-,root,root,-)
%_kde3_bindir/ktalkd
%_kde3_bindir/ktalkdlg
%_kde3_bindir/mail.local
%dir %_kde3_docdir/HTML/en/ktalkd/
%doc %_kde3_docdir/HTML/en/ktalkd/*
%_kde3_libdir/kde3/kcm_ktalkd.*
%dir %_kde3_datadir/sounds/
%_kde3_datadir/sounds/ktalkd.wav
%_kde3_datadir/applications/kde/kcmktalkd.desktop
%_kde3_datadir/config/ktalkdrc
%dir %_kde3_docdir/HTML/en/kcontrol/kcmtalkd/
%doc %_kde3_docdir/HTML/en/kcontrol/kcmtalkd/*
%_kde3_iconsdir/*/*/*/ktalkd*

#-----------------------------------------------------------

%package kppp
Group: Graphical desktop/KDE3
Summary: Dialer and front end for pppd
Requires: ppp, %{name}-kppp-provider
Provides: kppp3
Provides: kde3-kppp
Conflicts: kdenetwork <= 3.1-31mdk
Conflicts: kdepim <= 3.1.92
Conflicts: kdenetwork-common <= 3.1.3-37mdk
Conflicts: kdenetwork-kppp  < 2:3.5.9-4
Obsoletes: kdenetwork-kppp
Obsoletes: kdenetwork3-kppp 
Provides: kdenetwork-kppp = %epoch:%version-%release
Provides: kdenetwork3-kppp = %epoch:%version-%release

%description kppp
Kppp is a dialer and front end for pppd.

%post kppp
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun kppp
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files kppp
%defattr(-,root,root,-)
%dir %_sysconfdir/pam.d/
%config(noreplace) %_sysconfdir/pam.d/kppp3
%attr(4755,root,root) %_kde3_bindir/kppp
%_kde3_bindir/kppplogview
%dir %_kde3_appsdir/kppp
%_kde3_appsdir/kppp/*
%_kde3_datadir/applications/kde/Kppp.desktop
%_kde3_datadir/applications/kde/kppplogview.desktop
%_kde3_iconsdir/*/*/*/kppp.png
%dir %_kde3_docdir/HTML/en/kppp/
%doc %_kde3_docdir/HTML/en/kppp/*
%exclude %_kde3_appsdir/kppp/Rules
%exclude %_kde3_appsdir/kppp/Provider

#-----------------------------------------------------------

%package kppp-provider
Group: Graphical desktop/KDE3
Summary: List of providers for pppd
Conflicts: kdepim <= 3.1.92
Conflicts: kdenetwork-common <= 3.1.3-37mdk
Obsoletes: kdenetwork-kppp-provider
Obsoletes: kdenetwork3-kppp-provider 
Provides: kdenetwork-kppp-provider = %epoch:%version-%release
Provides: kdenetwork3-kppp-provider = %epoch:%version-%release

%description kppp-provider
List of providers for kppp

%files kppp-provider
%defattr(-,root,root,-)
%_kde3_appsdir/kppp/Rules
%_kde3_appsdir/kppp/Provider

#-----------------------------------------------------------

%package ksirc
Group: Graphical desktop/KDE3
Summary: KDE IRC
Provides: ksirc3
Provides: kde3-ksirc
Conflicts: kdenetwork <= 3.1-31mdk
Conflicts: kdepim <= 3.1.92
Conflicts: kdenetwork-common <= 3.1.3-37mdk
Obsoletes: kdenetwork-kxmlrpcd < 2:3.5.9
Obsoletes: %lib_name-ksirc < 2:3.5.9
Obsoletes: kdenetwork-ksirc <= 2:3.5.10
Obsoletes: kdenetwork-ksirc
Obsoletes: kdenetwork3-ksirc 
Provides: kdenetwork-ksirc = %epoch:%version-%release
Provides: kdenetwork3-ksirc = %epoch:%version-%release

%description ksirc
KDE internet relay chat client.

%post ksirc
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun ksirc
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files ksirc
%defattr(-,root,root,-)
%_kde3_bindir/ksirc
%_kde3_bindir/dsirc
%_kde3_datadir/applications/kde/ksirc.desktop
%dir %_kde3_docdir/HTML/en/ksirc/
%doc %_kde3_docdir/HTML/en/ksirc/*
%_kde3_datadir/config/ksircrc
%_kde3_libdir/kde3/ksirc.*
%dir %_kde3_appsdir/ksirc/
%_kde3_appsdir/ksirc/*
%_kde3_iconsdir/*/*/*/ksirc.png
%_kde3_libdir/libkdeinit_ksirc.*

#-----------------------------------------------------------

%package kwifimanager
Group: Graphical desktop/KDE3
Summary: KWifimanager
Provides: kwifimanager3
Provides: kde3-kwifimanager
Conflicts: kdenetwork <= 3.1-31mdk
Conflicts: kdepim <= 3.1.92
Conflicts: kdenetwork-common < 1:3.4.2-11mdk
Requires: wireless-tools
Obsoletes: %lib_name-kwifimanager < 2:3.5.9
Obsoletes: kdenetwork-kwifimanager
Obsoletes: kdenetwork3-kwifimanager
Provides: kdenetwork-kwifimanager = %epoch:%version-%release
Provides: kdenetwork3-kwifimanager = %epoch:%version-%release

%description kwifimanager
A wireless LAN connection monitor.

%post kwifimanager
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun kwifimanager
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files kwifimanager
%defattr(-,root,root,-)
%_kde3_bindir/kwifimanager
%_kde3_datadir/applications/kde/kcmwifi.desktop
%_kde3_datadir/applications/kde/kwifimanager.desktop
%_kde3_appsdir/kicker/applets/kwireless.desktop
%dir %_kde3_appsdir/kwifimanager/
%_kde3_appsdir/kwifimanager/*
%_kde3_iconsdir/*/*/*/kwifimanager*
%_kde3_libdir/libkwireless.*
%_kde3_libdir/kde3/kcm_wifi.*
%dir %_kde3_docdir/HTML/en/kwifimanager/
%doc %_kde3_docdir/HTML/en/kwifimanager/*

#-----------------------------------------------------------

%package kdict
Group: Graphical desktop/KDE3
Summary: Kdict program
Provides: kdict3
Provides: kde3-kdict
Conflicts: kdenetwork <= 3.1-31mdk
Conflicts: kdepim <= 3.1.92
Conflicts: kdenetwork-common <= 3.1.3-37mdk
Obsoletes: kdenetwork-kxmlrpcd < 2:3.5.9
Obsoletes: %lib_name-kdict < 2:3.5.9
Obsoletes: kdenetwork-kdict
Obsoletes: kdenetwork3-kdict
Provides: kdenetwork-kdict = %epoch:%version-%release
Provides: kdenetwork3-kdict = %epoch:%version-%release

%description kdict
Kdict is a graphical client for the DICT Protocol. It enables you 
to search through dictionary-like databases for a word or phrase, then 
displays suitable definitions. 

%post kdict
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun kdict
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files kdict
%defattr(-,root,root,-)
%_kde3_bindir/kdict
%dir %_kde3_docdir/HTML/en/kdict/
%doc %_kde3_docdir/HTML/en/kdict/*
%dir %_kde3_appsdir/kdict/
%_kde3_appsdir/kdict/*
%_kde3_datadir/applications/kde/kdict.desktop
%_kde3_libdir/kde3/kdict_panelapplet.*
%_kde3_appsdir/kicker/applets/kdictapplet.desktop
%_kde3_iconsdir/*/*/*/kdict*
%_kde3_libdir/kde3/kdict.*
%_kde3_libdir/kde3/kio_jabberdisco.*
%_kde3_libdir/libkdeinit_kdict.*

#-----------------------------------------------------------

%package kget
Group: Graphical desktop/KDE3
Summary: Kget program
Provides: kget3
Provides: kde3-kget
Conflicts: kdenetwork <= 3.1-31mdk
Conflicts: kdepim <= 3.1.92
Conflicts: kdenetwork-common <= 3.1.3-37mdk
Obsoletes: kdenetwork-kget
Obsoletes: kdenetwork3-kget
Provides: kdenetwork-kget = %epoch:%version-%release
Provides: kdenetwork3-kget = %epoch:%version-%release

%description kget
An advanced download manager for KDE.

%post kget
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun kget
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files kget
%defattr(-,root,root,-)
%_kde3_bindir/kget
%dir %_kde3_appsdir/kget/
%_kde3_appsdir/kget/*
%_kde3_appsdir/khtml/kpartplugins/kget_plug_in.desktop
%_kde3_libdir/kde3/khtml_kget.*
%_kde3_datadir/applications/kde/kget.desktop
%_kde3_datadir/mimelnk/application/x-kgetlist.desktop
%_kde3_appsdir/khtml/kpartplugins/kget_plug_in.rc
%_kde3_iconsdir/*/*/*/khtml_kget*
%_kde3_iconsdir/*/*/*/kget*
%dir %_kde3_docdir/HTML/en/kget/
%doc %_kde3_docdir/HTML/en/kget/*

%_kde3_appsdir/konqueror/servicemenus/kget_download.desktop

#-----------------------------------------------------------

%package krfb
Group: Graphical desktop/KDE3
Summary: Krfb, Krdc program
Provides: krdc3
Provides: krfb3
Provides: kde3-krdc
Provides: kde3-krfb 
Conflicts: kdenetwork <= 3.1-31mdk
Conflicts: kdepim <= 3.1.92
Conflicts: kdenetwork-common <= 3.1.3-37mdk
Obsoletes: kdenetwork-krfb
Obsoletes: kdenetwork3-krfb
Provides: kdenetwork-krfb = %epoch:%version-%release
Provides: kdenetwork3-krfb = %epoch:%version-%release

%description krfb
KDE Desktop Sharing allows you to invite somebody at a remote 
location to watch and possibly control your desktop.

%post krfb
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun krfb
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files krfb
%defattr(-,root,root,-)
%_kde3_bindir/krdc
%_kde3_bindir/krfb
%_kde3_bindir/krfb_httpd
%_kde3_datadir/services/vnc.protocol
%_kde3_datadir/services/kinetd_krfb.desktop
%dir %_kde3_appsdir/kinetd/
%_kde3_appsdir/kinetd/*
%dir %_kde3_docdir/HTML/en/krfb/
%doc %_kde3_docdir/HTML/en/krfb/*
%doc %_kde3_docdir/HTML/en/krdc/*
%_kde3_datadir/applications/kde/kcmkrfb.desktop
%_kde3_datadir/applications/kde/krdc.desktop
%_kde3_datadir/applications/kde/krfb.desktop
%dir %_kde3_appsdir/krfb/
%_kde3_appsdir/krfb/*
%dir %_kde3_appsdir/krdc/
%_kde3_appsdir/krdc/*
%_kde3_libdir/kde3/kcm_krfb.*
%_kde3_libdir/kde3/kded_kinetd.*
%_kde3_iconsdir/*/*/*/krfb*
%_kde3_iconsdir/*/*/*/krdc*
%_kde3_datadir/servicetypes/kinetdmodule.desktop
%_kde3_datadir/services/kded/kinetd.desktop
%_kde3_datadir/services/kinetd_krfb_httpd.desktop

#-----------------------------------------------------------

%package knewsticker
Group: Graphical desktop/KDE3
Summary: RDF newsticker applet
Provides: knewsticker3
Provides: kde3-knewsticker
Obsoletes: %lib_name-knewsticker < 2:3.5.9
Conflicts: kdenetwork <= 3.1-31mdk
Conflicts: kdepim <= 3.1.92
Conflicts: kdenetwork-common < 1:3.4.2-11mdk
Obsoletes: kdenetwork-knewsticker
Obsoletes: kdenetwork3-knewsticker
Provides: kdenetwork-knewsticker = %epoch:%version-%release
Provides: kdenetwork3-knewsticker = %epoch:%version-%release

%description knewsticker
Knewsticker: RDF newsticker applet

%post knewsticker
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%update_menus
%endif

%postun knewsticker
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%if %mdkversion < 200900
%clean_menus
%endif

%files knewsticker
%defattr(-,root,root,-)
%_kde3_bindir/knewstickerstub 
%dir %_kde3_docdir/HTML/en/knewsticker/
%doc %_kde3_docdir/HTML/en/knewsticker/*
%_kde3_datadir/applications/kde/knewsticker-standalone.desktop
%dir %_kde3_appsdir/knewsticker/
%_kde3_appsdir/knewsticker/*
%_kde3_appsdir/kicker/applets/knewsticker.desktop
%dir %_kde3_appsdir/kconf_update/
%_kde3_appsdir/kconf_update/knewsticker.upd
%_kde3_appsdir/kconf_update/knt-0.1-0.2.pl
%_kde3_iconsdir/*/*/*/knewsticker.png
%_kde3_datadir/applnk/.hidden/knewstickerstub.desktop
%_kde3_libdir/kde3/knewsticker_panelapplet.*
%_kde3_libdir/kde3/libkntsrcfilepropsdlg.*

#-----------------------------------------------------------

%prep
%setup -q -n kdenetwork-%version
%patch1 -p0
%patch2 -p1
#%patch3 -p0
#%patch4 -p0
%patch5 -p0
#%patch6 -p1
#%patch7 -p0
%patch8 -p1
#%patch9 -p1
%patch10 -p0
%patch11 -p0

%build

PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/
export xdg_menudir=%_sysconfdir/xdg/kde/menus

make -f admin/Makefile.common cvs

%configure_kde3 \
    --with-extra-includes=/usr/include/avahi-compat-libdns_sd/:/opt/kde3/include/tqt \
    --with-extra-libs=/opt/kde3/lib \
    --without-xmms
	
%make

%install
rm -fr %buildroot
%makeinstall_std

install -d -m 0755 %buildroot/etc/rc.d/init.d
install -m 0755 %SOURCE2 %buildroot/etc/rc.d/init.d/lisa

install -d -m 0755 %buildroot/%_sysconfdir/pam.d/
install -m 0644 %SOURCE1 %buildroot/%_sysconfdir/pam.d/kppp3

%clean
rm -fr %buildroot


%changelog
* Fri Jul 22 2010 Tim Williams <tim@my-place.org.uk> 2:3.5.12-1mvt2010.2
+ Update to Trinity 3.5.12 sources
+ Add xdg and build process patches
+ Fix kdenetwork-3.5.7-fix-kdebug-120625.patch
- Remove kdenetwork-3.5.8-fix-desktop-files.patch
- Remove kdenetwork-3.5.9-fix-underlinking.patch
- Remove kdenetwork-3.5.10-gcc44.patch
- Remove kdenetwork-3.5.10-kopete_fix_yahoo.patch

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 2:3.5.10-8mvt2010.0
+ Rebuild for MDV 2010.1

* Tue Jan 12 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 2:3.5.10-7mvt2010.0
+ Rebuilt for 2010.0
+ Fix automake 1.11 and autoconf 2.64 incompability
+ Fix kopete yahoo protocol

* Thu Apr 23 2009 Frederic Crozat <fcrozat@mandriva.com> 2:3.5.10-5mdv2009.1
+ Revision: 368894
- Fix uninstallable package

* Wed Apr 22 2009 Frederic Crozat <fcrozat@mandriva.com> 2:3.5.10-4mdv2009.1
+ Revision: 368670
- Fix incorrect dependency on kdenetwork-common (Mdv bug #50180)

* Wed Apr 22 2009 Nicolas Lécureuil <neoclust@mandriva.org> 2:3.5.10-3mdv2009.1
+ Revision: 368612
- Fix conflicts

* Fri Apr 03 2009 Nicolas Lécureuil <neoclust@mandriva.org> 2:3.5.10-2mdv2009.1
+ Revision: 363689
- Fix Requires for lisa

* Thu Apr 02 2009 Helio Chissini de Castro <helio@mandriva.com> 2:3.5.10-1mdv2009.1
+ Revision: 363587
- Pushing back kde3 kdenetwork :-/
- Another headache generated for the bring kde3 back to live

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - import kdenetwork

