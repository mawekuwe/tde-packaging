# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-kdegraphics
Version:	%{?version}
Release:	%{?release}%{?dist}%{_variant}
License:	GPL
Summary:    K Desktop Environment - Graphics Applications

Group:      Applications/Multimedia
Prefix:		%{_prefix}

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kdegraphics-%{version}.tar.gz

# TDE 3.5.13
## RHEL / Fedora specific patches
### [kdegraphics/ksnapshot] Missing -lXext in LDFLAGS (required for Fedora 15)
Patch0:		kdegraphics-3.5.13-ksnapshot_ldflags.patch
### [kdegraphics/kpovmodeler] CMAKE does not detect GL/glu.h (on RHEL5)
Patch1:		kdegraphics-3.5.13-kpovmodeler_check_glu.patch
### [kdegraphics/kfile-plugins/dependencies/poppler-tqt] Compile 'poppler-tqt' only if HAVE_POPPLER_016
Patch2:		kdegraphics-3.5.13-disable_poppler.patch
### [kdegraphics/kpdf/xpdf] Disable 'mkstemps' support for RHEL5
Patch3:		kdegraphics-3.5.13-xpdf_disable_mkstemps.patch
### [kdegraphics/kpovmodeler] CMAKE missing GLU_LIBRARIES
Patch4:		kdegraphics-3.5.13-kpovmodeler_missing_gl_ldflags.patch

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
# kuickshow
BuildRequires: imlib-devel
#kfile-plugin
BuildRequires: OpenEXR-devel
# kpdf
BuildRequires: freetype-devel
BuildRequires: poppler-devel
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
BuildRequires: poppler-qt-devel
%endif
BuildRequires: libpaper-devel
# ksvg
BuildRequires: fontconfig-devel
BuildRequires: fribidi-devel
BuildRequires: lcms-devel
BuildRequires: libart_lgpl-devel
BuildRequires: libXmu-devel

# kpovmodeler
BuildRequires: libGL-devel libGLU-devel libXi-devel

Requires: tqtinterface
Requires: trinity-arts
Requires: trinity-kdelibs
Requires: ghostscript
Requires: %{name}-libs = %{version}-%{release}

%if "%{_prefix}" == "/usr"
Provides: kdegraphics3 = %{version}-%{release}
Conflicts: kdegraphics
%endif

%description
Graphics applications for the K Desktop Environment, including
* kamera (digital camera support)
* kcoloredit (palette editor and color chooser)
* kdvi (displays TeX .dvi files)
* kghostview (displays postscript files)
* kiconedit (icon editor)
* kooka (scanner application)
* kpdf (displays PDF files)
* kruler (screen ruler and color measurement tool)
* ksnapshot (screen capture utility)
* kview (image viewer for GIF, JPEG, TIFF, etc.)

%package devel
Summary: Development files for %{name} 
Provides: kdegraphics3-devel = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Group: Development/Libraries
%description devel
%{summary}.

## FIXME: move more stuff to -extras
%package extras
Summary: Extra applications from %{name} 
Group: Applications/Multimedia
Requires: %{name}-libs = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description extras
%{summary}, including:
* kfax
* kfaxview
* kpovmodler

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-kdelibs >= %{version}
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.



%prep
%setup -q -n kdegraphics
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if 0%{?rhel} && 0%{?rhel} <= 5
%patch3 -p1
%endif
%patch4 -p1

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
%if 0%{?rhel} && 0%{?rhel} <= 5
  -DWITH_PDF=OFF \
%else
  -DWITH_PDF=ON \
%endif
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


%post
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post extras
/sbin/ldconfig ||:
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun extras
/sbin/ldconfig ||:
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :


%files extras
%defattr(-,root,root,-)

# kfax
%doc rpmdocs/kfax/
%{_bindir}/kfax
%{_datadir}/applications/kde/kfax.desktop
%{_datadir}/apps/kfax/
%{_datadir}/icons/hicolor/??x??/apps/kfax.png
%{_datadir}/icons/hicolor/scalable/apps/kfax.svgz

