# Default version for this component
%define kdecomp katapult
%define version 0.3.2.1
%define release 1

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
Summary:	Faster access to applications, bookmarks, and other items.
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Source0:	%{kdecomp}-3.5.12.tar.gz
Patch0:		katapult-0.3.2.1_to_0.3.2.2.patch

# TQt4 port Katapult. This enables compilation under both Qt3 and Qt4.
Patch1:		r1233929.diff


BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils

%description
Katapult is an application for KDE, designed to allow faster access to
applications, bookmarks, and other items. It is plugin-based, so it can
launch anything that is has a plugin for. Its display is driven by
plugins as well, so its appearance is completely customizable. It was
inspired by Quicksilver for OS X. 


%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1
#patch1 -p2

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

export CXXFLAGS="-DTQ_OBJECT=//"

chmod +x ./configure

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
/sbin/ldconfig

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
/sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/*
%{_datadir}/applications/*/*.desktop
%{_datadir}/icons/*/*/*/*
%{_datadir}/locale/*/*/*.mo
%{_datadir}/services/*.desktop
%{_datadir}/servicetypes/*.desktop
%{tde_libdir}/*.so
%{_libdir}/*.so.*
%{tde_docdir}/HTML/en/katapult


%exclude %{tde_libdir}/*.la
%exclude %{_libdir}/*.so
%exclude %{_libdir}/*.la

%Changelog
* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.3.2.1-1
- Initial release for RHEL 6.0
- Import to GIT

