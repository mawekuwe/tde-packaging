# Default version for this component
%define kdecomp wlassistant

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_tdedocdir}


Name:		trinity-%{kdecomp}
Summary:	User friendly KDE frontend for wireless network connection [Trinity]
Version:	0.5.7
Release:	1%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://wlassistant.sourceforge.net/

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-tdelibs-devel
BuildRequires:	trinity-tdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	python
BuildRequires:	scons

%description
Wireless Assistant scans for wireless access points and displays link quality,
encryption and other useful information. When user wants to connect to a
network, Wireless Assistant opens up its wizards and guides the user through
Wi-Fi settings. After a successful connection is made the settings are
remembered so next time the user won't have to enter them again.


%prep
%setup -q -n applications/%{kdecomp}

# Ugly hack to modify TQT include directory inside SCONS files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i bksys/kde.py \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g"


%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

scons configure \
  prefix=%{tde_prefix} \
  execprefix=%{tde_bindir} \
  libdir=%{tde_libdir} \
  qtdir=${QTDIR} \
  kdedir=%{tde_prefix} \
  kdeincludes=%{tde_tdeincludedir} \
  qtincludes=${QTINC} \
  kdelibs=%{tde_libdir} \
  qtlibs=${QTLIB} \
  extraincludes=%{tde_includedir}:%{tde_includedir}/tqt:${QTINC}

scons -j4


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
scons install DESTDIR=%{buildroot}

%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc ChangeLog VERSION
%{tde_bindir}/wlassistant
%{tde_datadir}/applnk/Utilities/wlassistant.desktop
%{tde_datadir}/icons/hicolor/16x16/apps/wlassistant.png
%{tde_datadir}/icons/hicolor/32x32/apps/wlassistant.png
%lang(ar) %{tde_datadir}/locale/ar/LC_MESSAGES/wlassistant.mo
%lang(ca) %{tde_datadir}/locale/ca/LC_MESSAGES/wlassistant.mo
%lang(es) %{tde_datadir}/locale/es/LC_MESSAGES/wlassistant.mo
%lang(fr) %{tde_datadir}/locale/fr/LC_MESSAGES/wlassistant.mo
%lang(nb) %{tde_datadir}/locale/nb/LC_MESSAGES/wlassistant.mo
%lang(pl) %{tde_datadir}/locale/pl/LC_MESSAGES/wlassistant.mo
%lang(pt) %{tde_datadir}/locale/pt_BR/LC_MESSAGES/wlassistant.mo
%lang(sv) %{tde_datadir}/locale/sv/LC_MESSAGES/wlassistant.mo
%lang(zh_CN) %{tde_datadir}/locale/zh_CN/LC_MESSAGES/wlassistant.mo
%lang(zh_TW) %{tde_datadir}/locale/zh_TW/LC_MESSAGES/wlassistant.mo


%Changelog
* Tue Nov 29 2011 Francois Andriot <francois.andriot@free.fr> - 0.5.7-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
