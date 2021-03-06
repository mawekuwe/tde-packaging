# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_version 3.5.13.2

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-tdegraphics
Version:	%{tde_version}
Release:	%{?!preversion:3}%{?preversion:2_%{preversion}}%{?dist}%{?_variant}

License:	GPL
Summary:    Trinity Desktop Environment - Graphics Applications

Group:      Applications/Multimedia
Prefix:		%{tde_prefix}

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz

# TDE
## RHEL / Fedora specific patches
# [kdegraphics/kpdf/xpdf] Disable 'mkstemps' support for RHEL5
Patch3:		kdegraphics-3.5.13-xpdf_disable_mkstemps.patch

# [tdegraphics] Fix build on RHEL4
Patch201:	kdegraphics-3.5.13.1-fix_rhel4_libraries.patch

BuildRequires: cmake >= 2.8
BuildRequires: trinity-tqtinterface-devel >= %{version}
BuildRequires: trinity-tdelibs-devel >= %{version}
BuildRequires: trinity-tdebase-devel >= %{version}
BuildRequires: gettext
BuildRequires: libmng-devel
%if 0%{?mdkversion} && 0%{?pclinuxos} == 0
BuildRequires: %{_lib}png15-devel
%else
BuildRequires: libpng-devel
%endif
BuildRequires: libtiff-devel
BuildRequires: automake libtool
BuildRequires: libusb-devel
BuildRequires: pcre-devel

# GIF support
%if 0%{?suse_version}
BuildRequires: giflib-devel
%else
BuildRequires: libungif-devel
%endif

# GPHOTO2 support
%if 0%{?suse_version}
BuildRequires: libgphoto2-devel
%else
BuildRequires: gphoto2-devel
%endif

# PAPER support
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_paper 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}paper-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	libpaper-devel
%endif
%endif

# T1LIB support
%if 0%{?suse_version} && 0%{?suse_version} <= 1230
%define with_t1lib 1
BuildRequires:	t1lib-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?fedora}
%define with_t1lib 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}t1lib-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora}
BuildRequires:	t1lib-devel
%endif
%endif

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}sane1-devel
# kuickshow
#BuildRequires:	%{_lib}imlib-devel
# kpovmodeler
BuildRequires:	%{_lib}xi-devel
# kgamma
BuildRequires:	%{_lib}xxf86vm-devel
# ksvg
%if 0%{?mgaversion} >= 4
BuildRequires:	%{_lib}xmu-devel
%else
BuildRequires:	%{_lib}xmu%{?mgaversion:6}-devel
%endif
# kpovmodeler
BuildRequires:	%{_lib}mesagl1-devel
BuildRequires:	%{_lib}mesaglu1-devel
%else
BuildRequires:	sane-backends-devel

# kuickshow
#BuildRequires:	imlib-devel

%if 0%{?rhel} == 4
BuildRequires:	xorg-x11-devel
%else
BuildRequires: libdrm-devel

# kpovmodeler
%if 0%{?suse_version} == 1140
BuildRequires:	libXi6-devel
%else
BuildRequires:	libXi-devel

# kgamma
BuildRequires:	libXxf86vm-devel
%endif

# ksvg
%if 0%{?suse_version} == 1140
BuildRequires:	xorg-x11-libXmu-devel
%else
BuildRequires:	libXmu-devel
%endif
%endif

# kpovmodeler
%if 0%{?suse_version}
%if 0%{?suse_version} >= 1220
BuildRequires:	Mesa-libGL-devel
BuildRequires:	Mesa-libGLU-devel
%else
BuildRequires:	Mesa-devel
%endif
%else
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
%endif
%endif

#kfile-plugin
BuildRequires:	OpenEXR-devel

# kpdf
%if 0%{?suse_version} == 1140
BuildRequires: freetype2-devel
%else
BuildRequires: freetype-devel
%endif

# poppler
%if 0%{?rhel} >=6 || 0%{?fedora} >= 15 || 0%{?suse_version}
BuildRequires: poppler-devel >= 0.12
#BuildRequires:	poppler-qt-devel >= 0.12
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}poppler-devel
%endif
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
# On RHEL 5, the distro-provided poppler is too old. We built a newer one.
BuildRequires:	trinity-poppler-devel >= 0.12
BuildRequires:	trinity-poppler-qt3-devel >= 0.12
%endif

# ksvg
BuildRequires: fontconfig-devel
%if 0%{?suse_version}
BuildRequires: liblcms-devel
%else
BuildRequires: lcms-devel
%endif
BuildRequires: libart_lgpl-devel

# kuickshow
#define build_kuickshow 1
BuildRequires: fribidi-devel

# kamera
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
%define build_kamera 1
%endif

# kmrml
#define build_kmrml 1
#Requires:		gift
Obsoletes:		trinity-kmrml

Obsoletes:	trinity-kdegraphics < %{version}-%{release}
Provides:	trinity-kdegraphics = %{version}-%{release}
Obsoletes:	trinity-kdegraphics-libs < %{version}-%{release}
Provides:	trinity-kdegraphics-libs = %{version}-%{release}
Obsoletes:	trinity-kdegraphics-extras < %{version}-%{release}
Provides:	trinity-kdegraphics-extras = %{version}-%{release}


%{?build_kamera:Requires: trinity-kamera = %{version}-%{release}}
Requires: trinity-kcoloredit = %{version}-%{release}
Requires: %{name}-kfile-plugins = %{version}-%{release}
Requires: trinity-kdvi = %{version}-%{release}
Requires: trinity-kfax = %{version}-%{release}
Requires: trinity-kfaxview = %{version}-%{release}
Requires: trinity-kgamma = %{version}-%{release}
Requires: trinity-kghostview = %{version}-%{release}
Requires: trinity-kiconedit = %{version}-%{release}
%{?build_kmrml:Requires: trinity-kmrml = %{version}-%{release}}
Requires: trinity-kolourpaint = %{version}-%{release}
Requires: trinity-kooka = %{version}-%{release}
Requires: trinity-kpdf = %{version}-%{release}
Requires: trinity-kpovmodeler = %{version}-%{release}
Requires: trinity-kruler = %{version}-%{release}
Requires: trinity-ksnapshot = %{version}-%{release}
Requires: trinity-ksvg = %{version}-%{release}
Requires: trinity-kview = %{version}-%{release}
Requires: trinity-kviewshell = %{version}-%{release}
Requires: trinity-libkscan = %{version}-%{release}
Requires: trinity-libpoppler-tqt = %{version}-%{release}

%description
Graphics applications for the Trinity Desktop Environment, including
%if 0%{?build_kamera}
* kamera (digital camera support)
%endif
* kcoloredit (palette editor and color chooser)
* kdvi (displays TeX .dvi files)
* kfax
* kfaxview
* kghostview (displays postscript files)
* kiconedit (icon editor)
* kooka (scanner application)
* kpdf (displays PDF files)
* kpovmodler
* kruler (screen ruler and color measurement tool)
* ksnapshot (screen capture utility)
* kview (image viewer for GIF, JPEG, TIFF, etc.)

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README

##########

%if 0%{?build_kamera}

%package -n trinity-kamera
Summary:	Digital camera io_slave for Konqueror
Group:		Applications/Graphics

%description -n trinity-kamera
This is a digital camera io_slave for TDE which uses gphoto2 and libgpio
to allow access to your camera's pictures with the URL camera:/

%post -n trinity-kamera
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kamera
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%files -n trinity-kamera
%defattr(-,root,root,-)
%{tde_tdelibdir}/kcm_kamera.la
%{tde_tdelibdir}/kcm_kamera.so
%{tde_tdelibdir}/kio_kamera.la
%{tde_tdelibdir}/kio_kamera.so
%{tde_tdeappdir}/kamera.desktop
%{tde_datadir}/icons/crystalsvg/*/actions/camera_test.png
%{tde_datadir}/icons/crystalsvg/*/apps/camera.png
%{tde_datadir}/icons/crystalsvg/*/devices/camera.png
%{tde_datadir}/icons/crystalsvg/*/filesystems/camera.png
%{tde_datadir}/services/camera.protocol
%{tde_tdedocdir}/HTML/en/kamera/

%endif

##########

%package -n trinity-kcoloredit
Summary:	A color palette editor and color picker for TDE
Group:		Applications/Graphics

%description -n trinity-kcoloredit
This package contains two programs, a color palette editor and also a color
picker.

%files -n trinity-kcoloredit
%defattr(-,root,root,-)
%{tde_bindir}/kcolorchooser
%{tde_bindir}/kcoloredit
%{tde_tdeappdir}/kcolorchooser.desktop
%{tde_tdeappdir}/kcoloredit.desktop
%{tde_datadir}/apps/kcoloredit/kcoloreditui.rc
%{tde_datadir}/icons/hicolor/*/apps/kcolorchooser.png
%{tde_datadir}/icons/hicolor/*/apps/kcoloredit.png
%{tde_tdedocdir}/HTML/en/kcoloredit/

%post -n trinity-kcoloredit
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kcoloredit
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package kfile-plugins
Summary:	TDE metainfo plugins for graphic files
Group:		Environment/Libraries
 
%description kfile-plugins
This packages provides meta information for graphic files (file sizes,
tags, etc. all from within the file manager).

%files kfile-plugins
%defattr(-,root,root,-)
%{tde_tdelibdir}/gsthumbnail.la
%{tde_tdelibdir}/gsthumbnail.so
%{tde_tdelibdir}/kfile_bmp.la
%{tde_tdelibdir}/kfile_bmp.so
%{tde_tdelibdir}/kfile_dds.la
%{tde_tdelibdir}/kfile_dds.so
%{tde_tdelibdir}/kfile_dvi.la
%{tde_tdelibdir}/kfile_dvi.so
%{tde_tdelibdir}/kfile_exr.la
%{tde_tdelibdir}/kfile_exr.so
%{tde_tdelibdir}/kfile_gif.la
%{tde_tdelibdir}/kfile_gif.so
%{tde_tdelibdir}/kfile_ico.la
%{tde_tdelibdir}/kfile_ico.so
%{tde_tdelibdir}/kfile_jpeg.la
%{tde_tdelibdir}/kfile_jpeg.so
%{tde_tdelibdir}/kfile_pcx.la
%{tde_tdelibdir}/kfile_pcx.so
%{tde_tdelibdir}/kfile_pdf.la
%{tde_tdelibdir}/kfile_pdf.so
%{tde_tdelibdir}/kfile_png.la
%{tde_tdelibdir}/kfile_png.so
%{tde_tdelibdir}/kfile_pnm.la
%{tde_tdelibdir}/kfile_pnm.so
%{tde_tdelibdir}/kfile_ps.la
%{tde_tdelibdir}/kfile_ps.so
%{tde_tdelibdir}/kfile_raw.la
%{tde_tdelibdir}/kfile_raw.so
%{tde_tdelibdir}/kfile_rgb.la
%{tde_tdelibdir}/kfile_rgb.so
%{tde_tdelibdir}/kfile_tga.la
%{tde_tdelibdir}/kfile_tga.so
%{tde_tdelibdir}/kfile_tiff.la
%{tde_tdelibdir}/kfile_tiff.so
%{tde_tdelibdir}/kfile_xbm.la
%{tde_tdelibdir}/kfile_xbm.so
%{tde_tdelibdir}/kfile_xpm.la
%{tde_tdelibdir}/kfile_xpm.so
%{tde_datadir}/services/gsthumbnail.desktop
%{tde_datadir}/services/kfile_bmp.desktop
%{tde_datadir}/services/kfile_dds.desktop
%{tde_datadir}/services/kfile_dvi.desktop
%{tde_datadir}/services/kfile_exr.desktop
%{tde_datadir}/services/kfile_gif.desktop
%{tde_datadir}/services/kfile_ico.desktop
%{tde_datadir}/services/kfile_jpeg.desktop
%{tde_datadir}/services/kfile_pcx.desktop
%{tde_datadir}/services/kfile_pdf.desktop
%{tde_datadir}/services/kfile_png.desktop
%{tde_datadir}/services/kfile_pnm.desktop
%{tde_datadir}/services/kfile_ps.desktop
%{tde_datadir}/services/kfile_raw.desktop
%{tde_datadir}/services/kfile_rgb.desktop
%{tde_datadir}/services/kfile_tga.desktop
%{tde_datadir}/services/kfile_tiff.desktop
%{tde_datadir}/services/kfile_xbm.desktop
%{tde_datadir}/services/kfile_xpm.desktop

##########

%package -n trinity-kdvi
Summary:	Dvi viewer for TDE
Group:		Applications/Graphics

%description -n trinity-kdvi
This program and KPart allow the user to display *.DVI files from TeX.

%files -n trinity-kdvi
%defattr(-,root,root,-)
%{tde_bindir}/kdvi
%{tde_tdelibdir}/kdvipart.la
%{tde_tdelibdir}/kdvipart.so
%{tde_tdeappdir}/kdvi.desktop
%{tde_datadir}/apps/kdvi/
%{tde_datadir}/config.kcfg/kdvi.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kdvi.png
%{tde_datadir}/icons/hicolor/scalable/apps/kdvi.svgz
%{tde_datadir}/services/kdvimultipage.desktop
%{tde_tdedocdir}/HTML/en/kdvi/

%post -n trinity-kdvi
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kdvi
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kfax
Summary:	G3/G4 fax viewer for Trinity
Group:		Applications/Graphics
Requires:	libtiff

%description -n trinity-kfax
A fax viewer for Trinity, supporting the display of raw and tiffed fax images
(g3, g3-2d, g4).

%files -n trinity-kfax
%defattr(-,root,root,-)
%{tde_bindir}/kfax
%{tde_tdeappdir}/kfax.desktop
%{tde_datadir}/apps/kfax/
%{tde_datadir}/icons/hicolor/??x??/apps/kfax.png
%{tde_datadir}/icons/hicolor/scalable/apps/kfax.svgz

%post -n trinity-kfax
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kfax
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kfaxview
Summary:	G3/G4 fax viewer for Trinity using kviewshell
Group:		Applications/Graphics

%description -n trinity-kfaxview
A fax viewer for Trinity, supporting the display of raw and tiffed fax images
(g3, g3-2d, g4).

This faxviewer uses kviewshell and is intended to replace the standalone
kfax application once it reproduces all of kfax's features.

%files -n trinity-kfaxview
%defattr(-,root,root,-)
%{tde_bindir}/kfaxview
%{tde_libdir}/libkfaximage.so.*
%{tde_tdelibdir}/kfaxviewpart.*
%{tde_tdeappdir}/kfaxview.desktop
%{tde_datadir}/apps/kfaxview/
%{tde_datadir}/icons/hicolor/??x??/apps/kfaxview.png
%{tde_datadir}/icons/hicolor/scalable/apps/kfaxview.svgz
%{tde_datadir}/services/kfaxmultipage.desktop
%{tde_datadir}/services/kfaxmultipage_tiff.desktop

%post -n trinity-kfaxview
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :
/sbin/ldconfig || :

%postun -n trinity-kfaxview
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :
/sbin/ldconfig || :

##########

%package -n trinity-kgamma
Summary:	Gamma correction module for the Trinity Control Center
Group:		Applications/Graphics

%description -n trinity-kgamma
KGamma is a Trinity Control Center module for gamma calibration/correction
of XFree86. With proper gamma settings, your display (websites, images,
etc.) will look the same on your monitor as on other monitors.

Homepage: http://kgamma.berlios.de/index2.php

%files -n trinity-kgamma
%defattr(-,root,root,-)
%{tde_bindir}/xf86gammacfg
%{tde_tdelibdir}/kcm_kgamma.la
%{tde_tdelibdir}/kcm_kgamma.so
%{tde_tdeappdir}/kgamma.desktop
%{tde_datadir}/apps/kgamma/
%{tde_datadir}/icons/hicolor/*/apps/kgamma.png
%{tde_tdedocdir}/HTML/en/kgamma/

%post -n trinity-kgamma
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kgamma
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kghostview
Summary:	PostScript viewer for Trinity
Group:		Applications/Graphics
Requires:	ghostscript

%description -n trinity-kghostview
KGhostview is Trinity's PostScript viewer. It is a port of Tim Theisen's
Ghostview program which is used to view documents prepared in Adobe's
PostScript page description language. PostScript is the major page
description language for printing on UNIX systems, and this application is
useful to preview material intended for printing, or for reading documents
online.

%files -n trinity-kghostview
%defattr(-,root,root,-)
%{tde_bindir}/kghostview
%{tde_tdelibdir}/libkghostviewpart.la
%{tde_tdelibdir}/libkghostviewpart.so
%{tde_libdir}/libkghostviewlib.so.*
%{tde_tdeappdir}/kghostview.desktop
%{tde_datadir}/apps/kconf_update/kghostview.upd
%{tde_datadir}/apps/kconf_update/update-to-xt-names.pl
%{tde_datadir}/apps/kghostview/
%{tde_datadir}/config.kcfg/kghostview.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kghostview.png
%{tde_datadir}/services/kghostview_part.desktop
%{tde_tdedocdir}/HTML/en/kghostview/

%post -n trinity-kghostview
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :
/sbin/ldconfig || :

%postun -n trinity-kghostview
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :
/sbin/ldconfig || :

##########

%package -n trinity-tdeiconedit
Summary:	An icon editor for Trinity
Group:		Applications/Graphics

Obsoletes:	trinity-kiconedit < %{version}-%{release}
Provides:	trinity-kiconedit = %{version}-%{release}

%description -n trinity-tdeiconedit
TDEIconedit allows you easily to create and edit icons.

%files -n trinity-tdeiconedit
%defattr(-,root,root,-)
%{tde_bindir}/kiconedit
%{tde_tdeappdir}/kiconedit.desktop
%{tde_datadir}/apps/kiconedit/
%{tde_datadir}/icons/hicolor/*/apps/kiconedit.png
%{tde_tdedocdir}/HTML/en/kiconedit/

%post -n trinity-tdeiconedit
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-tdeiconedit
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%if 0%{?build_kmrml}

%package -n trinity-kmrml
Summary: 	A Konqueror plugin for searching pictures
Group:		Applications/Graphics

%description -n trinity-kmrml
MRML is short for Multimedia Retrieval Markup Language, which defines a
protocol for querying a server for images based on their content. See 
http://www.mrml.net about MRML and the GNU Image Finding Tool (GIFT), an 
MRML server.

%files -n trinity-kmrml
%defattr(-,root,root,-)
%{tde_bindir}/mrmlsearch
%{tde_tdelibdir}/kcm_kmrml.la
%{tde_tdelibdir}/kcm_kmrml.so
%{tde_tdelibdir}/kded_daemonwatcher.la
%{tde_tdelibdir}/kded_daemonwatcher.so
%{tde_tdelibdir}/kio_mrml.la
%{tde_tdelibdir}/kio_mrml.so
%{tde_tdelibdir}/libkmrmlpart.la
%{tde_tdelibdir}/libkmrmlpart.so
%{tde_tdelibdir}/mrmlsearch.la
%{tde_tdelibdir}/mrmlsearch.so
%{tde_libdir}/libkdeinit_mrmlsearch.so
%{tde_tdeappdir}/kcmkmrml.desktop
%{tde_datadir}/apps/konqueror/servicemenus/mrml-servicemenu.desktop
%{tde_datadir}/mimelnk/text/mrml.desktop
%{tde_datadir}/services/kded/daemonwatcher.desktop
%{tde_datadir}/services/mrml.protocol
%{tde_datadir}/services/mrml_part.desktop

%post -n trinity-kmrml
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :
/sbin/ldconfig || :

%postun -n trinity-kmrml
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :
/sbin/ldconfig || :

%endif

##########

