# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
%define tde_appdir %{_datadir}/applications/kde
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-tdegraphics
Version:	3.5.13
Release:	5%{?dist}%{_variant}
License:	GPL
Summary:    Trinity Desktop Environment - Graphics Applications

Group:      Applications/Multimedia
Prefix:		%{_prefix}

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kdegraphics-%{version}.tar.gz

# TDE 3.5.13
## RHEL / Fedora specific patches
# [kdegraphics/ksnapshot] Missing -lXext in LDFLAGS (required for Fedora 15)
Patch0:		kdegraphics-3.5.13-ksnapshot_ldflags.patch
# [kdegraphics/kpovmodeler] CMAKE does not detect GL/glu.h (on RHEL5)
Patch1:		kdegraphics-3.5.13-kpovmodeler_check_glu.patch
# [kdegraphics/kfile-plugins/dependencies/poppler-tqt] Compile 'poppler-tqt' only if HAVE_POPPLER_016
Patch2:		kdegraphics-3.5.13-disable_poppler.patch
# [kdegraphics/kpdf/xpdf] Disable 'mkstemps' support for RHEL5
Patch3:		kdegraphics-3.5.13-xpdf_disable_mkstemps.patch
# [kdegraphics/kpovmodeler] CMAKE missing GLU_LIBRARIES
Patch4:		kdegraphics-3.5.13-kpovmodeler_missing_gl_ldflags.patch
# [kdegraphics] Fix compilation with GCC 4.7
Patch5:		kdegraphics-3.5.13-fix_gcc47_compilation.patch
# [kdegraphics] Fix FTBFS due to poppler-tqt
Patch6:		kdegraphics-3.5.13-fix_poppler_support.patch
# [tdegraphics] Fix corrupt image file. [Commit #d655a9f8]
Patch7:		kdegraphics-3.5.13-fix_corrupt_image_file.patch

BuildRequires: cmake >= 2.8
BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: gettext
BuildRequires: libmng-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libungif-devel
BuildRequires: automake libtool
BuildRequires: gphoto2-devel
BuildRequires: sane-backends-devel
BuildRequires: libusb-devel
BuildRequires: t1lib-devel
BuildRequires: libdrm-devel

# kgamma
BuildRequires: libXxf86vm-devel
#kfile-plugin
BuildRequires: OpenEXR-devel
# kpdf
BuildRequires: freetype-devel
%if 0%{?rhel} >=6 || 0%{?fedora} >= 15
BuildRequires: poppler-devel >= 0.12
BuildRequires: poppler-qt-devel >= 0.12
%else
BuildRequires: trinity-poppler-devel
BuildRequires: trinity-poppler-qt3-devel >= 0.12
%endif

BuildRequires: libpaper-devel
# ksvg
BuildRequires: fontconfig-devel
BuildRequires: lcms-devel
BuildRequires: libart_lgpl-devel
BuildRequires: libXmu-devel

# kpovmodeler
BuildRequires: libGL-devel libGLU-devel libXi-devel

# kuickshow
BuildRequires: imlib-devel
BuildRequires: fribidi-devel

#Requires: tqtinterface
#Requires: trinity-arts
#Requires: trinity-kdelibs


Obsoletes:	trinity-kdegraphics < %{version}-%{release}
Provides:	trinity-kdegraphics = %{version}-%{release}
Obsoletes:	trinity-kdegraphics-libs < %{version}-%{release}
Provides:	trinity-kdegraphics-libs = %{version}-%{release}
Obsoletes:	trinity-kdegraphics-extras < %{version}-%{release}
Provides:	trinity-kdegraphics-extras = %{version}-%{release}


Requires: trinity-kamera = %{version}-%{release}
Requires: trinity-kcoloredit = %{version}-%{release}
Requires: %{name}-kfile-plugins = %{version}-%{release}
Requires: trinity-kdvi = %{version}-%{release}
Requires: trinity-kfax = %{version}-%{release}
Requires: trinity-kfaxview = %{version}-%{release}
Requires: trinity-kgamma = %{version}-%{release}
Requires: trinity-kghostview = %{version}-%{release}
Requires: trinity-kiconedit = %{version}-%{release}
Requires: trinity-kmrml = %{version}-%{release}
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
Requires: %{name}-libpoppler-tqt = %{version}-%{release}

%description
Graphics applications for the Trinity Desktop Environment, including
* kamera (digital camera support)
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

##########

%package -n trinity-kamera
Summary:	Digital camera io_slave for Konqueror
Group:		Applications/Graphics

