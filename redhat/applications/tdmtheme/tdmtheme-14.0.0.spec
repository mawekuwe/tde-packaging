# Default version for this component
%define tde_pkg tdmtheme
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
Summary:		theme manager for TDM [Trinity]
Version:		1.2.2
Release:		%{?!preversion:6}%{?preversion:5_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://beta.smileaf.org/projects

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

Obsoletes:		trinity-kdmtheme < %{version}-%{release}
Provides:		trinity-kdmtheme = %{version}-%{release}


%description
kdmtheme is a theme manager for KDM. It provides a TDE Control Module (KCM)
that allows you to easily install, remove and change your KDM themes.



%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
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
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-final \
  --enable-new-ldflags \
  --enable-closure \
  --enable-rpath \
  --enable-gcc-hidden-visibility

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%clean
%__rm -rf %{buildroot}



%files
%defattr(-,root,root,-)
%{tde_tdelibdir}/kcm_tdmtheme.la
%{tde_tdelibdir}/kcm_tdmtheme.so
%{tde_tdeappdir}/tdmtheme.desktop
%{tde_tdedocdir}/HTML/en/tdmtheme/


%post
update-desktop-database %{tde_appdir} &> /dev/null

%postun
update-desktop-database %{tde_appdir} &> /dev/null


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 1.2.2-6
- Initial release for TDE 14.0.0

* Thu Jun 27 2013 Francois Andriot <francois.andriot@free.fr> - 1.2.2-5
- Fix tdmtheme crash. This resolves Bug 1544

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 1.2.2-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 1.2.2-3
- Initial release for TDE 3.5.13.1

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 1.2.2-2
- Rebuilt for Fedora 17
- Removes post and postun
- Removes the 'lintian' stuff from Debian

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 1.2.2-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
