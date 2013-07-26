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

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Summary: Audio-decoding framework 
Name:	 trinity-akode 
Version: 2.0.2
Release:	5%{?dist}%{?_variant}

License: LGPLv2+
Group: 	 System Environment/Libraries
#URL:	 http://carewolf.com/akode/  
URL:	 http://www.kde-apps.org/content/show.php?content=30375
Source0:	akode-2.0.2.tar.bz2

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


# Legacy Fedora 9 patches
Patch1: akode-pulseaudio.patch
Patch2: akode-2.0.2-multilib.patch
Patch3: akode-2.0.2-flac113-portable.patch
Patch4: akode-2.0.2-gcc43.patch

# New patch for Fedora 16 / TDE 3.5.13
Patch10: akode-autotools.patch
Patch11: akode-2.0.2-fix_ffmpeg_include.patch
Patch12: akode-2.0.2-fix_ftbfs.patch

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
Requires: %{name} = %{version}-%{release}
%{?_with_jack:Requires: %{name}-jack = %{version}-%{release}}
%{?_with_pulseaudio:Requires: %{name}-pulseaudio = %{version}-%{release}}
%{?_with_libsamplerate:Requires: %{name}-libsamplerate = %{version}-%{release}}
%{?_with_libmad:Requires: %{name}-libmad = %{version}-%{release}}
Requires: pkgconfig

%description devel
%{summary}.

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
Requires: %{name} = %{version}-%{release}

%description jack 
%{summary}.

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
Requires: %{name} = %{version}-%{release}

%description pulseaudio
%{summary}.
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
Requires: %{name} = %{version}-%{release}

%description libsamplerate 
%{summary}.

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
Requires: %{name} = %{version}-%{release}

%description libmad 
%{summary}.

%files libmad
%{tde_libdir}/libakode_mpeg_decoder.la
%{tde_libdir}/libakode_mpeg_decoder.so

%post libmad
/sbin/ldconfig

%postun libmad 
/sbin/ldconfig

%endif

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n akode-%{version}

%patch1 -p1 -b .pulseaudio
%patch2 -p1 -b .multilib
%patch3 -p4 -b .flac113_portable
%patch4 -p1 -b .gcc43

%patch10 -p1 -b .autotools
%patch11 -p1 -b .ffmpeg
%patch12 -p1 -b .ftbfs

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f admin/Makefile.common cvs

%build
%configure \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --includedir=%{tde_includedir} \
  --datadir=%{tde_datadir} \
  --disable-static \
  --enable-shared \
  --disable-debug --disable-warnings --disable-dependency-tracking \
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
  %{?_with_libmad} %{!?_with_libmad:--without-libmad} \
  --enable-closure \
  --enable-new-ldflags \
  --enable-final

%__make %{?_smp_mflags} LIBTOOL=$(which libtool)


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
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2.0.2-5
- Initial release for TDE 14.0.0

* Sat Jan 19 2013 Francois Andriot <francois.andriot@free.fr> - 2.0.2-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 2.0.2-3
- Initial release for TDE 3.5.13.1

* Mon Jul 30 2012 Francois Andriot <francois.andriot@free.fr> - 2.0.2-2
- Re-adds '.la' files

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 2.0.2-1
- Port to TDE 3.5.13
- Based on spec file from Fedora 9 'akode-2.0.2-5'
