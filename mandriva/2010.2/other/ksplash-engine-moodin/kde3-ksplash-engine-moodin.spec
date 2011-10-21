%define oldname ksplash-engine-moodin
Name: kde3-%{oldname}
Version: 0.4.2
Release: %mkrel 19
Summary: Splash Screen Engine for KDE3
License:   GPL
URL:       http://moodwrod.com/
Group:     Graphical desktop/KDE3
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:    http://moodwrod.com/files/%{oldname}_0.4.2.tar.bz2
# a Qt4 based Svg render to be used in moodin
Source1:   svgrender.tar.bz2
Patch1:    moodin-autoconf.patch
Patch2:    moodin-0.4.2-fix-bug.patch
Patch3:    moodin-0.4.2-memleak-bug.patch
Patch4:    moodinkde-use-svg.patch
Patch5:    moodin-use-label-offset.patch
Patch6:    moodin-fix-svg.patch
Patch7:    moodin-automake.patch
Patch8:    moodin-external_svgrender.patch 
Patch9:    moodin-fix_drawing_on_compiz.patch
Patch10:   moodin-drawing_and_scaling_fixes.patch
Patch11:   moodin-fix_svg_on_base_resolution.patch
Patch12:   kde-3.5.10-acinclude.patch
Patch13:   moodin-kdehome-kde3.patch
BuildRequires:	kde3-macros
BuildRequires:	libkde3base4-devel
BuildRequires:	art_lgpl-devel
# for the svgrender
BuildRequires:  qt4-devel
%if %mdkversion < 201000
BuildRequires: autoconf <= 1:2.63
%else
BuildRequires: autoconf >= 1:2.65
%endif
BuildRequires: automake >= 1.6.1
Obsoletes: %{oldname}
Provides: %{oldname}

%description
Splash Screen Engine for KDE3
Heavily customizable engine for various types of themes

FEATURES:
- Scale cache
- Fading images
- Use current icon set or custom images
- Unlimited Custom text labels
- Set fading delay and length
- Custom image arrangement
- Resolution independent themes


%prep
rm -rf %buildroot

%setup -q -n moodin -a1

%patch1 -p1 -b .autoconf
%patch2 -p1 -b .fix_bug
%patch3 -p1 -b .fix_mem_leak
%patch4 -p1 -b .use_svg
%patch5 -p1 -b .use_status_offset
%patch6 -p1 -b .fix_svg
%patch7 -p1 -b .automake
%patch8 -p1 -b .external_svgrender
%patch9 -p1 -b .fix_drawing
%patch10 -p1 -b .fix_scaling
%patch11 -p1 -b .fix_svg_base_resolution
%if %mdkversion >= 201000
%patch12 -p1
%patch13 -p1
%endif


%build
make -f admin/Makefile.common
%configure_kde3

# svgrender 
pushd svgrender
  qmake
  make
popd

%install
rm -rf %buildroot
%{makeinstall_std}

# svgrender
mkdir -p %buildroot%_kde3_bindir
install -m0755 svgrender/svgrender %buildroot%_kde3_bindir/moodin_svgrender

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc COPYING INSTALL AUTHORS
%_kde3_bindir/moodin_svgrender
%_kde3_libdir/kde3/ksplashmoodin.la
%_kde3_libdir/kde3/ksplashmoodin.so
%_kde3_appsdir/ksplash/Themes/FingerPrint/*.png
%_kde3_appsdir/ksplash/Themes/FingerPrint/*.jpg
%_kde3_appsdir/ksplash/Themes/FingerPrint/Theme.rc
%_kde3_appsdir/ksplash/Themes/MoodinKDE/*.jpg
%_kde3_appsdir/ksplash/Themes/MoodinKDE/*.png
%_kde3_appsdir/ksplash/Themes/MoodinKDE/Theme.rc
%_kde3_datadir/services/ksplashmoodin.desktop




%changelog

* Thu Jul 14 2011 Tim Williams <tim@my-place.ortg.uk> 0.4.2-19mvt2010.2
+ rebuild for MDV 2010.2/Trinity KDE

* Mon Jul 19 2010 Tim Williams <tim@my-place.ortg.uk> 0.4.2-18mvt2010.1
+ Rebuild for MDV 2010.1

* Thu Feb 18 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.4.2-17mvt2010.0
+ Make default config dir as$HOME/.kde3 to avoid future conflicts with KDE4

* Fri Feb 12 2010 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.4.2-16mvt2010.0
+ KDE builds with autoconf 2.65, add patch for this and
  set autoconf to version 2.65
- Rename package name and group to avoid possible future kde4 conflicts

* Thu Nov 26 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.4.2-15mvt2010.0
+ Rename package to avoid unvanted KDE4 upgrade

* Fri Nov 13 2009 Tim Williams <tim@my-place.org.uk> 0.4.2-14mdv2009.0
+ Rebuild for MDV 2010.0

* Sun Jul 13 2008 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.2-13mdv2009.0
+ Revision: 234340
- Rebuild

* Thu May 08 2008 Helio Chissini de Castro <helio@mandriva.com> 0.4.2-12mdv2009.0
+ Revision: 204726
- Move to /opt

* Thu Feb 28 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.4.2-11mdv2008.1
+ Revision: 176248
- Fix svg rendering when the screen resolution is the same as the base resolution

* Wed Feb 27 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.4.2-10mdv2008.1
+ Revision: 175815
- Add a patch fixing many problems of Moodin:
   * Inter-widget transparency
   * scaling images when using a svg background
   * Proper handling svg images.

* Tue Feb 26 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.4.2-9mdv2008.1
+ Revision: 175394
- Add a patch fixing drawing when compiz is running

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix no-buildroot-tag

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-8mdv2008.1
+ Revision: 141782
- rebuilt against openldap-2.4.7 libs

* Thu Dec 20 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 0.4.2-7mdv2008.1
+ Revision: 135891
- Fix automake 1.10 detection
- Use an external svg rendering helper (Qt4 based)

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Feb 14 2007 Laurent Montel <lmontel@mandriva.com> 0.4.2-6mdv2007.0
+ Revision: 120903
- Fix svg

* Wed Feb 14 2007 Laurent Montel <lmontel@mandriva.com> 0.4.2-5mdv2007.1
+ Revision: 120754
- Improve
- Fix other mem leak
- Fix some mem leak
- Fix configure
- Import ksplash-engine-moodin

* Mon Jul 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.2-2mdv2007.0
- Rebuild for new extension

* Sun Dec 18 2005 Sebastien Savarin <plouf@mandriva.org> 0.4.2-1mdk
- First Mandriva Linux release

