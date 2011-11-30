# Default version for this component
%define kdecomp ktorrent
%define version 2.2.6
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
Summary:	BitTorrent client for Trinity
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://ktorrent.org

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext


%description
KTorrent is a BitTorrent program for Trinity. Its features include speed capping
(both down and up), integrated searching, UDP tracker support, preview of
certain file types (video and audio) and integration into the KDE Panel
enabling background downloading.
 

%prep
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
    --with-extra-includes=%{_includedir}/tqt


# Not SMP safe !
%__make


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%find_lang %{kdecomp}


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


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%{_bindir}/ktcachecheck
%{_bindir}/ktorrent
%{_bindir}/ktshell
%{_bindir}/kttorinfo
%{_bindir}/ktupnptest
%{_libdir}/libktorrent-2.2.6.so
%{_libdir}/libktorrent.la
%{_libdir}/libktorrent.so
%{tde_libdir}/ktinfowidgetplugin.la
%{tde_libdir}/ktinfowidgetplugin.so
%{tde_libdir}/ktipfilterplugin.la
%{tde_libdir}/ktipfilterplugin.so
%{tde_libdir}/ktlogviewerplugin.la
%{tde_libdir}/ktlogviewerplugin.so
%{tde_libdir}/ktpartfileimportplugin.la
%{tde_libdir}/ktpartfileimportplugin.so
%{tde_libdir}/ktrssfeedplugin.la
%{tde_libdir}/ktrssfeedplugin.so
%{tde_libdir}/ktscanfolderplugin.la
%{tde_libdir}/ktscanfolderplugin.so
%{tde_libdir}/ktschedulerplugin.la
%{tde_libdir}/ktschedulerplugin.so
%{tde_libdir}/ktsearchplugin.la
%{tde_libdir}/ktsearchplugin.so
%{tde_libdir}/ktstatsplugin.la
%{tde_libdir}/ktstatsplugin.so
%{tde_libdir}/ktupnpplugin.la
%{tde_libdir}/ktupnpplugin.so
%{tde_libdir}/ktwebinterfaceplugin.la
%{tde_libdir}/ktwebinterfaceplugin.so
%{_datadir}/applications/kde/ktorrent.desktop
%{_datadir}/apps/ktorrent
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svgz
%{_datadir}/services/*.desktop
%{_datadir}/servicetypes/ktorrentplugin.desktop


%Changelog
* Tue Nov 29 2011 Francois Andriot <francois.andriot@free.fr> - 2.2.6-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
