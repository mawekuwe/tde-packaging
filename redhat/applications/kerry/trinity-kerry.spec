# Default version for this component
%define kdecomp kerry
%define version 0.2.1
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
Summary:	a KDE frontend for the Beagle desktop search daemon [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://en.opensuse.org/Kerry

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Source1:	kerry.1.docbook

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	libbeagle-devel >= 0.3.0
#BuildRequires:	docbook-utils
BuildRequires:	docbook2X

%description
Kerry is a Trinity frontend for the Beagle desktop search daemon.

A program for indexing and searching user's data. At the moment, it can index
filesystems, chat logs, mail and data, RSS and other.



%prep
%setup -q -n applications/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}



%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

#%__install -D -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/kerry.1.docbook
#docbook2man %{buildroot}%{_mandir}/man1/kerry.1.docbook

%find_lang %{kdecomp}

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


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%{_datadir}/locale/*/LC_MESSAGES/kcmbeagle.mo
%{_bindir}/beagled-shutdown
%{_bindir}/kerry
%{_libdir}/libkdeinit_kerry.la
%{_libdir}/libkdeinit_kerry.so
%{tde_libdir}/kcm_beagle.la
%{tde_libdir}/kcm_beagle.so
%{tde_libdir}/kerry.la
%{tde_libdir}/kerry.so
%{_datadir}/applications/kde/kcmbeagle.desktop
%{_datadir}/applications/kde/kerry.desktop
%{_datadir}/applnk/.hidden/kcmkerry.desktop
%{_datadir}/apps/kerry/search-running.mng
%{_datadir}/autostart/beagled.desktop
%{_datadir}/autostart/kerry.autostart.desktop
%{_datadir}/icons/hicolor/*/*/*


%Changelog
* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 0.2.1-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
