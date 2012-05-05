# Default version for this component
%define kdecomp gtk-qt-engine
%define version 0.8
%define release 2

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
Summary:	theme engine using Qt for GTK+ 2.x and Trinity
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [gtk-qt-engine] Fix inclusion of 'glib.h'
Patch1:		gtk-qt-engine-3.5.13-fix_glib_include.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
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

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
sed -i CMakeLists.txt \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"

%__mkdir build
cd build
%cmake \
	..

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


%clean
%__rm -rf %{buildroot}



%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_libdir}/kcm_kcmgtk.la
%{tde_libdir}/kcm_kcmgtk.so
%{_datadir}/applications/kcmgtk.desktop
%{_usr}/%{_lib}/gtk-2.0/2.10.0/engines/libqtengine.so
%{_usr}/share/themes/Qt/gtk-2.0/gtkrc
%{_datadir}/locale/*/LC_MESSAGES/*.mo


%Changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.8-2
- Rebuilt for Fedora 17
- Fix FTBFS with newer glib
- Removes useless post and postun

* Sun Nov 20 2011 Francois Andriot <francois.andriot@free.fr> - 0.8-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
