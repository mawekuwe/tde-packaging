%define oname KOSD

Name: kosd-kde3
Version: 0.2.3
Release: %mkrel 5
Summary: An application showing OSD to respond volume buttons
License: GPLv2+
Group: Graphical desktop/KDE3
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.kde-apps.org/content/show.php?content=81457
Source: http://www.kde-apps.org/CONTENT/content-files/81457-%{oname}-%{version}.tar.bz2
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
Requires: kde3-kmix
Obsoletes: kde3-kvolumeosd < %version

%description
KOSD is a simple KDE application that runs in the background and
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

%find_lang kosd --with-html

mkdir -p %buildroot%_kde3_datadir/applications/kde
mv %buildroot/share/applications/*.desktop %buildroot%_kde3_datadir/applications/kde

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post
%{update_menus}
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_kde3_icon_cache hicolor
%endif

%files -f kosd.lang
%defattr(-,root,root)
%{_kde3_bindir}/kosd
%{_kde3_appsdir}/kosd
%{_kde3_datadir}/applications/kde/*.desktop
%{_kde3_iconsdir}/hicolor/*/apps/*


%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 0.2.3-5mdv2010.2
+ Rebuild for Trinity

* Fri Jul 23 2010 Tim Williams <tim@my-place.org.uk> 0.2.3-4mdv2010.1
+ Rebuild for MDV 2010.1

* Sat Feb 13 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.2.3-3mdv2010.0
+ Fix built issues with autocnf 2.65 and automake 1.11
+ Change package group

* Mon Nov 16 2009 Tim Williams <tim@my-place.org.uk> 0.2.3-2mdv2010.0
+ Rebuild for MDV 2010.0

* Fri Aug 01 2008 Funda Wang <fundawang@mandriva.org> 0.2.3-1mdv2009.0
+ Revision: 259119
- New version 0.2.3

* Wed Jul 30 2008 Funda Wang <fundawang@mandriva.org> 0.2.2-1mdv2009.0
+ Revision: 254587
- New version 0.2.2

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jun 04 2008 Funda Wang <fundawang@mandriva.org> 0.2.1-1mdv2009.0
+ Revision: 214973
- Rename to kosd
- new version 0.2.1
- rename to kosd

* Fri May 09 2008 Funda Wang <fundawang@mandriva.org> 0.1-2mdv2009.0
+ Revision: 205328
- fix post and postun script

* Fri May 09 2008 Funda Wang <fundawang@mandriva.org> 0.1-1mdv2009.0
+ Revision: 205299
- fix name
- import source and spec
- Created package structure for kde3-kvolumeosd.

