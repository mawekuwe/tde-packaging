# Default version for this component
%define kdecomp kvpnc
%define version 0.9.6a
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
Summary:	vpn clients frontend for TDE
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-master.tar.gz
Source1:	admin-master.tar.gz

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils

%description
KVpnc is a TDE frontend for various vpn clients.

It supports :
 * Cisco-compatible VPN client (vpnc)
 * IPSec (freeswan, openswan, racoon)
 * Point-to-Point Tunneling Protocol (PPTP) client (pptp-linux)
 * Virtual Private Network daemon (openvpn)


%prep
unset QTDIR; . /etc/profile.d/qt.sh
%setup -q -n %{kdecomp}-master

# 'admin' folder from GIT
%setup -q -n %{kdecomp}-master -a 1
%__rm -rf admin
%__mv -f admin-master admin

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
%doc AUTHORS ChangeLog COPYING README TODO



%Changelog
* Sat Dec 10 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.6a-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

