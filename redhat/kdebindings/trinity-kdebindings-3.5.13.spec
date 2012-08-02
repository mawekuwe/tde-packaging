# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
%define tde_bindir %{_prefix}/bin
%define tde_datadir %{_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{_prefix}/include
%define tde_libdir %{_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:		trinity-tdebindings
Summary:	TDE bindings to non-C++ languages
Version:	3.5.13
Release:	5%{?dist}%{_variant}

License:	GPLv2
Group:		User Interface/Desktops

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kdebindings-%{version}.tar.gz

# RedHat Legacy patches (from Fedora)
Patch1:		kdebindings-3.5.6-libgcj.patch

# [kdebindings] Removes 'hpi' support in openjdk (obsolete in openjdk 1.7.0) [Bug #978]
Patch2:		kdebindings-3.5.13-openjdk_remove_hpi_support.patch
# [kdebindings] Allow compilation with Ruby >= 1.9 [Bug #597]
Patch3:		kdebindings-3.5.13-ruby_1.9.patch
# [kdebindings] Fix various build issues [Bug #597]
Patch4:		kdebindings-3.5.13-fixes.patch
# [kdebindings] Fix smoke compilation on MGA2 (missing LDFLAGS)
Patch5:		kdebindings-3.5.13-missing_ldflags.patch


BuildRequires: autoconf automake libtool m4
BuildRequires: tqtinterface-devel
BuildRequires: trinity-arts-devel
BuildRequires: trinity-kdelibs-devel

BuildRequires: desktop-file-utils
BuildRequires: zlib-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: gtk2-devel
BuildRequires: java-openjdk
BuildRequires: xulrunner-devel

%if 0%{?fedora}
BuildRequires: glib-devel
BuildRequires: gtk+-devel
%endif
%if 0%{?mgaversion}
BuildRequires: %{_lib}glib1.2-devel
BuildRequires: %{_lib}gtk+-devel
%endif

%if 0%{?mgaversion}
BuildRequires:	%{_lib}gdk_pixbuf2.0-devel
%else
%if 0%{?fedora} >= 17
BuildRequires: gdk-pixbuf2-devel
%else
BuildRequires: gdk-pixbuf-devel
%endif
%endif


## Python
BuildRequires: python-devel
%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

## ruby
BuildRequires: ruby-devel >= 1.8, ruby
%{!?ruby_arch: %define ruby_arch %(ruby -rrbconfig -e 'puts Config::CONFIG["archdir"]')}
%{!?ruby_rubylibdir: %define ruby_rubylibdir %(ruby -rrbconfig -e 'puts Config::CONFIG["rubylibdir"]')}
# Ruby 1.9 includes are located in strance directories ... (taken from ruby 1.9 spec file)
%global	_normalized_cpu	%(echo %{_target_cpu} | sed 's/^ppc/powerpc/;s/i.86/i386/;s/sparcv./sparc/;s/armv.*/arm/')

## java
%if 0%{?rhel} > 0 && 0%{?rhel} < 6
BuildRequires: java-1.4.2-gcj-compat-devel libgcj-devel gcc-java
%else
BuildRequires: java-devel >= 1.4.2
%if 0%{?fedora} >= 17
BuildRequires: java-1.7.0-openjdk-devel
%else
BuildRequires: java-1.6.0-openjdk-devel
%endif
%endif
%define java_home %{_usr}/lib/jvm/java
%define _with_java --with-java=%{java_home}

## Perl
BuildRequires:	perl-devel
%define perl_vendorarch %{expand:%%(eval `perl -V:installvendorarch`; echo $installvendorarch)}


Obsoletes:	trinity-kdebindings < %{version}-%{release}
Provides:	trinity-kdebindings = %{version}-%{release}

# Metapackage requires
Requires: trinity-tdebindings-java = %{version}-%{release}
Requires: trinity-libsmokeqt1 = %{version}-%{release}
Requires: trinity-libsmokekde1 = %{version}-%{release}
Requires: trinity-perl-dcop = %{version}-%{release}
Requires: trinity-python-dcop = %{version}-%{release}
Requires: trinity-libkjsembed1 = %{version}-%{release}
Requires: trinity-kjscmd = %{version}-%{release}
Requires: trinity-juic = %{version}-%{release}
Requires: trinity-libkorundum0-ruby = %{version}-%{release}
Requires: trinity-libqt0-ruby = %{version}-%{release}


%description
TDE/DCOP bindings to non-C++ languages

%files

##########

%package java
Summary:	TDE Java bindings metapackage [Trinity]
Group:		Environment/Libraries
Requires:	trinity-libdcop3-java = %{version}-%{release}
Requires:	trinity-libdcop3-jni = %{version}-%{release}
Requires:	trinity-libqt3-java = %{version}-%{release}
Requires:	trinity-libqt3-jni = %{version}-%{release}
Requires:	trinity-libtrinity-java = %{version}-%{release}
Requires:	trinity-libtrinity-jni = %{version}-%{release}

%description java
A metapackage depending on all TDE, Qt and DCOP bindings libraries
related to the Java language.

This package is part of the official TDE bindings module.

%files java
%defattr(-,root,root,-)

##########

%package -n trinity-libdcop3-java
Summary:	DCOP bindings for Java [Trinity]
Group:		Environment/Libraries

Requires:	trinity-libdcop3-jni = %{version}-%{release}

%description -n trinity-libdcop3-java
This package contains the Java classes necessary to run Java programs
using the Java DCOP bindings. DCOP is the TDE Desktop COmmunications
Protocol, used for communicating with running TDE applications.

This package is part of the official TDE bindings module.

%files -n trinity-libdcop3-java
%defattr(-,root,root,-)
#%{tde_datadir}/java/dcopjava*.jar
%{tde_libdir}/java/org/kde/DCOP/*.class

##########

%package -n trinity-libdcop3-java-devel
Summary:	DCOP bindings for Java (dcopidl2java program) [Trinity]
Group:		Development/Libraries
Requires:	trinity-libdcop3-java = %{version}-%{release}

%description -n trinity-libdcop3-java-devel
This package contains the dcopidl2java program which generates Java 
stubs from DCOP IDL files, necessary to do development with the DCOP Java
bindings. DCOP is the TDE Desktop COmmunications Protocol, used for
communicating with running TDE applications.

This package is part of the official TDE bindings module.

%files -n trinity-libdcop3-java-devel
%defattr(-,root,root,-)
%{tde_bindir}/dcopidl2java

##########

%package -n trinity-libdcop3-jni
Summary:	DCOP bindings for Java ( Native libraries ) [Trinity]
Group:		Environment/Libraries

%description -n trinity-libdcop3-jni
This package contains the shared libraries and scripts necessary to
run programs using the Java DCOP bindings. DCOP is the TDE Desktop
COmmunications Protocol, used for communicating with running TDE
applications.

This package is part of the official TDE bindings module.

%files -n trinity-libdcop3-jni
%defattr(-,root,root,-)
%{tde_libdir}/libjavadcop.la
%{tde_libdir}/libjavadcop.so

%post -n trinity-libdcop3-jni
/sbin/ldconfig || :

%postun -n trinity-libdcop3-jni
/sbin/ldconfig || :

##########

%package -n trinity-libqt3-java
Summary:	Java bindings for Qt [Trinity]
Group:		Environment/Libraries
Requires:	trinity-libdcop3-jni = %{version}-%{release}
Requires:	trinity-libqt3-jni = %{version}-%{release}
Requires:	trinity-juic = %{version}-%{release}

%description -n trinity-libqt3-java
This package contains the Java classes necessary to run Java programs
using the Java Qt bindings. Qt is a very popular GUI toolkit, used by
the TDE desktop environment.

It also includes many example programs that make use of these bindings,
plus many of the Qt Tutorial examples translated into Java.

This package is part of the official TDE bindings module.

%files -n trinity-libqt3-java
%defattr(-,root,root,-)
%{tde_libdir}/java/qtjava*.jar
%{tde_tdedocdir}/HTML/en/javalib/

##########

%package -n trinity-libqt3-jni
Summary:	Java bindings for Qt ( Native libraries ) [Trinity]
Group:		Environment/Libraries

%description -n trinity-libqt3-jni
This package contains the shared libraries necessary to run Java
programs using the Java Qt bindings. Qt is a very popular GUI
toolkit, used by the TDE desktop environment.

This package is part of the official TDE bindings module.

%files -n trinity-libqt3-jni
%defattr(-,root,root,-)
%{tde_libdir}/libqtjavasupport.la
%{tde_libdir}/libqtjavasupport.so
%{tde_libdir}/libqtjavasupport.so.*
%{tde_libdir}/jni/libqtjava.la
%{tde_libdir}/jni/libqtjava.so
%{tde_libdir}/jni/libqtjava.so.*
%doc qtjava/ChangeLog

%post -n trinity-libqt3-jni
/sbin/ldconfig || :

%postun -n trinity-libqt3-jni
/sbin/ldconfig || :

##########

%package -n trinity-libtrinity-java
Summary:	tdelibs bindings for Java [Trinity]
Group:		Environment/Libraries

Requires:	trinity-libtrinity-jni = %{version}-%{release}

%description -n trinity-libtrinity-java
This package contains the Java classes necessary to run Java programs
using the Java tdelibs bindings. TDE is the Trinity Desktop Environment, a
very popular UNIX Desktop Environment.

It also includes some example applications that use these Java
classes, and multiple usage samples of the most common TDE classes.

This package is part of the official TDE bindings module.

%files -n trinity-libtrinity-java
%defattr(-,root,root,-)
%{tde_libdir}/java/koala*.jar

##########

%package -n trinity-libtrinity-jni
Summary:	tdelibs bindings for java ( Native libraries ) [Trinity]
Group:		Environment/Libraries

%description -n trinity-libtrinity-jni
This package contains the shared libraries necessary to run Java
programs using the Java tdelibs bindings. TDE is the Trinity Desktop
Environment, a very popular UNIX Desktop Environment.

This package is part of the official TDE bindings module.

%files -n trinity-libtrinity-jni
%defattr(-,root,root,-)
%{tde_libdir}/jni/libkdejava.la
%{tde_libdir}/jni/libkdejava.so
%{tde_libdir}/jni/libkdejava.so.*
%doc kdejava/ChangeLog

##########

%package -n trinity-libsmokeqt1
Summary:	SMOKE Binding Library to Qt
Group:		Environment/Libraries

%description -n trinity-libsmokeqt1
The "Scripting Meta Object Kompiler Engine" library is used by
various TDE language bindings packages to provide interfaces to the
Qt library.

This package is part of the official TDE bindings module.

%files -n trinity-libsmokeqt1
%defattr(-,root,root,-)
%{tde_libdir}/libsmokeqt.so.*

%post -n trinity-libsmokeqt1
/sbin/ldconfig || :

%postun -n trinity-libsmokeqt1
/sbin/ldconfig || :

##########

%package -n trinity-libsmokeqt-devel
Summary:	SMOKE Binding Library to Qt - Development Files
Group:		Development/Libraries
Requires:	trinity-libsmokeqt1 = %{version}-%{release}

%description -n trinity-libsmokeqt-devel
The "Scripting Meta Object Kompiler Engine" library is used by
various TDE language bindings packages to provide interfaces to the
Qt library. This package contains the development files for the
library.

If you are a normal user, you probably don't need this
package.

This package is part of the official TDE bindings module.

%files -n trinity-libsmokeqt-devel
%defattr(-,root,root,-)
%{tde_includedir}/smoke.h
%{tde_libdir}/libsmokeqt.so
%{tde_libdir}/libsmokeqt.la

%post -n trinity-libsmokeqt-devel
/sbin/ldconfig || :

%postun -n trinity-libsmokeqt-devel
/sbin/ldconfig || :

##########

%package -n trinity-libsmokekde1
Summary:	SMOKE Binding Library to TDE
Group:		Environment/Libraries

%description -n trinity-libsmokekde1
The "Scripting Meta Object Kompiler Engine" library is used by
various TDE language bindings packages to provide interfaces to the
TDE libraries.

This package is part of the official TDE bindings module.

%files -n trinity-libsmokekde1
%defattr(-,root,root,-)
%{tde_libdir}/libsmokekde.so.*

%post -n trinity-libsmokekde1
/sbin/ldconfig || :

%postun -n trinity-libsmokekde1
/sbin/ldconfig || :

##########

%package -n trinity-libsmokekde-devel
Summary:	SMOKE Binding Library to TDE - Development Files
Group:		Development/Libraries
Requires:	trinity-libsmokekde1 = %{version}-%{release}

%description -n trinity-libsmokekde-devel
The "Scripting Meta Object Kompiler Engine" library is used by
various TDE language bindings packages to provide interfaces to the
Qt and TDE libraries. This package contains the development files for
the library.

If you are a normal user, you probably don't need this
package.

This package is part of the official TDE bindings module.

%files -n trinity-libsmokekde-devel
%defattr(-,root,root,-)
%{tde_libdir}/libsmokekde.so
%{tde_libdir}/libsmokekde.la

%post -n trinity-libsmokekde-devel
/sbin/ldconfig || :

%postun -n trinity-libsmokekde-devel
/sbin/ldconfig || :

##########

%package -n trinity-perl-dcop
Summary:	DCOP Bindings for Perl 
Group:		Development/Libraries

Obsoletes:	trinity-kdebindings-dcopperl < %{version}-%{release}
Provides:	trinity-kdebindings-dcopperl = %{version}-%{release}

%description -n trinity-perl-dcop
Perl bindings to the DCOP interprocess communication protocol used by TDE

%files -n trinity-perl-dcop
%defattr(-,root,root,-)
%{perl_vendorarch}/auto/DCOP/*
%{perl_vendorarch}/DCOP.pm
%{perl_vendorarch}/DCOP/*
%doc dcopperl/AUTHORS dcopperl/Changes dcopperl/README dcopperl/TODO
%{tde_mandir}/man3/DCOP.3pm*

##########

%package -n trinity-python-dcop
Summary:	DCOP bindings for Python
Group:		Environment/Libraries
Requires:	python
#Provides:	%{name}-dcoppython = %{version}-%{release}

%description -n trinity-python-dcop
This package contains the shared libraries necessary to run and
develop Python programs using the Python DCOP bindings
libraries. DCOP is the TDE Desktop COmmunications Protocol, used for
communicating with running TDE applications.

This package is part of the official TDE bindings module.

%files -n trinity-python-dcop
%defattr(-,root,root,-)
%{python_sitearch}/pcop.la
%{python_sitearch}/pcop.so
%{python_sitearch}/pydcop.py*

##########

%package -n trinity-libkjsembed1
Summary:	Embedded JavaScript library
Group:		Environment/Libraries

%description -n trinity-libkjsembed1
This package contains the shared libraries necessary to run programs
linked with the KJSEmbed library. This library provides JavaScript
embedded scripting facilities to TDE applications.

This package is part of the official TDE bindings module.

%files -n trinity-libkjsembed1
%defattr(-,root,root,-)
%{tde_libdir}/libkjsembed.so.*
%{tde_tdelibdir}/libimagefxplugin.la
%{tde_tdelibdir}/libimagefxplugin.so
%{tde_datadir}/services/imagefx_plugin.desktop
%{tde_tdelibdir}/libqprocessplugin.so
%{tde_tdelibdir}/libqprocessplugin.la
%{tde_datadir}/services/qprocess_plugin.desktop
%{tde_tdelibdir}/libfileitemplugin.la
%{tde_tdelibdir}/libfileitemplugin.so
%{tde_datadir}/services/kfileitem_plugin.desktop
%{tde_datadir}/apps/kjsembed/cmdline.js
%{tde_datadir}/servicetypes/binding_type.desktop
%{tde_bindir}/embedjs
%{tde_datadir}/apps/embedjs/embedjsui.rc
%{tde_datadir}/applnk/Utilities/embedjs.desktop
%{tde_datadir}/icons/hicolor/16x16/apps/embedjs.png
%{tde_datadir}/icons/hicolor/32x32/apps/embedjs.png
%{tde_tdelibdir}/libjavascript.la
%{tde_tdelibdir}/libjavascript.so
%{tde_datadir}/apps/kate/scripts/swaptabs.js
%{tde_datadir}/apps/kate/scripts/swaptabs.ui
%{tde_datadir}/apps/kate/scripts/swaptabs.desktop
%{tde_datadir}/services/javascript.desktop
%doc kjsembed/docs/ChangeLog

%post -n trinity-libkjsembed1
/sbin/ldconfig ||:
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database >& /dev/null ||:

%postun -n trinity-libkjsembed1
/sbin/ldconfig ||:
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database >& /dev/null ||:

##########

%package -n trinity-libkjsembed-devel
Summary:	Embedded JavaScript library (Development files)
Group:		Development/Libraries
Requires:	trinity-libkjsembed1 = %{version}-%{release}

%description -n trinity-libkjsembed-devel
This package contains the header files and symbolic links necessary
to develop and compile programs using the KJSEmbed library. This
library provides JavaScript embedded scripting facilities to TDE
applications.

It also includes lots of example programs that make use of these
bindings, plus comprehensive documentation of the bindings.

This package is part of the official TDE bindings module.

%files -n trinity-libkjsembed-devel
%defattr(-,root,root,-)
%{tde_includedir}/kjsembed/
%{tde_libdir}/libkjsembed.so
%{tde_libdir}/libkjsembed.la
%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/

%post -n trinity-libkjsembed-devel
/sbin/ldconfig || :

%postun -n trinity-libkjsembed-devel
/sbin/ldconfig || :

##########

%package -n trinity-kjscmd
Summary:	A script interpreter using the TDE JavaScript library
Group:		Environment/Libraries

%description -n trinity-kjscmd
This package contains the kjscmd program, which is a standalone
JavaScript interpreter using the KJSEmbed library.

This package is part of the official TDE bindings module.

%files -n trinity-kjscmd
%defattr(-,root,root,-)
%{tde_bindir}/kjscmd
%{tde_tdeappdir}/kjscmd.desktop
%{tde_mandir}/man1/kjscmd.*
%{tde_tdelibdir}/libjsconsoleplugin.la
%{tde_tdelibdir}/libjsconsoleplugin.so

%post -n trinity-kjscmd
update-desktop-database >& /dev/null ||:

%postun -n trinity-kjscmd
update-desktop-database >& /dev/null ||:

##########

%package -n trinity-juic
Summary:	The Qt Java UI Compiler
Group:		Environment/Libraries
Requires:	trinity-libqt3-java = %{version}-%{release}

%description -n trinity-juic
This package contains the juic program, which is used to convert
a UI description file generated by the Qt Designer, and converts
it into a Qt Java class. It is necessary for compiling and 
developing programs using the Qt Java bindings together with Qt
Designer.

This package is part of the official TDE bindings module.

%files -n trinity-juic
%defattr(-,root,root,-)
%{tde_bindir}/juic
%{tde_datadir}/juic/

##########

%package -n trinity-libkorundum0-ruby
Summary:	TDE bindings for Ruby [Trinity]
Group:		Environment/Libraries
Requires:	trinity-libqt0-ruby = %{version}-%{release}

%description -n trinity-libkorundum0-ruby
This package contains the files necessary for running and developing
Ruby code using the Korundum TDE Ruby bindings.

It also includes some example programs and templates that make use of
these bindings.

This package is part of the official TDE bindings module.

%files -n trinity-libkorundum0-ruby
%defattr(-,root,root,-)
%{tde_bindir}/rbkdesh
%{tde_bindir}/rbkdeapi
%{tde_bindir}/krubyinit
%{tde_bindir}/rbkconfig_compiler
%{ruby_rubylibdir}/Korundum.rb
%{ruby_rubylibdir}/KDE/korundum.rb
%if 0%{?fedora} == 17
%{_usr}/%{_lib}/korundum.la
%{_usr}/%{_lib}/korundum.so*
%else
%{ruby_arch}/korundum.la
%{ruby_arch}/korundum.so*
%endif
%doc korundum/ChangeLog

%post -n trinity-libkorundum0-ruby
/sbin/ldconfig || :

%postun -n trinity-libkorundum0-ruby
/sbin/ldconfig || :

##########

%package -n trinity-libqt0-ruby
Summary:	Qt bindings for Ruby [Trinity]
Group:		Environment/Libraries
Requires:	ruby

%description -n trinity-libqt0-ruby
This package contains the files necessary for running and developing
Ruby code using the Qt Ruby bindings.

It also includes some example programs that make use of these bindings,
plus many of the Qt Tutorial examples translated into Ruby.

This package is part of the official TDE bindings module.

%files -n trinity-libqt0-ruby
%defattr(-,root,root,-)
%{tde_bindir}/rbqtsh
%{tde_bindir}/rbqtapi
%{tde_bindir}/rbuic
%{tde_bindir}/qtrubyinit
%{ruby_rubylibdir}/Qt/qtruby.rb
%{ruby_rubylibdir}/Qt.rb
%{ruby_arch}/qtruby.so*
%{ruby_arch}/qtruby.la
%if 0%{?fedora} >= 17
%{_usr}/%{_lib}/qui.so*
%{_usr}/%{_lib}/qui.la
%else
%{ruby_arch}/qui.so*
%{ruby_arch}/qui.la
%endif
%doc qtruby/ChangeLog

%post -n trinity-libqt0-ruby
/sbin/ldconfig || :

%postun -n trinity-libqt0-ruby
/sbin/ldconfig || :

##########

%if 0
%package -n trinity-kmozilla
Summary:	Kmozilla for TDE
Group:		Environment/Libraries

%description -n trinity-kmozilla
%{summary}

%files -n trinity-kmozilla
%defattr(-,root,root,-)
%{tde_bindir}/kmozilla
%{tde_libdir}/libkmozillapart.so.*
%{tde_libdir}/libkmozillapart.so
%{tde_libdir}/libkmozillapart.la
%{tde_datadir}/services/kmozilla.desktop
%endif

##########

%package -n trinity-xpart-notepad
Summary:	A small XPart editor
Group:		Applications/Utilities

%description -n trinity-xpart-notepad
xpart_notepad is a small XPart editor. Use it to understand how to use XPart.

%files -n trinity-xpart-notepad
%defattr(-,root,root,-)
%{tde_bindir}/shell_xparthost
%{tde_bindir}/xp_notepad
%{tde_libdir}/libxp_notepadpart.la
%{tde_libdir}/libxp_notepadpart.so
%{tde_libdir}/libxp_notepadpart.so.*
%{tde_datadir}/services/xp_notepad.desktop
%doc xparts/xpart_notepad/README

%post -n trinity-xpart-notepad
/sbin/ldconfig || :

%postun -n trinity-xpart-notepad
/sbin/ldconfig || :

##########

%package -n trinity-libgtkxparts1
Summary:	Xparts library for GTK
Group:		Environment/Libraries

%description -n trinity-libgtkxparts1
%{summary}

%files -n trinity-libgtkxparts1
%defattr(-,root,root,-)
%{tde_libdir}/libgtkxparts.so.*
%{tde_libdir}/libgtkxparts.la

%post -n trinity-libgtkxparts1
/sbin/ldconfig || :

%postun -n trinity-libgtkxparts1
/sbin/ldconfig || :

##########

%package -n trinity-libkdexparts1
Summary:	Xparts library for KDE
Group:		Environment/Libraries

%description -n trinity-libkdexparts1
%{summary}

%files -n trinity-libkdexparts1
%defattr(-,root,root,-)
%{tde_libdir}/libkdexparts.so.*
%{tde_libdir}/libkdexparts.la

%post -n trinity-libkdexparts1
/sbin/ldconfig || :

%postun -n trinity-libkdexparts1
/sbin/ldconfig || :

##########

%package -n trinity-libxparts-devel
Summary:	Xparts development files
Group:		Development/Libraries
Requires:	trinity-libgtkxparts1 = %{version}-%{release}
Requires:	trinity-libkdexparts1 = %{version}-%{release}

%description -n trinity-libxparts-devel
%{summary}

%files -n trinity-libxparts-devel
%defattr(-,root,root,-)
%{tde_includedir}/xkparts/
%{tde_libdir}/libgtkxparts.so
%{tde_libdir}/libkdexparts.so

%post -n trinity-libxparts-devel
/sbin/ldconfig || :

%postun -n trinity-libxparts-devel
/sbin/ldconfig || :

##########

%package xparts-extras
Summary:	Extra xparts for TDE [Trinity]
Group:		Environment/Libraries

# Metapckage requires
Requires:	trinity-xpart-notepad = %{version}-%{release}
Requires:	trinity-libgtkxparts1 = %{version}-%{release}
Requires:	trinity-libkdexparts1 = %{version}-%{release}
Requires:	trinity-libdcop-c = %{version}-%{release}

%description xparts-extras
This package contains extra xparts-based modules for Trinity
This includes the mozilla-konqueror plugin

This package is part of the official TDE bindings module.

%files xparts-extras

###########

%package -n trinity-libdcop-c
Summary:	DCOP bindings for C [Trinity]
Group:		Environment/Libraries

%description -n trinity-libdcop-c
%{summary}

%files -n trinity-libdcop-c
%defattr(-,root,root,-)
%{tde_libdir}/libdcopc.so.*

%post -n trinity-libdcop-c
/sbin/ldconfig || :

%postun -n trinity-libdcop-c
/sbin/ldconfig || :

###########

%package -n trinity-libdcop-c-devel
Summary:	DCOP bindings for C, development files [Trinity]
Group:		Development/Libraries
Requires:	trinity-libdcop-c = %{version}-%{release}

%description -n trinity-libdcop-c-devel
%{summary}

%files -n trinity-libdcop-c-devel
%defattr(-,root,root,-)
%{tde_libdir}/libdcopc.so
%{tde_libdir}/libdcopc.la
%{tde_includedir}/dcopc/

%post -n trinity-libdcop-c-devel
/sbin/ldconfig || :

%postun -n trinity-libdcop-c-devel
/sbin/ldconfig || :

##########

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	trinity-tdelibs-devel 

Obsoletes:	trinity-kdebindings-devel < %{version}-%{release}
Provides:	trinity-kdebindings-devel = %{version}-%{release}

# Metapackage
Requires:	trinity-libsmokeqt-devel = %{version}-%{release}
Requires:	trinity-libdcop3-java-devel = %{version}-%{release}
Requires:	trinity-libsmokekde-devel = %{version}-%{release}
Requires:	trinity-libkjsembed-devel = %{version}-%{release}
Requires:	trinity-libxparts-devel = %{version}-%{release}
Requires:	trinity-libdcop-c-devel = %{version}-%{release}
Requires:	trinity-tdebindings-devel = %{version}-%{release}

%description devel
Development files for the TDE bindings.

%files devel

##########

%prep
%setup -q -n kdebindings
%patch1 -p1 -b .libgcj

%if 0%{?fedora} >= 17
%patch2 -p1 -b .libhpi
%patch3 -p1
%endif
%patch4 -p1
%patch5 -p1

# Adds non-standard Ruby include path in include dirs
for d in \
  qtruby/rubylib/qtruby \
  qtruby/rubylib/designer/uilib \
  qtruby/bin \
  korundum/rubylib/korundum \
  korundum/bin \
; do
  echo -e "\nINCLUDES += -I%{_usr}/include/%{_normalized_cpu}-%{_target_os}" >> "${d}/Makefile.am"
done

# Disable kmozilla, it does not build with recent xulrunner (missing 'libmozjs.so')
%__sed -i "xparts/Makefile.am" \
  -e "s|SUBDIRS = .*|SUBDIRS = src xpart_notepad|"

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i "admin/acinclude.m4.in" \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

unset JAVA_HOME ||:
%{?java_home:JAVA_HOME=%{java_home}; export JAVA_HOME}

# sip/PyQt/PyKDE built separately, not here
export DO_NOT_COMPILE="$DO_NOT_COMPILE python"

%configure \
  --exec-prefix=%{_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --docdir=%{tde_docdir} \
  --includedir=%{tde_includedir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking \
  --with-extra-libs=%{tde_libdir} \
  --with-pythondir=%{_usr} \
  --enable-closure \
  --enable-final \
  %{?_with_java} %{!?_with_java:--without-java} \
  %{?_enable_qscintilla} %{!?_enable_qscintilla:--disable-qscintilla} \
  --with-extra-includes=%{tde_includedir}/tqt

pushd dcopperl
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL INSTALLDIRS=vendor

# Ugly hack to add TQT include directory in Makefile
# Also modifies the man pages directory
sed -i Makefile \
  -e "s|^\(INC = .*\)|\1 -I%{tde_includedir}/tqt|" \
  -e "s|/usr/share/man|%{tde_mandir}|g"

%__make OPTIMIZE="$RPM_OPT_FLAGS" ||:
popd

# smoke (not smp-safe)
%__make -C smoke

# The rest is smp-safe
%__make %{?_smp_mflags} PYTHON=%{__python}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf $RPM_BUILD_ROOT

%__make install DESTDIR=%{?buildroot} \
  PYTHON=%{__python}

# Removes some perl files
find $RPM_BUILD_ROOT -type f -a \( -name perllocal.pod -o -name .packlist \
  -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'

# locale's
%find_lang %{name} || touch %{name}.lang
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d $RPM_BUILD_ROOT$HTML_DIR ]; then
for lang_dir in $RPM_BUILD_ROOT$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
    # replace absolute symlinks with relative ones
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && ln -nsf ../common $i/common
      done
    popd
  fi
done  
fi  

# Installs juic
%__install -D -m 755 qtjava/designer/juic/bin/juic	%{?buildroot}%{tde_bindir}/juic
%__install -d -m 755 %{?buildroot}%{tde_datadir}/juic/common
%__install qtjava/designer/juic/common/*.xml %{?buildroot}%{tde_datadir}/juic/common
%__install qtjava/designer/juic/common/*.xsl %{?buildroot}%{tde_datadir}/juic/common
%__install -d -m 755 %{?buildroot}%{tde_datadir}/juic/java
%__install qtjava/designer/juic/java/*.xml %{?buildroot}%{tde_datadir}/juic/java
%__install qtjava/designer/juic/java/*.xsl %{?buildroot}%{tde_datadir}/juic/java
%__install qtjava/designer/juic/juic.xsl  %{?buildroot}%{tde_datadir}/juic

# kjsembed sample files
%__install -d -m 755 %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/
%__install kjsembed/plugins/customobject_plugin.cpp %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/
%__install kjsembed/plugins/customobject_plugin.h %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/
%__install kjsembed/plugins/customobject_plugin.desktop %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/
%__install kjsembed/plugins/customqobject_plugin.cpp %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/
%__install kjsembed/plugins/customqobject_plugin.h %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/
%__install kjsembed/plugins/customqobject_plugin.desktop %{?buildroot}%{tde_docdir}/trinity-libkjsembed-devel/plugin-examples/customobject/


%clean
%__rm -rf $RPM_BUILD_ROOT



%changelog
* Sun Jul 29 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-5
- Split into several packages
- Add support for Mageia 2 
- Fix dcopperl man page location
- Removes strange install stuff from legacy Fedora

* Tue Apr 24 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Add support for Fedora 17
- Removes 'hpi' support in openjdk (obsolete in openjdk 1.7.0) [Bug #978]
- Allow compilation with Ruby >= 1.9 [Bug #597]
- Fix various build issues [Bug #597]

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Fix HTML directory location

* Fri Nov 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Add missing BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sat Sep 03 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
- Built with future TDE version (3.5.13 + cmake + QT3.3.8d)
