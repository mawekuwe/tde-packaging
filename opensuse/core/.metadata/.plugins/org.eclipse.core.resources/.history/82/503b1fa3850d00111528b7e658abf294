#
# spec file for package qt3-extensions
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           qt3-extensions
BuildRequires:  cups-devel krb5-devel mysql-devel postgresql-devel qt3-devel sqlite2-devel unixODBC-devel update-desktop-files
%if %suse_version > 1020
BuildRequires:  fdupes
%endif
License:        GPL, QPL
Version:        3.3.8c
Release:        1
AutoReqProv:    on
Requires:       qt3 = %version
Group:          Development/Tools/Other
Summary:        Qt3 Extensions
# COMMON-BEGIN
# COMMON-BEGIN
%define x11_free -x11-free-
%define rversion 3.3.8b
Source0:        qt%{x11_free}%rversion.tar.bz2
Source1:        build_script.sh
Source2:        qtconfig3.desktop
Source3:        qtrc
Source4:        assistant3.png
Source6:        assistant3.desktop
Source7:        designer.desktop
Source8:        designer.png
Source9:        linguist.desktop
Source5:        linguist.png
Source10:       qt3.sh
Source11:       qt3.csh
# Translations did not change at 3.3.8c
Source12:       qt3-3.3.8b-translations.tar.bz2
Source100:      qtkdeintegration_x11.cpp
Source101:      qtkdeintegration_x11_p.h
Source102:      baselibs.conf
Source200:      attributes
Source201:      update_spec.pl
Patch1:         aliasing.diff
Patch2:         head.diff
Patch4:         qt3-never-strip.diff
Patch5:         external-libs.diff
Patch6:         0001-dnd_optimization.patch
Patch7:         0002-dnd_active_window_fix.patch
Patch8:         0007-qpixmap_constants.patch
Patch11:        0038-dragobject-dont-prefer-unknown.patch
Patch12:        qtrc-path.diff
Patch14:        lib64-plugin-support.diff
Patch15:        pluginmanager-fix.diff
Patch18:        no-rpath.dif
Patch19:        shut-up.diff
Patch20:        rubberband.diff
Patch21:        fix-GL-loading.diff
Patch23:        fix-accessible.diff
# From http://www.freedesktop.org/wiki/Software_2fImmoduleQtDownload
# Current version from http://freedesktop.org/~daisuke/qt-x11-immodule-unified-qt3.3.5-20060318.diff.bz2
Patch25:        qt-x11-immodule-unified-qt3.3.8-20060318.diff
Patch28:        fix-key-release-event-with-imm.diff
Patch29:        0047-fix-kmenu-width.diff
Patch31:        limit-image-size.diff
Patch34:        0005-qpixmap_mitshm.patch
Patch35:        qt-transparency.patch
Patch37:        0055-qtextedit_zoom.patch
Patch38:        0048-qclipboard_hack_80072.patch
Patch39:        fix-qtranslator-crash.diff
Patch40:        0059-qpopup_has_mouse.patch
Patch41:        0060-qpopup_ignore_mousepos.patch
Patch42:        add_qexport_visibility.patch
Patch43:        0056-khotkeys_input_84434.patch
Source250:      enable-designer-plugins.diff
Patch53:        fix-xinerama-dialog-placement.diff
Patch54:        kmenu-search-fix.diff
Patch55:        qt3-fix-cast.diff
Patch100:       qt.patch
Patch101:       qt3-arm-gcc4.patch
Patch102:       xinerama.patch
Patch113:       fix-assistant-path.patch
Patch117:       qtimer-debug.diff
Patch119:       xinerama-qpopupmenu.diff
Patch121:       qt3-warnings.diff
Patch123:       use-xrandr-1.2.diff
Patch125:       qcstring-format-warnings.diff
Patch127:       mng-reading-fix.patch
Patch128:       0079-compositing-types.patch
Patch129:       0080-net-wm-sync-request.patch
Patch132:       revert-qt-3.3.8-khmer-fix.diff
Patch133:       0085-fix-buildkey.diff
Patch134:       fix-xinput-clash.diff
Patch135:       parseFontName.diff
Patch136:       qt3-no-date.diff
Patch137:       popen-leak-fix.diff
Patch138:       qt3-libpng14.diff
Patch139:       gcc46.diff

