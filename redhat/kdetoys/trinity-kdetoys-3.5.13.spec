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

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Summary:		Trinity Desktop Environment - Toys and Amusements
Name:			trinity-tdetoys
Group:			Amusements/Graphics
Version:		3.5.13
Release:		3%{?dist}%{?_variant}

License: GPLv2+
Source0: kdetoys-%{version}.tar.gz

# [kdetoys] Missing LDFLAGS cause FTBFS on Mageia 2
Patch1:		kdetoys-3.5.13-missing_ldflags.patch

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: autoconf automake libtool m4
BuildRequires: desktop-file-utils
BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: gettext

Obsoletes:		trinity-kdetoys < %{version}-%{release}
Provides:		trinity-kdetoys = %{version}-%{release}

# Metapackage
Requires: trinity-amor = %{version}-%{release}
Requires: trinity-eyesapplet = %{version}-%{release}
Requires: trinity-fifteenapplet = %{version}-%{release}
Requires: trinity-kmoon = %{version}-%{release}
Requires: trinity-kodo = %{version}-%{release}
Requires: trinity-kteatime = %{version}-%{release}
Requires: trinity-ktux = %{version}-%{release}
Requires: trinity-kweather = %{version}-%{release}
Requires: trinity-kworldclock = %{version}-%{release}


%description
Includes: 
* amor: Amusing Misuse Of Resources put's comic figures above your windows
* eyesapplet: a kicker applet similar to XEyes
* fifteenapplet: kicker applet, order 15 pieces in a 4x4 square by moving them
* kmoon: system tray applet showing the moon phase
* kodo: mouse movement meter
* kteatime: system tray applet that makes sure your tea doesn't get too strong
* ktux: Tux-in-a-Spaceship screen saver
* kweather: kicker applet that will display the current weather outside
* kworldwatch: application and kicker applet showing daylight area on the world
               globe

NOTE: kicker applets and screen savers require kdebase to be installed, 
and user to be logged-in to TDE.

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README

##########

%package -n trinity-amor
Summary:	a Trinity creature for your desktop
Group:		Amusements/Graphics

%description -n trinity-amor
AMOR stands for Amusing Misuse Of Resources. It provides several different
characters who prance around your X screen doing tricks and giving you tips.

Note that AMOR will only work with some window managers. Both KWin (the
KDE window manager) and Metacity (a GTK2 window manager) are supported.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-amor
%defattr(-,root,root,-)
%{tde_bindir}/amor
%{tde_datadir}/apps/amor/
%{tde_tdeappdir}/amor.desktop
%{tde_datadir}/icons/hicolor/*/apps/amor.png
%{tde_tdedocdir}/HTML/en/amor/
%doc AUTHORS COPYING README

%post -n trinity-amor
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-amor
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-eyesapplet
Summary:	eyes applet for Trinity
Group:		Amusements/Graphics

%description -n trinity-eyesapplet
An applet for the KDE panel containing a pair of eyes that follow your mouse
around the screen.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-eyesapplet
%defattr(-,root,root,-)
%{tde_tdelibdir}/eyes_panelapplet.la
%{tde_tdelibdir}/eyes_panelapplet.so
%{tde_datadir}/apps/kicker/applets/eyesapplet.desktop
%doc AUTHORS COPYING README

##########

%package -n trinity-fifteenapplet
Summary:	fifteen pieces puzzle for Trinity
Group:		Amusements/Graphics

%description -n trinity-fifteenapplet
An applet for the KDE panel that lets you play the Fifteen Pieces
sliding block puzzle. You have to order 15 pieces in a 4x4 square by
moving them around.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-fifteenapplet
%defattr(-,root,root,-)
%{tde_tdelibdir}/fifteen_panelapplet.la
%{tde_tdelibdir}/fifteen_panelapplet.so
%{tde_datadir}/apps/kicker/applets/kfifteenapplet.desktop
%doc AUTHORS COPYING README

##########

%package -n trinity-kmoon
Summary:	moon phase indicator for Trinity
Group:		Amusements/Graphics

%description -n trinity-kmoon
An applet for the KDE panel that displays the current phase of the moon.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-kmoon
%defattr(-,root,root,-)
%{tde_tdelibdir}/kmoon_panelapplet.la
%{tde_tdelibdir}/kmoon_panelapplet.so
%{tde_datadir}/apps/kicker/applets/kmoonapplet.desktop
%{tde_datadir}/apps/kmoon/
%{tde_datadir}/icons/hicolor/*/apps/kmoon.png
%{tde_tdedocdir}/HTML/en/kmoon/
%doc AUTHORS COPYING README

%post -n trinity-kmoon
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:

%postun
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:

##########

%package -n trinity-kodo
Summary:	mouse odometer for Trinity
Group:		Amusements/Graphics

%description -n trinity-kodo
KOdometer measures your desktop mileage. It tracks the movement of your mouse
pointer across your desktop and renders it in inches/feet/miles! It can
do cm/metres/km too. Its most exciting feature is the tripometer.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-kodo
%defattr(-,root,root,-)
%{tde_bindir}/kodo
%{tde_tdeappdir}/kodo.desktop
%{tde_datadir}/apps/kodo/numbers.png
%{tde_datadir}/icons/hicolor/*/apps/kodo.png
%{tde_tdedocdir}/HTML/en/kodo/
%doc AUTHORS COPYING README

%post -n trinity-kodo
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kodo
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kteatime
Summary:	Trinity utility for making a fine cup of tea
Group:		Amusements/Graphics

%description -n trinity-kteatime
KTeaTime is a handy timer for steeping tea. No longer will you have to
guess at how long it takes for your tea to be ready. Simply select the
type of tea you have, and it will alert you when the tea is ready to
drink.

KTeaTime sits in the Trinity system tray.

Please note that KTeaTime is written explicitly for Trinity. If you are
using a non-KDE window manager or desktop environment then it is quite
possible that KTeaTime will not work on your system.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-kteatime
%defattr(-,root,root,-)
%{tde_bindir}/kteatime
%{tde_tdeappdir}/kteatime.desktop
%{tde_datadir}/apps/kteatime/
%{tde_datadir}/icons/hicolor/*/apps/kteatime.png
%{tde_tdedocdir}/HTML/en/kteatime/
%doc AUTHORS COPYING README

%post -n trinity-kteatime
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kteatime
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-ktux
Summary:	Tux screensaver for Trinity
Group:		Amusements/Graphics

%description -n trinity-ktux
A neat Tux-in-a-spaceship screensaver for the K Desktop Environment (KDE).

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-ktux
%defattr(-,root,root,-)
%{tde_bindir}/ktux
%{tde_datadir}/apps/ktux/
%{tde_datadir}/applnk/System/ScreenSavers/ktux.desktop
%{tde_datadir}/icons/hicolor/*/apps/ktux.png
%doc AUTHORS COPYING README

%post -n trinity-ktux
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:

%postun -n trinity-ktux
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:

##########

%package -n trinity-kweather
Summary:	weather display applet for Trinity
Group:		Amusements/Graphics

%description -n trinity-kweather
An applet for the KDE panel that displays your area's current weather.
Information shown includes the temperature, wind speed, air pressure
and more. By pressing a button a full weather report can be obtained.

KWeather also provides a weather service that can track multiple weather
stations and provide this information to other applications, including
Konqueror's sidebar and Kontact's summary page.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-kweather
%defattr(-,root,root,-)
%{tde_bindir}/kweatherservice
%{tde_bindir}/kweatherreport
%{tde_libdir}/lib[kt]deinit_kweatherreport.so
%{tde_libdir}/lib[kt]deinit_kweatherreport.la
%{tde_tdelibdir}/kcm_weather.so
%{tde_tdelibdir}/kcm_weather.la
%{tde_tdelibdir}/kcm_weatherservice.so
%{tde_tdelibdir}/kcm_weatherservice.la
%{tde_tdelibdir}/kweatherreport.so
%{tde_tdelibdir}/kweatherreport.la
%{tde_tdelibdir}/weather_panelapplet.la
%{tde_tdelibdir}/weather_panelapplet.so
%{tde_datadir}/apps/kicker/applets/kweather.desktop
%{tde_datadir}/apps/kweather/
%{tde_datadir}/apps/kweatherservice/stations.dat
%{tde_datadir}/apps/kweatherservice/weather_stations.desktop
%{tde_datadir}/icons/hicolor/*/apps/kweather.png
%{tde_datadir}/services/kweatherservice.desktop
%{tde_datadir}/services/kcmweather.desktop
%{tde_datadir}/services/kcmweatherservice.desktop
%{tde_tdedocdir}/HTML/en/kweather/
%doc AUTHORS COPYING README

%post -n trinity-kweather
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kweather
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kworldclock
Summary:	earth watcher for Trinity
Group:		Amusements/Graphics

%description -n trinity-kworldclock
Displays where in the world it is light and dark depending on time, as
well as offering the time in all of the major cities of the world.
This can be run standalone, as an applet in the KDE panel or as a
desktop background.

Additional kworldclock themes are available in the tdeartwork-misc package.

This package is part of Trinity, and a component of the TDE toys module.

%files -n trinity-kworldclock
%defattr(-,root,root,-)
%{tde_bindir}/kworldclock
%{tde_tdelibdir}/ww_panelapplet.la
%{tde_tdelibdir}/ww_panelapplet.so
%{tde_tdeappdir}/kworldclock.desktop
%{tde_datadir}/apps/kdesktop/programs/kdeworld.desktop
%{tde_datadir}/apps/kicker/applets/kwwapplet.desktop
%{tde_datadir}/apps/kworldclock/
%{tde_datadir}/icons/hicolor/*/apps/kworldclock.png
%{tde_tdedocdir}/HTML/en/kworldclock/
%doc AUTHORS COPYING README

%post -n trinity-kworldclock
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kworldclock
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%prep
%setup -q -n kdetoys
%patch1 -p1 -b .ftbfs

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
   --prefix=%{tde_prefix} \
   --exec-prefix=%{tde_prefix} \
   --bindir=%{tde_bindir} \
   --libdir=%{tde_libdir} \
   --datadir=%{tde_datadir} \
   --includedir=%{tde_tdeincludedir} \
   --disable-rpath \
   --enable-new-ldflags \
   --enable-closure \
   --disable-debug --disable-warnings \
   --disable-dependency-tracking --enable-final \
   --with-extra-includes=%{tde_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf "%{buildroot}"
%__make install DESTDIR=%{buildroot}

# replace absolute symlink with relative
ln -nfs tips-en %{buildroot}%{tde_datadir}/apps/amor/tips

## File lists
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
        [ -d $i -a -L $i/common ] && ln -nsf ../common $i/common
      done
    popd
  fi
done
fi

# Useless include file from Amor
%__rm -f %{buildroot}%{tde_tdeincludedir}/AmorIface.h


%clean
%__rm -rf %{buildroot}


%changelog
* Wed Aug 01 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Split into several packages
- Renames to 'trinity-tdetoys'
- Add support for Mageia 2

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Fix HTML directory location

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Fri Oct 28 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT

