# If TDE is built iwn a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}/kde
%define tde_appdir %{_datadir}/applications/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


# Fedora review:  http://bugzilla.redhat.com/195486

## Conditional build:
# RHEL6: xmms is outdated !
#define _with_xmms --with-xmms
%ifnarch s390 s390x
%define _with_wifi --with-wifi
%endif

Name:    tdenetwork
Version: 3.5.13
Release: 5%{?dist}%{?_variant}
Summary: Trinity Desktop Environment - Network Applications

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

License: GPLv2
Group:   Applications/Internet

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: kdenetwork-%{version}.tar.gz
Source1: kppp.pamd
Source2: ktalk
Source4: lisarc
Source5: lisa.redhat

# RedHat/Fedora legacy patches
Patch3: kdenetwork-3.5.8-kppp.patch
Patch4: kdenetwork-3.2.3-resolv.patch
# include more/proper ppp headers
Patch6: kdenetwork-3.5.9-krfb_httpd.patch

# [kdenetwork] Fix kopete protocol compilation [Bug #695]
Patch10:	kdenetwork-3.5.13-kopete_msn_protocol.patch
Patch11:	kdenetwork-3.5.13-kopete_sms_protocol.patch
Patch12:	kdenetwork-3.5.13-kopete_jabber_protocol.patch
Patch13:	kdenetwork-3.5.13-kopete_motionawayplugin_ftbfs.patch
# [kdenetwork] Fix references to "qname.h" [Bug #700]
Patch14:	kdenetwork-3.5.13-reference_to_qmake_h.patch
# WTF is this ? shitty hack in autotool was forgotten in CMAKE port ! [Bug #695]
Source10:	kdenetwork-3.5.13-dummy.cpp
# [tdenetwork] Fix linear alphabet string errors [Commit #3516f9bc]
Patch15:	kdenetwork-3.5.13-fix_alphabet_string_error.patch
# [tdenetwork] Remove "More Applications" from TDE menu. [Bug #653] [Commit #f86a2538]
Patch17:	kdenetwork-3.5.13-remove_more_applications_from_menu.patch
# [tdenetwork] Improve Kaffeine support in Kopete now listening plugin [Commit #f6708531]
Patch18:	kdenetwork-3.5.13-improve_kaffeine_support_in_nowlistening_plugin.patch

BuildRequires:	gettext
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	coreutils 
BuildRequires:	openssl-devel
BuildRequires:  avahi-qt3-devel
BuildRequires:	sqlite-devel
BuildRequires:	libgadu-devel
BuildRequires:	speex-devel

%if 0%{?fedora} > 4 || 0%{?rhel} > 4
BuildRequires: libXmu-devel libXScrnSaver-devel libXtst-devel libXxf86vm-devel
%endif
%if "%{?_with_wifi:1}" == "1"
%if 0%{?fedora} > 5 || 0%{?rhel} > 4
BuildRequires: wireless-tools-devel
%else
BuildRequires: wireless-tools
%endif
%endif
BuildRequires: openslp-devel
%ifarch %{ix86}
# BR: %{_includedir}/valgrind/valgrind.h
BuildRequires: valgrind
%endif
%{?_with_xmms:BuildRequires: xmms-devel}

%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
BuildRequires:	libv4l-devel
%endif

Obsoletes:	trinity-kdenetwork < %{version}-%{release}
Obsoletes:	trinity-kdenetwork-libs
Obsoletes:	trinity-kdenetwork-extras
Provides:	trinity-kdenetwork = %{version}-%{release}
Provides:	trinity-kdenetwork-extras = %{version}-%{release}

Requires: usermode-gtk

Requires: trinity-dcoprss = %{version}-%{release}
Requires: %{name}-filesharing = %{version}-%{release}
Requires: trinity-kdict = %{version}-%{release}
Requires: %{name}-kfile-plugins = %{version}-%{release}
Requires: trinity-kget = %{version}-%{release}
Requires: trinity-knewsticker = %{version}-%{release}
Requires: trinity-kopete = %{version}-%{release}
Requires: trinity-kopete-nowlistening = %{version}-%{release}
Requires: trinity-kpf = %{version}-%{release}
Requires: trinity-kppp = %{version}-%{release}
Requires: trinity-krdc = %{version}-%{release}
Requires: trinity-krfb = %{version}-%{release}
Requires: trinity-ksirc = %{version}-%{release}
Requires: trinity-ktalkd = %{version}-%{release}
Requires: trinity-kwifimanager = %{version}-%{release}
Requires: trinity-librss = %{version}-%{release}
Requires: trinity-lisa = %{version}-%{release}

%description
This metapackage includes a collection of network and networking related
applications provided with the official release of Trinity.

Networking applications, including:
* dcoprss: RSS utilities for Trinity
* filesharing: Network filesharing configuration module for Trinity
* kdict: Dictionary client for Trinity
* kfile-plugins: Torrent metainfo plugin for Trinity
* kget: downloader manager
* knewsticker: RDF newsticker applet
* kopete: chat client
* kopete-nowlistening: (xmms) plugin for Kopete.
* kpf: Public fileserver for Trinity
* kppp: dialer and front end for pppd
* krdc: a client for Desktop Sharing and other VNC servers
* krfb: Desktop Sharing server, allow others to access your desktop via VNC
* ksirc: IRC client for Trinity
* ktalkd: Talk daemon for Trinity
* kwifimanager: Wireless lan manager for Trinity
* librss: RSS library for Trinity
* lisa: lan information server


##########

%package -n trinity-dcoprss
Summary:		RSS utilities for Trinity
Group:			Applications/Internet

%description -n trinity-dcoprss
dcoprss is a RSS to DCOP bridge, allowing all
DCOP aware applications to access RSS news feeds. There is also
a few sample utilities provided.
RSS is a standard for publishing news headlines.
DCOP is the TDE interprocess communication protocol.

%files -n trinity-dcoprss
%defattr(-,root,root,-)
%{_bindir}/feedbrowser
%{_bindir}/rssclient
%{_bindir}/rssservice
%{_datadir}/services/rssservice.desktop

%post -n trinity-dcoprss
update-desktop-database 2> /dev/null || : 

%postun -n trinity-dcoprss
update-desktop-database 2> /dev/null || : 

##########

%package devel
Summary:		Development files for the Trinity network module
Group:			Development/Libraries
Requires:		trinity-kdict = %{version}-%{release}
Requires:		trinity-kopete = %{version}-%{release}
Requires:		trinity-ksirc = %{version}-%{release}
Requires:		trinity-librss = %{version}-%{release}
Requires:		trinity-kdelibs-devel

Obsoletes:	trinity-kdenetwork-devel < %{version}-%{release}
Provides:	trinity-kdenetwork-devel = %{version}-%{release}

%description devel
This is the development package which contains the headers for the KDE RSS
library as well as the Kopete chat client, as well as miscellaneous
development-related files for the TDE network module.

%files devel
%defattr(-,root,root,-)
%{_includedir}/kopete/*.h
%{_includedir}/kopete/ui/*.h
%{_includedir}/rss/*.h
%{_libdir}/libkdeinit_kdict.la
%{_libdir}/libkdeinit_ksirc.la
%{_libdir}/libkopete.la
%{_libdir}/libkopete.so
%{_libdir}/libkopete_msn_shared.la
%{_libdir}/libkopete_msn_shared.so
%{_libdir}/libkopete_oscar.la
%{_libdir}/libkopete_oscar.so
%{_libdir}/libkopete_videodevice.la
%{_libdir}/libkopete_videodevice.so
%{_libdir}/librss.la
%{_libdir}/librss.so

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

##########

%package filesharing
#Recommends:	perl-suid
Summary:		Network filesharing configuration module for Trinity
Group:   		Applications/Internet

%description filesharing
This package provides a TDE Control Center module to configure
NFS and Samba.

%files filesharing
%defattr(-,root,root,-)
%{tde_libdir}/fileshare_propsdlgplugin.la
%{tde_libdir}/fileshare_propsdlgplugin.so
%{tde_libdir}/kcm_fileshare.la
%{tde_libdir}/kcm_fileshare.so
%{tde_libdir}/kcm_kcmsambaconf.la
%{tde_libdir}/kcm_kcmsambaconf.so
%{tde_appdir}/fileshare.desktop
%{tde_appdir}/kcmsambaconf.desktop
%{_datadir}/icons/hicolor/*/apps/kcmsambaconf.png
%{_datadir}/services/fileshare_propsdlgplugin.desktop

%post filesharing
for f in hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

%postun filesharing
for f in hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

##########

%package -n trinity-kdict
Summary:		Dictionary client for Trinity
Group:			Applications/Internet

%description -n trinity-kdict
KDict is an advanced TDE graphical client for the DICT Protocol, with full
Unicode support. It enables you to search through dictionary databases for a
word or phrase, then displays suitable definitions. KDict tries to ease
basic as well as advanced queries.

