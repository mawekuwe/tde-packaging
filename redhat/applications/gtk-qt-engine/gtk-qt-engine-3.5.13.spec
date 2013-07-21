# Default version for this component
%define kdecomp gtk-qt-engine

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-%{kdecomp}
Summary:	theme engine using Qt for GTK+ 2.x and Trinity
Version:	0.8
Release:	3%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Source1:	gtk-qt-engine.rc.sh
Source2:	gtkrc-2.0-kde4
Source3:	gtkrc-2.0-kde-kde4

# [gtk-qt-engine] Fix inclusion of 'glib.h'
Patch1:		gtk-qt-engine-3.5.13-fix_glib_include.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-tdelibs-devel
BuildRequires:	trinity-tdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext


%description
The GTK-Qt Theme Engine (also known as gtk-qt-engine) is a GTK 2 theme engine
that calls Qt to do the actual drawing. This makes your GTK 2 applications
look almost like real Qt applications and gives you a more unified desktop
experience.

Please note that this package is targeted at Trinity users and therefore provides
a way to configure it from within KControl.


%prep
%setup -q -n applications/%{kdecomp}
%patch1 -p1

# Renames the '.po' files
for f in po/*/*.po; do
  pushd ${f%/*}
  mv -f *.po gtk-qt-engine.po
  popd
done

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i "CMakeLists.txt" \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

%if 0%{?rhel} || 0%{?fedora}
%__mkdir_p build
cd build
%endif

%cmake \
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

%find_lang %{kdecomp}

# Adds TDE's specific GTKRC
%__install -D -m 644 %{SOURCE1} %{buildroot}%{tde_datadir}/kgtk/gtk-qt-engine.rc.sh
%__install -D -m 644 %{SOURCE2} %{buildroot}%{tde_datadir}/kgtk/.gtkrc-2.0-kde4
%__install -D -m 644 %{SOURCE3} %{buildroot}%{tde_datadir}/kgtk/.gtkrc-2.0-kde-kde4

%clean
%__rm -rf %{buildroot}



%files -f %{kdecomp}.lang
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


%Changelog
* Mon Aug 27 2012 Francois Andriot <francois.andriot@free.fr> - 0.8-3
- Add missing gtkrc files

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.8-2
- Rebuilt for Fedora 17
- Fix FTBFS with newer glib
- Removes useless post and postun

* Sun Nov 20 2011 Francois Andriot <francois.andriot@free.fr> - 0.8-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
