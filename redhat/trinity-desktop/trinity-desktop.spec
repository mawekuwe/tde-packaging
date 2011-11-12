# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

Name:		trinity-desktop
Version:	%{version}
Release:	%{?release}%{?dist}%{?_variant}
License:	GPL
Summary:	Meta-package to install TDE
Group:		User Interface/Desktops

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Source0:	trinity-3.5.13-fedora.repo
Source1:	trinity-3.5.13-rhel.repo

Requires:	trinity-kdeaccessibility >= %{version}
Requires:	trinity-kdeaddons >= %{version}
Requires:	trinity-kdeadmin >= %{version}
Requires:	trinity-kdeartwork >= %{version}
Requires:	trinity-kdeartwork-icons >= %{version}
Requires:	trinity-kdebase >= %{version}
Requires:	trinity-kdebindings >= %{version}
Requires:	trinity-kdeedu >= %{version}
Requires:	trinity-kdegames >= %{version}
Requires:	trinity-kdegraphics >= %{version}
Requires:	trinity-kdemultimedia >= %{version}
Requires:	trinity-kdenetwork >= %{version}
Requires:	trinity-kdepim >= %{version}
Requires:	trinity-kdeutils >= %{version}
Requires:	trinity-kdetoys >= %{version}
Requires:	trinity-repo >= %{version}

%description
The TDE project aims to keep the KDE3.5 computing style alive, as well as 
polish off any rough edges that were present as of KDE 3.5.10. Along 
the way, new useful features will be added to keep the environment 
up-to-date.
Toward that end, significant new enhancements have already been made in 
areas such as display control, network connectivity, user 
authentication, and much more!

%package dev
Group:		User Interface/Desktops
Summary:	Meta-package to install TDE development tools

Requires:	trinity-kdesdk >= %{version}
Requires:	trinity-kdevelop >= %{version}
Requires:	trinity-kdewebdev >= %{version}

%description dev
%{summary}

%package extras
Group:		User Interface/Desktops
Summary:	Meta-package to install extra TDE packages

Requires:	trinity-kdeaddons-extras >= %{version}
Requires:	trinity-kdebase-extras >= %{version}
Requires:	trinity-kdegraphics-extras >= %{version}
Requires:	trinity-kdemultimedia-extras >= %{version}
Requires:	trinity-kdenetwork-extras >= %{version}
Requires:	trinity-kdeutils-extras >= %{version}

%description extras
%{summary}

%package all
Group:		User Interface/Desktops
Summary:	Meta-package to install all TDE packages

Requires:	%{name} == %{version}
Requires:	%{name}-dev == %{version}
Requires:	%{name}-extras == %{version}

%description all
%{summary}

%package -n trinity-repo
Group:		User Interface/Desktops
Summary:	Yum configuration files for Trinity

%description -n trinity-repo
%{summary}

%prep

%build

%install
%__rm -rf %{?buildroot}
%__mkdir_p %{?buildroot}%{_sysconfdir}/yum.repos.d
%if 0%{?fedora}
%__install -m 644 %{SOURCE0} %{?buildroot}%{_sysconfdir}/yum.repos.d
%else
%__install -m 644 %{SOURCE1} %{?buildroot}%{_sysconfdir}/yum.repos.d
%endif

%files

%files dev

%files extras

%files all

%files -n trinity-repo
%{_sysconfdir}/yum.repos.d/*.repo

%changelog
* Sat Nov 12 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Add 'repo' package
