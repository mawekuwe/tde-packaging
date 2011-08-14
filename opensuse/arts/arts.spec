#
# spec file for package arts
#
# Copyright (c) 2011 the Trinity Project (opensuse).
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
  
# Please submit bugfixes or comments via http://bugs.trinitydesktop.org/
#

# norootforbuild


Name:           arts
BuildRequires:  alsa-devel audiofile-devel glib2-devel jack-devel libdrm-devel libjpeg-devel libvorbis-devel libtqt4-devel readline-devel update-desktop-files
BuildRequires:	tde-filesystem
Requires:	tde-filesystem
License:        GPLv2+
Group:          Productivity/Multimedia/Sound/Players
Summary:        Modular Software Synthesizer
PreReq:         permissions
Version:        3.5.12.99
Release:        1
Source0:        %{name}-%{version}.tar.bz2
Source1:        artswrapper.7.gz
Source2:        baselibs.conf
Patch2:         no-informational-messages.diff
Patch5:         arts-vorbis-fix.dif
Patch7:         fortify_source.patch
Patch8:         arts-start-on-demand.diff
Patch9:         avoid_la_files.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A modular software synthesizer that generates realtime audio streams,
includes midi support, is easily extendable, and uses CORBA for
separation of GUI and synthesis.



Authors:
--------
    Stefan Westerfeld <stefan@space.twc.de>

%package devel
License:        GPLv2+
# usefiles /opt/tde/bin/artsc-config /opt/tde/bin/mcopidl
Summary:        Include Files and Libraries mandatory for Development.
Group:          Development/Libraries/Other
Provides:       tdelibs:/opt/tde/include/artsc/artsc.h
Requires:       libtqt4-devel arts = %version glib2-devel jack-devel libogg-devel libvorbis-devel audiofile-devel libstdc++-devel
Requires:       alsa-devel

%description devel
A modular software synthesizer that generates realtime audio streams,
supports MIDI, is easily extendable, and uses CORBA for separation of
the GUI and synthesis.



Authors:
--------
    Stefan Westerfeld <stefan@space.twc.de>

%package gmcop
License:        GPLv2+
# usesubdirs gmcop
Summary:        A Modular Software Synthesizer
Group:          Productivity/Multimedia/Sound/Players

%description gmcop
A modular software synthesizer that generates real-time audio streams,
supports midi, is easily extendable, and uses CORBA for separation of
GUI and synthesis.



Authors:
--------
    Stefan Westerfeld <stefan@space.twc.de>

%prep
%setup -q
%patch2
%patch5
%patch7
%patch8
%patch9

%build
CXXFLAGS="$CXXFLAGS $RPM_OPT_FLAGS -DNDEBUG" CFLAGS="$CXXFLAGS" %cmake_tde -d=build

#%ifarch %ix86
# I trust in arts runtime checking ...
#echo "#define HAVE_X86_SSE 1" >> config.h
#%endif
# broken automake ?
#make -C flow/gsl gslconfig.h
# broken automake ?
#make %{?jobs:-j%jobs}

%make_tde -d=build

%install
%makeinstall_tde -d=build
%ifarch x86_64
mkdir -p $RPM_BUILD_ROOT/%{_tde_libdir}
ln -sf ../lib64/mcop $RPM_BUILD_ROOT/%{_tde_libdir}/mcop
%endif
mkdir -p -m 755 $RPM_BUILD_ROOT/%_mandir/man7
cp %SOURCE1 $RPM_BUILD_ROOT/%_mandir/man7/

%clean
rm -rf $RPM_BUILD_ROOT

%post
%run_ldconfig
%run_permissions

%postun
%run_ldconfig

%post gmcop
%run_ldconfig

%postun gmcop
%run_ldconfig
%verifyscript
%verify_permissions -e %{_tde_bindir}/artswrapper

%files
%defattr(-,root,root,755)
%doc COPYING.LIB COPYING
%dir %{_tde_prefix}
%dir %{_tde_bindir}
%{_tde_bindir}/artscat
%{_tde_bindir}/arts[dpsr]*
%verify(not mode) %{_tde_bindir}/artswrapper
%dir /opt/kde3/%_lib
%{_tde_libdir}/libarts*.so.*
%{_tde_libdir}/libkmedia2*.so.*
%{_tde_libdir}/libmcop.so.*
%{_tde_libdir}/libmcop_mt.so.*
%{_tde_libdir}/libqtmcop.so.*
%{_tde_libdir}/libsoundserver_idl.so.*
%{_tde_libdir}/libx11globalcomm.so.*
# these need to be in the base package for lt_dlopen()
%{_tde_libdir}/*.so
%{_tde_libdir}/mcop
%ifarch x86_64
/opt/tde/lib
%endif
%{_mandir}/man7/artswrapper.7.gz

%files gmcop
%defattr(-,root,root)
%{_tde_libdir}/libgmcop.so.*

%files devel
%defattr(-,root,root)
%{_tde_bindir}/artsc-config
%{_tde_bindir}/mcopidl
%dir %{_tde_includedir}
%{_tde_includedir}/*
%{_tde_libdir}/*.la

%changelog
