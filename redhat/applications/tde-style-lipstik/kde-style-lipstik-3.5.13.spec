# Default version for this component
%define kdecomp kde-style-lipstik

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
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-style-lipstik
Summary:	Lipstik style for TDE
Version:	2.2.3
Release:	2%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

Obsoletes:		trinity-kde-style-lipstik

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-tdelibs-devel
BuildRequires:	trinity-tdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext


%description
Based on the plastik style, Lipstik is a purified style with many options to
tune your desktop look.

Lipstik also provides Lipstik-color-schemes


%prep
%setup -q -n applications/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --datadir=%{tde_datadir} \
  --libdir=%{tde_libdir} \
  --disable-rpath \
  --with-extra-includes=%{tde_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%clean
%__rm -rf %{buildroot}



%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_tdelibdir}/kstyle_lipstik_config.la
%{tde_tdelibdir}/kstyle_lipstik_config.so
%{tde_tdelibdir}/plugins/styles/lipstik.la
%{tde_tdelibdir}/plugins/styles/lipstik.so
%{tde_datadir}/apps/kdisplay/color-schemes/lipstiknoble.kcsrc
%{tde_datadir}/apps/kdisplay/color-schemes/lipstikstandard.kcsrc
%{tde_datadir}/apps/kdisplay/color-schemes/lipstikwhite.kcsrc
%{tde_datadir}/apps/kstyle/themes/lipstik.themerc


%Changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 2.2.3-2
- Rebuilt for Fedora 17
- Fix HTML directory location
- Removes post and postun

* Sat Nov 19 2011 Francois Andriot <francois.andriot@free.fr> - 2.2.3-1
- Initial release for RHEL 5, RHEL 6, Fedora 15, Fedora 16
