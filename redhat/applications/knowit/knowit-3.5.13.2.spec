# Default version for this component
%define tde_pkg knowit
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
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		Tool for managing notes [Trinity]
Version:		0.10
Release:		%{?!preversion:4}%{?preversion:3_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext


%description
KnowIt is a tool for managing notes which are organized in
tree-like hierarchy. It is similar to TuxCards,
but TDE-based, and requires Trinity.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

# Warning: --enable-final causes FTBFS
%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --disable-final \
  --enable-closure \
  --enable-rpath

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%__mkdir_p %{buildroot}%{tde_tdeappdir}
%__mv %{buildroot}%{tde_datadir}/applnk/Applications/knowit.desktop %{buildroot}%{tde_tdeappdir}/knowit.desktop
%__rm -r %{buildroot}%{tde_datadir}/applnk


%find_lang %{tde_pkg}



%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_appdir} > /dev/null
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
update-desktop-database %{tde_appdir} > /dev/null
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/knowit
%{tde_tdeappdir}/knowit.desktop
%{tde_datadir}/apps/knowit/knowitui.rc
%{tde_datadir}/apps/knowit/tips
%{tde_tdedocdir}/HTML/en/knowit/common
%{tde_tdedocdir}/HTML/en/knowit/index.cache.bz2
%{tde_tdedocdir}/HTML/en/knowit/index.docbook
%{tde_tdedocdir}/HTML/en/knowit/screenshot.png
%{tde_datadir}/icons/hicolor/*/apps/knowit.png


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 0.10-4
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.10-3
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.10-2
- Initial release for TDE 3.5.13.1

* Wed Nov 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.10-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
