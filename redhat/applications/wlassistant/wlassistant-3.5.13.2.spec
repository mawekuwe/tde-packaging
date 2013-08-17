# Default version for this component
%define tde_pkg wlassistant
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

%define _docdir %{tde_tdedocdir}


Name:			trinity-%{tde_pkg}
Summary:		User friendly TDE frontend for wireless network connection [Trinity]
Version:		0.5.7
Release:		%{?!preversion:4}%{?preversion:3_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://wlassistant.sourceforge.net/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

BuildRequires:	python
BuildRequires:	cmake >= 2.8

%description
Wireless Assistant scans for wireless access points and displays link quality,
encryption and other useful information. When user wants to connect to a
network, Wireless Assistant opens up its wizards and guides the user through
Wi-Fi settings. After a successful connection is made the settings are
remembered so next time the user won't have to enter them again.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

# Shitty hack for RHEL4 ...
if [ -d "/usr/X11R6" ]; then
  export CMAKE_INCLUDE_PATH="${CMAKE_INCLUDE_PATH}:/usr/X11R6/include:/usr/X11R6/%{_lib}"
  export CFLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
  export CXXFLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%__mkdir_p build
cd build
%endif

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DBUILD_ALL=on \
  ..

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc ChangeLog VERSION
%{tde_bindir}/wlassistant
%{tde_tdeappdir}/wlassistant.desktop
%{tde_datadir}/icons/hicolor/16x16/apps/wlassistant.png
%{tde_datadir}/icons/hicolor/32x32/apps/wlassistant.png
%lang(ar) %{tde_datadir}/locale/ar/LC_MESSAGES/wlassistant.mo
%lang(ca) %{tde_datadir}/locale/ca/LC_MESSAGES/wlassistant.mo
%lang(es) %{tde_datadir}/locale/es/LC_MESSAGES/wlassistant.mo
%lang(fr) %{tde_datadir}/locale/fr/LC_MESSAGES/wlassistant.mo
%lang(nb) %{tde_datadir}/locale/nb/LC_MESSAGES/wlassistant.mo
%lang(pl) %{tde_datadir}/locale/pl/LC_MESSAGES/wlassistant.mo
%lang(pt) %{tde_datadir}/locale/pt_BR/LC_MESSAGES/wlassistant.mo
%lang(sv) %{tde_datadir}/locale/sv/LC_MESSAGES/wlassistant.mo
%lang(zh_CN) %{tde_datadir}/locale/zh_CN/LC_MESSAGES/wlassistant.mo
%lang(zh_TW) %{tde_datadir}/locale/zh_TW/LC_MESSAGES/wlassistant.mo


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 0.5.7-4
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.5.7-3
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.5.7-2
- Initial release for TDE 3.5.13.1

* Tue Nov 29 2011 Francois Andriot <francois.andriot@free.fr> - 0.5.7-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
