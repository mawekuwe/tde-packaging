# Default version for this component
%define tde_pkg gwenview
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
Summary:		Gwenview is an image viewer for TDE.
Version:		1.4.2
Release:		%{?!preversion:11}%{?preversion:10_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

# EXIV2 support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}exiv2-devel
%endif
%if 0%{?suse_version}
BuildRequires:	libexiv2-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	exiv2-devel
%endif

%if "%{?tde_prefix}" == "/usr"
Conflicts: kdegraphics
%endif


%description
Gwenview is a fast and easy to use image viewer/browser for TDE.
All common image formats are supported, such as PNG(including transparency),
JPEG(including EXIF tags and lossless transformations), GIF, XCF (Gimp
image format), BMP, XPM and others. Standard features include slideshow,
fullscreen view, image thumbnails, drag'n'drop, image zoom, full network
transparency using the KIO framework, including basic file operations and
browsing in compressed archives, non-blocking GUI with adjustable views.
Gwenview also provides image and directory KParts components for use e.g. in
Konqueror. Additional features, such as image renaming, comparing,
converting, and batch processing, HTML gallery and others are provided by the
KIPI image framework.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; source /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --docdir=%{tde_tdedocdir} \
  --includedir=%{tde_tdeincludedir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Removes useless files (-devel ?)
%__rm -f %{?buildroot}%{tde_libdir}/libgwenviewcore.so


%clean
%__rm -rf %{buildroot}


%post
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done
/sbin/ldconfig


%postun
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done
/sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/gwenview
%{tde_libdir}/libgwenviewcore.la
%{tde_libdir}/libgwenviewcore.so.1
%{tde_libdir}/libgwenviewcore.so.1.0.0
%{tde_libdir}/libkdeinit_gwenview.la
%{tde_libdir}/libkdeinit_gwenview.so
%{tde_tdelibdir}/gwenview.la
%{tde_tdelibdir}/gwenview.so
%{tde_tdelibdir}/libgvdirpart.la
%{tde_tdelibdir}/libgvdirpart.so
%{tde_tdelibdir}/libgvimagepart.la
%{tde_tdelibdir}/libgvimagepart.so
%{tde_tdeappdir}/gwenview.desktop
%{tde_datadir}/apps/gwenview/
%{tde_datadir}/apps/gvdirpart/gvdirpart.rc
%{tde_datadir}/apps/gvimagepart/gvimagepart.rc
%{tde_datadir}/apps/gvimagepart/gvimagepartpopup.rc
%{tde_datadir}/apps/kconf_update/gwenview_1.4_osdformat.sh
%{tde_datadir}/apps/kconf_update/gwenview_1.4_osdformat.upd
%{tde_datadir}/apps/kconf_update/gwenview_thumbnail_size.sh
%{tde_datadir}/apps/kconf_update/gwenview_thumbnail_size.upd
%{tde_datadir}/apps/konqueror/servicemenus/konqgwenview.desktop
%{tde_datadir}/config.kcfg/fileoperationconfig.kcfg
%{tde_datadir}/config.kcfg/fileviewconfig.kcfg
%{tde_datadir}/config.kcfg/fullscreenconfig.kcfg
%{tde_datadir}/config.kcfg/gvdirpartconfig.kcfg
%{tde_datadir}/config.kcfg/imageviewconfig.kcfg
%{tde_datadir}/config.kcfg/miscconfig.kcfg
%{tde_datadir}/config.kcfg/slideshowconfig.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/gvdirpart.png
%{tde_datadir}/icons/crystalsvg/scalable/apps/gvdirpart.svg
%{tde_datadir}/icons/hicolor/*/apps/gwenview.png
%{tde_datadir}/icons/hicolor/*/apps/gvdirpart.png
%{tde_datadir}/icons/hicolor/scalable/apps/gvdirpart.svg
%{tde_datadir}/icons/hicolor/scalable/apps/gwenview.svgz
%{tde_datadir}/man/man1/gwenview.1*
%{tde_datadir}/services/gvdirpart.desktop
%{tde_datadir}/services/gvimagepart.desktop
%lang(en) %{tde_tdedocdir}/HTML/en/gwenview/

%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1.4.2-11
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 1.4.2-10
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 1.4.2-9
- Initial release for TDE 3.5.13.1

* Sat Aug 04 2012 Francois Andriot <francois.andriot@free.fr> - 1.4.2-8
- Add support for Mageia 2 and Mandriva 2011
- Define QT_CLEAN_NAMESPACE during libmng checks [Commit #59c7639f]

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 1.4.2-7
- Rebuilt for Fedora 17
- Fix post and postun
- Adds patches from GIT

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.2-6
- Fix HTML directory location

* Fri Nov 04 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.2-5
- Adds missing files

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.2-4
- Rebuilt for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15

* Wed Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.2-3
- Import to GIT

* Wed Aug 24 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.2-2
- Add fix for Fedora 15

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.2-1
- Correct macro to install under "/opt", if desired

* Sat Aug 13 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.2-0
- Initial release for RHEL 6.0

