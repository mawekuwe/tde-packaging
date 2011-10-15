%define _requires_exceptions devel\(linux-gate\)\\|perl\(open\)

%define support_ldap 1

%define compile_apidox 0
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define compile_smb 1
%{?_no_smb: %{expand: %%global compile_smb 0}}

%define use_kickoff_menu 1
%{?_disable_kickoff_menu: %{expand: %%global use_kickoff_menu 0}}

%define lib_name_orig libkdebase
%define lib_major 4
%define lib_name %mklibname kde3base %lib_major
%define lib_name_fixed %mklibname kdebase %lib_major
%define epoch_kdelibs 30000000
%define epoch_arts 30000001

%define lib_name_orig_kttsd %mklibname kttsd
%define lib_major_kttsd 0
%define lib_name_kttsd %lib_name_orig_kttsd%lib_major_kttsd

%define oname kdebase
%define rname kdebase3

Name: kde3-kdebase
Summary: K Desktop Environment - Core files
Version: 3.5.12
Release: %mkrel 6
Epoch: 1
Group: Graphical desktop/KDE3
License:	GPL
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
Source1: mandriva-profile-chooser-2.0.tar.bz2
Source2: kdm-migrate.pl
Source3: mandriva-startkde
Source4: kdebase-3.5-kde.pam
Source5: kdebase-3.5-kde3-np
Source8: kdebase-3.5-wizard_small.png
Source9: kdebase-konsole-fixed-font.conf
Source10: kdeeject
Source11: net_applet.desktop
Source12: xsettings-kde.desktop
Source13: mandriva-mdvonline.desktop
Source14: mandriva-gurpmi.desktop
Source15: x-urpmi.desktop
Source16: x-urpmi-media.desktop
Source100: kickoff-mandriva-data.tar.bz2 
#Source200: kdebase-3.5.12-configure

###             ###
### Patch party ###
###             ###
# Please keep it this section organised
Patch1: kdebase-kscreensaver-pamd.patch
Patch2:	kdebase-3.5.3-fix-media-fuser.patch
Patch3:	kdebase-3.4.0-fix-scrnsaver.patch
Patch4:	kdebase-3.5.10-fix-vibrate-dialog.patch
Patch7: kdebase-3.3.2-fix-kdm-theme-mdk.patch
Patch8: kdebase-3.4.2-fix-kdm-server-args.patch
Patch9: kdebase-3.5.3-logout-without-confirmation.patch
Patch20: kdebase-3.5.7-clock-drakclock.patch
# LZMA support
Patch21: kdebase-3.5.7-lzma_support.patch 
# GTK ia_ora settings fix
Patch22: kdebase-3.5.4-fix-gtk-style.patch
Patch24: kdebase-3.5.7-kdesktop_firstrun.patch
Patch26: kdebase-3.5.7-translation-override.patch
# fix firstboot focusing
Patch27: kdebase-3.4.2-mdkft.patch
Patch28: kdebase-3.5.7-khelpcenter-htdigsearch-path.patch
Patch35: kdebase-post-3.5.8-add-change-session-icon.patch
Patch37: kdebase-post-3.5.9-screensaver-onlyshowin-kde.patch
Patch39: kdebase-post-3.5.9-Fix-kcontrol-menu-entry.patch
Patch41: kdebase-3.5.12-kdm-kcontrol-usericon.patch
Patch42: kdebase-post-3.5.9-bookmark-global-copy.patch
Patch43: kdebase-3.5.9-update-usb.ids.patch
Patch44: kdebase-post-3.5.12-fix-choose-webbrowser-kcontrol.patch
Patch60: khotkeys-only_kde.patch
################################################
#Patches from Pardus Linux
Patch104: detect-media-types.patch
Patch111: mediamanager-mount-point-utf8.diff
Patch112: media_saferemove.patch
Patch113: turkish-preview.patch
################################################
Patch120: fix_openssl.patch
Patch130: kdebase-3.5.12-config.patch
Patch131: kde-3.5.10-acinclude.patch
Patch132: kdebase-3.5.12-move-xdg-menu-dir.patch
Patch133: kdebase-3.5.12-startkde.patch
Patch134: kdebase-3.5.12-menus.patch
Patch135: kdebase-3.5.12-fix-kcontrol-menu.patch

BuildRequires: kdelibs3-devel >= %epoch_kdelibs:3.5.5
BuildRequires: fontconfig-devel >= 2.1-9mdk
BuildRequires: mkfontdir
BuildRequires: mkfontscale
BuildRequires: pam-devel
BuildRequires: freetype2-devel
BuildRequires: libsasl-devel
BuildRequires: openldap-devel
BuildRequires: avahi-compat-libdns_sd-devel 
BuildRequires: avahi-client-devel
BuildRequires: libsmbclient-devel > 3.0
BuildRequires: libieee1284-devel
BuildRequires: OpenEXR-devel
BuildRequires: hal-devel 
BuildRequires: libdbus-qt-1-devel
BuildRequires: libusb-devel
BuildRequires: libxml2-utils
BuildRequires: X11-devel
BuildRequires: mesaglut-devel
BuildRequires: bdftopcf
BuildRequires: imake
BuildRequires: automake >= 1.6.1
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%endif
BuildRequires: autoconf >= 1:2.65
BuildRequires: libraw1394-devel
BuildRequires: qt3-doc
BuildRequires: lua-devel
BuildRequires: resmgr-devel
BuildRequires: xinitrc
BuildRequires: lm_sensors-devel >  2.10
BuildRequires: liblazy-devel >= 0.2
BuildRequires: libbeagle-devel >= 0.3.0
%if %use_kickoff_menu
BuildConflicts: lm_utils
BuildConflicts: lm_utils-devel
BuildConflicts: liblm_sensors1
BuildConflicts: liblm_sensors1-devel
%endif
Suggests: %name-progs
Suggests: %name-konsole
Suggests: %name-kdeprintfax
Suggests: %name-kate
Suggests: %name-kmenuedit
Suggests: %name-ksysguard
Conflicts: kdebase <= 3.1.94-13mdk
Provides: %oname = %{epoch}:%{version}-%{release}
Provides: %rname = %{epoch}:%{version}-%{release}
BuildRoot: %_tmppath/%name-%version-%release-root

%description
Core applications for the K Desktop Environment.
Here is an overview of the directories:

	- drkonqi: if ever an app crashes (heaven forbid!) then Dr.Konqi will be so
          kind and make a stack trace. This is a great help for the
          developers to fix the bug.
	- kappfinder: searches your hard disk for non-KDE applications, e.g. Acrobat
             Reader (tm) and installs those apps under the K start button
	- kate: a fast and advanced text editor with nice plugins
	- kcheckpass: small program to enter and check passwords, only to be used by
             other programs
	- kcontrol: the KDE Control Center allows you to tweak the KDE settings
	- kdcop: GUI app to browse for DCOP interfaces, can also execute them
	- kdebugdialog: allows you to specify which debug messages you want to see
	- kdeprint: the KDE printing system
	- kdesktop: you guessed it: the desktop above the panel
	- kdesu: a graphical front end to "su"
	- kdm: replacement for XDM, for those people that like graphical logins
	- kfind: find files
	- khelpcenter: the app to read all great documentation about KDE
	- khotkeys: intercepts keys and can call applications
	- kicker: the panel at the botton with the K start button and the 
				taskbar etc
	- kioslave: infrastructure that helps make every application internet 
				enabled e.g. to directly save a 
				file to ftp://place.org/dir/file.txt
	- klipper: enhances and extenses the X clipboard
	- kmenuedit: edit for the menu below the K start button
	- konqueror: the file manager and web browser you get easily used to
	- kpager: applet to show the contents of the virtual desktops
	- kpersonalizer: the customization wizard you get when you first start KDE
	- kreadconfig: a tool for shell scripts to get info from KDE's config files
	- kscreensaver: the KDE screensaver environment and lot's of savers
	- ksmserver: the KDE session manager (saves program status on login, 
				restarts those program at the next login)
	- ksplash: the screen displayed while KDE starts
	- kstart: to launch applications with special window properties
         such as iconified etc
	- ksysguard: task manager and system monitor, even for remote systems
	- ksystraycmd: allows to run any application in the system tray
	- ktip: gives you tips how to use KDE
	- kwin: the KDE window manager
	- kxkb: a keyboard map tool
	- legacyimport: odd name for a cute program to load GTK themes
	- libkonq: some libraries needed by Konqueror
	- nsplugins: together with OSF/Motif or Lesstif allows you to use Netscape
			(tm) plugins in Konqueror

%files
%doc README

#-----------------------------------------------------------------------------

%package progs
Summary: K Desktop Environment - Core files
Group: Development/KDE and Qt
Obsoletes: kfontinst < 1:3.5.9
Obsoletes: kio_fish < 1:3.5.9
Provides: kfontinst3
Provides: kde3-kfontinst 
Provides: kio_fish3 
Provides: kde3-kio_fish
Provides: %oname-progs = %{epoch}:%{version}-%{release}
Provides: %rname-progs = %{epoch}:%{version}-%{release}
Obsoletes:       %rname-common
Obsoletes:       %oname-common
Requires(post):  desktop-file-utils
Requires(postun):desktop-file-utils
Requires: 	 ksplash-engine-moodin
# We use an external krandr
Requires: krandr
# For kio-fish MDK bug#16934
Requires: openssh-clients
Requires: xinit
Requires: iceauth
Requires: xkbcomp
Requires: xsetroot
Requires: xset
Requires: setxkbmap
Requires: xmessage
Requires: htdig
Requires: xprop
Obsoletes: kdebase <= 3.1-83mdk
Obsoletes: kdebase3 <= 1:3.5.9
Obsoletes: mandrake-menu-directory 
Provides: kdebase3 = %{epoch}:%{version}-%{release}
Obsoletes: %rname-common
Obsoletes: %oname-common
Conflicts: kdebase-common <= 3.2.3-97mdk
Conflicts: kdebase3-common < 1:3.5.9.mdv
Conflicts: kdeutils-kdepasswd <= 3.2.3-100mdk
Conflicts: mandrakelinux-kde-config-file <= 10.1-6mdk
Conflicts: kdeutils =< 2.2.2-28mdk  
Conflicts: kdebase <= 3.1-84mdk
Conflicts: galaxy-kde < 0.9.5-1mdk
Conflicts: galaxy-kde-kwin < 0.9.5-1mdk
Requires(pre):	kdelibs3 >= %{epoch_kdelibs}:3.3.2-6mdk
Requires: arts3 >= %{epoch_arts}:1.1.2-2mdk
Requires: %lib_name = %{epoch}:%{version}-%{release}
Requires: kde-config-file >= 10.2-2mdk
#Requires: mdklaunchhelp >= 9.1
Requires: kdebase-servicemenu
Requires: initscripts >= 7.04-3mdk 
Requires: desktop-common-data
Requires: indexhtml >= 9.0-2mdk
Requires: libsmbclient
Requires: %name-common = %{epoch}:%{version}-%{release}
Requires: qt >= 3.3.6-1mdk
Requires: kdelibs3-common >= 3.3.2-54mdk
Requires: sasl-plug-plain
Requires: %name-ksysguard

%description progs
Core applications for the K Desktop Environment.
Here is an overview of the directories:

	- drkonqi: if ever an app crashes (heaven forbid!) then Dr.Konqi will be so
          kind and make a stack trace. This is a great help for the
          developers to fix the bug.
	- kappfinder: searches your hard disk for non-KDE applications, e.g. Acrobat
             Reader (tm) and installs those apps under the K start button
	- kate: a fast and advanced text editor with nice plugins
	- kcheckpass: small program to enter and check passwords, only to be used by
             other programs
	- kcontrol: the KDE Control Center allows you to tweak the KDE settings
	- kdcop: GUI app to browse for DCOP interfaces, can also execute them
	- kdebugdialog: allows you to specify which debug messages you want to see
	- kdeprint: the KDE printing system
	- kdesktop: you guessed it: the desktop above the panel
	- kdesu: a graphical front end to "su"
	- kdm: replacement for XDM, for those people that like graphical logins
	- kfind: find files
	- khelpcenter: the app to read all great documentation about KDE
	- khotkeys: intercepts keys and can call applications
	- kicker: the panel at the botton with the K start button and the 
				taskbar etc
	- kioslave: infrastructure that helps make every application internet 
				enabled e.g. to directly save a 
				file to ftp://place.org/dir/file.txt
	- klipper: enhances and extenses the X clipboard
	- kmenuedit: edit for the menu below the K start button
	- konqueror: the file manager and web browser you get easily used to
	- kpager: applet to show the contents of the virtual desktops
	- kpersonalizer: the customization wizard you get when you first start KDE
	- kreadconfig: a tool for shell scripts to get info from KDE's config files
	- kscreensaver: the KDE screensaver environment and lot's of savers
	- ksmserver: the KDE session manager (saves program status on login, 
				restarts those program at the next login)
	- ksplash: the screen displayed while KDE starts
	- kstart: to launch applications with special window properties
         such as iconified etc
	- ksystraycmd: allows to run any application in the system tray
	- ktip: gives you tips how to use KDE
	- kwin: the KDE window manager
	- kxkb: a keyboard map tool
	- legacyimport: odd name for a cute program to load GTK themes
	- libkonq: some libraries needed by Konqueror
	- nsplugins: together with OSF/Motif or Lesstif allows you to use Netscape
			(tm) plugins in Konqueror

