# Default version for this component
%define tde_pkg kaffeine
%define tde_version 14.0.0

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man

%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:			trinity-%{tde_pkg}
Summary:		Xine-based media player

Version:		0.8.8
Release:		%{?!preversion:6}%{?preversion:5_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Multimedia
URL:			http://kaffeine.sourceforge.net/

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	gettext
BuildRequires:	libvorbis-devel
BuildRequires:	libcdio-devel

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	libcdda-devel
BuildRequires:	%{_lib}xext%{?mgaversion:6}-devel
BuildRequires:	%{_lib}xtst%{?mgaversion:6}-devel
BuildRequires:	%{_lib}xinerama%{?mgaversion:1}-devel
# dvb
%if 0%{?pclinuxos} == 0
BuildRequires:	kernel-headers
%endif
BuildRequires:	libgstreamer-devel >= 0.10
BuildRequires:	libgstreamer-plugins-base-devel >= 0.10
%else
BuildRequires:	cdparanoia
BuildRequires:	cdparanoia-devel
%if 0%{?suse_version} >= 1220
BuildRequires:	libcdio-paranoia-devel
%endif

# X11 stuff
%if 0%{?rhel} || 0%{?fedora} || 0%{?mdkversion} || 0%{?mgaversion} || 0%{?suse_version} >= 1220
%if 0%{?rhel} == 4
BuildRequires:	xorg-x11-devel 
%else
BuildRequires:	libXext-devel 
BuildRequires:	libXtst-devel
BuildRequires:	libXinerama-devel
%endif
%endif

# dvb
BuildRequires:	gstreamer-devel
%if 0%{?suse_version}
BuildRequires:	gstreamer-0_10-plugins-base-devel
%endif
%if 0%{?rhel} == 4
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-devel
%endif
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	glibc-kernheaders 
%endif
%endif

%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
BuildRequires:	libxcb-devel
%endif

# xine-lib
%if 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
BuildRequires:	libxine-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	xine-lib-devel
%endif

# LAME
%if 0%{?suse_version}
BuildRequires:	libmp3lame-devel
%else
BuildRequires:	lame-devel
%endif

Requires:		%{name}-libs = %{version}-%{release}

%description
Kaffeine is a xine-based media player for TDE.  It plays back CDs,
and VCDs, and can decode all (local or streamed) multimedia formats 
supported by xine-lib.
Additionally, Kaffeine is fully integrated in TDE, it supports drag
and drop and provides an editable playlist, a bookmark system, a
Konqueror plugin, OSD and much more.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{tde_bindir}/kaffeine
%{tde_libdir}/libkaffeinepart.so
%{tde_tdelibdir}/lib*.*
%{tde_datadir}/appl*/*/*.desktop
%{tde_datadir}/apps/gstreamerpart/
%{tde_datadir}/apps/kaffeine/
%{tde_datadir}/apps/konqueror/servicemenus/*.desktop
%{tde_datadir}/apps/profiles/
%{tde_datadir}/icons/hicolor/*/*/*
%{tde_datadir}/mimelnk/*/*.desktop
%{tde_datadir}/service*/*.desktop
%{tde_tdedocdir}/HTML/en/kaffeine/

%post
touch --no-create %{tde_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{tde_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database >& /dev/null ||:
/sbin/ldconfig || :

%postun
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database >& /dev/null ||:
/sbin/ldconfig || :

##########

%package devel
Summary:		Development files for %{name}
Group:			Development/Libraries
Requires:		%{name}-libs = %{version}-%{release}
Requires:		trinity-tdelibs-devel

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kaffeine/
%{tde_libdir}/lib*.so
%exclude %{tde_libdir}/libkaffeinepart.so

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

##########

%package libs
Summary:		%{name} runtime libraries
Group:			System Environment/Libraries

# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires:		%{name} = %{version}-%{release}

%description libs
%{summary}.

%files libs
%defattr(-,root,root,-)
%{tde_libdir}/lib*.so.*

%post libs
/sbin/ldconfig || :

%postun libs
/sbin/ldconfig || :

##########


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"

%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export TDEDIR=%{tde_prefix}

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --mandir=%{tde_mandir} \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final \
  --disable-rpath \
  --with-xinerama \
  --with-gstreamer \
  --with-lame \
  --with-extra-libs=%{_prefix}/%{_lib} \
  --enable-closure \
%if 0%{?rhel} > 0 && 0%{?rhel} <= 5
  --without-dvb \
%endif
  

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

## File lists
# locale's
%find_lang %{tde_pkg}
# HTML (1.0)
HTML_DIR=$(tde-config --expandvars --install html)
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
rm -f $RPM_BUILD_ROOT%{tde_libdir}/lib*.la
rm -f $RPM_BUILD_ROOT%{tde_datadir}/mimelnk/application/x-mplayer2.desktop

%clean
rm -rf $RPM_BUILD_ROOT



%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.8.8-6
- Initial release for TDE 14.0.0

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.8.8-5
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.8-4
- Initial release for TDE 3.5.13.1

* Fri Aug 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.8-3
- Add support for Mageia 2 and Mandriva 2011
- Added automake initialization with proper program name and version [Bug #858] [Commit #4e982fa3]
- Fixed online hyperlink to win32 codecs download location. [Commit #5086f358]

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.8-2
- Rebuilt for Fedora 17
- Adds more patches from GIT.

* Mon Apr 23 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.8-1
- Updates version to 0.8.8
- Fix nominal "tqt" typos and fix slow DVB start. [Bug #729, #899]
- Change location where Kaffeine stores temporary pipe files from $HOME to the more appropriate $TDEHOME/tmp-$HOSTNAME.
- Work around Xine crash when displaying still logo image by creating a small movie file to replace it [Bug #511, #559]
- Add man page

* Sun Dec 04 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.6-2
- Disable 'libxcb-devel' for RHEL 5 compilation
- Fix HTML directory location

* Wed Nov 09 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.6-1
- Spec file based on Fedora 8 'kaffeine-0.8.6-3'
