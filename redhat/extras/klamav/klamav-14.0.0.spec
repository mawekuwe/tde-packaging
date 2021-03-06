# Default version for this component
%define tde_pkg klamav
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
Summary:        Frontend for clamav
Version:		0.46
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
#URL:			http://www.trinitydesktop.org/
Url:            http://klamav.sourceforge.net/

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{tde_pkg}-%{tde_version}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext
BuildRequires:	curl-devel
BuildRequires:	gmp-devel
BuildRequires:	sqlite-devel
#BuildRequires:	unsermake
BuildRequires:  fdupes

BuildRequires:  clamav
Requires:		clamav

%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:  clamav-devel
%endif


%description
A TDE front-end for the Clam AntiVirus antivirus toolkit.

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{tde_pkg}-%{version}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

# Warning: --enable-final causes FTBFS
%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --docdir=%{tde_tdedocdir} \
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
  --disable-gcc-hidden-visibility \
  \
  --without-included-sqlite \
  --with-extra-includes=%{_includedir}/tqt

find . -name "*.cpp" | while read f; do
  mf="${f%.cpp}.moc"
  if grep -qw "${mf##*/}" "${f}" && [ ! -f "${mf}" ]; then
    tqmoc "${f%.cpp}.h" -o "${mf}"
  fi
done

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}
	

%post
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done
/sbin/ldconfig


%postun
for f in hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done
/sbin/ldconfig


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/ScanWithKlamAV
%{tde_bindir}/klamarkollon
%{tde_bindir}/klamav
%{tde_bindir}/klammail
%{tde_tdeappdir}/klamav.desktop
%{tde_datadir}/apps/klamav/
%{tde_datadir}/apps/konqueror/servicemenus/klamav-dropdown.desktop
%{tde_datadir}/config.kcfg/klamavconfig.kcfg
%{tde_tdedocdir}/HTML/en/klamav02/
%{tde_datadir}/icons/hicolor/32x32/apps/klamav.png
%{tde_datadir}/icons/hicolor/48x48/apps/klamav.png


%changelog
* Sat Sep 20 2014 Francois Andriot <francois.andriot@free.fr> - 0.46-1
- Initial release for TDE 14.0.0
