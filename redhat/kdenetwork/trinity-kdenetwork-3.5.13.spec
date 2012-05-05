# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 4

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


# Fedora review:  http://bugzilla.redhat.com/195486

## Conditional build:
# disabled, for now, doesn't build -- Rex
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

# [kdenetwork] Fix kopete protocol compilation [Bug #695]
Patch10:	kdenetwork-3.5.13-kopete_msn_protocol.patch
Patch11:	kdenetwork-3.5.13-kopete_sms_protocol.patch
Patch12:	kdenetwork-3.5.13-kopete_jabber_protocol.patch
Patch13:	kdenetwork-3.5.13-kopete_motionawayplugin_ftbfs.patch
# [kdenetwork] Fix references to "qname.h" [Bug #700]
Patch14:	kdenetwork-3.5.13-reference_to_qmake_h.patch
# WTF is this ? shitty hack in autotool was forgotten in CMAKE port ! [Bug #695]
Source10:	kdenetwork-3.5.13-dummy.cpp

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
BuildRequires: openslp-devel
## kopete:
BuildRequires: libxml2-devel libxslt-devel
%ifarch %{ix86}
# BR: %{_includedir}/valgrind/valgrind.h
BuildRequires: valgrind
%endif
#jabber
BuildRequires: libidn-devel
#jabber/jingle
BuildRequires: expat-devel glib2-devel ortp-devel speex-devel
# jabber/ssl
#{?fedora:Requires(hint): qca-tls}
# sametime
BuildRequires: meanwhile-devel
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

BuildRequires: libgadu-devel
BuildRequires: speex-devel

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
Requires: trinity-kdelibs
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
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p4


# TDE 3.5.13: missing 'dummy.cpp' in MSN protocol
%__install -m 644 %{SOURCE10} kopete/protocols/msn/dummy.cpp

%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"
export LD_LIBRARY_PATH="%{_libdir}"

%__mkdir build
cd build
%cmake \
  -DWITH_JINGLE=ON \
  -DWITH_SPEEX=ON \
  -DWITH_WEBCAM=ON \
  -DWITH_GSM=OFF \
  -DWITH_ARTS=ON \
  -DBUILD_ALL=ON \
  -DBUILD_KOPETE_PROTOCOL_ALL=ON \
  -DBUILD_KOPETE_PLUGIN_ALL=ON \
  ..

# kdenetwork building is not SMP safe
%__make


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


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
ln -s /usr/bin/consolehelper %{buildroot}%{_bindir}/kppp
mkdir -p %{buildroot}/etc/security/console.apps
cat > %{buildroot}/etc/security/console.apps/kppp3 <<EOF
USER=root
PROGRAM=%{_sbindir}/kppp
SESSION=true
EOF
%endif

# ktalk
%__install -p -m 0644 -D  %{SOURCE2} %{buildroot}%{_sysconfdir}/xinetd.d/ktalk

# Add lisa startup script
%__install -p -m 0644 -D %{SOURCE4} %{buildroot}%{_sysconfdir}/lisarc
%__install -p -m 0755 -D %{SOURCE5} %{buildroot}%{_initrddir}/lisa

# RHEL 5: Avoids conflict with 'kdenetwork'
%if 0%{?rhel} == 5
%__mv -f %{buildroot}%{_sysconfdir}/lisarc %{buildroot}%{_sysconfdir}/lisarc.tde
%endif

# Avoids conflict with trinity-kvirc
%__mv -f %{buildroot}%{_datadir}/services/irc.protocol %{buildroot}%{_datadir}/apps/kopete/


%post
/sbin/chkconfig --add lisa ||:
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :
if [ -r %{_sysconfdir}/lisarc.tde ] && [ ! -r %{_sysconfdir}/lisarc ]; then
	cp -f %{_sysconfdir}/lisarc.tde %{_sysconfdir}/lisarc
fi

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

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

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
%{tde_docdir}/HTML/??/ksirc/
%{_bindir}/ksirc
%{_libdir}/libkdeinit_ksirc.*
%{tde_libdir}/ksirc.*
%{_datadir}/applications/kde/ksirc.desktop
%{_datadir}/apps/ksirc/
%config(noreplace) %{_datadir}/config/ksircrc
%{_datadir}/icons/hicolor/*/apps/ksirc.*

# kdict
%{tde_docdir}/HTML/en/kdict
%{_bindir}/kdict
%{tde_libdir}/kdict*
%{_libdir}/libkdeinit_kdict.*
%{_datadir}/applications/kde/kdict.desktop
%{_datadir}/apps/kdict
%{_datadir}/apps/kicker/applets/kdictapplet.desktop
%{_datadir}/icons/hicolor/*/apps/kdict.*

# ktalk
%{tde_docdir}/HTML/en/ktalkd
%{_bindir}/ktalkd*
%{tde_libdir}/kcm_ktalkd.*
%{_datadir}/applications/kde/kcmktalkd.desktop
%config(noreplace) %{_datadir}/config/ktalkdrc
%{_datadir}/icons/crystalsvg/*/apps/ktalkd.*
%{_datadir}/sounds/ktalkd.wav
%config(noreplace) %{_sysconfdir}/xinetd.d/ktalk

# kpf
%{tde_docdir}/HTML/en/kpf
%{tde_libdir}/kpf*
%{_datadir}/apps/kicker/applets/kpfapplet.desktop
%{_datadir}/icons/crystalsvg/*/apps/kpf.*
%{_datadir}/services/kpfpropertiesdialogplugin.desktop

%if "%{?_with_wifi:1}" == "1"
# kwifimanager
%doc %{tde_docdir}/HTML/en/kwifimanager
%{_bindir}/kwifimanager
%{tde_libdir}/kcm_wifi.*
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
%{tde_libdir}/*nowlistening*
%endif

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README

# ksirc
%exclude %{_bindir}/ksirc
%exclude %{_libdir}/libkdeinit_ksirc.*
%exclude %{tde_libdir}/ksirc.*
%exclude %{_datadir}/applications/kde/ksirc.desktop
%exclude %{_datadir}/apps/ksirc/
%exclude %{_datadir}/config/ksircrc
%exclude %{tde_docdir}/HTML/??/ksirc/
%exclude %{_datadir}/icons/hicolor/??x??/apps/ksirc.png

# kdict
%exclude %{tde_docdir}/HTML/en/kdict
%exclude %{_bindir}/kdict
%exclude %{tde_libdir}/kdict*
%exclude %{_libdir}/libkdeinit_kdict.*
%exclude %{_datadir}/applications/kde/kdict.desktop
%exclude %{_datadir}/apps/kdict
%exclude %{_datadir}/apps/kicker/applets/kdictapplet.desktop
%exclude %{_datadir}/icons/hicolor/128x128/apps/kdict.png
%exclude %{_datadir}/icons/hicolor/??x??/apps/kdict.png
%exclude %{_datadir}/icons/hicolor/scalable/apps/kdict.svgz

# ktalk
%exclude %{tde_docdir}/HTML/en/ktalkd
%exclude %{_sysconfdir}/xinetd.d/ktalk
%exclude %{_bindir}/ktalkd*
%exclude %{tde_libdir}/kcm_ktalkd.*
%exclude %{_datadir}/applications/kde/kcmktalkd.desktop
%exclude %{_datadir}/config/ktalkdrc
%exclude %{_datadir}/icons/crystalsvg/128x128/apps/ktalkd.png
%exclude %{_datadir}/icons/crystalsvg/??x??/apps/ktalkd.png
%exclude %{_datadir}/sounds/ktalkd.wav

# kpf
%exclude %{tde_libdir}/kpf*
%exclude %{_datadir}/apps/kicker/applets/kpfapplet.desktop
%exclude %{tde_docdir}/HTML/en/kpf
%exclude %{_datadir}/icons/crystalsvg/??x??/apps/kpf.png
%exclude %{_datadir}/services/kpfpropertiesdialogplugin.desktop

%ifnarch s390 s390x
# kwifimanager
%exclude %{_bindir}/kwifimanager
%exclude %{tde_libdir}/kcm_wifi.*
%exclude %{_datadir}/applications/kde/kcmwifi.desktop
%exclude %{_datadir}/applications/kde/kwifimanager.desktop
%exclude %{_datadir}/apps/kwifimanager
%exclude %{tde_docdir}/HTML/en/kwifimanager
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
%exclude %{tde_libdir}/*nowlistening*
%endif

%if %console_helper
%config(noreplace) /etc/security/console.apps/kppp3
%config(noreplace) /etc/pam.d/kppp3
%{_sbindir}/kppp
%else
%attr(4755,root,root) %{_bindir}/kppp
%endif
%config(noreplace) %{_sysconfdir}/lisarc*
%config(noreplace) %{_initrddir}/lisa
%{_libdir}/libkdeinit_*.so
%{tde_libdir}/*
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
%{_includedir}/*
%{_libdir}/libkopete*.so
%{_libdir}/librss.so


%changelog
* Sun Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Enable Kopete protocols & plugins compilation
- Enables all features (openslp, jingle, ...) on all distros
- Moves 'irc.protocol' file to prevent conflict with other packages

* Thu Nov 17 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Fix symbolic link to 'consolehelper'

* Sat Nov 12 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Removes conflict on file 'lisarc' for RHEL 5

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Tue Oct 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT

