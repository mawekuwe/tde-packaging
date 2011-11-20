# Default version for this component
%define kdecomp fusion-icon
%define version 0.0.0+git20071028
%define release 1

%define _prefix /usr
%if "%{?python2_sitelib}" == ""
%define python2_sitelib    %(python2 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	tray icon to launch and manage Compiz Fusion [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	python
Requires:		python

%description
The OpenCompositing Project brings 3D desktop visual effects that
improve the usability and eye candy of the X Window System and provide
increased productivity.

This package contains a tray icon that can launch Compiz and its
decorators.


%prep
%setup -q -n applications/%{kdecomp}

%__sed -i Makefile \
  -e "s,^PREFIX = .*,PREFIX = '%{_prefix}'," \
  -e "s,^DESTDIR = .*,DESTDIR = '%{buildroot}',"

%build
export PATH="%{_bindir}:${PATH}"
%__make


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%{_bindir}/fusion-icon
%{python2_sitelib}/FusionIcon/
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
%{python2_sitelib}/fusion_icon-0.0.0_git-py*.egg-info
%endif
%{_datadir}/applications/fusion-icon.desktop
%{_datadir}/icons/hicolor/22x22/apps/fusion-icon.png
%{_datadir}/icons/hicolor/24x24/apps/fusion-icon.png
%{_datadir}/icons/hicolor/48x48/apps/fusion-icon.png
%{_datadir}/icons/hicolor/scalable/apps/fusion-icon.svg


%Changelog
* Sat Nov 19 2011 Francois Andriot <francois.andriot@free.fr> - 0.0.0+git20071028-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
