# Default version for this component
%define kdecomp digikam

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

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-%{kdecomp}
Summary:	digital photo management application for KDE [Trinity]
Version:	0.9.6
Release:	3%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [digikam] Fix digikam FTBFS due to jpeg code [Commit #b9419cd5]
Patch1:		digikam-3.5.13-fix_ftbfs_jpeg_code.patch
# [digikam] Fix FTBFS due to png code [Bug #595] [Commit #3e27b07f]
Patch2:		digikam-3.5.13-fix_ftbfs_png_code.patch
# [digikam] Remove version.h. Cruft from an older version prior to 0.9.6.
#   Part of an extensive cleanup of various problems with kipi-plugins, digikam,
#   and gwenview to resolve bug reports 241, 962, 963.
Patch3:		digikam-3.5.13-remove_version_h.patch
# [digikam] Fix usage of obsolete libpng jmpbuf member [Commit #7d0d82b7]
Patch4:		digikam-3.5.13-fix_obsolete_libpng_jmpbuf.patch
# [digikam] GCC 4.7 fix. [Bug #958] [Commit #a9489034]
Patch5:		digikam-3.5.13-gcc_47_fix.patch
# [digikam] GCC 4.7 fix. [Bug #958] [Commit #a209c81b]
Patch6:		digikam-3.5.13-gcc_47_fix2.patch
# [digikam] Fix 'format not a string literal' error [Commit #029218cd]
Patch7:		digikam-3.5.13-fix_fomat_not_string_literal.patch
# [digikam] Update patch in GIT hash a9489034 to use reinterpret_cast. [Commit #5a043853]
Patch8:		digikam-3.5.13-fix_reinterpret_cast.patch
# [digikam] Fix FTBFS on png >= 0.15 [Commit #18ecd512]
Patch9:		digikam-3.5.13-fix_ftbfs_png_015.patch
# [digikam] Missing LDFLAGS cause FTBFS on Mageia 2 / Mandriva 2011
Patch10:	digikam-3.5.13-missing_ldflags.patch


BuildRequires: tqtinterface-devel
BuildRequires: trinity-arts-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: trinity-libkexiv2-devel
BuildRequires: trinity-libkdcraw-devel
BuildRequires: trinity-libkipi-devel
%if 0%{?rhel} == 5 || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires: gphoto2-devel
%else
BuildRequires: libgphoto2-devel
%endif
BuildRequires: libtiff-devel
BuildRequires: jasper-devel

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}exiv2-devel
%else
BuildRequires:	exiv2-devel
%endif

Requires:	trinity-libkexiv2
Requires:	trinity-libkdcraw
Requires:	trinity-libkipi

%description
An easy to use and powerful digital photo management
application, which makes importing, organizing and manipulating
digital photos a "snap".  An interface is provided to connect to
your digital camera, preview the images and download and/or
delete them.

The digiKam built-in image editor makes the common photo correction
a simple task. The image editor is extensible via plugins and,
the digikamimageplugins project has been merged to digiKam core
since release 0.9.2, all useful image editor plugins are available
in the base installation.

digiKam can also make use of the KIPI image handling plugins to
extend its capabilities even further for photo manipulations,
import and export, etc. The kipi-plugins package contains many
very useful extentions.

digiKam is based in part on the work of the Independent JPEG Group.


%package devel
Group:		Development/Libraries
Summary:	Development files for %{name}
Requires:	%{name} = %{version}

%description devel
%{summary}


%prep
%setup -q -n applications/%{kdecomp}
%patch1 -p1
%patch2 -p1
%patch3 -p1 -E
%patch4 -p1 
%patch5 -p1 -b .gcc47
%patch6 -p1 -b .gcc47
%patch7 -p1 -b .ftbfs
%patch8 -p1
%patch9 -p1 -b .png015
%patch10 -p1 -b .ftbfs


# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_tdeincludedir}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  --disable-rpath \
  --with-extra-includes=%{tde_tdeincludedir}/tqt \
  --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%find_lang %{kdecomp}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
