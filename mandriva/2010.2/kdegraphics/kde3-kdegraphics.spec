%define _requires_exceptions devel\(linux-gate\)

%define launchers /etc/dynamic/launchers/scanner

%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define lib_name_orig kdegraphics
%define lib_oname %mklibname kdegraphics %lib_major
%define lib_major 0
%define lib_name %mklibname kde3-kdegraphics %lib_major

%define oname kdegraphics

Name: kde3-kdegraphics
Version: 3.5.12
Release: %mkrel 1
Epoch: 1
Group: Graphical desktop/KDE3
Summary: K Desktop Environment - Graphics
License: GPL
URL: http://www.kde.org/
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
Patch0: kdegraphics-3.5.12-fix-kdpf-menuEntry.desktop
Patch1: kdegraphics-3.5.12-ksnapshot-use-xdg-dir.patch
#Patch2: kdegraphics-3.5.9-fix-underllinking.patch
Patch3: kdegraphics-3.5.12-kgamma_opendisplay.patch
#Patch4: ksvg-3.5.10-new-fribidi.patch
Patch5: kdegraphics-3.5.3-gphoto2-config.patch
Patch6: kde-3.5.10-acinclude.patch
#Patch7: fix_autotools.patch
Patch8: kdebase-3.5.12-move-xdg-menu-dir.patch
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: kde3-macros
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%endif
BuildRequires: autoconf >= 1:2.65
BuildRequires: automake > 1.5
BuildRequires: kdelibs3-devel 
BuildRequires: jpeg-devel 
BuildRequires: png-devel 
BuildRequires: libimlib-devel libtiff-devel
BuildRequires: zlib-devel 
BuildRequires: bzip2-devel
BuildRequires: gettext texinfo
BuildRequires: X11-devel 
BuildRequires: freetype2-devel
BuildRequires: openssl-devel 
BuildRequires: libsane-devel 
BuildRequires: OpenEXR-devel
BuildRequires: libtiff-progs
BuildRequires: gphoto2-devel
BuildRequires: fribidi-devel
BuildRequires: fontconfig-devel
# necessary for displaying info into konqueror pdfinfo
BuildRequires: xpdf
BuildRequires: mesaglut-devel
BuildRequires: libpoppler-qt-devel
BuildRequires: libv4l-devel
Suggests: kde3-kdegraphics-ksnapshot = %epoch:%version-%release
Suggests: kde3-kdegraphics-common = %epoch:%version-%release
Suggests: kde3-kdegraphics-kuickshow = %epoch:%version-%release
Suggests: kde3-kdegraphics-kdvi = %epoch:%version-%release
Suggests: kde3-kdegraphics-kfax = %epoch:%version-%release
Suggests: kde3-kdegraphics-kghostview = %epoch:%version-%release
Suggests: kde3-kdegraphics-kiconedit = %epoch:%version-%release   
Suggests: kde3-kdegraphics-kcolorchooser = %epoch:%version-%release   
Suggests: kde3-kdegraphics-kcoloredit = %epoch:%version-%release   
Suggests: kde3-kdegraphics-kpovmodeler = %epoch:%version-%release    
Suggests: kde3-kdegraphics-kruler = %epoch:%version-%release    
Suggests: kde3-kdegraphics-mrmlsearch = %epoch:%version-%release    
Suggests: kde3-kdegraphics-kview = %epoch:%version-%release    
Suggests: kde3-kdegraphics-kpdf = %epoch:%version-%release
Suggests: kde3-kdegraphics-kamera = %epoch:%version-%release
Requires: fribidi
Provides: kdegraphics3 = %epoch:%version-%release
Provides: kdegraphics = %epoch:%version-%release
Obsoletes: kdegraphics
Obsoletes: kdegraphics3

%description
Graphical tools for the K Desktop Environment.
kdegraphics is a collection of graphic oriented applications:

	- kamera: digital camera io_slave for Konqueror. Together gPhoto this 
			allows you to access your camera's picture with the URL kamera:/
	- kcoloredit: contains two programs: a color value editor and also 
			a color picker
	- kdvi: program (and embeddable KPart) to display *.DVI files from TeX
	- kfax: a program to display raw and tiffed fax images (g3, g3-2d, g4)
	- kfaxview: an embeddable KPart to display tiffed fax images
	- kfile-plugins: provide meta information for graphic files
	- kghostview: program (and embeddable KPart) to display *.PDF and *.PS
	- kiconedit: an icon editor
	- kooka: a raster image scan program, based on SANE and libkscan
	- kruler: a ruler in inch, centimeter and pixel to check distances 
	 		  on the screen
	- ksnapshot: make snapshots of the screen contents
	- kuickshow: fast and comfortable imageviewer
	- kview: picture viewer, provided as standalone program and embeddable KPart
	- kviewshell: generic framework for viewer applications

%files
%defattr(-,root,root,-)
%doc README

#----------------------------------------------------------------------

%package common
Summary:	Common files for kdegraphics
Group: Graphical desktop/KDE3	
Requires:   kdelibs3 
Requires:   libgphoto-hotplug
Obsoletes:  %oname-common
Obsoletes:  kdegraphics3
Provides: kdegraphics3-common = %epoch:%version-%release
Provides:   kgamma3


%description common
Common files for kdegraphics

%files common
%defattr(-,root,root)
%_kde3_datadir/applications/kde/kgamma.desktop
%dir %_kde3_appsdir/kgamma/
%_kde3_appsdir/kgamma/*
%doc %_kde3_docdir/HTML/en/kgamma
%_kde3_bindir/xf86gammacfg
%_kde3_appsdir/kconf_update/update-to-xt-names.pl
%_kde3_libdir/kde3/kcm_kgamma.*
%_kde3_libdir/kde3/kfile_*
%_kde3_libdir/kde3/emptymultipagepart.*
%_kde3_datadir/servicetypes/kmultipage.desktop
%_kde3_datadir/services/emptymultipage.desktop
%_kde3_iconsdir/*/*/*/kgamma*
%_kde3_iconsdir/*/*/filesystems/*
%_kde3_iconsdir/*/*/actions/*
%_kde3_iconsdir/*/*/devices/*
%_kde3_datadir/services/kfile_*
%_kde3_datadir/services/scanservice.desktop

#----------------------------------------------------------------------

%package -n %lib_name-common
Summary:	Libraries files for kdegraphics
Group:		System/Libraries
Obsoletes:	%lib_name
Obsoletes:     %lib_oname

%description -n %lib_name-common
Libraries files for kdegraphics

%files -n %lib_name-common
%defattr(-,root,root)
%_kde3_libdir/libkmultipage.la*  
%_kde3_libdir/libkmultipage.so.*

#----------------------------------------------------------------------

%package kolourpaint
Summary:    Free and easy-to-use paint program for KDE
Group: Graphical desktop/KDE3
Provides:   kde3-kolourpaint
Obsoletes:  %oname-kolourpaint < 1:3.5.10-3
Obsoletes:  kdegraphics3-kolourpaint < 1:3.5.10-3
Provides:  kdegraphics3-kolourpaint < 1:3.5.10-3
Obsoletes:  kdegraphics <= 3.1-9.1mdk

%description kolourpaint
KolourPaint is a free, easy-to-use paint program for KDE.
It aims to be conceptually simple to understand; providing a level of
functionality targeted towards the average user. It's designed for daily
tasks like:
  Painting - drawing diagrams and "finger painting" 
  Image Manipulation - editing screenshots and photos; applying effects 
  Icon Editing - drawing clipart and logos with transparency 
It's not an unusable and monolithic program where simple tasks like drawing 
lines become near impossible. Nor is it so simple that it lacks essential 
features like Undo/Redo. KolourPaint is opensource software written in C++
using the Qt and KDE libraries

%files kolourpaint
%defattr(-,root,root)
%_kde3_bindir/kolourpaint
%_kde3_datadir/applications/kde/kolourpaint.desktop
%dir %_kde3_appsdir/kolourpaint
%_kde3_appsdir/kolourpaint/*
%doc %_kde3_docdir/HTML/en/kolourpaint
%_kde3_iconsdir/*/*/*/kolourpaint*

#----------------------------------------------------------------------

%package mrmlsearch
Summary:	Short for Multimedia Retrieval Markup Language
Group: Graphical desktop/KDE3
Obsoletes: %lib_name-mrmlsearch
Obsoletes:  %oname-mrmlsearch 

%description mrmlsearch
MRML is short for Multimedia Retrieval Markup Language,
which defines a protocol for querying a server for images
based on their content. See http://www.mrml.net about MRML
and the GNU Image Finding Tool (GIFT), an MRML server.

This package consists of an mrml kio-slave that handles
the communication with the MRML server and a KPart to
be embedded e.g. into Konqueror.

With those, you can search for images by giving an example
image and let the server look up similar images. The query
result can be refined by giving positive/negative feedback.

%files mrmlsearch
%defattr(-,root,root)
%_kde3_bindir/mrmlsearch
%_kde3_libdir/kde3/kcm_kmrml.*
%_kde3_libdir/kde3/kio_mrml.*
%_kde3_libdir/kde3/libkmrmlpart.*
%_kde3_libdir/kde3/kded_daemonwatcher.*
%_kde3_datadir/applications/kde/kcmkmrml.desktop
%_kde3_datadir/services/mrml.protocol
%_kde3_datadir/services/mrml_part.desktop
%_kde3_datadir/services/kded/daemonwatcher.desktop
%_kde3_appsdir/konqueror/servicemenus/mrml-servicemenu.desktop
%_kde3_datadir/mimelnk/text/mrml.desktop
%_kde3_libdir/kde3/mrmlsearch.*
%_kde3_libdir/libkdeinit_mrmlsearch.*

#----------------------------------------------------------------------

%package -n %lib_name-common-devel
Summary:	Include files for kdegraphics
Group:		Development/KDE and Qt
Requires:   %{lib_name}-common = %epoch:%version-%release
Obsoletes:	kdegraphics-devel < %epoch:%version-%release
Obsoletes:	%lib_name-devel < %epoch:%version-%release
Provides:	kdegraphics-devel = %epoch:%version-%release
Provides:	%lib_name-devel = %epoch:%version-%release
Provides:   kdegraphics3-devel = %epoch:%version-%release
Provides:	%{lib_name_orig}-common-devel = %epoch:%version-%release

%description -n %lib_name-common-devel
This package contains include files needed to build applications 
based on kdegraphic.

%files -n %lib_name-common-devel
%defattr(-,root,root)
%_kde3_includedir/*.h
%_kde3_libdir/libkmultipage.so

#----------------------------------------------------------------------


%package kooka
Summary:    Raster image scan program for the KDE system
Group: Graphical desktop/KDE3
Requires:	kdelibs3 
Requires:	gocr, sane
Requires:	%lib_name-kooka = %epoch:%version-%release
Provides:	kde3-kooka
Provides:	kooka3
Provides:       kdegraphics3-kooka
Provides:	scanner-gui
Obsoletes:  %oname-kooka

%description kooka
This package contains a raster image scan program, based on SANE and libkscan.

%files kooka
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kooka
%dir %_kde3_appsdir/kooka
%_kde3_appsdir/kooka/*
%_kde3_datadir/config/kookarc
%_kde3_bindir/kooka
%_kde3_datadir/applications/kde/kooka.desktop
%config(noreplace) %launchers/%name.desktop

#----------------------------------------------------------------------

%package kdvi
Summary:    DVI Viewer
Group: Graphical desktop/KDE3
Provides:	kdvi3
Provides:	kde3-kdvi
Requires:	%lib_name-common = %epoch:%version-%release
Requires:	kde3-kdegraphics-common = %epoch:%version-%release
# kdvi requires kviewpart which is in kview, do NOT remove this provide
# or kdvi won't work
Requires:	kde3-kdegraphics-kview
Requires:	tetex
Obsoletes: %oname-kdvi < 1:3.5.10-3


%description kdvi
Kdvi package

%files kdvi
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kdvi
%_kde3_libdir/kde3/kdvipart.*
%_kde3_iconsdir/*/*/*/kdvi.*
%_kde3_datadir/services/kdvimultipage.desktop
%_kde3_datadir/config.kcfg/kdvi.kcfg
%_kde3_bindir/kdvi           
%_kde3_datadir/applications/kde/kdvi.desktop           
%dir %_kde3_appsdir/kdvi/
%_kde3_appsdir/kdvi/*

#----------------------------------------------------------------------

%package kfax
Summary:    Kfax package
Group: Graphical desktop/KDE3
Provides:	kfax3
Provides:	kde3-kfax
Requires:   %lib_name-common = %epoch:%version-%release
Requires:   kde3-kdegraphics-kview 
Obsoletes:	%lib_name-kfax
Obsoletes:  %oname-kfax < 1:3.5.10-3

%description kfax
A program to display raw and tiffed fax images (g3, g3-2d, g4).

%files kfax
%defattr(-,root,root)
%_kde3_libdir/kde3/djvuviewpart.*
%_kde3_libdir/libdjvu.*
%_kde3_appsdir/djvumultipage.rc
%_kde3_datadir/config.kcfg/djvumultipage.kcfg
%_kde3_datadir/services/djvumultipage.desktop
%_kde3_bindir/kfax        
%_kde3_bindir/kfaxview
%_kde3_datadir/applications/kde/kfax.desktop           
%_kde3_datadir/applications/kde/kfaxview.desktop
%dir %_kde3_appsdir/kfax/
%_kde3_appsdir/kfax/*
%dir %_kde3_appsdir/kfaxview
%_kde3_appsdir/kfaxview/*
%_kde3_iconsdir/*/*/*/kfax*
%_kde3_datadir/services/kfaxmultipage.desktop
%_kde3_datadir/services/kfaxmultipage_tiff.desktop
%_kde3_libdir/kde3/kfaxviewpart.*
# This is a module, not library. We will not change buildsystem
# on kde 3 and the install should be fixed on kde4
%_kde3_libdir/libkfaximage.*

#----------------------------------------------------------------------

%package kruler
Summary:    Kruler package
Group: Graphical desktop/KDE3
Provides:	kde3-kruler
Provides:       kdegraphics3-kruler
Provides:	kruler3
Obsoletes:  %oname-kruler

%description kruler
A ruler in inch, centimeter and pixel to check distances on the screen

%files kruler
%defattr(-,root,root)
%_kde3_bindir/kruler  
%_kde3_datadir/applnk/Graphics/kruler.desktop
%_kde3_iconsdir/*/*/*/kruler*
%_kde3_datadir/applications/kde/kruler.desktop           
%dir %_kde3_appsdir/kruler/
%_kde3_appsdir/kruler/*
%doc %_kde3_docdir/HTML/en/kruler

#----------------------------------------------------------------------

%package kghostview
Summary:    Kghostview package
Group: Graphical desktop/KDE3
Provides:	kghostview3
Provides:	kde3-kghostview
Provides:       kdegraphics3-kghostview
Requires:	ghostscript, ghostscript-module-X
Obsoletes:	kdegraphics-common
Obsoletes:  %oname-kghostview

%description kghostview
A program (and embeddable KPart) to display *.PDF and *.PS

%files kghostview
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kghostview
%_kde3_iconsdir/*/*/*/kghostview.*
%_kde3_appsdir/kconf_update/kghostview.upd
%dir %_kde3_datadir/config.kcfg/
%_kde3_datadir/config.kcfg/kghostview.kcfg
%_kde3_bindir/kghostview  
%_kde3_datadir/applications/kde/kghostview.desktop   
%_kde3_datadir/services/kghostview_part.desktop
%dir %_kde3_appsdir/kghostview/
%_kde3_appsdir/kghostview/*
%_kde3_libdir/kde3/libkghostviewpart.*
%_kde3_libdir/kde3/gsthumbnail.*
%_kde3_datadir/services/gsthumbnail.desktop

#----------------------------------------------------------------------

%package -n %lib_name-kghostview
Summary:    Library for kghostview 
Group:      System/Libraries
Obsoletes:  kdegraphics

%description -n %lib_name-kghostview
Library for kghostview

%files -n %lib_name-kghostview
%defattr(-,root,root)
%_kde3_libdir/libkghostviewlib.la
%_kde3_libdir/libkghostviewlib.so.*

#----------------------------------------------------------------------

%package -n %lib_name-kghostview-devel
Summary:    Devel for kghostview 
Group:      Development/KDE and Qt
Requires:	%lib_name-kghostview = %epoch:%version-%release

%description -n %lib_name-kghostview-devel
Library for kghostview

%files -n %lib_name-kghostview-devel
%defattr(-,root,root)
%_kde3_libdir/libkghostviewlib.so

#----------------------------------------------------------------------

%package kpdf
Summary:    Kpdf package
Group: Graphical desktop/KDE3
Provides:	kpdf3
Provides:	kde3-kpdf
Provides:       kdegraphics3-kpdf
# (fundawang) Suggest xpdf-common which contains unicodemap and xpdfrc, so
# that the default installation could render more international glyphs (#33546):
Suggests: 	xpdf-common
Obsoletes:  kdegraphics
Obsoletes:  %oname-kpdf

%description kpdf
kpdf program

%files kpdf
%defattr(-,root,root)
%_kde3_bindir/kpdf
%dir %_kde3_appsdir/kpdf/
%_kde3_appsdir/kpdf/*
%dir %_kde3_appsdir/kpdfpart/
%_kde3_appsdir/kpdfpart/*
%_kde3_datadir/services/kpdf_part.desktop
%_kde3_iconsdir/*/*/*/kpdf*
%_kde3_libdir/kde3/kfile_pdf.*	 
%_kde3_datadir/services/kfile_pdf.desktop
%_kde3_libdir/kde3/libkpdfpart.*
%_kde3_datadir/config.kcfg/kpdf.kcfg
%doc %_kde3_docdir/HTML/en/kpdf
%_kde3_datadir/applications/kde/kpdf.desktop           

#----------------------------------------------------------------------

%package ksnapshot
Summary:    Ksnaphot package
Group: Graphical desktop/KDE3
Provides:	ksnapshot3
Provides:	kde3-ksnapshot
Provides:       kdegraphics3-ksnapshot
Obsoletes:  %oname-ksnapshot

%description ksnapshot
KSnapshot is intended to be an easy to use program for making
screenshots. I can be bound to the Print Screen key, as the program
takes a snapshot of the desktop on startup (before it displays it
window), so it's a simple way of of making snapshots.

%files ksnapshot
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/ksnapshot
%_kde3_bindir/ksnapshot  
%_kde3_datadir/applications/kde/ksnapshot.desktop
%_kde3_iconsdir/*/*/*/ksnapshot*

#----------------------------------------------------------------------


%package kpovmodeler
Summary:    Kpovmodeler package
Group: Graphical desktop/KDE3
Provides:	kpovmodeler3
Provides:	kde3-kpovmodeler
Provides:       kdegraphics3-kpovmodeler
Obsoletes:  %oname-kpovmodeler

%description kpovmodeler
Program to enter scenes for the 3D rendering engine PovRay.

%files kpovmodeler
%defattr(-,root,root)
%_kde3_bindir/kpovmodeler  
%doc %_kde3_docdir/HTML/en/kpovmodeler
%_kde3_libdir/kde3/libkpovmodelerpart.*
%_kde3_iconsdir/*/*/*/kpovmodeler*
%dir %_kde3_appsdir/kpovmodeler/
%_kde3_appsdir/kpovmodeler/*
%_kde3_datadir/applications/kde/kpovmodeler.desktop

#----------------------------------------------------------------------

%package -n %lib_name-kpovmodeler
Summary:    Library for kpovmodeler package
Group:      System/Libraries
Obsoletes:  kdegraphics

%description -n %lib_name-kpovmodeler
Library for kpovmodeler.

%files -n %lib_name-kpovmodeler
%defattr(-,root,root)
%_kde3_libdir/libkpovmodeler.la
%_kde3_libdir/libkpovmodeler.so.*

#----------------------------------------------------------------------

%package -n %lib_name-kpovmodeler-devel
Summary:    Devel for kpovmodeler package
Group:      Development/KDE and Qt
Requires:	%lib_name-kpovmodeler = %epoch:%version-%release

%description -n %lib_name-kpovmodeler-devel
Devel for kpovmodeler.

%files -n %lib_name-kpovmodeler-devel
%defattr(-,root,root)
%_kde3_libdir/libkpovmodeler.so

#----------------------------------------------------------------------

%package kiconedit
Summary:    Kiconedit package
Group: Graphical desktop/KDE3
Provides:	kiconedit3
Provides:	kde3-kiconedit
Provides:       kdegraphics3-kiconedit
Obsoletes:  kdegraphics
Obsoletes:  %oname-kiconedit

%description kiconedit
An icon editor.

%files kiconedit
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kiconedit
%_kde3_datadir/applications/kde/kiconedit.desktop    
%dir %_kde3_appsdir/kiconedit
%_kde3_appsdir/kiconedit/*
%_kde3_iconsdir/*/*/*/kiconedit*
%_kde3_bindir/kiconedit   

#----------------------------------------------------------------------

%package kview
Summary:    Kview package
Group: Graphical desktop/KDE3
Provides:	kview3
Provides:	kde3-kview
Provides:       kdegraphics3-kview
Obsoletes:  kdegraphics
Obsoletes:	kdegraphics-ksvg
Obsoletes:	kdegraphics-common
Obsoletes:  %oname-kview

%description kview
Kview is a  picture viewer, provided as standalone program and embeddable KPart

%files kview
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kview
%_kde3_bindir/kview
%_kde3_bindir/kviewshell
%_kde3_datadir/config.kcfg/kviewshell.kcfg
%_kde3_libdir/kde3/kviewerpart.*
%_kde3_datadir/applications/kde/kview.desktop           
%_kde3_libdir/kde3/kview.*
%_kde3_libdir/libkdeinit_kview.*      
%_kde3_libdir/kde3/kcm_kview*.*
%_kde3_datadir/services/kviewviewer.desktop
%dir %_kde3_datadir/services/kconfiguredialog/
%_kde3_datadir/services/kconfiguredialog/kviewcanvasconfig.desktop
%_kde3_datadir/services/kconfiguredialog/kviewgeneralconfig.desktop
%_kde3_datadir/services/kconfiguredialog/kviewpluginsconfig.desktop
%_kde3_datadir/services/kconfiguredialog/kviewviewerpluginsconfig.desktop
%dir %_kde3_appsdir/kview/
%_kde3_appsdir/kview/*
%_kde3_datadir/services/kviewcanvas.desktop
%_kde3_datadir/servicetypes/kimageviewercanvas.desktop
%_kde3_datadir/servicetypes/kimageviewer.desktop
%dir %_kde3_appsdir/kviewviewer/
%_kde3_appsdir/kviewviewer/*
%_kde3_libdir/kde3/kview_*
%_kde3_libdir/kde3/libkview*
%_kde3_libdir/kde3/libphotobook.*
%_kde3_iconsdir/*/*/*/photobook*
%_kde3_iconsdir/*/*/*/kview*
%_kde3_datadir/services/photobook.desktop
%dir %_kde3_appsdir/kviewerpart/
%_kde3_appsdir/kviewerpart/*
%dir %_kde3_appsdir/kviewshell/
%_kde3_appsdir/kviewshell/*
%dir %_kde3_appsdir/photobook/
%_kde3_appsdir/photobook/*

#----------------------------------------------------------------------

%package -n %lib_name-kview
Summary:    Librarie for Kview package
Group:      System/Libraries
Obsoletes:  kdegraphics

%description -n %lib_name-kview
Libraries for Kview package

%files -n %lib_name-kview
%defattr(-,root,root)
%_kde3_libdir/libkimageviewer.so.*
%_kde3_libdir/libkimageviewer.la

#----------------------------------------------------------------------

%package -n %lib_name-kview-devel
Summary:    Devel file for Kview package
Group:      Development/KDE and Qt
Requires:	%lib_name-kview = %epoch:%version-%release
Provides:	%{lib_name_orig}-kview-devel = %epoch:%version-%release

%description -n %lib_name-kview-devel
Devel files for Kview package

%files -n %lib_name-kview-devel
%defattr(-,root,root)
%_kde3_libdir/libkimageviewer.so
%_kde3_includedir/kviewshell/*.h

#----------------------------------------------------------------------

%package kuickshow
Summary:    Kuickshow package
Group: Graphical desktop/KDE3
Provides:	kuickshow3
Provides:	kde3-kuickshow
Provides:       kdegraphics3-kuickshow
Obsoletes:  kdegraphics
Obsoletes:	%lib_name-kuickshow
Obsoletes:  %oname-kuickshow

%description kuickshow
A fast and comfortable imageviewer.

%files kuickshow
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kuickshow
%_kde3_bindir/kuickshow  
%_kde3_iconsdir/*/*/*/kuickshow*
%_kde3_datadir/applications/kde/kuickshow.desktop
%dir %_kde3_appsdir/kuickshow/
%_kde3_appsdir/kuickshow/*
%_kde3_libdir/kde3/kuickshow.*  
%_kde3_libdir/libkdeinit_kuickshow.*

#----------------------------------------------------------------------

%package kcoloredit
Summary:    Kcoloredit package
Group: Graphical desktop/KDE3
Provides:	kcoloredit3
Provides:	kde3-kcoloredit
Provides:       kdegraphics3-kcoloredit
Obsoletes:  kdegraphics-kpaint
Obsoletes:  %oname-kcoloredit

%description kcoloredit
A fast and comfortable imageviewer.

%files kcoloredit
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kcoloredit
%dir %_kde3_appsdir/kcoloredit
%_kde3_datadir/applications/kde/kcoloredit.desktop     
%_kde3_appsdir/kcoloredit/*
%_kde3_bindir/kcoloredit     
%_kde3_iconsdir/*/*/*/kcoloredit*

#----------------------------------------------------------------------

%package kcolorchooser
Summary:    Kcolorchooser package
Group: Graphical desktop/KDE3
Provides: kde3-kcolorchooser
Provides: kdegraphics3-kcolorchooser
Provides: kcolorchooser3
Obsoletes:  kdegraphics-kpaint
Obsoletes:  %oname-kcolorchooser


%description kcolorchooser
A fast and comfortable imageviewer.

%files kcolorchooser
%defattr(-,root,root)
%_kde3_bindir/kcolorchooser  
%_kde3_datadir/applications/kde/kcolorchooser.desktop  
%_kde3_iconsdir/*/*/*/kcolorchooser*

#----------------------------------------------------------------------

%package -n %lib_name-kooka
Summary:    Library for Kooka 
Group:      System/Libraries
Requires:	kdelibs >= 30000000:3.1.2-1mdk
Obsoletes:  kdegraphics

%description  -n %lib_name-kooka
Library for Kooka 

%post kooka
update-alternatives --install %{launchers}/kde.desktop scanner.kde.dynamic %launchers/%name.desktop 31
update-alternatives --install %{launchers}/gnome.desktop scanner.gnome.dynamic %launchers/%name.desktop 29

%postun kooka
if [ $1 = 0 ]; then
  update-alternatives --remove scanner.kde.dynamic %launchers/%name.desktop
  update-alternatives --remove scanner.gnome.dynamic %launchers/%name.desktop
fi

%files -n %lib_name-kooka
%defattr(-,root,root)
%_kde3_libdir/libkscan.so.*
%_kde3_libdir/libkscan.la

#----------------------------------------------------------------------

%package -n %lib_name-kooka-devel
Summary:    Devel files for Kooka 
Group:      Development/KDE and Qt
Requires:	kdelibs >= 30000000:3.1.2-1mdk
Requires:	%lib_name-kooka = %epoch:%version-%release
Provides:	%{lib_name_orig}-kooka-devel = %epoch:%version-%release

%description  -n %lib_name-kooka-devel
Devel files for Kooka 

%files -n %lib_name-kooka-devel
%defattr(-,root,root)
%_kde3_libdir/libkscan.so

#----------------------------------------------------------------------
%package kamera
Summary:    Camera io slave for KDE3 
Group: Graphical desktop/KDE3
Requires:       kdelibs >= 30000000:3.1.2-1mdk

%description  kamera
KDE3 io slave camera

%files kamera
%defattr(-,root,root)
%doc %_kde3_docdir/HTML/en/kamera/*
%_kde3_datadir/services/camera.protocol
%_kde3_datadir/applications/kde/kamera.desktop
%_kde3_iconsdir/*/*/apps/camera*
%_kde3_libdir/kde3/kio_kamera.*
%_kde3_libdir/kde3/kcm_kamera.*
#----------------------------------------------------------------------

