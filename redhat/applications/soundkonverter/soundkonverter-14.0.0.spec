# Default version for this component
%define tde_pkg soundkonverter
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

%define _docdir %{tde_tdedocdir}


Name:			trinity-%{tde_pkg}
Summary:		audio converter frontend for Trinity
Version:		0.3.8
Release:		%{?!preversion:4}%{?preversion:3_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Application/Multimedia

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://potracegui.sourceforge.net

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils


%description
soundKonverter is a frontend to various audio converters.

The key features are:
 - Audio conversion
 - Replay Gain calculation
 - CD ripping

soundKonverter supports reading and writing tags for many formats, so the tags
are preserved when converting files.

It comes with an Amarok script.

See 'soundkonverter-amarok' package for more informations.

See README.Debian for more informations on supported formats.


%package amarok
Summary:		audio converter frontend for Trinity (Amarok script)
Group:			Application/Multimedia
Requires:		%{name} = %{version}-%{release}
Requires:		trinity-amarok

%description amarok
Amarok script for soundKonverter. It allows you to easily transcode files when
transferring them to your media device.

See the 'soundkonverter-trinity' package for more information.


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
  --enable-gcc-hidden-visibility \
  \
  --with-extra-includes=/usr/include/cdda
   
%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}

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


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_bindir}/soundkonverter
%{tde_bindir}/userscript.sh
%{tde_tdeappdir}/soundkonverter.desktop
%{tde_datadir}/apps/konqueror/servicemenus/audiocd_extract_with_soundkonverter.desktop
%{tde_datadir}/apps/soundkonverter
%exclude %{tde_datadir}/apps/soundkonverter/amarokscript/README
%exclude %{tde_datadir}/apps/soundkonverter/amarokscript/soundKonverter.rb
%{tde_tdedocdir}/HTML/en/soundkonverter/common
%{tde_tdedocdir}/HTML/en/soundkonverter/index.cache.bz2
%{tde_tdedocdir}/HTML/en/soundkonverter/index.docbook
%{tde_datadir}/icons/hicolor/*/apps/soundkonverter*.png
%{tde_datadir}/mimelnk/application/x-la.soundkonverter.desktop
%{tde_datadir}/mimelnk/application/x-ofc.soundkonverter.desktop
%{tde_datadir}/mimelnk/application/x-ofr.soundkonverter.desktop
%{tde_datadir}/mimelnk/application/x-ofs.soundkonverter.desktop
%{tde_datadir}/mimelnk/application/x-shorten.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/amr.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/x-ape.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/x-bonk.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/x-pac.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/x-tta.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/x-wavpack-correction.soundkonverter.desktop
%{tde_datadir}/mimelnk/audio/x-wavpack.soundkonverter.desktop
%{tde_datadir}/mimelnk/video/x-flv.soundkonverter.desktop

%files amarok
%defattr(-,root,root,-)
%{tde_datadir}/apps/soundkonverter/amarokscript/README
%{tde_datadir}/apps/soundkonverter/amarokscript/soundKonverter.rb


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.3.8-4
- Initial release for TDE 14.0.0

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.3.8-3
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.3.8-2
- Initial release for TDE 3.5.13.1

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.3.8-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16

