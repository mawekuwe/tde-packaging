# Default version for this component
%define tde_pkg tdepowersave
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


Name:		trinity-%{tde_pkg}
Version:	0.7.3
Release:	%{?!preversion:5}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:	Power management applet for Trinityfiles or directories.

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

Obsoletes:		trinity-kpowersave < %{version}-%{release}
Provides:		trinity-kpowersave = %{version}-%{release}

%description
TDEPowersave is a TDE systray applet which allows to control the power 
management settings and policies of your computer.

Current feature list:
 * support for ACPI, APM and PMU
 * trigger suspend to disk/ram and standby
 * switch cpu frequency policy (between: performance, dynamic and powersave)
 * applet icon with information about AC state, battery fill and battery
   (warning) states
 * applet tooltip with information about battery fill and remaining battery 
   time/percentage
 * autosuspend (to suspend the machine if the user has been inactive for a 
   defined time)
 * a global configurable blacklist with programs which prevent autosuspend
   (e.g. videoplayer and cd burning tools)
 * trigger lock screen and select the lock method
 * KNotify support
 * online help
 * localisations for many languages
 
TDEPowersave supports schemes with following configurable specific 
settings for:
 * screensaver
 * DPMS
 * autosuspend
 * scheme specific blacklist for autosuspend
 * notification settings


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"
	
if ! rpm -E %%cmake|grep -q "cd build"; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_appdir} > /dev/null
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

# Disables automatic poweroff, make sure we match both "kpowersave" and "tdepowersave"
if [ $1 = 1 ] && [ -r /etc/acpi/actions/power.sh ]; then
  %__cp -f "/etc/acpi/actions/power.sh" "/etc/acpi/actions/power.sh.tdepowersavebackup"
  %__sed -i "/etc/acpi/actions/power.sh" -e "s|kpowersave|powersave|"
fi

%postun
update-desktop-database %{tde_appdir} > /dev/null
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

if [ $1 = 0 ] && [ -r "/etc/acpi/actions/power.sh.tdepowersavebackup" ]; then
  %__mv -f "/etc/acpi/actions/power.sh.tdepowersavebackup" "/etc/acpi/actions/power.sh"
fi


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_bindir}/tdepowersave
%{tde_libdir}/libtdeinit_tdepowersave.la
%{tde_libdir}/libtdeinit_tdepowersave.so
%{tde_tdelibdir}/tdepowersave.la
%{tde_tdelibdir}/tdepowersave.so
%{tde_tdeappdir}/tdepowersave.desktop
%{tde_datadir}/apps/tdepowersave/eventsrc
%{tde_datadir}/apps/tdepowersave/icons/*/*/*/*.png
%{tde_datadir}/icons/hicolor/*/*/*.png
%{tde_datadir}/autostart/tdepowersave-autostart.desktop
%{tde_datadir}/config/tdepowersaverc

%lang(cs) %{tde_tdedocdir}/HTML/cs/tdepowersave/
%lang(de) %{tde_tdedocdir}/HTML/de/tdepowersave/
%lang(en) %{tde_tdedocdir}/HTML/en/tdepowersave/
%lang(fi) %{tde_tdedocdir}/HTML/fi/tdepowersave/
%lang(hu) %{tde_tdedocdir}/HTML/hu/tdepowersave/
%lang(nb) %{tde_tdedocdir}/HTML/nb/tdepowersave/


%changelog
* Thu Jul 04 2013 Francois Andriot <francois.andriot@free.fr> - 0.7.3-5
- Initial release for TDE 14.0.0
