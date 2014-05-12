%define tde_version 14.0.0

# Always install under standard prefix
%define tde_prefix /usr
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}


Name:		trinity-tqt3
Version:	3.5.0
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:	The shared library for the Trinity Qt 3 GUI toolkit

License:	QPL or GPLv2 or GPLv3
Group:		System Environment/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{tde_version}-%{release}-root-%(%{__id_u} -n)
Url:		http://www.trinitydesktop.org

Prefix:		%{tde_prefix}

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

# [tqt3] Unexplained FTBFS on RHEL5
Patch1:		tqt3-14.0.0-rhel5_ftbfs.patch

BuildRequires: desktop-file-utils
BuildRequires: libmng-devel
BuildRequires: glibc-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: zlib-devel
BuildRequires: giflib-devel
BuildRequires: perl
BuildRequires: sed
BuildRequires: findutils
BuildRequires: tar
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: desktop-file-utils

# CUPS support
BuildRequires: cups-devel

# GLIB2 support
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version} || 0%{?rhel} >= 6
%define with_glibmainloop 1
BuildRequires: glib2-devel
%endif

# UUID support
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version} || 0%{?rhel} >= 6
BuildRequires: libuuid-devel
%endif
%if 0%{?rhel} == 5
BuildRequires: e2fsprogs-devel
%endif

# NAS support
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_nas 1
BuildRequires: nas-devel
%endif

# Xrender support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libXrender-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: libxrender-devel
%endif

# Xrandr support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libXrandr-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: libxrandr-devel
%endif

# Xcursor support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libXcursor-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: libxcursor-devel
%endif

# Xinerama support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libXinerama-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: libxinerama-devel
%endif

# Xft support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libXft-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: libxft-devel
%endif

# Xext support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libXext-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: libxext-devel
%endif

# X11 support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libX11-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: libx11-devel
%endif

# SM support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libSM-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: libsm-devel
%endif

# ICE support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libICE-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: libice-devel
%endif

# XT support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libXt-devel
%endif

# XMU support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libXmu-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: libxmu-devel
%endif

# XI support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: libXi-devel
%endif

# Xorg support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: xorg-x11-proto-devel
%endif

# MESA support
%if 0%{?rhel} || 0%{?fedora}
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires: mesaglu-devel
%endif
%if 0%{?suse_version}
BuildRequires: Mesa-libGL-devel
BuildRequires: Mesa-libGLU-devel
%endif

# MYSQL support
BuildRequires: mysql-devel

# unixODBC support
BuildRequires: unixODBC-devel

# SQLITE support
BuildRequires: sqlite-devel

# POSTGRESQL support
BuildRequires: postgresql
BuildRequires: postgresql-devel

# Firebird support
%if 0%{?mdkversion} || 0%{?mgaversion}
%define with_ibase 1
BuildRequires:	firebird-devel
%endif

# x86_64 specific stuff
%if "%{_lib}" != "lib"
%if 0%{?mdkversion} || ( 0%{?mgaversion} && 0%{?mgaversion} <= 2)
BuildRequires: linux32
%else
BuildRequires: util-linux
%endif
%endif

# GCC visibility stuff
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version} || 0%{?rhel} >= 6
%define EXTRA_CFLAGS -fvisibility=hidden -fvisibility-inlines-hidden
%endif 
 
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: coreutils
Requires: fontconfig >= 2.0
Requires: /etc/ld.so.conf.d

%description
TQt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications
for the X Window System.

TQt is written in C++ and is fully object-oriented.

This package contains the shared library needed to run TQt 3
applications, as well as the README files for TQt 3.

%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

