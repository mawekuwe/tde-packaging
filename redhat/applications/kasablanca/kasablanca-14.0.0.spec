# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# Default version for this component
%define tde_pkg kasablanca
%define tde_version 14.0.0

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man

%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		Graphical FTP client
Version:		0.4.0.2
Release:		%{?!preversion:4}%{?preversion:3_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Url:			http://kasablanca.berlios.de/ 
Group:			Applications/Internet 
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:	trinity-tqt3-devel >= 3.5.0
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	gettext 
BuildRequires:	openssl-devel

%if 0%{?suse_version}
BuildRequires:	utempter-devel
%else
%if 0%{?rhel} == 4
%else
BuildRequires:	libutempter-devel
%endif
%endif

%description
Kasablanca is an ftp client, among its features are currently: 
* ftps encryption via AUTH TLS
* fxp (direct server to server transfer), supporting alternative mode.
* advanced bookmarking system.
* fast responsive multithreaded engine.
* concurrent connections to multiple hosts.
* interactive transfer queue, movable by drag and drop.
* small nifty features, like a skiplist.


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

## Needed(?) for older/legacy setups, harmless otherwise
if pkg-config openssl ; then
	export CPPFLAGS="$CPPFLAGS $(pkg-config --cflags-only-I openssl)"
fi

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --includedir=%{tde_tdeincludedir} \
  --datadir=%{tde_datadir} \
  --disable-static \
  --disable-rpath \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final \
  --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf $RPM_BUILD_ROOT 
%__make install DESTDIR=$RPM_BUILD_ROOT

# locale's
%find_lang %{tde_pkg}


%clean
%__rm -rf $RPM_BUILD_ROOT 


%post
touch --no-create %{tde_datadir}/icons/hicolor &> /dev/null || :


%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &> /dev/null
  gtk-update-icon-cache %{tde_datadir}/icons/hicolor &> /dev/null || :
fi


%posttrans
gtk-update-icon-cache %{tde_datadir}/icons/hicolor &> /dev/null || :


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README 
%{tde_bindir}/kasablanca
%{tde_datadir}/apps/kasablanca/
%{tde_datadir}/config.kcfg/kbconfig.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kasablanca.png
%{tde_tdedocdir}/HTML/en/kasablanca/
%{tde_datadir}/applnk/Utilities/kasablanca.desktop


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.4.0.2-4
- Initial release for TDE 14.0.0

* Sat Jan 19 2013 Francois Andriot <francois.andriot@free.fr> - 0.4.0.2-3
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.4.0.2-2
- Initial release for TDE 3.5.13.1

* Sun Dec 04 2011 Francois Andriot <francois.andriot@free.fr> - 0.4.0.2-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
- Based on Fedora 12 Spec 'kasablanca-0.4.0.2-17'
