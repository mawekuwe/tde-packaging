# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 3

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:    trinity-kdegames
Summary: Trinity Desktop Environment - Games
Version: %{?version}
Release: %{?release}%{?dist}%{?_variant}

License: GPLv2
Group:   Amusements/Games

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source: 	kdegames-%{version}.tar.gz

# [kdegames/ktuberling] Fix ktuberling pictures loading
Patch0:		kdegames-3.5.13-ktuberling_fail_load_picture.patch

Provides: kdegames3 = %{version}-%{release}

Requires: %{name}-libs = %{version}-%{release}

BuildRequires: trinity-kdelibs-devel

%description
Games and gaming libraries for the K Desktop Environment.
Included with this package are: kenolaba, kasteroids, kblackbox, kmahjongg,
kmines, konquest, kpat, kpoker, kreversi, ksame, kshisen, ksmiletris,
ksnake, ksirtet, katomic, kjumpingcube, ktuberling.

%package devel
Summary: Development files for %{name} 
Group: Development/Libraries
License: LGPLv2
Provides: kdegames3-devel = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Requires: trinity-kdelibs-devel
%description devel
%{summary}.
Install %{name}-devel if you wish to develop or compile games for the
KDE desktop.

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-kdelibs
License: LGPLv2
# include to paranoid, installing libs-only is still mostly untested -- Rex
#Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.



%prep
%setup -q -n kdegames
%patch0 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
   --enable-new-ldflags \
   --disable-dependency-tracking \
   --disable-rpath \
   --enable-final \
   --disable-debug \
   --disable-warnings \
   --enable-closure \
   --includedir=%{_includedir}/kde \
   --disable-setgid \
   --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# locale's
%find_lang %{name} || touch %{name}.lang
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}$HTML_DIR ]; then
for lang_dir in %{buildroot}$HTML_DIR/* ; do
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
for dir in k* lskat ; do
  for file in AUTHORS ChangeLog README TODO ; do
    test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
  done
done


%clean
%__rm -rf %{buildroot}


%post
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS README COPYING
%doc rpmdocs/*
%{_bindir}/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/apps/*
%{_datadir}/config*/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mimelnk/*/*
%{_datadir}/service*/*
%{tde_libdir}/*
%{_libdir}/libkdeinit_*.so

%files libs
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la

%files devel
%defattr(-,root,root,-)
%doc COPYING.LIB
%doc libkdegames/README libkdegames/TODO
%{tde_includedir}/*
%{_libdir}/lib*.so
%exclude %{_libdir}/libkdeinit_*.so


%changelog
* Sun Dec 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Fix ktuberling picture loading [TDE Bug #638]

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Fix HTML directory location

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sat Sep 09 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
