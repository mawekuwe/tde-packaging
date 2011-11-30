# Default version for this component
%define kdecomp rosegarden
%define version 1.7.0
%define release 1

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
Summary:	music editor and MIDI/audio sequencer [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group: 	    Applications/Multimedia

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.rosegardenmusic.com/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Patch0:		rosegarden-3.5.13-ftbfs.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	fftw-devel
BuildRequires:	dssi-devel
BuildRequires:	liblo-devel
BuildRequires:	liblrdf-devel
BuildRequires:	fontconfig-devel

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

# Hard-coded path to TQT binaries spotted !!!
%__sed -i CMakeLists.txt \
	-e "s,/usr/bin/uic-tqt,%{_bindir}/uic-tqt,g" \
	-e "s,/usr/bin/tmoc,%{_bindir}/tmoc,g" \
	-e "s,/usr/include/tqt,%{_includedir}/tqt,g"

%build
unset QTDIR && . %{_sysconfdir}/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"

%__mkdir_p build
cd build
%cmake \
	-DWANT_DEBUG=OFF \
	-DWANT_FULLDBG=OFF \
	-DWANT_SOUND=ON \
	-DWANT_JACK=OFF \
	-DWANT_DSSI=ON \
%if 0%{?fedora} > 0
	-DWANT_LIRC=ON \
%else
	-DWANT_LIRC=OFF \
%endif
	-DWANT_PCH=OFF \
	-DWANT_TEST=OFF \
 	-DBUILD_ALL=ON \
	..

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


%find_lang %{kdecomp}

%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%{_bindir}/rosegarden
%{_bindir}/rosegarden-audiofile-importer
%{_bindir}/rosegarden-lilypondview
%{_bindir}/rosegarden-project-package
%{_bindir}/rosegardensequencer

%files data -f %{kdecomp}.lang
%defattr(-,root,root,-)
%{_datadir}/applications/kde/rosegarden.desktop
%{_datadir}/apps/profiles/rosegarden.profile.xml
%lang(en) %{tde_docdir}/HTML/en/rosegarden
%lang(es) %{tde_docdir}/HTML/es/rosegarden
%lang(ja) %{tde_docdir}/HTML/ja/rosegarden
%lang(sv) %{tde_docdir}/HTML/sv/rosegarden
%{_datadir}/apps/rosegarden
%{_datadir}/icons/*/*/*/*
%{_datadir}/mimelnk/audio/x-rosegarden-device.desktop
%{_datadir}/mimelnk/audio/x-rosegarden.desktop
%{_datadir}/mimelnk/audio/x-rosegarden21.desktop
%{_datadir}/mimelnk/audio/x-soundfont.desktop


%Changelog
* Sat Nov 26 2011 Francois Andriot <francois.andriot@free.fr> - 1.7.0-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
