# Default version for this component
%define kdecomp kdiff3
%define version 0.9.91
%define release 4

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
Summary:	KDiff3 is a utility for comparing and/or merging two or three text files or directories.
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

# [kdiff3] Rename old tq methods that no longer need a unique name [Commit #c7e29c46]
Patch0:		bp000-c7e29c46.diff
# [kdiff3] Remove additional unneeded tq method conversions [Commit #9b57232f]
Patch1:		bp001-9b57232f.diff
# [kdiff3] Rename obsolete tq methods to standard names [Commit #d654b107]
Patch2:		bp002-d654b107.diff

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils

%description
Shows the differences line by line and character by character (!).
Provides an automatic merge-facility and
an integrated editor for comfortable solving of merge-conflicts.
Supports KIO on TDE (allows accessing ftp, sftp, fish, smb etc.).
Unicode & UTF-8 support


%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt \
    --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%clean
%__rm -rf %{buildroot}


%post
for f in hicolor locolor; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done

%postun
for f in hicolor locolor; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/*
%{_datadir}/apps/*/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*
%{_datadir}/locale/*/*/*.mo
%{tde_docdir}/HTML/*/*
%{_datadir}/services/*.desktop
%{tde_libdir}/*.so
%{_datadir}/applnk/Development/*.desktop
%{_datadir}/applnk/.hidden/*.desktop
%{_mandir}/man*/*

%{tde_libdir}/*.la

%Changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.91-4
- Rebuilt for Fedora 17
- Fix HTML directory location
- Fix post and postun
- Rename old tq methods that no longer need a unique name [Commit #c7e29c46]
- Remove additional unneeded tq method conversions [Commit #9b57232f]
- Rename obsolete tq methods to standard names [Commit #d654b107]

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.91-3
- Rebuilt for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15

* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.91-2
- Import to GIT

* Wed Aug 24 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.91-1
- Correct macro to install under "/opt", if desired

* Sun Aug 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.91-0
- Initial build for RHEL 6.0

