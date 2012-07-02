# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
%define tde_appdir %{_datadir}/applications/kde
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity

Name:		trinity-tdeaddons
Summary:	Trinity Desktop Environment - Plugins
Version:	3.5.13
Release:	5%{?dist}%{?_variant}

License:	GPLv2
Group:		User Interface/Desktops

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Obsoletes:	trinity-kdeaddons < %{version}-%{release}
Provides:	trinity-kdeaddons = %{version}-%{release}
Obsoletes:	trinity-kdeaddons-extras < %{version}-%{release}
Provides:	trinity-kdeaddons-extras = %{version}-%{release}

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: kdeaddons-%{version}.tar.gz
Source1: metabar-fedora.tar.bz2
Source2: metabarrc

BuildRequires: autoconf automake libtool m4
BuildRequires: trinity-kdebase-devel
BuildRequires: trinity-kdegames-devel
BuildRequires: trinity-kdemultimedia-devel
BuildRequires: trinity-kdepim-devel

BuildRequires: SDL-devel
BuildRequires: alsa-lib-devel
BuildRequires: openssl-devel
BuildRequires: db4-devel

%if 0%{?fedora}
BuildRequires: xmms-devel
%endif

#Requires: which

Requires: trinity-atlantikdesigner = %{version}-%{release}
Requires: trinity-kaddressbook-plugins = %{version}-%{release}
Requires: trinity-kate-plugins = %{version}-%{release}
Requires: trinity-tdeaddons-kfile-plugins = %{version}-%{release}
Requires: trinity-kicker-applets = %{version}-%{release}
Requires: trinity-knewsticker-scripts = %{version}-%{release}
Requires: trinity-konq-plugins = %{version}-%{release}
Requires: trinity-ksig = %{version}-%{release}
Requires: trinity-noatun-plugins = %{version}-%{release}


%description
A collection of TDE Addons/Plugins, including: 
* atlantikdesigner: game board designer
* konq-plugins: akregator, babelfish, domtreeviewer, imagerotation, validators, webarchiver
* kate (plugins) 
* kicker-applets: kbinaryclock, kolourpicker, ktimemon, mediacontrol
* knewsticker-scripts
* noatun-plugins

%files
%defattr(-,root,root,-)
%doc README
%doc rpmdocs/*

##########

%package -n trinity-atlantikdesigner
Summary:	Game board designer for Atlantik
Group:		Applications/Games
#Requires:	trinity-atlantik
Requires:	trinity-kdegames

%description -n trinity-atlantikdesigner
Atlantik Designer is a game board designer for the game Atlantik.

Atlantik is a TDE client for playing Monopoly-like board games on the
monopd network.  It can play any board supported by the network
server, including the classic Monopoly game as well as the Atlantik
game in which the properties include several major cities in North
America and Europe.

%files -n trinity-atlantikdesigner
%defattr(-,root,root,-)
%doc atlantikdesigner/TODO
%{_bindir}/atlantikdesigner
%{_datadir}/apps/atlantikdesigner
%{tde_appdir}/atlantikdesigner.desktop
%{_datadir}/icons/hicolor/*/apps/atlantikdesigner.png

%post -n trinity-atlantikdesigner
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-atlantikdesigner
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kaddressbook-plugins
Summary:	Plugins for KAddressBook, the Trinity address book
Group:		Applications/Utilities
Requires:	trinity-kaddressbook

%description -n trinity-kaddressbook-plugins
This package contains a variety of useful plugins for the KDE address
book.  These plugins can be loaded through the TDE address book settings.

Highlights include exporting postal addresses as flags in KWorldClock,
as well as importing and exporting contacts in the native format used
by the German freemail provider GMX.

%files -n trinity-kaddressbook-plugins
%defattr(-,root,root,-)
%{tde_libdir}/libkaddrbk_geo_xxport.la
%{tde_libdir}/libkaddrbk_geo_xxport.so
%{tde_libdir}/libkaddrbk_gmx_xxport.la
%{tde_libdir}/libkaddrbk_gmx_xxport.so
%{_datadir}/apps/kaddressbook
%{_datadir}/services/kaddressbook

##########

%package -n trinity-kate-plugins
Summary:	Plugins for Kate, the TDE Advanced Text Editor
Group:		Applications/Utilities
Requires:	trinity-kate
Requires:	tidy

%description -n trinity-kate-plugins
This package contains a variety of useful plugins for Kate, the KDE
Advanced Text Editor.  These plugins can be loaded through the plugin
manager in Kate settings.

