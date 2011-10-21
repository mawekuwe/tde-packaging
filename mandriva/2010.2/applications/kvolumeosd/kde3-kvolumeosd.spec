%define oname KVolumeOSD

Name: kde3-kvolumeosd
Version: 0.1
Release: %mkrel 6
Summary: An application showing OSD to respond volume buttons
License: GPLv2+
Group: Graphical desktop/KDE3
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.kde-apps.org/content/show.php?content=80354
Source: http://www.kde-apps.org/CONTENT/content-files/80354-%{oname}-%{version}.tar.gz
Patch0:         kde-3.5.10-acinclude.patch
Patch1:         fix_autotools.patch
BuildRequires:  kde3-macros
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
BuildRequires: automake >= 1.6.1
%else
BuildRequires: autoconf >= 1:2.65
BuildRequires: automake >= 1.11
%endif
BuildRequires: kdelibs-devel
BuildRequires: desktop-file-utils
Requires: kdemultimedia-kmix

%description
KVolumeOSD is a simple KDE application that runs in the background and
responds to volume buttons by showing a little OSD. It delegates the
actual job of adjusting the volume to KMix.

%prep
%setup -q -n %{oname}
%if %mdkversion >= 201000
%patch0 -p1
%patch1 -p1
%endif

%build
make -f Makefile.cvs
%configure_kde3
%make

%install
rm -rf %buildroot
%makeinstall_std

desktop-file-install --vendor='' --delete-original \
	--dir %buildroot%_kde3_datadir/applications/kde \
	--add-category='Audio;Mixer' \
	%buildroot%_kde3_datadir/applnk/Utilities/kvolumeosd.desktop

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post
%{update_menus}
%update_kde3_icon_cache hicolor

%postun
%{clean_menus}
%clean_kde3_icon_cache hicolor
%endif

%files
%defattr(-,root,root)
%{_kde3_bindir}/kvolumeosd
%{_kde3_appsdir}/kvolumeosd
%{_kde3_datadir}/doc/HTML/en/kvolumeosd
%{_kde3_datadir}/applications/kde/*.desktop
%{_kde3_iconsdir}/hicolor/*/apps/*


%changelog
* Mon Jul 18 2011 Tim Williams <tim@my-place.org.uk> 0.1-6mdv2010.2
+ Rebuild for Trinity

* Fri Jul 23 2010 Tim Williams <tim@my-place.org.uk> 0.1-5mdv2010.1
+ Rebuild MDV 2010.1

* Sun Feb 14 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.1-4mvt2010.0
+ Fix build with autoconf 2.65 and automake 1.11
+ Change package group

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 0.1-3mdv2010.0
+ Rebuild MDV 2010.0

* Fri May 09 2008 Funda Wang <fundawang@mandriva.org> 0.1-2mdv2009.0
+ Revision: 205328
- fix post and postun script
- fix name
- import source and spec
- Created package structure for kde3-kvolumeosd.

