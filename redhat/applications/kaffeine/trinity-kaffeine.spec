# Default version for this component
%define kdecomp kaffeine
%define version 0.8.6
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	sudo frontend for Trinity

Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License: GPLv2+
Summary: Xine-based media player
Group:   Applications/Multimedia
URL:     http://kaffeine.sourceforge.net/

Source0: kaffeine-3.5.13.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gettext
BuildRequires: trinity-kdelibs-devel
BuildRequires: cdparanoia-devel cdparanoia
BuildRequires: libvorbis-devel
BuildRequires: xine-lib-devel
BuildRequires: libxcb-devel
BuildRequires: libXext-devel libXinerama-devel libXtst-devel
BuildRequires: libcdio-devel
# dvb
BuildRequires: glibc-kernheaders 
BuildRequires: gstreamer-devel >= 0.10, gstreamer-plugins-base-devel >= 0.10

Requires: %{name}-libs = %{version}-%{release}

%description
Kaffeine is a xine-based media player for KDE.  It plays back CDs,
and VCDs, and can decode all (local or streamed) multimedia formats 
supported by xine-lib.
Additionally, Kaffeine is fully integrated in KDE, it supports drag
and drop and provides an editable playlist, a bookmark system, a
Konqueror plugin, OSD and much more.

%package devel
Summary: Development files for %{name}
Group:   Development/Libraries
Requires: %{name}-libs = %{version}-%{release}
Requires: trinity-kdelibs-devel
%description devel
%{summary}.

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
# helps multilib upgrades
Obsoletes: %{name} < %{version}-%{release}
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.



%prep
%setup -q -n applications/kaffeine

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
sed -i admin/acinclude.m4.in \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f admin/Makefile.common

%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

# easier than patching, and using 
#  --with-extra-includes=%{_includedir}/cdda below -- Rex
#CPPFLAGS="-I%{_includedir}/cdda"; export CPPFLAGS

%configure \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --disable-final \
  --with-gstreamer \
  --without-lame \
  --with-extra-includes=%{_includedir}/tqt
  

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

## File lists
# locale's
%find_lang %{kdecomp}
# HTML (1.0)
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d $RPM_BUILD_ROOT$HTML_DIR ]; then
for lang_dir in $RPM_BUILD_ROOT$HTML_DIR/* ; do
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

# Unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la
rm -f $RPM_BUILD_ROOT%{_datadir}/mimelnk/application/x-mplayer2.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database >& /dev/null ||:

%postun
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database >& /dev/null ||:

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/kaffeine
%{_libdir}/libkaffeinepart.so
%{tde_libdir}/lib*.*
%{_datadir}/appl*/*/*.desktop
%{_datadir}/apps/gstreamerpart/
%{_datadir}/apps/kaffeine/
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/apps/profiles/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mimelnk/*/*.desktop
%{_datadir}/service*/*.desktop
%{_docdir}/HTML/en/kaffeine

%files libs
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/kaffeine/
%{_libdir}/lib*.so
%exclude %{_libdir}/libkaffeinepart.so


%changelog
* Wed Nov 09 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.6-1
- Spec file based on Fedora 8 'kaffeine-0.8.6-3'