%package -n trinity-kolourpaint
Summary:	A simple paint program for Trinity
Group:		Applications/Graphics

%description -n trinity-kolourpaint
KolourPaint is a very simple paint program for Trinity. It aims to be
conceptually simple to understand; providing a level of functionality
targeted towards the average user. It's designed for daily tasks like:

* Painting - drawing diagrams and "finger painting" 
* Image Manipulation - editing screenshots and photos; applying effects 
* Icon Editing - drawing clipart and logos with transparency 

It's not an unusable and monolithic program where simple tasks like
drawing lines become near impossible. Nor is it so simple that it lacks
essential features like Undo/Redo.

Homepage: http://kolourpaint.sourceforge.net

%files -n trinity-kolourpaint
%defattr(-,root,root,-)
%{tde_bindir}/kolourpaint
%{tde_tdeappdir}/kolourpaint.desktop
%{tde_datadir}/apps/kolourpaint/
%{tde_datadir}/icons/hicolor/*/apps/kolourpaint.png
%{tde_datadir}/icons/hicolor/scalable/apps/kolourpaint.svgz
%{tde_tdedocdir}/HTML/en/kolourpaint/

%post -n trinity-kolourpaint
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kolourpaint
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kooka
Summary:	Scanner program for Trinity
Group:		Applications/Graphics

%description -n trinity-kooka
Kooka is an open source GNU/Linux scan program based on SANE and
KScan library.

Kooka helps you to handle the most important scan parameters, find the
correct image file format to save and manage your scanned images. It
offers support for different OCR modules. Libkscan, a autonomous part
of Kooka, provides a scan service for easy and consistent use to all
KDE applications.

Install ocrad or gocr if you wish to enable optical character recognition
in kooka.

Homepage: http://kooka.kde.org/

%files -n trinity-kooka
%defattr(-,root,root,-)
%{tde_datadir}/config/kookarc
%{tde_bindir}/kooka
%{tde_tdeappdir}/kooka.desktop
%{tde_datadir}/apps/kooka/
%{tde_tdedocdir}/HTML/en/kooka/

%post -n trinity-kooka
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kooka
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kpdf
Summary:	PDF viewer for Trinity
Group:		Applications/Graphics
#Recommends: kghostview-trinity (= ${binary:Version})

%description -n trinity-kpdf
KPDF allows you to view PDF (Portable Document Format) files. This package
includes kpdfpart so you can embed in konqueror or run as a standalone
application.

%files -n trinity-kpdf
%defattr(-,root,root,-)
%{tde_bindir}/kpdf
%{tde_tdelibdir}/libkpdfpart.la
%{tde_tdelibdir}/libkpdfpart.so
%{tde_tdeappdir}/kpdf.desktop
%{tde_datadir}/apps/kpdf/shell.rc
%{tde_datadir}/apps/kpdfpart/part.rc
%{tde_datadir}/config.kcfg/kpdf.kcfg
%{tde_tdedocdir}/HTML/en/kpdf/
%{tde_datadir}/icons/hicolor/*/apps/kpdf.png
%{tde_datadir}/icons/hicolor/scalable/apps/kpdf.svgz
%{tde_datadir}/services/kpdf_part.desktop

%post -n trinity-kpdf
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kpdf
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kpovmodeler
Summary:	A graphical editor for povray scenes
Group:		Applications/Graphics
#Requires:	povray

%description -n trinity-kpovmodeler
KPovmodeler is KDE's graphical editor for povray scenes. KPovModeler is a
modeling and composition program for creating POV-Ray scenes in KDE.

For most modelers, POV-Ray is nothing but a rendering engine. This greatly
limits the innate possibilities of the POV-Ray scripted language. This
is not the case for KPovModeler, which allows you to use all the features
of POV-Ray through the translation of POV-Ray language into a graphical
tree.

kpovmodeler uses the povray package, currently available only in Debian's
non-free, unsupported repository.

Homepage: http://www.kpovmodeler.org

%files -n trinity-kpovmodeler
%defattr(-,root,root,-)
%{tde_bindir}/kpovmodeler
%{tde_libdir}/libkpovmodeler.so.*
%{tde_tdelibdir}/libkpovmodelerpart.*
%{tde_tdeappdir}/kpovmodeler.desktop
%{tde_datadir}/apps/kpovmodeler/
%{tde_datadir}/icons/crystalsvg/*/mimetypes/kpovmodeler_doc.*
%{tde_datadir}/icons/hicolor/*/apps/kpovmodeler.*
%doc %{tde_tdedocdir}/HTML/en/kpovmodeler/

%post -n trinity-kpovmodeler
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :
/sbin/ldconfig || :

%postun -n trinity-kpovmodeler
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :
/sbin/ldconfig || :

##########

%package -n trinity-kruler
Summary:	A screen ruler and color measurement tool for Trinity
Group:		Applications/Graphics

%description -n trinity-kruler
Kruler is a screen ruler (using pixels) and color measurement tool for KDE.