%files
%defattr(-,root,root,-)
%doc FAQ LICENSE* README* changes*
%dir %{tde_libdir}/tqt3/plugins
%dir %{tde_libdir}/tqt3/plugins/sqldrivers
#%dir %{tde_libdir}/tqt3/plugins/styles
%{tde_datadir}/tqt3/translations/
%dir %{tde_libdir}/tqt3/plugins/designer
%{tde_libdir}/tqt3/plugins/designer/libcppeditor.so
%{tde_libdir}/tqt3/plugins/designer/libdlgplugin.so
%{tde_libdir}/tqt3/plugins/designer/libgladeplugin.so
%{tde_libdir}/tqt3/plugins/designer/libkdevdlgplugin.so
%{tde_libdir}/tqt3/plugins/designer/librcplugin.so
%{tde_libdir}/tqt3/plugins/designer/libwizards.so
%dir %{tde_libdir}/tqt3/plugins/imageformats
%{tde_libdir}/tqt3/plugins/imageformats/libqmng.so
%dir %{tde_libdir}/tqt3/plugins/inputmethods
%{tde_libdir}/tqt3/plugins/inputmethods/libqimsw-multi.so
%{tde_libdir}/tqt3/plugins/inputmethods/libqimsw-none.so
%{tde_libdir}/tqt3/plugins/inputmethods/libqsimple.so
%{tde_libdir}/tqt3/plugins/inputmethods/libqxim.so
%{tde_libdir}/libtqt-mt.so.3
%{tde_libdir}/libtqt-mt.so.3.5
%{tde_libdir}/libtqt-mt.so.3.5.0
%{tde_libdir}/libtqt-mt.la
%{tde_libdir}/libtqui.so.1
%{tde_libdir}/libtqui.so.1.0
%{tde_libdir}/libtqui.so.1.0.0
%{tde_libdir}/libtqtdesignercore.so.1
%{tde_libdir}/libtqtdesignercore.so.1.0
%{tde_libdir}/libtqtdesignercore.so.1.0.0
%{tde_libdir}/libtqteditor.so.1
%{tde_libdir}/libtqteditor.so.1.0
%{tde_libdir}/libtqteditor.so.1.0.0
%{tde_libdir}/libtqassistantclient.so.1
%{tde_libdir}/libtqassistantclient.so.1.0
%{tde_libdir}/libtqassistantclient.so.1.0.0

##########

%package config
Summary: Graphical configuration tool for programs using TQt 3
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description config
TQt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications
for the X Window System.

TQt is written in C++ and is fully object-oriented.

This package contains a graphical configuration tool for programs using TQt 3.

%files config
%defattr(-,root,root,-)
%{tde_bindir}/tqtconfig

##########

%package devel
Summary: Development files for the TQt 3 GUI toolkit
Group: Development/Libraries

Requires: %{name} = %{version}-%{release}
Requires: %{name}-designer = %{version}-%{release}

%description devel
The %{name}-devel package contains the files necessary to develop
applications using the TQt GUI toolkit: the header files, the TQt meta
object compiler.

Install %{name}-devel if you want to develop GUI applications using the TQt 3
toolkit.

%files devel
%defattr(-,root,root,-)
%{tde_bindir}/tqtconv2ui
%{tde_bindir}/tqvfb
%{tde_bindir}/tqmoc
%{tde_bindir}/tquic
%{tde_bindir}/tqtfindtr
%{tde_bindir}/tqt20fix
%{tde_bindir}/tqtrename140
%{tde_bindir}/tqassistant
%{tde_bindir}/tqm2ts
%{tde_bindir}/tqmake
%{tde_bindir}/tqembed
%{tde_bindir}/tqlinguist
%{tde_bindir}/tqlupdate
%{tde_bindir}/tqlrelease
%{tde_bindir}/tqtcreatecw
%{tde_bindir}/maketqpf
%{tde_bindir}/tqtmergetr
%{tde_bindir}/msg2tqm
%{tde_datadir}/tqt3/mkspecs/
%{tde_datadir}/tqt3/phrasebooks/
%{tde_includedir}/tqt3/
%{tde_libdir}/libtqtdesignercore.prl
%{tde_libdir}/libtqtdesignercore.so
%{tde_libdir}/libtqteditor.prl
%{tde_libdir}/libtqteditor.so
%{tde_libdir}/libtqassistantclient.prl
%{tde_libdir}/libtqassistantclient.so
%{tde_libdir}/libtqt-mt.so
%{tde_libdir}/libtqt-mt.prl
%{tde_libdir}/libtqui.so
%{tde_libdir}/libtqui.prl
%{tde_libdir}/pkgconfig/tqt-mt.pc


%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

##########

