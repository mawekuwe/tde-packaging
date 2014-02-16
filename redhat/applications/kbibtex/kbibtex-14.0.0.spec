# Default version for this component
%define tde_pkg kbibtex
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

Name:           trinity-kbibtex
Version:        0.2.3
Release:		%{?!preversion:2}%{?preversion:1_%{preversion}}%{?dist}%{?_variant}
Summary:        A BibTeX editor for TDE

Group:          Applications/Internet
License:        GPLv2+
URL:            http://www.unix-ag.uni-kl.de/~fischer/kbibtex/download.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

%description
KBibTeX is a BibTeX editor for TDE to edit bibliographies used with LaTeX.
KBibTeX is released under the GNU Public License (GPL) version 2 or any later version.

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

# Warning: --enable-final causes FTBFS
%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --disable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility
  
%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

# Useless files ..
%__rm -f %{?buildroot}%{tde_tdelibdir}/*.a

%find_lang %{tde_pkg}


%clean
%__rm -rf $RPM_BUILD_ROOT


%post
for i in hicolor ; do
 touch --no-create %{tde_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{tde_datadir}/icons/$i 2>/dev/null || :
done
update-desktop-database %{tde_tdeappdir} > /dev/null

%postun
for i in hicolor ; do
 touch --no-create %{tde_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{tde_datadir}/icons/$i 2>/dev/null || :
done
update-desktop-database %{tde_tdeappdir} > /dev/null


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING NEWS README TODO ChangeLog
%{tde_bindir}/kbibtex
%{tde_tdelibdir}/libkbibtexpart.la
%{tde_tdelibdir}/libkbibtexpart.so
%{tde_tdeappdir}/kbibtex.desktop
%{tde_datadir}/apps/kbibtex/
%{tde_datadir}/apps/kbibtexpart/kbibtex_part.rc
%{tde_datadir}/apps/kbibtexpart/xslt/MARC21slim2MODS3.xsl
%{tde_datadir}/apps/kbibtexpart/xslt/MARC21slimUtils.xsl
%{tde_datadir}/apps/kbibtexpart/xslt/UNIMARC2MODS3.xsl
%{tde_datadir}/apps/kbibtexpart/xslt/html.xsl
%{tde_datadir}/icons/hicolor/*/apps/kbibtex.png
%{tde_datadir}/services/kbibtex_part.desktop
%{tde_mandir}/man1/kbibtex.1*
%{tde_tdedocdir}/HTML/en/kbibtex/


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.2.3-2
- Initial release for TDE 14.0.0

* Fri Mar 29 2013 Francois Andriot <francois.andriot@free.fr> - 0.2.3-1
- Initial release for TDE 3.5.13.2
