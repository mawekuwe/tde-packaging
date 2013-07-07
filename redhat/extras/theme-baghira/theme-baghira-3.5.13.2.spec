# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# Speed build options
%define debug_package %{nil}
%define __spec_install_post %{nil}
AutoReq: no

# TDE 3.5.13 specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:                   trinity-theme-baghira
Version:                0.8
Release:                2%{?dist}%{?_variant}
Summary:                Baghira theme for Trinity
License:                GPL
Group:                  Graphical desktop/KDE
Source0:                http://prdownloads.sourceforge.net/baghira/baghira-0.8.tar.bz2
Source1:                admin-3.5.13.2.tar.gz
Patch0:                 baghira-3.5.13.1-fix_ftbfs.patch
Patch1:					baghira-0.8-fix_autotools.patch
Url:                    http://baghira.sourceforge.net/
BuildRoot:              %{_tmppath}/baghira-%{version}-buildroot

BuildRequires:          qt3-devel
BuildRequires:          trinity-tdebase-devel >= 3.5.13.2

%if 0%{?fedora} || 0%{?rhel} || 0%{?suse_version}
BuildRequires:          libjpeg-devel
%else
BuildRequires:          X11-devel
BuildRequires:          jpeg-devel
%endif

%description
Baghira is a very nice native Trinity style and windec
originally based on Mosfet's Liquid style.

This package contains non-free icons..

%package devel
Summary:        Header files and static libraries from %name
Group:          Development/C
Requires:		%{name} = %{version}-%{release}

%description devel
Libraries and includes files for
developing programs based on %name

This package is in PLF because it contains non-free icons.

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

%prep
%setup -q -n baghira-%{version} -a 1
%patch0 -p1 -b .ftbfs
%patch1 -p1 -b .autotools

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i "admin/acinclude.m4.in" \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"

%build
unset QTDIR || : ; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export KDEDIR=%{tde_prefix}

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --includedir=%{tde_tdeincludedir} \
  --datadir=%{tde_datadir} \
  --with-qt-libraries=${QTLIB:-${QTDIR}/%{_lib}} \
  --disable-static \
  --disable-rpath \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final \
  --with-extra-includes=%{tde_includedir}/tqt

%__make %{?_smp_mflags}

%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

install -d %{buildroot}/%{tde_libdir}/baghira-%{version}
install -d %{buildroot}/%{tde_tdeincludedir}/baghira-%{version}

mv %{buildroot}/%{tde_libdir}/libbaghirastarter.la %{buildroot}/%{tde_libdir}/baghira-%{version}/libbaghirastarter.la
mv %{buildroot}/%{tde_libdir}/libbaghirastarter.so %{buildroot}/%{tde_libdir}/baghira-%{version}/libbaghirastarter.so.%{major}
mv %{buildroot}/%{tde_libdir}/usermanager_panelapplet.la %{buildroot}/%{tde_libdir}/baghira-%{version}/usermanager_panelapplet.la
mv %{buildroot}/%{tde_libdir}/usermanager_panelapplet.so %{buildroot}/%{tde_libdir}/baghira-%{version}/usermanager_panelapplet.so.%{major}
mv %{buildroot}/%{tde_tdeincludedir}/baghirasidebar.h %{buildroot}/%{tde_tdeincludedir}/baghira-%{version}/baghirasidebar.h
mv %{buildroot}/%{tde_tdeincludedir}/baghirasidebariface.h %{buildroot}/%{tde_tdeincludedir}/baghira-%{version}/baghirasidebariface.h
mv %{buildroot}/%{tde_tdeincludedir}/dndlistbox.h %{buildroot}/%{tde_tdeincludedir}/baghira-%{version}/dndlistbox.h
mv %{buildroot}/%{tde_tdeincludedir}/linkview.h %{buildroot}/%{tde_tdeincludedir}/baghira-%{version}/linkview.h
mv %{buildroot}/%{tde_tdeincludedir}/listboxlink.h %{buildroot}/%{tde_tdeincludedir}/baghira-%{version}/listboxlink.h

