# Default version for this component
%define tde_pkg kbfx
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


Name:			trinity-%{tde_pkg}
Summary:		an alternative to K-Menu for TDE [Trinity]
Version:		0.4.9.3.1
Release:		%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

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


%description
KBFX is an alternative to the classical K-Menu button and its menu.
It improves the user experience by enabling him to set a bigger (and thus more
visible) start button and by finally replacing the Win95-like K-Menu.
If you still want the old menu, because you're used to it, it is still
available as an option in kbfx. We recommend, however, that you give the Spinx
bar a try.

Homepage: http://www.kbfx.org


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

# Fix TDE executable path in 'CMakeLists.txt' ...
%__sed -i "CMakeLists.txt" \
  -e "s|/usr/bin/uic-tqt|%{tde_bindir}/uic-tqt|" \
  -e "s|/usr/bin/tmoc|%{tde_bindir}/tmoc|" \
  -e "s|/usr/include/tqt||"
  
%build
unset QTDIR QTINC QTLIB
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
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DDATA_INSTALL_DIR=%{tde_datadir}/apps \
  -DMIME_INSTALL_DIR=%{tde_datadir}/mimelnk \
  -DXDG_APPS_INSTALL_DIR=%{tde_tdeappdir} \
  -DDOC_INSTALL_DIR=%{tde_tdedocdir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  \
  -DUSE_STRIGI=OFF \
  -DUSE_MENUDRAKE=OFF \
  -DBUILD_DOC=ON \
  -DBUILD_ALL=OFF \
  ..

# Not SMP safe !
%__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build VERBOSE=1


%clean
%__rm -rf %{buildroot}


%post
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
update-desktop-database %{tde_appdir} &> /dev/null

%postun
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
update-desktop-database %{tde_appdir} &> /dev/null


%files
%defattr(-,root,root,-)
%{tde_bindir}/kbfxconfigapp
%{tde_tdeincludedir}/kbfx/
%{tde_libdir}/kbfx/plugins/libkbfxplasmadataplasmoid.la
%{tde_libdir}/kbfx/plugins/libkbfxplasmadataplasmoid.so
%{tde_libdir}/kbfx/plugins/libkbfxplasmadatasettings.la
%{tde_libdir}/kbfx/plugins/libkbfxplasmadatasettings.so
%{tde_libdir}/kbfx/plugins/libkbfxplasmadatastub.la
%{tde_libdir}/kbfx/plugins/libkbfxplasmadatastub.so
%{tde_libdir}/kbfx/plugins/libkbfxplasmarecentstuff.la
%{tde_libdir}/kbfx/plugins/libkbfxplasmarecentstuff.so
%{tde_libdir}/libkbfxcommon.la
%{tde_libdir}/libkbfxcommon.so
%{tde_libdir}/libkbfxdata.la
%{tde_libdir}/libkbfxdata.so
%{tde_tdelibdir}/kbfxspinx.la
%{tde_tdelibdir}/kbfxspinx.so
%{tde_tdeappdir}/kbfx_theme.desktop
%{tde_tdeappdir}/kbfxconfigapp.desktop
%{tde_datadir}/apps/kbfx/skins/*/*
%{tde_datadir}/apps/kbfxconfigapp/kbfxconfigappui.rc
%{tde_datadir}/apps/kicker/applets/kbfxspinx.desktop
%{tde_datadir}/apps/konqueror/servicemenus/kbfx_install_theme.desktop
%{tde_datadir}/apps/konqueror/servicemenus/kbfx_prepare_theme.desktop
#%{tde_tdedocdir}/HTML/en/common/kbfx-*.jpg
#%{tde_tdedocdir}/HTML/en/kbfxconfigapp/
%{tde_tdedocdir}/kbfx/
%{tde_datadir}/icons/hicolor/*/apps/kbfx.png
%{tde_datadir}/icons/hicolor/*/apps/kbfxconfigapp.png
#%{tde_datadir}/locale/*/LC_MESSAGES/kbfxconfigapp.mo
%{tde_datadir}/mimelnk/application/x-kbfxtheme.desktop


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.4.9.3.1-5
- Initial release for TDE 14.0.0
