# Default version for this component
%define kdecomp koffice

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

# Disable Kross support for RHEL <= 5 (python is too old)
%if 0%{?fedora} > 0 || 0%{?rhel} >= 6 || 0%{?mgaversion} || 0%{?mdkversion}
%define with_kross 1
%endif

%if 0%{?fedora} >= 17
%define with_ruby 0
%else
%define with_ruby 1
%endif

# Ruby 1.9 includes are located in strance directories ... (taken from ruby 1.9 spec file)
%global	_normalized_cpu	%(echo %{_target_cpu} | sed 's/^ppc/powerpc/;s/i.86/i386/;s/sparcv./sparc/;s/armv.*/arm/')


Name:		trinity-%{kdecomp}
Summary:	An integrated office suite
Version:	1.6.3
Release:	5%{?dist}%{?_variant}

Group:          Applications/Productivity
License:        GPLv2+

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Source100:      koshell.png

# [lib/kross/python/scripts/RestrictedPython/Utilities.py] Syntax error [Bug #679]
Patch2:		koffice-3.5.13-kross_utilities_syntax.patch
# [koffice/chalk] Fix GraphicksMagick 1.3 support [Bug #353]
Patch3:		koffice-3.5.13-chalk_gmagick.patch
# [koffice/kexi] Various patches for kexi, found on the web [Bug # 777]
Patch5:		kexi-fix-possible-crash-in-buffered-mode-sqlite-2.patch
Patch6:		kexi-hide_hourglass-1.1.3-2.patch
Patch7:		kexi-fix-support-for-boolean-types-in-migration.patch
Patch8:		kexi-mysql_migrate_long_text-1.1.3.patch
Patch9:		kexi-fix-support-for-boolean-types.patch
Patch10:	kexi-thoushand_objects_support-1.1.3-2.patch
Patch11:	kexi-fp_expressions-1.1.3.patch
# [koffice] Fix compilation with GCC 4.7 [Bug #958]
Patch12:	koffice-3.5.13-fix_gcc47_compilation.patch
# [koffice] Fix compilation with Ruby 1.9 [Bug #735]
Patch13:	koffice-3.5.13-fix_ruby_1.9.patch 
# [koffice] Fix compilation with libpng [Bug #603]
Patch14:	koffice-3.5.13-fix_libpng.patch
# [koffice] Fix FTBFS due to missing libraries [Bug #657] [Commit #5c69fcd3]
#  Clean up lib paths in LDFLAGS - moved to LIBADD
#  For KWord and and KPresenter added linking kspell2
#  For KSpread added linking kutils
Patch15:	koffice-3.5.13-fix_bug_657.patch
# [koffice] Fix accidental conversions of binary files [Bug #1033] [Commit #dbe89307]
Source1:	koffice-3.5.13-damaged_binary_files.tar.gz
# [koffice] Missing LDFLAGS cause FTBFS on Mageia / Mandriva
Patch16:	koffice-3.5.13-missing_ldflags.patch

# BuildRequires: world-devel ;)
BuildRequires:  trinity-tdelibs-devel
BuildRequires:  trinity-tdegraphics-devel
BuildRequires:  automake libtool
BuildRequires:  freetype-devel
BuildRequires:  fontconfig-devel
BuildRequires:  libart_lgpl-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libjpeg-devel
BuildRequires:  ImageMagick-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  python-devel
BuildRequires:  pcre-devel
BuildRequires:  lcms-devel
BuildRequires:  gettext-devel
BuildRequires:  mysql-devel
BuildRequires:  desktop-file-utils
BuildRequires:  perl
BuildRequires:  doxygen
BuildRequires:  aspell-devel
BuildRequires:  libxslt-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  libexif-devel
BuildRequires:  readline-devel
%if 0%{?with_ruby}
BuildRequires:  ruby ruby-devel >= 1.8.2
%endif
BuildRequires:  libpaper-devel
BuildRequires:	libutempter-devel
BuildRequires:	GraphicsMagick-devel >= 1.1.0

BuildRequires:	trinity-tdegraphics-libpoppler-tqt-devel

# These libraries are either too old or too recent on distributions !
# We always provide our versions with TDE...
BuildRequires:	trinity-libwpd-devel
BuildRequires:  trinity-libpqxx-devel

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}mesagl1-devel
BuildRequires:	%{_lib}mesaglu1-devel
BuildRequires:	%{_lib}xi-devel
BuildRequires:  wv2-devel
%else
BuildRequires:  libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:  libXi-devel
BuildRequires:  trinity-wv2-devel
%endif

%description
KOffice is an integrated office suite.

%package suite
Summary:        An integrated office suite
Group:          Applications/Productivity
Obsoletes:      %{name} <= %{version}-%{release}
Obsoletes:      %{name}-i18n < 4:%{version}
Requires:       %{name}-core = %{version}-%{release} 
Requires:       %{name}-kword = %{version}-%{release} 
Requires:       %{name}-kspread = %{version}-%{release} 
Requires:       %{name}-kpresenter = %{version}-%{release}
Requires:       %{name}-kivio = %{version}-%{release}
Requires:       %{name}-karbon = %{version}-%{release}
Requires:       %{name}-kugar = %{version}-%{release}
Requires:       %{name}-kexi = %{version}-%{release}
Requires:       %{name}-kexi-driver-mysql = %{version}-%{release}
Requires:       %{name}-kexi-driver-pgsql = %{version}-%{release}
Requires:       %{name}-kchart = %{version}-%{release}
Requires:       %{name}-kformula = %{version}-%{release}
Requires:       %{name}-filters = %{version}-%{release}
Requires:       %{name}-kplato = %{version}-%{release}
Requires:       %{name}-chalk = %{version}-%{release}

