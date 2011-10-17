%define oname kio-sysinfo
Name: kde3-%oname
Version: 1.8.2
Release: %mkrel 14
Summary: KIO Slave sysinfo:/
License: LGPL
Group: System/Libraries
URL: http://www.kde-apps.org/content/show.php?content=58704
Source0: http://download.tuxfamily.org/kiosysinfo/Sources/%oname-%version.tar.gz
# Source1:	48x48/apps/kcmprocessor.png
Source1:	cpu.png
# Source2:	48x48/devices/system.png
Source2:	sysinfo.png
Patch0: kio-sysinfo-1.8.2-suse-10.3.patch
Patch1: kio-sysinfo-1.8.2-uz-translation.patch
Patch2: kio-sysinfo-1.8.2-gcc4.patch
Patch3: kde-3.5.10-acinclude.patch
Patch4: fix_autotools.patch
BuildRequires: kdelibs-devel
BuildRequires: hal-devel
BuildRequires: dbus-devel
BuildRequires: libhd-devel
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%endif
BuildRequires: autoconf >= 1:2.65
BuildRequires: automake >= 1.6.1
BuildRequires: kde3-macros
BuildRoot: %{_tmppath}/%{name}-%{version}
Obsoletes: sysinfo < 1.8.2-4

%description
KIO Slave sysinfo:/. It shows various information about your pc, 
like cpu, ram. kernel version, exc. It also shows the removable 
devices and partition (total space/available space) and you can open,
mount and unmount it from this KIO slave.

%files -f kio_sysinfo.lang
%defattr(-,root,root)
%{_kde3_libdir}/kde3/*
%{_kde3_datadir}/applications/kde/kfmclient_sysinfo.desktop
%{_kde3_appsdir}/sysinfo
%{_kde3_datadir}/mimelnk/application/x-sysinfo.desktop
%{_kde3_datadir}/services/ksysinfopart.desktop
%{_kde3_datadir}/services/sysinfo.protocol

#--------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%if %mdkversion >= 201000
%patch3 -p1
%patch4 -p1
%endif
%__cp -f %SOURCE1 about/images/cpu.png
%__cp -f %SOURCE2 about/images/sysinfo.png

%build
make -f admin/Makefile.common

%configure_kde3 \
	--with-qt-dir=%{qt3dir} \
	--with-qt-includes=%{qt3include} \
	--with-qt-libraries=%{qt3lib}

%make

%install
rm -rf %buildroot

%makeinstall_std

%{find_lang} kio_sysinfo

%clean
rm -rf %{buildroot}


%changelog

* Thu Jul 14 2011 Tim Williams <tim@my-place.org.uk> 1.8.2-14mvt2010.2
+ rebuild for trinity KDE

* Mon Jul 19 2010 Tim Williams <tim@my-place.org.uk> 1.8.2-13mvt2010
+ Rebuild for MDV 2010.1

* Sun Feb 07 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 1.8.2-12mvt2010
+ Fix built with autoconf 2.65 and asutmoake 1.11

* Fri Nov 13 2009 Tim Williams <tim@my-place.org.uk> 1.8.2-11mdv2010.0
+ Rebuild for MDV 2010.0

* Tue Jun 24 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1.8.2-10mdv2009.0
+ Revision: 228752
- Fix specfile name
- Fix with new name

* Sun Jun 08 2008 Funda Wang <fundawang@mandriva.org> 1.8.2-10mdv2009.0
+ Revision: 216987
- rebuild for new major of hwinfo

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 1.8.2-9mdv2009.0
+ Revision: 204707
- Move to /opt

* Tue Apr 01 2008 Nicolas Lécureuil <neoclust@mandriva.org> 1.8.2-8mdv2008.1
+ Revision: 191468
- Use neutral icon again

* Wed Mar 26 2008 Helio Chissini de Castro <helio@mandriva.com> 1.8.2-7mdv2008.1
+ Revision: 190353
- Fix for bug https://qa.mandriva.com/show_bug.cgi?id=39173 - Proper dbus/hal device handling

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 1.8.2-6mdv2008.1
+ Revision: 141781
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 21 2007 Funda Wang <fundawang@mandriva.org> 1.8.2-5mdv2008.1
+ Revision: 100829
- Updated patch0 from bug#32822

* Fri Oct 12 2007 Funda Wang <fundawang@mandriva.org> 1.8.2-4mdv2008.1
+ Revision: 97268
- Rename to kio-sysinfo as sysinfo is too confusing

* Thu Sep 27 2007 Funda Wang <fundawang@mandriva.org> 1.8.2-3mdv2008.0
+ Revision: 93343
- really fix bug#32031

* Tue Aug 28 2007 Helio Chissini de Castro <helio@mandriva.com> 1.8.2-2mdv2008.0
+ Revision: 72846
- Fix mimelnk placement

* Tue Aug 21 2007 Funda Wang <fundawang@mandriva.org> 1.8.2-1mdv2008.0
+ Revision: 68729
- New version 1.8.2

  + Eskild Hustvedt <eskild@mandriva.org>
    - Fixed description

* Sat Aug 04 2007 Funda Wang <fundawang@mandriva.org> 1.8.1-1mdv2008.0
+ Revision: 58918
- Rediff uz patch

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version
    - bzip2 sources

* Wed Jul 25 2007 Funda Wang <fundawang@mandriva.org> 1.8-2mdv2008.0
+ Revision: 55432
- Add uz translation to fix mdvbug#32031

* Tue Jul 24 2007 Funda Wang <fundawang@mandriva.org> 1.8-1mdv2008.0
+ Revision: 55039
- New version
- uz translation has been merged upstream
- do not use autotools for kde packages
- use aclocal
- BR libhd
- Replace images with icons here: http://www.kde-look.org/content/show.php?content=61727
- New verison
- rediff patch

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - New patch for Uzbek translations (thanks  to Mashrab Kuvatov)
    - [FEATURE] Add Uzbek translations ( thanks to Mashrab Kuvatov) (bug report #32031)

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 1.3-4mdv2008.0
+ Revision: 36204
- rebuild with correct optflags

  + Nicolas Lécureuil <neoclust@mandriva.org>
    -Patch0: Make Sysinfo:/ display Mandriva Linux on System: instead of nothing

* Mon Jun 04 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1.3-2mdv2008.0
+ Revision: 35108
- Fix File List
- Import sysinfo

