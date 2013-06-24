# Default version for this component
%if "%{?version}" == ""
%define version 3.5.12
%endif
%define release 5

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


# Fedora review:  http://bugzilla.redhat.com/195486

## Conditional build:
# disabled, for now, doesn't build -- Rex
#define _enable_jingle --enable-jingle
%define _enable_sametime_plugin --enable-sametime-plugin
#define _enable_slp --enable-slp
# RHEL6: xmms is outdated !
#define _with_xmms --with-xmms
%ifnarch s390 s390x
%define _with_wifi --with-wifi
%endif

%define console_helper 1 

Name:    trinity-kdenetwork
Version: %{?version}
Release: %{?release}%{?dist}%{?_variant}
Summary: K Desktop Environment - Network Applications

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

License: GPLv2
Group:   Applications/Internet

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides: kdenetwork3 = %{version}-%{release}

Source0: kdenetwork-%{version}.tar.gz
Source1: kppp.pamd
Source2: ktalk
Source4: lisarc
Source5: lisa.redhat

# RedHat/Fedora legacy patches
Patch3: kdenetwork-3.5.8-kppp.patch
Patch4: kdenetwork-3.2.3-resolv.patch
# include more/proper ppp headers
Patch6: kdenetwork-3.5.9-krfb_httpd.patch

# Trinity official patches, from SVN
# Use libv4l1-videodev.h when available in kdenetwork
Patch7: r1243951.diff

# Trinity unofficial patches
#  Compiling Kopete for Fedora15 ...
Patch8: kdenetwork-kopete-gcc45.patch

Requires: %{name}-libs = %{version}-%{release}

BuildRequires: gettext
BuildRequires: trinity-kdelibs-devel
BuildRequires: coreutils 
BuildRequires: openssl-devel
%if 0%{?fedora} > 4 || 0%{?rhel} > 4
BuildRequires: libXmu-devel libXScrnSaver-devel libXtst-devel libXxf86vm-devel
%endif
%if "%{?_with_wifi:1}" == "1"
%if 0%{?fedora} > 5 || 0%{?rhel} > 4
BuildRequires: wireless-tools-devel
%else
BuildRequires: wireless-tools
%endif
%endif
%{?_enable_slp:BuildRequires: openslp-devel}
## kopete:
BuildRequires: libxml2-devel libxslt-devel
%ifarch %{ix86}
# BR: %{_includedir}/valgrind/valgrind.h
BuildRequires: valgrind
%endif
#jabber
BuildRequires: libidn-devel
#jabber/jingle
%{?_enable_jingle:BuildRequires: expat-devel glib2-devel ortp-devel speex-devel}
# jabber/ssl
#{?fedora:Requires(hint): qca-tls}
# sametime
%{?_enable_sametime_plugin:BuildRequires: meanwhile-devel}
%{?_with_xmms:BuildRequires: xmms-devel}
Requires: jasper
## kppp
Requires: ppp
## krdc
Requires: rdesktop
## lisa
Requires(preun):  chkconfig
Requires(post):   chkconfig
#Requires(hint): samba-client
BuildRequires:  avahi-qt3-devel

%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
BuildRequires:	libv4l-devel
%endif

%if 0%{?console_helper}
Requires: usermode-gtk
%endif


%description
Networking applications, including:
* kget: downloader manager
* kio_lan: lan browsing kio slave
* knewsticker: RDF newsticker applet
* kopete: chat client
* kppp: dialer and front end for pppd
* krdc: a client for Desktop Sharing and other VNC servers
* krfb: Desktop Sharing server, allow others to access your desktop via VNC
* lisa: lan information server

%package devel
Summary: Development files for %{name} 
Group: Development/Libraries
Provides: kdenetwork3-devel = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Requires: trinity-kdelibs-devel
%description devel
%{summary}. 

%package extras
Summary: Extras packages for %{name} 
Group: Applications/Internet
Requires: %{name}-libs = %{version}-%{release}
%if "%{?_with_xmms:1}" == "1"
Obsoletes: %{name}-nowlistening < %{version}-%{release}
Provides:  %{name}-nowlistening = %{version}-%{release}
%endif
%description extras
More Networking applications for the K Desktop Environment:
 * ksirc
 * kdict
 * ktalkd
 * kpf
 * kwifimanager
%if "%{?_with_xmms:1}" == "1"
 * nowlistening (xmms) plugin for Kopete.
%endif

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-kdelibs >= %{version}
# helps multilib upgrades
Obsoletes: %{name} < %{version}-%{release}
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%setup -q -n kdenetwork

%if %{console_helper}
%patch3 -p1 -b .kppp
%endif
%patch4 -p1 -b .resolv
%patch6 -p1 -b .krfb_httpd
%patch7 -p1
%patch8 -p1

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure                        \
   --enable-new-ldflags           \
   --disable-dependency-tracking  \
   --disable-rpath                \
   --disable-debug                \
   --disable-warnings             \
   --enable-final                 \
   --includedir=%{tde_includedir} \
  %{?_enable_jingle} %{!?_enable_jingle:--disable-jingle} \
  %{?_enable_sametime_plugin} %{!?_enable_sametime_plugin:--disable-sametime-plugin} \
  %{?_enable_slp} %{!?_enable_slp:--disable-slp} \
  %{?_with_wifi} %{!?_with_wifi:--without-wifi} \
  %{?_with_xmms} %{!?_with_xmms:--without-xmms} \
  --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}

