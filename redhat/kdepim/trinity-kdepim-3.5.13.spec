# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
%define tde_appdir %{_datadir}/applications/kde
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity

# KDEPIM specific features
%if 0%{?fedora}
%define with_gnokii 1
%else
%define with_gnokii 0
%endif

# TDEPIM optional features
#BuildRequires: opensync-devel
%define		with_kitchensync 0


Name:		tdepim
Version:	3.5.13
Release:	6%{?dist}%{?_variant}
License:	GPL
Group:		Applications/Productivity

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
Summary:	Personal Information Management apps from the official Trinity release

Prefix:		%{_prefix}

Source0:	kdepim-%{version}.tar.gz

# [kdepim] Fix compilation with GCC 4.7 [Bug #958]
Patch1:		kdepim-3.5.13-fix_gcc47_compilation.patch
# [tdepim] Reverse patch from GIT hash 33e649c9. [Bug #406] [Commit #2d5f15c8]
Patch2:		kdepim-3.5.13-fix_check_mail.patch
# [tdepim] Fix kmail composer crash [Bug #953]
Patch3:		kdepim-3.5.13-fix_composer_crash.patch
# [tdepim] Fix KMail counting of unread messages in the system tray icon [Commit #40c435e5]
Patch4:		kdepim-3.5.13-fix_systray_count.patch
# [tdepim] Fix knotes not appearing on the desktop when a session is restored. [Bug #987] [Commit #533f494f]
Patch5:		kdepim-3.5.13-fix_knotes_after_restored.patch
# [tdepim] Fix knotes to not close notes during saving session. [Bug #987] [Commit #c48253af]
Patch6:		kdepim-3.5.13-fix_knotes_on_suspend.patch
# [tdepim] Fix linear alphabet string errors [Bug 635] [Commit #80bc593e]
Patch7:		kdepim-3.5.13-fix_linear_alphabet.patch
# [tdepim] Fix infinite loop on IMAP4 authentication failure [Bug #1007]
Patch8:		kdepim-3.5.13-fix_kio_imap4_infinite_loop.patch
# [tdepim] Fix infinite loop on kmime_utils addquotes
Patch9:		kdepim-3.5.13-fix_kio_imap4_addquotes.patch
Patch10:	kdepim-3.5.13-fix_segv.patch
# [tdepim] Update kalarmd icon reference, which does not exist, to kalarm. [Commit #228ad1c6]
Patch11:	kdepim-3.5.13-fix_kalarm_icon_reference.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	gpgme-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	flex
BuildRequires:	libical-devel
BuildRequires:	boost-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	libXcomposite-devel
BuildRequires:	pcre-devel
BuildRequires:	glib2-devel
BuildRequires:	gcc-c++ make

BuildRequires:	libcaldav-devel
BuildRequires:	libcarddav-devel

%if 0%{?with_gnokii}
BuildRequires:	gnokii-devel
%endif

%if 0%{?fedora} >= 15
BuildRequires:	flex-static
%endif
%if 0%{?rhel} > 0 && 0%{?rhel} <= 5
BuildRequires:	trinity-libcurl-devel
%else
BuildRequires:	curl-devel
%endif

Requires:	libtdepim = %{version}-%{release}
Requires:	tdepim-kfile-plugins = %{version}-%{release}
Requires:	tdepim-kio-plugins = %{version}-%{release}
Requires:	tdepim-kresources = %{version}-%{release}
Requires:	tdepim-wizards = %{version}-%{release}
Requires:	trinity-akregator = %{version}-%{release}
Requires:	trinity-kaddressbook = %{version}-%{release}
Requires:	trinity-kalarm = %{version}-%{release}
Requires:	trinity-kandy = %{version}-%{release}
Requires:	trinity-karm = %{version}-%{release}
Requires:	trinity-kleopatra = %{version}-%{release}
Requires:	trinity-kmail = %{version}-%{release}
Requires:	trinity-kmailcvt = %{version}-%{release}
Requires:	trinity-kmobile = %{version}-%{release}
Requires:	trinity-knode = %{version}-%{release}
Requires:	trinity-knotes = %{version}-%{release}
Requires:	trinity-kode = %{version}-%{release}
Requires:	trinity-konsolekalendar = %{version}-%{release}
Requires:	trinity-kontact = %{version}-%{release}
Requires:	trinity-korganizer = %{version}-%{release}
Requires:	trinity-korn = %{version}-%{release}
Requires:	trinity-ktnef = %{version}-%{release}
Requires:	trinity-libindex = %{version}-%{release}
Requires:	trinity-libkcal = %{version}-%{release}
Requires:	trinity-libkgantt = %{version}-%{release}
Requires:	trinity-libkleopatra = %{version}-%{release}
Requires:	trinity-libkmime = %{version}-%{release}
Requires:	trinity-libkpimexchange = %{version}-%{release}
Requires:	trinity-libkpimidentities = %{version}-%{release}
Requires:	trinity-libksieve = %{version}-%{release}
Requires:	trinity-libktnef = %{version}-%{release}
Requires:	trinity-libmimelib = %{version}-%{release}

Obsoletes:	trinity-kdepim < %{version}-%{release}
Provides:	trinity-kdepim = %{version}-%{release}

%description
This metapackage includes a collection of Personal Information Management
(PIM) applications provided with the official release of Trinity.

%files

##########

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries

Obsoletes:	trinity-kdepim-devel < %{version}-%{release}
Provides:	trinity-kdepim-devel = %{version}-%{release}

Requires:	%{name} = %{version}-%{release}
Requires:	libtdepim-devel = %{version}-%{release}
Requires:	trinity-karm-devel = %{version}-%{release}
Requires:	trinity-knotes-devel = %{version}-%{release}
Requires:	trinity-kontact-devel = %{version}-%{release}
Requires:	trinity-korganizer-devel = %{version}-%{release}
Requires:	trinity-libindex-devel = %{version}-%{release}
Requires:	trinity-libkcal-devel = %{version}-%{release}
Requires:	trinity-libkgantt-devel = %{version}-%{release}
Requires:	trinity-libkleopatra-devel = %{version}-%{release}
Requires:	trinity-libkmime-devel = %{version}-%{release}
Requires:	trinity-libkpimexchange-devel = %{version}-%{release}
Requires:	trinity-libkpimidentities-devel = %{version}-%{release}
Requires:	trinity-libksieve-devel = %{version}-%{release}
Requires:	trinity-libktnef-devel = %{version}-%{release}
Requires:	trinity-libmimelib-devel = %{version}-%{release}
Requires:	tdepim-cmake = %{version}-%{release}
Requires:	tdepim-kresources-devel = %{version}-%{release}

%description devel
This metapackage includes all development files for TDE PIM.

%files devel

##########

%package -n trinity-akregator
Summary:	RSS feed aggregator for TDE
Group:		Applications/Internet
Requires:	libtdepim = %{version}-%{release}
Requires:	trinity-libkcal = %{version}-%{release}

%description -n trinity-akregator
aKregator is a fast, lightweight, and intuitive feed reader program
for TDE.  It allows you to quickly browse through hundreds of
thousands of internet feeds in a quick, efficient, and familiar way.

%files -n trinity-akregator
%{_bindir}/akregator
%{tde_libdir}/libakregatorpart.la
%{tde_libdir}/libakregatorpart.so
%{tde_libdir}/libakregator_mk4storage_plugin.la
%{tde_libdir}/libakregator_mk4storage_plugin.so
%{_libdir}/libakregatorprivate.la
%{_libdir}/libakregatorprivate.so
%{_libdir}/libakregatorprivate.so.0
%{_libdir}/libakregatorprivate.so.0.0.0
%{tde_appdir}/akregator.desktop
%{_datadir}/apps/akregator
%{_datadir}/config.kcfg/akregator.kcfg
%{_datadir}/config.kcfg/mk4config.kcfg
%{_datadir}/icons/hicolor/128x128/apps/akregator.png
%{_datadir}/icons/crystalsvg/16x16/actions/rss_tag.png
%{_datadir}/icons/crystalsvg/22x22/actions/rss_tag.png
%{_datadir}/icons/crystalsvg/32x32/actions/rss_tag.png
%{_datadir}/icons/crystalsvg/48x48/actions/rss_tag.png
%{_datadir}/icons/crystalsvg/64x64/actions/rss_tag.png
%{_datadir}/icons/crystalsvg/16x16/apps/akregator_empty.png
%{_datadir}/icons/hicolor/16x16/apps/akregator.png
%{_datadir}/icons/hicolor/22x22/apps/akregator.png
%{_datadir}/icons/hicolor/32x32/apps/akregator.png
%{_datadir}/icons/hicolor/48x48/apps/akregator.png
%{_datadir}/icons/hicolor/64x64/apps/akregator.png
%{_datadir}/icons/hicolor/scalable/apps/akregator.svgz
%{_datadir}/services/akregator_mk4storage_plugin.desktop
%{_datadir}/services/akregator_part.desktop
%{_datadir}/services/feed.protocol
%{_datadir}/services/kontact/akregatorplugin*.desktop
%{_datadir}/servicetypes/akregator_plugin.desktop
%{tde_docdir}/HTML/en/akregator
%{tde_includedir}/akregator

