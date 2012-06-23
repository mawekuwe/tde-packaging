# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
%define tde_appdir %{_datadir}/applications/kde
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		tdeutils
Version:	3.5.13
Release:	6%{?dist}%{?_variant}
License:	GPL
Summary:	TDE Utilities
Group:		Applications/System

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kdeutils-%{version}.tar.gz
Source1:	klaptop_acpi_helper.pam
Source2:	klaptop_acpi_helper.console
Source3:	kcmlaptoprc

Obsoletes:	trinity-kdeutils < %{version}-%{release}
Provides:	trinity-kdeutils = %{version}-%{release}
Obsoletes:	trinity-kdeutils-extras < %{version}-%{release}
Provides:	trinity-kdeutils-extras = %{version}-%{release}

# RedHat / Fedora legacy patches
Patch1:		kdf-3.0.2-label.patch

# TDE 3.5.13 RHEL/Fedora patches
## [kdeutils/klaptodaemon] removes dpkg commands
Patch2:		kdeutils-3.5.13-klaptopdaemon_dpkg_command.patch
## [tdeutils] Allow ark embedding [Bug #670] [Commit #2a1d4a67]
Patch3:		kdeutils-3.5.13-fix_ark_embedding.patch
## [tdeutils] Remove "More Applications" from TDE menu. Add Utility category to KEdit. [Bug #653] [Commit #803f4752]
Patch4:		kdeutils-3.5.13-remove_more_applications.patch
## [tdeutils] Reorganize KControl menu tree. [Commit #7780bb7b]
##   * Move former KInfoCenter items -> Hardware/Information.
##   * Move Laptop Battery -> Hardware.
Patch5:		kdeutils-3.5.13-reorganize_kcontrol_menu_tree.patch
## [tdeutils] Further organize TDE Menu. [Commit #b970fc42]
Patch6:		kdeutils-3.5.13-further_organise_menu.patch
## [tdeutils] [Ark] Repairs and extensions [Bug #1030] [Commit #1c84948d]
##  Added support for Arj
##  Added support for check archives
##  Added support for password processing
##  Fix show broken filenames into real UTF-8
Patch7:		kdeutils-3.5.13-ark_repairs_and_extensions.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	tdelibs-devel
BuildRequires:	autoconf automake libtool m4
BuildRequires:	gettext
BuildRequires:	net-snmp-devel
BuildRequires:	python-devel
BuildRequires:	gmp-devel

%if 0%{?fedora} > 4 || 0%{?rhel} > 4
BuildRequires:	libXScrnSaver-devel libXtst-devel
%endif

%if 0%{?fedora}
BuildRequires:	xmms-devel
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
Requires: trinity-klaptopdaemon = %{version}-%{release}
Requires: trinity-kmilo = %{version}-%{release}
Requires: trinity-kmilo-legacy = %{version}-%{release}
Requires: trinity-kregexpeditor = %{version}-%{release}
Requires: trinity-ksim = %{version}-%{release}
Requires: trinity-ktimer = %{version}-%{release}
Requires: trinity-kwalletmanager = %{version}-%{release}
Requires: trinity-superkaramba = %{version}-%{release}

Requires(post):		/sbin/ldconfig
Requires(postun):	/sbin/ldconfig

%files


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
  * klaptopdaemon (battery monitoring and management for laptops);
  * kmilo
  * kregexpeditor (regular expression editor)
  * ksim (system information monitor);
  * ktimer (task scheduler)
  * kwikdisk (removable media utility)

##########

%package -n trinity-ark
Summary:	graphical archiving tool for Trinity
Group:		Applications/Utilities
#Requires:	ncompress
Requires:	unzip, zip
#Requires:	zoo
Requires:	bzip2
#Requires:	p7zip
Requires:	xz
Requires:	lzma
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
%{_bindir}/ark
%{tde_libdir}/ark.la
%{tde_libdir}/ark.so
%{tde_libdir}/libarkpart.la
%{tde_libdir}/libarkpart.so
%{_libdir}/lib[kt]deinit_ark.so
%{tde_appdir}/ark.desktop
%{_datadir}/apps/ark/
%{_datadir}/config.kcfg/ark.kcfg
%{_datadir}/icons/hicolor/*/apps/ark.png
%{_datadir}/icons/hicolor/scalable/apps/ark.svgz
%{_datadir}/services/ark_part.desktop
%{tde_docdir}/HTML/en/ark/

%post -n trinity-ark
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-ark
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

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
%{_bindir}/kcalc
%{tde_libdir}/kcalc.la
%{tde_libdir}/kcalc.so
%{_libdir}/lib[kt]deinit_kcalc.so
%{tde_appdir}/kcalc.desktop
%{_datadir}/apps/kcalc/
%{_datadir}/apps/kconf_update/kcalcrc.upd
%{_datadir}/config.kcfg/kcalc.kcfg
%{_datadir}/icons/hicolor/*/apps/kcalc.png
%{_datadir}/icons/hicolor/scalable/apps/kcalc.svgz
%{tde_docdir}/HTML/en/kcalc/

