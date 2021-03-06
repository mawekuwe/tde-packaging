# Default version for this component
%define tde_pkg kmyfirewall
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
Summary:		iptables based firewall configuration tool for TDE [Trinity]
Version:		1.1.1
Release:		%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils


%description
KMyFirewall attempts to make it easier to setup iptables based firewalls on
Linux systems. It will be the right tool if you like to have a so called
"Personal Firewall" running on your Linux box, but don't have the time and/or
the interest to spend hours in front of the iptables manual just to setup a 
Firewall that keeps the "bad" people out.

There is also the possibility to save entire rule sets, so you only have to
configure your rule set one time and then you can use it on several computers
giving each of them a similar configuration (p.e. school networks, office,
university etc.)

%package devel
Summary:		Development files for %{name}
Group:			Development/Libraries
Requires:		%{name} = %{version}-%{release}

%description devel
%{summary}


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
for f in hicolor locolor; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done
/sbin/ldconfig || :

%postun
update-desktop-database %{tde_appdir} > /dev/null
for f in hicolor locolor; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done
/sbin/ldconfig || :


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING COPYING-DOCS README TODO
%{tde_bindir}/kmyfirewall
%{tde_libdir}/libkmfcore.so.*
%{tde_libdir}/libkmfwidgets.so.*
%{tde_tdelibdir}/libkmfcompiler_ipt.la
%{tde_tdelibdir}/libkmfcompiler_ipt.so
%{tde_tdelibdir}/libkmfgenericinterfacepart.la
%{tde_tdelibdir}/libkmfgenericinterfacepart.so
%{tde_tdelibdir}/libkmfinstaller_linux.la
%{tde_tdelibdir}/libkmfinstaller_linux.so
%{tde_tdelibdir}/libkmfinstallerplugin.la
%{tde_tdelibdir}/libkmfinstallerplugin.so
%{tde_tdelibdir}/libkmfipteditorpart.la
%{tde_tdelibdir}/libkmfipteditorpart.so
%{tde_tdelibdir}/libkmfruleoptionedit_custom.la
%{tde_tdelibdir}/libkmfruleoptionedit_custom.so
%{tde_tdelibdir}/libkmfruleoptionedit_interface.la
%{tde_tdelibdir}/libkmfruleoptionedit_interface.so
%{tde_tdelibdir}/libkmfruleoptionedit_ip.la
%{tde_tdelibdir}/libkmfruleoptionedit_ip.so
%{tde_tdelibdir}/libkmfruleoptionedit_limit.la
%{tde_tdelibdir}/libkmfruleoptionedit_limit.so
%{tde_tdelibdir}/libkmfruleoptionedit_mac.la
%{tde_tdelibdir}/libkmfruleoptionedit_mac.so
%{tde_tdelibdir}/libkmfruleoptionedit_protocol.la
%{tde_tdelibdir}/libkmfruleoptionedit_protocol.so
%{tde_tdelibdir}/libkmfruleoptionedit_state.la
%{tde_tdelibdir}/libkmfruleoptionedit_state.so
%{tde_tdelibdir}/libkmfruleoptionedit_tos.la
%{tde_tdelibdir}/libkmfruleoptionedit_tos.so
%{tde_tdelibdir}/libkmfruletargetoptionedit_log.la
%{tde_tdelibdir}/libkmfruletargetoptionedit_log.so
%{tde_tdelibdir}/libkmfruletargetoptionedit_mark.la
%{tde_tdelibdir}/libkmfruletargetoptionedit_mark.so
%{tde_tdelibdir}/libkmfruletargetoptionedit_nat.la
%{tde_tdelibdir}/libkmfruletargetoptionedit_nat.so
%{tde_tdelibdir}/libkmfruletargetoptionedit_tos.la
%{tde_tdelibdir}/libkmfruletargetoptionedit_tos.so
%{tde_tdeappdir}/kmyfirewall.desktop
%{tde_datadir}/apps/kmfgenericinterfacepart/kmfgenericinterfacepartui.rc
%{tde_datadir}/apps/kmfipteditorpart/kmfipteditorpartui.rc
%{tde_datadir}/apps/kmfsystray
%{tde_datadir}/apps/kmyfirewall
%{tde_datadir}/config.kcfg/kmfconfig.kcfg
%{tde_datadir}/config/kmyfirewallrc
%{tde_tdedocdir}/HTML/en/kmyfirewall/
%{tde_datadir}/icons/hicolor/*/apps/kmyfirewall.png
%{tde_datadir}/icons/locolor/*/apps/kmyfirewall.png
%{tde_datadir}/mimelnk/application/kmfgrs.desktop
%{tde_datadir}/mimelnk/application/kmfnet.desktop
%{tde_datadir}/mimelnk/application/kmfpkg.desktop
%{tde_datadir}/mimelnk/application/kmfrs.desktop
%{tde_datadir}/services/kmf*.desktop
%{tde_datadir}/servicetypes/kmf*.desktop

%files devel
%{tde_tdeincludedir}/kmyfirewall
%{tde_libdir}/libkmfcore.la
%{tde_libdir}/libkmfcore.so
%{tde_libdir}/libkmfwidgets.la
%{tde_libdir}/libkmfwidgets.so

%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1.1.1-5
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 1.1.1-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 1.1.1-3
- Initial release for TDE 3.5.13.1

* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 1.1.1-2
- GCC 4.7 fixes. [Commit #88d2d2a7]

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 1.1.1-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16

