# Default version for this component
%define kdecomp kio-locate

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


Name:		trinity-%{kdecomp}
Summary:	kio-slave for the locate command [Trinity]
Version:	0.4.5
Release:	2%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.12.tar.gz

# [kio-locate] Fix compilation with GCC 4.7
Patch1:		kio-locate-3.5.13-fix_gcc47_compilation.patch

BuildRequires: tqtinterface-devel
BuildRequires: trinity-tdelibs-devel
BuildRequires: trinity-tdebase-devel
BuildRequires: desktop-file-utils

BuildRequires:	scons

%description
Adds support for the "locate:" and "locater:"
protocols to Konqueror and other TDE applications.

This enables you to perform locate searches as you
would in a terminal. The result is displayed just
as a directory.


%prep
%setup -q -n applications/%{kdecomp}
#patch1 -p1 -b .install

# Ugly hack to modify TQT include directory inside SCONS files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i "admin/kde.py" \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g"


%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export CXXFLAGS="-I%{tde_includedir}/tqt ${CXXFLAGS}"
scons configure
scons


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
scons install DESTDIR=%{buildroot}

%clean
%__rm -rf %{buildroot}



%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO
%{tde_tdelibdir}/kio_locate.la
%{tde_tdelibdir}/kio_locate.so
%{tde_tdedocdir}/HTML/en/kio-locate/
%{tde_datadir}/services/locate.protocol
%{tde_datadir}/services/locater.protocol
%{tde_datadir}/services/rlocate.protocol
%{tde_datadir}/services/searchproviders/locate.desktop


%Changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.4.5-2
- Rebuilt for Fedora 17
- Removes post and postun
- Fix compilation with GCC 4.7

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.4.5-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

