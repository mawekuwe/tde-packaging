# If Trinity is built in a specific prefix, we move all directories under it
%if "%{_prefix}" != "/usr"
%define _variant .opt
%endif

# Basic package informations
%define kdecomp amarok
%define version 1.4.10
%define release 1

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



# TODO:
# Rio Karma support : libkarma

%if 0%{?fedora} > 0 && 0%{?fedora} < 9
# define to include konquisidebar support for kde3 desktop
%define konq 1
%endif

# No Xine support on older RHEL
%if 0%{?rhel} && 0%{?rhel} <= 5
%define _with_xine %{nil}
%else
%define _with_xine 1
%endif

Name:    trinity-%{kdecomp}
Summary: A drop-down terminal emulator.
Version: %{version}
Release: %{release}%{?dist}%{?_variant}

Group: 	    Applications/Multimedia
License:    GPLv2+
Url:        http://amarok.kde.org
Source0:    amarok-3.5.13.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# RedHat / Fedora legacy patches
Patch1:     amarok-1.4.8-gcc43.patch

BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  esound-devel
BuildRequires:  gettext
BuildRequires:  trinity-kdelibs-devel
%if 0%{?konq}
BuildRequires:  trinity-kdebase-devel
%else
Obsoletes: %{name}-konqueror < %{version}-%{release}
%endif
BuildRequires:  taglib-devel 
BuildRequires:  libifp-devel
# Ipod
BuildRequires:  libgpod-devel
BuildRequires: libmp4v2-devel
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
BuildRequires:  xine-lib-devel
BuildRequires:	sqlite-devel
# not used anymore, in favor of libvisual ? -- Rex
#%{?fedora:BuildRequires:  xmms-devel}
BuildRequires:	dbus-devel
BuildRequires:	dbus-tqt-devel

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
%if 0%{?_with_xine}
# xine-lib
Provides: %{name}-engine-xine = %{version}-%{release}
%endif


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
Requires:   libvisual-plugins
%description visualisation
Amarok can use visualisation plugins from different origins.
Right now, only xmms is supported, which means that you can
use any of xmms' visualisation plugins with Amarok.


%prep
%setup -q -n applications/amarok
%patch1 -p1 -b .gcc43


%build
unset QTDIR && . %{_sysconfdir}/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"

%__mkdir_p build
cd build
%cmake \
	-DWITH_LIBVISUAL=ON \
	-DWITH_KONQSIDEBAR=OFF \
	-DWITH_XINE=ON \
	-DWITH_YAUAP=ON \
	-DWITH_IPOD=ON \
	-DWITH_IFP=ON \
	-DWITH_NJB=ON \
	-DWITH_MTP=ON \
	-DWITH_RIOKARMA=OFF \
	-DWITH_DAAP=ON \
	-DBUILD_ALL=ON \
	..

%__make %{?_smp_mflags}

%install
rm -fr $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT -C build

# desktop files
desktop-file-install  --vendor "" \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications/kde \
        --delete-original \
        $RPM_BUILD_ROOT%{_datadir}/applications/kde/amarok.desktop

# unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la
%if ! 0%{?konq}
rm -f $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus/*.desktop
%endif


# HTML
for lang_dir in $RPM_BUILD_ROOT%{_docdir}/HTML/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    [ "$lang" == "en" ] && d=en/%{name} || d=$lang
    echo "%lang($lang) %doc %{_docdir}/HTML/$d" >> %{name}.lang
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
rm -fr $RPM_BUILD_ROOT


%files
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
#%{_datadir}/services/amarok_riokarma-mediadevice.desktop
#%{tde_libdir}/libamarok_riokarma-mediadevice.*
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


%{tde_docdir}/HTML/*/amarok
%{_datadir}/locale/*/LC_MESSAGES/amarok.mo

%if 0%{?konq}
%files konqueror
%defattr(-,root,root,-)
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{tde_libdir}/konqsidebar_universalamarok.*
%{_datadir}/apps/konqsidebartng/*/amarok.desktop
%endif

%files visualisation
%defattr(-,root,root,-)
%{_bindir}/amarok_libvisual


%changelog
* Wed Nov 09 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.10-1
- Initial build for TDE 3.5.13 on RHEL 5, RHEL 6, Fedora 15, Fedora 16
- Spec file based on Fedora 8 'amarok-1.4.10-1'
