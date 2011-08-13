#
# spec file for package kdelibs3
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild


Name:           kdelibs3
BuildRequires:  OpenEXR-devel arts-devel aspell-devel cups-devel fam-devel flac-devel krb5-devel
BuildRequires:  libart_lgpl-devel libidn-devel libsndfile libtiff-devel
BuildRequires:  libxslt-devel openldap2-devel pcre-devel qt3-devel sgml-skel
BuildRequires:  db-devel libacl-devel libattr-devel unsermake update-desktop-files utempter
BuildRequires:  unzip
%if %suse_version > 1020
BuildRequires:  avahi-compat-mDNSResponder-devel fdupes libbz2-devel libjasper-devel
%else
BuildRequires:  libjasper mDNSResponder-devel
%endif
%if %suse_version > 1000
BuildRequires:  libdrm-devel
%endif
Url:            http://www.kde.org
License:        BSD3c(or similar) ; GPLv2+ ; LGPLv2.1+
Group:          System/GUI/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        KDE Base Libraries
Version:        3.5.10
Release:        47
Obsoletes:      kde3-i18n kups keramik kdelibs3-cups kdelibs3-33addons kdepim3-networkstatus
Provides:       kups keramik kdelibs3-cups kdelibs3-33addons kdepim3-networkstatus
Provides:       kdelibs3_base = 3.3
# bug437293
%ifarch ppc64
Obsoletes:      kdelibs3-64bit
%endif
#
Requires:       qt3 >= %( echo `rpm -q --queryformat '%{VERSION}' qt3`)
Requires:       openssl kdelibs3-default-style
%if %suse_version > 1020
Requires:       hicolor-icon-theme
%endif
%if %suse_version > 1000
Recommends:     ispell enscript
%endif
%if %suse_version > 1010
Requires:       sudo
%endif
Source0:        kdelibs-%{version}.tar.bz2
Source2:        do_make
Source3:        baselibs.conf
Source4:        api_docu_description
Source6:        kde3rc
Source7:        common_options
# svn export svn://anonsvn.kde.org/home/kde/branches/KDE/3.5/kde-common/admin
Source8:        admin.tar.bz2
Source9:        cr16-filesys-file_broken.png
Source10:       kdemm-20050330.tar.bz2
Source11:       10888-bt.tar.gz
Source12:       mimetype-icons.tar.bz2
Source14:       vnd.openxmlformats-officedocument.wordprocessingml.document.desktop
Source15:       vnd.openxmlformats-officedocument.presentationml.presentation.desktop
Source16:       vnd.openxmlformats-officedocument.spreadsheetml.sheet.desktop
Patch0:         3_5_BRANCH.diff
Patch1:         kdeversion.diff
Patch2:         admin.diff
Patch3:         show-distribution.diff
Patch5:         applications.menu-fallback.diff
Patch7:         stat-on-media.diff
Patch8:         kmimelist.diff
Patch9:         x-kde-InitialPreference.diff
Patch10:        disable-idn-support.diff
Patch11:        silence.diff
Patch12:        smooth-scrolling.diff
Patch13:        rubberband-selection.diff
Patch15:        add-suse-translations.diff
Patch16:        kde3rc.dif
Patch17:        artwork.diff
Patch26:        mimetype-changes.diff
Patch27:        noauto-package.diff
Patch29:        prefer_distribution_settings.dif
Patch34:        allow-man-setgid.diff
Patch40:        clever-menu.diff
Patch43:        fileshare.diff
Patch44:        fontconfig-reverse-lookup.diff
Patch45:        limit-max-image-size.diff
Patch50:        fix-gnome-help-support.diff
Patch950:       fix-gnome-help-support_legacy.diff
Patch52:        kdeprint-restart-cupsd.diff
Patch54:        kdemm.diff
Patch55:        fix-kdemm-build.diff
Patch56:        fix-dcopidlng-within-kdelibs-build.diff
Patch57:        kdemm-filepreview.diff
Patch60:        fix-qxembed.diff
Patch65:        integrate-global-pixmaps-new.diff
Patch66:        integrate-global-pixmaps-10.1.diff
Patch70:        ktip-icon-hack.diff
Patch80:        CATALOG.kdelibs3.diff
Patch81:        xml-catalog.diff
Patch83:        kdelibs3-gcc-4.1-miscompile.diff
Patch85:        desktop-translations.diff
Patch86:        use-xauthlocalhostname.diff
Patch88:        mozilla-sliders.patch
Patch89:        kdeprint-utf8.diff
Patch90:        kimproxy-warning.diff
Patch95:        kdelibs_networkstatus_branch2.diff
Patch97:        autostart-spec.diff
Patch105:       kdelibs3-hicolor-scalable-sizes.patch
Patch106:       use-mediamanager.diff
Patch108:       patch-mimetype-iconnames.diff
Patch109:       fix-kerberos-printing.diff
Patch110:       printpreview.patch
Patch111:       kfile-beagle.diff
Patch112:       xinerama.patch
Patch113:       kremoteencoding-utf8.diff
Patch114:       no-progress-for-beagle-status-query.diff
Patch117:       kickoff-drop-shadow.diff
Patch122:       disable-samba-dialog-without-smb.diff
Patch123:       lpoptions-cups-1.2.diff
Patch124:       spellcheck-default-utf8.diff
Patch125:       kde4-applications.diff
Patch126:       avahi-pidfile.diff
Patch127:       x-jar-desktop.diff
Patch128:       google-mail.diff
Patch129:       default-useragent.diff
Patch130:       kwalletd-try-open.diff
Patch131:       textcompletion-editor.diff
Patch132:       no-debug-by-default.diff
Patch133:       flash-player-non-oss.diff
Patch134:       bundle-locale-help.diff
Patch149:       networkstatus.diff
Patch150:       kdesu-settings.diff
Patch152:       bug-399296_ftphandling-fix.diff
Patch153:       bug-382959_kabc_fix_vcardparser.patch
Patch154:       r874968-ebay-crash.diff
Patch155:       gcc44.diff
Patch156:       fix-macmenu.patch
Patch157:       ignore-inline-menu.diff
Patch158:       bnc557126.diff
Patch159:       xmlhttprequest_3.x.diff
Patch160:       kdecode_fakes_include.diff
Patch161:       gcc45.diff
Patch162:       arts-acinclude.patch
Patch163:       kdelibs-3.5.10-ossl-1.x.patch
Patch164:       light_v_2_scrollbar_patch.patch