%post -n trinity-kcalc
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kcalc
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kcharselect
Summary:	character selector for Trinity
Group:		Applications/Utilities

%description -n trinity-kcharselect
A character set selector for TDE.

%files -n trinity-kcharselect
%defattr(-,root,root,-)
%{_bindir}/kcharselect
%{tde_libdir}/kcharselect_panelapplet.la
%{tde_libdir}/kcharselect_panelapplet.so
%{tde_appdir}/KCharSelect.desktop
%{_datadir}/apps/kcharselect/
%{_datadir}/apps/kconf_update/kcharselect.upd
%{_datadir}/apps/kicker/applets/kcharselectapplet.desktop
%{_datadir}/icons/hicolor/*/apps/kcharselect.png
%{tde_docdir}/HTML/en/kcharselect/

%post -n trinity-kcharselect
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kcharselect
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kdelirc
Summary:	infrared control for Trinity
Group:		Applications/Utilities

%description -n trinity-kdelirc
This is a frontend for the LIRC suite to use infrared devices with TDE.

%files -n trinity-kdelirc
%defattr(-,root,root,-)
%{_bindir}/irkick
%{tde_libdir}/irkick.la
%{tde_libdir}/irkick.so
%{tde_libdir}/kcm_kcmlirc.la
%{tde_libdir}/kcm_kcmlirc.so
%{_libdir}/lib[kt]deinit_irkick.so
%{tde_appdir}/irkick.desktop
%{tde_appdir}/kcmlirc.desktop
%{_datadir}/apps/irkick/
%{_datadir}/apps/profiles/klauncher.profile.xml
%{_datadir}/apps/profiles/konqueror.profile.xml
%{_datadir}/apps/profiles/noatun.profile.xml
%{_datadir}/apps/profiles/profile.dtd
%{_datadir}/apps/remotes/RM-0010.remote.xml
%{_datadir}/apps/remotes/cimr100.remote.xml
%{_datadir}/apps/remotes/hauppauge.remote.xml
%{_datadir}/apps/remotes/remote.dtd
%{_datadir}/apps/remotes/sherwood.remote.xml
%{_datadir}/apps/remotes/sonytv.remote.xml
%{_datadir}/autostart/irkick.desktop
%{_datadir}/icons/hicolor/*/apps/irkick.png
%{_datadir}/icons/locolor/*/apps/irkick.png
%{tde_docdir}/HTML/en/irkick/
%{tde_docdir}/HTML/en/kcmlirc/

%post -n trinity-kdelirc
/sbin/ldconfig
for f in hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kdelirc
/sbin/ldconfig
for f in hicolor locolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kdessh
Summary:	ssh frontend for Trinity
Group:		Applications/Utilities
Requires:	openssh-clients

%description -n trinity-kdessh
This package contains TDE's frontend for ssh.

%files -n trinity-kdessh
%defattr(-,root,root,-)
%{_bindir}/kdessh

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
%{_bindir}/kdf
%{_bindir}/kwikdisk
%{tde_libdir}/kcm_kdf.la
%{tde_libdir}/kcm_kdf.so
%{tde_appdir}/kcmdf.desktop
%{tde_appdir}/kdf.desktop
%{tde_appdir}/kwikdisk.desktop
%{_datadir}/apps/kdf/
%{_datadir}/icons/crystalsvg/*/apps/kcmdf.png
%{_datadir}/icons/hicolor/*/apps/kdf.png
%{_datadir}/icons/hicolor/*/apps/kwikdisk.png
%{tde_docdir}/HTML/en/kdf/
%{tde_docdir}/HTML/en/kinfocenter/blockdevices/

