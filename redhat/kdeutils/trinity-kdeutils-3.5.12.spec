# Default version for this component
%if "%{?version}" == ""
%define version 3.5.12
%endif
%define release 6

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


Name:		trinity-kdeutils
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}
License:	GPL
Summary:	TDE Utilities
Group:		Applications/System

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}

Source0:	kdeutils-%{version}.tar.gz
Source1: klaptop_acpi_helper.pam
Source2: klaptop_acpi_helper.console
Source3: kcmlaptoprc

BuildRequires:	tqtinterface
BuildRequires:	trinity-arts
BuildRequires:	trinity-kdelibs

# RedHat / Fedora legacy patches
Patch1: kdf-3.0.2-label.patch

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Requires:	tqtinterface
Requires:	trinity-kdelibs

BuildRequires: gettext
BuildRequires: net-snmp-devel
BuildRequires: python-devel
BuildRequires: gmp-devel
%if 0%{?fedora} > 4 || 0%{?rhel} > 4
BuildRequires: libXScrnSaver-devel libXtst-devel
%endif
BuildRequires: xmms-devel

%define superkaramba_ver 0.39
Obsoletes: superkaramba < 0:%{superkaramba_ver}
Provides:  superkaramba = 0:%{superkaramba_ver}

%description
Utilities for the Trinity Desktop Environment, including:
  * ark (tar/gzip archive manager)
  * kcalc (scientific calculator)
  * kcharselect (character selector)
  * kdepasswd (change password)
  * kdessh (ssh front end)
  * kdf (view disk usage)
  * kedit (simple text editor)
  * kfloppy (floppy formatting tool)
  * kgpg (gpg gui)
  * khexedit (hex editor)
  * kjots (note taker)
  * kregexpeditor (regular expression editor)
  * ktimer (task scheduler)
  * kwikdisk (removable media utility)

# afaik, nobody BR's it, and it pulls kdeutils into multilib -- Rex
%package devel
Summary: Development files for %{name} 
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: %{name}-extras = %{version}-%{release}
Requires: trinity-kdelibs-devel
%description devel
Development files for %{name}.

%package extras
Summary: Extras packages from %{name} 
Group: Applications/Internet
Requires: %{name} = %{version}-%{release}
%if 0%{?fedora} > 5 || 0%{?rhel} > 4
Requires: pm-utils
%endif
Requires: usermode
%description extras
More Utilities for the K Desktop Environment:
 * kmilo
 * ksim (system information monitor);
 * klaptopdaemon (battery monitoring and management for laptops);


%prep
%setup -q -n kdeutils

%patch1 -p1 -b .label

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f admin/Makefile.common

%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
   --enable-new-ldflags \
   --disable-dependency-tracking \
   --disable-rpath \
   --disable-debug --disable-warnings \
   --enable-final \
   --includedir=%{tde_includedir} \
   --with-snmp \
   --with-xscreensaver \
   --with-extra-includes=%{_includedir}/tqt \
   --enable-closure

%__make %{?_smp_mflags}

%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{?buildroot}
%make_install

# Show only in KDE (really? -- Rex)
for i in kcalc kregexpeditor Kjots ktimer kdf kcmdf ksim KFloppy KEdit \
  KCharSelect ark kwalletmanager kwalletconfig \
 irkick kcmlirc laptop pcmcia kvaio thinkpad kwikdisk; do
 if [ -f %{buildroot}%{_datadir}/applications/kde/$i.desktop ] ; then
   echo "OnlyShowIn=KDE;" >> %{buildroot}%{_datadir}/applications/kde/$i.desktop
 fi
