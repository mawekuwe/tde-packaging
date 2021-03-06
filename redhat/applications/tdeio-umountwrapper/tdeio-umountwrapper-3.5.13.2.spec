# Default version for this component
%define tde_pkg tdeio-umountwrapper
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
Summary:		progress dialog for safely removing devices in Trinity.
Version:		0.2
Release:		%{?!preversion:7}%{?preversion:6_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://frode.kde.no/misc/tdeio_umountwrapper/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Source1:		media_safelyremove.desktop


BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

Obsoletes:		trinity-kio-umountwrapper < %{version}-%{release}
Provides:		trinity-kio-umountwrapper = %{version}-%{release}

%description
Wrapper around kio_media_mountwrapper.
Provides a progress dialog for Safely Removing of devices in Trinity.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"

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
  --enable-final \
  --enable-new-ldflags \
  --enable-closure \
  --enable-rpath

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%__install -D -m 644 %{SOURCE1} %{?buildroot}%{tde_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_kio-umountwrapper
%__install -D -m 644 %{SOURCE1} %{?buildroot}%{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_kio-umountwrapper


%clean
%__rm -rf %{buildroot}

%post
for f in konqueror d3lphin; do
  update-alternatives --install \
    %{tde_datadir}/apps/${f}/servicemenus/media_safelyremove.desktop \
    media_safelyremove.desktop_${f} \
    %{tde_datadir}/apps/${f}/servicemenus/media_safelyremove.desktop_kio-umountwrapper \
    20
done

%postun
if [ $1 -eq 0 ]; then
  for f in konqueror d3lphin; do
    update-alternatives --remove \
      media_safelyremove.desktop_${f} \
      %{tde_datadir}/apps/${f}/servicemenus/media_safelyremove.desktop_kio-umountwrapper
  done
fi

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_bindir}/kio_umountwrapper
%{tde_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_kio-umountwrapper
%{tde_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_kio-umountwrapper


%changelog
* Sat Sep 28 2013 Francois Andriot <francois.andriot@free.fr> - 0.2-7
- Fix inadvertent 'kio' renaming

* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 0.2-6
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.2-5
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.2-4
- Initial release for TDE 3.5.13.1

* Sun Jul 08 2012 Francois Andriot <francois.andriot@free.fr> - 0.2-3
- Add 'desktop' file, to make this program useful :-)

* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 0.2-2
- Rebuilt for Fedora 17
- Removes post and postun

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.2-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16