%post -n trinity-kdf
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kdf
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

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
%{_bindir}/kedit
%{tde_libdir}/kedit.la
%{tde_libdir}/kedit.so
%{_libdir}/lib[kt]deinit_kedit.so
%{tde_appdir}/KEdit.desktop
%{_datadir}/apps/kedit/keditui.rc
%{_datadir}/config.kcfg/kedit.kcfg
%{_datadir}/icons/hicolor/*/apps/kedit.png
%{tde_docdir}/HTML/en/kedit/

%post -n trinity-kedit
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kedit
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

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
%{_bindir}/kfloppy
%{tde_appdir}/KFloppy.desktop
%{_datadir}/apps/konqueror/servicemenus/floppy_format.desktop
%{_datadir}/icons/hicolor/*/apps/kfloppy.png
%{tde_docdir}/HTML/en/kfloppy/

%post -n trinity-kfloppy
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kfloppy
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

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
%{_bindir}/kgpg
%{tde_appdir}/kgpg.desktop
%{_datadir}/apps/kgpg/
%{_datadir}/apps/konqueror/servicemenus/encryptfile.desktop
%{_datadir}/apps/konqueror/servicemenus/encryptfolder.desktop
%{_datadir}/autostart/kgpg.desktop
%{_datadir}/config.kcfg/kgpg.kcfg
%{_datadir}/icons/hicolor/*/apps/kgpg.png
%{tde_docdir}/HTML/en/kgpg/

%post -n trinity-kgpg
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kgpg
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

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
%{_bindir}/khexedit
%{tde_libdir}/libkbyteseditwidget.la
%{tde_libdir}/libkbyteseditwidget.so
%{tde_libdir}/libkhexedit2part.la
%{tde_libdir}/libkhexedit2part.so
%{_libdir}/libkhexeditcommon.so.*
%{tde_appdir}/khexedit.desktop
%{_datadir}/apps/khexedit/
%{_datadir}/apps/khexedit2part/khexedit2partui.rc
%{_datadir}/icons/hicolor/*/apps/khexedit.png
%{_datadir}/services/kbyteseditwidget.desktop
%{_datadir}/services/khexedit2part.desktop
%{tde_docdir}/HTML/en/khexedit/

%post -n trinity-khexedit
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-khexedit
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kjots
Summary:	note taking utility for Trinity
Group:		Applications/Utilities

%description -n trinity-kjots
Kjots is a small note taker program. Name and idea are taken from the jots
program included in the tkgoodstuff package.

