%define oname kdebindings
%define _disable_final 1

%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define internal_sip 0
%{?_internal_sip: %{expand: %%global internal_sip 1}}

%define java 1

%define lib_major_kdec	1
%define lib_kdec	%mklibname kdec %{lib_major_kdec}

%define lib_major_kjsembed	1
%define lib_kjsembed	%mklibname kde3kjsembed %{lib_major_kjsembed}

%define lib_major_smoke	1
%define lib_smoke	%mklibname smoke %{lib_major_smoke}

%define perl_man3dir    %_mandir

Name: kde3-%{oname}
Summary: Kdebindings
Version: 3.5.12
Release: %mkrel 1
Epoch: 1
Group: Graphical desktop/KDE3
URL: ftp://ftp.kde.org/pub/kde/stable/%version/src/
Source0: ftp://ftp.kde.org/pub/kde/stable/%version/src/%oname-%version.tar.bz2
#Patch0: kdebindings-3.5.8-gcc4-bug21304-workaround.patch
#Patch1: kdebindings-3.5.10-cast-fix.patch 
Patch2: kdebindings-3.5.7-fix-man-dir.patch
Patch3: kdebindings-3.5.7-java-ldflags.patch
Patch4: kdebindings-3.5.7-sinjdoc.patch
Patch5: kde-3.5.10-acinclude.patch
#Patch6: fix_autotools.patch
Patch7: kdebase-3.5.12-move-xdg-menu-dir.patch
Patch8: kdebase-3.5.12-config.patch

License: GPL
BuildRoot: %_tmppath/%oname-%version-%release-root
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%endif
BuildRequires: autoconf >= 1:2.65
BuildRequires: gettext 
BuildRequires: kdelibs3-devel
BuildRequires: kdebase3-devel
BuildRequires: bzip2-devel
BuildRequires: perl-devel
BuildRequires: texinfo
BuildRequires: ruby-devel
BuildRequires: openssl-devel
%if %with java
%if %mdkversion < 200810
BuildRequires: jpackage-utils
%else
BuildRequires: java-rpmbuild
%endif
BuildRequires: java-devel-openjdk
%endif
# External packages now
#BuildConflicts: python-devel


%description
This package contains:
	* dcopjava: DCOP bindings for Java
	* dcopperl: DCOP bindings for Perl
	* kalyptus: C, Objective-C and Java bindings generator
	* koala (optional): KDE bindings for Java JNI to use Qt/KDE classes with Java
	* qtjava (optional): Qt bindings for Java JNI to use Qt/KDE classes with Java
	* ruby-qt: Qt bindings for Ruby

#------------------------------------------------------------

%define lib_smoke_kde %mklibname smokekde 1

%package -n %{lib_smoke_kde}
Summary: KDE generic bindings library
Group: Development/KDE and Qt
Provides:  %{oname}-%{lib_smoke_kde} = %epoch:%version-%release
Obsoletes: %{lib_kdec}-devel < 3.5.1
Obsoletes: %{lib_kdec} < 3.5.1
Obsoletes: libsmoke1 <= 3.5.1


%description -n %{lib_smoke_kde}
KDE generic bindings library.

%if %mdkversion < 200900
%post -n %{lib_smoke_kde} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_smoke_kde} -p /sbin/ldconfig
%endif

%files -n %{lib_smoke_kde}
%defattr(-,root,root)
%_kde3_libdir/libsmokekde.so.*

#------------------------------------------------------------

%define lib_smoke_qt %mklibname smokeqt 1

%package -n %{lib_smoke_qt}
Summary: Qt generic bindings library
Group: Development/KDE and Qt
Provides:  %{oname}-%{lib_smoke_qt} = %epoch:%version-%release
Obsoletes: %{lib_kdec}-devel < 3.5.1
Obsoletes: %{lib_kdec} < 3.5.1
Obsoletes: libsmoke1 <= 3.5.1

%description -n %{lib_smoke_qt}
Qt generic bindings library.

%if %mdkversion < 200900
%post -n %{lib_smoke_qt} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_smoke_qt} -p /sbin/ldconfig
%endif

%files -n %{lib_smoke_qt}
%defattr(-,root,root)
%_kde3_libdir/libsmokeqt.so.*

#------------------------------------------------------------

