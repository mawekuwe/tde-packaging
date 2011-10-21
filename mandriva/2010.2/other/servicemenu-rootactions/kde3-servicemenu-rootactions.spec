
Name: 		kde3-servicemenu-rootactions
Summary:	Root actions for D3lphin/Konqueror context menu
Version: 	2.4.7.1 
Release: 	%mkrel 3
Url:		http://www.kde-apps.org/content/show.php/Root+Actions+Servicemenu?content=48411
Group:		Graphical desktop/KDE
License:	GPL-2
Source0: 	48411-rootactions_servicemenu_2.4.7.1.tar.gz
BuildArch:  	noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot 
Requires: kdebase-progs

%description  
Root Actions servicemenu provides a convenient way to perform several actions 'as root', from the right-click context menu in KDE filemanager.

%prep
rm -rf %{buildroot} 
%setup -q -n rootactions_servicemenu_2.4.7
#We are building this ackage for KDE3. Remove unneeded KDE4 parts
rm -rf Root_Actions_2.4.7/*-KDE4

%install
mkdir -p %{buildroot}%_kde3_bindir
cp Root_Actions_2.4.7/rootactions-servicemenu.pl %{buildroot}%_kde3_bindir

mkdir -p %{buildroot}%_kde3_appsdir/dolphin/servicemenus
cp Root_Actions_2.4.7/dolphin-KDE3/*.desktop %{buildroot}%_kde3_appsdir/dolphin/servicemenus

mkdir -p %{buildroot}%_kde3_appsdir/konqueror/servicemenus
cp Root_Actions_2.4.7/konqueror-KDE3/*.desktop %{buildroot}%_kde3_appsdir/konqueror/servicemenus

%clean  
rm -rf %{buildroot} 
 
%files   
%defattr(0755,root,root)
%doc changelog GPL-2
%attr(755,root,root) %_kde3_bindir/rootactions-servicemenu.pl
%_kde3_appsdir/*

%changelog  
* Mon Jul 18 2011 Tim Williams <tim@my-place.org.uk> 2.4.7.1-3mvt2010.1
- Rebuilt for Trinity

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 2.4.7.1-2mvt2010.1
- Rebuilt for MDV 2010.1

* Mon Nov 23 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 2.4.7.1-1mvt2010.0
- Packaged for KDE3 Mandriva 2010.0
