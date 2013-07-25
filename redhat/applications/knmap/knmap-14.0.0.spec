# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# Default version for this component
%define tde_pkg knmap
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
Version:        2.1
Release:		%{?!preversion:2}%{?preversion:1_%{preversion}}%{?dist}%{?_variant}
Summary:        An NMAP frontend for TDE

Group:          Applications/Internet
License:        GPLv2+
URL:            http://sourceforge.net/projects/knmap/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz


BuildRequires:	desktop-file-utils
BuildRequires:	trinity-tqt3-devel >= 3.5.0
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	gettext

Requires:		nmap

%description
Knmap is a TDE-based interface to the 'nmap' facility.

The main Knmap window provides for the entry of nmap options and the
display of nmap-generated output.

This program is a complete re-write of one by the same name written by
Alexandre Sagala. The last version of that program was 0.9 which was
released on 2003-03-09 and targeted the KDE 2.2 and QT 2.3 environments.

Not to mention that it did not cater for the full set of 'nmap' options.
Or, perhaps, 'nmap' progressed whilst that version of Knmap languished.
 .
http://www.kde-apps.org/content/show.php?content=31108


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
	--bindir=%{tde_bindir} \
	--libdir=%{tde_libdir} \
	--datadir=%{tde_datadir} \
	--includedir=%{tde_tdeincludedir} \
	--enable-closure
  
%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT


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


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{tde_bindir}/knmap
%{tde_datadir}/applnk/Utilities/knmap.desktop
%{tde_datadir}/apps/knmap/knmapui.rc
%{tde_datadir}/apps/knmap/nmap_manpage.html
%{tde_datadir}/apps/knmap/nmap_manpage.html.diff
%{tde_tdedocdir}/HTML/en/knmap/
%{tde_datadir}/icons/hicolor/16x16/apps/knmap.png
%{tde_datadir}/icons/hicolor/16x16/apps/knmapman.png
%{tde_datadir}/icons/hicolor/16x16/apps/localman.png
%{tde_datadir}/icons/hicolor/16x16/apps/manpage.png
%{tde_datadir}/icons/hicolor/16x16/apps/manstylesheet.png
%{tde_datadir}/icons/hicolor/16x16/apps/profilecopy.png
%{tde_datadir}/icons/hicolor/16x16/apps/profiledelete.png
%{tde_datadir}/icons/hicolor/16x16/apps/profileload.png
%{tde_datadir}/icons/hicolor/16x16/apps/profilerename.png
%{tde_datadir}/icons/hicolor/16x16/apps/profilesave.png
%{tde_datadir}/icons/hicolor/16x16/apps/profilesaveas.png
%{tde_datadir}/icons/hicolor/16x16/apps/scanclose.png
%{tde_datadir}/icons/hicolor/16x16/apps/scanduplicate.png
%{tde_datadir}/icons/hicolor/16x16/apps/scannew.png
%{tde_datadir}/icons/hicolor/16x16/apps/scanrename.png
%{tde_datadir}/icons/hicolor/16x16/apps/zoomcustom.png
%{tde_datadir}/icons/hicolor/16x16/apps/zoomin.png
%{tde_datadir}/icons/hicolor/16x16/apps/zoomout.png
%{tde_datadir}/icons/hicolor/32x32/apps/knmap.png
%{tde_datadir}/icons/hicolor/32x32/apps/knmapman.png
%{tde_datadir}/icons/hicolor/32x32/apps/localman.png
%{tde_datadir}/icons/hicolor/32x32/apps/manpage.png
%{tde_datadir}/icons/hicolor/32x32/apps/manstylesheet.png
%{tde_datadir}/icons/hicolor/32x32/apps/profilecopy.png
%{tde_datadir}/icons/hicolor/32x32/apps/profiledelete.png
%{tde_datadir}/icons/hicolor/32x32/apps/profileload.png
%{tde_datadir}/icons/hicolor/32x32/apps/profilerename.png
%{tde_datadir}/icons/hicolor/32x32/apps/profilesave.png
%{tde_datadir}/icons/hicolor/32x32/apps/profilesaveas.png
%{tde_datadir}/icons/hicolor/32x32/apps/scanclose.png
%{tde_datadir}/icons/hicolor/32x32/apps/scanduplicate.png
%{tde_datadir}/icons/hicolor/32x32/apps/scannew.png
%{tde_datadir}/icons/hicolor/32x32/apps/scanrename.png
%{tde_datadir}/icons/hicolor/32x32/apps/zoomcustom.png
%{tde_datadir}/icons/hicolor/32x32/apps/zoomin.png
%{tde_datadir}/icons/hicolor/32x32/apps/zoomout.png


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2.1-2
- Initial release for TDE 14.0.0

* Mon Apr 08 2013 Francois Andriot <francois.andriot@free.fr> - 2.1-1
- Initial release for TDE 3.5.13.2
