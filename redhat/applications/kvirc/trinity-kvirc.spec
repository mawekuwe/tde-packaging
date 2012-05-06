# Default version for this component
%define kdecomp kvirc
%define version 3.4.0
%define release 2

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
Summary:	Trinity based next generation IRC client with module support
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://kvirc.net/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [kvirc] Modules do not install in correct folder [RHEL/Fedora]
Patch0:		kvirc-3.5.13-directories.patch
# [kvirc] FTBFS because of missing link libraries [Bug #991]
Patch1:		kvirc-3.5.13-ftbfs.patch

# [kvirc] Rename old tq methods that no longer need a unique name [Commit #32a249ba]
Patch2:		bp000-32a249ba.diff
# [kvirc] Remove additional unneeded tq method conversions [Commit #f9114981]
Patch3:		bp001-f9114981.diff
# [kvirc] Rename obsolete tq methods to standard names [Commit #2dd6d32b]
Patch4:		bp002-2dd6d32b.diff
# [kvirc] Rename a few stragglers [Commit #1c00d6ff]
Patch5:		bp003-1c00d6ff.diff
# [kvirc] Fix FTBFS [Commits #ff96f491, #2285efe5]
Patch6:		bp004-ff96f491.diff
Patch7:		bp005-2285efe5.diff
# [kvirc] Fix linear alphabet string errors [Commit #51bbe9e5]
Patch8:		bp006-51bbe9e5.diff
# [kvirc] Fix inadvertent "TQ" changes. [Commit #a24a8595]
Patch9:		bp007-a24a8595.diff
# [kvirc] Fix "acinclude.m4" file [Bug #980]
Patch10:	kvirc-3.5.13-fix_acinclude_m4.patch
    
BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

Requires:	%{name}-data = %{version}-%{release}

%description
A highly configurable graphical IRC client with an MDI interface,
built-in scripting language, support for IRC DCC, drag & drop file
browsing, and much more. KVIrc uses the KDE widget set, can be extended
using its own scripting language, integrates with KDE, and supports
custom plugins.

If you are a developer and you want to write a custom module for KVIrc,
you need to install the kvirc-dev package.

%package data
Group:		Applications/Utilities
Summary:	Data files for KVIrc
Requires:	%{name} = %{version}-%{release}

%description data
This package contains the architecture-independent data needed by KVIrc in
order to run, such as icons and images, language files, and shell scripts.
It also contains complete reference guides on scripting and functions
within KVIrc in its internal help format. Unless you want to use KVIrc only
as a very simple IRC client you are likely to want to write scripts to
tailor KVIrc to your needs.

KVIrc is a graphical IRC client based on the KDE widget set which integrates
with the K Desktop Environment version 3.

%package devel
Group:		Development/Libraries
Summary:	Development files for KVIrc
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains KVIrc libraries and include files you need if you
want to develop plugins for KVIrc.

KVIrc is a graphical IRC client based on the KDE widget set which integrates
with the K Desktop Environment version 3.


%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

# Hardcoded absolute PATH to KDEDIR in source code ! That sucks !
%__sed -i "src/kvirc/kernel/kvi_app_fs.cpp" \
  -e "s|/opt/kde3/lib|%{_prefix}/%{_lib}|g"
%__sed -i "src/kvirc/kernel/kvi_app_setup.cpp" \
  -e "s|/opt/kde3|%{_prefix}|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
./autogen.sh


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"
export KDEDIR=%{_prefix}

%configure \
	--disable-rpath \
	--with-fno-rtti --with-aa-fonts --with-big-channels \
	--enable-perl --with-pic --enable-wall \
	--with-ix86-asm \
	--with-qt-moc=%{_bindir}/tmoc \
	--with-extra-includes=%{_includedir}/tqt \
	--with-kde-services-dir=%{_datadir}/services \
	--with-kde-library-dir=%{_libdir} \
	--with-kde-include-dir=%{_includedir}

# Symbolic links must exist prior to parallel building
%__make symlinks -C src/kvilib/build
%__make symlinks -C src/kvirc/build

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Debian maintainer has renamed 'COPYING' file to 'EULA', so we do the same ...
%__mv \
  %{?buildroot}%{_datadir}/kvirc/3.4/license/COPYING \
  %{?buildroot}%{_datadir}/kvirc/3.4/license/EULA

%clean
%__rm -rf %{buildroot}


%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc ChangeLog FAQ README TODO
%{_bindir}/kvirc
%{_libdir}/*.so.*
%{_libdir}/kvirc/*/modules/*.so

%files data
%defattr(-,root,root,-)
%{_bindir}/kvi_run_netscape
%{_bindir}/kvi_search_help
%{_libdir}/kvirc/*/modules/caps/
%{_datadir}/applnk/Internet/kvirc.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/kvirc
%{_datadir}/mimelnk/text/*.desktop
%{_datadir}/services/*.protocol
%{_mandir}/man1/kvirc.1

%files devel
%defattr(-,root,root,-)
%{_bindir}/kvirc-config
%{_includedir}/kvirc/
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/kvirc/*/modules/*.la


%Changelog
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
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