%files -n trinity-kdict
%defattr(-,root,root,-)
%{_bindir}/kdict
%{tde_libdir}/kdict.*
%{tde_libdir}/kdict_panelapplet.*
%{_libdir}/libkdeinit_kdict.*
%{tde_appdir}/kdict.desktop
%{_datadir}/apps/kdict
%{_datadir}/apps/kicker/applets/kdictapplet.desktop
%{_datadir}/icons/hicolor/*/apps/kdict.*
%{tde_docdir}/HTML/en/kdict

%post -n trinity-kdict
for f in hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

%postun -n trinity-kdict
for f in hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

##########

%package kfile-plugins
Summary:		Torrent metainfo plugin for Trinity
Group:			Applications/Internet

%description kfile-plugins
This package provides a metainformation plugin for bittorrent files.
TDE uses kfile-plugins to provide metainfo tab in the files properties
dialog in konqueror and other file-handling applications.

%files kfile-plugins
%{tde_libdir}/kfile_torrent.la
%{tde_libdir}/kfile_torrent.so
%{_datadir}/services/kfile_torrent.desktop

%post kfile-plugins
update-desktop-database 2> /dev/null || : 

%postun kfile-plugins
update-desktop-database 2> /dev/null || : 

##########

%package -n trinity-kget
Summary:		download manager for Trinity
Group:			Applications/Internet

%description -n trinity-kget
KGet is a a download manager similar to GetRight or Go!zilla. It keeps
all your downloads in one dialog and you can add and remove transfers.
Transfers can be paused, resumed, queued or scheduled.
Dialogs display info about status of transfers - progress, size, speed
and remaining time. Program supports drag & drop from TDE
applications and Netscape.

%files -n trinity-kget
%defattr(-,root,root,-)
%{_bindir}/kget
%{tde_libdir}/khtml_kget.la
%{tde_libdir}/khtml_kget.so
%{tde_appdir}/kget.desktop
%{_datadir}/apps/kget
%{_datadir}/apps/khtml/kpartplugins/kget_plug_in.desktop
%{_datadir}/apps/khtml/kpartplugins/kget_plug_in.rc
%{_datadir}/apps/konqueror/servicemenus/kget_download.desktop
%{_datadir}/icons/crystalsvg/*/actions/khtml_kget.png
%{_datadir}/icons/crystalsvg/*/apps/kget.png
%{_datadir}/icons/crystalsvg/*/mimetypes/kget_list.png
%{_datadir}/mimelnk/application/x-kgetlist.desktop
%{_datadir}/sounds/KGet_Added.ogg
%{_datadir}/sounds/KGet_Finished.ogg
%{_datadir}/sounds/KGet_Finished_All.ogg
%{_datadir}/sounds/KGet_Started.ogg
%{tde_docdir}/HTML/en/kget

%post -n trinity-kget
for f in crystalsvg ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

%postun -n trinity-kget
for f in crystalsvg ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

##########

%package -n trinity-knewsticker
Summary:		news ticker applet for Trinity
Group:			Applications/Internet

%description -n trinity-knewsticker
This is a news ticker applet for the Trinity panel. It can scroll news from
your favorite news sites, such as lwn.net, /. and freshmeat.net.
To achieve this, KNewsTicker requires the news sites to provide a
RSS feed to newsitems. KNewsTicker already comes with a selection of
good news sources which provide such files.

