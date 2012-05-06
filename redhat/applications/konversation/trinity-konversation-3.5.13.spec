# Default version for this component
%define kdecomp konversation
%define version 1.1
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	user friendly Internet Relay Chat (IRC) client for KDE [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [konversation] Rename old tq methods that no longer need a unique name [Commit #01f5ea83]
Patch0:		bp000-01f5ea83.diff
# [konversation] Remove additional unneeded tq method conversions [Commit #efdae4e7]
Patch1:		bp001-efdae4e7.diff
# [konversation] Rename obsolete tq methods to standard names [Commit #c64099e5]
Patch2:		bp002-c64099e5.diff
# [konversation] Fix linear alphabet string errors [Commit #440010aa]
Patch3:		bp003-440010aa.diff
# [konversation] Fix inadvertent "TQ" changes. [Commit #ca3d6cef]
Patch4:		96f2a488.diff
Patch5:		bp004-ca3d6cef.diff

BuildRequires: tqtinterface-devel
BuildRequires: trinity-arts-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext

BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: libXi-devel


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



%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt \
    --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}



%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/*
%{_datadir}/applications/*/*.desktop
%{_datadir}/locale/*/LC_MESSAGES/konversation.mo
%{_datadir}/config.kcfg/konversation.kcfg
%{_datadir}/services/*.protocol
#%{_datadir}/servicetypes/digikamimageplugin.desktop
%{_datadir}/apps/*/
%{tde_docdir}/HTML/*/konversation/
%{_datadir}/icons/*/*/*/*
#%{_mandir}/man*/*

%Changelog
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