%package devel-docs
Summary: Documentation for the TQt 3 GUI toolkit
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description devel-docs
The %{name}-devel-docs package contains the man pages, the HTML documentation and
example programs for TQt 3.

%files devel-docs
%defattr(-,root,root,-)
%doc examples
%doc tutorial
%{tde_datadir}/tqt3/doc/html/

##########

%package ODBC
Summary: ODBC drivers for TQt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description ODBC
ODBC driver for TQt 3's SQL classes (QSQL)

%files ODBC
%defattr(-,root,root,-)
%{tde_libdir}/tqt3/plugins/sqldrivers/libqsqlodbc.so

##########

%package MySQL
Summary: MySQL drivers for TQt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description MySQL
MySQL driver for TQt 3's SQL classes (QSQL)

%files MySQL
%defattr(-,root,root,-)
%{tde_libdir}/tqt3/plugins/sqldrivers/libqsqlmysql.so

##########

%package PostgreSQL
Summary: PostgreSQL drivers for TQt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description PostgreSQL
PostgreSQL driver for TQt 3's SQL classes (QSQL)

%files PostgreSQL
%defattr(-,root,root,-)
%{tde_libdir}/tqt3/plugins/sqldrivers/libqsqlpsql.so

##########

%package sqlite
Summary: sqlite drivers for TQt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description sqlite
sqlite driver for TQt 3's SQL classes (QSQL)

%files sqlite
%defattr(-,root,root,-)
%{tde_libdir}/tqt3/plugins/sqldrivers/libqsqlite.so

##########

%if 0%{?with_ibase}
%package ibase
Summary: ibase drivers for TQt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description ibase
ibase driver for TQt 3's SQL classes (QSQL)

%files ibase
%defattr(-,root,root,-)
%{tde_libdir}/tqt3/plugins/sqldrivers/libqsqlibase.so
%endif

##########

%package designer
Summary: In3erface designer (IDE) for the TQt 3 toolkit
Group: Development/Tools
Requires: %{name}-devel = %{version}-%{release}

%description designer
The %{name}-designer package contains an User Interface designer tool
for the TQt 3 toolkit.

%files designer
%defattr(-,root,root,-)
%{tde_bindir}/tqdesigner
%{tde_datadir}/tqt3/templates/

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
%if 0%{?rhel} == 5
%patch1 -p1 -b .ftbfs
%endif

