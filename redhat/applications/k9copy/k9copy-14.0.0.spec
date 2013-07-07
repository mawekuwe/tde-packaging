# Default version for this component
%define tde_pkg k9copy
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
Summary:		DVD backup tool for Trinity
Version:		1.2.3
Release:		%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

Patch1:		k9copy-3.5.13.2-fix_k3b_link.patch

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

# Warning: the target distribution must have ffmpeg !
BuildRequires:	ffmpeg-devel
Requires:		ffmpeg

%description
k9copy is a tabbed tool that allows to copy of one or more titles from a DVD9
to a DVD5, in thesame way than DVDShrink for Microsoft Windows (R).
This is the Trinity version


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
#patch1 -p1 -b .ftbfs

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

# FFMPEG ...
if [ -d /usr/include/ffmpeg ]; then
	export CXXFLAGS="${RPM_OPT_FLAGS} -I/usr/include/ffmpeg"
fi

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --disable-rpath \
  --enable-closure \
  --disable-k3bdevices

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
update-desktop-database %{tde_appdir} &> /dev/null

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
update-desktop-database %{tde_appdir} &> /dev/null


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/k9copy
%{tde_tdeappdir}/k9copy.desktop
%{tde_datadir}/apps/k9copy/
%{tde_datadir}/apps/konqueror/servicemenus/k9copy_open.desktop
%lang(en) %{tde_tdedocdir}/HTML/en/k9copy/
%{tde_datadir}/icons/hicolor/*/apps/k9copy.png


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 1.2.3-5
- Initial release for TDE 14.0.0

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 1.2.3-4
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 1.2.3-3
- Initial release for TDE 3.5.13.1

* Sat Aug 04 2012 Francois Andriot <francois.andriot@free.fr> - 1.2.3-2
- Add support for MGA2 and MDV2011
- Fix 'format not a string literal' error. Clean up warning. [Commit #3bfc84b0]
- Fix FTBFS [Commit #62acebb7]
- Fix 'format not a string literal' error [Commit #d9ed8b32]
- Fix remaining string format errors [Commit #a8e98ad9]
- Fix another string format error [Commit #b3bb8a8f]
- Fix FTBFS [Commit #ca864ede]
- Fix format string error [Commit #a016df82]

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 1.2.3-2
- Fix HTML directory location

* Sat Nov 19 2011 Francois Andriot <francois.andriot@free.fr> - 1.2.3-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