%post -n trinity-akregator
/sbin/ldconfig
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-akregator
/sbin/ldconfig
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kaddressbook
Summary:	TDE addressbook application
Group:		Applications/Communications
Requires:	trinity-kdebase-pim-ioslaves
Requires:	tdepim-kresources = %{version}-%{release}

%description -n trinity-kaddressbook
KAddressBook is the main address book application for TDE; it enables you
to manage your contacts efficiently and comfortably. It can load and save
your contacts to many different locations, including the local file system,
LDAP servers, and SQL databases.

%files -n trinity-kaddressbook
%{_bindir}/kabc2mutt
%{_bindir}/kaddressbook
%{_bindir}/kabcdistlistupdater
%{tde_libdir}/kcm_kabconfig.la
%{tde_libdir}/kcm_kabconfig.so
%{tde_libdir}/kcm_kabcustomfields.la
%{tde_libdir}/kcm_kabcustomfields.so
%{tde_libdir}/kcm_kabldapconfig.la
%{tde_libdir}/kcm_kabldapconfig.so
%{tde_libdir}/ldifvcardthumbnail.la
%{tde_libdir}/ldifvcardthumbnail.so
%{tde_libdir}/libkaddrbk_*.la
%{tde_libdir}/libkaddrbk_*.so
%{tde_libdir}/libkaddressbookpart.la
%{tde_libdir}/libkaddressbookpart.so
%{_libdir}/libkabinterfaces.so.1
%{_libdir}/libkabinterfaces.so.1.0.0
%{_libdir}/libkaddressbook.so.0
%{_libdir}/libkaddressbook.so.0.0.0
%{tde_appdir}/kaddressbook.desktop
%{_datadir}/apps/kaddressbook
%{_datadir}/icons/hicolor/128x128/apps/kaddressbook.png
%{_datadir}/icons/hicolor/16x16/apps/kaddressbook.png
%{_datadir}/icons/hicolor/32x32/apps/kaddressbook.png
%{_datadir}/icons/hicolor/48x48/apps/kaddressbook.png
%{_datadir}/icons/hicolor/64x64/apps/kaddressbook.png
%{_datadir}/services/kabconfig.desktop
%{_datadir}/services/kabcustomfields.desktop
%{_datadir}/services/kabldapconfig.desktop
%{_datadir}/services/kaddressbook
%{_datadir}/services/kontact/kaddressbookplugin.desktop
%{_datadir}/services/kresources/kabc/imap.desktop
%{_datadir}/services/ldifvcardthumbnail.desktop
%{_datadir}/servicetypes/dcopaddressbook.desktop
%{_datadir}/servicetypes/kaddressbook_contacteditorwidget.desktop
%{_datadir}/servicetypes/kaddressbookimprotocol.desktop
%{_datadir}/servicetypes/kaddressbook_extension.desktop
%{_datadir}/servicetypes/kaddressbook_view.desktop
%{_datadir}/servicetypes/kaddressbook_xxport.desktop
%{tde_docdir}/HTML/en/kaddressbook
%{_datadir}/autostart/kabcdistlistupdater.desktop
%{tde_includedir}/kaddressbook
%{tde_includedir}/kabc

# kaddressbook-devel
%{_libdir}/libkabinterfaces.la
%{_libdir}/libkabinterfaces.so
%{_libdir}/libkaddressbook.la
%{_libdir}/libkaddressbook.so

%post -n trinity-kaddressbook
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kaddressbook
/sbin/ldconfig
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kalarm
Summary:	Trinity alarm message, command and email scheduler
Group:		Applications/Communications
Requires:	trinity-libkpimidentities = %{version}-%{release}

%description -n trinity-kalarm
KAlarm provides a graphical interface to schedule personal timed events -
pop-up alarm messages, command execution and sending emails. There is a
range of options for configuring recurring events.

A pop-up alarm can show either a simple text message, or the contents of a
text or image file, It can optionally be spoken, or play a sound file. You
can choose its appearance, and set reminders. Among KAlarm's other
facilities, you can set up templates to allow KAlarm to be used as a 'tea
timer'.

As an alternative to using the graphical interface, alarms can be scheduled
from the command line or via DCOP calls from other programs. KAlarm is
TDE-based, but will also run on other desktops.

%files -n trinity-kalarm
%{_bindir}/kalarm
%{_bindir}/kalarmd
%{tde_appdir}/kalarm.desktop
%{_datadir}/applnk/.hidden/kalarmd.desktop
%{_datadir}/applnk/Applications/kalarm.desktop
%{_datadir}/apps/kalarm
%{_datadir}/autostart/kalarm.tray.desktop
%{_datadir}/autostart/kalarmd.autostart.desktop
%{_datadir}/icons/crystalsvg/16x16/actions/kalarm.png
%{_datadir}/icons/hicolor/16x16/apps/kalarm.png
%{_datadir}/icons/crystalsvg/22x22/actions/kalarm.png
%{_datadir}/icons/hicolor/32x32/apps/kalarm.png
%{_datadir}/icons/hicolor/48x48/apps/kalarm.png
%{tde_docdir}/HTML/en/kalarm

%post -n trinity-kalarm
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kalarm
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kandy
Summary:	Trinity mobile phone utility
Group:		Applications/Communications

%description -n trinity-kandy
At the moment Kandy is more or less a terminal program with some special
features to store commands and their parameters, but is also has a simple GUI
to access the phone book of a mobile phone and it is able to save this phone
book to the TDE address book.

Kandy is aimed at mobile phones with integrated (GSM) modems.

%files -n trinity-kandy
%{_bindir}/kandy
%{_bindir}/kandy_client
%{tde_appdir}/kandy.desktop
%{_datadir}/applnk/Utilities/kandy.desktop
%{_datadir}/apps/kandy
%{_datadir}/config.kcfg/kandy.kcfg
%{tde_docdir}/HTML/en/kandy

%post -n trinity-kandy
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kandy
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-karm
Summary:	Trinity time tracker tool
Group:		Applications/Productivity

%description -n trinity-karm
KArm is a time tracker for busy people who need to keep track of the amount of
time they spend on various tasks.