%files -n trinity-knewsticker
%defattr(-,root,root,-)
%{_bindir}/knewstickerstub
%{tde_libdir}/knewsticker_panelapplet.la
%{tde_libdir}/knewsticker_panelapplet.so
%{tde_libdir}/kntsrcfilepropsdlg.la
%{tde_libdir}/kntsrcfilepropsdlg.so
%{tde_appdir}/knewsticker-standalone.desktop
%{_datadir}/applnk/.hidden/knewstickerstub.desktop
%{_datadir}/apps/kconf_update/knewsticker.upd
%{_datadir}/apps/kconf_update/knt-0.1-0.2.pl
%{_datadir}/apps/kicker/applets/knewsticker.desktop
%{_datadir}/apps/knewsticker/eventsrc
%{_datadir}/icons/hicolor/*/apps/knewsticker.png
%{_datadir}/services/kntsrcfilepropsdlg.desktop
%{tde_docdir}/HTML/en/knewsticker

%post -n trinity-knewsticker
for f in hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

%postun -n trinity-knewsticker
for f in hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

##########

%package -n trinity-kopete
Summary:		instant messenger for Trinity
Group:			Applications/Internet
URL:			http://kopete.kde.org

#Recommends: qca-tls
#Suggests: tdeartwork-emoticons-trinity, khelpcenter-trinity, imagemagick, gnupg, gnomemeeting
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	meanwhile-devel
#jabber
BuildRequires:	libidn-devel
#jabber/jingle
BuildRequires:	expat-devel
BuildRequires:	glib2-devel
BuildRequires:	ortp-devel
BuildRequires:	speex-devel
# jabber/ssl
#{?fedora:Requires(hint): qca-tls}
Requires:		jasper

%description -n trinity-kopete
Kopete is an instant messenger program which can communicate with a variety
of IM systems, such as Yahoo, ICQ, MSN, IRC and Jabber.

Support for more IM protocols can be added through a plugin system.

%files -n trinity-kopete
%defattr(-,root,root,-)
# nowlistening support
%exclude %{_datadir}/apps/kopete/*nowlisteningchatui*
%exclude %{_datadir}/apps/kopete/*nowlisteningui*
%exclude %{_datadir}/config.kcfg/nowlisteningconfig.kcfg
%exclude %{_datadir}/services/kconfiguredialog/*nowlistening*
%exclude %{_datadir}/services/*nowlistening*
%exclude %{tde_libdir}/*nowlistening*
# Main kopete package
%{_bindir}/kopete
%{_bindir}/kopete_latexconvert.sh
%{_libdir}/kconf_update_bin/kopete_account_kconf_update
%{_libdir}/kconf_update_bin/kopete_nameTracking_kconf_update
%{_libdir}/kconf_update_bin/kopete_pluginloader2_kconf_update
%{tde_libdir}/kcm_kopete_*.so
%{tde_libdir}/kcm_kopete_*.la
%{tde_libdir}/kio_jabberdisco.la
%{tde_libdir}/kio_jabberdisco.so
%{tde_libdir}/kopete_*.la
%{tde_libdir}/kopete_*.so
%{tde_libdir}/libkrichtexteditpart.la
%{tde_libdir}/libkrichtexteditpart.so
%{_libdir}/libkopete_msn_shared.so.*
%{_libdir}/libkopete_oscar.so.*
%{_libdir}/libkopete.so.*
%{_libdir}/libkopete_videodevice.so.*
%{tde_appdir}/kopete.desktop
%{_datadir}/apps/kconf_update/kopete-*
%{_datadir}/apps/kopete
%{_datadir}/apps/kopete_*/*.rc
%{_datadir}/apps/kopeterichtexteditpart/kopeterichtexteditpartfull.rc
%{_datadir}/config.kcfg/historyconfig.kcfg
%{_datadir}/config.kcfg/kopeteidentityconfigpreferences.kcfg
%{_datadir}/config.kcfg/kopete.kcfg
%{_datadir}/config.kcfg/latexconfig.kcfg
%{_datadir}/icons/crystalsvg/*/actions/voicecall.png
%{_datadir}/icons/crystalsvg/*/actions/webcamreceive.png
%{_datadir}/icons/crystalsvg/*/actions/webcamsend.png
%{_datadir}/icons/crystalsvg/*/actions/account_offline_overlay.png
%{_datadir}/icons/crystalsvg/*/actions/add_user.png
%{_datadir}/icons/crystalsvg/*/actions/contact_away_overlay.png
%{_datadir}/icons/crystalsvg/*/actions/contact_busy_overlay.png
%{_datadir}/icons/crystalsvg/*/actions/contact_food_overlay.png
%{_datadir}/icons/crystalsvg/*/actions/contact_invisible_overlay.png
%{_datadir}/icons/crystalsvg/*/actions/contact_phone_overlay.png
%{_datadir}/icons/crystalsvg/*/actions/contact_xa_overlay.png
%{_datadir}/icons/crystalsvg/*/actions/delete_user.png
%{_datadir}/icons/crystalsvg/*/actions/edit_user.png
%{_datadir}/icons/crystalsvg/*/actions/emoticon.png
%{_datadir}/icons/crystalsvg/*/actions/jabber_away.png
%{_datadir}/icons/crystalsvg/*/actions/jabber_chatty.png
#%{_datadir}/icons/crystalsvg/*/actions/jabber_connecting.mng
%{_datadir}/icons/crystalsvg/*/actions/jabber_group.png
%{_datadir}/icons/crystalsvg/*/actions/jabber_invisible.png
%{_datadir}/icons/crystalsvg/*/actions/jabber_na.png
%{_datadir}/icons/crystalsvg/*/actions/jabber_offline.png
%{_datadir}/icons/crystalsvg/*/actions/jabber_online.png
%{_datadir}/icons/crystalsvg/*/actions/jabber_original.png
%{_datadir}/icons/crystalsvg/*/actions/jabber_raw.png
%{_datadir}/icons/crystalsvg/*/actions/jabber_serv_off.png
%{_datadir}/icons/crystalsvg/*/actions/jabber_serv_on.png
%{_datadir}/icons/crystalsvg/*/actions/jabber_xa.png
%{_datadir}/icons/crystalsvg/*/actions/kopeteavailable.png
%{_datadir}/icons/crystalsvg/*/actions/kopeteaway.png
%{_datadir}/icons/crystalsvg/*/actions/kopeteeditstatusmessage.png
%{_datadir}/icons/crystalsvg/*/actions/kopetestatusmessage.png
%{_datadir}/icons/crystalsvg/*/actions/metacontact_away.png
%{_datadir}/icons/crystalsvg/*/actions/metacontact_offline.png
%{_datadir}/icons/crystalsvg/*/actions/metacontact_online.png
%{_datadir}/icons/crystalsvg/*/actions/metacontact_unknown.png
%{_datadir}/icons/crystalsvg/*/actions/newmsg.png
%{_datadir}/icons/crystalsvg/*/actions/search_user.png
%{_datadir}/icons/crystalsvg/*/actions/show_offliners.png
%{_datadir}/icons/crystalsvg/*/actions/status_unknown_overlay.png
%{_datadir}/icons/crystalsvg/*/actions/status_unknown.png
%{_datadir}/icons/crystalsvg/*/apps/jabber_gateway_aim.png
%{_datadir}/icons/crystalsvg/*/apps/jabber_gateway_gadu.png
%{_datadir}/icons/crystalsvg/*/apps/jabber_gateway_http-ws.png
%{_datadir}/icons/crystalsvg/*/apps/jabber_gateway_icq.png
%{_datadir}/icons/crystalsvg/*/apps/jabber_gateway_irc.png
%{_datadir}/icons/crystalsvg/*/apps/jabber_gateway_msn.png
%{_datadir}/icons/crystalsvg/*/apps/jabber_gateway_qq.png
%{_datadir}/icons/crystalsvg/*/apps/jabber_gateway_smtp.png
%{_datadir}/icons/crystalsvg/*/apps/jabber_gateway_tlen.png
%{_datadir}/icons/crystalsvg/*/apps/jabber_gateway_yahoo.png
%{_datadir}/icons/crystalsvg/*/apps/jabber_protocol.png
%{_datadir}/icons/crystalsvg/*/apps/kopete_all_away.png
%{_datadir}/icons/crystalsvg/*/apps/kopete_offline.png
%{_datadir}/icons/crystalsvg/*/apps/kopete_some_away.png
%{_datadir}/icons/crystalsvg/*/apps/kopete_some_online.png
%{_datadir}/icons/crystalsvg/*/mimetypes/kopete_emoticons.png
%{_datadir}/icons/crystalsvg/scalable/actions/account_offline_overlay.svgz
%{_datadir}/icons/hicolor/*/apps/kopete.png
%{_datadir}/icons/hicolor/*/actions/emoticon.png
%{_datadir}/icons/hicolor/*/actions/jabber_away.png
%{_datadir}/icons/hicolor/*/actions/jabber_chatty.png
#%{_datadir}/icons/hicolor/*/actions/jabber_connecting.mng
%{_datadir}/icons/hicolor/*/actions/jabber_group.png
%{_datadir}/icons/hicolor/*/actions/jabber_invisible.png
%{_datadir}/icons/hicolor/*/actions/jabber_na.png
%{_datadir}/icons/hicolor/*/actions/jabber_offline.png
%{_datadir}/icons/hicolor/*/actions/jabber_online.png
%{_datadir}/icons/hicolor/*/actions/jabber_original.png
%{_datadir}/icons/hicolor/*/actions/jabber_raw.png
%{_datadir}/icons/hicolor/*/actions/jabber_serv_off.png
%{_datadir}/icons/hicolor/*/actions/jabber_serv_on.png
%{_datadir}/icons/hicolor/*/actions/jabber_xa.png
%{_datadir}/icons/hicolor/*/actions/kopeteavailable.png
%{_datadir}/icons/hicolor/*/actions/kopeteaway.png
%{_datadir}/icons/hicolor/*/actions/newmsg.png
%{_datadir}/icons/hicolor/*/actions/status_unknown_overlay.png
%{_datadir}/icons/hicolor/*/actions/status_unknown.png
%{_datadir}/icons/hicolor/*/apps/jabber_protocol.png
%{_datadir}/icons/hicolor/scalable/apps/kopete2.svgz
%{_datadir}/mimelnk/application/x-icq.desktop
%{_datadir}/mimelnk/application/x-kopete-emoticons.desktop
%{_datadir}/services/aim.protocol
%{_datadir}/services/chatwindow.desktop
%{_datadir}/services/emailwindow.desktop
#%{_datadir}/services/irc.protocol /opt/trinity/share/apps/kopete/
%{_datadir}/services/jabberdisco.protocol
%{_datadir}/services/kconfiguredialog/kopete_*.desktop
%{_datadir}/services/kopete_*.desktop
%{_datadir}/icons/crystalsvg/16x16/apps/jabber_gateway_sms.png
%{_datadir}/servicetypes/kopete*.desktop
%{_datadir}/sounds/Kopete_*.ogg
%{tde_docdir}/HTML/en/kopete
# jingle support for kopete
%{_bindir}/relayserver
%{_bindir}/stunserver
# winpopup support for kopete
%{_bindir}/winpopup-install.sh
%{_bindir}/winpopup-send.sh
# meanwhile protocol support for kopete
%{tde_libdir}/new_target0.la
%{tde_libdir}/new_target0.so
# motionaway plugin for kopete
%{_datadir}/config.kcfg/motionawayconfig.kcfg
# smpp plugin for kopete
%{_datadir}/config.kcfg/smpppdcs.kcfg


%post -n trinity-kopete
for f in crystalsvg hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 
/sbin/ldconfig

%postun -n trinity-kopete
for f in crystalsvg hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 
/sbin/ldconfig

##########

%package -n trinity-kopete-nowlistening
Summary:		Nowlistening (xmms) plugin for Kopete.
Group:			Applications/Internet

%description -n trinity-kopete-nowlistening
Kopete includes the "Now Listening" plug-in that can report what music you
are currently listening to, in a number of different players, including
noatun, kscd, juk, kaffeine and amarok.

%files -n trinity-kopete-nowlistening
%defattr(-,root,root,-)
%{_datadir}/apps/kopete/*nowlisteningchatui*
%{_datadir}/apps/kopete/*nowlisteningui*
%{_datadir}/config.kcfg/nowlisteningconfig.kcfg
%{_datadir}/services/kconfiguredialog/*nowlistening*
%{_datadir}/services/*nowlistening*
%{tde_libdir}/*nowlistening*

##########

%package -n trinity-kpf
Summary:		Public fileserver for Trinity
Group:			Applications/Internet

%description -n trinity-kpf
kpf provides simple file sharing using HTTP. kpf is strictly a public
fileserver, which means that there are no access restrictions to shared
files. Whatever you select for sharing is available to anyone. kpf is
designed to be used for sharing files with friends.

%files -n trinity-kpf
%defattr(-,root,root,-)
%{tde_libdir}/kpf*
%{_datadir}/apps/kicker/applets/kpfapplet.desktop
%{_datadir}/icons/crystalsvg/*/apps/kpf.*
%{_datadir}/services/kpfpropertiesdialogplugin.desktop
%{tde_docdir}/HTML/en/kpf

