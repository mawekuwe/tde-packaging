# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_version 3.5.13.2

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_sbindir %{tde_prefix}/sbin

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:		trinity-tdeutils
Version:	%{tde_version}
Release:	%{?!preversion:3}%{?preversion:2_%{preversion}}%{?dist}%{?_variant}
License:	GPL
Summary:	TDE Utilities
Group:		Applications/System

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Source1:	klaptop_acpi_helper.pam
Source2:	klaptop_acpi_helper.console
Source3:	kcmlaptoprc

Patch1:		kdeutils-3.5.13.2-rhel4.patch

Obsoletes:	trinity-kdeutils < %{version}-%{release}
Provides:	trinity-kdeutils = %{version}-%{release}
Obsoletes:	trinity-kdeutils-extras < %{version}-%{release}
Provides:	trinity-kdeutils-extras = %{version}-%{release}
Obsoletes:	tdeutils < %{version}-%{release}
Provides:	tdeutils = %{version}-%{release}

BuildRequires:	cmake >= 2.8
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	autoconf automake libtool m4
BuildRequires:	gettext
BuildRequires:	net-snmp-devel
BuildRequires:	python-devel
BuildRequires:	gmp-devel

%if 0%{?fedora} >= 5 || 0%{?rhel} >= 5
BuildRequires:	libXScrnSaver-devel
BuildRequires:	libXtst-devel
%endif

#%if 0%{?fedora}
#BuildRequires:	xmms-devel
#%endif

# KLAPTOPDAEMON
#  Not for RHEL 4!
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define build_klaptopdaemon 1
%endif

# XSCREENSAVER support
#  Not for RHEL 4!
%if 0%{?rhel} >= 5 || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion} || 0%{?suse_version}
%define with_xscreensaver 1
%endif

# CONSOLEHELPER (usermode) support
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%define with_consolehelper 1

# Avoids relinking, which breaks consolehelper
%define dont_relink 1
%endif


Requires: trinity-ark = %{version}-%{release}
Requires: trinity-kcalc = %{version}-%{release}
Requires: trinity-kcharselect = %{version}-%{release}
Requires: trinity-kdelirc = %{version}-%{release}
Requires: trinity-kdessh = %{version}-%{release}
Requires: trinity-kdf = %{version}-%{release}
Requires: trinity-kedit = %{version}-%{release}
Requires: trinity-kfloppy = %{version}-%{release}
Requires: trinity-kgpg = %{version}-%{release}
Requires: trinity-khexedit = %{version}-%{release}
Requires: trinity-kjots = %{version}-%{release}
%{?build_klaptopdaemon:Requires: trinity-klaptopdaemon = %{version}-%{release}}
Requires: trinity-kmilo = %{version}-%{release}
Requires: trinity-kmilo-legacy = %{version}-%{release}
Requires: trinity-kregexpeditor = %{version}-%{release}
Requires: trinity-ksim = %{version}-%{release}
Requires: trinity-ktimer = %{version}-%{release}
Requires: trinity-kwalletmanager = %{version}-%{release}
Requires: trinity-superkaramba = %{version}-%{release}


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
%if 0%{?build_klaptopdaemon}
  * klaptopdaemon (battery monitoring and management for laptops);
%endif
  * kmilo
  * kregexpeditor (regular expression editor)
  * ksim (system information monitor);
  * ktimer (task scheduler)
  * kwikdisk (removable media utility)

%files

##########

%package -n trinity-ark
Summary:	graphical archiving tool for Trinity
Group:		Applications/Utilities
#Requires:	ncompress
Requires:	unzip
Requires:	zip
#Requires:	zoo
Requires:	bzip2
#Requires:	p7zip
#Requires:	xz
#Requires:	lzma
#Requires:	rar, unrar

%description -n trinity-ark
Ark is a graphical program for managing various archive formats within the
TDE environment. Archives can be viewed, extracted, created and modified
from within Ark.
 
The program can handle various formats such as tar, gzip, bzip2, zip, rar and
lha (if appropriate command-line programs are installed).

Ark can work closely with Konqueror in the KDE environment to handle archives,
if you install the Konqueror Integration plugin available in the konq-plugins
package.