Highlights include spell checking, text filtering, HTML/XML construction
and validation, vim/emacs modeline handling, templates for new files
and text snippets, opening of C/C++ headers, extraction of C/C++ symbols,
a tab bar, a Python browser and even more.

%files -n trinity-kate-plugins
%defattr(-,root,root,-)
%{tde_libdir}/katecppsymbolviewerplugin.la
%{tde_libdir}/katecppsymbolviewerplugin.so
%{tde_libdir}/katefiletemplates.la
%{tde_libdir}/katefiletemplates.so
%{tde_libdir}/katefll_plugin.la
%{tde_libdir}/katefll_plugin.so
%{tde_libdir}/katehelloworldplugin.la
%{tde_libdir}/katehelloworldplugin.so
%{tde_libdir}/katehtmltoolsplugin.la
%{tde_libdir}/katehtmltoolsplugin.so
%{tde_libdir}/kateinsertcommandplugin.la
%{tde_libdir}/kateinsertcommandplugin.so
%{tde_libdir}/katemakeplugin.la
%{tde_libdir}/katemakeplugin.so
%{tde_libdir}/katemodelineplugin.la
%{tde_libdir}/katemodelineplugin.so
%{tde_libdir}/kateopenheaderplugin.la
%{tde_libdir}/kateopenheaderplugin.so
%{tde_libdir}/katepybrowseplugin.la
%{tde_libdir}/katepybrowseplugin.so
%{tde_libdir}/katesnippetsplugin.la
%{tde_libdir}/katesnippetsplugin.so
%{tde_libdir}/katetextfilterplugin.la
%{tde_libdir}/katetextfilterplugin.so
%{tde_libdir}/katexmlcheckplugin.la
%{tde_libdir}/katexmlcheckplugin.so
%{tde_libdir}/katexmltoolsplugin.la
%{tde_libdir}/katexmltoolsplugin.so
%{tde_libdir}/libkatetabbarextensionplugin.la
%{tde_libdir}/libkatetabbarextensionplugin.so
%{_datadir}/applnk/.hidden/katefll.desktop
%{_datadir}/apps/kate
%{_datadir}/apps/katepart
%{_datadir}/apps/katexmltools
%{_datadir}/services/katecppsymbolviewer.desktop
%{_datadir}/services/katefiletemplates.desktop
%{_datadir}/services/katefll_plugin.desktop
%{_datadir}/services/katehelloworld.desktop
%{_datadir}/services/katehtmltools.desktop
%{_datadir}/services/kateinsertcommand.desktop
%{_datadir}/services/katemake.desktop
%{_datadir}/services/katemodeline.desktop
%{_datadir}/services/kateopenheader.desktop
%{_datadir}/services/katepybrowse.desktop
%{_datadir}/services/katesnippets.desktop
%{_datadir}/services/katetabbarextension.desktop
%{_datadir}/services/katetextfilter.desktop
%{_datadir}/services/katexmlcheck.desktop
%{_datadir}/services/katexmltools.desktop
%{tde_docdir}/HTML/en/kate-plugins/

##########

%package kfile-plugins
Summary:	Trinity file dialog plugins for text files and folders
Group:		Applications/Utilities

%description kfile-plugins
This is a collection of plugins for the TDE file dialog.  These plugins
extend the file dialog to offer advanced meta-information for text,
HTML and desktop files, as well as for folders, Windows .lnk files,
MIME archives and X.509 certificates.

This package also includes plugins for the KDE file rename dialog,
allowing a user to more easily decide what to do when faced with a
decision regarding conflicting filenames.  Rename dialog plugins are
provided for audio and image files.

%files kfile-plugins
%defattr(-,root,root,-)
%{_bindir}/lnkforward
%{tde_libdir}/kfile_cert.la
%{tde_libdir}/kfile_cert.so
%{tde_libdir}/kfile_desktop.la
%{tde_libdir}/kfile_desktop.so
%{tde_libdir}/kfile_folder.la
%{tde_libdir}/kfile_folder.so
%{tde_libdir}/kfile_html.la
%{tde_libdir}/kfile_html.so
%{tde_libdir}/kfile_lnk.la
%{tde_libdir}/kfile_lnk.so
%{tde_libdir}/kfile_mhtml.la
%{tde_libdir}/kfile_mhtml.so
%{tde_libdir}/kfile_txt.la
%{tde_libdir}/kfile_txt.so
%{tde_libdir}/librenaudioplugin.la
%{tde_libdir}/librenaudioplugin.so
%{tde_libdir}/librenimageplugin.la
%{tde_libdir}/librenimageplugin.so
%{_datadir}/applnk/.hidden/lnkforward.desktop
%{_datadir}/mimelnk/application/x-win-lnk.desktop
%{_datadir}/services/kfile_cert.desktop
%{_datadir}/services/kfile_desktop.desktop
%{_datadir}/services/kfile_folder.desktop
%{_datadir}/services/kfile_html.desktop
%{_datadir}/services/kfile_lnk.desktop
%{_datadir}/services/kfile_mhtml.desktop
%{_datadir}/services/kfile_txt.desktop
%{_datadir}/services/renaudiodlg.desktop
%{_datadir}/services/renimagedlg.desktop

