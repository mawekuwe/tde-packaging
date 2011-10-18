%define name    kde3-kaffeine
%define oname   kaffeine
%define version 3.5.12
%define pre rc2
%define release %mkrel 1
%define xineversion 1.1.11.1
%define fversion %version
%define _kde3_liconsdir %_kde3_iconsdir/large
%define _kde3_miconsdir %_kde3_iconsdir/mini
%define reallibname %mklibname %{oname} %{major}

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A Xine-based Media Player for KDE3
License:        GPL
URL:            http://kaffeine.sourceforge.net/
Group:          Graphical desktop/KDE3
Source:         http://prdownloads.sourceforge.net/kaffeine/%oname-%fversion.tar.bz2
#Patch0:         kaffeine_configure.patch
#Patch1:         kaffeine_dvb.diff
#Patch2:         kaffeine-link.diff
#Patch3:         kaffeine-0.8.8-fix_autotools.patch
Patch4:         kdebase-3.5.12-move-xdg-menu-dir.patch
Patch5:         kdebase-3.5.12-config.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  kde3-macros
BuildRequires:  kdelibs-devel
BuildRequires:  libxine-devel >= %xineversion
BuildRequires:  libgstreamer-plugins-base-devel >= 0.10
BuildRequires:  libcdda-devel
BuildRequires:  %{_lib}xorg-x11-devel
BuildRequires:  libcdio-devel
%if %mdkversion < 201000
BuildRequires:  autoconf <= 2.63
%else
BuildRequires:  autoconf >= 2.65
%endif
BuildRequires:  automake >= 1.6
Requires:       xine-plugins >= %xineversion
Requires:       kdelibs => 3.5.10
Obsoletes:      reallibname < 0.8.8
Obsoletes:      kaffeine < 0.8.8
Provides:       kaffeine = %version-%release

%description
Kaffeine is a Xine-based Media Player for QT/KDE3.


%package devel
Group:          Development/KDE and Qt
Summary:        Kaffeine kpart library headers
Requires:       %name = %version-%release
Provides:       kaffeine-devel = %version-%release
Obsoletes:      libkaffeine0-devel

%description devel
Kaffeine is a Xine-based Media Player for QT/KDE3. This is a kpart
library of Kaffeine.

%prep
%setup -q -n %oname-%fversion
#%patch0
#%patch1
#%patch2
#%if %mdkversion >= 201000
#%patch3 -p1
#%endif
%patch4 -p0
%patch5 -p0

%build
make -f admin/Makefile.common cvs
export UNSERMAKE=NO
export QTDIR=%qt3dir
export QTLIB=%qt3lib
export CFLAGS=${RPM_OPT_FLAGS}
export CXXFLAGS=${RPM_OPT_FLAGSi}

PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/
export xdg_menudir=%_sysconfdir/xdg/kde/menus

make -f admin/Makefile.common cvs

