#
# spec file for package rosegarden (version R14.0.0)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%define tde_version 14.0.0
%define tde_pkg rosegarden
%define tde_prefix /opt/trinity
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


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.7.0
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:	Music editor and MIDI/audio sequencer [Trinity]
Group:		Applications/Multimedia
URL:		http://www.rosegardenmusic.com/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	cmake libtool
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	fdupes

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

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

# IDN support
BuildRequires:  libidn-devel

# GAMIN support
#  Not on openSUSE.
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_gamin 1
BuildRequires:  gamin-devel
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


##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########


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
update-desktop-database %{tde_tdeappdir} > /dev/null
for f in hicolor locolor; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done

%postun
update-desktop-database %{tde_tdeappdir} > /dev/null
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
* Mon Jul 29 2013 Francois Andriot <francois.andriot@free.fr> - 2:1.7.0-1
- Initial release for TDE 14.0.0
