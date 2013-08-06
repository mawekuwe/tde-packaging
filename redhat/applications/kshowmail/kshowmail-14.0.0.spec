# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# Default version for this component
%define tde_pkg kshowmail
%define tde_version 14.0.0

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
Version:        3.3.1
Release:		%{?!preversion:2}%{?preversion:1_%{preversion}}%{?dist}%{?_variant}
Summary:        Look messages into your mail server.

Group:          Applications/Internet
License:        GPLv2+
URL:            http://sourceforge.net/projects/kshowmail/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tdepim-devel >= %{tde_version}

%description
Very simply kshowmail is a program that allows you to look in on your mail server,
see what is waiting, decide if it is legitimate, and delete it right off of the server if it is not.
All without dragging any messages into your computer. 

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
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-final \
  --enable-new-ldflags \
  --enable-closure \
  --enable-rpath \
  --enable-gcc-hidden-visibility
  
%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{tde_pkg}


%clean
%__rm -rf $RPM_BUILD_ROOT


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{tde_bindir}/kshowmail
%{tde_tdelibdir}/kcm_kshowmailconfigaccounts.la
%{tde_tdelibdir}/kcm_kshowmailconfigaccounts.so
%{tde_tdelibdir}/kcm_kshowmailconfigactions.la
%{tde_tdelibdir}/kcm_kshowmailconfigactions.so
%{tde_tdelibdir}/kcm_kshowmailconfigdisplay.la
%{tde_tdelibdir}/kcm_kshowmailconfigdisplay.so
%{tde_tdelibdir}/kcm_kshowmailconfigfilter.la
%{tde_tdelibdir}/kcm_kshowmailconfigfilter.so
%{tde_tdelibdir}/kcm_kshowmailconfiggeneral.la
%{tde_tdelibdir}/kcm_kshowmailconfiggeneral.so
%{tde_tdelibdir}/kcm_kshowmailconfiglog.la
%{tde_tdelibdir}/kcm_kshowmailconfiglog.so
%{tde_tdelibdir}/kcm_kshowmailconfigspamcheck.la
%{tde_tdelibdir}/kcm_kshowmailconfigspamcheck.so
%{tde_datadir}/applnk/Internet/kshowmail.desktop
%{tde_datadir}/apps/kshowmail/kshowmailui.rc
%{tde_datadir}/apps/kshowmail/pics/eraser.png
%{tde_datadir}/apps/kshowmail/pics/kshowmail.png
%{tde_datadir}/apps/kshowmail/pics/kshowmail24.png
%{tde_datadir}/apps/kshowmail/pics/letter-closed.png
%{tde_datadir}/apps/kshowmail/pics/letter-open.png
%{tde_datadir}/apps/kshowmail/pics/ok.png
%{tde_datadir}/apps/kshowmail/pics/tool.png
%{tde_datadir}/apps/kshowmail/sounds/neuepost.wav
%{tde_datadir}/apps/kshowmail/sounds/newmail.wav
%{tde_datadir}/services/kshowmailconfigaccounts.desktop
%{tde_datadir}/services/kshowmailconfigactions.desktop
%{tde_datadir}/services/kshowmailconfigdisplay.desktop
%{tde_datadir}/services/kshowmailconfigfilter.desktop
%{tde_datadir}/services/kshowmailconfiggeneral.desktop
%{tde_datadir}/services/kshowmailconfiglog.desktop
%{tde_datadir}/services/kshowmailconfigspamcheck.desktop
%lang(de) %{tde_tdedocdir}/HTML/de/kshowmail/
%lang(en) %{tde_tdedocdir}/HTML/en/kshowmail/
%lang(es) %{tde_tdedocdir}/HTML/es/kshowmail/
%lang(fr) %{tde_tdedocdir}/HTML/fr/kshowmail/
%lang(hu) %{tde_tdedocdir}/HTML/hu/kshowmail/
%lang(it) %{tde_tdedocdir}/HTML/it/kshowmail/
%lang(ru) %{tde_tdedocdir}/HTML/ru/kshowmail/
%lang(sv) %{tde_tdedocdir}/HTML/sv/kshowmail/


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 3.3.1-2
- Initial release for TDE 14.0.0

* Thu Apr 25 2013 Francois Andriot <francois.andriot@free.fr> - 3.3.1-1
- Initial release for TDE 3.5.13.2
