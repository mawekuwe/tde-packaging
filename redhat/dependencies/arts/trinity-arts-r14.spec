# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%endif


Name:		trinity-arts
Version:	r14
Release:	1%{?dist}%{?_variant}
License:	GPL
Summary:	aRts (analog realtime synthesizer) - the TDE sound system
Group:		System Environment/Daemons 

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	arts-%{version}.tar.gz

BuildRequires:	cmake >= 2.8
BuildRequires:	tqtinterface-devel
BuildRequires:	audiofile-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	glib2-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:	gsl-devel
BuildRequires:	libvorbis-devel
BuildRequires:	esound-devel
BuildRequires:	jack-audio-connection-kit-devel

Requires:		tqtinterface == %{version}
Requires:		audiofile

%if "%{?_prefix}" == "/usr"
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


%package devel
Group:		Development/Libraries
Summary:	%{name} - Development files
Requires:	%{name} = %{version}-%{release}
%if "%{?_prefix}" == "/usr"
Obsoletes:	arts-devel
%endif

%description devel
Development files for %{name}

%prep
%setup -q -n dependencies/arts

%build
%__mkdir build
cd build
%cmake \
  -DINCLUDE_INSTALL_DIR=%{_includedir}/arts \
  -DPKGCONFIG_INSTALL_DIR=%{_libdir}/pkgconfig \
  -DWITH_ALSA=ON \
  -DWITH_AUDIOFILE=ON \
  -DWITH_VORBIS=ON \
  -DWITH_MAD=OFF \
  -DWITH_ESOUND=ON \
  -DWITH_JACK=ON \
  ..


%__make %{?_smp_mflags}

%install
%__rm -rf %{?buildroot}
%__make install -C build DESTDIR=%{?buildroot}

%clean
%__rm -rf %{?buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING.LIB
%dir %{_libdir}/mcop
%dir %{_libdir}/mcop/Arts
%{_libdir}/mcop/Arts/*
%{_libdir}/mcop/*.mcopclass
%{_libdir}/mcop/*.mcoptype
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la
%{_bindir}/artscat
%{_bindir}/artsd
%{_bindir}/artsdsp
%{_bindir}/artsplay
%{_bindir}/artsrec
%{_bindir}/artsshell
%{_bindir}/artswrapper

%files devel
%defattr(-,root,root,-)
%{_bindir}/mcopidl
%dir %{_includedir}
%{_includedir}/*/
%{_bindir}/artsc-config
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a


%changelog
* Thu Feb 16 2012 Francois Andriot <francois.andriot@free.fr> - r14-1
- Initial build for TDE R14, using 'tqt3' instead of 'qt3'
