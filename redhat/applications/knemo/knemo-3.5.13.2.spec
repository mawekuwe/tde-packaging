# Default version for this component
%define tde_pkg knemo
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
Summary:		network interfaces monitor for the Trinity systray
Version:		0.4.8
Release:		%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

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

%if 0%{?fedora} >= 18
BuildRequires:	net-tools
%endif


%description
KNemo displays an icon in the systray for every network interface.
Tooltips and an info dialog provide further information about the
interface.  Passive popups inform about interface changes.
A traffic plotter is also integrated.

knemo polls the network interface status every second using the
ifconfig, route and iwconfig tools. 

Homepage: http://extragear.kde.org/apps/knemo/



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
  --enable-rpath

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_appdir} > /dev/null
touch --no-create %{tde_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/crystalsvg || :

%postun
update-desktop-database %{tde_appdir} > /dev/null
touch --no-create %{tde_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/crystalsvg || :


%files
%defattr(-,root,root,-)
%{tde_tdelibdir}/kcm_knemo.la
%{tde_tdelibdir}/kcm_knemo.so
%{tde_tdelibdir}/kded_knemod.la
%{tde_tdelibdir}/kded_knemod.so
%{tde_tdeappdir}/kcm_knemo.desktop
%{tde_datadir}/apps/knemo/eventsrc
%{tde_datadir}/icons/crystalsvg/*/*/*.png
%{tde_datadir}/locale/*/LC_MESSAGES/knemod.mo
%{tde_datadir}/locale/*/LC_MESSAGES/kcm_knemo.mo
%{tde_datadir}/services/kded/knemod.desktop


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 0.4.8-5
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.4.8-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.4.8-3
- Initial release for TDE 3.5.13.1

* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 0.4.8-2
- Rebuild for Fedora 17

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 0.4.8-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
