# Default version for this component
%define kdecomp kpowersave
%define version 0.7.3
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}
Summary:	HAL based power management applet for Trinityfiles or directories.

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz


BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils

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


%prep
%setup -q -n applications/%{kdecomp}

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
	
%__mkdir build
cd build
%cmake \
	..

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


%clean
%__rm -rf %{buildroot}


%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/kpowersave
%{_libdir}/libkdeinit_kpowersave.la
%{_libdir}/libkdeinit_kpowersave.so
%{tde_libdir}/kpowersave.la
%{tde_libdir}/kpowersave.so
%{_datadir}/applications/kde/kpowersave.desktop
%{_datadir}/apps/kpowersave/eventsrc
%{_datadir}/apps/kpowersave/icons/*/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/autostart/kpowersave-autostart.desktop
%{_datadir}/config/kpowersaverc

%Changelog
* Sat Nov 26 2011 Francois Andriot <francois.andriot@free.fr> - 0.7.3-2
- Add missing /sbin/ldconfig
- Add missing doc file

* Sat Nov 19 2011 Francois Andriot <francois.andriot@free.fr> - 0.7.3-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