%description -n trinity-kamera
This is a digital camera io_slave for TDE which uses gphoto2 and libgpio
to allow access to your camera's pictures with the URL camera:/

%post -n trinity-kamera
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kamera
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%files -n trinity-kamera
%defattr(-,root,root,-)
%{tde_libdir}/kcm_kamera.la
%{tde_libdir}/kcm_kamera.so
%{tde_libdir}/kio_kamera.la
%{tde_libdir}/kio_kamera.so
%{tde_appdir}/kamera.desktop
%{_datadir}/icons/crystalsvg/*/actions/camera_test.png
%{_datadir}/icons/crystalsvg/*/apps/camera.png
%{_datadir}/icons/crystalsvg/*/devices/camera.png
%{_datadir}/icons/crystalsvg/*/filesystems/camera.png
%{_datadir}/services/camera.protocol
%{tde_docdir}/HTML/en/kamera/

##########

%package -n trinity-kcoloredit
Summary:	A color palette editor and color picker for TDE
Group:		Applications/Graphics

%description -n trinity-kcoloredit
This package contains two programs, a color palette editor and also a color
picker.

%files -n trinity-kcoloredit
%defattr(-,root,root,-)
%{_bindir}/kcolorchooser
%{_bindir}/kcoloredit
%{tde_appdir}/kcolorchooser.desktop
%{tde_appdir}/kcoloredit.desktop
%{_datadir}/apps/kcoloredit/kcoloreditui.rc
%{_datadir}/icons/hicolor/*/apps/kcolorchooser.png
%{_datadir}/icons/hicolor/*/apps/kcoloredit.png
%{tde_docdir}/HTML/en/kcoloredit/

##########

%package kfile-plugins
Summary:	TDE metainfo plugins for graphic files
Group:		Environment/Libraries
 
%description kfile-plugins
This packages provides meta information for graphic files (file sizes,
tags, etc. all from within the file manager).

%files kfile-plugins
%defattr(-,root,root,-)
%{tde_libdir}/gsthumbnail.la
%{tde_libdir}/gsthumbnail.so
%{tde_libdir}/kfile_bmp.la
%{tde_libdir}/kfile_bmp.so
%{tde_libdir}/kfile_dds.la
%{tde_libdir}/kfile_dds.so
%{tde_libdir}/kfile_dvi.la
%{tde_libdir}/kfile_dvi.so
%{tde_libdir}/kfile_exr.la
%{tde_libdir}/kfile_exr.so
%{tde_libdir}/kfile_gif.la
%{tde_libdir}/kfile_gif.so
%{tde_libdir}/kfile_ico.la
%{tde_libdir}/kfile_ico.so
%{tde_libdir}/kfile_jpeg.la
%{tde_libdir}/kfile_jpeg.so
%{tde_libdir}/kfile_pcx.la
%{tde_libdir}/kfile_pcx.so
%{tde_libdir}/kfile_pdf.la
%{tde_libdir}/kfile_pdf.so
%{tde_libdir}/kfile_png.la
%{tde_libdir}/kfile_png.so
%{tde_libdir}/kfile_pnm.la
%{tde_libdir}/kfile_pnm.so
%{tde_libdir}/kfile_ps.la
%{tde_libdir}/kfile_ps.so
%{tde_libdir}/kfile_raw.la
%{tde_libdir}/kfile_raw.so
%{tde_libdir}/kfile_rgb.la
%{tde_libdir}/kfile_rgb.so
%{tde_libdir}/kfile_tga.la
%{tde_libdir}/kfile_tga.so
%{tde_libdir}/kfile_tiff.la
%{tde_libdir}/kfile_tiff.so
%{tde_libdir}/kfile_xbm.la
%{tde_libdir}/kfile_xbm.so
%{tde_libdir}/kfile_xpm.la
%{tde_libdir}/kfile_xpm.so
%{_datadir}/services/gsthumbnail.desktop
%{_datadir}/services/kfile_bmp.desktop
%{_datadir}/services/kfile_dds.desktop
%{_datadir}/services/kfile_dvi.desktop
%{_datadir}/services/kfile_exr.desktop
%{_datadir}/services/kfile_gif.desktop
%{_datadir}/services/kfile_ico.desktop
%{_datadir}/services/kfile_jpeg.desktop
%{_datadir}/services/kfile_pcx.desktop
%{_datadir}/services/kfile_pdf.desktop
%{_datadir}/services/kfile_png.desktop
%{_datadir}/services/kfile_pnm.desktop
%{_datadir}/services/kfile_ps.desktop
%{_datadir}/services/kfile_raw.desktop
%{_datadir}/services/kfile_rgb.desktop
%{_datadir}/services/kfile_tga.desktop
%{_datadir}/services/kfile_tiff.desktop
%{_datadir}/services/kfile_xbm.desktop
%{_datadir}/services/kfile_xpm.desktop

##########

%package -n trinity-kdvi
Summary:	Dvi viewer for TDE
Group:		Applications/Graphics

%description -n trinity-kdvi
This program and KPart allow the user to display *.DVI files from TeX.

%files -n trinity-kdvi
%defattr(-,root,root,-)
%{_bindir}/kdvi
%{tde_libdir}/kdvipart.la
%{tde_libdir}/kdvipart.so
%{tde_appdir}/kdvi.desktop
%{_datadir}/apps/kdvi/
%{_datadir}/config.kcfg/kdvi.kcfg
%{_datadir}/icons/hicolor/*/apps/kdvi.png
%{_datadir}/icons/hicolor/scalable/apps/kdvi.svgz
%{_datadir}/services/kdvimultipage.desktop
%{tde_docdir}/HTML/en/kdvi/

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
%doc rpmdocs/kfax/
%{_bindir}/kfax
%{tde_appdir}/kfax.desktop
%{_datadir}/apps/kfax/
%{_datadir}/icons/hicolor/??x??/apps/kfax.png
%{_datadir}/icons/hicolor/scalable/apps/kfax.svgz

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
%{_bindir}/kfaxview
%{_libdir}/libkfaximage.so.*
%{_libdir}/libkfaximage.so
%{_libdir}/libkfaximage.la
%{tde_libdir}/kfaxviewpart.*
%{tde_appdir}/kfaxview.desktop
%{_datadir}/apps/kfaxview/
%{_datadir}/icons/hicolor/??x??/apps/kfaxview.png
%{_datadir}/icons/hicolor/scalable/apps/kfaxview.svgz
%{_datadir}/services/kfaxmultipage.desktop
%{_datadir}/services/kfaxmultipage_tiff.desktop

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
%{_bindir}/xf86gammacfg
%{tde_libdir}/kcm_kgamma.la
%{tde_libdir}/kcm_kgamma.so
%{tde_appdir}/kgamma.desktop
%{_datadir}/apps/kgamma/
%{_datadir}/icons/hicolor/*/apps/kgamma.png
%{tde_docdir}/HTML/en/kgamma/

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
%{_bindir}/kghostview
%{tde_libdir}/libkghostviewpart.la
%{tde_libdir}/libkghostviewpart.so
%{_libdir}/libkghostviewlib.so.*
%{tde_appdir}/kghostview.desktop
%{_datadir}/apps/kconf_update/kghostview.upd
%{_datadir}/apps/kconf_update/update-to-xt-names.pl
%{_datadir}/apps/kghostview/
%{_datadir}/config.kcfg/kghostview.kcfg
%{_datadir}/icons/hicolor/*/apps/kghostview.png
%{_datadir}/services/kghostview_part.desktop
%{tde_docdir}/HTML/en/kghostview/

##########

%package -n trinity-kiconedit
Summary:	An icon editor for Trinity
Group:		Applications/Graphics

%description -n trinity-kiconedit
KIconedit allows you easily to create and edit icons.

%files -n trinity-kiconedit
%defattr(-,root,root,-)
%{_bindir}/kiconedit
%{tde_appdir}/kiconedit.desktop
%{_datadir}/apps/kiconedit/
%{_datadir}/icons/hicolor/*/apps/kiconedit.png
%{tde_docdir}/HTML/en/kiconedit/

