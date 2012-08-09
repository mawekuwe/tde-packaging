# Default version for this component
%define kdecomp rosegarden

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

%define _docdir %{tde_tdedocdir}


Name:		trinity-%{kdecomp}
Summary:	music editor and MIDI/audio sequencer [Trinity]
Version:	1.7.0
Release:	3%{?dist}%{?_variant}

License:	GPLv2+
Group: 	    Applications/Multimedia

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.rosegardenmusic.com/

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [rosegarden] Version 3.5.13-sru
Patch0:		rosegarden-3.5.13-sru-20120806.patch
# [rosegarden] Missing LDFLAGS cause FTBFS
Patch1:		rosegarden-3.5.13-missing_ldflags.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-tdelibs-devel
BuildRequires:	trinity-tdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	fftw-devel
BuildRequires:	dssi-devel
BuildRequires:	liblo-devel
BuildRequires:	liblrdf-devel
BuildRequires:	fontconfig-devel

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}jack-devel
%else
BuildRequires:	jack-audio-connection-kit-devel
%endif

Requires:	lilypond
Requires:	perl-XML-Twig
Requires:	libsndfile-utils

# LIRC does not exist on RHEL.
%if 0%{?fedora} > 0
BuildRequires:	lirc-devel
%endif

Requires:	%{name}-data == %{version}-%{release}

%description
Rosegarden is a KDE application which provides a mixed Audio/MIDI
sequencer (for playback and recording), a multi-track editor, music
editing using both piano-roll and score notation, MIDI file IO,
lilypond and Csound files export, etc.

%package data
Group: 	    Applications/Multimedia
Requires:	%{name} == %{version}-%{release}
Summary:	music editor and MIDI/audio sequencer data files [Trinity]

%description data
Rosegarden is a KDE application which provides a mixed Audio/MIDI
sequencer (for playback and recording), a multi-track editor, music
editing using both piano-roll and score notation, MIDI file IO,
lilypond and Csound files export, etc.

This package provides the data files necessary for running Rosegarden


%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1
%patch1 -p1

# Hard-coded path to TQT binaries spotted !!!
%__sed -i CMakeLists.txt \
	-e "s|/usr/bin/uic-tqt|%{tde_bindir}/uic-tqt|g" \
	-e "s|/usr/bin/tmoc|%{tde_bindir}/tmoc|g" \
	-e "s|/usr/include/tqt|%{tde_includedir}/tqt|g"

%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export CMAKE_INCLUDE_PATH="%{tde_includedir}:%{tde_includedir}/tqt:%{tde_tdeincludedir}"

# Enables "messages" (debug)
%__sed -i CMakeLists.txt -e "s|#MESSAGE|MESSAGE|g"

%if 0%{?rhel} || 0%{?fedora}
%__mkdir_p build
cd build
%endif

%cmake \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  -DCMAKE_SKIP_RPATH="OFF" \
  -DWANT_DEBUG=OFF \
  -DWANT_FULLDBG=OFF \
  -DWANT_SOUND=ON \
  -DWANT_JACK=ON \
  -DWANT_DSSI=ON \
%if 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
  -DWANT_LIRC=ON \
%else
  -DWANT_LIRC=OFF \
%endif
  -DWANT_PCH=OFF \
  -DWANT_TEST=OFF \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags} || %__make VERBOSE=1


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


%find_lang %{kdecomp}

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

%files data -f %{kdecomp}.lang
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


%Changelog
* Mon Aug 06 2012 Francois Andriot <francois.andriot@free.fr> - 1.7.0-3
- Switch to branch 3.5.13-sru
 
* Sun Apr 06 2012 Francois Andriot <francois.andriot@free.fr> - 1.7.0-2
- Updated to build with gcc 4.7. [Commit #15276f36]
- Enables JACK support

* Sat Nov 26 2011 Francois Andriot <francois.andriot@free.fr> - 1.7.0-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
