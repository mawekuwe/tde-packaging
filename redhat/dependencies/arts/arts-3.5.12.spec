# Default version for this component
%if "%{?version}" == ""
%define version 3.5.12
%endif
%define release 6

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.12 specific building variables
BuildRequires:	autoconf automake libtool m4


Name:		trinity-arts
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}
License:	GPL
Summary:	aRts (analog realtime synthesizer) - the KDE sound system
Group:		System Environment/Daemons 

Vendor:		Trinity Project
URL:		http://www.trinitydesktop.org/
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	arts-%{version}.tar.gz

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

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/"*"/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"

%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
  --disable-rpath \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking \
  --enable-new-ldflags \
  --disable-libmad \
  --with-alsa \
  --enable-final \
  --enable-closure \
  --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}

%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot}

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
%{_includedir}/arts/
%{_includedir}/artsc/
%{_bindir}/artsc-config
%{_libdir}/lib*.so


%changelog
* Fri Sep 16 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-6
- Add support for RHEL 5.

* Mon Sep 12 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-5
- Add "Group" field

* Sun Sep 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-4
- Import to GIT
- Removes cmake stuff, build with autotools only

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-3
- Correct macro to install under "/opt", if desired

* Sat Dec 18 2010  Francois Andriot <francois.andriot@free.fr> - 3.5.12-2
- Add cmake support
- Add some BuildRequires

* Fri Dec 17 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-1
- Add macro _kde3_prefix to define custom installation prefix (ex: /opt/trinity)
- Add '--with-extra-includes=%{_includedir}/tqt'

* Tue Dec 07 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-0
- Initial version

