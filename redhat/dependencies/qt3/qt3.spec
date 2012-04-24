# Default version for this component
%if "%{?version}" == ""
%define version 3.3.8.d
%endif

# Always install under standard prefix
%define _prefix /usr

# This allows the legacy RHEL/Fedora patches to apply in TDE version.
%define _default_patch_fuzz 2

# The following QT4 packages should NOT be installed to
# allow QT3 compilation (please uninstall them prior to compile)
#  qt
#  qt-sqlite
#  qt-mysql
#  qt-x11
#  qt-devel
# ...maybe others !!!!

Name:			qt3
Version:		%{?version}
Release:		6%{?dist}
Summary:		The shared library for the Qt 3 GUI toolkit

License:		QPL or GPLv2 or GPLv3
Group:			System Environment/Libraries
URL:			http://www.trinitydesktop.org/

Obsoletes:		%{name} < %{version}-%{release}
Provides:		%{name} = %{version}-%{release}

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: qt3-3.3.8.d.tar.gz
Source2: qt.sh
Source3: qt.csh
Source4: designer3.desktop
Source5: assistant3.desktop
Source6: linguist3.desktop
Source7: qtconfig3.desktop

Patch1: qt-3.3.4-print-CJK.patch
Patch2: qt-3.0.5-nodebug.patch
Patch3: qt-3.1.0-makefile.patch
Patch4: qt-x11-free-3.3.7-umask.patch
Patch5: qt-x11-free-3.3.6-strip.patch
Patch7: qt-x11-free-3.3.2-quiet.patch
#Patch8: qt-x11-free-3.3.3-qembed.patch
Patch12: qt-uic-nostdlib.patch
Patch13: qt-x11-free-3.3.6-qfontdatabase_x11.patch
#Patch14: qt-x11-free-3.3.3-gl.patch
#Patch19: qt-3.3.3-gtkstyle.patch 
#Patch20: qt-x11-free-3.3.8b-gcc4-buildkey.patch
#Patch24: qt-x11-free-3.3.5-uic.patch
Patch25: qt-x11-free-3.3.8b-uic-multilib.patch
Patch27: qt-3.3.6-fontrendering-ml_IN-209097.patch
Patch29: qt-3.3.8-fontrendering-as_IN-209972.patch
Patch31: qt-3.3.6-fontrendering-te_IN-211259.patch
Patch32: qt-3.3.6-fontrendering-214371.patch
Patch33: qt-3.3.8-fontrendering-#214570.patch
Patch34: qt-3.3.6-fontrendering-ml_IN-209974.patch
Patch35: qt-3.3.6-fontrendering-ml_IN-217657.patch
Patch37: qt-3.3.6-fontrendering-gu-228452.patch
Patch38: qt-x11-free-3.3.8-odbc.patch
Patch39: qt-x11-free-3.3.7-arm.patch
Patch40: qt-x11-free-3.3.8b-typo.patch

# immodule patches
#Patch50: qt-x11-immodule-unified-qt3.3.8-20071116.diff.bz2
#Patch51: qt-x11-immodule-unified-qt3.3.5-20051012-quiet.patch
#Patch52: qt-x11-free-3.3.8b-fix-key-release-event-with-imm.diff
Patch53: qt-x11-free-3.3.6-qt-x11-immodule-unified-qt3.3.5-20060318-resetinputcontext.patch

# qt-copy patches
#Patch100: 0038-dragobject-dont-prefer-unknown.patch
#Patch101: 0047-fix-kmenu-width.diff
#Patch102: 0048-qclipboard_hack_80072.patch
#Patch103: 0056-khotkeys_input_84434.patch
#patch105: 0073-xinerama-aware-qpopup.patch
#Patch107: 0079-compositing-types.patch
#Patch108: 0080-net-wm-sync-request-2.patch
Patch110: 0084-compositing-properties.patch

# upstream patches
Patch200: qt-x11-free-3.3.4-fullscreen.patch
#Patch201: qt-x11-free-3.3.8b-gcc43.patch

# TDE 3.5.13 patches
Patch300: qt3-3.3.8.d-updates_zh-tw_translations.patch

## [qt3] Fix Qt3 builds with libpng15. [Bug #683]
Patch301: 1326063972:e278b858739babff5cc19ca81a661e1256d162e7.diff

