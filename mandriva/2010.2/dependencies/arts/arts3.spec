%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}
%define oname arts
%define epoch_arts 30000001

# Define short-cuts for libification
%define major	1

%define libname	%mklibname arts %{major}

%define lib_name_orig libarts

Name: arts3
Summary: Arts - Libraries
Version: 1.5.12
Release: %mkrel 1
Epoch: %{epoch_arts}
Group: Graphical desktop/KDE3
License: ARTISTIC BSD GPL_V2 LGPL_V2 QPL_V1.0
BuildRoot: %_tmppath/%name-%version-%release-root
Requires(pre): %{libname} = %{epoch_arts}:%version-%release
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
Patch0: arts-1.5.3-resmgr.patch
Patch2: arts-1.5.3-mcop-msgkill.patch
Patch4: arts-1.5.9-gcc4.3.x-compile.patch
Patch5: kde-3.5.10-acinclude.patch
BuildRequires: kde3-macros
BuildRequires: audiofile-devel
BuildRequires: qt3-devel
BuildRequires: glib2-devel
BuildRequires: alsa-lib-devel
BuildRequires: resmgr-devel
BuildRequires: X11-devel
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%endif
BuildRequires: autoconf >= 1:2.65
BuildRequires:	esound-devel
BuildRequires:	multiarch-utils >= 1.0.3
BuildRequires:	jackit-devel
BuildRequires:  libvorbis-devel
BuildRequires: libtqtinterface-devel >= 3.5.12
BuildConflicts: mas-devel
Obsoletes:	aethera =< 0.9.3-5mdk
Obsoletes: brahms =< 1.02-3mdk
Obsoletes: dotNETStyle =< 0.9.2-2mdk 
Obsoletes: drivetweak-kde- =< 0.9.1-1mdk 
Obsoletes: guarddog =< 1.9.14-1mdk
Obsoletes:  k3b =< 0.5.1-2mdk
Obsoletes: karchiver =< 2.0.5-3mdk
Obsoletes: kdestudio =< 2.0.0-10mdk 
Obsoletes: kdevmon =< 0.4.5-2mdk
Obsoletes: keduca =< 0.4-6mdk
Obsoletes: keurocalc =< 0.5.8-1mdk
Obsoletes:  kfontinst =< 0.10-1mdk
Obsoletes: kgesture =< 0.3-6mdk
Obsoletes: kguitar =< 0.4-2mdk 
Obsoletes: kinkatta =< 1.00-1mdk
Obsoletes: kmag =< 0.7-1mdk
Obsoletes: kmymoney2 =< 0.4-1mdk
Obsoletes: knetfilter =< 2.2.5-1mdk 
Obsoletes: komba2 =< 0.72-1mdk 
Obsoletes: koncd =< 1.0rc2-2mdk
Obsoletes: konnector =< 0.5-4mdk
Obsoletes:	konverse =< 0.2-3mdk
Obsoletes: kover =< 0.8.3-2mdk
Obsoletes: kreatecd =< 1.1.0-2mdk
Obsoletes: krpmbuilder =< 0.2.6-4mdk
Obsoletes: krusader =< 1.01-1mdk
Obsoletes: kshowmail =< 2.2.3-1mdk
Obsoletes: ksnuffle =< 2.2-6mdk
Obsoletes: ksplashml =< 0.92-1mdk
Obsoletes: kstars =< 0.8.5-1mdk
Obsoletes: kstocks =< 2.0.2-8mdk
Obsoletes: ktexmaker2 =< 1.7-2mdk
Obsoletes: ktouch =< 1.0-4mdk
Obsoletes: kuickshow =< 0.8.2-3mdk
Obsoletes:  kwatch =< 2.2.0-1mdk
Obsoletes: kwave =< 0.6.3-3mdk
Obsoletes: kwintv =< 0.8.11-5mdk
Obsoletes: kxicq2 =< 0.7.6-1mdk
Obsoletes: kxmleditor =< 0.7.1-2mdk
Obsoletes: libbrahms0 =< 1.02-3mdk
Obsoletes: libkarchiver2 =< 2.0.5-3mdk
Obsoletes: libkguitar1 =< 0.4-2mdk
Obsoletes: libxmms-kde1 =< 6.5-5mdk
Obsoletes: sakuraplayer =< 1.0.6-1mdk umlmodeller =< 1.0.3-5mdk 
Obsoletes: cervisia =< 1.4.1-7mdk
Obsoletes: kbiff =< 3.5.4-3mdk
Obsoletes:  kcpuload =< 1.90-11mdk
Obsoletes: kdbg =< 1.2.5-1mdk
Obsoletes: kdeaddons3
Obsoletes: kdeadmin3
Obsoletes: kdeartwork3
Obsoletes: kdebindings3
Obsoletes: kdemultimedia3
Obsoletes: kdemultimedia3-aktion
Obsoletes: kdenetwork3
Obsoletes: kdepim3
Obsoletes: kdesdk3
Obsoletes: kdetoys3
Obsoletes: kdeutils3
Obsoletes: kdevelop3
Obsoletes: klogic =< 1.35-1mdk
Obsoletes: klyx =< 2.0-17mdk
Obsoletes: kmago =< 1.1.2-5mdk
Obsoletes: knetload =< 1.91-8mdk
Obsoletes: koffice =< 1.1.1-14mdk
Obsoletes: kpl2 =< 2.3.0-1mdk
Obsoletes: krootwarning =< 8.2-13mdk
Obsoletes: krozat =< 8.2-13mdk
Obsoletes: ksetiwatch =< 2.2.5-1mdk
Obsoletes: ktelnet =< 0.7b1-13mdk
Obsoletes: kvirc =< 2.1.1-5mdk
Obsoletes: libqt2-devel =< 2.3.1-29mdk
Obsoletes: licq-kde =< 1.0.4-2mdk
Obsoletes: qt2-designer =< 2.3.1-29mdk
Obsoletes: qtrans =< 0.1.1-7mdk
Obsoletes: quanta =< 2.0.1-2mdk
Obsoletes: kdelibs-sound 
Obsoletes:	%{libname}-static-devel
Obsoletes:  arts3 < %{epoch_arts}:1.5.3
Provides:	arts3 = %{epoch_arts}:%version-%release
BuildConflicts:	unsermake
Conflicts: arts < 30000001:1.5.10-4
Provides: arts = %epoch_arts:%version-%release

