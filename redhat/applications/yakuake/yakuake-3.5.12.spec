# Default version for this component
%define kdecomp yakuake
%define version 2.8.1
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/kde3


Name:		trinity-%{kdecomp}
Summary:	Yakuake is a Quake-style terminal emulator based on KDE Konsole technology.
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Source0:	%{kdecomp}-3.5.12.tar.gz

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils

%description
Yakuake is a Quake-style terminal emulator based on KDE Konsole technology.

%prep
%setup -q -n applications/%{kdecomp}

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
%make_install


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/*
%{_datadir}/applications/*/*.desktop
%{_datadir}/apps/*/
%{_datadir}/icons/*/*/*/*
%{_datadir}/locale/*/*/*.mo
%{_datadir}/config.kcfg/*.kcfg

%Changelog
* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 2.8.1-2
- Import to GIT

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 2.8.1-1
- Correct macro to install under "/opt", if desired

* Sun Aug 14 2011 Francois Andriot <francois.andriot@free.fr> - 2.8.1-0
- Initial build for RHEL 6.0

