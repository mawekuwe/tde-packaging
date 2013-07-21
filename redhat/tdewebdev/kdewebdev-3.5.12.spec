# Default version for this component
%if "%{?version}" == ""
%define version 3.5.12
%endif
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/kde3

Name:		trinity-kdewebdev
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}
License:	GPL
Summary:	Web development applications 
Group:		Applications/Editors

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kdewebdev-%{version}.tar.gz
Source1: http://download.sourceforge.net/quanta/css.tar.bz2
Source2: http://download.sourceforge.net/quanta/html.tar.bz2
Source3: http://download.sourceforge.net/quanta/php_manual_en_20030401.tar.bz2
Source4: http://download.sourceforge.net/quanta/javascript.tar.bz2
Source5: hi48-app-kxsldbg.png

Patch0: javascript.patch
Patch1: kdewebdev-3.5.4-kxsldbg-icons.patch


BuildRequires:	desktop-file-utils
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdesdk-devel
BuildRequires:	libxslt-devel libxml2-devel
%if 0%{?rhel} == 4
# a bogus dep in libexslt.la file from EL-4 (WONTFIX bug http://bugzilla.redhat.com/142241)
BuildRequires:	libgcrypt-devel
%endif
BuildRequires:	perl

Requires: %{name}-libs = %{version}-%{release}

# optional
Requires:	tidy

Provides:	kdewebdev3 = %{version}-%{release}

Obsoletes: quanta < %{version}-%{release}
Provides:  quanta = %{version}-%{release}

%define kommander_ver 1.2.2
#Obsoletes: kommander < %{kommander_ver}-%{release}
Provides:  kommander = %{kommander_ver}-%{release}

%description
%{summary}, including:
* kfilereplace: batch search and replace tool
* kimagemapeditor: HTML image map editor
* klinkstatus: link checker
* kommander: visual dialog building tool
* kxsldbg: xslt Debugger
* quanta+: web development

%package devel
Group: Development/Libraries
Summary: Header files and documentation for %{name} 
Provides: kdewebdev3-devel = %{version}-%{release}
Requires: trinity-kdelibs-devel
Requires: %{name}-libs = %{version}-%{release}
Obsoletes: quanta-devel < %{version}-%{release}
%description devel
%{summary}.

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-kdelibs
# helps multilib upgrades
%description libs
%{summary}.


%prep
%setup -q -a 1 -a 2 -a 3 -a 4 -n kdewebdev
%patch0 -p0 -b .javascript
%patch1 -p1 -b .kxsldbg-icons

install -m644 -p %{SOURCE5} kxsldbg/

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f admin/Makefile.common


%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%if 0%{?fedora} >= 15
export CXXFLAGS="${CXXFLAGS} -fpermissive"
%endif

%configure \
  --includedir=%{tde_includedir} \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --disable-dependancy-tracking --enable-final \
  --with-extra-includes=%{_includedir}/tqt \

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot}


## package separately?  Why doesn't upstream include this? -- Rex
# install docs
for i in css html javascript ; do
   pushd $i
   ./install.sh <<EOF
%{buildroot}%{_datadir}/apps/quanta/doc
EOF
   popd
   rm -rf $i
done
cp -a php php.docrc %{buildroot}%{_datadir}/apps/quanta/doc/

# make symlinks relative
pushd %{buildroot}%{tde_docdir}/HTML/en
for i in *; do
   if [ -d $i -a -L $i/common ]; then
      rm -f $i/common
      ln -nfs ../common $i
   fi
done
popd

# rpmdocs
for dir in k* quanta; do
  for file in AUTHORS ChangeLog README TODO ; do
    test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
  done
done


%post
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :


%post libs
/sbin/ldconfig

%postun libs
/sbin/ldconfig


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc rpmdocs/*
%{_bindir}/*
%{tde_libdir}/*
%{_datadir}/applications/kde/*
%{_datadir}/applnk/.hidden/*
%{_datadir}/apps/*
%doc %{_datadir}/apps/quanta/doc
%{_datadir}/config.kcfg/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*
%{_datadir}/mimelnk/application/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{tde_docdir}/HTML/en/*


%files libs
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{tde_includedir}/*


%changelog
* Mon Sep 19 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-2
- Add support for RHEL5

* Thu Sep 15 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-1
- Initial release for RHEL 6 / Fedora 15
- Use Spec file from Fedora8 "kdewebdev-3.5.10-1"
- Import to GIT
