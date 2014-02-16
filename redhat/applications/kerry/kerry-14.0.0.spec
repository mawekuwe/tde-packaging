# Default version for this component
%define tde_pkg kerry
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
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		a TDE frontend for the Beagle desktop search daemon [Trinity]
Version:		0.2.1
Release:		%{?!preversion:4}%{?preversion:3_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://en.opensuse.org/Kerry

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:		kerry.1.docbook


BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext
BuildRequires:	libbeagle-devel >= 0.3.0


%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	docbook2x
%else
BuildRequires:	docbook2X
%endif

%description
Kerry is a Trinity frontend for the Beagle desktop search daemon.

A program for indexing and searching user's data. At the moment, it can index
filesystems, chat logs, mail and data, RSS and other.


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
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility

%__make %{?_smp_mflags}



%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

#%__install -D -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/kerry.1.docbook
#docbook2man %{buildroot}%{_mandir}/man1/kerry.1.docbook

%find_lang %{tde_pkg}

%clean
%__rm -rf %{buildroot}


%post
/sbin/ldconfig || :
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
update-desktop-database %{tde_appdir} &> /dev/null

%postun
/sbin/ldconfig || :
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
update-desktop-database %{tde_appdir} &> /dev/null


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_datadir}/locale/*/LC_MESSAGES/kcmbeagle.mo
%{tde_bindir}/beagled-shutdown
%{tde_bindir}/kerry
%{tde_libdir}/libtdeinit_kerry.la
%{tde_libdir}/libtdeinit_kerry.so
%{tde_tdelibdir}/kcm_beagle.la
%{tde_tdelibdir}/kcm_beagle.so
%{tde_tdelibdir}/kerry.la
%{tde_tdelibdir}/kerry.so
%{tde_tdeappdir}/kcmbeagle.desktop
%{tde_tdeappdir}/kerry.desktop
%{tde_datadir}/applnk/.hidden/kcmkerry.desktop
%{tde_datadir}/apps/kerry/search-running.mng
%{tde_datadir}/autostart/beagled.desktop
%{tde_datadir}/autostart/kerry.autostart.desktop
%{tde_datadir}/icons/hicolor/*/*/*


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.2.1-4
- Initial release for TDE 14.0.0

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.2.1-3
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.2.1-2
- Initial release for TDE 3.5.13.1

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 0.2.1-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
