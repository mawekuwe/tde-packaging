# Default version for this component
%define kdecomp kmymoney

# Required for Mageia 2: removes the ldflag '--no-undefined'
%define _disable_ld_no_undefined 1

%if 0%{?mgaversion} || 0%{?mdkversion}
%define qt3pluginsdir %{_libdir}/qt3/plugins
%else
%define qt3pluginsdir %{_libdir}/qt-3.3/plugins
%endif

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


Name:		trinity-%{kdecomp}
Summary:	personal finance manager for TDE

Version:	1.0.5
Release:	2%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Source1:	kmymoneytitlelabel.png
Patch0:		kmymoney-3.5.13-recode_ftbfs.patch

# TDE Commit: 2a54aa58cfe166f48d6f1395cbc6c9bfd5e31bfc
Patch1:		kmymoney-3.5.13-lots_of_crash.patch

# TDE Commit: 8654cea10f6902719006d5975db7dc07b2fcc713
Patch2:		kmymoney-3.5.13-update_to_1.0.5.patch

# [kmymoney] Fix compilation with GCC 4.7 [Bug #958]
Patch3:		kmymoney-3.5.13-fix_gcc47_compilation.patch

# [kmymoney] Missing LDFLAGS causing FTBFS
Patch4:		kmymoney-3.5.13-missing_ldflags.patch

# [kmymoney] Fix QT3 plugins directory location
Patch5:		kmymoney-3.5.13-fix_qt3_plugins_location.patch

BuildRequires: tqtinterface-devel
BuildRequires: trinity-arts-devel
BuildRequires: trinity-tdelibs-devel
BuildRequires: trinity-tdebase-devel
BuildRequires: desktop-file-utils

BuildRequires: recode
BuildRequires: html2ps
BuildRequires: libofx-devel

%if 0%{?mgaversion}
BuildRequires: %{_lib}OpenSP5-devel
%else
BuildRequires: opensp-devel
%endif

Requires:		%{name}-common == %{version}

%description
KMyMoney is the Personal Finance Manager for TDE. It operates similar to
MS-Money and Quicken, supports different account types, categorisation of
expenses, QIF import/export, multiple currencies and initial online banking
support.


%package common
Summary:	KMyMoney architecture independent files
Group:		Applications/Utilities
Requires:	%{name} == %{version}

%description common
This package contains architecture independent files needed for KMyMoney to
run properly. It also provides KMyMoney documentation. Therefore, unless you
have '%{name}' package installed, you will hardly find this package useful.


%package devel
Summary:	KMyMoney development files
Group:		Development/Libraries
Requires:	%{name} == %{version}

%description devel
This package contains development files needed for KMyMoney plugins.


%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1 -b .qtpluginsdir

%__install -m644 %{SOURCE1} kmymoney2/widgets/

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

# Required to find the QT3 plugins directory
%if 0%{?mgaversion} || 0%{?mdkversion}
export QTPLUGINS=%{_libdir}/qt3/plugins
%endif

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  --disable-rpath \
  --with-extra-includes=%{tde_includedir}/tqt \
  --enable-closure \
  --enable-pdf-docs \
  --enable-ofxplugin \
  --enable-ofxbanking \
  --enable-qtdesigner \
  --enable-sqlite3

# Fix FTBFS inside sqlite3 archive
patch -p1 < %{PATCH4}

%__make %{?_smp_mflags}

%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}

# Required to find the QT3 plugins directory
%if 0%{?mgaversion} || 0%{?mdkversion}
export QTPLUGINS=%{_libdir}/qt3/plugins
%endif

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

%find_lang kmymoney2

%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_appdir} > /dev/null
/sbin/ldconfig
for f in hicolor locolor Tango oxygen; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done

%postun
update-desktop-database %{tde_appdir} > /dev/null
/sbin/ldconfig
for f in hicolor locolor Tango oxygen; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done

%files
%defattr(-,root,root,-)
%{tde_bindir}/kmymoney
%{tde_bindir}/kmymoney2
%{tde_tdeappdir}/kmymoney2.desktop
%{tde_datadir}/mimelnk/application/x-kmymoney2.desktop
%{tde_datadir}/servicetypes/kmymoneyimporterplugin.desktop
%{tde_datadir}/servicetypes/kmymoneyplugin.desktop
%{tde_libdir}/*.so.*
%{tde_tdelibdir}/kmm_ofximport.la
%{tde_tdelibdir}/kmm_ofximport.so

%files common -f kmymoney2.lang
%defattr(-,root,root,-)
%{tde_datadir}/apps/kmymoney2/html/
%{tde_datadir}/apps/kmymoney2/icons/*/*/*/*.png
%{tde_datadir}/apps/kmymoney2/kmymoney2ui.rc
%{tde_datadir}/apps/kmymoney2/misc/financequote.pl
%{tde_datadir}/apps/kmymoney2/pics/*.png
%{tde_datadir}/apps/kmymoney2/templates/*/*.kmt
%{tde_datadir}/apps/kmymoney2/tips
%{tde_datadir}/config.kcfg/kmymoney2.kcfg
%{tde_datadir}/icons/hicolor/*/*/*.png
%{tde_datadir}/icons/Tango/*/*/*.png
%{tde_datadir}/icons/Tango/scalable/*.svgz
%{tde_datadir}/icons/locolor/*/*/*.png
%{tde_datadir}/icons/oxygen/*/*/*.png
%{tde_datadir}/icons/oxygen/scalable/*.svgz
%{tde_tdedocdir}/HTML/en/kmymoney2/
%{tde_mandir}/man1/kmymoney2.*
%{tde_datadir}/apps/kmm_ofximport/kmm_ofximport.rc
%{tde_datadir}/services/kmm_ofximport.desktop


%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kmymoney/*.h
%{tde_libdir}/libkmm_kdchart.la
%{tde_libdir}/libkmm_mymoney.la
%{tde_libdir}/libkmm_plugin.la
%{tde_libdir}/*.so
%{qt3pluginsdir}/sqldrivers/libsqlite3*.so
%{qt3pluginsdir}/designer/libkmymoney.so

%Changelog
* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.5-2
- Rebuild for Fedora 17
- Fix compilation with GCC 4.7 [Bug #958]

* Sun Jan 15 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.5-1
- Updates to upstream 1.0.5

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 1.0.4-1
- Initial release for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15