/sbin/ldconfig
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
/sbin/ldconfig
update-desktop-database %{tde_appdir} 2> /dev/null || : 

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/digikam
%{tde_bindir}/digikamthemedesigner
%{tde_bindir}/digitaglinktree
%{tde_bindir}/showfoto
%{tde_libdir}/libdigikam.so.0
%{tde_libdir}/libdigikam.so.0.0.0
%{tde_tdelibdir}/kio_digikamalbums.la
%{tde_tdelibdir}/kio_digikamalbums.so
%{tde_tdelibdir}/kio_digikamdates.la
%{tde_tdelibdir}/kio_digikamdates.so
%{tde_tdelibdir}/kio_digikamsearch.la
%{tde_tdelibdir}/kio_digikamsearch.so
%{tde_tdelibdir}/kio_digikamtags.la
%{tde_tdelibdir}/kio_digikamtags.so
%{tde_tdelibdir}/kio_digikamthumbnail.la
%{tde_tdelibdir}/kio_digikamthumbnail.so
%{tde_tdeappdir}/digikam.desktop
%{tde_tdeappdir}/showfoto.desktop
%{tde_datadir}/apps/digikam/
%{tde_datadir}/apps/konqueror/servicemenus/digikam-download.desktop
%{tde_datadir}/apps/konqueror/servicemenus/digikam-gphoto2-camera.desktop
%{tde_datadir}/apps/konqueror/servicemenus/digikam-mount-and-download.desktop
%{tde_datadir}/apps/showfoto/
%{tde_datadir}/icons/hicolor/*/apps/digikam.png
%{tde_datadir}/icons/hicolor/*/apps/showfoto.png
%{tde_datadir}/services/digikamalbums.protocol
%{tde_datadir}/services/digikamdates.protocol
%{tde_datadir}/services/digikamimageplugin_adjustcurves.desktop
%{tde_datadir}/services/digikamimageplugin_adjustlevels.desktop
%{tde_datadir}/services/digikamimageplugin_antivignetting.desktop
%{tde_datadir}/services/digikamimageplugin_blurfx.desktop
%{tde_datadir}/services/digikamimageplugin_border.desktop
%{tde_datadir}/services/digikamimageplugin_channelmixer.desktop
%{tde_datadir}/services/digikamimageplugin_charcoal.desktop
%{tde_datadir}/services/digikamimageplugin_colorfx.desktop
%{tde_datadir}/services/digikamimageplugin_core.desktop
%{tde_datadir}/services/digikamimageplugin_distortionfx.desktop
%{tde_datadir}/services/digikamimageplugin_emboss.desktop
%{tde_datadir}/services/digikamimageplugin_filmgrain.desktop
%{tde_datadir}/services/digikamimageplugin_freerotation.desktop
%{tde_datadir}/services/digikamimageplugin_hotpixels.desktop
%{tde_datadir}/services/digikamimageplugin_infrared.desktop
%{tde_datadir}/services/digikamimageplugin_inpainting.desktop
%{tde_datadir}/services/digikamimageplugin_inserttext.desktop
%{tde_datadir}/services/digikamimageplugin_lensdistortion.desktop
%{tde_datadir}/services/digikamimageplugin_noisereduction.desktop
%{tde_datadir}/services/digikamimageplugin_oilpaint.desktop
%{tde_datadir}/services/digikamimageplugin_perspective.desktop
%{tde_datadir}/services/digikamimageplugin_raindrop.desktop
%{tde_datadir}/services/digikamimageplugin_restoration.desktop
%{tde_datadir}/services/digikamimageplugin_sheartool.desktop
%{tde_datadir}/services/digikamimageplugin_superimpose.desktop
%{tde_datadir}/services/digikamimageplugin_texture.desktop
%{tde_datadir}/services/digikamimageplugin_whitebalance.desktop
%{tde_datadir}/services/digikamsearch.protocol
%{tde_datadir}/services/digikamtags.protocol
%{tde_datadir}/services/digikamthumbnail.protocol
%{tde_datadir}/servicetypes/digikamimageplugin.desktop
%{tde_mandir}/man*/*
%{tde_tdedocdir}/HTML/en/digikam-apidocs/


%files devel
%{tde_tdeincludedir}/digikam_export.h
%{tde_tdeincludedir}/digikam/
%{tde_libdir}/libdigikam.so
%{tde_libdir}/libdigikam.la


%Changelog
* Fri Aug 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.6-3
- Add support for Mageia 2 and Mandriva 2011
- Removes old patches, adds GIT patches.
- Fix digikam FTBFS due to jpeg code [Commit #b9419cd5]
- Fix FTBFS due to png code [Bug #595] [Commit #3e27b07f]
- Remove version.h. Cruft from an older version prior to 0.9.6.
- Fix usage of obsolete libpng jmpbuf member [Commit #7d0d82b7]
- GCC 4.7 fix. [Bug #958] [Commit #a9489034]
- GCC 4.7 fix. [Bug #958] [Commit #a209c81b]
- Fix 'format not a string literal' error [Commit #029218cd]
- Update patch in GIT hash a9489034 to use reinterpret_cast. [Commit #5a043853]
- Fix FTBFS on png >= 0.15 [Commit #18ecd512]

* Sun Jul 08 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.6-3
- Fix man directory location
- Fix postinstall
- Fix description
- Add "BuildRequires: exiv2-devel"

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.6-2
- gcc 4.7 + libpng 1.5 patch for digikam (consolidated) [Bug #958]

* Sun Nov 06 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.6-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

