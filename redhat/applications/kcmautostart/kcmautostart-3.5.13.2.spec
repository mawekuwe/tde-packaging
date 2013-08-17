# Default version for this component
%define tde_pkg kchmviewer
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


Name:			trinity-kcmautostart
Summary:		Manage applications automatic startup.
Version:		1.0
Release:		%{?!preversion:4}%{?preversion:3_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kcmautostart-3.5.13.tar.gz

# [kcmautostart] Fix FTBFS with TDE 3.5.13
Patch1:		kcmautostart-3.5.13-ftbfs.patch
# [kcmautostart] Add French support
Patch2:		kcmautostart-3.5.13-add_french.patch
# [kcmautostart] kcmautostart crash on exit
Patch3:		kcmautostart-3.5.13-fix_crash_on_exit.patch
# [kcmautostart] Fix french translation
Patch4:		kcmautostart-3.5.13-fix_fr_translation.patch

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gcc-c++

Requires:		trinity-tdebase >= %{tde_version}

%description
%{summary}

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n applications/kcmautostart
%patch1 -p1 -b .ftbfs
%patch2 -p1
%patch3 -p1 -b .crash_on_exit
%patch4 -p1 -b .fr_translation

%__sed -i admin/acinclude.m4.in \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang autostart


%clean
%__rm -rf %{buildroot}


%files -f autostart.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{tde_tdelibdir}/kcm_autostart.la
%{tde_tdelibdir}/kcm_autostart.so
%{tde_tdeappdir}/autostart.desktop
%{tde_tdedocdir}/HTML/en/autostart/


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-4
- Build for Fedora 19

* Sat Jan 19 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-3
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 1.0-2
- Initial release for TDE 3.5.13.1

* Thu May 10 2012 Francois Andriot <francois.andriot@free.fr> - 1.0-1
- Initial release for TDE 3.5.13
