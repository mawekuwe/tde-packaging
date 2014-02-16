# Default version for this component
%define tde_pkg dolphin
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


Name:			trinity-%{tde_pkg}
Summary:		File manager for TDE focusing on usability 
Version:		0.9.2
Release:		%{?!preversion:9}%{?preversion:8_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext


%description
Dolphin focuses on being only a file manager.
This approach allows to optimize the user
interface for the task of file management.


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

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --docdir=%{tde_tdedocdir} \
  --libdir=%{tde_libdir} \
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

# Makes 'media_safelyremove.desktop' an alternative
%__mv -f %{buildroot}%{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop %{buildroot}%{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_d3lphin

# Locales
%find_lang d3lphin


%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_tdeappdir} -q &> /dev/null
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
update-alternatives --install \
  %{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop \
  media_safelyremove.desktop_d3lphin \
  %{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_d3lphin \
  15

%preun
if [ $1 -eq 0 ]; then
  update-alternatives --remove \
    media_safelyremove.desktop_d3lphin \
    %{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_d3lphin || :
fi

%postun
update-desktop-database %{tde_tdeappdir} -q &> /dev/null
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files -f d3lphin.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO
%{tde_bindir}/d3lphin
%{tde_tdeappdir}/d3lphin.desktop
%{tde_datadir}/apps/d3lphin/
%{tde_datadir}/icons/hicolor/*/apps/d3lphin.png
%lang(en) %{tde_tdedocdir}/HTML/en/d3lphin/


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.9.2-9
- Initial release for TDE 14.0.0
