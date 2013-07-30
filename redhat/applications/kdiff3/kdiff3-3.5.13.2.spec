# Default version for this component
%define tde_pkg kdiff3
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
Summary:		KDiff3 is a utility for comparing and/or merging two or three text files or directories.
Version:		0.9.91
Release:		%{?!preversion:7}%{?preversion:6_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

%description
Shows the differences line by line and character by character (!).
Provides an automatic merge-facility and
an integrated editor for comfortable solving of merge-conflicts.
Supports KIO on TDE (allows accessing ftp, sftp, fish, smb etc.).
Unicode & UTF-8 support


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt3.sh
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
  --disable-rpath \
  \
  --with-extra-includes=%{tde_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Unwanted files
%__rm -rf %{?buildroot}%{tde_tdedocdir}/HTML/kdiff3/

%find_lang %{tde_pkg}

%clean
%__rm -rf %{buildroot}


%post
for f in hicolor locolor; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} &>/dev/null || :
done

%postun
for f in hicolor locolor; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} &>/dev/null || :
done


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/kdiff3
%{tde_datadir}/apps/kdiff3/
%{tde_datadir}/apps/kdiff3part/
%{tde_datadir}/icons/hicolor/*/apps/kdiff3.png
%{tde_datadir}/icons/locolor/*/apps/kdiff3.png
%{tde_tdedocdir}/HTML/*/kdiff3/
%{tde_datadir}/services/kdiff3_plugin.desktop
%{tde_datadir}/services/kdiff3part.desktop
%{tde_datadir}/applnk/Development/*.desktop
%{tde_datadir}/applnk/.hidden/kdiff3plugin.desktop
%{tde_mandir}/man*/*
%{tde_tdelibdir}/libkdiff3part.la
%{tde_tdelibdir}/libkdiff3part.so
%{tde_tdelibdir}/libkdiff3plugin.la
%{tde_tdelibdir}/libkdiff3plugin.so

%changelog
* Sun Jul 28 2013 Francois Andriot <francois.andriot@free.fr> - 0.9.91-7
- Rebuild with NDEBUG option

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.9.91-6
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.91-5
- Initial release for TDE 3.5.13.1

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
- Initial release for RHEL 6.0

