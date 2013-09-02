# Default version for this component
%define tde_pkg kpilot
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
Summary:		TDE Palm Pilot hot-sync tool
Version:		0.7
Release:		%{?!preversion:7}%{?preversion:6_%{preversion}}%{?dist}%{?_variant}

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
BuildRequires:	pilot-link-devel
BuildRequires:	trinity-tdepim-devel >= %{tde_version}

%description
KPilot is an application that synchronizes your Palm Pilot or similar device
(like the Handspring Visor) with your TDE desktop, much like the Palm HotSync
software does for Windows.  KPilot can back-up and restore your Palm Pilot
and synchronize the built-in applications with their TDE counterparts.


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
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Unwanted files
%__rm -f %{?buildroot}%{tde_libdir}/libkpilot.so



%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_appdir} > /dev/null
for f in hicolor locolor crystalsvg; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done
/sbin/ldconfig || :

%postun
update-desktop-database %{tde_appdir} > /dev/null
for f in hicolor locolor crystalsvg; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done
/sbin/ldconfig || :


%files
%defattr(-,root,root,-)
%{tde_bindir}/kpalmdoc
%{tde_bindir}/kpilot
%{tde_bindir}/kpilotDaemon
%{tde_tdeincludedir}/kpilot
%{tde_libdir}/libkpilot.la
%{tde_libdir}/libkpilot.so.0
%{tde_libdir}/libkpilot.so.0.0.0
%{tde_tdelibdir}/conduit_address.la
%{tde_tdelibdir}/conduit_address.so
%{tde_tdelibdir}/conduit_doc.la
%{tde_tdelibdir}/conduit_doc.so
%{tde_tdelibdir}/conduit_knotes.la
%{tde_tdelibdir}/conduit_knotes.so
%{tde_tdelibdir}/conduit_memofile.la
%{tde_tdelibdir}/conduit_memofile.so
%{tde_tdelibdir}/conduit_notepad.la
%{tde_tdelibdir}/conduit_notepad.so
%{tde_tdelibdir}/conduit_popmail.la
%{tde_tdelibdir}/conduit_popmail.so
%{tde_tdelibdir}/conduit_sysinfo.la
%{tde_tdelibdir}/conduit_sysinfo.so
%{tde_tdelibdir}/conduit_time.la
%{tde_tdelibdir}/conduit_time.so
%{tde_tdelibdir}/conduit_todo.la
%{tde_tdelibdir}/conduit_todo.so
%{tde_tdelibdir}/conduit_vcal.la
%{tde_tdelibdir}/conduit_vcal.so
%{tde_tdelibdir}/kcm_kpilot.la
%{tde_tdelibdir}/kcm_kpilot.so
%{tde_tdeappdir}/kpalmdoc.desktop
%{tde_tdeappdir}/kpilot.desktop
%{tde_tdeappdir}/kpilotdaemon.desktop
%{tde_datadir}/apps/kaddressbook/contacteditorpages/KPilotCustomFieldEditor.ui
%{tde_datadir}/apps/tdeconf_update/kpalmdoc.upd
%{tde_datadir}/apps/tdeconf_update/kpilot.upd
%{tde_datadir}/apps/kpilot
%{tde_datadir}/config.kcfg/*.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/*.png
%{tde_datadir}/icons/hicolor/*/apps/*.png
%{tde_datadir}/icons/locolor/*/apps/*.png
%{tde_datadir}/services/*.desktop
%{tde_datadir}/servicetypes/kpilotconduit.desktop


%changelog
* Mon Jul 29 2013 Francois Andriot <francois.andriot@free.fr> - 0.7-7
- Initial release for TDE 14.0.0
