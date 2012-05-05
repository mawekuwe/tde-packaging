# Default version for this component
%define kdecomp kaffeine
%define version 0.8.8
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%define _mandir %{_datadir}/man
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary: Xine-based media player

Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License: GPLv2+
Group:   Applications/Multimedia
URL:     http://kaffeine.sourceforge.net/

Source0:	kaffeine-3.5.13.tar.gz
Source2:	kaffeine.1

# [kaffeine] Work around Xine crash when displaying still logo image by creating a small movie file to replace it [Bug #511, #559]
Source1:		508cb342-logo



# [kaffeine] Rename old tq methods that no longer need a unique name[Commit #60ed202f]
Patch1:			kaffeine-3.5.13-rename_old_tq_methods.patch
# [kaffeine] Remove additional unneeded tq method conversions [Commit #701a1249]
Patch2:			kaffeine-3.5.13-remove_additional_tq_conversions.patch
# [kaffeine] Rename obsolete tq methods to standard names [Commit #66805baf]
Patch3:			kaffeine-3.5.13-rename_obsolete_tq_methods.patch
# [kaffeine] Rename a few stragglers [Commit #89b5fd35]
Patch4:			kaffeine-3.5.13-renames_a_few_stragglers.patch
# [kaffeine] Error out if critical OSD-related defines are not set [Commit #25b89439]
Patch5:			kaffeine-3.5.13-error_out_if_critical_osd_defines_not_set.patch
# [kaffeine] Work around Xine crash when displaying still logo image by creating a small movie file to replace it [Bug #559, #511] [Commit #508cb342]
Patch6:			kaffeine-3.5.13-work_around_xine_crash.patch
# [kaffeine] Fix nominal "tqt" typos and fix slow DVB start. [Bug #729, #899] [Commit #fd68e4c4]
Patch7:			kaffeine-3.5.13-fix_slow_dvb_start.patch
# [kaffeine] Change location where Kaffeine stores temporary pipe files from $HOME to the more appropriate $TDEHOME/tmp-$HOSTNAME. [Commit #b480e3db]
Patch8:			kaffeine-3.5.13-fix_temporary_location.patch
# [kaffeine] Fix typos, branding, and inadvertent tqt changes. [Commit #0e3d0ed6]
Patch9:			kaffeine-3.5.13-fix_typos_branding_tqt.patch
# [kaffeine] Fix installation of localization files [Bug #858]
Patch10:		kaffeine-3.5.13-fix_localization_files.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gettext
BuildRequires: trinity-kdelibs-devel
BuildRequires: cdparanoia-devel cdparanoia
BuildRequires: libvorbis-devel
BuildRequires: xine-lib-devel
BuildRequires: libXext-devel libXinerama-devel libXtst-devel
BuildRequires: libcdio-devel

%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
BuildRequires: libxcb-devel
%endif

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

%patch1 -p1
%patch2 -p1
%patch3 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f admin/Makefile.common

%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"


%configure \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final \
  --disable-rpath \
  --with-xinerama \
  --with-gstreamer \
  --without-lame \
  --with-extra-includes=%{_includedir}/tqt \
  --with-extra-libs=%{_prefix}/%{_lib} \
  --enable-closure \
%if 0%{?rhel} > 0 && 0%{?rhel} <= 5
  --without-dvb \
%endif
  

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

%__install -D -m 644 %{SOURCE1} %{?buildroot}%{_datadir}/apps/kaffeine/logo
%__install -D -m 644 %{SOURCE2} %{?buildroot}%{_mandir}/man1/kaffeine.1

%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database >& /dev/null ||:
/sbin/ldconfig || :

%postun
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database >& /dev/null ||:
/sbin/ldconfig || :

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
%{tde_docdir}/HTML/en/kaffeine
%{_mandir}/*/*

%files libs
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/kaffeine/
%{_libdir}/lib*.so
%exclude %{_libdir}/libkaffeinepart.so


%changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.8-2
- Rebuilt for Fedora 17
- Adds more patches from GIT.

* Mon Apr 23 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.8-1
- Updates version to 0.8.8
- Fix nominal "tqt" typos and fix slow DVB start. [Bug #729, #899]
- Change location where Kaffeine stores temporary pipe files from $HOME to the more appropriate $KDEHOME/tmp-$HOSTNAME.
- Work around Xine crash when displaying still logo image by creating a small movie file to replace it [Bug #511, #559]
- Add man page

* Sun Dec 04 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.6-2
- Disable 'libxcb-devel' for RHEL 5 compilation
- Fix HTML directory location

* Wed Nov 09 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.6-1
- Spec file based on Fedora 8 'kaffeine-0.8.6-3'