##########

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
%{_bindir}/mrmlsearch
%{tde_libdir}/kcm_kmrml.la
%{tde_libdir}/kcm_kmrml.so
%{tde_libdir}/kded_daemonwatcher.la
%{tde_libdir}/kded_daemonwatcher.so
%{tde_libdir}/kio_mrml.la
%{tde_libdir}/kio_mrml.so
%{tde_libdir}/libkmrmlpart.la
%{tde_libdir}/libkmrmlpart.so
%{tde_libdir}/mrmlsearch.la
%{tde_libdir}/mrmlsearch.so
%{_libdir}/lib[kt]deinit_mrmlsearch.so
%{tde_appdir}/kcmkmrml.desktop
%{_datadir}/apps/konqueror/servicemenus/mrml-servicemenu.desktop
%{_datadir}/mimelnk/text/mrml.desktop
%{_datadir}/services/kded/daemonwatcher.desktop
%{_datadir}/services/mrml.protocol
%{_datadir}/services/mrml_part.desktop

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
%{_bindir}/kolourpaint
%{tde_appdir}/kolourpaint.desktop
%{_datadir}/apps/kolourpaint/
%{_datadir}/icons/hicolor/*/apps/kolourpaint.png
%{_datadir}/icons/hicolor/scalable/apps/kolourpaint.svgz
%{tde_docdir}/HTML/en/kolourpaint/

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
%{_datadir}/config/kookarc
%{_bindir}/kooka
%{tde_appdir}/kooka.desktop
%{_datadir}/apps/kooka/
%{tde_docdir}/HTML/en/kooka/

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
%{_bindir}/kpdf
%{tde_libdir}/libkpdfpart.la
%{tde_libdir}/libkpdfpart.so
%{tde_appdir}/kpdf.desktop
%{_datadir}/apps/kpdf/shell.rc
%{_datadir}/apps/kpdfpart/part.rc
%{_datadir}/config.kcfg/kpdf.kcfg
%{tde_docdir}/HTML/en/kpdf/
%{_datadir}/icons/hicolor/*/apps/kpdf.png
%{_datadir}/icons/hicolor/scalable/apps/kpdf.svgz
%{_datadir}/services/kpdf_part.desktop

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
%doc rpmdocs/kpovmodeler/
%{_bindir}/kpovmodeler
%{_libdir}/libkpovmodeler.so.*
%{_libdir}/libkpovmodeler.la
%{tde_libdir}/libkpovmodelerpart.*
%{tde_appdir}/kpovmodeler.desktop
%{_datadir}/apps/kpovmodeler/
%{_datadir}/icons/crystalsvg/*/mimetypes/kpovmodeler_doc.*
%{_datadir}/icons/hicolor/*/apps/kpovmodeler.*
%doc %{tde_docdir}/HTML/en/kpovmodeler/

##########

%package -n trinity-kruler
Summary:	A screen ruler and color measurement tool for Trinity
Group:		Applications/Graphics

%description -n trinity-kruler
Kruler is a screen ruler (using pixels) and color measurement tool for KDE.