%post progs
%make_session

%postun progs
%make_session

%files progs
%defattr(-,root,root)
%_sysconfdir/X11/wmsession.d/*KDE3
%_kde3_bindir/kde3
%_kde3_bindir/kfontinst
%_kde3_bindir/khc_indexbuilder
%_kde3_bindir/kwin_killer_helper
%_kde3_bindir/kwriteconfig
%_kde3_bindir/kinfocenter
%_kde3_bindir/klocaldomainurifilterhelper
%_kde3_bindir/appletproxy
%_kde3_bindir/drkonqi
%_kde3_bindir/kdialog
%_kde3_bindir/extensionproxy
%_kde3_bindir/kdm-migrate.pl
%_kde3_bindir/kaccess
%_kde3_bindir/kappfinder
%attr(4755,root,root) %_kde3_bindir/kcheckpass
%_kde3_bindir/kcminit
%_kde3_bindir/kcontrol
%_kde3_bindir/kwin_rules_dialog
%_kde3_bindir/kcontroledit
%_kde3_bindir/kdeinstallktheme
%_kde3_bindir/kdepasswd
%_kde3_bindir/kfontview
%dir %_kde3_appsdir/kfontview/
%_kde3_appsdir/kfontview/kfontviewpart.rc
%_kde3_appsdir/kfontview/kfontviewui.rc
%dir %_kde3_appsdir/remoteview/
%_kde3_appsdir/remoteview/smb-network.desktop
%_kde3_bindir/kdcop
%_kde3_bindir/kdebugdialog
%_kde3_bindir/kdeeject
%_kde3_bindir/kdesktop
%_kde3_bindir/kfind
%_kde3_bindir/ksystraycmd
%_kde3_bindir/kdesktop_lock
%_kde3_bindir/kdesu
%attr(2755,root,nogroup) %_kde3_bindir/kdesud
%_kde3_bindir/keditbookmarks
%_kde3_bindir/keditfiletype
%_kde3_bindir/kfmclient
%_kde3_bindir/khelpcenter
%_kde3_bindir/khotkeys
%_kde3_bindir/kicker
%_kde3_bindir/kjobviewer
%_kde3_bindir/klipper
%_kde3_bindir/konqueror
%_kde3_bindir/kpager
%_kde3_bindir/kpersonalizer
%_kde3_bindir/kprinter 
%_kde3_bindir/krdb
%_kde3_bindir/kreadconfig
%_kde3_bindir/ksmserver
%_kde3_bindir/ksplash
%_kde3_bindir/kstart
%_kde3_bindir/ktip
%_kde3_bindir/kwebdesktop
%_kde3_bindir/kwin
%_kde3_bindir/kwrite
%_kde3_bindir/kxkb
%_kde3_bindir/startkde*

%_kde3_bindir/kpm
%_kde3_bindir/lpr-kprinter
%_kde3_bindir/qtcups
#
#
#
# David - 3.0-0.beta1.8mdk - Screensavers
#                            Please not included those which can have legal
#                            issue (kmatrix is a good example)
%_kde3_bindir/kblankscrn.kss
%_kde3_bindir/krandom.kss
%_kde3_bindir/kapplymousetheme
#_kde3_bindir/kio_system_documenthelper
%_kde3_bindir/kcminit_startup

#-----------------------------------------------------------------------------

%package ksysguard
Summary: Ksysguard
Group: Graphical desktop/KDE3
Provides: %oname-ksysguard = %{epoch}:%{version}-%{release}
Provides: %rname-ksysguard = %{epoch}:%{version}-%{release}
Obsoletes: %oname-ksysguard
Obsoletes: %rname-ksysguard
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description ksysguard
KDE System Guard Daemon is the daemon part of ksysguard. The daemon can
be installed on a remote machine to enable ksysguard on another machine
to monitor it through the daemon running there.

%files ksysguard
%defattr(-,root,root)
%_kde3_bindir/ksysguardd
%_kde3_bindir/ksysguard
%dir %_kde3_appsdir/ksysguard/
%_kde3_appsdir/ksysguard/*
%_kde3_datadir/applications/kde/ksysguard.desktop
%doc %_kde3_docdir/HTML/en/ksysguard
%exclude %_sysconfdir/ksysguarddrc

#-----------------------------------------------------------------------------

%package konsole
Summary: Konsole
Group: Graphical desktop/KDE3
Requires: %name-common = %{epoch}:%{version}-%{release}
Obsoletes: %lib_name-konsole < 1:3.5.9
Conflicts: %lib_name < %epoch:3.5.3-11mdv2007.0
Requires: %name-progs = %{epoch}:%{version}-%{release}
Requires: fontconfig
Requires: x11-font-misc-misc
Provides: konsole3 = %{epoch}:%{version}-%{release}
Provides: kde3-konsole = %{epoch}:%{version}-%{release}
Provides: %oname-konsole = %{epoch}:%{version}-%{release}
Provides: %rname-konsole = %{epoch}:%{version}-%{release}
Obsoletes: %oname-konsole
Obsoletes: %rname-konsole

%description konsole
A shell program similar to xterm for KDE

%post konsole
/usr/sbin/update-alternatives --install /usr/bin/xvt xvt /usr/bin/konsole 35
/usr/bin/fc-cache
%if %mdkversion < 200900
%update_menus
%endif

%postun konsole
%if %mdkversion < 200900
%clean_menus
%endif
if [ "$1" = "0" ]; then
   /usr/sbin/update-alternatives --remove xvt /usr/bin/konsole
fi

%files konsole
%defattr(-,root,root)
%_kde3_bindir/konsole
%dir %_kde3_appsdir/konsole/
%_kde3_appsdir/konsole/*
%_kde3_datadir/applications/kde/konsole.desktop
%doc %_kde3_docdir/HTML/en/kcontrol/kcmkonsole
%doc %_kde3_docdir/HTML/en/konsole
%_kde3_libdir/kde3/kcm_konsole.*
%_kde3_libdir/kde3/kickermenu_konsole.*
%_kde3_libdir/kde3/libkonsolepart.*
%_kde3_libdir/kde3/konsole.*
%_sysconfdir/fonts/conf.d/99-konsole.conf
%_kde3_libdir/libkdeinit_konsole.*
# We dont need 9x15, as already provided by system
%exclude %_kde3_appsdir/konsole/fonts/9x15.pcf.gz 

#-----------------------------------------------------------------------------

%package kdeprintfax
Summary:	Kdeprintfax
Group:		Graphical desktop/KDE3
Requires:	%name-progs = %{epoch}:%{version}-%{release}
Requires:	%name-common = %{epoch}:%{version}-%{release}
Requires:	enscript
Requires:	efax
Provides: kdeprintfax3 = %{epoch}:%{version}-%{release}
Provides: kde3-kdeprintfax = %{epoch}:%{version}-%{release}
Provides: %oname-kdeprintfax = %{epoch}:%{version}-%{release}
Provides: %rname-kdeprintfax = %{epoch}:%{version}-%{release}
Obsoletes: %oname-kdeprintfax
Obsoletes: %rname-kdeprintfax

%description kdeprintfax
Programm to send fax

%files kdeprintfax
%defattr(-,root,root)
%_kde3_bindir/kdeprintfax
%dir %_kde3_appsdir/kdeprintfax
%_kde3_appsdir/kdeprintfax/*
%_kde3_datadir/applications/kde/kdeprintfax.desktop

#-----------------------------------------------------------------------------

%package kate
Summary:	Kate
Group:		Graphical desktop/KDE3
Requires:	%name-progs = %{epoch}:%{version}-%{release}
Requires:	%name-common = %{epoch}:%{version}-%{release}
Requires:	%lib_name-kate = %{epoch}:%{version}-%{release}
Conflicts: %lib_name < %epoch:3.5.3-11mdv2007.0
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Provides: kate3  = %{epoch}:%{version}-%{release}
Provides: kde3-kate  = %{epoch}:%{version}-%{release}
Provides: %oname-kate = %{epoch}:%{version}-%{release}
Provides: %rname-kate = %{epoch}:%{version}-%{release}
Obsoletes: %oname-kate
Obsoletes: %rname-kate

%description kate
A fast and advanced text editor with nice plugins

%files kate
%defattr(-,root,root)
%_kde3_bindir/kate
%config(noreplace) %_kde3_datadir//config/katerc
%doc %_kde3_docdir/HTML/en/kate
%dir %_kde3_appsdir/kate/
%_kde3_appsdir/kate/*
%_kde3_datadir/applications/kde/kate.desktop
%_kde3_libdir/kde3/kate.la
%_kde3_libdir/kde3/kate.so

#-----------------------------------------------------------------------------

%package -n %lib_name-kate
Summary:	Libraries for Kate
Group:		System/Libraries
Provides: 	%lib_name_orig-kate = %{epoch}:%{version}-%{release}
Obsoletes: %lib_name-kate-devel < 1:3.5.9
Conflicts: kdebase <= 3.1.94-13mdk
Conflicts: %lib_name < %epoch:3.5.3-11mdv2007.0

%description -n %lib_name-kate
Libraries for kate program

%files -n %lib_name-kate
%defattr(-,root,root)
%_kde3_libdir/libkdeinit_kate.la
%_kde3_libdir/libkateinterfaces.la
%_kde3_libdir/libkateinterfaces.so.*
%_kde3_libdir/libkdeinit_kate.so
%_kde3_libdir/libkateutils.so.*
%_kde3_libdir/libkateutils.la
%_kde3_libdir/kde3/kickermenu_kate.*

#-----------------------------------------------------------------------------

%package -n %lib_name
Group:   System/Libraries
Summary: Libraries for kdebase
Requires: %name-session-plugins
%if %use_kickoff_menu
Requires: kde3-kio-sysinfo
Requires: kde3-kickoff-i18n
%endif
Provides: %lib_name_orig = %{epoch}:%{version}-%{release}
Provides: %lib_name_fixed = %{epoch}:%{version}-%{release}
Conflicts: %lib_name_kttsd <= 0.3.0
Conflicts: kdeartwork <= 3.3.2-14mdk
Conflicts: %lib_name <= %epoch:3.5.5-10mdv2007.1
Obsoletes: kdebase-kcontrol-data < 1:3.5.9

%description -n %lib_name
Libraries for the K Desktop Environment.

%files -n %lib_name
%defattr(-,root,root)
%_kde3_libdir/libkasbar.la
%_kde3_libdir/libkdeinit_appletproxy.la
%_kde3_libdir/libkdeinit_extensionproxy.la
%_kde3_libdir/libkdeinit_kdesktop.la
%_kde3_libdir/libkdeinit_keditbookmarks.la
%_kde3_libdir/libkdeinit_kfmclient.la
%_kde3_libdir/libkdeinit_khotkeys.la
%_kde3_libdir/libkdeinit_kicker.la
%_kde3_libdir/libkdeinit_kjobviewer.la
%_kde3_libdir/libkdeinit_klipper.la
%_kde3_libdir/libkdeinit_konqueror.la
%_kde3_libdir/libkdeinit_ksmserver.la
%_kde3_libdir/libkdeinit_kwin.la
%_kde3_libdir/libkdeinit_kwrite.la
%_kde3_libdir/libkdeinit_kxkb.la
%_kde3_libdir/libkickermain.la
%if %use_kickoff_menu
%_kde3_libdir/libkickoffsearch_interfaces.la
#_kde3_libdir/kde3/kickoffsearch_*
%_kde3_libdir/libkickoffsearch_interfaces.so.*
%endif
%_kde3_libdir/libkonqsidebarplugin.la
%_kde3_libdir/libkonq.la
%_kde3_libdir/libksgrd.la
%_kde3_libdir/libtaskbar.la
%_kde3_libdir/libtaskmanager.la
%_kde3_libdir/libkdeinit_kcontrol.la
%_kde3_libdir/libkdeinit_kcminit.la
%_kde3_libdir/libkdeinit_kprinter.la
%_kde3_libdir/libksplashthemes.so.*
%_kde3_libdir/kde3/kio_*
%_kde3_libdir/libkdeinit_kprinter.so
%_kde3_libdir/libkickermain.so.*
%_kde3_libdir/libkonqsidebarplugin.so.*
%_kde3_libdir/libkonq.so.*
%_kde3_libdir/libksgrd.so.*
%_kde3_libdir/libtaskbar.so.*
%_kde3_libdir/libtaskmanager.so.*
%_kde3_libdir/libkdeinit_khelpcenter.la
%_kde3_libdir/libkdeinit_khelpcenter.so
%_kde3_libdir/libkasbar.so.*
%_kde3_libdir/libkdeinit_appletproxy.so
%_kde3_libdir/libkdeinit_extensionproxy.so
%_kde3_libdir/libkdeinit_kdesktop.so
%_kde3_libdir/libkdeinit_keditbookmarks.so
%_kde3_libdir/libkdeinit_kfmclient.so
%_kde3_libdir/libkdeinit_khotkeys.so
%_kde3_libdir/libkdeinit_kicker.so
%_kde3_libdir/libkdeinit_kjobviewer.so
%_kde3_libdir/libkdeinit_klipper.so
%_kde3_libdir/libkdeinit_konqueror.so
%_kde3_libdir/libkdeinit_ksmserver.so
%_kde3_libdir/libkdeinit_kwin.so
%_kde3_libdir/libkdeinit_kwrite.so
%_kde3_libdir/libkdeinit_kxkb.so
%_kde3_libdir/libkdeinit_kcontrol.so
%_kde3_libdir/libkdeinit_kcminit.so
%_kde3_libdir/libkdeinit_kaccess.so
%_kde3_libdir/libkdecorations.so.*
%_kde3_libdir/libkdecorations.la
%_kde3_libdir/libkdeinit_kaccess.la
%_kde3_libdir/libksplashthemes.la
%_kde3_libdir/libkdeinit_kcontroledit.la
%_kde3_libdir/libkdeinit_kcontroledit.so
%_kde3_libdir/libkdeinit_kwin_rules_dialog.la
%_kde3_libdir/libkdeinit_kwin_rules_dialog.so
%_kde3_libdir/libkfontinst.la
%_kde3_libdir/libkfontinst.so.*
%_kde3_libdir/kde3/khotkeys_arts.la
%_kde3_libdir/kde3/khotkeys_arts.so
%_kde3_libdir/libkhotkeys_shared.la
%_kde3_libdir/libkhotkeys_shared.so.*
%_kde3_libdir/kde3/kcminit_startup.la
%_kde3_libdir/kde3/kcminit_startup.so
%_kde3_libdir/libkdeinit_kcminit_startup.la
%_kde3_libdir/libkdeinit_kcminit_startup.so
%_kde3_libdir/kde3/kded_homedirnotify.la
%_kde3_libdir/kde3/kded_homedirnotify.so
%_kde3_libdir/kde3/kded_medianotifier.la
%_kde3_libdir/kde3/kded_medianotifier.so
%_kde3_libdir/kde3/exrthumbnail.la
%_kde3_libdir/kde3/exrthumbnail.so
%_kde3_libdir/kde3/kded_khotkeys.la
%_kde3_libdir/kde3/kded_khotkeys.so
%_kde3_libdir/kde3/kded_mediamanager.la
%_kde3_libdir/kde3/kded_mediamanager.so
%_kde3_libdir/kde3/kded_remotedirnotify.la
%_kde3_libdir/kde3/kded_remotedirnotify.so
%_kde3_libdir/kde3/kded_systemdirnotify.la
%_kde3_libdir/kde3/kded_systemdirnotify.so
%_kde3_libdir/kde3/kfile_media.la
%_kde3_libdir/kde3/kfile_media.so
%_kde3_libdir/kde3/kfile_trash.la
%_kde3_libdir/kde3/kfile_trash.so
%_kde3_libdir/kde3/kwin3_plastik.la
%_kde3_libdir/kde3/kwin3_plastik.so
%_kde3_libdir/kde3/kwin_plastik_config.la
%_kde3_libdir/kde3/kwin_plastik_config.so
%_kde3_libdir/kde3/libkhtmlkttsdplugin.la
%_kde3_libdir/kde3/libkhtmlkttsdplugin.so
%_kde3_libdir/kde3/media_panelapplet.la
%_kde3_libdir/kde3/media_panelapplet.so
%_kde3_libdir/kde3/trash_panelapplet.la
%_kde3_libdir/kde3/trash_panelapplet.so
%_kde3_libdir/kde3/libkfontviewpart.la
%_kde3_libdir/kde3/libkfontviewpart.so
%_kde3_libdir/kde3/kwin_rules_dialog.la
%_kde3_libdir/kde3/kwin_rules_dialog.so
%_kde3_libdir/kde3/sidebar_panelextension.la
%_kde3_libdir/kde3/sidebar_panelextension.so
%dir %_kde3_libdir/kconf_update_bin/
%_kde3_libdir/kconf_update_bin/khotkeys_update
%_kde3_libdir/kconf_update_bin/kwin_update_window_settings
%_kde3_libdir/kconf_update_bin/kicker-3.4-reverseLayout
%_kde3_libdir/kconf_update_bin/kwin_update_default_rules
%_kde3_libdir/kde3/appletproxy.la
%_kde3_libdir/kde3/appletproxy.so
%_kde3_libdir/kde3/cursorthumbnail.la
%_kde3_libdir/kde3/cursorthumbnail.so
%_kde3_libdir/kde3/djvuthumbnail.la
%_kde3_libdir/kde3/djvuthumbnail.so
%_kde3_libdir/kde3/extensionproxy.la
%_kde3_libdir/kde3/extensionproxy.so
%_kde3_libdir/kde3/kaccess.la
%_kde3_libdir/kde3/kaccess.so
%_kde3_libdir/kde3/kcminit.la
%_kde3_libdir/kde3/kcminit.so
%_kde3_libdir/kde3/kcontrol.la
%_kde3_libdir/kde3/kcontrol.so
%_kde3_libdir/kde3/kded_konqy_preloader.la
%_kde3_libdir/kde3/kded_konqy_preloader.so
%_kde3_libdir/kde3/kdesktop.la
%_kde3_libdir/kde3/kdesktop.so
%_kde3_libdir/kde3/keditbookmarks.la
%_kde3_libdir/kde3/keditbookmarks.so
%_kde3_libdir/kde3/kfmclient.la
%_kde3_libdir/kde3/kfmclient.so
%_kde3_libdir/kde3/khotkeys.la
%_kde3_libdir/kde3/khotkeys.so
%_kde3_libdir/kde3/kicker.la
%_kde3_libdir/kde3/kicker.so
%_kde3_libdir/kde3/kjobviewer.la
%_kde3_libdir/kde3/kjobviewer.so
%_kde3_libdir/kde3/klipper.la
%_kde3_libdir/kde3/klipper.so
%_kde3_libdir/kde3/konqsidebar_web.la
%_kde3_libdir/kde3/konqsidebar_web.so
%_kde3_libdir/kde3/konqueror.la
%_kde3_libdir/kde3/konqueror.so
%_kde3_libdir/kde3/kprinter.la
%_kde3_libdir/kde3/kprinter.so
%_kde3_libdir/kde3/ksmserver.la
%_kde3_libdir/kde3/ksmserver.so
%_kde3_libdir/kde3/ksplashdefault.la
%_kde3_libdir/kde3/ksplashdefault.so
%_kde3_libdir/kde3/ksplashredmond.la
%_kde3_libdir/kde3/ksplashredmond.so
%_kde3_libdir/kde3/ksplashstandard.la
%_kde3_libdir/kde3/ksplashstandard.so
%_kde3_libdir/kde3/kwin.la
%_kde3_libdir/kde3/kwin.so
%_kde3_libdir/kde3/kwin3_default.la
%_kde3_libdir/kde3/kwin3_default.so
%_kde3_libdir/kde3/kwin3_keramik.la
%_kde3_libdir/kde3/kwin3_keramik.so
%_kde3_libdir/kde3/kwin3_laptop.la
%_kde3_libdir/kde3/kwin3_laptop.so
%_kde3_libdir/kde3/kwin3_modernsys.la
%_kde3_libdir/kde3/kwin3_modernsys.so
%_kde3_libdir/kde3/kwin3_redmond.la
%_kde3_libdir/kde3/kwin3_redmond.so
%_kde3_libdir/kde3/kwin3_b2.la
%_kde3_libdir/kde3/kwin3_b2.so
%_kde3_libdir/kde3/kwin3_quartz.la
%_kde3_libdir/kde3/kwin3_quartz.so
%_kde3_libdir/kde3/kwin3_web.la
%_kde3_libdir/kde3/kwin3_web.so
%_kde3_libdir/kde3/kwin_b2_config.la
%_kde3_libdir/kde3/kwin_b2_config.so
%_kde3_libdir/kde3/kwin_quartz_config.la
%_kde3_libdir/kde3/kwin_quartz_config.so
%_kde3_libdir/kde3/kwin_default_config.la
%_kde3_libdir/kde3/kwin_default_config.so
%_kde3_libdir/kde3/kwin_keramik_config.la
%_kde3_libdir/kde3/kwin_keramik_config.so
%_kde3_libdir/kde3/kwin_modernsys_config.la
%_kde3_libdir/kde3/kwin_modernsys_config.so
%_kde3_libdir/kde3/kwrite.la
%_kde3_libdir/kde3/kwrite.so
%_kde3_libdir/kde3/kxkb.la
%_kde3_libdir/kde3/kxkb.so
%_kde3_libdir/kde3/libkfindpart.la
%_kde3_libdir/kde3/libkfindpart.so
%_kde3_libdir/kde3/menu_panelapplet.la
%_kde3_libdir/kde3/menu_panelapplet.so
%_kde3_libdir/kde3/kstyle_keramik_config.la
%_kde3_libdir/kde3/kstyle_keramik_config.so
%_kde3_libdir/kde3/kcm_*
%exclude %_kde3_libdir/kde3/kcm_konsole.*
%exclude %_kde3_libdir/kde3/kcm_nsplugins.*
%exclude %_kde3_libdir/kde3/kcm_randr.*
%_kde3_libdir/kde3/kcontroledit.la
%_kde3_libdir/kde3/kcontroledit.so
%_kde3_libdir/kde3/kded_kwrited.la
%_kde3_libdir/kde3/kded_kwrited.so
%_kde3_libdir/kde3/konq_remoteencoding.la
%_kde3_libdir/kde3/konq_remoteencoding.so
%_kde3_libdir/kde3/konqsidebar_tree.la
%_kde3_libdir/kde3/liblocaldomainurifilter.la
%_kde3_libdir/kde3/liblocaldomainurifilter.so
%_kde3_libdir/kde3/clock_panelapplet.so*
%_kde3_libdir/kde3/dockbar_panelextension.so*
%_kde3_libdir/kde3/htmlthumbnail.so
%_kde3_libdir/kde3/imagethumbnail.so
%_kde3_libdir/kde3/kasbar_panelextension.so*
%_kde3_libdir/kde3/khelpcenter.so
%_kde3_libdir/kde3/klipper_panelapplet.so
%_kde3_libdir/kde3/konq_aboutpage.so
%_kde3_libdir/kde3/konq_iconview.so
%_kde3_libdir/kde3/konq_listview.so
%_kde3_libdir/kde3/konq_shellcmdplugin.so
%_kde3_libdir/kde3/konq_sidebar.so
%_kde3_libdir/kde3/konq_sidebartree_bookmarks.so
%_kde3_libdir/kde3/konq_sidebartree_dirtree.so
%_kde3_libdir/kde3/konq_sidebartree_history.so
%_kde3_libdir/kde3/konqsidebar_tree.so
%_kde3_libdir/kde3/konq_sound.so
%_kde3_libdir/kde3/launcher_panelapplet.so*
%_kde3_libdir/kde3/libkdeprint_part.so
%_kde3_libdir/kde3/libkshorturifilter.so
%_kde3_libdir/kde3/libkuriikwsfilter.so
%_kde3_libdir/kde3/libkurisearchfilter.so
%_kde3_libdir/kde3/lockout_panelapplet.so*
%_kde3_libdir/kde3/minipager_panelapplet.so*
%_kde3_libdir/kde3/naughty_panelapplet.so*
%_kde3_libdir/kde3/run_panelapplet.so*
%_kde3_libdir/kde3/sysguard_panelapplet.so*
%_kde3_libdir/kde3/systemtray_panelapplet.so*
%_kde3_libdir/kde3/taskbar_panelapplet.so*
%_kde3_libdir/kde3/taskbar_panelextension.so*
%_kde3_libdir/kde3/textthumbnail.so
%_kde3_libdir/kde3/kded_favicons.so
%_kde3_libdir/kde3/fontthumbnail.so
%_kde3_libdir/kde3/kfile_font.so
%_kde3_libdir/kde3/libkmanpart.so
%_kde3_libdir/kde3/clock_panelapplet.la
%_kde3_libdir/kde3/dockbar_panelextension.la
%_kde3_libdir/kde3/htmlthumbnail.la
%_kde3_libdir/kde3/imagethumbnail.la
%_kde3_libdir/kde3/kasbar_panelextension.la
%_kde3_libdir/kde3/khelpcenter.la
%_kde3_libdir/kde3/media_propsdlgplugin.la
%_kde3_libdir/kde3/media_propsdlgplugin.so
%_kde3_libdir/kde3/klipper_panelapplet.la
%_kde3_libdir/kde3/konq_aboutpage.la
%_kde3_libdir/kde3/konq_iconview.la
%_kde3_libdir/kde3/konq_listview.la
%_kde3_libdir/kde3/konq_shellcmdplugin.la
%_kde3_libdir/kde3/konq_sidebar.la
%_kde3_libdir/kde3/konq_sidebartree_bookmarks.la
%_kde3_libdir/kde3/konq_sidebartree_dirtree.la
%_kde3_libdir/kde3/konq_sidebartree_history.la
%_kde3_libdir/kde3/konq_sound.la
%_kde3_libdir/kde3/launcher_panelapplet.la
%_kde3_libdir/kde3/libkdeprint_part.la
%_kde3_libdir/kde3/libkshorturifilter.la
%_kde3_libdir/kde3/libkuriikwsfilter.la
%_kde3_libdir/kde3/libkurisearchfilter.la
%_kde3_libdir/kde3/lockout_panelapplet.la
%_kde3_libdir/kde3/minipager_panelapplet.la
%_kde3_libdir/kde3/naughty_panelapplet.la
%_kde3_libdir/kde3/run_panelapplet.la
%_kde3_libdir/kde3/sysguard_panelapplet.la
%_kde3_libdir/kde3/systemtray_panelapplet.la
%_kde3_libdir/kde3/taskbar_panelapplet.la
%_kde3_libdir/kde3/taskbar_panelextension.la
%_kde3_libdir/kde3/textthumbnail.la
%_kde3_libdir/kde3/kded_favicons.la
%_kde3_libdir/kde3/fontthumbnail.la
%_kde3_libdir/kde3/kfile_font.la
%_kde3_libdir/kde3/libkmanpart.la
%_kde3_libdir/kde3/kickermenu_*
%exclude %_kde3_libdir/kde3/kickermenu_konsole.*
%exclude %_kde3_libdir/kde3/kickermenu_kate.*

#-----------------------------------------------------------------------------

%package common
Group:          Graphical desktop/KDE3
Summary:        Config file and icons file for %name
Requires(pre):  %lib_name = %{epoch}:%{version}-%{release}
Conflicts:	    kdemoreartwork-plastik <= 0.3.3-1mdk
Conflicts:      kdebase <= 3.2.3-97mdk
Conflicts:		kdeedu <= 1:3.2.3
Conflicts:		mandriva-theme <= 1.0.6
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes:      kdebase-kcontrol-data < 1:3.5.9
Provides:       %oname-common = %{epoch}:%{version}-%{release}
Provides:       %rname-common = %{epoch}:%{version}-%{release}
Obsoletes:      %rname-common
Obsoletes:      %oname-common

%description common
This packages contains all icons, config file etc...

%files common
%defattr(-,root,root)
%_sysconfdir/xdg/kde
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-kde3-hicolor.*
%{_var}/lib/rpm/filetriggers/gtk-icon-cache-kde3-crystalsvg.*
%config(noreplace) /etc/pam.d/kde3
%config(noreplace) /etc/pam.d/kscreensaver3
%config(noreplace) /etc/pam.d/kde3-np
%config(noreplace) %_kde3_configdir/kdesktop_custom_menu1
%config(noreplace) %_kde3_configdir/kdesktop_custom_menu2
%config(noreplace) %_kde3_configdir/klipperrc
%config(noreplace) %_kde3_configdir/konqsidebartng.rc
%config(noreplace) %_kde3_configdir/kshorturifilterrc
%config(noreplace) %_kde3_configdir/kxkb_groups
%config(noreplace) %_kde3_datadir/fonts/override/fonts.dir
%_kde3_bindir/kxdglauncher
%_kde3_bindir/kasbar
%_kde3_bindir/kbookmarkmerger
%_kde3_bindir/kcheckrunning
%_kde3_bindir/khc_docbookdig.pl
%_kde3_bindir/khc_htdig.pl
%_kde3_bindir/khc_htsearch.pl
%_kde3_bindir/khc_mansearch.pl
%_kde3_bindir/khc_beagle_index.pl
%_kde3_bindir/khc_beagle_search.pl
%_kde3_bindir/kio_media_mounthelper
%_kde3_bindir/knetattach
%_kde3_bindir/kompmgr
%_kde3_bindir/ksplashsimple
%_kde3_bindir/ktrash
%_kde3_appsdir/khtml/kpartplugins/*.desktop
%_kde3_appsdir/khtml/kpartplugins/*.rc
%dir %_kde3_docdir/HTML/
%dir %_kde3_docdir/HTML/en/
%dir %_kde3_datadir/desktop-directories/
%_kde3_datadir/desktop-directories/*.directory
%doc %_kde3_docdir/HTML/en/kcontrol
# Exclude just the ones that not belongs here
%exclude %_kde3_docdir/HTML/en/kcontrol/kcmkonsole
%doc %_kde3_docdir/HTML/en/kdebugdialog
%doc %_kde3_docdir/HTML/en/kdcop
%doc %_kde3_docdir/HTML/en/kdesu
%doc %_kde3_docdir/HTML/en/kdm
%doc %_kde3_docdir/HTML/en/kfind
%doc %_kde3_docdir/HTML/en/ksplashml
%doc %_kde3_docdir/HTML/en/kxkb
%doc %_kde3_docdir/HTML/en/khelpcenter
%doc %_kde3_docdir/HTML/en/kdeprint
%doc %_kde3_docdir/HTML/en/kicker
%doc %_kde3_docdir/HTML/en/knetattach
%doc %_kde3_docdir/HTML/en/kioslave
%doc %_kde3_docdir/HTML/en/klipper
%doc %_kde3_docdir/HTML/en/konqueror
%doc %_kde3_docdir/HTML/en/kpager
%doc %_kde3_docdir/HTML/en/kwrite
%doc %_kde3_docdir/HTML/en/kompmgr
%doc %_kde3_docdir/HTML/en/kinfocenter
%dir %_kde3_appsdir/kinfocenter/
%_kde3_appsdir/kinfocenter/kinfocenterui.rc
%_kde3_datadir/applnk/.hidden/*.desktop
%exclude %_kde3_datadir/applnk/.hidden/randr.desktop
%_kde3_datadir/applnk/.hidden/.directory
%_kde3_datadir/applnk/*.desktop
%dir %_kde3_datadir/applnk/Internet/
%_kde3_datadir/applnk/Internet/*.desktop
%dir %_kde3_datadir/applnk/Settings/LookNFeel/
%dir %_kde3_datadir/applnk/Settings/LookNFeel/Themes/
%_kde3_datadir/applnk/Settings/LookNFeel/Themes/*.desktop
%_kde3_datadir/applnk/Settings/LookNFeel/*.desktop
%dir %_kde3_datadir/applnk/Settings/WebBrowsing/
%_kde3_datadir/applnk/Settings/WebBrowsing/*.desktop
%exclude %_kde3_datadir/applnk/Settings/WebBrowsing/nsplugin.desktop
%_kde3_datadir/applnk/System/ScreenSavers/*.desktop
%_kde3_datadir/applnk/System/*.desktop
%dir %_kde3_datadir/applnk/Toys/
%_kde3_datadir/applnk/Toys/*.desktop
%dir %_kde3_datadir/applnk/Utilities/
%_kde3_datadir/applnk/Utilities/*.desktop
%dir %_kde3_configdir.kcfg/
%_kde3_configdir.kcfg/*.kcfg
%dir %_kde3_appsdir/
%dir %_kde3_appsdir/clockapplet/
%_kde3_appsdir/clockapplet/*
%dir %_kde3_appsdir/kthememanager/themes/
%_kde3_appsdir/kthememanager/themes/*
%dir %_kde3_appsdir/kcontroledit/
%_kde3_appsdir/kcontroledit/*
%dir %_kde3_appsdir/drkonqi/
%_kde3_appsdir/drkonqi/*
%doc %_kde3_docdir/HTML/en/kappfinder/man-kappfinder.1.docbook
%dir %_kde3_appsdir/kappfinder/
%_kde3_appsdir/kappfinder/*
%exclude %_kde3_appsdir/kappfinder/apps/Games/Roguelikes/*.desktop
%exclude %_kde3_appsdir/kappfinder/apps/Games/Arcade/*.desktop
%dir %_kde3_appsdir/kbookmark/
%_kde3_appsdir/kbookmark/*
%dir %_kde3_appsdir/kcmcss/
%_kde3_appsdir/kcmcss/*
%dir %_kde3_appsdir/kcminput/
%_kde3_appsdir/kcminput/*
%dir %_kde3_appsdir/kcmkeys
%_kde3_appsdir/kcmkeys/*
%dir %_kde3_appsdir/kcmlocale/
%_kde3_appsdir/kcmlocale/*
%dir %_kde3_appsdir/khotkeys/
%_kde3_appsdir/khotkeys/*
%dir %_kde3_appsdir/kcontrol/
%_kde3_appsdir/kcontrol/*
%dir %_kde3_appsdir/kconf_update/
%_kde3_appsdir/kconf_update/*.upd
%_kde3_appsdir/kconf_update/*.pl
%_kde3_appsdir/kconf_update/*.sh
%dir %_kde3_appsdir/kcm_componentchooser
%_kde3_appsdir/kcm_componentchooser/*
%dir %_kde3_appsdir/kdcop
%_kde3_appsdir/kdcop/*
%dir %_kde3_appsdir/kdeprint_part
%_kde3_appsdir/kdeprint_part/*
%dir %_kde3_appsdir/kdeprint
%_kde3_appsdir/kdeprint/*
%dir %_kde3_appsdir/kdesktop
%_kde3_appsdir/kdesktop/*
%dir %_kde3_appsdir/kdewizard
%_kde3_appsdir/kdewizard/*
%dir %_kde3_appsdir/kdisplay
%_kde3_appsdir/kdisplay/*
%dir %_kde3_appsdir/keditbookmarks/
%_kde3_appsdir/keditbookmarks/*
%dir %_kde3_appsdir/kfindpart/
%_kde3_appsdir/kfindpart/*
%dir %_kde3_appsdir/khelpcenter/
%_kde3_appsdir/khelpcenter/*
%dir %_kde3_appsdir/kicker
%_kde3_appsdir/kicker/*
%dir %_kde3_appsdir/kio_finger/
%_kde3_appsdir/kio_finger/*
%dir %_kde3_appsdir/kio_info/
%_kde3_appsdir/kio_info/*
%dir %_kde3_appsdir/kjobviewer/
%_kde3_appsdir/kjobviewer/*
%dir %_kde3_appsdir/konqiconview/
%_kde3_appsdir/konqiconview/*
%dir %_kde3_appsdir/konqlistview/
%_kde3_appsdir/konqlistview/*
%dir %_kde3_appsdir/konqsidebartng/
%_kde3_appsdir/konqsidebartng/*
%dir %_kde3_appsdir/konqueror/
%_kde3_appsdir/konqueror/*
%dir %_kde3_appsdir/kpersonalizer
%_kde3_appsdir/kpersonalizer/*
%dir %_kde3_appsdir/ksplash/
%_kde3_appsdir/ksplash/*
%dir %_kde3_appsdir/kwin/
%_kde3_appsdir/kwin/*
%dir %_kde3_appsdir/kwrite/
%_kde3_appsdir/kwrite/*
%dir %_kde3_appsdir/kaccess
%_kde3_appsdir/kaccess/*
%_kde3_appsdir/kio_man/kio_man.css
%dir %_kde3_appsdir/ksmserver
%_kde3_appsdir/ksmserver/*
%dir %_kde3_appsdir/naughtyapplet/
%_kde3_appsdir/naughtyapplet/*
%dir %_kde3_datadir/autostart/
%_kde3_datadir/autostart/*
%_kde3_iconsdir/*/*/actions/*
%_kde3_iconsdir/*/*/apps/*
%_kde3_iconsdir/*/*/devices/*
%_kde3_datadir/locale/en_US
%_kde3_datadir/locale/l10n/*
%_kde3_datadir/applications/kde/*.desktop
%exclude %_kde3_datadir/applications/kde/kate.desktop
%exclude %_kde3_datadir/applications/kde/kdeprintfax.desktop
%exclude %_kde3_datadir/applications/kde/kmenuedit.desktop
%exclude %_kde3_datadir/applications/kde/konsole.desktop
%exclude %_kde3_datadir/applications/kde/ksysguard.desktop
%exclude %_kde3_datadir/applications/kde/krandrtray.desktop
%dir %_kde3_appsdir/kcmusb
%_kde3_appsdir/kcmusb/*
%dir %_kde3_appsdir/systemview
%_kde3_appsdir/systemview/*
%dir %_kde3_datadir/mimelnk/
%dir %_kde3_datadir/mimelnk/application
%_kde3_datadir/mimelnk/application/*
%dir %_kde3_datadir/mimelnk/media
%_kde3_datadir/mimelnk/media/*
%dir %_kde3_datadir/mimelnk/print/
%_kde3_datadir/mimelnk/print/*
%dir %_kde3_datadir/mimelnk/fonts/
%_kde3_datadir/mimelnk/fonts/*
%dir %_kde3_datadir/mimelnk/inode/
%_kde3_datadir/mimelnk/inode/system_directory.desktop
%dir %_kde3_datadir/services
%_kde3_datadir/services/*
%dir %_kde3_datadir/servicetypes/
%_kde3_datadir/servicetypes/*
%dir %_kde3_datadir/sounds/
%_kde3_datadir/sounds/*
%dir %_kde3_datadir/templates/
%_kde3_datadir/templates/*
%_kde3_datadir/templates/.source
%dir %_kde3_datadir/wallpapers/
%_kde3_datadir/wallpapers/*
%dir %_kde3_appsdir/kcmview1394/
%_kde3_appsdir/kcmview1394/oui.db
# Don't autostart ktip
%exclude %_kde3_datadir/autostart/ktip.desktop
# Not on desktop
%exclude %_kde3_appsdir/kdesktop/DesktopLinks/System.desktop
# Disable superuser modes
%exclude %_kde3_datadir/applications/kde/konsolesu.desktop
%exclude %_kde3_datadir/applications/kde/konquerorsu.desktop
# Disable internal krandrtray. Using new 1.2 based by Boiko
%exclude %_kde3_datadir/applications/kde/krandrtray.desktop
%exclude %_kde3_bindir/krandrtray

#-----------------------------------------------------------------------------

%package -n %lib_name-devel
Summary:    Devel stuff for kdebase
Group:	    Development/KDE and Qt
Obsoletes:  %lib_name-kate-devel < 1:3.5.9
Obsoletes:  kdebase3-devel < 1:3.5.9
Requires:   kdelibs3-devel >= %{epoch_kdelibs}:3.5.3
Requires:   %lib_name = %{epoch}:%{version}-%{release} 
Requires:   %lib_name-kate = %{epoch}:%{version}-%{release} 
Provides:   kdebase-devel = %{epoch}:%{version}-%{release}
Provides:   kdebase3-devel = %{epoch}:%{version}-%{release}
Provides:   %lib_name_fixed-devel
Conflicts:  kdebase <= 3.1.94-13mdk

%description  -n %lib_name-devel
This package contains header files needed if you wish to build applications
based on kdebase.

%files -n %lib_name-devel
%defattr(-,root,root)
%_kde3_includedir/*
%_kde3_libdir/libkateinterfaces.so
%_kde3_libdir/libkateutils.so
%_kde3_libdir/libkickermain.so
%if %use_kickoff_menu
%_kde3_libdir/libkickoffsearch_interfaces.so
%endif
%_kde3_libdir/libkonqsidebarplugin.so
%_kde3_libdir/libkonq.so
%_kde3_libdir/libksgrd.so
%_kde3_libdir/libtaskbar.so
%_kde3_libdir/libtaskmanager.so
%_kde3_libdir/libkdecorations.so
%_kde3_libdir/libksplashthemes.so
%_kde3_libdir/libkhotkeys_shared.so
%_kde3_libdir/libkfontinst.so
%_kde3_libdir/libkasbar.so

#-----------------------------------------------------------------------------

%if %compile_apidox

%package devel-doc
Group:Development/KDE and Qt
Summary: Development documentation for %name
Requires: kdelibs-devel-doc
BuildRequires: doxygen 
BuildRequires: graphviz
BuildRequires: kdelibs-devel-doc

%description devel-doc
This packages contains all development documentation for kdelibs

%files devel-doc
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/kdebase-apidocs

%endif

#-----------------------------------------------------------------------------

%package nsplugins
Summary:	Netscape Plugins for kdebase
Group:		Graphical desktop/KDE3
Requires:	%name-progs = %{epoch}:%{version}-%{release}
Obsoletes:     kdebase3-nsplugins < 1:3.5.9
Provides:      kdebase3-nsplugins = %{epoch}:%{version}-%{release}
Obsoletes: kdebase-kcontrol-nsplugins < 1:3.5.9
Provides:       %oname-nsplugins = %{epoch}:%{version}-%{release}
Obsoletes: %oname-nsplugins
Obsoletes: %rname-nsplugins

%description nsplugins
This package contains the Netscape plugins for konqueror files.

%files nsplugins
%defattr(-,root,root)
%_kde3_bindir/nspluginscan
%_kde3_bindir/nspluginviewer
%_kde3_datadir/applnk/Settings/WebBrowsing/nsplugin.desktop
%_kde3_appsdir/plugin/nspluginpart.rc
%_kde3_libdir/kde3/libnsplugin.*
%_kde3_libdir/kde3/kcm_nsplugins.*

#-----------------------------------------------------------------------------

%package session-plugins
Summary:    Session plugins for kdesktop/kdm
Group:      Graphical desktop/KDE3
%define release_min_mkrel_kdebase %mkrel 4
Conflicts:     %lib_name  <= %epoch:3.5.5-%release_min_mkrel_kdebase
Provides:       %oname-session-plugins = %{epoch}:%{version}-%{release}
Provides:       %rname-session-plugins = %{epoch}:%{version}-%{release}
Obsoletes: %oname-session-plugins
Obsoletes: %rname-session-plugins

%description session-plugins
This package contains sessions plugins for kdesktop kdm.
It allows to login into with kdm and lock/unlock kdesktop screensaver.


%files session-plugins
%defattr(-,root,root)
%_kde3_libdir/kde3/kgreet_winbind.la
%_kde3_libdir/kde3/kgreet_winbind.so
%_kde3_libdir/kde3/kgreet_classic.la
%_kde3_libdir/kde3/kgreet_classic.so
%_kde3_libdir/kde3/kgreet_pam.la
%_kde3_libdir/kde3/kgreet_pam.so


#-----------------------------------------------------------------------------

%package kdm
Summary: kdm for kdebase
Group: Graphical desktop/KDE3
Requires: kdm-config-file
Provides: kdm3 = %{epoch}:%{version}-%{release}
Provides: kde3-kdm = %{epoch}:%{version}-%{release}
Provides: dm
Requires: xinitrc
Requires: %name-session-plugins
Requires: %name-common
Obsoletes: kdebase-kdm-config-file <= %epoch:%version-%release
%define release_min_mkrel %mkrel 10
Provides:  %oname-kdm = %{epoch}:%{version}-%{release}
Provides:  %rname-kdm = %{epoch}:%{version}-%{release}
Obsoletes: %oname-kdm
Obsoletes: %rname-kdm

%description kdm
This package contains kdm.

%post kdm
%make_session

%files kdm
%defattr(-,root,root)
%_kde3_bindir/kdm
%_kde3_bindir/kdmctl
%_kde3_bindir/kdm_config
%_kde3_bindir/kdm_greet
%_kde3_bindir/krootimage
%_kde3_bindir/genkdmconf
%dir %_kde3_appsdir/kdm
%_kde3_appsdir/kdm/*
%dir %_kde3_docdir/kdm/
%_kde3_docdir/kdm/README
%_kde3_configdir/kdm/README
%{_sysconfdir}/logrotate.d/kdm3
%exclude %_kde3_appsdir/kdm/sessions/
%exclude %_kde3_configdir/kdm/X*
%exclude %_kde3_configdir/kdm/kdmrc
%exclude %_kde3_configdir/kdm/backgroundrc

#-----------------------------------------------------------------------------

%package kmenuedit
Summary: kmenuedit 
Group: Graphical desktop/KDE3
Obsoletes: %lib_name-kmenuedit < 1:3.5.9
Conflicts: %name-common <= 1:3.5.8 
Provides: kmenuedit3 = %{epoch}:%{version}-%{release}
Provides: kde3-kmenuedit = %{epoch}:%{version}-%{release}
Provides:  %oname-kmenuedit = %{epoch}:%{version}-%{release}
Provides:  %rname-kmenuedit = %{epoch}:%{version}-%{release}
Obsoletes: %oname-kmenuedit
Obsoletes: %rname-kmenuedit

%description kmenuedit
Kmenuedit for kdebase

%files kmenuedit
%defattr(-,root,root)
%_kde3_bindir/kmenuedit
%doc %_kde3_docdir/HTML/en/kmenuedit
%dir %_kde3_appsdir/kmenuedit/
%_kde3_appsdir/kmenuedit/*
%_kde3_datadir/applications/kde/kmenuedit.desktop
%_kde3_libdir/kde3/kmenuedit.*
%_kde3_libdir/libkdeinit_kmenuedit.*

#-----------------------------------------------------------------------------

%prep
%setup -q -a 1 -n %oname-%version

%patch1 -p1 -b .screensaver_pam
%patch2 -p1 -b .fix_media_fuser_path
%patch3 -p1 -b .fix_screensaver
%patch4 -p0 -b .fix_vibrate_dialog
%patch7 -p1 -b .fix_kdm_theme
%patch8 -p1 -b .fix_kdm_server_args
%patch9 -p1 -b .fix_logout_without_confirmation
# Categories not apply anymore
%patch20 -p1 -b .drakclock
%patch21 -p1 -b .lzma_support
%patch22 -p1 -b .fix_gtk_style
%patch24 -p1 -b .kdesktop_firstrun
%patch26 -p1 -b .translation_kdm
%patch27 -p1 -b .fix_firstboot
%patch28 -p1 -b .khelpcenter_htsearch_path
%patch35 -p0 -b .add_switch_icons
%patch37 -p0 -b .fix_showOnly_screensaver
%patch39 -p1 -b .kcontrol_menu_entry
%patch41 -p0
%patch42 -p1 -b .bookmark_copy
%patch43 -p0 -b .update_usb.ids
%patch44 -p0
%patch60 -p1
#########################################
#Begin patch with Pardus patches
%patch104 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p0
##########################################
#%if %mdkversion > 201000
%patch120 -p1
#%endif
%patch130 -p0
%patch131 -p1
%patch132 -p0
%patch133 -p0
%patch134 -p1
%patch135 -p0

%if %use_kickoff_menu
# kickoff data
tar xfj %SOURCE100
%endif

%build
%define _disable_ld_no_undefined 1

#
#cp configure configure.orig
#rm -f configure
#cp %SOURCE200 configure

export QTDIR=%qt3dir
export KDEDIR=%{_kde3_prefix}
#export CFLAGS="$CFLAGS -DPIC -fPIC"
#export CXXFLAGS="$CXXFLAGS -DPIC -fPIC"
export CXXFLAGS="$CXXFLAGS -I/usr/lib/qt3/include/ "

%if %use_kickoff_menu
export CXXFLAGS="$CXXFLAGS -DKDELIBS_SUSE -I/usr/include/libbeagle "
export CFLAGS="$CFLAGS -DKDELIBS_SUSE -I/usr/include/libbeagle "
%endif

export xdg_menudir=%_sysconfdir/xdg/kde/menus
make -f admin/Makefile.common cvs

PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/

%configure_kde3 \
   --with-pam=kde3 \
   --with-kss-pam=kscreensaver3 \
   --with-cdparanoia \
   --without-lame \
   --with-vorbis \
   --with-qt-libraries=%qt3lib \
%if %support_ldap			
   --with-ldap \
%else
   --without-ldap \
%endif			
  --with-hal \
  --with-extra-includes=/usr/include/avahi-compat-libdns_sd/:/opt/kde3/include/tqt \
  --with-extra-libs=/opt/kde3/lib

%if %use_kickoff_menu
# We need create kicker config settings before 
# due still using auto* things, otherwise compilation breaks
pushd kicker/kicker/core
    make extensionSettings.h
popd
#pushd kicker/kicker/ui
#    make kmenubase.h
#popd
%endif

%make

%if %compile_apidox
   make apidox
%endif

%install
rm -fr %buildroot

export RUN_KAPPFINDER=no
export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
make DESTDIR=%buildroot install

# Install kde pam configuration file
install -d -m 0755 %buildroot%_sysconfdir/pam.d/
install -m 0644 %SOURCE4 %buildroot%_sysconfdir/pam.d/kde3
install -m 0644 %SOURCE5 %buildroot%_sysconfdir/pam.d/kde3-np

# Install kscreensaver pam configuration file
install -m 0644 kscreensaver.pamd %buildroot%_sysconfdir/pam.d/kscreensaver3

# Keep KDM migration
install -m 0644 %SOURCE2 %buildroot/%_kde3_bindir/

# Add chksession support
# David - 3.0-0.beta1.8mdk - We don't use the _sysconfdir macro here because
#                            this file need to be installed in /etc/ and not
#                            in /opt/kde3/etc/ (or KDE 3 will not be displayed
#                            in KDM/GDM.
#                            We will also need to rename 11KDE in 01KDE when
#                            KDE 3 will be used as default KDE.
install -d -m 0775 %buildroot/%{_sysconfdir}/X11/wmsession.d/
cat << EOF > %buildroot/%{_sysconfdir}/X11/wmsession.d/01KDE3
NAME=KDE
ICON=kde-wmsession.xpm
DESC=The K Desktop Environment
EXEC=%_kde3_bindir/startkde
SCRIPT:
exec %_kde3_bindir/startkde
EOF


# David - 2.1-0.20010210.1mdk - Change kdesud owners and permission (per request
#                               of binary)
# David - 2.1-1mdk - It seems that Coolo made some modifications in Makefile to
#                    set that automatically in KDE post 2.1. To check in next
#                    CVS code update
chmod 2755 %buildroot/%_kde3_bindir/kdesud
chmod 4755 %buildroot/%_kde3_bindir/kcheckpass 

# Link KDM images directory to faces directory
rm -fr %buildroot/%_kde3_appsdir/kdm/pics/users/
pushd  %buildroot/%_kde3_appsdir/kdm/pics
	ln -s %{_datadir}/mdk/faces users
popd

# Remove KDE hat...
rm -f %buildroot/%_kde3_appsdir/kdewizard/pics/wizard_small.png
# ...and install a safe image
install -m 0644 %SOURCE8 %buildroot/%_kde3_appsdir/kdewizard/pics/wizard_small.png

# David - 2.2.0.beta1.3mdk - Remove a potential problem with Apple
rm -f %buildroot/%_kde3_datadir/wallpapers/default_blue.jpg

install -d %buildroot/%_kde3_appsdir/kdesktop/Desktop

# David - 2.2.2-77mdk - The QtCUPS and KUPS packages are taken from the distro,
#                       because QtCUPS got integrated into KDE and is "kprinter"
#                       now and KUPS is the KDE Printing Manager now (KDE
#                       Control Center, "System"/"Printing Manager". The tools
#                       are generalized to aso work with LPD or LPRng. To help
#                       the old-fashioned users who always type "kups" and
#                       "qtcups" at the command prompt
(
cd %buildroot/%_kde3_bindir
ln -s kprinter qtcups
ln -s kprinter lpr-kprinter
)

# Console font to fontconfig
install -d -m 0755 %buildroot/%_sysconfdir/fonts/conf.d
install -m 0644 %SOURCE9 %buildroot/%_sysconfdir/fonts/conf.d/99-konsole.conf

# Mandriva startkde
#install -m 0755 %SOURCE3 %buildroot/%_kde3_bindir/startkde

# logrotate
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cat << EOF > %{buildroot}%{_sysconfdir}/logrotate.d/kdm3
/var/log/kdm3.log {
    weekly
    notifempty
    missingok
    nocompress
}
EOF

install -m 0755 %SOURCE10 %buildroot/%_kde3_bindir/kdeeject

install -m 0755 %SOURCE11 %buildroot/%_kde3_datadir/autostart/
install -m 0755 %SOURCE12 %buildroot/%_kde3_datadir/autostart/
install -m 0755 %SOURCE13 %buildroot/%_kde3_datadir/autostart/
install -m 0755 %SOURCE14 %buildroot/%_kde3_datadir/applnk/.hidden/
install -m 0755 %SOURCE15 %buildroot/%_kde3_datadir/mimelnk/application/
install -m 0755 %SOURCE16 %buildroot/%_kde3_datadir/mimelnk/application/

# automatic gtk icon cache update on rpm installs/removals
# (see http://wiki.mandriva.com/en/Rpm_filetriggers)
install -d %buildroot%{_var}/lib/rpm/filetriggers
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-kde3-hicolor.filter << EOF
^./opt/kde3/share/icons/hicolor/
EOF
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-kde3-hicolor.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /opt/kde3/share/icons/hicolor
fi
EOF
chmod 755 %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-kde3-hicolor.script

cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-kde3-crystalsvg.filter << EOF
^./opt/kde3/share/icons/crystalsvg/
EOF
cat > %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-kde3-crystalsvg.script << EOF
#!/bin/sh
if [ -x /usr/bin/gtk-update-icon-cache ]; then 
  /usr/bin/gtk-update-icon-cache --force --quiet /opt/kde3/share/icons/crystalsvg
fi
EOF
chmod 755 %buildroot%{_var}/lib/rpm/filetriggers/gtk-icon-cache-kde3-crystalsvg.script

desktop-file-install \
  --add-category="System" \
  --add-only-show-in="KDE" \
  --dir %buildroot%_kde3_datadir/applications/kde \
  --add-only-show-in="KDE" \
	%buildroot%_kde3_datadir/applications/kde/KControl.desktop

#Fix xdg dir
#mkdir %buildroot/etc/xdg/kde
#mv %buildroot/etc/xdg/menus %buildroot/etc/xdg/kde

%clean
rm -fr %buildroot



%changelog
* Wed Jul 27 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-6mvt2010.2
+ Fix kcontrol meni patch mysteriously missing from last build. Trying again...
+ Fix problem with kdebase-3.5.12-kdm-kcontrol-usericon.patch

* Tue Jul 26 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-5mvt2010.2
+ Add kdebase-3.5.12-kdm-kcontrol-usericon.patch

* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-4mvt2010.2
+ Add kdebase-3.5.12-fix-kcontrol-menu.patch

* Mon Jul 18 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-3mvt2010.2
+ Add kdebase-post-3.5.12-fix-choose-webbrowser-kcontrol.patch
+ Add kdebase-3.5.12-move-xdg-menu-dir.patch
+ Add kdebase-3.5.12-startkde.patch

* Mon Jul 18 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-2mvt2010.2
+ Fix xdg dirs

* Fri Feb 2 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-1mvt2010.2
+ Rebuild for MDV 2010.2 and Trinity 3.5.12
+ Fix the following patches for compatibility with code changes:
  kdebase-3.5.3-fix-media-fuser.patch
  kdebase-3.4.0-fix-scrnsaver.patch
  kdebase-3.5.10-fix-vibrate-dialog.patch
  kdebase-3.3.2-fix-kdm-theme-mdk.patch
  kdebase-3.5.7-clock-drakclock.patch
  kdebase-3.5.4-fix-gtk-style.patch
  kdebase-3.5.7-kdesktop_firstrun.patch
  kdebase-3.5.7-khelpcenter-htdigsearch-path.patch
  kdebase-3.5.8-kmenu_tooltip_support.patch
  detect-media-types.patch
  mediamanager-mount-point-utf8.diff
  turkish-preview.patch
+ Comment out for later removal if not needed
  kdebase-3.5.10-fix-build.patch
  kdebase-3.5.10-fix-build-beagle.patch
  kdm-utf8-password.patch
  kio_media_i18n.patch
  kate_desktop_file.patch
  select-wm-gui.diff
- Remove the following patches which don't work, aren't needed or are now in the core:
  kdebase-3.5.6-rubberband.patch
  kdebase-3.5.4-rubberband-kcmstyle.patch
  kdebase-3.5.10-konqsidebar-restrictions.patch
  kdebase-post-3.5.10-kickoff-kicker.patch
  kdebase-post-3.5.8-kickoff-kcontrol.patch
  kdebase-post-3.5.10-kickoff-mandriva.patch
  kdebase-3.5.8-new_kside_top_layout.patch
  kdebase-post-3.5.9-kickoff-button.patch
  kdebase-3.5.6-kicker-kmenu.patch
  kdebase-3.5.6-kicker-top.patch
  kdebase-3.5.8-menu_icon_switch.patch
  suspend-unmount.diff
  kdebase-3.5.7-xdg-user-dirs-dirpath.patch
  kdebase-3.5.10-ksmserver-timed.patch
  kdebase-3.5.7-handle_fstab_unomunt.patch
  kdebase-3.5.8-kdm-suspend.patch
  kdebase-3.5.10-ksmserver-suspend.patch
  kdebase-3.5.8-theme-selector.patch
  kdebase-kdm-makeitcool.patch
  kdebase-kdm-consolekit.patch
  kdebase-3.5.8-kmenu_tooltip_support.patch
  kcontrol-energy.diff
  kdebase-3.5.9-kdesktop-crossfade.patch
  kdebase-3.5.9-kdm-kcontrol-usericon.patch
  kdebase-post-3.5.9-bookmark-global-copy.patch
  kdebase-post-3.5.9-kbackground-xml-selector.patch
  kdebase-3.5.9-kdesktop-resize-bug.patch
  kdebase-post-3.5.9-kickoff-shadow-zoom.patch
  kdebase-3.5.9-kdesktop-bg-nullImage.patch
  kdebase-3.5.9-kdesktop-desktop_change-bug.patch
  kdebase-3.5.10-gcc4.patch
  kdebase-post-3.5.10-rev863267.patch
  kdebase-post-3.5.10-rev864963.patch
  add-polkit-support-to-halbackend.patch
  change-monetary-symbol-to-TL.patch
  kdebase-3.5.10-nspluginloader-fix-load-plugins-on-demand.patch
  konsole_url_handling.patch
  fix_autotools.patch
  systray_order.diff

* Fri Jul 16 2010 Tim Williams <tim@my-place.org.uk> 1:3.5.10-34mvt2010.1
- Removed kdebase-3.5.10-xdg-dirs-set-paths.patch, this was causing a build failure

* Wed May 05 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-33mvt2010.1
+ Rebuild for 2010.1
+ Add fix_openssl.patch to fix compilation with new openssl package

* Wed Mar 24 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-32mvt2010.0
+ Add Kwin patch (patch 118) to provide kde4-kwin and compiz wm support
+ Add systray order patch

* Thu Feb 18 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-31mvt2010.0
+ Make default config dir as $HOME/.kde3 to avoid future conflicts with KDE4
+ Fix KControl doesn't show up in menu issue

* Sun Jan 17 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-30mvt2010.0
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65

* Sat Jan 16 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-29mvt2010.0
+ Fix kdm won't provide dm issue

* Fri Jan 08 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-28mvt2010.0
+ Add missing gurpmi and x-urpmi desktop files
+ Use automake 1.11 and above
+ KDE won't built with autoconf 2.64, fix spec file to 2.63
+ Add fancy application start animations
+ Patch kate.desktop so, multiple files could be opened in one kate session.

* Thu Dec 31 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-27mvt2010.0
+ Add xdg-user-dirs implemention to kickoff menu style

* Tue Dec 22 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-26mvt2010.0
+ Add Pardus patches to imporve usability and fix kio slave issues
 - detect-media-types.patch
 - add-polkit-support-to-halbackend.patch
 - change-monetary-symbol-to-TL.patch
 - kdebase-3.5.10-nspluginloader-fix-load-plugins-on-demand.patch
 - kdm-utf8-password.patch
 - kio_media_i18n.patch
 - konsole_url_handling.patch
 - mediamanager-mount-point-utf8.diff
 - media_saferemove.patch
 - turkish-preview.patch

* Sun Nov 22 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-25mvt2010.0
+ Fixed libname to avoid unwanted KDE4 upgrade
+ added fix_detect_media_types patch

* Fri Nov 13 2009 Tim Williams <tim@my-place.org.uk> 1:3.5.10-24mdv2010.0
+ Rebuild for MDV 2010.0
+ kdebase-3.5.10-gcc4.patch

* Thu Apr 23 2009 Frederic Crozat <fcrozat@mandriva.com> 1:3.5.10-23mdv2009.1
+ Revision: 368909
- Don't build devel doc
- Move session file to progs subpackage to fix filetrigger

* Sat Mar 28 2009 Anssi Hannula <anssi@mandriva.org> 1:3.5.10-22mdv2009.1
+ Revision: 361977
- add more conflicts with old packages

* Fri Mar 27 2009 Anssi Hannula <anssi@mandriva.org> 1:3.5.10-21mdv2009.1
+ Revision: 361676
- rebuild for missing packages on x86_64

* Mon Mar 23 2009 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-20mdv2009.1
+ Revision: 360568
- Add back provide

* Sun Mar 22 2009 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-19mdv2009.1
+ Revision: 360323
- More conflicts fixes

* Sun Mar 22 2009 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-18mdv2009.1
+ Revision: 360320
- Fix conflicts

  + Herton Ronaldo Krzesinski <herton@mandriva.com.br>
    - Don't provide and conflict same range of kdebase-ksysguard version,
      remove Provides.
    - Remove redundant Conflict for kdebase-ksysguard, keep the one with
      greater epoch:version-release.
    - Revert previous change for kdebase-ksysguard update error.

* Fri Mar 20 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:3.5.10-16mdv2009.1
+ Revision: 359155
- kdelibs-devel is now kdelibs3-devel, change requirements.
- Fix following update error from older packages:
  kdebase-ksysguard < 30000000:3.5.10-8 conflicts with kdebase3-ksysguard-1:3.5.10-15mdv2009.1.i586
  kdebase-ksysguard < 1:3.5.10-9 conflicts with kdebase3-ksysguard-1:3.5.10-15mdv2009.1.i586

* Wed Mar 18 2009 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-15mdv2009.1
+ Revision: 357162
- Add conflicts to ease upgrade

* Wed Mar 18 2009 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-14mdv2009.1
+ Revision: 357135
- Remove Wrong requires

* Tue Mar 17 2009 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-12mdv2009.1
+ Revision: 356609
- Add Provides to ease upgrade

* Tue Mar 17 2009 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-10mdv2009.1
+ Revision: 356311
- Fix Requires

* Mon Mar 16 2009 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-9mdv2009.1
+ Revision: 355934
- Adapt to new name
- Build with beagle
- Start to fix build
- Change kdebase to kdebase3 ( kde3 reintroduction step 3 )

  + Funda Wang <fundawang@mandriva.org>
    - rediff consolekit patch
    - rediff ksmserver-suspend patch
    - rediff ksmserver-timed patch
    - rediff kickoff mandriva patch
    - rediff kickoff patch
    - rediff vibrate dialog patch
    - rebuild for new libraw1394

* Sat Nov 08 2008 Adam Williamson <awilliamson@mandriva.org> 1:3.5.10-7mdv2009.1
+ Revision: 301160
- drop krootwarning dep (it is broken and will only be rewritten for kde4, not
  fixed)

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against new libxcb

* Mon Sep 29 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-6mdv2009.0
+ Revision: 289240
- add upstream patch
  Fix the passing the 'locale' mount option:
- read the real locale from the environment (including the charset), the language is of no use to FS drivers,
- do not attempt to store the locale in the config file, it has to be the current one,
- only pass the locale if the filesystem type is ntfs-3g, HAL is broken and lists 'locale' as available with the Linux
  in-kernel ntfs driver (http://bugs.freedesktop.org/show_bug.cgi?id=17753)

* Mon Sep 29 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.10-5mdv2009.0
+ Revision: 289118
- Fix source name
- Add some autostart files
- allow the entire range of valid ports on knetattach
- Fix File list
- fix name of logrotate file

* Tue Sep 16 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-3mdv2009.0
+ Revision: 285192
- Moved wmsession to make upgrade easier

* Wed Sep 10 2008 Frederic Crozat <fcrozat@mandriva.com> 1:3.5.10-2mdv2009.0
+ Revision: 283518
- Fix filetriggers for icon cache, was using old path

* Tue Aug 26 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-1mdv2009.0
+ Revision: 276330
- Update for probably the last upstream kdebase from kde3

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] Fix Mounting USB sticks with spaces in label (Bug #30139)
    - update hal privilege names to match newer hal versions (11.0 or newer)

* Fri Jul 04 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.9-50mdv2009.0
+ Revision: 231887
- Fixing khotkeys to autostart only with KDE
- Removing CrossFade effect on KDE 3 desktop changes

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add patch 123: Avoid lockup after a failed login on LDAP systems, which give
      'LDAP Password incorrect: try again' and want to get the right one again.
    - Revive logrotate conf file

* Tue Jun 24 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-47mdv2009.0
+ Revision: 228753
- Fix Requires
- [BUGFIX] Remove extra space in NAME (Bug #41612)

* Mon Jun 16 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-45mdv2009.0
+ Revision: 220504
- For some strange reason kdebase package not arrived on BS. Revuilding

* Sun Jun 15 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.9-44mdv2009.0
+ Revision: 219246
- fix kickoff underlinking

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - add rpm filetrigger running gtk-update-icon-cache when rpm install/remove hicolor/crystalsvg icons for kde3
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.9-43mdv2009.0
+ Revision: 214530
- rebuild for new qt3 libdir

  + Danilo Cesar Lemes de Paula <danilo@mandriva.com>
    - Decrease the number of steps of Hour based transitions (Kdesktop)

* Mon May 19 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 1:3.5.9-42mdv2009.0
+ Revision: 208975
- Use versioned obsoletes

* Fri May 09 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-41mdv2009.0
+ Revision: 205302
- Fix macros for cache image

* Tue May 06 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-40mdv2009.0
+ Revision: 201679
- Fixed konsole font dir
- Fixed session entry
- removed ksysguard useless script ( was about time )

* Mon May 05 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-39mdv2009.0
+ Revision: 201372
- Same invalid arts require breaking x86_64

* Sun May 04 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-38mdv2009.0
+ Revision: 201022
- Moving for /opt
- Adding patches using de then "inpatch  log info

* Thu Apr 03 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-36mdv2008.1
+ Revision: 192288
- Fixing last mistake in add unicode string instead of real utf8 string to translation in tooltip

* Wed Apr 02 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.9-35mdv2008.1
+ Revision: 191983
- Fixing a Kdesktop/background bug (screen come to black when there isn't any file into slideshow)

* Wed Apr 02 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-34mdv2008.1
+ Revision: 191799
- Fixed kdeeject. We should stop to try using magic and not update it...

* Wed Apr 02 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-33mdv2008.1
+ Revision: 191677
- Added possibility to enable/disable shadow on text on menu button. Default is false
- Fixes "zoom" effect showing icons on big tooltips. The standard is 128x128

* Wed Apr 02 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-32mdv2008.1
+ Revision: 191620
- Fix double copy and message advise on bookmarks initializing

  + Danilo Cesar Lemes de Paula <danilo@mandriva.com>
    - Adding KDesktop resize pb patch to buildsystem
    - Solving the problem with background refresh delay when users tries to resize desktop with Krandr

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - Fix tooltip internationalization on menus

* Mon Mar 24 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-30mdv2008.1
+ Revision: 189790
- kwin bugfix patch from branch

* Sat Mar 22 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-29mdv2008.1
+ Revision: 189486
- Fix groups ( tks to pterjan)

* Tue Mar 18 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-28mdv2008.1
+ Revision: 188630
- kwin minimize fix from kdebase branch

  + Danilo Cesar Lemes de Paula <danilo@mandriva.com>
    - Fixing KControl/Background xml recover

* Tue Mar 18 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.9-27mdv2008.1
+ Revision: 188503
- Rebuilding the package with a higher release number to add
  KControl/Background XML support.
- Kcontrol/Background modified. Now users can select betwin normal slide show or
  XML controled slide show

* Fri Mar 14 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-26mdv2008.1
+ Revision: 187964
- Add conflicts on kmenuedit

* Fri Mar 14 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-25mdv2008.1
+ Revision: 187949
- Fixing bug https://qa.mandriva.com/show_bug.cgi?id=38789

* Tue Mar 11 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.9-24mdv2008.1
+ Revision: 185868
- Fixing KBackground CrossFade effect bug, acording with
  https://qa.mandriva.com/show_bug.cgi?id=38598

* Mon Mar 10 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-23mdv2008.1
+ Revision: 183663
- Update with trayproxy and messagebox patches.

* Mon Mar 10 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.9-22mdv2008.1
+ Revision: 183489
- Colorband fixed under Kbackground by using QImage insted QPixmap (and X11 stuffs)

* Fri Mar 07 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-21mdv2008.1
+ Revision: 181614
- Another chnage but not change because is already changed in the last change button change :-/
- Copy global bookmark if exists to user dir, and if user doesn't have already one

* Thu Mar 06 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-20mdv2008.1
+ Revision: 181053
- KDM Userlist icon not resizes anymore for an arbitary size. Now users can have fun with baboon :-)

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add a Requires on mandriva-kde-translation

* Thu Mar 06 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-18mdv2008.1
+ Revision: 180267
- Translation support not needed here as this is done on kdelibs now
- Add translation support for mandriva strings in kde

  + Helio Chissini de Castro <helio@mandriva.com>
    - Fixed common icon taskbar resizing
    - Fixed text over standard menu button

  + Andreas Hasenack <andreas@mandriva.com>
    - pam_nologin has to be in auth also for kde3-np
    - move system-auth to the bottom of the session section
      in the pam config files, or else a "sufficient" module
      in the included file could prevent other modules *after*
      the include statement from being called (#37801)
    - pam_nologin's proper section is the account one, not auth

* Tue Mar 04 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.9-16mdv2008.1
+ Revision: 178858
- Adding a new support to Kbackground change Image acording a XML file, using crossFade effects

* Tue Mar 04 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-15mdv2008.1
+ Revision: 178416
- Post 3.5.9 bug fixes from kde branch.
- Unbreaking lm_sensors
- Fixing multiple crashes on khotkeys

* Tue Mar 04 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-14mdv2008.1
+ Revision: 178249
- Fix button sizing and alignment. No more auto resizing unless specified in max size. Button is now centralized.
  Config entries KMenuButtonScale, TextRelativeXPos and TextRelativeYPos are obsoleted.
  Added KMenuButtonMaxVSize. Mandriva defualt size for 2008.1 is 22, all kicker sizes larger than 32 will have their
  own button scaled to the proper size.
- Fix positioning of Text on both horizontal and vertical. Vertical calculation is not perfect but is more than ok for now.
- kickoff now uses same button code, so no more ugly different buttons for both menus.

* Fri Feb 29 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.9-13mdv2008.1
+ Revision: 176870
- Fix the kdm theme selector so that it works using mandriva themes

* Thu Feb 28 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-12mdv2008.1
+ Revision: 176428
- Change mandrake_desk for desktop-common-data as requested by Frederic Crozat

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Update usb.ids database

* Wed Feb 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-11mdv2008.1
+ Revision: 175935
- Major KDM themer fixes. Userlist is now NIS and LDAP friendly
- Fixed font weight in themer. Now is possible add font="Sans 12 WEIGHT", where weight can be any of Light, DemiBold Bold, Black or Normal.
  Normal is default
- Fixed non-local UserList ( NIS, LDAP, etc.. )
- Added support to show or not real user name ( double line with real user name ). Default is false

* Tue Feb 26 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-10mdv2008.1
+ Revision: 175599
- KDM themer now have support for define icon users size
- KDM themer userlist support now is fixed
  TODO Alternate userlist background, possible button support
- KDM kcontrol user small refactor to match XDG user face /usr/share/faces/. KDM comes next

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add patch42 : add translations support + Fix typo
    - Fallback on official tarball and use patch until this is not on svn
    - Add translation support on mandriva-profile-chooser
    - [BUGFIX] Remove logrotate for kdm (Bug 34068)

* Fri Feb 22 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.9-7mdv2008.1
+ Revision: 174010
- Adding CrossFade effect into Kdesktop Background changes

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] Fix Kcontrol menu entry to show that this is KDE related (Bug #35870)

* Wed Feb 20 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-6mdv2008.1
+ Revision: 173263
- Fixed kate bug bu Colin Guthrie
- Fix BKO #158069 - Kate bad position

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [FEATURE] Add patch38: Fix Kcontrol energy module when Kpowersave is on  (Bug #32021)
    - Delete $kdehome/Autostart/alignment-icons.desktop if it exist as we do not have it anymore
      This file existed on 2007.1 so this make migration problem
    - Remove if as backports are done
    - Add switch for backports

* Sat Feb 16 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-3mdv2008.1
+ Revision: 169312
- make screensaver-onlyshowin-kde.patch patch back again

* Fri Feb 15 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-2mdv2008.1
+ Revision: 168878
- Make consolekit patch come back (Patch34)

* Thu Feb 14 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-1mdv2008.1
+ Revision: 168526
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches intregrated
- Patch for icon sizing on KDM listing disabled until formal spec arrive for new KDM

* Wed Feb 13 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-17mdv2008.1
+ Revision: 167182
- Make rpmlint happier
- Add back icon for switch user option in Kmenu

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - Add support for Tooltip in the KMenu entries showing an brief description of
      what the application is for

* Fri Feb 01 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.8-16mdv2008.1
+ Revision: 161250
- Change the layout of the top row of the menu: now the KDE version is shown
  on the right

* Fri Feb 01 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.8-15mdv2008.1
+ Revision: 161169
- Fixing mandriva-profile-chooser application to work with alternatives

* Fri Jan 25 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.8-14mdv2008.1
+ Revision: 158031
- Update kdm style gdm like patch, from make it cool branch
- Update console kit patch

* Tue Jan 22 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.8-13mdv2008.1
+ Revision: 156242
- Fixing double top bar widget drawing. The situation that triggers double bars was directed connected to hability to show or
  not recent apps on menu. With recent show enabled ( larger than 0 ), double bars are appearing.
  With no recent show enabled, no bar appears at all.

* Wed Jan 16 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-12mdv2008.1
+ Revision: 153912
- [BUGFIX] Do not put kcontrol own widgets inside of QXEmbed. (Bug #36478)

* Wed Jan 09 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.8-11mdv2008.1
+ Revision: 147327
- Kickoff should not be the default one. Thanks to neoclust to catch another fail point

* Wed Jan 09 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.8-10mdv2008.1
+ Revision: 147156
- Fixed wrong icon on kickoff patch
- Added menu icon switch patch for compilation without kickoff, as requested by Nicolas Lecureil
- Time based logout dcop call for ksmserver.

* Tue Jan 08 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.8-9mdv2008.1
+ Revision: 146890
- Integrated all Mandriva changes in mandriva-kickoff.patch, including menu icon switch
- Added switch of menu type in kcontrol
- Removed obsolete patches
- Integrated kicker top patch on mandriva kickoff patch

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Do not show screensavers on the menu

* Tue Jan 08 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.8-8mdv2008.1
+ Revision: 146625
- Bug Fixes in KDM Theme Selector.

* Fri Jan 04 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.8-7mdv2008.1
+ Revision: 144918
- Add a KDM Theme Selector in KControl

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Dec 23 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-6mdv2008.1
+ Revision: 137336
- first step to fix build against new beagle
- Fix Beagle includes in kickoff patch

  + Helio Chissini de Castro <helio@mandriva.com>
    - Updated for lates branch with merged flash fix patches
    - Disabled kickoff menu for now, since not all mandriva patches are integrated
    - Recompile against new libldap
    - libbeagle should be now 0.3.0 or higher
    - Fixed apidocs install dir ( no more versioning )
    - Added new flash patch for kdebase from novell
    - Updated kickoff patch to fix compile order
    - Commented old beagle query code ( old api )
    - Add missing patch
    - Enabled initial kickoff Mandriva changes patch
    - Fixed liblazy api imcompatibilities
    - Fixed consolekit patch
    - Updated ksmserver suspend patch against liblazy
    - Added kdm suspend patch against liblazy
    - Proper tarball with admin included
    - Added with-console-kit option in configure instead of use hardcoded WITH_CONSOLE_KIT
    - Add first part of mandriva kickoff patch
    - Beginning changes to kickoff update. Old patch replaced bu official from suse branch. Mandriva post patch coming, including button switch
    - Updated to branch, as agreed between kde team
    - Added new console-kit version of the patch, ready to be commited upstream uppon maintainer agreement
    - Added Lubos flash patch to test
    - removed all post-3.5.8 patches already included in new tarball

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - require the righ lm_sensor library
    - rebuild for new libbeagle

* Fri Nov 23 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.8-3mdv2008.1
+ Revision: 111505
- Set QTDIR on startkde pointing to qt3, as qt4 will be the default qt in 2008.1

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Forwardport fixed ConsoleKit patch from Frederic Crozat (Patch18)
      This fixes the kdm bug that prevent remote login (Bug #34786)

* Sun Nov 04 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-2mdv2008.1
+ Revision: 105871
- Add missing BuildRequire
- Add usptream 3.5.9 branch patches
  	- Fix memleak
  	- Fix some compilation issues
  	- Fix some DPMS issues
- Add usptream 3.5.9 branch patches
  	- Add better upstram fix for gdm 2.19+ ( Patch 149 )
  	- Fix no_action with firefox under klipper ( Patch 154 )
  	- Fix media unmount ( Patch 152 )

* Thu Nov 01 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-1mdv2008.1
+ Revision: 104717
- Use mandriva icons on Kickoff
- [BUGFIX] Add Network keyword to have wizard assistant shown (Bug #35185)
- [BUGFIX] Fix quick launcher applet for Home url (Bug #34450)
- Start to add kickoff back ( part 1 )
- Remove merged patches
  Update patch 110
- Kde 3.5.8
- Remove upstream merged patches

* Tue Oct 23 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.7-41mdv2008.1
+ Revision: 101564
- htsearch is installed in /usr/bin in our distro

* Fri Oct 19 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-40mdv2008.1
+ Revision: 100208
- [BUGFIX] Fix screensaver issue (Bug #32778)
- [BUGFIX] Add htdig for building inex support (Bug #22053)

* Fri Oct 12 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.7-39mdv2008.1
+ Revision: 97269
- sysinfo has been renamed to kio-sysinfo

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-ended-with-dot

* Wed Oct 03 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-38mdv2008.0
+ Revision: 95068
- Do not require kate, just suggest it

* Tue Oct 02 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-37mdv2008.0
+ Revision: 94808
- Fix the kdm translation patch by forwarding the LANG env var from kdm to the
  greeter.
- Re-add a wrongly removed patch fixing firstboot focusing on kdm

  + Helio Chissini de Castro <helio@mandriva.com>
    - Fix kdm localization. Original code is bypassing all locales assigning only language set on kdmrc.
      Now code validates LANGUAGE env var, otherwise fallbacks to kdmrc Language set and in the last
      resource standard en_US.

* Fri Sep 28 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-36mdv2008.0
+ Revision: 93747
- Fix unmounting of media devices that are on fstab (#30157)

* Fri Sep 28 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-35mdv2008.0
+ Revision: 93510
- [BUGFIX] Add icon for "Lock Current && Start New Session" (Bug #23900)

* Wed Sep 26 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-34mdv2008.0
+ Revision: 93093
- Make kdesktop copy desktop files to the user home dir on first run (#33204)

* Tue Sep 25 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-33mdv2008.0
+ Revision: 92923
- Enable sound server at KDE startup (#32306)
- Make kdebase-progs require the external KRandR

* Fri Sep 21 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-32mdv2008.0
+ Revision: 91968
- More menu fixes ( maybe latests ;) )
- More menu fixes

* Fri Sep 21 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-31mdv2008.0
+ Revision: 91828
- Make the kmenu squared icon scale too.

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] Do not show KTip on the menu (Bug #33757)
    - [BUGFIX] Add logrotate file for KDM (Bug #23227)
    - [BUGFIX] Do not show Kappfinder on the menu (Bug #33062)
    - [BUGFIX] Do not show kicker kcm on menu (Bug #33064)
    - [BUGFIX] Show KHelpcenter on the Documentation menu (Bug #32842)
    - [BUGFIX] Do not display Kpersonaliser on the menu (Bug #33063)

* Tue Sep 18 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-30mdv2008.0
+ Revision: 89722
- Removed the unfinished button config dialog
- Add a context menu entry making it possible to switch between mandriva menu
  icon and the default kde menu icon.

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] Do not display kpager (Bug #32671)
    - [BUGFIX] move out Kjobviewer of system tool section (Bug #33439)

* Mon Sep 17 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-29mdv2008.0
+ Revision: 89321
- Readd a patch to fix gtk color handling for Ia Ora

* Fri Sep 14 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-27mdv2008.0
+ Revision: 85383
- [BUGFIX] Make KControl appear on the menu (BUG #32678)
- [BUGFIX] Fix compatibility with gdm 2.19 (BUG #31460)

* Thu Sep 13 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-26mdv2008.0
+ Revision: 85319
- Add lzma support (#32877)

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] Do not display screensavers on the menu ( NoDisplay=true )

* Tue Sep 04 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-25mdv2008.0
+ Revision: 78999
- Added lates patches fomr branch
- Removed nsplugin patch, thanks to Fred Crozat that added workaround patch in gtk
- Added call to drackclock, as required by Andreas

* Thu Aug 30 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-23mdv2008.0
+ Revision: 76297
- Another broken patch causing headaches. Now the "konqueror fixes" was leading to wrong test on tab
  and rewriting location bar with invalid address from other tab. What did i say about non tested
  patches and put non valid text inside ?
- Lubos fixed my patch to linking pluginspath on nsplugins. Way better than use a static link.

* Wed Aug 29 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-22mdv2008.0
+ Revision: 74618
- Requires krandr
- Fix again another invalid patch not tested. People should take care when add things without know
  exactly if would work.

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - Remove files that are now in the krandr packages

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add upstream patch from BRANCH "Avoid reports about X errors"

* Tue Aug 28 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-20mdv2008.0
+ Revision: 72701
- xrandr should not be requires anymore.

  + Michael Scherer <misc@mandriva.org>
    - fix typo leading to uninstallable package ( i guess "x andr" should be "xrandr" )

* Mon Aug 27 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-19mdv2008.0
+ Revision: 72237
- Removed krandrtray < 1.2 support. 1.2 support will be provided by external package for KDE 3.
- Added recent patches from kdebase branch

* Fri Aug 24 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-18mdv2008.0
+ Revision: 70790
- Added xdg-user-dirs patch for enble in kde modification
- Added new menu modifications asked by fcrozat
- Removed old /etc/xdg/kde/menu
- Added remaining branch patches

* Tue Aug 21 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-17mdv2008.0
+ Revision: 68734
- Reenable mozilla nsplugin code. The previous issue was triggered by a different bug.

  + Funda Wang <fundawang@mandriva.org>
    - fix file conflict between nsplugin and common subpackage

* Thu Aug 16 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-15mdv2008.0
+ Revision: 64069
- Again, nsplugin is behaving weirdly due to gtk init on flash plugin, happening just in i586. Boiko did a patch for old
  nspluginviewer but not fix the new mozilla based code. For now mozilla base patch will be disabled
  to keep Boiko's patch working and we will find a better solution after, since Mozilla code is way
  improved...

* Tue Aug 14 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-14mdv2008.0
+ Revision: 63176
- Added post 3.5.7 patches from branch.
- Added mozilla nspplugin sdk code patch
- Removed erroneous xinerama options
- Minor spec fix
- Added konsole font for proper place. We do not need call an fc-cache forced on common package,
  just on konsole, which provides de fixed font
- Removed obsolete cal to kicker migrate

* Mon Aug 13 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-13mdv2008.0
+ Revision: 62572
- Fix some duplicates that were preventing a proper installation

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add OnlyShowIn on keyboard_layout.desktop file (bug #32471)
    - Add upstream patch to fix konqueror issues (Patch211)
    - Allow to have Konqueror on menu on non- WM
    - [BUGFIX] Do not forget to call functions file (for gprintf) (Bug #32176)

  + Helio Chissini de Castro <helio@mandriva.com>
    - Fix patch for menu in sidebar

  + Anssi Hannula <anssi@mandriva.org>
    - move kate, kmenuedit, konsole, ksysguard menu entries to their
      respective packages to avoid having menu entries or mimetype
      associations that only return an error

* Fri Jul 27 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-12mdv2008.0
+ Revision: 56451
- * Big Cleanup
  Old menu files, upgrades and root interface removed. Root interface will be exchanged for a better
  kde-config solution, if root interface still desired
  Many patches are exchanged for upstream versions, and commited on upstream when relevant
  Patches removed:
- kdebase-3.0.3-fix-index-html.patch: Obsoleted
- kdebase-3.1-fix-load-default-panel-appl-in-simplified-menu.patch: Obsoleted
- kdebase-3.2-add-multimedia-key.patch: Hardcoded entry. Will be handled by kde-config
- kdebase-3.2-fix-paste-action-in-konsole.patch: Not needed anymore. Upstream similar solution
  already in code
- kdebase-3.2-kde-info2html.patch: Use strict back.
- kdebase-3.3-remove-help-entry-into-kdesktop.patch: Hardcoded entry. Will be handled by kde-config
- kdebase-3.3.2-fix-miniclip-icon.patch: Hardcoded entry. Will be handled by kde-config
- kdebase-3.4.0-fix-arts-mdk-bugs-11671.patch: Exchanged by upstream patch
- kdebase-3.4.0-fix-mdk-merge-dir.patch: Not needed anymore
- kdebase-3.4.0-konqueror-about.patch: Not needed anymore. Can be done in kde-config
- kdebase-3.4.92-ksplashscreen-mdk.tar.bz: We're not using this anymore. Time to obsolete this old
  code
- kdebase-3.5.6-startkde.patch: Replaced for mandriva-startkde as file
- kdebase-3.5.6-fix-screensaver-nodisplay.patch: Exchanged by upstream patch
- kdebase-3.5.3-add-mdv-device.patch: No devices:/ anymore hardcoded
- kdebase-3.5.4-fix-screensaver-onlyshowin-kde.patch: Exchanged by upstream patch
- kdebase-3.5.6-disable-kicker-notify.patch: Obsoleted
- kdebase-3.4.2-startkde-align-icones.patch: Hacked solution not applied anymore
- kdebase-3.5.2-startkde-move-menu-directory.patch: Obsoleted
- kdebase-3.5.3-fix-kthememanager-enable-button.patch: exchanged by upstream
- kdebase-3.4.2-fix-wrap-crash.patch: Exchanged by upstream patch
- kdebase-3.4.2-fix-default-kthememanager-name.patch: Hardcoded config
- kdebase-3.5.3-xinerama.patch: Exchanged by upstream patch
- kdebase-3.5.4-fix-gtk-style.patch: Hardcoded config
- kdebase-3.5.3-install-script-kde.patch: Not needed anymore
- kdebase-3.2.3-fix-makefile-crypto.patch: Exchanged by upstream patch
- kdebase-3.5.6-launch-mcc.patch: Not applied anymore
- kdebase-3.5.4-media-mnt.patch: Moving to standard /media
- kdebase-3.5.6-fix-load-kmix.patch: Hardcoded config
- kdebase-3.4.0-fix-mdk-bug-16007.patch: Obsoleted
- kdebase-3.4.0-fix-kfileivi.patch: Exchanged by upstream patch
- kdebase-3.5.6-kicker-desktop.patch: Hardcoded config
- kdebase-3.4.2-mdkft.patch: Not needed anymore
- kdebase-3.5.4-fix-old-icon-pos.patch: Obsoleted
- kdebase-3.4.92-fix-detect-ntfs-partition.patch: Obsoleted
- kdebase-3.4.2-kwin-theme.patch: Obsoletes by kde-config
- kdebase-3.5.4-international-bookmarks.patch: Hardcoded config. Can go in kde-config
- Avoid preview crashes when view is invalid

* Fri Jul 27 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-11mdv2008.0
+ Revision: 56407
- Workaround a flashplayer plugin bug that appeared after latest gtk update

  + Frederic Crozat <fcrozat@mandriva.com>
    - Patch183 (Fedora): add ConsoleKit support

* Mon Jul 23 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-10mdv2008.0
+ Revision: 54628
- Add proper patch
- Fix Buildrequire
- [BUGFIX] Fix kdeeject patch (closing bugs #30153 and #31830)
- [BUGFIX] Add missing fatal_error function ( bug #31830)
- [BUGFIX] Show key bindings in the menu (Bug #31558)
- [BUGFIX] Do not own /etc/X11/wmsession.d ( bug #31561)
-[BUGFIX] Fix typo on desktop file ( bug #31436)
- Fix OnlyShowIn=KDE;

  + Olivier Blin <oblin@mandriva.com>
    - require kdebase-common in kdebase-kdm (for pam files)

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 1:3.5.7-8mdv2008.0
+ Revision: 36177
- rebuild with correct optflags

  + Christiaan Welvaart <spturtle@mandriva.org>
    - remove kcontrol-ppc from filelist

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Remove hardcoded packager

  + Helio Chissini de Castro <helio@mandriva.com>
    - Fix suspend menu on kickoff entries

* Mon Jun 04 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-7mdv2008.0
+ Revision: 35224
- Fix categories
- Add Requires on sysinfo if Kickoff is build (bug #31168)
- More category fixes
- Remove patch90: Broken Klipper launch

  + Helio Chissini de Castro <helio@mandriva.com>
    - Removed ancient files
    - Removed more hardcoded files and moved for config package
    - Added konsole real transparency patch
    - Better change the mess now before we reach new release. Moving only the daemon doesn't make sense since it's do nothnig alone, so move all ksysguard tool is more usefull.

* Tue May 29 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-2mdv2008.0
+ Revision: 32543
- [feature] Split ksysguardd in its own package (#16352)

* Thu May 17 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.7-1mdv2008.0
+ Revision: 27565
- BuildRequires mkfontscale
- BuildRequires mkfontdir

  + Helio Chissini de Castro <helio@mandriva.com>
    - 3.5.7 release
    - Added translations for kickoff menu
    - Modified kicker patches to match extra image on rtl languages
    - Remove all references and ifdefs for old distributions.
    - Removed old patches that od not apply or are solved in different way in upstream KDE
    - Back to use stable branch.
    - Removed all references to old menudir method. We are using xdg and xdg only now.
    - As requested by users, kickoff menu adapted to Mandriva style as alternative.

  + Olivier Blin <oblin@mandriva.com>
    - add missing escape to fix configure

* Mon Apr 23 2007 Laurent Montel <lmontel@mandriva.org> 1:3.5.6-35mdv2008.0
+ Revision: 17171
- Fix nsplugins