# kfaxview
%{_bindir}/kfaxview
%{_libdir}/libkfaximage.so
%{_libdir}/libkfaximage.la
%{tde_libdir}/kfaxviewpart.*
%{_datadir}/applications/kde/kfaxview.desktop
%{_datadir}/apps/kfaxview/
%{_datadir}/icons/hicolor/??x??/apps/kfaxview.png
%{_datadir}/icons/hicolor/scalable/apps/kfaxview.svgz
%{_datadir}/services/kfaxmultipage.desktop
%{_datadir}/services/kfaxmultipage_tiff.desktop

# kpovmodeler
%doc rpmdocs/kpovmodeler/
%doc %{tde_docdir}/HTML/en/kpovmodeler/
%{_bindir}/kpovmodeler
%{_libdir}/libkpovmodeler.so.*
%{_libdir}/libkpovmodeler.la
%{tde_libdir}/libkpovmodelerpart.*
%{_datadir}/applications/kde/kpovmodeler.desktop
%{_datadir}/apps/kpovmodeler/
%{_datadir}/icons/crystalsvg/*/mimetypes/kpovmodeler_doc.*
%{_datadir}/icons/hicolor/*/apps/kpovmodeler.*

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%doc rpmdocs/*

# kfax
%exclude %{_bindir}/kfax
%exclude %{_datadir}/applications/kde/kfax.desktop
%exclude %{_datadir}/apps/kfax/
%exclude %{_datadir}/icons/hicolor/*/apps/kfax.*

# kfaxview
%exclude %{_bindir}/kfaxview
%exclude %{_libdir}/libkfaximage.so
%exclude %{_libdir}/libkfaximage.la
%exclude %{tde_libdir}/kfaxviewpart.*
%exclude %{_datadir}/applications/kde/kfaxview.desktop
%exclude %{_datadir}/apps/kfaxview/
%exclude %{_datadir}/icons/hicolor/*/apps/kfaxview.*
%exclude %{_datadir}/services/kfaxmultipage.desktop
%exclude %{_datadir}/services/kfaxmultipage_tiff.desktop

# kpovmodeler
%exclude %{tde_docdir}/HTML/en/kpovmodeler/
%exclude %{_bindir}/kpovmodeler
%exclude %{_libdir}/libkpovmodeler.*
%exclude %{tde_libdir}/libkpovmodelerpart.*
%exclude %{_datadir}/applications/kde/kpovmodeler.desktop
%exclude %{_datadir}/apps/kpovmodeler/
%exclude %{_datadir}/icons/crystalsvg/*/mimetypes/kpovmodeler_doc.*
%exclude %{_datadir}/icons/hicolor/*/apps/kpovmodeler.*

%{_bindir}/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/applnk/Graphics/*kruler.desktop
%{_datadir}/apps/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/config*/*
%{_datadir}/service*/*
%{_datadir}/mimelnk/*/*
%{_libdir}/libkdeinit_*.so
%{tde_libdir}/*
%doc %lang(en) %{tde_docdir}/HTML/en/*

%files libs
%defattr(-,root,root,-)
%exclude %{_libdir}/libkfaximage.la
%exclude %{_libdir}/libkpovmodeler.la
%exclude %{_libdir}/libkpovmodeler.so.*
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la
# Why ???
%{_libdir}/libdjvu.so

%files devel
%defattr(-,root,root,-)
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
%{tde_includedir}/*
%endif
%{_includedir}/dom/*
%{_includedir}/ksvg/*
%{_includedir}/kviewshell/*
%{_includedir}/libtext2path-0.1/*
%{_includedir}/kmultipageInterface.h
%{_datadir}/cmake/*.cmake
%{_libdir}/lib*.so
#exclude %{_libdir}/libkpovmodeler.so
%exclude %{_libdir}/libkfaximage.so
%exclude %{_libdir}/libkdeinit_*.so
%exclude %{_libdir}/libdjvu.so

%changelog
* Wed Nov 02 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Fix kpovmodeler compilation on RHEL 5 (patch4)

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15
- RHEL 5 build has some features disabled (see patches)

* Sun Sep 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