##########

%package -n trinity-kicker-applets
Summary:	Applets for Kicker, the Trinity panel
Group:		Applications/Utilities
Requires:	trinity-kicker

%description -n trinity-kicker-applets
This package contains a variety of applets for Kicker, the KDE panel.
These applets will appear in the panel's Add--Applet menu.

Included are a system monitor, a colour picker, a media player controller,
a mathematical evaluator and a binary clock.

The media control applet does not support XMMS, as this would force all
kicker-applets users to install XMMS. If you want a kicker applet that
controls XMMS, install the xmms-kde-trinity package.

%files -n trinity-kicker-applets
%defattr(-,root,root,-)
%{tde_libdir}/kolourpicker_panelapplet.la
%{tde_libdir}/kolourpicker_panelapplet.so
%{tde_libdir}/ktimemon_panelapplet.la
%{tde_libdir}/ktimemon_panelapplet.so
%{tde_libdir}/math_panelapplet.la
%{tde_libdir}/math_panelapplet.so
%{tde_libdir}/mediacontrol_panelapplet.la
%{tde_libdir}/mediacontrol_panelapplet.so
%{tde_libdir}/kbinaryclock_panelapplet.la
%{tde_libdir}/kbinaryclock_panelapplet.so
%{_datadir}/apps/kicker/applets
%{_datadir}/apps/mediacontrol
%{_datadir}/config.kcfg/kbinaryclock.kcfg
%{_datadir}/icons/locolor/*/apps/ktimemon.png
%{_datadir}/icons/crystalsvg/*/apps/ktimemon.png
%{tde_docdir}/HTML/en/kicker-applets/

%post -n trinity-kicker-applets
for f in crystalsvg locolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done

%postun -n trinity-kicker-applets
for f in crystalsvg locolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done

##########

%package -n trinity-knewsticker-scripts
Summary: scripts for KNewsTicker, the Trinity news ticker
Group:		Applications/Utilities
Requires:	perl
Requires:	python
#Requires:	libfinance-quote-perl
#Requires:	libmime-perl
#Requires:	libnews-nntpclient-perl
Requires:	perl-libwww-perl
Requires:	trinity-knewsticker

%description -n trinity-knewsticker-scripts
This package contains a variety of scripts that provide additional news
sources for KNewsTicker, the news ticker applet for the TDE panel.

Highlights include newsgroup handling, stock data retrieval, sports scores
and various local news sources.

%files -n trinity-knewsticker-scripts
%defattr(-,root,root,-)
%{_datadir}/apps/knewsticker/

##########

%package -n trinity-konq-plugins
Summary:	plugins for Konqueror, the Trinity file/web/doc browser
Group:		Applications/Utilities
Requires:	libjpeg
Requires:	python
Requires:	rsync
#Requires:	unison
Requires:	trinity-konqueror
%if 0%{?fedora} > 0
Requires:	python-exif
%endif

%description -n trinity-konq-plugins
This package contains a variety of useful plugins for Konqueror, the
file manager, web browser and document viewer for KDE.  Many of these
plugins will appear in Konqueror's Tools menu.

Highlights for web browsing include web page translation, web page archiving,
auto-refreshing, HTML and CSS structural analysis, a search toolbar, a
sidebar news ticker, fast access to common options, bookmarklets, a crash
monitor, a microformat availability indicator, a del.icio.us bookmarks
sidebar, and integration with the aKregator RSS feed reader.

Highlights for directory browsing include directory filters, image gallery
creation, archive compression and extraction, quick copy/move, a sidebar
media player, a file information metabar/sidebar, a media folder helper, a
graphical disk usage viewer and image conversions and transformations.

