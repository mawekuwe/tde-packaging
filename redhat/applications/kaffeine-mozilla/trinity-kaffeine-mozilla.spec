# Default version for this component
%define kdecomp kaffeine-mozilla
%define version 0.4.3.1
%define release 2

%define _prefix /usr

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	mozilla plugin that lanches kaffeine for supported media types [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Multimedia

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# Fix 'nspr' includes location
Patch1:		kaffeine-mozilla-3.5.13-fix_nspr_include.patch

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils

BuildRequires:	libXaw-devel
BuildRequires:	nspr-devel
Requires:		trinity-kaffeine

%description
This mozilla plugin launches kaffeine, the xine-based media player for KDE,
when a page containing a supported media format is loaded.


%prep
unset QTDIR; . /etc/profile.d/qt.sh
%setup -q -n applications/%{kdecomp}
%patch1 -p1

%__cp -f "/usr/share/aclocal/libtool.m4" .
%__cp -f "/usr/share/libtool/config/ltmain.sh" .
autoreconf -fiv


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt \
    --enable-closure \
    --prefix=%{_prefix}/%{_lib}/mozilla

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
/sbin/ldconfig || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
/sbin/ldconfig || :


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%exclude %{_libdir}/mozilla/plugins/kaffeineplugin.a
%{_libdir}/mozilla/plugins/kaffeineplugin.la
%{_libdir}/mozilla/plugins/kaffeineplugin.so


%Changelog
* Thu Apr 26 2012 Francois Andriot <francois.andriot@free.fr> - 0.4.3.1-2
- Rebuild with nicer patch.

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.4.3.1.dfsg-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

