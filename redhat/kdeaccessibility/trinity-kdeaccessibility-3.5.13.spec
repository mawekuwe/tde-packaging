# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Summary: K Desktop Environment - Accessibility
Name:    trinity-kdeaccessibility
Version: %{?version}
Release: %{?release}%{?dist}%{?_variant}

License: GPLv2
Group: User Interface/Desktops

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Source0: kdeaccessibility-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Provides: kdeaccessibility3 = %{version}-%{release}

Requires: trinity-kdelibs
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

BuildRequires: desktop-file-utils
BuildRequires: trinity-kdelibs-devel
BuildRequires: alsa-lib-devel
%if 0%{?fedora} > 4 || 0%{?rhel} > 4
BuildRequires: libXtst-devel
%endif

%description
Included with this package are:
* kmag, a screen magnifier,
* kmousetool, a program for people whom it hurts to click the mouse,
* kmouth, program that allows people who have lost their voice
  to let their computer speak for them.

%package devel
Summary: Development files for %{name}
Group:   Development/Libraries
Provides: kdeaccessibility3-devel = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: trinity-kdelibs-devel
%description devel
%{summary}.


%prep
%setup -q -n kdeaccessibility

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
sed -i admin/acinclude.m4.in \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
  --includedir=%{tde_includedir} \
  --disable-rpath \
  --enable-new-ldflags \
  --enable-closure \
  --disable-debug --disable-warnings \
  --enable-final \
  --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

desktop-file-install \
  --vendor="" \
  --dir %{buildroot}%{_datadir}/applications/kde \
  --delete-original \
  %{buildroot}%{_datadir}/applnk/Applications/*.desktop ||:

# file lists for locale
%find_lang %{name} || touch %{name}.lang
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}/$HTML_DIR ]; then
  for lang_dir in %{buildroot}/$HTML_DIR/* ; do
    if [ -d $lang_dir ]; then
      lang=$(basename $lang_dir)
      echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
      # replace absolute symlinks with relative ones
      pushd $lang_dir
         for i in *; do
           [ -d $i -a -L $i/common ] && ln -nsf ../common $i/common
         done
      popd
    fi
  done
fi

# rpmdocs
for dir in kmag kmousetool ksayit kttsd ; do
  for file in AUTHORS ChangeLog README TODO ; do
    test -s  $dir/$file && install -p -m644 -D $dir/$file rpmdocs/$dir/$file
  done
done



%clean
%__rm -rf %{buildroot}


%post
/sbin/ldconfig ||:
for icon_theme in mono hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${icon_theme} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${icon_theme} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun
/sbin/ldconfig ||:
for icon_theme in mono hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${icon_theme} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${icon_theme} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING
%doc rpmdocs/*
%{_bindir}/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/apps/*/
%{_datadir}/config/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*
%{_datadir}/icons/mono/
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/service*/*.desktop
%{_libdir}/lib*.so.*
%{_libdir}/*.la
%{tde_libdir}/*

# Misc docs
%doc %lang(en) %{_docdir}/HTML/en/kmag
%doc %lang(en) %{_docdir}/HTML/en/kmousetool
%doc %lang(en) %{_docdir}/HTML/en/kmouth
%doc %lang(en) %{_docdir}/HTML/en/kttsd


%files devel
%defattr(-,root,root,-)
%{tde_includedir}/*
%{_libdir}/lib*.so


%changelog
* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sun Sep 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
- Spec file based on Fedora 8 "kdeaccessibility-3.5.10-1"
