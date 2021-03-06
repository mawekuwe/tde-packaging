# Default version for this component
%define tde_pkg gtk-qt-engine
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
Summary:		theme engine using Qt for GTK+ 2.x and Trinity
Version:		0.8
Release:		%{?!preversion:7}%{?preversion:6_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:		gtk-qt-engine.rc.sh
Source2:		gtkrc-2.0-kde4
Source3:		gtkrc-2.0-kde-kde4

# Fix severe iceweasel/icedove tab bar corruption
# Clean up minor build warnings
Patch1:			1383169502:f181fbbb337a75257089e64afabd04dac2e1d466.diff
# Fix numerous drawing glitches in Firefox
Patch2:			1387752298:6e6dbb068e03a8bb818a76ba774d6f94ade7389f.diff
# Fix Firefox scrollbars
Patch3:			1387757695:a90aa09722d47f5f4009b089d8d874354899bdb8.diff
# Fix Firefox text edit widget glitches
# Clean up minor build warnings
Patch4:			1387965535:0330b848db129b3dc4daa2a57272ec3b2fb7984c.diff

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext


%description
The GTK-Qt Theme Engine (also known as gtk-qt-engine) is a GTK 2 theme engine
that calls Qt to do the actual drawing. This makes your GTK 2 applications
look almost like real Qt applications and gives you a more unified desktop
experience.

Please note that this package is targeted at Trinity users and therefore provides
a way to configure it from within KControl.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-3.5.13.2%{?preversion:~%{preversion}}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

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
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DDATA_INSTALL_DIR=%{tde_datadir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  ..

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

%find_lang gtkqtengine

# Adds TDE's specific GTKRC
%__install -D -m 644 %{SOURCE1} %{buildroot}%{tde_datadir}/kgtk/gtk-qt-engine.rc.sh
%__install -D -m 644 %{SOURCE2} %{buildroot}%{tde_datadir}/kgtk/.gtkrc-2.0-kde4
%__install -D -m 644 %{SOURCE3} %{buildroot}%{tde_datadir}/kgtk/.gtkrc-2.0-kde-kde4


%clean
%__rm -rf %{buildroot}


%files -f gtkqtengine.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_tdelibdir}/kcm_kcmgtk.la
%{tde_tdelibdir}/kcm_kcmgtk.so
%{tde_appdir}/kcmgtk.desktop
%{tde_datadir}/kgtk/gtk-qt-engine.rc.sh
%{tde_datadir}/kgtk/.gtkrc-2.0-kde4
%{tde_datadir}/kgtk/.gtkrc-2.0-kde-kde4

# The following files are outside TDE's directory
%{_libdir}/gtk-2.0/2.10.0/engines/libqtengine.so
%{_datadir}/themes/Qt/gtk-2.0/gtkrc


%changelog
* Mon Jan 06 2014 Francois Andriot <francois.andriot@free.fr> - 0.8-7
- Backport fixes from R14

* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 0.8-6
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.8-5
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.8-4
- Initial release for TDE 3.5.13.1

* Mon Aug 27 2012 Francois Andriot <francois.andriot@free.fr> - 0.8-3
- Add missing gtkrc files

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.8-2
- Rebuilt for Fedora 17
- Fix FTBFS with newer glib
- Removes useless post and postun

* Sun Nov 20 2011 Francois Andriot <francois.andriot@free.fr> - 0.8-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
