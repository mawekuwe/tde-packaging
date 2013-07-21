# Default version for this component
%define kdecomp kuickshow
%define version 0.8.13
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{tde_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_includedir %{tde_includedir}/kde
%define tde_libdir %{tde_libdir}/kde3


Name:		trinity-%{kdecomp}
Summary:	Quick picture viewer for KDE 
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Source0:	%{kdecomp}-3.5.12.tar.gz

Conflicts:	trinity-kdegraphics

BuildRequires: tqtinterface-devel
BuildRequires: trinity-tdelibs-devel
BuildRequires: trinity-tdebase-devel
BuildRequires: desktop-file-utils
BuildRequires: imlib-devel

%description
Kuickshow is a picture viewer for KDE. It displays the directory structure,
displaying images as thumbnails.
Clicking on an image shows the image in its normal size. 


%prep
%setup -q -n applications/%{kdecomp}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{tde_includedir}/tqt \
    --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%make_install


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
%doc AUTHORS COPYING
%{tde_bindir}/*
%{tde_datadir}/applications/*/*.desktop
%{tde_datadir}/apps/*/
%{tde_tdedocdir}/HTML/en/*/
%{tde_datadir}/icons/*/*/*/*
%{tde_libdir}/libkdeinit_%{kdecomp}.so

%exclude %{tde_libdir}/*.la
%exclude %{tde_libdir}/*/*.so
%exclude %{tde_libdir}/*/*.la


%Changelog
* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.13-2
- Import to GIT

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.13-1
- Correct macro to install under "/opt", if desired

* Sat Aug 13 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.13-0
- Initial release for RHEL 6.0

