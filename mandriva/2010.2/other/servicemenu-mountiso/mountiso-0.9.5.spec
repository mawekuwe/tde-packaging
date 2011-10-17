%define name 		kde3-servicemenu-mountiso
%define origname 	mountiso
%define version 	0.9.5
%define release     	%mkrel 3
%define group 		Graphical desktop/KDE
%define arch 		noarch
%define distro 	%(rpm -qf --qf='%{VERSION}' /etc/mandrake-release)


Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		%{group}
Summary: 	MountISO - ISO Imager Mounter
Source0: 	%{origname}-%{version}.tar.bz2 
Patch0:         fix_weird_iso_names.patch
Url: 		http://www.kde-apps.org/content/show.php/MountISO?content=11577
BuildRoot: 	%{_tmppath}/%{origname}-%{version}-buildroot
BuildArch: 	%{arch}
#Conflicts:
Obsoletes:	%{origname}
#BuildRequires:	
Requires:	kdebase
Suggests:	ccd2iso cdemu extract-xiso bchunk mdf2iso


%description
Mount ISO Image is an advanced script which allows to perform multiple operations with ISO, NRG (Nero Burning ROM), UDF (DVD), CUE/BIN, CCD/IMG/SUB (CloneCD), XDVDFS (XBOX) and MDF images.

Optionally can be installed the packages “ccd2iso, cdemu and extract-xiso”.

Translations
------------
- German (by Markus Bloch)
- Italian (by marcosegato)
- Russian (by Jinjiru)
- Serbian (by Mladen Pejaković)
- Spanish (by Javier Ariza Rodríguez & Alberto Garcia)
- Turkish (by Atilla Öntaş)


%prep
%setup -q -n usr
%patch0 -p1
%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%_kde3_datadir
mkdir -p %{buildroot}%_kde3_bindir
cp -R bin/* %{buildroot}%_kde3_bindir/
cp -R share/* %{buildroot}%_kde3_datadir/
#remove x-cue.desktop. Conflicts with kdelibs3-common-30000000:3.5.10-12mvt2010.0.x86_64
pushd  %buildroot/%_kde3_datadir/
    rm -rf mimelnk/application/x-cue.desktop
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_kde3_bindir/*
%_kde3_appsdir/konqueror/servicemenus/*.desktop
%_kde3_appsdir/d3lphin/servicemenus/*.desktop
%_kde3_datadir/mimelnk/application/*.desktop

%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 0.9.5-3mvt2010.2
- Built for Trinity KDE

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 0.9.5-2mvt2010.0
- Built for MDV 2010.1

* Sat Nov 21 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.9.5-1mvt2010.0
-Packaged for 2010.0

* Sat Mar 22 2008 maik3531 <maik3531@web.de> 0.9.5-1pclos2007
- rebuild to PCLinuxOS
- provide a new Source0
- add description -l de & summary de

* Fri Mar 21 2008 Erkan Kaplan <erkan@linux-sevenler.org>
- First build 

