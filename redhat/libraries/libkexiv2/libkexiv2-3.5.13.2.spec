# Default version for this component
%define tde_pkg libkexiv2
%define tde_version 3.5.13.2

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

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-%{tde_pkg}
Summary:	Qt like interface for the libexiv2 library (runtime) [Trinity]

Epoch:		1
Version:	0.1.7
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

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
BuildRequires: gettext

# AUTOTOOLS
BuildRequires: automake autoconf libtool
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}ltdl-devel
%endif
%if 0%{?fedora} || 0%{?rhel} >= 5 || 0%{?suse_version} >= 1220
BuildRequires:	libtool-ltdl-devel
%endif

# EXIV2
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}exiv2-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	exiv2-devel
%endif
%if 0%{?suse_version}
BuildRequires:	libexiv2-devel
%endif

%description
libkexif2 contains the library of libkexiv2.
Libkexif is a wrapper around Exiv2 library to manipulate pictures metadata.

%package devel
Group:		Development/Libraries
Summary:	Qt like interface for the libexiv2 library (development) [Trinity]
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
libkexif2-devel contains development files and documentation for libkexiv2
library.  The library documentation is available on kexiv2.h header file.
Libkexif is a wrapper around Exiv2 library to manipulate pictures metadata.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; source /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --libdir=%{tde_libdir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# RHEL4: pkgconfig files do not support 'URL' keyword .
%if 0%{?rhel} == 4
%__sed -i %{?buildroot}%{tde_libdir}/pkgconfig/*.pc -e "s/^URL: /#URL: /"
%endif


%clean
%__rm -rf %{buildroot}


%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :


%files
%defattr(-,root,root,-)
%{tde_libdir}/libkexiv2.so.*

%files devel
%defattr(-,root,root,-)
%{tde_libdir}/libkexiv2.so
%{tde_libdir}/libkexiv2.la
%{tde_tdeincludedir}/libkexiv2/
%{tde_libdir}/pkgconfig/libkexiv2.pc


%Changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 0.1.7-1
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2