%define qt_dirname qt-3.3
%define qtdir %{_libdir}/%{qt_dirname}
%define qt_docdir %{_docdir}/qt-devel-%{version}

%define smp 1
%define immodule 1
%define debug 0

# MySQL plugins
%define plugin_mysql -plugin-sql-mysql
%define mysql_include_dir %{_includedir}/mysql
%define mysql_lib_dir %{_libdir}/mysql

# Postgres plugins
%define plugin_psql -plugin-sql-psql

# ODBC plugins
%define plugin_odbc -plugin-sql-odbc

# sqlite plugins
%define plugin_sqlite -plugin-sql-sqlite

%define plugins_style -qt-style-cde -qt-style-motifplus -qt-style-platinum -qt-style-sgi -qt-style-windows -qt-style-compact -qt-imgfmt-png -qt-imgfmt-jpeg -qt-imgfmt-mng
%define plugins %{plugin_mysql} %{plugin_psql} %{plugin_odbc} %{plugin_sqlite} %{plugins_style}

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: coreutils
Requires: fontconfig >= 2.0
Requires: /etc/ld.so.conf.d

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
BuildRequires: cups-devel
BuildRequires: tar
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libXrender-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXinerama-devel
BuildRequires: libXft-devel
BuildRequires: libXext-devel
BuildRequires: libX11-devel
BuildRequires: libSM-devel
BuildRequires: libICE-devel
BuildRequires: libXt-devel
BuildRequires: libXmu-devel
BuildRequires: libXi-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: desktop-file-utils
BuildRequires: mysql-devel
BuildRequires: postgresql-devel
BuildRequires: unixODBC-devel
BuildRequires: sqlite-devel
BuildRequires: gcc-c++
BuildRequires: make


%package config
Summary: Graphical configuration tool for programs using Qt 3
Group: User Interface/Desktops
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-config < %{version}-%{release}
Provides:  %{name}-config = %{version}-%{release}


%package devel
Summary: Development files for the Qt 3 GUI toolkit
Group: Development/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: freetype-devel
Requires: fontconfig-devel
Requires: libXrender-devel
Requires: libXrandr-devel
Requires: libXcursor-devel
Requires: libXinerama-devel
Requires: libXft-devel
Requires: libXext-devel
Requires: libX11-devel
Requires: libSM-devel
Requires: libICE-devel
Requires: libXt-devel
Requires: xorg-x11-proto-devel
Requires: libpng-devel
Requires: libjpeg-devel
Requires: libmng-devel
Requires: mesa-libGL-devel
Requires: mesa-libGLU-devel

Obsoletes: %{name}-devel < %{version}-%{release}
Provides:  %{name}-devel = %{version}-%{release}


%package devel-docs
Summary: Documentation for the Qt 3 GUI toolkit
Group: Development/Libraries
Requires: %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes: %{name}-devel-docs < %{version}-%{release}
Provides:  %{name}-devel-docs = %{version}-%{release}


%package ODBC
Summary: ODBC drivers for Qt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes: %{name}-ODBC < %{version}-%{release}
Provides:  %{name}-ODBC = %{version}-%{release}


%package MySQL
Summary: MySQL drivers for Qt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes: %{name}-MySQL < %{version}-%{release}
Provides:  %{name}-MySQL = %{version}-%{release}


%package PostgreSQL
Summary: PostgreSQL drivers for Qt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes: %{name}-PostgreSQL < %{version}-%{release}
Provides:  %{name}-PostgreSQL = %{version}-%{release}


%package sqlite
Summary: sqlite drivers for Qt 3's SQL classes
Group: System Environment/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes: %{name}-sqlite < %{version}-%{release}
Provides:  %{name}-sqlite = %{version}-%{release}


%package designer
Summary: Interface designer (IDE) for the Qt 3 toolkit
Group: Development/Tools
Requires: %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes: %{name}-designer < %{version}-%{release}
Provides:  %{name}-designer = %{version}-%{release}


%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications
for the X Window System.

Qt is written in C++ and is fully object-oriented.

This package contains the shared library needed to run Qt 3
applications, as well as the README files for Qt 3.


%description config
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications
for the X Window System.

Qt is written in C++ and is fully object-oriented.

This package contains a graphical configuration tool for programs using Qt 3.


%description devel
The %{name}-devel package contains the files necessary to develop
applications using the Qt GUI toolkit: the header files, the Qt meta
object compiler.

