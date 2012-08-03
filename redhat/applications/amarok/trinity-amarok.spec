# Basic package informations
%define kdecomp amarok

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-%{kdecomp}
Summary:	Media player
Version:	1.4.10
Release:	6%{?dist}%{?_variant}

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

Patch6:		amarok-3.5.13-adds_ruby_1.9_support.patch
Patch7:		amarok-3.5.13-fix_gcc47_compilation.patch

# [amarok] Fix inotify detection [Commit #899586da]
Patch11:	amarok-3.5.13-fix_inotify_support.patch

BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  esound-devel
BuildRequires:  gettext
BuildRequires:	tqtinterface-devel
BuildRequires:  trinity-kdelibs-devel
BuildRequires:  trinity-kdebase-devel
BuildRequires:	pcre-devel
BuildRequires:  taglib-devel 
BuildRequires:  libifp-devel
# Ipod
%if 0%{?rhel} == 5
BuildRequires:  trinity-libgpod-devel >= 0.4.2
%else
BuildRequires:  libgpod-devel >= 0.4.2
%endif
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
BuildRequires:  SDL-devel
BuildRequires:  taglib-devel
BuildRequires:	sqlite-devel
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	trinity-libkarma-devel
BuildRequires:	trinity-karma-sharp
%else
BuildRequires:	libkarma-devel
BuildRequires:	karma-sharp
%endif
# not used anymore, in favor of libvisual ? -- Rex
#%{?fedora:BuildRequires:  xmms-devel}
BuildRequires:	dbus-devel
BuildRequires:	dbus-tqt-devel
BuildRequires:	trinity-akode-devel
BuildRequires:	trinity-konqueror-devel

# ruby
BuildRequires:	ruby
BuildRequires:  ruby-devel

# To open the selected browser, works with Patch2
Requires:  xdg-utils
Requires(post): xdg-utils
Requires(postun): xdg-utils

# xine-lib
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:  libxine-devel
%else
BuildRequires:  xine-lib-devel
%endif


%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}inotifytools-devel
%else
%endif


%description
Amarok is a multimedia player with:
 - fresh playlist concept, very fast to use, with drag and drop
 - plays all formats supported by the various engines
 - audio effects, like reverb and compressor
 - compatible with the .m3u and .pls formats for playlists
 - nice GUI, integrates into the TDE look, but with a unique touch

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS ChangeLog README
%{tde_bindir}/amarok
%{tde_bindir}/amarokapp
%{tde_bindir}/amarokcollectionscanner
%{tde_bindir}/amarok_proxy.rb
%{tde_datadir}/apps/amarok/
%{tde_datadir}/icons/hicolor/*/*/*
%{tde_datadir}/applications/kde/*.desktop
%{tde_datadir}/servicetypes/*.desktop
%{tde_datadir}/apps/profiles/amarok.profile.xml
%{tde_datadir}/config/amarokrc
%{tde_datadir}/config.kcfg/*.kcfg
%{tde_datadir}/services/amarokitpc.protocol
%{tde_datadir}/services/amaroklastfm.protocol
%{tde_datadir}/services/amarokpcast.protocol
# -libs ?  -- Rex
%{tde_libdir}/libamarok.*
# DAAP
%{tde_bindir}/amarok_daapserver.rb
%{tde_tdelibdir}/libamarok_daap-mediadevice.*
%{tde_datadir}/services/amarok_daap-mediadevice.desktop
# Mass-storage
%{tde_datadir}/services/amarok_massstorage-device.desktop
%{tde_tdelibdir}/libamarok_massstorage-device.*
# NFS
%{tde_datadir}/services/amarok_nfs-device.desktop
%{tde_tdelibdir}/libamarok_nfs-device.*
# SMB
%{tde_datadir}/services/amarok_smb-device.desktop
%{tde_tdelibdir}/libamarok_smb-device.*
# IPod
%{tde_datadir}/services/amarok_ipod-mediadevice.desktop
%{tde_tdelibdir}/libamarok_ipod-mediadevice.*
# VFAT
%{tde_datadir}/services/amarok_generic-mediadevice.desktop
%{tde_tdelibdir}/libamarok_generic-mediadevice.*
# iRiver
%{tde_datadir}/services/amarok_ifp-mediadevice.desktop
%{tde_tdelibdir}/libamarok_ifp-mediadevice.*
# Creative Zen
%{tde_datadir}/services/amarok_njb-mediadevice.desktop
%{tde_tdelibdir}/libamarok_njb-mediadevice.*
# MTP players
%{tde_datadir}/services/amarok_mtp-mediadevice.desktop
%{tde_tdelibdir}/libamarok_mtp-mediadevice.*
# Rio Karma
%{tde_datadir}/services/amarok_riokarma-mediadevice.desktop
%{tde_tdelibdir}/libamarok_riokarma-mediadevice.*
# Void engine (noop)
%{tde_datadir}/services/amarok_void-engine_plugin.desktop
%{tde_tdelibdir}/libamarok_void-engine_plugin.*
# Xine engine
%{tde_datadir}/services/amarok_xine-engine.desktop
%{tde_tdelibdir}/libamarok_xine-engine.*
## Gstreamer engine
#%{tde_datadir}/services/amarok_gst10engine_plugin.desktop
#%{tde_tdelibdir}/libamarok_gst10engine_plugin.*
# YAUAP
%{tde_datadir}/services/amarok_yauap-engine_plugin.desktop
%{tde_tdelibdir}/libamarok_yauap-engine_plugin.*
# AKODE
%{tde_datadir}/services/amarok_aKode-engine.desktop
%{tde_tdelibdir}/libamarok_aKode-engine.*

%post
/sbin/ldconfig
xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :
xdg-desktop-menu forceupdate 2> /dev/null || :

%postun
/sbin/ldconfig
xdg-icon-resource forceupdate --theme hicolor 2> /dev/null || :
xdg-desktop-menu forceupdate 2> /dev/null || :


##########

%package ruby
Summary:	%{name} Ruby support
Group:		Applications/Multimedia
Requires: %{name} = %{version}-%{release}
# For dir ownership and some default plugins (lyrics)
Requires:  ruby

%description ruby
%{summary}.

%files ruby
%defattr(-,root,root,-)
%{tde_libdir}/ruby_lib/*

##########

%package konqueror
Summary:	Amarok konqueror (service menus, sidebar) support
Group:		Applications/Multimedia

Requires:	%{name} = %{version}-%{release}
Requires:	trinity-konqueror

%description konqueror
%{summary}.

%files konqueror
%defattr(-,root,root,-)
%{tde_datadir}/apps/konqueror/servicemenus/*.desktop
%{tde_tdelibdir}/konqsidebar_universalamarok.*
%{tde_datadir}/apps/konqsidebartng/*/amarok.desktop


