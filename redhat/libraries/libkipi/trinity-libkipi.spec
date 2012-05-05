# Default version for this component
%define kdecomp libkipi
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
Summary:	library for apps that want to use kipi-plugins (runtime version) [Trinity]

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
Libkipi is a library
  o that contains common routines and widget used by kipi-plugins
  o to ease implementation of the kipi-plugins interface in an application
    that wants to use kipi-plugins
    
Homepage: http://www.kipi-plugins.org/


%package devel
Group:		Development/Libraries
Summary:	library for apps that want to use kipi-plugins (development version) [Trinity]
Requires:	%{name} = %{version}

%description devel
Libkipi is a library
  o that contains common routines and widget used by kipi-plugins
  o to ease implementation of the kipi-plugins interface in an application
    that wants to use kipi-plugins
    
This package contains development files and documentation for libkipi library.
Homepage: http://www.kipi-plugins.org/

%prep
%setup -q -n libraries/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"

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
%{_datadir}/apps/kipi/data/*.png
%{_datadir}/icons/*/*/*/kipi.png
%{_datadir}/locale/*/LC_MESSAGES/libkipi.mo
%{_datadir}/servicetypes/kipiplugin.desktop

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%Changelog
* Sun Nov 06 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.11-1
- Initial release for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15