Install %{name}-devel if you want to develop GUI applications using the Qt 3
toolkit.


%description devel-docs
The %{name}-devel-docs package contains the man pages, the HTML documentation and
example programs for Qt 3.


%description ODBC
ODBC driver for Qt 3's SQL classes (QSQL)


%description MySQL
MySQL driver for Qt 3's SQL classes (QSQL)


%description PostgreSQL
PostgreSQL driver for Qt 3's SQL classes (QSQL)


%description sqlite
sqlite driver for Qt 3's SQL classes (QSQL)


%description designer
The %{name}-designer package contains an User Interface designer tool
for the Qt 3 toolkit.


%prep
%setup -q -n qt3
%patch1 -p1 -b .cjk
%patch2 -p1 -b .ndebug
%patch3 -p1 -b .makefile
%patch4 -p1 -b .umask
%patch5 -p1
%patch7 -p1 -b .quiet
#patch8 -p1 -b .qembed
%patch12 -p1 -b .nostdlib
%patch13 -p1 -b .fonts
#patch14 -p1 -b .gl
#patch19 -p1 -b .gtk
#patch20 -p1 -b .gcc4-buildkey
#patch24 -p1 -b .uic
%patch25 -p1 -b .uic-multilib
%patch27 -p1 -b .fontrendering-ml_IN-bz#209097
%patch29 -p1 -b .fontrendering-as_IN-bz#209972
%patch31 -p1 -b .fontrendering-te_IN-bz#211259
%patch32 -p1 -b .fontrendering-bz#214371
%patch33 -p1 -b .fontrendering-#214570
%patch34 -p1 -b .fontrendering-#209974
%patch35 -p1 -b .fontrendering-ml_IN-217657
%patch37 -p1 -b .fontrendering-gu-228452
%patch38 -p1 -b .odbc
# it's not 100% clear to me if this is safe for all archs -- Rex
%ifarch armv5tel
%patch39 -p1 -b .arm
%endif
%patch40 -p1

# immodule patches
%if %{immodule}
#patch50 -p1
#patch51 -p1 -b .quiet
#patch52 -p1 -b .fix-key-release-event-with-imm
%patch53 -p1 -b .resetinputcontext
%endif

# qt-copy patches
#patch100 -p0 -b .0038-dragobject-dont-prefer-unknown
#patch101 -p0 -b .0047-fix-kmenu-width
#patch102 -p0 -b .0048-qclipboard_hack_80072
#patch103 -p0 -b .0056-khotkeys_input_84434
#patch105 -p0 -b .0073-xinerama-aware-qpopup
#patch107 -p0 -b .0079-compositing-types
#patch108 -p0 -b .0080-net-wm-sync-request
%patch110 -p0 -b .0084-compositing-properties

# upstream patches
%patch200 -p1 -b .fullscreen
#patch201 -p1 -b .gcc34

# TDE 3.5.13 patches
%patch300 -p1
%patch301 -p1

# convert to UTF-8
iconv -f iso-8859-1 -t utf-8 < doc/man/man3/qdial.3qt > doc/man/man3/qdial.3qt_
mv doc/man/man3/qdial.3qt_ doc/man/man3/qdial.3qt

%build
export QTDIR=`/bin/pwd`
export LD_LIBRARY_PATH="$QTDIR/lib:$LD_LIBRARY_PATH"
export PATH="$QTDIR/bin:$PATH"
export QTDEST=%{qtdir}

%if %{smp}
   export SMP_MFLAGS="%{?_smp_mflags}"
%endif

%if %{immodule}
   sh ./make-symlinks.sh
%endif

# set correct X11 prefix
perl -pi -e "s,QMAKE_LIBDIR_X11.*,QMAKE_LIBDIR_X11\t=," mkspecs/*/qmake.conf
perl -pi -e "s,QMAKE_INCDIR_X11.*,QMAKE_INCDIR_X11\t=," mkspecs/*/qmake.conf
perl -pi -e "s,QMAKE_INCDIR_OPENGL.*,QMAKE_INCDIR_OPENGL\t=," mkspecs/*/qmake.conf
perl -pi -e "s,QMAKE_LIBDIR_OPENGL.*,QMAKE_LIBDIR_OPENGL\t=," mkspecs/*/qmake.conf

