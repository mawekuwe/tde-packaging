# REMOVE TDELIBS4-DEVEL before building !!!!

# Default version for this component
%define tde_pkg kvirc
%define tde_version 14.0.0

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

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		Trinity based next generation IRC client with module support
Version:		3.4.0
Release:		%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://kvirc.net/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

Requires:		%{name}-data = %{version}-%{release}

%description
A highly configurable graphical IRC client with an MDI interface,
built-in scripting language, support for IRC DCC, drag & drop file
browsing, and much more. KVIrc uses the TDE widget set, can be extended
using its own scripting language, integrates with TDE, and supports
custom plugins.

If you are a developer and you want to write a custom module for KVIrc,
you need to install the kvirc-dev package.

%package data
Group:			Applications/Utilities
Summary:		Data files for KVIrc
Requires:		%{name} = %{version}-%{release}

%description data
This package contains the architecture-independent data needed by KVIrc in
order to run, such as icons and images, language files, and shell scripts.
It also contains complete reference guides on scripting and functions
within KVIrc in its internal help format. Unless you want to use KVIrc only
as a very simple IRC client you are likely to want to write scripts to
tailor KVIrc to your needs.

KVIrc is a graphical IRC client based on the TDE widget set which integrates
with the K Desktop Environment version 3.

%package devel
Group:			Development/Libraries
Summary:		Development files for KVIrc
Requires:		%{name} = %{version}-%{release}

%description devel
This package contains KVIrc libraries and include files you need if you
want to develop plugins for KVIrc.

KVIrc is a graphical IRC client based on the TDE widget set which integrates
with the K Desktop Environment version 3.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

# Hardcoded absolute PATH to TDEDIR in source code ! That sucks !
%__sed -i "src/kvirc/kernel/kvi_app_fs.cpp" \
  -e "s|/opt/kde3/lib|%{tde_libdir}|g"
%__sed -i "src/kvirc/kernel/kvi_app_setup.cpp" \
  -e "s|/opt/kde3|%{tde_prefix}|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
./autogen.sh


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  --with-big-channels \
  --enable-perl --with-pic --enable-wall \
  --with-ix86-asm \
  --with-kde-services-dir=%{tde_datadir}/services \
  --with-kde-library-dir=%{tde_libdir} \
  --with-kde-include-dir=%{tde_tdeincludedir} \
  --with-qt-name=tqt \
  --with-qt-library-dir=%{_libdir} \
  --with-qt-include-dir=%{_includedir}/tqt3 \
  --with-qt-moc=%{_bindir}/tmoc

# Symbolic links must exist prior to parallel building
%__make symlinks -C src/kvilib/build
%__make symlinks -C src/kvirc/build

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Debian maintainer has renamed 'COPYING' file to 'EULA', so we do the same ...
%__mv \
  %{?buildroot}%{tde_datadir}/kvirc/3.4/license/COPYING \
  %{?buildroot}%{tde_datadir}/kvirc/3.4/license/EULA


%clean
%__rm -rf %{buildroot}


%post
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
/sbin/ldconfig
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc ChangeLog FAQ README TODO
%{tde_bindir}/kvirc
%{tde_libdir}/*.so.*
#%{tde_libdir}/kvirc/*/modules/*.so

%files data
%defattr(-,root,root,-)
%{tde_bindir}/kvi_run_netscape
%{tde_bindir}/kvi_search_help
#%{tde_libdir}/kvirc/*/modules/caps/
%{tde_datadir}/applnk/Internet/kvirc.desktop
%{tde_datadir}/icons/hicolor/*/*/*.png
%{tde_datadir}/icons/hicolor/*/*/*.svgz
%{tde_datadir}/icons/hicolor/*/*/*.xpm
%{tde_datadir}/kvirc
%{tde_datadir}/mimelnk/text/*.desktop
%{tde_datadir}/services/*.protocol
%{tde_mandir}/man1/kvirc.1

%files devel
%defattr(-,root,root,-)
%{tde_bindir}/kvirc-config
%{tde_includedir}/kvirc/
%{tde_libdir}/*.la
%{tde_libdir}/*.so
#%{tde_libdir}/kvirc/*/modules/*.la


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 3.4.0-5
- Initial release for TDE 14.0.0

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.4.0-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 3.4.0-3
- Initial release for TDE 3.5.13.1

* Sat May 05 2012 Francois Andriot <francois.andriot@free.fr> - 3.4.0-2
- Rebuilt for Fedora 17
- Fix HTML directory location
- Rename old tq methods that no longer need a unique name [Commit #32a249ba]
- Remove additional unneeded tq method conversions [Commit #f9114981]
- Rename obsolete tq methods to standard names [Commit #2dd6d32b]
- Rename a few stragglers [Commit #1c00d6ff]
- Fix FTBFS [Commits #ff96f491, #2285efe5]
- Fix linear alphabet string errors [Commit #51bbe9e5]
- Fix inadvertent "TQ" changes. [Commit #a24a8595]
- Fix "acinclude.m4" file [Bug #980]
 
* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.4.0-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