%files -n trinity-kjots
%defattr(-,root,root,-)
%{_bindir}/kjots
%{tde_appdir}/Kjots.desktop
%{_datadir}/apps/kjots/
%{_datadir}/config.kcfg/kjots.kcfg
%{_datadir}/icons/hicolor/*/apps/kjots.png
%{tde_docdir}/HTML/en/kjots/

%post -n trinity-kjots
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kjots
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-klaptopdaemon
Summary:	battery monitoring and management for laptops using Trinity
Group:		Applications/Utilities
Requires:	pm-utils
Requires:	usermode

%description -n trinity-klaptopdaemon
This package contains utilities to monitor batteries and configure
power management, for laptops, from within TDE.

%files -n trinity-klaptopdaemon
%defattr(-,root,root,-)
%{_bindir}/klaptop_acpi_helper
%{_bindir}/klaptop_check
%{tde_libdir}/kcm_laptop.la
%{tde_libdir}/kcm_laptop.so
%{tde_libdir}/kded_klaptopdaemon.la
%{tde_libdir}/kded_klaptopdaemon.so
%{_libdir}/libkcmlaptop.so.*
%{tde_appdir}/laptop.desktop
%{tde_appdir}/pcmcia.desktop
%{_datadir}/apps/klaptopdaemon/
%{_datadir}/icons/crystalsvg/*/apps/laptop_battery.png
%{_datadir}/icons/crystalsvg/*/apps/laptop_pcmcia.png
%{_datadir}/icons/crystalsvg/scalable/apps/laptop_battery.svgz
%{_datadir}/services/kded/klaptopdaemon.desktop
%{tde_docdir}/HTML/en/kcontrol/kcmlowbatcrit/
%{tde_docdir}/HTML/en/kcontrol/kcmlowbatwarn/
%{tde_docdir}/HTML/en/kcontrol/laptop/
%{tde_docdir}/HTML/en/kcontrol/powerctrl/

# RHEL/Fedora specific
%{_sysconfdir}/pam.d/klaptop_acpi_helper
%attr(644,root,root) %{_sysconfdir}/security/console.apps/klaptop_acpi_helper
%{_sbindir}/klaptop_acpi_helper
%config %{_datadir}/config/kcmlaptoprc

%post -n trinity-klaptopdaemon
/sbin/ldconfig
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-klaptopdaemon
/sbin/ldconfig
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

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
%{tde_libdir}/kded_kmilod.la
%{tde_libdir}/kded_kmilod.so
%{tde_libdir}/kmilo_generic.la
%{tde_libdir}/kmilo_generic.so
%{_libdir}/libkmilo.so.*
%{_datadir}/services/kded/kmilod.desktop
%{_datadir}/services/kmilo/kmilo_generic.desktop
%{_datadir}/servicetypes/kmilo/kmilopluginsvc.desktop

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
%{tde_libdir}/kcm_kvaio.la
%{tde_libdir}/kcm_kvaio.so
%{tde_libdir}/kcm_thinkpad.la
%{tde_libdir}/kcm_thinkpad.so
%{tde_libdir}/kmilo_asus.la
%{tde_libdir}/kmilo_asus.so
%{tde_libdir}/kmilo_delli8k.la
%{tde_libdir}/kmilo_delli8k.so
%{tde_libdir}/kmilo_kvaio.la
%{tde_libdir}/kmilo_kvaio.so
%{tde_libdir}/kmilo_thinkpad.la
%{tde_libdir}/kmilo_thinkpad.so
%{tde_appdir}/kvaio.desktop
%{tde_appdir}/thinkpad.desktop
%{_datadir}/services/kmilo/kmilo_asus.desktop
%{_datadir}/services/kmilo/kmilo_delli8k.desktop
%{_datadir}/services/kmilo/kmilo_kvaio.desktop
%{_datadir}/services/kmilo/kmilo_thinkpad.desktop

##########

%package -n trinity-kregexpeditor
Summary:	graphical regular expression editor plugin for Trinity
Group:		Applications/Utilities

%description -n trinity-kregexpeditor
This package contains a graphical regular expression editor plugin for use
with TDE. It let you draw your regular expression in an unambiguous way.

%files -n trinity-kregexpeditor
%defattr(-,root,root,-)
%{_bindir}/kregexpeditor
%{tde_libdir}/libkregexpeditorgui.la
%{tde_libdir}/libkregexpeditorgui.so
%{_libdir}/libkregexpeditorcommon.so.*
%{tde_appdir}/kregexpeditor.desktop
%{_datadir}/apps/kregexpeditor/
%{_datadir}/icons/hicolor/*/apps/kregexpeditor.png
%{_datadir}/services/kregexpeditorgui.desktop
%{tde_docdir}/HTML/en/KRegExpEditor/

%post -n trinity-kregexpeditor
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kregexpeditor
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

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
%config %{_datadir}/config/ksim_panelextensionrc
%{tde_libdir}/ksim_*.la
%{tde_libdir}/ksim_*.so
%{_libdir}/libksimcore.so.*
%{_datadir}/apps/kicker/extensions/ksim.desktop
%{_datadir}/apps/ksim/
%{tde_docdir}/HTML/en/ksim/
%{_datadir}/icons/crystalsvg/*/apps/ksim.png
%{_datadir}/icons/crystalsvg/*/devices/ksim_cpu.png

%post -n trinity-ksim
/sbin/ldconfig
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done

%postun -n trinity-ksim
/sbin/ldconfig
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null  ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
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
%{_bindir}/ktimer
%{tde_appdir}/ktimer.desktop
%{_datadir}/icons/hicolor/*/apps/ktimer.png
%{tde_docdir}/HTML/en/ktimer/

%post -n trinity-ktimer
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-ktimer
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

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
%{_bindir}/kwalletmanager
%{tde_libdir}/kcm_kwallet.la
%{tde_libdir}/kcm_kwallet.so
%{tde_appdir}/kwalletconfig.desktop
%{tde_appdir}/kwalletmanager.desktop
%{tde_appdir}/kwalletmanager-kwalletd.desktop
%{_datadir}/apps/kwalletmanager/
%{_datadir}/icons/hicolor/*/apps/kwalletmanager.png
%{_datadir}/services/kwallet_config.desktop
%{_datadir}/services/kwalletmanager_show.desktop
%{tde_docdir}/HTML/en/kwallet/

%post -n trinity-kwalletmanager
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kwalletmanager
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

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
%{_bindir}/superkaramba
%{_datadir}/applnk/Utilities/superkaramba.desktop
%{_datadir}/apps/superkaramba/superkarambaui.rc
%{_datadir}/icons/crystalsvg/*/apps/superkaramba.png
%{_datadir}/icons/crystalsvg/*/mimetypes/superkaramba_theme.png
%{_datadir}/icons/crystalsvg/scalable/apps/superkaramba.svgz
%{_datadir}/icons/crystalsvg/scalable/mimetypes/superkaramba_theme.svgz
%{_datadir}/mimelnk/application/x-superkaramba.desktop
%{tde_docdir}/HTML/en/superkaramba/

%post -n trinity-superkaramba
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done

%postun -n trinity-superkaramba
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/$f 2> /dev/null ||:
done

##########

# afaik, nobody BR's it, and it pulls kdeutils into multilib -- Rex
%package devel
Summary:	Development files for %{name} 
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	tdelibs-devel

Obsoletes:	trinity-kdeutils-devel < %{version}-%{release}
Provides:	trinity-kdeutils-devel = %{version}-%{release}

%description devel
Development files for %{name}.

%files devel
%defattr(-,root,root,-)
%{tde_includedir}/*
%{_libdir}/libkcmlaptop.la
%{_libdir}/libkcmlaptop.so
%{_libdir}/lib[kt]deinit_ark.la
%{_libdir}/lib[kt]deinit_irkick.la
%{_libdir}/lib[kt]deinit_kcalc.la
%{_libdir}/lib[kt]deinit_kedit.la
%{_libdir}/libkmilo.la
%{_libdir}/libkmilo.so
%{_libdir}/libkregexpeditorcommon.la
%{_libdir}/libkregexpeditorcommon.so
%{_libdir}/libksimcore.la
%{_libdir}/libksimcore.so
%{_libdir}/libkhexeditcommon.la
%{_libdir}/libkhexeditcommon.so

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

##########

%prep
%setup -q -n kdeutils

%patch1 -p1 -b .label
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"

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
%__make install DESTDIR=%{?buildroot}

# Show only in KDE (really? -- Rex)
for i in kcalc kregexpeditor Kjots ktimer kdf kcmdf ksim KFloppy KEdit \
  KCharSelect ark kwalletmanager kwalletconfig \
 irkick kcmlirc laptop pcmcia kvaio thinkpad kwikdisk; do
 if [ -f %{buildroot}%{_datadir}/applications/kde/$i.desktop ] ; then
   echo "OnlyShowIn=KDE;" >> %{buildroot}%{_datadir}/applications/kde/$i.desktop
 fi
done

## File lists
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
%__install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/klaptop_acpi_helper
%__install -p -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/security/console.apps/klaptop_acpi_helper

pushd %{buildroot}%{_bindir}
  %__mkdir_p %{buildroot}%{_sbindir}
  %__mv klaptop_acpi_helper ../sbin
  %__ln_s /usr/bin/consolehelper klaptop_acpi_helper
popd

# klaptop setting
%__install -p -D -m 644 %{SOURCE3} %{buildroot}%{_datadir}/config/kcmlaptoprc


%clean
%__rm -rf %{?buildroot}



%changelog
* Fri Jun 22 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-6
- Split in several packages
- Allow ark embedding [Bug #670] [Commit #2a1d4a67]
- Remove "More Applications" from TDE menu. Add Utility category to KEdit. [Bug #653] [Commit #803f4752]
- [tdeutils] Reorganize KControl menu tree. [Commit #7780bb7b]
- Further organize TDE Menu. [Commit #b970fc42]
- [Ark] Repairs and extensions [Bug #1030] [Commit #1c84948d]

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-5
- Fix HTML directory location

* Thu Nov 17 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Fix symbolic link to 'consolehelper'

* Fri Nov 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Removes 'dpkg' commands inside klaptopdaemon

* Fri Nov 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Updates BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Mon Sep 05 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT

