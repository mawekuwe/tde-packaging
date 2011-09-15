# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 0

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-kdebase
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}
License:	GPL
Summary:	Trinity KDE Base Programs

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}

Source0:	kdebase-%{version}.tar.gz

# TDE for RHEL/Fedora specific patches
# [kdebase/kdesu] Remove 'ignore' button on 'kdesu' dialog box
Patch3:		kdebase-3.5.13-kdesu-noignorebutton.patch
# [kdebase/kdesktop] Modifies "open terminal here" on desktop
Patch5:		kdebase-3.5.12-desktop-openterminalhere.patch
# [kdebase/kioslave]: Forces HAL backend to use HAL mount options
Patch6:		kdebase-3.5.12-halmountoptions.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	qt3-devel >= 3.3.8d
BuildRequires:	openssl-devel
BuildRequires:	avahi-devel avahi-qt3-devel
BuildRequires:	imake
BuildRequires:	xorg-x11-proto-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	dbus-devel dbus-qt-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	libfontenc-devel
BuildRequires:	hal-devel
BuildRequires:	audiofile-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libraw1394-devel
BuildRequires:	openldap-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pam-devel
BuildRequires:	libXdmcp-devel
BuildRequires:	libxkbfile-devel
BuildRequires:	dbus-tqt-devel

Requires:	tqtinterface
Requires:	trinity-arts
Requires:	trinity-kdelibs
Requires:	qt3 >= 3.3.8d
Requires:	openssl
Requires:	avahi avahi-qt3
Requires:	dbus-tqt


# RHEL 6 Configuration files are provided in separate packages
%if "%{?_prefix}" == "/usr"
Requires:	kde-settings-kdm
%endif
Requires:	redhat-menus

%description
Core applications for the Trinity K Desktop Environment.  Included are: kdm
(replacement for xdm), kwin (window manager), konqueror (filemanager,
web browser, ftp client, ...), konsole (xterm replacement), kpanel
(application starter and desktop pager), kaudio (audio server),
kdehelp (viewer for kde help files, info and man pages), kthememgr
(system for managing alternate theme packages) plus other KDE
components (kcheckpass, kikbd, kscreensaver, kcontrol, kfind,
kfontmanager, kmenuedit).


%package devel
Requires:	%{name}
Requires:	%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kdelibs-devel
Summary:	%{summary} - Development files
%if "%{?_prefix}" == "/usr"
Obsoletes:	kdebase3-devel
%endif
Group:		Development/Libraries
%description devel
Header files for developing applications using %{name}.
Install kdebase-devel if you want to develop or compile Konqueror,
Kate plugins or KWin styles.


%package extras
Summary: Extra applications from %{name}
Group: User Interface/Desktops
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description extras
%{summary}, including:
 * kappfinder
 * kpager
 * ktip
 * kpersonalizer


%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-kdelibs >= %{version}
%if "%{?_prefix}" == "/usr"
Obsoletes: kdebase3-libs
%endif
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description libs
%{summary}


%package pim-ioslaves
Summary: PIM KIOslaves from %{name}
Group: System Environment/Libraries
%description pim-ioslaves
Protocol handlers (KIOslaves) for personal information management, including:
 * kio_ldap
 * kio_nntp
 * kio_pop3
 * kio_smtp


%prep
%setup -q -n kdebase
%patch3 -p1
%patch5 -p1
%patch6 -p1

# Gets the cmake modules in current build directory
%__mkdir_p cmake/modules
%__cp -f %{_datadir}/cmake/*.* cmake/modules

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"
export LD_LIBRARY_PATH="%{_libdir}"

%__mkdir build
cd build
%cmake \
  -DWITH_SASL=ON \
  -DWITH_LDAP=ON \
  -DWITH_SAMBA=ON \
  -DWITH_OPENEXR=ON \
  -DWITH_XCOMPOSITE=ON \
  -DWITH_XCURSOR=ON \
  -DWITH_XFIXES=ON \
  -DWITH_XRANDR=ON \
  -DWITH_XRENDER=ON \
  -DWITH_XDAMAGE=ON \
  -DWITH_XEXT=ON \
  -DWITH_LIBUSB=ON \
  -DWITH_LIBRAW1394=ON \
  -DWITH_PAM=ON \
  -DWITH_SHADOW=OFF \
  -DWITH_XDMCP=ON \
  -DWITH_XINERAMA=ON \
  -DWITH_ARTS=ON \
  -DWITH_I8K=OFF \
  -DWITH_HAL=ON \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags} 

%install
%__rm -rf %{?buildroot}
%__mkdir_p %{?buildroot}
%make_install -C build

# Adds a GDM/KDM/XDM session called 'TDE'
%if "%{?_prefix}" != "/usr"
%__mkdir_p "%{?buildroot}%{_usr}/share/xsessions"
install -m 644 "%{?buildroot}%{_datadir}/apps/kdm/sessions/tde.desktop" "%{?buildroot}%{_usr}/share/xsessions/tde.desktop"
%endif

# Modifies 'startkde' to set KDEDIR and KDEHOME hardcoded specific for TDE
sed -i "%{?buildroot}%{_bindir}/startkde" \
  -e '/^echo "\[startkde\] Starting startkde.".*/ s,$,\nexport KDEDIR=%{_prefix}\nexport KDEHOME=~/.trinity,'