%description
aRts is a short form for "analog realtime synthesizer". The idea of the whole 
thing is to create/process sound using small modules which do certain tasks. 
These may be create a waveform (oscillators), play samples, filter data, add 
signals, perform effects like delay/flanger/chorus, or output the data to the
soundcard.

%files
%defattr(-,root,root,-)
%_kde3_bindir/artscat
%_kde3_bindir/artsd    
%_kde3_bindir/artsplay  
%_kde3_bindir/artsshell    
%_kde3_bindir/artsdsp  
%_kde3_bindir/artsrec   
%_kde3_bindir/artswrapper

#----------------------------------------------------------------------

%package -n %{libname}
Group:      System/Libraries
Summary:    The libraries for arts 
Obsoletes:  libarts2, libarts3
Requires: libtqtinterface >= 3.5.12-1

%description -n %{libname}
Libraries needed for arts.

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root,-)
%_kde3_libdir/*.la
%_kde3_libdir/*.so.*
%dir %_kde3_libdir/mcop/
%_kde3_libdir/mcop/*
%_sysconfdir/ld.so.conf.d/*

#----------------------------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary:	Development files for arts
Requires: %{libname} = %{epoch_arts}:%version-%release
Obsoletes: %{_lib}arts1-devel
Obsoletes: libarts2-devel
Obsoletes: libarts3-devel
Provides: arts-devel
Provides: libarts-devel
Conflicts: arts <= %epoch_arts:1.5.3-5mdv2007

%description devel
Development libraries for arts.

%files devel
%defattr(-,root,root,-)
%_kde3_bindir/artsc-config
%multiarch %_kde3_bindir/*/artsc-config
%_kde3_bindir/mcopidl
%_kde3_libdir/*.so
%_kde3_includedir/*

#----------------------------------------------------------------------

%prep
%setup -q -n %oname-%version
%patch0 -p0 -b .resmgr
%patch2 -p1 -b .msgkill
%patch4 -p1 -b .gcc4.3
%patch5 -p1

%build
# Patch from resmgr needs rebuild builsystem
make -f admin/Makefile.common
QTDIR=%qt3dir
export QTDIR
PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;

%configure_kde3 \
	--without-nas \

%make


%install
rm -fr %buildroot

%makeinstall_std
%multiarch_binaries $RPM_BUILD_ROOT%{_kde3_bindir}/artsc-config
%multiarch_includes $RPM_BUILD_ROOT%{_kde3_includedir}/arts/gsl/gslconfig.h

install -d %buildroot/%_sysconfdir/ld.so.conf.d
cat > %buildroot/%_sysconfdir/ld.so.conf.d/%{libname}.conf <<EOF
%_kde3_libdir
EOF


%clean
rm -fr %buildroot





%changelog
* Thu Feb 03 2011 Tim Williams <tim@my-place.org.uk> 30000001:1.5.12-11mdf2010.2
+ Add Trinity KDE 3.5.12 sources
+ Add libtqtinterface dependencies
- Remove arts-1.5.0-check_tmp_dir.patch and fix_autotools.patch, no longer necessary

* Tue May 04 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 30000001:1.5.10-11mvt2010.1
+ Rebuild

* Sat Jan 16 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 30000001:1.5.10-11mvt2010.0
+ Use automake 1.11 and above
+ Patch for built with autoconf 2.65
+ Fix package group

* Tue Nov 14 2009 Tim Williams <tim@my-place.org.uk> 30000001:1.5.10-10mdv2010.0
- Remove some of the obsoletes which are causing problems

* Fri Nov 13 2009 Tim Williams <tim@my-place.org.uk> 30000001:1.5.10-9mdv2010.0
+ Rebuild for MDV 2010.0

* Sat Mar 28 2009 Anssi Hannula <anssi@mandriva.org> 30000001:1.5.10-8mdv2009.1
+ Revision: 361978
- fix apparent typo in provides/conflicts change of r356949

* Fri Mar 27 2009 Anssi Hannula <anssi@mandriva.org> 30000001:1.5.10-7mdv2009.1
+ Revision: 361677
- fix new obsolete for biarch

* Wed Mar 25 2009 Helio Chissini de Castro <helio@mandriva.com> 30000001:1.5.10-6mdv2009.1
+ Revision: 361121
- The return of undead. Changing name from libarts1-devel to a real arts3-devel

* Tue Mar 17 2009 Nicolas Lécureuil <neoclust@mandriva.org> 30000001:1.5.10-5mdv2009.1
+ Revision: 356949
- Add provides

* Sun Mar 15 2009 Nicolas Lécureuil <neoclust@mandriva.org> 30000001:1.5.10-4mdv2009.1
+ Revision: 355208
- Remove old spec file
- Update to new name
- Change arts to arts3 ( kde3 reintroduction step 1 )

* Sat Feb 28 2009 Anssi Hannula <anssi@mandriva.org> 30000001:1.5.10-3mdv2009.1
+ Revision: 345972
- rebuild due to removed i586 binaries

* Sat Nov 08 2008 Adam Williamson <awilliamson@mandriva.org> 30000001:1.5.10-2mdv2009.1
+ Revision: 300956
- rebuild for xcb changes

* Tue Aug 26 2008 Helio Chissini de Castro <helio@mandriva.com> 30000001:1.5.10-1mdv2009.0
+ Revision: 276164
- Update for probably the last upstream arts from kde3

* Wed Aug 06 2008 Thierry Vignaud <tvignaud@mandriva.com> 30000001:1.5.9-8mdv2009.0
+ Revision: 264319
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jun 02 2008 Helio Chissini de Castro <helio@mandriva.com> 30000001:1.5.9-7mdv2009.0
+ Revision: 214278
- Fix compilations against gcc 4.3.x. Close bug https://qa.mandriva.com/show_bug.cgi?id=41171

  + Funda Wang <fundawang@mandriva.org>
    - rebuild for new qt3

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Rebuild because of qt3 move

* Sat May 03 2008 Helio Chissini de Castro <helio@mandriva.com> 30000001:1.5.9-3mdv2009.0
+ Revision: 200792
- Begin changes for kde. Time to go to /opt
- Added arts.conf on ld.so.conf.d

* Sat Mar 22 2008 Nicolas Lécureuil <neoclust@mandriva.org> 30000001:1.5.9-2mdv2008.1
+ Revision: 189485
- Fix groups ( tks to pterjan)

* Thu Feb 14 2008 Helio Chissini de Castro <helio@mandriva.com> 30000001:1.5.9-1mdv2008.1
+ Revision: 167752
- Last arts ever arrived. 1.5.9. This will be the last update for old codebase and closing the cycle of stable releases of KDE3

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix description-line-too-long
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Oct 23 2007 Nicolas Lécureuil <neoclust@mandriva.org> 30000001:1.5.8-1mdv2008.1
+ Revision: 101650
- Arts 1.5.8 from kde 3.5.8
- Add Patch5, it fixes problems between aRts and Knotify

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - add buildconflict on unsermake as it gets used by default if installed and breaks building

  + Anssi Hannula <anssi@mandriva.org>
    - remove hardcoded packager tag

* Mon May 21 2007 Olivier Blin <oblin@mandriva.com> 30000001:1.5.7-2mdv2008.0
+ Revision: 29295
- build with esound support

* Wed May 16 2007 Helio Chissini de Castro <helio@mandriva.com> 30000001:1.5.7-1mdv2008.0
+ Revision: 27452
- 1.5.7 release

