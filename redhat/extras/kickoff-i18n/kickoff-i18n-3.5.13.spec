# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# Speed build options
%define debug_package %{nil}
%define __spec_install_post %{nil}
AutoReq: no

# TDE 3.5.13 specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_doc %{tde_datadir}/doc

%define _docdir %{tde_docdir}


Name:			trinity-kickoff-i18n
Summary:		Kickoff translations for Trinity Desktop Environment
Version:		1.0
Release:		1%{?dist}%{?_variant}
Group:			System/Internationalization
License:		GPL
URL:			http://www.mandriva.com

Source0:		kickoff-i18n-1.0.tar.bz2
Patch0:			kickoff-i18n-1.0-uz-po.patch
Patch1:			kickoff-i18n-1.0-tr-po.patch

# [kickoff-i18n] Fix directories for Trinity
Patch2:			kickoff-i18n-1.0-fix_trinity_location.patch
# [kickoff-i18n] Fix build with automake 1.11
Patch3:			kickoff-i18n-1.0-fix_autotools_detection.patch

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:		noarch

BuildRequires:	qt3-devel
BuildRequires:	trinity-tdelibs-devel

%description
kickoff translations

%prep
%setup -q -n kickoff-i18n-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1 -b .dir
%patch3 -p1 -b .automake

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

./configure \
    --prefix=%{tde_prefix} \
    --exec-prefix=%{tde_prefix} \
    --datadir=%{tde_datadir}

%__make %{?_smp_mflags}

%install
%__rm -fr %{buildroot}
%__make install DESTDIR=%{?buildroot}

%find_lang kickoff

%clean
#rm -fr %{buildroot}

%files -f kickoff.lang
%defattr(-,root,root,-)

%changelog
* Fri Aug 03 2012 Francois Andriot <francois.andriot@free.fr> - 1.0-1
- Initial release for TDE 3.5.13