# don't use rpath
perl -pi -e "s|-Wl,-rpath,| |" mkspecs/*/qmake.conf

perl -pi -e "s|-O2|$INCLUDES %{optflags} -fno-strict-aliasing|g" mkspecs/*/qmake.conf

# set correct lib path
if [ "%{_lib}" == "lib64" ] ; then
  perl -pi -e "s,/usr/lib /lib,/usr/%{_lib} /%{_lib},g" config.tests/{unix,x11}/*.test
  perl -pi -e "s,/lib /usr/lib,/%{_lib} /usr/%{_lib},g" config.tests/{unix,x11}/*.test
fi

# build shared, threaded (default) libraries
echo yes | ./configure \
  -prefix $QTDEST \
  -docdir %{qt_docdir} \
%if %{_lib} == lib64
  -platform linux-g++-64 \
%else
  -platform linux-g++ \
%endif
%if %{debug}
  -debug \
%else
  -release \
%endif
  -shared \
  -largefile \
  -qt-gif \
  -system-zlib \
  -system-libpng \
  -system-libmng \
  -system-libjpeg \
  -no-exceptions \
  -enable-styles \
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
  -enable-opengl \
  -enable-sql \
  -qt-style-motif \
  %{plugins} \
  -stl \
  -thread \
  -cups \
  -sm \
  -xinerama \
  -xrender \
  -xkb \
  -ipv6 \
  -dlopen-opengl \
  -xft \
  -tablet

make $SMP_MFLAGS src-qmake

# build sqlite plugin
pushd plugins/src/sqldrivers/sqlite
qmake -o Makefile sqlite.pro
popd

# build psql plugin
pushd plugins/src/sqldrivers/psql
qmake -o Makefile "INCLUDEPATH+=%{_includedir}/pgsql %{_includedir}/pgsql/server %{_includedir}/pgsql/internal" "LIBS+=-lpq" psql.pro
popd

# build mysql plugin
pushd plugins/src/sqldrivers/mysql
qmake -o Makefile "INCLUDEPATH+=%{mysql_include_dir}" "LIBS+=-L%{mysql_lib_dir} -lmysqlclient" mysql.pro
popd

# build odbc plugin
pushd plugins/src/sqldrivers/odbc
qmake -o Makefile "LIBS+=-lodbc" odbc.pro
popd

make $SMP_MFLAGS src-moc
make $SMP_MFLAGS sub-src
make $SMP_MFLAGS sub-tools UIC="$QTDIR/bin/uic -nostdlib -L $QTDIR/plugins"

%install
rm -rf %{buildroot}

export QTDIR=`/bin/pwd`
export LD_LIBRARY_PATH="$QTDIR/lib:$LD_LIBRARY_PATH"
export PATH="$QTDIR/bin:$PATH"
export QTDEST=%{qtdir}

make install INSTALL_ROOT=%{buildroot}

for i in findtr qt20fix qtrename140 lrelease lupdate ; do
   install bin/$i %{buildroot}%{qtdir}/bin/
done

mkdir -p %{buildroot}%{_libdir}/pkgconfig/
mv %{buildroot}%{qtdir}/lib/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

# install man pages
mkdir -p %{buildroot}%{_mandir}
cp -fR doc/man/* %{buildroot}%{_mandir}/

# clean up
make -C tutorial clean
make -C examples clean

# Make sure the examples can be built outside the source tree.
# Our binaries fulfill all requirements, so...
perl -pi -e "s,^DEPENDPATH.*,,g;s,^REQUIRES.*,,g" `find examples -name "*.pro"`

# don't include Makefiles of qt examples/tutorials
find examples -name "Makefile" | xargs rm -f
find examples -name "*.obj" | xargs rm -rf
find examples -name "*.moc" | xargs rm -rf
find tutorial -name "Makefile" | xargs rm -f

for a in */*/Makefile ; do
  sed 's|^SYSCONF_MOC.*|SYSCONF_MOC		= %{qtdir}/bin/moc|' < $a > ${a}.2
  mv -v ${a}.2 $a
done

mkdir -p %{buildroot}/etc/profile.d
install -m 644 %{SOURCE2} %{SOURCE3} %{buildroot}/etc/profile.d/

# Add desktop files
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --vendor="qt" \
  %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7}