%package -n smoke-devel
Summary: Header files for libsmoke
Group: Development/KDE and Qt
Requires: %{lib_smoke_qt} = %epoch:%version-%release
Requires: %{lib_smoke_kde} = %epoch:%version-%release
Provides: libsmoke-devel = %epoch:%version-%release
Provides:  %{oname}-smoke-devel = %epoch:%version-%release
Obsoletes: %{lib_smoke}-devel < 3.5.1
Obsoletes: %{lib_kdec}-devel < 3.5.1
Obsoletes: %{lib_kdec} < 3.5.1

%description -n smoke-devel
Smoke devel files.

%files -n smoke-devel
%defattr(-,root,root)
%_kde3_includedir/smoke.h
%_kde3_libdir/libsmokekde.la
%_kde3_libdir/libsmokekde.so
%_kde3_libdir/libsmokeqt.so
%_kde3_libdir/libsmokeqt.la

#------------------------------------------------------------

%package -n kde3-kjsembed
Summary:	KJS Javascript interpreter
Group: Development/KDE and Qt
Conflicts:	%{lib_smoke_kde} <= %{epoch}:3.5.0-2mdk
Obsoletes: kjsembed < 1:3.5.10

%description -n kde3-kjsembed
A library for embedding the KJS Javascript interpreter in application.

%if %mdkversion < 200900
%post -n kde3-kjsembed
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun -n kde3-kjsembed
%clean_menus
%clean_icon_cache hicolor
%endif


%files -n kde3-kjsembed
%defattr(-,root,root)
%_kde3_bindir/kjscmd
# %_kde3_bindir/jsaccess
%_kde3_bindir/embedjs
%_kde3_libdir/kde3/libqprocessplugin.*
%_kde3_libdir/kde3/libjsconsoleplugin.*
# %_kde3_libdir/kde3/libcustomobjectplugin.*
# %_kde3_libdir/kde3/libcustomqobjectplugin.*
%_kde3_libdir/kde3/libimagefxplugin.*
%_kde3_libdir/kde3/libfileitemplugin.*
%_kde3_libdir/kde3/libjavascript.*
%_kde3_datadir/applnk/Utilities/embedjs.desktop
%_kde3_appsdir/embedjs/embedjsui.rc
%_kde3_appsdir/kate/scripts/swaptabs.desktop
%_kde3_appsdir/kate/scripts/swaptabs.js
%_kde3_appsdir/kate/scripts/swaptabs.ui
%_kde3_appsdir/kjsembed/cmdline.js
%_kde3_datadir/services/qprocess_plugin.desktop
%_kde3_datadir/applications/kde/kjscmd.desktop
# %_kde3_datadir/services/customobject_plugin.desktop
# %_kde3_datadir/services/customqobject_plugin.desktop
%_kde3_datadir/servicetypes/binding_type.desktop
%_kde3_datadir/services/imagefx_plugin.desktop
%_kde3_datadir/services/javascript.desktop
%_kde3_datadir/services/kfileitem_plugin.desktop
%_kde3_datadir/icons/*/*/*/embedjs.png
%_mandir/man1/kjscmd.1*

#------------------------------------------------------------

%package -n %lib_kjsembed
Summary:	KJS Javascript interpreter
Group: Development/KDE and Qt
Conflicts: kjsembed < 3.5.1
Provides:  %{oname}-%lib_kjsembed = %epoch:%version-%release

%description -n %lib_kjsembed
A library for embedding the KJS Javascript interpreter in application.

%if %mdkversion < 200900
%postun -n %lib_kjsembed -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %lib_kjsembed -p /sbin/ldconfig
%endif

%files -n %lib_kjsembed
%defattr(-,root,root)
%_kde3_libdir/libkjsembed.so.*

#------------------------------------------------------------

%package -n %lib_kjsembed-devel
Summary:	Header files for KJS Javascript interpreter
Group:		Development/KDE and Qt
Requires: %lib_kjsembed = %epoch:%version-%release
Provides: kjsembed-devel = %epoch:%version-%release
Provides:  %{oname}-%lib_kjsembed-devel = %epoch:%version-%release
Conflicts: %lib_kjsembed < 1:3.5.1

%description -n %lib_kjsembed-devel
Header files for embedding the KJS Javascript interpreter in application.

