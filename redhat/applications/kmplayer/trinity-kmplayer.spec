# Default version for this component
%define kdecomp kmplayer
%define version 0.10.0c
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	media player for Trinity
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Multimedia

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://kmplayer.kde.org

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Patch0:		kmplayer-3.5.13-ftbfs.patch

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils

BuildRequires:	libXv-devel
BuildRequires:	dbus-tqt-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel

Requires:	%{name}-base

%description
A basic audio/video viewer application for Trinity.

KMPlayer can:
* play DVD (DVDNav only with the Xine player)
* play VCD
* let the backend players play from a pipe (read from stdin)
* play from a TV device (experimental)
* show backend player's console output
* launch ffserver (only 0.4.8 works) when viewing from a v4l device
* DCOP KMediaPlayer interface support
* VDR viewer frontend (with *kxvplayer), configure VDR keys with standard KDE
  shortcut configure window
* Lots of configurable shortcuts. Highly recommended for the VDR keys
  (if you have VDR) and volume increase/decrease


%package base
Group:			Applications/Multimedia
Summary:		Base files for KMPlayer [Trinity]

%description base
Core files needed for KMPlayer.


%package konq-plugins
Group:			Applications/Multimedia
Requires:		trinity-kmplayer-base, trinity-kdebase
Summary:		KMPlayer plugin for KHTML/Konqueror [Trinity]

%description konq-plugins
This plugin enables audio/video playback inside konqueror, using Xine (with
*kxineplayer) or GStreamer (with *kgstplayer), such as movie trailers, web
tv or radio. It mimics QuickTime, MS Media Player and RealPlayer plugin
browser plugins.


%package doc
Group:			Applications/Multimedia
Requires:		%{name} = %{version}-%{release}
Summary:		Handbook for KMPlayer [Trinity]

%description doc
Documention for KMPlayer, a basic audio/video viewer application for KDE.


%prep
unset QTDIR; . /etc/profile.d/qt.sh
%setup -q -n applications/%{kdecomp}
%patch0 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i "admin/acinclude.m4.in" \
	-e "s,/usr/include/tqt,%{_includedir}/tqt,g" \
	-e "s,kde_htmldir='.*',kde_htmldir='%{tde_docdir}/HTML',g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt:%{_includedir}/dbus-1.0 \
    --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{kdecomp}

%clean
%__rm -rf %{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post base
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
/sbin/ldconfig || :

%postun base
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
/sbin/ldconfig || :

%post konq-plugins -p /sbin/ldconfig
%postun konq-plugins  -p /sbin/ldconfig


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%doc README TODO
%{_bindir}/kmplayer
%{_bindir}/knpplayer
%{_bindir}/kxvplayer
%{_libdir}/libkdeinit_kmplayer.la
%{_libdir}/libkdeinit_kmplayer.so
%{tde_libdir}/kmplayer.la
%{tde_libdir}/kmplayer.so
%{_datadir}/applications/kde/kmplayer.desktop
%{_datadir}/apps/kmplayer
%exclude %{_datadir}/mimelnk/application/x-mplayer2.desktop
%{_datadir}/services/kmplayer_part.desktop

%files base
%defattr(-,root,root,-)
%{_libdir}/libkmplayercommon.la
%{_libdir}/libkmplayercommon.so
%{_bindir}/kgstplayer
%{_bindir}/kxineplayer
%{_datadir}/config/kmplayerrc
%{_datadir}/apps/kmplayer/bookmarks.xml
%{_datadir}/apps/kmplayer/noise.gif
%{_datadir}/apps/kmplayer/pluginsinfo
%{_datadir}/icons/hicolor/*/apps/kmplayer.png
%{_datadir}/icons/hicolor/*/apps/kmplayer.svgz
%{_datadir}/mimelnk/application/x-kmplayer.desktop
%{_datadir}/mimelnk/video/x-ms-wmp.desktop


%files doc
%defattr(-,root,root,-)
%{tde_docdir}/HTML/*/kmplayer

%files konq-plugins
%defattr(-,root,root,-)
%{tde_libdir}/libkmplayerpart.la
%{tde_libdir}/libkmplayerpart.so
%{_datadir}/apps/kmplayer/kmplayerpartui.rc
%{_datadir}/apps/kmplayer/pluginsinfo
%{_datadir}/services/kmplayer_part.desktop


%Changelog
* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.10.0c-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