%files -n trinity-ark
%defattr(-,root,root,-)
%{tde_bindir}/ark
%{tde_tdelibdir}/ark.la
%{tde_tdelibdir}/ark.so
%{tde_tdelibdir}/libarkpart.la
%{tde_tdelibdir}/libarkpart.so
%{tde_libdir}/libkdeinit_ark.so
%{tde_tdeappdir}/ark.desktop
%{tde_datadir}/apps/ark/
%{tde_datadir}/config.kcfg/ark.kcfg
%{tde_datadir}/icons/hicolor/*/apps/ark.png
%{tde_datadir}/icons/hicolor/scalable/apps/ark.svgz
%{tde_datadir}/services/ark_part.desktop
%{tde_tdedocdir}/HTML/en/ark/

%post -n trinity-ark
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-ark
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kcalc
Summary:	calculator for Trinity
Group:		Applications/Utilities

%description -n trinity-kcalc
KCalc is TDE's scientific calculator.

It provides:
* trigonometric functions, logic operations, and statistical calculations
* easy cut and paste of numbers from/into its display
* a results-stack which lets you conveniently recall previous results
* configurable precision, and number of digits after the period

%files -n trinity-kcalc
%defattr(-,root,root,-)
%{tde_bindir}/kcalc
%{tde_tdelibdir}/kcalc.la
%{tde_tdelibdir}/kcalc.so
%{tde_libdir}/libkdeinit_kcalc.so
%{tde_tdeappdir}/kcalc.desktop
%{tde_datadir}/apps/kcalc/
%{tde_datadir}/apps/kconf_update/kcalcrc.upd
%{tde_datadir}/config.kcfg/kcalc.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kcalc.png
%{tde_datadir}/icons/hicolor/scalable/apps/kcalc.svgz
%{tde_tdedocdir}/HTML/en/kcalc/

%post -n trinity-kcalc
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kcalc
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kcharselect
Summary:	character selector for Trinity
Group:		Applications/Utilities

%description -n trinity-kcharselect
A character set selector for TDE.

%files -n trinity-kcharselect
%defattr(-,root,root,-)
%{tde_bindir}/kcharselect
%{tde_tdelibdir}/kcharselect_panelapplet.la
%{tde_tdelibdir}/kcharselect_panelapplet.so
%{tde_tdeappdir}/KCharSelect.desktop
%{tde_datadir}/apps/kcharselect/
%{tde_datadir}/apps/kconf_update/kcharselect.upd
%{tde_datadir}/apps/kicker/applets/kcharselectapplet.desktop
%{tde_datadir}/icons/hicolor/*/apps/kcharselect.png
%{tde_tdedocdir}/HTML/en/kcharselect/

%post -n trinity-kcharselect
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kcharselect
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kdelirc
Summary:	infrared control for Trinity
Group:		Applications/Utilities

%description -n trinity-kdelirc
This is a frontend for the LIRC suite to use infrared devices with TDE.

%files -n trinity-kdelirc
%defattr(-,root,root,-)
%{tde_bindir}/irkick
%{tde_tdelibdir}/irkick.la
%{tde_tdelibdir}/irkick.so
%{tde_tdelibdir}/kcm_kcmlirc.la
%{tde_tdelibdir}/kcm_kcmlirc.so
%{tde_libdir}/libkdeinit_irkick.so
%{tde_tdeappdir}/irkick.desktop
%{tde_tdeappdir}/kcmlirc.desktop
%{tde_datadir}/apps/irkick/
%{tde_datadir}/apps/profiles/klauncher.profile.xml
%{tde_datadir}/apps/profiles/konqueror.profile.xml
%{tde_datadir}/apps/profiles/noatun.profile.xml
%{tde_datadir}/apps/profiles/profile.dtd
%{tde_datadir}/apps/remotes/RM-0010.remote.xml
%{tde_datadir}/apps/remotes/cimr100.remote.xml
%{tde_datadir}/apps/remotes/hauppauge.remote.xml
%{tde_datadir}/apps/remotes/remote.dtd
%{tde_datadir}/apps/remotes/sherwood.remote.xml
%{tde_datadir}/apps/remotes/sonytv.remote.xml
%{tde_datadir}/autostart/irkick.desktop
%{tde_datadir}/icons/hicolor/*/apps/irkick.png
%{tde_datadir}/icons/locolor/*/apps/irkick.png
%{tde_tdedocdir}/HTML/en/irkick/
%{tde_tdedocdir}/HTML/en/kcmlirc/

