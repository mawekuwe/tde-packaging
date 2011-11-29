# Default version for this component
%define kdecomp wlassistant
%define version 0.5.7
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
Summary:	User friendly KDE frontend for wireless network connection [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://wlassistant.sourceforge.net/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
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
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g"


%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

scons configure \
  prefix=%{_prefix} \
  execprefix=%{_bindir} \
  libdir=%{_libdir} \
  qtdir=${QTDIR} \
  kdedir=%{_prefix} \
  kdeincludes=%{_includedir} \
  qtincludes=${QTINC} \
  kdelibs=%{_libdir} \
  qtlibs=${QTLIB} \
  extraincludes=%{_includedir}:%{_includedir}/tqt:${QTINC}

scons -j4


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
scons install DESTDIR=%{buildroot}

%clean
%__rm -rf %{buildroot}


%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc ChangeLog VERSION
%{_bindir}/wlassistant
%{_datadir}/applnk/Utilities/wlassistant.desktop
%{_datadir}/icons/hicolor/16x16/apps/wlassistant.png
%{_datadir}/icons/hicolor/32x32/apps/wlassistant.png
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/wlassistant.mo
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/wlassistant.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/wlassistant.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/wlassistant.mo
%lang(nb) %{_datadir}/locale/nb/LC_MESSAGES/wlassistant.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/wlassistant.mo
%lang(pt) %{_datadir}/locale/pt_BR/LC_MESSAGES/wlassistant.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/wlassistant.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/wlassistant.mo
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/wlassistant.mo


%Changelog
* Tue Nov 29 2011 Francois Andriot <francois.andriot@free.fr> - 0.5.7-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
