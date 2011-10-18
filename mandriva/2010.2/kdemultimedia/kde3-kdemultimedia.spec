%define _requires_exceptions devel\(libnoatunarts\)\\|libnoatunarts.so\\|devel\(libnoatunarts\(.*\)\\|libwinskinvis.so\\|libartseffects.so\\|libmpeg-0.3.0.so\\|libyafcore.so\\|libyafxplayer.so\\|devel\(libartsbuilder\)

%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define lib_name_orig lib%{name}
%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}
%define oname kdemultimedia

Name: kde3-%{oname}
Summary: K Desktop Environment - Multimedia
Version: 3.5.12
Release: %mkrel 1
Epoch: 1
Group: Graphical desktop/KDE3
License: GPL
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
#Patch0: mandriva_fixes.patch
Patch1: kde-3.5.10-acinclude.patch
#Patch2: fix_autotools.patch
Patch3: kdebase-3.5.12-move-xdg-menu-dir.patch
Patch4: kdebase-3.5.12-config.patch
BuildRequires: kde3-macros
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%endif
BuildRequires: autoconf >= 1:2.65
BuildRequires: automake > 1.5
BuildRequires: cdparanoia 
BuildRequires: musicbrainz-devel
BuildRequires: mad-devel 
BuildRequires: oggvorbis-devel
BuildRequires: libxine-devel 
BuildRequires: taglib-devel >= 1.5
BuildRequires: libflac++-devel
BuildRequires: libtunepimp-devel 
BuildRequires: libtheora-devel
BuildRequires: libcdda-devel
BuildRequires: libflac++-devel
BuildRequires: liboggflac++-devel
BuildRequires: libspeex-devel
BuildRequires: libsamplerate-devel
BuildRequires: X11-devel
BuildRequires: qt3-devel
BuildRequires: kdelibs-devel
BuildRequires: akode-devel
BuildRequires: libfreebob-devel
BuildRoot:	%_tmppath/%name-%version-%release-root
Provides: kdemultimedia = %epoch:%version-%release
Provides: kdemultimedia3 = %epoch:%version-%release
Obsoletes: kdemultimedia
Obsoletes: kdemultimedia3
Conflicts: %{mklibname kdemultimedia 1}-noatun <= %epoch:3.2-14mdk
# Don't add kdemultimedia-arts package on meta provides
# This package have offensive mcop files and is usefull just
# if you want develop new synthesizer objects with artsbuilder 
Requires: kdemultimedia-common = %epoch:%version-%release
Requires: kdemultimedia-kmix = %epoch:%version-%release
Requires: kdemultimedia-kmid = %epoch:%version-%release
Requires: kdemultimedia-kaudiocreator = %epoch:%version-%release
Requires: kdemultimedia-kscd = %epoch:%version-%release
Requires: kdemultimedia-kaboodle = %epoch:%version-%release
Suggests: kdemultimedia-noatun = %epoch:%version-%release

%description
Multimedia tools for the K Desktop Environment.
	- noatun: a multimedia player for sound and movies, very extensible due 
			  to it's plugin interface
	- kaudiocreator: CD ripper and audio encoder frontend.
	- kaboodle: light media player
	- kmid: A standalone and embeddable midi player, includes a karaoke-mode
	- kmix: the audio mixer as a standalone program and Kicker applet
	- kscd: A CD player with an interface to the internet CDDB database
	- krec: A recording frontend using aRts

%files

#-------------------------------------------------------------------------

%package common
Summary:	Common files for kdemultimedia
Group:		Graphical desktop/KDE3
Requires:	%lib_name-common = %epoch:%version-%release
Requires:	arts, vorbis-tools
Obsoletes:	kdemultimedia3-common
Obsoletes:      kdemultimedia-common
Provides:	kdemultimedia3-common = %epoch:%version-%release
Provides:       kdemultimedia-common = %epoch:%version-%release
Obsoletes:	kdemultimedia-aktion < 1:3.5.9
Conflicts:	%{mklibname kdemultimedia 1}-kscd-devel <= 3.1.3-16mdk
Conflicts:  %{mklibname kdemultimedia 1}-noatun <= 3.2-14mdk
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires: kde-config-file

%description common
Common files for kdemultimedia


