# Default version for this component
%define tde_pkg kpowersave
%define tde_version 3.5.13.2

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

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Version:		0.7.3
Release:		%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}
Summary:		HAL based power management applet for Trinityfiles or directories.

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz


BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	hal-devel
BuildRequires:	trinity-dbus-tqt-devel >= 1:0.63


%description
KPowersave is a TDE systray applet which allows to control the power 
management settings and policies of your computer.
It relies on HAL to do the heavy lifting.

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
 
KPowersave supports schemes with following configurable specific 
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
unset QTDIR || : ; . /etc/profile.d/qt3.sh
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


%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_appdir} > /dev/null
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
update-desktop-database %{tde_appdir} > /dev/null
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_bindir}/kpowersave
%{tde_libdir}/libkdeinit_kpowersave.la
%{tde_libdir}/libkdeinit_kpowersave.so
%{tde_tdelibdir}/kpowersave.la
%{tde_tdelibdir}/kpowersave.so
%{tde_tdeappdir}/kpowersave.desktop
%{tde_datadir}/apps/kpowersave/eventsrc
%{tde_datadir}/apps/kpowersave/icons/*/*/*/*.png
%{tde_datadir}/icons/hicolor/*/*/*.png
%{tde_datadir}/autostart/kpowersave-autostart.desktop
%{tde_datadir}/config/kpowersaverc

%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 0.7.3-5
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.7.3-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.7.3-3
- Initial release for TDE 3.5.13.1

* Sat Nov 26 2011 Francois Andriot <francois.andriot@free.fr> - 0.7.3-2
- Add missing /sbin/ldconfig
- Add missing doc file

* Sat Nov 19 2011 Francois Andriot <francois.andriot@free.fr> - 0.7.3-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
