# Default version for this component
%define kdecomp libkdcraw
%define version 3.5.13
%define release 1

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
Summary:	Raw picture decoding C++ library (runtime) [Trinity]

Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires: tqtinterface-devel
BuildRequires: trinity-arts-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: desktop-file-utils
BuildRequires: lcms-devel, libjpeg-devel, pkgconfig
BuildRequires: automake autoconf libtool libtool-ltdl-devel
BuildRequires: gettext

%description
C++ interface around dcraw binary program used to decode RAW
picture files.
This library is used by kipi-plugins, digiKam and others kipi host programs.
libkdcraw contains the library of libkdcraw.

%package devel
Group:		Development/Libraries
Summary:	RAW picture decoding C++ library (development) [Trinity]
Requires:	%{name} = %{version}

%description devel
Libkdcraw is a C++ interface around dcraw binary program used to
decode Raw picture files.
libkdcraw-devel contains development files and documentation. The
library documentation is available on kdcraw.h header file.



%prep
%setup -q -n libraries/%{kdecomp}

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

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}



%clean
%__rm -rf %{buildroot}


%post
/sbin/ldconfig || :

%postun
/sbin/ldconfig || :

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*
%{_datadir}/icons/*/*/*/kdcraw.png
%{_datadir}/locale/*/LC_MESSAGES/libkdcraw.mo

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%Changelog
* Sun Nov 06 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.11-1
- Initial release for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15
