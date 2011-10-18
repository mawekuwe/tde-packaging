Name: kde3-kicker-backgrounds
Version: 0.1
Release: %mkrel 4
Summary: KDE-Look.org kicker backgrounds for KDE3
License:   GPL
URL:       http://moodwrod.com/
Group:     Graphical desktop/KDE3
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:    kicker_wallpapers-0.1.tar.bz2
Requires:  kdebase-common

%description
These are background images for kicker,comes from kde-look.org

Included images are:
- GlassPanels
http://kde-look.org/CONTENT/content-files/86301-GlassPanels.tar.gz
- Coloured flames
http://kde-look.org/CONTENT/content-files/83263-ColouredFlames.tar.gz
- total work pack
http://kde-look.org/CONTENT/content-files/64870-TWarchivio.tar.gz


%prep
rm -rf %buildroot

%setup -q -n kicker_wallpapers-0.1

%build
mkdir -p %buildroot%_kde3_appsdir/kicker/wallpapers
for i in $(find . -name "*.png")
do 
  install -m0644 $i %buildroot%_kde3_appsdir/kicker/wallpapers
done

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%_kde3_appsdir/kicker/wallpapers/*.png





%changelog
* Mon Jul 18 2011 Tim Williams <tim@my-place.org.uk> 0.1-4mvt2010.2
+ Build for Trinity

* Fri Jul 23 2010 Tim Williams <tim@my-place.org.uk> 0.1-3mvt2010.1
+ Build for MDV 2010.1

* Wed Feb 10 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.1-2mvt2010.0
- Change package group

* Thu Nov 26 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.1-1mvt2010.0
+ Initial RPM