%files -n trinity-konq-plugins
%defattr(-,root,root,-)
%{_datadir}/config/translaterc
%{_bindir}/fsview
%{_bindir}/jpegorient
%{_bindir}/kio_media_realfolder
%{tde_libdir}/konq_sidebarnews.la
%{tde_libdir}/konq_sidebarnews.so
%{tde_libdir}/konqsidebar_delicious.la
%{tde_libdir}/konqsidebar_delicious.so
%{tde_libdir}/konqsidebar_mediaplayer.la
%{tde_libdir}/konqsidebar_mediaplayer.so
%{tde_libdir}/konqsidebar_metabar.la
%{tde_libdir}/konqsidebar_metabar.so
%{tde_libdir}/libakregatorkonqfeedicon.la
%{tde_libdir}/libakregatorkonqfeedicon.so
%{tde_libdir}/libakregatorkonqplugin.la
%{tde_libdir}/libakregatorkonqplugin.so
%{tde_libdir}/libarkplugin.la
%{tde_libdir}/libarkplugin.so
%{tde_libdir}/libautorefresh.la
%{tde_libdir}/libautorefresh.so
%{tde_libdir}/libbabelfishplugin.la
%{tde_libdir}/libbabelfishplugin.so
%{tde_libdir}/libcrashesplugin.la
%{tde_libdir}/libcrashesplugin.so
%{tde_libdir}/libdirfilterplugin.la
%{tde_libdir}/libdirfilterplugin.so
%{tde_libdir}/librsyncplugin.la
%{tde_libdir}/librsyncplugin.so
%{tde_libdir}/libdomtreeviewerplugin.la
%{tde_libdir}/libdomtreeviewerplugin.so
%{tde_libdir}/libfsviewpart.la
%{tde_libdir}/libfsviewpart.so
%{tde_libdir}/libkhtmlsettingsplugin.la
%{tde_libdir}/libkhtmlsettingsplugin.so
%{tde_libdir}/kcm_kuick.la
%{tde_libdir}/kcm_kuick.so
%{tde_libdir}/libkimgallery.la
%{tde_libdir}/libkimgallery.so
%{tde_libdir}/libkuickplugin.la
%{tde_libdir}/libkuickplugin.so
%{tde_libdir}/libmfkonqmficon.la
%{tde_libdir}/libmfkonqmficon.so
%{tde_libdir}/libminitoolsplugin.la
%{tde_libdir}/libminitoolsplugin.so
%{tde_libdir}/librellinksplugin.la
%{tde_libdir}/librellinksplugin.so
%{tde_libdir}/libsearchbarplugin.la
%{tde_libdir}/libsearchbarplugin.so
%{tde_libdir}/libuachangerplugin.la
%{tde_libdir}/libuachangerplugin.so
%{tde_libdir}/libvalidatorsplugin.la
%{tde_libdir}/libvalidatorsplugin.so
%{tde_libdir}/libwebarchiverplugin.la
%{tde_libdir}/libwebarchiverplugin.so
%{tde_libdir}/webarchivethumbnail.la
%{tde_libdir}/webarchivethumbnail.so
%{_datadir}/applnk/.hidden/arkplugin.desktop
%{_datadir}/applnk/.hidden/kcmkuick.desktop
%{_datadir}/applnk/.hidden/kuickplugin.desktop
%{_datadir}/applnk/.hidden/mediaplayerplugin.desktop
%{_datadir}/applnk/.hidden/crashesplugin.desktop
%{_datadir}/applnk/.hidden/dirfilterplugin.desktop
%{_datadir}/applnk/.hidden/rsyncplugin.desktop
%{_datadir}/applnk/.hidden/fsview.desktop
%{_datadir}/applnk/.hidden/khtmlsettingsplugin.desktop
%{_datadir}/applnk/.hidden/kimgalleryplugin.desktop
%{_datadir}/applnk/.hidden/plugin_babelfish.desktop
%{_datadir}/applnk/.hidden/plugin_domtreeviewer.desktop
%{_datadir}/applnk/.hidden/plugin_validators.desktop
%{_datadir}/applnk/.hidden/plugin_webarchiver.desktop
%{_datadir}/applnk/.hidden/uachangerplugin.desktop
%{_datadir}/apps/akregator
%{_datadir}/apps/domtreeviewer
%{_datadir}/apps/fsview
%{_datadir}/apps/imagerotation/orient.py*
%{_datadir}/apps/imagerotation/exif.py*
%{_datadir}/apps/khtml/kpartplugins
%{_datadir}/apps/konqiconview
%{_datadir}/apps/konqlistview
%{_datadir}/apps/konqsidebartng
%{_datadir}/apps/konqueror/icons
%{_datadir}/apps/konqueror/kpartplugins
%{_datadir}/apps/konqueror/servicemenus
%{_datadir}/apps/metabar/iconsrc
%{_datadir}/apps/metabar/themes/default/default.css
%{_datadir}/apps/metabar/themes/default/layout.html
%{_datadir}/apps/microformat/pics/microformat.png
%{_datadir}/config.kcfg/konq_sidebarnews.kcfg
%{_datadir}/icons/locolor/16x16/apps/autorefresh.png
%{_datadir}/icons/crystalsvg/16x16/actions/babelfish.png
%{_datadir}/icons/crystalsvg/16x16/actions/cssvalidator.png
%{_datadir}/icons/crystalsvg/16x16/actions/domtreeviewer.png
%{_datadir}/icons/crystalsvg/16x16/actions/htmlvalidator.png
%{_datadir}/icons/crystalsvg/16x16/actions/imagegallery.png
%{_datadir}/icons/crystalsvg/16x16/actions/remotesync.png
%{_datadir}/icons/crystalsvg/16x16/actions/remotesyncconfig.png
%{_datadir}/icons/crystalsvg/16x16/actions/minitools.png
%{_datadir}/icons/crystalsvg/16x16/actions/validators.png
%{_datadir}/icons/crystalsvg/16x16/actions/webarchiver.png
%{_datadir}/icons/crystalsvg/16x16/apps/konqsidebar_delicious.png
%{_datadir}/icons/crystalsvg/16x16/apps/konqsidebar_mediaplayer.png
%{_datadir}/icons/crystalsvg/16x16/apps/konqsidebar_news.png
%{_datadir}/icons/crystalsvg/22x22/actions/babelfish.png
%{_datadir}/icons/crystalsvg/22x22/actions/cssvalidator.png
%{_datadir}/icons/crystalsvg/22x22/actions/domtreeviewer.png
%{_datadir}/icons/crystalsvg/22x22/actions/htmlvalidator.png
%{_datadir}/icons/crystalsvg/22x22/actions/imagegallery.png
%{_datadir}/icons/crystalsvg/22x22/actions/remotesync.png
%{_datadir}/icons/crystalsvg/22x22/actions/remotesyncconfig.png
%{_datadir}/icons/crystalsvg/22x22/actions/minitools.png
%{_datadir}/icons/crystalsvg/22x22/actions/validators.png
%{_datadir}/icons/crystalsvg/22x22/actions/webarchiver.png
%{_datadir}/icons/crystalsvg/22x22/apps/konqsidebar_mediaplayer.png
%{_datadir}/icons/crystalsvg/32x32/actions/minitools.png
%{_datadir}/icons/crystalsvg/32x32/apps/konqsidebar_mediaplayer.png
%{_datadir}/icons/crystalsvg/48x48/actions/minitools.png
%{_datadir}/icons/crystalsvg/48x48/apps/konqsidebar_mediaplayer.png
%{_datadir}/icons/hicolor/16x16/apps/metabar.png
%{_datadir}/icons/hicolor/22x22/apps/fsview.png
%{_datadir}/icons/hicolor/32x32/apps/fsview.png
%{_datadir}/icons/hicolor/32x32/apps/metabar.png
%{_datadir}/icons/hicolor/48x48/apps/metabar.png
%{_datadir}/icons/hicolor/64x64/apps/metabar.png
%{_datadir}/icons/hicolor/scalable/apps/metabar.svgz
%{_datadir}/icons/hicolor/128x128/apps/metabar.png
%{_datadir}/icons/locolor/32x32/apps/konqsidebar_mediaplayer.png
%{_datadir}/services/akregator_konqplugin.desktop
%{_datadir}/services/ark_plugin.desktop
%{_datadir}/services/fsview_part.desktop
%{_datadir}/services/kuick_plugin.desktop
%{_datadir}/services/webarchivethumbnail.desktop
%{tde_libdir}/libadblock.la
%{tde_libdir}/libadblock.so
%{tde_docdir}/HTML/en/konq-plugins/