%package ksvg
Summary:    Ksvg package
Group: Graphical desktop/KDE3
Requires:	%lib_name-ksvg = %epoch:%version-%release
Provides:	ksvg3
Provides:	kde3-ksvg
Provides:       kdegraphics3-ksvg
Obsoletes:  kdegraphics
Obsoletes: %oname-ksvg < 1:3.5.10-3

%description ksvg
KSVG is a KDE implementation of the Scalable Vector Graphics Specifications.

%files ksvg
%defattr(-,root,root)
%_kde3_bindir/svgdisplay
%_kde3_bindir/printnodetest
%_kde3_libdir/kde3/libksvg*
%_kde3_libdir/kde3/svgthumbnail.*
%_kde3_datadir/servicetypes/ksvgrenderer.desktop
%_kde3_datadir/services/svgthumbnail.desktop
%_kde3_datadir/services/ksvglibartcanvas.desktop
%_kde3_datadir/services/ksvgplugin.desktop
%dir %_kde3_appsdir/ksvg/
%_kde3_appsdir/ksvg/ksvgplugin.rc

#----------------------------------------------------------------------

%package -n %lib_name-ksvg
Summary:    Library for Ksvg
Group:      System/Libraries
Requires:   kdelibs >= 30000000:3.1.2-1mdk
Obsoletes:  kdegraphics

