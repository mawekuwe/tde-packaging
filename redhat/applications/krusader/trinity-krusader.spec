# Default version for this component
%define kdecomp krusader
%define version 1.90.0
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%define _mandir %{_datadir}/man
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	twin-panel (commander-style) file manager for KDE (and other desktops)
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [krusader] GCC 4.7 fixes. [Commit #fdf6d340]
Patch1:		krusader-3.5.13-fix_gcc47_compilation.patch

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils

BuildRequires:	trinity-kdebindings-devel

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


%prep
%setup -q -n applications/%{kdecomp}
%patch1 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt:%{tde_includedir}

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{kdecomp}

%clean
%__rm -rf %{buildroot}


%post
for f in crystalsvg locolor ; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done

%postun
for f in crystalsvg locolor ; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING FAQ README TODO
%{_bindir}/krusader
%{tde_libdir}/kio_krarc.la
%{tde_libdir}/kio_krarc.so
%{tde_libdir}/kio_virt.la
%{tde_libdir}/kio_virt.so
%{_datadir}/applications/kde/krusader.desktop
%{_datadir}/applications/kde/krusader_root-mode.desktop
%{_datadir}/apps/krusader
%{tde_docdir}/HTML/en/krusader
%{tde_docdir}/HTML/ru/krusader
%{_datadir}/icons/crystalsvg/*/apps/*.png
%{_datadir}/icons/locolor/*/apps/*.png
%{_datadir}/services/krarc.protocol
%{_datadir}/services/virt.protocol
%{_mandir}/man1/krusader.1


%Changelog
* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 1.90.0-2
- Rebuild for Fedora 17
- GCC 4.7 fixes. [Commit #fdf6d340]

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 1.90.0-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