%post -n trinity-kpf
for f in crystalsvg ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

%postun -n trinity-kpf
for f in crystalsvg ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

##########

%package -n trinity-kppp
Summary:		modem dialer and ppp frontend for Trinity
Group:			Applications/Internet
Requires:		ppp

%description -n trinity-kppp
KPPP is a dialer and front end for pppd. It allows for interactive
script generation and network setup. It will automate the dialing in
process to your ISP while letting you conveniently monitor the entire
process.

Once connected KPPP will provide a rich set of statistics and keep
track of the time spent online for you.

%files -n trinity-kppp
%defattr(-,root,root,-)
%config(noreplace) /etc/security/console.apps/kppp3
%config(noreplace) /etc/pam.d/kppp3
%{_bindir}/kppp
%{_bindir}/kppplogview
%{_sbindir}/kppp
%{tde_appdir}/Kppp.desktop
%{tde_appdir}/kppplogview.desktop
%{_datadir}/apps/checkrules
%{_datadir}/apps/kppp
%{_datadir}/icons/hicolor/*/apps/kppp.png
%{tde_docdir}/HTML/en/kppp

%post -n trinity-kppp
for f in hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

%postun -n trinity-kppp
for f in hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

##########

%package -n trinity-krdc
Summary:		Remote Desktop Connection for Trinity
Group:			Applications/Internet
Requires:		rdesktop

%description -n trinity-krdc
krdc is an TDE graphical client for the rfb protocol, used by VNC,
and if rdesktop is installed, krdc can connect to Windows Terminal
Servers using RDP.

%files -n trinity-krdc
%defattr(-,root,root,-)
%{_bindir}/krdc
%{tde_appdir}/krdc.desktop
%{_datadir}/apps/konqueror/servicemenus/smb2rdc.desktop
%{_datadir}/apps/krdc
%{_datadir}/icons/crystalsvg/*/apps/krdc.png
%{_datadir}/services/rdp.protocol
%{_datadir}/services/vnc.protocol
%{tde_docdir}/HTML/en/krdc

%post -n trinity-krdc
for f in crystalsvg ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

%postun -n trinity-krdc
for f in crystalsvg ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

##########

%package -n trinity-krfb
Summary:		Desktop Sharing for Trinity
Group:			Applications/Internet

%description -n trinity-krfb
Desktop Sharing (krfb) is a server application that allows you to share
your current session with a user on another machine, who can use a
VNC client like krdc to view or even control the desktop. It doesn't
require you to start a new X session - it can share the current session.
This makes it very useful when you want someone to help you perform a
task.

%files -n trinity-krfb
%defattr(-,root,root,-)
%{_bindir}/krfb
%{_bindir}/krfb_httpd
%{tde_libdir}/kcm_krfb.la
%{tde_libdir}/kcm_krfb.so
%{tde_libdir}/kded_kinetd.la
%{tde_libdir}/kded_kinetd.so
%{tde_appdir}/kcmkrfb.desktop
%{tde_appdir}/krfb.desktop
%{_datadir}/apps/kinetd/eventsrc
%{_datadir}/apps/krfb
%{_datadir}/icons/crystalsvg/*/apps/krfb.png
%{_datadir}/icons/locolor/*/apps/krfb.png
%{_datadir}/services/kded/kinetd.desktop
%{_datadir}/services/kinetd_krfb.desktop
%{_datadir}/services/kinetd_krfb_httpd.desktop
%{_datadir}/servicetypes/kinetdmodule.desktop
%{tde_docdir}/HTML/en/krfb

%post -n trinity-krfb
for f in crystalsvg locolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

%postun -n trinity-krfb
for f in crystalsvg locolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

##########

%package -n trinity-ksirc
Summary:		IRC client for Trinity
Group:			Applications/Internet

%description -n trinity-ksirc
KSirc is an IRC chat client for KDE. It supports scripting with Perl and has a
lot of compatibility with mIRC for general use.

If you want to connect to an IRC server via SSL, you will need to install the
recommended package libio-socket-ssl-perl.

%files -n trinity-ksirc
%defattr(-,root,root,-)
%{_bindir}/dsirc
%{_bindir}/ksirc
%{_libdir}/libkdeinit_ksirc.*
%{tde_libdir}/ksirc.*
%{tde_appdir}/ksirc.desktop
%{_datadir}/apps/ksirc/
%config(noreplace) %{_datadir}/config/ksircrc
%{_datadir}/icons/hicolor/*/apps/ksirc.*
%{tde_docdir}/HTML/??/ksirc/

%post -n trinity-ksirc
for f in hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 
/sbin/ldconfig


%postun -n trinity-ksirc
for f in hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 
/sbin/ldconfig

##########

%package -n trinity-ktalkd
Summary:		Talk daemon for Trinity
Group:			Applications/Internet

%description -n trinity-ktalkd
KTalkd is an enhanced talk daemon - a program to handle incoming talk
requests, announce them and allow you to respond to it using a talk
client. Note that KTalkd is designed to run on a single-user workstation,
and shouldn't be run on a multi-user machine.

%files -n trinity-ktalkd
%defattr(-,root,root,-)
%{_bindir}/ktalkd*
%{_bindir}/mail.local
%{tde_libdir}/kcm_ktalkd.*
%{tde_appdir}/kcmktalkd.desktop
%config(noreplace) %{_datadir}/config/ktalkdrc
%{_datadir}/icons/crystalsvg/*/apps/ktalkd.*
%{_datadir}/sounds/ktalkd.wav
%config(noreplace) %{_sysconfdir}/xinetd.d/ktalk
%{tde_docdir}/HTML/en/kcontrol/kcmtalkd
%{tde_docdir}/HTML/en/ktalkd

%post -n trinity-ktalkd
for f in crystalsvg ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

%postun -n trinity-ktalkd
for f in crystalsvg ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

##########

%if "%{?_with_wifi:1}" == "1"
%package -n trinity-kwifimanager
#Depends: ${shlibs:Depends}, wireless-tools
#Suggests: khelpcenter-trinity
Summary:		Wireless lan manager for Trinity
Group:			Applications/Internet

%description -n trinity-kwifimanager
KWiFiManager suite is a set of tools which allows you to manage your
wireless LAN connection under the K Desktop Environment. It provides
information about your current connection. KWiFiManager supports every
wavelan card that uses the wireless extensions interface.

%files -n trinity-kwifimanager
%defattr(-,root,root,-)
%{_bindir}/kwifimanager
%{tde_libdir}/kcm_wifi.*
%{tde_libdir}/libkwireless.la
%{tde_libdir}/libkwireless.so
%{tde_appdir}/kcmwifi.desktop
%{tde_appdir}/kwifimanager.desktop
%{_datadir}/apps/kicker/applets/kwireless.desktop
%{_datadir}/apps/kwifimanager
%{_datadir}/icons/hicolor/*/apps/kwifimanager.png
%{_datadir}/icons/hicolor/*/apps/kwifimanager.svgz
%doc %{tde_docdir}/HTML/en/kwifimanager

%post -n trinity-kwifimanager
for f in hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 

%postun -n trinity-kwifimanager
for f in hicolor ; do
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f}  2> /dev/null || :
done
update-desktop-database 2> /dev/null || : 
%endif

##########

%package -n trinity-librss
Summary:		RSS library for Trinity
Group:			Environment/Libraries

%description -n trinity-librss
This is the runtime package for programs that use the TDE RSS library.
End users should not need to install this, it should get installed
automatically when needed.

%files -n trinity-librss
%defattr(-,root,root,-)
%{_libdir}/librss.so.*

%post -n trinity-librss
/sbin/ldconfig

%postun -n trinity-librss
/sbin/ldconfig

##########

%package -n trinity-lisa
Summary:			LAN information server for Trinity
Group:				Applications/Internet
Requires(preun):	chkconfig
Requires(post):		chkconfig

%description -n trinity-lisa
LISa is intended to provide KDE with a kind of "network neighborhood"
but relying only on the TCP/IP protocol.

%files -n trinity-lisa
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/lisarc*
%config(noreplace) %{_initrddir}/lisa
%{tde_libdir}/kcm_lanbrowser.la
%{tde_libdir}/kcm_lanbrowser.so
%{tde_libdir}/kio_lan.la
%{tde_libdir}/kio_lan.so
%{_datadir}/applnk/.hidden/kcmkiolan.desktop
%{_datadir}/applnk/.hidden/kcmlisa.desktop
%{_datadir}/applnk/.hidden/kcmreslisa.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/lisa.desktop
%{_datadir}/apps/konqueror/dirtree/remote/lan.desktop
%{_datadir}/apps/lisa/README
%{_datadir}/apps/remoteview/lan.desktop
%{tde_docdir}/HTML/en/kcontrol/lanbrowser/common
%{tde_docdir}/HTML/en/kcontrol/lanbrowser/index.cache.bz2
%{tde_docdir}/HTML/en/kcontrol/lanbrowser/index.docbook
%{tde_docdir}/HTML/en/lisa
%{_datadir}/services/lan.protocol
%{_datadir}/services/rlan.protocol
%{_bindir}/lisa
%{_bindir}/reslisa

%post -n trinity-lisa
/sbin/chkconfig --add lisa ||:
update-desktop-database 2> /dev/null || : 

%postun -n trinity-lisa
if [ $1 -eq 0 ]; then
  /sbin/chkconfig --del lisa ||:
  /sbin/service lisa stop > /dev/null 2>&1 ||:
fi
update-desktop-database 2> /dev/null || : 

##########

%package -n trinity-kdnssd
#Recommends: avahi-daemon
#Suggests: avahi-autoipd | zeroconf
Summary: Zeroconf support for KDE
Group:			Applications/Internet

%description -n trinity-kdnssd
A kioslave and kded module that provide Zeroconf support. Try
"zeroconf:/" in Konqueror.

%files -n trinity-kdnssd
%defattr(-,root,root,-)
%{_datadir}/services/zeroconf.protocol
%{_datadir}/services/invitation.protocol
%{_datadir}/services/kded/dnssdwatcher.desktop
%{_datadir}/apps/remoteview/zeroconf.desktop
%{_datadir}/apps/zeroconf/_http._tcp
%{_datadir}/apps/zeroconf/_ftp._tcp
%{_datadir}/apps/zeroconf/_ldap._tcp
%{_datadir}/apps/zeroconf/_webdav._tcp
%{_datadir}/apps/zeroconf/_nfs._tcp
%{_datadir}/apps/zeroconf/_ssh._tcp
%{_datadir}/apps/zeroconf/_rfb._tcp
%{tde_libdir}/kio_zeroconf.so
%{tde_libdir}/kio_zeroconf.la
%{tde_libdir}/kded_dnssdwatcher.so
%{tde_libdir}/kded_dnssdwatcher.la

%post -n trinity-kdnssd
update-desktop-database 2> /dev/null || : 

%postun -n trinity-kdnssd
update-desktop-database 2> /dev/null || : 

##########

%prep
%setup -q -n kdenetwork

%patch3 -p1 -b .kppp
%patch4 -p1 -b .resolv
%patch6 -p1 -b .krfb_httpd
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p4
%patch15 -p1
%patch17 -p1
%patch18 -p1


# TDE 3.5.13: missing 'dummy.cpp' in MSN protocol
%__install -m 644 %{SOURCE10} kopete/protocols/msn/dummy.cpp

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"
export LD_LIBRARY_PATH="%{_libdir}"

%__mkdir build
cd build
%cmake \
  -DWITH_JINGLE=ON \
  -DWITH_SPEEX=ON \
  -DWITH_WEBCAM=ON \
  -DWITH_GSM=OFF \
  -DWITH_ARTS=ON \
  -DBUILD_ALL=ON \
  -DBUILD_KOPETE_PROTOCOL_ALL=ON \
  -DBUILD_KOPETE_PLUGIN_ALL=ON \
  ..

# kdenetwork building is not SMP safe
%__make 


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


## File lists
# locale's
%find_lang %{name} || touch %{name}.lang
# HTML (1.0)
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}$HTML_DIR ]; then
for lang_dir in %{buildroot}$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
    # replace absolute symlinks with relative ones
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && %{__rm} -f $i/common && ln -sf ../common $i/common
      done
    popd
  fi
done
fi

# Show only in KDE, FIXME, need to re-evaluate these -- Rex
for i in fileshare kcmkrfb kcmktalkd kcmwifi krfb kppp kppplogview \
   kwifimanager kget knewsticker ksirc kdict ; do
   if [ -f %{buildroot}%{_datadir}/applications/kde/$i.desktop ] ; then
      echo "OnlyShowIn=KDE;" >> %{buildroot}%{_datadir}/applications/kde/$i.desktop
   fi
done

# Run kppp through consolehelper
install -p -m644 -D %{SOURCE1} %{buildroot}/etc/pam.d/kppp3
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/kppp %{buildroot}%{_sbindir}
ln -s /usr/bin/consolehelper %{buildroot}%{_bindir}/kppp
mkdir -p %{buildroot}/etc/security/console.apps
cat > %{buildroot}/etc/security/console.apps/kppp3 <<EOF
USER=root
PROGRAM=%{_sbindir}/kppp
SESSION=true
EOF

# ktalk
%__install -p -m 0644 -D  %{SOURCE2} %{buildroot}%{_sysconfdir}/xinetd.d/ktalk

# Add lisa startup script
%__install -p -m 0644 -D %{SOURCE4} %{buildroot}%{_sysconfdir}/lisarc
%__install -p -m 0755 -D %{SOURCE5} %{buildroot}%{_initrddir}/lisa

# RHEL 5: Avoids conflict with 'kdenetwork'
%if 0%{?rhel} == 5
%__mv -f %{buildroot}%{_sysconfdir}/lisarc %{buildroot}%{_sysconfdir}/lisarc.tde
%endif

# Avoids conflict with trinity-kvirc
%__mv -f %{buildroot}%{_datadir}/services/irc.protocol %{buildroot}%{_datadir}/apps/kopete/

%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README


%changelog
* Sat Jun 16 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-5
- Split single package in multiple packages
- Removes useless 'Provides'
- Updates 'BuildRequires'
- Fix linear alphabet string errors [Commit #3516f9bc]
- Remove "More Applications" from TDE menu. [Bug #653] [Commit #f86a2538]
- Improve Kaffeine support in Kopete now listening plugin [Commit #f6708531]

* Sun Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Enable Kopete protocols & plugins compilation
- Enables all features (openslp, jingle, ...) on all distros
- Moves 'irc.protocol' file to prevent conflict with other packages

* Thu Nov 17 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Fix symbolic link to 'consolehelper'

* Sat Nov 12 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Removes conflict on file 'lisarc' for RHEL 5

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Tue Oct 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT

