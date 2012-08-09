# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

%define tde_tdeincludedir %{tde_includedir}/kde

%define _docdir %{tde_prefix}/share/doc

Name:		trinity-arts
Version:	3.5.13
Release:	4%{?dist}%{?_variant}
License:	GPL
Summary:	aRts (analog realtime synthesizer) - the KDE sound system
Group:		System Environment/Daemons 

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	arts-%{version}.tar.gz

# TDE 3.5.13: Re-enable lost OSS support
Patch0:		arts-3.5.13-enable_oss.patch

# TDE 3.5.13: Re-enable lost JACK support
Patch1:		arts-3.5.13-enable_jack.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	audiofile-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	glib2-devel
BuildRequires:	gsl-devel
BuildRequires:	libvorbis-devel
BuildRequires:	esound-devel

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}jack-devel
BuildRequires:	%{_lib}ltdl-devel
%else
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libtool-ltdl-devel
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8

Requires:		tqtinterface
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
%patch0 -p1
%patch1 -p1

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

%if 0%{?rhel} || 0%{?fedora}
%__mkdir_p build
cd build
%endif

%cmake \
  -DCMAKE_INSTALL_PREFIX=%{tde_prefix} \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir}/arts \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DPKGCONFIG_INSTALL_DIR=%{tde_libdir}/pkgconfig \
  -DWITH_ALSA=ON \
  -DWITH_AUDIOFILE=ON \
  -DWITH_VORBIS=ON \
  -DWITH_MAD=OFF \
  -DWITH_ESOUND=ON \
  -DWITH_JACK=ON \
  -DCMAKE_SKIP_RPATH="OFF" \
  ..


%__make %{?_smp_mflags}

%install
%__rm -rf %{?buildroot}
%__make install -C build DESTDIR=%{?buildroot}

%clean
%__rm -rf %{?buildroot}

%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :


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

%files devel
%defattr(-,root,root,-)
%{tde_bindir}/mcopidl
%{tde_tdeincludedir}/arts/
%{tde_includedir}/artsc/
%{tde_bindir}/artsc-config
%{tde_libdir}/lib*.so
%{tde_libdir}/pkgconfig/*.pc
%{tde_libdir}/*.a


%changelog
* Fri Dec 16 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Enables JACK support

* Mon Nov 14 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Enables OSS and ESD support

* Thu Nov 03 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Add missing BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Fri Sep 02 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
- Built with future TDE version (3.5.13 + cmake + QT3.3.8d)
