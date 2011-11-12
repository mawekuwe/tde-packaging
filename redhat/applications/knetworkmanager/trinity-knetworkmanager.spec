# Default version for this component
%define kdecomp knetworkmanager
%if 0%{?fedora} >= 15
%define version 0.9
%else
%define version 0.8
%endif
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}/kde
%define tde_libdir %{_libdir}/trinity

Name:			trinity-%{kdecomp}
Version:		%{?version}
Release:		%{?release}%{?dist}%{?_variant}

Summary:        Trinity applet for Network Manager

Group:          Applications/Internet
License:        GPLv2+
URL:            http://en.opensuse.org/Projects/KNetworkManager

%if "%{?version}" == "0.9"
Source0:		%{kdecomp}9-3.5.13.tar.gz
%else
Source0:		%{kdecomp}8-3.5.13.tar.gz
%endif

Patch0:			knetworkmanager-3.5.13-missing_includes.patch
Patch1:			knetworkmanager-3.5.13-wpa_passphrase_lag.patch

# For knetworkmanager 0.9 only !
Patch10:		knetworkmanager-3.5.13-subdir_version.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       NetworkManager-gnome
Requires:       kde-filesystem
BuildRequires:  desktop-file-utils

BuildRequires:	dbus-1-tqt-devel
BuildRequires:	dbus-tqt-devel
BuildRequires:	NetworkManager-glib-devel

%description
KNetworkManager is a system tray applet for controlling network
connections on systems that use the NetworkManager daemon.


%package devel
Summary:        Common data shared among the MySQL GUI Suites
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers for knetworkmanager


%prep 
%if "%{?version}" == "0.9"
%setup -q -n applications/%{kdecomp}9
%else
%setup -q -n applications/%{kdecomp}8
%endif

%if "%{?version}" == "0.9"
%patch10 -p1
%endif

cd knetworkmanager-0.*/src
%patch0 -p3
%patch1 -p3



%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"
export LD_LIBRARY_PATH="%{_libdir}"

# Missing TDE macros
%__mkdir_p cmake
%__ln_s %{_datadir}/cmake cmake/modules

%__mkdir build
cd build
%cmake ..
%__make %{?_smp_mflags} 

%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=%{?buildroot} -C build


%clean
%__rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

%files 
%defattr(-,root,root,-)
%{_bindir}/knetworkmanager
%{_libdir}/*.la
%{_libdir}/*.so
%{_sysconfdir}/dbus-1/system.d/knetworkmanager.conf
%{_datadir}/applications/kde/knetworkmanager.desktop
%{_datadir}/apps/knetworkmanager
%{_datadir}/icons/*/*/apps/knetworkmanager*
%{_datadir}/servicetypes/knetworkmanager_plugin.desktop
%{_datadir}/servicetypes/knetworkmanager_vpnplugin.desktop


%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{tde_libdir}/*.la
%{tde_libdir}/*.so

%changelog
* Tue Nov 11 2011 Francois Andriot <francois.andriot@free.fr> - 0.8-1
- Initial build
