# Default version for this component
%define tde_pkg konversation
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
Summary:		user friendly Internet Relay Chat (IRC) client for TDE [Trinity]
Version:		1.1
Release:		%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

BuildRequires:	libxslt-devel
%if 0%{?suse_version}
BuildRequires:	docbook-xsl-stylesheets
%else
BuildRequires:	docbook-style-xsl
%endif

%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}xi-devel
%endif
%if 0%{?rhel} >= 5|| 0%{?fedora} || 0%{?suse_version} >= 1220
BuildRequires:	libXi-devel
%endif
%if 0%{?suse_version} == 1140
BuildRequires:	libXi6-devel
%endif

%description
Konversation is a client for the Internet Relay Chat (IRC) protocol.
It is easy to use and well-suited for novice IRC users, but novice
and experienced users alike will appreciate its many features:

 * Standard IRC features
 * Easy to use graphical interface
 * Multiple server and channel tabs in a single window
 * IRC color support
 * Pattern-based message highlighting and OnScreen Display
 * Multiple identities for different servers
 * Multi-language scripting support (with DCOP)
 * Customizable command aliases
 * NickServ-aware log-on (for registered nicknames)
 * Smart logging
 * Traditional or enhanced-shell-style nick completion
 * DCC file transfer with resume support



%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; source /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/konversation
%{tde_tdeappdir}/konversation.desktop
%{tde_datadir}/apps/kconf_update/konversation-0.19-appearance.pl
%{tde_datadir}/apps/kconf_update/konversation-0.19-colorcodes.pl
%{tde_datadir}/apps/kconf_update/konversation-0.19-colors.pl
%{tde_datadir}/apps/kconf_update/konversation-0.19-custombrowser.pl
%{tde_datadir}/apps/kconf_update/konversation-0.19-notifylists.pl
%{tde_datadir}/apps/kconf_update/konversation-0.19-sortorder.pl
%{tde_datadir}/apps/kconf_update/konversation-0.19-tabplacement.pl
%{tde_datadir}/apps/kconf_update/konversation-0.20-customfonts.pl
%{tde_datadir}/apps/kconf_update/konversation-0.20-quickbuttons.pl
%{tde_datadir}/apps/kconf_update/konversation.upd
%{tde_datadir}/apps/konversation/
%{tde_datadir}/config.kcfg/konversation.kcfg
%{tde_datadir}/services/konvirc.protocol
%{tde_datadir}/services/konvirc6.protocol
%{tde_tdedocdir}/HTML/*/konversation/
%{tde_datadir}/icons/crystalsvg/*/actions/kimproxyaway.png
%{tde_datadir}/icons/crystalsvg/*/actions/kimproxyoffline.png
%{tde_datadir}/icons/crystalsvg/*/actions/kimproxyonline.png
%{tde_datadir}/icons/crystalsvg/*/actions/char.png
%{tde_datadir}/icons/crystalsvg/*/actions/konv_message.png
%{tde_datadir}/icons/crystalsvg/scalable/actions/kimproxyaway.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/kimproxyoffline.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/kimproxyonline.svgz
%{tde_datadir}/icons/crystalsvg/scalable/actions/konv_message.svgz
%{tde_datadir}/icons/hicolor/*/apps/konversation.png
%{tde_datadir}/icons/hicolor/scalable/apps/konversation.svgz


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1.1-5
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 1.1-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 1.1-3
- Initial release for TDE 3.5.13.1

* Sat May 05 2012 Francois Andriot <francois.andriot@free.fr> - 1.1-2
- Rebuild for Fedora 17
- Fix HTML directory location
- Rename old tq methods that no longer need a unique name [Commit #01f5ea83]
- Remove additional unneeded tq method conversions [Commit #efdae4e7]
- Rename obsolete tq methods to standard names [Commit #c64099e5]
- Fix linear alphabet string errors [Commit #440010aa]
- Fix inadvertent "TQ" changes. [Commit #ca3d6cef]

* Mon Nov 07 2011 Francois Andriot <francois.andriot@free.fr> - 1.1-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

