# Default version for this component
%define tde_pkg kiosktool
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
Version:		1.0
Release:		%{?!preversion:6}%{?preversion:5_%{preversion}}%{?dist}%{?_variant}
Summary:		tool to configure the TDE kiosk framework

License:		GPLv2+
Group:			Applications/Multimedia

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/


Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext


%description
A Point&Click tool for system administrators to enable 
TDE's KIOSK features or otherwise preconfigure TDE for 
groups of users.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; source /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"

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
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{tde_pkg}


%clean
%__rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{tde_datadir}/icons/crystalsvg ||:
gtk-update-icon-cache -q %{tde_datadir}/icons/crystalsvg 2> /dev/null ||:
update-desktop-database >& /dev/null ||:

%postun
touch --no-create %{tde_datadir}/icons/crystalsvg ||:
gtk-update-icon-cache -q %{tde_datadir}/icons/crystalsvg 2> /dev/null ||:
update-desktop-database >& /dev/null ||:



%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc ChangeLog COPYING README TODO
%{tde_bindir}/kiosktool
%{tde_bindir}/kiosktool-kdedirs
%{tde_tdeappdir}/kiosktool.desktop
%{tde_datadir}/apps/kiosktool/*.png
%{tde_tdedocdir}/HTML/en/kiosktool/
%{tde_datadir}/icons/crystalsvg/*/apps/kiosktool.png
%{tde_datadir}/apps/kiosktool/kiosk_data.xml
%{tde_datadir}/apps/kiosktool/kiosktoolui.rc

%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-6
- Build for Fedora 19

* Sun Jul 28 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-5
- Rebuild with NDEBUG option

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 1.0-3
- Initial release for TDE 3.5.13.1

* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 1.0-2
- Rebuilt for Fedora 17
- Fix post and postun

* Sat Nov 19 2011 Francois Andriot <francois.andriot@free.fr> - 1.0-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