# TQt integration
Patch200:       qt-3.3.8c.diff

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains extension libraries for Qt 3, such as the
Netscape plug-in modules.

This package contains extension libraries for Qt 3, such as the
Netscape plug-in modules.

This package contains extension libraries for Qt 3, such as the
Netscape plug-in modules.

This package contains extension libraries for Qt 3, such as the
Netscape plug-in modules.

%define build_sub_dirs src plugins/src tools/designer/uilib/ tools/designer/uic tools/qtconfig tools/assistant/lib tools/assistant tutorial

%prep
%setup -q -n qt%{x11_free}%rversion
%patch1
%patch2
%patch4
%patch5
%patch6
%patch7
%patch8
%patch11
%patch12
if [ "%_lib" = "lib64" ]; then
%patch14
fi
%patch15
%patch18
%patch19
%patch20
%patch23
%patch25
%patch28
%patch29
%patch31
%patch34
%patch35
%patch37
%patch38
%patch39
%patch40
%patch41
%patch42
%patch43
%patch100
%patch102
%patch53
%patch54
%patch55
%patch101
%patch113
%patch117
%patch119
%patch121
%patch123
ln -sf $PWD/src/inputmethod/qinputcontextfactory.h include/
ln -sf $PWD/src/inputmethod/qinputcontextplugin.h  include/
ln -sf $PWD/src/kernel/qinputcontext.h       include/
ln -sf $PWD/src/kernel/qinputcontextinterface_p.h include/private/
ln -sf $PWD/src/kernel/qximinputcontext_p.h       include/private/
if [ %_lib = "lib" ]; then
sed 's,/lib64/,/lib/,' %PATCH21 | patch -p0
else
%patch21
fi
%patch125
%patch127
%patch128
%patch129
%patch132
%patch133
%patch134
%patch135
%patch136
%patch137
%if %suse_version > 1120
%patch138 -p1
%endif
%patch139
%patch200
# copy qt kde integration files
cp %SOURCE100 %SOURCE101 src/kernel/
cp %SOURCE101 include/private/
cd translations
tar xvjf %SOURCE12
cd ..
# COMMON-END
# COMMON-END

%description
This package contains extension libraries for Qt 3, such as the
Netscape plug-in modules.

This package contains extension libraries for Qt 3, such as the
Netscape plug-in modules.

This package contains extension libraries for Qt 3, such as the
Netscape plug-in modules.

This package contains extension libraries for Qt 3, such as the
Netscape plug-in modules.

%package -n qt3-devel-examples
Summary:        Programming Examples for Qt 3
AutoReqProv:    on
Group:          Development/Sources
Provides:       qt3-examples
Obsoletes:      qt3-examples

%description  -n qt3-devel-examples
This package contains small executables with code to demonstrate Qt
programming.

Have a look in /usr/share/doc/packages/qt3/examples/.

%package -n qt3-mysql
Summary:        MySQL Plug-In for Qt
Provides:       qt3_database_plugin
Group:          Productivity/Databases/Clients

%description  -n qt3-mysql
Plug-in for using the MySQL database with the generic Qt database
interface.

%package -n qt3-unixODBC
Summary:        A UnixODBC Plug-In for Qt
Provides:       qt3_database_plugin
Group:          Productivity/Databases/Clients

%description  -n qt3-unixODBC
A plug-in for using UnixODBC supported databases with the generic Qt
database interface.

%package -n qt3-postgresql
Summary:        A PostgreSQL Plug-In for Qt
Provides:       qt3_database_plugin
Group:          Productivity/Databases/Clients

%description  -n qt3-postgresql
A Plug-in for using the PostgreSQL database with the generic Qt
database interface.

%package -n qt3-sqlite
Summary:        SQLite Database Plug-In for Qt
Provides:       qt3_database_plugin
Group:          Development/Tools/Other

%description  -n qt3-sqlite
The Qt database supports SQLite with this plug-in. (No configured and
running daemon is required.)

%package  -n qt3-devel-tools
Summary:        User Interface Builder and other tools (designer, assistant, linguist)
AutoReqProv:    on
Requires:       qt3-devel = %version
Provides:       qt3-designer
Obsoletes:      qt3-designer
Group:          Development/Tools/GUI Builders

%description  -n qt3-devel-tools
The designer creates .ui files. The uic generates C++ code from these
files. The package also contains the Qt Assistant (Qt documentation
browser) and the Qt Linguist (for translations).

%package -n qt3-man
Summary:        Qt 3 Man Pages
AutoReqProv:    on
Requires:       qt3-devel = %version
Conflicts:      qtman qt-man
Group:          Documentation/Man

%description -n qt3-man
This package contains all the man pages for all the Qt 3 classes.

%build
export QTDIR=/usr/lib/qt3/
export WLIB=%_lib
export VERSION=%suse_version
source %{SOURCE1} %{version}
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
#
# compile threaded version to build all tools.
# the lib itself becomes packaged from qt3.spec
#
call_configure -thread -shared -L$PWD/%_lib $OPTIONS
ln -sf /usr/lib/qt3/%_lib/* lib/
ln -sf /usr/lib/qt3/bin/* bin/
cd plugins/src
make %{?jobs:-j%jobs}
make INSTALL_ROOT=$RPM_BUILD_ROOT install
cd -
#
# build examples
#
cd tools/assistant/lib
make %{?jobs:-j%jobs}
cd -
cd examples
make %{?jobs:-j%jobs}
cd -
#
# build extra tools
#
cd tools
make %{?jobs:-j%jobs}
make INSTALL_ROOT=$RPM_BUILD_ROOT install
for i in qvfb qembed qconfig msg2qm mergetr ; do
  cd "$i" && make %{?jobs:-j%jobs} && install -m 0755 $i ${RPM_BUILD_ROOT}/usr/lib/qt3/bin/ && cd -
done
cd ..
install -m 0755 bin/findtr bin/qt20fix bin/qtrename140 ${RPM_BUILD_ROOT}/usr/lib/qt3/bin/
if [ %_lib = lib64 ]; then
 for i in $RPM_BUILD_ROOT/usr/lib/qt3/plugins/*/*.so; do
   mv "$i" "${i%.so}.lib64.so"
 done
fi

%install
export WLIB=%_lib
export VERSION=%suse_version
source %{SOURCE1}
post_install $RPM_BUILD_ROOT/usr/lib/qt3/
#
# create default doc dir
#
install -d -m 0755 ${RPM_BUILD_ROOT}/%{_docdir}/qt3/
#
# create links in ld.so.conf path
#
install -d -m 0755 ${RPM_BUILD_ROOT}/%{_libdir}
#install -d -m 0755 ${RPM_BUILD_ROOT}/usr/bin/
#ln -sf ../lib/qt3/bin/designer     ${RPM_BUILD_ROOT}/usr/bin/designer
#ln -sf ../lib/qt3/bin/linguist     ${RPM_BUILD_ROOT}/usr/bin/linguist
%suse_update_desktop_file -i designer  Qt Development GUIDesigner
%suse_update_desktop_file -i linguist  Qt Development Translation
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps
perl -pi -e 's/Icon=designer/Icon=designer3/' ${RPM_BUILD_ROOT}/usr/share/applications/designer.desktop
perl -pi -e 's,Exec=designer,Exec=/usr/lib/qt3/bin/designer,' ${RPM_BUILD_ROOT}/usr/share/applications/designer.desktop
mv ${RPM_BUILD_ROOT}/usr/share/applications/designer.desktop ${RPM_BUILD_ROOT}/usr/share/applications/designer3.desktop
install -m 0644 tools/assistant/images/designer.png $RPM_BUILD_ROOT/usr/share/pixmaps/designer3.png
rm -f ${RPM_BUILD_ROOT}/usr/share/pixmaps/designer.png
perl -pi -e 's,Exec=linguist,Exec=/usr/lib/qt3/bin/linguist,' ${RPM_BUILD_ROOT}/usr/share/applications/linguist.desktop
perl -pi -e 's,Icon=linguist,Icon=linguist3,' ${RPM_BUILD_ROOT}/usr/share/applications/linguist.desktop
mv ${RPM_BUILD_ROOT}/usr/share/pixmaps/linguist.png ${RPM_BUILD_ROOT}/usr/share/pixmaps/linguist3.png