%post -n trinity-kdelirc
/sbin/ldconfig
for f in hicolor locolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kdelirc
/sbin/ldconfig
for f in hicolor locolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kdessh
Summary:	ssh frontend for Trinity
Group:		Applications/Utilities
%if 0%{?suse_version}
Requires:	openssh
%else
Requires:	openssh-clients
%endif

%description -n trinity-kdessh
This package contains TDE's frontend for ssh.

%files -n trinity-kdessh
%defattr(-,root,root,-)
%{tde_bindir}/kdessh

##########

%package -n trinity-kdf
Summary:	disk space utility for Trinity
Group:		Applications/Utilities

%description -n trinity-kdf
KDiskFree displays the available file devices (hard drive partitions, floppy
and CD drives, etc.) along with information on their capacity, free space, type
and mount point. It also allows you to mount and unmount drives and view them
in a file manager.

%files -n trinity-kdf
%defattr(-,root,root,-)
%{tde_bindir}/kdf
%{tde_bindir}/kwikdisk
%{tde_tdelibdir}/kcm_kdf.la
%{tde_tdelibdir}/kcm_kdf.so
%{tde_tdeappdir}/kcmdf.desktop
%{tde_tdeappdir}/kdf.desktop
%{tde_tdeappdir}/kwikdisk.desktop
%{tde_datadir}/apps/kdf/
%{tde_datadir}/icons/crystalsvg/*/apps/kcmdf.png
%{tde_datadir}/icons/hicolor/*/apps/kdf.png
%{tde_datadir}/icons/hicolor/*/apps/kwikdisk.png
%{tde_tdedocdir}/HTML/en/kdf/
%{tde_tdedocdir}/HTML/en/kinfocenter/blockdevices/

%post -n trinity-kdf
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kdf
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kedit
Summary:	basic text editor for Trinity
Group:		Applications/Utilities

%description -n trinity-kedit
A simple text editor for TDE.

It can be used with Konqueror for text and configuration file browsing.
KEdit also serves well for creating small plain text documents. KEdit's
functionality will intentionally remain rather limited to ensure a
reasonably fast start.

%files -n trinity-kedit
%defattr(-,root,root,-)
%{tde_bindir}/kedit
%{tde_tdelibdir}/kedit.la
%{tde_tdelibdir}/kedit.so
%{tde_libdir}/libkdeinit_kedit.so
%{tde_tdeappdir}/KEdit.desktop
%{tde_datadir}/apps/kedit/keditui.rc
%{tde_datadir}/config.kcfg/kedit.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kedit.png
%{tde_tdedocdir}/HTML/en/kedit/

%post -n trinity-kedit
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kedit
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kfloppy
Summary:	floppy formatter for Trinity
Group:		Applications/Utilities
Requires:	dosfstools

%description -n trinity-kfloppy
Kfloppy is a utility that provides a straightforward graphical means
to format 3.5" and 5.25" floppy disks.

%files -n trinity-kfloppy
%defattr(-,root,root,-)
%{tde_bindir}/kfloppy
%{tde_tdeappdir}/KFloppy.desktop
%{tde_datadir}/apps/konqueror/servicemenus/floppy_format.desktop
%{tde_datadir}/icons/hicolor/*/apps/kfloppy.png
%{tde_tdedocdir}/HTML/en/kfloppy/

%post -n trinity-kfloppy
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kfloppy
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kgpg
Summary:	GnuPG frontend for Trinity
Group:		Applications/Utilities
Requires:	trinity-konsole
Requires:	gnupg

%description -n trinity-kgpg
Kgpg is a frontend for GNU Privacy Guard (GnuPG). It provides file
encryption, file decryption and key management.

Features:
* an editor mode for easily and quickly encrypting or decrypting a file
  or message which is typed, copied, pasted or dragged into the editor,
  or which is double-clicked in the file manager
* Konqueror integration for encrypting or decrypting files
* a panel applet for encrypting / decrypting files or the clipboard
  contents, etc.
* key management functions (generation, import, export, deletion and
  signing)
* decrypting clipboard contents, including integration with Klipper

%files -n trinity-kgpg
%defattr(-,root,root,-)
%{tde_bindir}/kgpg
%{tde_tdeappdir}/kgpg.desktop
%{tde_datadir}/apps/kgpg/
%{tde_datadir}/apps/konqueror/servicemenus/encryptfile.desktop
%{tde_datadir}/apps/konqueror/servicemenus/encryptfolder.desktop
%{tde_datadir}/autostart/kgpg.desktop
%{tde_datadir}/config.kcfg/kgpg.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kgpg.png
%{tde_tdedocdir}/HTML/en/kgpg/

