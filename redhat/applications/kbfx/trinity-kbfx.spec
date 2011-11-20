# Default version for this component
%define kdecomp kbfx
%define version 0.4.9.3.1
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	an alternative to K-Menu for KDE [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
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

# Fix TDE executable path in CMakeLists.txt
%__sed -i "CMakeLists.txt" \
  -e "s,/usr/bin/uic-tqt,%{_bindir}/uic-tqt," \
  -e "s,/usr/bin/tmoc,%{_bindir}/tmoc," \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
	
%__mkdir build
cd build
%cmake \
  -DUSE_STRIGI=OFF \
  -DUSE_MENUDRAKE=OFF \
  -DUSE_KDE4=OFF \
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
%{_bindir}/kbfxconfigapp
%{_includedir}/kbfx
%{_libdir}/kbfx/plugins/libkbfxplasmadataplasmoid.la
%{_libdir}/kbfx/plugins/libkbfxplasmadataplasmoid.so
%{_libdir}/kbfx/plugins/libkbfxplasmadatasettings.la
%{_libdir}/kbfx/plugins/libkbfxplasmadatasettings.so
%{_libdir}/kbfx/plugins/libkbfxplasmadatastub.la
%{_libdir}/kbfx/plugins/libkbfxplasmadatastub.so
%{_libdir}/kbfx/plugins/libkbfxplasmarecentstuff.la
%{_libdir}/kbfx/plugins/libkbfxplasmarecentstuff.so
%{_libdir}/libkbfxcommon.la
%{_libdir}/libkbfxcommon.so
%{_libdir}/libkbfxdata.la
%{_libdir}/libkbfxdata.so
%{tde_libdir}/libkbfxspinx.la
%{tde_libdir}/libkbfxspinx.so
%{_datadir}/applications/kde/kbfx_theme.desktop
%{_datadir}/applications/kde/kbfxconfigapp.desktop
%{_datadir}/apps/kbfx/skins/*/*
%{_datadir}/apps/kbfxconfigapp/kbfxconfigappui.rc
%{_datadir}/apps/kicker/applets/kbfxspinx.desktop
%{_datadir}/apps/konqueror/servicemenus/kbfx_install_theme.desktop
%{_datadir}/apps/konqueror/servicemenus/kbfx_prepare_theme.desktop
%{_docdir}/HTML/en/common/kbfx-*.jpg
%{_docdir}/HTML/en/kbfxconfigapp/index.cache.bz2
%{_docdir}/HTML/en/kbfxconfigapp/index.docbook
%{_docdir}/kbfx
%{_datadir}/icons/hicolor/*/apps/kbfx.png
%{_datadir}/icons/hicolor/*/apps/kbfxconfigapp.png
%{_datadir}/locale/*/LC_MESSAGES/kbfxconfigapp.mo
%{_datadir}/mimelnk/application/x-kbfxtheme.desktop

%Changelog
* Sun Nov 20 2011 Francois Andriot <francois.andriot@free.fr> - 0.4.9.3.1-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