##### these files are not getting installed by "make install" ... bug ?
#
#
# install manpages
#
rm -rf $RPM_BUILD_ROOT/%{_mandir}
install -d  $RPM_BUILD_ROOT/%{_mandir}
cp -a doc/man/* $RPM_BUILD_ROOT/%{_mandir}/
#
# install examples
#
install -d  ${RPM_BUILD_ROOT}/usr/lib/qt3/doc/
find ./examples/ \
  -name \*.o -o -name .obj -o -name .moc -o -name Makefile \
  | xargs rm -rf
cp -a examples ${RPM_BUILD_ROOT}/usr/lib/qt3/doc/
ln -sf /usr/lib/qt3/doc/examples ${RPM_BUILD_ROOT}/%{_docdir}/qt3/
#
# to be sure we do not package files which are packaged in other qt3 packages
#
rpm -ql qt3 qt3-devel qt3-devel-doc \
 | while read i ; do 
   [ -d "$i" ] || rm -f $RPM_BUILD_ROOT/"$i"
done
#
# we do have them in qt3-devel-doc already
#
rm -f $RPM_BUILD_ROOT/usr/lib/qt3/bin/assistant
rm -f $RPM_BUILD_ROOT/usr/lib/qt3/%_lib/libqassistantclient.*
rm -f $RPM_BUILD_ROOT/usr/lib/qt3/translations/assistant_de.qm

for l in $RPM_BUILD_ROOT/usr/lib/qt3/%_lib/*.a; do
  strip --strip-unneeded $l
done

%if %suse_version > 1020
%fdupes -s $RPM_BUILD_ROOT
%endif

%pre
if test -L usr/lib/qt3; then
  rm usr/lib/qt3
fi

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
%run_ldconfig

%post -n qt3-devel-tools
%run_ldconfig

%files
%defattr(-,root,root)
/usr/lib/qt3/bin/qembed
/usr/lib/qt3/bin/qvfb

%files -n qt3-mysql
%defattr(-,root,root)
%dir /usr/lib/qt3/plugins/sqldrivers
/usr/lib/qt3/plugins/sqldrivers/libqsqlmysql*.so

%files -n qt3-postgresql
%defattr(-,root,root)
%dir /usr/lib/qt3/plugins/sqldrivers
/usr/lib/qt3/plugins/sqldrivers/libqsqlpsql*.so

%files -n qt3-unixODBC
%defattr(-,root,root)
%dir /usr/lib/qt3/plugins/sqldrivers
/usr/lib/qt3/plugins/sqldrivers/libqsqlodbc*.so

%files -n qt3-sqlite
%defattr(-,root,root)
%dir /usr/lib/qt3/plugins/sqldrivers
/usr/lib/qt3/plugins/sqldrivers/libqsqlite*.so

%files -n qt3-devel-tools
%defattr(-,root,root)
#/usr/bin/designer
#/usr/bin/linguist
/usr/lib/qt3/bin/qconfig
/usr/lib/qt3/bin/findtr
/usr/lib/qt3/bin/qt20fix
/usr/lib/qt3/bin/qtrename140
/usr/lib/qt3/bin/msg2qm
/usr/lib/qt3/bin/mergetr
/usr/lib/qt3/bin/designer
/usr/lib/qt3/bin/linguist
/usr/lib/qt3/bin/qm2ts
/usr/lib/qt3/bin/lrelease
/usr/lib/qt3/bin/lupdate
/usr/lib/qt3/templates
/usr/lib/qt3/plugins/designer
/usr/lib/qt3/phrasebooks
/usr/lib/qt3/%_lib/libdesignercore.*
/usr/lib/qt3/%_lib/libeditor.*
/usr/share/applications/*
/usr/share/pixmaps/designer3.png
/usr/share/pixmaps/linguist3.png

%files -n qt3-devel-examples
%defattr(-,root,root)
%dir /usr/lib/qt3/doc
/%{_docdir}/qt3/examples
/usr/lib/qt3/doc/examples

%files -n qt3-man
%defattr(-,root,root)
%{_mandir}/man*/*

%changelog
