%define oname   deKorator
Name:		kde3-kwinstyle-%{oname}
Version:	0.3
Release:	%mkrel 3
Source:		%{oname}-%{version}.tar.bz2
Patch0:         fix_autotools.patch
Patch1:         kde-3.5.10-acinclude.patch
Summary:	KDE3 Window Decoration Generator
URL:		http://kde-look.org/content/show.php/deKorator?content=31447
License:	GPL
Group:		Graphical desktop/KDE3
BuildRequires:  kde3-macros
%if %mdkversion < 201000
BuildRequires:  autoconf <= 1:2.63
%else
BuildRequires:  autoconf >= 1:2.65
%endif
BuildRequires:  automake >= 1.6
BuildRequires:  %{_lib}xorg-x11-devel
BuildRequires:  kdelibs-devel
BuildRequires:  kdebase-devel
BuildRequires:  libpng-devel
BuildRequires:  qt3-devel
Requires:	kdelibs >= 3.5.9
Requires:	kdebase >= 3.5.9	
BuildRoot:	%{_tmppath}/%{name}-root

%description
Design your own window decorations with
deKorator!

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
%patch1 -p1

%build

make -f admin/Makefile.common
%configure_kde3
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std





%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 2009000
%post
/sbin/ldconfig

%postun
/sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%_kde3_appsdir/kwin/%{oname}.desktop
%_kde3_libdir/*
%changelog
* Mon Jul 18 2011 Tim Williams <tim@my-place.org.uk> 0.3-3mvt2010.2
+ rebuild for Trinity

* Sat May 08 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.3-2mvt2010.0
- fix buildrequires

* Tue Apr 20 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.3-1mvt2010.0
+ Package for 2010.0 release
