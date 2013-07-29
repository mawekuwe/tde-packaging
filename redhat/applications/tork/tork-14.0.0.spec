# Default version for this component
%define tde_pkg tork
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

Name:           trinity-tork
Version:        0.33
Release:		%{?!preversion:2}%{?preversion:1_%{preversion}}%{?dist}%{?_variant}
Summary:        Anonymity Manager for TDE

Group:          Applications/Internet
License:        GPLv2+
URL:            sourceforge.net/projects/tolrk/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdepim-devel >= %{tde_version}
BuildRequires:	torsocks

%description
TorK is an Anonymity Manager for the TDE Desktop. Browse anonymously on 
Konqueror/Firefox/Opera. Send anonymous email via the MixMinion network.
Use ssh/irc/IM anonymously. Control and monitor your anonymous traffic 
on the Tor network.

%if 0%{?suse_version}
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

# NOTICE: --enable-final causes FTBFS !
%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --mandir=%{tde_mandir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --disable-final \
  --enable-new-ldflags \
  --enable-closure \
  --disable-rpath \
  --enable-gcc-hidden-visibility
  
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
%doc AUTHORS COPYING README TODO ChangeLog USINGTORK
%{tde_bindir}/tork
%{tde_bindir}/torkarkollon
%{tde_tdeappdir}/tork.desktop
%{tde_datadir}/apps/konqueror/servicemenus/tork_downloadwithfirefox.desktop
%{tde_datadir}/apps/konqueror/servicemenus/tork_downloadwithkonqueror.desktop
%{tde_datadir}/apps/konqueror/servicemenus/tork_downloadwithopera.desktop
%{tde_datadir}/apps/tork/
%{tde_datadir}/config.kcfg/torkconfig.kcfg
%{tde_tdedocdir}/HTML/en/tork/
%{tde_datadir}/icons/hicolor/*/actions/tork.png
%{tde_datadir}/icons/hicolor/*/apps/tork.png
%{tde_datadir}/menu/tork
%{tde_datadir}/pixmaps/tork.xpm
%{tde_mandir}/man1/tork.1*
%{tde_mandir}/man1/torkarkollon.1*


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.33-2
- Initial release for TDE 14.0.0

* Thu Apr 25 2013 Francois Andriot <francois.andriot@free.fr> - 0.33-1
- Initial release for TDE 3.5.13.2
