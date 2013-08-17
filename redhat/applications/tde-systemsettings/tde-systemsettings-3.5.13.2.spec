# Default version for this component
%define tde_pkg tde-systemsettings
%define tde_version 3.5.13.2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
# Currently, menu files under /etc/xdg conflict with KDE4
%define tde_sysconfdir %{tde_prefix}/etc
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


Name:			trinity-tde-systemsettings
Summary:		easy to use control centre for TDE
Version:		0.0svn20070312
Release:		%{?!preversion:8}%{?preversion:7_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:	kde-settings-laptops.directory

Provides:	trinity-kde-systemsettings = %{version}-%{release}
Obsoletes:	trinity-kde-systemsettings < %{version}-%{release}
Provides:	trinity-systemsettings = %{version}-%{release}
Obsoletes:	trinity-systemsettings < %{version}-%{release}

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

Requires:		trinity-guidance

%description
System preferences is a replacement for the TDE
Control Centre with an improved user interface.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export KDEDIR="%{tde_prefix}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --sysconfdir=%{tde_sysconfdir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-final \
  --enable-new-ldflags \
  --enable-closure \
  --enable-rpath

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%__install -D -m 644 %{SOURCE1} %{buildroot}%{tde_datadir}/desktop-directories/kde-settings-laptops.directory

# Unwanted files
%__rm -f %{buildroot}%{tde_datadir}/applications/kde/kcmfontinst.desktop
%__rm -f %{buildroot}%{tde_datadir}/desktop-directories/kde-settings-power.directory
%__rm -f %{buildroot}%{tde_datadir}/desktop-directories/kde-settings-system.directory

%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/crystalsvg || :
update-desktop-database %{tde_tdeappdir} -q &> /dev/null

%postun
touch --no-create %{tde_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/crystalsvg || :
update-desktop-database %{tde_tdeappdir} -q &> /dev/null

%files
%defattr(-,root,root,-)
%doc README TODO
%{tde_sysconfdir}/xdg/menus/applications-merged/system-settings-merge.menu
%{tde_sysconfdir}/xdg/menus/system-settings.menu
%{tde_bindir}/systemsettings
%{tde_datadir}/applications/kde/audioencoding.desktop
%{tde_datadir}/applications/kde/defaultapplication.desktop
%{tde_datadir}/applications/kde/kcm_knetworkconfmodule_ss.desktop
%{tde_datadir}/applications/kde/laptoppowermanagement.desktop
%{tde_datadir}/applications/kde/medianotifications.desktop
%{tde_datadir}/applications/kde/systemsettings.desktop
%{tde_datadir}/apps/systemsettings/systemsettingsui.rc
%{tde_datadir}/config/systemsettingsrc
%{tde_datadir}/desktop-directories/*.directory
%{tde_datadir}/icons/crystalsvg/*/apps/systemsettings.png



%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 0.0svn20070312-8
- Build for Fedora 19

* Sat Jun 29 2013 Francois Andriot <francois.andriot@free.fr> - 0.0svn20070312-7
- Rebuild

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.0svn20070312-6
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.0svn20070312-5
- Initial release for TDE 3.5.13.1

* Wed Jul 11 2012 Francois Andriot <francois.andriot@free.fr> - 0.0svn20070312-4
- Fix XDG menu directory location (again)

* Sun Jul 08 2012 Francois Andriot <francois.andriot@free.fr> - 0.0svn20070312-3
- Updates 'Requires: trinity-guidance' to reflect package renaming

* Wed Dec 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.0svn20070312-2
- Fix XDG menu directory location

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.0svn20070312-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16

