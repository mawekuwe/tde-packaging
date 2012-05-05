# Default version for this component
%define kdecomp ksquirrel
%define version 0.8.0
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%define _mandir %{_datadir}/man
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	Powerful Trinity image viewer
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Amusements/Games

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-libkipi-devel
BuildRequires:	trinity-libksquirrel-devel
#BuildRequires:	libkexif-devel

%description
KSquirrel is an image viewer for TDE with disk navigator, file tree,
multiple directory view, thumbnails, extended thumbnails, dynamic
format support, DCOP interface, KEXIF and KIPI plugins support.

KSquirrel is a fast and convenient image viewer for KDE featuring
OpenGL and dynamic format support.


%prep
%setup -q -n applications/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
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

%find_lang %{kdecomp}

%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files -f %{kdecomp}
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING LICENSE LICENSE.GFDL LICENSE.LGPL README TODO
%{_bindir}/ksquirrel
%{_bindir}/ksquirrel-libs-configurator
%{_bindir}/ksquirrel-libs-configurator-real
%{tde_libdir}/libksquirrelpart.la
%{tde_libdir}/libksquirrelpart.so
%{_datadir}/applications/kde/ksquirrel.desktop
%{_datadir}/apps/dolphin/servicemenus/dolphksquirrel-dir.desktop
%{_datadir}/apps/konqueror/servicemenus/konqksquirrel-dir.desktop
%{_datadir}/apps/ksquirrel/
%{_datadir}/apps/ksquirrelpart/ksquirrelpart.rc
%{_datadir}/config/magic/x-ras.magic
%{_datadir}/config/magic/x-sun.magic
%{_datadir}/config/magic/x-utah.magic
%{tde_docdir}/HTML/*/ksquirrel
%{_datadir}/icons/hicolor/*/apps/ksquirrel.png
%{_datadir}/mimelnk/image/*.desktop
%{_datadir}/services/ksquirrelpart.desktop
%{_datadir}/locale/*/LC_MESSAGES/ksquirrel.mo
%{_mandir}/man1/ksquirrel.1

%Changelog
* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.1-2
- Rebuild for Fedora 17
- Fix HTML directory location

* Sun Nov 20 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.0-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
