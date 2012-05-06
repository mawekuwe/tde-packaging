# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-kdeaddons
Summary:	Trinity Desktop Environment - Plugins
Version:	3.5.13
Release:	4%{?dist}%{?_variant}

License:	GPLv2
Group:		User Interface/Desktops

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: kdeaddons-%{version}.tar.gz
Source1: metabar-fedora.tar.bz2
Source2: metabarrc

BuildRequires: autoconf automake libtool m4
BuildRequires: trinity-kdebase-devel
BuildRequires: trinity-kdegames-devel
BuildRequires: trinity-kdemultimedia-devel
BuildRequires: trinity-kdepim-devel
BuildRequires: SDL-devel
BuildRequires: alsa-lib-devel
BuildRequires: openssl-devel
BuildRequires: db4-devel

%if 0%{?fedora}
BuildRequires: xmms-devel
Obsoletes: %{name}-xmms < %{version}-%{release}
# used in jpegorient (#312641)
Requires: python-exif
%endif

Requires: trinity-kdebase
Requires: which

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
A collection of TDE Addons/Plugins, including: 
* konq-plugins: akregator, babelfish, domtreeviewer, imagerotation, validators, webarchiver
* kate (plugins) 
* kicker-applets: kbinaryclock, kolourpicker, ktimemon, mediacontrol
* knewsticker-scripts

%package extras
Group: User Interface/Desktops
Summary: Extras packages from kdeaddons
Requires: %{name} = %{version}-%{release}
Requires: trinity-kdegames
Obsoletes: %{name}-atlantikdesigner < %{version}-%{release}
%description extras
This package includes:
* atlantikdesigner: game board designer
* noatun-plugins


%prep
%setup -q -a 1 -n kdeaddons

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
  --includedir=%{tde_includedir} \
  --disable-rpath \
  --enable-new-ldflags \
  --enable-closure \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final \
  --with-extra-includes=%{_includedir}/tqt


%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# File lists for locale
HTML_DIR=$(kde-config --expandvars --install html)
touch %{name}.lang
if [ -d %{buildroot}/$HTML_DIR ]; then
 for lang_dir in %{buildroot}/$HTML_DIR/* ; do
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

# rpmdocs
for dir in konq-plugins ; do
  for file in AUTHORS ChangeLog README TODO ; do
    test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
  done
done

%if 0%{?fedora} > 0
# install fedora metabar theme
cp -prf fedora %{buildroot}%{_datadir}/apps/metabar/themes
install -m644 -p %{SOURCE2} %{buildroot}%{_datadir}/config/
%endif


%post
/sbin/ldconfig
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun
/sbin/ldconfig
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%post extras
touch --no-create %{_datadir}/icons/hicolor 2> /dev/null ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:

%postun extras
touch --no-create %{_datadir}/icons/hicolor 2> /dev/null ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:


%clean
%__rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README
%doc rpmdocs/*
%{_bindir}/*
%{tde_libdir}/*
%{_datadir}/applications/kde/*
%{_datadir}/applnk/.hidden/*
%{_datadir}/apps/akregator/pics/*
%{_datadir}/apps/domtreeviewer/
%{_datadir}/apps/fsview/
%{_datadir}/apps/imagerotation/
%{_datadir}/apps/kaddressbook/*
%{_datadir}/apps/kate/*
%{_datadir}/apps/katepart/syntax/*
%{_datadir}/apps/katexmltools
# own dir so we don't need to Requires: kdenetwork too
%dir %{_datadir}/apps/knewsticker
%{_datadir}/apps/knewsticker/*
%{_datadir}/apps/khtml/kpartplugins/*
%{_datadir}/apps/konq*view/kpartplugins/*
%{_datadir}/apps/konqueror/icons/*/*/*/*
%dir %{_datadir}/apps/konqueror/kpartplugins/
%{_datadir}/apps/konqueror/kpartplugins/*
%{_datadir}/apps/konqueror/servicemenus/*
%{_datadir}/apps/konqsidebartng/*/*
%{_datadir}/apps/mediacontrol/
%{_datadir}/apps/metabar/
%{_datadir}/apps/microformat/
#%{_datadir}/apps/noatun/*
%{_datadir}/apps/kicker/applets/*
%{_datadir}/apps/ksig/
%{_datadir}/config*/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*
%{_datadir}/mimelnk/*/*
%{_datadir}/service*/*

# atlantikdesigner
%exclude %{_bindir}/atlantikdesigner
%exclude %{_datadir}/icons/hicolor/*/*/atlantikdesigner*
%exclude %{_datadir}/applications/kde/atlantikdesigner.desktop

# noatun-plugins
%exclude %{_bindir}/noatun*
%exclude %{tde_libdir}/noatun*
%exclude %{_datadir}/apps/noatun/*


%files extras
%defattr(-,root,root,-)

# atlantikdesigner
%doc atlantikdesigner/TODO
%{_bindir}/atlantikdesigner
%{_datadir}/apps/atlantikdesigner/
%{_datadir}/icons/hicolor/*/*/atlantikdesigner*
%{_datadir}/applications/kde/atlantikdesigner.desktop

# noatun-plugins
%{_bindir}/noatun*
%{tde_libdir}/noatun*
%{_datadir}/apps/noatun/*


%changelog
* Sat May 05 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Removes SDL patch for noatun

* Thu Dec 15 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Fix content of -extras package
- Fix various packaging issues

* Fri Nov 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Updates BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sat Oct 29 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT

