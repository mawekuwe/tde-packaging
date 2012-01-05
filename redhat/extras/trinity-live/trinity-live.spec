# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 2

%define _datadir %{_usr}/share

Name:		trinity-live
Version:	%{version}
Release:	%{?release}%{?dist}
License:	GPL
Summary:	Trinity Spins
Group:		Applications/System

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Requires:	fedora-kickstarts
Requires:	livecd-tools

Source0:	fedora-live-tde-base.ks
Source1:	fedora-livecd-tde.ks

%description
This package contains the Trinity configuration file to build a Fedora
LiveCD containing Fedora.

%package openbox
Summary:	bootstrap 'openbox' script that runs TDE's kwin
Requires:	trinity-kdebase
BuildArch:	noarch
Group:		Applications/System

%description openbox
There is a bug in 'firstboot' that prevents it to invoke 'openbox' correctly.
The provided script redirects 'openbox' to 'kwin'.
It is used on the Fedora TDE LiveCD.

%prep

%build
cat <<EOF >openbox
#!/bin/sh

# This script is used by 'firstboot' only.
# It allows to run TDE's kwin instead of openbox.

export PATH=%{_bindir}:\${PATH}
export HOME=/root
rm -rf \${HOME}/.DCOPserver*

rpm -e trinity-live-openbox

exec kwin \$@
EOF

%install
%__rm -rf %{?buildroot}
%__mkdir_p %{?buildroot}%{_datadir}/spin-kickstarts
%__install -m 644 %{SOURCE0} %{?buildroot}%{_datadir}/spin-kickstarts
%__install -m 644 %{SOURCE1} %{?buildroot}%{_datadir}/spin-kickstarts

# Openbox
%__install -D -m 755 openbox "%{?buildroot}/usr/local/bin/openbox"


%files
%{_datadir}/spin-kickstarts/fedora-live-tde-base.ks
%{_datadir}/spin-kickstarts/fedora-livecd-tde.ks

%files openbox
/usr/local/bin/openbox


%changelog
* Mon Dec 02 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- More TDE 3.5.13 specific visual settings
- Updates all packages to fix TDE bugs
- Add more applications

* Wed Nov 09 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial build
