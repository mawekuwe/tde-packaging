# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:    trinity-tdevelop
Summary: Integrated Development Environment for C++/C
Version: 3.5.13
Release: 5%{?dist}%{?_variant}

License:	GPLv2
Group:		Development/Tools

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source: kdevelop-%{version}.tar.gz
Source1: ftp://129.187.206.68/pub/unix/ide/KDevelop/c_cpp_reference-2.0.2_for_KDE_3.0.tar.bz2

# [c_cpp_ref] Fix library directories detection
Patch1: c_cpp_reference-2.0.2-config.patch

# [kdevelop] fix FTBFS
Patch2: kdevelop-3.5.13-kdevdesigner-ftbfs.patch

# [kdevelop] Fix compilation with GCC 4.7 [Bug #958]
Patch3: kdevelop-3.5.13-gcc47.patch

# [c_cpp_ref] Fix installation of 'asm' files
Patch4:	c_cpp_reference-2.0.2-install.patch

Requires: %{name}-libs = %{version}-%{release}


Requires: make
Requires: perl
Requires: flex >= 2.5.4
%if 0%{?rhel} || 0%{?fedora}
Requires:	qt3-designer >= 3.3.8.d
%else
Requires:	%{_lib}qt3-devel >= 3.3.8.d
%endif
Requires: gettext
Requires: ctags

BuildRequires: cmake >= 2.8
BuildRequires: tqtinterface-devel >= 3.5.13
BuildRequires: trinity-arts-devel >= 3.5.13
BuildRequires: trinity-tdelibs-devel >= 3.5.13
#BuildRequires: qt3-devel-docs >= 3.3.8.d
%if 0%{?mgaversion} || 0%{?mdkversion}
#BuildRequires:	%{_lib}db5.1-devel
%else
BuildRequires: db4-devel
%endif
BuildRequires: flex
# FIXME: No CVS support in KDevelop? This is going to suck...
# Requires kdesdk3.
BuildRequires:	trinity-tdesdk-devel >= 3.5.13
BuildRequires:	subversion-devel
BuildRequires:	neon-devel
# looks like this is dragged in by apr-devel (dep of subversion-devel), but not
# a dependency
BuildRequires:	openldap-devel

Obsoletes:	trinity-kdevelop < %{version}-%{release}
Provides:	trinity-kdevelop = %{version}-%{release}

%description
The TDevelop Integrated Development Environment provides many features
that developers need as well as providing a unified interface to programs
like gdb, the C/C++ compiler, and make. TDevelop manages or provides:

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

%files
%defattr(-,root,root,-)
%{tde_bindir}/*
%{tde_tdelibdir}/*
%{tde_libdir}/kconf_update_bin/*
%{tde_tdeappdir}/*
%{tde_datadir}/apps/*
%{tde_datadir}/config/*
%{tde_datadir}/desktop-directories/*
%{tde_datadir}/icons/hicolor/*/*/*
%{tde_datadir}/icons/locolor/*/*/*
%{tde_datadir}/mimelnk/*.desktop
%{tde_datadir}/mimelnk/*/*
%{tde_datadir}/services/*
%{tde_datadir}/servicetypes/*
%{tde_tdedocdir}/HTML/en/*

%post
for f in hicolor locolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun
for f in hicolor locolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name}-libs = %{version}-%{release}

Obsoletes:	trinity-kdevelop-devel < %{version}-%{release}
Provides:	trinity-kdevelop-devel = %{version}-%{release}

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{tde_libdir}/lib*.so
%{tde_libdir}/lib*.la
%{tde_includedir}/*

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

##########

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-kdelibs
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{version}-%{release}

Obsoletes:	trinity-kdevelop-libs < %{version}-%{release}
Provides:	trinity-kdevelop-libs = %{version}-%{release}

%description libs
%{summary}.

%files libs
%defattr(-,root,root,-)
%{tde_libdir}/lib*.so.*

%post libs
/sbin/ldconfig || :

%postun libs
/sbin/ldconfig || :

##########

%prep
%setup -q -n kdevelop -a1
%patch1 -p0 -b .config
%patch2 -p1
%patch3 -p1 -b .gcc47
%patch4 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i "admin/acinclude.m4.in" \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"

%__rm -rf c_cpp_reference-2.0.2_for_KDE_3.0/admin
%__cp -ar admin c_cpp_reference-2.0.2_for_KDE_3.0/
%__make -C c_cpp_reference-2.0.2_for_KDE_3.0 -f admin/Makefile.common cvs


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{tde_includedir}:%{tde_includedir}/tqt"
export LD_LIBRARY_PATH="%{tde_libdir}"

# c references
pushd c_cpp_reference-2.0.2_for_KDE_3.0
%configure \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --with-qt-libraries=${QTLIB} \
  --with-qt-includes=${QTINC} \
  --with-extra-libs=%{tde_libdir}
popd

%if 0%{?rhel} || 0%{?fedora}
%__mkdir_p build
cd build
%endif

%cmake \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DCMAKE_SKIP_RPATH="OFF" \
  -DWITH_BUILDTOOL_ALL=ON \
  -DWITH_LANGUAGE_ALL=ON \
  -DWITH_VCS_ALL=OFF \
  -DBUILD_ALL=ON \
  ..
  

%__make %{?_smp_mflags} VERBOSE=1

# c references
cd ..
%__make %{?_smp_mflags} -C c_cpp_reference-2.0.2_for_KDE_3.0

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build
%__make install DESTDIR=%{buildroot} -C c_cpp_reference-2.0.2_for_KDE_3.0

# remove useless files
#%__rm -rf %{buildroot}%{tde_prefix}/kdevbdb


%clean
%__rm -rf %{buildroot}


%changelog
* Wed Aug 01 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-5
- Renames to 'trinity-tdevelop'
- Add support for Mageia 2

* Sun Jul 08 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Removes runtime dependency to 'trinity-kdelibs'

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Fix installation on Fedora 17
- Fix compilation on GCC 4.7

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Fix HTML directory location

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sat Oct 29 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
- Based on SPEC file from Fedora: kdevelop 9:3.5.3-1
