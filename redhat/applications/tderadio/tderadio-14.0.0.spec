# Default version for this component
%define tde_pkg tderadio
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

%if 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version}
%define with_lirc 1
%endif

Name:			trinity-%{tde_pkg}
Summary:		Comfortable Radio Application for TDE [Trinity]
Version:		0.1.1.1
Release:		%{?!preversion:8}%{?preversion:7_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext
BuildRequires:	libsndfile-devel
%{?with_lirc:BuildRequires:	lirc-devel}

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}twolame-devel
%endif
%if 0%{?suse_version}
BuildRequires:	libtwolame-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	lame-devel
%endif

Obsoletes:		trinity-kradio < %{version}-%{release}
Provides:		trinity-kradio = %{version}-%{release}

%description
KRadio is a comfortable radio application for Trinity with support for 
V4L and V4L2 radio cards drivers.

KRadio currently provides

 * V4L/V4L2 radio support
%if 0%{?with_lirc}
 * Remote control support (LIRC)
%endif
 * Alarms, sleep Countdown
 * Several GUI Controls (Docking Menu, Station Quickbar, Radio Display)
 * Recording capabilities, including MP3 and Ogg/Vorbis encoding
 * Timeshifter functionality
 * Extendable plugin architecture

This package also includes a growing collection of station preset
files for many cities around the world contributed by KRadio users.

As KRadio is based on an extendable plugin architecture, contributions
of new plugins (e.g. Internet Radio Streams, new cool GUIs) are welcome.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"



%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

# Warning: --enable-visibility causes applications fails to start !
%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-final \
  --enable-new-ldflags \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility \
  \
  %{?with_lirc:--enable-lirc} %{?!with_lirc:--disable-lirc} \
  --enable-v4l2 \
  --enable-lame \
  --enable-ogg \
  --enable-alsa \
  --enable-oss

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%post
for f in hicolor locolor ; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done
update-desktop-database %{tde_appdir} -q &> /dev/null ||:

%postun
for f in hicolor locolor ; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done
update-desktop-database %{tde_appdir} -q &> /dev/null ||:


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/convert-presets
%{tde_bindir}/tderadio
%{tde_libdir}/tderadio/plugins/*.la
%{tde_libdir}/tderadio/plugins/*.so
%{tde_tdeappdir}/tderadio.desktop
%{tde_datadir}/apps/tderadio/
%{tde_datadir}/icons/hicolor/*/*/tderadio*.png
%{tde_datadir}/icons/locolor/*/*/tderadio*.png
%lang(de) %{tde_datadir}/locale/de/LC_MESSAGES/*.mo
%lang(ru) %{tde_datadir}/locale/ru/LC_MESSAGES/*.mo

%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.1.1.1-8
- Initial release for TDE 14.0.0
