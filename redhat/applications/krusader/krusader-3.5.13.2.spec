# Default version for this component
%define tde_pkg krusader
%define tde_version 3.5.13.2

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

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		twin-panel (commander-style) file manager for TDE (and other desktops)
Version:		1.90.0
Release:		%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

Patch0:			krusader-3.5.13.2-tmpvfs-ftbfs.patch

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-tdebindings-devel >= %{tde_version}


%description
Krusader is a simple, easy, powerful, twin-panel (commander-style) file
manager for TDE and other desktops, similar to Midnight Commander (C) or Total
Commander (C).

It provides all the file management features you could possibly want.

Plus: extensive archive handling, mounted filesystem support, FTP,
advanced search module, viewer/editor, directory synchronisation,
file content comparisons, powerful batch renaming and much much more.

It supports archive formats: ace, arj, bzip2, deb, iso, lha, rar, rpm, tar,
zip and 7-zip.

It handles KIOSlaves such as smb:// or fish://.

Almost completely customizable, Krusader is very user friendly, fast and looks
great on your desktop.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
%patch0 -p1 -b .ftbfs

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"

# Warning: --enable-final causes FTBFS
%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --disable-final \
  --enable-closure \
  --enable-rpath

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}

%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_appdir} > /dev/null
for f in crystalsvg locolor ; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done

%postun
update-desktop-database %{tde_appdir} > /dev/null
for f in crystalsvg locolor ; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING FAQ README TODO
%{tde_bindir}/krusader
%{tde_tdelibdir}/kio_krarc.la
%{tde_tdelibdir}/kio_krarc.so
%{tde_tdelibdir}/kio_virt.la
%{tde_tdelibdir}/kio_virt.so
%{tde_tdeappdir}/krusader.desktop
%{tde_tdeappdir}/krusader_root-mode.desktop
%{tde_datadir}/apps/krusader
%{tde_tdedocdir}/HTML/en/krusader/
%lang(ru) %{tde_tdedocdir}/HTML/ru/krusader/
%{tde_datadir}/icons/crystalsvg/*/apps/*.png
%{tde_datadir}/icons/locolor/*/apps/*.png
%{tde_datadir}/services/krarc.protocol
%{tde_datadir}/services/virt.protocol
%{tde_mandir}/man1/krusader.1


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1.90.0-5
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 1.90.0-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 1.90.0-3
- Initial release for TDE 3.5.13.1

* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 1.90.0-2
- Rebuild for Fedora 17
- GCC 4.7 fixes. [Commit #fdf6d340]

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 1.90.0-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16

