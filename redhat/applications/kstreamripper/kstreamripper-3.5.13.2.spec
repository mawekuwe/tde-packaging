# Default version for this component
%define tde_pkg kstreamripper
%define tde_version 3.5.13.2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		TDE frontend for streamripper

Version:		0.3.4
Release:		%{?!preversion:4}%{?preversion:3_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	scons


%description
KStreamRipper is a small frontend for the streamripper command
line utility. Streamripper captures internet shoutcast radio streams
on your harddisk and splits them up in mp3 files. KStreamRipper helps
you with managing/ripping your preferred streams.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__sed -i kde.py \
  -e "s|include/kde|include/tde|g"

%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"

scons -Q -j4 \
  qtlibs=${QTLIB:-${QTDIR}/%{_lib}}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{tde_bindir}/kstreamripper
%{tde_datadir}/applnk/Utilities/kstreamripper.desktop
%{tde_datadir}/apps/kstreamripper/kstreamripperui.rc
%{tde_tdedocdir}/HTML/en/kstreamripper/



%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 0.3.4-4
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.3.4-3
- Initial release for TDE 3.5.13.2

* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 0.3.4-2
- Initial release for TDE 3.5.13.1

* Wed Nov 02 2011 Francois Andriot <francois.andriot@free.fr> - 0.3.4-1
- Initial release for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15
