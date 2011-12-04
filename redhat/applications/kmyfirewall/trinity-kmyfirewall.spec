# Default version for this component
%define kdecomp kmyfirewall
%define version 1.1.1
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	iptables based firewall configuration tool for KDE [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz


BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils


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


%prep
unset QTDIR; . /etc/profile.d/qt.sh
%setup -q -n applications/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g" \
  -e "s,kde_htmldir='.*',kde_htmldir='%{tde_docdir}/HTML',g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt \
    --enable-closure

%__make %{?_smp_mflags}

%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
/sbin/ldconfig || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
/sbin/ldconfig || :


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING COPYING-DOCS README TODO
%{_bindir}/kmyfirewall
%{_libdir}/libkmfcore.so.*
%{_libdir}/libkmfwidgets.so.*
%{tde_libdir}/libkmfcompiler_ipt.la
%{tde_libdir}/libkmfcompiler_ipt.so
%{tde_libdir}/libkmfgenericinterfacepart.la
%{tde_libdir}/libkmfgenericinterfacepart.so
%{tde_libdir}/libkmfinstaller_linux.la
%{tde_libdir}/libkmfinstaller_linux.so
%{tde_libdir}/libkmfinstallerplugin.la
%{tde_libdir}/libkmfinstallerplugin.so
%{tde_libdir}/libkmfipteditorpart.la
%{tde_libdir}/libkmfipteditorpart.so
%{tde_libdir}/libkmfruleoptionedit_custom.la
%{tde_libdir}/libkmfruleoptionedit_custom.so
%{tde_libdir}/libkmfruleoptionedit_interface.la
%{tde_libdir}/libkmfruleoptionedit_interface.so
%{tde_libdir}/libkmfruleoptionedit_ip.la
%{tde_libdir}/libkmfruleoptionedit_ip.so
%{tde_libdir}/libkmfruleoptionedit_limit.la
%{tde_libdir}/libkmfruleoptionedit_limit.so
%{tde_libdir}/libkmfruleoptionedit_mac.la
%{tde_libdir}/libkmfruleoptionedit_mac.so
%{tde_libdir}/libkmfruleoptionedit_protocol.la
%{tde_libdir}/libkmfruleoptionedit_protocol.so
%{tde_libdir}/libkmfruleoptionedit_state.la
%{tde_libdir}/libkmfruleoptionedit_state.so
%{tde_libdir}/libkmfruleoptionedit_tos.la
%{tde_libdir}/libkmfruleoptionedit_tos.so
%{tde_libdir}/libkmfruletargetoptionedit_log.la
%{tde_libdir}/libkmfruletargetoptionedit_log.so
%{tde_libdir}/libkmfruletargetoptionedit_mark.la
%{tde_libdir}/libkmfruletargetoptionedit_mark.so
%{tde_libdir}/libkmfruletargetoptionedit_nat.la
%{tde_libdir}/libkmfruletargetoptionedit_nat.so
%{tde_libdir}/libkmfruletargetoptionedit_tos.la
%{tde_libdir}/libkmfruletargetoptionedit_tos.so
%{_datadir}/applications/kde/kmyfirewall.desktop
%{_datadir}/apps/kmfgenericinterfacepart/kmfgenericinterfacepartui.rc
%{_datadir}/apps/kmfipteditorpart/kmfipteditorpartui.rc
%{_datadir}/apps/kmfsystray
%{_datadir}/apps/kmyfirewall
%{_datadir}/config.kcfg/kmfconfig.kcfg
%{_datadir}/config/kmyfirewallrc
%{tde_docdir}/HTML/en/kmyfirewall/common
%{tde_docdir}/HTML/en/kmyfirewall/index.cache.bz2
%{tde_docdir}/HTML/en/kmyfirewall/index.docbook
%{_datadir}/icons/*/*/apps/kmyfirewall.png
%{_datadir}/mimelnk/application/kmfgrs.desktop
%{_datadir}/mimelnk/application/kmfnet.desktop
%{_datadir}/mimelnk/application/kmfpkg.desktop
%{_datadir}/mimelnk/application/kmfrs.desktop
%{_datadir}/services/kmf*.desktop
%{_datadir}/servicetypes/kmf*.desktop

%files devel
%{_includedir}/kmyfirewall
%{_libdir}/libkmfcore.la
%{_libdir}/libkmfcore.so
%{_libdir}/libkmfwidgets.la
%{_libdir}/libkmfwidgets.so

%Changelog
* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 1.0-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