%files -n trinity-kruler
%defattr(-,root,root,-)
%{tde_bindir}/kruler
%{tde_tdeappdir}/kruler.desktop
%{tde_datadir}/applnk/Graphics/kruler.desktop
%{tde_datadir}/apps/kruler/
%{tde_datadir}/icons/hicolor/*/apps/kruler.png
%{tde_tdedocdir}/HTML/en/kruler/

%post -n trinity-kruler
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kruler
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-ksnapshot
Summary:	Screenshot utility for Trinity
Group:		Applications/Graphics

%description -n trinity-ksnapshot
KSnapshot is a simple applet for taking screenshots. It is capable of 
capturing images of either the whole desktop or just a single window. 
The images can then be saved in a variety of formats.

%files -n trinity-ksnapshot
%defattr(-,root,root,-)
%{tde_bindir}/ksnapshot
%{tde_tdeappdir}/ksnapshot.desktop
%{tde_datadir}/icons/hicolor/*/apps/ksnapshot.png
%{tde_datadir}/icons/hicolor/scalable/apps/ksnapshot.svgz
%{tde_tdedocdir}/HTML/en/ksnapshot/

%post -n trinity-ksnapshot
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-ksnapshot
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-ksvg
Summary:	SVG viewer for Trinity
Group:		Applications/Graphics

%description -n trinity-ksvg
KSVG allows you view SVG (scalable vector graphics) files. This package
includes kpart so you can embed it in konqueror and a standalone
application.

%files -n trinity-ksvg
%defattr(-,root,root,-)
%{tde_bindir}/printnodetest
%{tde_bindir}/svgdisplay
%{tde_tdelibdir}/libksvgplugin.la
%{tde_tdelibdir}/libksvgplugin.so
%{tde_tdelibdir}/libksvgrendererlibart.la
%{tde_tdelibdir}/libksvgrendererlibart.so
%{tde_tdelibdir}/svgthumbnail.la
%{tde_tdelibdir}/svgthumbnail.so
%{tde_libdir}/libksvg.so.0
%{tde_libdir}/libksvg.so.0.0.1
%{tde_libdir}/libtext2path.so.0
%{tde_libdir}/libtext2path.so.0.0.0
%{tde_datadir}/apps/ksvg/ksvgplugin.rc
%{tde_datadir}/services/ksvglibartcanvas.desktop
%{tde_datadir}/services/ksvgplugin.desktop
%{tde_datadir}/services/svgthumbnail.desktop
%{tde_datadir}/servicetypes/ksvgrenderer.desktop

%post -n trinity-ksvg
/sbin/ldconfig || :

%postun -n trinity-ksvg
/sbin/ldconfig || :

##########

%package -n trinity-kview
Summary:	Simple image viewer/converter for Trinity
Group:		Applications/Graphics

%description -n trinity-kview
KView is a simple image viewer and converter application. It supports
a number of plugins, which add an array of basic editing capabilities
as well.

%files -n trinity-kview
%defattr(-,root,root,-)
%{tde_bindir}/kview
%{tde_tdelibdir}/kcm_kviewcanvasconfig.la
%{tde_tdelibdir}/kcm_kviewcanvasconfig.so
%{tde_tdelibdir}/kcm_kviewgeneralconfig.la
%{tde_tdelibdir}/kcm_kviewgeneralconfig.so
%{tde_tdelibdir}/kcm_kviewpluginsconfig.la
%{tde_tdelibdir}/kcm_kviewpluginsconfig.so
%{tde_tdelibdir}/kcm_kviewpresenterconfig.la
%{tde_tdelibdir}/kcm_kviewpresenterconfig.so
%{tde_tdelibdir}/kcm_kviewviewerpluginsconfig.la
%{tde_tdelibdir}/kcm_kviewviewerpluginsconfig.so
%{tde_tdelibdir}/kview.la
%{tde_tdelibdir}/kview.so
%{tde_tdelibdir}/kview_browserplugin.la
%{tde_tdelibdir}/kview_browserplugin.so
%{tde_tdelibdir}/kview_effectsplugin.la
%{tde_tdelibdir}/kview_effectsplugin.so
%{tde_tdelibdir}/kview_presenterplugin.la
%{tde_tdelibdir}/kview_presenterplugin.so
%{tde_tdelibdir}/kview_scannerplugin.la
%{tde_tdelibdir}/kview_scannerplugin.so
%{tde_tdelibdir}/libkviewcanvas.la
%{tde_tdelibdir}/libkviewcanvas.so
%{tde_tdelibdir}/libkviewviewer.la
%{tde_tdelibdir}/libkviewviewer.so
%{tde_libdir}/libkdeinit_kview.so
%{tde_libdir}/libkimageviewer.so.*
%{tde_tdelibdir}/libphotobook.la
%{tde_tdelibdir}/libphotobook.so
%{tde_tdeappdir}/kview.desktop
%{tde_datadir}/apps/kview/
%{tde_datadir}/apps/kviewviewer/
%{tde_datadir}/apps/photobook/photobookui.rc
%{tde_datadir}/icons/crystalsvg/*/apps/photobook.png
%{tde_datadir}/icons/hicolor/*/apps/kview.png
%{tde_datadir}/services/kconfiguredialog/kviewcanvasconfig.desktop
%{tde_datadir}/services/kconfiguredialog/kviewgeneralconfig.desktop
%{tde_datadir}/services/kconfiguredialog/kviewpluginsconfig.desktop
%{tde_datadir}/services/kconfiguredialog/kviewpresenterconfig.desktop
%{tde_datadir}/services/kconfiguredialog/kviewviewerpluginsconfig.desktop
%{tde_datadir}/services/kviewcanvas.desktop
%{tde_datadir}/services/kviewviewer.desktop
%{tde_datadir}/services/photobook.desktop
%{tde_datadir}/servicetypes/kimageviewer.desktop
%{tde_datadir}/servicetypes/kimageviewercanvas.desktop
%{tde_tdedocdir}/HTML/en/kview/

