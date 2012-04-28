# Default version for this component
%define kdecomp koffice
%define version 1.6.3
%define release 4

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity

# Disable Kross support for RHEL <= 5 (python is too old)
%if 0%{?fedora} > 0 || 0%{?rhel} >= 6
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
Summary:        An integrated office suite
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

Group:          Applications/Productivity
License:        GPLv2+

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Source100:      koshell.png

# [koffice] Disable GraphicksMagick version >= 1.2.0 [Bug #353]
Patch0:		koffice-3.5.13-disable_graphicksmagick.patch
# [filters/chalk/pdf] Fix poppler-qt detection [Bug #783]
Patch1:		koffice-3.5.13-fix_poppler_detect.patch
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

# BuildRequires: world-devel ;)
BuildRequires:  trinity-kdelibs-devel
BuildRequires:  trinity-kdegraphics-devel
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
BuildRequires:  trinity-wv2-devel >= 0.4.0
#BuildRequires:  trinity-libpqxx-devel >= 2.6.0
BuildRequires:  libpqxx-devel
BuildRequires:  doxygen
BuildRequires:  aspell-devel
BuildRequires:  libxslt-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  libexif-devel
BuildRequires:  libGL-devel libGLU-devel
BuildRequires:  readline-devel
%if 0%{?with_ruby}
BuildRequires:  ruby ruby-devel >= 1.8.2
%endif
BuildRequires:  libpaper-devel
BuildRequires:  libXi-devel
BuildRequires:	libutempter-devel
BuildRequires:	poppler-qt-devel >= 0.1.2
BuildRequires:	GraphicsMagick-devel >= 1.1.0
BuildRequires:	trinity-libwpd-devel


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
#if 0%{?fedora} > 9 
Requires:       lyx-cmex10-fonts
#else
#Requires:       mathml-fonts
#endif
%if 0%{?fedora} > 10
Requires:       dejavu-lgc-sans-fonts
%else
Requires:       dejavu-lgc-fonts 
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
%patch13 -p1
%patch14 -p5

# use LGC variant instead
%__sed -i.dejavu-lgc \
  -e 's|DejaVu Sans|DejaVu LGC Sans|' \
  -e 's|dejavu sans|dejavu lgc sans|' \
  lib/kformula/{contextstyle,fontstyle,symboltable}.cc 

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
  --disable-rpath --disable-dependency-tracking \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --with-pic --enable-shared --disable-static \
  --with-extra-libs=%{_libdir} \
  --enable-final \
  --with-extra-includes=%{_includedir}/tqt \
  --enable-closure \
  --disable-kexi-macros \
%if 0%{?with_kross} > 0
  --enable-scripting \
%else
  --disable-scripting \
%endif

%__make %{?_smp_mflags}


%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

[ ! -f %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/koshell.png ] && \
%__install -p -D -m644 %{SOURCE100} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/koshell.png

# Replace absolute symlinks with relative ones
pushd %{buildroot}%{tde_docdir}/HTML
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
  --dir=%{buildroot}%{_datadir}/applications/kde \
  --vendor="" \
  --delete-original \
  %{buildroot}%{_datadir}/applnk/Office/*.desktop

## Hack-in NoDisplay=True (http://bugzilla.redhat.com/245061)
## until http://bugzilla.redhat.com/245190 is fixed
for desktop_file in %{buildroot}%{_datadir}/applnk/.hidden/*.desktop ; do
  grep "^NoDisplay=" ${desktop_file} || \
    echo "NoDisplay=True" >> ${desktop_file}
done

## unpackaged files
# fonts
rm -rfv %{buildroot}%{_datadir}/apps/kformula/fonts/
# libtool archives
rm -f %{buildroot}%{_libdir}/lib*.la
# shouldn't these be in koffice-l10n? 
rm -f %{buildroot}%{_datadir}/locale/pl/LC_MESSAGES/kexi_{add,delete}_column_gui_transl_pl.sh
# -devel symlinks to nuke
rm -f %{buildroot}%{_libdir}/lib*common.so
rm -f %{buildroot}%{_libdir}/lib*filters.so
rm -f %{buildroot}%{_libdir}/lib*private.so
rm -f %{buildroot}%{_libdir}/libkarbon*.so
rm -f %{buildroot}%{_libdir}/libkchart*.so
rm -f %{buildroot}%{_libdir}/libkexi*.so
rm -f %{buildroot}%{_libdir}/libkisexiv2.so
rm -f %{buildroot}%{_libdir}/libkformdesigner.so
rm -f %{buildroot}%{_libdir}/libkplato*.so
rm -f %{buildroot}%{_libdir}/libkpresenter*.so
rm -f %{buildroot}%{_libdir}/libkword*.so
rm -f %{buildroot}%{_libdir}/libkross*.so
rm -f %{buildroot}%{_libdir}/libkugar*.so


%clean
%__rm -rf %{buildroot}

%post core
touch --no-create %{_datadir}/icons/crystalsvg &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
touch --no-create %{_datadir}/icons/locolor &> /dev/null || :

%postun core
if [ $1 -eq 0 ]; then
  gtk-update-icon-cache %{_datadir}/icons/crystalsvg &> /dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/locolor &> /dev/null || :
  update-desktop-database -q &> /dev/null ||:
fi

%posttrans core
gtk-update-icon-cache %{_datadir}/icons/crystalsvg &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/locolor &> /dev/null || :
update-desktop-database -q &> /dev/null ||:

%post kword -p /sbin/ldconfig

%postun kword -p /sbin/ldconfig

%posttrans kword
update-desktop-database -q &> /dev/null ||:

%post kpresenter -p /sbin/ldconfig

%postun kpresenter -p /sbin/ldconfig

%posttrans kpresenter
update-desktop-database -q &> /dev/null ||:

%post kugar -p /sbin/ldconfig

%postun kugar -p /sbin/ldconfig

%posttrans kugar
update-desktop-database -q &> /dev/null ||:

%post kexi -p /sbin/ldconfig

%postun kexi -p /sbin/ldconfig

%posttrans kexi
update-desktop-database -q &> /dev/null ||:

%post kchart -p /sbin/ldconfig

%postun kchart -p /sbin/ldconfig

%posttrans kchart
update-desktop-database -q &> /dev/null ||:

%post filters -p /sbin/ldconfig
%postun filters -p /sbin/ldconfig 

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post chalk -p /sbin/ldconfig

%postun chalk -p /sbin/ldconfig

%posttrans chalk
update-desktop-database -q &> /dev/null ||:

%files suite
#empty => virtual package

%files core
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/koshell
%{_bindir}/kthesaurus
%{_bindir}/koconverter
%{_libdir}/libkdeinit_koshell.so
%{_libdir}/libkdeinit_kthesaurus.so
%{tde_libdir}/kfile_koffice.*
%{tde_libdir}/kfile_ooo.*
%{tde_libdir}/kfile_abiword.*
%{tde_libdir}/kfile_gnumeric.*
%{tde_libdir}/kodocinfopropspage.*
%{tde_libdir}/kofficescan.*
%{tde_libdir}/kofficethumbnail.*
%{tde_libdir}/koshell.*
%{tde_libdir}/kthesaurus.*
%{tde_libdir}/kwmailmerge_classic.*
%{tde_libdir}/kwmailmerge_kabc.*
%{tde_libdir}/kwmailmerge_qtsqldb_power.*
%{tde_libdir}/kwmailmerge_qtsqldb.*
%{tde_libdir}/libkounavailpart.*
%{tde_libdir}/libkprkword.*
%{tde_libdir}/libthesaurustool.*
%{tde_libdir}/clipartthumbnail.*
%{_datadir}/apps/koffice/
%{_datadir}/apps/konqueror/servicemenus/*
%{_datadir}/apps/koshell/
%{_datadir}/apps/thesaurus/
%{_datadir}/config.kcfg/koshell.kcfg
%{tde_docdir}/HTML/en/koffice/
%{tde_docdir}/HTML/en/koshell/
%{tde_docdir}/HTML/en/thesaurus/
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*
%{_datadir}/services/clipartthumbnail.desktop
%{_datadir}/services/kfile*.desktop
%{_datadir}/services/kwmailmerge*.desktop
%{_datadir}/services/kodocinfopropspage.desktop
%{_datadir}/services/kofficethumbnail.desktop
%{_datadir}/services/kounavail.desktop
%{_datadir}/services/kprkword.desktop
%{_datadir}/services/thesaurustool.desktop
%{_datadir}/servicetypes/kochart.desktop
%{_datadir}/servicetypes/kofficepart.desktop
%{_datadir}/servicetypes/koplugin.desktop
%{_datadir}/servicetypes/kwmailmerge.desktop
%{_datadir}/servicetypes/widgetfactory.desktop
%{_datadir}/applications/kde/*koffice.desktop
%{_datadir}/applications/kde/*KThesaurus.desktop
%{_datadir}/applications/kde/*koshell.desktop
%{_datadir}/apps/kofficewidgets/
%if 0%{?with_kross} > 0
%{_datadir}/apps/kross/
%{tde_libdir}/krosspython.*
%if 0%{?with_ruby}
%{tde_libdir}/krossruby.*
%endif
%endif

%files libs
%defattr(-,root,root,-)
%doc COPYING.LIB
#_libdir/libk*common.so.*
%{_libdir}/libkarboncommon.so.*
%{_libdir}/libkspreadcommon.so.*
%{_libdir}/libkdchart.so.*
%{_libdir}/libkochart.so.*
%{_libdir}/libkofficecore.so.*
%{_libdir}/libkofficeui.so.*
%{_libdir}/libkotext.so.*
%{_libdir}/libkowmf.so.*
%{_libdir}/libkopainter.so.*
%{_libdir}/libkstore.so.*
%{_libdir}/libkwmailmerge_interface.so.*
%{_libdir}/libkwmf.so.*
%{_libdir}/libkformulalib.so.*
%{_libdir}/libkopalette.so.*
%{_libdir}/libkoproperty.so.*
%if 0%{?with_kross} > 0
%{_libdir}/libkrossapi.so.*
%{_libdir}/libkrossmain.so.*
%endif

%files devel
%defattr(-,root,root,-)
%lang(en) %{tde_docdir}/HTML/en/koffice-apidocs/
%{_includedir}/*
# FIXME: include only shlib symlinks we know/want to export
%{_libdir}/lib*.so
%exclude %{_libdir}/libkdeinit_*.so
%exclude %{_libdir}/libkudesignercore.so

%files kword
%defattr(-,root,root,-)
%lang(en) %{tde_docdir}/HTML/en/kword/
%{_bindir}/kword
%{_libdir}/libkdeinit_kword.so
%{_libdir}/libkwordprivate.so.*
%{tde_libdir}/libkwordpart.*
%{tde_libdir}/kword.*
%{_datadir}/apps/kword/
%{_datadir}/services/kword*.desktop
%{_datadir}/services/kwserial*.desktop
%{_datadir}/templates/TextDocument.desktop
%{_datadir}/templates/.source/TextDocument.kwt
%{_datadir}/applications/kde/*kword.desktop

%files kspread
%defattr(-,root,root,-)
%lang(en) %{tde_docdir}/HTML/en/kspread/
%{_bindir}/kspread
%{_libdir}/libkdeinit_kspread.so
%{tde_libdir}/kspread.*
%{tde_libdir}/libkspreadpart.*
%{tde_libdir}/kwmailmerge_kspread.*
%{tde_libdir}/libcsvexport.*
%{tde_libdir}/libcsvimport.*
%{tde_libdir}/libgnumericexport.*
%{tde_libdir}/libgnumericimport.*
%{tde_libdir}/libkspreadhtmlexport.*
%{tde_libdir}/libkspreadinsertcalendar.*
%{tde_libdir}/libopencalcexport.*
%{tde_libdir}/libopencalcimport.*
%{tde_libdir}/libqproimport.*
%{_datadir}/apps/kspread/
%{_datadir}/services/kspread*.desktop
%{_datadir}/templates/SpreadSheet.desktop
%{_datadir}/templates/.source/SpreadSheet.kst
%{_datadir}/applications/kde/*kspread.desktop
%if 0%{?with_kross} > 0
%{tde_libdir}/kspreadscripting.*
%{tde_libdir}/krosskspreadcore.*
%endif

%files kpresenter
%defattr(-,root,root,-)
%lang(en) %{tde_docdir}/HTML/en/kpresenter/
%{_bindir}/kpresenter
%{_bindir}/kprconverter.pl
%{_libdir}/libkdeinit_kpresenter.so
%{_libdir}/libkpresenterimageexport.so.*
%{_libdir}/libkpresenterprivate.so.*
%{tde_libdir}/*kpresenter*.*
%{_datadir}/apps/kpresenter/
%{_datadir}/services/kpresenter*.desktop
%{_datadir}/templates/Presentation.desktop
%{_datadir}/templates/.source/Presentation.kpt
%{_datadir}/applications/kde/*kpresenter.desktop

%files karbon
%defattr(-,root,root,-)
%lang(en) %{tde_docdir}/HTML/en/karbon/
%{_bindir}/karbon
%{_libdir}/libkdeinit_karbon.so
%{tde_libdir}/*karbon*.*
%{tde_libdir}/libwmfexport.*
%{tde_libdir}/libwmfimport.*
%{_datadir}/apps/karbon/
%{_datadir}/services/karbon*
%{_datadir}/servicetypes/karbon_module.desktop
%{_datadir}/templates/Illustration.desktop
%{_datadir}/templates/.source/Illustration.karbon
%{_datadir}/applications/kde/*karbon.desktop

%files kugar
%defattr(-,root,root,-)
%lang(en) %{tde_docdir}/HTML/en/kugar/
%{_bindir}/kugar
%{_bindir}/kudesigner
%{_libdir}/libkdeinit_kugar.so
%{_libdir}/libkdeinit_kudesigner.so
%{_libdir}/libkugarlib.so.*
%{_libdir}/libkudesignercore.so
%{tde_libdir}/kudesigner.*
%{tde_libdir}/kugar.*
%{tde_libdir}/libkudesignerpart.*
%{tde_libdir}/libkugarpart.*
%{_datadir}/apps/kudesigner/
%{_datadir}/apps/kugar/
%{_datadir}/services/kugar*.desktop
%{_datadir}/applications/kde/*kugar.desktop
%{_datadir}/applications/kde/*kudesigner.desktop

%files kexi
%defattr(-,root,root,-)
%lang(en) %{tde_docdir}/HTML/en/kexi/
%{_bindir}/kexi*
%{_bindir}/ksqlite*
%{_libdir}/libkdeinit_kexi.so
%{_libdir}/libkexi*.so.*
%{_libdir}/libkformdesigner.so.*
%{tde_libdir}/kformdesigner_*.*
%{tde_libdir}/kexidb_sqlite2driver.*
%{tde_libdir}/kexidb_sqlite3driver.*
%{tde_libdir}/kexihandler_*.*
%{tde_libdir}/kexi.*
# moved here to workaround bug #394101, alternative is to move libkexi(db|dbparser|utils) to -libs)
%{tde_libdir}/libkspreadkexiimport.*
%{_datadir}/config/kexirc
%{_datadir}/config/magic/kexi.magic
%{_datadir}/mimelnk/application/*
%{_datadir}/servicetypes/kexi*.desktop
%{_datadir}/services/kexi/
%{_datadir}/apps/kexi/
%{_datadir}/services/kformdesigner/*
%{_datadir}/applications/kde/*kexi.desktop
%{_datadir}/services/kexidb_sqlite*driver.desktop
%if 0%{?with_kross} > 0
%{_bindir}/krossrunner
%{tde_libdir}/krosskexiapp.*
%{tde_libdir}/krosskexidb.*
%endif

%files kexi-driver-mysql
%defattr(-,root,root,-)
%{tde_libdir}/kexidb_mysqldriver.*
%{tde_libdir}/keximigrate_mysql.*
%{_datadir}/services/keximigrate_mysql.desktop
%{_datadir}/services/kexidb_mysqldriver.desktop

%files kexi-driver-pgsql
%defattr(-,root,root,-)
%{tde_libdir}/kexidb_pqxxsqldriver.*
%{tde_libdir}/keximigrate_pqxx.*
%{_datadir}/services/kexidb_pqxxsqldriver.desktop
%{_datadir}/services/keximigrate_pqxx.desktop

%files kchart
%defattr(-,root,root,-)
%lang(en) %{tde_docdir}/HTML/en/kchart/
%{_bindir}/kchart
%{_libdir}/libkchart*.so.*
%{_libdir}/libkdeinit_kchart.so
%{tde_libdir}/*kchart*.*
%{_datadir}/apps/kchart/
%{_datadir}/services/kchart*.desktop
%{_datadir}/applications/kde/*kchart.desktop

%files kformula
%defattr(-,root,root,-)
%lang(en) %{tde_docdir}/HTML/en/kformula/
%{_bindir}/kformula
%{_libdir}/libkdeinit_kformula.so
%{tde_libdir}/*kformula*.*
%{_datadir}/apps/kformula/
%{_datadir}/services/kformula*.desktop
%{_datadir}/applications/kde/*kformula.desktop

%files kivio
%defattr(-,root,root,-)
%lang(en) %{tde_docdir}/HTML/en/kivio/
%{_bindir}/kivio
%{_libdir}/libkdeinit_kivio.so
%{_libdir}/libkiviocommon.so.*
%{tde_libdir}/*kivio*.*
%{tde_libdir}/straight_connector.*
%{_datadir}/apps/kivio/
%{_datadir}/config.kcfg/kivio.kcfg
%{_datadir}/services/kivio*.desktop
%{_datadir}/applications/kde/*kivio.desktop

%files filters
%defattr(-,root,root,-)
%{_libdir}/libkwordexportfilters.so.*
%{tde_libdir}/libabiwordexport.*
%{tde_libdir}/libabiwordimport.*
%{tde_libdir}/libamiproexport.*
%{tde_libdir}/libamiproimport.*
%{tde_libdir}/libapplixspreadimport.*
%{tde_libdir}/libapplixwordimport.*
%{tde_libdir}/libasciiexport.*
%{tde_libdir}/libasciiimport.*
%{tde_libdir}/libdbaseimport.*
%{tde_libdir}/libdocbookexport.*
%{tde_libdir}/libexcelimport.*
%{tde_libdir}/libgenerickofilter.*
%{tde_libdir}/libhtmlexport.*
%{tde_libdir}/libhtmlimport.*
%{tde_libdir}/libkarbonepsimport.*
%{tde_libdir}/libkfolatexexport.*
%{tde_libdir}/libkfomathmlexport.*
%{tde_libdir}/libkfomathmlimport.*
%{tde_libdir}/libkfopngexport.*
%{tde_libdir}/libkspreadlatexexport.*
%{tde_libdir}/libkugarnopimport.*
%{tde_libdir}/libkwordkword1dot3import.*
%{tde_libdir}/libkwordlatexexport.*
%{tde_libdir}/libmswriteexport.*
%{tde_libdir}/libmswriteimport.*
%{tde_libdir}/libooimpressexport.*
%{tde_libdir}/libooimpressimport.*
%{tde_libdir}/liboowriterexport.*
%{tde_libdir}/liboowriterimport.*
%{tde_libdir}/libpalmdocexport.*
%{tde_libdir}/libpalmdocimport.*
%{tde_libdir}/libpdfimport.*
%{tde_libdir}/librtfexport.*
%{tde_libdir}/librtfimport.*
%{tde_libdir}/libwmlexport.*
%{tde_libdir}/libwmlimport.*
%{tde_libdir}/libwpexport.*
%{tde_libdir}/libwpimport.*
%{tde_libdir}/libmswordimport.*
%{tde_libdir}/libxsltimport.*
%{tde_libdir}/libxsltexport.*
%{tde_libdir}/libhancomwordimport.*
%{tde_libdir}/libkfosvgexport.*
%{tde_libdir}/liboodrawimport.*
%{tde_libdir}/libolefilter.*
%{_datadir}/apps/xsltfilter/
%{_datadir}/services/generic_filter.desktop
%{_datadir}/services/ole_powerpoint97_import.desktop
%{_datadir}/services/xslt*.desktop
%{_datadir}/servicetypes/kofilter*.desktop

%files kplato
%defattr(-,root,root,-)
%lang(en) %{tde_docdir}/HTML/en/kplato/
%{_bindir}/kplato
%{_libdir}/libkdeinit_kplato.so
%{tde_libdir}/kplato.*
%{tde_libdir}/libkplatopart.*
%{_datadir}/apps/kplato/
%{_datadir}/services/kplatopart.desktop
%{_datadir}/applications/kde/*kplato.desktop

%files chalk
%defattr(-,root,root,-)
%{_bindir}/chalk
%{tde_libdir}/chalkblurfilter.la
%{tde_libdir}/chalkblurfilter.so
%{tde_libdir}/chalkbumpmap.la
%{tde_libdir}/chalkbumpmap.so
%{tde_libdir}/chalkcimg.la
%{tde_libdir}/chalkcimg.so
%{tde_libdir}/chalk_cmyk_*
%{tde_libdir}/chalkcmykplugin.la
%{tde_libdir}/chalkcmykplugin.so
%{tde_libdir}/chalkcolorify.la
%{tde_libdir}/chalkcolorify.so
%{tde_libdir}/chalkcolorrange.la
%{tde_libdir}/chalkcolorrange.so
%{tde_libdir}/chalkcolorsfilters.la
%{tde_libdir}/chalkcolorsfilters.so
%{tde_libdir}/chalkcolorspaceconversion.la
%{tde_libdir}/chalkcolorspaceconversion.so
%{tde_libdir}/chalkconvolutionfilters.la
%{tde_libdir}/chalkconvolutionfilters.so
%{tde_libdir}/chalkdefaultpaintops.la
%{tde_libdir}/chalkdefaultpaintops.so
%{tde_libdir}/chalkdefaulttools.la
%{tde_libdir}/chalkdefaulttools.so
%{tde_libdir}/chalkdropshadow.la
%{tde_libdir}/chalkdropshadow.so
%{tde_libdir}/chalkembossfilter.la
%{tde_libdir}/chalkembossfilter.so
%{tde_libdir}/chalkexample.la
%{tde_libdir}/chalkexample.so
%{tde_libdir}/chalkextensioncolorsfilters.la
%{tde_libdir}/chalkextensioncolorsfilters.so
%{tde_libdir}/chalkfastcolortransfer.la
%{tde_libdir}/chalkfastcolortransfer.so
%{tde_libdir}/chalkfiltersgallery.la
%{tde_libdir}/chalkfiltersgallery.so
%{tde_libdir}/chalk_gray_*
%{tde_libdir}/chalkgrayplugin.la
%{tde_libdir}/chalkgrayplugin.so
%{tde_libdir}/chalkhistogramdocker.la
%{tde_libdir}/chalkhistogramdocker.so
%{tde_libdir}/chalkhistogram.la
%{tde_libdir}/chalkhistogram.so
%{tde_libdir}/chalkimageenhancement.la
%{tde_libdir}/chalkimageenhancement.so
%{tde_libdir}/chalkimagesize.la
%{tde_libdir}/chalkimagesize.so
%{tde_libdir}/chalk.la
%{tde_libdir}/chalklenscorrectionfilter.la
%{tde_libdir}/chalklenscorrectionfilter.so
%{tde_libdir}/chalklevelfilter.la
%{tde_libdir}/chalklevelfilter.so
%{tde_libdir}/chalk_lms_*
%{tde_libdir}/chalkmodifyselection.la
%{tde_libdir}/chalkmodifyselection.so
%{tde_libdir}/chalknoisefilter.la
%{tde_libdir}/chalknoisefilter.so
%{tde_libdir}/chalkoilpaintfilter.la
%{tde_libdir}/chalkoilpaintfilter.so
%{tde_libdir}/chalkpixelizefilter.la
%{tde_libdir}/chalkpixelizefilter.so
%{tde_libdir}/chalkraindropsfilter.la
%{tde_libdir}/chalkraindropsfilter.so
%{tde_libdir}/chalkrandompickfilter.la
%{tde_libdir}/chalkrandompickfilter.so
%{tde_libdir}/chalk_rgb_*
%{tde_libdir}/chalkrgbplugin.la
%{tde_libdir}/chalkrgbplugin.so
%{tde_libdir}/chalkrotateimage.la
%{tde_libdir}/chalkrotateimage.so
%{tde_libdir}/chalkroundcornersfilter.la
%{tde_libdir}/chalkroundcornersfilter.so
%{tde_libdir}/chalkselectiontools.la
%{tde_libdir}/chalkselectiontools.so
%{tde_libdir}/chalkselectopaque.la
%{tde_libdir}/chalkselectopaque.so
%{tde_libdir}/chalkseparatechannels.la
%{tde_libdir}/chalkseparatechannels.so
%{tde_libdir}/chalkshearimage.la
%{tde_libdir}/chalkshearimage.so
%{tde_libdir}/chalksmalltilesfilter.la
%{tde_libdir}/chalksmalltilesfilter.so
%{tde_libdir}/chalk.so
%{tde_libdir}/chalkscreenshot.la
%{tde_libdir}/chalkscreenshot.so
%{tde_libdir}/chalksobelfilter.la
%{tde_libdir}/chalksobelfilter.so
%{tde_libdir}/chalksubstrate.la
%{tde_libdir}/chalksubstrate.so
%{tde_libdir}/chalktoolcrop.la
%{tde_libdir}/chalktoolcrop.so
%{tde_libdir}/chalktoolcurves.la
%{tde_libdir}/chalktoolcurves.so
%{tde_libdir}/chalktoolfilter.la
%{tde_libdir}/chalktoolfilter.so
%{tde_libdir}/chalktoolperspectivegrid.la
%{tde_libdir}/chalktoolperspectivegrid.so
%{tde_libdir}/chalktoolperspectivetransform.la
%{tde_libdir}/chalktoolperspectivetransform.so
%{tde_libdir}/chalktoolpolygon.la
%{tde_libdir}/chalktoolpolygon.so
%{tde_libdir}/chalktoolpolyline.la
%{tde_libdir}/chalktoolpolyline.so
%{tde_libdir}/chalktoolselectsimilar.la
%{tde_libdir}/chalktoolselectsimilar.so
%{tde_libdir}/chalktoolstar.la
%{tde_libdir}/chalktoolstar.so
%{tde_libdir}/chalktooltransform.la
%{tde_libdir}/chalktooltransform.so
%{tde_libdir}/chalkunsharpfilter.la
%{tde_libdir}/chalkunsharpfilter.so
%{tde_libdir}/chalkwavefilter.la
%{tde_libdir}/chalkwavefilter.so
%{tde_libdir}/chalkwetplugin.la
%{tde_libdir}/chalkwetplugin.so
%{tde_libdir}/chalk_ycbcr_*
%{tde_libdir}/libchalkgmagickexport.la
%{tde_libdir}/libchalkgmagickexport.so
%{tde_libdir}/libchalkgmagickimport.la
%{tde_libdir}/libchalkgmagickimport.so
%{tde_libdir}/libchalkjpegexport.la
%{tde_libdir}/libchalkjpegexport.so
%{tde_libdir}/libchalkjpegimport.la
%{tde_libdir}/libchalkjpegimport.so
%{tde_libdir}/libchalk_openexr_export.la
%{tde_libdir}/libchalk_openexr_export.so
%{tde_libdir}/libchalk_openexr_import.la
%{tde_libdir}/libchalk_openexr_import.so
%{tde_libdir}/libchalkpart.la
%{tde_libdir}/libchalkpart.so
%{tde_libdir}/libchalkpdfimport.la
%{tde_libdir}/libchalkpdfimport.so
%{tde_libdir}/libchalkpngexport.la
%{tde_libdir}/libchalkpngexport.so
%{tde_libdir}/libchalkpngimport.la
%{tde_libdir}/libchalkpngimport.so
%{tde_libdir}/libchalk_raw_import.la
%{tde_libdir}/libchalk_raw_import.so
%{tde_libdir}/libchalktiffexport.la
%{tde_libdir}/libchalktiffexport.so
%{tde_libdir}/libchalktiffimport.la
%{tde_libdir}/libchalktiffimport.so
%{_libdir}/libkdeinit_chalk.so
%{_libdir}/libchalk_cmyk_*.so.*
%{_libdir}/libchalkcolor.so.*
%{_libdir}/libchalkcommon.so.*
%{_libdir}/libchalkgrayscale.so.*
%{_libdir}/libchalk_gray_*.so.*
%{_libdir}/libchalkimage.so.*
%{_libdir}/libchalk_lms_*.so.*
%{_libdir}/libchalk_rgb_*.so.*
%{_libdir}/libchalkrgb.so.*
%{_libdir}/libchalkui.so.*
%{_libdir}/libchalk_ycbcr_*.so.*
%if 0%{?with_kross} > 0
%{tde_libdir}/krosschalkcore.la
%{tde_libdir}/krosschalkcore.so
%{tde_libdir}/chalkscripting.la
%{tde_libdir}/chalkscripting.so
%{_libdir}/libchalkscripting.so.*
%endif

%files chalk-data
%{_datadir}/applications/kde/chalk.desktop
%{_datadir}/applnk/.hidden/chalk_*.desktop
%{_datadir}/apps/konqueror/servicemenus/chalk_konqi.desktop
%{_datadir}/apps/chalk
%{_datadir}/apps/chalkplugins
%lang(en) %{tde_docdir}/HTML/en/chalk
%{_datadir}/icons/hicolor/*/apps/chalk.png
%{_datadir}/services/chalk*.desktop
%{_datadir}/servicetypes/chalk*.desktop


%changelog
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
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
- Based on Spec file from Fedora 11 'koffice-2:1.6.3-25.20090306svn'
- Removed 'krita', added 'chalk'
