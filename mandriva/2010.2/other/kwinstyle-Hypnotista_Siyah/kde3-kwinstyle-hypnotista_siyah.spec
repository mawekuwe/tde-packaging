
Summary:	Hypnotista_Siyah Window Decoration for KDE3
Name:		kde3-kwinstyle-Hypnotista_Siyah
Version:	0.1
Release:	%mkrel 3
URL:			http://www.kde-look.org/content/show.php?content=33203
Source0:		http://www.kde-look.org/CONTENT/content-files/33203-Hypnotista_Siyah-%{version}.tar.gz
Patch0:			fix_autotools.patch
Group:			Graphical desktop/KDE3
License:		GPL
BuildRoot:		%{_tmppath}/%{name}-root
BuildRequires:		kde3-macros
%if %mdkversion < 201000
BuildRequires:		autoconf <= 1:2.63
%else
BuildRequires:		autoconf >= 1:2.65
%endif
BuildRequires:		automake >= 1.6
BuildRequires:		%{_lib}xorg-x11-devel
BuildRequires:		kdelibs-devel
BuildRequires:		kdebase-devel
BuildRequires:		libpng-devel
BuildRequires:		qt3-devel
Requires:		kdelibs >= 3.5.9
Requires:		kdebase >= 3.5.9

%description
Window Decoration inspired of windows vista visual style for KDE3
This decoration is black version of Hypnotista Sade.

%prep
%setup -q -n Hypnotista_Siyah-%{version}
%if %mdkversion >= 201000
%patch0 -p1
%endif


%build
export QTDIR=%qt3dir

make -f Makefile.cvs
%configure_kde3

%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%if %mdkversion < 2009000
%post
/sbin/ldconfig

%postun
/sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%_kde3_appsdir/kwin/*.desktop
%_kde3_libdir/kde3/*.la
%_kde3_libdir/kde3/*.so

%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 0.1-3mvt2010.2
- Rebuild for Trinity

* Sat May 08 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.1-2mvt2010.0
- fix buildrequires

* Sun Feb 21 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.1-1mvt2010.0
+ Packaged for mdv 2010.0
- Patch to compile with autoconf 2.65 and automake 1.11
