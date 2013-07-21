# Default version for this component
%define kdecomp filelight-l10n

%define debug_package %{nil}


# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:		trinity-%{kdecomp}
Summary:	Localization (l10n) for Filelight, disk space usage tool [Trinity]
Version:	1.0
Release:	2%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities
%if 0%{?fedora} > 0 || 0%{?rhel} >= 6
BuildArch:	noarch
%endif

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-tdelibs-devel
BuildRequires:	trinity-tdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

Requires:		trinity-filelight

%description
This package provides localization(l10n) files (translations and docs) for
Filelight, Filelight allows you to understand your disk usage by graphically
representing your filesystem as a set of concentric, segmented rings.

See the 'filelight' package description for more information.



%prep
%setup -q -n applications/%{kdecomp}

# Removes 'en' (primary) language HTML doc, since it is already in main package.
%__rm -rf doc/filelight

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"



%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{_includedir}"

./configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --datadir=%{tde_datadir} \
  --docdir=%{tde_tdedocdir} \
  --disable-rpath \
  --with-extra-includes=%{tde_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang filelight --with-kde


%clean
%__rm -rf %{buildroot}




%files -f filelight.lang
%defattr(-,root,root,-)


%Changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 1.0-2
- Rebuilt for Fedora 17
- Removes useless post and postun

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 1.0-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