%description  -n %lib_name-ksvg
Library for Ksvg

%files -n %lib_name-ksvg
%defattr(-,root,root)
%_kde3_libdir/libksvg.la
%_kde3_libdir/libksvg.so.*
%_kde3_libdir/libtext2path.la
%_kde3_libdir/libtext2path.so.*


#----------------------------------------------------------------------

%package -n %lib_name-ksvg-devel
Summary:    Devel files for Ksvg 
Group:      Development/KDE and Qt
Requires:       kdelibs >= 30000000:3.1.2-1mdk
Requires:       %lib_name-ksvg = %epoch:%version-%release
Provides:       %{lib_name_orig}-ksvg-devel = %epoch:%version-%release

%description  -n %lib_name-ksvg-devel
Devel files for Ksvg

%files -n %lib_name-ksvg-devel
%defattr(-,root,root)
%_kde3_libdir/libksvg.so
%_kde3_libdir/libtext2path.so
%dir %_kde3_includedir/dom/
%_kde3_includedir/dom/*.h
%dir %_kde3_includedir/ksvg/
%_kde3_includedir/ksvg/*.h
%dir %_kde3_includedir/libtext2path-0.1/
%_kde3_includedir/libtext2path-0.1/*.h

#----------------------------------------------------------------------





%prep
%setup -q -n kdegraphics-%{version}
%patch0 -p0 -b .fix_kdf_menuEntry
%patch1 -p0 -b .xdg_dir
#%patch2 -p0 -b .underlinking
%patch3 -p0 -b .fix_opendisplay
#%patch4 -p0 -b .fribidi
%patch5 -p1
%if %mdkversion >= 201000
%patch6 -p1
%patch8 -p0
%endif

%build

PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/
export xdg_menudir=%_sysconfdir/xdg/kde/menus

make -f admin/Makefile.common cvs
#make -f Makefile.cvs

%configure_kde3 \
	--with-kamera \
        --with-gphoto2-libraries=%_libdir
%make

%install
rm -fr %buildroot

make install DESTDIR=%buildroot

mkdir -p $RPM_BUILD_ROOT%launchers
cat > $RPM_BUILD_ROOT%launchers/%name.desktop << EOF
[Desktop Entry]
Name=Kooka \$devicename
Comment=Kooka
Exec=%_kde3_bindir/kooka
Terminal=false
Icon=scanner
Type=Application
EOF

%clean
rm -fr %buildroot



%changelog

* Wed Jul 20 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-1mdv2010.2
- Remove fix_autotools.patch, kdegraphics-3.5.9-fix-underllinking.patch
+ Add kdebase-3.5.12-move-xdg-menu-dir.patch
+ Update to Tinity 3.5.12 sources
+ Add kdegraphics-3.5.12-fix-kdpf-menuEntry.desktop to replace older patch
+ Add kdegraphics-3.5.12-ksnapshot-use-xdg-dir.patch to replace older patch
+ Add kdegraphics-3.5.12-kgamma_opendisplay.patch to replace older patch
- Remove ksvg-3.5.10-new-fribidi.patch
+ Move %_kde3_libdir/kde3/libdjvu.* to %_kde3_libdir/libdjvu.* in kfax

* Wed Mar 17 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-8mvt2010.0
+ Patch for gphoto2 for kamera ioslave (again)

* Sun Jan 17 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-7mvt2010.0
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65:patch6
+ Fix automake 1.11 issue:patch7
+ Fix group

* Mon Dec 21 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-6mdv2010.0
+ Reubilt for 2010.0 release
+ Patch for gphoto2

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 1:3.5.10-5mdv2010.0
+ Rebuild for MDV 2010.0

* Thu Apr 23 2009 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-4mdv2009.1
+ Revision: 368889
- Fix invalid conflicts and obsoletes

* Thu Apr 23 2009 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-3mdv2009.1
+ Revision: 368829
- Solve autoconflicts on kde3-kdegraphics-common

* Wed Mar 25 2009 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-2mdv2009.1
+ Revision: 361144
- Bump to rebuild against cooker

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - build
    - Adapt to new layout
    - Rename to new kde3 layout

  + root <root>
    - Branching 2009.0 release for updates.

* Wed Sep 24 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.10-2mdv2009.0
+ Revision: 287740
- supports newer fribidi
- put back kfile_pdf because re-enabled poppler-qt3

* Wed Aug 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-1mdv2009.0
+ Revision: 276631
- Update for probably the last upstream kdegraphics from kde3

* Tue Jul 22 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.9-11mdv2009.0
+ Revision: 240654
- Make sure kgamma only calls XOpenDisplay() once, avoiding race conditions
  with krandr config module

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 08 2008 Funda Wang <fundawang@mandriva.org> 1:3.5.9-10mdv2009.0
+ Revision: 216892
- drop kfile_pdf plugin for missing poppler-qt3
- more fix
- disable poppler
- add patch to fix underlinking
- There is no poppler-qt3 backend

* Mon May 12 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-9mdv2009.0
+ Revision: 206116
- Remove unneeded Obsoletes

* Fri May 09 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-8mdv2009.0
+ Revision: 205315
- Fix use of kde3 macros

* Sun May 04 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-7mdv2009.0
+ Revision: 201129
- Move to /opt/kde3
- Added patch with "inpatch" logs

* Sat Mar 22 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.9-7mdv2008.1
+ Revision: 189494
- Fix groups ( tks to pterjan)

* Fri Mar 14 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-6mdv2008.1
+ Revision: 187982
- kpdf buffer overflow fixes from kde branch

* Tue Mar 11 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-5mdv2008.1
+ Revision: 186961
- Solution for https://qa.mandriva.com/show_bug.cgi?id=37650. Thanks to Albert that care to look our problem

* Mon Mar 10 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-4mdv2008.1
+ Revision: 183813
- Possible solution for bug https://qa.mandriva.com/show_bug.cgi?id=37650

* Tue Mar 04 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-3mdv2008.1
+ Revision: 178442
- Post 3.5.9 branch fixes
- kdvi crash fix related to font unload
- kpdf check for valid null entry

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1:3.5.9-2mdv2008.1
+ Revision: 170919
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Thu Feb 14 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-1mdv2008.1
+ Revision: 168619
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches intregrated

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-not-capitalized

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 29 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.8-4mdv2008.1
+ Revision: 139306
- rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 30 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.8-3mdv2008.1
+ Revision: 114055
- let ksnapshot use xdg dir by default.

* Wed Nov 07 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-2mdv2008.1
+ Revision: 106792
- fixes for CVE-2007-4352/CVE-2007-5392/CVE-2007-5493
- Add usptream 3.5.9 branch patches
  	- Fix memleak
  	- Fix compilation
  	- Fix pdf password encoding (kpdf)
  	- Splash rework (kolourpaint
  	- Fix crash in kolourpaint

* Sun Oct 28 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.8-1mdv2008.1
+ Revision: 102787
- KDE 3.5.8
  remove merged patches

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-ended-with-dot

* Fri Sep 28 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-8mdv2008.0
+ Revision: 93619
- [BUGFIX] Fix kpdf and kghostview menu entry
- [BUGFIX] Do not provide Office category on kpdf and kghostview desktop files (Bug # 24114)

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill hardcoded icon extension
    - explain latest commit

* Thu Sep 13 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.7-7mdv2008.0
+ Revision: 85236
- Suggest xpdf-common which contains unicodemap and xpdfrc, so
   that the default installation could render more international glyphs.

* Wed Sep 05 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-6mdv2008.0
+ Revision: 80394
- kpdf patches from branch. Mostly print fix

* Tue Sep 04 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.7-5mdv2008.0
+ Revision: 79101
- PDFViewer is not a valid category
- Rebuild against latest poppler

* Fri Aug 17 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-4mdv2008.0
+ Revision: 65201
- Added post kamera and kpdf patches from kde branch

* Mon Aug 13 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.5.7-3mdv2008.0
+ Revision: 62571
- kdegraphics-common should not provide kdegraphics (#32494)
- kdvi needs kviewpart to work, so it should require kview (#26095)

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Fix menu categories (bug #32467)
    - Fix kpdf menu Entry ( bug #32033)

* Mon Jul 30 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-2mdv2008.0
+ Revision: 56539
- Post 3.5.7 kpdf cve patch

* Wed May 16 2007 Helio Chissini de Castro <helio@mandriva.com> 1mdv2008.0-current
+ Revision: 27446
- 3.5.7 release

