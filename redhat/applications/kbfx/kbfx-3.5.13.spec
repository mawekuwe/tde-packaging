# Default version for this component
%define kdecomp kbfx

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
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-%{kdecomp}
Summary:	an alternative to K-Menu for KDE [Trinity]
Version:	0.4.9.3.1
Release:	1%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [kbfx] Missing LDFLAGS cause FTBFS on Mageia 2 and Mandriva 2011
Patch1:		kbfx-3.5.13-missing_ldflags.patch
# [kbfx] Some files are installed in wrong directories ...
Patch2:		kbfx-3.5.13-fix_install_directories.patch


BuildRequires: tqtinterface-devel
BuildRequires: trinity-tdelibs-devel
BuildRequires: trinity-tdebase-devel
BuildRequires: desktop-file-utils

%description
KBFX is an alternative to the classical K-Menu button and its menu.
It improves the user experience by enabling him to set a bigger (and thus more
visible) start button and by finally replacing the Win95-like K-Menu.
If you still want the old menu, because you're used to it, it is still
available as an option in kbfx. We recommend, however, that you give the Spinx
bar a try.

Homepage: http://www.kbfx.org


%prep
%setup -q -n applications/%{kdecomp}
%patch1 -p1 -b .ldflags
%patch2 -p1 -b .dir

# Fix TDE executable path in 'CMakeLists.txt' ...
%__sed -i "CMakeLists.txt" \
  -e "s|/usr/bin/uic-tqt|%{tde_bindir}/uic-tqt|" \
  -e "s|/usr/bin/tmoc|%{tde_bindir}/tmoc|" \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|"
  
# Prevents hardcoded TDE directories ...
%__sed -i "cmakemodules/FindKdeLibs.cmake" \
  -e "s|^\(set(HTML_INSTALL_DIR.*\)|#\1|" \
  -e "s|^\(set(INCLUDE_INSTALL_DIR.*\)|#\1|"

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{tde_includedir}:%{tde_tdeincludedir}:%{tde_includedir}/tqt"

%if 0%{?rhel} || 0%{?fedora}
%__mkdir_p build
cd build
%endif

%cmake \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DDOC_INSTALL_DIR=%{tde_tdedocdir} \
  -DHTML_INSTALL_DIR=%{tde_tdedocdir}/HTML \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DUSE_STRIGI=OFF \
  -DUSE_MENUDRAKE=OFF \
  -DUSE_KDE4=OFF \
  ..

%__make %{?_smp_mflags}


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
%{tde_tdelibdir}/libkbfxspinx.la
%{tde_tdelibdir}/libkbfxspinx.so
%{tde_tdeappdir}/kbfx_theme.desktop
%{tde_tdeappdir}/kbfxconfigapp.desktop
%{tde_datadir}/apps/kbfx/skins/*/*
%{tde_datadir}/apps/kbfxconfigapp/kbfxconfigappui.rc
%{tde_datadir}/apps/kicker/applets/kbfxspinx.desktop
%{tde_datadir}/apps/konqueror/servicemenus/kbfx_install_theme.desktop
%{tde_datadir}/apps/konqueror/servicemenus/kbfx_prepare_theme.desktop
%{tde_tdedocdir}/HTML/en/common/kbfx-*.jpg
%{tde_tdedocdir}/HTML/en/kbfxconfigapp/index.cache.bz2
%{tde_tdedocdir}/HTML/en/kbfxconfigapp/index.docbook
%{tde_tdedocdir}/kbfx/
%{tde_datadir}/icons/hicolor/*/apps/kbfx.png
%{tde_datadir}/icons/hicolor/*/apps/kbfxconfigapp.png
%{tde_datadir}/locale/*/LC_MESSAGES/kbfxconfigapp.mo
%{tde_datadir}/mimelnk/application/x-kbfxtheme.desktop


%Changelog
* Sun Nov 20 2011 Francois Andriot <francois.andriot@free.fr> - 0.4.9.3.1-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