%post -n trinity-kview
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :
/sbin/ldconfig || :

%postun -n trinity-kview
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :
/sbin/ldconfig || :

##########

%package -n trinity-kviewshell
Summary:	Generic framework for viewer applications in Trinity
Group:		Applications/Graphics

%description -n trinity-kviewshell
KViewShell is a generic viewing framework that allows the graphical
applications, such as the kview image viewer, to be embedded in other
KDE applications, such as Konqueror.

KViewShell comes with a djvuviewpart plugin included, for viewing
DjVu images.

%files -n trinity-kviewshell
%defattr(-,root,root,-)
%{tde_bindir}/kviewshell
%{tde_libdir}/libdjvu.la
%{tde_libdir}/libdjvu.so
%{tde_tdelibdir}/djvuviewpart.so
%{tde_tdelibdir}/djvuviewpart.la
%{tde_tdelibdir}/emptymultipagepart.la
%{tde_tdelibdir}/emptymultipagepart.so
%{tde_tdelibdir}/kviewerpart.la
%{tde_tdelibdir}/kviewerpart.so
%{tde_libdir}/libkmultipage.so.*
%{tde_datadir}/apps/djvumultipage.rc
%{tde_datadir}/apps/kviewerpart/
%{tde_datadir}/apps/kviewshell/kviewshell.rc
%{tde_datadir}/config.kcfg/djvumultipage.kcfg
%{tde_datadir}/config.kcfg/kviewshell.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/kviewshell.png
%{tde_datadir}/services/emptymultipage.desktop
%{tde_datadir}/services/djvumultipage.desktop
%{tde_datadir}/servicetypes/kmultipage.desktop

%post -n trinity-kviewshell
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig || :

%postun -n trinity-kviewshell
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig || :

##########

%package -n trinity-libkscan
Summary:	Scanner library for Trinity
Group:		Environment/Libraries

