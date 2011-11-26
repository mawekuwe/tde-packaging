# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific variables
BuildRequires:	cmake >= 2.8
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity

%define _default_patch_fuzz 2
%define qt_version 3.3.8d
%define qt_ver %{qt_version}

Name:    trinity-kdevelop
Summary: Integrated Development Environment for C++/C
Version: %{?version}
Release: %{?release}%{?dist}%{?_variant}


License: GPLv2
Group: Development/Tools

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source: kdevelop-%{version}.tar.gz
Source1: ftp://129.187.206.68/pub/unix/ide/KDevelop/c_cpp_reference-2.0.2_for_KDE_3.0.tar.bz2

# RedHat Legacy patches
Patch1: c_cpp_reference-2.0.2-config.patch

# TDE 3.5.13 patches
## RHEL / Fedora RPM specific patches
Patch2: kdevelop-3.5.13-kdevdesigner-ftbfs.patch


Provides: kdevelop3 = %{version}-%{release}

Requires: %{name}-libs = %{version}-%{release}


Requires: trinity-kdelibs-devel
Requires: make
Requires: perl
Requires: flex >= 2.5.4
Requires: qt3-designer
Requires: gettext
Requires: ctags

BuildRequires: tqtinterface-devel
BuildRequires: trinity-arts-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdelibs-apidocs
BuildRequires: qt3-devel-docs
BuildRequires: db4-devel
BuildRequires: flex
# FIXME: No CVS support in KDevelop? This is going to suck...
# Requires kdesdk3.
BuildRequires: trinity-kdesdk-devel
BuildRequires: subversion-devel neon-devel
# looks like this is dragged in by apr-devel (dep of subversion-devel), but not
# a dependency
BuildRequires: openldap-devel

%description
The KDevelop Integrated Development Environment provides many features
that developers need as well as providing a unified interface to programs
like gdb, the C/C++ compiler, and make. KDevelop manages or provides:

All development tools needed for C++ programming like Compiler,
Linker, automake and autoconf; KAppWizard, which generates complete,
ready-to-go sample applications; Classgenerator, for creating new
classes and integrating them into the current project; File management
for sources, headers, documentation etc. to be included in the
project; The creation of User-Handbooks written with SGML and the
automatic generation of HTML-output with the KDE look and feel;
Automatic HTML-based API-documentation for your project's classes with
cross-references to the used libraries; Internationalization support
for your application, allowing translators to easily add their target
language to a project;

KDevelop also includes WYSIWYG (What you see is what you get)-creation
of user interfaces with a built-in dialog editor; Debugging your
application by integrating KDbg; Editing of project-specific pixmaps
with KIconEdit; The inclusion of any other program you need for
development by adding it to the "Tools"-menu according to your
individual needs.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Provides: kdevelop3-devel = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Requires: trinity-kdelibs-devel
%description devel
%{summary}.

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-kdelibs
# helps multilib upgrades
Obsoletes: %{name} < %{version}-%{release}
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.



%prep

%setup -q -n kdevelop -a1
%patch1 -p0 -b .config
%patch2 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g" \
  -e "s,kde_htmldir='.*',kde_htmldir='%{tde_docdir}/HTML',g"


%__rm -rf c_cpp_reference-2.0.2_for_KDE_3.0/admin
%__cp -a admin c_cpp_reference-2.0.2_for_KDE_3.0/
%__make -C c_cpp_reference-2.0.2_for_KDE_3.0 -f admin/Makefile.common cvs


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"
export LD_LIBRARY_PATH="%{_libdir}"

# c references
pushd c_cpp_reference-2.0.2_for_KDE_3.0
%configure \
  --with-qt-libraries=$QTDIR/lib \
  --with-qt-includes=$QTDIR/include \
  --with-extra-libs=%{_libdir}
popd

%__mkdir build
cd build
%cmake \
  -DWITH_BUILDTOOL_ALL=ON \
  -DWITH_LANGUAGE_ALL=ON \
  -DWITH_VCS_ALL=OFF \
  -DBUILD_ALL=ON \
  ..
  

%__make %{?_smp_mflags}

cd ..
%__make %{?_smp_mflags} -C c_cpp_reference-2.0.2_for_KDE_3.0

%install
%__rm -rf %{buildroot}
cd build
%__make install DESTDIR=%{buildroot}
cd ..
%__make install DESTDIR=%{buildroot} -C c_cpp_reference-2.0.2_for_KDE_3.0

# remove useless files
%__rm -rf %{buildroot}%{_prefix}/kdevbdb


%post
for f in hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun
for f in hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{tde_docdir}/HTML/en/*
%{_bindir}/*
%{tde_libdir}/*
%{_libdir}/kconf_update_bin/*
%{_datadir}/applications/kde/*
%{_datadir}/apps/*
%{_datadir}/config/*
%{_datadir}/desktop-directories/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*
%{_datadir}/mimelnk/*.desktop
%{_datadir}/mimelnk/*/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*

%files libs
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_includedir}/*


%changelog
* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Fix HTML directory location

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sat Oct 29 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
- Based on SPEC file from Fedora: kdevelop 9:3.5.3-1