# fix variables in 'qmake.conf'
%__sed -i mkspecs/*/qmake.conf \
  -e "s|^QMAKE_INCDIR_QT.*|QMAKE_INCDIR_QT		= %{_includedir}/tqt3|" \
  -e "s|\$(QTDIR)|/usr|g" \
  -e "s|-lqt|-ltqt|g" \
  -e "s|^QMAKE_CFLAGS		=.*|QMAKE_CFLAGS		= %{?optflags}|" \
  -e "s|^QMAKE_INCDIR		=.*|QMAKE_INCDIR		= %{_includedir}|" \
  -e "s|^QMAKE_LIBDIR		=.*|QMAKE_LIBDIR		= %{_libdir}|" \
  -e "s|^QMAKE_RPATH		= .*|QMAKE_RPATH		=|" \
  -e "s|^QMAKE_STRIP             =.*|QMAKE_STRIP             =|" \
  -e "s|^QMAKE_STRIPFLAGS_LIB 	+=.*|QMAKE_STRIPFLAGS_LIB 	+=|" \
  -e "s|^QMAKE_MOC		=.*|QMAKE_MOC		= %{_bindir}/tqmoc|" \
  -e "s|^QMAKE_UIC		=.*|QMAKE_UIC		= %{_bindir}/tquic|" \
  -e "s|^QMAKE_INCDIR_QT		=.*|QMAKE_INCDIR_QT		= %{_includedir}/tqt3|" \
  -e "s|^QMAKE_LIBDIR_QT         =.*|QMAKE_LIBDIR_QT         = %{_libdir}|" \


%build
unset QTDIR QTINC QTLIB
export QTDIR=$(pwd)
export PATH=${QTDIR}/bin:$PATH
export MANPATH=${QTDIR}/doc/man:$MANPATH
export LD_LIBRARY_PATH="${QTDIR}/lib"

# Checks for supplementary include dir
INCDIRS=""
for d in \
	%{_includedir}/fontconfig \
	%{_includedir}/pgsql \
	%{_includedir}/pgsql/server \
	%{_includedir}/postgresql/server \
	%{_includedir}/Xft2 \
	%{_includedir}/Xft2/X11/Xft \
	%{_includedir}/mysql \
	%{_includedir}/libpng15 \
; do
	if [ -d "${d}" ]; then
		INCDIRS="${INCDIRS} -I${d}"
	fi
done

# Checks for supplementary library dirs
LIBDIRS=""
for d in \
	%{_libdir}/mysql \
	%{_libdir}/pgsql \
; do
	if [ -d "${d}" ]; then
		LIBDIRS="${LIBDIRS} -L${d}"
	fi
done

# build shared, threaded (default) libraries
echo yes | ./configure \
		${INCDIRS} \
		${LIBDIRS} \
		-L%{_libdir} \
		-prefix		"%{tde_prefix}" \
		-libdir		"%{tde_libdir}" \
		-sysconfdir	"%{_sysconfdir}/tqt3" \
		-datadir	"%{tde_datadir}/tqt3" \
		-headerdir	"%{tde_includedir}/tqt3" \
		-docdir		"%{tde_datadir}/tqt3/doc" \
		-plugindir	"%{tde_libdir}/tqt3/plugins" \
		-translationdir	"%{tde_datadir}/tqt3/translations" \
		\
		-thread \
		-shared \
		-fast \
		-no-exceptions \
%if "%{_lib}" == "lib64"
		-platform linux-g++-64 \
%else
		-platform linux-g++ \
%endif
		\
		-nis				\
		-no-pch				\
		-cups				\
		-stl				\
		-ipv6				\
		\
		-sm				\
		-xshape				\
		-xinerama			\
		-xcursor			\
		-xrandr				\
		-xrender			\
		-xft				\
		-tablet				\
		-xkb				\
		\
		-system-zlib			\
		-system-libpng			\
		-system-libmng			\
		-system-libjpeg			\
		%{?with_nas:-system-nas-sound} %{?!with_nas:-no-nas-sound}		\
		\
		-enable-opengl			\
		-dlopen-opengl			\
		\
		-qt-gif				\
		-qt-imgfmt-png			\
		-qt-imgfmt-jpeg			\
		-plugin-imgfmt-mng		\
		\
		-plugin-sql-odbc		\
		-plugin-sql-psql		\
		-plugin-sql-mysql		\
		%{?with_ibase:-plugin-sql-ibase}		\
		-plugin-sql-sqlite		\
		\
		-lfontconfig			\
		-inputmethod			\
		%{?with_glibmainloop:-glibmainloop} \
		-debug \
		-v

# proceed
%__make %{?_smp_mflags} sub-src sub-plugins sub-tools

# build tqtconv2ui
%__make -C tools/designer/tools/tqtconv2ui

# build tqvfb
%__make -C tools/tqvfb

# fix .prl files
%__sed -i lib/*.prl -e "s|${QTDIR}|%{tde_datadir}/tqt3|g"


%install
%__rm -rf %{buildroot}
export QTDIR=$(pwd)
export PATH=${QTDIR}/bin:$PATH

# Installs 'libtqt-mt.so.3' library
%__make -C src INSTALL_ROOT=%{?buildroot} install_target

# Installs all the remaining
%__make INSTALL_ROOT=%{?buildroot} install
%__make INSTALL_ROOT=%{?buildroot} plugins-install

%__install -m755 bin/tqtrename140 %{?buildroot}%{_bindir}
%__install -m755 bin/tqt20fix %{?buildroot}%{_bindir}
%__install -m755 bin/tqtfindtr %{?buildroot}%{_bindir}

# install tqtconv2ui
%__install -m755 bin/tqtconv2ui %{?buildroot}%{_bindir}/tqtconv2ui

# install tqvfb
%__install -m755 tools/tqvfb/tqvfb %{?buildroot}%{_bindir}/tqvfb


%clean
%__rm -rf %{buildroot}


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.0-1
- Initial release for TDE R14.0.0