Patch201:       kdelibs-3.5.4-CVE-2009-1690.patch
Patch203:       kdelibs-3.5.10-latex-syntax-kile-2.0.3.patch
Patch204:       kdelibs-3.5.10-CVE-2009-2702.patch
Patch205:       kdelibs-3.5.10-cve-2009-2537-select-length.patch
Patch206:       kdelibs-3.5.10-cve-2009-1725.patch
Patch207:       kdelibs-3.5.10-cve-2009-1698.patch

Patch210:       kdelibs-3.5.10-kio.patch
Patch211:       oom_score_adj.patch
Patch212:       kcontrol_crash_patch.diff

%description
This package contains kdelibs, one of the basic packages of the K
Desktop Environment. It contains the necessary libraries for the KDE
desktop.

This package is absolutely necessary for using KDE.

%package arts
License:        BSD3c(or similar) ; GPLv2+ ; LGPLv2.1+
Summary:        KDE aRts support
Group:          System/GUI/KDE
Provides:       kdelibs3:/opt/kde3/bin/artsmessage
# bug437293
%ifarch ppc64
Obsoletes:      kdelibs3-arts-64bit
%endif
#
Requires:       arts >= %( echo `rpm -q --queryformat '%{VERSION}' arts`)
%if %suse_version > 1000
Recommends:     kdemultimedia3-arts
%endif

%description arts
This package contains bindings and gui elements for using aRts sound
daemon.

%package default-style
License:        BSD3c(or similar) ; GPLv2+ ; LGPLv2.1+
Summary:        The default KDE style
Group:          System/GUI/KDE
Provides:       kdelibs3:/opt/kde3/%_lib/libkdefx.so.4

%description default-style
This package contains the Plastik widget style and libkdefx. It only
depends on Qt, not the KDE libraries.

%package doc
License:        BSD3c(or similar) ; GPLv2+ ; LGPLv2.1+
Summary:        Documentation for KDE Base Libraries
Group:          System/GUI/KDE
Provides:       kdelibs3:/opt/kde3/share/apps/ksgmltools2
Provides:       kdelibs3_doc
Requires:       sgml-skel libxml2
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat} /usr/bin/xmlcatalog /usr/bin/edit-xml-catalog
PreReq:         sed grep awk

%description doc
This package contains the core environment and templates for the KDE
help system.

%package devel
License:        BSD3c(or similar) ; GPLv2+ ; LGPLv2.1+
# usefiles /opt/kde3/bin/dcopidl /opt/kde3/bin/dcopidl2cpp /opt/kde3/bin/kdb2html /opt/kde3/bin/preparetips 
Requires:       qt3-devel libvorbis-devel kdelibs3 = %version autoconf automake libxslt-devel libxml2-devel libart_lgpl-devel libjpeg-devel 
# next line from kde3-devel-packages macro
Requires:       kdelibs3-doc libtiff-devel openssl-devel update-desktop-files
%if %suse_version > 1000
Requires:       libdrm-devel dbus-1-qt3-devel
%else
Requires:       dbus-1-qt
%endif
Requires:       libattr-devel libacl-devel
%if %suse_version > 1020
Requires:       avahi-compat-mDNSResponder-devel libbz2-devel
%else
Requires:       mDNSResponder-devel
%endif
Requires:       kdelibs3-arts
Summary:        KDE Base Package: Build Environment
Group:          System/GUI/KDE
Requires:       fam-devel pcre-devel libidn-devel arts-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
  echo %suse_version
%setup -q -n kdelibs-%{version}
%patch0
%patch1
%patch3
%patch5
%patch7
%patch10
%patch11
%patch12
%patch13
%patch15
%patch16
%patch17
%patch26
%patch27
%patch29
#%patch43
#disable it because of BIC
#%patch45
%if %suse_version > 1020
%patch50
%else
%patch950
%endif
%patch52
%patch34
%patch44
%patch40
%patch8
%patch9
tar xfvj %SOURCE10
# TODO!
%patch54
%patch55
%patch56
%patch57
%patch60
# 10.2 goes back to the version without suseadds
%if %suse_version > 1010
%patch65
%else
%if %suse_version > 1000
%patch66
%else
%patch65
%endif
%endif
%patch70
rm -rf admin
bunzip2 -cd %{SOURCE8} | tar xfv - --exclude=.cvsignore --exclude=CVS
install -m 755 %{SOURCE2} admin
%patch2
%patch80 -p 1
%patch81
%if %suse_version > 1000
%patch83
%endif
%patch85
%patch86
%patch88
%patch89
%patch90
%patch95
%patch97
%if %suse_version < 1030
%patch105 -p 1
%endif
%patch106
%patch108
%patch109
%patch110
%patch111
%patch112
%patch113
%patch114
%patch117
%patch122
%if %suse_version > 1010
%patch123
%endif
%patch124
%patch125
%patch126
%patch127
%patch128
%patch129
%patch130
%patch131
%patch132
%if %suse_version > 1020
%patch133
%patch134
%endif
%patch149
%patch150
%patch152
%patch153
%patch154
%patch155
%patch156
%if %suse_version > 1110
%patch157
%endif
%patch158
%patch159
%patch160
%patch161
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch201 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206
%patch207 -p1
%patch210 -p1
%patch211 -p1
%patch212

tar xfvj %SOURCE12
#
# define KDE version exactly
#
myrelease=$(echo %release | cut -d. -f-1)
sed 's,#define KDE_VERSION_STRING "\(.*\)",#define KDE_VERSION_STRING "\1 \\"release '$myrelease'\\"",' kdecore/kdeversion.h > kdecore/kdeversion.h_ && mv kdecore/kdeversion.h_ kdecore/kdeversion.h
#
# create build enviroment
# 
UNSERMAKE=yes make -f admin/Makefile.common cvs

%build
export PATH=$PWD/admin/:$PATH
FINAL="--enable-final"
CFLAGS="$CFLAGS -fno-strict-aliasing"
CXXFLAGS="$CXXFLAGS -fno-strict-aliasing"
%ifarch armv4l
  FINAL=""
  CXXFLAGS="$CXXFLAGS -O0"
%endif
   FLAGS="$FLAGS --with-pcsc-dir=/usr "
   FLAGS="$FLAGS --disable-rpath"
  OPTIONS="$FLAGS $FINAL \
       --prefix=/opt/kde3 \
       --with-qt-dir=/usr/lib/qt3 \
       --enable-threading \
       --enable-mt \
       --with-xinerama \
       --with-ssl-dir=/usr/ssl \
       --mandir=%_mandir \
       --sysconfdir=%_sysconfdir \
       --enable-new-ldflags"
  #
  # common_options
  #
  sed -e 's,@_lib@,%_lib,g' -e "s,@configkde@,$OPTIONS,g" \
    %{SOURCE7} > ../common_options
  . ../common_options
  rm -rf $RPM_BUILD_ROOT
  export PATH=/opt/kde3/bin:$PATH
  if [ %_lib = lib64 ]; then
        EXTRA_OPTIONS="--enable-libsuffix=64"
  fi
%if %is_plus
  EXTRA_OPTIONS="$EXTRA_OPTIONS --enable-dnotify"
%endif
export path_sudo=/usr/bin/sudo
  #
  # define the distribution exactly
  #
  test -e /.buildenv && . /.buildenv
%if %is_plus
  # supplementary package
  DISTRI="openSUSE $BUILD_DISTRIBUTION_VERSION UNSUPPORTED"
%else
  # official build on released and maintained products
  DISTRI="openSUSE $BUILD_DISTRIBUTION_VERSION"
%endif
  sed 's,#define KDE_VERSION_STRING "\(.*\)",#define KDE_VERSION_STRING "\1 '"$ADD_VERSION"'",' kdecore/kdeversion.h > kdecore/kdeversion.h_ && mv kdecore/kdeversion.h_ kdecore/kdeversion.h
  # find MIT kerberos
  export PATH=/usr/lib/mit/bin:$PATH
  # fast-malloc is not needed anymore
  ./configure $configkde $EXTRA_OPTIONS \
    --enable-fast-malloc=no \
    --with-distribution="$DISTRI"
do_make %{?jobs:-j %jobs} 
#
xmlcatbin=/usr/bin/xmlcatalog
# CATALOG=docbook-simple.xml
# $xmlcatbin --noout --create $CATALOG
# $xmlcatbin --noout --add "public" \
#   "-//OASIS//DTD Simplified DocBook XML V1.0//EN" \
#   "file://%{xml_mod_dtd_dir}/sdocbook.dtd" $CATALOG
# $xmlcatbin --noout --add "system" \
#   "http://www.oasis-open.org/docbook/xml/simple/1.0/sdocbook.dtd" \
#   "file://%{xml_mod_dtd_dir}/sdocbook.dtd" $CATALOG
%define FOR_ROOT_CAT for-catalog-%{name}-%{version}.xml
CATALOG=/opt/kde3/share/apps/ksgmltools2/customization/catalog.xml
rm -f %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --create %{FOR_ROOT_CAT}.tmp
# $xmlcatbin --noout --add "delegateSystem" \
#   "http://www.oasis-open.org/docbook/xml/simple/" \
#   "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegatePublic" \
  "-//KDE//DTD DocBook XML V4.2" \
  "file://$CATALOG" %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegatePublic" \
  "-//KDE//ELEMENTS" \
  "file://$CATALOG" %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegatePublic" \
  "-//KDE//ENTITIES" \
  "file://$CATALOG" %{FOR_ROOT_CAT}.tmp
# Create tag
sed '/<catalog/a\
  <group id="%{name}-%{version}">
/<\/catalog/i\
  </group>' \
  %{FOR_ROOT_CAT}.tmp > %{FOR_ROOT_CAT}

%install
  . ../common_options
  mkdir -p $RPM_BUILD_ROOT/etc/opt/kde3/ 
  install -m 0644 ../common_options \
        $RPM_BUILD_ROOT/etc/opt/kde3/common_options
  export PATH=$PWD/admin/:$PATH
  do_make DESTDIR=$RPM_BUILD_ROOT $INSTALL_TARGET
  mkdir -p $RPM_BUILD_ROOT/opt/kde3/share/config.kcfg
  install -D %SOURCE9 $RPM_BUILD_ROOT/opt/kde3/share/icons/crystalsvg/16x16/filesystems/file_broken.png
  mv $RPM_BUILD_ROOT/etc/xdg/menus/applications.menu \
     $RPM_BUILD_ROOT/etc/xdg/menus/applications.menu.kde
  #
  # lib64 compatibility symlink
  #
%ifarch x86_64 ppc64 s390x mips64 sparc64
    mkdir -p $RPM_BUILD_ROOT/opt/kde3/lib/kde3/
    ln -sf ../../lib64/kde3/plugins \
         $RPM_BUILD_ROOT/opt/kde3/lib/kde3/plugins-lib64
