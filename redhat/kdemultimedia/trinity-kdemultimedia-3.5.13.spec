# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
%define tde_appdir %{_datadir}/applications/kde
%define tde_docdir %{_docdir}
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity

# former extras bits
%define _with_akode --with-akode
## not currently compatible with libtunepimp-0.5 (only libtunepimp-0.4)
#define _with_musicbrainz --with-musicbrainz
%define _with_taglib --with-taglib

#%if 0%{?fedora}
%define _with_xine --with-xine
#%endif

Name:    trinity-tdemultimedia
Summary: Multimedia applications for the Trinity Desktop Environment (TDE)
Version: 3.5.13
Release: 8%{?dist}%{?_variant}

License: GPLv2
Group:   Applications/Multimedia

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kdemultimedia-%{version}.tar.gz

%if "%{_prefix}" == "/usr"
Provides: kdemultimedia3 = %{version}-%{release}
%endif

# RedHat Legacy patches (from Fedora 8)
Patch3: kdemultimedia-3.4.0-xdg.patch
Patch5: kdemultimedia-3.5.7-pthread.patch

# [kdemultimedia] Fix MMX detection [Bug #800]
Patch10:	kdemultimedia-3.5.13-fix_mmx_detection.patch
# [tdemultimedia] Remove "More Applications" from TDE menu. [Commit #31e44a7b]
Patch21:	kdemultimedia-3.5.13-remove_more_applications.patch
# [tdemultimedia] Fix linear alphabet string errors [Commit #fd6afacf]
Patch22:	kdemultimedia-3.5.13-fix_linear_alphabet.patch

Obsoletes:	trinity-kdemultimedia < %{version}-%{release}
Provides:	trinity-kdemultimedia = %{version}-%{release}
Obsoletes:	trinity-kdemultimedia-libs < %{version}-%{release}
Provides:	trinity-kdemultimedia-libs = %{version}-%{release}
Obsoletes:	trinity-kdemultimedia-extras < %{version}-%{release}
Provides:	trinity-kdemultimedia-extras = %{version}-%{release}
Obsoletes:	trinity-kdemultimedia-extras-libs < %{version}-%{release}
Provides:	trinity-kdemultimedia-extras-libs = %{version}-%{release}


BuildRequires: cmake >= 2.8
BuildRequires: tqtinterface-devel
BuildRequires: trinity-arts-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: qt3-devel >= 3.3.8.d

BuildRequires: zlib-devel
BuildRequires: libvorbis-devel
BuildRequires: audiofile-devel
BuildRequires: desktop-file-utils
BuildRequires: libtheora-devel
BuildRequires: flac-devel
BuildRequires: alsa-lib-devel 
BuildRequires: cdparanoia-devel cdparanoia
BuildRequires: gstreamer-devel
BuildRequires: automake libtool
%{?_with_akode:BuildRequires: trinity-akode-devel}
%{?_with_musicbrainz:BuildRequires: libmusicbrainz-devel libtunepimp-devel}
%{?_with_taglib:BuildRequires: taglib-devel}
%{?_with_xine:BuildRequires: xine-lib-devel}
BuildRequires:	libXxf86dga-devel
BuildRequires:	libXxf86vm-devel
BuildRequires:	libXt-devel

Requires: trinity-artsbuilder = %{version}-%{release}
Requires: trinity-juk = %{version}-%{release}
Requires: trinity-kaboodle = %{version}-%{release}
Requires: trinity-kaudiocreator = %{version}-%{release}
Requires: %{name}-kfile-plugins = %{version}-%{release}
Requires: %{name}-kappfinder-data = %{version}-%{release}
Requires: %{name}-kio-plugins = %{version}-%{release}
Requires: trinity-kmid = %{version}-%{release}
Requires: trinity-kmix = %{version}-%{release}
Requires: trinity-krec = %{version}-%{release}
Requires: trinity-kscd = %{version}-%{release}
Requires: trinity-libarts-akode = %{version}-%{release}
Requires: trinity-libarts-audiofile = %{version}-%{release}
Requires: trinity-libarts-mpeglib = %{version}-%{release}
Requires: trinity-libarts-xine = %{version}-%{release}
Requires: trinity-libkcddb = %{version}-%{release}
Requires: trinity-mpeglib = %{version}-%{release}
Requires: trinity-noatun = %{version}-%{release}


%description
The Trinity Desktop Environment (TDE) is a GUI desktop for the X Window
System. The %{name} package contains multimedia applications for
TDE, including:
  artsbuilder, Synthesizer designer for aRts
  juk, a media player
  kmid, a midi player
  kmix, an audio mixer
  arts, additional functionality for the aRts sound system
  krec, a recording tool
  kscd, an Audio-CD player
  kaudiocreator, a graphical frontend for audio file creation 
  kaboodle, a media player
  noatun, a media player

%files

##########

%package -n trinity-artsbuilder
Summary:	Synthesizer designer for aRts
Group:		Applications/Multimedia

%description -n trinity-artsbuilder
This is the analog Realtime synthesizer's graphical design tool.

%files -n trinity-artsbuilder
%{_bindir}/artsbuilder
%{_bindir}/artscontrol
%{_bindir}/midisend
%{_libdir}/libartsbuilder.la
%{_libdir}/libartsbuilder.so.*
%{_libdir}/libartscontrolapplet.la
%{_libdir}/libartscontrolapplet.so.*
%{_libdir}/libartscontrolsupport.la
%{_libdir}/libartscontrolsupport.so.*
%{_libdir}/libartsgui_idl.la
%{_libdir}/libartsgui_idl.so.*
%{_libdir}/libartsgui_kde.la
%{_libdir}/libartsgui_kde.so.*
%{_libdir}/libartsgui.la
%{_libdir}/libartsgui.so.*
%{_libdir}/libartsmidi_idl.la
%{_libdir}/libartsmidi_idl.so.*
%{_libdir}/libartsmidi.la
%{_libdir}/libartsmidi.so.*
%{_libdir}/libartsmodulescommon.la
%{_libdir}/libartsmodulescommon.so.*
%{_libdir}/libartsmoduleseffects.la
%{_libdir}/libartsmoduleseffects.so.*
%{_libdir}/libartsmodulesmixers.la
%{_libdir}/libartsmodulesmixers.so.*
%{_libdir}/libartsmodules.la
%{_libdir}/libartsmodules.so.*
%{_libdir}/libartsmodulessynth.la
%{_libdir}/libartsmodulessynth.so.*
%{_libdir}/mcop/Arts/ArtsBuilderLoader.mcopclass
%{_libdir}/mcop/artsbuilder.mcopclass
%{_libdir}/mcop/artsbuilder.mcoptype
%{_libdir}/mcop/Arts/Button.mcopclass
%{_libdir}/mcop/Arts/EffectRackGuiFactory.mcopclass
%{_libdir}/mcop/Arts/Effect_WAVECAPTURE.mcopclass
%{_libdir}/mcop/Arts/Environment/Container.mcopclass
%{_libdir}/mcop/Arts/Environment/EffectRackItem.mcopclass
%{_libdir}/mcop/Arts/Environment/InstrumentItemGuiFactory.mcopclass
%{_libdir}/mcop/Arts/Environment/InstrumentItem.mcopclass
%{_libdir}/mcop/Arts/Environment/MixerItem.mcopclass
%{_libdir}/mcop/Arts/Fader.mcopclass
%{_libdir}/mcop/Arts/FiveBandMonoComplexEQGuiFactory.mcopclass
%{_libdir}/mcop/Arts/FiveBandMonoComplexEQ.mcopclass
%{_libdir}/mcop/Arts/FreeverbGuiFactory.mcopclass
%{_libdir}/mcop/Arts/GenericGuiFactory.mcopclass
%{_libdir}/mcop/Arts/GraphLine.mcopclass
%{_libdir}/mcop/artsgui.mcopclass
%{_libdir}/mcop/artsgui.mcoptype
%{_libdir}/mcop/Arts/HBox.mcopclass
%{_libdir}/mcop/Arts/Label.mcopclass
%{_libdir}/mcop/Arts/LayoutBox.mcopclass
%{_libdir}/mcop/Arts/LevelMeter.mcopclass
%{_libdir}/mcop/Arts/LineEdit.mcopclass
%{_libdir}/mcop/Arts/LittleStereoMixerChannelGuiFactory.mcopclass
%{_libdir}/mcop/Arts/LittleStereoMixerChannel.mcopclass
%{_libdir}/mcop/Arts/LocalFactory.mcopclass
%{_libdir}/mcop/Arts/MidiManager.mcopclass
%{_libdir}/mcop/artsmidi.mcopclass
%{_libdir}/mcop/artsmidi.mcoptype
%{_libdir}/mcop/Arts/MixerGuiFactory.mcopclass
%{_libdir}/mcop/artsmodulescommon.mcopclass
%{_libdir}/mcop/artsmodulescommon.mcoptype
%{_libdir}/mcop/artsmoduleseffects.mcopclass
%{_libdir}/mcop/artsmoduleseffects.mcoptype
%{_libdir}/mcop/artsmodules.mcopclass
%{_libdir}/mcop/artsmodules.mcoptype
%{_libdir}/mcop/artsmodulesmixers.mcopclass
%{_libdir}/mcop/artsmodulesmixers.mcoptype
%{_libdir}/mcop/artsmodulessynth.mcopclass
%{_libdir}/mcop/artsmodulessynth.mcoptype
%{_libdir}/mcop/Arts/MonoSimpleMixerChannelGuiFactory.mcopclass
%{_libdir}/mcop/Arts/MonoSimpleMixerChannel.mcopclass
%{_libdir}/mcop/Arts/MonoToStereo.mcopclass
%{_libdir}/mcop/Arts/PopupBox.mcopclass
%{_libdir}/mcop/Arts/Poti.mcopclass
%{_libdir}/mcop/Arts/SimpleMixerChannelGuiFactory.mcopclass
%{_libdir}/mcop/Arts/SimpleMixerChannel.mcopclass
%{_libdir}/mcop/Arts/SpinBox.mcopclass
%{_libdir}/mcop/Arts/StereoBalanceGuiFactory.mcopclass
%{_libdir}/mcop/Arts/StereoBalance.mcopclass
%{_libdir}/mcop/Arts/StereoCompressorGuiFactory.mcopclass
%{_libdir}/mcop/Arts/StereoFirEqualizerGuiFactory.mcopclass
%{_libdir}/mcop/Arts/StereoToMono.mcopclass
%{_libdir}/mcop/Arts/StereoVolumeControlGuiFactory.mcopclass
%{_libdir}/mcop/Arts/StereoVolumeControlGui.mcopclass
%{_libdir}/mcop/Arts/StructureBuilder.mcopclass
%{_libdir}/mcop/Arts/StructureDesc.mcopclass
%{_libdir}/mcop/Arts/Synth_ATAN_SATURATE.mcopclass
%{_libdir}/mcop/Arts/Synth_AUTOPANNER.mcopclass
%{_libdir}/mcop/Arts/Synth_BRICKWALL_LIMITER.mcopclass
%{_libdir}/mcop/Arts/Synth_CAPTURE_WAV.mcopclass
%{_libdir}/mcop/Arts/Synth_CDELAY.mcopclass
%{_libdir}/mcop/Arts/Synth_COMPRESSOR.mcopclass
%{_libdir}/mcop/Arts/Synth_DATA.mcopclass
%{_libdir}/mcop/Arts/Synth_DEBUG.mcopclass
%{_libdir}/mcop/Arts/Synth_DELAY.mcopclass
%{_libdir}/mcop/Arts/Synth_DIV.mcopclass
%{_libdir}/mcop/Arts/Synth_ENVELOPE_ADSR.mcopclass
%{_libdir}/mcop/Arts/Synth_FM_SOURCE.mcopclass
%{_libdir}/mcop/Arts/Synth_FREEVERB.mcopclass
%{_libdir}/mcop/Arts/Synth_FX_CFLANGER.mcopclass
%{_libdir}/mcop/Arts/Synth_MIDI_DEBUG.mcopclass
%{_libdir}/mcop/Arts/Synth_MIDI_TEST.mcopclass
%{_libdir}/mcop/Arts/Synth_MOOG_VCF.mcopclass
%{_libdir}/mcop/Arts/Synth_NIL.mcopclass
%{_libdir}/mcop/Arts/Synth_NOISE.mcopclass
%{_libdir}/mcop/Arts/Synth_OSC.mcopclass
%{_libdir}/mcop/Arts/Synth_PITCH_SHIFT_FFT.mcopclass
%{_libdir}/mcop/Arts/Synth_PITCH_SHIFT.mcopclass
%{_libdir}/mcop/Arts/Synth_PLAY_PAT.mcopclass
%{_libdir}/mcop/Arts/Synth_PSCALE.mcopclass
%{_libdir}/mcop/Arts/Synth_RC.mcopclass
%{_libdir}/mcop/Arts/Synth_SEQUENCE_FREQ.mcopclass
%{_libdir}/mcop/Arts/Synth_SEQUENCE.mcopclass
%{_libdir}/mcop/Arts/Synth_SHELVE_CUTOFF.mcopclass
%{_libdir}/mcop/Arts/Synth_STD_EQUALIZER.mcopclass
%{_libdir}/mcop/Arts/Synth_STEREO_COMPRESSOR.mcopclass
%{_libdir}/mcop/Arts/Synth_STEREO_FIR_EQUALIZER.mcopclass
%{_libdir}/mcop/Arts/Synth_STEREO_PITCH_SHIFT_FFT.mcopclass
%{_libdir}/mcop/Arts/Synth_STEREO_PITCH_SHIFT.mcopclass
%{_libdir}/mcop/Arts/Synth_TREMOLO.mcopclass
%{_libdir}/mcop/Arts/Synth_VOICE_REMOVAL.mcopclass
%{_libdir}/mcop/Arts/Synth_WAVE_PULSE.mcopclass
%{_libdir}/mcop/Arts/Synth_WAVE_SOFTSAW.mcopclass
%{_libdir}/mcop/Arts/Synth_WAVE_SQUARE.mcopclass
%{_libdir}/mcop/Arts/Synth_WAVE_TRI.mcopclass
%{_libdir}/mcop/Arts/Synth_XFADE.mcopclass
%{_libdir}/mcop/Arts/VBox.mcopclass
%{_libdir}/mcop/Arts/VoiceRemovalGuiFactory.mcopclass
%{_libdir}/mcop/Arts/Widget.mcopclass
%{tde_appdir}/artsbuilder.desktop
%{tde_appdir}/artscontrol.desktop
%{_datadir}/apps/artsbuilder/
%{_datadir}/apps/artscontrol/
%{_datadir}/apps/kicker/applets/artscontrolapplet.desktop
%{_datadir}/icons/crystalsvg/*/actions/artsaudiomanager.png
%{_datadir}/icons/crystalsvg/*/actions/artsbuilderexecute.png
%{_datadir}/icons/crystalsvg/*/actions/artsenvironment.png
%{_datadir}/icons/crystalsvg/*/actions/artsfftscope.png
%{_datadir}/icons/crystalsvg/*/actions/artsmediatypes.png
%{_datadir}/icons/crystalsvg/*/actions/artsmidimanager.png
%{_datadir}/icons/crystalsvg/scalable/actions/artsaudiomanager.svgz
%{_datadir}/icons/crystalsvg/scalable/actions/artsenvironment.svgz
%{_datadir}/icons/crystalsvg/scalable/actions/artsfftscope.svgz
%{_datadir}/icons/crystalsvg/scalable/actions/artsmediatypes.svgz
%{_datadir}/icons/crystalsvg/scalable/actions/artsmidimanager.svgz
%{_datadir}/icons/hicolor/*/apps/artsbuilder.png
%{_datadir}/icons/hicolor/*/apps/artscontrol.png
%{_datadir}/icons/hicolor/scalable/apps/artsbuilder.svgz
%{_datadir}/icons/hicolor/scalable/apps/artscontrol.svgz
%{_datadir}/mimelnk/application/x-artsbuilder.desktop
%{tde_docdir}/HTML/en/artsbuilder/

%post -n trinity-artsbuilder
/sbin/ldconfig
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-artsbuilder
/sbin/ldconfig
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-juk
Summary:	Music organizer and player for Trinity
Group:		Applications/Multimedia

%description -n trinity-juk
JuK (pronounced "jook") is a jukebox and music manager for the TDE
desktop similar to jukebox software on other platforms such as
iTunes or RealOne.

Some of JuK's features include:
* Support for Ogg Vorbis and MP3 formats
* Tag editing support for both formats, including ID3v2 for MP3 files.
  Multitagging or editing a selection of multiple files at once is also
  supported
* Output to either the aRts, default KDE sound system, or GStreamer
* Management of your "collection" and multiple playlists
* Import and export to m3u playlists
* Binary caching of audio meta-data and playlist information for faster
  load times (starting with the second time you run JuK)
* Integration into TDE that allows drag-and-drop and clipboard usage
  with other TDE and X apps

%files -n trinity-juk
%{_bindir}/juk
%{tde_appdir}/juk.desktop
%{_datadir}/apps/juk/
%{_datadir}/apps/konqueror/servicemenus/jukservicemenu.desktop
%{_datadir}/icons/crystalsvg/*/actions/juk_dock.png
%{_datadir}/icons/hicolor/*/apps/juk.png
%{tde_docdir}/HTML/en/juk/

%post -n trinity-juk
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-juk
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kaboodle
Summary:	light, embedded media player for Trinity
Group:		Applications/Multimedia

Requires:	trinity-libarts-xine = %{version}-%{release}

%description -n trinity-kaboodle
Kaboodle is a light, embedded media player, supporting both video and audio,
for TDE. It uses the aRts framework for playing media files.

%files -n trinity-kaboodle
%{_bindir}/kaboodle
%{tde_libdir}/libkaboodlepart.la
%{tde_libdir}/libkaboodlepart.so
%{tde_appdir}/kaboodle.desktop
%{_datadir}/apps/kaboodle/
%{_datadir}/icons/hicolor/*/apps/kaboodle.png
%{_datadir}/services/kaboodle_component.desktop
%{_datadir}/services/kaboodleengine.desktop
%{tde_docdir}/HTML/en/kaboodle/

%post -n trinity-kaboodle
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kaboodle
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kaudiocreator
Summary:	CD ripper and audio encoder frontend for Trinity
Group:		Applications/Multimedia

Requires:	%{name}-kio-plugins = %{version}-%{release}
Requires:	vorbis-tools
Requires:	flac

%description -n trinity-kaudiocreator
KAudioCreator is a tool for audio extraction (ripping) and encoding. It can
keep your WAV files, or convert them to Ogg/Vorbis, MP3, or FLAC. It also
searches CDDB to retrieve the information of the disk.

%files -n trinity-kaudiocreator
%{_bindir}/kaudiocreator
%{tde_appdir}/kaudiocreator.desktop
%{_datadir}/apps/kaudiocreator/
%{_datadir}/apps/kconf_update/kaudiocreator-libkcddb.upd
%{_datadir}/apps/kconf_update/kaudiocreator-meta.upd
%{_datadir}/apps/kconf_update/upgrade-kaudiocreator-metadata.sh
%{_datadir}/apps/konqueror/servicemenus/audiocd_extract.desktop
%{_datadir}/config.kcfg/kaudiocreator.kcfg
%{_datadir}/config.kcfg/kaudiocreator_encoders.kcfg
%{_datadir}/icons/hicolor/*/apps/kaudiocreator.png
%{_datadir}/icons/locolor/*/apps/kaudiocreator.png
%{tde_docdir}/HTML/en/kaudiocreator/

%post -n trinity-kaudiocreator
for f in hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kaudiocreator
for f in hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package kfile-plugins
Summary:	au/avi/m3u/mp3/ogg/wav plugins for kfile
Group:		Applications/Multimedia

%description kfile-plugins
au/avi/m3u/mp3/ogg/wav file metainformation plugins for Trinity.

%files kfile-plugins
%{tde_libdir}/kfile_au.la
%{tde_libdir}/kfile_au.so
%{tde_libdir}/kfile_avi.la
%{tde_libdir}/kfile_avi.so
%{tde_libdir}/kfile_flac.la
%{tde_libdir}/kfile_flac.so
%{tde_libdir}/kfile_m3u.la
%{tde_libdir}/kfile_m3u.so
%{tde_libdir}/kfile_mp3.la
%{tde_libdir}/kfile_mp3.so
%{tde_libdir}/kfile_mpc.la
%{tde_libdir}/kfile_mpc.so
%{tde_libdir}/kfile_mpeg.la
%{tde_libdir}/kfile_mpeg.so
%{tde_libdir}/kfile_ogg.la
%{tde_libdir}/kfile_ogg.so
%{tde_libdir}/kfile_sid.la
%{tde_libdir}/kfile_sid.so
%{tde_libdir}/kfile_theora.la
%{tde_libdir}/kfile_theora.so
%{tde_libdir}/kfile_wav.la
%{tde_libdir}/kfile_wav.so
%{_datadir}/services/kfile_au.desktop
%{_datadir}/services/kfile_avi.desktop
%{_datadir}/services/kfile_flac.desktop
%{_datadir}/services/kfile_m3u.desktop
%{_datadir}/services/kfile_mp3.desktop
%{_datadir}/services/kfile_mpc.desktop
%{_datadir}/services/kfile_mpeg.desktop
%{_datadir}/services/kfile_ogg.desktop
%{_datadir}/services/kfile_sid.desktop
%{_datadir}/services/kfile_theora.desktop
%{_datadir}/services/kfile_wav.desktop

##########

%package kappfinder-data
Summary:	multimedia data for kappfinder-trinity
Group:		Applications/Multimedia

Requires: 	trinity-kappfinder

%description kappfinder-data
This package provides data on multimedia applications for kappfinder.

%files kappfinder-data
%{_datadir}/apps/kappfinder/*
%{_datadir}/desktop-directories/[kt]de-multimedia-music.directory
%{_prefix}/etc/xdg/menus/applications-merged/trinity-multimedia-music.menu

##########

%package kio-plugins
Summary:	Enables the browsing of audio CDs under Konqueror
Group:		Applications/Multimedia

%description kio-plugins
This package allow audio CDs to be browsed like a file system using
Konqueror and the audiocd:/ URL.

%files kio-plugins
%{tde_libdir}/kcm_audiocd.la
%{tde_libdir}/kcm_audiocd.so
%{tde_libdir}/kio_audiocd.la
%{tde_libdir}/kio_audiocd.so
%{tde_libdir}/libaudiocd_encoder_flac.la
%{tde_libdir}/libaudiocd_encoder_flac.so
%{tde_libdir}/libaudiocd_encoder_lame.la
%{tde_libdir}/libaudiocd_encoder_lame.so
%{tde_libdir}/libaudiocd_encoder_vorbis.la
%{tde_libdir}/libaudiocd_encoder_vorbis.so
%{tde_libdir}/libaudiocd_encoder_wav.la
%{tde_libdir}/libaudiocd_encoder_wav.so
%{_libdir}/libaudiocdplugins.so.*
%{tde_appdir}/audiocd.desktop
%{_datadir}/apps/kconf_update/audiocd.upd
%{_datadir}/apps/kconf_update/upgrade-metadata.sh
%{_datadir}/config.kcfg/audiocd_lame_encoder.kcfg
%{_datadir}/config.kcfg/audiocd_vorbis_encoder.kcfg
%{_datadir}/services/audiocd.protocol
%{tde_docdir}/HTML/en/kioslave/audiocd.docbook

%post kio-plugins
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun kio-plugins
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kmid
Summary:	MIDI/karaoke player for Trinity
Group:		Applications/Multimedia

%description -n trinity-kmid
This package provides a MIDI and karaoke player for TDE.

%files -n trinity-kmid
%{_bindir}/kmid
%{tde_libdir}/libkmidpart.la
%{tde_libdir}/libkmidpart.so
%{_libdir}/libkmidlib.so.*
%{tde_appdir}/kmid.desktop
%{_datadir}/apps/kmid/
%{_datadir}/icons/hicolor/*/apps/kmid.png
%{_datadir}/mimelnk/audio/x-karaoke.desktop
%{_datadir}/servicetypes/audiomidi.desktop
%{tde_docdir}/HTML/en/kmid/

