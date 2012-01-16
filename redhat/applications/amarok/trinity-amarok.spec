# Basic package informations
%define kdecomp amarok
%define version 1.4.10
%define release 4

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires:	cmake >= 2.8
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:    trinity-%{kdecomp}
Summary: Media player
Version: %{version}
Release: %{release}%{?dist}%{?_variant}

Group: 	    Applications/Multimedia
License:    GPLv2+
Url:        http://amarok.kde.org

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:    amarok-3.5.13.tar.gz

# RedHat / Fedora legacy patches
Patch1:     amarok-1.4.8-gcc43.patch

# TDE 3.5.13 RHEL/Fedora patches
Patch2:		amarok-3.5.13-cmake_konqsidebar.patch
Patch3:		amarok-3.5.13-taglib_include.patch
Patch4:		amarok-3.5.13-enable_riokarma.patch
Patch5:		amarok-3.5.13-enable_akode.patch

BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  esound-devel
BuildRequires:  gettext
BuildRequires:  trinity-kdelibs-devel
BuildRequires:  trinity-kdebase-devel
BuildRequires:  taglib-devel 
BuildRequires:  libifp-devel
# Ipod
BuildRequires:  libgpod-devel >= 0.4.2
BuildRequires:	libmp4v2-devel
# MTP players
BuildRequires:  libmtp-devel
BuildRequires:  libmusicbrainz-devel
# Creative Nomad Jukebox
BuildRequires:  libnjb-devel
BuildRequires:  libtool
%if 0%{?fedora} > 4 || 0%{?rhel} > 4
BuildRequires:  libtool-ltdl-devel
%endif
BuildRequires:  libtunepimp-devel
BuildRequires:  libusb-devel
BuildRequires:  libvisual-devel
BuildRequires:  mysql-devel
BuildRequires:  postgresql-devel
BuildRequires:  ruby-devel ruby
BuildRequires:  SDL-devel
BuildRequires:  taglib-devel
BuildRequires:	sqlite-devel
BuildRequires:	libkarma-devel karma-sharp
# not used anymore, in favor of libvisual ? -- Rex
#%{?fedora:BuildRequires:  xmms-devel}
BuildRequires:	dbus-devel
BuildRequires:	dbus-tqt-devel
BuildRequires:	akode-devel

# For dir ownership and some default plugins (lyrics), -ruby subpkg?  -- Rex
Requires:  ruby

# To open the selected browser, works with Patch2
Requires:  xdg-utils
Requires(post): xdg-utils
Requires(postun): xdg-utils

Obsoletes: amarok-arts < 1.3, amarok-akode < 1.3

Obsoletes: amarok-devel < %{version}-%{release}
%if 0%{?fedora} > 6 && 0%{?fedora} < 9
# need to keep this around for previous releases, so not to break multilib compat.
Provides:  amarok-devel = %{version}-%{release}
%endif

# engines, etc...
# old, obsolete ones: arts, akode
Obsoletes: amarok-arts < 1.3, amarok-akode < 1.3
# xine-lib
BuildRequires:  xine-lib-devel
Provides: %{name}-engine-xine = %{version}-%{release}


%description
Amarok is a multimedia player with:
 - fresh playlist concept, very fast to use, with drag and drop
 - plays all formats supported by the various engines
 - audio effects, like reverb and compressor
 - compatible with the .m3u and .pls formats for playlists
 - nice GUI, integrates into the KDE look, but with a unique touch


%package konqueror
Summary: Amarok konqueror (service menus, sidebar) support
Group:   Applications/Multimedia
Requires: %{name} = %{version}-%{release}
%description konqueror
%{summary}.

%package visualisation
Summary:    Visualisation plugins for Amarok
Group:      Applications/Multimedia
Requires:   %{name} = %{version}-%{release}
# No plugins by default, we need libvisual-plugins
#Requires:   libvisual-plugins
%description visualisation
Amarok can use visualisation plugins from different origins.
Right now, only xmms is supported, which means that you can
use any of xmms' visualisation plugins with Amarok.


%prep
%setup -q -n applications/amarok
%patch1 -p1 -b .gcc43
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1


%build
unset QTDIR && . %{_sysconfdir}/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"

%__mkdir_p build
cd build
%cmake \
	-DWITH_LIBVISUAL=ON \
	-DWITH_KONQSIDEBAR=ON \
	-DWITH_XINE=ON \
	-DWITH_YAUAP=ON \
	-DWITH_AKODE=ON \
	-DWITH_IPOD=ON \
	-DWITH_IFP=ON \
	-DWITH_NJB=ON \
	-DWITH_MTP=ON \
	-DWITH_RIOKARMA=ON \
	-DWITH_DAAP=ON \
	-DBUILD_ALL=ON \
	-DQT_LIBRARY_DIRS=${QTLIB} \
	..

%__make %{?_smp_mflags}

%install
%__rm -fr $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT -C build

# desktop files
desktop-file-install  --vendor "" \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications/kde \
        --delete-original \
        $RPM_BUILD_ROOT%{_datadir}/applications/kde/amarok.desktop

# unpackaged files
%__rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la


# HTML
for lang_dir in $RPM_BUILD_ROOT%{tde_docdir}/HTML/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    [ "$lang" == "en" ] && d=en/amarok || d=$lang
    echo "%lang($lang) %doc %{tde_docdir}/HTML/$d" >> %{name}.lang
  fi
done

# Locales
for locale in $RPM_BUILD_ROOT%{_datadir}/locale/* ; do
  if [ -r $locale/LC_MESSAGES/amarok.mo ]; then
    lang=$(basename $locale)
    echo "%lang($lang) %{_datadir}/locale/$lang/LC_MESSAGES/amarok.mo" >> %{name}.lang
  fi
done


%post
/sbin/ldconfig
xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :
xdg-desktop-menu forceupdate 2> /dev/null || :

%postun
/sbin/ldconfig
xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :
xdg-desktop-menu forceupdate 2> /dev/null || :


%clean
%__rm -fr $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS ChangeLog README
%{_bindir}/amarok
%{_bindir}/amarokapp
%{_bindir}/amarokcollectionscanner
%{_bindir}/amarok_proxy.rb
%{_datadir}/apps/amarok/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/servicetypes/*.desktop
%{_datadir}/apps/profiles/amarok.profile.xml
%{_datadir}/config/amarokrc
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/services/amarokitpc.protocol
%{_datadir}/services/amaroklastfm.protocol
%{_datadir}/services/amarokpcast.protocol
# -libs ?  -- Rex
%{_libdir}/libamarok.*
# -ruby ? -- Rex
%{_libdir}/ruby_lib/*
# DAAP
%{_bindir}/amarok_daapserver.rb
%{tde_libdir}/libamarok_daap-mediadevice.*
%{_datadir}/services/amarok_daap-mediadevice.desktop
# Mass-storage
%{_datadir}/services/amarok_massstorage-device.desktop
%{tde_libdir}/libamarok_massstorage-device.*
# NFS
%{_datadir}/services/amarok_nfs-device.desktop
%{tde_libdir}/libamarok_nfs-device.*
# SMB
%{_datadir}/services/amarok_smb-device.desktop
%{tde_libdir}/libamarok_smb-device.*
# IPod
%{_datadir}/services/amarok_ipod-mediadevice.desktop
%{tde_libdir}/libamarok_ipod-mediadevice.*
# VFAT
%{_datadir}/services/amarok_generic-mediadevice.desktop
%{tde_libdir}/libamarok_generic-mediadevice.*
# iRiver
%{_datadir}/services/amarok_ifp-mediadevice.desktop
%{tde_libdir}/libamarok_ifp-mediadevice.*
# Creative Zen
%{_datadir}/services/amarok_njb-mediadevice.desktop
%{tde_libdir}/libamarok_njb-mediadevice.*
# MTP players
%{_datadir}/services/amarok_mtp-mediadevice.desktop
%{tde_libdir}/libamarok_mtp-mediadevice.*
# Rio Karma
%{_datadir}/services/amarok_riokarma-mediadevice.desktop
%{tde_libdir}/libamarok_riokarma-mediadevice.*
# Void engine (noop)
%{_datadir}/services/amarok_void-engine_plugin.desktop
%{tde_libdir}/libamarok_void-engine_plugin.*
# Xine engine
%{_datadir}/services/amarok_xine-engine.desktop
%{tde_libdir}/libamarok_xine-engine.*
## Gstreamer engine
#%{_datadir}/services/amarok_gst10engine_plugin.desktop
#%{tde_libdir}/libamarok_gst10engine_plugin.*
# YAUAP
%{_datadir}/services/amarok_yauap-engine_plugin.desktop
%{tde_libdir}/libamarok_yauap-engine_plugin.*
# AKODE
%{_datadir}/services/amarok_aKode-engine.desktop
%{tde_libdir}/libamarok_akode-engine.*



%files konqueror
%defattr(-,root,root,-)
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{tde_libdir}/konqsidebar_universalamarok.*
%{_datadir}/apps/konqsidebartng/*/amarok.desktop

%files visualisation
%defattr(-,root,root,-)
%{_bindir}/amarok_libvisual


%changelog
* Mon Jan 16 2012 Francois Andriot <francois.andriot@free.fr> - 1.4.10-4
- Enable 'akode' support
- Removes 'libvisual-plugins' dependency (obsolete ?)

* Mon Nov 28 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.10-3
- Enable riokarma support
- Enhance localized files packaging

* Sat Nov 26 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.10-2
- Enable RHEL 5 compilation
- Add konqueror sidebar

* Wed Nov 09 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.10-1
- Initial build for TDE 3.5.13 on RHEL 5, RHEL 6, Fedora 15, Fedora 16
- Spec file based on Fedora 8 'amarok-1.4.10-1'
