# Default version for this component
%define tde_pkg kmymoney
%define tde_version 3.5.13.2

# Required for Mageia 2: removes the ldflag '--no-undefined'
%define _disable_ld_no_undefined 1

%if 0%{?mgaversion} || 0%{?mdkversion}
%define qt3pluginsdir %{_libdir}/qt3/plugins
%endif
%if 0%{?rhel} || 0%{?fedora}
%define qt3pluginsdir %{_libdir}/qt-3.3/plugins
%endif
%if 0%{?suse_version}
%define qt3pluginsdir /usr/lib/qt3/plugins
%endif

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		personal finance manager for TDE

Version:		1.0.5
Release:		%{?!preversion:6}%{?preversion:5_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:		kmymoneytitlelabel.png

# [kmymoney] Fix FTBFS
Patch1:		kmymoney-3.5.13.2-ftbfs.patch

# [admin] Fix automake 1.13 build issue
Patch2:			admin-fix-parallel-test.diff

# [kmymoney] Missing LDFLAGS causing FTBFS
Patch4:		kmymoney-3.5.13-missing_ldflags.patch

# [kmymoney] Fix QT3 plugins directory location
Patch5:		kmymoney-3.5.13-fix_qt3_plugins_location.patch

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	recode
BuildRequires:	libofx-devel

# OPENSP support
%if 0%{?mgaversion} || 0%{?pclinuxos} || 0%{?mdkversion}
%if 0%{?mgaversion} || 0%{?pclinuxos}
%if 0%{?mgaversion} >= 4
BuildRequires:	%{_lib}osp-devel
%else
BuildRequires:	%{_lib}OpenSP5-devel
%endif
%else
BuildRequires:	opensp-devel
%endif
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	opensp-devel
%endif
%if 0%{?rhel} == 4
BuildRequires:	openjade-devel
%endif

Requires:		%{name}-common == %{version}-%{release}

%description
KMyMoney is the Personal Finance Manager for TDE. It operates similar to
MS-Money and Quicken, supports different account types, categorisation of
expenses, QIF import/export, multiple currencies and initial online banking
support.


%package common
Summary:		KMyMoney architecture independent files
Group:			Applications/Utilities
Requires:		%{name} == %{version}

%description common
This package contains architecture independent files needed for KMyMoney to
run properly. It also provides KMyMoney documentation. Therefore, unless you
have '%{name}' package installed, you will hardly find this package useful.


%package devel
Summary:		KMyMoney development files
Group:			Development/Libraries
Requires:		%{name} == %{version}

%description devel
This package contains development files needed for KMyMoney plugins.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
%patch1 -p1 -b .ftbfs
%patch2 -p1 -b .automake113
%if 0%{?mgaversion} || 0%{?mdkversion}
%patch5 -p1 -b .qtpluginsdir
%endif

%__install -m644 %{SOURCE1} kmymoney2/widgets/

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"
export KDEDIR="%{tde_prefix}"

# Required to find the QT3 plugins directory
%if 0%{?mgaversion} || 0%{?mdkversion}
export QTPLUGINS="%{_libdir}/qt3/plugins"
%endif

# Fix strange FTBFS on RHEL4
%if 0%{?rhel} == 4
grep -v "^#~" po/it.po >/tmp/it.po && mv -f /tmp/it.po po/it.po
%endif

# Warning: --enable-final causes FTBFS
%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --disable-final \
  --enable-closure \
  --enable-rpath \
  \
  --disable-pdf-docs \
  --enable-ofxplugin \
  --enable-ofxbanking \
  --enable-qtdesigner \
  --enable-sqlite3

# Fix FTBFS inside sqlite3 archive
patch -p1 < %{PATCH4}

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}

# Required to find the QT3 plugins directory
%if 0%{?mgaversion} || 0%{?mdkversion}
export QTPLUGINS=%{_libdir}/qt3/plugins
%endif

%__make install DESTDIR=%{buildroot}

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

%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1.0.5-6
- Build for Fedora 19

* Sun Jul 28 2013 Francois Andriot <francois.andriot@free.fr> - 1.0.5-5
- Rebuild with NDEBUG option

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 1.0.5-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.5-3
- Initial release for TDE 3.5.13.1

* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.5-2
- Rebuild for Fedora 17
- Fix compilation with GCC 4.7 [Bug #958]

* Sun Jan 15 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.5-1
- Updates to upstream 1.0.5

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 1.0.4-1
- Initial release for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15