%post -n trinity-kmid
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kmid
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kmix
Summary:	Sound mixer applet for Trinity
Group:		Applications/Multimedia

%description -n trinity-kmix
This package includes TDE's dockable sound mixer applet.

%files -n trinity-kmix
%{_bindir}/kmix
%{_bindir}/kmixctrl
%{tde_libdir}/kmix.la
%{tde_libdir}/kmix.so
%{tde_libdir}/kmix_panelapplet.la
%{tde_libdir}/kmix_panelapplet.so
%{tde_libdir}/kmixctrl.la
%{tde_libdir}/kmixctrl.so
%{_libdir}/lib[kt]deinit_kmix.so
%{_libdir}/lib[kt]deinit_kmixctrl.so
%{tde_appdir}/kmix.desktop
%{_datadir}/apps/kicker/applets/kmixapplet.desktop
%{_datadir}/apps/kmix/
%{_datadir}/autostart/restore_kmix_volumes.desktop
%{_datadir}/icons/hicolor/*/apps/kmix.png
%{_datadir}/services/kmixctrl_restore.desktop
%{tde_docdir}/HTML/en/kmix/

%post -n trinity-kmix
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kmix
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-krec
Summary:	Sound recorder utility for Trinity
Group:		Applications/Multimedia

%description -n trinity-krec
This is a sound recording utility for Trinity.

%files -n trinity-krec
%{_bindir}/krec
%{tde_libdir}/kcm_krec.la
%{tde_libdir}/kcm_krec.so
%{tde_libdir}/kcm_krec_files.la
%{tde_libdir}/kcm_krec_files.so
%{tde_libdir}/krec.la
%{tde_libdir}/krec.so
%{tde_libdir}/libkrecexport_ogg.la
%{tde_libdir}/libkrecexport_ogg.so
%{tde_libdir}/libkrecexport_wave.la
%{tde_libdir}/libkrecexport_wave.so
%{_libdir}/lib[kt]deinit_krec.so
%{tde_appdir}/krec.desktop
%{_datadir}/apps/krec/
%{_datadir}/icons/hicolor/*/apps/krec.png
%{_datadir}/services/kcm_krec.desktop
%{_datadir}/services/kcm_krec_files.desktop
%{_datadir}/services/krec_exportogg.desktop
%{_datadir}/services/krec_exportwave.desktop
%{_datadir}/servicetypes/krec_exportitem.desktop
%{tde_docdir}/HTML/en/krec/

%post -n trinity-krec
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-krec
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kscd
Summary:	Audio CD player for Trinity
Group:		Applications/Multimedia

%description -n trinity-kscd
This is Trinity's audio CD player.