%files common
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kioslave/audiocd.docbook
%_kde3_bindir/yaf-cdda
%_kde3_bindir/yaf-mpgplay
%_kde3_bindir/yaf-splay
%_kde3_bindir/yaf-tplay
%_kde3_bindir/yaf-vorbis
%_kde3_bindir/yaf-yuv
%_kde3_libdir/kde3/kfile_*.la
%_kde3_libdir/kde3/kfile_*.so
%_kde3_libdir/kde3/kcm_audiocd.*
%_kde3_libdir/kde3/kio_audiocd.*
%_kde3_appsdir/konqueror/servicemenus/audiocd_play.desktop
%_kde3_appsdir/konqueror/servicemenus/audiocd_extract.desktop
%_kde3_datadir/desktop-directories/kde-multimedia-music.directory
%_kde3_appsdir/kconf_update/audiocd.upd
%_kde3_appsdir/kconf_update/upgrade-metadata.sh
%_kde3_datadir/applications/kde/audiocd.desktop
%_kde3_iconsdir/*/*/*/arts*
%dir %_kde3_appsdir/videothumbnail/
%_kde3_appsdir/videothumbnail/*
%_kde3_datadir/services/audiocd.protocol
%_kde3_datadir/services/kfile_*
%_kde3_libdir/kde3/videothumbnail.*
%_kde3_libdir/kde3/libaudiocd_*
%_kde3_appsdir/kappfinder/apps/Multimedia/*.desktop
%_kde3_datadir/services/videothumbnail.desktop
%_kde3_datadir/config.kcfg/audiocd_lame_encoder.kcfg
%_kde3_datadir/config.kcfg/audiocd_vorbis_encoder.kcfg

#-------------------------------------------------------------------------

%package -n %lib_name-common-devel
Summary:	Header files for kdemultimedia
Group:		Development/KDE and Qt
Requires:       %lib_name-common = %epoch:%version-%release
Obsoletes:  kdemultimedia3-devel
Provides:   kdemultimedia3-devel = %epoch:%version-%release
Provides:   kdemultimedia-devel = %epoch:%version-%release
Provides:   %{mklibname kdemultimedia 1} = %epoch:%version-%release
Provides:   %{mklibname kdemultimedia3 1} = %epoch:%version-%release
Obsoletes:  kdemultimedia-devel
Obsoletes:  %{mklibname kdemultimedia 1}
Obsoletes:  %{mklibname kdemultimedia3 1}
Obsoletes:  %lib_name-devel < 1:3.5.9
Provides:   %lib_name-devel = %epoch:%version-%release
Provides:   %lib_name_orig-common-devel = %epoch:%version-%release
Conflicts:  %{mklibname kdemultimedia 1}-kscd-devel <= %epoch:3.4.2-10mdk
Conflicts:  %{mklibname kdemultimedia 1}-noatun <= %epoch:3.2-14mdk

%description -n %lib_name-common-devel
Header files needed for developing kdemultimedia applications.

%files -n %lib_name-common-devel
%defattr(-,root,root,-)
%_kde3_includedir/*
%_kde3_libdir/libaudiocdplugins.so
%_kde3_libdir/libmpeg.so
%_kde3_libdir/libkcddb.so
%_kde3_libdir/libkmidlib.so
%_kde3_libdir/libmpeg-0.3.0.so
%_kde3_libdir/libyafxplayer.so
%_kde3_libdir/libyafcore.so
%_kde3_libdir/libmpeg.la
%_kde3_libdir/libyafcore.la
%_kde3_libdir/libyafxplayer.la
%_kde3_libdir/libarts_*.so
%exclude %_kde3_includedir/noatun
%exclude %_kde3_includedir/arts

#-------------------------------------------------------------------------

%package -n %lib_name-common
Summary:	Libraries files for kdemultimedia
Group:         System/Libraries
Obsoletes: %lib_name < 1:3.5.9
Obsoletes:  %{mklibname kdemultimedia 1}-common
Obsoletes:  %{mklibname kdemultimedia3 1}-common
Provides: %lib_name = %epoch:%version-%release
Provides: %lib_name_orig-common = %epoch:%version-%release
Provides:   %{mklibname kdemultimedia 1}-common = %epoch:%version-%release
Provides:   %{mklibname kdemultimedia3 1}-common = %epoch:%version-%release
Conflicts: %{mklibname kdemultimedia 1}-kscd-devel <= 3.1.3-16mdk
Conflicts: kdemultimedia-common < %epoch:3.5.3-8mdv2007.0

%description -n %lib_name-common
Libraries files needed for developing kdemultimedia applications.

%files -n %lib_name-common
%defattr(-,root,root,-)
%_kde3_libdir/libkmidlib.la
%_kde3_libdir/libkmidlib.so.*
%_kde3_libdir/libkcddb.la
%_kde3_libdir/libkcddb.so.*
%_kde3_libdir/libaudiocdplugins.la
%_kde3_libdir/libaudiocdplugins.so.*
%_kde3_libdir/mcop/xine*
%_kde3_libdir/libarts_xine.so.*
%_kde3_libdir/libarts_xine.la
%_kde3_libdir/mcop/akode*
%_kde3_libdir/libarts_akode.so.*
%_kde3_libdir/libarts_akode.la
%_kde3_libdir/mcop/audiofile*
%_kde3_libdir/libarts_audiofile.so.*
%_kde3_libdir/libarts_audiofile.la
%_kde3_bindir/mpeglibartsplay
%_kde3_libdir/libarts_mpeglib*.so.*
%_kde3_libdir/libarts_mpeglib*.la
%_kde3_libdir/libarts_splay.so.*
%_kde3_libdir/libarts_splay.la
%_kde3_libdir/mcop/CDDAPlayObject.mcopclass
%_kde3_libdir/mcop/MP3PlayObject.mcopclass
%_kde3_libdir/mcop/NULLPlayObject.mcopclass
%_kde3_libdir/mcop/OGGPlayObject.mcopclass
%_kde3_libdir/mcop/SplayPlayObject.mcopclass
%_kde3_libdir/mcop/WAVPlayObject.mcopclass

#-------------------------------------------------------------------------

%package juk
Summary:       Jukebox and music manager for the KDE desktop
Group:         Graphical desktop/KDE3
Requires:      kdemultimedia-common = %epoch:%version-%release
Obsoletes:  kdemultimedia-juk
Obsoletes:  kdemultimedia3-juk
Provides:   kdemultimedia3-juk = %epoch:%version-%release
Provides:   kdemultimedia-juk = %epoch:%version-%release
Provides:	kde3-juk = %epoch:%version-%release
Conflicts:  %{mklibname kdemultimedia 1}-kscd-devel <= 3.1.3-16mdk
Conflicts:  %{mklibname kdemultimedia 1}-noatun <= 3.2-14mdk
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description juk
JuK is a jukebox and music manager for the KDE desktop similar to 
jukebox software on other platforms such as iTunes or RealOne. 
Its features include support for Ogg Vorbis and MP3 formats, 
tag editing support for both formats (including ID3v2 for MP3 files), 
output to aRts or GStreamer, multiple playlists, and lots of other 
groovy stuff.


%files juk
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/juk
%_kde3_bindir/juk
%_kde3_datadir/applications/kde/juk.desktop
%_kde3_iconsdir/*/*/*/juk*
%dir %_kde3_appsdir/juk
%_kde3_appsdir/juk/*
%_kde3_appsdir/konqueror/servicemenus/jukservicemenu.desktop

#-------------------------------------------------------------------------

%package kmix
Summary:       Kmix, kmixctrl program
Group:         Graphical desktop/KDE3
Obsoletes:  kdemultimedia-kmix
Obsoletes:  kdemultimedia3-kmix
Provides:   kdemultimedia3-kmix = %epoch:%version-%release
Provides:   kdemultimedia-kmix = %epoch:%version-%release
Provides:	kde3-kmix = %epoch:%version-%release
Provides: 	kde3-kmixctrl = %epoch:%version-%release
Conflicts:  %{mklibname kdemultimedia 1}-kscd-devel <= 3.1.3-16mdk
Conflicts:  %{mklibname kdemultimedia 1}-noatun <= 3.2-14mdk
Requires:	arts
Requires:	 alsa-utils
Obsoletes:	%lib_name-kmix < 1:3.5.9

%description kmix
The audio mixer as a standalone program and Kicker applet


%files kmix
%defattr(-,root,root,-)
%_kde3_bindir/kmix
%_kde3_bindir/kmixctrl
%doc %_kde3_docdir/HTML/en/kmix
%_kde3_libdir/kde3/kmix*.so
%_kde3_libdir/kde3/kmix*.la
%_kde3_datadir/autostart/restore_kmix_volumes.desktop
%_kde3_iconsdir/*/*/*/kmix*
%_kde3_datadir/services/kmixctrl_restore.desktop
%_kde3_datadir/applications/kde/kmix.desktop
%dir %_kde3_appsdir/kmix/
%_kde3_appsdir/kmix/*
%_kde3_appsdir/kicker/applets/kmixapplet.desktop
%_kde3_libdir/libkdeinit_kmix.*
%_kde3_libdir/libkdeinit_kmixctrl.*

#-------------------------------------------------------------------------

%package krec
Summary:       Krec program
Group:         Graphical desktop/KDE3
Requires:	%lib_name-common = %epoch:%version-%release
Conflicts:      kdemultimedia <= 3.1-10mdk
Obsoletes:  kdemultimedia-krec
Obsoletes:  kdemultimedia3-krec
Provides:   kdemultimedia3-krec = %epoch:%version-%release
Provides:   kdemultimedia-krec = %epoch:%version-%release
Provides:	kde3-krec = %epoch:%version-%release
Conflicts:  %{mklibname kdemultimedia 1}-kscd-devel <= 3.1.3-16mdk
Conflicts:  %{mklibname kdemultimedia 1}-noatun <= 3.2-14mdk
Obsoletes: %lib_name-krec < 1:3.5.9

%description krec
A recording frontend using aRts


%files krec
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/krec
%_kde3_bindir/krec
%dir %_kde3_appsdir/krec/
%_kde3_appsdir/krec/*
%_kde3_datadir/applications/kde/krec.desktop
%_kde3_iconsdir/*/*/*/krec.*
%_kde3_libdir/kde3/kcm_krec_files.*
%_kde3_libdir/kde3/krec.*
%_kde3_libdir/kde3/kcm_krec.*
%_kde3_libdir/kde3/libkrecexport_*
%_kde3_libdir/libkdeinit_krec.*
%_kde3_datadir/services/krec_*
%_kde3_datadir/services/kcm_krec*
%_kde3_datadir/servicetypes/krec_*

#-------------------------------------------------------------------------

%package kscd
Summary:       Kscd program
Group:         Graphical desktop/KDE3
Obsoletes:  kdemultimedia-kscd
Obsoletes:  kdemultimedia3-kscd
Provides:   kdemultimedia3-kscd = %epoch:%version-%release
Provides:   kdemultimedia-kscd = %epoch:%version-%release
Provides:	kde3-kscd = %epoch:%version-%release
Conflicts:  %{mklibname kdemultimedia 1}-kscd-devel <= 3.1.3-16mdk
Conflicts:  %{mklibname kdemultimedia 1}-noatun <= 3.2-14mdk
Requires:	arts
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes: %lib_name-kscd < 1:3.5.9
Obsoletes: %lib_name-kscd-devel < 1:3.5.9

%description kscd
A CD player with an interface to the internet CDDB database


%files kscd
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/kscd
%_kde3_bindir/kscd
%_kde3_bindir/workman2cddb.pl
%_kde3_iconsdir/*/*/*/kscd*
%_kde3_datadir/config.kcfg/kscd.kcfg
%_kde3_datadir/config.kcfg/libkcddb.kcfg
%_kde3_datadir/applications/kde/libkcddb.desktop
%_kde3_datadir/applications/kde/kscd.desktop
%dir %_kde3_appsdir/kscd/
%_kde3_appsdir/kscd/*
%_kde3_appsdir/profiles/kscd.profile.xml
%_kde3_appsdir/kconf_update/kcmcddb-emailsettings.upd
%_kde3_libdir/kde3/kcm_cddb.*
%_kde3_datadir/mimelnk/text/xmcd.desktop

#-------------------------------------------------------------------------

%package kmid
Summary:       Kmid program
Group:         Graphical desktop/KDE3
Obsoletes:  kdemultimedia-kmid
Obsoletes:  kdemultimedia3-kmid
Obsoletes:  kdemultimedia-kmidi
Obsoletes:  kdemultimedia3-kmidi
Provides:   kdemultimedia3-kmid = %epoch:%version-%release
Provides:   kdemultimedia-kmid = %epoch:%version-%release
Provides:   kdemultimedia3-kmidi = %epoch:%version-%release
Provides:   kdemultimedia-kmidi = %epoch:%version-%release
Provides: kde3-kmid = %epoch:%version-%release
Provides: kde3-kmidi = %epoch:%version-%release
Conflicts:  %{mklibname kdemultimedia 1}-kscd-devel <= 3.1.3-16mdk
Conflicts:  %{mklibname kdemultimedia 1}-noatun <= 3.2-14mdk
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description kmid
Kmid program


%files kmid
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/kmid
%_kde3_bindir/kmid
%_kde3_iconsdir/*/*/*/kmid.*
%_kde3_libdir/kde3/libkmidpart.*
%dir %_kde3_appsdir/kmid/
%_kde3_appsdir/kmid/*
%_kde3_datadir/mimelnk/audio/x-karaoke.desktop
%_kde3_datadir/servicetypes/audiomidi.desktop
%_kde3_datadir/applications/kde/kmid.desktop

#-------------------------------------------------------------------------

%package kaudiocreator
Summary:       Kaudiocreator program
Group:         Graphical desktop/KDE3
Obsoletes:  kdemultimedia-kaudiocreator
Obsoletes:  kdemultimedia3-kaudiocreator
Provides:   kdemultimedia3-kaudiocreator = %epoch:%version-%release
Provides:   kdemultimedia-kaudiocreator = %epoch:%version-%release
Provides:	kde3-kaudiocreator = %epoch:%version-%release
Conflicts:  %{mklibname kdemultimedia 1}-kscd-devel <= 3.1.3-16mdk
Conflicts:  %{mklibname kdemultimedia 1}-noatun <= 3.2-14mdk
Requires:	arts
Requires:	%lib_name-common = %epoch:%version-%release
Requires:	kdemultimedia-common = %epoch:%version-%release
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description kaudiocreator
CD ripper and audio encoder frontend.



%files kaudiocreator
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/kaudiocreator
%_kde3_bindir/kaudiocreator
%_kde3_datadir/applications/kde/kaudiocreator.desktop
%dir %_kde3_appsdir/kaudiocreator/
%_kde3_appsdir/kaudiocreator/*
%_kde3_iconsdir/*/*/*/kaudiocreator*
%_kde3_appsdir/kconf_update/kaudiocreator-libkcddb.upd
%_kde3_datadir/config.kcfg/kaudiocreator.kcfg
%_kde3_datadir/config.kcfg/kaudiocreator_encoders.kcfg
%_kde3_appsdir/kconf_update/kaudiocreator-meta.upd
%_kde3_appsdir/kconf_update/upgrade-kaudiocreator-metadata.sh

#-------------------------------------------------------------------------

%package kaboodle
Summary: Kaboodle program
Group: Graphical desktop/KDE3
Obsoletes:  kdemultimedia-kaboodle
Obsoletes:  kdemultimedia3-kaboodle
Provides:   kdemultimedia3-kaboodle = %epoch:%version-%release
Provides:   kdemultimedia-kaboodle = %epoch:%version-%release
Provides: kde3-kaboodle = %epoch:%version-%release
Conflicts: %{mklibname kdemultimedia 1}-kscd-devel <= 3.1.3-16mdk
Conflicts: %{mklibname kdemultimedia 1}-noatun <= 3.2-14mdk
Requires: arts
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes: %lib_name-kaboodle < 1:3.5.9

%description kaboodle
Light media player


%files kaboodle
%defattr(-,root,root,-)
%doc %_kde3_docdir/HTML/en/kaboodle
%_kde3_bindir/kaboodle
%_kde3_datadir/services/kaboodle*
%_kde3_datadir/applications/kde/kaboodle.desktop
%_kde3_iconsdir/*/*/*/kaboodle*
%_kde3_libdir/kde3/libkaboodlepart.*
%dir %_kde3_appsdir/kaboodle/
%_kde3_appsdir/kaboodle/*

#-------------------------------------------------------------------------

%package arts
Summary: Arts synth control programs
Group: Graphical desktop/KDE3
Obsoletes:  kdemultimedia-arts
Obsoletes:  kdemultimedia3-arts
Provides:   kdemultimedia3-arts = %epoch:%version-%release
Provides:   kdemultimedia-arts = %epoch:%version-%release
Requires: %lib_name-arts = %epoch:%version-%release
Requires: %lib_name-common = %epoch:%version-%release
Conflicts: %lib_name-common < %epoch:3.5.3-7mdv2007.0

%description arts
A synthesizer control programs


%files arts
%defattr(-,root,root,-)
%_kde3_bindir/artsbuilder
%_kde3_bindir/artscontrol
%_kde3_bindir/midisend
%dir %_kde3_appsdir/artsbuilder
%_kde3_appsdir/artsbuilder/*
%dir %_kde3_appsdir/artscontrol
%_kde3_appsdir/artscontrol/*
%doc %_kde3_docdir/HTML/en/artsbuilder
%_kde3_appsdir/kicker/applets/artscontrolapplet.desktop
%_kde3_datadir/mimelnk/application/x-artsbuilder.desktop
%_kde3_datadir/applications/kde/artsbuilder.desktop
%_kde3_datadir/applications/kde/artscontrol.desktop
%dir %_kde3_libdir/mcop/Arts
%_kde3_libdir/mcop/Arts/*

#-------------------------------------------------------------------------

%package -n %lib_name-arts
Summary:   Library for arts program
Group:     System/Libraries
Obsoletes:  %{mklibname kdemultimedia 1}-arts
Obsoletes:  %{mklibname kdemultimedia3 1}-arts
Provides: %lib_name_orig-arts = %epoch:%version-%release
Provides:   %{mklibname kdemultimedia 1}-arts = %epoch:%version-%release
Provides:   %{mklibname kdemultimedia3 1}-arts = %epoch:%version-%release
Conflicts: %lib_name-common < %{epoch}:3.5.3-5mdv2007.0

%description -n %lib_name-arts
Library for arts program


%files -n %lib_name-arts
%defattr(-,root,root,-)
%_kde3_libdir/mcop/artsmodulescommon.*
%_kde3_libdir/mcop/artsbuilder.*
%_kde3_libdir/mcop/artsmodules.*
%_kde3_libdir/mcop/artsmodulesmixers.*
%_kde3_libdir/mcop/artsmodulessynth.*
%_kde3_libdir/mcop/artsmoduleseffects.*
%_kde3_libdir/mcop/artsmidi.*
%_kde3_libdir/mcop/artsgui.*
%_kde3_libdir/libartsbuilder.la
%_kde3_libdir/libartsbuilder.so.*
%_kde3_libdir/libartscontrolapplet.la
%_kde3_libdir/libartscontrolapplet.so.*
%_kde3_libdir/libartscontrolsupport.la
%_kde3_libdir/libartscontrolsupport.so.*
%_kde3_libdir/libartsgui_idl.la
%_kde3_libdir/libartsgui_idl.so.*
%_kde3_libdir/libartsgui_kde.la
%_kde3_libdir/libartsgui_kde.so.*
%_kde3_libdir/libartsgui.la
%_kde3_libdir/libartsgui.so.*
%_kde3_libdir/libartsmidi_idl.la
%_kde3_libdir/libartsmidi_idl.so.*
%_kde3_libdir/libartsmidi.la
%_kde3_libdir/libartsmidi.so.*
%_kde3_libdir/libartsmodulescommon.la
%_kde3_libdir/libartsmodulescommon.so.*
%_kde3_libdir/libartsmoduleseffects.la
%_kde3_libdir/libartsmoduleseffects.so.*
%_kde3_libdir/libartsmodules.la
%_kde3_libdir/libartsmodulesmixers.la
%_kde3_libdir/libartsmodulesmixers.so.*
%_kde3_libdir/libartsmodules.so.*
%_kde3_libdir/libartsmodulessynth.la
%_kde3_libdir/libartsmodulessynth.so.*

#-------------------------------------------------------------------------

%package -n %lib_name-arts-devel
Summary: Devel headers and libraries for arts program
Group: Development/KDE and Qt
Conflicts: %lib_name-common-devel < %epoch:3.5.3-7mdv2007.0
Obsoletes:  %{mklibname kdemultimedia 1}-arts-devel
Obsoletes:  %{mklibname kdemultimedia3 1}-arts-devel
Provides: %lib_name_orig-arts-devel = %epoch:%version-%release
Provides:   %{mklibname kdemultimedia 1}-arts-devel = %epoch:%version-%release
Provides:   %{mklibname kdemultimedia3 1}-arts-devel = %epoch:%version-%release
Requires: %lib_name-arts = %epoch:%version-%release

%description -n %lib_name-arts-devel
Devel headers and libraries for arts

%files -n %lib_name-arts-devel
%defattr(-,root,root,-)
%_kde3_libdir/libartsbuilder.so
%_kde3_libdir/libartscontrolapplet.so
%_kde3_libdir/libartscontrolsupport.so
%_kde3_libdir/libartsgui_idl.so
%_kde3_libdir/libartsgui_kde.so
%_kde3_libdir/libartsgui.so
%_kde3_libdir/libartsmidi_idl.so
%_kde3_libdir/libartsmidi.so
%_kde3_libdir/libartseffects.so
%_kde3_libdir/libartsmodulescommon.so
%_kde3_libdir/libartsmoduleseffects.so
%_kde3_libdir/libartsmodules.so
%_kde3_libdir/libartsmodulesmixers.so
%_kde3_libdir/libartsmodulessynth.so

#-------------------------------------------------------------------------

%package noatun
Summary:       Noatun program
Group:         Graphical desktop/KDE3
Obsoletes:  kdemultimedia-noatun
Obsoletes:  kdemultimedia3-noatun
Provides:   kdemultimedia3-noatun = %epoch:%version-%release
Provides:   kdemultimedia-noatun = %epoch:%version-%release
Requires:	%lib_name-noatun = %epoch:%version-%release
Requires:	%lib_name-common = %epoch:%version-%release
Conflicts:  %{mklibname kdemultimedia 1}-kscd-devel <= 3.1.3-16mdk
Conflicts:  %{mklibname kdemultimedia 1}-noatun <= 3.2-14mdk
Provides:	kde3-noatun = %epoch:%version-%release
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description noatun
A multimedia player for sound and movies, very extensible due to 
it's plugin interface


%files noatun
%defattr(-,root,root,-)
%_kde3_bindir/noatun
%doc %_kde3_docdir/HTML/en/noatun
%dir %_kde3_appsdir/noatun
%_kde3_appsdir/noatun/*
%_kde3_libdir/kde3/noatun*.*
%_kde3_iconsdir/*/*/*/noatun*
%_kde3_datadir/applications/kde/noatun.desktop
%_kde3_datadir/mimelnk/interface/x-winamp-skin.desktop
%_kde3_libdir/kconf_update_bin/noatun20update
%_kde3_appsdir/kconf_update/noatun.upd

#-------------------------------------------------------------------------

%package -n %lib_name-noatun
Summary:    Librarie for Noatun  program
Group:      System/Libraries
Conflicts:  kdemultimedia <= 3.1-10mdk
Obsoletes:  %{mklibname kdemultimedia 1}-noatun
Obsoletes:  %{mklibname kdemultimedia3 1}-noatun
Provides:   %{mklibname kdemultimedia 1}-noatun = %epoch:%version-%release
Provides:   %{mklibname kdemultimedia3 1}-noatun = %epoch:%version-%release
Provides:   %lib_name_orig-noatun = %epoch:%version-%release
Conflicts:  %{mklibname kdemultimedia 1}-kscd-devel <= 3.1.3-16mdk
Conflicts:  %{mklibname kdemultimedia 1}-noatun <= 3.2-14mdk
Conflicts:  %lib_name-common < %{epoch}:3.5.3-5mdv2007.0

%description -n %lib_name-noatun
Library for noatun program


%files -n %lib_name-noatun
%defattr(-,root,root,-)
%dir %_kde3_libdir/mcop/Noatun/
%_kde3_libdir/mcop/Noatun/*
%_kde3_libdir/mcop/artseffects.mcopclass            
%_kde3_libdir/mcop/VoiceRemoval.mcopclass
%_kde3_libdir/mcop/artseffects.mcoptype             
%_kde3_libdir/mcop/noatunarts.mcopclass  
%_kde3_libdir/mcop/winskinvis.mcopclass
%_kde3_libdir/mcop/ExtraStereoGuiFactory.mcopclass  
%_kde3_libdir/mcop/noatunarts.mcoptype   
%_kde3_libdir/mcop/winskinvis.mcoptype
%_kde3_libdir/mcop/ExtraStereo.mcopclass            
%_kde3_libdir/mcop/RawWriter.mcopclass
%_kde3_libdir/kde3/noatun*.so
%_kde3_libdir/kde3/noatun.la
%_kde3_libdir/libartseffects.la*
%_kde3_libdir/libnoatuncontrols.so.*
%_kde3_libdir/libnoatuntags.so.*
%_kde3_libdir/libnoatunarts.la*
%_kde3_libdir/libnoatun.la*
%_kde3_libdir/libwinskinvis.la*
%_kde3_libdir/libnoatun.so.*
%_kde3_libdir/libnoatuncontrols.la*
%_kde3_libdir/libnoatuntags.la*
%_kde3_libdir/libkdeinit_noatun.la
%_kde3_libdir/libkdeinit_noatun.so
%_kde3_libdir/libnoatunarts.so

#-------------------------------------------------------------------------

%package -n %lib_name-noatun-devel
Summary:    Devel files for Noatun  program
Group:      Development/KDE and Qt
Requires:   %lib_name-noatun = %epoch:%version-%release
Requires:   %lib_name-arts-devel = %epoch:%version-%release
Obsoletes:  %{mklibname kdemultimedia 1}-noatun-devel
Obsoletes:  %{mklibname kdemultimedia3 1}-noatun-devel
Provides:   %{mklibname kdemultimedia 1}-noatun-devel = %epoch:%version-%release
Provides:   %{mklibname kdemultimedia3 1}-noatun-devel = %epoch:%version-%release
Provides:   %lib_name_orig-noatun-devel = %epoch:%version-%release
Provides:   kde3-noatun-devel = %epoch:%version-%release
Conflicts:  %{mklibname kdemultimedia 1}-kscd-devel <= 3.1.3-16mdk
Conflicts:  %{mklibname kdemultimedia 1}-noatun <= 3.2-14mdk

%description -n %lib_name-noatun-devel
Devel files for noatun program

%files -n %lib_name-noatun-devel
%defattr(-,root,root,-)
%dir %_kde3_includedir/noatun/
%_kde3_includedir/noatun/*.h
%_kde3_libdir/libnoatuncontrols.so
%_kde3_libdir/libnoatun.so
%_kde3_libdir/libnoatuntags.so
%_kde3_libdir/libwinskinvis.so

#-------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
#%patch0 -p1
%if %mdkversion >= 201000
%patch1 -p1
#%patch2 -p1
%endif
%patch3 -p0
%patch4 -p0

%build
export QTDIR=%qt3dir

PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/
export xdg_menudir=%_sysconfdir/xdg/kde/menus

make -f admin/Makefile.common cvs

%configure_kde3 \
   --with-akode \
   --with-kscd-cdda

%make


%install
rm -fr %buildroot

%makeinstall_std

# David - 2.2-0.beta1.1mdk - Remove some non legal songs
for i in %buildroot/%_kde3_appsdir/kmidi/*.mid ; do rm -f $i ; done

install -d -m 0775 %buildroot/%_kde3_datadir/config/
%__rm -fr %buildroot%_sysconfdir/xdg/kde/menus/applications-merged/kde-multimedia-music.menu 

%clean
rm -fr %buildroot


%changelog
* Thu Jul 21 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-1mvt2010.2
+ Update to Trinity 3.5.12
- Remove fix autotools patch
+ Add kdebase-3.5.12-move-xdg-menu-dir.patch
+ Add kdebase-3.5.12-config.patch
- Remove mandriva_fixes.patch

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 1:3.5.10-3mvt2010.1
+ Rebuild for 2010.1

* Sat Nov 21 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-2mvt2010.0
- Rebuild for 2010.0
- Change package name to avoid KDE4 upgrade
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65:patch5
+ Fix automake 1.11 issue:patch6

* Fri Aug 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-1mdv2009.0
+ Revision: 277180
- Latest kde 3 upstream package

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:3.5.9-7mdv2009.0
+ Revision: 267778
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 11 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.9-6mdv2009.0
+ Revision: 217916
- Bump release
- add  patch to fix underlink (draft)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon May 19 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 1:3.5.9-5mdv2009.0
+ Revision: 208986
- User versioned obsoletes and fixed some provides versions

* Wed May 07 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-4mdv2009.0
+ Revision: 202886
- Move for /opt

* Sat Mar 22 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-3mdv2008.1
+ Revision: 189495
- Fix groups ( tks to pterjan)

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:3.5.9-2mdv2008.1
+ Revision: 170920
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-1mdv2008.1
+ Revision: 169027
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches integrated
- Removed config s that was already applied on mandriva-kde-config

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-not-capitalized

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 24 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-2mdv2008.1
+ Revision: 137371
- Rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 28 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-1mdv2008.1
+ Revision: 102848
- Kde 3.5.8
  Remove merged patches
- KDE 3.5.8
  Remove merged patches

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-ended-with-dot

* Wed Oct 03 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-9mdv2008.0
+ Revision: 95073
- Do not require noatun, just suggest it

* Thu Sep 20 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 1:3.5.7-8mdv2008.0
+ Revision: 91351
- Rebuilt.

* Wed Sep 19 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-6mdv2008.0
+ Revision: 90804
- Do not package kde-multimedia-music.menu (Bug #32473)

* Fri Aug 10 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-5mdv2008.0
+ Revision: 61479
- Add 2 upstream xpatches from BRANCH
- Add some upstream patches from BRANCH
  Add comments on some already existing patches

* Thu Aug 09 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-4mdv2008.0
+ Revision: 60840
- Fix menu entries
- Add upstream patches from KDE3_5 BRANCH
- Add Patch3: Fix invalid desktop files

* Mon Jun 04 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.7-3mdv2008.0
+ Revision: 34993
- More provides for kdemultimedia-arts-devel

* Wed May 16 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-1mdv2008.0
+ Revision: 27449
- 3.5.7 release


* Wed Mar 21 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-2mdv2007.1
+ Revision: 147391
- Disable this patch
- 3.5.63.5.63.5.6

* Mon Nov 06 2006 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.5-4mdv2007.1
+ Revision: 76996
- Yes, looks like build on chroot is working ! Add missing requires for
  kdelibs-devel ( are strangely kdelibs-common ) and buildrequires for qt3-devel
- Adde missing buildreq X11-devel. Thanks to Anssi Hannula.

  + Laurent Montel <lmontel@mandriva.com>
    - Fix buildrequries
    - Rebuild
    - Add packager tag
    - 3.5.5

* Wed Sep 13 2006 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.4-6mdv2007.0
+ Revision: 61140
- Adde priority change on kscd. Removed audiodevice default ( kscd will base on
  priority guess )

* Fri Sep 08 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-5mdv2007.0
+ Revision: 60456
- New package (2006-09-07 3.5.4-5mdv)
  Fix upgrade 2006->2007

* Thu Sep 07 2006 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.4-4mdv2007.0
+ Revision: 60395
- Fix from upstream to bug http://qa.mandriva.com/show_bug.cgi?id=21221
  Thanks to peroyvind for point this one

* Fri Aug 25 2006 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.4-3mdv2007.0
+ Revision: 57781
- Add last part of kcontrol patch
- Fix last cd-xa patch
- Added defaults patches for kio_audiocd
- kmix fix from kde branch tree
- cd-xa fix from kde branch tree

* Sun Aug 06 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-1mdv2007.0
+ Revision: 53212
- New package (2006/08/05 3.5.4-1mdv)

  + Helio Chissini de Castro <helio@mandriva.com>
    - Updated for latest official kde 3.5.4 release

* Fri Jul 28 2006 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.3-10mdv2007.0
+ Revision: 42303
- Fixed audiofilearts plugin load. Users with libkdemultimedia-common package
  installed will suffer a crash with last package

* Sat Jul 22 2006 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.3-9mdv2007.0
+ Revision: 41896
- The broken mcop interface was moved for new kdemultimedia-arts package. To
  keep compatibility, the packages libkdemultimedia-arts and
  libkdemultimedia-arts-devel was created. The arts output packages, splitted on
  last login was reverted to main common package, since there's no need for this
  specific split.
  The reason why package kdemultimedia-arts with the broken mcop ifaces is still
  enabled comes from the use of arts as a music synthesizer, effects processor,
  but not used frequently by users. Installing this specific package will make
  kde audio notifications crash artsd.
  The kdemultimedia meta package not install kdemultimedia arts package.
  TODO: Remove kdemultimedia-arts functionality ?
- kdemultimedia arts mcop modules are causing major arts crashes, mainly on
  system notification, so the decision to split package was necessary. New packages created:
- kdemutimedia-arts-akode
- kdemutimedia-arts-xine
- kdemutimedia-arts-mpeglib
- kdemutimedia-arts-audiofile
- kdemutimedia-arts
- libkdemultimedia1-arts
  Next path is trace which is the offender mcop library on package kdemultimedia-arts that crashes
  system audio notification ( and recursive crashes on arts ), then disable it and make noatun
  available for meta package kdemultimedia again. Users installing noatun today will
  suffer from arts notification crashes. The problem is upstream and should be
  fixed locally since there are no plans to change arts architecture on last 3.x
  kde releases

* Fri Jul 21 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.3-6mdv2007.0
+ Revision: 41704
- Disable debug
- Use macro
- Add requires(post) to fix upgrade
--enable-new-ldflags doesn't work on x86_64
- Fix setuid
- Allow to build on 2006
- 3.5.3
- Rebuild against new xorg
- Rebuild to add category
- Move xdg menu directory
- Add missing files
- 3.5.2
- 3.5.1
- MDK9.2 is obsolete now
- Fix buildrequires for mdk <=2006
- Add libfreebob-devel as buildrequires
- Sync with kde3.5 branch
- Sync with kde3.5 branch
- Fix buildrequires
- Fix file list
- Use akode to compile kdemultimedia
- Real kde3.5
- 3.5.0
- Fix spec file
- Move libyafcore.so into kdemultimedia-common
  (not sure that it's the good method)
- Fix typo
- 3.4.92
- Remove requires on libnoatunarts.so
- Rebuild
- Fix kscd autostart
- Fix compile under x86_64
- Add direct audio device by default patch from  fundawang
- New sync (kaudiocreator fixes)
- New sync
- Fix kscd crash kde bug #17468
- Remove debug
  Fix diff from 3.4.2 branch
- 3.4.2

  + Helio Chissini de Castro <helio@mandriva.com>
    - Clean and rearrange spec file
    - Added tarball from kde branch as discussed on meeting in 28/06
    - Removed rpath and added configure macro invalidating libtoolize
    - Added strip macro as stated by Nanar ( for unstable builds )
    - Removed unused and invalid patches
    - Standard menu reenabled for now. ( Waiting final changes on new menu )
    - Fixed noatun file list ( thanks neoclust )
    - Obsolete kmidi package and added kpart on kmid package ( timidy not exists
      anymore on kde package )
    - Make remaining patches bunzipped
    - Uploading package ./kdemultimedia

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 05 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-7mdk
- Rebuild

* Fri Apr 22 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-6mdk
- Add missing buildrequires found by Christiaan Welvaart <cjw@daneel.dyndns.org>

* Mon Apr 18 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-5mdk
- Oops fix exception

* Mon Apr 18 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-4mdk
- Fix depend
- Fix requires

* Thu Apr 14 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-3mdk
- Add  alsa-utils MDK #11144

* Wed Apr 13 2005 Laurent MONTEL <lmontel@mandriva.com>  3.4.0-2mdk
- Add patch32: fix kscd numeric acces

* Thu Apr 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0 
- Use --enable-new-ldflags
- Reactivate debug
- Fix exception

* Mon Mar 21 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-22mdk
- Add patch22: fix build with cdda

* Tue Mar 15 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-21mdk
- Add patch21: fix audiocd encoder "The quality setting is a double and not integer."

* Thu Mar 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-20mdk
- Requires kaudiocreator on kdemultimedia-common MDK #14450

* Fri Mar 04 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-19mdk
- Add patch20: fix kfile-flac crash

* Fri Feb 18 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-18mdk
- Fix juk : "Restore the playlist time display when stop is pressed."

* Mon Feb 14 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-17mdk
- Fix kscd config file (multimedia shortcut)
- Add jukrc shortcut file

* Fri Feb 11 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.3.2-16mdk
- fix build on x86_64

* Thu Feb 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-15mdk
- Add patch26: fix launch kscd with device

* Thu Feb 10 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-14mdk
- Disable debug

* Fri Jan 28 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-13mdk
- Fix generated menu entry

* Wed Jan 26 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-12mdk
- Fix MDK bug "Unknown Protocol 'audiocd'."

* Tue Jan 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-11mdk
- Add patch25: fix autostart restore kmix (disable by default as in config)

* Sat Jan 22 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-10mdk
- Add patch24: fix kscd kde bug #92164 (re read shortcut)

* Mon Jan 17 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-9mdk
- Add patch23: fix juk kde bug #97097

* Sat Jan 15 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-8mdk
- Rebuild

* Wed Dec 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-7mdk
- Add patch22: fix kaudiocreator path

* Tue Dec 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-6mdk
- Add missing buildrequires as requested by Per �yvind Karlsen (thanks)

* Fri Dec 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-5mdk
- Add patch21: fix kscd duplicate entry into shortcut

* Fri Dec 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-4mdk
- Add kscdrc to multimedia shortcut

* Fri Dec 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-3mdk
- Fix missing package

* Thu Dec 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-2mdk
- Fix menu

* Tue Nov 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Tue Nov 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-8mdk
- Fix other arts requires

* Mon Nov 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-7mdk
- Requires arts

* Thu Oct 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-6mdk
- Bye-bye %%buildfor

* Wed Oct 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-5mdk
- Fix create audiocd menu

* Fri Oct 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-4mdk
- Fix other buildrequires

* Sat Oct 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-3mdk
- Fix buildrequires

* Wed Oct 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-2mdk
- Deprecated mdk < 9.2
- Sync with CVS

* Fri Oct 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-1mdk
- 3.3.1

* Sat Oct 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-6mdk
- Rebuild with new taglib

* Wed Sep 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-4mdk
- Sync with kde 3.3 branch

* Wed Sep 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-3mdk
- Fix conflict

* Wed Sep 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-2mdk
- Sync with kde 3.3 branch (fix kscd)

* Fri Sep 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.0-1mdk
- 3.3.0

* Wed Sep 01 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-12mdk
- Fix kcddb install menu

* Thu Aug 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-11mdk
- Add patch19: add command line to kscd "kscd --device /dev/hdc" necessary
	for magicdev

* Sat Aug 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-10mdk
- Remove debug

* Thu Aug 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-9mdk
- Add patch18: fix kscd change device

* Sat Jul 31 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-8mdk
- Use musicbrain

* Fri Jul 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-7mdk
- Fix dependancy

* Sat Jul 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-6mdk
- Fix spec file

* Thu Jul 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-5mdk
- Fix remove rpath

* Wed Jul 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-4mdk
- Rebuild

* Wed Jun 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-3mdk
- Add patch17: fix patch on close
- Sync with CVS

* Sat Jun 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-2mdk
- Add missing buildrequires

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-6mdk
- Rebuild

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-5mdk
- Fix conflict

* Wed Jun 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-4mdk
- Rebuild with debug

* Sat May 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-3mdk
- Sync with CVS

* Fri May 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-2mdk
- Rebuild again qt 3.3.2

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.2-1mdk
- 3.2.2

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-3mdk
- Fix spec file for using rpmbuildupdate

* Sat Apr 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-2mdk
- Fix conflict reported by Titi

* Fri Apr 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

* Wed Mar 31 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-15mdk
- Use %%configure
- Use mdkversion

* Mon Mar 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-14mdk
- Fix patch16: don't load volume on statup

