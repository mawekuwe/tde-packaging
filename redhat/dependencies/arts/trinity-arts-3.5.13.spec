# Default version for this component
%if "%{?version}" == ""
%define version 1.5.10
%endif
%define release 0

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8


Name:		trinity-arts
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}
License:	GPL
Summary:	aRts (analog realtime synthesizer) - the KDE sound system

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

Source0:	arts-%{version}.tar.gz
Prefix:		%{_prefix}

BuildRequires:	tqtinterface-devel
BuildRequires:	audiofile-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	glib2-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:	gsl-devel

Requires:	tqtinterface
Requires:	audiofile

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
Requires:	%{name}
Summary:	%{name} - Development files
%if "%{?_prefix}" == "/usr"
Obsoletes:	arts-devel
%endif

%description devel
Development files for %{name}

%prep
%setup -q -n dependencies/arts

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh

%__mkdir build
cd build
%cmake \
  -DINCLUDE_INSTALL_DIR=%{_includedir}/arts \
  -DPKGCONFIG_INSTALL_DIR=%{_libdir}/pkgconfig \
  -DWITH_MAD=OFF \
  ..

%__make %{?_smp_mflags}

%install
%make_install -C build

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
%exclude %{_libdir}/*.a


%changelog
* Fri Sep 02 2011 Francois Andriot <francois.andriot@free.fr> - 1.5.10-0
- Import to GIT
- Built with future TDE version (3.5.13 + cmake + QT3.3.8d)