%endif
  #
  # add missing directories
  #
  for i in Applications Development Editors Edutainment Games Graphics Internet Multimedia Office Settings System Toys Utilities WordProcessing; do
    install -d -m 0755 $RPM_BUILD_ROOT/opt/kde3/share/applnk/$i
  done
  rm -f locale.list
  for i in $(find /usr/share/locale -mindepth 1 -maxdepth 1 -type d | sed 's:/usr/share/locale/::'); do
    install -d -m 755 $RPM_BUILD_ROOT/opt/kde3/share/locale/$i
    install -d -m 755 $RPM_BUILD_ROOT/opt/kde3/share/locale/$i/LC_MESSAGES
    install -d -m 755 $RPM_BUILD_ROOT/opt/kde3/share/doc/HTML/$i
    echo "%lang($i) %doc /opt/kde3/share/locale/$i" >> locale.list
  done
  %suse_update_desktop_file kresources X-KDE-settings-desktop
  # unlike with other modules, kde_post_install shouldn't
  # be put at the end of %install
  kde_post_install
  # now create a filesystem layer
  for theme in hicolor locolor; do
    for j in actions apps filesystems mimetypes; do
      for i in 16 22 32 48 64 128; do
        install -d -m 0755 $RPM_BUILD_ROOT/opt/kde3/share/icons/${theme}/${i}x${i}/${j}
      done
      install -d -m 0755 $RPM_BUILD_ROOT/opt/kde3/share/icons/${theme}/scalable/${j}
    done
  done
  install -d -m 0755 $RPM_BUILD_ROOT/etc/opt/kde3/%_lib
  install -d -m 0755 $RPM_BUILD_ROOT/etc/opt/kde3/share/config
  install -d -m 0755 $RPM_BUILD_ROOT/opt/kde3/share/apps/kdelibs/
  install -m 0644 %SOURCE6 $RPM_BUILD_ROOT/etc/
  rm -f $RPM_BUILD_ROOT/opt/kde3/%_lib/libkdeinit_*.la
  #
  # add additional icon path
  #
  mkdir -p ${RPM_BUILD_ROOT}/opt/kde3/share/apps/kdelibs
  rm -f admin/*.orig
  cp -a admin ${RPM_BUILD_ROOT}/opt/kde3/share/apps/kdelibs/
  # This is not needed on SUSE Linux! - Marcus Meissner <meissner@suse.de>
  rm $RPM_BUILD_ROOT/opt/kde3/bin/kgrantpty
  #
  # our version is in kdebase3
  #
  rm -f $RPM_BUILD_ROOT/opt/kde3/bin/fileshare*
  #
  # no sources for man pages
  #
  rm -f $RPM_BUILD_ROOT/opt/kde3/share/doc/HTML/en/kdelibs/man-*
  # 
  # install BitTorrent icons
  #
  tar xfvz %SOURCE11
  for i in 16x16 22x22 32x32 48x48 64x64 128x128 ; do
      install -m 0644 bt/$i/mimetypes/bt.png \
              $RPM_BUILD_ROOT/opt/kde3/share/icons/crystalsvg/$i/mimetypes/torrent.png
  done
  cp CATALOG.%{name} catalog.xml ${RPM_BUILD_ROOT}/opt/kde3/share/apps/ksgmltools2/customization/
  mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/xml
  cp %{FOR_ROOT_CAT} ${RPM_BUILD_ROOT}%{_sysconfdir}/xml
#  rm -f $RPM_BUILD_ROOT/opt/kde3/%_lib/libkdefakes.la
#  rm -f $RPM_BUILD_ROOT/opt/kde3/%_lib/libkjava.la
%if %suse_version > 1020
rm -f $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/index.theme
%endif
  # .desktop files in kdeaccessibility3 require the kttsd icon
  for i in {16x16,22x22,32x32,48x48,64x64,128x128,scalable}; do mv $RPM_BUILD_ROOT/opt/kde3/share/icons/crystalsvg/$i/apps/kttsd.* $RPM_BUILD_ROOT/opt/kde3/share/icons/hicolor/$i/apps/;done
  install -m 0644 %SOURCE14 $RPM_BUILD_ROOT/opt/kde3/share/mimelnk/application/
  install -m 0644 %SOURCE15 $RPM_BUILD_ROOT/opt/kde3/share/mimelnk/application/
  install -m 0644 %SOURCE16 $RPM_BUILD_ROOT/opt/kde3/share/mimelnk/application/
  # fix bnc#396153
  for i in 16x16 22x22 32x32 48x48 64x64 128x128; do
    ln -s /opt/kde3/share/icons/crystalsvg/$i/filesystems/network.png $RPM_BUILD_ROOT/opt/kde3/share/icons/crystalsvg/$i/filesystems/preferences-system-network.png
    ln -s /opt/kde3/share/icons/crystalsvg/$i/filesystems/desktop.png $RPM_BUILD_ROOT/opt/kde3/share/icons/crystalsvg/$i/filesystems/preferences-desktop.png
  done
  chmod a-x $RPM_BUILD_ROOT/opt/kde3/share/icons/crystalsvg/16x16/filesystems/file_broken.png
  %if %suse_version > 1020
  %fdupes -s $RPM_BUILD_ROOT
  %endif
  %if %suse_version > 1110
  mkdir -p $RPM_BUILD_ROOT/etc/opt/kde3/share/applications
  touch $RPM_BUILD_ROOT/etc/opt/kde3/share/applications/mimeinfo.cache
  mkdir -p $RPM_BUILD_ROOT/opt/kde3/share/applications
  touch $RPM_BUILD_ROOT/opt/kde3/share/applications/mimeinfo.cache
  %endif
# Create /etc/ld.so.conf.d/kdelibs3.conf 
mkdir -p $RPM_BUILD_ROOT/etc/ld.so.conf.d
cat > $RPM_BUILD_ROOT/etc/ld.so.conf.d/kdelibs3.conf <<EOF
%ifarch s390x sparc64 x86_64 ppc64
/opt/kde3/lib64
%endif
/opt/kde3/lib
EOF

%post
  %run_ldconfig
  %run_permissions

%postun
  rm -f usr/share/doc/KDE3-API/index.html
  %run_ldconfig

%post arts
  %run_ldconfig

%postun arts
  %run_ldconfig

%post default-style
  %run_ldconfig

%postun default-style
  %run_ldconfig

%post doc
  if [ -x %{regcat} ]; then
    %{regcat} -a /opt/kde3/share/apps/ksgmltools2/customization/CATALOG.%{name} >/dev/null 2>&1
  fi
  if [ -x /usr/bin/edit-xml-catalog ]; then
    edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
      --add /etc/xml/%{FOR_ROOT_CAT}
  fi

%postun doc
  if [ "$1" = "0" -a -x %{regcat} ]; then
    %{regcat} -r /opt/kde3/share/apps/ksgmltools2/customization/CATALOG.%{name} >/dev/null 2>&1
  fi
  # remove entries only on removal of file
  if [ ! -f %{xml_sysconf_dir}/%{FOR_ROOT_CAT} -a -x /usr/bin/edit-xml-catalog ] ; then
    edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
      --del %{name}-%{version}
  fi
  exit 0

%clean
  rm -rf ${RPM_BUILD_ROOT}

%files default-style
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.BSD COPYING.LIB NAMING README 
/opt/kde3/%_lib/libkdefx.so.*
/opt/kde3/%_lib/kde3/plugins/styles/plastik.*

%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.BSD COPYING.LIB NAMING README 
/etc/ld.so.conf.d/kdelibs3.conf
%dir /etc/opt/kde3
%dir /opt/kde3
%dir /opt/kde3/bin
%dir /opt/kde3/include
%dir /opt/kde3/share
%dir /opt/kde3/share/config.kcfg
%_mandir/man*/*
/opt/kde3/bin/checkXML
/opt/kde3/bin/dcop
/opt/kde3/bin/dcopclient
/opt/kde3/bin/dcopfind
/opt/kde3/bin/dcopobject
/opt/kde3/bin/dcopref
/opt/kde3/bin/dcops*
/opt/kde3/bin/dcopquit
/opt/kde3/bin/imagetops
/opt/kde3/bin/ka*
/opt/kde3/bin/kbuildsycoca
/opt/kde3/bin/kco*
/opt/kde3/bin/kcmshell
/opt/kde3/bin/kded
/opt/kde3/bin/kdeinit*
/opt/kde3/bin/start_kdeinit
/opt/kde3/bin/start_kdeinit_wrapper
/opt/kde3/bin/kde-config
/opt/kde3/bin/kde-menu
/opt/kde3/bin/kdesu_stub
/opt/kde3/bin/kdontchangethehostname
/opt/kde3/bin/kfile
/opt/kde3/bin/ki*
/opt/kde3/bin/kfmexec
/opt/kde3/bin/klauncher
/opt/kde3/bin/kmailservice
/opt/kde3/bin/ktradertest
/opt/kde3/bin/knotify
/opt/kde3/bin/kstartupconfig
/opt/kde3/bin/kdostartupconfig
%verify(not mode) /opt/kde3/bin/kpac_dhcp_helper
/opt/kde3/bin/ksendbugmail
/opt/kde3/bin/kshell
/opt/kde3/bin/ktelnetservice
/opt/kde3/bin/kwrapper
/opt/kde3/bin/lnusertemp
/opt/kde3/bin/make_driver_db_lpr
/opt/kde3/bin/khotnewstuff
/opt/kde3/bin/makekdewidgets
%dir /opt/kde3/%_lib
%dir /opt/kde3/%_lib/kde3
/opt/kde3/%_lib/kde3/dcopserver.*
/opt/kde3/%_lib/kde3/kaddprinterwizard.*
/opt/kde3/%_lib/kde3/kbuildsycoca.*
/opt/kde3/%_lib/kde3/kcmshell.*
/opt/kde3/%_lib/kde3/kcm_kresources.*
/opt/kde3/%_lib/kde3/kconf_update.*
/opt/kde3/%_lib/kde3/kcookiejar.*
/opt/kde3/%_lib/kde3/kded.*
/opt/kde3/%_lib/kde3/kded_proxyscout.*
/opt/kde3/%_lib/kde3/kfileaudiopreview.*
/opt/kde3/%_lib/kde3/klauncher.*
/opt/kde3/%_lib/kde3/knotify.*
/opt/kde3/%_lib/kde3/kabc*
/opt/kde3/%_lib/kde3/kbzip2filter.*
/opt/kde3/%_lib/kde3/kded_k*
/opt/kde3/%_lib/kde3/kdeprint_ext.*
/opt/kde3/%_lib/kde3/kdeprint_lp*
/opt/kde3/%_lib/kde3/kdeprint_rlpr.*
/opt/kde3/%_lib/kde3/kdeprint_tool_escputil.*
/opt/kde3/%_lib/kde3/kgzipfilter.*
/opt/kde3/%_lib/kde3/khtmlimagepart.*
/opt/kde3/%_lib/kde3/ki*
/opt/kde3/%_lib/kde3/kjavaappletviewer.*
/opt/kde3/%_lib/kde3/ktexteditor_*
/opt/kde3/%_lib/kde3/libk*
/opt/kde3/%_lib/kde3/kspell_*
/opt/kde3/%_lib/kde3/kstyle_plastik_config.*
/opt/kde3/%_lib/kde3/kstyle_highcontrast_config.*
/opt/kde3/%_lib/kde3/libshellscript.*
%exclude /opt/kde3/%_lib/kde3/plugins/styles/plastik.*
/opt/kde3/%_lib/kde3/plugins
/opt/kde3/%_lib/libDCOP.so.*
%exclude /opt/kde3/%_lib/libkdefx.so.*
/opt/kde3/%_lib/libk*.so.*
/opt/kde3/%_lib/libvcard.so.*
/opt/kde3/%_lib/libkdeinit*.so
/opt/kde3/%_lib/libnetworkstatus.so.*
/opt/kde3/%_lib/libconnectionmanager.so.*
/opt/kde3/%_lib/kde3/kded_networkstatus.*
/opt/kde3/share/applnk
%dir /opt/kde3/share/apps
/opt/kde3/share/apps/LICENSES
/opt/kde3/share/apps/ka*
/opt/kde3/share/apps/kc*
%dir /opt/kde3/share/apps/kdeprint
/opt/kde3/share/apps/kdeprint/apsdriver*
/opt/kde3/share/apps/kdeprint/filters
/opt/kde3/share/apps/kdeprint/icons
/opt/kde3/share/apps/kdeprint/lprngtooldriver1
/opt/kde3/share/apps/kdeprint/pics
%dir /opt/kde3/share/apps/kdeprint/plugins
/opt/kde3/share/apps/kdeprint/plugins/ext.print
/opt/kde3/share/apps/kdeprint/plugins/lp*.print
/opt/kde3/share/apps/kdeprint/plugins/rlpr.print
/opt/kde3/share/apps/kdeprint/s*
/opt/kde3/share/apps/kdeprint/t*
/opt/kde3/share/apps/kdeui
/opt/kde3/share/apps/kdewidgets
/opt/kde3/share/apps/khtml
/opt/kde3/share/apps/kio_uiserver
/opt/kde3/share/apps/kjava
/opt/kde3/share/apps/knotify
/opt/kde3/share/apps/kssl
/opt/kde3/share/apps/kstyle
/opt/kde3/share/apps/ktexteditor_*
/opt/kde3/share/apps/proxyscout
/opt/kde3/share/apps/knewstuff
/opt/kde3/share/autostart
/opt/kde3/share/config
/opt/kde3/share/emoticons
/opt/kde3/share/icons
/opt/kde3/share/locale
/opt/kde3/share/mimelnk
/opt/kde3/share/service*
%config /etc/kde3rc
/opt/kde3/share/applications
/opt/kde3/bin/cupsd*
/opt/kde3/bin/make_driver_db_cups
/opt/kde3/%_lib/kde3/kdeprint_cups.*
/opt/kde3/%_lib/kde3/cupsdconf.*
/opt/kde3/share/apps/kdeprint/cups*
/opt/kde3/share/apps/kdeprint/kde_logo.png
/opt/kde3/share/apps/kdeprint/plugins/cups.print
/opt/kde3/share/apps/kdeprint/preview*
%ifarch x86_64 ppc64 s390x mips64 sparc64
%dir /opt/kde3/lib
%dir /opt/kde3/lib/kde3
/opt/kde3/lib/kde3/plugins-lib64
%endif
/etc/xdg/menus
%if %suse_version > 1110
%dir /etc/opt/kde3
%dir /etc/opt/kde3/share
%dir /etc/opt/kde3/share/applications
%ghost /etc/opt/kde3/share/applications/mimeinfo.cache
%dir /opt/kde3
%dir /opt/kde3/share
%dir /opt/kde3/share/applications
%ghost /opt/kde3/share/applications/mimeinfo.cache
%endif

