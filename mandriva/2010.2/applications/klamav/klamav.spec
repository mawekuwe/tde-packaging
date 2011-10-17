Summary:	KDE frontend for the Clam AntiVirus virus scanner
Name:		klamav
Version:	0.46
Release:	%mkrel 4
License:	GPLv2+
Group:		File tools
URL:		http://sourceforge.net/projects/klamav/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}-source.tar.gz
Source1:	klamav.sh
Patch0:		klamav-0.46-default-db-dir.diff
Patch1:         klamav-0.42-fix-window-size.patch
Patch2:		klamav-0.41.1-pwd-echo.patch
Patch3:		klamav-0.46-gcc43.patch
BuildRequires:	kdelibs-devel
BuildRequires:	clamav-devel >= 0.93
BuildRequires:	desktop-file-utils
Requires:	clamav >= 0.93
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
KlamAV provides ClamAV protection for the KDE desktop. It includes
'on access' scanning, manual scanning, quarantine management,
downloading of updates, mail scanning, and automated installation.

%prep

%setup -qn %{name}-%{version}-source/%{name}-%{version}
#patch0 -p1 -b .default_db_directory
%patch1 -p0 -b .fix_window_size
%patch2 -p1 -b .pwd-echo
%patch3 -p1 -b .gcc43

%build
%configure_kde3
%make

%install
rm -Rf %{buildroot}

%makeinstall_std

mkdir -p %{buildroot}/{%{_menudir},%{_miconsdir},%{_liconsdir}}

mkdir -p %{buildroot}%{_kde3_datadir}/applications/kde
desktop-file-install --vendor='' --delete-original \
	--dir=%{buildroot}%{_kde3_datadir}/applications/kde \
	--remove-category="Application" \
	--add-category="Security" \
	%{buildroot}%{_kde3_datadir}/applnk/Utilities/klamav.desktop


# Copy translated virus browser
# Next release this shoul be made standard
mv %{buildroot}%{_kde3_bindir}/klamav %{buildroot}%{_kde3_bindir}/klamav-real
cp %SOURCE1 %{buildroot}%{_kde3_bindir}/klamav

%find_lang %{name} --with-html --all-name

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -Rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%attr (755,root,root) %{_kde3_bindir}/*
%{_kde3_datadir}/apps/%{name}
%{_kde3_iconsdir}/*/*/*/%{name}.png
%{_kde3_datadir}/applications/kde/*.desktop
%{_kde3_datadir}/apps/konqueror/servicemenus/klamav-dropdown.desktop
%{_kde3_datadir}/config.kcfg/*.kcfg


%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 0.46-4mdv2010.2
+ Rebuild for Trinity

* Wed Jul 21 2010 Tim Williams <tim@my-place.org.uk> 0.46-3mdv2010.1
+ Rebuild for MDV 2010.1

* Tue Nov 17 2009 Tim Williams <tim@my-place.org.uk> 0.46-2mdv2010.0
+ Rebuild for MDV 2010.0

* Sat Mar 14 2009 Buchan Milne <bgmilne@mandriva.org> 0.46-1mdv2009.1
+ Revision: 355062
- New version 0.46
- drop vlamav 0.nf patch, fixed upstream
- rediff patches

* Thu Sep 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.44-2mdv2009.0
+ Revision: 280731
- fix build against clamav-0.94 libs
- rebuild against new clamav libs

* Sun Jul 06 2008 Funda Wang <fundawang@mandriva.org> 0.44-1mdv2009.0
+ Revision: 232258
- New version 0.44
- switch to /opt
- drop patch4 not needed

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed May 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.42-4mdv2009.0
+ Revision: 209718
- bump release
- sync with fedora
- rebuild

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Fix some UI issues

* Sun Jan 20 2008 Funda Wang <fundawang@mandriva.org> 0.42-1mdv2008.1
+ Revision: 155212
- New version 0.42

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 09 2007 Funda Wang <fundawang@mandriva.org> 0.41.1-2mdv2008.0
+ Revision: 60769
- drop old menu
- New version 0.41.1


* Sun Mar 04 2007 Emmanuel Andry <eandry@mandriva.org> 0.41-2mdv2007.0
+ Revision: 131925
- rebuild for new libclamav

* Sat Feb 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.41-1mdv2007.1
+ Revision: 125377
- new version
- use --disable-rpath
- pass some other options into the %%configure
- drop sources 2,4,5
- use %%find_lang
- some cleans in spec file

* Thu Dec 14 2006 Emmanuel Andry <eandry@mandriva.org> 0.39-2mdv2007.1
+ Revision: 96844
- remove support for version older than MDV10.1

* Thu Dec 14 2006 Emmanuel Andry <eandry@mandriva.org> 0.39-1mdv2007.1
+ Revision: 96583
- New version 0.39
  drop patches 1 2 3 4 5

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Helio Chissini de Castro <helio@mandriva.com>
    - Fix for proxy cnofigurations. Not everyone use proxy with user and pwd.
    - Fixed media:/ or devices:/ patch
    - Added patch for translate html files. Still not the optimal solution, but
      works for current requirements
    - Added translation for .html about files
    - Fixded pt_BR translation. Patch will be submitted upstream
    - Added better ui handling by Gustavo Boiko <boiko@mandriva.com>, using media:/
      on KDE 3.5
    - No nrpoc compilation
    - Upload packages with OEM fixes
    - Created package structure for klamav.

* Tue Nov 22 2005 Laurent MONTEL <lmontel@mandriva.com> 0.32-1
- 0.32

* Fri Nov 18 2005 Oden Eriksson <oeriksson@mandriva.com> 0.22.1-2mdk
- rebuilt against openssl-0.9.8a

* Fri Aug 26 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.22.1-1mdk
- New release 0.22.1

* Tue Jul 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.22-1mdk
- New release 0.22

* Wed Jul 13 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.20.1-1mdk
- New release 0.20.1

* Fri May 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.20-1mdk
-  0.20

* Tue May 24 2005 Eskild Hustvedt <eskild@mandriva.org> 0.17.2-3mdk
- Rebuild

* Fri Apr 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.17.2-2mdk
- Fix BuildRequires

* Fri Apr 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.17.2-1mdk
- 0.17.2

* Wed Apr 13 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.17-1mdk
- 0.17
- rediff P0
- nuke rpath

* Sat Apr 09 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.12.1-1mdk
- 0.12.1
- use the %%mkrel macro
- fix description
- fix P0, in another place

* Sat Oct 16 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.06-1mdk
- 0.06

* Wed Sep 29 2004 Buchan Milne <bgmilne@linux-mandrake.com> 0.05-1mdk
- first Mandrake package
- p0 to use our clamav-db path

