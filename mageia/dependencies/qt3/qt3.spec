%define Werror_cflags %nil

# QTDIR is always /usr/lib/qt3, whether that's a lib64 architecture or
# not (sublibdirs are correctly qualified in the latter case however).
%define qtdir	%{_prefix}/lib/qt3
%define libqt3name	%mklibname qt 3

%define libqassistantname %mklibname qassistantclient 1
%define libdesignercore %mklibname designercore 1
%define libeditor %mklibname editor 1

%define nameqt	qt-x11-free

%define buildSQL 1
%{?_without_SQL: %{expand4 %%global buildSQL 0}}

%define buildDebug 0
%{?_with_debug: %{expand: %%global buildDebug 1}}

%define buildStatic 1
%{?_without_static: %{expand: %%global buildStatic 0}}

%define buildImmodule 1
%{?_without_immodule: %{expand: %%global buildImmodule 0}}

%define plugindir  %_libdir/qt3/plugins

Name: qt3
Version: 3.3.8.d
Release: %mkrel 1%{?dist}
License: GPLv3+ and QPL
Summary: Qt3 Sources
Group: System/Libraries
URL: http://www.trolltech.com
#Source: %nameqt-%version.tar.gz
Source0: qt3-3.3.8.d.tar.gz
Source1: qt3.macros
Source2: qt3-assistant.desktop
Source3: qt3-designer.desktop
Source4: qt3-linguist.desktop
Source5: qt3-designer-sh
Source6: qt3-assistant-sh
Source7: qt3-uic-sh
Source8: qt3-README-Mageia
Source9: 90qtrc-jp
Patch1: qt-3.1.1-fix-xft2-compile.patch
Patch2: qt-3.2.3-fix-cupslib.patch
Patch4: qt-x11-free-3.3.5-no-rpath.patch
Patch5: qt-3.3.2-fix-configure.patch
Patch8: qt-3.3.5-lib64-plugins.patch
Patch10: qt-3.3.3-fix-accessible.patch
Patch12: fix-key-release-event-with-imm.diff
Patch13: qt-x11-free-3.3.6-lib64.patch
Patch14: qt-x11-free-3.3.4-linux32.patch
Patch15: qt-visibility.patch
Patch16: qt-x11-free-3.3.5-makelibshared.patch
Patch24: qt-x11-free-3.3.5-qtranslator-crash.patch
Patch28: qt-x11-immodule-nodebug.diff
Patch29: fix-x11-immodule.diff
Patch30: fix-im-crash-on-exit.diff
Patch31: workaround-for-xlib-xim-bug.diff
Patch56: qt3-3.3.6-fix-xorg7.0.patch
Patch58: qt-3.3.6-fix-qfile-message-error.patch
Patch59: qt-3.3.6-fix-qfile-message-error2.patch
Patch63: qt-x11-free-3.3.8-qmo35263.patch
Patch64: qt-x11-free-3.3.8b-unixodb-64.patch
Patch65: qt-x11-free-3.3.8b-cstddef.patch
Patch66: qt-x11-free-3.3.8b-force-png12.patch
#-------------- KDE qt-copy patches ( added the relevant ones )
Patch102: 0017-qiconview-ctrl_rubber.patch 
Patch104: 0035-qvaluelist-streaming-operator.patch 
Patch115: 0078-argb-visual-hack.patch 
Buildroot: %_tmppath/%name-%version-%release-root
%if %buildSQL
BuildRequires: mysql-devel 
BuildRequires: unixODBC-devel 
BuildRequires: libpq-devel
%endif
BuildRequires: freetype2-devel
BuildRequires: mesaglu-devel
BuildRequires: libsm-devel
BuildRequires: libice-devel
BuildRequires: libx11-devel
BuildRequires: libxcursor-devel
BuildRequires: libxext-devel
BuildRequires: libxft-devel
BuildRequires: libxinerama-devel
BuildRequires: libxmu-devel
BuildRequires: libxrandr-devel
BuildRequires: libxrender-devel
BuildRequires: fontconfig-devel
BuildRequires: bzip2-devel
BuildRequires: libjpeg-devel
BuildRequires: libmng-devel
BuildRequires: pkgconfig(libpng12)
BuildRequires: zlib-devel 
BuildRequires: nas-devel
BuildRequires: libiodbc-devel
%if "%{_lib}" != "lib"
BuildRequires: linux32
%endif
BuildRequires: postgresql-devel

%description
Qt is a complete and well-designed multi-platform object-oriented framework for
developing graphical user interface (GUI) applications using C++. Qt has
seamless integration with OpenGL/Mesa 3D libraries.

#--------------------------------------------------------------------

%package -n %libqt3name
Summary: Qt3 - Shared libraries
Group: System/Libraries
Requires: %{name}-common = %version
Provides:	qt3 = %{version}-%{release}

%description -n %libqt3name
Qt is a complete and well-designed multi-platform object-oriented framework for
developing graphical user interface (GUI) applications using C++. Qt has
seamless integration with OpenGL/Mesa 3D libraries.

This package contains shared libraries. 

%postun -n %libqt3name 
if [ "$1" = "0" ]; then
   rm -f /etc/ld.so.conf.new
   grep -v -e "^%qtdir/%_lib$" /etc/ld.so.conf > /etc/ld.so.conf.new
   mv -f /etc/ld.so.conf.new /etc/ld.so.conf
fi

%files -n %libqt3name
%defattr(-,root,root,-)
%dir %qtdir/
%_libdir/libqt-mt.so.3
%_libdir/libqt-mt.so.3.3
%_libdir/libqt-mt.so.3.3.8
%_libdir/libqt-mt.la
%_libdir/libqui.so.1
%_libdir/libqui.so.1.0
%_libdir/libqui.so.1.0.0
%_libdir/*.prl

%dir %{plugindir}/styles/
%{plugindir}/styles/*style.so

%if %{buildImmodule}
%dir %{plugindir}/inputmethods/
%{plugindir}/inputmethods/*.so
%endif

#--------------------------------------------------------------------

%package -n %libqt3name-devel
Summary: Qt3 - Files needed to build Qt3 based applications
Group: Development/KDE and Qt
Requires: %libqt3name = %version-%release
Requires: %{libeditor} = %version-%release
Requires: %{libqassistantname} = %version-%release
Requires: %{libdesignercore} = %version-%release
Provides: libqt-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: libqt3-pch-headers < 3.3.5

%description -n %libqt3name-devel
The qt3-devel package contains the files necessary to develop
applications using the Qt GUI toolkit: the header files, the Qt meta
object compiler.

%post -n %libqt3name-devel
update-alternatives --install %_bindir/qmake qmake %qtdir/bin/qmake 10

%postun -n %libqt3name-devel
if ! [ -e %qtdir/bin/qmake ]; then
  update-alternatives --remove qmake %qtdir/bin/qmake
fi

%files -n %libqt3name-devel
%defattr(-,root,root,-)
%doc %_mandir/man1/*
%doc %_mandir/man3/*
%_bindir/designer-qt3
%_libdir/*.so
%_sysconfdir/rpm/macros.d/*
%_libdir/pkgconfig/*.pc
%_datadir/applications/*
%dir %qtdir/
%dir %qtdir/bin
%qtdir/bin/designer 
%qtdir/bin/lrelease  
%qtdir/bin/moc    
%qtdir/bin/%multiarch_platform/qmake
%qtdir/bin/qmake
%qtdir/bin/uic
%qtdir/bin/lupdate   
%qtdir/bin/qm2ts  
%dir %qtdir/include/%multiarch_platform
%qtdir/include/%multiarch_platform/*.h
%dir %qtdir/include/
%qtdir/include/*
%dir %qtdir/templates/
%qtdir/templates/*.ui
%dir %{plugindir}/designer
%{plugindir}/designer/*
%dir %qtdir/mkspecs/
%qtdir/mkspecs/*
%dir %qtdir/src/
%qtdir/src/*
%{qtdir}/bin/createcw
%{qtdir}/bin/makeqpf
%{qtdir}/bin/mergetr
%{qtdir}/bin/msg2qm
%{qtdir}/bin/qembed
%dir %qtdir/bin/%multiarch_platform

#--------------------------------------------------------------------
%if %{buildStatic}

%package -n %libqt3name-static-devel
Summary: Qt3 - Static files needed to build Qt3 based applications
Group: Development/KDE and Qt
Requires: %libqt3name-devel = %version-%release
Provides: libqt-static-devel = %{version}-%{release}
Provides: %{name}-static-devel = %{version}-%{release}

%description -n %libqt3name-static-devel
This package contains:
  - files needed to build static Qt based applications

%files -n %libqt3name-static-devel
%defattr(-,root,root,-)
%_libdir/*.a

%endif

#--------------------------------------------------------------------

%package common
Summary:	Config, language file for Qt
Group:      Development/KDE and Qt
Requires:   %libqt3name = %version
Obsoletes:	libqt3-common < %{version}-%{release}
Provides:	libqt3-common = %{version}-%{release}
# Laurent : allow to install package which use this provides (commercial packages which want to install under distro and used this provides
Provides:	qt = %{version}-%{release}
Provides:	qt3 = %{version}-%{release}

%description common
This package contains all config file and language file

%post common
update-alternatives --install %_bindir/qtconfig qtconfig %qtdir/bin/qtconfig 10

%postun common
if ! [ -e %qtdir/bin/qtconfig ]; then
  update-alternatives --remove qtconfig %qtdir/bin/qtconfig 
fi

%files common
%defattr(-,root,root,-)
%dir %{plugindir}
%if %buildSQL
%dir %{plugindir}/sqldrivers
%endif
%dir %qtdir/phrasebooks/
%qtdir/phrasebooks/*.qph
%dir %qtdir/
%dir %qtdir/bin
%qtdir/bin/qtconfig
%_sysconfdir/profile.d/*.csh
%_sysconfdir/profile.d/*.sh
%config(noreplace) %_sysconfdir/qtrc
%config(noreplace) %_sysconfdir/kstylerc
%dir %qtdir/translations/
%qtdir/translations/*.qm
%_sysconfdir/X11/xinit.d/*

#--------------------------------------------------------------------

%if %buildSQL
%package -n %libqt3name-mysql
Summary: 	MySQL plugin for Qt
Group: 		Development/KDE and Qt
Requires:	%libqt3name = %version-%release
Provides:	%{name}-MySQL = %{version}-%{release}

%description -n %libqt3name-mysql
This package contain the MySQL plugin for Qt.

%files -n %libqt3name-mysql
%defattr(-,root,root)
%{plugindir}/sqldrivers/libqsqlmysql.so


%package -n %libqt3name-psql
Summary: 	PostgresSQL plugin for Qt
Group: 		Development/KDE and Qt
Requires:	%libqt3name = %version-%release
Provides:	%{name}-PostgreSQL = %{version}-%{release}

%description -n %libqt3name-psql
This package contain the PostgresSQL plugin for Qt.


%files -n %libqt3name-psql
%defattr(-,root,root)
%{plugindir}/sqldrivers/libqsqlpsql.so

%package -n %libqt3name-odbc
Summary: 	ODBC plugin for Qt
Group: 		Development/KDE and Qt
Requires:	%libqt3name = %version-%release
Provides:	%{name}-ODBC = %{version}-%{release}

%description -n %libqt3name-odbc
This package contain the ODBC plugin for Qt.


%files -n %libqt3name-odbc
%defattr(-,root,root)
%{plugindir}/sqldrivers/libqsqlodbc.so


%package -n %libqt3name-sqlite
Summary: 	Sqlite 2 plugin for Qt
Group: 		Development/KDE and Qt
Requires:	%libqt3name = %version-%release
Provides:	%{name}-Sqlite = %{version}-%{release}

%description -n %libqt3name-sqlite
This package contain the Sqlite 2 plugin for Qt.

%files -n %libqt3name-sqlite
%defattr(-,root,root)
%{plugindir}/sqldrivers/libqsqlite.so

%endif

#--------------------------------------------------------------------

%package -n %libqassistantname
Summary: Qt3 - Shared libraries
Group: System/Libraries

%description -n %libqassistantname
Qt3 - Shared libraries

%files -n %libqassistantname
%defattr(-,root,root)
%_libdir/libqassistantclient.so.*

#--------------------------------------------------------------------

%package assistant
Summary: Qt assistant
Group: Development/KDE and Qt

%description assistant
This package contain Qt assistant

%files assistant
%defattr(-,root,root)
%_bindir/assistant-qt3
%qtdir/bin/assistant  

#--------------------------------------------------------------------

%package linguist
Summary: Qt linguist
Group: Development/KDE and Qt

%description linguist
This package contain Qt linguist

%files linguist
%defattr(-,root,root)
%qtdir/bin/linguist       

#--------------------------------------------------------------------

%package -n %libdesignercore
Summary: Qt3 - Shared libraries
Group: System/Libraries

%description -n %libdesignercore
Qt3 - Shared libraries

%files -n %libdesignercore
%defattr(-,root,root)
%_libdir/libdesignercore.so.*

#--------------------------------------------------------------------

%package -n %libeditor
Summary: Qt3 - Shared libraries
Group: System/Libraries

%description -n %libeditor
Qt3 - Shared libraries

%files -n %libeditor
%defattr(-,root,root)
%_libdir/libeditor.so.*

#--------------------------------------------------------------------

%package example
Summary:    Qt examples
Group:      Development/KDE and Qt
Obsoletes:  libqt3-example
Provides:   libqt3-example
BuildArch: noarch

%description example
This package contain Qt example.

%files example
%defattr(-,root,root)
%dir %_docdir/%name/examples
%doc %_docdir/%name/examples/*

#--------------------------------------------------------------------

%package tutorial
Summary:    Qt tutorials
Group:      Development/KDE and Qt
BuildArch: noarch

%description tutorial
This package contain Qt tutorial.

%files tutorial
%defattr(-,root,root)
%dir %_docdir/%name/tutorial
%doc %_docdir/%name/tutorial/*

#--------------------------------------------------------------------

%package doc
Summary: Qt documentation
Group: Development/KDE and Qt
Conflicts:libqt3-devel <= 3.3.4-13mdk
BuildArch: noarch

%description doc
This package contain Qt documentation

%post doc
# Remove old qt3 doc directories
find %_docdir -maxdepth 1 -type d -name qt-3.\* -exec rm -rf {} \;

%files doc
%dir %_docdir/%name
%doc %_docdir/%name/FAQ
%doc %_docdir/%name/LICENSE*
%doc %_docdir/%name/README*
%dir %_docdir/%name/doc/
%dir %_docdir/%name/doc/html/
%doc %_docdir/%name/doc/html/*
%dir %qtdir/doc/
%qtdir/doc/html

#--------------------------------------------------------------------


%prep
%setup -q -n qt3

%patch1 -p1 -b .fix_xft_compile
%patch2 -p1 -b .fix_cups_lib
%patch4 -p0 
%patch5 -p1 -b .fix_configure_space
%patch13 -p1 -b .lib64
%patch14 -p1 -b .linux32
%patch10 -p1 -b .fix_accessible
%patch15 -p1 -b .fix_qt_export
%patch16 -p1 -b .sharedlibs
%patch24 -p0 -b .qtranslator
%patch56 -p1 -b .fix_xorg_7.0
%patch58 -p1 -b .fix_qfile_message_error
%patch59 -p1 -b .fix_qfile_message_error
%patch63 -p0 -b .fix_bug_35263
%if "%_lib" == "lib64"
%patch64 -p0 -b .fix_unixodbc
%endif
%patch65 -p1 -b .gcc46
%patch66 -p0 -b .libpng
# KDE qt-copy patches
%patch102 -p0 -b .qt-copy
%patch104 -p0 -b .qt-copy
%patch115 -p0 -b .qt-copy

# (Anssi 01/2008)
# Hack to disable stripping, a better fix for configure script welcome:
mkdir -p stripbin
echo "#!/bin/true" > stripbin/strip
chmod +x stripbin/strip

sed -e "s|^QMAKE_STRIP.*=.*|QMAKE_STRIP =|" -i mkspecs/linux-g++*/qmake.conf
sed -e "s|^QMAKE_CFLAGS\t.*$|QMAKE_CFLAGS = %{optflags}  -DPIC -fPIC|" \
        -e "s|^QMAKE_LFLAGS\t.*=.*$|QMAKE_LFLAGS = %{ldflags} |" \
        -e "s|^QMAKE_LFLAGS_PLUGIN\t.*\+= |QMAKE_LFLAGS_PLUGIN = %(echo %ldflags|sed -e 's#-Wl,--no-undefined##') |" \
        -i mkspecs/linux-g++*/qmake.conf

%build
export QTDIR=$(/bin/pwd)
export PATH=$(pwd)/stripbin:$QTDIR/bin:$PATH
export MANPATH=$QTDIR/doc/man:$MANPATH
export LD_LIBRARY_PATH=$QTDIR/lib:$LD_LIBRARY_PATH

%if %{buildImmodule}
sh ./make-symlinks.sh
%endif

# Default platform (take care to lib64 arches)
PLATFORM=linux-g++
%if "%_lib" == "lib64"
PLATFORM=linux-g++-64
%endif
echo "#define QT_MITSHM" >> mkspecs/${PLATFORM}/qplatformdefs.h

function main_configure {
echo "yes" | ./configure \
	-I/usr/include/postgresql/server/ \
	-I/usr/include/fontconfig \
	-I/usr/include/Xft2 \
	-I/usr/include/Xft2/X11/Xft \
	-I/usr/include/mysql/ \
	-I/usr/include/libpng12 \
	-prefix %qtdir/ \
	-libdir %_libdir \
	-plugindir %{plugindir} \
	-sysconfdir %_sysconfdir \
	-docdir %_docdir/%name/doc/ \
   %if %{buildDebug}
   -debug \
   %else
	-release \
   %endif
	-qt-gif \
	-system-zlib \
	-no-exceptions \
	-platform $PLATFORM \
	-enable-tools \
	-enable-kernel \
	-enable-widgets \
	-enable-dialogs \
	-enable-iconview \
	-enable-workspace \
	-enable-network \
	-enable-canvas \
	-enable-table \
	-enable-xml \
	-enable-input \
	-enable-opengl \
	-dlopen-opengl \
	%if %buildSQL		
		-enable-sql \
		-plugin-sql-mysql \
		-plugin-sql-odbc \
		-plugin-sql-psql \
		-plugin-sql-sqlite \
	%endif
	-plugin-style-cde \
	-plugin-style-compact \
	-plugin-style-motif \
	-plugin-style-sgi \
	-plugin-style-platinum \
	-plugin-style-motifplus \
	-thread \
	-stl \
	-qt-imgfmt-png \
	-qt-imgfmt-jpeg \
	-qt-imgfmt-mng  \
	-system-libpng \
	-system-libjpeg \
	-system-libmng \
	-sm \
	-xkb \
	-xinerama \
	-xrender \
	-xrandr \
	-xcursor \
	-xft \
	-nis \
	-no-tablet \
	-v \
	-xkb \
	$*
}

%if %{buildStatic}

main_configure -static 
pushd src
	%make && make INSTALL_ROOT=%{buildroot} install_target
popd
mkdir -p safelib
mv -f lib/libqt-mt.a safelib
%endif

# Build shared
main_configure -shared 
%make symlinks src-qmake src-moc sub-src sub-tools

%install
export QTDIR=$(/bin/pwd)
export PATH=$(pwd)/stripbin:$QTDIR/bin:$PATH
export MANPATH=$QTDIR/doc/man:$MANPATH
export LD_LIBRARY_PATH=$QTDIR/lib:$LD_LIBRARY_PATH
rm -fr %buildroot

