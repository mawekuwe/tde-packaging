#
# spec file for package qt3
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



Name:           qt3
#Remember also to modify Requires in -devel package
BuildRequires:  Mesa-devel c++_compiler cups-devel freetype2-devel libjpeg-devel libmng-devel pkgconfig update-desktop-files xorg-x11-devel
Url:            http://www.trolltech.com/
License:        GPLv2 ; GPLv3 ; QPL ..
%if %suse_version > 1120
BuildRequires:  libpng14-compat-devel
%else
BuildRequires:  libpng-devel
%endif
Group:          System/Libraries
# bug437293
%ifarch ppc64
Obsoletes:      qt3-64bit
%endif
#
Summary:        A library for developing applications with graphical user interfaces
Version:        3.3.8d
Release:        110
Provides:       qt_library_%version
Recommends:     kdelibs3-default-style
PreReq:         /bin/grep
# COMMON-BEGIN
%define x11_free -x11-free-
%define rversion 3.3.8b
Source0:        http://mirror.its.uidaho.edu/pub/trinity/releases/3.5.13/dependencies/qt3-3.3.8.d.tar.gz
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
Patch12:        qtrc-path.diff
Patch14:        lib64-plugin-support.diff
Patch15:        pluginmanager-fix.diff
Patch18:        no-rpath.dif
Patch19:        shut-up.diff
Patch21:        fix-GL-loading.diff
Patch23:        fix-accessible.diff
Patch28:        fix-key-release-event-with-imm.diff
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

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qt is a program library for developing applications with graphical user
interfaces. It allows you to rapidly develop professional programs. The
Qt library is available not only for Linux but for a great number of
Unices and even for Windows. Thus it is possible to write programs that
may be easily ported to those platforms.

You need a license for using Qt with a non-GPL application, which can
be acquired from sales@trolltech.com.

See /usr/share/doc/packages/qt3 for details about the new features of
the current Qt library!

%define build_sub_dirs src plugins/src tools/designer/uilib/ tools/designer/uic tools/qtconfig tools/assistant/lib tools/assistant tutorial

%prep
%setup -q -n qt3
%patch1
%patch2
%patch4
%patch5
%patch12
if [ "%_lib" = "lib64" ]; then
%patch14
fi
%patch15
%patch18
%patch19
%patch23
#%patch28
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
# copy qt kde integration files
cp %SOURCE100 %SOURCE101 src/kernel/
cp %SOURCE101 include/private/
cd translations
tar xvjf %SOURCE12
cd ..
# COMMON-END

%package devel
License:        GPLv2 ; GPLv3 ; QPL ..
Summary:        Include Files and Libraries mandatory for Development
Requires:       qt3 = %version 
Requires:       pkgconfig cups-devel freetype2-devel libmng-devel libjpeg-devel c++_compiler xorg-x11-devel
%if %suse_version > 1120
Recommends:     libpng14-compat-devel
Requires:       libpng-devel
%else
Requires:       libpng-devel
%endif
%if %suse_version > 1000
Requires:       Mesa-devel
%else
Requires:       xorg-x11-Mesa xorg-x11-Mesa-devel
%endif
%ifnarch x86_64 s390x sparc64 ppc64 mips64
Conflicts:      devel_libs-32bit
%endif
# bug437293
%ifarch ppc64
Obsoletes:      qt3-devel-64bit
%endif
#
Group:          Development/Libraries/X11

%description devel
You need this package if you want to compile programs with Qt 3. It
contains the "Qt Crossplatform Development Kit 2". Under /usr/lib/qt3
you will find include files.

You need a license for using Qt with a non-GPL application. A license
can be acquired at sales@trolltech.com.

