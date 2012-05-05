# Default version for this component
%define kdecomp gwenview
%define version 1.4.2
%define release 7

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%define _mandir %{_datadir}/man
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	Gwenview is an image viewer for KDE.
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [gwenview] Rename old tq methods that no longer need a unique name [Commit #d0bdd0d7]
Patch1:	gwenview-3.5.13-rename_old_tq_method.patch
# [gwenview] Remove additional unneeded tq method conversions [Commit #eba1d381]
Patch2:	gwenview-3.5.13-remove_additional_tq_conversions.patch
# [gwenview] Rename obsolete tq methods to standard names [Commit #04fccf73]
Patch3:	gwenview-3.5.13-rename_obsolete_tq_methods.patch
# [gwenview] Rename a few stragglers [Commit #b4881a61]
Patch4:	gwenview-3.5.13-rename_a_few_stragglers.patch
# [gwenview] Fix FTBFS [Commit #1ca2f739]
Patch5:	gwenview-3.5.13-fix_ftbfs.patch
# [gwenview] Fix FTBFS in jpeg code [Commit #ace6f270]
Patch6:	gwenview-3.5.13-fix_ftbfs_in_jpeg_code.patch
# [gwenview] Fix linear alphabet string errors [Commit #9cb99cdb]
Patch7:	gwenview-3.5.13-fix_alphabet_string_error.patch
# [gwenview] Fix building with libpng 1.5. [Commit #303be455]
Patch8:	gwenview-3.5.13-fix_building_libpng15.patch
# [gwenview] Fix inadvertent tqt changes. Part of an extensive cleanup of various problems
#   with kipi-plugins, digikam, and gwenview to resolve bug reports 241, 962, 963. [Commit #1eac443e]
Patch9:	gwenview-3.5.13-fix_various_problems.patch



BuildRequires: tqtinterface-devel
BuildRequires: trinity-arts-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: exiv2-devel

%if "%{?_prefix}" == "/usr"
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


%prep
%setup -q -n applications/%{kdecomp}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1


# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt \
    --enable-closure

%__make
# %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}



## File lists
# HTML (1.0)
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}$HTML_DIR ]; then
for lang_dir in %{buildroot}$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
    # replace absolute symlinks with relative ones
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../common $i/common
      done
    popd
  fi
done
fi


%clean
%__rm -rf %{buildroot}


%post
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done
/sbin/ldconfig

%postun
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/applications/*/*.desktop
%{_datadir}/services/*.desktop
%{_datadir}/apps/*/
%{_datadir}/config.kcfg/*
%{tde_docdir}/HTML/en/*/
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_mandir}/man*/*

%{_libdir}/*.so
%{_libdir}/*.la
%{tde_libdir}/*.so
%{tde_libdir}/*.la



%Changelog
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

* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.2-3
- Import to GIT

* Wed Aug 24 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.2-2
- Add fix for Fedora 15

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.2-1
- Correct macro to install under "/opt", if desired

* Sat Aug 13 2011 Francois Andriot <francois.andriot@free.fr> - 1.4.2-0
- Initial build for RHEL 6.0

