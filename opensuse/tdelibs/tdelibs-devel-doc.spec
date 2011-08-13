#
# spec file for package kdelibs3-devel-doc
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


Name:           kdelibs3-devel-doc
BuildRequires:  OpenEXR-devel aspell-devel cups-devel db-devel doxygen graphviz kdelibs3-devel krb5-devel libjasper libsndfile openldap2-devel qt3-devel-doc utempter xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-scalable
%if %suse_version > 1020
BuildRequires:  avahi-compat-mDNSResponder-devel fdupes
%else
BuildRequires:  mDNSResponder-devel
%endif
Url:            http://www.kde.org
License:        GPLv2+
Group:          Documentation/HTML
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Additional Package Documentation
Version:        3.5.10
Release:        44
%define       kdelibs_patch_level b
BuildArch:      noarch
Requires:       kdelibs3 qt3-devel-doc
Source0:        kdelibs-%{version}.tar.bz2
Source1:        create-kdeapi
Source4:        api_docu_description

%description
This package contains a generated API documentation for all library
classes provided by kdelibs. The index page for all KDE API functions
is:

file:/usr/share/doc/KDE3-API/index.html



Authors:
--------
    The KDE Team <kde@kde.org>

%prep
  echo %suse_version
%setup -q -n kdelibs-%{version}
. /etc/opt/kde3/common_options
update_admin --no-unsermake

%build
. /etc/opt/kde3/common_options
export QTDOCDIR=/usr/share/doc/packages/qt3/html
./configure $configkde --with-distribution="$DISTRI" --enable-libsuffix=`/opt/kde3/bin/kde-config --libsuffix`
do_make apidox 

%install
. /etc/opt/kde3/common_options
  list=`find . -name Makefile.am | xargs grep Doxy | sed -e "s,/Makefile.am.*,," | sort -u `
  for i in $list; do do_make -C $i DESTDIR=$RPM_BUILD_ROOT install-apidox || true; done
  # The modern way, with kdevelop-incompatible api documentation :/
  mkdir -p $RPM_BUILD_ROOT/usr/share/doc/KDE3-API/
  # *** everytime you edit the following line, you made a mistake. Update admin tarball
  # *** version instead
  KDEDOCDIR=$kde_htmldir/en/kdelibs-apidocs
  # this is forgotten, but kdevelop needs it
  mkdir -p $RPM_BUILD_ROOT/$KDEDOCDIR
  if test -d apidocs/qt; then
    cp -a apidocs/qt $RPM_BUILD_ROOT/$KDEDOCDIR
  fi
  set +x
  exitc=0
  for i in `ls -1 $RPM_BUILD_ROOT/$KDEDOCDIR/*/html/index.html`; do 
      lib=`echo $i | sed -e 's,/html/index.html,,; s,.*/\([^/]*\)$,\1,'`
      if ! egrep "^$lib:" %SOURCE4 ; then
  	echo "ERROR: no description for library $lib"
        exitc=1
      fi
      sed -n -e 's@'"${lib}"':\(.*\)@\1@p' %SOURCE4 > ${RPM_BUILD_ROOT}/${KDEDOCDIR}/${lib}/description.SuSE
      echo "kdelibs"                          > ${RPM_BUILD_ROOT}/${KDEDOCDIR}/${lib}/package.SuSE
  done
  if test "$exitc" != 0; then
	exit $exitc
  fi
  ln -s $KDEDOCDIR/index.html $RPM_BUILD_ROOT/usr/share/doc/KDE3-API/index.html
  rm -rf ${RPM_BUILD_ROOT}/opt/kde3/share/apps
  mkdir -p $RPM_BUILD_ROOT/opt/kde3/share/apps/kdelibs
  install -m 0755 %SOURCE1 $RPM_BUILD_ROOT/opt/kde3/share/apps/kdelibs/
  %if %suse_version > 1020
  %fdupes -s $RPM_BUILD_ROOT
  %endif

%post
/opt/kde3/share/apps/kdelibs/create-kdeapi

%clean
  rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%dir /opt/kde3/share
%dir /opt/kde3/share/apps
%dir /opt/kde3/share/apps/kdelibs
/usr/share/doc/KDE3-API
/opt/kde3/share/apps/kdelibs/create-kdeapi
/opt/kde3/share/doc

%changelog
