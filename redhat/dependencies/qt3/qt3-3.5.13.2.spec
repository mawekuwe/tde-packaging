# Always install under standard prefix
%define _prefix /usr

# The following QT4 packages should NOT be installed to
# allow QT3 compilation (please uninstall them prior to compile)
#  qt
#  qt-sqlite
#  qt-mysql
#  qt-x11
#  qt-devel
# ...maybe others !!!!

%if 0%{?rhel} <= 5 && 0%{?fedora} <= 7
Name:			qt
%else
Name:			qt3
%endif

Epoch:			1
Version:		3.3.8.d%{?preversion:_%{preversion}}
Release:		10%{?dist}
Summary:		The shared library for the Qt 3 GUI toolkit

License:		QPL or GPLv2 or GPLv3
Group:			System Environment/Libraries
URL:			http://www.trinitydesktop.org/

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides:		qt3 = %{?epoch:%{epoch}:}%{version}-%{release}

Source0: trinity-qt3-3.5.13.2%{?preversion:~%{preversion}}.tar.gz
Source2: qt.sh
Source3: qt.csh
Source4: designer3.desktop
Source5: assistant3.desktop
Source6: linguist3.desktop
Source7: qtconfig3.desktop

# Monolithic patch for QT3 for TDE 3.5.13.2
Patch1: qt3-3.5.13.2.patch

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
BuildRequires: perl
BuildRequires: sed
BuildRequires: findutils
BuildRequires: cups-devel
BuildRequires: tar
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: desktop-file-utils
BuildRequires: mysql-devel
BuildRequires: postgresql-devel
BuildRequires: unixODBC-devel
BuildRequires: sqlite-devel
BuildRequires: gcc-c++
BuildRequires: make

%if 0%{?rhel} == 4
BuildRequires: libungif-devel
BuildRequires: xorg-x11-devel
%else
BuildRequires: giflib-devel
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
%endif

%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications
for the X Window System.

Qt is written in C++ and is fully object-oriented.

This package contains the shared library needed to run Qt 3
applications, as well as the README files for Qt 3.

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

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

##########

%package config
Summary: Graphical configuration tool for programs using Qt 3
Group: User Interface/Desktops
Requires:	qt3 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	qt3-config = %{?epoch:%{epoch}:}%{version}-%{release}

%description config
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications
for the X Window System.

Qt is written in C++ and is fully object-oriented.

This package contains a graphical configuration tool for programs using Qt 3.

%files config
%defattr(-,root,root,-)
%{qtdir}/bin/qtconfig
%{_datadir}/applications/*qtconfig*.desktop
%{_datadir}/pixmaps/qtconfig3.png

##########

%package devel
Summary: Development files for the Qt 3 GUI toolkit
Group: Development/Libraries
Requires:	qt3 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	qt3-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: freetype-devel
Requires: fontconfig-devel
Requires: libpng-devel
Requires: libjpeg-devel
Requires: libmng-devel
%if 0%{?rhel} == 4
BuildRequires: xorg-x11-devel
%else
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
Requires: mesa-libGL-devel
Requires: mesa-libGLU-devel
%endif

%description devel
The %{name}-devel package contains the files necessary to develop
applications using the Qt GUI toolkit: the header files, the Qt meta
object compiler.

Install %{name}-devel if you want to develop GUI applications using the Qt 3
toolkit.

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

##########

%package devel-docs
Summary: Documentation for the Qt 3 GUI toolkit
Group: Development/Libraries
Requires: %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?rhel} <= 5 && 0%{?fedora} <= 7
Obsoletes: qt-devel-docs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:  qt-devel-docs = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description devel-docs
The %{name}-devel-docs package contains the man pages, the HTML documentation and
example programs for Qt 3.

%files devel-docs
%defattr(-,root,root,-)
%doc examples
%doc tutorial
%{_mandir}/*/*

##########

%package ODBC
Summary: ODBC drivers for Qt 3's SQL classes
Group: System Environment/Libraries
Requires:	qt3 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	qt3-ODBC = %{?epoch:%{epoch}:}%{version}-%{release}

%description ODBC
ODBC driver for Qt 3's SQL classes (QSQL)

%files ODBC
%defattr(-,root,root,-)
%{qtdir}/plugins/sqldrivers/libqsqlodbc.so

##########

%package MySQL
Summary: MySQL drivers for Qt 3's SQL classes
Group: System Environment/Libraries
Requires:	qt3 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	qt3-MySQL = %{?epoch:%{epoch}:}%{version}-%{release}

%description MySQL
MySQL driver for Qt 3's SQL classes (QSQL)

%files MySQL
%defattr(-,root,root,-)
%{qtdir}/plugins/sqldrivers/libqsqlmysql.so

##########

%package PostgreSQL
Summary: PostgreSQL drivers for Qt 3's SQL classes
Group: System Environment/Libraries
Requires:	qt3 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	qt3-PostgreSQL = %{?epoch:%{epoch}:}%{version}-%{release}

%description PostgreSQL
PostgreSQL driver for Qt 3's SQL classes (QSQL)