%if 0%{?fedora}
%{_datadir}/apps/metabar/themes/fedora/
%{_datadir}/config/metabarrc
%endif

%post -n trinity-konq-plugins
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done

%postun -n trinity-konq-plugins
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done

##########

%package -n trinity-ksig
Summary:	Graphical tool for managing multiple email signatures
Group:		Applications/Utilities
Requires:	trinity-kmail

%description -n trinity-ksig
KSig is a graphical tool for keeping track of many different email
signatures.  The signatures themselves can be edited through KSig's
graphical user interface.  A command-line interface is then available
for generating random or daily signatures from this list.

The command-line interface makes a suitable plugin for generating
signatures in external mail clients such as KMail.

%files -n trinity-ksig
%defattr(-,root,root,-)
%{_bindir}/ksig
%{tde_appdir}/ksig.desktop
%{_datadir}/apps/ksig/ksigui.rc
%{_datadir}/icons/hicolor/*/apps/ksig.png
%{tde_docdir}/HTML/en/ksig/

%post -n trinity-ksig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-ksig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-noatun-plugins
Summary:	plugins for Noatun, the Trinity media player
Group:		Applications/Utilities
Requires:	trinity-noatun

%description -n trinity-noatun-plugins
This package contains a variety of useful plugins for Noatun, the audio and
video media player for TDE.  These plugins can be loaded through the plugin
manager in Noatun settings.

Highlights include an alarm clock, guessing tags from filenames, adjustable
playback speed, capture to wave file and displaying lyrics, plus a variety
of user interfaces, playlists and visualisation plugins.

%files -n trinity-noatun-plugins
%defattr(-,root,root,-)
%{_bindir}/noatunsynaescope.bin
%{_bindir}/noatuntippecanoe.bin
%{_bindir}/noatuntyler.bin
%{tde_libdir}/noatunalsaplayer.la
%{tde_libdir}/noatunalsaplayer.so
%{tde_libdir}/noatunblurscope.la
%{tde_libdir}/noatunblurscope.so
%{tde_libdir}/noatuncharlatan.la
%{tde_libdir}/noatuncharlatan.so
%{tde_libdir}/noatundub.la
%{tde_libdir}/noatundub.so
%{tde_libdir}/noatun_ffrs.la
%{tde_libdir}/noatun_ffrs.so
%{tde_libdir}/noatunluckytag.la
%{tde_libdir}/noatunluckytag.so
%{tde_libdir}/noatunlyrics.la
%{tde_libdir}/noatunlyrics.so
%{tde_libdir}/noatunmadness.la
%{tde_libdir}/noatunmadness.so
%{tde_libdir}/noatun_oblique.la
%{tde_libdir}/noatun_oblique.so
%{tde_libdir}/noatunpitchablespeed.la
%{tde_libdir}/noatunpitchablespeed.so
%{tde_libdir}/noatunsynaescope.la
%{tde_libdir}/noatunsynaescope.so
%{tde_libdir}/noatuntippecanoe.la
%{tde_libdir}/noatuntippecanoe.so
%{tde_libdir}/noatuntyler.la
%{tde_libdir}/noatuntyler.so
%{tde_libdir}/noatunwakeup.la
%{tde_libdir}/noatunwakeup.so
%{tde_libdir}/noatunwavecapture.la
%{tde_libdir}/noatunwavecapture.so
%{_datadir}/apps/noatun/*
%{_datadir}/icons/crystalsvg/16x16/apps/synaescope.png

%post -n trinity-noatun-plugins
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done

%postun -n trinity-noatun-plugins
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done

##########



%prep
%setup -q -a 1 -n kdeaddons

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
  --includedir=%{tde_includedir} \
  --disable-rpath \
  --enable-new-ldflags \
  --enable-closure \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final \
  --with-extra-includes=%{_includedir}/tqt


%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# File lists for locale
HTML_DIR=$(kde-config --expandvars --install html)
touch %{name}.lang
if [ -d %{buildroot}/$HTML_DIR ]; then
 for lang_dir in %{buildroot}/$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
    # replace absolute symlinks with relative ones
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../common $i/common
      done
    popd
  fi
 done
fi

# rpmdocs
for dir in konq-plugins ; do
  for file in AUTHORS ChangeLog README TODO ; do
    test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
  done
done

%if 0%{?fedora} > 0
# install fedora metabar theme
cp -prf fedora %{buildroot}%{_datadir}/apps/metabar/themes
install -m644 -p %{SOURCE2} %{buildroot}%{_datadir}/config/
%endif





%clean
%__rm -rf %{buildroot}




%changelog
* Fri Jun 29 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-5
- Split in several packages

* Sat May 05 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Removes SDL patch for noatun

* Thu Dec 15 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Fix content of -extras package
- Fix various packaging issues

* Fri Nov 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Updates BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sat Oct 29 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT

