# Always install under '/usr'
%define _prefix /usr

Summary: Audio-decoding framework 
Name:	 akode 
Version: 2.0.2
Release: 6%{?dist}

License: LGPLv2+
Group: 	 System Environment/Libraries
#URL:	 http://carewolf.com/akode/  
URL:	 http://www.kde-apps.org/content/show.php?content=30375
Source0: http://www.kde-apps.org/CONTENT/content-files/akode-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


# Legacy Fedora 9 patches
Patch1: akode-pulseaudio.patch
Patch2: akode-2.0.2-multilib.patch
Patch3: akode-2.0.2-flac113-portable.patch
Patch4: akode-2.0.2-gcc43.patch

# New patch for Fedora 16 / TDE 3.5.13
Patch10: akode-autotools.patch

# Optional features that are always enabled :-)
%define _with_flac --with-flac
%define _with_jack --with-jack
%define _with_libsamplerate --with-libsamplerate

# Pulseaudio is not available on RHEL 5 and earlier
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 6
%define _with_pulseaudio --with-pulseaudio
%endif

BuildRequires: automake libtool
BuildRequires: alsa-lib-devel
%{?_with_flac:BuildRequires: flac-devel}
%{?_with_jack:BuildRequires: jack-audio-connection-kit-devel}
%{?_with_libsamplerate:BuildRequires: libsamplerate-devel}
BuildRequires: libvorbis-devel
%{?_with_pulseaudio:BuildRequires: pulseaudio-libs-devel}
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

%package devel
Summary: Headers for developing programs that will use %{name} 
Group:   Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
%description devel
%{summary}.

%package jack 
Summary: Jack audio output backend for %{name}
Group:   Development/Libraries
Requires: %{name} = %{version}-%{release}
%description jack 
%{summary}.

%package pulseaudio
Summary: Pulseaudio output backend for %{name}
Group:   Development/Libraries
Requires: %{name} = %{version}-%{release}
%description pulseaudio
%{summary}.
Recommended for network transparent audio.

# Packaged separately to keep main/core %{akode} package LGPL-clean.
%package libsamplerate 
Summary: Resampler based on libsamplerate for %{name}
Group:   Development/Libraries
License: GPLv2+
Requires: %{name} = %{version}-%{release}
%description libsamplerate 
%{summary}.


%prep
%setup -q -n akode-%{version}

%patch1 -p1 -b .pulseaudio
%patch2 -p1 -b .multilib
%patch3 -p4 -b .flac113_portable
%patch4 -p1 -b .gcc43

%patch10 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g" \
  -e "s,kde_htmldir='.*',kde_htmldir='%{tde_docdir}/HTML',g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f admin/Makefile.common cvs

%build
%configure \
  --disable-static \
  --enable-shared \
  --disable-debug --disable-warnings --disable-dependency-tracking \
  --with-libltdl \
  --with-alsa \
  --with-oss \
  %{?_with_flac} %{!?_with_flac:--without-flac} \
  %{?_with_jack} %{!?_with_jack:--without-jack} \
  %{?_with_libsamplerate} %{!?_with_libsamplerate:--without-libsamplerate} \
  %{?_with_pulseaudio} %{!?_with_pulseaudio:--without-pulseaudio} \
  --with-speex \
  --with-vorbis \
  --without-ffmpeg \
  --without-libmad \
  --enable-closure \
  --enable-new-ldflags \
  --enable-final

%__make %{?_smp_mflags} LIBTOOL=$(which libtool)


%install
%__rm -rf %{buildroot} 
%__make install DESTDIR=%{buildroot}

# unpackaged files
%__rm -f %{buildroot}%{_libdir}/lib*.la
%__rm -f %{buildroot}%{_libdir}/lib*.a
#rm -f %{buildroot}%{_libdir}/libakode_oss_sink.so

# rpmdocs
for file in AUTHORS COPYING NEWS README TODO ; do
  test -s  "$file" && install -p -m644 -D "$file" "rpmdocs/$file"
done


%clean
%__rm -rf %{buildroot} 


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc rpmdocs/* 
%{_bindir}/akodeplay
%{_libdir}/libakode.so.*
%{_libdir}/libakode_alsa_sink.so
%{_libdir}/libakode_mpc_decoder.so
%{_libdir}/libakode_oss_sink.so
%{_libdir}/libakode_xiph_decoder.so

%files devel
%defattr(-,root,root,-)
%{_bindir}/akode-config
%{_includedir}/*
%{_libdir}/libakode.so
%{_libdir}/pkgconfig/*.pc

%if "%{?_with_jack:1}" == "1"
%files jack 
%defattr(-,root,root,-)
%{_libdir}/libakode_jack_sink.so
%endif

# License: GPLv2+
%if "%{?_with_libsamplerate:1}" == "1"
%files libsamplerate
%defattr(-,root,root,-)
%{_libdir}/libakode_src_resampler.so
%endif

%if "%{?_with_pulseaudio:1}" == "1"
%files pulseaudio
%defattr(-,root,root,-)
%{_libdir}/libakode_polyp_sink.so
%endif


%changelog
* Fri Jan 13 2012 Francois Andriot <francois.andriot@free.fr> 2.0.2-6
- Port to TDE 3.5.13
- Based on spec file from Fedora 9 'akode-2.0.2-5'

* Tue Feb 12 2008 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-5 
- gcc43 patch 

* Mon Jan 07 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 2.0.2-4
- -Requires: %%name-pulseaudio (can be added to kde-settings-pulseaudio)

* Sun Dec 23 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.0.2-3
- fix flac113 support

* Sun Dec 23 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.0.2-2
- fix multilib conflicts (#340591)

* Sun Dec 23 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.0.2-1
- akode-2.0.2

* Wed Sep 26 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.0.1-9
- BR: pulseaudio-libs-devel

* Mon Aug 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.0.1-8
- -libsamplerate: License: GPLv2+
- omit oss_sink

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.0.1-7
- Requires: %%{name}-pulseaudio (f8+)
- License: LGPLv2+

* Thu Feb 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.0.1-6
- respin (for flac, fc7+)

* Mon Feb 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 2.0.1-5
- enable pulseaudio support
- Requires: akode-pulseaudio (f7+)

* Thu Dec 14 2006 Rex Dieter <rexdieter[AT]users.sf.net> 2.0.1-4
- enable jack support (subpkg)
- package (GPL'd) libsamplerate-based resampler separately, 
  to keep main pkg LGPL-clean

* Mon Aug 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 2.0.1-2
- fc6 respin

* Mon Aug 07 2006 Rex Dieter <rexdieter[AT]users.sf.net> 2.0.1-1
- 2.0.1

* Fri Jul 21 2006 Rex Dieter <rexdieter[AT]users.sf.net>
- fc6: gcc/glibc respin

* Fri Feb 10 2006 Rex Dieter <rexdieter[AT]users.sf.net> 
- fc5: gcc/glibc respin

* Mon Dec 19 2005 Rex Dieter <rexdieter[AT]users.sf.net> 2.0-1
- 2.0(final)

* Wed Nov 23 2005 Rex Dieter <rexdieter[AT]users.sf.net> 2.0-0.4.rc1
- 2.0rc1 

* Wed Nov 23 2005 Rex Dieter <rexdieter[AT]users.sf.net. 2.0-0.2.b3
- --without-libltdl

* Tue Nov 22 2005 Rex Dieter <rexdieter[AT]users.sf.net> 2.0-0.1.b3
- akode-2.0b3