%__make install DESTDIR=%{buildroot}
# RHEL6: kppp seems to be not installed by previous command ???
%__make install DESTDIR=%{buildroot} -C kppp


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
        [ -d $i -a -L $i/common ] && %{__rm} -f $i/common && ln -sf ../common $i/common
      done
    popd
  fi
done
fi

# Show only in KDE, FIXME, need to re-evaluate these -- Rex
for i in fileshare kcmkrfb kcmktalkd kcmwifi krfb kppp kppplogview \
   kwifimanager kget knewsticker ksirc kdict ; do
   if [ -f %{buildroot}%{_datadir}/applications/kde/$i.desktop ] ; then
      echo "OnlyShowIn=KDE;" >> %{buildroot}%{_datadir}/applications/kde/$i.desktop
   fi
done

%if %console_helper
# Run kppp through consolehelper
install -p -m644 -D %{SOURCE1} %{buildroot}/etc/pam.d/kppp3
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/kppp %{buildroot}%{_sbindir}
ln -s consolehelper %{buildroot}%{_bindir}/kppp
mkdir -p %{buildroot}/etc/security/console.apps
cat > %{buildroot}/etc/security/console.apps/kppp3 <<EOF
USER=root
PROGRAM=%{_sbindir}/kppp
SESSION=true
EOF
%endif

# ktalk
install -p -m 0644 -D  %{SOURCE2} %{buildroot}%{_sysconfdir}/xinetd.d/ktalk

# Add lisa startup script
install -p -m 0644 -D %{SOURCE4} %{buildroot}%{_sysconfdir}/lisarc
install -p -m 0755 -D %{SOURCE5} %{buildroot}%{_initrddir}/lisa

%post
/sbin/chkconfig --add lisa ||:
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

%preun
if [ $1 -eq 0 ]; then
  /sbin/chkconfig --del lisa ||:
  /sbin/service lisa stop > /dev/null 2>&1 ||:
fi

%post libs
/sbin/ldconfig

%postun libs
/sbin/ldconfig

%post extras
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done

%postun extras
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done


%clean
%__rm -rf %{buildroot}


%files extras
%defattr(-,root,root,-)

# ksirc
%{_docdir}/HTML/??/ksirc/
%{_bindir}/ksirc
%{_libdir}/libkdeinit_ksirc.*
%{_libdir}/kde3/ksirc.*
%{_datadir}/applications/kde/ksirc.desktop
%{_datadir}/apps/ksirc/
%config(noreplace) %{_datadir}/config/ksircrc
%{_datadir}/icons/hicolor/*/apps/ksirc.*

# kdict
%{_docdir}/HTML/en/kdict
%{_bindir}/kdict
%{_libdir}/kde3/kdict*
%{_libdir}/libkdeinit_kdict.*
%{_datadir}/applications/kde/kdict.desktop
%{_datadir}/apps/kdict
%{_datadir}/apps/kicker/applets/kdictapplet.desktop
%{_datadir}/icons/hicolor/*/apps/kdict.*

# ktalk
%{_docdir}/HTML/en/ktalkd
%{_bindir}/ktalkd*
%{_libdir}/kde3/kcm_ktalkd.*
%{_datadir}/applications/kde/kcmktalkd.desktop
%config(noreplace) %{_datadir}/config/ktalkdrc
%{_datadir}/icons/crystalsvg/*/apps/ktalkd.*
%{_datadir}/sounds/ktalkd.wav
%config(noreplace) %{_sysconfdir}/xinetd.d/ktalk

# kpf
%{_docdir}/HTML/en/kpf
%{_libdir}/kde3/kpf*
%{_datadir}/apps/kicker/applets/kpfapplet.desktop
%{_datadir}/icons/crystalsvg/*/apps/kpf.*
%{_datadir}/services/kpfpropertiesdialogplugin.desktop

%if "%{?_with_wifi:1}" == "1"
# kwifimanager
%doc %{_docdir}/HTML/en/kwifimanager
%{_bindir}/kwifimanager
%{_libdir}/kde3/kcm_wifi.*
%{_datadir}/applications/kde/kcmwifi.desktop
%{_datadir}/applications/kde/kwifimanager.desktop
%{_datadir}/apps/kwifimanager
%{_datadir}/icons/hicolor/*/apps/kwifimanager.png
%endif

%if "%{?_with_xmms:1}" == "1"
#files nowlistening
#defattr(-,root,root,-)
%{_datadir}/apps/kopete/*nowlisteningchatui*
%{_datadir}/apps/kopete/*nowlisteningui*
%{_datadir}/services/kconfiguredialog/*nowlistening*
%{_datadir}/services/*nowlistening*
%{_libdir}/kde3/*nowlistening*
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README

# ksirc
%exclude %{_bindir}/ksirc
%exclude %{_libdir}/libkdeinit_ksirc.*
%exclude %{_libdir}/kde3/ksirc.*
%exclude %{_datadir}/applications/kde/ksirc.desktop
%exclude %{_datadir}/apps/ksirc/
%exclude %{_datadir}/config/ksircrc
%exclude %{_docdir}/HTML/??/ksirc/
%exclude %{_datadir}/icons/hicolor/??x??/apps/ksirc.png

# kdict
%exclude %{_docdir}/HTML/en/kdict
%exclude %{_bindir}/kdict
%exclude %{_libdir}/kde3/kdict*
%exclude %{_libdir}/libkdeinit_kdict.*
%exclude %{_datadir}/applications/kde/kdict.desktop
%exclude %{_datadir}/apps/kdict
%exclude %{_datadir}/apps/kicker/applets/kdictapplet.desktop
%exclude %{_datadir}/icons/hicolor/128x128/apps/kdict.png
%exclude %{_datadir}/icons/hicolor/??x??/apps/kdict.png
%exclude %{_datadir}/icons/hicolor/scalable/apps/kdict.svgz

# ktalk
%exclude %{_docdir}/HTML/en/ktalkd
%exclude %{_sysconfdir}/xinetd.d/ktalk
%exclude %{_bindir}/ktalkd*
%exclude %{_libdir}/kde3/kcm_ktalkd.*
%exclude %{_datadir}/applications/kde/kcmktalkd.desktop
%exclude %{_datadir}/config/ktalkdrc
%exclude %{_datadir}/icons/crystalsvg/128x128/apps/ktalkd.png
%exclude %{_datadir}/icons/crystalsvg/??x??/apps/ktalkd.png
%exclude %{_datadir}/sounds/ktalkd.wav

# kpf
%exclude %{_libdir}/kde3/kpf*
%exclude %{_datadir}/apps/kicker/applets/kpfapplet.desktop
%exclude %{_docdir}/HTML/en/kpf
%exclude %{_datadir}/icons/crystalsvg/??x??/apps/kpf.png
%exclude %{_datadir}/services/kpfpropertiesdialogplugin.desktop

%ifnarch s390 s390x
# kwifimanager
%exclude %{_bindir}/kwifimanager
%exclude %{_libdir}/kde3/kcm_wifi.*
%exclude %{_datadir}/applications/kde/kcmwifi.desktop
%exclude %{_datadir}/applications/kde/kwifimanager.desktop
%exclude %{_datadir}/apps/kwifimanager
%exclude %{_docdir}/HTML/en/kwifimanager
%exclude %{_datadir}/icons/hicolor/128x128/apps/kwifimanager.png
%exclude %{_datadir}/icons/hicolor/??x??/apps/kwifimanager.png
%exclude %{_datadir}/icons/hicolor/scalable/apps/kwifimanager.svgz
%endif

# nowlistening
%if "%{?_with_xmms:1}" == "1"
%exclude %{_datadir}/apps/kopete/*nowlisteningchatui*
%exclude %{_datadir}/apps/kopete/*nowlisteningui*
%exclude %{_datadir}/services/kconfiguredialog/*nowlistening*
%exclude %{_datadir}/services/*nowlistening*
%exclude %{_libdir}/kde3/*nowlistening*
%endif

%{_docdir}/HTML/en/*
%if %console_helper
%config(noreplace) /etc/security/console.apps/kppp3
%config(noreplace) /etc/pam.d/kppp3
%{_sbindir}/kppp
%else
%attr(4755,root,root) %{_bindir}/kppp
%endif
%config(noreplace) %{_sysconfdir}/lisarc
%config(noreplace) %{_initrddir}/lisa
%{_libdir}/libkdeinit_*.so
%if "%{?_with_wifi:1}" == "1"
%{_libdir}/libkwireless.*
%endif
%{_libdir}/kde3/*
%{_libdir}/kconf_update_bin/*
%{_bindir}/*
%{_datadir}/apps/*
%{_datadir}/applications/kde/*
%{_datadir}/applnk/.hidden/*
%{_datadir}/config/*
%{_datadir}/config.kcfg/*
%{_datadir}/icons/*/*/*/*
%{_datadir}/mimelnk/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/sounds/*

%files libs
%defattr(-,root,root,-)
%{_libdir}/libkopete*.so.*
%{_libdir}/libkopete*.la
%{_libdir}/librss.so.*
%{_libdir}/librss.la

%files devel
%defattr(-,root,root,-)
%{_includedir}/kde/*
%{_libdir}/libkopete*.so
%{_libdir}/librss.so


%changelog
* Mon Sep 19 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-5
- Add support for RHEL5

* Sun Sep 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-4
- Import to GIT

* Tue Aug 23 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-3
- Add correction for Fedora 15
- Add patch7 for V4L compilation

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-2
- Correct macro to install under "/opt", if desired

* Fri Aug 05 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-1
- Initial version
- Spec file based on Fedora 8 "kdenetwork 7:3.5.10-1"