# Renames '/etc/ksysguarddrc' to avoid conflict with KDE4 'ksysguard'
mv -f %{?buildroot}%{_sysconfdir}/ksysguarddrc %{?buildroot}%{_sysconfdir}/ksysguarddrc.tde

%clean
%__rm -rf %{?buildroot}


%post
touch --no-create %{_datadir}/icons/crystalsvg 2> /dev/null || :
gtk-update-icon-cache --quiet %{_datadir}/icons/crystalsvg  2> /dev/null || :
update-desktop-database 2> /dev/null || : 
# Dirty hack to install '/etc/ksysguardrc' alongside with KDE4
[ -r %{_sysconfdir}/ksysguarddrc ] || cp -f %{_sysconfdir}/ksysguarddrc.tde %{_sysconfdir}/ksysguarddrc

%postun
touch --no-create %{_datadir}/icons/crystalsvg 2> /dev/null || :
gtk-update-icon-cache --quiet %{_datadir}/icons/crystalsvg  2> /dev/null || :
update-desktop-database 2> /dev/null || : 


%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post extras
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun extras
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :


%files extras
%defattr(-,root,root,-)
# kappfinder
%{_bindir}/kappfinder
%{_datadir}/applications/kde/kappfinder.desktop
%{_datadir}/applnk/System/kappfinder.desktop
%{_datadir}/apps/kappfinder/
%{_datadir}/icons/hicolor/*/apps/kappfinder.png
# ktip
%{_bindir}/ktip
%{_datadir}/applications/kde/ktip.desktop
%{_datadir}/applnk/Toys/ktip.desktop
%{_datadir}/apps/kdewizard
%{_datadir}/autostart/ktip.desktop
%{_datadir}/icons/hicolor/*/apps/ktip*
# kpersonalizer
%{_bindir}/kpersonalizer
%{_datadir}/applications/kde/kpersonalizer.desktop
%{_datadir}/applnk/System/kpersonalizer.desktop
%{_datadir}/apps/kpersonalizer/
%{_datadir}/icons/crystalsvg/*/apps/kpersonalizer.png
# kpager
%{_bindir}/kpager
%{_datadir}/applications/kde/kpager.desktop
%{_datadir}/applnk/Utilities/kpager.desktop
%{_datadir}/icons/hicolor/*/apps/kpager.png


%files
%defattr(-,root,root,-)
# kappfinder
%exclude %{_datadir}/applications/kde/kappfinder.desktop
%exclude %{_datadir}/applnk/System/kappfinder.desktop
%exclude %{_datadir}/apps/kappfinder/
%exclude %{_datadir}/icons/hicolor/*/apps/kappfinder.png
# ktip
%exclude %{_datadir}/applications/kde/ktip.desktop
%exclude %{_datadir}/applnk/Toys/ktip.desktop
%exclude %{_datadir}/apps/kdewizard
%exclude %{_datadir}/autostart/ktip.desktop
%exclude %{_datadir}/icons/hicolor/*/apps/ktip*
# kpersonalizer
%exclude %{_datadir}/applications/kde/kpersonalizer.desktop
%exclude %{_datadir}/applnk/System/kpersonalizer.desktop
%exclude %{_datadir}/apps/kpersonalizer/
%exclude %{_datadir}/icons/crystalsvg/*/apps/kpersonalizer.png
# kpager
%exclude %{_datadir}/applications/kde/kpager.desktop
%exclude %{_datadir}/applnk/Utilities/kpager.desktop
%exclude %{_datadir}/icons/hicolor/*/apps/kpager.png

%doc AUTHORS COPYING README
%{tde_docdir}/HTML/en/*
%config(noreplace) %{_sysconfdir}/ksysguarddrc.tde
%{_bindir}/genkdmconf
%{_bindir}/kaccess
%{_bindir}/kapplymousetheme
%{_bindir}/kate
%{_bindir}/kblankscrn.kss
%{_bindir}/kbookmarkmerger
%{_bindir}/kcminit
%{_bindir}/kcminit_startup
%{_bindir}/kcontrol
%{_bindir}/kcontroledit
%{_bindir}/kdebugdialog
%{_bindir}/kdeinstallktheme
%{_bindir}/kdepasswd
%{_bindir}/kdesu
%attr(0755,root,root) %{_bindir}/kdesud
%{_bindir}/kdialog
%{_bindir}/kdm
%{_bindir}/kdmctl
%{_bindir}/keditbookmarks
%{_bindir}/keditfiletype
%{_bindir}/kfind
%{_bindir}/kfmclient
%{_bindir}/khelpcenter
%{_bindir}/khotkeys
%{_bindir}/kinfocenter
%{_bindir}/klipper
%{_bindir}/kmenuedit
%{_bindir}/konqueror
%{_bindir}/konsole
%{_bindir}/krandom.kss
%{_bindir}/krandrtray
%{_bindir}/krdb
%{_bindir}/kreadconfig
%{_bindir}/ksmserver
%{_bindir}/ksplashsimple
%{_bindir}/kstart
%{_bindir}/ksysguard
%{_bindir}/ksysguardd
%{_bindir}/ksystraycmd
%{_bindir}/ktrash
%{_bindir}/kwin
%{_bindir}/kwin_killer_helper
%{_bindir}/kwin_rules_dialog
%{_bindir}/kwrite
%{_bindir}/kwriteconfig
%{_bindir}/kxkb
%{_bindir}/nspluginscan
%{_bindir}/nspluginviewer
%{_bindir}/startkde
%{_bindir}/kcheckrunning
%{_bindir}/kdesktop
%{_bindir}/kdesktop_lock
%{_bindir}/kdm_config
%{_bindir}/kdm_greet
%{_bindir}/kfontinst
%{_bindir}/kfontview
%{_bindir}/krootimage
%{_bindir}/kwebdesktop
%{_datadir}/autostart/*
%{_datadir}/desktop-directories/*
%{_datadir}/locale/*/entry.desktop
%{_datadir}/locale/l10n
%{_datadir}/templates/*
%{_datadir}/templates/.source/*
%{_datadir}/wallpapers/*
%{_bindir}/appletproxy
%{_bindir}/drkonqi
%{_bindir}/extensionproxy
%{_bindir}/kasbar
%attr(4755,root,root) %{_bindir}/kcheckpass
%{_bindir}/kdeeject
%{_bindir}/khc_docbookdig.pl
%{_bindir}/khc_htdig.pl
%{_bindir}/khc_htsearch.pl
%{_bindir}/khc_indexbuilder
%{_bindir}/khc_mansearch.pl
%{_bindir}/kicker
%{_bindir}/knetattach
%{_bindir}/kompmgr
%{_bindir}/kpm
%{_bindir}/ksplash
%{_libdir}/kconf_update_bin
%{_datadir}/applnk/*.desktop
%{_datadir}/applnk/*/*
%{_datadir}/applnk/.hidden/*
%exclude %{_datadir}/applnk/.hidden/.directory
%{_datadir}/config.kcfg/*
%{_bindir}/kio_media_mounthelper
%{_bindir}/kdcop
%{_bindir}/kdeprintfax
%{_bindir}/khc_beagle_index.pl
%{_bindir}/khc_beagle_search.pl
%{_bindir}/kxdglauncher
%{_bindir}/kjobviewer
%{_bindir}/klocaldomainurifilterhelper
%{_bindir}/kprinter
%{_datadir}/applications/*/*
%{_datadir}/apps/*
%{_datadir}/icons/*color/*/*/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/mimelnk/*/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/sounds/*
%{tde_libdir}/*
%{_libdir}/libkdeinit_*.*
%{_sysconfdir}/xdg/menus/applications-merged/kde-essential.menu
%{_sysconfdir}/xdg/menus/kde-information.menu
%{_sysconfdir}/xdg/menus/kde-screensavers.menu
%{_sysconfdir}/xdg/menus/kde-settings.menu
/usr/share/xsessions/*.desktop
# Remove conflicts with redhat-menus
%if "%{?_prefix}" != "/usr"
%config(noreplace) %{_datadir}/config/*
%else
%exclude %{_datadir}/config
%endif
# exclude pim-ioslaves files from main package
%exclude %{tde_libdir}/kio_ldap.*
%exclude %{tde_libdir}/kio_nntp.*
%exclude %{tde_libdir}/kio_pop3.*
%exclude %{tde_libdir}/kio_smtp.*
%exclude %{_datadir}/services/ldap*.protocol
%exclude %{_datadir}/services/nntp*.protocol
%exclude %{_datadir}/services/pop3*.protocol
%exclude %{_datadir}/services/smtp*.protocol

# New in TDE 3.5.13
%{_bindir}/krootbacking

%files libs
%defattr(-,root,root,-)
%exclude %{_libdir}/libkdeinit_*.*
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la

%files pim-ioslaves
%defattr(-,root,root,-)
%{tde_libdir}/kio_ldap.*
%{tde_libdir}/kio_nntp.*
%{tde_libdir}/kio_pop3.*
%{tde_libdir}/kio_smtp.*
%{_datadir}/services/ldap*.protocol
%{_datadir}/services/nntp*.protocol
%{_datadir}/services/pop3*.protocol
%{_datadir}/services/smtp*.protocol

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%dir %{_includedir}/kate
%{_includedir}/kate/*
%dir %{_includedir}/kwin
%{_includedir}/kwin/*
%dir %{_includedir}/ksgrd
%{_includedir}/ksgrd/*
%dir %{_includedir}/ksplash
%{_includedir}/ksplash/*
%{_libdir}/lib*.so
%exclude %{_libdir}/libkdeinit_*.*
# New in TDE 3.5.13
%{_datadir}/cmake/*.cmake

%changelog
* Sat Sep 03 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12.99-0
- Import to GIT
- Use TDE 3.5.13, cmake, QT3.3.3.8d
