#
# spec file for package avahi-tqt
#
# Copyright (c) 2014 François Andriot <francois.andriot@free.fr>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http:/www.trinitydesktop.org/
#

# TDE specific building variables
%define tde_version 14.0.0
%define tde_prefix /opt/trinity
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

Name:		trinity-avahi-tqt
Epoch:		2
Version:	0.6.30
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:	LGPL-2.0+
Summary:	Avahi TQt integration library
Group:		System/Libraries

Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		/usr
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqt3-devel >= 3.5.0
BuildRequires:	trinity-tqtinterface-devel >= 1:4.2.0-1

BuildRequires:	gcc-c++
BuildRequires:	gettext-devel
BuildRequires:	libtool

# DBUS support
%if 0%{?suse_version}
BuildRequires:	dbus-1-devel
%endif
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	dbus-devel
%endif

# AVAHI support
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	%{_lib}avahi-client-devel
%endif
%if 0%{?suse_version} || 0%{?rhel} || 0%{?fedora}
BuildRequires:	avahi-devel
%endif

# EXPAT support
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	expat-devel
%endif
%if 0%{?suse_version} || 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	libexpat-devel
%endif

Requires:		trinity-tqt3 >= 3.5.0
Requires:		trinity-tqtinterface >= 1:4.2.0-1

%description
Avahi is a fully LGPL framework for Multicast DNS Service Discovery.
It allows programs to publish and discover services and hosts
running on a local network with no specific configuration. For
example you can plug into a network and instantly find printers to
print to, files to look at and people to talk to.
 .
This library contains the interface to integrate the Avahi libraries
into a TQt main loop application.

##########

%package -n libavahi-tqt
Summary:	Avahi TQt integration library
Group:		System/Libraries

%if 0%{?mgaversion} || 0%{?mdkversion}
Provides:		%{_lib}avahi-qt3
%endif

Obsoletes:		avahi-tqt
Provides:		avahi-tqt = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-avahi-tqt
Provides:		trinity-avahi-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libavahi-tqt
Avahi is a fully LGPL framework for Multicast DNS Service Discovery.
It allows programs to publish and discover services and hosts
running on a local network with no specific configuration. For
example you can plug into a network and instantly find printers to
print to, files to look at and people to talk to.
 .
This library contains the interface to integrate the Avahi libraries
into a TQt main loop application.

%post -n libavahi-tqt
/sbin/ldconfig || :

%postun -n libavahi-tqt
/sbin/ldconfig || :

%files -n libavahi-tqt
%defattr(-,root,root,-)
%{_libdir}/libavahi-tqt.so.1
%{_libdir}/libavahi-tqt.so.1.0.0

##########

%package -n libavahi-tqt-devel
Summary:	Avahi TQt integration library (Development Files)
Group:		Development/Libraries
Requires:	libavahi-tqt = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?mgaversion} || 0%{?mdkversion}
Provides:		%{_lib}avahi-qt3-devel
%endif

Obsoletes:		avahi-tqt-devel
Provides:		avahi-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-avahi-tqt-devel
Provides:		trinity-avahi-tqt-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libavahi-tqt-devel
Avahi is a fully LGPL framework for Multicast DNS Service Discovery.
It allows programs to publish and discover services and hosts
running on a local network with no specific configuration. For
example you can plug into a network and instantly find printers to
print to, files to look at and people to talk to.
 .
This library contains the interface to integrate the Avahi libraries
into a TQt main loop application.

%post -n libavahi-tqt-devel
/sbin/ldconfig || :

%postun -n libavahi-tqt-devel
/sbin/ldconfig || :

%files -n libavahi-tqt-devel
%defattr(-,root,root,-)
%{_includedir}/avahi-tqt/
%{_libdir}/libavahi-tqt.so
%{_libdir}/libavahi-tqt.la
%{_libdir}/pkgconfig/avahi-tqt.pc

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
./autogen.sh


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --exec-prefix=%{_prefix} \
  --includedir=%{_includedir} \
  --libdir=%{_libdir} \
  \
  --disable-static \
  --disable-dependency-tracking \
  \
  --enable-compat-libdns_sd \
  --with-systemdsystemunitdir=/lib/systemd/system

%__make %{?_smp_mflags}


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot}


%clean
%__rm -rf %{?buildroot}


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2:0.6.30-1
- Initial release for TDE 14.0.0