%build
export VERSION=%suse_version
source %SOURCE1 %{version}
export WLIB=%_lib
export QTDIR=`pwd`
if [ %_lib == "lib64" ]; then
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DUSE_LIB64_PATHES"
fi
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
#
# call build from build_script.rpmrc for threaded Qt library
# only really needed tools will be builded here, all extra tools will be
# builded in qt3.spec
#
call_configure -v -thread -shared -no-sql-mysql -no-sql-psql -no-sql-odbc -no-sql-sqlite $OPTIONS
for i in %build_sub_dirs ; do
 cd $i
 make %{?jobs:-j%jobs}
 cd -
done

%install
export VERSION=%suse_version
export WLIB=%_lib
export QTDIR=`pwd`
source %SOURCE1 %{version}
for i in %build_sub_dirs ; do
 cd $i
 make INSTALL_ROOT=$RPM_BUILD_ROOT install
 cd -
done
post_install $RPM_BUILD_ROOT/usr/lib/qt3/
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/
sed -i -e 's, on: .*,,' $RPM_BUILD_ROOT/usr/lib/qt3/%_lib/*.la
#
# copy additional files
#
install -m 0755 bin/qmake bin/moc ${RPM_BUILD_ROOT}/usr/lib/qt3/bin/
install -m 0755 -d ${RPM_BUILD_ROOT}/usr/lib/qt3/translations/
install -m 0644 translations/*.qm ${RPM_BUILD_ROOT}/usr/lib/qt3/translations/
if [ %_lib = lib64 ]; then
 for i in $RPM_BUILD_ROOT/usr/lib/qt3/plugins/*/*.so; do
   mv "$i" "${i%.so}.lib64.so"
 done
