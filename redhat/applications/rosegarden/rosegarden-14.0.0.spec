# Default version for this component
%define tde_pkg rosegarden
%define tde_version 14.0.0

# Required for Mageia 2: removes the ldflag '--no-undefined'
%define _disable_ld_no_undefined 1

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
Summary:		music editor and MIDI/audio sequencer [Trinity]
Version:		1.7.0
Release:		%{?!preversion:7}%{?preversion:6_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Multimedia

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.rosegardenmusic.com/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext
BuildRequires:	fftw-devel
BuildRequires:	liblo-devel
BuildRequires:	fontconfig-devel

# DSSI support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	dssi-devel
%endif

# LRDF support
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	liblrdf-devel
%endif

# JACK support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}jack-devel
%else
BuildRequires:	jack-audio-connection-kit-devel
%endif

# LIRC support
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 6
%define with_lirc 1
BuildRequires:	lirc-devel
%endif

Requires:		lilypond
Requires:		perl-XML-Twig

%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
Requires:		libsndfile-progs
%else
%if 0%{?rhel}
Requires:		libsndfile
%else
Requires:		libsndfile-utils
%endif
%endif


Requires:		%{name}-data == %{version}-%{release}

%description
Rosegarden is a TDE application which provides a mixed Audio/MIDI
sequencer (for playback and recording), a multi-track editor, music
editing using both piano-roll and score notation, MIDI file IO,
lilypond and Csound files export, etc.

%package data
Group:			Applications/Multimedia
Requires:		%{name} == %{version}-%{release}
Summary:		music editor and MIDI/audio sequencer data files [Trinity]

%description data
Rosegarden is a TDE application which provides a mixed Audio/MIDI
sequencer (for playback and recording), a multi-track editor, music
editing using both piano-roll and score notation, MIDI file IO,
lilypond and Csound files export, etc.

This package provides the data files necessary for running Rosegarden


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

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
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DWANT_SOUND=ON \
  -DWANT_JACK=ON \
  -DWANT_DSSI=ON \
  %{?with_lirc:-DWANT_LIRC=ON} %{?!with_lirc:-DWANT_LIRC=OFF} \
  -DWANT_PCH=OFF \
  -DWANT_TEST=OFF \
  -DWANT_DEBUG=OFF \
  -DWANT_FULLDBG=OFF \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build

# Unwanted files
%__rm -f %{?buildroot}%{tde_libdir}/*.a

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_appdir} > /dev/null
for f in hicolor locolor; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done

%postun
update-desktop-database %{tde_appdir} > /dev/null
for f in hicolor locolor; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done


%files
%defattr(-,root,root,-)
%{tde_bindir}/rosegarden
%{tde_bindir}/rosegarden-audiofile-importer
%{tde_bindir}/rosegarden-lilypondview
%{tde_bindir}/rosegarden-project-package
%{tde_bindir}/rosegardensequencer

%files data -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_tdeappdir}/rosegarden.desktop
%{tde_datadir}/apps/profiles/rosegarden.profile.xml
%lang(en) %{tde_tdedocdir}/HTML/en/rosegarden
%lang(es) %{tde_tdedocdir}/HTML/es/rosegarden
%lang(ja) %{tde_tdedocdir}/HTML/ja/rosegarden
%lang(sv) %{tde_tdedocdir}/HTML/sv/rosegarden
%{tde_datadir}/apps/rosegarden
%{tde_datadir}/icons/hicolor/*/*/*
%{tde_datadir}/icons/locolor/*/*/*
%{tde_datadir}/mimelnk/audio/x-rosegarden-device.desktop
%{tde_datadir}/mimelnk/audio/x-rosegarden.desktop
%{tde_datadir}/mimelnk/audio/x-rosegarden21.desktop
%{tde_datadir}/mimelnk/audio/x-soundfont.desktop


%changelog
* Mon Jul 29 2013 Francois Andriot <francois.andriot@free.fr> - 1.7.0-7
- Initial release for TDE 14.0.0
