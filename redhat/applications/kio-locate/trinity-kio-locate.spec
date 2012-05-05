# Default version for this component
%define kdecomp kio-locate
%define version 0.4.5
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	kio-slave for the locate command [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [kio-locate] Fix compilation with GCC 4.7
Patch1:		kio-locate-3.5.13-fix_gcc47_compilation.patch

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
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
%patch1 -p1

# Ugly hack to modify TQT include directory inside SCONS files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/kde.py \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g"


%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"
scons configure
scons


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
scons install DESTDIR=%{buildroot}

%clean
%__rm -rf %{buildroot}



%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO
%{tde_libdir}/kio_locate.la
%{tde_libdir}/kio_locate.so
%{tde_docdir}/HTML/en/kio-locate/index.cache.bz2
%{tde_docdir}/HTML/en/kio-locate/index.docbook
%{tde_docdir}/HTML/en/kio-locate/screenshot.png
%{_datadir}/services/locate.protocol
%{_datadir}/services/locater.protocol
%{_datadir}/services/rlocate.protocol
%{_datadir}/services/searchproviders/locate.desktop


%Changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.4.5-2
- Rebuilt for Fedora 17
- Removes post and postun
- Fix compilation with GCC 4.7

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.4.5-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