%files -n trinity-karm
%{_bindir}/karm
%{_libdir}/libkarm.so.0
%{_libdir}/libkarm.so.0.0.0
%{tde_libdir}/libkarmpart.la
%{tde_libdir}/libkarmpart.so
%{tde_appdir}/karm.desktop
%{_datadir}/applnk/Utilities/karm.desktop
%{_datadir}/apps/karm
%{_datadir}/apps/karmpart
%{_datadir}/icons/hicolor/*/apps/karm.png
%{_datadir}/services/karm_part.desktop
%{_datadir}/services/kontact/karmplugin.desktop
%{tde_docdir}/HTML/en/karm

%post -n trinity-karm
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-karm
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-karm-devel
Summary:	Development files for karm
Group:		Development/Libraries

%description -n trinity-karm-devel
%{summary}

%files -n trinity-karm-devel
%{_libdir}/libkarm.so
%{_libdir}/libkarm.la

%post -n trinity-karm-devel
/sbin/ldconfig

%postun -n trinity-karm-devel
/sbin/ldconfig

##########

%package kfile-plugins
Summary:	TDE File dialog plugins for palm and vcf files
Group:		Environment/Libraries

%description kfile-plugins
File dialog plugins for palm and vcf files.

%files kfile-plugins
%{tde_libdir}/kfile_ics.la
%{tde_libdir}/kfile_ics.so
%{tde_libdir}/kfile_vcf.la
%{tde_libdir}/kfile_vcf.so
%{_datadir}/services/kfile_ics.desktop
%{_datadir}/services/kfile_vcf.desktop

##########

%package kio-plugins
Summary:	Trinity pim I/O Slaves
Group:		Environment/Libraries

%description kio-plugins
This package includes the pim kioslaves. This includes imap4, sieve,
and mbox.

%files kio-plugins
%{tde_libdir}/kio_groupwise.la
%{tde_libdir}/kio_groupwise.so
%{tde_libdir}/kio_imap4.la
%{tde_libdir}/kio_imap4.so
%{tde_libdir}/kio_mbox.la
%{tde_libdir}/kio_mbox.so
%{tde_libdir}/kio_scalix.la
%{tde_libdir}/kio_scalix.so
%{tde_libdir}/kio_sieve.la
%{tde_libdir}/kio_sieve.so
%{_datadir}/services/groupwise.protocol
%{_datadir}/services/groupwises.protocol
%{_datadir}/services/imap4.protocol
%{_datadir}/services/imaps.protocol
%{_datadir}/services/mbox.protocol
%{_datadir}/services/scalix.protocol
%{_datadir}/services/scalixs.protocol
%{_datadir}/services/sieve.protocol


##########

%package kresources
Summary:	Trinity pim resource plugins
Group:		Environment/Libraries
#Requires:	trinity-kaddressbook = %{version}-%{release}
#Requires:	trinity-korganizer = %{version}-%{release}
#Requires:	trinity-knotes = %{version}-%{release}
Requires:	libcaldav
Requires:	libcarddav

%description kresources
This package includes several plugins needed to interface with groupware
servers. It also includes plugins for features such as blogging and
tracking feature plans.

%files kresources
%{tde_libdir}/kcal_caldav.la
%{tde_libdir}/kcal_caldav.so
%{tde_libdir}/kcal_groupdav.la
%{tde_libdir}/kcal_groupdav.so
%{tde_libdir}/kcal_groupwise.la
%{tde_libdir}/kcal_groupwise.so
%{tde_libdir}/kcal_kolab.la
%{tde_libdir}/kcal_kolab.so
%{tde_libdir}/kcal_scalix.la
%{tde_libdir}/kcal_scalix.so
%{tde_libdir}/kcal_newexchange.la
%{tde_libdir}/kcal_newexchange.so
%{tde_libdir}/kcal_resourcefeatureplan.la
%{tde_libdir}/kcal_resourcefeatureplan.so
%{tde_libdir}/kcal_slox.la
%{tde_libdir}/kcal_slox.so
%{tde_libdir}/kcal_xmlrpc.la
%{tde_libdir}/kcal_xmlrpc.so
%{tde_libdir}/knotes_kolab.la
%{tde_libdir}/knotes_kolab.so
%{tde_libdir}/knotes_scalix.la
%{tde_libdir}/knotes_scalix.so
%{tde_libdir}/knotes_xmlrpc.la
%{tde_libdir}/knotes_xmlrpc.so
%{_libdir}/libkabckolab.so.0
%{_libdir}/libkabckolab.so.0.0.0
%{_libdir}/libkabcscalix.so.0
%{_libdir}/libkabcscalix.so.0.0.0
%{_libdir}/libkabc_groupdav.so.1
%{_libdir}/libkabc_groupdav.so.1.0.0
%{_libdir}/libkabc_groupwise.so.1
%{_libdir}/libkabc_groupwise.so.1.0.0
%{_libdir}/libkabc_newexchange.so.1
%{_libdir}/libkabc_newexchange.so.1.0.0
%{_libdir}/libkabc_slox.so.0
%{_libdir}/libkabc_slox.so.0.0.0
%{_libdir}/libkabc_xmlrpc.so.1
%{_libdir}/libkabc_xmlrpc.so.1.0.0
%{_libdir}/libkcalkolab.so.0
%{_libdir}/libkcalkolab.so.0.0.0
%{_libdir}/libkcalscalix.so.0
%{_libdir}/libkcalscalix.so.0.0.0
%{_libdir}/libkcal_caldav.so.1
%{_libdir}/libkcal_caldav.so.1.0.0
%{_libdir}/libkabc_carddav.so.1
%{_libdir}/libkabc_carddav.so.1.0.0
%{_libdir}/libkcal_groupdav.so.1
%{_libdir}/libkcal_groupdav.so.1.0.0
%{_libdir}/libkcal_groupwise.so.1
%{_libdir}/libkcal_groupwise.so.1.0.0
%{_libdir}/libkcal_newexchange.so.1
%{_libdir}/libkcal_newexchange.so.1.0.0
%{_libdir}/libkcal_resourcefeatureplan.so.1
%{_libdir}/libkcal_resourcefeatureplan.so.1.0.0
%{_libdir}/libkcal_slox.so.0
%{_libdir}/libkcal_slox.so.0.0.0
%{_libdir}/libkcal_xmlrpc.so.1
%{_libdir}/libkcal_xmlrpc.so.1.0.0
%{_libdir}/libkgroupwarebase.so.0
%{_libdir}/libkgroupwarebase.so.0.0.0
%{_libdir}/libkgroupwaredav.so.0
%{_libdir}/libkgroupwaredav.so.0.0.0
%{_libdir}/libknoteskolab.so.0
%{_libdir}/libknoteskolab.so.0.0.0
%{_libdir}/libknotesscalix.so.0
%{_libdir}/libknotesscalix.so.0.0.0
%{_libdir}/libknotes_xmlrpc.so.1
%{_libdir}/libknotes_xmlrpc.so.1.0.0
%{_libdir}/libkslox.so.0
%{_libdir}/libkslox.so.0.0.0
%{_libdir}/libgwsoap.so.0
%{_libdir}/libgwsoap.so.0.0.0
%{_datadir}/services/kresources/kabc/kabc_groupdav.desktop
%{_datadir}/services/kresources/kabc/kabc_groupwise.desktop
%{_datadir}/services/kresources/kabc/kabc_newexchange.desktop
%{_datadir}/services/kresources/kabc/kabc_opengroupware.desktop
%{_datadir}/services/kresources/kabc/kabc_ox.desktop
%{_datadir}/services/kresources/kabc/kabc_slox.desktop
%{_datadir}/services/kresources/kabc/kabc_xmlrpc.desktop
%{_datadir}/services/kresources/kabc/kolab.desktop
%{_datadir}/services/kresources/kabc/scalix.desktop
%{_datadir}/services/kresources/kcal/exchange.desktop
%{_datadir}/services/kresources/kcal/kcal_caldav.desktop
%{_datadir}/services/kresources/kabc/kabc_carddav.desktop
%{_datadir}/services/kresources/kcal/kcal_groupdav.desktop
%{_datadir}/services/kresources/kcal/kcal_groupwise.desktop
%{_datadir}/services/kresources/kcal/kcal_newexchange.desktop
%{_datadir}/services/kresources/kcal/kcal_opengroupware.desktop
%{_datadir}/services/kresources/kcal/kcal_ox.desktop
%{_datadir}/services/kresources/kcal/kcal_resourcefeatureplan.desktop
%{_datadir}/services/kresources/kcal/kcal_slox.desktop
%{_datadir}/services/kresources/kcal/kcal_xmlrpc.desktop
%{_datadir}/services/kresources/kcal/kolab.desktop
%{_datadir}/services/kresources/kcal/scalix.desktop
%{_datadir}/services/kresources/knotes/knotes_xmlrpc.desktop
%{_datadir}/services/kresources/knotes/kolabresource.desktop
%{_datadir}/services/kresources/knotes/scalix.desktop

%{_datadir}/apps/kconf_update/upgrade-resourcetype.pl
%{_datadir}/apps/kconf_update/kolab-resource.upd

%{tde_libdir}/kabc_carddav.la
%{tde_libdir}/kabc_carddav.so
%{tde_libdir}/kabc_groupdav.la
%{tde_libdir}/kabc_groupdav.so
%{tde_libdir}/kabc_groupwise.la
%{tde_libdir}/kabc_groupwise.so
%{tde_libdir}/kabc_kolab.la
%{tde_libdir}/kabc_kolab.so
%{tde_libdir}/kabc_newexchange.la
%{tde_libdir}/kabc_newexchange.so
%{tde_libdir}/kabc_scalix.la
%{tde_libdir}/kabc_scalix.so
%{tde_libdir}/kabc_slox.la
%{tde_libdir}/kabc_slox.so
%{tde_libdir}/kabc_xmlrpc.la
%{tde_libdir}/kabc_xmlrpc.so

%post kresources
/sbin/ldconfig

%postun kresources
/sbin/ldconfig

##########

%package kresources-devel
Summary:	Development files for kresources
Group:		Development/Libraries
Requires:	tdepim-kresources = %{version}-%{release}
Requires:	libcaldav
Requires:	libcarddav

%description kresources-devel
%{summary}

%files kresources-devel
%{_libdir}/libkslox.la
%{_libdir}/libkslox.so
%{_libdir}/libkabc_groupdav.la
%{_libdir}/libkabc_groupdav.so
%{_libdir}/libkabc_groupwise.la
%{_libdir}/libkabc_groupwise.so
%{_libdir}/libgwsoap.la
%{_libdir}/libgwsoap.so
%{_libdir}/libkabc_carddav.la
%{_libdir}/libkabc_carddav.so
%{_libdir}/libkabc_newexchange.la
%{_libdir}/libkabc_newexchange.so
%{_libdir}/libkabc_slox.la
%{_libdir}/libkabc_slox.so
%{_libdir}/libkabc_xmlrpc.la
%{_libdir}/libkabc_xmlrpc.so
%{_libdir}/libkabckolab.la
%{_libdir}/libkabckolab.so
%{_libdir}/libkabcscalix.la
%{_libdir}/libkabcscalix.so
%{_libdir}/libkcal_caldav.la
%{_libdir}/libkcal_caldav.so
%{_libdir}/libkcal_groupdav.la
%{_libdir}/libkcal_groupdav.so
%{_libdir}/libkcal_groupwise.la
%{_libdir}/libkcal_groupwise.so
%{_libdir}/libkcal_newexchange.la
%{_libdir}/libkcal_newexchange.so
%{_libdir}/libkcal_resourcefeatureplan.la
%{_libdir}/libkcal_resourcefeatureplan.so
%{_libdir}/libkcal_slox.la
%{_libdir}/libkcal_slox.so
%{_libdir}/libkcal_xmlrpc.la
%{_libdir}/libkcal_xmlrpc.so
%{_libdir}/libkcalkolab.la
%{_libdir}/libkcalkolab.so
%{_libdir}/libkcalscalix.la
%{_libdir}/libkcalscalix.so
%{_libdir}/libkgroupwarebase.la
%{_libdir}/libkgroupwarebase.so
%{_libdir}/libkgroupwaredav.la
%{_libdir}/libkgroupwaredav.so
%{_libdir}/libknotes_xmlrpc.la
%{_libdir}/libknotes_xmlrpc.so
%{_libdir}/libknoteskolab.la
%{_libdir}/libknoteskolab.so
%{_libdir}/libknotesscalix.la
%{_libdir}/libknotesscalix.so
%{tde_includedir}/kpimprefs.h

%post kresources-devel
/sbin/ldconfig

%postun kresources-devel
/sbin/ldconfig

##########

%package wizards
Summary:	Trinity server configuration wizards
Group:		Applications/Communications

%description wizards
This package contains KDE-based wizards for configuring eGroupware,
Kolab, and SUSE Linux Openexchange servers.

%files wizards
%{_bindir}/egroupwarewizard
%{_bindir}/exchangewizard
%{_bindir}/groupwarewizard
%{_bindir}/groupwisewizard
%{_bindir}/kolabwizard
%{_bindir}/scalixadmin
%{_bindir}/scalixwizard
%{_bindir}/sloxwizard
%{tde_libdir}/libegroupwarewizard.la
%{tde_libdir}/libegroupwarewizard.so
%{tde_libdir}/libexchangewizard.la
%{tde_libdir}/libexchangewizard.so
%{tde_libdir}/libgroupwisewizard.la
%{tde_libdir}/libgroupwisewizard.so
%{tde_libdir}/libkolabwizard.la
%{tde_libdir}/libkolabwizard.so
%{tde_libdir}/libscalixwizard.la
%{tde_libdir}/libscalixwizard.so
%{tde_libdir}/libsloxwizard.la
%{tde_libdir}/libsloxwizard.so
%{tde_appdir}/groupwarewizard.desktop
%{_datadir}/config.kcfg/egroupware.kcfg
%{_datadir}/config.kcfg/groupwise.kcfg
%{_datadir}/config.kcfg/kolab.kcfg
%{_datadir}/config.kcfg/scalix.kcfg
%{_datadir}/config.kcfg/slox.kcfg

%post wizards
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun wizards
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%if %{?with_kitchensync}
%package -n trinity-kitchensync
Summary:	Synchronization framework
Group:		Applications/Communications
#Suggests: konqueror-trinity
#Conflicts: kdebluetooth-irmcsync-trinity (<< 0.99+1.0beta2-4.1), ksync-trinity

%description -n trinity-kitchensync
This package contains a synchronization framework, still under heavy
development (?).  Kitchensync uses opensync.

%files -n trinity-kitchensync
%{_bindir}/kitchensync
%{tde_libdir}/libkitchensyncpart.la
%{tde_libdir}/libkitchensyncpart.so
%{_datadir}/apps/kitchensync
%{_libdir}/libkitchensync.so.0
%{_libdir}/libkitchensync.so.0.0.0
%{_libdir}/libqopensync.so.0
%{_libdir}/libqopensync.so.0.0.0
%{tde_appdir}/kitchensync.desktop
%{_datadir}/icons/hicolor/16x16/apps/kitchensync.png
%{_datadir}/icons/hicolor/22x22/apps/kitchensync.png
%{_datadir}/icons/hicolor/32x32/apps/kitchensync.png
%{_datadir}/icons/hicolor/48x48/apps/kitchensync.png

%post -n trinity-kitchensync
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kitchensync
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :
%endif

##########

%package -n trinity-kleopatra
Summary:	Trinity Certificate Manager
Group:		Applications/Communications
Requires:	gnupg2
Requires:	dirmngr
Requires:	pinentry

%description -n trinity-kleopatra
Kleopatra is the TDE tool for managing X.509 certificates in the gpgsm
keybox and for retrieving certificates from LDAP servers.

%files -n trinity-kleopatra
%{_bindir}/kleopatra
%{_bindir}/kwatchgnupg
%{tde_libdir}/kcm_kleopatra.la
%{tde_libdir}/kcm_kleopatra.so
%{tde_appdir}/kleopatra_import.desktop
%{_datadir}/apps/kleopatra
%{_datadir}/apps/kwatchgnupg
%{_datadir}/services/kleopatra_config_*.desktop
%{tde_docdir}/HTML/en/kleopatra
%{tde_docdir}/HTML/en/kwatchgnupg

%post -n trinity-kleopatra
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kleopatra
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kmail
Summary:	Trinity Email client
Group:		Applications/Communications
Requires:	tdepim-kio-plugins = %{version}-%{release}
Requires:	gnupg2
Requires:	pinentry
Requires:	procmail
Requires:	trinity-kaddressbook = %{version}-%{release}
Requires:	trinity-kleopatra = %{version}-%{release}
Requires:	trinity-kdebase-pim-ioslaves

Provides: imap-client, mail-reader

%description -n trinity-kmail
KMail is a fully-featured email client that fits nicely into the TDE
desktop. It has features such as support for IMAP, POP3, multiple accounts,
mail filtering and sorting, PGP/GnuPG privacy, and inline attachments.

You need to install tdepim-kio-plugins if you want to use IMAP or
mbox files, and/or tdebase-kio-plugins if you want to use POP3.

%files -n trinity-kmail
%{_datadir}/config/kmail.antispamrc
%{_datadir}/config/kmail.antivirusrc
%{_bindir}/kmail
%{_bindir}/kmail_*.sh
%{tde_libdir}/kcm_kmail.la
%{tde_libdir}/kcm_kmail.so
%{tde_libdir}/libkmail_bodypartformatter_application_octetstream.la
%{tde_libdir}/libkmail_bodypartformatter_application_octetstream.so
%{tde_libdir}/libkmail_bodypartformatter_text_calendar.la
%{tde_libdir}/libkmail_bodypartformatter_text_calendar.so
%{tde_libdir}/libkmail_bodypartformatter_text_vcard.la
%{tde_libdir}/libkmail_bodypartformatter_text_vcard.so
%{tde_libdir}/libkmail_bodypartformatter_text_xdiff.la
%{tde_libdir}/libkmail_bodypartformatter_text_xdiff.so
%{tde_libdir}/libkmailpart.la
%{tde_libdir}/libkmailpart.so
%{_libdir}/libkmailprivate.la
%{_libdir}/libkmailprivate.so
%{tde_appdir}/KMail.desktop
%{tde_appdir}/kmail_view.desktop
%{_datadir}/apps/kconf_update/kmail-3.1-update-new-mail-notification-settings.pl
%{_datadir}/apps/kconf_update/kmail-3.1-use-UOID-for-identities.pl
%{_datadir}/apps/kconf_update/kmail-3.1.4-dont-use-UOID-0-for-any-identity.pl
%{_datadir}/apps/kconf_update/kmail-3.2-misc.sh
%{_datadir}/apps/kconf_update/kmail-3.2-update-loop-on-goto-unread-settings.sh
%{_datadir}/apps/kconf_update/kmail-3.3-aegypten.pl
%{_datadir}/apps/kconf_update/kmail-3.3-misc.pl
%{_datadir}/apps/kconf_update/kmail-3.3-move-identities.pl
%{_datadir}/apps/kconf_update/kmail-3.3-split-sign-encr-keys.sh
%{_datadir}/apps/kconf_update/kmail-3.3-use-ID-for-accounts.pl
%{_datadir}/apps/kconf_update/kmail-3.3b1-misc.pl
%{_datadir}/apps/kconf_update/kmail-3.4-misc.pl
%{_datadir}/apps/kconf_update/kmail-3.4.1-update-status-filters.pl
%{_datadir}/apps/kconf_update/kmail-3.5-trigger-flag-migration.pl
%{_datadir}/apps/kconf_update/kmail-3.5-filter-icons.pl
%{_datadir}/apps/kconf_update/kmail-pgpidentity.pl
%{_datadir}/apps/kconf_update/kmail-upd-identities.pl
%{_datadir}/apps/kconf_update/kmail.upd
%{_datadir}/apps/kconf_update/upgrade-signature.pl
%{_datadir}/apps/kconf_update/upgrade-transport.pl
%{_datadir}/apps/kmail
%{_datadir}/config.kcfg/custommimeheader.kcfg
%{_datadir}/config.kcfg/kmail.kcfg
%{_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_datadir}/config.kcfg/replyphrases.kcfg
%{_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_datadir}/icons/hicolor/128x128/apps/kmail.png
%{_datadir}/icons/hicolor/16x16/apps/kmail.png
%{_datadir}/icons/hicolor/22x22/apps/kmail.png
%{_datadir}/icons/crystalsvg/22x22/apps/kmaillight.png
%{_datadir}/icons/hicolor/32x32/apps/kmail.png
%{_datadir}/icons/crystalsvg/32x32/apps/kmaillight.png
%{_datadir}/icons/hicolor/48x48/apps/kmail.png
%{_datadir}/icons/hicolor/64x64/apps/kmail.png
%{_datadir}/icons/hicolor/scalable/apps/kmail.svgz
%{_datadir}/services/kmail_config_*.desktop
%{_datadir}/services/kontact/kmailplugin.desktop
%{_datadir}/servicetypes/dcopimap.desktop
%{_datadir}/servicetypes/dcopmail.desktop
%{tde_docdir}/HTML/en/kmail
%{tde_includedir}/kmail
%{tde_includedir}/kmail*.h

%post -n trinity-kmail
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kmail
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########
 
%package -n trinity-kmailcvt
Summary:	Trinity KMail mail folder converter
Group:		Applications/Communications
Requires:	trinity-kmail = %{version}-%{release}

%description -n trinity-kmailcvt
Converts mail folders to KMail format.  Formats supported for import
include Outlook Express, Evolution, and plain mbox.

%files -n trinity-kmailcvt
%{_bindir}/kmailcvt
%{_datadir}/applnk/Utilities/kmailcvt.desktop
%{_datadir}/apps/kmailcvt
%{_datadir}/icons/crystalsvg/16x16/apps/kmailcvt.png
%{_datadir}/icons/crystalsvg/32x32/apps/kmailcvt.png
%{_datadir}/icons/crystalsvg/48x48/apps/kmailcvt.png

%post -n trinity-kmailcvt
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done

%postun -n trinity-kmailcvt
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done

##########

%package -n trinity-knode
Summary:	Trinity news reader
Group:		Applications/Internet

%description -n trinity-knode
KNode is an easy-to-use, convenient newsreader. It is intended to be usable
by inexperienced users, but also includes support for such features as
MIME attachments, article scoring, and creating and verifying GnuPG
signatures.

%files -n trinity-knode
%{_bindir}/knode
%{tde_libdir}/kcm_knode.la
%{tde_libdir}/kcm_knode.so
%{tde_libdir}/libknodepart.la
%{tde_libdir}/libknodepart.so
%{_libdir}/libknodecommon.la
%{_libdir}/libknodecommon.so
%{_libdir}/libknodecommon.so.3
%{_libdir}/libknodecommon.so.3.0.0
%{tde_appdir}/KNode.desktop
%{_datadir}/apps/knode
%{tde_docdir}/HTML/en/knode
%{_datadir}/icons/hicolor/128x128/apps/knode.png
%{_datadir}/icons/hicolor/128x128/apps/knode2.png
%{_datadir}/icons/hicolor/16x16/apps/knode.png
%{_datadir}/icons/hicolor/16x16/apps/knode2.png
%{_datadir}/icons/hicolor/32x32/apps/knode.png
%{_datadir}/icons/hicolor/32x32/apps/knode2.png
%{_datadir}/icons/hicolor/48x48/apps/knode.png
%{_datadir}/icons/hicolor/48x48/apps/knode2.png
%{_datadir}/icons/hicolor/64x64/apps/knode.png
%{_datadir}/icons/hicolor/64x64/apps/knode2.png
%{_datadir}/services/knewsservice.protocol
%{_datadir}/services/knode_config_*.desktop
%{_datadir}/services/kontact/knodeplugin.desktop

%post -n trinity-knode
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-knode
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-knotes
Summary:	Trinity sticky notes
Group:		Applications/Utilities
Requires:	tdepim-kresources = %{version}-%{release}

%description -n trinity-knotes
KNotes is a program that lets you write sticky notes. The notes are saved
automatically when you exit the program, and they display when you open the
program.  The program supports printing and mailing your notes.

%files -n trinity-knotes
%{_bindir}/knotes
%{tde_libdir}/knotes_local.la
%{tde_libdir}/knotes_local.so
%{_libdir}/libknotes.so.0
%{_libdir}/libknotes.so.0.0.0
%{tde_appdir}/knotes.desktop
%{_datadir}/apps/knotes
%{_datadir}/config.kcfg/knoteconfig.kcfg
%{_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_datadir}/icons/hicolor/*/apps/knotes.png
%{_datadir}/services/kresources/knotes/imap.desktop
%{_datadir}/services/kresources/knotes/local.desktop
%{_datadir}/services/kresources/knotes_manager.desktop
%{_datadir}/services/kontact/knotesplugin.desktop
%{tde_docdir}/HTML/en/knotes

