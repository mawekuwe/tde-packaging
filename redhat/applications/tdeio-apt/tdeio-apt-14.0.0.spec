# Default version for this component
%define tde_pkg tdeio-apt
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
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		An apt-cache ioslave for Trinity
Version:		0.13.2
Release:		%{?!preversion:2}%{?preversion:1_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://lpnotfr.free.fr/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils


%description
tdeio-apt is an ioslave which provides the apt:/ protocol. It
integrates apt-cache functionalities into Konqueror, making
browsing the packages easier. It provides:
 - apt-cache search: apt:/search?expression
 - apt-cache show: apt:/show?package . The show? target
   prints the policy too.
 - apt-cache policy: apt:/policy?package


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
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --disable-rpath \
  --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang kio-apt


%clean
%__rm -rf %{buildroot}


%files -f kio-apt.lang
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG ChangeLog COPYING
%{tde_tdelibdir}/tdeio_apt.la
%{tde_tdelibdir}/tdeio_apt.so
%{tde_datadir}/apps/tdeio_apt/kdedeb_logo.png
%{tde_datadir}/apps/tdeio_apt/tdeio_apt.css
%{tde_datadir}/services/apt+http.protocol
%{tde_datadir}/services/apt.protocol
%{tde_datadir}/services/searchproviders/apt-file.desktop
%{tde_datadir}/services/searchproviders/apt-files.desktop
%{tde_datadir}/services/searchproviders/apt-search.desktop


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.13.2-2
- Initial release for TDE 14.0.0

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.13.2-1
- Initial release for TDE 3.5.13.2

