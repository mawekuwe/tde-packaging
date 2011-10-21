%define realversion	0.2-beta2



Summary:	Konqueror Sidebar Plugin that shows Metadata and Information
Name:		kmetabar
Version:	0.2beta2
Release:	%mkrel 3
Source:		http://kde-apps.org/content/files/28725-kmetabar-%{realversion}.tar.bz2
URL:		http://kde-apps.org/content/show.php?content=28725
Patch0:         kmetabar-fix.patch
Patch1:         kmetabar-kdemacros.diff
Group:		Graphical desktop/KDE3
License:	GPLv2+
BuildRoot:	%{_tmppath}/build-%{_name}-%{_version}
Requires:	kdelibs3
Requires:	arts, expat, fam, jack, kdebase3, libogg, libvorbis, glib2
Requires:	libart_lgpl, libpng, libstdc++, libgcc, resmgr, zlib
BuildRequires:	kdelibs3-devel,arts-devel, expat-devel, fam-devel
BuildRequires:	kdebase3-devel,libogg-devel
BuildRequires:	libvorbis-devel, glib2-devel
BuildRequires:	libart_lgpl-devel,libpng-devel

%description
A sidebar plugin for KDE's Konqueror which shows information and actions for
selected files and directories.

This is a fork of the "metabar" project: http://sourceforge.net/projects/metabar

%prep
%setup -q -n %{name}-0.2-beta2
%patch0 -p0
cd %{name}
%patch1 -p0

%configure_kde3

%build
cd %{name}
%{make}

%install
%{__rm} -rf %{buildroot}
cd  %{name}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%_kde3_libdir/kde3/konqsidebar_kmetabar.so
%_kde3_libdir/kde3/konqsidebar_kmetabar.la
%_kde3_appsdir/kmetabar
%_kde3_appsdir/konqsidebartng/add/kmetabar_add.desktop
%_kde3_appsdir/konqsidebartng/entries/kmetabar.desktop
%_kde3_iconsdir/*/*x*/apps/kmetabar.png
%_kde3_docdir/*

%changelog
* Mon Jul 18 2011 <tim@my-place.org.uk> 0.2.beta2-3mvt2010.2
- Packaged for Trinity

* Fri Jul 23 2010 <tim@my-place.org.uk> 0.2.beta2-2mvt2010.1
- Packaged for 2010.1

* Tue Dec 22 2009 <atilla_ontas@mandriva.org> 0.2.beta2-1mvt2010.0
 - Packaged for 2010.0