ln -s libbaghirastarter.so.%{major} %{buildroot}/%{tde_libdir}/baghira-%{version}/libbaghirastarter.so
ln -s usermanager_panelapplet.so.%{major} %{buildroot}/%{tde_libdir}/baghira-%{version}/usermanager_panelapplet.so


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog COPYING NEWS TODO
%{tde_bindir}/bab
%{tde_tdelibdir}/b_menu_panelapplet.*
%{tde_tdelibdir}/kstyle_baghira_config.*
%{tde_tdelibdir}/kwin3_baghira.*
%{tde_tdelibdir}/kwin_baghira_config.*
%{tde_tdelibdir}/plugins/styles/baghira.*
%{tde_datadir}/apps/kdisplay/color-schemes/Aqua*
#%{tde_datadir}/apps/kicker/applets/b_menuapplet.desktop
%{tde_datadir}/apps/kicker/applets/usermanager.desktop
%{tde_datadir}/apps/konqsidebartng/add/baghirasidebar_add.desktop
%{tde_datadir}/apps/konqsidebartng/entries/baghirasidebar.desktop
%{tde_datadir}/apps/kicker/applets/starter.desktop
%{tde_datadir}/apps/kstyle/themes/baghira.themerc
%{tde_datadir}/apps/kwin/baghira.desktop
%{tde_datadir}/icons/crystalsvg/*/*/baghira*
%{tde_datadir}/icons/crystalsvg/*/*/bab_*
%{tde_datadir}/apps/baghira/poof.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bStarter.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bStarter_down.png
%{tde_datadir}/icons/crystalsvg/22x22/actions/bStarter_hover.png


%files devel
%defattr(-,root,root)
%{tde_libdir}/baghira-%{version}/libbaghirastarter.la
%{tde_libdir}/baghira-%{version}/libbaghirastarter.so*
%{tde_tdelibdir}/konqsidebar_baghirasidebar.la
%{tde_tdelibdir}/konqsidebar_baghirasidebar.so
%{tde_libdir}/baghira-%{version}/usermanager_panelapplet.la
%{tde_libdir}/baghira-%{version}/usermanager_panelapplet.so*
%{tde_tdeincludedir}/baghira-%{version}/baghirasidebar.h
%{tde_tdeincludedir}/baghira-%{version}/baghirasidebariface.h
%{tde_tdeincludedir}/baghira-%{version}/dndlistbox.h
%{tde_tdeincludedir}/baghira-%{version}/linkview.h
%{tde_tdeincludedir}/baghira-%{version}/listboxlink.h


%changelog
* Sat Jan 19 2013 Francois Andriot <francois.andriot@free.fr> - 0.8-2
- Initial release for TDE 3.5.13.2

* Tue Nov 20 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.1
- Initial build for TDE 3.5.13.1

* Tue Jan 8 2008 Javier Rodas <jrodas@zarb.org> 0.8-2plf2008.1
- KDE 3.5.8 version in Mandriva 2008.1
- KDE svn admin headers now packaged in Source1

* Mon Sep 18 2006 Javier Rodas <jrodas@zarb.org> 0.8-2plf2007.0
- Fix Source0 local reference
- KDE 3.5.4 admin headers are downloaded with subversion
- Fix Baghira devel package directory paths
- Fix BuildRequires

* Fri Sep 15 2006 Javier Rodas <jrodas@zarb.org> 0.8-1plf2007.0
- 0.8
- Replaced KDE admin headers in the source file (for KDE 3.5.4)
- Fix BuildRequires
- Removed the patch file

* Thu Oct 13 2005 neoclust <neoclust@mandriva.com> 0.7-1plf
- 0.7
- remove redundant buildrequires

* Mon Mar 04 2005 Nicolas L�ureuil <neoclust@zarb.org> 0.6-3plf
- Add PLF reason
- bzipped patch 
- Make rpmlint happier

* Mon Mar 04 2005 Nicolas L�ureuil <neoclust@zarb.org> 0.6-2plf
- New version
- Fix compile ( Patch0 from Gentoo)
- Spec Cleanup
- rpmbuildupdatable

* Mon Dec 06 2004 Laurent Culioli <laurent@zarb.org> 0.6-1plf
- Initial Release.
