# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# Default version for this component
%define tde_pkg mplayerthumbs
%define tde_version 14.0.0

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man

%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:           trinity-%{tde_pkg}
Version:        0.5b
Release:		%{?!preversion:2}%{?preversion:1_%{preversion}}%{?dist}%{?_variant}
Summary:        A video thumbnail generator for TDE file managers.

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://kde-apps.org/content/show.php?content=41180
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

Requires:		mplayer

%description
MPlayerThumbs is a video thumbnail generator for TDE file managers 
(Konqueror, Dolphin, ...).
It needs mplayer (of course) to generate thumbnails, and it contains no 
linking to any library, so in a x86_64 system you can freely use the 
32bit mplayer binary with win32codecs by configuring the application 
launching the mplayerthumbsconfig helper application.
It catches a random frame from 15% to 70%, checking also how contrasted 
is the image, and dropping bad frames.


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
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --htmldir=%{tde_tdedocdir}/HTML \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-final \
  --enable-new-ldflags \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility

%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT


%clean
%__rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{tde_bindir}/mplayerthumbsconfig
%{tde_tdelibdir}/videopreview.la
%{tde_tdelibdir}/videopreview.so
%{tde_datadir}/apps/videopreview/
%{tde_datadir}/config.kcfg/mplayerthumbs.kcfg
%{tde_datadir}/services/videopreview.desktop
%{tde_tdedocdir}/HTML/en/videopreview/


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.5b-2
- Initial release for TDE 14.0.0

* Mon Apr 08 2013 Francois Andriot <francois.andriot@free.fr> - 0.5b-1
- Initial release for TDE 3.5.13.2
