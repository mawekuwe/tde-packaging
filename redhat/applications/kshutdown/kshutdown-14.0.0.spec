# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# Default version for this component
%define tde_pkg kshutdown
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

Name:           trinity-%{tde_pkg}
Version:        1.0.4
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:        An advanced shut down utility for TDE

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://kde-apps.org/content/show.php?content=41180
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:	trinity-tqt3-devel >= 3.5.0
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

%description
It has 4 main commands:

- Shut Down (logout and halt the system),
- Reboot (logout and reboot the system),
- Lock Screen (lock the screen using a screen saver),
- Logout (end the session and logout the user).

It features time and delay options, command line support, wizard,
and sounds.


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
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --htmldir=%{tde_tdedocdir}/HTML \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-final \
  --enable-new-ldflags \
  --enable-closure \
  --disable-rpath \
  --enable-gcc-hidden-visibility

%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{tde_pkg}


%clean
%__rm -rf $RPM_BUILD_ROOT

%post
update-desktop-database %{tde_datadir}/applications -q &> /dev/null
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done

%postun
update-desktop-database %{tde_datadir}/applications -q &> /dev/null
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{tde_bindir}/kshutdown
%{tde_tdelibdir}/kshutdownlockout_panelapplet.la
%{tde_tdelibdir}/kshutdownlockout_panelapplet.so
%{tde_datadir}/applications/kshutdown.desktop
%{tde_datadir}/apps/kicker/applets/kshutdownlockout.desktop
%{tde_datadir}/apps/kshutdown/
%{tde_datadir}/apps/tdeconf_update/kshutdown.upd
%{tde_datadir}/icons/hicolor/*/apps/kshutdown.png
%lang(de) %{tde_datadir}/doc/tde/HTML/de/kshutdown/
%lang(en) %{tde_datadir}/doc/tde/HTML/en/kshutdown/



%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 1.0.4-1
- Initial release for TDE 14.0.0