make install INSTALL_ROOT=%buildroot/

rm -rf %buildroot/%qtdir/bin/qmake
install -m 0755  qmake/qmake %buildroot/%qtdir/bin/

# David - 3.0.0-0.11mdk - Install a README for Mandriva Linux
install -m 0644 %SOURCE8 %buildroot/%_docdir/%name/README.Mandriva_Linux
perl -pi -e "s|QtVersion|%version|" %buildroot/%_docdir/%name/README.Mandriva_Linux
perl -pi -e "s|PackageVersion|%version-%release|" %buildroot/%_docdir/%name/README.Mandriva_Linux

# David - 3.0.0-0.11mdk - Install missing documentation
install -d -m 0755 %buildroot/%_docdir/%name/
install -m 0644 FAQ       %buildroot/%_docdir/%name/
install -m 0644 LICENSE*  %buildroot/%_docdir/%name/
install -m 0644 README    %buildroot/%_docdir/%name/
install -m 0644 README-QT.TXT %buildroot/%_docdir/%name/

# David - 3.0.0-0.11mdk - Install man pages
install -d -m 0755 %buildroot/%_mandir/man1/
for i in doc/man/man1/* ; do
		if [ ! -d $i ] ; then
		   install -m 0644 $i %buildroot/%_mandir/man1/
		fi
done
#
install -d -m 0755 %buildroot/%_mandir/man3/
for i in doc/man/man3/* ; do
	    if [ ! -d $i ] ; then
   			install -m 0644 $i %buildroot/%_mandir/man3/
	    fi
done

install -d -m 0755 %buildroot/%_bindir/
install -m 0755 bin/moc %buildroot/%qtdir/bin/moc

# David - 3.0.1-2mdk - Install .pri files needed to build examples and tutorials
install -d -m 0755 %buildroot/%qtdir/src/
for i in src/*.pri; do
   install -m 0644 $i %buildroot/%qtdir/src/
done


cp -ar examples/ %buildroot/%_docdir/%name
cp -ar tutorial/ %buildroot/%_docdir/%name

# Fix include directory for examples ( based on David Faure changes )
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../../include|%qtdir/include|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../include|%qtdir/include|"

# Fix lib directory for examples
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../../../lib/libqt-mt.prl|%_libdir/libqt-mt.prl|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../../lib/libqt-mt.prl|%_libdir/libqt-mt.prl|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../lib/libqt-mt.prl|%_libdir/libqt-mt.prl|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../src/qt_professional.pri|%qtdir/src/qt_professional.pri|"

# Set RPM_BUILD_DIR to QTDIR
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|%_builddir/qt-%version|%qtdir|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|%_builddir/qt-x11-free-%version/mkspecs/|%qtdir/mkspecs/|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|%_builddir/qt-x11-free-%version/|%qtdir/|"
find %buildroot/%_docdir/%name/{examples,tutorial} -name Makefile | xargs perl -pi -e "s|../../lib/libqassistantclient.prl|%_libdir/libqassistantclient.prl|"

# Remove .obj .moc directories
for name in `find %buildroot/%_docdir/%name/{examples,tutorial} -type d -name .obj`; do
   rm -rf $name
done
for name in `find %buildroot/%_docdir/%name/{examples,tutorial} -type d -name .moc`; do
   rm -rf $name
done

install -m 0755 %SOURCE5 %buildroot/%_bindir/designer-qt3
install -m 0755 %SOURCE6 %buildroot/%_bindir/assistant-qt3

cd %buildroot/%qtdir/
install -d -m 0755 doc
ln -s %_docdir/%name/doc/html/ doc/html
cd -

install -d -m 0755 %buildroot/%_sysconfdir/profile.d/
cat >> %buildroot/%_sysconfdir/profile.d/qt.csh << EOF
if (! \$?QTDIR ) then
    setenv QTDIR "%qtdir"
endif
if (! \$?QTINC ) then
    setenv QTINC "%qtdir/include"
endif
if (! \$?QTLIB ) then
    setenv QTLIB "%_libdir"
endif
if (! \$?QT_XFT ) then
    setenv QT_XFT 0
endif
EOF

cat >> %buildroot/%_sysconfdir/profile.d/qt.sh << EOF
#! /bin/bash
[ -z "\$QTDIR" ] && QTDIR="%qtdir"
[ -z "\$QTINC" ] && QTINC="%qtdir/include"
[ -z "\$QTLIB" ] && QTLIB="%_libdir"
[ -z "\$QT_XFT" ] && QT_XFT=0

if ! echo \${PATH} | /bin/grep -q \$QTDIR/bin ; then
   PATH=\$QTDIR/bin:\${PATH}
fi

export PATH QTDIR QTINC QTLIB QT_XFT
EOF

# Generate default qtrc
install -d -m 0755 %buildroot/%_sysconfdir/
cat >> %buildroot/%_sysconfdir/qtrc << EOF
[3.3]
libraryPath=%{plugindir}

[General]
enableXft=true
font=Sans,10,-1,5,0,0,0,0,0,0
style=plastik
useXft=true
EOF

cat >> %buildroot/%_sysconfdir/kstylerc << EOF
[Settings]
MenuDropShadow=true
MenuOpacity=0.9
MenuTransparencyEngine=Disabled
SemiTransparentRubberband=true
EOF


install -d -m 0755 %buildroot/%_datadir/applications
install -m 0644 %SOURCE2 %buildroot/%_datadir/applications/qt3-assistant.desktop
install -m 0644 %SOURCE3 %buildroot/%_datadir/applications/qt3-designer.desktop
install -m 0644 %SOURCE4 %buildroot/%_datadir/applications/qt3-linguist.desktop

# Multiarch fixes
%multiarch_binaries %buildroot%qtdir/bin/qmake

%multiarch_includes %buildroot%qtdir/include/qconfig.h

%if %{buildStatic}
# Static install
install -d -m 0755 %buildroot/%_libdir/ 
install -m644 safelib/*  %{buildroot}/%_libdir/
%endif

# Removing invalid symlink. They really should not be here
# Old symlink if was set in right place, would create a cyclic symlynk
cd %buildroot/%qtdir/mkspecs/
if [ -h default ]; then
   rm -f default/linux*
fi
# provide default64 for multiarch devel
%if "%_lib" == "lib64"
ln -sf linux-g++-64 default64
%endif
cd -

# Install rpm macros
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
install -m 0644 %SOURCE1 %buildroot/%_sysconfdir/rpm/macros.d

mkdir -p %buildroot/%_sysconfdir/X11/xinit.d/
install -m 0755 %SOURCE9 %buildroot/%_sysconfdir/X11/xinit.d/

# Fix all buildroot paths

%clean
rm -fr %buildroot





%changelog
* Sat Jul 27 2012 Francois Andriot <francois.andriot@free.fr> 3.3.8.d-1
- Initial build for MGA2

* Mon Dec 26 2011 fwang <fwang> 3.3.8b-30.mga2
+ Revision: 187720
- set system flags

* Thu Dec 08 2011 fwang <fwang> 3.3.8b-27.mga2
+ Revision: 178838
- rebuild for new odbc

* Thu Sep 15 2011 fwang <fwang> 3.3.8b-26.mga2
+ Revision: 143741
- force libpng12
- drop png14 patch
- add incluedir for libpng12
- build with png12 (old libs, not required by any other packages besides lsb)
- add arch patch to fix build with latest libpng
- rebuild for new libpng

* Fri Mar 25 2011 dmorgan <dmorgan> 3.3.8b-25.mga1
+ Revision: 77244
- Rebuild against new mysql

* Tue Feb 01 2011 stewb <stewb> 3.3.8b-24.mga1
+ Revision: 45606
- bump release
- include,mkspecs,templates always in lib/qt3
- qt3 is blacklisted, build a stripped down version with no -devel (for LSB)
- imported package qt3


* Mon Jan 31 2011 Stew Benedict <stewbintn@gmail.com>
- initial import/clean

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 3.3.8b-22mdv2011.0
+ Revision: 627007
- rebuilt against mysql-5.5.8 libs, again

* Mon Dec 27 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.8b-21mdv2011.0
+ Revision: 625428
- rebuilt against mysql-5.5.8 libs

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 3.3.8b-20mdv2011.0
+ Revision: 604333
- rebuild for new zlib

  + Thierry Vignaud <tv@mandriva.org>
    - let the doc subpackage be noarch

* Wed Feb 17 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.8b-18mdv2010.1
+ Revision: 507040
- rebuild

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.8b-17mdv2010.1
+ Revision: 488797
- rebuilt against libjpeg v8

* Sun Aug 16 2009 Funda Wang <fwang@mandriva.org> 3.3.8b-16mdv2010.0
+ Revision: 416869
- rebuild for libjpeg7

* Wed Jun 10 2009 Helio Chissini de Castro <helio@mandriva.com> 3.3.8b-15mdv2010.0
+ Revision: 384888
- Create xinit.d entry for jp
- Remove invalid rubber add patch

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 3.3.8b-14mdv2009.1
+ Revision: 364936
- really fix configure_qt3 (introduce libdir declaration)

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 3.3.8b-13mdv2009.1
+ Revision: 364863
- fix configure_qt3

* Mon Feb 09 2009 Helio Chissini de Castro <helio@mandriva.com> 3.3.8b-12mdv2009.1
+ Revision: 338888
- Added unixodbc 64 bits patch to compile
- Get rid of patch fuzz issue
- Fix qt3 macros to rebuild qt3 apps

  + Oden Eriksson <oeriksson@mandriva.com>
    - use lowercase mysql-devel

* Sun Dec 07 2008 Funda Wang <fwang@mandriva.org> 3.3.8b-11mdv2009.1
+ Revision: 311526
- rebuild for new mysql

* Tue Oct 21 2008 Helio Chissini de Castro <helio@mandriva.com> 3.3.8b-10mdv2009.1
+ Revision: 296186
- Avoid environment vars be expanded

* Tue Oct 21 2008 Helio Chissini de Castro <helio@mandriva.com> 3.3.8b-9mdv2009.1
+ Revision: 296154
- Cleanup environment

* Tue Sep 30 2008 Helio Chissini de Castro <helio@mandriva.com> 3.3.8b-8mdv2009.0
+ Revision: 290138
- Remove PATH for qt3 bin, was a bad idea at all. Moved the necessary things for qt3 macros in configure_qt3

* Wed Sep 24 2008 Helio Chissini de Castro <helio@mandriva.com> 3.3.8b-7mdv2009.0
+ Revision: 287878
- Qt3 never should have his path before qt4

* Tue Sep 23 2008 Helio Chissini de Castro <helio@mandriva.com> 3.3.8b-6mdv2009.0
+ Revision: 287517
- postgres has headers in different place now
- Add PATH to bin qt3

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - ensure comment does not appear in qt3-common's %%postun
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jun 02 2008 Helio Chissini de Castro <helio@mandriva.com> 3.3.8b-4mdv2009.0
+ Revision: 214268
- Changed qt3plugins for proper place. Thanks to Funda Wang to point this. Fix bug https://qa.mandriva.com/show_bug.cgi?id=41183
- Added qmake_qt3 macro and qt3bin

* Tue May 27 2008 Helio Chissini de Castro <helio@mandriva.com> 3.3.8b-3mdv2009.0
+ Revision: 211755
- As suggested by pixel, libraries now sit under _libdir. To join the movement, plugins gone now to _libdir/qt3/plugins, which made a cleaner solution for install both plugins and libs for i586 and x86_64
- No shell script was harmed during this task...

* Mon May 26 2008 Helio Chissini de Castro <helio@mandriva.com> 3.3.8b-2mdv2009.0
+ Revision: 211435
- Fixed ld.so.conf.d dir creation
- As new gcc 4.3.1 becomes more pedantic, small changes are needed in the immoldule patch
- Moving the ld.so.conf parsing to a ld.so.conf.d solution

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-not-capitalized

* Mon Jan 28 2008 Helio Chissini de Castro <helio@mandriva.com> 3.3.8b-1mdv2008.1
+ Revision: 159197
- Introducing qt 3.3.8b, the official GPL v3 release. Beyond the GPL v3 release, some patches and fixes intended to be in
  possible future release 3.3.9 was added, so here's the list of previous package patches already merged:
- qt-3.3.8-fix-chinese-japanese-font.patch
- qt3-3.3.8-fix-CVE-2007-4137.patch
- qt-x11-free-3.3.8.tar.bz2
- 0081-format-string-fixes.diff
- 0077-utf8-decoder-fixes.diff
- qt3-fix-unicode-font-cache.patch
- qt3-3.3.8-fix-mysql-segfault.patch
- 0076-fix-qprocess.diff

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add patch to fix chinese and japanese fonts (Bug #17014)

* Thu Jan 24 2008 Anssi Hannula <anssi@mandriva.org> 3.3.8-13mdv2008.1
+ Revision: 157672
- use optflags (they were dropped without log entry in 2005, probably
  inadvertently)
- fix debug packages (do not strip before symbols are collected)

* Wed Jan 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.3.8-12mdv2008.1
+ Revision: 153774
- no executable bit on profile.d scriptlet

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 23 2007 Helio Chissini de Castro <helio@mandriva.com> 3.3.8-11mdv2008.1
+ Revision: 111592
- Due to next release Qt4 will be major qt environment, we needeed change a few things on qt3:
- No more designer and assistant pure links on /usr/bin. Using alternatives. Desktop files points to *-qt3
  to be present on menu
- No more qmake link on /usr/bin. Provided by alternatives. Qt4 have priority.
- No more qtconfig link on /usr/bin. Provided by alternatives. qt4 have priority
- qt bin dir isn't in the PATH anymore. Not needed
- QTDIR remains . Qt4 nor depends on this var except in for build.
- ld.so.conf.d entries remains untouchable
- Qt4 and Qt3 still can be installed simultaneously. The only difference now is that if user need
  qt3 build environment by default, need change the alternatives for qtconfig and qmake. So
  update-alternative --config qmake should do the job

* Mon Nov 12 2007 Funda Wang <fwang@mandriva.org> 3.3.8-10mdv2008.1
+ Revision: 108175
- rebuild for new lzma

  + Thierry Vignaud <tv@mandriva.org>
    - fix description (this is neither License tag nor build explanations)

* Sun Nov 04 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.3.8-9mdv2008.1
+ Revision: 105615
- [BUGFIX] Fix bug with DejaVu fonts (Patch 63) (Bug #35263)

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Sat Sep 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.3.8-8mdv2008.0
+ Revision: 93831
- [BUGFIX] Fix mysql segfault ( Bug #34149)

* Fri Sep 14 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.3.8-7mdv2008.0
+ Revision: 85525
- Fix CVE-2007-4137
- Fix validation errors on desktop files
- Fix validation errors on desktop files

  + Funda Wang <fwang@mandriva.org>
    - fix Chinese translaitons of qt3-designer.desktop, it should be charset independent

* Tue Jul 31 2007 Helio Chissini de Castro <helio@mandriva.com> 3.3.8-6mdv2008.0
+ Revision: 57148
- Format string error fixes.
  http://trolltech.com/company/newsroom/announcements/press.2007-07-27.7503755960

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Clean descriptions
    -[BUGFIX] Fix Requires ( Bug #15491)

* Thu May 31 2007 Helio Chissini de Castro <helio@mandriva.com> 3.3.8-5mdv2008.0
+ Revision: 33430
- Removed old non used patches
- Added relevant ( non BIC ) patches from qt-copy, including composite aware.
  Most relevant is MIT-SHM patch, which should improve large image handling. All patches are
  documented internally.
- Remove switches for 2006 distro
- Created qt3-assistant and qt3-linguist packages
- Removed old debian like menudir entries
- Removed qt-copy switches ( patches comes separated now )

* Thu May 10 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.3.8-4mdv2008.0
+ Revision: 26148
- set $QTINC & $QTLIB in profile.d scripts to avoid special needs for
  qt apps at build time (finally fixes #27808)


* Fri Mar 30 2007 Laurent Montel <lmontel@mandriva.com> 3.3.8-4mdv2007.1
+ Revision: 149898
- Fix qt3 utf8 vulnerability

* Wed Mar 21 2007 Laurent Montel <lmontel@mandriva.com> 3.3.8-3mdv2007.1
+ Revision: 147483
- Fix qt3 default config

* Wed Mar 21 2007 Laurent Montel <lmontel@mandriva.com> 3.3.8-2mdv2007.1
+ Revision: 147345
- Fix space touch (I hope

* Tue Feb 27 2007 Laurent Montel <lmontel@mandriva.com> 3.3.8-1mdv2007.1
+ Revision: 126234
- Fix patch
- Add new immodule patch
  rediff all immodule patch
- 3.3.8
  (need to rediff some patch)

* Tue Feb 13 2007 Helio Chissini de Castro <helio@mandriva.com> 3.3.7-5mdv2007.1
+ Revision: 120391
- Moved qt doc dir for qt3, instead of qt-%%version. Since we can have officially one qt3 installed a
  time on Mandriva system, there's no need of versionated directories. This solves the issue of
  having multiple empty dirs from old upgrade. Similar approach need to be done on qt4 package.

  + Laurent Montel <lmontel@mandriva.com>
    - Don't requires on version-%%{release} as requested
    - Rebuild

* Mon Jan 08 2007 Laurent Montel <lmontel@mandriva.com> 3.3.7-3mdv2007.1
+ Revision: 106201
- Fix bn_IN rendering character

* Fri Jan 05 2007 Laurent Montel <lmontel@mandriva.com> 3.3.7-2mdv2007.1
+ Revision: 104421
- Rebuild

* Wed Oct 25 2006 Laurent Montel <lmontel@mandriva.com> 3.3.7-1mdv2007.0
+ Revision: 72261
- 3.3.7

* Fri Oct 20 2006 Laurent Montel <lmontel@mandriva.com> 3.3.6-19mdv2007.1
+ Revision: 71345
- Fix overflow

* Wed Sep 06 2006 Laurent Montel <lmontel@mandriva.com> 3.3.6-18mdv2007.0
+ Revision: 59934
- New package (3.3.6-18mdv 2006-09-05)
  Add patch to fix search xorg lib on all arch (patch from gb)
  Rebuild against new mysql

* Tue Sep 05 2006 Laurent Montel <lmontel@mandriva.com> 3.3.6-17mdv2007.0
+ Revision: 59714
- d
- New package (3.3.6-17mdv 2006-09-04)
  Add patch from Gwenole Beauchesne <gbeauchesne@mandriva.com>
- readd functional multiarch support
- fix 32-bit builds on lib64 systems
- fix menu file names in qt3-devel package
- augment X.org 7.0 path patch for other linux arches
- Fix bug #15491

* Fri Aug 11 2006 Laurent Montel <lmontel@mandriva.com> 3.3.6-16mdv2007.0
+ Revision: 55311
- New package (2006/08/10 3.3.6-16mdv)
  Add patch to improve qfile debug
- Better error message with qfile

* Sat Jul 29 2006 Helio Chissini de Castro <helio@mandriva.com> 3.3.6-14mdv2007.0
+ Revision: 42346
- Added rpm macros for qt. Now qt rpm packages can use the following macros
  %%qt3dir, %%qt3include, %%qt3lib, %%qt3plugins.
- Added path for Qt binaries. Some programs need access to devel binaries like lrelease
- Desktop files changed place
- Increase release
- Added arabic fonts fix provided by Trolltech
- Redent modification requires that qmake points for default itself. this fixes
  the bug http://qa.mandriva.com/show_bug.cgi?id=21522
- Fix typo
- Fix symlinks. This solve bug http://qa.mandriva.com/show_bug.cgi?id=15090, the
  "qt likes my build dir" infamous bug
- Of course, raise the release number...
- Immodule fix for the most nasty Mandriva Qt bug on Xim. Finally this bug can
  be closed. Reference: http://qa.mandriva.com/show_bug.cgi?id=16300
- Increase release and add %%mkrel
- Added patch for http://qa.mandriva.com/show_bug.cgi?id=16432
  Thanks for Michael Scherer for report
- Removed initial font speedup patch
- Updated with qt-copy from 20051216. This release have added two patches
  described bu Lubos Lunak ( l.lunak@kde.org ) on kde-packager list:
  "Two patches that make Qt rely noticeably less on (slow) fontconfig
  font listing, resulting in significant performance gains. They could
  still use a bit more testing, I myself consider them stable though."
- Remove -b from qmake patches, to avoid wrong addition in packaging
- Finally found qmake error on x86_64. Standard makefiles generated for x86_64
  arches pointed Qt library path for QTDIR/lib, and on Mandriva is QTDIR/lib64.
  This force packages like qca, which use plain qmake scripts, need a lot of
  perl, sed and changes to compile. This solves kdevelop base templates too.
- Fix multiarch plugins in a proper way, using standard qt configue. qt plugins
  now search lib or lib64 depending od their arch. No need more patches and spec
  changes, neiher add another option on configure
- Disable some explicit qDebug call making imm patch less annoying
- Fixed wrong %%config on qtrc. Should be (noreplace)
- Fixed plugin mess
- Clean a little bit more spec
- Fixed designer wrapper
- Fixed default qtrc to match lib<arch> under plugins
- Removed invalid info for tutorial and example build on README
- Fixed removal of extra .moc .obj in tutorial and examples
-Fixed sqlite patch. Correct sqlite version is 2, not 3
- Updated version before submit
- Added missing source
- Qt3 package sanitizing
- Removed all explicit qt-copy patches in favour of qt-copy standard
- Fixed again the immodule bug and merge minor xim adapted patch
- Added patch for no-strict-aliasing on OpenType ( from OpenSUSE )
- Added patch for disable input method on password entry ( from OpenSUSE )
- Added patch for match external sqlite library and avoid use of internal zlib
- Removed xmu patch
- Updated GL load patch
- Added patch for fix xpm handling ( from OpenSUSE )
- Added patch for takeitem crashes in qlistview ( from OpenSUSE )
- Added patch for fonts speedup ( from KDE project )
- Added visual rubberband patch from brazilian KDE developer Andr?\195?\169 Magalh?\195?\163es
- Added patch for qtranslator crash ( from OpenSUSE )
- Fixed plugin directory ( lib/lib64 ) for qt designer wrapper
- Added patch for designer plugins ( from OpenSUSE )
- Complete static-to-shared patch, with libdesignercore and libeditor
- Fixed library search for lib64 on unix test scripts
- Fixed svn changelog finally (none)
- Do not ship examples and tutorial in compressed format. Originally this
  solution was take as all code is compiled. Avoiding compilation make smaller
  packages.
- Remove qmake.cache
- Tutorial package restored
- We are Mandriva now
- Put changelog back on spec since breakage on svn ( again )
  * Tue Oct 25 2005 Helio Chissini de Castro <helio@mandriva.com> 3.3.5-1mdk
- Fix immpatch to compile
- Fix changelog merge
- Fix immpatch to compile
- Added libqassistant as shared. Some KDE apps since 3.5 need ( new kdevelop for
  kdevdesigner )
- Move file section to same package section
- Removed old 3.3.4 not used anymore
- Fixed my fault for not noted that svn isn' t up to date
- Added changelog back to spec avoiding temp the svn log problem ( inconsistency )
- Obsolete pch package
- Disable imm patch. Wrong input module code crash kicker output when some event comes from system tray and uses X11 event queue
- Updated with upstream package to subversion
- Bunzipped all patches
- Created doc package ( reduce devel package size )
- Created static-devel package
- Clean up spec to new layout, allowing both static and shared compilation
- Uploading current spec
- Uploading package ./qt3

  + Laurent Montel <lmontel@mandriva.com>
    - Simplify patch from neoclust to create menu entry
    - Use macro
    - Rebuild because cluster was not update...
      => I hope that now build will be ok
    - Fix search xorg lib when we are on x86_64 and compile with xorg >= 7.0
    - Increase release number
    - Readd patch to fix press enter
    - Add patch to improve xinerama support
    - Rebuild against new gcc-glibc
    - Fix install
      Diable nas
    - F**k split xorg lib...
    - I don't understand idea to split all lib....
    - Other buildrequires fix
    - Start to fix buildrequires with new xorg
    - quote not necessary
    - Fix error
    - Adapt to new xdg menu
    - Reactivate static lib for several project in connectiva
    - Increase version
    - Reactivate immodule
      Disable compile of static lib (any program use it)
      Remove unused patch
    - add patch
    - Update source
    - Time to update it => 3.3.6
      Adapt patch
      Disable for the moment inputmethod
      Next step fix all multi-arch "breakage"...
    - Add patch to disable patch36 which create BIC
      (apply just for MDK <=200600)
    - Rebuild for missing package
    - Add Provides qt3 (requested by Erwan)
    - Fix typo
      * Wed Nov 02 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.5-3mdk
    - Rebuild with new mysql
      * Thu Oct 27 2005 Helio Chissini de Castro <helio@mandriva.com> 3.3.5-2mdk
    - New immodule patch
    - 3.3.5
    - qt3.3.5
    - Fix postun when we have x86_64 and i586 pkg
    - Fix kicker crash (qtimm bugs...)
      * Mon Sep 19 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.4-23mdk
    - Fix kicker crash
    - Added libqassistant as shared. Some KDE apps since 3.5 need ( new kdevelop for
      kdevdesigner )
    - Move file section to same package section
    - Removed old 3.3.4 not used anymore
    - Allow to compile with all gcc4
    - Fix qt3 visibility support
    - Rebuild on x86_64 with new gcc
    - Update

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Sat May 21 2005 Laurent Montel <lmontel@mandriva.com>
+ 2005-07-06 08:08:53 (307)
- Rebuild on x86_64 with new gcc

* Mon May 16 2005 Helio Chissini de Castro <helio@mandriva.com>
+ 2005-06-28 20:23:48 (251)
- Updated with upstream package to subversion
- Bunzipped all patches
- Created doc package ( reduce devel package size )
- Created static-devel package
- Clean up spec to new layout, allowing both static and shared compilation

* Sat May 14 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.4-11mdk
- Enable sqlite
- Add patch114: fix kde bug #106974
- Add patch113: fix misscompile with gcc-4.0 (fix printing and co)

* Fri May 13 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.4-10mdk
- Add missing buildrequires on x86_64 : linux32

* Tue May 10 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.4-9mdk
- Try to activate immodule

* Thu May 05 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.4-8mdk
- Rebuild with new gcc-4.0.0

* Fri Apr 22 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.4-7mdk
- Fix qmake (patch from Gwenole)

* Tue Apr 12 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.3.4-6mdk
- Fix email
- multiarch & linux32 fixes

* Mon Mar 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.4-5mdk
- Rebuild

* Mon Feb 28 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.4-4mdk
-  Update patch100 and qt-immodule related things patch from UTUMI Hirosi <utuhiro78@yahoo.co.jp>

* Wed Feb 09 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.4-3mdk
- Remove perl -pi -e for man file (Fixed in this release)

* Thu Jan 27 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.4-2mdk
- Reapply some patch

* Wed Jan 26 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.4-1mdk
- 3.3.4

* Tue Jan 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-32mdk
- Add patch110 "correctly propagate orientation of wheel events to viewport/content of QScrollView"

* Wed Dec 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-31mdk
- Fix menu

* Thu Nov 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-30mdk
- Add patch109: fix kde bug #84434

* Tue Nov 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-29mdk
- Add patch105: fix 64bit fullscreen
- Add patch106: fix kde bug #88128 (fix focus)
- Add patch107: fix kde bug #58719 (fix qpopupmenu)
- Add patch108: fix kde bug #74778 (fix qpopupmenu)

* Fri Oct 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-28mdk
- Add patch105: fix QTextEdit::zoomIn/Out

* Fri Oct 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-27mdk
- Add qtrc default

* Fri Sep 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-26mdk
- Remove patch103: pb with image

* Wed Sep 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-25mdk
- Disable immodule, there is some bug reported on bugs.kde.org

* Sat Sep 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-24mdk
- Add patch103 fix mitshm image

* Tue Sep 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-23mdk
- Fix create %%_libdir/pkgconfig/ patch from Doug Keller <doug@voidstar.us> thanks

* Sat Sep 11 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-22mdk
- Move qtconfig link into %%_bindir

* Thu Sep 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-21mdk
- Fix load GL (patch from Gb)

* Wed Sep 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-20mdk
- Add patch97: fix qrichtext regression

* Tue Sep 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-19mdk
- Fix man page

* Fri Sep 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-18mdk
- Add patch96: fix qtoolbar fix kde bug #77047

* Fri Sep 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-17mdk
- Fix export QTDIR

* Fri Aug 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-16mdk
- Use qt-x11-immodule-bc-qt3.3.3.patch

* Fri Aug 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-15mdk
- Add patch101-102: fix qt-immute

* Fri Aug 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-14mdk
- Add patch92: fix load xmu
- Add patch93: fix accessible plugins
- Add patch94: fix xpm handling
- Add patch95: fix gif handler

* Thu Aug 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-13mdk
- Fix "qt3-set-QTDIR-environment-csh" too patch from "Nick Brown <nickbrown@mandrake.org>"

* Thu Aug 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-12mdk
- Adapt patch from Gb to define position of plugins dir 
		"handle multilib plugins dir"

* Thu Aug 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-11mdk
- Fix qtdir.sh fix from Nick Brown <nickbrown@mandrake.org>

* Thu Aug 26 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-10mdk
- Add patch90: fix qtconfig apply patch from "Amrein-Marie Christophe"

* Wed Aug 25 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-9mdk
- Fix menu

* Fri Aug 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-8mdk
- Remove unused patch

* Thu Aug 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-7mdk
- Create link to qt-mt.pc to /usr/lib/pkgconfig

* Thu Aug 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-6mdk
- Fix opengl

* Thu Aug 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-5mdk
- Disable patch88, but to load OpenGL extension we must install Mesa-devel...

* Tue Aug 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-4mdk
- Update qt-immute patch but not activated by default because java doesn't 
	work with this patch

* Sat Aug 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-3mdk
- Fix qmake mdk bug #10746

* Fri Aug 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-2mdk
- Minor clean spec

* Thu Aug 12 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.3-1mdk
- 3.3.3

* Fri Aug 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-28mdk
- Tiny spec file fix, patch from "Stefan van der Eijk" <stefan@eijk.nu> thanks.

* Thu Aug 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-27mdk
- Add conditional build to build qt-immodule (patch from titi)

* Tue Jul 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-26mdk
- Fix spec file

* Wed Jul 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-25mdk
- Add patch87: fix load opengl don't use libGL.so but libGL.so.1

* Tue Jul 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-24mdk
- Fix provides for qt3-pch-headers
- Add debug version

* Tue Jul 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-23mdk
- Try pch

* Sat Jul 10 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-22mdk
- Remove patch100 it breaks applet java into konqueror (I don't know why for the moment)

* Wed Jul 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-21mdk
- Fix mimetype

* Wed Jun 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-20mdk
- Fix example compile

* Wed Jun 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-19mdk
- Fix again

* Wed Jun 30 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-18mdk
- Fix .qmake.cache bug reported by Leon Widdershoven <leon.widdershoven@imasgroep.nl>

* Tue Jun 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-17mdk
- Add patch from UTUMI Hirosi <utuhiro78@yahoo.co.jp> support for qt-immodule
- Add patch86: fix image cache
- Add patch87: fix unicode font cache

* Wed Jun 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-16mdk
- Add patch84: fix qiconview repaint

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-15mdk
- Rebuild

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-14mdk
- Add patch83: fix space into qconfig.h (Austin Acton <aacton@yorku.ca> asked me that it will fix some problem into compile package)

* Wed May 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-13mdk
- Add patch82: fix kde bug 80072 "konqueror freezes for some seconds when selecting text in text field with mouse"

* Sat May 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-12mdk
- Fix patch81

* Sat May 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-11mdk
- Fix to found Sans font

* Sat May 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-10mdk
- Fix configure
- Add patch81: try to fix accent in french language

* Thu May 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-9mdk
- Fix patch47

* Wed May 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-8mdk
- Reapply patch to active aa by default

* Wed May 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-7mdk
- Add patch46: fix kmenu width
- Add some patch from qt-copy (patch to test)

* Wed May 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-6mdk
- Try to reactivate patch37

* Wed May 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-5mdk
- Reactive some patch/remove some ununsed patch

* Wed May 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-4mdk
- Disable compile to support qt3.3.2

* Thu Apr 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Thu Apr 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-20mdk
- Add patch45: fix qprinter + cups (workaround)

* Tue Apr 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-19mdk
- Add patch44: fix kuickshow fullscreen pb

* Thu Apr 01 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-18mdk
- Use mdkversion

