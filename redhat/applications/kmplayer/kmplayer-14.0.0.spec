# Default version for this component
%define tde_pkg kmplayer
%define tde_version 14.0.0

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		media player for Trinity
Version:		0.10.0c
Release:		%{?!preversion:6}%{?preversion:5_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Multimedia

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://kmplayer.kde.org

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils


# GSTREAMER support
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos}
BuildRequires:	libgstreamer0.10-devel
%else
BuildRequires:	%{_lib}gstreamer0.10-devel
%endif
BuildRequires:	%{_lib}gstreamer-plugins-base0.10-devel
%endif
%if 0%{?rhel} == 4
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-devel
%endif
%if 0%{?rhel} >= 5|| 0%{?fedora}
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
%endif
%if 0%{?suse_version}
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-0_10-plugins-base-devel
%endif

# X11 stuff
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	libxv-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version} >= 1210
BuildRequires:	libXv-devel
%endif
%if 0%{?rhel} == 4
BuildRequires:	xorg-x11-devel 
%endif
%if 0%{?suse_version} == 1140
BuildRequires:	xorg-x11-libXv-devel
%endif

Requires:		%{name}-base = %{version}-%{release}

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
* VDR viewer frontend (with *kxvplayer), configure VDR keys with standard TDE
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
Requires:		%{name}-base = %{version}-%{release}
Requires:		trinity-tdebase >= %{tde_version}
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
Documention for KMPlayer, a basic audio/video viewer application for TDE.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}

# Removes unwanted files
%__rm -f %{?buildroot}%{tde_datadir}/mimelnk/application/x-mplayer2.desktop


%clean
%__rm -rf %{buildroot}


%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

%post base
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
/sbin/ldconfig || :

%postun base
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
/sbin/ldconfig || :


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO kmplayer.lsm
%{tde_bindir}/kmplayer
%{tde_bindir}/knpplayer
%{tde_bindir}/kxvplayer
%{tde_libdir}/libtdeinit_kmplayer.la
%{tde_libdir}/libtdeinit_kmplayer.so
%{tde_tdelibdir}/kmplayer.la
%{tde_tdelibdir}/kmplayer.so
%{tde_tdeappdir}/kmplayer.desktop
%{tde_datadir}/apps/kmplayer
%{tde_datadir}/services/kmplayer_part.desktop

%files base
%defattr(-,root,root,-)
%{tde_libdir}/libkmplayercommon.la
%{tde_libdir}/libkmplayercommon.so
%{tde_bindir}/kgstplayer
%{tde_bindir}/kxineplayer
%{tde_datadir}/config/kmplayerrc
%{tde_datadir}/apps/kmplayer/bookmarks.xml
%{tde_datadir}/apps/kmplayer/noise.gif
%{tde_datadir}/apps/kmplayer/pluginsinfo
%{tde_datadir}/icons/hicolor/*/apps/kmplayer.png
%{tde_datadir}/icons/hicolor/*/apps/kmplayer.svgz
%{tde_datadir}/mimelnk/application/x-kmplayer.desktop
%{tde_datadir}/mimelnk/video/x-ms-wmp.desktop


%files doc
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/*/kmplayer

%files konq-plugins
%defattr(-,root,root,-)
%{tde_tdelibdir}/libkmplayerpart.la
%{tde_tdelibdir}/libkmplayerpart.so
%{tde_datadir}/apps/kmplayer/kmplayerpartui.rc
%{tde_datadir}/apps/kmplayer/pluginsinfo
%{tde_datadir}/services/kmplayer_part.desktop


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.10.0c-6
- Initial release for TDE 14.0.0

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.10.0c-5
- Initial release for TDE 3.5.13.2

* Sat Nov 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.10.0c-4
- Fix xine 1.2 support (openSUSE 12.2 only)

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.10.0c-3
- Initial release for TDE 3.5.13.1

* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 0.10.0c-2
- Fix compilation with GCC 4.7 [Commit #5106117b]

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.10.0c-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16

