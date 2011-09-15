# Default version for this component
%if "%{?version}" == ""
%define version 3.5.12
%endif
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/kde3

%define _default_patch_fuzz 2
%define qt_version 3.3.8b
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

Prefix:	%{_prefix}

Source: kdevelop-%{version}.tar.gz
Source1: ftp://129.187.206.68/pub/unix/ide/KDevelop/c_cpp_reference-2.0.2_for_KDE_3.0.tar.bz2

# RedHat Legacy patches
Patch1: c_cpp_reference-2.0.2-config.patch
#Patch2: kdevelop-2.1.5_for_KDE_3.1-doc.patch
# improved integration for the KDE 4 template - no special KDE 4 build environment needed in Fedora
Patch4: kdevelop-3.5.2-kde4template.patch

#upstream patches

Provides: kdevelop3 = %{version}-%{release}

Requires: %{name}-libs = %{version}-%{release}


Requires: trinity-kdelibs-devel
Requires: make
Requires: perl
Requires: flex >= 2.5.4
Requires: qt3-designer
Requires: gettext
Requires: ctags

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
#patch2 -p1 -b .doc
#patch4 -p1 -b .kde4template

%__rm -rf c_cpp_reference-2.0.2_for_KDE_3.0/admin
%__cp -a admin c_cpp_reference-2.0.2_for_KDE_3.0/
%__make -C c_cpp_reference-2.0.2_for_KDE_3.0 -f admin/Makefile.common cvs

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
QTDIR="" && source /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

# Fix KDE detection fail in "./configure" because tqt.h cannot be found
export CXXFLAGS="${CXXFLAGS} -I%{_includedir}/tqt"

# c references
pushd c_cpp_reference-2.0.2_for_KDE_3.0
%configure \
  --with-qt-libraries=$QTDIR/lib \
  --with-qt-includes=$QTDIR/include \
  --with-extra-libs=%{_libdir} \
  --with-extra-includes=%{_includedir}/tqt
popd

%configure \
   --enable-new-ldflags \
   --disable-dependency-tracking \
   --disable-rpath \
   --disable-debug \
   --disable-warnings \
   --enable-final \
   --with-qtdoc-dir=%{_docdir}/qt-devel-%{qt_ver}/html/ \
   --with-kdelibsdoc-dir=%{tde_docdir}/HTML/en/kdelibs-apidocs/ \
   --with-extra-libs=%{_libdir} \
   --with-extra-includes=%{_includedir}/tqt


# parallel make disabled because otherwise main.cpp can get built before
# profileeditorbase.h is fully generated
%__make
%__make %{?_smp_mflags} -C c_cpp_reference-2.0.2_for_KDE_3.0


%install
%__rm -rf %{buildroot}

%make_install
%make_install -C c_cpp_reference-2.0.2_for_KDE_3.0

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
%{_datadir}/mimelnk/application/*
%{_datadir}/mimelnk/text/*
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
* Sun Sep 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-1
- Initial build for RHEL 6
- Spec file based on Fedora 8 "kdeedu-3.5.3-1"
- Import to GIT
