# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 0

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


%define appdir %{_datadir}/applications/kde

# former extras bits
#define _with_akode --with-akode
## not currently compatible with libtunepimp-0.5 (only libtunepimp-0.4)
#define _with_musicbrainz --with-musicbrainz
%define _with_taglib --with-taglib
%define _with_xine --with-xine

Name:    trinity-kdemultimedia
Summary: Multimedia applications for the K Desktop Environment (KDE)
Version: %{?version}
Release: %{?release}%{?dist}%{?_variant}

License: GPLv2
Group:   Applications/Multimedia

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: kdemultimedia-%{version}.tar.gz

Provides: kdemultimedia3 = %{version}-%{release}

# RedHat Legacy patches (from Fedora 8)
Patch3: kdemultimedia-3.4.0-xdg.patch
Patch5: kdemultimedia-3.5.7-pthread.patch


Provides: kdemultimedia3 = %{version}-%{release}

Requires: %{name}-libs = %{version}-%{release}

BuildRequires: zlib-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: libvorbis-devel
BuildRequires: audiofile-devel
BuildRequires: desktop-file-utils
BuildRequires: libtheora-devel
BuildRequires: flac-devel
BuildRequires: alsa-lib-devel 
BuildRequires: cdparanoia-devel cdparanoia
BuildRequires: gstreamer-devel
BuildRequires: automake libtool
%{?_with_akode:BuildRequires: akode-devel}
%{?_with_musicbrainz:BuildRequires: libmusicbrainz-devel libtunepimp-devel}
%{?_with_taglib:BuildRequires: taglib-devel}
%{?_with_xine:BuildRequires: xine-lib-devel}
BuildRequires:	libXxf86dga-devel
BuildRequires:	libXxf86vm-devel

%description
The K Desktop Environment (KDE) is a GUI desktop for the X Window
System. The %{name} package contains multimedia applications for
KDE, including:
  kmid, a midi player
  kmix, an audio mixer
  arts, additional functionality for the aRts sound system
  krec, a recording tool
  kscd, an Audio-CD player
  kaudiocreator, a graphical frontend for audio file creation 

%package devel
Summary: Development files for %{name}, aRts and noatun plugins
Group: Development/Libraries
Provides: kdemultimedia3-devel = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
# for noatun shlib(s)
Requires: %{name}-extras-libs = %{version}-%{release}
Requires: trinity-kdelibs-devel
%description devel
{summary}.
Install %{name}-devel if you wish to develop or compile any
applications using aRtsbuilder, aRtsmidi, aRtskde, aRts modules or
noatun plugins.

%package extras
Summary: Extra applications from %{name} 
Group: Applications/Multimedia
Requires: %{name}-extras-libs = %{version}-%{release}
%description extras
%{summary}, including:
 * juk, a media player
 * kaboodle, a media player
 * noatun, a media player

%package extras-libs
Summary: Extra %{name} runtime libraries 
Group: System Environment/Libraries 
Requires: %{name}-libs = %{version}-%{release}
%description extras-libs
%{summary}.

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-kdelibs
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%setup -q -n kdemultimedia
%patch3 -p1 -b .xdg
%patch5 -p1 -b .pthread

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

%configure  \
   --enable-new-ldflags \
   --disable-dependency-tracking \
   --includedir=%{tde_includedir} \
   --with-cdparanoia \
   --with-flac \
   --with-theora \
   --with-vorbis \
   --with-alsa \
   --with-gstreamer \
   --without-lame \
   --disable-debug \
   --disable-warnings \
   --enable-final \
   --disable-rpath \
  %{?_with_akode} %{!?_with_akode:--without-akode} \
  %{?_with_musicbrainz} %{!?_with_musicbrainz:--without-musicbrainz} \
  %{?_with_taglib} %{!?_with_taglib:--without-taglib} \
  %{?_with_xine} %{!?_with_xine:--without-xine} \
   --with-extra-includes=%{_usr}/include/cdda:%{_includedir}/tqt \
   --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{?buildroot} 
%__make install DESTDIR=%{buildroot}

## Remove/uninstall (conflicting) bits we don't want
%__rm -f $RPM_BUILD_ROOT%{_libdir}/mcop/akode*MPEGPlayObject.mcopclass

# only show in KDE, really? -- Rex (FIXME)
for f in %{buildroot}%{appdir}/*.desktop ; do
  if [ -f %{buildroot}%{appdir}/*.desktop ] ; then
    echo "OnlyShowIn=KDE;" >> $f
  fi
done

# don't make these world-writeable
chmod go-w %{buildroot}%{_datadir}/apps/kscd/*

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
for dir in k* ; do
  for file in AUTHORS ChangeLog README TODO ; do
    if test -s "$dir/$file" ; then
       install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
       # exclude kaboodle, juk, noatun
       if [ $dir != kaboodle -a $dir != juk -a $dir != noatun ] ; then
         echo "%doc rpmdocs/$dir/" >> %{name}.lang
       fi
    fi
  done
done


%post
/sbin/ldconfig
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun
/sbin/ldconfig
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post extras-libs -p /sbin/ldconfig

%postun extras-libs -p /sbin/ldconfig

%post extras
/sbin/ldconfig
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun extras
/sbin/ldconfig
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :


%clean
%__rm -rf %{buildroot}


%files extras
%defattr(-,root,root,-)

# kaboodle
%doc rpmdocs/kaboodle/
%doc %lang(en) %{_docdir}/HTML/en/kaboodle/
%{_bindir}/kaboodle
%{tde_libdir}/libkaboodlepart.*
%{_datadir}/applications/kde/kaboodle.desktop
%{_datadir}/apps/kaboodle/
%{_datadir}/icons/hicolor/*/apps/kaboodle.png
%{_datadir}/services/kaboodle*