%description suite
KOffice is an integrated office suite.

%package core
Summary:        Core support files for %{name} 
Group:          Applications/Productivity
Requires:       %{name}-libs = %{version}-%{release}
Requires:       perl
Conflicts:      koffice-i18n < %{version}
%description core
%{summary}.

%package libs
Summary:        Runtime libraries for %{name} 
Group:          System Environment/Libraries
Conflicts:      %{name} <= %{version}-%{release}
Requires:       trinity-kdelibs
License:        LGPLv2+
%description libs
%{summary}.

%package devel
Summary:        Development files for %{name} 
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}
License:        LGPLv2+
%description devel
%{summary}.

%package kword
Summary:	A frame-based word processor capable of professional standard documents
Group:          Applications/Productivity
Requires:       %{name}-core = %{version}-%{release}
%description kword
%{summary}.

%package kspread
Summary:        A powerful spreadsheet application
Group:          Applications/Productivity
Requires:       %{name}-core = %{version}-%{release}
%description kspread
%{summary}.

%package kpresenter
Summary:        A full-featured presentation program
Group:          Applications/Productivity
Requires:       %{name}-core = %{version}-%{release}
%description kpresenter
%{summary}.

%package kivio
Summary:        A flowcharting application
Group:          Applications/Productivity
Requires:       %{name}-core = %{version}-%{release}
Obsoletes:      kivio < %{version}-%{release}
%description kivio
%{summary}.

%package karbon
Summary:        A vector drawing application
Group:          Applications/Productivity
Requires:       %{name}-core = %{version}-%{release}
%description karbon
%{summary}.

%package kugar
Summary:        A tool for generating business quality reports
Group:          Applications/Productivity
Requires:       %{name}-core = %{version}-%{release}
%description kugar
%{summary}.

%package kexi
Summary:        An integrated environment for managing data
Group:          Applications/Productivity
Requires:       %{name}-core = %{version}-%{release}
%description kexi
%{summary}.
For additional database drivers take a look at %{name}-kexi-driver-*

%package kexi-driver-mysql
Summary:        Mysql-driver for kexi
Group:          Applications/Productivity
Requires:       %{name}-kexi = %{version}-%{release}
%description kexi-driver-mysql
%{summary}.

%package kexi-driver-pgsql
Summary:        Postgresql driver for kexi
Group:          Applications/Productivity
Requires:       %{name}-kexi = %{version}-%{release}
%description kexi-driver-pgsql
%{summary}.

%package kchart
Summary:        An integrated graph and chart drawing tool
Group:          Applications/Productivity
Requires:       %{name}-core = %{version}-%{release}
%description kchart
%{summary}.

%package kformula
Summary:        A powerful formula editor
Group:          Applications/Productivity
Requires:       %{name}-core = %{version}-%{release}

%if 0%{?mgaversion} || 0%{?mdkversion}
Requires:		fonts-ttf-dejavu
%else
Requires:       lyx-cmex10-fonts
%if 0%{?fedora} >= 11 || 0%{?rhel} >= 6
Requires:       dejavu-lgc-sans-fonts
%else
Requires:       dejavu-lgc-fonts 
%endif
%endif

%description kformula
%{summary}.

%package filters
Summary:        Import and Export Filters for KOffice
Group:          Applications/Productivity
Requires:       %{name}-core = %{version}-%{release}
%description filters
%{summary}.

%package kplato
Summary:         An integrated project management and planning tool
Group:           Applications/Productivity
Requires:        %{name}-core = %{version}-%{release}
%description kplato
%{summary}.

%package chalk
Summary:		 pixel-based image manipulation program for the TDE Office Suite [Trinity]
Group:           Applications/Productivity
Requires:        %{name}-core = %{version}-%{release}
Requires:        %{name}-chalk-data = %{version}-%{release}
Requires:        %{name}-filters
%description chalk
Chalk is a painting and image editing application for KOffice. Chalk contains
both ease-of-use and fun features like guided painting.

This package is part of the TDE Office Suite.

%package chalk-data
Summary:		data files for Chalk painting program [Trinity]
Group:           Applications/Productivity
%description chalk-data
This package contains architecture-independent data files for Chalk,
the painting program shipped with the TDE Office Suite.

See the chalk package for further information.

This package is part of the TDE Office Suite.



%prep
%setup -q -n applications/%{kdecomp}
%setup -q -n applications/%{kdecomp} -a 1

#patch0 -p1
#patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p0
%patch12 -p1 -b .gcc47
%if 0%{?fedora} >= 17
%patch13 -p1 -b .ruby
%patch14 -p1 -b .libpng
%endif
%patch15 -p1
%patch16 -p1

# use LGC variant instead
%__sed -i.dejavu-lgc \
  -e 's|DejaVu Sans|DejaVu LGC Sans|' \
  -e 's|dejavu sans|dejavu lgc sans|' \
  lib/kformula/{contextstyle,fontstyle,symboltable}.cc 

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  --disable-rpath --disable-dependency-tracking \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --with-pic --enable-shared --disable-static \
  --with-extra-libs=%{tde_libdir} \
  --enable-final \
  --with-extra-includes=%{tde_includedir}/tqt:%{tde_includedir}/arts \
  --enable-closure \
  --disable-kexi-macros \
  --with-pqxx-includes=%{tde_includedir} \
  --with-pqxx-libraries=%{tde_libdir} \
