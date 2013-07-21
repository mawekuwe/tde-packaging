# Default version for this component
%define kdecomp ksquirrel

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
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-%{kdecomp}
Summary:	Powerful Trinity image viewer
Version:	0.8.0
Release:	3%{?dist}%{?_variant}

License:	GPLv2+
Group:		Amusements/Games

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.1.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= 3.5.13.1
BuildRequires:	trinity-tdelibs-devel >= 3.5.13.1
BuildRequires:	trinity-tdebase-devel >= 3.5.13.1
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


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{kdecomp}-3.5.13.1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  --disable-rpath \
  --with-extra-includes=%{tde_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{kdecomp}

%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_appdir} > /dev/null
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
update-desktop-database %{tde_appdir} > /dev/null
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files -f %{kdecomp}
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING LICENSE LICENSE.GFDL LICENSE.LGPL README TODO
%{tde_bindir}/ksquirrel
%{tde_bindir}/ksquirrel-libs-configurator
%{tde_bindir}/ksquirrel-libs-configurator-real
%{tde_tdelibdir}/libksquirrelpart.la
%{tde_tdelibdir}/libksquirrelpart.so
%{tde_tdeappdir}/ksquirrel.desktop
%{tde_datadir}/apps/dolphin/servicemenus/dolphksquirrel-dir.desktop
%{tde_datadir}/apps/konqueror/servicemenus/konqksquirrel-dir.desktop
%{tde_datadir}/apps/ksquirrel/
%{tde_datadir}/apps/ksquirrelpart/ksquirrelpart.rc
%{tde_datadir}/config/magic/x-ras.magic
%{tde_datadir}/config/magic/x-sun.magic
%{tde_datadir}/config/magic/x-utah.magic
%{tde_tdedocdir}/HTML/*/ksquirrel
%{tde_datadir}/icons/hicolor/*/apps/ksquirrel.png
%{tde_datadir}/mimelnk/image/*.desktop
%{tde_datadir}/services/ksquirrelpart.desktop
%{tde_datadir}/locale/*/LC_MESSAGES/ksquirrel.mo
%{tde_mandir}/man1/ksquirrel.1

%changelog
* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.0-3
- Initial release for TDE 3.5.13.1

* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.1-2
- Rebuild for Fedora 17
- Fix HTML directory location

* Sun Nov 20 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.0-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