%files arts
%defattr(-,root,root)
/opt/kde3/bin/artsmessage
/opt/kde3/%_lib/libartskde.so.*

%files doc
%defattr(-,root,root)
%doc /opt/kde3/share/doc
/opt/kde3/bin/meinproc
/opt/kde3/share/apps/ksgmltools2
%config %{_sysconfdir}/xml/%{FOR_ROOT_CAT}

%files devel
%defattr(-,root,root)
%dir /opt/kde3/share/apps/kdelibs
%config /etc/opt/kde3/common_options
/opt/kde3/bin/dcopidl*
/opt/kde3/bin/kmimelist
/opt/kde3/bin/preparetips
/opt/kde3/bin/ksvgtopng
/opt/kde3/bin/kunittestmodrunner
#/opt/kde3/bin/MISC
/opt/kde3/include/*
/opt/kde3/share/apps/dcopidlng
/opt/kde3/share/apps/kdelibs/admin
/opt/kde3/%_lib/libartskde.la
/opt/kde3/%_lib/libkunittest.la
/opt/kde3/%_lib/libkunittest.so
/opt/kde3/%_lib/libartskde.so
/opt/kde3/%_lib/libDCOP.so
/opt/kde3/%_lib/libvcard.so
/opt/kde3/%_lib/libvcard.la
/opt/kde3/%_lib/libDCOP.la
/opt/kde3/%_lib/lib*.a
/opt/kde3/%_lib/libkabc_dir.la
/opt/kde3/%_lib/libkabc_dir.so
/opt/kde3/%_lib/libkabc_file.la
/opt/kde3/%_lib/libkabc_file.so
/opt/kde3/%_lib/libkabc.la
/opt/kde3/%_lib/libkabc_ldapkio.la
/opt/kde3/%_lib/libkabc_ldapkio.so
/opt/kde3/%_lib/libkabc.so
/opt/kde3/%_lib/libkatepartinterfaces.la
/opt/kde3/%_lib/libkatepartinterfaces.so
/opt/kde3/%_lib/libkdecore.la
/opt/kde3/%_lib/libkdecore.so
/opt/kde3/%_lib/libkdefakes.la
/opt/kde3/%_lib/libkdefakes.so
/opt/kde3/%_lib/libkdefx.la
/opt/kde3/%_lib/libkdefx.so
/opt/kde3/%_lib/libkdemm.la
/opt/kde3/%_lib/libkdemm.so
/opt/kde3/%_lib/libkdeprint.la
/opt/kde3/%_lib/libkdeprint_management.la
/opt/kde3/%_lib/libkdeprint_management.so
/opt/kde3/%_lib/libkdeprint.so
/opt/kde3/%_lib/libkdesasl.la
/opt/kde3/%_lib/libkdesasl.so
/opt/kde3/%_lib/libkdesu.la
/opt/kde3/%_lib/libkdesu.so
/opt/kde3/%_lib/libkdeui.la
/opt/kde3/%_lib/libkdeui.so
/opt/kde3/%_lib/libkdnssd.la
/opt/kde3/%_lib/libkdnssd.so
/opt/kde3/%_lib/libkhtml.la
/opt/kde3/%_lib/libkhtml.so
/opt/kde3/%_lib/libkimproxy.la
/opt/kde3/%_lib/libkimproxy.so
/opt/kde3/%_lib/libkio.la
/opt/kde3/%_lib/libkio.so
/opt/kde3/%_lib/libkjava.la
/opt/kde3/%_lib/libkjava.so
/opt/kde3/%_lib/libkjs.la
/opt/kde3/%_lib/libkjs.so
/opt/kde3/%_lib/libkmdi2.la
/opt/kde3/%_lib/libkmdi2.so
/opt/kde3/%_lib/libkmdi.la
/opt/kde3/%_lib/libkmdi.so
/opt/kde3/%_lib/libkmediaplayer.la
/opt/kde3/%_lib/libkmediaplayer.so
/opt/kde3/%_lib/libkmid.la
/opt/kde3/%_lib/libkmid.so
/opt/kde3/%_lib/libknewstuff.la
/opt/kde3/%_lib/libknewstuff.so
/opt/kde3/%_lib/libkntlm.la
/opt/kde3/%_lib/libkntlm.so
/opt/kde3/%_lib/libkparts.la
/opt/kde3/%_lib/libkparts.so
/opt/kde3/%_lib/libkresources.la
/opt/kde3/%_lib/libkresources.so
/opt/kde3/%_lib/libkscreensaver.la
/opt/kde3/%_lib/libkscreensaver.so
/opt/kde3/%_lib/libkscript.la
/opt/kde3/%_lib/libkscript.so
/opt/kde3/%_lib/libkspell2.la
/opt/kde3/%_lib/libkspell2.so
/opt/kde3/%_lib/libkspell.la
/opt/kde3/%_lib/libkspell.so
/opt/kde3/%_lib/libktexteditor.la
/opt/kde3/%_lib/libktexteditor.so
/opt/kde3/%_lib/libkutils.la
/opt/kde3/%_lib/libkutils.so
/opt/kde3/%_lib/libkwalletbackend.la
/opt/kde3/%_lib/libkwalletbackend.so
/opt/kde3/%_lib/libkwalletclient.la
/opt/kde3/%_lib/libkwalletclient.so
/opt/kde3/%_lib/libnetworkstatus.la
/opt/kde3/%_lib/libnetworkstatus.so
/opt/kde3/%_lib/libconnectionmanager.la
/opt/kde3/%_lib/libconnectionmanager.so

%changelog