%if 0%{?with_kross} > 0
  --enable-scripting \
%else
  --disable-scripting \
%endif

%__make %{?_smp_mflags}


%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

[ ! -f %{buildroot}%{tde_datadir}/icons/hicolor/48x48/apps/koshell.png ] && \
%__install -p -D -m644 %{SOURCE100} %{buildroot}%{tde_datadir}/icons/hicolor/48x48/apps/koshell.png

# Replace absolute symlinks with relative ones
pushd %{buildroot}%{tde_tdedocdir}/HTML
for lang in *; do
  if [ -d $lang ]; then
    pushd $lang
    for i in */*; do
      [ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../../common $i/common
    done
    popd
  fi
done
popd

desktop-file-install \
  --dir=%{buildroot}%{tde_tdeappdir} \
  --vendor="" \
  --delete-original \
  %{buildroot}%{tde_datadir}/applnk/Office/*.desktop

## Hack-in NoDisplay=True (http://bugzilla.redhat.com/245061)
## until http://bugzilla.redhat.com/245190 is fixed
%if 0%{?rhel} || 0%{?fedora}
for desktop_file in %{buildroot}%{tde_datadir}/applnk/.hidden/*.desktop ; do
  grep "^NoDisplay=" ${desktop_file} || \
    echo "NoDisplay=True" >> ${desktop_file}
done
%endif

## unpackaged files
# fonts
rm -rfv %{buildroot}%{tde_datadir}/apps/kformula/fonts/
# libtool archives
rm -f %{buildroot}%{tde_libdir}/lib*.la
# shouldn't these be in koffice-l10n? 
rm -f %{buildroot}%{tde_datadir}/locale/pl/LC_MESSAGES/kexi_{add,delete}_column_gui_transl_pl.sh
# -devel symlinks to nuke
rm -f %{buildroot}%{tde_libdir}/lib*common.so
rm -f %{buildroot}%{tde_libdir}/lib*filters.so
rm -f %{buildroot}%{tde_libdir}/lib*private.so
rm -f %{buildroot}%{tde_libdir}/libkarbon*.so
rm -f %{buildroot}%{tde_libdir}/libkchart*.so
rm -f %{buildroot}%{tde_libdir}/libkexi*.so
rm -f %{buildroot}%{tde_libdir}/libkisexiv2.so
rm -f %{buildroot}%{tde_libdir}/libkformdesigner.so
rm -f %{buildroot}%{tde_libdir}/libkplato*.so
rm -f %{buildroot}%{tde_libdir}/libkpresenter*.so
rm -f %{buildroot}%{tde_libdir}/libkword*.so
rm -f %{buildroot}%{tde_libdir}/libkross*.so
rm -f %{buildroot}%{tde_libdir}/libkugar*.so


%clean
%__rm -rf %{buildroot}

%post core
touch --no-create %{tde_datadir}/icons/crystalsvg &> /dev/null || :
touch --no-create %{tde_datadir}/icons/hicolor &> /dev/null || :
touch --no-create %{tde_datadir}/icons/locolor &> /dev/null || :

%postun core
if [ $1 -eq 0 ]; then
  gtk-update-icon-cache %{tde_datadir}/icons/crystalsvg &> /dev/null || :
  gtk-update-icon-cache %{tde_datadir}/icons/hicolor &> /dev/null || :
  gtk-update-icon-cache %{tde_datadir}/icons/locolor &> /dev/null || :
  update-desktop-database -q &> /dev/null ||:
fi

%posttrans core
gtk-update-icon-cache %{tde_datadir}/icons/crystalsvg &> /dev/null || :
gtk-update-icon-cache %{tde_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{tde_datadir}/icons/locolor &> /dev/null || :
update-desktop-database -q &> /dev/null ||:

%post karbon
/sbin/ldconfig || :

%postun karbon
/sbin/ldconfig || :

%post kword
/sbin/ldconfig || :

%postun kword
/sbin/ldconfig || :

%posttrans kword
update-desktop-database -q &> /dev/null ||:

%post kpresenter
/sbin/ldconfig || :

%postun kpresenter
/sbin/ldconfig || :

%posttrans kpresenter
update-desktop-database -q &> /dev/null ||:

%post kugar
/sbin/ldconfig || :

%postun kugar
/sbin/ldconfig || :

%posttrans kugar
update-desktop-database -q &> /dev/null ||:

%post kexi
/sbin/ldconfig || :

%postun kexi
/sbin/ldconfig || :

%posttrans kexi
update-desktop-database -q &> /dev/null ||:

%post kchart
/sbin/ldconfig || :

%postun kchart
/sbin/ldconfig || :

%posttrans kchart
update-desktop-database -q &> /dev/null ||:

%post filters
/sbin/ldconfig || :

%postun filters
/sbin/ldconfig || :

%post libs
/sbin/ldconfig || :

%postun libs
/sbin/ldconfig || :

%post chalk
/sbin/ldconfig || :

%postun chalk
/sbin/ldconfig || :

%posttrans chalk
update-desktop-database -q &> /dev/null ||:

%files suite
#empty => virtual package

%files core
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{tde_bindir}/koshell
%{tde_bindir}/kthesaurus
%{tde_bindir}/koconverter
%{tde_libdir}/libkdeinit_koshell.so
%{tde_libdir}/libkdeinit_kthesaurus.so
%{tde_tdelibdir}/kfile_koffice.*
%{tde_tdelibdir}/kfile_ooo.*
%{tde_tdelibdir}/kfile_abiword.*
%{tde_tdelibdir}/kfile_gnumeric.*
%{tde_tdelibdir}/kodocinfopropspage.*
%{tde_tdelibdir}/kofficescan.*
%{tde_tdelibdir}/kofficethumbnail.*
%{tde_tdelibdir}/koshell.*
%{tde_tdelibdir}/kthesaurus.*
%{tde_tdelibdir}/kwmailmerge_classic.*
%{tde_tdelibdir}/kwmailmerge_kabc.*
%{tde_tdelibdir}/kwmailmerge_qtsqldb_power.*
%{tde_tdelibdir}/kwmailmerge_qtsqldb.*
%{tde_tdelibdir}/libkounavailpart.*
%{tde_tdelibdir}/libkprkword.*
%{tde_tdelibdir}/libthesaurustool.*
%{tde_tdelibdir}/clipartthumbnail.*
%{tde_datadir}/apps/koffice/
%{tde_datadir}/apps/konqueror/servicemenus/*
%{tde_datadir}/apps/koshell/
%{tde_datadir}/apps/thesaurus/
%{tde_datadir}/config.kcfg/koshell.kcfg
%{tde_tdedocdir}/HTML/en/koffice/
%{tde_tdedocdir}/HTML/en/koshell/
%{tde_tdedocdir}/HTML/en/thesaurus/
%{tde_datadir}/icons/crystalsvg/*/*/*
%{tde_datadir}/icons/hicolor/*/*/*
%{tde_datadir}/icons/locolor/*/*/*
%{tde_datadir}/services/clipartthumbnail.desktop
%{tde_datadir}/services/kfile*.desktop
%{tde_datadir}/services/kwmailmerge*.desktop
%{tde_datadir}/services/kodocinfopropspage.desktop
%{tde_datadir}/services/kofficethumbnail.desktop
%{tde_datadir}/services/kounavail.desktop
%{tde_datadir}/services/kprkword.desktop
%{tde_datadir}/services/thesaurustool.desktop
%{tde_datadir}/servicetypes/kochart.desktop
%{tde_datadir}/servicetypes/kofficepart.desktop
%{tde_datadir}/servicetypes/koplugin.desktop
%{tde_datadir}/servicetypes/kwmailmerge.desktop
%{tde_datadir}/servicetypes/widgetfactory.desktop
%{tde_tdeappdir}/*koffice.desktop
%{tde_tdeappdir}/*KThesaurus.desktop
%{tde_tdeappdir}/*koshell.desktop
%{tde_datadir}/apps/kofficewidgets/
%if 0%{?with_kross} > 0
%{tde_datadir}/apps/kross/
%{tde_tdelibdir}/krosspython.*
%if 0%{?with_ruby}
%{tde_tdelibdir}/krossruby.*
%endif
%endif

%files libs
%defattr(-,root,root,-)
%doc COPYING.LIB
#_libdir/libk*common.so.*
%{tde_libdir}/libkarboncommon.so.*
%{tde_libdir}/libkspreadcommon.so.*
%{tde_libdir}/libkdchart.so.*
%{tde_libdir}/libkochart.so.*
%{tde_libdir}/libkofficecore.so.*
%{tde_libdir}/libkofficeui.so.*
%{tde_libdir}/libkotext.so.*
%{tde_libdir}/libkowmf.so.*
%{tde_libdir}/libkopainter.so.*
%{tde_libdir}/libkstore.so.*
%{tde_libdir}/libkwmailmerge_interface.so.*
%{tde_libdir}/libkwmf.so.*
%{tde_libdir}/libkformulalib.so.*
%{tde_libdir}/libkopalette.so.*
%{tde_libdir}/libkoproperty.so.*
%if 0%{?with_kross} > 0
%{tde_libdir}/libkrossapi.so.*
%{tde_libdir}/libkrossmain.so.*
%endif

%files devel
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/koffice-apidocs/
%{tde_includedir}/*
# FIXME: include only shlib symlinks we know/want to export
%{tde_libdir}/lib*.so
%exclude %{tde_libdir}/libkdeinit_*.so
%exclude %{tde_libdir}/libkudesignercore.so

%files kword
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kword/
%{tde_bindir}/kword
%{tde_libdir}/libkdeinit_kword.so
%{tde_libdir}/libkwordprivate.so.*
%{tde_tdelibdir}/libkwordpart.*
%{tde_tdelibdir}/kword.*
%{tde_datadir}/apps/kword/
%{tde_datadir}/services/kword*.desktop
%{tde_datadir}/services/kwserial*.desktop
%{tde_datadir}/templates/TextDocument.desktop
%{tde_datadir}/templates/.source/TextDocument.kwt
%{tde_tdeappdir}/*kword.desktop

%files kspread
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kspread/
%{tde_bindir}/kspread
%{tde_libdir}/libkdeinit_kspread.so
%{tde_tdelibdir}/kspread.*
%{tde_tdelibdir}/libkspreadpart.*
%{tde_tdelibdir}/kwmailmerge_kspread.*
%{tde_tdelibdir}/libcsvexport.*
%{tde_tdelibdir}/libcsvimport.*
%{tde_tdelibdir}/libgnumericexport.*
%{tde_tdelibdir}/libgnumericimport.*
%{tde_tdelibdir}/libkspreadhtmlexport.*
%{tde_tdelibdir}/libkspreadinsertcalendar.*
%{tde_tdelibdir}/libopencalcexport.*
%{tde_tdelibdir}/libopencalcimport.*
%{tde_tdelibdir}/libqproimport.*
%{tde_datadir}/apps/kspread/
%{tde_datadir}/services/kspread*.desktop
%{tde_datadir}/templates/SpreadSheet.desktop
%{tde_datadir}/templates/.source/SpreadSheet.kst
%{tde_tdeappdir}/*kspread.desktop
%if 0%{?with_kross} > 0
%{tde_tdelibdir}/kspreadscripting.*
%{tde_tdelibdir}/krosskspreadcore.*
%endif

%files kpresenter
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kpresenter/
%{tde_bindir}/kpresenter
%{tde_bindir}/kprconverter.pl
%{tde_libdir}/libkdeinit_kpresenter.so
%{tde_libdir}/libkpresenterimageexport.so.*
%{tde_libdir}/libkpresenterprivate.so.*
%{tde_tdelibdir}/*kpresenter*.*
%{tde_datadir}/apps/kpresenter/
%{tde_datadir}/services/kpresenter*.desktop
%{tde_datadir}/templates/Presentation.desktop
%{tde_datadir}/templates/.source/Presentation.kpt
%{tde_tdeappdir}/*kpresenter.desktop

%files karbon
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/karbon/
%{tde_bindir}/karbon
%{tde_libdir}/libkdeinit_karbon.so
%{tde_tdelibdir}/*karbon*.*
%{tde_tdelibdir}/libwmfexport.*
%{tde_tdelibdir}/libwmfimport.*
%{tde_datadir}/apps/karbon/
%{tde_datadir}/services/karbon*
%{tde_datadir}/servicetypes/karbon_module.desktop
%{tde_datadir}/templates/Illustration.desktop
%{tde_datadir}/templates/.source/Illustration.karbon
%{tde_tdeappdir}/*karbon.desktop

%files kugar
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kugar/
%{tde_bindir}/kugar
%{tde_bindir}/kudesigner
%{tde_libdir}/libkdeinit_kugar.so
%{tde_libdir}/libkdeinit_kudesigner.so
%{tde_libdir}/libkugarlib.so.*
%{tde_libdir}/libkudesignercore.so
%{tde_tdelibdir}/kudesigner.*
%{tde_tdelibdir}/kugar.*
%{tde_tdelibdir}/libkudesignerpart.*
%{tde_tdelibdir}/libkugarpart.*
%{tde_datadir}/apps/kudesigner/
%{tde_datadir}/apps/kugar/
%{tde_datadir}/services/kugar*.desktop
%{tde_tdeappdir}/*kugar.desktop
%{tde_tdeappdir}/*kudesigner.desktop

%files kexi
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kexi/
%{tde_bindir}/kexi*
%{tde_bindir}/ksqlite*
%{tde_libdir}/libkdeinit_kexi.so
%{tde_libdir}/libkexi*.so.*
%{tde_libdir}/libkformdesigner.so.*
%{tde_tdelibdir}/kformdesigner_*.*
%{tde_tdelibdir}/kexidb_sqlite2driver.*
%{tde_tdelibdir}/kexidb_sqlite3driver.*
%{tde_tdelibdir}/kexihandler_*.*
%{tde_tdelibdir}/kexi.*
# moved here to workaround bug #394101, alternative is to move libkexi(db|dbparser|utils) to -libs)
%{tde_tdelibdir}/libkspreadkexiimport.*
%{tde_datadir}/config/kexirc
%{tde_datadir}/config/magic/kexi.magic
%{tde_datadir}/mimelnk/application/*
%{tde_datadir}/servicetypes/kexi*.desktop
%{tde_datadir}/services/kexi/
%{tde_datadir}/apps/kexi/
%{tde_datadir}/services/kformdesigner/*
%{tde_tdeappdir}/*kexi.desktop
%{tde_datadir}/services/kexidb_sqlite*driver.desktop
%if 0%{?with_kross} > 0
%{tde_bindir}/krossrunner
%{tde_tdelibdir}/krosskexiapp.*
%{tde_tdelibdir}/krosskexidb.*
%endif

%files kexi-driver-mysql
%defattr(-,root,root,-)
%{tde_tdelibdir}/kexidb_mysqldriver.*
%{tde_tdelibdir}/keximigrate_mysql.*
%{tde_datadir}/services/keximigrate_mysql.desktop
%{tde_datadir}/services/kexidb_mysqldriver.desktop

%files kexi-driver-pgsql
%defattr(-,root,root,-)
%{tde_tdelibdir}/kexidb_pqxxsqldriver.*
%{tde_tdelibdir}/keximigrate_pqxx.*
%{tde_datadir}/services/kexidb_pqxxsqldriver.desktop
%{tde_datadir}/services/keximigrate_pqxx.desktop

%files kchart
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kchart/
%{tde_bindir}/kchart
%{tde_libdir}/libkchart*.so.*
%{tde_libdir}/libkdeinit_kchart.so
%{tde_tdelibdir}/*kchart*.*
%{tde_datadir}/apps/kchart/
%{tde_datadir}/services/kchart*.desktop
%{tde_tdeappdir}/*kchart.desktop

%files kformula
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kformula/
%{tde_bindir}/kformula
%{tde_libdir}/libkdeinit_kformula.so
%{tde_tdelibdir}/*kformula*.*
%{tde_datadir}/apps/kformula/
%{tde_datadir}/services/kformula*.desktop
%{tde_tdeappdir}/*kformula.desktop

%files kivio
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kivio/
%{tde_bindir}/kivio
%{tde_libdir}/libkdeinit_kivio.so
%{tde_libdir}/libkiviocommon.so.*
%{tde_tdelibdir}/*kivio*.*
%{tde_tdelibdir}/straight_connector.*
%{tde_datadir}/apps/kivio/
%{tde_datadir}/config.kcfg/kivio.kcfg
%{tde_datadir}/services/kivio*.desktop
%{tde_tdeappdir}/*kivio.desktop

%files filters
%defattr(-,root,root,-)
%{tde_libdir}/libkwordexportfilters.so.*
%{tde_tdelibdir}/libabiwordexport.*
%{tde_tdelibdir}/libabiwordimport.*
%{tde_tdelibdir}/libamiproexport.*
%{tde_tdelibdir}/libamiproimport.*
%{tde_tdelibdir}/libapplixspreadimport.*
%{tde_tdelibdir}/libapplixwordimport.*
%{tde_tdelibdir}/libasciiexport.*
%{tde_tdelibdir}/libasciiimport.*
%{tde_tdelibdir}/libdbaseimport.*
%{tde_tdelibdir}/libdocbookexport.*
%{tde_tdelibdir}/libexcelimport.*
%{tde_tdelibdir}/libgenerickofilter.*
%{tde_tdelibdir}/libhtmlexport.*
%{tde_tdelibdir}/libhtmlimport.*
%{tde_tdelibdir}/libkarbonepsimport.*
%{tde_tdelibdir}/libkfolatexexport.*
%{tde_tdelibdir}/libkfomathmlexport.*
%{tde_tdelibdir}/libkfomathmlimport.*
%{tde_tdelibdir}/libkfopngexport.*
%{tde_tdelibdir}/libkspreadlatexexport.*
%{tde_tdelibdir}/libkugarnopimport.*
%{tde_tdelibdir}/libkwordkword1dot3import.*
%{tde_tdelibdir}/libkwordlatexexport.*
%{tde_tdelibdir}/libmswriteexport.*
%{tde_tdelibdir}/libmswriteimport.*
%{tde_tdelibdir}/libooimpressexport.*
%{tde_tdelibdir}/libooimpressimport.*
%{tde_tdelibdir}/liboowriterexport.*
%{tde_tdelibdir}/liboowriterimport.*
%{tde_tdelibdir}/libpalmdocexport.*
%{tde_tdelibdir}/libpalmdocimport.*
%{tde_tdelibdir}/libpdfimport.*
%{tde_tdelibdir}/librtfexport.*
%{tde_tdelibdir}/librtfimport.*
%{tde_tdelibdir}/libwmlexport.*
%{tde_tdelibdir}/libwmlimport.*
%{tde_tdelibdir}/libwpexport.*
%{tde_tdelibdir}/libwpimport.*
%{tde_tdelibdir}/libmswordimport.*
%{tde_tdelibdir}/libxsltimport.*
%{tde_tdelibdir}/libxsltexport.*
%{tde_tdelibdir}/libhancomwordimport.*
%{tde_tdelibdir}/libkfosvgexport.*
%{tde_tdelibdir}/liboodrawimport.*
%{tde_tdelibdir}/libolefilter.*
%{tde_datadir}/apps/xsltfilter/
%{tde_datadir}/services/generic_filter.desktop
%{tde_datadir}/services/ole_powerpoint97_import.desktop
%{tde_datadir}/services/xslt*.desktop
%{tde_datadir}/servicetypes/kofilter*.desktop

%files kplato
%defattr(-,root,root,-)
%lang(en) %{tde_tdedocdir}/HTML/en/kplato/
%{tde_bindir}/kplato
%{tde_libdir}/libkdeinit_kplato.so
%{tde_tdelibdir}/kplato.*
%{tde_tdelibdir}/libkplatopart.*
%{tde_datadir}/apps/kplato/
%{tde_datadir}/services/kplatopart.desktop
%{tde_tdeappdir}/*kplato.desktop

%files chalk
%defattr(-,root,root,-)
%{tde_bindir}/chalk
%{tde_tdelibdir}/chalkblurfilter.la
%{tde_tdelibdir}/chalkblurfilter.so
%{tde_tdelibdir}/chalkbumpmap.la
%{tde_tdelibdir}/chalkbumpmap.so
%{tde_tdelibdir}/chalkcimg.la
%{tde_tdelibdir}/chalkcimg.so
%{tde_tdelibdir}/chalk_cmyk_*
%{tde_tdelibdir}/chalkcmykplugin.la
%{tde_tdelibdir}/chalkcmykplugin.so
%{tde_tdelibdir}/chalkcolorify.la
%{tde_tdelibdir}/chalkcolorify.so
%{tde_tdelibdir}/chalkcolorrange.la
%{tde_tdelibdir}/chalkcolorrange.so
%{tde_tdelibdir}/chalkcolorsfilters.la
%{tde_tdelibdir}/chalkcolorsfilters.so
%{tde_tdelibdir}/chalkcolorspaceconversion.la
%{tde_tdelibdir}/chalkcolorspaceconversion.so
%{tde_tdelibdir}/chalkconvolutionfilters.la
%{tde_tdelibdir}/chalkconvolutionfilters.so
%{tde_tdelibdir}/chalkdefaultpaintops.la
%{tde_tdelibdir}/chalkdefaultpaintops.so
%{tde_tdelibdir}/chalkdefaulttools.la
%{tde_tdelibdir}/chalkdefaulttools.so
%{tde_tdelibdir}/chalkdropshadow.la
%{tde_tdelibdir}/chalkdropshadow.so
%{tde_tdelibdir}/chalkembossfilter.la
%{tde_tdelibdir}/chalkembossfilter.so
%{tde_tdelibdir}/chalkexample.la
%{tde_tdelibdir}/chalkexample.so
%{tde_tdelibdir}/chalkextensioncolorsfilters.la
%{tde_tdelibdir}/chalkextensioncolorsfilters.so
%{tde_tdelibdir}/chalkfastcolortransfer.la
%{tde_tdelibdir}/chalkfastcolortransfer.so
%{tde_tdelibdir}/chalkfiltersgallery.la
%{tde_tdelibdir}/chalkfiltersgallery.so
%{tde_tdelibdir}/chalk_gray_*
%{tde_tdelibdir}/chalkgrayplugin.la
%{tde_tdelibdir}/chalkgrayplugin.so
%{tde_tdelibdir}/chalkhistogramdocker.la
%{tde_tdelibdir}/chalkhistogramdocker.so
%{tde_tdelibdir}/chalkhistogram.la
%{tde_tdelibdir}/chalkhistogram.so
%{tde_tdelibdir}/chalkimageenhancement.la
%{tde_tdelibdir}/chalkimageenhancement.so
%{tde_tdelibdir}/chalkimagesize.la
%{tde_tdelibdir}/chalkimagesize.so
%{tde_tdelibdir}/chalk.la
%{tde_tdelibdir}/chalklenscorrectionfilter.la
%{tde_tdelibdir}/chalklenscorrectionfilter.so
%{tde_tdelibdir}/chalklevelfilter.la
%{tde_tdelibdir}/chalklevelfilter.so
%{tde_tdelibdir}/chalk_lms_*
%{tde_tdelibdir}/chalkmodifyselection.la
%{tde_tdelibdir}/chalkmodifyselection.so
%{tde_tdelibdir}/chalknoisefilter.la
%{tde_tdelibdir}/chalknoisefilter.so
%{tde_tdelibdir}/chalkoilpaintfilter.la
%{tde_tdelibdir}/chalkoilpaintfilter.so
%{tde_tdelibdir}/chalkpixelizefilter.la
%{tde_tdelibdir}/chalkpixelizefilter.so
%{tde_tdelibdir}/chalkraindropsfilter.la
%{tde_tdelibdir}/chalkraindropsfilter.so
%{tde_tdelibdir}/chalkrandompickfilter.la
%{tde_tdelibdir}/chalkrandompickfilter.so
%{tde_tdelibdir}/chalk_rgb_*
%{tde_tdelibdir}/chalkrgbplugin.la
%{tde_tdelibdir}/chalkrgbplugin.so
%{tde_tdelibdir}/chalkrotateimage.la
%{tde_tdelibdir}/chalkrotateimage.so
%{tde_tdelibdir}/chalkroundcornersfilter.la
%{tde_tdelibdir}/chalkroundcornersfilter.so
%{tde_tdelibdir}/chalkselectiontools.la
%{tde_tdelibdir}/chalkselectiontools.so
%{tde_tdelibdir}/chalkselectopaque.la
%{tde_tdelibdir}/chalkselectopaque.so
%{tde_tdelibdir}/chalkseparatechannels.la
%{tde_tdelibdir}/chalkseparatechannels.so
%{tde_tdelibdir}/chalkshearimage.la
%{tde_tdelibdir}/chalkshearimage.so
%{tde_tdelibdir}/chalksmalltilesfilter.la
%{tde_tdelibdir}/chalksmalltilesfilter.so
%{tde_tdelibdir}/chalk.so
%{tde_tdelibdir}/chalkscreenshot.la
%{tde_tdelibdir}/chalkscreenshot.so
%{tde_tdelibdir}/chalksobelfilter.la
%{tde_tdelibdir}/chalksobelfilter.so
%{tde_tdelibdir}/chalksubstrate.la
%{tde_tdelibdir}/chalksubstrate.so
%{tde_tdelibdir}/chalktoolcrop.la
%{tde_tdelibdir}/chalktoolcrop.so
%{tde_tdelibdir}/chalktoolcurves.la
%{tde_tdelibdir}/chalktoolcurves.so
%{tde_tdelibdir}/chalktoolfilter.la
%{tde_tdelibdir}/chalktoolfilter.so
%{tde_tdelibdir}/chalktoolperspectivegrid.la
%{tde_tdelibdir}/chalktoolperspectivegrid.so
%{tde_tdelibdir}/chalktoolperspectivetransform.la
%{tde_tdelibdir}/chalktoolperspectivetransform.so
%{tde_tdelibdir}/chalktoolpolygon.la
%{tde_tdelibdir}/chalktoolpolygon.so
%{tde_tdelibdir}/chalktoolpolyline.la
%{tde_tdelibdir}/chalktoolpolyline.so
%{tde_tdelibdir}/chalktoolselectsimilar.la
%{tde_tdelibdir}/chalktoolselectsimilar.so
%{tde_tdelibdir}/chalktoolstar.la
%{tde_tdelibdir}/chalktoolstar.so
%{tde_tdelibdir}/chalktooltransform.la
%{tde_tdelibdir}/chalktooltransform.so
%{tde_tdelibdir}/chalkunsharpfilter.la
%{tde_tdelibdir}/chalkunsharpfilter.so
%{tde_tdelibdir}/chalkwavefilter.la
%{tde_tdelibdir}/chalkwavefilter.so
%{tde_tdelibdir}/chalkwetplugin.la
%{tde_tdelibdir}/chalkwetplugin.so
%{tde_tdelibdir}/chalk_ycbcr_*
%{tde_tdelibdir}/libchalkgmagickexport.la
%{tde_tdelibdir}/libchalkgmagickexport.so
%{tde_tdelibdir}/libchalkgmagickimport.la
%{tde_tdelibdir}/libchalkgmagickimport.so
%{tde_tdelibdir}/libchalkjpegexport.la
%{tde_tdelibdir}/libchalkjpegexport.so
%{tde_tdelibdir}/libchalkjpegimport.la
%{tde_tdelibdir}/libchalkjpegimport.so
%{tde_tdelibdir}/libchalk_openexr_export.la
%{tde_tdelibdir}/libchalk_openexr_export.so
%{tde_tdelibdir}/libchalk_openexr_import.la
%{tde_tdelibdir}/libchalk_openexr_import.so
%{tde_tdelibdir}/libchalkpart.la
%{tde_tdelibdir}/libchalkpart.so
%{tde_tdelibdir}/libchalkpdfimport.la
%{tde_tdelibdir}/libchalkpdfimport.so
%{tde_tdelibdir}/libchalkpngexport.la
%{tde_tdelibdir}/libchalkpngexport.so
%{tde_tdelibdir}/libchalkpngimport.la
%{tde_tdelibdir}/libchalkpngimport.so
%{tde_tdelibdir}/libchalk_raw_import.la
%{tde_tdelibdir}/libchalk_raw_import.so
%{tde_tdelibdir}/libchalktiffexport.la
%{tde_tdelibdir}/libchalktiffexport.so
%{tde_tdelibdir}/libchalktiffimport.la
%{tde_tdelibdir}/libchalktiffimport.so
%{tde_libdir}/libkdeinit_chalk.so
%{tde_libdir}/libchalk_cmyk_*.so.*
%{tde_libdir}/libchalkcolor.so.*
%{tde_libdir}/libchalkcommon.so.*
%{tde_libdir}/libchalkgrayscale.so.*
%{tde_libdir}/libchalk_gray_*.so.*
%{tde_libdir}/libchalkimage.so.*
%{tde_libdir}/libchalk_lms_*.so.*
%{tde_libdir}/libchalk_rgb_*.so.*
%{tde_libdir}/libchalkrgb.so.*
%{tde_libdir}/libchalkui.so.*
%{tde_libdir}/libchalk_ycbcr_*.so.*
%if 0%{?with_kross} > 0
%{tde_tdelibdir}/krosschalkcore.la
%{tde_tdelibdir}/krosschalkcore.so
%{tde_tdelibdir}/chalkscripting.la
%{tde_tdelibdir}/chalkscripting.so
%{tde_libdir}/libchalkscripting.so.*
%endif

%files chalk-data
%{tde_tdeappdir}/chalk.desktop
%{tde_datadir}/applnk/.hidden/chalk_*.desktop
%{tde_datadir}/apps/konqueror/servicemenus/chalk_konqi.desktop
%{tde_datadir}/apps/chalk
%{tde_datadir}/apps/chalkplugins
%lang(en) %{tde_tdedocdir}/HTML/en/chalk
%{tde_datadir}/icons/hicolor/*/apps/chalk.png
%{tde_datadir}/services/chalk*.desktop
%{tde_datadir}/servicetypes/chalk*.desktop


