# Default version for this component
%define kdecomp kopete-otr
%define version 0.7
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
Summary:	Off-The-Record encryption for Kopete [Trinity]
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

# Kopete is provided by kdenetwork
BuildRequires:	trinity-kdenetwork-devel
Requires:		trinity-kdenetwork
BuildRequires:	libotr-devel

%description
This plugin enables Off-The-Record encryption for the KDE instant
messenger Kopete. Using this plugin you can encrypt chatsessions to other
users with IM-Cients supporting the OTR encryption method.


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
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/libkotr.la
%{_libdir}/libkotr.so
%{_libdir}/libkotr.so.0
%{_libdir}/libkotr.so.0.0.0
%{tde_libdir}/kcm_kopete_otr.la
%{tde_libdir}/kcm_kopete_otr.so
%{tde_libdir}/kopete_otr.la
%{tde_libdir}/kopete_otr.so
%{_datadir}/apps/kopete_otr
%{_datadir}/config.kcfg/kopete_otr.kcfg
%{tde_docdir}/HTML/en/kopete_otr/common
%{tde_docdir}/HTML/en/kopete_otr/index.cache.bz2
%{tde_docdir}/HTML/en/kopete_otr/index.docbook
%{_datadir}/icons/crystalsvg/16x16/apps/kopete_otr.png
%{_datadir}/locale/de/LC_MESSAGES/kopete_otr.mo
%{_datadir}/services/kconfiguredialog/kopete_otr_config.desktop
%{_datadir}/services/kopete_otr.desktop


%Changelog
* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.7-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

