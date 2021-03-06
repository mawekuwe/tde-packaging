#
# spec file for package fileshareset
#
# Copyright (c) 2014 Trinity Desktop Environment
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
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# Extract from 'fileshareset.cpp'
#copyright            : (C) 2003 SuSE AG 
#email                : Uwe.Gansert@suse.de

Name:		fileshareset
Version:	2.0
Release:	1%{?dist}
Summary:	Set and list fileshares
Group:		System/Management
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		/usr
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        %{name}-%{version}.tar.gz

# for set_permissions macro
%if 0%{?suse_version}
PreReq: permissions
%endif

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  gcc-c++

#Requires:       

%description
This package contains the the fileshareset utility to allow users to
add or remove file shares.  It's also possible to list currently shared
locations. /etc/security/fileshare.conf is the main configuration file
This utility was originally written for openSUSE KDE3.


%prep
%setup -q -n fileshareset2
aclocal
autoconf
automake -a -c


%build
export CXXFLAGS="$CXXFLAGS -fPIE"
export CFLAGS="$CFLAGS -fPIE"
export LDFLAGS="$LDFLAGS -pie"
%configure
%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

# Install the man page
%__install -D -m 644 man/fileshareset.8 %{?buildroot}%{_mandir}/man8/fileshareset.8

# Install the default configuration file
mkdir -p "${RPM_BUILD_ROOT}%{_sysconfdir}/security/"
echo "RESTRICT=yes" > "${RPM_BUILD_ROOT}%{_sysconfdir}/security/fileshare.conf"


%clean
%__rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/filesharelist
%{_mandir}/man8/fileshareset.8*
%config(noreplace) %{_sysconfdir}/security/fileshare.conf

# Setuid program
%if 0%{?suse_version}
%verify(not mode) %{_bindir}/fileshareset
%else
%attr(4755,root,root) %{_bindir}/fileshareset
%endif


%if 0%{?suse_version}
# Check permissions on setuid files (openSUSE specific)
%verifyscript
%verify_permissions -e /usr/bin/fileshareset
%endif


%changelog
* Sun Oct 5 2014 François Andriot <francois.andriot@free.fr> - 2.0-1
- Initial build for TDE R14