%files PostgreSQL
%defattr(-,root,root,-)
%{qtdir}/plugins/sqldrivers/libqsqlpsql.so

##########

%package sqlite
Summary: sqlite drivers for Qt 3's SQL classes
Group: System Environment/Libraries
Requires:	qt3 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	qt3-sqlite = %{?epoch:%{epoch}:}%{version}-%{release}

%description sqlite
sqlite driver for Qt 3's SQL classes (QSQL)

%files sqlite
%defattr(-,root,root,-)
%{qtdir}/plugins/sqldrivers/libqsqlite.so

##########

%package designer
Summary: Interface designer (IDE) for the Qt 3 toolkit
Group: Development/Tools
Requires:	qt3 = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	qt3-designer = %{?epoch:%{epoch}:}%{version}-%{release}

%description designer
The %{name}-designer package contains an User Interface designer tool
for the Qt 3 toolkit.

%files designer
%defattr(-,root,root,-)
%{qtdir}/templates
%{qtdir}/bin/designer
%{_datadir}/applications/*designer*.desktop
%{_datadir}/pixmaps/designer3.png

##########

%prep
%setup -q -n trinity-qt3-3.5.13.2%{?preversion:~%{preversion}}

%patch1 -p1


# convert to UTF-8
iconv -f iso-8859-1 -t utf-8 < doc/man/man3/qdial.3qt > doc/man/man3/qdial.3qt_
mv doc/man/man3/qdial.3qt_ doc/man/man3/qdial.3qt

%build
export QTDIR=`/bin/pwd`
export LD_LIBRARY_PATH="$QTDIR/lib:$LD_LIBRARY_PATH"
export PATH="$QTDIR/bin:$PATH"
export QTDEST=%{qtdir}

# Huho ... it looks like we are not detecting some libraries correctly under RHEL4 ...
%if 0%{?rhel} == 4
%__sed -i plugins/src/inputmethods/xim/xim.pro \
  -e "/INCLUDEPATH/ s|$| /usr/include/freetype2|"
%endif

%if %{smp}
   export SMP_MFLAGS="%{?_smp_mflags}"
%endif

%if %{immodule}
   sh ./make-symlinks.sh
%endif

# set correct X11 prefix
if [ -d /usr/X11R6 ]; then
  perl -pi -e "s,QMAKE_LIBDIR_X11.*,QMAKE_LIBDIR_X11\t=/usr/X11R6/%{_lib}," mkspecs/*/qmake.conf
  perl -pi -e "s,QMAKE_INCDIR_X11.*,QMAKE_INCDIR_X11\t=/usr/X11R6/include," mkspecs/*/qmake.conf
else
  perl -pi -e "s,QMAKE_LIBDIR_X11.*,QMAKE_LIBDIR_X11\t=," mkspecs/*/qmake.conf
  perl -pi -e "s,QMAKE_INCDIR_X11.*,QMAKE_INCDIR_X11\t=," mkspecs/*/qmake.conf
fi
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

# Fix QTLIB is under 'lib' instead of 'lib64' under RHEL/Fedora
sed -i "mkspecs/linux-g++-64/qmake.conf" -e "s|\$(QTDIR)/lib64|\$(QTDIR)/lib|"

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
%if 0%{?rhel} == 4
  -no-xinerama \
  -no-xrandr \
%else
  -xinerama \
  -xrandr \
%endif
  -xrender \
  -xkb \
  -ipv6 \
  -dlopen-opengl \
  -xft \
  -tablet -v

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

install -D -m 644 "%{SOURCE2}" %{buildroot}/etc/profile.d/qt3.sh
install -D -m 644 "%{SOURCE3}" %{buildroot}/etc/profile.d/qt3.csh

# Add desktop files
mkdir -p "%{buildroot}%{_datadir}/applications"
desktop-file-install \
  --dir "%{buildroot}%{_datadir}/applications" \
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
install -D -m 644 "tools/assistant/images/qt.png"         "%{buildroot}%{_datadir}/pixmaps/qtconfig3.png"
install -D -m 644 "tools/assistant/images/designer.png"   "%{buildroot}%{_datadir}/pixmaps/designer3.png"
install -D -m 644 "tools/assistant/images/assistant.png"  "%{buildroot}%{_datadir}/pixmaps/assistant3.png"
install -D -m 644 "tools/assistant/images/linguist.png"   "%{buildroot}%{_datadir}/pixmaps/linguist3.png"

# own style directory
mkdir -p "%{buildroot}%{qtdir}/plugins/styles"


%clean
rm -rf %{buildroot}


%changelog
* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-10
- Initial release for TDE 3.5.13.2

* Sat Sep 29 2012 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-9
- Initial release for TDE 3.5.13.1

* Sat Apr 28 2012 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-8
- Fix Provides and Obsoletes, again and again ...

* Sat Apr 28 2012 Francois Andriot <francois.andriot@free.fr> - 3.3.8.d-7
- Fix Provides and Obsoletes. Now only for RHEL 5.

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
- Initial release for RHEL 6, RHEL 5, and Fedora 15
- Switch to Trinity Version
- Spec file based on RHEL 6 'qt3-3.3.8b-29'