fi
#
# move pkgconfig files
#
mkdir -p $RPM_BUILD_ROOT/%_libdir/pkgconfig
mv $RPM_BUILD_ROOT/usr/lib/qt3/%_lib/pkgconfig/*.pc \
   $RPM_BUILD_ROOT/%_libdir/pkgconfig
rmdir $RPM_BUILD_ROOT/usr/lib/qt3/%_lib/pkgconfig
#
# move docs in doc dir
#
install -d -m 0755 ${RPM_BUILD_ROOT}/%{_defaultdocdir}/qt3/
install -d -m 0755 ${RPM_BUILD_ROOT}/usr/lib/qt3/mkspecs/
install -d -m 0755 ${RPM_BUILD_ROOT}/usr/lib/qt3/mkspecs/
cp -a mkspecs/*    ${RPM_BUILD_ROOT}/usr/lib/qt3/mkspecs/
if [ %_lib == "lib64" ]; then
  ln -sf linux-g++-64 ${RPM_BUILD_ROOT}/usr/lib/qt3/mkspecs/default
else
  ln -sf linux-g++ ${RPM_BUILD_ROOT}/usr/lib/qt3/mkspecs/default
fi
find ${RPM_BUILD_ROOT}/usr/lib/qt3/mkspecs -type f -perm /111 -print0 | xargs -0 chmod a-x
#
# create links in ld.so.conf path
#
install -d -m 0755 ${RPM_BUILD_ROOT}/%{_libdir}
ln -sf ../lib/qt3/%{_lib}/libqt-mt.so.3 ${RPM_BUILD_ROOT}/%{_libdir}/libqt-mt.so.3
ln -sf ../lib/qt3/%{_lib}/libqui.so.1   ${RPM_BUILD_ROOT}/%{_libdir}/libqui.so.1
[ "lib" != "%{_lib}" ] && \
   ln -sf ../lib/qt3 ${RPM_BUILD_ROOT}/%{_libdir}/qt3
mkdir -p ${RPM_BUILD_ROOT}/etc/profile.d
install -m 644 %SOURCE10 %SOURCE11 ${RPM_BUILD_ROOT}/etc/profile.d
#
# default qt settings
#
mkdir -p ${RPM_BUILD_ROOT}/etc/X11
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/qt3/etc/
ln -sf /etc/X11/ ${RPM_BUILD_ROOT}/usr/lib/qt3/etc/settings
install -m 0644 %SOURCE3 ${RPM_BUILD_ROOT}/etc/X11/qtrc
#
# clean broken links
#
if [ %_lib == "lib64" ]; then
 rm ${RPM_BUILD_ROOT}/usr/lib/qt3/mkspecs/linux-g++-64/linux-g++-64
else
 rm ${RPM_BUILD_ROOT}/usr/lib/qt3/mkspecs/linux-g++/linux-g++
fi
rm -rf ${RPM_BUILD_ROOT}/usr/lib/qt3/doc/html

%pre
if test -L usr/lib/qt3; then
  rm usr/lib/qt3
fi

%post
/sbin/ldconfig
if ! grep -q '^\[3.3\]' etc/X11/qtrc ; then
echo ""      >> etc/X11/qtrc
echo "[3.3]" >> etc/X11/qtrc
echo "libraryPath=/opt/kde3/lib64/kde3/plugins/:/opt/kde3/lib/kde3/plugins/" >> etc/X11/qtrc
fi

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,755)
# FIXME provide new changelog if kb9vqf will give one
%doc changes-3.3.8b README* LICENSE* MANIFEST FAQ
%dir /usr/lib/qt3/translations
%dir /usr/lib/qt3
%dir /usr/lib/qt3/bin
%dir /usr/lib/qt3/%{_lib}
%{_libdir}/libqt-mt.so.*
%{_libdir}/libqui.so.*
/usr/lib/qt3/bin/qtconfig
/usr/lib/qt3/%{_lib}/libqt-mt.so.*
/usr/lib/qt3/%{_lib}/libqui.so.*
%dir /usr/lib/qt3/etc
/usr/lib/qt3/etc/settings
/usr/lib/qt3/plugins
/usr/lib/qt3/bin/assistant
%lang(de) /usr/lib/qt3/translations/assistant_de.qm
%lang(ar) /usr/lib/qt3/translations/qt_ar.qm
%lang(ca) /usr/lib/qt3/translations/qt_ca.qm
%lang(cs) /usr/lib/qt3/translations/qt_cs.qm
%lang(de) /usr/lib/qt3/translations/qt_de.qm
%lang(es) /usr/lib/qt3/translations/qt_es.qm
%lang(fr) /usr/lib/qt3/translations/qt_fr.qm
%lang(he) /usr/lib/qt3/translations/qt_he.qm
%lang(ru) /usr/lib/qt3/translations/qt_ru.qm
%lang(sk) /usr/lib/qt3/translations/qt_sk.qm
%lang(it) /usr/lib/qt3/translations/qt_it.qm
%lang(ja) /usr/lib/qt3/translations/qt_ja.qm
%lang(nb) /usr/lib/qt3/translations/qt_nb.qm
%lang(pl) /usr/lib/qt3/translations/qt_pl.qm
%lang(pt) /usr/lib/qt3/translations/qt_pt-br.qm
%lang(pt) /usr/lib/qt3/translations/qt_pt.qm
%lang(zh) /usr/lib/qt3/translations/qt_zh-cn.qm
%lang(zh) /usr/lib/qt3/translations/qt_zh-tw.qm
%config(noreplace) /etc/X11/qtrc
%ifarch s390x sparc64 x86_64 ppc64 mips64
%dir %{_libdir}/qt3
%endif

%files devel
%defattr(-,root,root,755)
# FIXME provide new changelog if kb9vqf will give one
%doc changes-3.3.8b
/usr/lib/qt3/bin/moc
/usr/lib/qt3/bin/qmake
/usr/lib/qt3/bin/uic
/usr/lib/qt3/include
/usr/lib/qt3/%{_lib}/libqt-mt.la
/usr/lib/qt3/%{_lib}/libqt-mt.so
/usr/lib/qt3/%{_lib}/libqt-mt.prl
/usr/lib/qt3/%{_lib}/libqui.so
/usr/lib/qt3/%{_lib}/libqui.prl
/usr/lib/qt3/mkspecs
/%_libdir/pkgconfig/qt-mt.pc
/usr/lib/qt3/%_lib/libqassistantclient.*
%config /etc/profile.d/qt3.*

%changelog
