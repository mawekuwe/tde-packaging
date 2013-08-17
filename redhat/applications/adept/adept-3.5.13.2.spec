# Default version for this component
%define tde_pkg adept
%define tde_version 3.5.13.2

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
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		Package management suite for Trinity
Version:		2.1.3
Release:		%{?!preversion:2}%{?preversion:1_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://lpnotfr.free.fr/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

Requires:		%{name}-manager = %{version}-%{release}
Requires:		%{name}-installer = %{version}-%{release}
Requires:		%{name}-updater = %{version}-%{release}
Requires:		%{name}-notifier = %{version}-%{release}
Requires:		%{name}-batch = %{version}-%{release}


%description
These packages belong to the adept suite:
 * adept-manager - package manager
 * adept-installer - application manager
 * adept-updater - system upgrade wizard
 * adept-notifier - systray notification of available updates


%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG ChangeLog COPYING

##########

%package common
Requires:		trinity-konsole
Summary:		Package manager for Trinity -- common files

%description common
Icons and other common files for all adept components.

##########

%package manager
Requires:		%{name}-common = %{version}-%{release}
Summary:		package manager for Trinity
 
%description manager
Adept Manager is a graphical user interface for package management.

Besides these basic functions the following features are provided:
 * Search and filter the list of available packages (also using debtags)
 * Perform smart system upgrades
 * Edit the list of used repositories (sources.list)
 * Configure packages through the debconf system

Please also install libtqt-perl if you want the TDE Debconf frontend
to function.

##########

%package installer
Requires:		%{name}-common = %{version}-%{release}
Summary:		simple user interface for application management (for Trinity)

%description installer
Adept Installer presents a list of applications available through the
Advanced Package Tool (APT). An application is considered a package
that contains a .desktop file for use with TDE, GNOME or other
desktop environment.

##########

%package updater
Requires:		%{name}-common = %{version}-%{release}
Summary:		system update tool for Trinity

%description updater
Adept Updater provides a simple wizard-style user interface to system
upgrades. It uses same algorithms as apt-get dist-upgrade.

##########

%package notifier
Requires:		%{name}-common = %{version}-%{release}
Requires:		%{name}-updater = %{version}-%{release}
Summary:		System tray notifier of available system updates
 
%description notifier
Adept Notifier provides a system tray icon notifying the user of
available updates.  It will run Adept Updater for the user when
clicked.

##########

%package batch
Requires:		%{name}-manager = %{version}-%{release}
Summary:		command line install for Adept

%description batch
Adept Batch lets you install packages with Adept from the
command line.  It is intended for shell scripts and being run
by external applications.

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --disable-rpath \
  --enable-closure

%__make %{?_smp_mflags} -C adept


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}




%changelog
* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 2.1.3-1
- Initial release for TDE 3.5.13.2