##########

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

%files visualisation
%defattr(-,root,root,-)
%{tde_bindir}/amarok_libvisual

##########


%prep
%setup -q -n applications/amarok
%patch1 -p1 -b .gcc43
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1 -b .ruby
%patch7 -p1

%patch11 -p1 -b .inotify


%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export CMAKE_INCLUDE_PATH="%{tde_includedir}:%{tde_includedir}/tqt:%{tde_tdeincludedir}"

%if 0%{?rhel} || 0%{?fedora}
%__mkdir_p build
cd build
%endif

%cmake \
	-DBIN_INSTALL_DIR=%{tde_bindir} \
	-DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
	-DLIB_INSTALL_DIR=%{tde_libdir} \
	-DSHARE_INSTALL_PREFIX=%{tde_datadir} \
	-DCMAKE_SKIP_RPATH="OFF" \
	-DQT_LIBRARY_DIRS="${QTLIB}" \
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
	..

%__make %{?_smp_mflags}

%install
%__rm -fr $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT -C build


# unpackaged files
%__rm -f $RPM_BUILD_ROOT%{tde_libdir}/lib*.la


# HTML
for lang_dir in $RPM_BUILD_ROOT%{tde_tdedocdir}/HTML/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    [ "$lang" == "en" ] && d=en/amarok || d=$lang
    echo "%lang($lang) %doc %{tde_tdedocdir}/HTML/$d" >> %{name}.lang
  fi
done

# Locales
for locale in $RPM_BUILD_ROOT%{tde_datadir}/locale/* ; do
  if [ -r $locale/LC_MESSAGES/amarok.mo ]; then
    lang=$(basename $locale)
    echo "%lang($lang) %{tde_datadir}/locale/$lang/LC_MESSAGES/amarok.mo" >> %{name}.lang
  fi
done



%clean
%__rm -fr $RPM_BUILD_ROOT






%changelog
* Mon Apr 29 2012 Francois Andriot <francois.andriot@free.fr> - 1.4.10-6
- Rebuilt for Fedora 17
- Fix compilation with GCC 4.7
- Fix inotify detection [Commit #899586da]

* Mon Mar 19 2012 Francois Andriot <francois.andriot@free.fr> - 1.4.10-5
- Replaces BR "libgpod" with "trinity-libgpod" for EL5

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