%files -n %lib_kjsembed-devel
%defattr(-,root,root)
%dir %_kde3_includedir/kjsembed/
%_kde3_includedir/kjsembed/*.h
%_kde3_libdir/libkjsembed.so
%_kde3_libdir/libkjsembed.la

#------------------------------------------------------------

%package -n perl-DCOP
Summary:	Perl DCOP bindings
Group: Development/KDE and Qt
Obsoletes: kdec < 3.5.1
Obsoletes: %{lib_kdec} < 3.5.1
Provides:  %{oname}-perl-DCOP = %epoch:%version-%release

%description -n perl-DCOP
Perl DCOP bindings.

%files -n perl-DCOP
%defattr(-,root,root)
%_mandir/man3/DCOP.*
%perl_sitearch/*.pm
%perl_sitearch/DCOP/Object.pm
%perl_sitearch/auto/DCOP/*.so

#------------------------------------------------------------

%define lib_ruby	%mklibname qtruby

%package -n ruby-qt
Summary: Qt bindings for Ruby
Group:		Development/KDE and Qt
Provides: qtruby = %{epoch}:%{version}-%{release}
Provides:  %{oname}-ruby-qt = %epoch:%version-%release
Obsoletes: %{lib_ruby} < 3.5.1
Obsoletes: %{lib_ruby}1 < 3.5.1
Obsoletes: %{lib_ruby}1-devel < 3.5.1
Obsoletes: qtruby < 3.5.5

%description -n ruby-qt
A binding for Ruby language.

%files -n ruby-qt
%defattr(-,root,root)
%_kde3_bindir/krubyinit
%_kde3_bindir/qtrubyinit
%_kde3_bindir/rbkdeapi
%_kde3_bindir/rbkdesh
%_kde3_bindir/rbqtapi
%_kde3_bindir/rbqtsh
%_kde3_bindir/rbuic
%_kde3_bindir/rbkconfig_compiler
%{_prefix}/lib/ruby/1.8/*
#%{_prefix}/lib/ruby/1.8/*/*

#------------------------------------------------------------

%if %with java

%define libqtjava %mklibname qtjavasupport 1

%package -n %{libqtjava}
Summary: Qt Java support library
Group: Development/KDE and Qt
Provides:  %{oname}-%{libqtjava} = %epoch:%version-%release

%description -n %{libqtjava}
Qt Java support library.

%if %mdkversion < 200900
%post -n %{libqtjava} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libqtjava} -p /sbin/ldconfig
%endif

%files -n %{libqtjava}
%defattr(-,root,root)
%_kde3_libdir/libqtjavasupport.so.*

%package -n qtjava
Summary: Qt bindings for Java
Group: Development/KDE and Qt
Provides: java-qt = %{epoch}:%{version}-%{release}
Provides:  %{oname}-qtjava = %epoch:%version-%release

%description -n qtjava
Qt bindings for Java.

%files -n qtjava
%defattr(0644,root,root,0755)
%doc qtjava/{AUTHORS,COPYING,ChangeLog,INSTALL,NEWS,README,TODO}
%doc qtjava/javalib/{examples,test,tutorial}
%attr(0755,root,root) %{_kde3_bindir}/javalib
%{_jnidir}/qtjava.jar
%{_jnidir}/qtjava-%{version}.jar
%{_kde3_libdir}/libqtjava.so
%doc %{_datadir}/doc/HTML/en/javalib
%{_kde3_datadir}/qtjava
%{_kde3_docdir}/HTML/en/javalib

%package -n qtjava-javadoc
Summary:        Javadoc for qtjava
Group:          Development/Java
Provides:       java-qt-javadoc = %{epoch}:%{version}-%{release}
Provides:  %{oname}-qtjava-javadoc = %epoch:%version-%release

%description -n qtjava-javadoc
Javadoc for qtjava.

%files -n qtjava-javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/qtjava-%{version}
%doc %dir %{_javadocdir}/qtjava

%package -n koala
Summary:	KDE bindings for Java
Group: Development/KDE and Qt
Requires: qtjava = %{epoch}:%{version}-%{release}
Provides:  %{oname}-koala = %epoch:%version-%release

%description -n koala
KDE bindings for Java.

%files -n koala
%defattr(0644,root,root,0755)
%doc kdejava/{AUTHORS,COPYING.LIB,ChangeLog,INSTALL,NEWS,README,TODO}
%doc kdejava/koala/{examples,test}
%attr(0755,root,root) %{_bindir}/koala
%{_jnidir}/koala.jar
%{_jnidir}/koala-%{version}.jar
%attr(-,root,root) %{_libdir}/libkdejava.*

%package -n koala-javadoc
Summary:        Javadoc for koala
Group:          Development/Java
Provides:       java-qt-javadoc = %{version}-%{release}
Provides:  %{oname}-koala-javadoc = %epoch:%version-%release

%description -n koala-javadoc
Javadoc for koala.

%files -n koala-javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/koala-%{version}
%doc %dir %{_javadocdir}/koala
%endif

#------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
%{__mkdir_p} qtjava/javalib/api
%{__mkdir_p} kdejava/koala/api
#%patch0 -p0 -b .gcc4
#%patch1 -p1 -b .cast
%patch2 -p1 -b .mandir
%patch3 -p1
%patch4 -p1
%if %mdkversion >= 201000
%patch5 -p1
#%patch6 -p1
%endif
%patch7 -p0
%patch8 -p0

%build
PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/
export xdg_menudir=%_sysconfdir/xdg/kde/menus

make -f admin/Makefile.common cvs

%configure_kde3 \
%if %with java
   --with-java=%{java_home}
%else
   --without-java
%endif

# kdebindings doesn't like smp compiling
make