%files -n trinity-kscd
%{_bindir}/kscd
%{_bindir}/workman2cddb.pl
%{tde_appdir}/kscd.desktop
%{_datadir}/apps/konqueror/servicemenus/audiocd_play.desktop
%{_datadir}/apps/kscd/
%{_datadir}/apps/profiles/kscd.profile.xml
%{_datadir}/config.kcfg/kscd.kcfg
%{_datadir}/icons/hicolor/*/apps/kscd.png
%{_datadir}/mimelnk/text/xmcd.desktop
%{tde_docdir}/HTML/en/kscd/

%post -n trinity-kscd
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kscd
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-libarts-akode
Summary:	Akode plugin for aRts
Group:		Environment/Libraries

%description -n trinity-libarts-akode
This package contains akode plugins for aRts.

%files -n trinity-libarts-akode
%{_libdir}/libarts_akode.la
%{_libdir}/libarts_akode.so
%{_libdir}/libarts_akode.so.*
%{_libdir}/mcop/akodearts.mcoptype
%{_libdir}/mcop/akodearts.mcopclass
%{_libdir}/mcop/akodeMPCPlayObject.mcopclass
%{_libdir}/mcop/akodePlayObject.mcopclass
%{_libdir}/mcop/akodeSpeexStreamPlayObject.mcopclass
%{_libdir}/mcop/akodeVorbisStreamPlayObject.mcopclass
%{_libdir}/mcop/akodeXiphPlayObject.mcopclass

%post -n trinity-libarts-akode
/sbin/ldconfig

%postun -n trinity-libarts-akode
/sbin/ldconfig

##########

%package -n trinity-libarts-audiofile
Summary:	Audiofile plugin for aRts
Group:		Environment/Libraries

%description -n trinity-libarts-audiofile
This package contains audiofile plugins for aRts.

%files -n trinity-libarts-audiofile
%{_libdir}/libarts_audiofile.la
%{_libdir}/libarts_audiofile.so
%{_libdir}/libarts_audiofile.so.*
%{_libdir}/mcop/Arts/audiofilePlayObject.mcopclass
%{_libdir}/mcop/audiofilearts.mcopclass
%{_libdir}/mcop/audiofilearts.mcoptype

%post -n trinity-libarts-audiofile
/sbin/ldconfig

%postun -n trinity-libarts-audiofile
/sbin/ldconfig

##########

%package -n trinity-libarts-mpeglib
Summary:	Mpeglib plugin for aRts, supporting mp3 and mpeg audio/video
Group:		Environment/Libraries

%description -n trinity-libarts-mpeglib
This package contains the mpeglib aRts plugin, supporting mp3 and mpeg
audio and video.

This is the arts (TDE Sound daemon) plugin.

%files -n trinity-libarts-mpeglib
%{_bindir}/mpeglibartsplay
%{_libdir}/libarts_mpeglib-0.3.0.so.*
%{_libdir}/libarts_mpeglib.la
%{_libdir}/libarts_splay.la
%{_libdir}/libarts_splay.so.*
%{_libdir}/mcop/CDDAPlayObject.mcopclass
%{_libdir}/mcop/MP3PlayObject.mcopclass
%{_libdir}/mcop/NULLPlayObject.mcopclass
%{_libdir}/mcop/OGGPlayObject.mcopclass
%{_libdir}/mcop/SplayPlayObject.mcopclass
%{_libdir}/mcop/WAVPlayObject.mcopclass

%post -n trinity-libarts-mpeglib
/sbin/ldconfig

%postun -n trinity-libarts-mpeglib
/sbin/ldconfig

##########

%package -n trinity-libarts-xine
Summary:	aRts plugin enabling xine support
Group:		Environment/Libraries

%description -n trinity-libarts-xine
This package contains aRts' xine plugin, allowing the use of the xine
multimedia engine though aRts.

%files -n trinity-libarts-xine
%{tde_libdir}/videothumbnail.la
%{tde_libdir}/videothumbnail.so
%{_libdir}/libarts_xine.la
%{_libdir}/libarts_xine.so
%{_libdir}/libarts_xine.so.*
%{_libdir}/mcop/xineAudioPlayObject.mcopclass
%{_libdir}/mcop/xineVideoPlayObject.mcopclass
%{_datadir}/apps/videothumbnail/sprocket-large.png
%{_datadir}/apps/videothumbnail/sprocket-medium.png
%{_datadir}/apps/videothumbnail/sprocket-small.png
%{_datadir}/services/videothumbnail.desktop

%post -n trinity-libarts-xine
/sbin/ldconfig

%postun -n trinity-libarts-xine
/sbin/ldconfig

##########

%package -n trinity-libkcddb
Summary:	CDDB library for Trinity
Group:		Environment/Libraries

%description -n trinity-libkcddb
The Trinity native CDDB (CD Data Base) library, providing easy access to Audio
CD meta-information (track titles, artist information, etc.) from on-line
databases, for TDE applications.

%files -n trinity-libkcddb
%{tde_libdir}/kcm_cddb.la
%{tde_libdir}/kcm_cddb.so
%{_libdir}/libkcddb.so.*
%{tde_appdir}/libkcddb.desktop
%{_datadir}/apps/kconf_update/kcmcddb-emailsettings.upd
%{_datadir}/config.kcfg/libkcddb.kcfg

%post -n trinity-libkcddb
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-libkcddb
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-mpeglib
Summary:	MP3 and MPEG-1 audio and video library
Group:		Environment/Libraries
Requires:	trinity-libarts-mpeglib = %{version}-%{release}

%description -n trinity-mpeglib
mpeglib is a MPEG-1 and MP3 audio and video library. It supports
MPEG-1 audio (layers 1, 2, 3), MPEG-1 video, MPEG-1 system layer,
and WAV playback

%files -n trinity-mpeglib
%{_bindir}/yaf-cdda
%{_bindir}/yaf-mpgplay
%{_bindir}/yaf-splay
%{_bindir}/yaf-tplay
%{_bindir}/yaf-vorbis
%{_bindir}/yaf-yuv
%{_libdir}/libmpeg-0.3.0.so
%{_libdir}/libyafcore.so
%{_libdir}/libyafxplayer.so

%post -n trinity-mpeglib
/sbin/ldconfig

%postun -n trinity-mpeglib
/sbin/ldconfig

##########

%package -n trinity-noatun
Summary:	Media player for Trinity
Group:		Applications/Multimedia

%description -n trinity-noatun
Noatun is an aRts-based audio and video player for Trinity. It supports all
formats supported by your installation of aRts (including aRts plugins).

%files -n trinity-noatun
%{_bindir}/noatun
%{_libdir}/kconf_update_bin/noatun20update
%{tde_libdir}/noatun.la
%{tde_libdir}/noatun.so
%{tde_libdir}/noatun_dcopiface.la
%{tde_libdir}/noatun_dcopiface.so
%{tde_libdir}/noatun_excellent.la
%{tde_libdir}/noatun_excellent.so
%{tde_libdir}/noatun_htmlexport.la
%{tde_libdir}/noatun_htmlexport.so
%{tde_libdir}/noatun_infrared.la
%{tde_libdir}/noatun_infrared.so
%{tde_libdir}/noatun_kaiman.la
%{tde_libdir}/noatun_kaiman.so
%{tde_libdir}/noatun_keyz.la
%{tde_libdir}/noatun_keyz.so
%{tde_libdir}/noatun_kjofol.la
%{tde_libdir}/noatun_kjofol.so
%{tde_libdir}/noatun_marquis.la
%{tde_libdir}/noatun_marquis.so
%{tde_libdir}/noatun_metatag.la
%{tde_libdir}/noatun_metatag.so
%{tde_libdir}/noatun_monoscope.la
%{tde_libdir}/noatun_monoscope.so
%{tde_libdir}/noatun_net.la
%{tde_libdir}/noatun_net.so
%{tde_libdir}/noatun_splitplaylist.la
%{tde_libdir}/noatun_splitplaylist.so
%{tde_libdir}/noatun_systray.la
%{tde_libdir}/noatun_systray.so
%{tde_libdir}/noatun_ui.la
%{tde_libdir}/noatun_ui.so
%{tde_libdir}/noatun_voiceprint.la
%{tde_libdir}/noatun_voiceprint.so
%{tde_libdir}/noatun_winskin.la
%{tde_libdir}/noatun_winskin.so
%{tde_libdir}/noatunsimple.la
%{tde_libdir}/noatunsimple.so
%{_libdir}/libartseffects.la
%{_libdir}/libartseffects.so
%{_libdir}/lib[kt]deinit_noatun.so
%{_libdir}/libnoatun.so.*
%{_libdir}/libnoatunarts.la
%{_libdir}/libnoatunarts.so
%{_libdir}/libnoatuncontrols.so.*
%{_libdir}/libnoatuntags.so.*
%{_libdir}/libwinskinvis.la
%{_libdir}/libwinskinvis.so
%{_libdir}/mcop/ExtraStereo.mcopclass
%{_libdir}/mcop/ExtraStereoGuiFactory.mcopclass
%{_libdir}/mcop/Noatun/Equalizer.mcopclass
%{_libdir}/mcop/Noatun/EqualizerSSE.mcopclass
%{_libdir}/mcop/Noatun/FFTScope.mcopclass
%{_libdir}/mcop/Noatun/FFTScopeStereo.mcopclass
%{_libdir}/mcop/Noatun/Listener.mcopclass
%{_libdir}/mcop/Noatun/RawScope.mcopclass
%{_libdir}/mcop/Noatun/RawScopeStereo.mcopclass
%{_libdir}/mcop/Noatun/Session.mcopclass
%{_libdir}/mcop/Noatun/StereoEffectStack.mcopclass
%{_libdir}/mcop/Noatun/StereoVolumeControl.mcopclass
%{_libdir}/mcop/Noatun/StereoVolumeControlSSE.mcopclass
%{_libdir}/mcop/Noatun/WinSkinFFT.mcopclass
%{_libdir}/mcop/RawWriter.mcopclass
%{_libdir}/mcop/VoiceRemoval.mcopclass
%{_libdir}/mcop/artseffects.mcopclass
%{_libdir}/mcop/artseffects.mcoptype
%{_libdir}/mcop/noatunarts.mcopclass
%{_libdir}/mcop/noatunarts.mcoptype
%{_libdir}/mcop/winskinvis.mcopclass
%{_libdir}/mcop/winskinvis.mcoptype
%{tde_appdir}/noatun.desktop
%{_datadir}/apps/kconf_update/noatun.upd
%{_datadir}/apps/noatun/
%{_datadir}/icons/hicolor/*/apps/noatun.png
%{_datadir}/mimelnk/interface/x-winamp-skin.desktop
%{tde_docdir}/HTML/en/noatun/

