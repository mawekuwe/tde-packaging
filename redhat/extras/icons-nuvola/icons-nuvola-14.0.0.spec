# Default version for this component
%define tde_pkg icons-nuvola
%define tde_version 14.0.0

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

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		Nuvola icons for TDE Desktop
Version:		1.0
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		icons-nuvola-14.0.0.tar.bz2

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext


%description
Nuvola SVG evolution of SKY icon theme.
 
 NUVOLA is an SVG based icon theme.
 This mean that all icons where designed with a vector graphics software and 
 then exported to SVG.
 Icons of the TDE version of Nuvola are PNG images (unscalable).
 SVG files are available (not always updated) on my web site in the "svg"
 section.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n nuvola


%build


%install
install -d -m 755 %{buildroot}%{tde_datadir}/icons/nuvola
install -d -m 755 %{buildroot}%{tde_datadir}/icons/nuvola/16x16
install -d -m 755 %{buildroot}%{tde_datadir}/icons/nuvola/32x32
install -d -m 755 %{buildroot}%{tde_datadir}/icons/nuvola/48x48
install -d -m 755 %{buildroot}%{tde_datadir}/icons/nuvola/64x64
install -d -m 755 %{buildroot}%{tde_datadir}/icons/nuvola/128x128
rm -f thanks.to~
cp -fr * %{buildroot}%{tde_datadir}/icons/nuvola/


%clean
%__rm -rf %{buildroot}




%files
%defattr(-,root,root,-)
%doc author license.txt readme.txt 
%{tde_datadir}/icons/nuvola/


%changelog
* Sat Sep 20 2014 Francois Andriot <francois.andriot@free.fr> - 1.0-1
- Initial release for TDE 14.0.0
