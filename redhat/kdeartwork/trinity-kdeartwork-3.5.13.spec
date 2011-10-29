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
%define tde_libdir %{_libdir}/trinity

# kdeartwork specific settings
# On RHEL 6, libart is too old !
%if 0%{?fedora} >= 15
%define with_libart 1
%endif


Name:    trinity-kdeartwork
Summary: Additional artwork (themes, sound themes, ...) for TDE
Version: %{?version}
Release: %{?release}%{?dist}%{?_variant}

License:	GPLv2
Group:		User Interface/Desktops
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
Url:		http://www.trinitydesktop.org/

Source: kdeartwork-%{version}.tar.gz

# FIXME: this should go in kde-settings -- Rex
Source1: webcollagerc

BuildRequires: gettext
BuildRequires: trinity-kdebase-devel
BuildRequires: nas-devel esound-devel jack-audio-connection-kit-devel
BuildRequires: xscreensaver
%if "%{?with_libart}" == "1"
BuildRequires: libart_lgpl-devel
%endif

Requires: trinity-kdebase

%description
Additional artwork (themes, sound themes, screensavers ...) for KDE.

# TODO: build this subpkg noarch
%package icons
Summary: Icon themes (kdeclassic, slick ....) for KDE
Group: User Interface/Desktops
%description icons
%{summary}.


%prep
%setup -q -n kdeartwork


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"
export LD_LIBRARY_PATH="%{_libdir}"

%__mkdir build
cd build
%cmake \
  -DWITH_XSCREENSAVER=ON \
%if "%{?with_libart}" == "1"
  -DWITH_LIBART=ON \
%else
  -DWITH_LIBART=OFF \
%endif
  -DWITH_OPENGL=ON \
  -DWITH_ARTS=ON \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install -C build DESTDIR=%{buildroot}

# webcollage -root -directory /usr/share/backgrounds/images #227683

# rpmdocs
for dir in IconThemes/* kworldclock kscreensaver/kxsconfig ; do
  for file in AUTHORS ChangeLog COPYRIGHT README TODO ; do
    test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
  done
done

# File lists
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
        [ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../common $i/common
      done
    popd
  fi
done
fi

# kde vs xscreensaver based screensavers
for screensaver in %{buildroot}%{_datadir}/applnk/System/ScreenSavers/*.desktop ; do
  if [ `grep '^TryExec=xscreensaver' $screensaver` ]; then
    echo $screensaver | sed -e "s|%{buildroot}||" >> %{name}-extras.lang
  else
    echo $screensaver | sed -e "s|%{buildroot}||" >> %{name}.lang
  fi
done



%post icons
for i in locolor ikons kdeclassic kids slick ; do
 touch --no-create %{_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{_datadir}/icons/$i 2>/dev/null || :
done

%postun icons
for i in locolor ikons kdeclassic kids slick ; do
 touch --no-create %{_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{_datadir}/icons/$i 2>/dev/null || :
done

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc kwin-styles/smooth-blend/COPYING
%doc rpmdocs/kworldclock
%{_bindir}/*.kss
%{tde_libdir}/plugins/styles/*
%{tde_libdir}/*.so
%{tde_libdir}/*.la
%{_datadir}/apps/kfiresaver/
%{_datadir}/apps/kscreensaver/
%{_datadir}/apps/kstyle/themes/*
%{_datadir}/apps/kwin/*
%{_datadir}/apps/kworldclock/
%{_datadir}/sounds/*
%{_datadir}/wallpapers/*
%{_datadir}/emoticons/*
%{_bindir}/kxs*

%files icons
%defattr(-,root,root,-)
%doc rpmdocs/IconThemes/*
%{_datadir}/icons/ikons/
%{_datadir}/icons/kdeclassic/
%{_datadir}/icons/kids/
%{_datadir}/icons/Locolor/
%{_datadir}/icons/slick/



%changelog
* Sun Sep 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
