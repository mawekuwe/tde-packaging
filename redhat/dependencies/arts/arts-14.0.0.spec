# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_version 14.0.0
%define tde_prefix /opt/trinity

%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_datadir %{tde_prefix}/share

%define tde_tdeincludedir %{tde_includedir}/tde

%define _docdir %{tde_datadir}/doc

Name:		trinity-arts
Epoch:		1
Version:	1.5.10
Release:	%{?!preversion:2}%{?preversion:1_%{preversion}}%{?dist}%{?_variant}
License:	GPL
Summary:	aRts (analog realtime synthesizer) - the TDE sound system
Group:		System Environment/Daemons 

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:	kcmartsrc-pulseaudio

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}

BuildRequires:	cmake >= 2.8
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig

BuildRequires:	audiofile-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	glib2-devel
BuildRequires:	gsl-devel
BuildRequires:	libvorbis-devel

# ESOUND support
%define with_esound 1
BuildRequires:	esound-devel

# JACK support
#  Not on RHEL4 !
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?suse_version}
%define with_jack 1
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}jack-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora}
BuildRequires:	jack-audio-connection-kit-devel
%endif
%if 0%{?suse_version}
BuildRequires:	libjack-devel
%endif
%endif

# LIBTOOL
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}ltdl-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora}
BuildRequires:	libtool-ltdl-devel
%endif
%if 0%{?suse_version}
%if 0%{?suse_version} >= 1220
BuildRequires:	libltdl-devel
%else
BuildRequires:	libtool
%endif
%endif

# MAD support
%ifarch i586 i686 x86_64
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} 
%define with_libmad 1
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:		%{_lib}mad-devel
%endif
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
BuildRequires:		libmad-devel
%endif
%endif
%endif

# Pulseaudio config file
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?suse_version}
%define with_pulseaudio 1
%endif

Requires:		trinity-tqtinterface >= %{tde_version}
Requires:		audiofile

%if "%{?tde_prefix}" == "/usr"
Obsoletes:	arts
%endif

%description
arts (analog real-time synthesizer) is the sound system of TDE.

The principle of arts is to create/process sound using small modules which do
certain tasks. These may be create a waveform (oscillators), play samples,
filter data, add signals, perform effects like delay/flanger/chorus, or
output the data to the soundcard.

By connecting all those small modules together, you can perform complex
tasks like simulating a mixer, generating an instrument or things like
playing a wave file with some effects.

%files
%defattr(-,root,root,-)
%doc COPYING.LIB
%dir %{tde_prefix}
%dir %{tde_bindir}
%dir %{tde_datadir}
%dir %{tde_datadir}/config
%dir %{tde_libdir}
%dir %{tde_libdir}/mcop
%dir %{tde_libdir}/mcop/Arts
%dir %{tde_libdir}/pkgconfig
%dir %{tde_includedir}
%dir %{tde_tdeincludedir}
%{tde_libdir}/mcop/Arts/*
%{tde_libdir}/mcop/*.mcopclass
%{tde_libdir}/mcop/*.mcoptype
%{tde_libdir}/lib*.so.*
%{tde_bindir}/artscat
%{tde_bindir}/artsd
%{tde_bindir}/artsdsp
%{tde_bindir}/artsplay
%{tde_bindir}/artsrec
%{tde_bindir}/artsshell
%{tde_bindir}/artswrapper
# The '.la' files are runtime, not devel !
%{tde_libdir}/lib*.la

%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

##########

%package devel
Group:		Development/Libraries
Summary:	%{name} - Development files
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%if "%{?tde_prefix}" == "/usr"
Obsoletes:	arts-devel
%endif

%description devel
Development files for %{name}

%files devel
%defattr(-,root,root,-)
%{tde_bindir}/mcopidl
# Arts includes are under 'tde' - this is on purpose !
%{tde_tdeincludedir}/arts/
# Artsc includes are not under 'tde'.
%{tde_includedir}/artsc/
%{tde_bindir}/artsc-config
%{tde_libdir}/lib*.so
%{tde_libdir}/pkgconfig/*.pc
%{tde_libdir}/*.a

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

##########

%if 0%{?with_pulseaudio}

%package config-pulseaudio
Group:		System Environment/Daemons
Summary:	%{name} - Default configuration file for Pulseaudio
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description config-pulseaudio
%{summary}

%files config-pulseaudio
%defattr(-,root,root,-)
%{tde_datadir}/config/kcmartsrc

%endif

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

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
  -DWITH_GCC_VISIBILITY=ON \
  \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DBIN_INSTALL_DIR="%{tde_bindir}" \
  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}/arts" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  \
  -DWITH_ALSA=ON \
  -DWITH_AUDIOFILE=ON \
  -DWITH_VORBIS=ON \
  %{?with_libmad:-DWITH_MAD=ON} %{!?with_libmad:-DWITH_MAD=OFF} \
  %{?with_esound:-DWITH_ESOUND=ON} \
  %{?with_jack:-DWITH_JACK=ON} \
  ..

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{?buildroot}
%__make install -C build DESTDIR=%{?buildroot}

# Installs the Pulseaudio configuration file
%if 0%{?with_pulseaudio}
%__install -D -m 644 %{SOURCE1} %{?buildroot}%{tde_datadir}/config/kcmartsrc
%endif


%clean
%__rm -rf %{?buildroot}


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 1:1.5.10-2
- Initial release for TDE R14.0.0
