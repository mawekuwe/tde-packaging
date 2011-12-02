# Default version for this component
%define kdecomp kdesvn
%define version 1.0.4
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%define _mandir %{_prefix}/share/man
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity

Name:		trinity-%{kdecomp}
Summary:	subversion client with tight KDE integration [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.elliptique.net/~ken/kima/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	subversion-devel
Requires:		trinity-kdesvn-kio-plugins = %{version}-%{release}


%description
KDESvn is a graphical client for the subversion revision control
system (svn).

Besides offering common and advanced svn operations, it features
a tight integration into KDE and can be embedded into other KDE 
applications like konqueror via the KDE component technology KParts.


%package -n trinity-libsvnqt
Group:		Development/Libraries
Summary: Qt wrapper library for subversion [Trinity]

%description -n trinity-libsvnqt
This package provides svnqt, a Qt wrapper library around the 
subversion library.

It is based on the RapidSvn SvnCpp library, a subversion client API 
written in C++.

%package -n trinity-libsvnqt-devel
Group:		Development/Libraries
Requires:	trinity-libsvnqt = %{version}-%{release}
Requires:	qt-devel
Requires:	subversion-devel
Summary:	Qt wrapper library for subversion (development files) [Trinity]

%description -n trinity-libsvnqt-devel
This package contains the header files and symbolic links that developers
using svnqt will need.


%package kio-plugins
Group:		Development/Libraries
Conflicts:	trinity-kdesdk-kio-plugins
Summary:	subversion I/O slaves for Trinity

%description kio-plugins
This packages includes KIO slaves for svn, svn+file, svn+http, 
svn+https, svn+ssh. This allows you to access subversion repositories 
inside any KIO enabled KDE application.

This package is part of tdesvn-trinity.


%prep
%setup -q -n applications/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
find . -name CMakeLists.txt -exec %__sed -i {} \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g" \
  -e "s,/usr/bin/tmoc,%{_bindir}/tmoc,g" \
  -e "s,/usr/bin/uic-tqt,%{_bindir}/uic-tqt,g" \
  \;

# More ugly hack to add TQT include directory in CMakeLists.txt	
%__sed -i CMakeLists.txt \
  -e "s,^\(INCLUDE_DIRECTORIES (\)$,\1\n%{_includedir}/tqt,"

# Moves HTML files to the correect location
find . -name "*.cmake" -exec %__sed -i {} \
  -e "s,/doc/HTML,/doc/kde/HTML,g" \
  \;

%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%__mkdir_p build
cd build
%cmake ..

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


%find_lang %{kdecomp} || touch %{kdecomp}.lang


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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/kdesvn
%{_bindir}/kdesvnaskpass
%{tde_libdir}/libkdesvnpart.la
%{tde_libdir}/libkdesvnpart.so
%{_datadir}/applications/kde/kdesvn.desktop
%{_datadir}/apps/kconf_update/kdesvn-use-external-update.sh
%{_datadir}/apps/kconf_update/kdesvnpartrc-use-external.upd
%{_datadir}/apps/kdesvn/kdesvnui.rc
%{_datadir}/apps/kdesvnpart/kdesvn_part.rc
%{_datadir}/apps/konqueror/servicemenus/kdesvn_subversion.desktop
%{_datadir}/config.kcfg/kdesvn_part.kcfg
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svgz
%{_mandir}/man1/kdesvn.1
%{_mandir}/man1/kdesvnaskpass.1
%{tde_docdir}/HTML

%files -n trinity-libsvnqt
%{_libdir}/libsvnqt.so.4
%{_libdir}/libsvnqt.so.4.2.2

%files -n trinity-libsvnqt-devel
%{_includedir}/svnqt
%{_libdir}/libsvnqt.so

%files kio-plugins
%{_datadir}/services/kded/kdesvnd.desktop
%{_datadir}/services/ksvn+file.protocol
%{_datadir}/services/ksvn+http.protocol
%{_datadir}/services/ksvn+https.protocol
%{_datadir}/services/ksvn+ssh.protocol
%{_datadir}/services/ksvn.protocol
%{_datadir}/services/svn+file.protocol
%{_datadir}/services/svn+http.protocol
%{_datadir}/services/svn+https.protocol
%{_datadir}/services/svn+ssh.protocol
%{_datadir}/services/svn.protocol
%{tde_libdir}/kio_ksvn.la
%{tde_libdir}/kio_ksvn.so
%{tde_libdir}/kded_kdesvnd.la
%{tde_libdir}/kded_kdesvnd.so


%Changelog
* Thu Dec 01 2011 Francois Andriot <francois.andriot@free.fr> - 1.0.4-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
