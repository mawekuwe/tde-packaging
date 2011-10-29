# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 0

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_libdir %{_libdir}/trinity


Name:		trinity-kdeutils
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}
License:	GPL
Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
Summary:	Trinity KDE Utilities
Prefix:		%{_prefix}

Source0:	kdeutils-%{version}.tar.gz

BuildRequires:	tqtinterface
BuildRequires:	trinity-arts
BuildRequires:	trinity-kdelibs

Requires:	tqtinterface
Requires:	trinity-kdelibs

%description
Trinity KDE Utilities.


%package devel
Requires:	%{name}
Summary:	%{name} - Development files
%description devel
Development files for %{name}.


%prep
%setup -q -n kdeutils

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
sed -i admin/acinclude.m4.in \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f admin/Makefile.common

%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"
export LDFLAGS="${LDFLAGS} -lqt-mt -lkdeui -L${QTLIB}"

%configure \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-dependency-tracking \
  --disable-debug --disable-warnings --enable-final \
  --with-xinerama \
  --with-extra-includes=%{_includedir}/tqt \
  --with-extra-libs=%{tde_libdir} \
  --enable-closure

%__make %{?_smp_mflags}

%install
%__rm -rf %{?buildroot}
%__mkdir_p %{?buildroot}
export PATH="%{_bindir}:${PATH}"
%make_install

%clean
%__rm -rf %{?buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/apps/*
%{_datadir}/autostart/*.desktop
%{_datadir}/config/*
%{_datadir}/icons/*
%{_datadir}/services/*
%{_datadir}/config.kcfg/*
%{_datadir}/servicetypes/kmilo/kmilopluginsvc.desktop
%{_libdir}/lib*.so.*
%{_libdir}/libkdeinit*.so
%{tde_libdir}/*.so
%{tde_docdir}/HTML/en/*

%{_datadir}/applnk/*/*
%{_datadir}/mimelnk/application/*


%files devel
%defattr(-,root,root,-)
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%{tde_libdir}/*.la

%changelog
* Mon Sep 05 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT

