# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_datadir %{tde_prefix}/share

%define tde_tdeincludedir %{tde_includedir}/tde

%define _docdir %{tde_datadir}/doc

Name:		trinity-arts
Version:	3.5.13.2
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:	GPL
Summary:	aRts (analog realtime synthesizer) - the TDE sound system
Group:		System Environment/Daemons 

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Source1:	kcmartsrc-pulseaudio

BuildRequires:	trinity-tqtinterface-devel >= %{version}
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
%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} 
%define with_libmad 1
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:		%{_lib}mad-devel
%endif
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel}
BuildRequires:		libmad-devel
%endif
%endif

# Pulseaudio config file
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?rhel} >= 6 || 0%{?fedora} || 0%{?suse_version}
%define with_pulseaudio 1
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8

Requires:		trinity-tqtinterface >= %{version}
Requires:		audiofile

%if "%{?tde_prefix}" == "/usr"
Obsoletes:	arts
%endif

%description
arts (analog real-time synthesizer) is the sound system of KDE 3.

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
%dir %{tde_libdir}/mcop
%dir %{tde_libdir}/mcop/Arts
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}

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
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}


%build
unset QTDIR || : ; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
%__mkdir_p build
cd build
%endif

%cmake \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DBIN_INSTALL_DIR="%{tde_bindir}" \
  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}/arts" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  -DWITH_ALSA=ON \
  -DWITH_AUDIOFILE=ON \
  -DWITH_VORBIS=ON \
  %{?with_libmad:-DWITH_MAD=ON} %{!?with_libmad:-DWITH_MAD=OFF} \
  %{?with_esound:-DWITH_ESOUND=ON} \
  %{?with_jack:-DWITH_JACK=ON} \
  -DCMAKE_SKIP_RPATH=OFF \
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
* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2

