%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define oname kdeutils
%define lib_name_orig lib%{oname}
%define lib_major 1
%define lib_name %mklibname %{name} %lib_major

%define tpctl_arches %{ix86}

%define build_superkaramba 0

Name: kde3-%{oname}
Summary: K Desktop Environment - Utilities
Version: 3.5.12
Release: %mkrel 1
Group: Graphical desktop/KDE3
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
Patch0: kdeutils-3.0-ktimer_icons.patch
#Patch1:	kdeutils-3.5.5-klaptop-pmsuspend.patch
#Patch3: kdeutils-3.5.8-lzma-support.patch
Patch4: kdeutils-3.5.9-fix-lha-support.patch
#Patch5: kdeutils-3.5.9-fix-underlink.patch
Patch6: kde-3.5.10-acinclude.patch
#Patch7: fix_autotools.patch

BuildRoot:	%_tmppath/%name-%version-%release-root
License:	GPL
Obsoletes: kdeutils3.0 < 3.5.3-3mdv2007.0 
Obsoletes: kdeutils3 < 3.5.3-3mdv2007.0 
Obsoletes: kdf < 3.5.3-3mdv2007.0
Obsoletes: kdeutils-kdepasswd < 3.5.3-3mdv2007.0
Provides: kdeutils3 = %version-%release 
Provides: %{oname} = %version-%release
Obsoletes: %{oname}
Obsoletes: kdeutils3
BuildRequires: kde3-macros
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%endif
BuildRequires: autoconf >= 1:2.65
BuildRequires: automake > 1.5
BuildRequires: X11-devel
BuildRequires: kdelibs-devel >= 3.2-13mdk
BuildRequires: arts3-devel >= 1.1
BuildRequires: kdebase-devel
BuildRequires: openssl-devel
BuildRequires: net-snmp-devel
BuildRequires:	gmp-devel
%py_requires -d
%ifarch %{tpctl_arches}
BuildRequires:	libtpctl-devel
%endif
BuildConflicts: libxmms-devel
Requires: %{name}-kedit = %version-%release
Requires: %{name}-kcalc = %version-%release
Requires: %{name}-ktimer = %version-%release
Requires: %{name}-kjots = %version-%release
Requires: %{name}-khexedit = %version-%release
Requires: %{name}-kfloppy = %version-%release
Requires: %{name}-kdf = %version-%release
Requires: %{name}-kcharselect = %version-%release
Requires: %{name}-ark = %version-%release
Requires: %lib_name-common = %version-%release
Requires: %{name}-kdessh = %version-%release
Requires: %{name}-ksim = %version-%release
Requires: %{name}-common = %version-%release
Requires: %{name}-klaptop = %version-%release
Requires: %{name}-kwalletmanager = %version-%release
%if %build_superkaramba
Requires: %{name}-superkaramba = %version-%release
%endif

%description
Utilities for the K Desktop Environment.
	- ark: manager for compressed files and archives
	- kcalc: scientific calculator
	- kcharselect: select special characters from any fonts 
			and put them into the clipboard
	- charselectapplet: dito, but as a Kicker applet
	- kcardtools:
	- kdessh: front end to ssh
	- kdf: like 'df', a graphical free disk space viewer
	- kedit: a simple text editor, without formatting like bold, italics etc
	- kfloppy: format a floppy disks with this app
	- khexedit: binary file editor
	- kjots: manages several "books" with a subject and notes
	- klaptopdaemon: battery and power management, including KControl plugins
	- kregexpeditor: graphical regular expression editor
	- ktimer: execute programs after some time

%files

#-----------------------------------------------------------------------------

%package klaptop
Summary:	Battery and power management
Group:		Graphical desktop/KDE3
Requires:	%lib_name-klaptop = %version-%release
Obsoletes:	kdeutils
Provides:	kde3-klaptop3 = %version-%release
Provides:	kdeutils3-klaptop = %version-%release 
Provides:	%{oname}-klaptop = %version-%release
Obsoletes:	%{oname}-klaptop
Obsoletes:	kdeutils3-klaptop
Conflicts:	kdeutils-common < 3.5.3-3mdv2007.0
%ifarch %{tpctl_arches}
Requires:	tpctl
%endif

%description klaptop
Battery and power management, including KControl plugins.

%if %mdkversion < 200900
%post klaptop
%update_menus
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun klaptop
%clean_menus
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif

%files klaptop
%defattr(-,root,root)
%attr(-,root,nogroup) %_kde3_bindir/klaptop_acpi_helper
%_kde3_bindir/klaptop_check
%_kde3_iconsdir/*/*/*/laptop*
%dir %_kde3_appsdir/klaptopdaemon/
%_kde3_appsdir/klaptopdaemon/*
%_kde3_datadir/services/kded/klaptopdaemon.desktop
%doc %_kde3_docdir/HTML/en/kcontrol/kcmlowbatcrit
%doc %_kde3_docdir/HTML/en/kcontrol/kcmlowbatwarn
%doc %_kde3_docdir/HTML/en/kcontrol/laptop
%doc %_kde3_docdir/HTML/en/kcontrol/powerctrl
%_kde3_datadir/applications/kde/pcmcia.desktop
%_kde3_datadir/applications/kde/laptop.desktop
%_kde3_libdir/kde3/kcm_laptop.*
%_kde3_libdir/kde3/kded_klaptopdaemon.*

#-----------------------------------------------------------------------------

%package -n %lib_name-klaptop
Summary:	Library for klaptop
Group:	 	Development/KDE and Qt	
Obsoletes:	%lib_name-klaptop-devel < 3.5.9
Provides:	%{lib_name_orig}-klaptop = %version-%release
Obsoletes:	%{lib_name_orig}-klaptop


%description -n %lib_name-klaptop
Library for klaptop.

%if %mdkversion < 200900
%post -n %lib_name-klaptop -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name-klaptop -p /sbin/ldconfig
%endif

%files -n %lib_name-klaptop
%defattr(-,root,root)
%_kde3_libdir/libkcmlaptop.la
%_kde3_libdir/libkcmlaptop.so.*

#-----------------------------------------------------------------------------

%package kmilo
Summary:        Battery and power management
Group:          Graphical desktop/KDE3
Requires:       %lib_name-kmilo = %version-%release
Obsoletes:      kdeutils <= 3.1
Provides:       kde3-kmilo3 = %version-%release
Conflicts:      kdeutils-common < 3.5.3-3mdv2007.0
Conflicts:      kdeutils-kmilo < 3.5.8-3
Provides:	kde3-klaptop3 = %version-%release
Provides:	kdeutils3-kmilo = %version-%release 
Provides:	%{oname}-kmilo = %version-%release
Obsoletes:	%{oname}-kmilo
Obsoletes:	kdeutils3-kmilo

%description kmilo
Battery and power management, including KControl plugins.

%if %mdkversion < 200900
%post kmilo
%update_menus
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun kmilo
%clean_menus
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif

%files kmilo
%defattr(-,root,root)
%_kde3_libdir/kde3/kded_kmilod.*
%_kde3_libdir/kde3/kmilo_asus.*
%_kde3_libdir/kde3/kmilo_delli8k.*
%_kde3_libdir/kde3/kmilo_generic.*
%_kde3_libdir/kde3/kmilo_kvaio.*
%_kde3_libdir/kde3/kmilo_thinkpad.*
%_kde3_libdir/kde3/kcm_kvaio.*
%_kde3_libdir/kde3/kcm_thinkpad.*
%_kde3_datadir/services/kded/kmilod.desktop
%_kde3_datadir/applications/kde/thinkpad.desktop
%_kde3_datadir/applications/kde/kvaio.desktop
%dir %_kde3_datadir/services/kmilo
%_kde3_datadir/services/kmilo/*
%dir %_kde3_datadir/servicetypes/kmilo
%_kde3_datadir/servicetypes/kmilo/kmilopluginsvc.desktop

#-----------------------------------------------------------------------------

%package -n %lib_name-kmilo
Summary:        Library for kmilo
Group:          Development/KDE and Qt
Conflicts:      %lib_name-klaptop < 3.5.8-4
Provides:	%{lib_name_orig}-kmilo = %version-%release
Obsoletes:	%{lib_name_orig}-kmilo

%description -n %lib_name-kmilo
Library for kmilo.

%if %mdkversion < 200900
%post -n %lib_name-kmilo -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name-kmilo -p /sbin/ldconfig
%endif

%files -n %lib_name-kmilo
%defattr(-,root,root)
%_kde3_libdir/libkmilo.la
%_kde3_libdir/libkmilo.so.*

#-----------------------------------------------------------------------------

%package common
Summary:	Kdeutils common files
Group:		Graphical desktop/KDE3
Requires:	%lib_name-common = %version-%release
Provides:	kdeutils3-common = %version-%release 
Provides:	%{oname}-common = %version-%release
Obsoletes:	%{oname}-common
Obsoletes:	kdeutils3-common
URL:        http://www.kde.org/

%description common
Kdeutils common files

%if %mdkversion < 200900
%post common
%update_menus
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun common
%clean_menus
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif

%files common
%defattr(-,root,root)
%_kde3_datadir/applications/kde/irkick.desktop       
%_kde3_datadir/applications/kde/kregexpeditor.desktop  
%_kde3_datadir/applications/kde/kcmlirc.desktop      
%doc %_kde3_docdir/HTML/en/kinfocenter/blockdevices
%doc %_kde3_docdir/HTML/en/kcmlirc
%doc %_kde3_docdir/HTML/en/irkick
%doc %_kde3_docdir/HTML/en/KRegExpEditor
%_kde3_iconsdir/*/*/*/kregexpeditor*
%_kde3_iconsdir/*/*/*/irkick*
%_kde3_bindir/kregexpeditor
%_kde3_bindir/irkick
%_kde3_libdir/kde3/irkick.*
%_kde3_libdir/kde3/kcm_kcmlirc.*
%dir %_kde3_appsdir/irkick
%_kde3_appsdir/irkick/*
%dir %_kde3_appsdir/profiles/
%_kde3_appsdir/profiles/*
%dir %_kde3_appsdir/remotes/
%_kde3_appsdir/remotes/*
%_kde3_datadir/autostart/irkick.desktop
%dir %_kde3_appsdir/kregexpeditor/
%_kde3_appsdir/kregexpeditor/*
%_kde3_datadir/services/kregexpeditorgui.desktop
%_kde3_libdir/libkdeinit_irkick.*
%_kde3_libdir/kde3/libkregexpeditorgui.*

#-----------------------------------------------------------------------------

%package ktimer
Summary:	Ktimer program
Group:		Graphical desktop/KDE3
Provides:	kde3-ktimer3 = %version-%release
Provides:	kdeutils3-ktimer = %version-%release 
Provides:	%{oname}-ktimer = %version-%release
Obsoletes:	%{oname}-ktimer
Obsoletes:	kdeutils3-ktimer
URL:        http://www.kde.org/

%description ktimer
Ktimer allows to execute programs after some time

%if %mdkversion < 200900
%post ktimer
%update_menus
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun ktimer
%clean_menus
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif


%files ktimer
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/ktimer
%_kde3_bindir/ktimer
%_kde3_datadir/applications/kde/ktimer.desktop
%_kde3_iconsdir/*/*/*/ktimer*

#-----------------------------------------------------------------------------

%package kdessh
Summary:	Kdessh program
Group:		Graphical desktop/KDE3
Provides:	kde3-kdessh3 = %version-%release
Provides:	kdeutils3-kdessh = %version-%release 
Provides:	%{oname}-kdessh = %version-%release
Obsoletes:	%{oname}-kdessh
Obsoletes:	kdeutils3-kdessh
URL:        http://www.kde.org/

%description kdessh
Front end to ssh

%files kdessh
%defattr(-,root,root)
%_kde3_bindir/kdessh

#-----------------------------------------------------------------------------

%package kjots
Summary:	Kjots program
Group:		Graphical desktop/KDE3
Provides:	kde3-kjots3 = %version-%release
Provides:	kde3-Kjots3 = %version-%release
Provides:	kdeutils3-kjots = %version-%release 
Provides:	%{oname}-kjots = %version-%release
Obsoletes:	%{oname}-kjots
Obsoletes:	kdeutils3-kjots
URL:        http://www.kde.org/

%description kjots
Manages several "books" with a subject and notes

%if %mdkversion < 200900
%post kjots
%update_menus
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun kjots
%clean_menus
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif

%files kjots
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kjots
%_kde3_iconsdir/*/*/*/kjots.*
%_kde3_bindir/kjots
%dir %_kde3_appsdir/kjots
%_kde3_appsdir/kjots/*
%_kde3_datadir/applications/kde/Kjots.desktop          
%_kde3_datadir/config.kcfg/kjots.kcfg

#-----------------------------------------------------------------------------

%package kfloppy
Summary:	Kfloppy program
Group:		Graphical desktop/KDE3
Requires:	dosfstools
Provides:	kde3-kfloppy3 = %version-%release
Provides:	kdeutils3-kfloppy = %version-%release 
Provides:	%{oname}-kfloppy = %version-%release
Obsoletes:	%{oname}-kfloppy
Obsoletes:	kdeutils3-kfloppy
URL:        http://www.kde.org/

%description kfloppy
Kfloppy allows to format a floppy disks with this app

%if %mdkversion < 200900
%post kfloppy
%update_menus
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun kfloppy
%clean_menus
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif

%files kfloppy
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kfloppy
%_kde3_iconsdir/*/*/*/kfloppy.*
%_kde3_bindir/kfloppy
%_kde3_datadir/applications/kde/KFloppy.desktop        
%_kde3_appsdir/konqueror/servicemenus/floppy_format.desktop

#-----------------------------------------------------------------------------

%package kdf
Summary:	Kdf program
Group:		Graphical desktop/KDE3
Provides:	kde3-kdf3 = %version-%release
Provides:	kdeutils3-kdf = %version-%release 
Provides:	%{oname}-kdf = %version-%release
Obsoletes:	%{oname}-kdf
Obsoletes:	kdeutils3-kdf
URL:        http://www.kde.org/

%description kdf
Like 'df', a graphical free disk space viewer

%if %mdkversion < 200900
%post kdf
%update_menus
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun kdf
%clean_menus
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif

%files kdf
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kdf
%_kde3_bindir/kdf
%_kde3_bindir/kwikdisk
%_kde3_iconsdir/*/*/*/kwikdisk.*
%_kde3_iconsdir/*/*/*/kdf.*
%_kde3_iconsdir/*/*/*/kcmdf.*
%dir %_kde3_appsdir/kdf
%_kde3_appsdir/kdf/*
%_kde3_datadir/applications/kde/kdf.desktop          
%_kde3_datadir/applications/kde/kwikdisk.desktop
%_kde3_datadir/applications/kde/kcmdf.desktop 
%_kde3_libdir/kde3/kcm_kdf.*

#-----------------------------------------------------------------------------

%package kcharselect
Summary:	Kcharselect program
Group:		Graphical desktop/KDE3
Provides:	kde3-kcharselect3 = %version-%release
Conflicts:      %lib_name-common < 3.5.3-3mdv2007.0
Conflicts:      %name-common < 3.5.8-6
Provides:	kdeutils3-kcharselect = %version-%release 
Provides:	%{oname}-kcharselect = %version-%release
Obsoletes:	%{oname}-kcharselect
Obsoletes:	kdeutils3-kcharselect

%description kcharselect
Kcharselect allows to select special characters from any fonts and put them
into the clipboard

%if %mdkversion < 200900
%post kcharselect
%update_menus
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun kcharselect
%clean_menus
%endif

%files kcharselect
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kcharselect
%_kde3_bindir/kcharselect
%_kde3_libdir/kde3/kcharselect_panelapplet.*
%_kde3_appsdir/kicker/applets/kcharselectapplet.desktop
%_kde3_iconsdir/*/*/*/kcharselect.*
%dir %_kde3_appsdir/kcharselect
%_kde3_appsdir/kcharselect/*
%_kde3_datadir/applications/kde/KCharSelect.desktop  
%_kde3_appsdir/kconf_update/kcharselect.upd

#-----------------------------------------------------------------------------

%package khexedit
Summary:	Khexedit program
Group:		Graphical desktop/KDE3
Provides:	kde3-khexedit3 = %version-%release
Requires:	%lib_name-khexedit = %version
Conflicts: %lib_name-khexedit < 3.5.3-3mdv2007.0
Provides:	kdeutils3-khexedit = %version-%release 
Provides:	%{oname}-khexedit = %version-%release
Obsoletes:	%{oname}-khexedit
Obsoletes:	kdeutils3-khexedit

%description khexedit
A binary file editor

%if %mdkversion < 200900
%post khexedit
%update_menus
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun khexedit
%clean_menus
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif

%files khexedit
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/khexedit
%_kde3_bindir/khexedit
%_kde3_iconsdir/*/*/*/khexedit.*
%_kde3_datadir/services/khexedit2part.desktop
%_kde3_appsdir/khexedit2part/khexedit2partui.rc
%dir %_kde3_appsdir/khexedit
%_kde3_appsdir/khexedit/*
%_kde3_datadir/applications/kde/khexedit.desktop       
%_kde3_datadir/services/kbyteseditwidget.desktop
%_kde3_libdir/kde3/libkbyteseditwidget.*
%_kde3_libdir/kde3/libkhexedit2part.*

#-----------------------------------------------------------------------------

%package -n %lib_name-khexedit
Summary:	Khexedit library
Group:		Development/KDE and Qt	
URL:        http://www.kde.org/
Obsoletes: %lib_name-khexedit-devel < 3.5.9
Provides:	%{lib_name_orig}-khexedit = %version-%release
Obsoletes:	%{lib_name_orig}-khexedit

%description -n %lib_name-khexedit
Library for file editor

%if %mdkversion < 200900
%post -n %lib_name-khexedit -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name-khexedit -p /sbin/ldconfig
%endif

%files -n %lib_name-khexedit
%defattr(-,root,root)
%_kde3_libdir/libkhexeditcommon.la
%_kde3_libdir/libkhexeditcommon.so.*

#-----------------------------------------------------------------------------

%package kedit
Summary:	Kedit program
Group:		Graphical desktop/KDE3
Obsoletes: %lib_name-kedit < 3.5.9
Provides:	kde3-kedit3 = %version-%release
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Provides:	kdeutils3-kedit = %version-%release 
Provides:	%{oname}-kedit = %version-%release
Obsoletes:	%{oname}-kedit
Obsoletes:	kdeutils3-kedit

%description kedit
A simple text editor, without formatting like bold, italics etc.

%if %mdkversion < 200900
%post kedit
%update_menus
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun kedit
%clean_menus
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif

%files kedit
%defattr(-,root,root)
%_kde3_bindir/kedit
%_kde3_libdir/kde3/kedit.*
%_kde3_libdir/libkdeinit_kedit.*
%doc %_kde3_docdir/HTML/en/kedit
%dir %_kde3_appsdir/kedit
%_kde3_appsdir/kedit/*
%_kde3_datadir/config.kcfg/kedit.kcfg
%_kde3_iconsdir/*/*/*/kedit.*
%_kde3_datadir/applications/kde/KEdit.desktop

#-----------------------------------------------------------------------------

%package ark
Summary:	Ark program
Group: Graphical desktop/KDE3
Obsoletes: %lib_name-ark < 3.5.9
Provides: kde3-ark3 = %version-%release
Requires: zip	
Requires: unzip
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Provides:	kdeutils3-ark = %version-%release 
Provides:	%{oname}-ark = %version-%release
Obsoletes:	%{oname}-ark
Obsoletes:	kdeutils3-ark

%description ark
Manager for compressed files and archives

%if %mdkversion < 200900
%post ark
%update_menus
%{update_desktop_database}
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun ark
%clean_menus
%{update_desktop_database}
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif

%files ark
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/ark
%_kde3_iconsdir/*/*/*/ark.*
%_kde3_bindir/ark
%dir %_kde3_appsdir/
%_kde3_appsdir/ark/*
%_kde3_datadir/applications/kde/ark.desktop          
%_kde3_libdir/kde3/ark.*
%_kde3_libdir/kde3/libarkpart.*
%_kde3_datadir/config.kcfg/ark.kcfg
%_kde3_datadir/services/ark_part.desktop
%_kde3_libdir/libkdeinit_ark.*

#-----------------------------------------------------------------------------

%package kcalc
Summary:	Kcalc program
Group:		Graphical desktop/KDE3
Obsoletes:	%lib_name-kcalc < 3.5.9
Provides:	kde3-kcalc3 = %version-%release
URL:        http://www.kde.org/
Provides:	kdeutils3-kcalc = %version-%release 
Provides:	%{oname}-kcalc = %version-%release
Obsoletes:	%{oname}-kcalc
Obsoletes:	kdeutils3-kcalc

%description kcalc
A scientific calculator

%if %mdkversion < 200900
%post kcalc
%update_menus
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun kcalc
%clean_menus
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif

%files kcalc
%defattr(-,root,root)
%_kde3_bindir/kcalc
%_kde3_datadir/applications/kde/kcalc.desktop
%_kde3_iconsdir/*/*/*/kcalc.*
%_kde3_libdir/kde3/kcalc.*
%_kde3_datadir/config.kcfg/kcalc.kcfg
%dir %_kde3_appsdir/kcalc/
%_kde3_appsdir/kcalc/*
%_kde3_appsdir/kconf_update/kcalcrc.upd
%doc %_kde3_docdir/HTML/en/kcalc
%_kde3_libdir/libkdeinit_kcalc.*

#-----------------------------------------------------------------------------

%package -n %lib_name-common-devel
Summary:	Header files for kdeutils
Group:		Development/KDE and Qt
Requires:	%lib_name-common = %version-%release
Requires:	%lib_name-ksim = %version-%release
URL:        http://www.kde.org/
Obsoletes: %lib_name-ksim-devel < 3.5.9
Obsoletes: %lib_name-khexedit-devel < 3.5.9
Obsoletes: %lib_name-klaptop-devel < 3.5.9
Obsoletes:  kdeutils3-devel, kdeutils-devel < 3.1
Provides:   kde3-kdeutils3-devel = %version-%release
Provides:   kde3-kdeutils-devel = %version-%release
Obsoletes:  %lib_name-devel < 3.1 
Provides:   %lib_name-devel = %version-%release
Conflicts:  %lib_name-common < 3.5.7-2
Provides:	%{lib_name_orig}-devel = %version-%release
Obsoletes:	%{lib_name_orig}-devel

%description -n %lib_name-common-devel
Headers files for kdeutils.

%files -n %lib_name-common-devel
%defattr(-,root,root,-)
%_kde3_includedir/*
%_kde3_libdir/libkregexpeditorcommon.so
%_kde3_libdir/libksimcore.so
%_kde3_libdir/libkcmlaptop.so
%_kde3_libdir/libkmilo.so
%_kde3_libdir/libkhexeditcommon.so

#-----------------------------------------------------------------------------

%package -n %lib_name-common
Summary:	Librarie files for kdeutils
Group:		Development/KDE and Qt
Obsoletes:	%lib_name < 3.1
Provides:	%lib_name = %version-%release
Provides:	%{lib_name_orig}-common = %version-%release
Obsoletes:	%{lib_name_orig}-common
URL:        http://www.kde.org/

%description -n %lib_name-common
Libraries files for kdeutils.

%if %mdkversion < 200900
%post -n %lib_name-common -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name-common -p /sbin/ldconfig
%endif

%files -n %lib_name-common
%defattr(-,root,root)
%_kde3_libdir/libkregexpeditorcommon.la
%_kde3_libdir/libkregexpeditorcommon.so.*

#-----------------------------------------------------------------------------

%package ksim
Summary:	Ksim program
Group:		Graphical desktop/KDE3
Requires:	%lib_name-ksim = %version-%release
Provides:	kde3-ksim3 = %version-%release
URL:        http://www.kde.org/
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Provides:	kdeutils3-ksim = %version-%release 
Provides:	%{oname}-ksim = %version-%release
Obsoletes:	%{oname}-ksim
Obsoletes:	kdeutils3-ksim

%description ksim
Ksim program

%files ksim
%defattr(-,root,root)
%_kde3_appsdir/kicker/extensions/ksim.desktop
%_kde3_libdir/kde3/ksim_*.*
%dir %_kde3_appsdir/ksim
%_kde3_appsdir/ksim/*
%_kde3_datadir/config/ksim_panelextensionrc
%doc %_kde3_docdir/HTML/en/ksim
%_kde3_iconsdir/*/*/*/ksim*

#-----------------------------------------------------------------------------

%package kgpg
Summary:	Kgpg Frontend for gpg
Group:		Graphical desktop/KDE3
Provides:	kde3-kgpg3 = %version-%release
URL:        http://www.kde.org/
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Provides:	kdeutils3-kgpg = %version-%release 
Provides:	%{oname}-kgpg = %version-%release
Obsoletes:	%{oname}-kgpg
Obsoletes:	kdeutils3-kgpg

%description kgpg
kgpg is a simple, free, open source KDE frontend for gpg.

%if %mdkversion < 200900
%post kgpg
%update_menus
%{update_desktop_database}
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun kgpg
%clean_menus
%{clean_desktop_database}
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif

%files kgpg
%defattr(-,root,root)
%_kde3_bindir/kgpg
%_kde3_datadir/applications/kde/kgpg.desktop           
%_kde3_datadir/config.kcfg/kgpg.kcfg
%_kde3_iconsdir/*/*/*/kgpg.*
%dir %_kde3_appsdir/kgpg
%_kde3_appsdir/kgpg/*
%doc %_kde3_docdir/HTML/en/kgpg
%_kde3_datadir/autostart/kgpg.desktop
%_kde3_appsdir/konqueror/servicemenus/encryptfile.desktop
%_kde3_appsdir/konqueror/servicemenus/encryptfolder.desktop

#-----------------------------------------------------------------------------
%if %build_superkaramba
%package superkaramba
Group:      Graphical desktop/KDE3
Summary:    Program that can display a lot of various information right on your desktop
Provides:	kde3-superkaramba3 = %version-%release
Conflicts:  kdenetwork <= 3.1.92
Obsoletes:  karamba
Provides:	kdeutils3-superkaramba = %version-%release 
Provides:	%{oname}-superkaramba = %version-%release
Obsoletes:	%{oname}-superkaramba
Obsoletes:	kdeutils3-superkaramba

%description superkaramba
Karamba is a KDE program that can display a lot of various information
right on your desktop. Karamba uses the same "fake" transparency effect
that e.g., Konsole can use. For the autor this is not a big problem as the
purpose of Karamba is sit on the background.

%files superkaramba
%defattr(-,root,root,-)
%_kde3_bindir/superkaramba
%_kde3_datadir/applnk/Utilities/superkaramba.desktop
%_kde3_appsdir/superkaramba/superkarambaui.rc
%doc %_kde3_docdir/HTML/en/superkaramba
%_kde3_iconsdir/*/*/*/superkaramba*
%_kde3_datadir/mimelnk/application/x-superkaramba.desktop

%endif

#-----------------------------------------------------------------------------

%package kwalletmanager
Summary:    Kwalletmanager program
Group:      Graphical desktop/KDE3
Provides:   kde3-kwalletmanager3 = %version-%release
URL:        http://www.kde.org/
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Provides:	kdeutils3-kwalletmanager = %version-%release 
Provides:	%{oname}-kwalletmanager = %version-%release
Obsoletes:	%{oname}-kwalletmanager
Obsoletes:	kdeutils3-kwalletmanager

%description kwalletmanager
Kwalletmanager program

%if %mdkversion < 200900
%post kwalletmanager
%update_menus
%{update_desktop_database}
%update_kde3_icon_cache crystalsvg
%update_kde3_icon_cache hicolor
%endif


%if %mdkversion < 200900
%postun kwalletmanager
%clean_menus
%{clean_desktop_database}
%clean_kde3_icon_cache crystalsvg
%clean_kde3_icon_cache hicolor
%endif

%files kwalletmanager
%defattr(-,root,root)
%_kde3_bindir/kwalletmanager
%_kde3_iconsdir/*/*/*/kwalletmanager.*
%_kde3_datadir/applications/kde/kwalletmanager-kwalletd.desktop
%doc %_kde3_docdir/HTML/en/kwallet
%_kde3_datadir/applications/kde/kwalletconfig.desktop
%_kde3_datadir/applications/kde/kwalletmanager.desktop
%_kde3_libdir/kde3/kcm_kwallet.*
%_kde3_datadir/services/kwallet_config.desktop
%_kde3_datadir/services/kwalletmanager_show.desktop
%dir %_kde3_appsdir/kwalletmanager/
%_kde3_appsdir/kwalletmanager/*

#-----------------------------------------------------------------------------

%package -n %lib_name-ksim
Summary:	Librarie files for kdeutils
Group:		Development/KDE and Qt
Provides:	%lib_name_orig-ksim = 1:%version-%release
Obsoletes: %lib_name-ksim-devel < 3.5.9
Provides:	%{lib_name_orig}-ksim = %version-%release
Obsoletes:	%{lib_name_orig}-ksim
URL:        http://www.kde.org/

%if %mdkversion < 200900
%post -n %lib_name-ksim -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_name-ksim -p /sbin/ldconfig
%endif

%description -n %lib_name-ksim
Libraries files for ksim.

%files -n %lib_name-ksim
%defattr(-,root,root)
%_kde3_libdir/libksimcore.la
%_kde3_libdir/libksimcore.so.*

#-----------------------------------------------------------------------------


%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
#%patch1 -p1 -b .fix_bug_21671
#%patch3 -p0 -b .lzma_support
%patch4 -p1 -b .lha_support
#%patch5 -p0 -b .underlink
%if %mdkversion >= 201000
%patch6 -p1
#%patch7 -p1
%endif

%build
export QTDIR=%qt3dir
make -f admin/Makefile.common cvs
PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/

%configure_kde3

%make

%install
rm -fr %buildroot

%makeinstall_std

chmod 2755 %buildroot/%_kde3_bindir/klaptop_acpi_helper
export EXCLUDE_FROM_STRIP=klaptop_acpi_helper

# Link KDM images directory to faces directory
rm -fr %buildroot/%_kde3_appsdir/kdm/pics/users/

%if !%{build_superkaramba}
rm -fr %buildroot/%_kde3_docdir/HTML/en/superkaramba

%endif

%clean
rm -fr %buildroot/



%changelog

* Thu Jul 14 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-1mvt2010.2
+ Rebuild for MDV 2010.2/Trinity
+ Update sources
- Remove fix_autotools.patch, kdeutils-3.5.5-klaptop-pmsuspend.patch, kdeutils-3.5.8-lzma-support.patch,
  kdeutils-3.5.9-fix-underlink.patch

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 1:3.5.10-5mvt2010.0
- Rebuild for MDV 2010.1

* Sun Jan 17 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-4mvt2010.0
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65:patch5
+ Fix automake 1.11 issue:patch6
+ New package name to avoid possible&unwanted KDE4 conflict (add kde3 prefix)

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 3.5.10-3mdv2010.0
- Rebuild for MDV 2010.0

* Thu Apr 23 2009 Frederic Crozat <fcrozat@mandriva.com> 3.5.10-2mdv2009.1
+ Revision: 368932
- remove doc for superkaramba when not building it
- Do not build superkaramba, because of python 2.6
- Rediff some patches

  + Helio Chissini de Castro <helio@mandriva.com>
    - Recompile against new python

* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.10-1mdv2009.0
+ Revision: 277229
- Latest kde 3 upstream package

* Fri Jul 25 2008 Funda Wang <fundawang@mandriva.org> 3.5.9-10mdv2009.0
+ Revision: 249242
- superkaramba should obsolete karamba

* Fri Jun 13 2008 Funda Wang <fundawang@mandriva.org> 3.5.9-9mdv2009.0
+ Revision: 218650
- specify qt3 dir
- add patch fix underlinking

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 20 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 3.5.9-8mdv2009.0
+ Revision: 209433
- Use versioned obsoletes

* Wed May 14 2008 Anssi Hannula <anssi@mandriva.org> 3.5.9-7mdv2009.0
+ Revision: 207284
- add '3' suffix to subpackage provides (suggested by neoclust)
- drop now unneeded old obsoletes
- drop duplicate kdeutils provide from common subpackage

* Mon May 12 2008 Funda Wang <fundawang@mandriva.org> 3.5.9-6mdv2009.0
+ Revision: 206097
- pacakge should not obsolete itself

* Sun May 11 2008 Funda Wang <fundawang@mandriva.org> 3.5.9-5mdv2009.0
+ Revision: 205565
- kde3 package shouldn't obsolete kde4 version

* Fri May 09 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.9-4mdv2009.0
+ Revision: 205325
- Fix use of kde3 macros

* Wed May 07 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.9-3mdv2009.0
+ Revision: 203073
- Move to /opt

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - [BUGFIX] Fix support of lha files (Bug #38086)
    - Do not show KHexedit  only on Kde menu (Bug #34402)

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 3.5.9-1mdv2008.1
+ Revision: 169153
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches integrated
- Removed config s that was already applied on mandriva-kde-config

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-not-capitalized
    - fix description-line-too-long

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - add removed mimetype

* Tue Jan 29 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.8-6mdv2008.1
+ Revision: 159728
- [BUGFIX] Fix file list for kcharselect (Bug #37302)

* Mon Jan 28 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.8-5mdv2008.1
+ Revision: 159478
- Remove OnlyShowIn to make firefox happier

* Sun Jan 27 2008 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.8-4mdv2008.1
+ Revision: 158799
- Fix File list
- [FEATURE] Move Kmilo in its own package (Bug #36731)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 29 2007 Funda Wang <fundawang@mandriva.org> 3.5.8-3mdv2008.1
+ Revision: 139071
- rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add unzip as Requires of Ark
    - Add usptream 3.5.9 branch patches
      	- Be sure zoo is well detected / installed

* Sun Oct 28 2007 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.8-1mdv2008.1
+ Revision: 102775
- Kde 3.5.8
  Rediff patches ( desktop and lzma )

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-ended-with-dot

* Thu Sep 27 2007 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.7-9mdv2008.0
+ Revision: 93240
- [BUGFIX] Do not show kwalletmanager on menu (Bug #33954)

* Thu Sep 20 2007 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.7-7mdv2008.0
+ Revision: 91479
- [BUGFIX] Move Kregexp editor on Development/Tools (Bug 33122)
- [BUGFIX] Let irkick on kontrol (Bug #32673)

* Wed Aug 08 2007 Oden Eriksson <oeriksson@mandriva.com> 3.5.7-6mdv2008.0
+ Revision: 60203
- rebuilt against new net-snmp libs

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - oops, fix actual unlzma usage in patch
    - add lzma support (P4)

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Fix OnlyShowIn=KDE;

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 3.5.7-5mdv2008.0
+ Revision: 36180
- rebuild with correct optflags

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Fix menus for KDE sub-sections

* Tue May 22 2007 Nicolas Lécureuil <neoclust@mandriva.org> 3.5.7-2mdv2008.0
+ Revision: 29745
- Fix File list (bug #30959)

* Wed May 16 2007 Helio Chissini de Castro <helio@mandriva.com> 3.5.7-1mdv2008.0
+ Revision: 27455
- 3.5.7 release


* Mon Mar 05 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-3mdv2007.0
+ Revision: 133230
- Fix provides
- Fix spec file
- Patch merged into svn
- 3.5.6
- Fix group
- Remove requires

* Wed Dec 13 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-3mdv2007.1
+ Revision: 96411
- Add patch from Blino to fix bug #21671

* Mon Dec 04 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-2mdv2007.1
+ Revision: 90474
- Rebuild against new python
- Fix bug reported by Jean-Loup Colautti (fix add file in zip)
  (Necessary to make test after add new patch...)

* Tue Oct 17 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-1mdv2007.1
+ Revision: 65623
- As said on maintainer we use official tarball
  not a random snapshot
  If there is a critical crash add a patch to fix it.

  + Helio Chissini de Castro <helio@mandriva.com>
    - Back to use branch tarballs. Now using post 3.5.5

* Thu Sep 14 2006 Helio Chissini de Castro <helio@mandriva.com> 3.5.4-7mdv2007.0
+ Revision: 61291
- Kmilo fixes for bug http://qa.mandriva.com/show_bug.cgi?id=21221
  special keys will be proper handled regarding mixer

* Tue Sep 12 2006 Helio Chissini de Castro <helio@mandriva.com> 3.5.4-6mdv2007.0
+ Revision: 60934
- Fix bug http://qa.mandriva.com/show_bug.cgi?id=25245. kwalletmanager systray not appears on startup. Thanks to neoclust
- Fix for strange bug on ark zip file

* Thu Sep 07 2006 Helio Chissini de Castro <helio@mandriva.com> 3.5.4-5mdv2007.0
+ Revision: 60414
- Fix from upstream to bug http://qa.mandriva.com/show_bug.cgi?id=19444
  Thanks again to peroyvind to catch this one

* Thu Aug 31 2006 Laurent Montel <lmontel@mandriva.com> 3.5.4-4mdv2007.0
+ Revision: 58784
- New package (3.5.4-4mdv 2006-08-30)
  Add patch to fix klaptop bug #113622

* Fri Aug 25 2006 Helio Chissini de Castro <helio@mandriva.com> 3.5.4-3mdv2007.0
+ Revision: 57790
- Added kcontrol defaults patch

  + Laurent Montel <lmontel@mandriva.com>
    - Fix klaptop mdk bug # 22466

* Fri Aug 04 2006 Laurent Montel <lmontel@mandriva.com> 3.5.4-2mdv2007.0
+ Revision: 43312
- Fix crash in kgpg
  (2008/08/03 3.5.4-2mdv)

  + Helio Chissini de Castro <helio@mandriva.com>
    - Updated for latest official kde 3.5.4 release

* Tue Jul 25 2006 Helio Chissini de Castro <helio@mandriva.com> 3.5.3-4mdv2007.0
+ Revision: 42010
- Another xmms depends case. Thanks to spturtle to point this out

* Sat Jul 22 2006 Helio Chissini de Castro <helio@mandriva.com> 3.5.3-3mdv2007.0
+ Revision: 41907
- Add obsoletes for invalid package kdepasswd
- Clean and rearrange spec file
- Added tarball from kde branch as discussed on meeting in 28/06
- Removed rpath and added configure macro invalidating libtoolize
- Added strip macro as stated by Nanar ( for unstable builds )
- Removed non used patches
- Moved modules to right packages and obsoletes invalid libraries
- Buzip patches
- We are Mandriva now
- Uploading package ./kdeutils

  + Laurent Montel <lmontel@mandriva.com>
    --enable-new-ldflags doesn't work on x86_64
    - Use macro
    - 3.5.3
    - Rebuild to generate category
    - 3.5.2
      Remove unused patch
    - 3.5.1
    - Enable debug only for cooker
      MDK9.2 is obsolete now
    - Rebuild with last net-snmp lib
    - Rebuild with new net-snmp
    - Fix buildrequires found by Christiaan Welvaart thanks
    - Real kde3.5
    - Fix typo
      * Wed Nov 02 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.5-3mdk
    - Rebuild with new mysql
      * Thu Oct 27 2005 Helio Chissini de Castro <helio@mandriva.com> 3.3.5-2mdk
    - New immodule patch
    - Fix typo
    - 3.4.2
    - Sync with svn
    - Rebuild
    - Fix compile on x86_64
    - Oops missing it
    - Remove debug
      Fix kfloppy with udev
    - 3.4.2

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Sat Apr 23 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-6mdk
- Add patch25: fix launch irck (bug found by Arnaud De Lorbeau)

* Sat Apr 23 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-5mdk
- Reactivate -fvisibility same as for ppc

* Fri Apr 22 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-4mdk
- Disable patch 6 to allow to use klirc

* Sat Apr 16 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-3mdk
- Fix kregexpeditor icon menu

* Fri Apr 15 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-2mdk
- Try to re-enable visibility (test ksim)

* Tue Apr 12 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-2mdk
- Enable debug
- Fix email
- --enable-new-ldflags

* Thu Apr 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0

* Thu Apr 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-22mdk
- Disable visibility to fix crash in ksim

* Sat Apr 02 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-21mdk
- Add patch25: fix kloppy + udev MDK bug #15156

* Sun Feb 20 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-20mdk
- Add patch24: fix kgpg fix kde bug #88414

* Wed Feb 16 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-19mdk
- Sync with CVS (fix calc)

* Mon Feb 14 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-18mdk
- Fix visibility into kmilo

* Thu Feb 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-17mdk
- Disable debug

* Mon Feb 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-16mdk
- Add patch23: fix kcalc kde bug #98522

* Thu Feb 03 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-15mdk
- Add patch21: fix kgpg kde bug #76427
- Add patch22: fix kgpg kde bug #87469

* Fri Jan 28 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-14mdk
- Fix generated menu entry

* Mon Jan 24 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-13mdk
- Disable visibility for ppc

* Thu Jan 20 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-12mdk
- Rebuild for missing package

* Sat Jan 15 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-11mdk
- Add patch20: fix ark kde bug #95386

* Thu Jan 13 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-10mdk
- Against other fix KDE_EXPORT

* Mon Jan 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-9mdk
- Add patch19: fix klaptop "do not allow to overwrite files outside /proc"

* Thu Jan 06 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-8mdk
- Add function to disable visibility

* Thu Jan 06 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-7mdk
- Now it supported -fvisibility

* Thu Dec 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-6mdk
- Fix bug found by Pascal Terjan (klaptop provided kdeutils :'((

* Wed Dec 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-5mdk
- Add patch19: fix kgpg shredder icons

* Fri Dec 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-4mdk
- Add patch18: fix kdf kde bug #94774

* Fri Dec 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-3mdk
- Fix generate menu (mdk bug #9775)

* Wed Dec 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-2mdk
- Fix menu

* Tue Nov 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Tue Nov 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-6mdk
- Fix kfloppy with udev

* Tue Nov 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-5mdk
- Fix build on x86_64 patch from (Gwenole Beauchesne <gbeauchesne@mandrakesoft.com>)

* Wed Oct 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-4mdk
- Remove %%buildfor

* Fri Oct 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-3mdk
- Fix requires tcptl

* Tue Oct 12 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-2mdk
- Deprecated mdk < 9.2

* Fri Oct 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-1mdk
- 3.3.1

* Thu Sep 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-4mdk
- Fix menu entry
- Fix thinkpad lib

* Wed Sep 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-3mdk
- Update from kde3.3 branch

* Sat Sep 11 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-2mdk
- Don't strip klaptop_acpi_helper

* Fri Sep 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-1mdk
- 3.3.0

* Fri Sep 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-25mdk
- Add patch16: fix kdf backgound

* Thu Sep 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-24mdk
- Remove kwiskdisk from autostart use kdebase to init it

* Thu Sep 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-23mdk
- Autostart kwikdisk

* Wed Sep 01 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-22mdk
- Sync with CVS (kcalc fix BUG 74657 BUG 78726)

* Sat Aug 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-21mdk
- Add patch15: fix kcalc kde bug 81485 "Enable/disable "MR" depending if 
				there is a value in memory or not"

* Sat Aug 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-20mdk
- Update kcmlaptoprc (file from Erwan)

* Thu Aug 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-19mdk
- Add patch14: fix kcalc kde bug #74657

* Wed Aug 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-18mdk
- Add requires on cpufreq for klaptop

* Wed Aug 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-17mdk
- Add default config for kcmlaptop

* Sat Aug 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-16mdk
- Add patch12: fix kfloppy progressbar
- Add patch13: fix kfloppy "Fix ext2 formatting (missing device name)"

* Fri Aug 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-15mdk
- Split klaptop

* Sat Aug 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-14mdk
- Fix menu

* Sat Aug 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-13mdk
- Add patch11: fix kfloppy kde bug #81545 "(msdos or ext2) work after
											the low-level formatting."

* Fri Aug 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-12mdk
- Add patch10: fix kloppy "360KB has only 40 tracks (see /etc/fdprm)"

* Sat Aug 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-11mdk
- Remove debug

* Thu Aug 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-10mdk
- Add patch9: fix kgpg mem leak

* Wed Aug 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-9mdk
- Fix buildrequires

* Tue Aug 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-8mdk
- Sync with CVS fix klatopdemon

* Sat Jul 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-7mdk
- Sync with CVS

* Thu Jul 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-6mdk
- Fix remove rpath

* Tue Jul 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-5mdk
- Add patch7 fix kchartselect applet bug kde #58820

* Fri Jul 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-4mdk
- Add patch6 fix kdelirc devices fix MDK kde bug #9973

* Wed Jul 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-3mdk
- Rebuild with new kdelibs

* Tue Jul 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-2mdk
- Add patch5: fix ark open recent action

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Thu Jun 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-4mdk
- Rebuild with debug

* Wed May 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-3mdk
- Fix obsolete

* Fri Apr 23 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-2mdk
- Add patch4: fix ark

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Fri Apr 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-3mdk
- Rebuild

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-2mdk
- Fix spec file for using rpmbuildupdate

* Fri Apr 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-1mdk
- kde 3.2.1

* Wed Mar 31 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-19mdk
- Use %%configure
- Use mdkverion
- Add support for 10.1

