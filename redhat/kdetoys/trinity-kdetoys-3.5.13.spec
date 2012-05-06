# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Summary: K Desktop Environment - Toys and Amusements
Name: 	 trinity-kdetoys
Group:	 Amusements/Graphics
Version: 3.5.13
Release: 2%{?dist}%{?_variant}

License: GPLv2+
Source0: kdetoys-%{version}.tar.gz

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: autoconf automake libtool m4
BuildRequires: desktop-file-utils
BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: gettext


%description
Includes: 
* amor: Amusing Misuse Of Resources put's comic figures above your windows
* eyesapplet: a kicker applet similar to XEyes
* fifteenapplet: kicker applet, order 15 pieces in a 4x4 square by moving them
* kmoon: system tray applet showing the moon phase
* kodo: mouse movement meter
* kteatime: system tray applet that makes sure your tea doesn't get too strong
* ktux: Tux-in-a-Spaceship screen saver
* kweather: kicker applet that will display the current weather outside
* kworldwatch: application and kicker applet showing daylight area on the world
               globe

NOTE: kicker applets and screen savers require kdebase to be installed, 
and user to be logged-in to KDE.


%prep
%setup -q -n kdetoys

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
  --includedir=%{_includedir}/kde \
  --disable-rpath \
  --enable-new-ldflags \
  --enable-closure \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final \
  --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf "%{buildroot}"
%__make install DESTDIR=%{buildroot}

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applnk/System/ScreenSavers \
  --vendor="" \
  %{buildroot}%{_datadir}/applnk/System/ScreenSavers/*.desktop ||:

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications/kde \
  --vendor="" \
  %{buildroot}%{_datadir}/applications/kde/*.desktop ||:

# replace absolute symlink with relative
ln -nfs tips-en %{buildroot}%{_datadir}/apps/amor/tips

## File lists
# locale's
%find_lang %{name} || touch %{name}.lang
# HTML (1.0)
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

## Unpackaged files
# not sure the point of just one header file 'AmorIface.h', omit (for now).
%__rm -rf %{buildroot}%{_includedir}


%post
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:

%postun
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/*
%{_libdir}/libkdeinit_*.*
%{tde_libdir}/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/applnk/System/ScreenSavers/*.desktop
%{_datadir}/apps/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/service*/*.desktop
%doc %lang(en) %{tde_docdir}/HTML/en/*

%clean
%__rm -rf %{buildroot}


%changelog
* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Fix HTML directory location

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Fri Oct 28 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT

