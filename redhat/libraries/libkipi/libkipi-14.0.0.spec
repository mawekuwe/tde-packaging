# Default version for this component
%define tde_pkg libkipi
%define tde_version 14.0.0

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man

%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-%{tde_pkg}
Summary:	library for apps that want to use kipi-plugins (runtime version) [Trinity]

Epoch:		1
Version:	0.1.5
Release:	%{?!preversion:2}%{?preversion:1_%{preversion}}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires: trinity-tqtinterface-devel >= %{tde_version}
BuildRequires: trinity-arts-devel >= 1:1.5.10
BuildRequires: trinity-tdelibs-devel >= %{tde_version}
BuildRequires: desktop-file-utils
%if 0%{?suse_version}
BuildRequires: liblcms-devel
%else
BuildRequires: lcms-devel
%endif
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig
BuildRequires: gettext

# AUTOTOOLS
BuildRequires: automake autoconf libtool
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}ltdl-devel
%endif
%if 0%{?fedora} || 0%{?rhel} >= 5 || 0%{?suse_version} >= 1220
BuildRequires:	libtool-ltdl-devel
%endif

%description
Libkipi is a library
  o that contains common routines and widget used by kipi-plugins
  o to ease implementation of the kipi-plugins interface in an application
    that wants to use kipi-plugins
    
Homepage: http://www.kipi-plugins.org/


%package devel
Group:		Development/Libraries
Summary:	library for apps that want to use kipi-plugins (development version) [Trinity]
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
Libkipi is a library
  o that contains common routines and widget used by kipi-plugins
  o to ease implementation of the kipi-plugins interface in an application
    that wants to use kipi-plugins
    
This package contains development files and documentation for libkipi library.
Homepage: http://www.kipi-plugins.org/


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%post
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig || :

%postun
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig || :

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_libdir}/libkipi.so.0
%{tde_libdir}/libkipi.so.0.1.1
%{tde_datadir}/apps/kipi/
%{tde_datadir}/icons/hicolor/*/apps/kipi.png
%{tde_datadir}/servicetypes/kipiplugin.desktop

%files devel
%defattr(-,root,root,-)
%{tde_libdir}/libkipi.so
%{tde_libdir}/libkipi.la
%{tde_tdeincludedir}/libkipi/
%{tde_libdir}/pkgconfig/libkipi.pc

%Changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.1.5-2
- Initial release for TDE 14.0.0