# Patch qmake to use qt-mt unconditionally
perl -pi -e "s,-lqt ,-lqt-mt ,g;s,-lqt$,-lqt-mt,g" %{buildroot}%{qtdir}/mkspecs/*/qmake.conf

# remove broken links
rm -f %{buildroot}%{qtdir}/mkspecs/default/linux-g++*
rm -f %{buildroot}%{qtdir}/lib/*.la

mkdir -p %{buildroot}/etc/ld.so.conf.d
echo "%{qtdir}/lib" > %{buildroot}/etc/ld.so.conf.d/qt-%{_arch}.conf

# install icons
mkdir %{buildroot}%{_datadir}/pixmaps
install -m 644 tools/assistant/images/qt.png %{buildroot}%{_datadir}/pixmaps/qtconfig3.png
install -m 644 tools/assistant/images/designer.png %{buildroot}%{_datadir}/pixmaps/designer3.png
install -m 644 tools/assistant/images/assistant.png %{buildroot}%{_datadir}/pixmaps/assistant3.png
install -m 644 tools/assistant/images/linguist.png %{buildroot}%{_datadir}/pixmaps/linguist3.png

# own style directory
mkdir -p %{buildroot}%{qtdir}/plugins/styles

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc FAQ LICENSE* README* changes*
%dir %{qtdir}
%dir %{qtdir}/bin
%dir %{qtdir}/lib
%dir %{qtdir}/plugins
%dir %{qtdir}/plugins/sqldrivers
%dir %{qtdir}/plugins/styles
%{qtdir}/translations
%{qtdir}/plugins/designer/
%if %{immodule}
%{qtdir}/plugins/inputmethods
%endif
%config /etc/profile.d/*
/etc/ld.so.conf.d/*
%{qtdir}/lib/libqui.so.*
%{qtdir}/lib/libqt*.so.*

%files config
%defattr(-,root,root,-)
%{qtdir}/bin/qtconfig
%{_datadir}/applications/*qtconfig*.desktop
%{_datadir}/pixmaps/qtconfig3.png

%files devel
%defattr(-,root,root,-)
%{qt_docdir}/
%{qtdir}/bin/moc
%{qtdir}/bin/uic
%{qtdir}/bin/findtr
%{qtdir}/bin/qt20fix
%{qtdir}/bin/qtrename140
%{qtdir}/bin/assistant
%{qtdir}/bin/qm2ts
%{qtdir}/bin/qmake
%{qtdir}/bin/qembed
%{qtdir}/bin/linguist
%{qtdir}/bin/lupdate
%{qtdir}/bin/lrelease
%{qtdir}/include
%{qtdir}/mkspecs
%{qtdir}/lib/libqt*.so
%{qtdir}/lib/libqui.so
%{qtdir}/lib/libeditor.a
%{qtdir}/lib/libdesigner*.a
%{qtdir}/lib/libqassistantclient.a
%{qtdir}/lib/*.prl
%{qtdir}/phrasebooks
%{_libdir}/pkgconfig/*
%{_datadir}/applications/*linguist*.desktop
%{_datadir}/applications/*assistant*.desktop
%{_datadir}/pixmaps/linguist3.png
%{_datadir}/pixmaps/assistant3.png

# QT 3.3.8.D (TDE): 4 binaries have appeared
%{qtdir}/bin/createcw
%{qtdir}/bin/makeqpf
%{qtdir}/bin/mergetr
%{qtdir}/bin/msg2qm

# QT 3.3.8.D (TDE): removes lots of unnecessary include files
# (where do they come from ??? They were not in 3.3.8b !)
%exclude %{qtdir}/include/btree.h
#%exclude %{qtdir}/include/config.h
%exclude %{qtdir}/include/crc32.h
%exclude %{qtdir}/include/debian_qsql_odbc.h
%exclude %{qtdir}/include/deflate.h
%exclude %{qtdir}/include/ftglue.h
%exclude %{qtdir}/include/ftxgdef.h
%exclude %{qtdir}/include/ftxgpos.h
%exclude %{qtdir}/include/ftxgsub.h
%exclude %{qtdir}/include/ftxopen.h
%exclude %{qtdir}/include/ftxopenf.h
%exclude %{qtdir}/include/hash.h
%exclude %{qtdir}/include/inffast.h
%exclude %{qtdir}/include/inffixed.h
%exclude %{qtdir}/include/inflate.h
%exclude %{qtdir}/include/inftrees.h
%exclude %{qtdir}/include/jchuff.h
%exclude %{qtdir}/include/jconfig.h
%exclude %{qtdir}/include/jdct.h
%exclude %{qtdir}/include/jdhuff.h
%exclude %{qtdir}/include/jerror.h
%exclude %{qtdir}/include/jinclude.h
%exclude %{qtdir}/include/jmemsys.h
%exclude %{qtdir}/include/jmorecfg.h
#%exclude %{qtdir}/include/jpegint.h
#%exclude %{qtdir}/include/jpeglib.h
%exclude %{qtdir}/include/jversion.h
#%exclude %{qtdir}/include/libmng.h
#%exclude %{qtdir}/include/libmng_chunk_io.h
#%exclude %{qtdir}/include/libmng_chunk_prc.h
#%exclude %{qtdir}/include/libmng_chunks.h
#%exclude %{qtdir}/include/libmng_cms.h
#%exclude %{qtdir}/include/libmng_conf.h
#%exclude %{qtdir}/include/libmng_data.h
#%exclude %{qtdir}/include/libmng_display.h
#%exclude %{qtdir}/include/libmng_dither.h
#%exclude %{qtdir}/include/libmng_error.h
#%exclude %{qtdir}/include/libmng_filter.h
#%exclude %{qtdir}/include/libmng_jpeg.h
#%exclude %{qtdir}/include/libmng_memory.h
#%exclude %{qtdir}/include/libmng_object_prc.h
#%exclude %{qtdir}/include/libmng_objects.h
#%exclude %{qtdir}/include/libmng_pixels.h
#%exclude %{qtdir}/include/libmng_read.h
#%exclude %{qtdir}/include/libmng_trace.h
#%exclude %{qtdir}/include/libmng_types.h
#%exclude %{qtdir}/include/libmng_write.h
#%exclude %{qtdir}/include/libmng_zlib.h
%exclude %{qtdir}/include/moc_yacc.h
%exclude %{qtdir}/include/opcodes.h
%exclude %{qtdir}/include/os.h
%exclude %{qtdir}/include/otlbuffer.h
%exclude %{qtdir}/include/pager.h
%exclude %{qtdir}/include/parse.h
#%exclude %{qtdir}/include/png.h
%exclude %{qtdir}/include/pngasmrd.h
%exclude %{qtdir}/include/pngconf.h
%exclude %{qtdir}/include/sqlite.h
%exclude %{qtdir}/include/sqliteInt.h
%exclude %{qtdir}/include/trees.h
%exclude %{qtdir}/include/vdbe.h
%exclude %{qtdir}/include/vdbeInt.h
#%exclude %{qtdir}/include/zconf.h
#%exclude %{qtdir}/include/zconf.in.h
#%exclude %{qtdir}/include/zlib.h
#%exclude %{qtdir}/include/zutil.h
%exclude %{qtdir}/mkspecs/linux-g++-sparc



%files devel-docs
%defattr(-,root,root,-)
%doc examples
%doc tutorial
%{_mandir}/*/*

