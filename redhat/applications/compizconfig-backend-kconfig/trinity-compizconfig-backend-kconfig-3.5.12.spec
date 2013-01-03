# Default version for this component
%if "%{?version}" == ""
%define kdecomp compizconfig-backend-kconfig
%define version 3.5.12
%endif
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{tde_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_libdir %{tde_libdir}/kde3


Name:		trinity-%{?kdecomp}
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}
Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
Summary:        kconfig backend for compizconfig

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://www.opencompositing.org

Prefix:		%{tde_prefix}

Source0:	%{kdecomp}-%{version}.tar.gz

BuildRequires: tqtinterface-devel
BuildRequires: trinity-tdelibs-devel
BuildRequires: trinity-tdebase-devel
BuildRequires: desktop-file-utils

BuildRequires:	libcompizconfig-devel intltool
Requires:		compiz


%description
The Compiz Fusion Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
through plugins and themes contributed by the community giving a
rich desktop experience.

This package contains the kconfig backend for libcompizconfig

%prep
%setup -q -n applications/%{kdecomp}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f admin/Makefile.common


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
  --with-extra-includes=%{tde_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{?buildroot}
%make_install


%clean
%__rm -rf %{?buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING.GPL COPYING.LGPL
%{_usr}/%{_lib}/compizconfig/backends/*.so
%exclude %{_usr}/%{_lib}/compizconfig/backends/*.la

%changelog
* Tue Sep 06 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-1
- Initial package
- Import to GIT