# noatun
%doc %lang(en) %{_docdir}/HTML/en/noatun/
%{_bindir}/noatun
%{_libdir}/kconf_update_bin/noatun20update
%{tde_libdir}/noatun*
%{_libdir}/libartseffects.*
%{_libdir}/libwinskinvis.*
%{_libdir}/libkdeinit_noatun.*
%{_datadir}/applications/kde/noatun.desktop
%{_datadir}/apps/kconf_update/noatun.upd
%{_datadir}/apps/noatun/
%{_datadir}/icons/hicolor/*/apps/noatun.png
%{_datadir}/mimelnk/interface/x-winamp-skin.desktop

# juk
%doc %lang(en) %{_docdir}/HTML/en/juk/
%{_bindir}/juk
%{_datadir}/applications/kde/juk.desktop
%{_datadir}/apps/juk/
%{_datadir}/apps/konqueror/servicemenus/jukservicemenu.desktop
%{_datadir}/icons/crystalsvg/*/*/juk*
%{_datadir}/icons/hicolor/*/apps/juk.png

%files extras-libs
%defattr(-,root,root,-)
%{_libdir}/libnoatun*.la
%{_libdir}/libnoatun*.so.*
%{_libdir}/libnoatunarts.so

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING

# kaboodle
%exclude %{tde_docdir}/HTML/en/kaboodle/
%exclude %{_bindir}/kaboodle
%exclude %{tde_libdir}/libkaboodlepart.*
%exclude %{_datadir}/applications/kde/kaboodle.desktop
%exclude %{_datadir}/apps/kaboodle/
%exclude %{_datadir}/icons/hicolor/*/apps/kaboodle.png
%exclude %{_datadir}/services/kaboodle*

# noatun
%exclude %{tde_docdir}/HTML/en/noatun/
%exclude %{_bindir}/noatun
%exclude %{_libdir}/kconf_update_bin/noatun20update
%exclude %{tde_libdir}/noatun*
%exclude %{_libdir}/libartseffects.*
%exclude %{_libdir}/libkdeinit_noatun.*
%exclude %{_libdir}/libnoatunarts.*
%exclude %{_libdir}/libnoatuncontrols.*
%exclude %{_libdir}/libnoatun.*
%exclude %{_libdir}/libnoatuntags.*
%exclude %{_libdir}/libwinskinvis.*
%exclude %{_datadir}/applications/kde/noatun.desktop
%exclude %{_datadir}/apps/kconf_update/noatun.upd
%exclude %{_datadir}/apps/noatun/
%exclude %{_datadir}/icons/hicolor/*/apps/noatun.png
%exclude %{_datadir}/mimelnk/interface/x-winamp-skin.desktop

# juk
%exclude %{tde_docdir}/HTML/en/juk/
%exclude %{_bindir}/juk
%exclude %{_datadir}/applications/kde/juk.desktop
%exclude %{_datadir}/apps/juk/
%exclude %{_datadir}/apps/konqueror/servicemenus/jukservicemenu.desktop
%exclude %{_datadir}/icons/crystalsvg/*/*/juk*
%exclude %{_datadir}/icons/hicolor/*/apps/juk.png

/etc/xdg/menus/applications-merged/*
%{_libdir}/mcop/*
%{_libdir}/libkdeinit_*.so
#%{_libdir}/liboggarts.so
%{tde_libdir}/*
%{_libdir}/kconf_update_bin/*
%{_bindir}/*
%{_datadir}/applications/kde/*
%{_datadir}/apps/*
%{_datadir}/autostart/*
%{_datadir}/config.kcfg/*
%{_datadir}/desktop-directories/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*
%{_datadir}/mimelnk/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*

# Misc HTML docs
%doc %lang(en) %{tde_docdir}/HTML/en/artsbuilder
%doc %lang(en) %{tde_docdir}/HTML/en/kaudiocreator
%doc %lang(en) %{tde_docdir}/HTML/en/kioslave/audiocd.docbook
%doc %lang(en) %{tde_docdir}/HTML/en/kmid
%doc %lang(en) %{tde_docdir}/HTML/en/kmix
%doc %lang(en) %{tde_docdir}/HTML/en/krec
%doc %lang(en) %{tde_docdir}/HTML/en/kscd


%files libs
%defattr(-,root,root,-)
%exclude %{_libdir}/libnoatun*.*
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la


%files devel
%defattr(-,root,root,-)
%{tde_includedir}/*
%{_libdir}/lib*.so
%exclude %{_libdir}/libkdeinit_*.so
%exclude %{_libdir}/libartseffects.so
%exclude %{_libdir}/libnoatunarts.*
#exclude %{_libdir}/liboggarts.so
%exclude %{_libdir}/libwinskinvis.so


%changelog
* Sat Sep 09 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Initial build for RHEL 6
- Spec file based on Fedora 8 "kdemultimedia-6:3.5.10-2"
