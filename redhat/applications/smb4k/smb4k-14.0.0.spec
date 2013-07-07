# Default version for this component
%define tde_pkg smb4k
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

%define _docdir %{tde_tdedocdir}


Name:			trinity-%{tde_pkg}
Summary:		A Samba (SMB) share advanced browser for Trinity
Version:		0.9.4
Release:		%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext


%description
Smb4K is a SMB (Windows) share browser for TDE. It uses the Samba software 
suite to access the SMB shares of the local network neighborhood. Its purpose
is to provide a program that's easy to use and has as many features as 
possible.

%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/smb4k
%{tde_bindir}/smb4k_cat
%{tde_bindir}/smb4k_kill
%{tde_bindir}/smb4k_mount
%{tde_bindir}/smb4k_mv
%{tde_bindir}/smb4k_umount
%{tde_libdir}/libsmb4kcore.so.2
%{tde_libdir}/libsmb4kcore.so.2.0.0
%{tde_libdir}/libsmb4kdialogs.la
%{tde_libdir}/libsmb4kdialogs.so
%{tde_tdelibdir}/konqsidebar_smb4k.la
%{tde_tdelibdir}/konqsidebar_smb4k.so
%{tde_tdelibdir}/libsmb4tdeconfigdialog.la
%{tde_tdelibdir}/libsmb4tdeconfigdialog.so
%{tde_tdelibdir}/libsmb4knetworkbrowser.la
%{tde_tdelibdir}/libsmb4knetworkbrowser.so
%{tde_tdelibdir}/libsmb4ksearchdialog.la
%{tde_tdelibdir}/libsmb4ksearchdialog.so
%{tde_tdelibdir}/libsmb4ksharesiconview.la
%{tde_tdelibdir}/libsmb4ksharesiconview.so
%{tde_tdelibdir}/libsmb4kshareslistview.la
%{tde_tdelibdir}/libsmb4kshareslistview.so
%{tde_tdeappdir}/smb4k.desktop
%{tde_datadir}/apps/konqsidebartng/add/smb4k_add.desktop
%{tde_datadir}/apps/smb4k/smb4k_shell.rc
%{tde_datadir}/apps/smb4knetworkbrowserpart/smb4knetworkbrowser_part.rc
%{tde_datadir}/apps/smb4ksharesiconviewpart/smb4ksharesiconview_part.rc
%{tde_datadir}/apps/smb4kshareslistviewpart/smb4kshareslistview_part.rc
%{tde_datadir}/config.kcfg/smb4k.kcfg
%{tde_datadir}/icons/crystalsvg/*/apps/smb4k.png
%{tde_tdedocdir}/HTML/en/smb4k/

%post
update-desktop-database %{tde_appdir} > /dev/null
touch --no-create %{tde_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/crystalsvg || :
/sbin/ldconfig || :

%postun
update-desktop-database %{tde_appdir} > /dev/null
touch --no-create %{tde_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/crystalsvg || :
/sbin/ldconfig || :

##########

%package devel
Summary:		Development files for %{name}
Group:			Development/Libraries
Requires:		%{name} = %{version}-%{release}

%description devel
%{summary}

%files devel
%{tde_tdeincludedir}/*.h
%{tde_libdir}/libsmb4kcore.la
%{tde_libdir}/libsmb4kcore.so

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

##########

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

export TDEDIR="%{tde_prefix}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  --disable-rpath \
  --enable-closure

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.9.4-5
- Initial release for TDE 14.0.0

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.9.4-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.4-3
- Initial release for TDE 3.5.13.1

* Sun Apr 08 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.4-2
- Rebuild for Fedora 17
- Fix compilation with GCC 4.7 |Commit #b4c7fd48]

* Wed Nov 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.4-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