%files sqlite
%defattr(-,root,root,-)
%{qtdir}/plugins/sqldrivers/libqsqlite.so

%files ODBC
%defattr(-,root,root,-)
%{qtdir}/plugins/sqldrivers/libqsqlodbc.so

%files PostgreSQL
%defattr(-,root,root,-)
%{qtdir}/plugins/sqldrivers/libqsqlpsql.so

%files MySQL
%defattr(-,root,root,-)
%{qtdir}/plugins/sqldrivers/libqsqlmysql.so

%files designer
%defattr(-,root,root,-)
%{qtdir}/templates
%{qtdir}/bin/designer
%{_datadir}/applications/*designer*.desktop
%{_datadir}/pixmaps/designer3.png


%changelog
* Tue Apr 24 2012 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-6
- Fix Qt3 builds with libpng15. [Bug #683]

* Sat Apr 21 2012 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-5
- Fix 'Provides' AGAIN !! [Bug #823]

* Mon Apr 02 2012 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-4
- Fix 'Provides' [Bug #823]

* Sun Dec 18 2011 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-3
- Updates zh_TW translations, thanks to Wei-Lun Chao .

* Thu Nov 03 2011 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-2
- Add missing BuildRequires

* Fri Sep 02 2011 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-1
- Initial build for RHEL 6, RHEL 5, and Fedora 15
- Switch to Trinity Version
- Spec file based on RHEL 6 'qt3-3.3.8b-29'