%files -n trinity-kruler
%defattr(-,root,root,-)
%{_bindir}/kruler
%{tde_appdir}/kruler.desktop
%{_datadir}/applnk/Graphics/kruler.desktop
%{_datadir}/apps/kruler/
%{_datadir}/icons/hicolor/*/apps/kruler.png
%{tde_docdir}/HTML/en/kruler/

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
%{_bindir}/ksnapshot
%{tde_appdir}/ksnapshot.desktop
%{tde_docdir}/HTML/en/ksnapshot/
%{_datadir}/icons/hicolor/*/apps/ksnapshot.png
%{_datadir}/icons/hicolor/scalable/apps/ksnapshot.svgz

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
%{_bindir}/printnodetest
%{_bindir}/svgdisplay
%{tde_libdir}/libksvgplugin.la
%{tde_libdir}/libksvgplugin.so
%{tde_libdir}/libksvgrendererlibart.la
%{tde_libdir}/libksvgrendererlibart.so
%{tde_libdir}/svgthumbnail.la
%{tde_libdir}/svgthumbnail.so
%{_libdir}/libksvg.so.0
%{_libdir}/libksvg.so.0.0.1
%{_libdir}/libtext2path.so.0
%{_libdir}/libtext2path.so.0.0.0
%{_datadir}/apps/ksvg/ksvgplugin.rc
%{_datadir}/services/ksvglibartcanvas.desktop
%{_datadir}/services/ksvgplugin.desktop
%{_datadir}/services/svgthumbnail.desktop
%{_datadir}/servicetypes/ksvgrenderer.desktop

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
%{_bindir}/kview
%{tde_libdir}/kcm_kviewcanvasconfig.la
%{tde_libdir}/kcm_kviewcanvasconfig.so
%{tde_libdir}/kcm_kviewgeneralconfig.la
%{tde_libdir}/kcm_kviewgeneralconfig.so
%{tde_libdir}/kcm_kviewpluginsconfig.la
%{tde_libdir}/kcm_kviewpluginsconfig.so
%{tde_libdir}/kcm_kviewpresenterconfig.la
%{tde_libdir}/kcm_kviewpresenterconfig.so
%{tde_libdir}/kcm_kviewviewerpluginsconfig.la
%{tde_libdir}/kcm_kviewviewerpluginsconfig.so
%{tde_libdir}/kview.la
%{tde_libdir}/kview.so
%{tde_libdir}/kview_browserplugin.la
%{tde_libdir}/kview_browserplugin.so
%{tde_libdir}/kview_effectsplugin.la
%{tde_libdir}/kview_effectsplugin.so
%{tde_libdir}/kview_presenterplugin.la
%{tde_libdir}/kview_presenterplugin.so
%{tde_libdir}/kview_scannerplugin.la
%{tde_libdir}/kview_scannerplugin.so
%{tde_libdir}/libkviewcanvas.la
%{tde_libdir}/libkviewcanvas.so
%{tde_libdir}/libkviewviewer.la
%{tde_libdir}/libkviewviewer.so
%{_libdir}/lib[kt]deinit_kview.so
%{_libdir}/libkimageviewer.so.*
%{tde_libdir}/libphotobook.la
%{tde_libdir}/libphotobook.so
%{tde_appdir}/kview.desktop
%{_datadir}/apps/kview/
%{_datadir}/apps/kviewviewer/
%{_datadir}/apps/photobook/photobookui.rc
%{_datadir}/icons/crystalsvg/*/apps/photobook.png
%{_datadir}/icons/hicolor/*/apps/kview.png
%{_datadir}/services/kconfiguredialog/kviewcanvasconfig.desktop
%{_datadir}/services/kconfiguredialog/kviewgeneralconfig.desktop
%{_datadir}/services/kconfiguredialog/kviewpluginsconfig.desktop
%{_datadir}/services/kconfiguredialog/kviewpresenterconfig.desktop
%{_datadir}/services/kconfiguredialog/kviewviewerpluginsconfig.desktop
%{_datadir}/services/kviewcanvas.desktop
%{_datadir}/services/kviewviewer.desktop
%{_datadir}/services/photobook.desktop
%{_datadir}/servicetypes/kimageviewer.desktop
%{_datadir}/servicetypes/kimageviewercanvas.desktop
%{tde_docdir}/HTML/en/kview/

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
%{_bindir}/kviewshell
%{_libdir}/libdjvu.la
%{_libdir}/libdjvu.so
%{tde_libdir}/djvuviewpart.so
%{tde_libdir}/djvuviewpart.la
%{tde_libdir}/emptymultipagepart.la
%{tde_libdir}/emptymultipagepart.so
%{tde_libdir}/kviewerpart.la
%{tde_libdir}/kviewerpart.so
%{_libdir}/libkmultipage.so.*
%{_datadir}/apps/djvumultipage.rc
%{_datadir}/apps/kviewerpart/
%{_datadir}/apps/kviewshell/kviewshell.rc
%{_datadir}/config.kcfg/djvumultipage.kcfg
%{_datadir}/config.kcfg/kviewshell.kcfg
%{_datadir}/icons/crystalsvg/*/apps/kviewshell.png
%{_datadir}/services/emptymultipage.desktop
%{_datadir}/services/djvumultipage.desktop
%{_datadir}/servicetypes/kmultipage.desktop

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
%{_libdir}/libkscan.so.*
%{_datadir}/icons/crystalsvg/16x16/actions/palette_color.png
%{_datadir}/icons/crystalsvg/16x16/actions/palette_gray.png
%{_datadir}/icons/crystalsvg/16x16/actions/palette_halftone.png
%{_datadir}/icons/crystalsvg/16x16/actions/palette_lineart.png
%{_datadir}/services/scanservice.desktop

##########

%package -n trinity-libkscan-devel
Summary:	Development files for the Trinity scanner library
Group:		Development/Libraries

%description -n trinity-libkscan-devel
This package contains development files for Trinity's scanner library.

%files -n trinity-libkscan-devel
%defattr(-,root,root,-)
%{_libdir}/libkscan.la
%{_libdir}/libkscan.so

##########

%package libpoppler-tqt
Summary:	TQt support for Poppler
Group:		Environment/Libraries

%description libpoppler-tqt
TQt support library for Poppler.
This library is used by the Trinity graphics file plugins for PDF support.

%files libpoppler-tqt
%defattr(-,root,root,-)
%{_libdir}/libpoppler-tqt.so.*

##########

%package libpoppler-tqt-devel
Summary:	Development files for TQt support for Poppler
Group:		Development/Libraries
Requires:	%{name}-libpoppler-tqt

%description libpoppler-tqt-devel
Development files of TQt support library for Poppler.
This package contains the development files needed to compile applications against poppler-tqt.

%files libpoppler-tqt-devel
%defattr(-,root,root,-)
%{tde_includedir}/poppler-link-qt3.h
%{tde_includedir}/poppler-page-transition.h
%{tde_includedir}/poppler-qt.h
%{_libdir}/libpoppler-tqt.la
%{_libdir}/libpoppler-tqt.so
#%{_libdir}/pkgconfig/poppler-tqt.pc

##########

%package devel
Summary:	Development files for %{name} 
Group:		Development/Libraries

Obsoletes:	trinity-kdegraphics-devel < %{version}-%{release}
Provides:	trinity-kdegraphics-devel = %{version}-%{release}

Requires: trinity-libkscan-devel = %{version}-%{release}
Requires: %{name}-libpoppler-tqt-devel = %{version}-%{release}

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{_includedir}/dom/
#%{_includedir}/kfaximage.h
%{_includedir}/kmultipageInterface.h
%{_includedir}/ksvg/
%{_includedir}/kviewshell/
%{_includedir}/libtext2path-0.1/BezierPath.h
%{_includedir}/libtext2path-0.1/Glyph.h
%{_includedir}/libtext2path-0.1/GlyphTracer.h
%{_libdir}/lib[kt]deinit_kview.la
%{_libdir}/lib[kt]deinit_mrmlsearch.la
%{_libdir}/libkghostviewlib.la
%{_libdir}/libkghostviewlib.so
%{_libdir}/libkimageviewer.la
%{_libdir}/libkimageviewer.so
%{_libdir}/libkmultipage.la
%{_libdir}/libkmultipage.so
%{_libdir}/libkpovmodeler.la
%{_libdir}/libkpovmodeler.so
%{_libdir}/libksvg.la
%{_libdir}/libksvg.so
%{_libdir}/libtext2path.la
%{_libdir}/libtext2path.so
%{_datadir}/cmake/*

############

# Excludes kuickshow (built separately)
%exclude %{_bindir}/kuickshow
%exclude %{tde_libdir}/kuickshow.la
%exclude %{tde_libdir}/kuickshow.so
%exclude %{_libdir}/lib[kt]deinit_kuickshow.la
%exclude %{_libdir}/lib[kt]deinit_kuickshow.so
%exclude %{tde_appdir}/kuickshow.desktop
%exclude %{_datadir}/apps/kuickshow/
%exclude %{_datadir}/icons/hicolor/*/apps/kuickshow.png
%exclude %{tde_docdir}/HTML/en/kuickshow/

##########

%prep
%setup -q -n kdegraphics
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if 0%{?rhel} && 0%{?rhel} <= 5
%patch3 -p1 -b .mkstemps
%endif
%patch4 -p1
%patch5 -p1 -b .gcc47
%patch6 -p1 -b .poppler
%patch7 -p1


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"
export LD_LIBRARY_PATH="%{_libdir}"

%__mkdir build
cd build
%cmake \
  -DWITH_T1LIB=ON \
  -DWITH_LIBPAPER=ON \
  -DWITH_TIFF=ON \
  -DWITH_OPENEXR=ON \
  -DWITH_PDF=ON \
  -DWITH_PDF=ON \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags}

%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

# locale's
%find_lang %{name} || touch %{name}.lang
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}$HTML_DIR ]; then
for lang_dir in %{buildroot}$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
    # replace absolute symlinks with relative ones
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && ln -nsf ../common $i/common
      done
    popd
  fi
done
fi

# rpmdocs
for dir in k* ; do
  for file in AUTHORS ChangeLog README TODO ; do
    if test -s "$dir/$file" ; then
       install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
       echo "%doc rpmdocs/$dir/" >> %{name}.lang
    fi
  done
done

# unpackaged files
# omit kpovmodeler-devel files (for now) -- Rex
rm -f %{buildroot}/libkpovmodeler.so


%clean
%__rm -rf %{buildroot}



%changelog
* Mon Jul 09 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-5
- Renames 'kdegraphics' to 'tdegraphics'
- Split in several packages

* Tue Nov 22 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Rebuild with poppler 0.12 for RHEL 5
- Re-adds qt-poppler include files

* Fri Nov 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Updates BuildRequires

* Wed Nov 02 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Fix kpovmodeler compilation on RHEL 5 (patch4)

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15
- RHEL 5 build has some features disabled (see patches)

* Sun Sep 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
