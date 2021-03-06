# Default version for this component
%define tde_pkg k3b
%define tde_version 3.5.13.2

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

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		CD/DVD burning application
Epoch:			1
Version:		1.0.5
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Group:			Applications/Archiving
License:		GPLv2+

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source2:		k3brc

# Fix FTBFS because AVCODEC_MAX_AUDIO_FRAME_SIZE is obsolete
Patch1:			k3b-3.5.13.2-fix_ffmpeg_support.patch

# Legacy RedHat / Fedora patches
# manual bufsize (upstream?)
Patch4:			k3b-1.0.4-manualbufsize.patch
# RHEL6: Fix K3B icon
Patch106:	trinity-k3b-icons.patch


BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel
BuildRequires:	hal-devel
BuildRequires:	gettext
BuildRequires:	libmpcdec-devel
BuildRequires:	libmusicbrainz-devel
BuildRequires:	libvorbis-devel
BuildRequires:	taglib-devel
BuildRequires:	zlib-devel

Requires(post): coreutils
Requires(postun): coreutils

Requires:		%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:		%{name}-common = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?suse_version} >= 1310
Requires:		wodim
REquires:		genisoimage
%else
Requires:		cdrecord
REquires:		mkisofs
%endif
Requires:		dvd+rw-tools

# CDRDAO support
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} >= 5
Requires:		cdrdao
%endif

# DBUS support
#  TQT bindings not available for RHEL4
%if 0%{?rhel} == 4
# Dbus bindings were rebuilt with Qt support
BuildRequires:	dbus-devel >= 0.22-12.EL.9p1
Requires:		dbus-qt >= 0.22-12.EL.9p1
%else
BuildRequires:	trinity-dbus-tqt-devel >= 1:0.63
Requires:		trinity-dbus-tqt >= 1:0.63
%endif

# SNDFILE support
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} >= 4
%define with_sndfile 1
BuildRequires:	libsndfile-devel
%endif

# SAMPLERATE support
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} >= 4
%define with_samplerate 1
BuildRequires:	libsamplerate-devel
%endif

# DVDREAD support
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} >= 4
%define with_dvdread 1
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}dvdread-devel
%else
BuildRequires:	libdvdread-devel
%endif
%endif

# FLAC support
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos}
BuildRequires:	libflac-devel
BuildRequires:	libflac++-devel
%else
BuildRequires:	%{_lib}flac-devel
BuildRequires:	%{_lib}flac++-devel
%endif
%else
BuildRequires:	flac-devel
%endif

# MAD support
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
%define with_libmad 1
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}mad-devel
%endif
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
BuildRequires:	libmad-devel
%endif
%endif

# LAME support
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
%define with_lame 1
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos}
BuildRequires:	liblame-devel
%else
BuildRequires:	%{_lib}lame-devel
%endif
%endif
%if 0%{?suse_version}
BuildRequires:	libmp3lame-devel
%endif
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:	lame-devel
%endif
%endif

# FFMPEG support
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
%define with_ffmpeg 1
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	%{_lib}ffmpeg-devel
%endif
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
BuildRequires:	ffmpeg-devel
%endif
%endif


%description
K3b provides a comfortable user interface to perform most CD/DVD
burning tasks. While the experienced user can take influence in all
steps of the burning process the beginner may find comfort in the
automatic settings and the reasonable k3b defaults which allow a quick
start.


%files
%defattr(-,root,root,-)
%doc AUTHORS README COPYING TODO ChangeLog
%{tde_bindir}/k3b
%{tde_tdelibdir}/kfile_k3b.la
%{tde_tdelibdir}/kfile_k3b.so
%{tde_tdelibdir}/kio_videodvd.la
%{tde_tdelibdir}/kio_videodvd.so
%{tde_tdelibdir}/libk3balsaoutputplugin.la
%{tde_tdelibdir}/libk3balsaoutputplugin.so
%{tde_tdelibdir}/libk3bartsoutputplugin.la
%{tde_tdelibdir}/libk3bartsoutputplugin.so
%{tde_tdelibdir}/libk3baudiometainforenamerplugin.la
%{tde_tdelibdir}/libk3baudiometainforenamerplugin.so
%{tde_tdelibdir}/libk3baudioprojectcddbplugin.la
%{tde_tdelibdir}/libk3baudioprojectcddbplugin.so
%{tde_tdelibdir}/libk3bexternalencoder.la
%{tde_tdelibdir}/libk3bexternalencoder.so
%{tde_tdelibdir}/libk3bflacdecoder.la
%{tde_tdelibdir}/libk3bflacdecoder.so
%if 0%{?with_sndfile}
%{tde_tdelibdir}/libk3blibsndfiledecoder.la
%{tde_tdelibdir}/libk3blibsndfiledecoder.so
%endif
%{tde_tdelibdir}/libk3bmpcdecoder.la
%{tde_tdelibdir}/libk3bmpcdecoder.so
%{tde_tdelibdir}/libk3boggvorbisdecoder.la
%{tde_tdelibdir}/libk3boggvorbisdecoder.so
%{tde_tdelibdir}/libk3boggvorbisencoder.la
%{tde_tdelibdir}/libk3boggvorbisencoder.so
%{tde_tdelibdir}/libk3bsoxencoder.la
%{tde_tdelibdir}/libk3bsoxencoder.so
%{tde_tdelibdir}/libk3bwavedecoder.la
%{tde_tdelibdir}/libk3bwavedecoder.so
%lang(en) %{tde_tdedocdir}/HTML/en/k3b/


##########

%package common
Summary:		Common files of %{name}
Group:			Applications/Archiving
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15 || 0%{?mgaversion} || 0%{?mdkversion}
BuildArch: noarch
%endif

%description common
%{summary}.

