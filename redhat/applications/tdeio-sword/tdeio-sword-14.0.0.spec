# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# Default version for this component
%define tde_pkg tdeio-sword
%define tde_version 14.0.0

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:           trinity-%{tde_pkg}
Version:        0.3
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:        tdeio-slave for the Sword Bible tool

Group:          Productivity/Networking/Ftp/Clients
License:        GPLv2+
URL:            http://lukeplant.me.uk/kio-sword/

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

%description
TDEio-Sword provides access to Bibles, commentaries
and other texts in an easy to use and attractive
interface -- the Konqueror web browser.  It does so
using the SWORD Bible project and implementing a TDE
ioslave, providing the sword:/ protocol.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-final \
  --enable-new-ldflags \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility \
  \
%if 0%{?fedora} >= 20 || 0%{?pclinuxos}
  --with-sword-dir=%{tde_prefix}
%endif

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{buildroot}


%post
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done


%postun
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} 2> /dev/null || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f}  2> /dev/null || :
done


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{tde_tdelibdir}/tdeio_sword.la
%{tde_tdelibdir}/tdeio_sword.so
%{tde_datadir}/apps/tdeio_sword/swordvertical.png
%{tde_datadir}/apps/tdeio_sword/tdeio_sword.css
%{tde_tdedocdir}/HTML/en/tdeio_sword/
%{tde_datadir}/icons/hicolor/*/apps/tdeio_sword.png
%{tde_datadir}/icons/hicolor/scalable/apps/tdeio_sword.svgz
%{tde_datadir}/services/sword.protocol


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.3-1
- Initial release for TDE 14.0.0