%post -n trinity-noatun
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-noatun
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package devel
Summary:	Development files for %{name}, aRts and noatun plugins
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	trinity-kdelibs-devel

Obsoletes:	trinity-kdemultimedia-devel < %{version}-%{release}
Provides:	trinity-kdemultimedia-devel = %{version}-%{release}

%description devel
{summary}.

Install %{name}-devel if you wish to develop or compile any
applications using aRtsbuilder, aRtsmidi, aRtskde, aRts modules or
noatun plugins.

%files devel
%{tde_includedir}/*
%{_libdir}/libarts_mpeglib.so
%{_libdir}/libarts_splay.so
%{_libdir}/libartsbuilder.so
%{_libdir}/libartscontrolapplet.so
%{_libdir}/libartscontrolsupport.so
%{_libdir}/libartsgui.so
%{_libdir}/libartsgui_idl.so
%{_libdir}/libartsgui_kde.so
%{_libdir}/libartsmidi.so
%{_libdir}/libartsmidi_idl.so
%{_libdir}/libartsmodules.so
%{_libdir}/libartsmodulescommon.so
%{_libdir}/libartsmoduleseffects.so
%{_libdir}/libartsmodulesmixers.so
%{_libdir}/libartsmodulessynth.so
%{_libdir}/libaudiocdplugins.la
%{_libdir}/libaudiocdplugins.so
%{_libdir}/libkcddb.la
%{_libdir}/libkcddb.so
%{_libdir}/lib[kt]deinit_kmix.la
%{_libdir}/lib[kt]deinit_kmixctrl.la
%{_libdir}/lib[kt]deinit_krec.la
%{_libdir}/lib[kt]deinit_noatun.la
%{_libdir}/libkmidlib.la
%{_libdir}/libkmidlib.so
%{_libdir}/libmpeg.la
%{_libdir}/libmpeg.so
%{_libdir}/libnoatun.la
%{_libdir}/libnoatun.so
%{_libdir}/libnoatuncontrols.la
%{_libdir}/libnoatuncontrols.so
%{_libdir}/libnoatuntags.la
%{_libdir}/libnoatuntags.so
%{_libdir}/libyafcore.la
%{_libdir}/libyafxplayer.la

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

##########


%prep
%setup -q -n kdemultimedia
%patch3 -p1 -b .xdg
%patch5 -p1 -b .pthread
%patch10 -p1
%patch21 -p1 -b .moreapplications
%patch22 -p1


# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure  \
   --enable-new-ldflags \
   --disable-dependency-tracking \
   --includedir=%{tde_includedir} \
   --with-cdparanoia \
   --with-flac \
   --with-theora \
   --with-vorbis \
   --with-alsa \
   --with-gstreamer \
   --without-lame \
   --disable-debug \
   --disable-warnings \
   --enable-final \
   --disable-rpath \
  %{?_with_akode} %{!?_with_akode:--without-akode} \
  %{?_with_musicbrainz} %{!?_with_musicbrainz:--without-musicbrainz} \
  %{?_with_taglib} %{!?_with_taglib:--without-taglib} \
  %{?_with_xine} %{!?_with_xine:--without-xine} \
   --with-extra-includes="%{_usr}/include/cdda:%{_includedir}/tqt" \
   --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{?buildroot} 
%__make install DESTDIR=%{buildroot}

## Remove/uninstall (conflicting) bits we don't want
#%__rm -f $RPM_BUILD_ROOT%{_libdir}/mcop/akode*MPEGPlayObject.mcopclass

# only show in KDE, really? -- Rex (FIXME)
#for f in %{buildroot}%{tde_appdir}/*.desktop ; do
#  if [ -f %{buildroot}%{tde_appdir}/*.desktop ] ; then
#    echo "OnlyShowIn=KDE;" >> $f
#  fi
#done

# don't make these world-writeable
chmod go-w %{buildroot}%{_datadir}/apps/kscd/*

# locale's
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}$HTML_DIR ]; then
for lang_dir in %{buildroot}$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
    # replace absolute symlinks with relative ones
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && ln -nsf ../common $i/common
      done
    popd
  fi
done
fi

# rpmdocs
for dir in k* ; do
  for file in AUTHORS ChangeLog README TODO ; do
    if test -s "$dir/$file" ; then
       install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
       # exclude kaboodle, juk, noatun
       if [ $dir != kaboodle -a $dir != juk -a $dir != noatun ] ; then
         echo "%doc rpmdocs/$dir/" >> %{name}.lang
       fi
    fi
  done
done

# Moves the XDG configuration files to TDE directory
%__install -p -D -m644 \
	"%{?buildroot}%{_sysconfdir}/xdg/menus/applications-merged/kde-multimedia-music.menu" \
	"%{?buildroot}%{_prefix}/etc/xdg/menus/applications-merged/trinity-multimedia-music.menu"
%__rm -rf "%{?buildroot}%{_sysconfdir}/xdg"


%clean
%__rm -rf %{buildroot}


%changelog
* Sun Jul 01 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-8
- Split in several packages
- Enables Xine support on RHEL/CentOS
- Removes previous patch. [Bug #503]

* Wed May 09 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-7
- Fix kmix not autostarting in the user's session. [Bug #503]

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-6
- Updates BuildRequires
- Remove "More Applications" from TDE menu. [Commit #31e44a7b]
- Fix linear alphabet string errors [Commit #fd6afacf]
 
* Mon Jan 16 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-5
- Enables 'akode' support
- Fix MMX support [Bug #800]

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Fix HTML directory location

* Sat Nov 12 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Moves XDG files in TDE prefix to avoid conflict with distro-provided KDE

* Fri Nov 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Updates BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sat Sep 09 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
- Spec file based on Fedora 8 "kdemultimedia-6:3.5.10-2"

