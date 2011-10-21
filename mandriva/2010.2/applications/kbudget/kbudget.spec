Summary: 	Budgeting and personal finance program for KDE
Name: 		kbudget
Version: 	0.6
Release:        %mkrel 13
License: 	GPL
Group: 		Office
Source0: 	%{name}-%{version}.tar.bz2
URL: 	        http://www.garandnet.net/kbudget/
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:  kdelibs3-devel
Patch0: kbudget-0.6-stdio.patch

%description
KBudget is a budgeting and personal finance program for KDE. 
It requires KDE 3 and is currently in early development.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q 
%patch0 -p0

%build
#make -f admin/Makefile.common cvs

export QTDIR=%_prefix/%_lib/qt3
export KDEDIR=%_prefix

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

# Search for qt/kde libraries in the right directories (avoid patch)
# NOTE: please don't regenerate configure scripts below
perl -pi -e "s@/lib(\"|\b[^/])@/%_lib\1@g if /(kde|qt)_(libdirs|libraries)=/" configure

%configure_kde3

%make

%install
rm -rf %{buildroot}
#make prefix=%{buildroot}%{_prefix} install
%makeinstall
%find_lang kbudget

%{__cp} %{buildroot}%{_iconsdir}/crystalsvg/22x22/apps/%{name}.png %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}%{_miconsdir}
%{__cp} %{buildroot}%{_iconsdir}/crystalsvg/16x16/apps/%{name}.png %{buildroot}%{_miconsdir}/%{name}.png
mkdir -p %{buildroot}%{_liconsdir}
%{__cp} %{buildroot}%{_iconsdir}/crystalsvg/48x48/apps/%{name}.png %{buildroot}%{_liconsdir}/%{name}.png


install -m 755 -d %buildroot%{_menudir}

%clean
rm -rf %{buildroot}

%post
%if %mdkversion > 200600
%update_icon_cache crystalsvg
%endif

%postun
%if %mdkversion > 200600
%clean_icon_cache crystalsvg
%endif

%files -f kbudget.lang
%defattr(-, root, root, 0755)
%doc README AUTHORS
%_bindir/%{name}


# copy regular icons to %_icondir
%_iconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png


%_iconsdir/crystalsvg/128x128/apps/*
%_iconsdir/crystalsvg/128x128/mimetypes/*
%_iconsdir/crystalsvg/16x16/apps/*
%_iconsdir/crystalsvg/16x16/mimetypes/*
%_iconsdir/crystalsvg/22x22/apps/*
%_iconsdir/crystalsvg/22x22/mimetypes/*
%_iconsdir/crystalsvg/32x32/apps/*
%_iconsdir/crystalsvg/32x32/mimetypes/*
%_iconsdir/crystalsvg/48x48/apps/*
%_iconsdir/crystalsvg/48x48/mimetypes/*
%_iconsdir/crystalsvg/scalable/apps/*
%_iconsdir/crystalsvg/scalable/mimetypes/*

%_datadir/applnk/Applications/%{name}.desktop
%_datadir/mimelnk/application/x-%{name}.desktop
%dir %_datadir/apps/%{name}
%_datadir/apps/%{name}/*.rc

# other html doc
%dir %_defaultdocdir/HTML/en/kbudget
%_defaultdocdir/HTML/en/kbudget/*



%changelog
* Wed Jul 21 2011 Tim Williams <tim@my-place.org.uk> 0.6-13mdv2010.2
+ Rebuild against Trinity 3.5.12

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 0.6-12mdv2010.1
+ MDV 2010.1 rebuild

* Tue Nov 17 2009 Tim Williams <tim@my-place.org.uk> 0.6-11mdv2010.0
+ MDV 2010.0 rebuild

* Wed Mar 25 2009 Helio Chissini de Castro <helio@mandriva.com> 0.6-10mdv2009.1
+ Revision: 361079
- Bump to rebuild against cooker

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Tue Feb 19 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6-7mdv2008.1
+ Revision: 172392
- fix update-menus-without-menu-file-in-%%post(|un)
- kdedesktop2mdkmenu.pl is no more
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request
- import kbudget

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Jun 26 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6-6mdv2007.0
- Use new menu
- Register icons

* Fri Dec 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.6-5mdk
- Fix Build
- use mkrel
- BuildRequires : kdelibs-devel

* Fri May 06 2005 Laurent MONTEL <lmontel@mandriva.com> 0.6-4mdk
- Fix build on x86_64

* Mon Jun 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6-3mdk
- Rebuils

* Tue Feb 24 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6-2mdk
- Fix distlint

* Wed Dec 31 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.6-1mdk
- 0.6

* Sun Oct 15 2003 Nicolas CHIPAUX <chipaux@mandrakesoft.com> 0.5-2mdk 
- libdir fix

* Sun Sep 23 2003 Nicolas CHIPAUX <chipaux@mandrakesoft.com> 0.5-1mdk 
- Initial release
