# Default version for this component
%define tde_pkg kkbswitch
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

%define _docdir %{tde_tdedocdir}


Name:			trinity-%{tde_pkg}
Summary:		keyboard layout indicator for TDE
Version:		1.4.3
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

Patch0:			kkbswitch-14.0.0-ftbfs.patch

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils


%description
KKBSwitch displays an icon in the system tray that indicates which layout is 
currently active and enables you to switch layouts by clicking the icon or by 
selecting from the menu. It works with all desktop environments.

Features include:
- Configurable icons for the keyboard layouts.
- The "toggle mode" to toggle between the two most recently-used keyboard 
  layouts.
- Choose to use a global layout or per-application or per-window layouts.
- Configurable keyboard shortcuts.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
%patch0 -p1 -b .ftbfs

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

# Warning: --enable-final causes FTBFS !
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
  --disable-final \
  --enable-new-ldflags \
  --enable-closure \
  --enable-rpath \
  --enable-gcc-hidden-visibility

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog README TODO
%{tde_bindir}/kkbswitch
%{tde_datadir}/applnk/Utilities/kkbswitch.desktop
%{tde_datadir}/apps/kkbswitch/group_names
%{tde_datadir}/apps/tdeconf_update/kkbswitch.upd
%{tde_datadir}/apps/tdeconf_update/kkbswitch_update_14_icons
%{tde_datadir}/apps/tdeconf_update/kkbswitch_update_14_options
%{tde_datadir}/autostart/kkbswitch.desktop
%{tde_tdedocdir}/HTML/en/kkbswitch/
%{tde_mandir}/man1/kkbswitch.1


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 1.4.3-1
- Initial release for TDE 14.0.0
