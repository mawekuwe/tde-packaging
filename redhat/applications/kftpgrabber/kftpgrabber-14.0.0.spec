# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# Default version for this component
%define tde_pkg kftpgrabber
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
Version:        0.8.1
Release:		%{?!preversion:2}%{?preversion:1_%{preversion}}%{?dist}%{?_variant}
Summary:        A FTP client for TDE.

Group:          Applications/Internet
License:        GPLv2+
URL:            http://www.kftp.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz


BuildRequires:	desktop-file-utils
BuildRequires:	trinity-tqt3-devel >= 3.5.0
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

%description

%package devel
Summary:  	Development files for %{name}
Group: 		Development/Libraries
Requires: 	%{name} = %{version}-%{release}

%description devel
%{summary}


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTDIR
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
	--prefix=%{tde_prefix} \
	--exec-prefix=%{tde_prefix} \
	--disable-dependency-tracking \
	--disable-rpath \
	--bindir=%{tde_bindir} \
	--libdir=%{tde_libdir} \
	--datadir=%{tde_datadir} \
	--includedir=%{tde_tdeincludedir} \
	--disable-static \
	--enable-closure
  
%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{tde_pkg}


%clean
%__rm -rf $RPM_BUILD_ROOT


%post
for i in hicolor ; do
 touch --no-create %{tde_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{tde_datadir}/icons/$i 2>/dev/null || :
done


%postun
for i in hicolor ; do
 touch --no-create %{tde_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{tde_datadir}/icons/$i 2>/dev/null || :
done


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{tde_bindir}/kftpgrabber
%{tde_libdir}/libkftpinterfaces.so.0
%{tde_libdir}/libkftpinterfaces.so.0.0.0
%{tde_tdelibdir}/kftpimportplugin_filezilla3.la
%{tde_tdelibdir}/kftpimportplugin_filezilla3.so
%{tde_tdelibdir}/kftpimportplugin_gftp.la
%{tde_tdelibdir}/kftpimportplugin_gftp.so
%{tde_tdelibdir}/kftpimportplugin_kftp.la
%{tde_tdelibdir}/kftpimportplugin_kftp.so
%{tde_tdelibdir}/kftpimportplugin_ncftp.la
%{tde_tdelibdir}/kftpimportplugin_ncftp.so
%{tde_tdeappdir}/kftpgrabber.desktop
%{tde_datadir}/apps/kftpgrabber/commands.xml
%{tde_datadir}/apps/kftpgrabber/kftpgrabber-bi-wizard.png
%{tde_datadir}/apps/kftpgrabber/kftpgrabber-logo.png
%{tde_datadir}/apps/kftpgrabber/kftpgrabberui.rc
%{tde_datadir}/config.kcfg/kftpgrabber.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kftpgrabber.png
%{tde_datadir}/services/kftpimportplugin_filezilla3.desktop
%{tde_datadir}/services/kftpimportplugin_gftp.desktop
%{tde_datadir}/services/kftpimportplugin_kftp.desktop
%{tde_datadir}/services/kftpimportplugin_ncftp.desktop
%{tde_datadir}/servicetypes/kftpbookmarkimportplugin.desktop

%files devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/kftpgrabber/kftpbookmarkimportplugin.h
%{tde_libdir}/libkftpinterfaces.la
%{tde_libdir}/libkftpinterfaces.so


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.8.1-2
- Initial release for TDE 14.0.0

* Mon Apr 08 2013 Francois Andriot <francois.andriot@free.fr> - 0.8.1-1
- Initial release for TDE 3.5.13.2