%post -n trinity-knotes
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-knotes
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-knotes-devel
Summary:	Development files for knots
Group:		Development/Libraries
Requires:	trinity-knotes = %{version}-%{release}
Requires:	tdepim-kresources-devel = %{version}-%{release}

%description -n trinity-knotes-devel
%{summary}

%files -n trinity-knotes-devel
%{_libdir}/libknotes.so
%{_libdir}/libknotes.la
%{tde_includedir}/KNotesAppIface.h
%{tde_includedir}/KNotesIface.h

%post -n trinity-knotes-devel
/sbin/ldconfig

%postun -n trinity-knotes-devel
/sbin/ldconfig

##########

%package -n trinity-kode
Summary:	Helper library for programmatic generation of C++ code
Group:		Development/Libraries

%description -n trinity-kode
This package includes a program kode for generation of C++ template files
and kxml_compiler for generation of C++ classes representing XML data
described by RelaxNG schemes.

%files -n trinity-kode
%{_bindir}/kode
%{_bindir}/kxml_compiler
%{_libdir}/libkode.la
%{_libdir}/libkode.so
%{_libdir}/libkode.so.1
%{_libdir}/libkode.so.1.0.0

%post -n trinity-kode
/sbin/ldconfig

%postun -n trinity-kode
/sbin/ldconfig

