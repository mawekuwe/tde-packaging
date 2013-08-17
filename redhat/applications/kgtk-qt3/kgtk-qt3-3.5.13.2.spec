# Default version for this component
%define tde_pkg kgtk-qt3
%define tde_version 3.5.13.2

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

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		Use TDE dialogs in Gtk apps
Version:		0.10.2
Release:		%{?!preversion:6}%{?preversion:5_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext


%description
This is an LD_PRELOAD hack that allows most GTK
applications to use Trinity's file dialogs when run under Trinity.

The Gtk file chooser functions have been overridden to communicate
with this TDE module/application.

This package includes the kqt3-wrapper


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%build
unset QTDIR; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%__mkdir_p build
cd build
%endif


%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DBUILD_ALL=ON \
  ..

# SMP safe !
%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

# The "preload" file is used by "startkde" script
%__install -d -m 755 "%{buildroot}%{tde_datadir}/kgtk"
echo "%{tde_libdir}/kgtk/libkgtk2.so" >"%{buildroot}%{tde_datadir}/kgtk/preload"

%find_lang kgtk



%clean
%__rm -rf %{buildroot}


%files -f kgtk.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{tde_bindir}/kdialogd-wrapper
%{tde_bindir}/kdialogd3
%{tde_bindir}/kgtk-wrapper
%{tde_bindir}/kgtk2-wrapper
%{tde_bindir}/kqt3-wrapper
%{tde_libdir}/kgtk/libkgtk2.so
%{tde_libdir}/kgtk/libkqt3.so
%{tde_datadir}/kgtk/preload

%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 0.10.2-6
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.10.2-5
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.10.2-4
- Initial release for TDE 3.5.13.1

* Sun Aug 26 2012 Francois Andriot <francois.andriot@free.fr> - 0.10.2-3
- Add 'preload' file for startkde script

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.10.2-2
- Rebuilt for Fedora 17
- Removes post and postun

* Thu Dec 01 2011 Francois Andriot <francois.andriot@free.fr> - 0.10.2-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
