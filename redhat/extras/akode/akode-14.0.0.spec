#
# spec file for package akode (version R14.0.0)
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

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%define tde_version 14.0.0
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

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

Name:		trinity-akode 
Summary: 	Audio-decoding framework 
Group: 		System Environment/Libraries
Epoch:		%{tde_epoch}
Version:	2.0.2
Release:	1%{?dist}%{?_variant}
URL:		http://www.kde-apps.org/content/show.php?content=30375

License:	LGPLv2+
#URL:		http://carewolf.com/akode/  

Source0:	akode-%{tde_version}.tar.gz

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


# FLAC support
%define _with_flac --with-flac
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos}
BuildRequires: libflac-devel
%else
BuildRequires: %{_lib}flac-devel
%endif
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: flac-devel
%endif

# JACK support
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define _with_jack --with-jack
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires: %{_lib}jack-devel
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires: jack-audio-connection-kit-devel
%endif
%endif

# SAMPLERATE support
%if 0%{?rhel} >= 4 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define _with_libsamplerate --with-libsamplerate
BuildRequires: libsamplerate-devel
%endif

# PULSEAUDIO support
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 6 || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define _with_pulseaudio --with-pulseaudio
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires: %{_lib}pulseaudio-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires: pulseaudio-libs-devel
%endif
%if 0%{?suse_version}
BuildRequires: pulseaudio-devel
%endif
%endif

# MAD support
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
%define _with_libmad --with-libmad
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:		%{_lib}mad-devel
%endif
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
BuildRequires:		libmad-devel
%endif
%endif


BuildRequires: automake libtool
BuildRequires: alsa-lib-devel
BuildRequires: libvorbis-devel
BuildRequires: speex-devel


%description
aKode is a simple audio-decoding frame-work that provides a uniform
interface to decode the most common audio-formats. It also has a direct
playback option for a number of audio-outputs.

aKode currently has the following decoder plugins:
* mpc: Decodes musepack aka mpc audio.
* xiph: Decodes FLAC, Ogg/FLAC, Speex and Ogg Vorbis audio. 

aKode also has the following audio outputs:
* alsa: Outputs to ALSA (dmix is recommended).
* jack
* pulseaudio

%files
%defattr(-,root,root,-)
%doc rpmdocs/* 
%{tde_bindir}/akodeplay
%{tde_libdir}/libakode.so.*
%{tde_libdir}/libakode_alsa_sink.la
%{tde_libdir}/libakode_alsa_sink.so
%{tde_libdir}/libakode_mpc_decoder.la
%{tde_libdir}/libakode_mpc_decoder.so
%{tde_libdir}/libakode_oss_sink.la
%{tde_libdir}/libakode_oss_sink.so
%{tde_libdir}/libakode_xiph_decoder.la
%{tde_libdir}/libakode_xiph_decoder.so

%post
/sbin/ldconfig

%postun 
/sbin/ldconfig

##########

%package devel
Summary: Headers for developing programs that will use %{name} 
Group:   Development/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%{?_with_jack:Requires: %{name}-jack = %{?epoch:%{epoch}:}%{version}-%{release}}
%{?_with_pulseaudio:Requires: %{name}-pulseaudio = %{?epoch:%{epoch}:}%{version}-%{release}}
%{?_with_libsamplerate:Requires: %{name}-libsamplerate = %{?epoch:%{epoch}:}%{version}-%{release}}
%{?_with_libmad:Requires: %{name}-libmad = %{?epoch:%{epoch}:}%{version}-%{release}}
Requires: pkgconfig

%description devel
This package contains the development files for Akode.

%files devel
%defattr(-,root,root,-)
%{tde_bindir}/akode-config
%{tde_includedir}/*
%{tde_libdir}/libakode.la
%{tde_libdir}/libakode.so
%{tde_libdir}/pkgconfig/*.pc

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

##########

%if "%{?_with_jack}" != ""

%package jack 
Summary: Jack audio output backend for %{name}
Group:   Development/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description jack 
This package contains the Jack audio output backend for Akode.

%files jack 
%defattr(-,root,root,-)
%{tde_libdir}/libakode_jack_sink.la
%{tde_libdir}/libakode_jack_sink.so

%post jack
/sbin/ldconfig

%postun jack
/sbin/ldconfig

%endif

##########

%if "%{?_with_pulseaudio}" != ""

%package pulseaudio
Summary: Pulseaudio output backend for %{name}
Group:   Development/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description pulseaudio
This package contains the pulseaudio backend for Akode.
Recommended for network transparent audio.

%files pulseaudio
%defattr(-,root,root,-)
%{tde_libdir}/libakode_polyp_sink.la
%{tde_libdir}/libakode_polyp_sink.so

%post pulseaudio
/sbin/ldconfig

%postun pulseaudio
/sbin/ldconfig

%endif

##########

# Packaged separately to keep main/core %{akode} package LGPL-clean.
%if "%{?_with_libsamplerate:1}" == "1"

%package libsamplerate 
Summary: Resampler based on libsamplerate for %{name}
Group:   Development/Libraries
License: GPLv2+
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description libsamplerate 
This package contains the samplerate decoder for Akode.

# License: GPLv2+
%files libsamplerate
%defattr(-,root,root,-)
%{tde_libdir}/libakode_src_resampler.la
%{tde_libdir}/libakode_src_resampler.so

%post libsamplerate
/sbin/ldconfig

%postun libsamplerate 
/sbin/ldconfig

%endif

##########

%if "%{?_with_libmad}" != ""

%package libmad
Summary: Decoder based on libmad for %{name}
Group:   Development/Libraries
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description libmad 
This package contains the mad decoder for Akode.

%files libmad
%{tde_libdir}/libakode_mpeg_decoder.la
%{tde_libdir}/libakode_mpeg_decoder.so

%post libmad
/sbin/ldconfig

%postun libmad 
/sbin/ldconfig

%endif

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n akode-2.0.2

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f admin/Makefile.common


%build
export CXXFLAGS="${RPM_OPT_FLAGS} -DHAVE_STDINT_H"

%configure \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --includedir=%{tde_includedir} \
  --datadir=%{tde_datadir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility \
  \
  --without-libltdl \
  --with-alsa \
  --with-oss \
  %{?_with_flac} %{!?_with_flac:--without-flac} \
  %{?_with_jack} %{!?_with_jack:--without-jack} \
  %{?_with_libsamplerate} %{!?_with_libsamplerate:--without-libsamplerate} \
  %{?_with_pulseaudio} %{!?_with_pulseaudio:--without-pulseaudio} \
  --with-speex \
  --with-vorbis \
  --without-ffmpeg \
  %{?_with_libmad} %{!?_with_libmad:--without-libmad}

%__make %{?_smp_mflags} LIBTOOL=/usr/bin/libtool


%install
%__rm -rf %{buildroot} 
%__make install DESTDIR=%{buildroot}

# unpackaged files
%__rm -f %{buildroot}%{tde_libdir}/*.a

# rpmdocs
for file in AUTHORS COPYING NEWS README TODO ; do
  test -s  "$file" && install -p -m644 -D "$file" "rpmdocs/$file"
done


%clean
%__rm -rf %{buildroot} 


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2:2.0.2-1
- Initial release for TDE 14.0.0