%files common
%defattr(-,root,root,-)
%{tde_tdeappdir}/k3b.desktop
%{tde_datadir}/applnk/.hidden/k3b-cue.desktop
%{tde_datadir}/applnk/.hidden/k3b-iso.desktop
%{tde_datadir}/apps/k3b/
%{tde_datadir}/apps/konqsidebartng/virtual_folders/services/videodvd.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_audiocd_rip.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_cd_copy.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_dvd_copy.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_handle_empty_cd.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_handle_empty_dvd.desktop
%{tde_datadir}/apps/konqueror/servicemenus/k3b_videodvd_rip.desktop
%{tde_datadir}/config/k3brc
%{tde_datadir}/mimelnk/application/x-k3b.desktop
%{tde_datadir}/icons/hicolor/*/apps/k3b.png
%{tde_datadir}/services/kfile_k3b.desktop
%{tde_datadir}/services/videodvd.protocol
%{tde_datadir}/sounds/k3b_error1.wav
%{tde_datadir}/sounds/k3b_success1.wav
%{tde_datadir}/sounds/k3b_wait_media1.wav


%post common
touch --no-create %{tde_datadir}/icons/hicolor ||:

%postun common
if [ $1 -eq 0 ] ; then
  touch --no-create %{tde_datadir}/icons/hicolor &> /dev/null
  gtk-update-icon-cache %{tde_datadir}/icons/hicolor &> /dev/null || :
  update-desktop-database %{tde_appdir} -q &> /dev/null
fi

%posttrans common
gtk-update-icon-cache %{tde_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database %{tde_appdir} -q &> /dev/null

##########

%package libs
Summary:		Runtime libraries for %{name}
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description libs
%{summary}.

%files libs
%defattr(-,root,root,-)
%{tde_libdir}/libk3b.so.3
%{tde_libdir}/libk3b.so.3.0.0
%{tde_libdir}/libk3bdevice.so.5
%{tde_libdir}/libk3bdevice.so.5.0.0

%post libs
/sbin/ldconfig

%postun libs
/sbin/ldconfig

##########

%package devel
Summary:		Files for the development of applications which will use %{name} 
Group:			Development/Libraries
Requires:		%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/*.h
%{tde_libdir}/libk3b.so
%{tde_libdir}/libk3bdevice.so

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

##########

%if 0%{?with_libmad}
%package plugin-mad
Summary:		The MAD plugin for K3B
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-mad
%{summary}.

MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2  extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II,
and Layer III a.k.a. MP3) are fully implemented.

%files plugin-mad
%defattr(-,root,root,-)
%{tde_tdelibdir}/libk3bmaddecoder.la
%{tde_tdelibdir}/libk3bmaddecoder.so
%endif

##########

%if 0%{?with_lame}
%package plugin-lame
Summary:		The LAME plugin for K3B
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-lame
%{summary}.

Personal and commercial use of compiled versions of LAME (or any other mp3
encoder) requires a patent license in some countries.

This package is in tainted, as MP3 encoding is covered by software patents.

%files plugin-lame
%defattr(-,root,root,-)
%{tde_tdelibdir}/libk3blameencoder.la
%{tde_tdelibdir}/libk3blameencoder.so
%endif

##########

%if 0%{?with_ffmpeg}
%package plugin-ffmpeg
Summary:		The FFMPEG plugin for K3B
Group:			System Environment/Libraries
Requires:		%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-ffmpeg
%{summary}.

ffmpeg is a hyper fast realtime audio/video encoder, a streaming server
and a generic audio and video file converter.

%files plugin-ffmpeg
%defattr(-,root,root,-)
%{tde_tdelibdir}/libk3bffmpegdecoder.la
%{tde_tdelibdir}/libk3bffmpegdecoder.so
%endif

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%patch1 -p1 -b .ffmpeg
%patch4 -p1 -b .manualbufsize
%patch106 -p1 -b .desktopfile

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

# FFMPEG trick ...
if [ -d /usr/include/ffmpeg ]; then
	export CXXFLAGS="${RPM_OPT_FLAGS} -I/usr/include/ffmpeg"
fi

# Notice: extra-includes is required to find arts headers
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
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  \
  --with-extra-includes=%{tde_includedir} \
  \
  --with-k3bsetup=no \
  --without-cdrecord-suid-root \
  --with-oggvorbis \
  --with-flac \
  %{?with_samplerate:--with-external-libsamplerate} \
  %{?with_dvdread:--with-libdvdread} %{?!with_dvdread:--without-libdvdread} \
  --with-musicbrainz \
  %{?with_sndfile:--with-sndfile} %{?!with_sndfile:--without-sndfile} \
  %{?with_ffmpeg:--with-ffmpeg} %{?!with_ffmpeg:--without-ffmpeg} \
  %{?with_lame:--with-lame} %{?!with_lame:--without-lame} \
  %{?with_libmad:--with-libmad} %{?!with_libmad:--without-libmad} \
  --with-musepack \
  --without-resmgr \
  --with-hal

# Strange behaviour on RHEL4 ...
%if 0%{?rhel} == 4
%__sed -i "libk3b/jobs/Makefile" -e "/^am_libjobs_la_final_OBJECTS/ s/ lo//g"
%__mkdir_p "libk3bdevice/.libs"
%__ln_s . "libk3bdevice/.libs/.libs"
%endif

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}
%__install -D -m 644 -p %{SOURCE2} %{buildroot}%{tde_datadir}/config/k3brc

# remove the .la files
%__rm -f %{buildroot}%{tde_libdir}/libk3b*.la 


%clean
%__rm -rf %{buildroot}


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1:1.0.5-1
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2

* Sun Jan 06 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.1-2
- Enables FFMPEG support
- Enables LAME support
- Enables MAD support

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13.1-1
- Initial release for TDE 3.5.13.1
- Remove requirement for resmgr

* Sat Aug 04 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-5
- Add support for Mageia 2 and Mandriva 2011
- Fix DBUS-TQT detection that prevented HAL support
- Adds requirement for resmgr

* Wed May 09 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Removes i18 files (built separately)

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Rebuilt for Fedora 17
- Fix compilation with GCC 4.7 [Bug #958]

* Sat Nov 05 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Updates BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sun Sep 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
