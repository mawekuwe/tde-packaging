# Default version for this component
%define tde_pkg tdesvn
%define tde_version 14.0.0

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		subversion client with tight TDE integration [Trinity]
Version:		1.0.4
Release:		%{?!preversion:8}%{?preversion:7_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.elliptique.net/~ken/kima/

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	subversion-devel
Requires:		%{name}-tdeio-plugins = %{version}-%{release}
Requires:		trinity-libsvnqt = %{version}-%{release}

Obsoletes:	trinity-kdesvn < %{version}-%{release}
Provides:	trinity-kdesvn = %{version}-%{release}

%description
TDESvn is a graphical client for the subversion revision control
system (svn).

Besides offering common and advanced svn operations, it features
a tight integration into TDE and can be embedded into other TDE 
applications like konqueror via the TDE component technology KParts.


%package -n trinity-libsvnqt
Group:			Development/Libraries
Summary:		Qt wrapper library for subversion [Trinity]

%description -n trinity-libsvnqt
This package provides svnqt, a Qt wrapper library around the 
subversion library.

It is based on the RapidSvn SvnCpp library, a subversion client API 
written in C++.

%package -n trinity-libsvnqt-devel
Group:			Development/Libraries
Requires:		trinity-libsvnqt = %{version}-%{release}
Requires:		qt-devel
Requires:		subversion-devel
Summary:		Qt wrapper library for subversion (development files) [Trinity]

%description -n trinity-libsvnqt-devel
This package contains the header files and symbolic links that developers
using svnqt will need.


%package tdeio-plugins
Group:			Development/Libraries
Conflicts:	trinity-kdesdk-tdeio-plugins
Summary:		subversion I/O slaves for Trinity

Obsoletes:	trinity-kdesvn-kio-plugins < %{version}-%{release}
Provides:	trinity-kdesvn-kio-plugins = %{version}-%{release}
Obsoletes:	trinity-tdesvn-kio-plugins < %{version}-%{release}
Provides:	trinity-tdesvn-kio-plugins = %{version}-%{release}

%description tdeio-plugins
This packages includes KIO slaves for svn, svn+file, svn+http, 
svn+https, svn+ssh. This allows you to access subversion repositories 
inside any KIO enabled TDE application.

This package is part of tdesvn-trinity.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

rm -f src/svnqt/CMakeLists.txt.orig
rm -fr src/svnqt/cache/sqlite3/



%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export CMAKE_INCLUDE_PATH="%{tde_tdeincludedir}"

if ! rpm -E %%cmake|grep -q "cd build"; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_includedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DMAN_INSTALL_DIR=%{tde_mandir}/man1 \
  -DPKGCONFIG_INSTALL_DIR=%{tde_tdelibdir}/pkgconfig \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DBUILD_DOC=ON \
  -DBUILD_TRANSLATIONS=ON \
  ..

# SMP safe !
%__make %{?_smp_mflags} || %__make


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

# Installs SVN protocols as alternatives
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+file.protocol %{?buildroot}%{tde_datadir}/services/svn+file.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+http.protocol %{?buildroot}%{tde_datadir}/services/svn+http.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+https.protocol %{?buildroot}%{tde_datadir}/services/svn+https.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn+ssh.protocol %{?buildroot}%{tde_datadir}/services/svn+ssh.protocol_tdesvn
%__mv -f %{?buildroot}%{tde_datadir}/services/svn.protocol %{?buildroot}%{tde_datadir}/services/svn.protocol_tdesvn

# Locales
%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%post -n trinity-libsvnqt
/sbin/ldconfig || :

%post tdeio-plugins
for proto in svn+file svn+http svn+https svn+ssh svn; do
  update-alternatives --install \
    %{tde_datadir}/services/${proto}.protocol \
    ${proto}.protocol \
    %{tde_datadir}/services/${proto}.protocol_tdesvn \
    20
done

%preun tdeio-plugins
if [ $1 -eq 0 ]; then
  for proto in svn+file svn+http svn+https svn+ssh svn; do
    update-alternatives --remove \
      ${proto}.protocol \
      %{tde_datadir}/services/${proto}.protocol_tdesvn || :
  done
fi



%postun -n trinity-libsvnqt
/sbin/ldconfig || :


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_bindir}/tdesvn
%{tde_bindir}/tdesvnaskpass
%{tde_tdelibdir}/tdesvnpart.la
%{tde_tdelibdir}/tdesvnpart.so
%{tde_datadir}/applications/tde/tdesvn.desktop
%{tde_datadir}/apps/tdeconf_update/tdesvn-use-external-update.sh
%{tde_datadir}/apps/tdeconf_update/tdesvnpartrc-use-external.upd
%{tde_datadir}/apps/tdesvn/tdesvnui.rc
%{tde_datadir}/apps/tdesvnpart/tdesvn_part.rc
%{tde_datadir}/apps/konqueror/servicemenus/tdesvn_subversion.desktop
%{tde_datadir}/config.kcfg/tdesvn_part.kcfg
%{tde_datadir}/icons/hicolor/*/*/*.png
%{tde_datadir}/icons/hicolor/*/*/*.svgz
%{tde_mandir}/man1/tdesvn.1*
%{tde_mandir}/man1/tdesvnaskpass.1*
%lang(en) %{tde_tdedocdir}/HTML/en/tdesvn/
%lang(nl) %{tde_tdedocdir}/HTML/nl/tdesvn/
%{tde_libdir}/libksvnwidgets.la
%{tde_libdir}/libksvnwidgets.so
%{tde_libdir}/libsvnfrontend.la
%{tde_libdir}/libsvnfrontend.so
%{tde_libdir}/libtdesvncfgreader.la
%{tde_libdir}/libtdesvncfgreader.so
%{tde_libdir}/libtdesvnevents.la
%{tde_libdir}/libtdesvnevents.so
%{tde_libdir}/libtdesvnhelpers.la
%{tde_libdir}/libtdesvnhelpers.so

%files -n trinity-libsvnqt
%defattr(-,root,root,-)
%{tde_libdir}/libsvnqt.so.4
%{tde_libdir}/libsvnqt.so.4.2.2

%files -n trinity-libsvnqt-devel
%defattr(-,root,root,-)
%{tde_includedir}/svnqt
%{tde_libdir}/libsvnqt.so

%files tdeio-plugins
%defattr(-,root,root,-)
%{tde_datadir}/services/kded/tdesvnd.desktop
%{tde_datadir}/services/ksvn+file.protocol
%{tde_datadir}/services/ksvn+http.protocol
%{tde_datadir}/services/ksvn+https.protocol
%{tde_datadir}/services/ksvn+ssh.protocol
%{tde_datadir}/services/ksvn.protocol
%{tde_datadir}/services/svn+file.protocol_tdesvn
%{tde_datadir}/services/svn+http.protocol_tdesvn
%{tde_datadir}/services/svn+https.protocol_tdesvn
%{tde_datadir}/services/svn+ssh.protocol_tdesvn
%{tde_datadir}/services/svn.protocol_tdesvn
%{tde_tdelibdir}/tdeio_ksvn.la
%{tde_tdelibdir}/tdeio_ksvn.so
%{tde_tdelibdir}/kded_tdesvnd.la
%{tde_tdelibdir}/kded_tdesvnd.so


%changelog
* Mon Jul 29 2013 Francois Andriot <francois.andriot@free.fr> - 1.0.4-8
- Initial release for TDE 14.0.0