%if %with java
pushd qtjava/javalib/api
%{javadoc} -classpath ".." -splitindex -windowtitle  "Qt 3.2 Java api" ../org/kde/qt/*.java
popd

pushd kdejava/koala/api
%{javadoc} -classpath "../koala.jar:../../../qtjava/javalib/qtjava.jar" \
  -author -version -splitindex -windowtitle  "Koala KDE 3.5.9 Java api" ../org/kde/koala/*.java -J-Xmx128m
popd
%endif

%install
if [ -d %buildroot ]; then rm -r %buildroot; fi

%makeinstall_std

%if %with java

%{__rm} %{buildroot}%{_kde3_libdir}/libqtjava.la
%{__rm} %{buildroot}%{_kde3_libdir}/libkdejava.la

%{__rm} %{buildroot}%{_kde3_libdir}/libqtjavasupport.la
%{__rm} %{buildroot}%{_kde3_libdir}/libqtjavasupport.so

%{__rm} %{buildroot}%/usr/lib/python2.6/site-packages/pcop.la
%{__rm} %{buildroot}%/usr/lib/python2.6/site-packages/pcop.so
%{__rm} %{buildroot}%/usr/lib/python2.6/site-packages/pydcop.py

(cd %{buildroot}%{_jnidir} && for jar in *.jar; do %{__mv} ${jar} `/bin/basename ${jar} .jar`-%{version}.jar; done)
(cd %{buildroot}%{_jnidir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

%{__mkdir_p} %{buildroot}%{_javadocdir}/qtjava-%{version}
%{__cp} -a qtjava/javalib/api/* %{buildroot}%{_javadocdir}/qtjava-%{version}
%{__ln_s} qtjava-%{version} %{buildroot}%{_javadocdir}/qtjava

%{__mkdir_p} %{buildroot}%{_javadocdir}/koala-%{version}
%{__cp} -a kdejava/koala/api/* %{buildroot}%{_javadocdir}/koala-%{version}
%{__ln_s} koala-%{version} %{buildroot}%{_javadocdir}/koala

%endif

%clean
if [ -d %buildroot ]; then rm -r %buildroot; fi



%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-1mvt2010.2
+ Rebuild for Trinity
- Remove autoconf patch
+ Add xdg and kdebase build patch
- Remove kdebindings-3.5.8-gcc4-bug21304-workaround.patch
- Remove kdebindings-3.5.10-cast-fix.patch
- Remove jsaccess, libcustomobjectplugin.*, libcustomqobjectplugin.*, customobject_plugin.desktop, customqobject_plugin.desktop
   from files list for kjsembed package. They no longer seem to be built/installed.

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 1:3.5.10-7mvt2010.1
+ Rebuild for MDV 2010.1

* Sun Jan 17 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-6mvt2010.0
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65:patch5
+ Fix automake 1.11 issue:patch6

* Wed Dec 23 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-5mvt2010.0
- Use upper release number to avoid unwanted KDE4 upgrade

* Mon Dec 21 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1:3.5.10-1mdv2010.0
+ Reubilt for 2010.0 release

* Wed Mar 25 2009 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-2mdv2009.1
+ Revision: 361142
- Bump to rebuild against cooker

* Mon Sep 01 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.10-1mdv2009.0
+ Revision: 278727
- Fixed kdebindings 3.5.10 build
- Renamed kjsembed to kde3-kjsembed. Amarok will be fixed later

  + Funda Wang <fundawang@mandriva.org>
    - There is no more qscintilla-qt3

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Rebuild for missing package

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 07 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-2mdv2009.0
+ Revision: 203483
- Move for /opt
- Disable java bindings since is completly mess right now
- Fixed proper build requires, due wrong report from buildsystem
- Mopve for new opt path

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add switch for backports

* Fri Feb 15 2008 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.9-1mdv2008.1
+ Revision: 169021
- Get away from branches. Last KDE 3 arriving !!
- Removed post-3.5.8 patches integrated

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix summary-not-capitalized

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1:3.5.8-4mdv2008.1
+ Revision: 151453
- rebuild for perl-5.10.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Dec 30 2007 Funda Wang <fundawang@mandriva.org> 1:3.5.8-3mdv2008.1
+ Revision: 139508
- rebuild

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1:3.5.8-2mdv2008.1
+ Revision: 127622
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Anssi Hannula <anssi@mandriva.org>
    - buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Kde 3.5.8
      Rediff patches

* Sun Sep 23 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1:3.5.7-13mdv2008.0
+ Revision: 92431
- Fix BuildRequires
- [BUGFIX] Do not show EmbedJS on the menu (Bug #33331)
- [BUGFIX] Do not show kjscmd on the menu (Bug #33332)

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild to filter out autorequires on GCJ AOT objects
    - remove unnecessary Requires(post) on java-gcj-compat

* Mon Aug 20 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-10mdv2008.0
+ Revision: 67996
- Disable python bindings build. External updated ones now are used

* Thu Aug 16 2007 David Walluck <walluck@mandriva.org> 1:3.5.7-9mdv2008.0
+ Revision: 64093
- fix explicit .bz2 extension on kjscmd.1 in file list
- make datadir for qtjava/javalib and kdejava/koala match %%_jnidir
- add additional documentation (examples, test, tutorial) which is not necessarily buildable
- copy the qtjava/designer files into the qtjava package
- build qtjava and koala

* Tue May 29 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-4mdv2008.0
+ Revision: 32557
- Fix buildrequires
- Updated for python qt 3.17.2
- Updated for sip 4.6
- Updated for python kde 3.16
- Removed the excludion of Mandriva Linux on python kde configure. Bad packaging on the past made
  maintainers put Mandriva in a blacklist. No longer necessary.
- Fix qscintilla test. The "multiarch" strategy breaks tests in on more application. We need to be
  sure if this approach worth expend lot of time maintaining package fixes for us only when whole
  world have a better life and have no problems at all
- Fix configure to install in proper place some python kde binaries

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add patch8 : Fix man dir (close bug #23903)
    - Add missing category ( Patch4)

* Wed May 23 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.7-2mdv2008.0
+ Revision: 29971
- Fix kdebindings to build against new qscintilla 1.7.
- 3.5.7 release

  + Funda Wang <fundawang@mandriva.org>
    - BuildRequires python-devel


* Fri Feb 02 2007 Laurent Montel <lmontel@mandriva.com> 3.5.6-1mdv2007.0
+ Revision: 115883
- 3.5.6

* Wed Dec 13 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.5-4mdv2007.1
+ Revision: 96179
- Add patch to compile under x86_64 (improve patch from neoclust)
- Rebuild again new python
- 3.5.5

  + Helio Chissini de Castro <helio@mandriva.com>
    - Introducing 3.5.5 ( stange not be compiled before )
    - Recompiling against new python
    - Fix python macros ( was hardcoded on 2.4 )
    - Renamed qtruby as ruby-qt, matching with other ruby modules naming scheme
    - Removed old invalid qtlib patch

* Sun Aug 06 2006 Laurent Montel <lmontel@mandriva.com> 1:3.5.4-1mdv2007.0
+ Revision: 53355
- New package (2006/08/05 3.5.4-1mdv)
- Remove EmbedJS just test program not necessary into package

* Sat Jul 22 2006 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.3-4mdv2007.0
+ Revision: 41887
- Increase release
- Fixed typo that prevents python-qt install. http://qa.mandriva.com/show_bug.cgi?id=23871

* Fri Jul 21 2006 Helio Chissini de Castro <helio@mandriva.com> 1:3.5.3-3mdv2007.0
+ Revision: 41713
- Disable smp compiling.
- Fix requires for python-qt
- Fixed configure macro
- Updated for main stable upstream version 3.5.3
- Fixed gcc 4 memory compile eater. Thanks to Danny.
- Fixed wrong lib64 detection
- Finally obsoleting external PyQt and sip packages. kdebindings provide up-to-date
  versions.
- Naming match python style now, so now we have python-kde and python-qt and
  python-sip.
- Fix for bug http://qa.mandriva.com/show_bug.cgi?id=17440
- Missing obsoletes
- Initial java package preparation. The current position of libgcj need some changes in
  java-compat tools. No effective package is created now.
- Both archs use multiarch on config.h
- x86 need test qtlib as well
- Bad bad multiproc compilation. kdebindings and cluster don't like distributed comp.
- Add missing patch
- Remodel kdebindings package using 3.5.1 release
- Smoke package is obsoleted in favor to move wrong placed sip runtime files to PyKDE new package
- x86_64 installs works
- kdec is finally obsoleted. The wrong files in there is moved to new packages
  perl-DCOP, python-dcop, lib(%%arch)smokeqt and lib(%%arch)smokekde. this solve a
  old nasty problem with dependencies.
- Create the smoke-devel package. perl-Qt bindings will be built correctly now.
- PyKDE package is created and is built against PyQt package and sip
- Removed all libtoolize bad magic and wrong rpath in favour of pristine source.
- TODO: See if any doc is available to bindings.
- Uploading package ./kdebindings

  + Laurent Montel <lmontel@mandriva.com>
    - Use macro
      Apply patch from neoclust to generate menu entry
    - Fix upgrade
    - 3.5.2
    - Active debug for cooker only
    - Add patch from trem <trem@zarb.org> to build on x86_64
    - Forgot to commit it
    - 3.5.0
      Remove conflict
    - Fix typo
      * Wed Nov 02 2005 Laurent MONTEL <lmontel@mandriva.com> 3.3.5-3mdk
    - Rebuild with new mysql
      * Thu Oct 27 2005 Helio Chissini de Castro <helio@mandriva.com> 3.3.5-2mdk
    - New immodule patch
    - 3.4.92
    - Fix compile
    - remove qtc and qtsharp from spec
    - buildrequires openssl-devel
      Patch from mpol@mandriva.org
    - Add build requires openssl-devel to fix MDV  #17275

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu Apr 21 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-4mdk
- Fix provides

* Tue Apr 19 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-3mdk
- Fix BuildRequires/Compile on x86_64 (thanks Nicolas Chipaux)

* Sun Apr 17 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-2mdk
- Rebuild

* Fri Apr 15 2005 Laurent MONTEL <lmontel@mandriva.com> 3.4.0-1mdk
- 3.4.0
- --enable-new-ldflags

* Fri Mar 18 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Mon Feb 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Thu Dec 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-3mdk
- 3.3.2

* Fri Oct 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-2mdk
- Sync with CVS

* Sat Oct 09 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-1mdk
- 3.3.1

* Sat Sep 11 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-9mdk
- Remove last mono buildRequires

* Wed Sep 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-8mdk
- Remove unused BuildRequires

* Fri Aug 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-7mdk
- Remove unused patch

* Fri Aug 13 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-6mdk
- Disable compile for mono

* Wed Aug 11 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-5mdk
- Fix add/remove debug

* Wed Jul 28 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-4mdk
- Fix spec file

* Thu Jul 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-3mdk
- Fix remove rpath

* Wed Jul 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-2mdk
- Obsoletes smokeqt

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.3-1mdk
- 3.2.3

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-2mdk
- 3.2.2

* Wed Apr 07 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-2mdk
- Fix spec file to using rpmbuildupdate

* Sat Apr 03 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2.1-1mdk
- 3.2.1

* Wed Mar 31 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-2mdk
- Use %%configure
- Use mdkversion

* Tue Feb 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.2-1mdk
- 3.2

