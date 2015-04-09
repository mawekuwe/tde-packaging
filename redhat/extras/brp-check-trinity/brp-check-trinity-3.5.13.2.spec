#
# spec file for package brp-check-trinity (version 3.5.13-SRU)
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

# TDE variables
%define tde_version 3.5.13.2
%define tde_prefix /opt/trinity

Name:		brp-check-trinity
Version:	1.0
Release:	1%{?dist}
Summary:	Build root policy check scripts for Trinity
Group:		System Environment/Daemons 
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

BuildRequires:	update-desktop-files
BuildRequires:	brp-check-suse
BuildRequires:	brp-extract-appdata
Requires:	update-desktop-files
Requires:	brp-check-suse
Requires:	brp-extract-appdata
Requires:	sed



%description
This package dynamically patches the openSUSE brp script to allow
building of Trinity Desktop Environment (TDE) instead of KDE3.
It should not be installed on runtime computer.


%files

%post
for i in \
	brp-desktop.data/applications.menu \
	brp-desktop.data/kde-settings.menu \
	brp-desktop.data/xdg_menu \
	brp-suse.d/brp-25-symlink \
	brp-suse.d/brp-72-extract-appdata \
	suse_update_desktop_file.sh \
; do
	echo "Patching file '/usr/lib/rpm/${i}' ..."
	install -D "/usr/lib/rpm/${i}" "/usr/lib/rpm.orig/${i}"
	sed -i "/usr/lib/rpm/${i}" \
		-e "s|opt/kde3|opt/trinity|g" \
		-e "s|kde-settings-|tde-settings-|g" \
		-e "s|doc/kde|doc/tde|g" \
		-e "s|kde_xdgdata|tde_xdgdata|g" \
done


%postun
for i in \
	brp-desktop.data/applications.menu \
	brp-desktop.data/kde-settings.menu \
	brp-desktop.data/xdg_menu \
	brp-suse.d/brp-25-symlink \
	brp-suse.d/brp-72-extract-appdata \
	suse_update_desktop_file.sh \
; do
	echo "Restoring file '/usr/lib/rpm/${i}' ..."
	install "/usr/lib/rpm.orig/${i}" "/usr/lib/rpm/${i}"
done
rm -rf "/usr/lib/rpm.orig"

##########

%prep

%build

%install

%clean
%__rm -rf %{?buildroot}


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 1.0-1
- Initial release for TDE R14.0.0