%configure_kde3 --disable-final --without-lame

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# (nl) this have been commited upstream, so remove desktop-file-install for next version
desktop-file-install --vendor='' \
        --dir=%buildroot%_kde3_datadir/applications/kde \
        --remove-key='Encoding' \
        --remove-category='Application' \
        %buildroot%_kde3_datadir/applications/kde/*.desktop


#mdk icons
install -D -m 644 %{buildroot}%_kde3_iconsdir/hicolor/48x48/apps/%{oname}.png %{buildroot}%_kde3_liconsdir/%{oname}.png
install -D -m 644 %{buildroot}%_kde3_iconsdir/hicolor/32x32/apps/%{oname}.png %{buildroot}%_kde3_iconsdir/%{oname}.png
install -D -m 644 %{buildroot}%_kde3_iconsdir/hicolor/16x16/apps/%{oname}.png %{buildroot}%_kde3_miconsdir/%{oname}.png


rm -f %buildroot%_kde3_datadir/mimelnk/application/x-mplayer2.desktop

#rename language files as kaffeine.mo
#otherwise we can't use translations on Mandy.(# Atilla ÖNTAŞ)
for i in $(find %buildroot%_kde3_datadir/locale -name "*-0.8.8.mo"); do j=$(echo $i | sed 's/-0.8.8.mo/.mo/g'); mv "$i" "$j"; done

%clean
rm -rf %{buildroot}


%files

%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL README TODO
%_kde3_bindir/kaffeine
%doc %_kde3_datadir/doc/HTML/en/kaffeine/
%_kde3_datadir/applications/kde/kaffeine.desktop
%_kde3_datadir/mimelnk/*/*
%_kde3_appsdir/konqueror/servicemenus/*
%_kde3_datadir/apps/gstreamerpart/gstreamer_part.rc
%_kde3_libdir/kde3/*
%_kde3_datadir/apps/kaffeine/*
%_kde3_appsdir/profiles/kaffeine.profile.xml
%_kde3_datadir/services/*
%_kde3_iconsdir/hicolor/*/*/*.png
%_kde3_liconsdir/%{oname}.png
%_kde3_miconsdir/%{oname}.png
%_kde3_iconsdir/%{oname}.png
%_kde3_datadir/servicetypes/kaffeineaudioencoder.desktop
%_kde3_datadir/servicetypes/kaffeinedvbplugin.desktop
%_kde3_datadir/servicetypes/kaffeineepgplugin.desktop
%_kde3_libdir/libkaffeinepart.so
%_kde3_datadir/locale/*



#--------------------------------------------------------------
%files devel
%defattr(-,root,root)
%_kde3_includedir/%oname/
%_kde3_libdir/libkaffeineaudioencoder.la
%_kde3_libdir/libkaffeineaudioencoder.so
%_kde3_libdir/libkaffeinedvbplugin.la
%_kde3_libdir/libkaffeinedvbplugin.so
%_kde3_libdir/libkaffeinepart.la
%_kde3_libdir/libkaffeineepgplugin.la
%_kde3_libdir/libkaffeineepgplugin.so

#--------------------------------------------------------------------

%package engine-gstreamer
Group:  Graphical desktop/KDE3
Summary: GStreamer engine for kaffeine
Requires: %{name}
Requires: gstreamer0.10-plugins-base >= 0.10
Requires: gstreamer0.10-plugins-good
Provides: kaffeine-engine-gstreamer
Obsoletes:kaffeine-engine-gstreamer < 0.8.8

%description engine-gstreamer
Summary: gstreamer engine for kaffeine

%files engine-gstreamer
%defattr(-,root,root)
%_kde3_libdir/kde3/libgstreamer*
%_kde3_appsdir/gstreamerpart
%_kde3_datadir/services/gstreamer*

#--------------------------------------------------------------------

%define major 0
%define libname %mklibname %{name} %{major}
%define reallibname %mklibname %{oname} %{major}

%package -n %libname
Group:          System/Libraries
Summary:        Kaffeine kpart library
Obsoletes:      %{reallibname} < 0.8.8
Provides:       %{reallibname}

%description -n %libname
Kaffeine is a Xine-based Media Player for QT/KDE3. This is a kpart
library of Kaffeine.


%files -n %libname
%defattr(-,root,root)
%_kde3_libdir/lib*.so.*


#--------------------------------------------------------------------

%package engine-xine
Group:  Graphical desktop/KDE3
Requires: xine-plugins
Summary: Xine engine for kaffeine
BuildRequires: gstreamer0.10-devel
BuildRequires: libgstreamer0.10-plugins-base-devel
BuildRequires: libxine-devel
Requires: %{name}
Provides: kaffeine-engine-xine
Obsoletes:kaffeine-engine-xine < 0.8.8

%description engine-xine
Summary: Xine engine for kaffeine

%files engine-xine
%defattr(-,root,root)
%_kde3_libdir/kde3/libxine*
%_kde3_appsdir/kaffeine/xine*
%_kde3_datadir/services/xine*

#--------------------------------------------------------------------
%changelog

* Mon Jul 25 2011 Tim Williams <tim@my-place.org.uk> 3.5.12-1mvf2011.2
+ Update to Trinity 3.5.12 sources
- Remove kaffeine-0.8.8-fix_autotools.patch, kaffeine_configure.patch, kaffeine-link.diff
+ Add kdebase-3.5.12-move-xdg-menu-dir.patch, kdebase-3.5.12-config.patch

* Sat Apr 08 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.8.8-3mvt2010.1
- fix buildrequires
- rebuild for 2010.1

* Tue Feb 09 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.8.8-2mvt2010.0
- Fix built with autoconf 2.65 and automake 1.11
- Change package group

* Sat Nov 21 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.8.8-1mvt2010.0
- Build KDE3 package for Mandriva
