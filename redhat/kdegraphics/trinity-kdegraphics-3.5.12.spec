# Default version for this component
%if "%{?version}" == ""
%define version 3.5.12
%endif
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/kde3


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

Source0:	kdegraphics-%{version}.tar.gz

# Official TDE patches (from SVN)
#  Fix kdegraphics FTBFS under gcc4.6
#  Thanks to David Rankin for the patch!
Patch0:		r1242777.diff

# [kdegraphics/kviewshell]: GCC >= 4.5 fix
#   avoid "documentWidget.cpp:290:70: error: taking address of temporary"
Patch1:		kdegraphics-documentwidget-gcc45.patch

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

# kgamma
BuildRequires: libXxf86vm-devel
# kuickshow
BuildRequires: imlib-devel
#kfile-plugin
BuildRequires: OpenEXR-devel
# kpdf
BuildRequires: freetype-devel
BuildRequires: poppler-qt-devel
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

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
   --enable-new-ldflags \
   --disable-dependency-tracking \
   --disable-rpath \
   --disable-debug \
   --disable-warnings \
   --enable-final \
   --includedir=%{_includedir}/kde \
   --with-xinerama \
   --with-extra-includes=%{_includedir}/tqt

%if 0%{?fedora} >= 15
# Ugly fix for kolourpaint - problem when linking libkdefx.so
sed -i kolourpaint/Makefile \
  -e 's,\($(kolourpaint_LINK) $(kolourpaint_OBJECTS) $(kolourpaint_LDADD) \)\($(LIBS)\),\1 -lkdefx \2,'
  
# Another ugly fix for kpdf - problem when linking fontconfig
sed -i kpdf/Makefile \
  -e '/^LDFLAGS = .*/ s,$, -lfontconfig,'
%endif

%__make %{?_smp_mflags}

%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

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
rm -rf %{buildroot}


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
%doc %{_docdir}/HTML/en/kpovmodeler/
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
%{_includedir}/kde/*
%{_libdir}/lib*.so
#exclude %{_libdir}/libkpovmodeler.so
%exclude %{_libdir}/libkfaximage.so
%exclude %{_libdir}/libkdeinit_*.so
%exclude %{_libdir}/libdjvu.so

%changelog
* Sun Sep 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-2 
- Import to GIT

* Wed Aug 24 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-1
- Add fix for Fedora 15
- Add 'patch0' and 'patch1' for GCC >= 4.5
- Correct macro to install under "/opt", if desired

* Thu Jun 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-0
- Initial build for RHEL 6.0
- SPEC file taken from Fedora 8 "kdegraphics 7:3.5.10-1"