##########

%package -n trinity-konsolekalendar
Summary:	Trinity konsole personal organizer
Group:		Applications/Productivity

%description -n trinity-konsolekalendar
KonsoleKalendar is a command-line interface to TDE calendars.
Konsolekalendar complements the TDE KOrganizer by providing a console
frontend to manage your calendars.

%files -n trinity-konsolekalendar
%{_bindir}/konsolekalendar
%{tde_appdir}/konsolekalendar.desktop
%{_datadir}/icons/crystalsvg/16x16/apps/konsolekalendar.png
%{_datadir}/icons/crystalsvg/22x22/apps/konsolekalendar.png
%{_datadir}/icons/crystalsvg/32x32/apps/konsolekalendar.png
%{tde_docdir}/HTML/en/konsolekalendar

%post -n trinity-konsolekalendar
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-konsolekalendar
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kontact
Summary:	Trinity pim application
Group:		Applications/Communications
Requires:	trinity-kmail = %{version}-%{release}
Requires:	trinity-korganizer = %{version}-%{release}
Requires:	trinity-kaddressbook = %{version}-%{release}
Requires:	trinity-knode = %{version}-%{release}
Requires:	trinity-knotes = %{version}-%{release}
Requires:	trinity-akregator = %{version}-%{release}

%description -n trinity-kontact
Kontact is the integrated solution to your personal information management
needs. It combines TDE applications like KMail, KOrganizer, and
KAddressBook into a single interface to provide easy access to mail,
scheduling, address book and other PIM functionality.

%files -n trinity-kontact
%{_bindir}/kontact
%{tde_libdir}/kcm_kmailsummary.la
%{tde_libdir}/kcm_kmailsummary.so
%{tde_libdir}/kcm_kontact.la
%{tde_libdir}/kcm_kontact.so
%{tde_libdir}/kcm_kontactknt.la
%{tde_libdir}/kcm_kontactknt.so
%{tde_libdir}/kcm_kontactsummary.la
%{tde_libdir}/kcm_kontactsummary.so
%{tde_libdir}/kcm_korgsummary.la
%{tde_libdir}/kcm_korgsummary.so
%{tde_libdir}/kcm_sdsummary.la
%{tde_libdir}/kcm_sdsummary.so
%{tde_libdir}/libkontact_*.la
%{tde_libdir}/libkontact_*.so
%{_libdir}/libkontact.so.1
%{_libdir}/libkontact.so.1.0.0
%{_libdir}/libkpinterfaces.so.1
%{_libdir}/libkpinterfaces.so.1.0.0
%{tde_appdir}/Kontact.desktop
%{tde_appdir}/kontactdcop.desktop
%{_datadir}/apps/kontact
%{_datadir}/apps/kontactsummary/kontactsummary_part.rc
%{_datadir}/config.kcfg/kontact.kcfg
%{_datadir}/icons/hicolor/*/apps/kontact.png
%{_datadir}/icons/crystalsvg/*/actions/kontact_*.png
%{_datadir}/services/kcmkmailsummary.desktop
%{_datadir}/services/kcmkontactknt.desktop
%{_datadir}/services/kcmkontactsummary.desktop
%{_datadir}/services/kcmkorgsummary.desktop
%{_datadir}/services/kcmsdsummary.desktop
%{_datadir}/services/kontact/newstickerplugin.desktop
%{_datadir}/services/kontact/specialdatesplugin.desktop
%{_datadir}/services/kontact/summaryplugin.desktop
%{_datadir}/services/kontact/weatherplugin.desktop
%{_datadir}/services/kontactconfig.desktop
%{_datadir}/servicetypes/kontactplugin.desktop
%{tde_docdir}/HTML/en/kontact
%{tde_docdir}/HTML/en/kpilot

%post -n trinity-kontact
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kontact
for f in crystalsvg hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-kontact-devel
Summary:	Development files for kontact
Group:		Development/Libraries
Requires:	trinity-kontact = %{version}-%{release}

%description -n trinity-kontact-devel
%{summary}

%files -n trinity-kontact-devel
%{_libdir}/libkontact.la
%{_libdir}/libkontact.so
%{_libdir}/libkpinterfaces.la
%{_libdir}/libkpinterfaces.so
%{tde_includedir}/kontact

%post -n trinity-kontact-devel
/sbin/ldconfig

%postun -n trinity-kontact-devel
/sbin/ldconfig

##########

%package -n trinity-korganizer
Summary:	Trinity personal organizer
Group:		Applications/Productivity
Requires:	trinity-libkpimidentities = %{version}-%{release}
Requires:	trinity-libkpimexchange = %{version}-%{release}
Requires:	tdepim-kresources = %{version}-%{release}

%description -n trinity-korganizer
This package contains KOrganizer, a calendar and scheduling program.

KOrganizer aims to be a complete program for organizing appointments,
contacts, projects, etc. KOrganizer natively supports information interchange
with other calendar applications, through the industry standard vCalendar
personal data interchange file format. This eases the move from other
modern PIMs to KOrganizer.

KOrganizer offers full synchronization with Palm Pilots, if kpilot is
installed.

%files -n trinity-korganizer
%{_bindir}/ical2vcal
%{_bindir}/korgac
%{_bindir}/korganizer
%{tde_libdir}/kcm_korganizer.la
%{tde_libdir}/kcm_korganizer.so
%{tde_libdir}/libkorg_*.la
%{tde_libdir}/libkorg_*.so
%{tde_libdir}/libkorganizerpart.la
%{tde_libdir}/libkorganizerpart.so
%{_libdir}/libkocorehelper.so.1
%{_libdir}/libkocorehelper.so.1.0.0
%{_libdir}/libkorg_stdprinting.so.1
%{_libdir}/libkorg_stdprinting.so.1.0.0
%{_libdir}/libkorganizer.so.1
%{_libdir}/libkorganizer.so.1.0.0
%{_libdir}/libkorganizer_calendar.so.1
%{_libdir}/libkorganizer_calendar.so.1.0.0
%{_libdir}/libkorganizer_eventviewer.so.1
%{_libdir}/libkorganizer_eventviewer.so.1.0.0
%{tde_appdir}/korganizer.desktop
%{_datadir}/apps/kconf_update/korganizer.upd
%{_datadir}/apps/korgac
%{_datadir}/apps/korganizer
%{_datadir}/autostart/korgac.desktop
%{_datadir}/config.kcfg/korganizer.kcfg
%{_datadir}/icons/hicolor/128x128/apps/korganizer.png
%{_datadir}/icons/hicolor/16x16/apps/korganizer.png
%{_datadir}/icons/hicolor/32x32/apps/korganizer.png
%{_datadir}/icons/hicolor/48x48/apps/korganizer.png
%{_datadir}/icons/hicolor/64x64/apps/korganizer.png
%{_datadir}/services/kontact/korganizerplugin.desktop
%{_datadir}/services/kontact/journalplugin.desktop
%{_datadir}/services/kontact/todoplugin.desktop
%{_datadir}/services/korganizer_*.desktop
%{_datadir}/services/korganizer
%{_datadir}/services/webcal.protocol
%{_datadir}/servicetypes/calendardecoration.desktop
%{_datadir}/servicetypes/calendarplugin.desktop
%{_datadir}/servicetypes/dcopcalendar.desktop
%{_datadir}/servicetypes/korganizerpart.desktop
%{_datadir}/servicetypes/korgprintplugin.desktop
%{tde_docdir}/HTML/en/korganizer
%{_includedir}/korganizer
%{tde_includedir}/korganizer
%{tde_includedir}/calendar

%post -n trinity-korganizer
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-korganizer
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-korganizer-devel
Summary:	Development files for korganizer
Group:		Development/Libraries
Requires:	trinity-korganizer = %{version}-%{release}

%description -n trinity-korganizer-devel
%{summary}

%files -n trinity-korganizer-devel
%{_libdir}/libkocorehelper.la
%{_libdir}/libkocorehelper.so
%{_libdir}/libkorg_stdprinting.la
%{_libdir}/libkorg_stdprinting.so
%{_libdir}/libkorganizer.la
%{_libdir}/libkorganizer.so
%{_libdir}/libkorganizer_calendar.la
%{_libdir}/libkorganizer_calendar.so
%{_libdir}/libkorganizer_eventviewer.la
%{_libdir}/libkorganizer_eventviewer.so

%post -n trinity-korganizer-devel
/sbin/ldconfig

%postun -n trinity-korganizer-devel
/sbin/ldconfig

##########

%package -n trinity-korn
Summary:	Trinity mail checker
Group:		Applications/Communications
Requires:	tdepim-kio-plugins = %{version}-%{release}
#Requires:	tdebase-kio-plugins-trinity

%description -n trinity-korn
Korn is a TDE mail checker that can display a small summary in the Kicker
tray.  It supports checking mbox, pop3, imap4, and nntp sources.

Once mail is received you can have Korn run a third party program or change
the color/icon of the Kicker display.  In addition to this you can have
Korn run a program once you click on the docked icon in Kicker.

%files -n trinity-korn
%{_bindir}/korn
%{_libdir}/kconf_update_bin/korn-3-4-config_change
%{tde_appdir}/KOrn.desktop
%{_datadir}/apps/kconf_update/korn-3-4-config_change.upd
%{_datadir}/apps/kconf_update/korn-3-5-metadata-update.pl
%{_datadir}/apps/kconf_update/korn-3-5-ssl-update.pl
%{_datadir}/apps/kconf_update/korn-3-5-update.upd
%{_datadir}/icons/hicolor/16x16/apps/korn.png
%{_datadir}/icons/hicolor/32x32/apps/korn.png
%{_datadir}/icons/hicolor/48x48/apps/korn.png
%{tde_docdir}/HTML/en/korn

%post -n trinity-korn
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-korn
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-ktnef
Summary:	Trinity TNEF viewer
Group:		Applications/Communications

%description -n trinity-ktnef
The TNEF File Viewer allows you to handle mail attachments using the TNEF
format. These attachments are usually found in mails coming from Microsoft
mail servers and embed the mail properties as well as the actual attachments.

%files -n trinity-ktnef
%{_bindir}/ktnef
%{tde_appdir}/ktnef.desktop
%{_datadir}/apps/ktnef
%{_datadir}/icons/hicolor/48x48/apps/ktnef.png
%{_datadir}/icons/locolor/16x16/apps/ktnef.png
%{_datadir}/icons/locolor/32x32/apps/ktnef.png
%{_datadir}/mimelnk/application/ms-tnef.desktop
%{tde_docdir}/HTML/en/ktnef

%post -n trinity-ktnef
for f in hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-ktnef
for f in hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package -n trinity-libindex
Summary:	Trinity indexing library
Group:		Environment/Libraries

%description -n trinity-libindex
This library provides text indexing and is currently used by KMail
to implement fast searches in mail bodies.

This is the runtime package for programs that use the libindex library.

%files -n trinity-libindex
%{_libdir}/libindex.so.0
%{_libdir}/libindex.so.0.0.0

%post -n trinity-libindex
/sbin/ldconfig

%postun -n trinity-libindex
/sbin/ldconfig

##########

%package -n trinity-libindex-devel
Summary:	Trinity indexing library [development]
Group:		Development/Libraries
Requires:	trinity-libindex = %{version}-%{release}

%description -n trinity-libindex-devel
This library provides text indexing and is currently used by KMail
to implement searching through mail text.

This is the development package which contains the headers for the libindex-trinity
library.

%files -n trinity-libindex-devel
%{_bindir}/indexlib-config
%{tde_includedir}/index
%{_libdir}/libindex.la
%{_libdir}/libindex.so

%post -n trinity-libindex-devel
/sbin/ldconfig

%postun -n trinity-libindex-devel
/sbin/ldconfig

##########

%package -n trinity-libkcal
Summary:	Trinity calendaring library
Group:		Environment/Libraries
#Requires:	tdepim-kresources = %{version}-%{release}

%description -n trinity-libkcal
This library provides a C++ API for handling the vCalendar and iCalendar
formats.

This is the runtime package for programs that use the libkcal-trinity library.

%files -n trinity-libkcal
%{tde_libdir}/kcal_kabc.la
%{tde_libdir}/kcal_kabc.so
%{tde_libdir}/kcal_localdir.la
%{tde_libdir}/kcal_localdir.so
%{tde_libdir}/kcal_local.la
%{tde_libdir}/kcal_local.so
%{tde_libdir}/kcal_remote.la
%{tde_libdir}/kcal_remote.so
%{_libdir}/libkcal.so.2
%{_libdir}/libkcal.so.2.0.0
%{_libdir}/libkcal_resourceremote.so.1
%{_libdir}/libkcal_resourceremote.so.1.0.0
%{_libdir}/libkholidays.so.1
%{_libdir}/libkholidays.so.1.0.0
%{_datadir}/apps/libkholidays
%{_datadir}/services/kresources/kcal/imap.desktop
%{_datadir}/services/kresources/kcal/kabc.desktop
%{_datadir}/services/kresources/kcal/local.desktop
%{_datadir}/services/kresources/kcal/localdir.desktop
%{_datadir}/services/kresources/kcal/remote.desktop
%{_datadir}/services/kresources/kcal_manager.desktop

%post -n trinity-libkcal
/sbin/ldconfig

%postun -n trinity-libkcal
/sbin/ldconfig

##########

%package -n trinity-libkcal-devel
Summary:	Trinity calendaring library [development]
Group:		Development/Libraries
Requires:	trinity-libkcal = %{version}-%{release}
Requires:	libtdepim-devel = %{version}-%{release}
Requires:	trinity-libktnef-devel = %{version}-%{release}

%description -n trinity-libkcal-devel
This library provides a C++ API for handling the vCalendar and iCalendar
formats.

This is the development package which contains the headers for the libkcal-trinity
library.

%files -n trinity-libkcal-devel
%{tde_includedir}/libemailfunctions/idmapper.h
%{tde_includedir}/libkcal
%{_includedir}/libkcal
%{_libdir}/libkcal.la
%{_libdir}/libkcal.so
%{_libdir}/libkcal_resourceremote.la
%{_libdir}/libkcal_resourceremote.so
%{_libdir}/libkholidays.la
%{_libdir}/libkholidays.so

%post -n trinity-libkcal-devel
/sbin/ldconfig

%postun -n trinity-libkcal-devel
/sbin/ldconfig

##########

%package -n libtdepim
Summary:	Trinity PIM library
Group:		Environment/Libraries
Requires:	trinity-libkcal = %{version}-%{release}

%description -n libtdepim
This is the runtime package for programs that use the libtdepim-trinity library.

%files -n libtdepim
%{tde_libdir}/plugins/designer/[kt]depimwidgets.la
%{tde_libdir}/plugins/designer/[kt]depimwidgets.so
%{tde_libdir}/plugins/designer/kpartsdesignerplugin.la
%{tde_libdir}/plugins/designer/kpartsdesignerplugin.so
%{_libdir}/lib[kt]depim.so.1
%{_libdir}/lib[kt]depim.so.1.0.0
%{_datadir}/apps/[kt]depimwidgets
%{_datadir}/apps/lib[kt]depim
%{_datadir}/apps/[kt]depim
%{_datadir}/config.kcfg/pimemoticons.kcfg
%{_datadir}/icons/crystalsvg/22x22/actions/button_fewer.png
%{_datadir}/icons/crystalsvg/22x22/actions/button_more.png

%post -n libtdepim
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig

%postun -n libtdepim
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig

##########

%package -n libtdepim-devel
Summary:	Trinity PIM library [development]
Group:		Development/Libraries
Requires:	libtdepim = %{version}-%{release}
Requires:	trinity-kdelibs-devel

%description -n libtdepim-devel
This is the development package which contains the headers for the libtdepim-trinity
library.

%files -n libtdepim-devel
%{tde_includedir}/[kt]depimmacros.h
%{_libdir}/lib[kt]depim.la
%{_libdir}/lib[kt]depim.so

%post -n libtdepim-devel
/sbin/ldconfig

%postun -n libtdepim-devel
/sbin/ldconfig

##########

%package -n trinity-libkgantt
Summary:	Trinity gantt charting library
Group:		Environment/Libraries

%description -n trinity-libkgantt
This is the runtime package for programs that use the libkgantt-trinity library.

%files -n trinity-libkgantt
%{_libdir}/libkgantt.so.0
%{_libdir}/libkgantt.so.0.0.2
%{_datadir}/apps/kgantt

%post -n trinity-libkgantt
/sbin/ldconfig

%postun -n trinity-libkgantt
/sbin/ldconfig

##########

%package -n trinity-libkgantt-devel
Summary:	Trinity gantt charting library [development]
Group:		Development/Libraries
Requires:	trinity-libkgantt = %{version}-%{release}
Requires:	libtdepim-devel = %{version}-%{release}

%description -n trinity-libkgantt-devel
This is the development package which contains the headers for the libkgantt-trinity
library.

%files -n trinity-libkgantt-devel
%{tde_includedir}/kgantt
%{_libdir}/libkgantt.la
%{_libdir}/libkgantt.so

%post -n trinity-libkgantt-devel
/sbin/ldconfig

%postun -n trinity-libkgantt-devel
/sbin/ldconfig

##########

%package -n trinity-libkleopatra
Summary:	TDE GnuPG interface libraries
Group:		Environment/Libraries
Requires:	gnupg

%description -n trinity-libkleopatra
This library is used by several TDE applications to interface to the
GnuPG program.

This is the runtime package for programs that use the libkleopatra-trinity library.

%files -n trinity-libkleopatra
%{_datadir}/config/libkleopatrarc
%{_libdir}/libgpgme++.so.0
%{_libdir}/libgpgme++.so.0.4.0
%{_libdir}/libkleopatra.so.1
%{_libdir}/libkleopatra.so.1.0.0
%{_libdir}/libkpgp.so.2
%{_libdir}/libkpgp.so.2.2.0
%{_libdir}/libqgpgme.so.0
%{_libdir}/libqgpgme.so.0.0.0
%{_datadir}/apps/kconf_update/kpgp-3.1-upgrade-address-data.pl
%{_datadir}/apps/kconf_update/kpgp.upd
%{_datadir}/apps/libkleopatra
%{_datadir}/icons/crystalsvg/16x16/apps/gpg.png
%{_datadir}/icons/crystalsvg/16x16/apps/gpgsm.png
%{_datadir}/icons/crystalsvg/22x22/apps/gpg.png
%{_datadir}/icons/crystalsvg/22x22/apps/gpgsm.png
%{_datadir}/icons/crystalsvg/32x32/apps/gpg.png
%{_datadir}/icons/crystalsvg/32x32/apps/gpgsm.png

%post -n trinity-libkleopatra
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig

%postun -n trinity-libkleopatra
for f in crystalsvg ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
/sbin/ldconfig

##########

%package -n trinity-libkleopatra-devel
Summary:	Trinity GnuPG interface libraries [development]
Group:		Development/Libraries
Requires:	trinity-libkleopatra = %{version}-%{release}
Requires:	libtdepim-devel = %{version}-%{release}

%description -n trinity-libkleopatra-devel
This library is used by several KDE applications to interface to the
GnuPG program.

This is the development package which contains the headers for the
libkleopatra-trinity library.

%files -n trinity-libkleopatra-devel
%{tde_includedir}/gpgme++
%{_includedir}/gpgme++
%{tde_includedir}/kleo
%{_includedir}/kleo
%{tde_includedir}/qgpgme
%{_libdir}/libgpgme++.la
%{_libdir}/libgpgme++.so
%{_libdir}/libkleopatra.la
%{_libdir}/libkleopatra.so
%{_libdir}/libkpgp.la
%{_libdir}/libkpgp.so
%{_libdir}/libqgpgme.la
%{_libdir}/libqgpgme.so

%post -n trinity-libkleopatra-devel
/sbin/ldconfig

%postun -n trinity-libkleopatra-devel
/sbin/ldconfig

##########

%package -n trinity-libkmime
Summary:	Trinity MIME interface library
Group:		Environment/Libraries
#Conflicts:	trinity-libmimelib

%description -n trinity-libkmime
This library provides a C++ interface to MIME messages, parsing them into
an object tree.

%files -n trinity-libkmime
%{_libdir}/libkmime.so.2
%{_libdir}/libkmime.so.2.2.0

%post -n trinity-libkmime
/sbin/ldconfig

%postun -n trinity-libkmime
/sbin/ldconfig

##########

%package -n trinity-libkmime-devel
Summary:	Development files for libkmime
Group:		Development/Libraries
Requires:	trinity-libkmime = %{version}-%{release}

%description -n trinity-libkmime-devel
%{summary}

%files -n trinity-libkmime-devel
%{_libdir}/libkmime.la
%{_libdir}/libkmime.so

%post -n trinity-libkmime-devel
/sbin/ldconfig

%postun -n trinity-libkmime-devel
/sbin/ldconfig

##########

%package -n trinity-libkpimexchange
Summary:	Trinity PIM Exchange library
Group:		Environment/Libraries

%description -n trinity-libkpimexchange
This is the runtime package for programs that use the libkpimexchange-trinity
library. 

%files -n trinity-libkpimexchange
%{tde_libdir}/resourcecalendarexchange.la
%{tde_libdir}/resourcecalendarexchange.so
%{_libdir}/libkpimexchange.so.1
%{_libdir}/libkpimexchange.so.1.0.0

%post -n trinity-libkpimexchange
/sbin/ldconfig

%postun -n trinity-libkpimexchange
/sbin/ldconfig

##########

%package -n trinity-libkpimexchange-devel
Summary:	Trinity PIM Exchange library [development]
Group:		Development/Libraries
Requires:	trinity-libkpimexchange = %{version}-%{release}
Requires:	trinity-libkcal-devel = %{version}-%{release}
Requires:	libtdepim-devel = %{version}-%{release}

%description -n trinity-libkpimexchange-devel
This is the development package which contains the headers for the
libkpimexchange-trinity library.

%files -n trinity-libkpimexchange-devel
%{tde_includedir}/[kt]depim/exchangeaccount.h
%{tde_includedir}/[kt]depim/exchangeclient.h
%{_libdir}/libkpimexchange.la
%{_libdir}/libkpimexchange.so

%post -n trinity-libkpimexchange-devel
/sbin/ldconfig

%postun -n trinity-libkpimexchange-devel
/sbin/ldconfig

##########

%package -n trinity-libkpimidentities
Summary:	Trinity PIM user identity information library
Group:		Environment/Libraries

%description -n trinity-libkpimidentities
This library provides information to TDE programs about user identity,
such as email address, organization, etc.

This is the runtime package for programs that use the libkpimidentities-trinity
library.

%files -n trinity-libkpimidentities
%{_libdir}/libkpimidentities.so.1
%{_libdir}/libkpimidentities.so.1.0.0

%post -n trinity-libkpimidentities
/sbin/ldconfig

%postun -n trinity-libkpimidentities
/sbin/ldconfig

##########

%package -n trinity-libkpimidentities-devel
Summary:	Development files for libkpimidentities
Group:		Development/Libraries
Requires:	trinity-libkpimidentities = %{version}-%{release}

%description -n trinity-libkpimidentities-devel
%{summary}

%files -n trinity-libkpimidentities-devel
%{_libdir}/libkpimidentities.la
%{_libdir}/libkpimidentities.so

%post -n trinity-libkpimidentities-devel
/sbin/ldconfig

%postun -n trinity-libkpimidentities-devel
/sbin/ldconfig

##########

%package -n trinity-libksieve
Summary:	Trinity mail/news message filtering library
Group:		Environment/Libraries

%description -n trinity-libksieve
This is the runtime package for programs that use the libksieve-trinity library.

%files -n trinity-libksieve
%{_libdir}/libksieve.so.0
%{_libdir}/libksieve.so.0.0.0

%post -n trinity-libksieve
/sbin/ldconfig

%postun -n trinity-libksieve
/sbin/ldconfig

##########

%package -n trinity-libksieve-devel
Summary:	Trinity mail/news message filtering library [development]
Group:		Development/Libraries
Requires:	trinity-libksieve = %{version}-%{release}
Requires:	libtdepim-devel = %{version}-%{release}

%description -n trinity-libksieve-devel
This is the development package which contains the headers for the libksieve-trinity
library.

%files -n trinity-libksieve-devel
%{tde_includedir}/ksieve
%{_libdir}/libksieve.la
%{_libdir}/libksieve.so

%post -n trinity-libksieve-devel
/sbin/ldconfig

%postun -n trinity-libksieve-devel
/sbin/ldconfig

##########

%package -n trinity-libktnef
Summary:	Library for handling KTNEF email attachments
Group:		Environment/Libraries

%description -n trinity-libktnef
This library handles mail attachments using the TNEF format. These
attachments are usually found in mails coming from Microsoft mail
servers and embed the mail properties as well as the actual
attachments.
.
This is the runtime library for packages using the ktnef-trinity library.

%files -n trinity-libktnef
%{_libdir}/libktnef.so.1
%{_libdir}/libktnef.so.1.0.0

%post -n trinity-libktnef
/sbin/ldconfig

%postun -n trinity-libktnef
/sbin/ldconfig

##########

%package -n trinity-libktnef-devel
Summary: KTNEF handler library [development]
Group:		Development/Libraries
Requires: trinity-libktnef = %{version}-%{release}
Requires: libtdepim-devel = %{version}-%{release}

%description -n trinity-libktnef-devel
This library handles mail attachments using the TNEF format. These
attachments are usually found in mails coming from Microsoft mail
servers and embed the mail properties as well as the actual
attachments.

This is the development package which contains the headers for the
ktnef-trinity library.

%files -n trinity-libktnef-devel
%{tde_includedir}/ktnef
%{_libdir}/libktnef.la
%{_libdir}/libktnef.so

%post -n trinity-libktnef-devel
/sbin/ldconfig

%postun -n trinity-libktnef-devel
/sbin/ldconfig

##########

%package -n trinity-libmimelib
Summary:	Trinity mime library
Group:		Environment/Libraries

%description -n trinity-libmimelib
This library is used by several Trinity applications to handle mime types.

This is the runtime package for programs that use the libmimelib-trinity library.

%files -n trinity-libmimelib
%{_libdir}/libmimelib.so.1
%{_libdir}/libmimelib.so.1.0.1

%post -n trinity-libmimelib
/sbin/ldconfig

%postun -n trinity-libmimelib
/sbin/ldconfig

##########

%package -n trinity-libmimelib-devel
Summary:	Trinity mime library [development]
Group:		Development/Libraries
Requires:	trinity-libmimelib = %{version}-%{release}

%description -n trinity-libmimelib-devel
This library is used by several KDE applications to handle mime types.

This is the development package which contains the headers for the
libmimelib library.

%files -n trinity-libmimelib-devel
%{tde_includedir}/mimelib
%{_libdir}/libmimelib.la
%{_libdir}/libmimelib.so

%post -n trinity-libmimelib-devel
/sbin/ldconfig

%postun -n trinity-libmimelib-devel
/sbin/ldconfig

##########

%package -n trinity-kmobile
Summary:	Synchronize and manage mobile phone with your PC.
Group:		Applications/Communications

%description -n trinity-kmobile
KMobileTools is a nice TDE-based application that allows to synchronize 
and manage mobile phones with your PC. It handles full SMS control, 
dialing calls, phonebook, and phone status monitoring.

%files -n trinity-kmobile
%{_bindir}/kmobile
%{_datadir}/icons/default.kde/32x32/devices/mobile_camera.png
%{_datadir}/icons/default.kde/32x32/devices/mobile_musicplayer.png
%{_datadir}/icons/default.kde/32x32/devices/mobile_organizer.png
%{_datadir}/icons/default.kde/32x32/devices/mobile_phone.png
%{_datadir}/icons/default.kde/32x32/devices/mobile_unknown.png
%{_datadir}/icons/hicolor/*/apps/kmobile.png
%{_datadir}/services/libkmobile_digicam.desktop
%{_datadir}/services/libkmobile_gammu.desktop
%{_datadir}/services/libkmobile_skeleton.desktop
%{_datadir}/servicetypes/libkmobile.desktop
%{_datadir}/apps/kmobile/kmobileui.rc
%{tde_appdir}/kmobile.desktop
%{tde_libdir}/libkmobile_skeleton.la
%{tde_libdir}/libkmobile_skeleton.so
%{_libdir}/libkmobileclient.la
%{_libdir}/libkmobileclient.so
%{_libdir}/libkmobiledevice.la
%{_libdir}/libkmobiledevice.so

%post -n trinity-kmobile
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun -n trinity-kmobile
for f in hicolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

##########

%package cmake
Summary:	CMAKE files and macros for tdepim.
Group:		Development/Libraries

%description cmake
%{summary}

%files cmake
%{_datadir}/cmake

##########

%prep
%setup -q -n kdepim
%patch1 -p1 -b .gcc47
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1 -b .addquotes
%patch10 -p1 -b .segv
%patch11 -p1


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"
export LD_LIBRARY_PATH="%{_libdir}"

%__mkdir build
cd build
%cmake \
  -DWITH_ARTS=ON \
  -DWITH_SASL=ON \
  -DWITH_NEWDISTRLISTS=ON  \
%if 0%{?with_gnokii}
  -DWITH_GNOKII=ON \
%else
  -DWITH_GNOKII=OFF \
%endif
  -DWITH_EXCHANGE=ON \
  -DWITH_EGROUPWARE=ON \
  -DWITH_KOLAB=ON \
  -DWITH_SLOX=ON \
  -DWITH_GROUPWISE=ON \
  -DWITH_FEATUREPLAN=ON \
  -DWITH_GROUPDAV=ON \
  -DWITH_BIRTHDAYS=ON \
  -DWITH_NEWEXCHANGE=ON \
  -DWITH_SCALIX=ON \
  -DWITH_CALDAV=ON \
  -DWITH_CARDDAV=ON \
  -DWITH_INDEXLIB=ON \
%if %{?with_kitchensync}
  -DBUILD_KITCHENSYNC=ON \
%endif
  -DBUILD_ALL=ON \
  ..

%__make  %{?_smp_mflags}

%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

%clean
%__rm -rf %{?buildroot}


%changelog
* Sat Jun 16 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-6
- Rename 'kdepim' to 'tdepim'
- Add 'Requires: trinity-kdebase-pim-ioslaves' to add POP3 support to kmail
- Split into several packages
- Update kalarmd icon reference, which does not exist, to kalarm. [Commit #228ad1c6]

* Sun May 27 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-5
- Fix KMail counting of unread messages in the system tray icon [Commit #40c435e5]
- Fix knotes not appearing on the desktop when a session is restored. [Bug #987] [Commit #533f494f]
- Fix knotes to not close notes during saving session. [Bug #987] [Commit #c48253af]
- Fix linear alphabet string errors [Bug 635] [Commit #80bc593e]
- Fix infinite loop on IMAP4 authentication failure [Bug #1007]

* Wed Apr 25 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Fix compilation with GCC 4.7 [Bug #958]
- Reverse patch from GIT hash 33e649c9. [Bug #406] [Commit #2d5f15c8]
- Fix kmail composer crash [Bug #953]

* Sun Nov 27 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Add missing files '*.la'

* Fri Nov 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Updates BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Mon Sep 05 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-0
- Import to GIT
