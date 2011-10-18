%define use_enable_indexlib 0
%{?_enable_indexlib: %{expand: %%global use_enable_indexlib 1}}

%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define lib_name_orig %mklibname kdepim
%define lib_major 2
%define lib_name %mklibname kde3kdepim %lib_major

%define lib_name_orig_akregator %mklibname akregator
%define lib_major_akregator 0
%define lib_name_akregator %lib_name_orig_akregator %lib_major_akregator

Name: kde3-kdepim
Version: 3.5.12
Release: %mkrel 2
Epoch: 1
Group: Graphical desktop/KDE3
Summary: K Desktop Environment - Person Information Management
License: GPL
URL: http://www.kde.org
Source:  ftp://ftp.kde.org/pub/kde/stable/%version/src/kdepim-%version.tar.bz2
Source1: kdepim-3.2-kontact-addressbook.sh  
Source2: kdepim-3.2-kontact-knotes.sh
Source3: kdepim-3.2-kontact-kmail.sh        
Source4: kdepim-3.2-kontact-korganizer.sh
Source5: kdepim-3.2-kontact-knode.sh
Source6: kdepim-3.2-kontact-akregator.sh
Source7: configguibarry.cpp
Source8: configguibarry.h
######   Patches   ########
Patch1:	 kdepim-3.4.0-fix-kmail-dimap-speedup.patch
Patch2:	 kdepim-3.4.0-use-point-kmail.patch
Patch3:	 kdepim-3.4.2-knode-disable-first-start.patch
#Patch4:  kdepim-3.5.3-kaddressbook-resources.patch
Patch5:  kdepim-3.5.4-fix-kalarm-call-twice-dialogbox.patch
Patch7:  kdepim-3.5.4-korganizer-use-sys-timezone.patch
Patch9:  kdepim-3.5.7-kmail-hide_help_button.patch
Patch11: kdepim-3.5.9-allow-knode-sideband.patch
Patch12: kdepim-3.5.9-kitchensync-handle-synce.patch
Patch13: kdepim-3.5.9-kitchensync-barry.patch
Patch14: kdepim-3.5.9-fix-underlinking.patch
Patch15: kdepim-only_kde3.patch
#Patch16: kdepim-3.5.10-gcc44.patch
Patch17: kde-3.5.10-acinclude.patch
#Patch18: fix_autotools.patch
Patch19: kdebase-3.5.12-config.patch
Patch20: kdebase-3.5.12-move-xdg-menu-dir.patch
BuildRoot: 	%_tmppath/%name-%version-%release-root
Conflicts:  kdenetwork <= 3.1.92
BuildRequires: kde3-macros
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%endif
BuildRequires: autoconf >= 1:2.65
BuildRequires: automake > 1.5
BuildRequires: kdelibs-devel >= 30000000:3.5
BuildRequires: gpgme-devel 
BuildRequires: X11-devel 
# MAL conduit is disabled upstream since 3.5.6: see source
# BuildRequires: libmal-devel >= 0.31
BuildRequires: libncurses-devel
BuildRequires: readline-devel
BuildRequires: pilot-link-devel
BuildRequires: libgpg-error-devel
BuildRequires: gnokii-devel
BuildRequires: graphviz
BuildRequires: libxml2-utils
BuildRequires: gnupg
BuildRequires: bluez-devel 
BuildRequires: libsasl-devel
BuildRequires: doxygen
BuildRequires: qt3-doc
BuildRequires: pilot-link-devel
BuildRequires: libopensync-devel < 0.30
BuildRequires: flex
BuildRequires: boost-devel
BuildRequires: bison
BuildRequires: byacc
BuildRequires: tcl-devel
BuildRequires: libical-devel
BuildRequires: libmal-devel
Requires: kde3-kdepim-karm 
Requires: kde3-kdepim-knotes 
Requires: kde3-kdepim-kaddressbook 
Requires: kde3-kdepim-kpilot 
Requires: kde3-kdepim-kmail 
Requires: kde3-kdepim-knode 
Requires: kde3-kdepim-kontact 
Requires: kde3-kdepim-korganizer 
Requires: kde3-kdepim-korn 
Requires: kde3-kdepim-ktnef 
Requires: kde3-kdepim-akregator 
Requires: kde3-kdepim-kandy 
Requires: kde3-kdepim-wizards 

%description
Information Management applications for the K Desktop Environment.
	- kaddressbook: The KDE addressbook application.
	- kandy: sync phone book entries between your cell phone and computer
         ("kandy" comes from "Handy", the german word used for a cellular)
	- korganizer: a calendar-of-events and todo-list manager
	- kpilot: to sync with your PalmPilot
	- kalarm: gui for setting up personal alarm/reminder messages
	- kalarmd: personal alarm/reminder messages daemon, shared by korganizer and
           kalarm.
	- kaplan: A shell for the PIM apps, still experimental.
	- karm: Time tracker.
	- kitchensync: Synchronisation framework, still under heavy development.
	- kfile-plugins: vCard KFIleItem plugin.
	- knotes: yellow notes application
	- konsolecalendar: Command line tool for accessing calendar files.
	- kmail: universal mail client
	- kmailcvt: converst addressbooks to kmail format

%files

#----------------------------------------------------------------------

%package common
Summary: Common files for kdepim
Group: Graphical desktop/KDE3
Conflicts: dynamic <= 0.3-2mdk
Conflicts: kdeutils <= 2.2.2-28mdk
Conflicts: kdenetwork <= 3.1.92
Conflicts: libkdenetwork2-common <= 1:3.1.3-37mdk
Conflicts: kdebase-common <= 1:3.3.2
Conflicts: kdepim-kpilot <= 1:3.5.3-5mdv2007
Conflicts: kdepim-kandy <= 1:3.5.3-5mdv2007
Conflicts: kdepim-kaddressbook < 1:3.5.8-2
Conflicts: kdepim-knotes <= 1:3.5.3-5mdv2007
Conflicts: kdepim-knode <= 1:3.5.3-5mdv2007
Conflicts: kdepim-kmail < 1:3.5.7-%mkrel 5
Conflicts: kdepim-devel < 1:3.5.7-%mkrel 15
Conflicts: kdepim-kontact <= 1:3.5.8-4mdv2008.1
Requires:  sasl-plug-digestmd5
Requires:  sasl-plug-login
Requires:  sasl-plug-plain
Obsoletes: kdepim =< 3.1-17mdk
Obsoletes: kdepim-ksync < 1:3.5.9
Obsoletes: kdepim-common = %epoch:%version-%release
Provides:  kdepim-common = %epoch:%version-%release
Obsoletes: %lib_name-ksync < 1:3.5.9
Requires:  kde-custom-icons
Requires:  %lib_name-common >= %epoch:%version-%release
Requires:  libical0

%description common
Common files for kdepim


%files common
%defattr(-,root,root,-)
%_kde3_iconsdir/*/*/*/button_*
%dir %_kde3_appsdir/kdepim/icons
%_kde3_appsdir/kdepim/icons/*
%_kde3_datadir/services/groupwise.protocol
%_kde3_datadir/services/groupwises.protocol
%_kde3_datadir/services/imap4.protocol
%_kde3_datadir/services/imaps.protocol
%_kde3_datadir/services/scalix*.protocol
%_kde3_datadir/services/kcmsdsummary.desktop
#%_kde3_datadir/services/kded/networkstatus.desktop
%_kde3_datadir/servicetypes/dcopimap.desktop
%_kde3_datadir/servicetypes/kaddressbookimprotocol.desktop
#%_kde3_bindir/networkstatustestservice
%_kde3_bindir/kode
%_kde3_bindir/kxml_compiler
%_kde3_bindir/kleopatra
%_kde3_bindir/kwatchgnupg
%_kde3_bindir/scalixadmin
%_kde3_appsdir/kleopatra/kleopatraui.rc
%dir %_kde3_appsdir/libkleopatra/
%_kde3_appsdir/libkleopatra/*
%_kde3_datadir/applications/kde/kleopatra_import.desktop
%_kde3_datadir/config/libkleopatrarc
%_kde3_datadir/services/kleopatra_*
%_kde3_libdir/kde3/kcm_kleopatra.*
%doc %_kde3_docdir/HTML/en/kleopatra
%dir %_kde3_appsdir/kwatchgnupg/
%_kde3_appsdir/kwatchgnupg/*
%dir %_kde3_appsdir/libkdepim
%_kde3_appsdir/libkdepim/*
%dir %_kde3_appsdir/kdepimwidgets
%_kde3_appsdir/kdepimwidgets/*
%dir %_kde3_appsdir/kgantt
%_kde3_appsdir/kgantt/*
#%dir %_kde3_appsdir/libical
#%_kde3_appsdir/libical/*
%doc %_kde3_docdir/HTML/en/kwatchgnupg
%_kde3_libdir/kde3/kcm_sdsummary.*
#%_kde3_libdir/kde3/kded_networkstatus.*
%_kde3_libdir/kde3/kio_groupwise.*
%_kde3_libdir/kde3/kio_imap4.*
%_kde3_libdir/kde3/kio_mbox.*
%_kde3_libdir/kde3/kio_sieve.*
%_kde3_libdir/kde3/kio_scalix.*
%_kde3_libdir/kde3/kcal_*
%_kde3_libdir/kde3/kcm_korgsummary.*
%_kde3_libdir/kde3/resourcecalendarexchange.*

%_kde3_datadir/applnk/.hidden/kalarmd.desktop
%_kde3_datadir/applnk/Applications/kalarm.desktop
%_kde3_appsdir/kconf_update/kpgp-3.1-upgrade-address-data.pl
%_kde3_appsdir/kconf_update/kpgp.upd
%dir %_kde3_datadir/services/kresources
%_kde3_datadir/services/kresources/*
%_kde3_appsdir/kconf_update/kolab-resource.upd
%_kde3_appsdir/kconf_update/upgrade-resourcetype.pl
%_kde3_datadir/services/kcmkorgsummary.desktop
%_kde3_datadir/services/sieve.protocol
%_kde3_datadir/servicetypes/dcopcalendar.desktop
%_kde3_datadir/servicetypes/korgprintplugin.desktop		 
%_kde3_datadir/applications/kde/konsolekalendar.desktop
%_kde3_iconsdir/*/*/*/konsolekalendar.*
%_kde3_iconsdir/*/*/*/korganizer*
%_kde3_appsdir/korgac/icons/crystalsvg/22x22/actions/korgac.png
%_kde3_appsdir/korgac/icons/crystalsvg/22x22/actions/korgac_disabled.png
%_kde3_datadir/services/mbox.protocol
%_kde3_datadir/config.kcfg/*
%exclude %_kde3_datadir/services/kresources/knotes/kolabresource.desktop
%exclude %_kde3_datadir/services/kresources/knotes_manager.desktop
%exclude %_kde3_datadir/services/kresources/kabc

#----------------------------------------------------------------------

%package kitchensync
Group:     Graphical desktop/KDE3
Summary:   Multiple backend sync program
Provides:  kitchensync3
Provides:  kde3-kitchensync
Obsoletes: kdepim-kitchensync = %epoch:%version-%release
Provides:  kdepim-kitchensync = %epoch:%version-%release
Conflicts: kdenetwork-common < %epoch:3.5.7

%description kitchensync
kitchensync is a multiple backend sync program


%files kitchensync
%defattr(-,root,root,-)
%_kde3_bindir/kitchensync
%dir %_kde3_appsdir/kitchensync
%_kde3_appsdir/kitchensync/*
%_kde3_libdir/kde3/libkitchensyncpart.*
%_kde3_datadir/applications/kde/kitchensync.desktop
%_kde3_iconsdir/*/*/*/kitchensync*

#----------------------------------------------------------------------

%package wizards
Summary:   Kdepim groupware wizards 
Group:     Graphical desktop/KDE3
Conflicts: kdepim-common < 1:3.5.7-%mkrel 5
Conflicts: kdepim-kontact < 1:3.5.7-%mkrel 5
Obsoletes: kdepim-wizards = %epoch:%version-%release
Provides:  kdepim-wizards = %epoch:%version-%release

%description wizards
This kdepim groupware wizards. This package provides transition tool to setup
or migrate groupware
accounts from some common existing groupware solutions on market.

%files wizards
%defattr(-,root,root)
%_kde3_datadir/applications/kde/groupwarewizard.desktop
%_kde3_bindir/*wizard
%_kde3_libdir/kde3/*wizard.*

#----------------------------------------------------------------------

%package -n %lib_name-kitchensync
Summary:        Library for kitchensync program
Group:          Development/KDE and Qt
Provides:       %lib_name_orig-kitchensync = %epoch:%version-%release
Obsoletes:      %lib_name_orig-kitchensync= %epoch:%version-%release

%description -n %lib_name-kitchensync
Library for kitchensync program


%files -n %lib_name-kitchensync
%defattr(-,root,root)
%_kde3_libdir/libkitchensync.so.*
%_kde3_libdir/libkitchensync.la

#----------------------------------------------------------------------

%package -n %lib_name-qopensync
Summary:    Librairy for qopensync program
Group:      Development/KDE and Qt
Provides:   %lib_name_orig-qopensync = %epoch:%version-%release
Obsoletes:  %lib_name_orig-qopensync= %epoch:%version-%release


%description -n %lib_name-qopensync
Qt backend for opensync library

%files -n %lib_name-qopensync
%defattr(-,root,root)
%_kde3_libdir/libqopensync.so.*
%_kde3_libdir/libqopensync.la

#----------------------------------------------------------------------

%package korn
Group:          Graphical desktop/KDE3
Summary:        Mail checker
Provides:       korn3
Provides:       kde3-korn
Provides:       kdepim-korn = %epoch:%version-%release
Obsoletes:      kdepim-korn = %epoch:%version-%release
Conflicts:      kdenetwork <= 3.1.92
Obsoletes:	kdenetwork-korn <= 3.1.3-22mdk
Requires:	kde3-kdepim-common = %epoch:%version-%release
Conflicts:      %name-kontact < %epoch:3.5.8-1

%description korn
A mail checker

%files korn
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/korn
%_kde3_bindir/korn             
%_kde3_datadir/applications/kde/KOrn.desktop
%_kde3_appsdir/kconf_update/korn-*
%_kde3_libdir/kconf_update_bin/korn-3-4-config_change
%_kde3_iconsdir/*/*/*/korn*

#----------------------------------------------------------------------

%package kandy
Group:          Graphical desktop/KDE3
Summary:        A mobile simple sync tool
Provides:       kandy3
Provides:       kde3-kandy
Provides:       kdepim-kandy = %epoch:%version-%release
Obsoletes:      kdepim-kandy = %epoch:%version-%release
Requires:	kde3-kdepim-common = %epoch:%version-%release

%description kandy
A mobile simple sync tool

%files kandy
%defattr(-,root,root,-)
%_kde3_bindir/kandy
%_kde3_bindir/kandy_client
%doc %_kde3_docdir/HTML/en/kandy
%_kde3_datadir/applications/kde/kandy.desktop
%dir %_kde3_appsdir/kandy/
%_kde3_appsdir/kandy/*
%_kde3_datadir/applnk/Utilities/kandy.desktop

#----------------------------------------------------------------------

%package akregator
Group:          Graphical desktop/KDE3
Summary:        KDE RSS aggregator with great look and feel
Provides:       akregator3
Provides:       kde3-akregator
Provides:       kdepim-akregator = %epoch:%version-%release
Obsoletes:      kdepim-akregator = %epoch:%version-%release
Obsoletes:	akregator <= 1.0.2
Obsoletes:      %lib_name-akregator < 1:3.5.9
Requires:	kde3-kdepim-common = %epoch:%version-%release
Conflicts: 	kdepim-devel < 1:3.5.7-9mdv
Conflicts:      %name-kontact < %epoch:3.5.8-1

%description akregator
aKregator is KDE RSS aggregator with great look and feel.


%files akregator
%defattr(-,root,root,0755)
%_kde3_bindir/akregator
%_kde3_bindir/kontact-akregator.sh
%_kde3_libdir/kde3/libakregator*
%_kde3_libdir/libakregatorprivate.*
%_kde3_datadir/services/kontact/akregatorplugin.desktop
%_kde3_datadir/applications/kde/akregator.desktop
%dir %_kde3_appsdir/akregator
%_kde3_appsdir/akregator/*
%_kde3_iconsdir/*/*/*/rss_tag*
%_kde3_iconsdir/*/*/*/akregator*
%_kde3_datadir/services/akregator_part.desktop   
%_kde3_datadir/services/feed.protocol
%_kde3_datadir/services/kontact/akregatorplugin3.2.desktop
%doc %_kde3_docdir/HTML/en/akregator
%_kde3_datadir/services/akregator_mk4storage_plugin.desktop
%_kde3_datadir/servicetypes/akregator_plugin.desktop

#----------------------------------------------------------------------

%package   devel
Summary:   Devel stuff for kdepim
Group:     Development/KDE and Qt
Provides:  kdepim-devel = %epoch:%version-%release
Obsoletes: kdepim-devel = %epoch:%version-%release
Obsoletes: %lib_name-common-devel < 1:3.5.9
Obsoletes: %lib_name-kmail-devel < 1:3.5.9
Obsoletes: %lib_name-devel < 1:3.5.9
Obsoletes: %lib_name-ktnef-devel < 1:3.5.9
Obsoletes: %lib_name-akregator-devel < 1:3.5.9
Obsoletes: %lib_name-kontact-devel < 1:3.5.9
Obsoletes: %lib_name-kpilot-devel < 1:3.5.9
Obsoletes: %lib_name-kaddressbook-devel < 1:3.5.9
Obsoletes: %lib_name-korganizer-devel < 1:3.5.9
Provides:  %lib_name-devel = %epoch:%version-%release
Requires:  %lib_name-common = %epoch:%version-%release
Requires:  %lib_name-ktnef = %epoch:%version-%release
Requires:  %lib_name-kitchensync = %epoch:%version-%release 
Requires:  %lib_name-qopensync = %epoch:%version-%release 
Requires:  %lib_name-kontact = %epoch:%version-%release
Requires:  %lib_name-kpilot = %epoch:%version-%release
Requires:  %lib_name-kaddressbook = %epoch:%version-%release
Requires:  %lib_name-korganizer = %epoch:%version-%release
Conflicts: kdepim-common < 1:3.5.7-%mkrel 15


%description devel
This package contains header files needed if you wish to build applications
based on kdepim.

%files devel
%defattr(-,root,root)
%_kde3_libdir/kde3/plugins/designer/*
%_kde3_includedir/*
%_kde3_libdir/*.so
%exclude %_kde3_libdir/libakregatorprivate.so
%exclude %_kde3_libdir/libkmailprivate.so

#----------------------------------------------------------------------
%if %compile_apidox

%package    devel-doc
Group:      Development/KDE and Qt
Summary:    Development documentation for %name
Requires:   qt3-doc
Requires:   kde3-kdelibs-devel-doc
Obsoletes:  %{lib_name}-common-devel < 1:3.5.7

%description devel-doc
This packages contains all development documentation for kdelibs

%files devel-doc
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/kdepim-%version-apidocs
%endif

#----------------------------------------------------------------------

%package -n %lib_name-common
Summary:	Library for kdepim
Group:		Development/KDE and Qt
Obsoletes:      %lib_name-common-devel < 1:3.5.9
Conflicts:	kdepim <= 1:3.1-17mdk
Conflicts:      libkdenetwork2-common <= 1:3.1.3-37mdk
Conflicts:	kdenetwork <= 1:3.1-31mdk
Conflicts:	%lib_name-kaddressbook <= 1:3.5.3-5mdk
Provides:	%lib_name = %epoch:%version-%release
Provides:       %lib_name_orig-common= %epoch:%version-%release
Obsoletes:      %lib_name_orig-common= %epoch:%version-%release
Obsoletes:	%lib_name <= 3.1-17mdk
Conflicts:      %name-kontact < 3.5.7-4

%description -n %lib_name-common
This package contains header files needed if you wish to build applications
based on kdepim.


%files -n %lib_name-common
%defattr(-,root,root)
%_kde3_libdir/libkcal.la
%_kde3_libdir/libkdepim.la
%_kde3_libdir/libkgantt.la
%_kde3_libdir/libkpimexchange.la
%_kde3_libdir/libkmime.la
%_kde3_libdir/libkmime.so.*
%_kde3_libdir/libkcalkolab.la
%_kde3_libdir/libkcalkolab.so.*
%_kde3_libdir/libkcalscalix.la
%_kde3_libdir/libkcalscalix.so.*
%_kde3_libdir/libkgroupwarebase.la
%_kde3_libdir/libkgroupwarebase.so.*
%_kde3_libdir/libkgroupwaredav.la
%_kde3_libdir/libkgroupwaredav.so.*
%_kde3_libdir/libkpgp.la
%_kde3_libdir/libkpgp.so.*
%_kde3_libdir/libknoteskolab.la
%_kde3_libdir/libknoteskolab.so.*
%_kde3_libdir/libknotesscalix.la
%_kde3_libdir/libknotesscalix.so.*
%_kde3_libdir/libkcal.so.*
%_kde3_libdir/libkdepim.so.*
%_kde3_libdir/libkgantt.so.*
%_kde3_libdir/libkpimexchange.so.*
%_kde3_libdir/libkholidays.la
%_kde3_libdir/libkholidays.so.*
%_kde3_libdir/libksieve.la
%_kde3_libdir/libksieve.so.*
%_kde3_libdir/libmimelib.la
%_kde3_libdir/libmimelib.so.*
%_kde3_libdir/libkode.la
%_kde3_libdir/libkode.so.*
%_kde3_libdir/libkocorehelper.la
%_kde3_libdir/libkocorehelper.so.*
%_kde3_libdir/libgpgme++.la
%_kde3_libdir/libgpgme++.so.*
%_kde3_libdir/libkcal_*.la
%_kde3_libdir/libkcal_*.so.*
%_kde3_libdir/libkleopatra.la
%_kde3_libdir/libkleopatra.so.*
%_kde3_libdir/libknotes_xmlrpc.la
%_kde3_libdir/libknotes_xmlrpc.so.*
%_kde3_libdir/libkorganizer_calendar.la
%_kde3_libdir/libkorganizer_calendar.so.*
%_kde3_libdir/libkpimidentities.la
%_kde3_libdir/libkpimidentities.so.*
%_kde3_libdir/libkslox.la
%_kde3_libdir/libkslox.so.*
%_kde3_libdir/libqgpgme.la
%_kde3_libdir/libqgpgme.so.*

#----------------------------------------------------------------------

%package kmail
Group:      Graphical desktop/KDE3
Summary:    KDE Mailer
Requires:   kdepim-common = %epoch:%version-%release
Provides:   kmail3
Provides:   kde3-kmail
Provides:   kdepim-kmail = %epoch:%version-%release
Obsoletes:  kdepim-kmail = %epoch:%version-%release
Requires:   indexhtml >= 10.0-6mdk
Requires:   kdebase-common
Requires:   pinentry-qt
Obsoletes:  kdenetwork-kmail <= %epoch:3.1.3-37mdk
Obsoletes:  %lib_name-kmail <= 1:3.5.3
Obsoletes:  %lib_name-kmail-devel < 1:3.5.9
Conflicts:  kdenetwork <= 3.1.92
Conflicts:  kdepim-devel < 1:3.5.7-9mdv
Conflicts:  %name-kontact < %epoch:3.5.8-1
Requires:   %lib_name-index >= %epoch:%version-%release

%description -n kde3-kdepim-kmail
KDE Mailer


%files kmail
%defattr(-,root,root,-)
%_kde3_bindir/kmail            
%_kde3_bindir/kmailcvt         
%_kde3_bindir/kontact-kmail.sh
%_kde3_bindir/kmail_antivir.sh
%_kde3_bindir/kmail_clamav.sh
%_kde3_bindir/kmail_fprot.sh
%_kde3_bindir/kmail_sav.sh
%_kde3_bindir/indexlib-config
%multiarch %_kde3_bindir/*/indexlib-config
%_kde3_libdir/kde3/kcm_kmail.*
%_kde3_libdir/kde3/kcm_kmailsummary.*
%_kde3_libdir/libkmailprivate.*
%_kde3_libdir/kde3/libkmailpart.*
%_kde3_libdir/kde3/libkmail_*
%_kde3_datadir/services/kcmkmailsummary.desktop
%_kde3_datadir/services/kmail_*
%_kde3_datadir/services/kontact/kmailplugin.desktop
%_kde3_appsdir/kconf_update/kmail*
%_kde3_datadir/applications/kde/KMail.desktop
%_kde3_iconsdir/*/*/*/gpg*
%_kde3_iconsdir/*/*/*/kmail*
%dir %_kde3_appsdir/kmail
%_kde3_appsdir/kmail/*
%_kde3_datadir/config/kmail.antivirusrc
%_kde3_datadir/applnk/Utilities/kmailcvt.desktop
%_kde3_datadir/applications/kde/kmail_view.desktop
%_kde3_datadir/config/kmail.antispamrc
%_kde3_appsdir/kconf_update/upgrade-signature.pl
%_kde3_appsdir/kconf_update/upgrade-transport.pl
%doc %_kde3_docdir/HTML/en/kmail
%dir %_kde3_appsdir/kmailcvt/
%_kde3_appsdir/kmailcvt/*
%_kde3_datadir/servicetypes/dcopmail.desktop

#----------------------------------------------------------------------

%package -n %lib_name-index
Group:          Development/KDE and Qt
Summary:        Library for kmail
Obsoletes:      %lib_name_orig-index = %epoch:%version
Obsoletes:      %lib_name-kmail < 1:3.5.9
Conflicts:	kdepim-common <= 1:3.5.3-5mdv2007
Conflicts:	kdepim-kmail <= 1:3.5.3-5mdv2007

%description -n %lib_name-index
Library for kmail


%files -n %lib_name-index
%defattr(-,root,root,-)
%_kde3_libdir/libindex.so.*
%_kde3_libdir/libindex.la

#----------------------------------------------------------------------

%package knode
Group:          Graphical desktop/KDE3
Summary:        KDE News Reader
Requires:       kde3-kdepim-common = %epoch:%version-%release
Provides:	kde3-knode
Provides:	knode3
Obsoletes:      kdepim-knode = %epoch:%version-%release
Provides:       kdepim-knode = %epoch:%version-%release
Conflicts:      kdenetwork <= 1:3.1.92
Obsoletes:      kdenetwork-knode <= 1:3.1.3-37mdk
Obsoletes:	%{lib_name}-knode < 1:3.5.9
Obsoletes:	%{lib_name}-knode-devel < 1:3.5.9
Conflicts: 	kdepim-devel < 1:3.5.7-9mdv
Conflicts:      %name-kontact < %epoch:3.5.8-1

%description knode
KDE News Reader.


%files knode
%defattr(-,root,root,-)
%_kde3_bindir/knode            
%_kde3_bindir/kontact-knode.sh
%_kde3_libdir/kde3/libknodepart.*
%_kde3_datadir/services/knewsservice.protocol
%_kde3_datadir/services/kontact/knodeplugin.desktop
%_kde3_datadir/services/kontact/newstickerplugin.desktop
%_kde3_datadir/applications/kde/KNode.desktop
%_kde3_iconsdir/*/*/*/knode*
%doc %_kde3_docdir/HTML/en/knode/*
%dir %_kde3_appsdir/knode
%_kde3_appsdir/knode/*
%_kde3_datadir/services/knode_*
%_kde3_libdir/kde3/kcm_knode.*
%_kde3_libdir/libknodecommon.so.*
%_kde3_libdir/libknodecommon.la

#----------------------------------------------------------------------

%package karm
Summary:	Karm program
Group:		Graphical desktop/KDE3
Provides:	karm3
Provides:	kde3-karm
Obsoletes:      kdepim-karm = %epoch:%version-%release
Provides:       kdepim-karm = %epoch:%version-%release
Conflicts:	kdepim <= 1:3.1-17mdk
Conflicts:      %name-kontact < %epoch:3.5.8-1

%description karm
Time tracker.


%files karm
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/karm
%_kde3_bindir/karm
%_kde3_datadir/applnk/Utilities/karm.desktop
%_kde3_datadir/services/karm_part.desktop
%_kde3_datadir/services/kontact/karmplugin.desktop
%_kde3_iconsdir/*/*/*/karm*
%_kde3_libdir/kde3/libkarmpart.*
%dir %_kde3_appsdir/karm/
%_kde3_appsdir/karm/*
%_kde3_datadir/applications/kde/karm.desktop
%dir %_kde3_appsdir/karmpart
%_kde3_appsdir/karmpart/*

#----------------------------------------------------------------------

%package ktnef
Summary:        Ktnef program
Group:          Graphical desktop/KDE3
Provides:       kde3-ktnef
Provides:       ktnef3
Obsoletes:      kdepim-ktnef = %epoch:%version-%release
Provides:       kdepim-ktnef = %epoch:%version-%release
Conflicts:      kdepim <= 1:3.1-17mdk
Requires:       %lib_name-ktnef >= %epoch:%version-%release

%description ktnef
Ktnef.


%files ktnef
%defattr(-,root,root,-)
%_kde3_bindir/ktnef
%dir %_kde3_appsdir/ktnef/
%_kde3_appsdir/ktnef/*
%_kde3_iconsdir/*/*/*/ktnef*
%doc %_kde3_docdir/HTML/en/ktnef/*
%_kde3_datadir/applications/kde/ktnef.desktop
%_kde3_datadir/mimelnk/application/ms-tnef.desktop

#----------------------------------------------------------------------

%package -n %lib_name-ktnef
Summary:        Library for Ktnef program
Group:          Development/KDE and Qt
Provides:       %lib_name_orig-ktnef= %epoch:%version-%release
Obsoletes:      %lib_name_orig-ktnef= %epoch:%version-%release
Obsoletes:      %lib_name-ktnef-devel < 1:3.5.9
Conflicts:      kdepim <= 1:3.1-17mdk
Conflicts:	%lib_name-common <= %epoch:3.3.1-21mdk

%description -n %lib_name-ktnef
Library for Ktnef.


%files -n %lib_name-ktnef
%defattr(-,root,root,-)
%_kde3_libdir/libktnef.la
%_kde3_libdir/libktnef.so.*

#----------------------------------------------------------------------

%package knotes
Group:		Graphical desktop/KDE3
Summary:	A color configurable tooltip notes application for desktop
Provides:       knotes3
Provides:       kde3-knotes
Obsoletes:      kdepim-knotes = %epoch:%version-%release
Provides:       kdepim-knotes = %epoch:%version-%release
Conflicts:	kdepim <= 1:3.1-17mdk
Conflicts:      %name-kontact < %epoch:3.5.8-1

%description knotes
A color configurable tooltip notes application for desktop


%files knotes
%defattr(-,root,root)
%_kde3_bindir/knotes
%_kde3_bindir/kontact-knotes.sh
%doc %_kde3_docdir/HTML/en/knotes
%dir %_kde3_appsdir/knotes/
%_kde3_appsdir/knotes/*
%_kde3_libdir/kde3/knotes_*
%_kde3_iconsdir/*/*/*/knotes*
%_kde3_datadir/applications/kde/knotes.desktop
%_kde3_datadir/services/kresources/knotes/kolabresource.desktop
%_kde3_datadir/services/kresources/knotes_manager.desktop
%_kde3_datadir/services/kontact/knotesplugin.desktop

#----------------------------------------------------------------------

%package kaddressbook
Summary:	Kaddressbook program
Group:		Graphical desktop/KDE3
Provides:       kaddressbook3
Provides:       kde3-kaddressbook
Obsoletes:      kdepim-kaddressbook = %epoch:%version-%release
Provides:       kdepim-kaddressbook = %epoch:%version-%release
Requires:       %lib_name-kaddressbook >= %epoch:%version-%release
Conflicts:      %name-kontact < %epoch:3.5.8-1
Conflicts:      %name-common < %epoch:3.5.8-2

%description kaddressbook
The KDE addressbook application.


%files kaddressbook
%defattr(-,root,root)
%_kde3_bindir/kaddressbook
%_kde3_bindir/kabc2mutt
%doc %_kde3_docdir/HTML/en/kaddressbook
%dir %_kde3_appsdir/kaddressbook
%_kde3_appsdir/kaddressbook/*
%_kde3_iconsdir/*/*/*/kaddressbook*
%_kde3_bindir/kontact-addressbook.sh
%_kde3_datadir/applications/kde/kaddressbook.desktop
%_kde3_datadir/services/kfile_ics.desktop
%_kde3_datadir/services/kfile_vcf.desktop
%_kde3_libdir/kde3/kabc_*
%_kde3_libdir/kde3/kfile_vcf.*
%_kde3_libdir/kde3/kfile_ics.*
%_kde3_libdir/kde3/libkaddressbookpart.*
%_kde3_libdir/kde3/kcm_kabconfig.*
%_kde3_libdir/kde3/kcm_kabldapconfig.*
%_kde3_libdir/kde3/libkaddrbk_*.*
%_kde3_libdir/kde3/ldifvcardthumbnail.*
%_kde3_libdir/kde3/kcm_kabcustomfields.*
%dir %_kde3_datadir/services/kaddressbook/
%_kde3_datadir/services/kaddressbook/*
%_kde3_datadir/services/kabconfig.desktop
%_kde3_datadir/services/kabldapconfig.desktop
%_kde3_datadir/services/ldifvcardthumbnail.desktop
%_kde3_datadir/servicetypes/dcopaddressbook.desktop
%_kde3_datadir/servicetypes/kaddressbook_*
%_kde3_datadir/services/kontact/kaddressbookplugin.desktop
%_kde3_datadir/services/kabcustomfields.desktop
%dir %_kde3_datadir/services/kresources/kabc/
%_kde3_datadir/services/kresources/kabc/*
%_kde3_bindir/kabcdistlistupdater
%_kde3_datadir/autostart/kabcdistlistupdater.desktop

#----------------------------------------------------------------------

%define libgwsoap %mklibname gwsoap 0

%package -n %libgwsoap
Summary: Kdepim library
Group: System/Libraries

%description  -n %libgwsoap
Library file for kdepim.


%files -n %libgwsoap
%defattr(-,root,root)
%_kde3_libdir/libgwsoap.so.*
%_kde3_libdir/libgwsoap.la

#----------------------------------------------------------------------

%package -n %lib_name-kaddressbook
Summary:    Library file for Kaddressbook
Group:      Development/KDE and Qt
Provides:   %lib_name_orig-kaddressbook = %epoch:%version-%release
Obsoletes:  %lib_name_orig-kaddressbook = %epoch:%version-%release
Obsoletes:  %lib_name-kaddressbook-devel < 1:3.5.9

%description  -n %lib_name-kaddressbook
Library file for kaddressbook


%files -n %lib_name-kaddressbook
%defattr(-,root,root)
%_kde3_libdir/libkaddressbook.la
%_kde3_libdir/libkaddressbook.so.*
%_kde3_libdir/libkabinterfaces.so.*
%_kde3_libdir/libkabinterfaces.la
%_kde3_libdir/libkabc*.la
%_kde3_libdir/libkabc*.so.*

#----------------------------------------------------------------------

%package korganizer
Summary:	Korganizer program
Group:		Graphical desktop/KDE3
Provides:       korganizer3
Provides:       kde3-korganizer
Provides:       kalarm3
Provides:       kde3-kalarm
Obsoletes:      kdepim-korganizer = %epoch:%version-%release
Provides:       kdepim-korganizer = %epoch:%version-%release
Requires:       kde3-kdepim-common = %epoch:%version-%release
Requires:       %lib_name-korganizer >= %epoch:%version-%release
Conflicts:      %name-kontact < %epoch:3.5.8-1

%description korganizer
A calendar-of-events and todo-list manager.


%files korganizer
%defattr(-,root,root)
%_kde3_bindir/kalarm
%_kde3_bindir/kalarmd
%_kde3_bindir/konsolekalendar
%_kde3_bindir/korgac
%_kde3_bindir/korganizer
%_kde3_bindir/kontact-korganizer.sh
%_kde3_bindir/ical2vcal
%_kde3_appsdir/kconf_update/korganizer.upd
%dir %_kde3_appsdir/korganizer
%_kde3_appsdir/korganizer/*
%dir %_kde3_appsdir/kalarm/
%_kde3_appsdir/kalarm/*
%dir %_kde3_appsdir/libkholidays/
%_kde3_appsdir/libkholidays/*
%_kde3_datadir/autostart/kalarm.tray.desktop
%_kde3_datadir/autostart/kalarmd.autostart.desktop
%_kde3_datadir/autostart/korgac.desktop
%_kde3_libdir/kde3/libkorg_*
%_kde3_libdir/kde3/kcm_korganizer.*
%_kde3_libdir/kde3/libkorganizerpart.*
%_kde3_datadir/applications/kde/kalarm.desktop
%_kde3_datadir/applications/kde/korganizer.desktop
%_kde3_iconsdir/*/*/*/kalarm*
%doc %_kde3_docdir/HTML/en/korganizer/*
%doc %_kde3_docdir/HTML/en/konsolekalendar/*
%doc %_kde3_docdir/HTML/en/kalarm
%_kde3_datadir/services/korganizer_*
%dir %_kde3_datadir/services/korganizer/
%_kde3_datadir/services/korganizer/*
%dir %_kde3_datadir/services/webcal.protocol
%_kde3_datadir/servicetypes/calendardecoration.desktop
%_kde3_datadir/servicetypes/calendarplugin.desktop
%_kde3_datadir/servicetypes/korganizerpart.desktop
%_kde3_datadir/services/kontact/korganizerplugin.desktop
%_kde3_datadir/services/kontact/journalplugin.desktop
%_kde3_datadir/services/kontact/todoplugin.desktop

#----------------------------------------------------------------------

%package -n %lib_name-korganizer
Summary:    Librairy for korganizer program
Group:      Development/KDE and Qt
Obsoletes:  %lib_name-korganizer-devel < 1:3.5.9
Provides:   %lib_name_orig-korganizer = %epoch:%version-%release
Obsoletes:  %lib_name_orig-korganizer = %epoch:%version-%release

%description -n %lib_name-korganizer
Librairy for korganizer program


%files -n %lib_name-korganizer
%defattr(-,root,root)
%_kde3_libdir/libkorganizer.la
%_kde3_libdir/libkorganizer.so.*
%_kde3_libdir/libkorganizer_eventviewer.la
%_kde3_libdir/libkorganizer_eventviewer.so.*
%_kde3_libdir/libkorg_stdprinting.la
%_kde3_libdir/libkorg_stdprinting.so.*

#----------------------------------------------------------------------

%package kpilot
Summary:        Kpilot program
Group:          Graphical desktop/KDE3
Requires:       %lib_name-kpilot >= %epoch:%version-%release
Provides:       kpilot3
Provides:       kde3-kpilot
Obsoletes:      kdepim-kpilot = %epoch:%version-%release
Provides:       kdepim-kpilot = %epoch:%version-%release
Conflicts:	%name-common <= %epoch:3.4.2-6mdk
Conflicts:      %name-kontact < %epoch:3.5.8-1

%description kpilot
To sync with your PalmPilot
Sync phone book entries between your palmtop and computer

%post kpilot 
%if %mdkversion < 200900
%update_menus
%endif
update-alternatives --install %_sysconfdir/dynamic/launchers/visor/kde.desktop visor.kde.dynamic %_sysconfdir/dynamic/launchers/visor/kpilot.desktop 30

%postun kpilot
%if %mdkversion < 200900
%clean_menus
%endif
if [ $1 = 0 ] ; then
	update-alternatives --remove visor.kde.dynamic %_sysconfdir/dynamic/launchers/visor/kpilot.desktop
fi

%files kpilot
%defattr(-,root,root)
%dir %_sysconfdir/dynamic/
%dir %_sysconfdir/dynamic/launchers/
%dir %_sysconfdir/dynamic/launchers/visor/
%config(noreplace) %_sysconfdir/dynamic/launchers/visor/kpilot.desktop
%_kde3_bindir/kpalmdoc
%_kde3_bindir/kpilot
%_kde3_bindir/kpilotDaemon
%_kde3_iconsdir/*/*/*/kpalmdoc*
%_kde3_iconsdir/*/*/*/kpilot*
%_kde3_libdir/kde3/kcm_kpilot.*
%_kde3_libdir/kde3/conduit_*
%_kde3_libdir/kde3/kfile_palm.*
%_kde3_datadir/services/kfile_palm.desktop
%_kde3_datadir/services/kpilot_config.desktop
%_kde3_datadir/services/*conduit.desktop
%_kde3_datadir/services/kontact/kpilotplugin.desktop
%_kde3_appsdir/kconf_update/kpilot.upd
%_kde3_datadir/applications/kde/kpalmdoc.desktop
%_kde3_appsdir/kconf_update/kpalmdoc.upd
%dir %_kde3_appsdir/kpilot
%_kde3_appsdir/kpilot/*
%_kde3_datadir/servicetypes/*conduit.desktop
%doc %_kde3_docdir/HTML/en/kpilot
%_kde3_datadir/applications/kde/kpilotdaemon.desktop
%_kde3_datadir/applications/kde/kpilot.desktop

#----------------------------------------------------------------------

%package -n %lib_name-kpilot
Summary:        Librairy for kpilot program
Group:          Development/KDE and Qt
Obsoletes:      %lib_name-kpilot-devel < 1:3.5.9
Provides:	%lib_name_orig-kpilot = %epoch:%version-%release
Obsoletes:      %lib_name_orig-kpilot = %epoch:%version-%release
Requires:	%lib_name-common = %epoch:%version-%release


%description -n %lib_name-kpilot
Librairy for kpilot program

%files -n %lib_name-kpilot
%defattr(-,root,root)
%_kde3_libdir/libkpilot.so.*
%_kde3_libdir/libkpilot.la

#----------------------------------------------------------------------

%package kontact
Summary:   Kontact program
Group:     Graphical desktop/KDE3
Provides:  kontact3
Provides:  kde3-kontact
Obsoletes: kdepim-kontact = %epoch:%version-%release
Provides:  kdepim-kontact = %epoch:%version-%release
Suggests:  kde3-kdepim-kmail = %epoch:%version-%release
Suggests:  kde3-kdepim-knotes = %epoch:%version-%release
Suggests:  kde3-kdepim-kaddressbook = %epoch:%version-%release
Suggests:  kde3-kdepim-knode = %epoch:%version-%release
Suggests:  kde3-kdepim-korganizer = %epoch:%version-%release
Suggests:  kde3-kdepim-akregator = %epoch:%version-%release
Requires:  %lib_name-kontact >= %epoch:%version-%release
Conflicts: kdeaddons <= 3.2.3-15mdk
Conflicts: kdepim-common <= 1:3.5.8-4mdv2008.1

%description kontact
KDE Kontact, an integrated personal information suite container application for
KDE.


%files kontact
%defattr(-,root,root)
%_kde3_bindir/kontact
%dir %_kde3_datadir/services/kontact/
%_kde3_datadir/services/kontact/*
%_kde3_datadir/services/kontactconfig.desktop
%_kde3_datadir/applications/kde/Kontact.desktop
%_kde3_datadir/applications/kde/kontactdcop.desktop
%dir %_kde3_appsdir/kontact/
%_kde3_appsdir/kontact/*
%_kde3_datadir/services/kcmkontactsummary.desktop
%dir %_kde3_appsdir/kontactsummary/
%_kde3_appsdir/kontactsummary/*
%_kde3_libdir/kde3/libkontact*
%_kde3_libdir/kde3/kcm_kontact*
%_kde3_datadir/servicetypes/kontactplugin.desktop
%_kde3_datadir/services/kcmkontactknt.desktop
%_kde3_iconsdir/*/*/*/kontact*
%doc %_kde3_docdir/HTML/en/kontact/*

%exclude %_kde3_datadir/services/kontact/akregatorplugin.desktop
%exclude %_kde3_datadir/services/kontact/akregatorplugin3.2.desktop
%exclude %_kde3_datadir/services/kontact/journalplugin.desktop
%exclude %_kde3_datadir/services/kontact/kaddressbookplugin.desktop
%exclude %_kde3_datadir/services/kontact/karmplugin.desktop
%exclude %_kde3_datadir/services/kontact/kmailplugin.desktop
%exclude %_kde3_datadir/services/kontact/knodeplugin.desktop
%exclude %_kde3_datadir/services/kontact/knotesplugin.desktop
%exclude %_kde3_datadir/services/kontact/korganizerplugin.desktop
%exclude %_kde3_datadir/services/kontact/newstickerplugin.desktop
%exclude %_kde3_datadir/services/kontact/todoplugin.desktop
%exclude %_kde3_datadir/services/kontact/kpilotplugin.desktop

#----------------------------------------------------------------------

%package -n %lib_name-kontact
Summary:        Librairy for kontact program
Group:          Development/KDE and Qt
Obsoletes:      %lib_name-kontact-devel < 1:3.5.9
Provides:	%lib_name_orig-kontact = %epoch:%version-%release
Obsoletes:      %lib_name_orig-kontact = %epoch:%version-%release
Conflicts:	%lib_name_akregator <= 1.0.2


%description -n %lib_name-kontact
Librairy for kontact program

%files -n %lib_name-kontact
%defattr(-,root,root)
%_kde3_libdir/libkontact.la
%_kde3_libdir/libkontact.so.*
%_kde3_libdir/libkpinterfaces.so.*
%_kde3_libdir/libkpinterfaces.la

#----------------------------------------------------------------------

%prep
%setup -q -n kdepim-%{version}
%patch1 -p1 -b .fix_dimap_speed
%patch2 -p1 -b .fix_use_point_kmail
%patch3 -p1 -b .disable_knode_first_start
#%patch4 -p0 -b .fix_add_resource_to_kaddressbook
%patch5 -p1 -b .fix_kalarm_call_twice_dialog
%patch7 -p1 -b .korganizer_use_sys_timezone
%patch9 -p1 -b .hide_help
%patch11 -p0 -b .knode_sideband
%patch12 -p1 -b .kitchensync_synce
%patch13 -p1 -b .kitchensync_barry
%patch14 -p1 -b .fix_underlinking
%patch15 -p1 
#%patch16 -p1
%if %mdkversion >= 201000
%patch17 -p1
#%patch18 -p1
%endif
%patch19 -p0
%patch20 -p0

install -m 0644 %{SOURCE7} kitchensync/src/configguibarry.cpp
install -m 0644 %{SOURCE8} kitchensync/src/configguibarry.h

%build
export QTDIR=%qt3dir
export KDEDIR=%_kde3_prefix

# Post patches need regenerate build
export xdg_menudir=%_sysconfdir/xdg/kde/menus
make -f admin/Makefile.common cvs

PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/

%configure_kde3 \
	--enable-newdistrlists \
%if %use_enable_indexlib    
	--enable-indexlib \
%endif
	--enable-pie

%make
%if %compile_apidox
make apidox
%endif



%install
rm -fr %buildroot
export PATH=%_kde3_bindir:$PATH

make install DESTDIR=%buildroot

%define launchers %_sysconfdir/dynamic/launchers/visor
mkdir -p %buildroot%launchers
cat > %buildroot%launchers/kpilot.desktop << EOF
[Desktop Entry]
Name=Kpilot \$devicename
Comment=PalmPilot Tool
Exec=%_kde3_bindir/kpilot
Terminal=false
Icon=kpilot
Type=Application
EOF

install -m 0755 %SOURCE1 %buildroot/%_kde3_bindir/kontact-addressbook.sh
install -m 0755 %SOURCE2 %buildroot/%_kde3_bindir/kontact-knotes.sh
install -m 0755 %SOURCE3 %buildroot/%_kde3_bindir/kontact-kmail.sh
install -m 0755 %SOURCE4 %buildroot/%_kde3_bindir/kontact-korganizer.sh
install -m 0755 %SOURCE5 %buildroot/%_kde3_bindir/kontact-knode.sh
install -m 0755 %SOURCE6 %buildroot/%_kde3_bindir/kontact-akregator.sh

install -d -m 0755 %buildroot/%_sysconfdir/xdg/menus/

%if %compile_apidox
make install-apidox DESTDIR=%buildroot/
%endif

%multiarch_binaries %buildroot/%_kde3_bindir/indexlib-config

%clean
rm -fr %buildroot



%changelog

* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-2mdv2010.2
+ fix libical0 dependency

* Thu Jul 21 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-1mdv2010.2
+ Update to Trinity 3.5.12 sources
+ Add kdebase-3.5.12-config.patch
+ Add kdebase-3.5.12-move-xdg-menu-dir.patch
- Remove fix autotools patch
+ Fix kdepim-3.4.0-use-point-kmail.patch
- Remove kdepim-3.5.3-kaddressbook-resources.patch
+ Fix kdepim-3.5.4-korganizer-use-sys-timezone.patch

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 1:3.5.10-3mdv2010.1
+ Rebuild for MDV 2010.1

* Fri Nov 13 2009 Tim Williams <tim@my-place.org.uk> 1:3.5.10-2mdv2010.0
+ Rebuild for MDV 2010.0
+ fix kdepim-3.5.3-kaddressbook-resources.patch
+ fix depim-3.5.9-kitchensync-handle-synce.patch
+ Add kdepim-3.5.10-gcc44.patch to fix gcc 4.4 problems
- Remove gcc44 patch

* Tue Aug 26 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-1mdv2009.0
+ Revision: 276426
- Update for probably the last upstream kdepim from kde3

* Fri Jul 04 2008 Danilo Cesar Lemes de Paula <danilo@mandriva.com> 1:3.5.9-16mdv2009.0
+ Revision: 231847
- Fixing Kdepim to start only with KDE

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Jun 10 2008 Adam Williamson <awilliamson@mandriva.com> 1:3.5.9-15mdv2009.0
+ Revision: 217318
- update handle-synce.patch to use blank configurator for old synce plugin:
  none of the configuration options work

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jun 07 2008 Anssi Hannula <anssi@mandriva.org> 1:3.5.9-14mdv2009.0
+ Revision: 216651
- fix underlinking issues (fix-underlinking.patch)

  + Adam Williamson <awilliamson@mandriva.com>
    - update kitchensync-handle-synce.patch with better descriptions for the two synce plugins

  + Funda Wang <fundawang@mandriva.org>
    - BR tcl-devel
    - rebuild for new qt3 libdir

* Mon May 19 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 1:3.5.9-11mdv2009.0
+ Revision: 208984
- Use versioned obsoletes

* Sun May 04 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-10mdv2009.0
+ Revision: 201063
- Moving for new path /opt/kde3
- Added all patches from branch using new "inpatch" log info

  + Adam Williamson <awilliamson@mandriva.com>
    - update copyright in configguibarry.cpp

* Wed Mar 19 2008 Adam Williamson <awilliamson@mandriva.com> 1:3.5.9-9mdv2008.1
+ Revision: 188758
- add configguibarry.cpp and configguibarry.h and update kitchensync-barry.patch: add a KitchenSync GUI configuration handler for barry-opensync (thanks to Helio Castro and Eduardo Habkost for writing most of the code)
- add kitchensync-barry.patch: recognize the Barry plugin (kitchensync)

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Use a better icon ( tks FACORAT Fabrice )
    - Add an icon for Kandy

* Fri Mar 14 2008 Adam Williamson <awilliamson@mandriva.com> 1:3.5.9-8mdv2008.1
+ Revision: 187737
- add kitchensync-handle-synce.patch: makes kitchensync handle synce's opensync plugin correctly (give it a name, use an icon, recognize it needs no configuration)
-This line, and following ones, will be ignored--
  file SPECS/kdepim.spec modified
  file SOURCES/kdepim-3.5.9-kitchensync-handle-synce.patch added

* Thu Mar 13 2008 Adam Williamson <awilliamson@mandriva.com> 1:3.5.9-7mdv2008.1
+ Revision: 187329
- drop the external source and spec handling for kitchensync opensync-0.3 branch as we're back on opensync 0.2 now

* Fri Mar 07 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-6mdv2008.1
+ Revision: 181270
- Commit 780164 on branch upstream KDE is creating corrupted attaches. Removing broken patch for now...

* Tue Mar 04 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-5mdv2008.1
+ Revision: 178492
- Multiple enterprose branch fixes merged back on stable branch

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] Allow Knode to be on the sidebar (Bug #31071)

* Mon Feb 18 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-4mdv2008.1
+ Revision: 171216
- Proper string test with isEmpty
- Body can be 0 in imap folder
- Avoid crash on imap folder parse
- Integrate kmail-avoid-crash-on-startup.diff patch from the openSUSE RPM

* Sun Feb 17 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-3mdv2008.1
+ Revision: 169528
- Fix patch 10
- Make desktop file patch back again

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-2mdv2008.1
+ Revision: 168834
- knodecommon now have their proper library/module separated. This change should fix some crying

* Thu Feb 14 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-1mdv2008.1
+ Revision: 168659
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches intregrated
- We're back to standard kdepim tarball, as enterprise is merged.
- Update kitchensync branch. ksync gone away

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-not-capitalized
    - fix description-line-too-long
    - fix 'error: for key "Icon" in group "Desktop Entry" is an icon name with an
      extension, but there should be no extension as described in the Icon Theme
      Specification if the value is not an absolute path'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 26 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.8-6mdv2008.1
+ Revision: 137852
- rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Fix menus (do not show them on Office section)

* Thu Nov 29 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.8-5mdv2008.1
+ Revision: 113920
- ksync comes back in enterprise branch
- scalix added
- Conflicts added for a strange dp in kdepim-common and kdepim-kontact
- Introducing enterprise branch
- Removing useless switches for kitchensync
- Fixing requires, otherwise would not compile on 2008.0. Now we're requiring only opensync >= 0.34 and
  possible backport need bring new opensync as well

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Fix menu desktop files

* Sun Nov 04 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.8-4mdv2008.1
+ Revision: 105785
- Rebuild against new libopensync

* Fri Nov 02 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-3mdv2008.1
+ Revision: 105285
- Fix Conflicts

* Fri Nov 02 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-2mdv2008.1
+ Revision: 105264
- Fix conflict

* Sun Oct 28 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-1mdv2008.1
+ Revision: 102754
- Fix File list. ( Bug #34209 )
- Removed upstream merged patches
  Rediffed patch0
- Kde 3.5.8
  Remove  upstream merged patches
  Comment patch that do not apply ( need to look deeply in them now )
  Start to allow to backport ( as opensyn 0.33 had been added as require ! )
- Removing Suggests on kontact package as this must be Requires

  + Funda Wang <fundawang@mandriva.org>
    - Update kitchensync opensync-0.3 branch

* Fri Oct 19 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.7-18mdv2008.1
+ Revision: 100464
- Update duplicate function patch
- Propose dirty but working patch to solve duplicate function defination
- BR opensync >= 0.33 in fact
- remove useless patch, as our new branch of kitchensync already contains it
- add kitchensync-OpenSync0.30API tarball
- Rebuild against latest libopensync

* Tue Oct 16 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:3.5.7-17mdv2008.1
+ Revision: 99033
- Remove kdepim-post-3.5.7-sieve-tls patch, it breaks managing of sieve
  scripts (#34353).

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-ended-with-dot

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] Change Requires into Suggests (Bug #34209)

* Sun Sep 30 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-16mdv2008.0
+ Revision: 94041
- Fix menu entry for KMail and Kontact

* Mon Sep 10 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-15mdv2008.0
+ Revision: 84159
- Added enterprise branch relevant patches
- Fix for kcfg issues in wizard

* Mon Aug 20 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-13mdv2008.0
+ Revision: 67953
- Added all kdepim related patches frm kde branch. Mostly fix coming from corporate branch

* Wed Jul 25 2007 Adam Williamson <awilliamson@mandriva.com> 1:3.5.7-12mdv2008.0
+ Revision: 55142
- disable libmal buildrequires (mal conduit is disabled upstream)

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] Fix Requires to ensuse good updates (bug #30341)

* Wed Jun 27 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-10mdv2008.0
+ Revision: 45226
- Add conflicts to the old kdepim-devel package (as it contains files that
  shouldn't be there)
- Remove some files that were wrongly listed in kdepim-devel

* Thu Jun 21 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-9mdv2008.0
+ Revision: 42341
- Do not show the "Help" button of the kmail wizard as there is no help on
  that (#28480)

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] Add Patch 116: Fix kmail cpu usage ( bug #31125)
    - Fix OnlyShowIn=KDE;

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 1:3.5.7-8mdv2008.0
+ Revision: 36179
- rebuild with correct optflags

* Tue Jun 05 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.7-6mdv2008.0
+ Revision: 35718
- Rebuild for package moving

* Fri May 25 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-5mdv2008.0
+ Revision: 31126
- Created package kdepim-wizards and added conflicts for old file owner ones. This solve a messy
  dependency chain. korganizer and other kontact components can be installed alone
- Removed some invalid and unecessary explicit requires
- Removed explicit version on kdepim requires
- Moved kcfg files for devel package
- Removed some unecessary ldconfig entries

* Thu May 24 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-4mdv2008.0
+ Revision: 30903
- Fix File list (#29454)
- patch8: Fix Menu entries
- Add BuildRequires

* Fri May 18 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-3mdv2008.0
+ Revision: 28324
- Fixed conflicts with old global common devel package and new doc-devel
- Minor update in official tarball from kde.org
- 3.5.7 release


* Fri Mar 30 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-9mdv2007.1
+ Revision: 149788
- Increase
- fix kaddressbook (fix update distribution list)

* Wed Mar 21 2007 Laurent Montel <lmontel@mandriva.com> 1:3.5.6-7mdv2007.1
+ Revision: 147240
- Fix crash with imap+wizard:bug found by Boubou
- Fix kmail crash

* Wed Mar 21 2007 Laurent Montel <lmontel@mandriva.com> 1:3.5.6-5mdv2007.1
+ Revision: 147138
- Fix kmail crash bug #113329

* Tue Mar 06 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.6-4mdv2007.1
+ Revision: 133904
- Added some patches coming from branch tree:
- Memory usage reduction ( commits 633777 633978 )
- Imap cache and parse speed up ( commits 633777 636466 )
- Imap cache crash ( commit 631934 )
- Quota feature, usual request from costumers ( commit 631698 )
- Removal of config storage of passwd ( commit 630633 )

  + Laurent Montel <lmontel@mandriva.com>
    - fix kmail bugs
    - Fix spec file
    - 3.5.6
    - Fix group

* Thu Jan 11 2007 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-5mdv2007.1
+ Revision: 107472
- Fix bug #28093

* Sat Dec 30 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-4mdv2007.1
+ Revision: 102858
- Fix korganizer mem leak
- Fix launch korganizer

* Tue Oct 17 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-2mdv2007.1
+ Revision: 65490
- Add tag packager
- As said on maintainer we use official tarball
  not a random snapshot
  If there is a critical crash add a patch to fix it.

  + Helio Chissini de Castro <helio@mandriva.com>
    - Missing icons on install
    - Back to use branch tarballs. Now using post 3.5.5

* Fri Sep 15 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-12mdv2007.0
+ Revision: 61390
- New package (2006-09-14 12mdv)
  Fix missing menu entry

* Thu Sep 14 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-11mdv2007.0
+ Revision: 61235
- New package (2006-09-13 11mdv)
  Korganizer needs kdepim-common (for icons/resources etc.)
- Fix buildrequires

* Thu Sep 07 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-10mdv2007.0
+ Revision: 60216
- New package (3.5.4-10mdv 2006/09/06)
  Rebuild against new libmal+pilot-link

* Sun Sep 03 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-9mdv2007.0
+ Revision: 59592
- New package (3.5.4-9mdv 2006/09/02)
  Fix kmail crash
- Fix akregator potential crash

* Thu Aug 31 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-8mdv2007.0
+ Revision: 58800
- New package (3.5.4-7mdv 2006-08-06)
  Fix crash in kmail

* Tue Aug 15 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-7mdv2007.0
+ Revision: 55959
- New package (2006/08/14 3.5.4-7mdv)
  Add other kmail fix

* Tue Aug 15 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-6mdv2007.0
+ Revision: 55871
- New package (2006/08/14 3.5.4-6mdv)
  Add a lot of kmail bugs fixes
- Fix korganizer crash

* Thu Aug 10 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-4mdv2007.0
+ Revision: 54652
- New package (2006/08/09 3.5.4-4mdv)
  Don't build by default --enable-indexlib too experimental

* Wed Aug 09 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-3mdv2007.0
+ Revision: 54380
- New package (2006/08/08 3.5.4-3mdv)
  Add patch to fix tabstop order in korganizer->freebusy (bug found by Nicolas Chipaux)

* Sat Aug 05 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-2mdv2007.0
+ Revision: 51723
- New version (2006/08/04 3.5.4-2mdv)
  Add patch to fix encode bad chars into xml in kresource/egrw

* Thu Aug 03 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-1mdv2007.0
+ Revision: 42978
- New Package 3.5.4-1mdv (2006/08/02)
- Fix launch kontact apps with new xdg menu
- Fix mini value
- fix spinbox value
- Fix focus into knewsticker
- Already add cancel button into dialog box
- Don't show text into sidebar by default
- Fix bug found by Nicolas Chipaux:
-> use system timezone
-> don't spam example.net all the time
- Add patch from jonas: fix kalarmd

  + Helio Chissini de Castro <helio@mandriva.com>
    - Added official 3.5.4 tarball
    - Removed already applied pop3 crash patch

* Tue Jul 25 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.3-11mdv2007.0
+ Revision: 41978
- Add patch to fix crash when we add resource to kaddressbook
  (thanks Nicolas Chipaux for bug report)
  I will add it into kde3.5 branch but too late for kde3.5.4

* Fri Jul 21 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.3-10mdv2007.0
+ Revision: 41689
- Disable debug

* Tue Jul 18 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.3-9mdv2007.0
+ Revision: 41411
- requires kde-custom-icons
- Readd requires on lib_name-common
  (otherwise I didn't understand how appli can be start)
- Add patch to fix some pop3 crash
- Patch206: initialize variable to avoid korganize crash (patch commited into kde3.5.4/kde4.0)
- Fix config empty trash
- Fix compile under x86_64
- Remove some old patch (patch from neoclust)
- Fix spec file
- 3.5.3
- Rebuild against new xorg
- Rebuild to create category
- Rebuild with new kdelibs/qt
  (remove BIC)
- Fix kmail crash
- Rebuild with new kdelibs
- Fix file list
- 3.5.2
  Clean spec file
  Fix bug #17182
  Fix bug #15569
- Update from branch
- 3.5.1
- Enable debug cooker only
  MDK 9.2 is obsolete now
- Diff from 3.5 branch
- Fix patch
- Fix: don't readd all the time first message
- Fix add separator in kmail->apply all filter menu
- Fix buildrequires
- Enable full indexing: BE CARREFULL experimental
- Fix buildrequires
- Enable two config option
- Rebuild for missing package
- fix spec file
- Real 3.5.0
- 3.5.0 (named rc1)
- Fix typo
  * Wed Nov 02 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.5-3mdk
- Rebuild with new mysql
  * Thu Oct 27 2005 Helio Chissini de Castro <helio@mandriva.com> 3.3.5-2mdk
- New immodule patch
- Fix install kontact-mdk icons
- Fix multiarch
- Fix file spec
- 3.4.2
- Rebuild
- Rebuild
- Rebuild
- Last sync
- Fix compile
- Fix spec file
- New sync to fix knode
- Fix kpilot file
- New sync
- Fix bug #16526
- New sync
- Fix other crash
- Fix crash when timer is null
- Fix kpilot crash when db doesn't exit
- Oops forgot to update release
- Disable knode first start => it blocks kontact at first launch and doesn't configure all kontact just knode
- Rebuild without debug
  Sync with svn
- Fix spec file
- Fix bug reported by Boiko
- Add script to launch akregator into kontact when kontact is already launched
- Fix compile apidoc with mdk <2006
- Fix compile apidoc
- 3.4.2
- Rebuild on x86_64
- Fix install on mdk <=2006
- Sync

  + Helio Chissini de Castro <helio@mandriva.com>
    - This define was commited by mistake
    - Clean and rearrange spec file
    - Added tarball from kde branch as discussed on meeting in 28/06
    - Removed rpath and added configure macro invalidating libtoolize
    - Added strip macro as stated by Nanar ( for unstable builds )
    - Removed bitmap files ( will be added in the upcoming mandriva-kde-icons package )
    - Remaining patches will be analised durong the configuration move
    - We are Mandriva now
    - Uploading package ./kdepim

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - Added a patch fixing a crash when using authenticated smtp. KDE Bug #101847

* Wed Jun 29 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.1-5mdk
- Adapt to add to svn

* Thu Jun 16 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.1-4mdk
- Update from SVN

* Tue Jun 14 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.1-3mdk
- Fix provides

* Thu Jun 09 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.1-2mdk
- Add requires on sasl plugin to fix authentification with imap

* Sat May 28 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.1-1mdk
- 3.4.1

* Tue May 24 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-11mdk
- Fix split

* Tue May 17 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-10mdk
- Sync with SVN

* Thu May 05 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-9mdk
- Rebuild with new GCC

* Wed May 04 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-8mdk
- Update from CVS

* Fri Apr 22 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-7mdk
- Add missing buildrequires found by Christiaan Welvaart <cjw@daneel.dyndns.org>

* Tue Apr 19 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-6mdk
- Reapply first message patch

* Tue Apr 19 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-5mdk
- Remove unused patch
- Reapply some patch (rediff from neoclust)

* Fri Apr 15 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-4mdk
- Update code from CVS
- Reactivate apidox
- Remove unused patch

* Wed Apr 13 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-3mdk
- Fix depend on devel package

* Mon Apr 11 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-2mdk
- Update code from CVS
- Reactive debug
- Use --enable-new-ldflags
- Change url
- Remove duplicate entry
- Clean patch from Neoclust <neoclust@mandrake.org>

* Thu Apr 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0

* Wed Mar 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-45mdk
- Rebuild for missing package

* Wed Mar 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-44mdk
- Add patch112: fix libkcal recurrence
- Add patch113: fix dimap speedup

* Tue Mar 08 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-43mdk
- Add requires on pinentry on kmail to fix encrypt mail

* Thu Mar 03 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-42mdk
- Add patch111: fix kmail don't empty trash

* Wed Mar 02 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-41mdk
- Add patch110: fix knode kde bug #100533

* Thu Feb 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-40mdk
- Add patch109: fix kmail kde bug #97274

* Wed Feb 23 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-39mdk
- Don't build with gpgme-devel (it's into contrib)

* Mon Feb 21 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-37mdk
- Add patch107: fix kontact kde bug #91676
- Add patch108: fix knode kde bug #93756

* Thu Feb 17 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-36mdk
- Add patch106: fix libical kde bug #94937

* Wed Feb 16 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-35mdk
- Add patch105: fix libkdepim kde bug #86292

* Sun Feb 13 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-34mdk
- Add patch104: fix kmail kde bug #98715

* Thu Feb 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-33mdk
- Add patch103: fix kpgp kde bug #92619
- Disable debug

* Wed Feb 09 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-32mdk
- Add patch102: fix kmail kde bug #56302

* Mon Feb 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-31mdk
- Sync with CVS (fix kalarm/kmail)

* Mon Jan 31 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-30mdk
- Add missing buildrequires.

* Fri Jan 28 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-29mdk
- Fix generate menu

* Thu Jan 27 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-28mdk
- Fix certmanager "Emit a DCOP signal when changing the gpgconf configuration data."

* Thu Jan 27 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-27mdk
- Add patch100: fix kmail encrypted mail

* Tue Jan 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-26mdk
- Rebuild for missing package

* Tue Jan 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-25mdk
- Add patch99: fix kmail header list empty

* Mon Jan 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-24mdk
- Add patch98: fix kmail kde bug #97692

* Mon Jan 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-23mdk
- Add patch97: fix kmail kde bug #84425

* Sat Jan 22 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-22mdk
- Rebuild against new readline asked by Per �yvind Karlsen

* Tue Jan 18 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-20mdk
- Add patch96: fix kontact dialog siez

* Mon Jan 17 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-19mdk
- Add patch95: fix kalarm spinbox + plastikstyle

* Mon Jan 17 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-18mdk
- Add patch94: fix korganizer mem leak

* Sat Jan 15 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-17mdk
- Add patch93: fix kmail kde bug #96722

* Fri Jan 14 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-16mdk
- Add patch92: Fix kde bug #96903

* Wed Jan 12 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-15mdk
- Add patch91: fix kaddressbook kde bug #96762

* Wed Jan 12 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-14mdk
- Add patch90: fix libkcal kde bug #94310

* Fri Jan 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-13mdk
- Fix kmail kde bug #94043

* Thu Jan 06 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-12mdk
- Fix kmail kde bug #96448

* Thu Dec 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-11mdk
- Fix knode kde bug #95937

* Tue Dec 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-10mdk
- Sync with CVS

* Tue Dec 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-9mdk
- Fix kde bug #95032

* Wed Dec 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-8mdk
- Fix spec file

* Fri Dec 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-7mdk
- Fix conflict

* Thu Dec 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-6mdk
- Fix conflict

* Thu Dec 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-5mdk
- Add patch86: fix kmail info column

* Thu Dec 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-4mdk
- Fix missing package

* Wed Dec 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-3mdk
- Use mandrakelinux-create-kde-mdk-menu

* Mon Dec 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-2mdk
- Split ktnef

* Tue Nov 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Fri Nov 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-21mdk
- Add requires on gnokii-devel

* Fri Nov 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-20mdk
- Add patch87: fix knode kde bug #93312

* Thu Nov 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-19mdk
- Add patch86: fix ressource exchange crash

* Tue Nov 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-18mdk
- Sync with CVS

* Tue Nov 02 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.3.1-17mdk
- fix build on LP64 platforms

* Thu Oct 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-16mdk
- Sync with CVS

* Tue Oct 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-15mdk
- Fix add patch85: add first message

* Thu Oct 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-14mdk
- Sync with CVS

* Thu Oct 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-13mdk
- Fix buildrequires

* Tue Oct 12 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-12mdk
- Deprecate mdk version < 9.2

* Fri Oct 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-11mdk
- 3.3.1

* Thu Sep 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-33mdk
- Update from CVS (kpilot)

* Wed Sep 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-32mdk
- Rebuild against kdelibs-3.3.0

* Wed Sep 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-22mdk
- Sync with CVS (fix kmail/korganizer/kalarm)

* Wed Sep 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-21mdk
- fix missing /

* Wed Sep 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-20mdk
- Fix knotes create directory (fix MDK bug #????)

* Sat Sep 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-19mdk
- Fix Upgrade from MDK9.1

* Sat Sep 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-18mdk
- Update from kde 3.3 branch (crahs into kmail)

* Sat Sep 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-17mdk
- Fix upgrade from MDK9.2

* Sat Sep 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-16mdk
- missing package

* Fri Sep 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-15mdk
- Fix requires on kdebase-common

* Thu Sep 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-14mdk
- Rebuild for missing package

* Wed Sep 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-13mdk
- Sync with CVS (fix kmail/kalarm)

* Sat Sep 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-12mdk
- Fix numero release when we compile it under kde 3.2 branch/3.3 branch

* Fri Sep 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-11mdk
- Try to compile apidoc
- Fix launcher desktop

* Thu Sep 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-10mdk
- Sync with CVS (fix korganizer/kmail)

* Thu Sep 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-9mdk
- Fix requires good kdelibs

* Wed Sep 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-7mdk
- Add patch84: fix kmail default color

* Tue Sep 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-6mdk
- Update from kde 3.3 branch

* Sat Sep 11 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-5mdk
- Sync with CVS

* Sat Sep 11 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-4mdk
- Fix compile kdepim against kde-3.3.x

* Fri Sep 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-3mdk
- Add patch84: fix certwartcher shortcut function

* Fri Sep 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-2mdk
- Remove kontact.menu => now kolab works very well

* Fri Sep 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-1mdk
- kde 3.3.0

-* Wed Sep 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-36mdk
- Add patch84: fix kmail default color

* Thu Sep 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-35mdk
- Add patch83: fix kmail kde bug 85301 "kmail freezes when switching folders"

* Sat Aug 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-34mdk
- Add patch82: fix knotes kde bug #87266 "by making sure that at least 
									10 pixels of a note are visible"

* Fri Aug 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-33mdk
- Add patch81: fix korganizer url "korganizer can handle URLs"

* Wed Aug 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-32mdk
- Add patch80: fix korganizer kde bug #78080

* Wed Aug 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-31mdk
- Fix menu

* Sat Aug 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-30mdk
- Fix menu

* Sat Aug 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-29mdk
- Add patch79: fix kmail "Check for the folders with the right foldername"

* Thu Aug 12 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-28mdk
- Remove quick search bar

* Wed Aug 11 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-27mdk
- Add patch77: fix dnd into kmail composer

* Tue Aug 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-26mdk
- Remove debug

* Wed Aug 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-25mdk
- Add patch76: fix kontact kde bug#86002

* Thu Jul 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-24mdk
- Fix spec file

* Fri Jul 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-23mdk
- Add patch75: fix kde bug #82242 "avoid deleting the filter actions 
				before they are unplugged from the popup menu"

* Thu Jul 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-22mdk
- Add patch74: fix remove rpath

* Wed Jul 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-21mdk
- Sync with CVS (kalarm/korganizer fix)

* Tue Jul 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-20mdk
- Add buildrequires doxygen

* Sat Jul 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-19mdk
- Add patch72: fix crash found by Nicolas Chipaux when we use "view source" and codec doesn't exist

* Fri Jul 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-18mdk
- Generate doc

* Thu Jul 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-17mdk
- Add patch71: fix kaddressbook, add focus to editor

* Wed Jul 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-16mdk
- Rebuild with new kdelibs

* Tue Jul 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-15mdk
- Add patch71: fix kmail kde bug #84422 "Fixed suggested filename when saving a message. subject.findRev(':') removed too much, better use KMMessage::cleanSubject() which only removes Re: and Fwd: stuff."

* Tue Jul 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-14mdk
- Add patch68: fix knode kde bug #50099 "Switch back to the composer if the user cancels the GPG signing instead of silently sending the article without signing."
- Add patch69: fix knode kde bug #52657 "More consistent toolbars between knode/knode in kontact and knode/kmail."
- Add patch70: fix resource exchange crash "fix crashes if network connection is borken"

* Fri Jul 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-13mdk
- Add patch66: knotes "Don't try to read from, and remove, a file that doesn't exist. This fixes a kdError on knotes startup."
- Add patch67: fix kmail kde bug #83756 "Be a bit more responsive when searching."

* Wed Jun 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-12mdk
- Sync with CVS

* Tue Jun 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-10mdk
- Fix kmail #84065
- Add patch65 fix libkcal

* Sat Jun 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-8mdk
- Sync with CVS

* Fri Jun 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-7mdk
- Fix kontact argument list

* Fri Jun 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-6mdk
- Update toolbar when we create antispam action

* Fri Jun 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-5mdk
- Update patch for antispam

* Thu Jun 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-4mdk
- Add patch62: fix kaddressbook delete button

* Thu Jun 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-3mdk
- Add filter log dialogbox
- Add kontact module list

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-2mdk
- Add patch58: remove mem leak into korganizer

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Sat Jun 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-9mdk
- Rebuild

* Thu May 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-8mdk
- Add patch57: duplicate filter rules

* Thu May 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-7mdk
- Sync with CVS

* Wed May 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-6mdk
- Add patch56: fix kmail filter action

* Wed May 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-5mdk
- Add patch55: fix update kmail account button

* Tue May 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-4mdk
- Rebuild with debug

* Thu May 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-3mdk
- Add patch54: fix kontact->kmail->summary update

* Thu Apr 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-2mdk
- Sync with CVS

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Fri Apr 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-7mdk
- Add patch52: disable reply menu when there is not a email selected (bug found by David Baudens)

* Wed Apr 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-6mdk
- Add patch51: fix korganizer crash (crash found by David Baudens)

* Wed Apr 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-5mdk
- Fix endloop

* Wed Apr 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-4mdk
- Add patch50: Add "search again action in kmail/knode" bug found by David Baudens

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-3mdk
- Fix spec file for using rpmbuildupdate

* Tue Apr 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-2mdk
- Remove not necessary patch (merged into KDE_3_2_BRANCH)

* Sat Apr 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

