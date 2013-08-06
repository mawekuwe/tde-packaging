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
Release:		%{?!preversion:8}%{?preversion:7_%{preversion}}%{?dist}%{?_variant}

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
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

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
  --enable-gcc-hidden-visibility

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


# Makes 'media_safelyremove.desktop' an alternative
%__mv -f %{buildroot}%{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop %{buildroot}%{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_d3lphin
%__ln_s %{_sysconfdir}/alternatives/media_safelyremove.desktop_d3lphin %{buildroot}%{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop
%__mkdir_p %{?buildroot}%{_sysconfdir}/alternatives
%__ln_s %{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop %{?buildroot}%{_sysconfdir}/alternatives/media_safelyremove.desktop_d3lphin

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
    %{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_d3lphin
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
%{_sysconfdir}/alternatives/media_safelyremove.desktop_d3lphin


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.9.2-8
- Initial release for TDE 14.0.0

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.9.2-7
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.2-6
- Initial release for TDE 3.5.13.1

* Sun Jul 08 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.2-5
- Add alternatives with 'kio-umountwrapper'

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.2-4
- Rebuild for Fedora 17
- Fix HTML installation directory

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.2-3
- Rebuilt for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15

* Wed Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.2-2
- Import to GIT

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.2-1
- Correct macro to install under "/opt", if desired

* Thu Jun 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.2-0
- Initial release for RHEL 6.0
- Based on FC7 'Dolphin 0.8.2-2" SPEC file.

