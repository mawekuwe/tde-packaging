#
# spec file for package qt3-devel-doc
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


Name:           qt3-devel-doc
BuildRequires:  cups-devel freeglut-devel freetype2-devel gcc-c++ pkgconfig qt3-devel update-desktop-files
%if %suse_version < 1130
BuildRequires:  libpng-devel
%else
BuildRequires:  libpng14-devel
%endif
Url:            http://www.trolltech.com/
License:        GPL, QPL
AutoReqProv:    on
Summary:        Documentation for the Qt 3 Development Kit
Group:          Documentation/HTML
Version:        3.3.8d
Release:        1
PreReq:         /bin/grep
BuildArch:      noarch 
Provides:       qt3-devel-tutorial
Obsoletes:      qt3-devel-tutorial
Requires:       qt3-devel
%define x11_free -x11-free-
%define rversion %version
# COMMON-BEGIN
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
This package contains the documentation for the Qt 3 Development Kit.

You will find documentation, precompiled examples, and a tutorial for
getting started with Qt in /usr/lib/qt3/doc.

This package contains the documentation for the Qt 3 Development Kit.

You will find documentation, precompiled examples, and a tutorial for
getting started with Qt in /usr/lib/qt3/doc.

This package contains the documentation for the Qt 3 Development Kit.

You will find documentation, precompiled examples, and a tutorial for
getting started with Qt in /usr/lib/qt3/doc.

This package contains the documentation for the Qt 3 Development Kit.

You will find documentation, precompiled examples, and a tutorial for
getting started with Qt in /usr/lib/qt3/doc.

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
# COMMON-END

%description
This package contains the documentation for the Qt 3 Development Kit.

You will find documentation, precompiled examples, and a tutorial for
getting started with Qt in /usr/lib/qt3/doc.

This package contains the documentation for the Qt 3 Development Kit.

You will find documentation, precompiled examples, and a tutorial for
getting started with Qt in /usr/lib/qt3/doc.

This package contains the documentation for the Qt 3 Development Kit.

You will find documentation, precompiled examples, and a tutorial for
getting started with Qt in /usr/lib/qt3/doc.

This package contains the documentation for the Qt 3 Development Kit.

You will find documentation, precompiled examples, and a tutorial for
getting started with Qt in /usr/lib/qt3/doc.

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
call_configure -thread -shared -no-sql-mysql -no-sql-psql -no-sql-odbc -no-sql-sqlite $OPTIONS
cd src
make %{?jobs:-j%jobs}
cd ..

%install
export VERSION=%suse_version
export WLIB=%_lib
export QTDIR=`pwd`
source %SOURCE1 %{version}
cd src
make INSTALL_ROOT=$RPM_BUILD_ROOT install_htmldocs
cd ..
#
# install menu entries
#
%suse_update_desktop_file -i -u qtconfig3 Qt Utility DesktopSettings
%suse_update_desktop_file -i assistant3 Qt Development Documentation

install -d -m 0755 ${RPM_BUILD_ROOT}/%{_defaultdocdir}/qt3/
ln -sf /usr/lib/qt3/doc/html ${RPM_BUILD_ROOT}/%{_defaultdocdir}/qt3/
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/
install -m 0644 %SOURCE4 $RPM_BUILD_ROOT/usr/share/pixmaps/

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%dir /usr/lib/qt3/doc
%doc /usr/lib/qt3/doc/html
%{_docdir}/qt3/html
/usr/share/applications/qtconfig3.desktop
/usr/share/applications/assistant3.desktop
/usr/share/pixmaps/assistant3.png

%changelog
