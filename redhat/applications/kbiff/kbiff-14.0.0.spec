# Default version for this component
%define tde_pkg kbiff
%define tde_version 14.0.0

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

%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:           trinity-%{tde_pkg}
Version:        3.9
Release:		%{?!preversion:2}%{?preversion:1_%{preversion}}%{?dist}%{?_variant}
Summary:        TDE mail notification utility 

Group:          Applications/Internet
License:        GPLv2+
URL:            http://sourceforge.net/projects/knmap/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

%description
Kbiff is a "xbiff"-like mail notification utility. It has  multiple pixmaps,
session management, and GUI configuration.  It can "dock" into the TDE panel.
It can display animated gifs, play system sounds, or run arbitrary shell
command when new mail arrives. It supports mbox, maildir, mh, POP3, IMAP4, and
NNTP mailboxes.

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
	--prefix=%{tde_prefix} \
	--exec-prefix=%{tde_prefix} \
	--disable-dependency-tracking \
	--disable-rpath \
	--disable-static \
	--bindir=%{tde_bindir} \
	--libdir=%{tde_libdir} \
	--mandir=%{tde_mandir} \
	--datadir=%{tde_datadir} \
	--includedir=%{tde_tdeincludedir} 
  
%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{tde_pkg}


%clean
%__rm -rf $RPM_BUILD_ROOT


%post
for i in hicolor locolor ; do
 touch --no-create %{tde_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{tde_datadir}/icons/$i 2>/dev/null || :
done


%postun
for i in hicolor locolor ; do
 touch --no-create %{tde_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{tde_datadir}/icons/$i 2>/dev/null || :
done


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{tde_bindir}/kbiff
%{tde_libdir}/libtdeinit_kbiff.la
%{tde_libdir}/libtdeinit_kbiff.so
%{tde_tdelibdir}/kbiff.la
%{tde_tdelibdir}/kbiff.so
%{tde_datadir}/applnk/Internet/kbiff.desktop
%{tde_datadir}/apps/kbiff/
%{tde_datadir}/icons/hicolor/*/apps/kbiff.png
%{tde_datadir}/icons/locolor/*/apps/kbiff.png
%{tde_mandir}/man1/kbiff.1*
%lang(de) %{tde_tdedocdir}/HTML/de/kbiff/
%lang(en) %{tde_tdedocdir}/HTML/en/kbiff/
%lang(es) %{tde_tdedocdir}/HTML/es/kbiff/
%lang(fr) %{tde_tdedocdir}/HTML/fr/kbiff/


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 3.9-2
- Initial release for TDE 14.0.0

* Mon Apr 08 2013 Francois Andriot <francois.andriot@free.fr> - 3.9-1
- Initial release for TDE 3.5.13.2