%post -n trinity-kgpg
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kgpg
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-khexedit
Summary:	Trinity hex editor
Group:		Applications/Utilities

%description -n trinity-khexedit
KHexEdit is an editor for the raw data of binary files.  It includes
find/replace functions, bookmarks, many configuration options, drag and drop
support and other powerful features.

%files -n trinity-khexedit
%defattr(-,root,root,-)
%{tde_bindir}/khexedit
%{tde_tdelibdir}/libkbyteseditwidget.la
%{tde_tdelibdir}/libkbyteseditwidget.so
%{tde_tdelibdir}/libkhexedit2part.la
%{tde_tdelibdir}/libkhexedit2part.so
%{tde_libdir}/libkhexeditcommon.so.*
%{tde_tdeappdir}/khexedit.desktop
%{tde_datadir}/apps/khexedit/
%{tde_datadir}/apps/khexedit2part/khexedit2partui.rc
%{tde_datadir}/icons/hicolor/*/apps/khexedit.png
%{tde_datadir}/services/kbyteseditwidget.desktop
%{tde_datadir}/services/khexedit2part.desktop
%{tde_tdedocdir}/HTML/en/khexedit/

%post -n trinity-khexedit
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-khexedit
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kjots
Summary:	note taking utility for Trinity
Group:		Applications/Utilities

%description -n trinity-kjots
Kjots is a small note taker program. Name and idea are taken from the jots
program included in the tkgoodstuff package.

%files -n trinity-kjots
%defattr(-,root,root,-)
%{tde_bindir}/kjots
%{tde_tdeappdir}/Kjots.desktop
%{tde_datadir}/apps/kjots/
%{tde_datadir}/config.kcfg/kjots.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kjots.png
%{tde_tdedocdir}/HTML/en/kjots/

%post -n trinity-kjots
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kjots
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%if 0%{?build_klaptopdaemon}

%package -n trinity-klaptopdaemon
Summary:	battery monitoring and management for laptops using Trinity
Group:		Applications/Utilities
Requires:	pm-utils

%if 0%{?with_consolehelper}
# package 'usermode' provides '/usr/bin/consolehelper-gtk'
%if 0%{?rhel} || 0%{?fedora}
Requires:	usermode-gtk
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
Requires:	usermode
%endif
%endif

%description -n trinity-klaptopdaemon
This package contains utilities to monitor batteries and configure
power management, for laptops, from within TDE.

%files -n trinity-klaptopdaemon
%defattr(-,root,root,-)
%{tde_bindir}/klaptop_acpi_helper
%{tde_bindir}/klaptop_check
%{tde_tdelibdir}/kcm_laptop.la
%{tde_tdelibdir}/kcm_laptop.so
%{tde_tdelibdir}/kded_klaptopdaemon.la
%{tde_tdelibdir}/kded_klaptopdaemon.so
%{tde_libdir}/libkcmlaptop.so.*
%{tde_tdeappdir}/laptop.desktop
%{tde_tdeappdir}/pcmcia.desktop
%{tde_datadir}/apps/klaptopdaemon/
%{tde_datadir}/icons/crystalsvg/*/apps/laptop_battery.png
%{tde_datadir}/icons/crystalsvg/*/apps/laptop_pcmcia.png
%{tde_datadir}/icons/crystalsvg/scalable/apps/laptop_battery.svgz
%{tde_datadir}/services/kded/klaptopdaemon.desktop
%{tde_tdedocdir}/HTML/en/kcontrol/kcmlowbatcrit/
%{tde_tdedocdir}/HTML/en/kcontrol/kcmlowbatwarn/
%{tde_tdedocdir}/HTML/en/kcontrol/laptop/
%{tde_tdedocdir}/HTML/en/kcontrol/powerctrl/

# ConsoleHelper support
%if 0%{?with_consolehelper}
%{_sysconfdir}/pam.d/klaptop_acpi_helper
%attr(644,root,root) %{_sysconfdir}/security/console.apps/klaptop_acpi_helper
%{tde_sbindir}/klaptop_acpi_helper
%{_sbindir}/klaptop_acpi_helper
%endif

%config %{tde_datadir}/config/kcmlaptoprc

%post -n trinity-klaptopdaemon
/sbin/ldconfig
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-klaptopdaemon
/sbin/ldconfig
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%endif

##########

%package -n trinity-kmilo
Summary:	laptop special keys support for Trinity
Group:		Applications/Utilities

%description -n trinity-kmilo
KMilo lets you use the special keys on some keyboards and laptops.

Usually this includes volume keys and other features. Currently, KMilo
comes with plugins for Powerbooks, Thinkpads, Vaios and generic keyboards
with special keys.

%files -n trinity-kmilo
%defattr(-,root,root,-)
%{tde_tdelibdir}/kded_kmilod.la
%{tde_tdelibdir}/kded_kmilod.so
%{tde_tdelibdir}/kmilo_generic.la
%{tde_tdelibdir}/kmilo_generic.so
%{tde_libdir}/libkmilo.so.*
%{tde_datadir}/services/kded/kmilod.desktop
%{tde_datadir}/services/kmilo/kmilo_generic.desktop
%{tde_datadir}/servicetypes/kmilo/kmilopluginsvc.desktop

%post -n trinity-kmilo
/sbin/ldconfig

%postun -n trinity-kmilo
/sbin/ldconfig

##########

%package -n trinity-kmilo-legacy
Summary:	non-standard plugins for KMilo
Group:		Applications/Utilities
Requires:	trinity-kmilo = %{version}-%{release}

%description -n trinity-kmilo-legacy
KMilo lets you use the special keys on some keyboards and laptops.

Usually this includes volume keys and other features. Currently, KMilo
comes with plugins for Powerbooks, Thinkpads and Vaios.

The intention is that all laptops work with the generic kmilo
plugin, if you need this package please file a bug.

%files -n trinity-kmilo-legacy
%defattr(-,root,root,-)
%{tde_tdelibdir}/kcm_kvaio.la
%{tde_tdelibdir}/kcm_kvaio.so
%{tde_tdelibdir}/kcm_thinkpad.la
%{tde_tdelibdir}/kcm_thinkpad.so
%{tde_tdelibdir}/kmilo_asus.la
%{tde_tdelibdir}/kmilo_asus.so
%{tde_tdelibdir}/kmilo_delli8k.la
%{tde_tdelibdir}/kmilo_delli8k.so
%{tde_tdelibdir}/kmilo_kvaio.la
%{tde_tdelibdir}/kmilo_kvaio.so
%{tde_tdelibdir}/kmilo_thinkpad.la
%{tde_tdelibdir}/kmilo_thinkpad.so
%{tde_tdeappdir}/kvaio.desktop
%{tde_tdeappdir}/thinkpad.desktop
%{tde_datadir}/services/kmilo/kmilo_asus.desktop
%{tde_datadir}/services/kmilo/kmilo_delli8k.desktop
%{tde_datadir}/services/kmilo/kmilo_kvaio.desktop
%{tde_datadir}/services/kmilo/kmilo_thinkpad.desktop

##########

%package -n trinity-kregexpeditor
Summary:	graphical regular expression editor plugin for Trinity
Group:		Applications/Utilities

%description -n trinity-kregexpeditor
This package contains a graphical regular expression editor plugin for use
with TDE. It let you draw your regular expression in an unambiguous way.

%files -n trinity-kregexpeditor
%defattr(-,root,root,-)
%{tde_bindir}/kregexpeditor
%{tde_tdelibdir}/libkregexpeditorgui.la
%{tde_tdelibdir}/libkregexpeditorgui.so
%{tde_libdir}/libkregexpeditorcommon.so.*
%{tde_tdeappdir}/kregexpeditor.desktop
%{tde_datadir}/apps/kregexpeditor/
%{tde_datadir}/icons/hicolor/*/apps/kregexpeditor.png
%{tde_datadir}/services/kregexpeditorgui.desktop
%{tde_tdedocdir}/HTML/en/KRegExpEditor/

%post -n trinity-kregexpeditor
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kregexpeditor
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-ksim
Summary:	system information monitor for Trinity
Group:		Applications/Utilities

%description -n trinity-ksim
KSim is a system monitor app which has its own plugin system with support
for GKrellm skins. It allows users to follow uptime, memory usage, network
connections, power, etc.

%files -n trinity-ksim
%defattr(-,root,root,-)
%config %{tde_datadir}/config/ksim_panelextensionrc
%{tde_tdelibdir}/ksim_*.la
%{tde_tdelibdir}/ksim_*.so
%{tde_libdir}/libksimcore.so.*
%{tde_datadir}/apps/kicker/extensions/ksim.desktop
%{tde_datadir}/apps/ksim/
%{tde_tdedocdir}/HTML/en/ksim/
%{tde_datadir}/icons/crystalsvg/*/apps/ksim.png
%{tde_datadir}/icons/crystalsvg/*/devices/ksim_cpu.png

%post -n trinity-ksim
/sbin/ldconfig
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done

%postun -n trinity-ksim
/sbin/ldconfig
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done

##########

%package -n trinity-ktimer
Summary:	timer utility for Trinity
Group:		Applications/Utilities

%description -n trinity-ktimer
This is a timer application for TDE. It allows you to execute commands after
a certain amount of time. It supports looping commands as well as delayed
command execution.

%files -n trinity-ktimer
%defattr(-,root,root,-)
%{tde_bindir}/ktimer
%{tde_tdeappdir}/ktimer.desktop
%{tde_datadir}/icons/hicolor/*/apps/ktimer.png
%{tde_tdedocdir}/HTML/en/ktimer/

%post -n trinity-ktimer
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-ktimer
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kwalletmanager
Summary:	wallet manager for Trinity
Group:		Applications/Utilities

%description -n trinity-kwalletmanager
This program keeps various wallets for any kind of data that the user can
store encrypted with passwords and can also serve as a password manager that
keeps a master password to all wallets.

%files -n trinity-kwalletmanager
%defattr(-,root,root,-)
%{tde_bindir}/kwalletmanager
%{tde_tdelibdir}/kcm_kwallet.la
%{tde_tdelibdir}/kcm_kwallet.so
%{tde_tdeappdir}/kwalletconfig.desktop
%{tde_tdeappdir}/kwalletmanager.desktop
%{tde_tdeappdir}/kwalletmanager-kwalletd.desktop
%{tde_datadir}/apps/kwalletmanager/
%{tde_datadir}/icons/hicolor/*/apps/kwalletmanager.png
%{tde_datadir}/services/kwallet_config.desktop
%{tde_datadir}/services/kwalletmanager_show.desktop
%{tde_tdedocdir}/HTML/en/kwallet/

%post -n trinity-kwalletmanager
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kwalletmanager
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-superkaramba
Summary:	a program based on karamba improving the eyecandy of TDE
Group:		Applications/Utilities

%description -n trinity-superkaramba
SuperKaramba is a tool based on karamba that allows anyone to easily create
and run little interactive widgets on a TDE desktop. Widgets are defined in a
simple text file and can be augmented with Python code to make them
interactive.

Here are just some examples of the things that can be done:
* Display system information such as CPU Usage, MP3 playing, etc.
* Create cool custom toolbars that work any way imaginable.
* Create little games or virtual pets that live on your desktop.
* Display information from the internet, such as weather and headlines.

%files -n trinity-superkaramba
%defattr(-,root,root,-)
%{tde_bindir}/superkaramba
%{tde_datadir}/applnk/Utilities/superkaramba.desktop
%{tde_datadir}/apps/superkaramba/superkarambaui.rc
%{tde_datadir}/icons/crystalsvg/*/apps/superkaramba.png
%{tde_datadir}/icons/crystalsvg/*/mimetypes/superkaramba_theme.png
%{tde_datadir}/icons/crystalsvg/scalable/apps/superkaramba.svgz
%{tde_datadir}/icons/crystalsvg/scalable/mimetypes/superkaramba_theme.svgz
%{tde_datadir}/mimelnk/application/x-superkaramba.desktop
%{tde_tdedocdir}/HTML/en/superkaramba/

%post -n trinity-superkaramba
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done

%postun -n trinity-superkaramba
for f in crystalsvg ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done

##########

# afaik, nobody BR's it, and it pulls kdeutils into multilib -- Rex
%package devel
Summary:	Development files for %{name} 
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	trinity-tdelibs-devel

Obsoletes:	trinity-kdeutils-devel < %{version}-%{release}
Provides:	trinity-kdeutils-devel = %{version}-%{release}
Obsoletes:	tdeutils-devel < %{version}-%{release}
Provides:	tdeutils-devel = %{version}-%{release}

%description devel
Development files for %{name}.

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/*
%if 0%{?build_klaptopdaemon}
%{tde_libdir}/libkcmlaptop.la
%{tde_libdir}/libkcmlaptop.so
%endif
%{tde_libdir}/libkdeinit_ark.la
%{tde_libdir}/libkdeinit_irkick.la
%{tde_libdir}/libkdeinit_kcalc.la
%{tde_libdir}/libkdeinit_kedit.la
%{tde_libdir}/libkmilo.la
%{tde_libdir}/libkmilo.so
%{tde_libdir}/libkregexpeditorcommon.la
%{tde_libdir}/libkregexpeditorcommon.so
%{tde_libdir}/libksimcore.la
%{tde_libdir}/libksimcore.so
%{tde_libdir}/libkhexeditcommon.la
%{tde_libdir}/libkhexeditcommon.so
%{tde_datadir}/cmake/libksimcore.cmake

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}
%if 0%{?rhel} == 4
%patch1 -p1 -b .rhel4
%endif


%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

# Do not build against any "/usr" installed KDE
export KDEDIR="%{tde_prefix}"

# Shitty hack for RHEL4 ...
if [ -d "/usr/X11R6" ]; then
  export CMAKE_INCLUDE_PATH="${CMAKE_INCLUDE_PATH}:/usr/X11R6/include:/usr/X11R6/%{_lib}"
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

if ! rpm -E %%cmake|grep -q "cd build"; then
  %__mkdir_p build
  cd build
fi

%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  \
  -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
  -DBIN_INSTALL_DIR="%{tde_bindir}" \
  -DDOC_INSTALL_DIR="%{tde_docdir}" \
  -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}" \
  -DLIB_INSTALL_DIR="%{tde_libdir}" \
  -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
  -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
  \
  -DWITH_DPMS=ON \
  %{?with_xscreensaver:-DWITH_XSCREENSAVER=ON} \
  -DWITH_ASUS=ON \
  -DWITH_POWERBOOK=OFF \
  -DWITH_POWERBOOK2=OFF \
  -DWITH_VAIO=ON \
  -DWITH_THINKPAD=ON \
  -DWITH_I8K=ON \
  -DWITH_SNMP=ON \
  -DWITH_SENSORS=ON \
  -DWITH_XMMS=ON \
  -DWITH_KNEWSTUFF=ON \
  -DBUILD_ALL=ON \
  %{?!build_klaptopdaemon:-DBUILD_KLAPTOPDAEMON=OFF} \
  ..
   
%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

%if 0%{?build_klaptopdaemon}
### Use consolehelper for 'klaptop_acpi_helper'
%if 0%{?with_consolehelper}
# Install configuration files
%__install -p -D -m 644 "%{SOURCE1}" "%{buildroot}%{_sysconfdir}/pam.d/klaptop_acpi_helper"
%__install -p -D -m 644 "%{SOURCE2}" "%{buildroot}%{_sysconfdir}/security/console.apps/klaptop_acpi_helper"
# Moves the actual binary from 'bin' to 'sbin'
%__mkdir_p "%{buildroot}%{tde_sbindir}" "%{buildroot}%{_sbindir}"
%__mv "%{buildroot}%{tde_bindir}/klaptop_acpi_helper" "%{buildroot}%{tde_sbindir}"
# Links to consolehelper
%__ln_s "%{_bindir}/consolehelper" "%{buildroot}%{tde_bindir}/klaptop_acpi_helper"
# Put another symlink under '/usr', otherwise consolehelper does not work
%if "%{tde_prefix}" != "/usr"
%__ln_s "%{tde_sbindir}/klaptop_acpi_helper" "%{?buildroot}%{_sbindir}/klaptop_acpi_helper"
%endif
%endif

# klaptop settings file
%__install -p -D -m 644 "%{SOURCE3}" "%{buildroot}%{tde_datadir}/config/kcmlaptoprc"

%else

# Klaptop's documentation is installed even if we did not build the program ...
%__rm -fr %{?buildroot}%{tde_tdedocdir}/HTML/en/kcontrol/kcmlowbatcrit/
%__rm -fr %{?buildroot}%{tde_tdedocdir}/HTML/en/kcontrol/kcmlowbatwarn/
%__rm -fr %{?buildroot}%{tde_tdedocdir}/HTML/en/kcontrol/laptop/
%__rm -fr %{?buildroot}%{tde_tdedocdir}/HTML/en/kcontrol/powerctrl/

%endif


%clean
%__rm -rf "%{?buildroot}"


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-3
- Build for Fedora 19

* Sun Jul 28 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-2
- Rebuild with NDEBUG option

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.5.13.2-1
- Initial release for TDE 3.5.13.2