done

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
        [ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../common $i/common
      done
    popd
    pushd $lang_dir/kcontrol
      for i in *; do
        [ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../../common $i/common
      done
    popd
  fi
done
fi

# using pam
install -p -D -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/pam.d/klaptop_acpi_helper
install -p -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/security/console.apps/klaptop_acpi_helper

pushd %{buildroot}%{_bindir}
  mkdir -p %{buildroot}%{_sbindir}
  mv klaptop_acpi_helper ../sbin
  ln -s consolehelper klaptop_acpi_helper
popd

# klaptop setting
install -p -D -m 644 %{SOURCE3} %{buildroot}%{_datadir}/config/kcmlaptoprc


%clean
%__rm -rf %{?buildroot}


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
  touch --no-create %{_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%post extras
/sbin/ldconfig
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done

%postun extras
/sbin/ldconfig
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done


%files extras
%defattr(-,root,root,-)

# kmilo
%{tde_libdir}/kded_kmilod.*
%{tde_libdir}/kmilo*
%{_libdir}/libkmilo.la
%{_libdir}/libkmilo.so.*
%{_datadir}/services/kded/kmilod.desktop
%{_datadir}/services/kmilo
%{_datadir}/servicetypes/kmilo

# ksim
%{tde_docdir}/HTML/*/ksim/
%{tde_libdir}/ksim*
%{_libdir}/libksimcore.la
%{_libdir}/libksimcore.so.*
%{_datadir}/apps/kicker/extensions/ksim.desktop
%{_datadir}/apps/ksim/
%config %{_datadir}/config/ksim_panelextensionrc
%{_datadir}/icons/crystalsvg/??x??/apps/ksim.png
%{_datadir}/icons/crystalsvg/16x16/devices/ksim_cpu.png

# klaptop
%{tde_docdir}/HTML/en/kcontrol
%{_sysconfdir}/pam.d/klaptop_acpi_helper
%attr(644,root,root) %{_sysconfdir}/security/console.apps/klaptop_acpi_helper
%{_bindir}/klaptop*
%{tde_libdir}/kded_klaptopdaemon.*
%{_sbindir}/klaptop_acpi_helper
%{_datadir}/apps/klaptopdaemon
%{_datadir}/services/kded/klaptopdaemon.desktop
%{tde_libdir}/kcm_laptop.*
%{_libdir}/libkcmlaptop.*
%{_datadir}/applications/kde/laptop.desktop
%config %{_datadir}/config/kcmlaptoprc
%{_datadir}/icons/crystalsvg/128x128/apps/laptop_battery.png
%{_datadir}/icons/crystalsvg/??x??/apps/laptop_battery.png
%{_datadir}/icons/crystalsvg/scalable/apps/laptop_battery.svgz


%files -f %{name}.lang
%defattr(-,root,root,-)

# kmilo
%exclude %{tde_libdir}/kded_kmilod.*
%exclude %{tde_libdir}/kmilo*
%exclude %{_libdir}/libkmilo.la
%exclude %{_libdir}/libkmilo.so.*
%exclude %{_datadir}/services/kded/kmilod.desktop
%exclude %{_datadir}/services/kmilo
%exclude %{_datadir}/servicetypes/kmilo

# ksim
%exclude %{tde_docdir}/HTML/*/ksim/
%exclude %{tde_libdir}/ksim*
%exclude %{_libdir}/libksimcore.la
%exclude %{_libdir}/libksimcore.so.*
%exclude %{_datadir}/apps/kicker/extensions/ksim.desktop
%exclude %{_datadir}/apps/ksim/
%exclude %{_datadir}/config/ksim_panelextensionrc
%exclude %{_datadir}/icons/crystalsvg/??x??/apps/ksim.png
%exclude %{_datadir}/icons/crystalsvg/16x16/devices/ksim_cpu.png

# klaptop
%exclude %{_sysconfdir}/pam.d/klaptop_acpi_helper
%exclude %{_sysconfdir}/security/console.apps/klaptop_acpi_helper
%exclude %{_bindir}/klaptop*
%exclude %{tde_libdir}/kded_klaptopdaemon.*
%exclude %{_sbindir}/klaptop_acpi_helper
%exclude %{_datadir}/apps/klaptopdaemon
%exclude %{_datadir}/services/kded/klaptopdaemon.desktop
%exclude %{tde_libdir}/kcm_laptop.*
%exclude %{_libdir}/libkcmlaptop.*
%exclude %{_datadir}/applications/kde/laptop.desktop
%exclude %{_datadir}/config/kcmlaptoprc
%exclude %{tde_docdir}/HTML/en/kcontrol/
%exclude %{_datadir}/icons/crystalsvg/128x128/apps/laptop_battery.png
%exclude %{_datadir}/icons/crystalsvg/??x??/apps/laptop_battery.png
%exclude %{_datadir}/icons/crystalsvg/scalable/apps/laptop_battery.svgz

%{tde_docdir}/HTML/en/*
%attr(644,root,root) %{_sysconfdir}/security/console.apps/*
%attr(644,root,root) %{_sysconfdir}/pam.d/*
%{_bindir}/*
%{_sbindir}/*
%{tde_libdir}/*
%{_libdir}/*.la
%{_libdir}/libkdeinit*.so
%{_libdir}/lib*.so.*
%{_datadir}/icons/*/*/*/*
%{_datadir}/apps/*
%config %{_datadir}/config/*
%{_datadir}/config.kcfg/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/applications/kde/*
%if 0%{?rhel} >= 6
%{_datadir}/applnk/Utilities/*
%{_datadir}/mimelnk/application/*
%endif
%{_datadir}/autostart/*

%files devel
%defattr(-,root,root,-)
%{tde_includedir}/*
%{_libdir}/libkcmlaptop.so
%{_libdir}/libkhexeditcommon.so
%{_libdir}/libkmilo.so
%{_libdir}/libkregexpeditorcommon.so
%{_libdir}/libksimcore.so


%changelog
* Mon Sep 12 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-6
- Merge Spec file from Fedora8 "kdeutils-3.5.10-6"

* Sun Sep 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-5
- Import to GIT

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-4
- Correct (again) macro to install under "/opt", if desired

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-3
- Correct macro to install under "/opt", if desired

* Sun Dec 19 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-2
- Rebuilt

* Fri Dec 17 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-1
- Add macro _kde3_prefix to define custom installation prefix (ex: /opt/kde3)
- Add '--with-extra-includes=%{_includedir}/tqt'

* Wed Dec 15 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.12-0
- Initial version

