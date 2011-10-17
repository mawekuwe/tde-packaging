%define oname   wisdom
Name:		kde3-style-%{oname}
Version:	0.5
Release:	%mkrel 3
Source:		http://kde-look.org/CONTENT/content-files/65140-%{oname}-%{version}.tar.bz2
Patch0:         fix_autotools.patch
Patch1:         kde-3.5.10-acinclude.patch
Summary:	KDE3 style based on Plastik and Serenity
URL:		http://kde-look.org/content/show.php/Wisdom?content=65140
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
Wisdom is a style for KDE 3.x based on Plastik and Serenity.

Here are the differences with Plastik:
- Windows XP-like arrows.
- Tree branches can be hidden.
- The kicker panel draws its one-pixel border in black.
- Panel 3D effects are lighter.
- Popup menus border follows the color scheme.
- Toolbar and menu separators are lighter.
- Other horizontal and vertical separators are removed.
- Group boxes are drawn in a Gnome-like look (i.e. without frame).
- Tab height is fixed: two pixels were missing.
- Focus is drawn with the highlight color. It is more discreet.
- The kdm login manager can be transparent.

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
%_kde3_appsdir/kstyle/themes/*
%_kde3_libdir/*

%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 0.5-3mvf2010.2
- Rebuild for Trinity

* Sat May 08 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.5-2mvt2010.0
- fix buildrequires

* Tue Apr 20 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.5-1mvt2010.0
+ Package for 2010.0 release