%changelog
* Sun Jul 08 2012 Francois Andriot <francois.andriot@free.fr> - 1.6.3-5
- Fix kformula dependancies (for RHEL6)
- Fix FTBFS due to missing libraries [Bug #657] [Commit #5c69fcd3]
  Clean up lib paths in LDFLAGS - moved to LIBADD
  For KWord and and KPresenter added linking kspell2
  For KSpread added linking kutils
- Fix accidental conversions of binary files [Bug #1033] [Commit #dbe89307]

* Thu Apr 26 2012 Francois Andriot <francois.andriot@free.fr> - 1.6.3-4
- Updates BuildRequires
- Build for Fedora 17
- Fix compilation with GCC 4.7 [Bug #958]
- Fix compilation with Ruby 1.9 [Bug #735]
- Fix compilation with libpng [Bug #603]

* Sat Jan 07 2012 Francois Andriot <francois.andriot@free.fr> - 1.6.3-3
- Fix GraphicksMagick 1.3 support [Bug #353]
- Various patches for kexi [Bug #777]

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 1.6.3-2
- Fix HTML directory location

* Tue Nov 22 2011 Francois Andriot <francois.andriot@free.fr> - 1.6.3-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
- Based on Spec file from Fedora 11 'koffice-2:1.6.3-25.20090306svn'
- Removed 'krita', added 'chalk'
