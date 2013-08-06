# Default version for this component
%define tde_pkg kuickshow
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
Summary:		Quick picture viewer for TDE 
Version:		0.8.13
Release:		%{?!preversion:8}%{?preversion:7_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

%if 0%{?rhel} || 0%{?fedora} || 0%{?mdkversion}
BuildRequires:	imlib-devel
%endif
%if 0%{?suse_version} || 0%{?mgaversion}
BuildRequires:	imlib1-devel
%endif

%description
Kuickshow is a picture viewer for TDE. It displays the directory structure,
displaying images as thumbnails.
Clicking on an image shows the image in its normal size. 


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
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
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
%__make install DESTDIR=%{?buildroot}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
/sbin/ldconfig

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/kuickshow
%{tde_datadir}/applications/*/*.desktop
%{tde_datadir}/apps/kuickshow/
%{tde_datadir}/icons/hicolor/*/*/*
%{tde_libdir}/libtdeinit_%{tde_pkg}.so
%{tde_libdir}/*.la
%{tde_tdelibdir}/*.so
%{tde_tdelibdir}/*.la
%{tde_tdedocdir}/HTML/en/kuickshow/


%changelog
* Mon Jul 29 2013 Francois Andriot <francois.andriot@free.fr> - 0.8.13-8
- Initial release for TDE 14.0.0

* Sun Jul 28 2013 Francois Andriot <francois.andriot@free.fr> - 0.8.13-7
- Rebuild with NDEBUG option

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.8.13-6
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.13-5
- Initial release for TDE 3.5.13.1

* Mon Jul 09 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.13-3
- Removes conflict with 'kdegraphics'

* Sat May 05 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.13-3
- Rename old tq methods that no longer need a unique name [Commit #8712ab46]
- Remove additional unneeded tq method conversions [Commit #28d9c774]
- Rename obsolete tq methods to standard names [Commit #bdeb8b3a]
- Remove inadvertent renaming [Commit #d97e403f] [Bug #863]

* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.13-2
- Import to GIT

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.13-1
- Correct macro to install under "/opt", if desired

* Sat Aug 13 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.13-0
- Initial release for RHEL 6.0

