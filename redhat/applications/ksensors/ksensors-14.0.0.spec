# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# Default version for this component
%define tde_pkg ksensors
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

Name:			trinity-ksensors
Version:		0.7.3
Release:		%{?!preversion:21}%{?preversion:20_%{preversion}}%{?dist}%{?_variant}

Summary:        Trinity Frontend to lm_sensors
Group:          Applications/System
License:        GPLv2+
URL:            http://ksensors.sourceforge.net/

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	desktop-file-utils
BuildRequires:	trinity-tqt3-devel >= 3.5.0
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	gettext

%if 0%{?suse_version}
BuildRequires:	libsensors4-devel
%else
BuildRequires:	lm_sensors-devel
%endif

# Keep archs in sync with lm_sensors
ExcludeArch:    s390 s390x

%description
KSensors is a nice lm-sensors frontend for the K Desktop Environment.
Install the hddtemp package if you wish to monitor hard disk
temperatures with KSensors.


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

# Warning: --enable-final causes FTBFS
%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --disable-final \
  --enable-closure \
  --disable-rpath \
  --enable-gcc-hidden-visibility

%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

# Creates autostart shortcut
%__install -dm 755 $RPM_BUILD_ROOT%{tde_datadir}/autostart
%__ln_s ../applnk/Utilities/ksensors.desktop \
    $RPM_BUILD_ROOT%{tde_datadir}/autostart

%find_lang %{tde_pkg}


%clean
%__rm -rf $RPM_BUILD_ROOT


%post
for f in locolor hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null || :
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null || :
done

%postun
for f in locolor hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null || :
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null || :
done


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING FAQ README TODO
%lang(es) %doc LEEME
%lang(de) %doc LIESMICH
%lang(fr) %doc LISEZMOI
%{tde_bindir}/ksensors
%{tde_datadir}/applnk/Utilities/ksensors.desktop
%{tde_datadir}/apps/ksensors/
%{tde_datadir}/autostart/ksensors.desktop
%{tde_datadir}/icons/hicolor/*/apps/ksensors.png
%{tde_datadir}/icons/locolor/
%{tde_datadir}/sounds/ksensors_alert.wav
%{tde_tdedocdir}/HTML/en/ksensors/


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.7.3-21
- Initial release for TDE 14.0.0

* Sat Jan 19 2013 Francois Andriot <francois.andriot@free.fr> - 0.7.3-20
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.7.3-19p3
- Initial release for TDE 3.5.13.1