%description -n trinity-libkscan
KScan is TDE's scanner library. It's used by kooka and by koffice currently.
It provides an easy-to-use library, which allows you to access your scanner
(as long as it's sane compatible).

%files -n trinity-libkscan
%defattr(-,root,root,-)
%{tde_libdir}/libkscan.so.*
%{tde_datadir}/icons/crystalsvg/16x16/actions/palette_color.png
%{tde_datadir}/icons/crystalsvg/16x16/actions/palette_gray.png
%{tde_datadir}/icons/crystalsvg/16x16/actions/palette_halftone.png
%{tde_datadir}/icons/crystalsvg/16x16/actions/palette_lineart.png
%{tde_datadir}/services/scanservice.desktop

%post -n trinity-libkscan
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig || :

%postun -n trinity-libkscan
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig || :

##########

%package -n trinity-libkscan-devel
Summary:	Development files for the Trinity scanner library
Group:		Development/Libraries

%description -n trinity-libkscan-devel
This package contains development files for Trinity's scanner library.

%files -n trinity-libkscan-devel
%defattr(-,root,root,-)
%{tde_libdir}/libkscan.la
%{tde_libdir}/libkscan.so

%post -n trinity-libkscan-devel
/sbin/ldconfig || :

%postun -n trinity-libkscan-devel
/sbin/ldconfig || :

##########

%package -n trinity-libpoppler-tqt
Summary:	TQt support for Poppler
Group:		Environment/Libraries
Obsoletes:	poppler-tqt < %{version}-%{release}
Provides:	poppler-tqt = %{version}-%{release}
Obsoletes:	%{name}-libpoppler-tqt < %{version}-%{release}
Provides:	%{name}-libpoppler-tqt = %{version}-%{release}

%description -n trinity-libpoppler-tqt
TQt support library for Poppler.
This library is used by the Trinity graphics file plugins for PDF support.

%files -n trinity-libpoppler-tqt
%defattr(-,root,root,-)
%{tde_libdir}/libpoppler-tqt.so.*

%post -n trinity-libpoppler-tqt
/sbin/ldconfig || :

%postun -n trinity-libpoppler-tqt
/sbin/ldconfig || :

##########

%package -n trinity-libpoppler-tqt-devel
Summary:	Development files for TQt support for Poppler
Group:		Development/Libraries
Requires:	trinity-libpoppler-tqt = %{version}-%{release}
Obsoletes:	poppler-tqt-devel < %{version}-%{release}
Provides:	poppler-tqt-devel = %{version}-%{release}
Obsoletes:	%{name}-libpoppler-tqt-devel < %{version}-%{release}
Provides:	%{name}-libpoppler-tqt-devel = %{version}-%{release}

%description -n trinity-libpoppler-tqt-devel
Development files of TQt support library for Poppler.
This package contains the development files needed to compile applications against poppler-tqt.

%files -n trinity-libpoppler-tqt-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/poppler-link-qt3.h
%{tde_tdeincludedir}/poppler-page-transition.h
%{tde_tdeincludedir}/poppler-qt.h
%{tde_libdir}/libpoppler-tqt.la
%{tde_libdir}/libpoppler-tqt.so
%{tde_libdir}/pkgconfig/poppler-tqt.pc

%post -n trinity-libpoppler-tqt-devel
/sbin/ldconfig || :

%postun -n trinity-libpoppler-tqt-devel
/sbin/ldconfig || :

##########

%package devel
Summary:	Development files for %{name} 
Group:		Development/Libraries

Obsoletes:	trinity-kdegraphics-devel < %{version}-%{release}
Provides:	trinity-kdegraphics-devel = %{version}-%{release}

Requires: %{name} = %{version}-%{release}
Requires: trinity-libkscan-devel = %{version}-%{release}
Requires: trinity-libpoppler-tqt-devel = %{version}-%{release}

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/dom/
%{tde_tdeincludedir}/kfaximage.h
%{tde_tdeincludedir}/kmultipageInterface.h
%{tde_tdeincludedir}/ksvg/
%{tde_tdeincludedir}/kviewshell/
%{tde_tdeincludedir}/libtext2path-0.1/BezierPath.h
%{tde_tdeincludedir}/libtext2path-0.1/Glyph.h
%{tde_tdeincludedir}/libtext2path-0.1/GlyphTracer.h
%{tde_libdir}/libkdeinit_kview.la
%if 0%{?build_kmrml}
%{tde_libdir}/libkdeinit_mrmlsearch.la
%endif
%{tde_libdir}/libkghostviewlib.la
%{tde_libdir}/libkghostviewlib.so
%{tde_libdir}/libkimageviewer.la
%{tde_libdir}/libkimageviewer.so
%{tde_libdir}/libkmultipage.la
%{tde_libdir}/libkmultipage.so
%{tde_libdir}/libkpovmodeler.la
%{tde_libdir}/libkpovmodeler.so
%{tde_libdir}/libksvg.la
%{tde_libdir}/libksvg.so
%{tde_libdir}/libtext2path.la
%{tde_libdir}/libtext2path.so
# kfaxview
%{tde_libdir}/libkfaximage.so
%{tde_libdir}/libkfaximage.la
# cmake
%{tde_datadir}/cmake/*

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

############

# Excludes kuickshow (built separately)
#%exclude %{tde_bindir}/kuickshow
#%exclude %{tde_tdelibdir}/kuickshow.la
#%exclude %{tde_tdelibdir}/kuickshow.so
#%exclude %{tde_libdir}/libkdeinit_kuickshow.la
#%exclude %{tde_libdir}/libkdeinit_kuickshow.so
#%exclude %{tde_tdeappdir}/kuickshow.desktop
#%exclude %{tde_datadir}/apps/kuickshow/
#%exclude %{tde_datadir}/icons/hicolor/*/apps/kuickshow.png
#%exclude %{tde_tdedocdir}/HTML/en/kuickshow/

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}

%if 0%{?rhel} && 0%{?rhel} <= 5
%patch3 -p1 -b .mkstemps
%endif

%if 0%{?rhel} == 4
%patch201 -p1 -b .rhel4
%endif

%if 0%{?build_kamera} == 0
%__rm -rf doc/kamera/
%endif

%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

# Do not build against any "/usr" installed KDE
export KDEDIR=%{tde_prefix}

# Specific path for RHEL4
if [ -d /usr/X11R6 ]; then
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

if ! rpm -E %%cmake|grep -q "cd build"; then
  %__mkdir_p build
  cd build
fi

# Note: the "-L%{tde_libdir}" is required for RHEL5, where poppler is under /opt/trinity.
%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG -L%{tde_libdir} -I%{tde_includedir}" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  \
  %{?with_t1lib:-DWITH_T1LIB=ON} \
  %{?with_paper:-DWITH_LIBPAPER=ON} \
  -DWITH_TIFF=ON \
  -DWITH_OPENEXR=ON \
  -DWITH_PDF=ON \
  -DBUILD_ALL=ON \
  -DBUILD_KUICKSHOW=OFF \
  %{!?build_kmrml:-DBUILD_KMRML=OFF} \
  %{!?build_kamera:-DBUILD_KAMERA=OFF} \
  ..

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build



%clean
%__rm -rf %{buildroot}


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-3
- Build for Fedora 19

* Sun Jul 28 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-2
- Rebuild with NDEBUG option

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2
