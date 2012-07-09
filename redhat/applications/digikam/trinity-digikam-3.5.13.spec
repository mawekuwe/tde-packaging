# Default version for this component
%define kdecomp digikam

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%define _mandir %{_datadir}/man
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_appdir %{_datadir}/applications/kde
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	digital photo management application for KDE [Trinity]
Version:	0.9.6
Release:	2%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# TDE 3.5.13 on RHEL/Fedora specific patches
Patch1:		digikam-3.5.13-jpegint-ftbfs.patch
# [digikam] Add support for libpng 1.4 [Bug #595]
Patch2:		digikam-3.5.13-fix_libpng_1.4.patch
# [digikam] gcc 4.7 + libpng 1.5 patch for digikam (consolidated) [Bug #958]
Patch3:		digikam-3.5.13-libpng15+gcc47_1.patch
# [digikam] Fix libpng support (again !!!)
Patch4:		digikam-3.5.13-fix_libpng_support.patch
# [digikam] Fix compilation with GCC 4.7
Patch5:		digikam-3.5.13-fix_gcc47_compilation.patch

BuildRequires: tqtinterface-devel
BuildRequires: trinity-arts-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: trinity-libkexiv2-devel
BuildRequires: trinity-libkdcraw-devel
BuildRequires: trinity-libkipi-devel
%if 0%{?rhel} == 5
BuildRequires: gphoto2-devel
%else
BuildRequires: libgphoto2-devel
%endif
BuildRequires: libtiff-devel
BuildRequires: jasper-devel
BuildRequires: exiv2-devel


%description
An easy to use and powerful digital photo management
application, which makes importing, organizing and manipulating
digital photos a "snap".  An interface is provided to connect to
your digital camera, preview the images and download and/or
delete them.

The digiKam built-in image editor makes the common photo correction
a simple task. The image editor is extensible via plugins and,
the digikamimageplugins project has been merged to digiKam core
since release 0.9.2, all useful image editor plugins are available
in the base installation.

digiKam can also make use of the KIPI image handling plugins to
extend its capabilities even further for photo manipulations,
import and export, etc. The kipi-plugins package contains many
very useful extentions.

digiKam is based in part on the work of the Independent JPEG Group.


%package devel
Group:		Development/Libraries
Summary:	Development files for %{name}
Requires:	%{name} = %{version}

%description devel
%{summary}


%prep
%setup -q -n applications/%{kdecomp}
%patch1 -p5
%patch2 -p1
%patch3 -p1
%patch4 -p1 -b .libpng
%if 0%{?fedora} >= 17
%patch5 -p1 -b .gcc47
%endif

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt \
    --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}



%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
/sbin/ldconfig

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
/sbin/ldconfig

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/*
%{_libdir}/*.so.*
%{tde_appdir}/*.desktop
%{_datadir}/locale/*/LC_MESSAGES/digikam.mo
%{_datadir}/services/*.desktop
%{_datadir}/services/*.protocol
%{_datadir}/servicetypes/digikamimageplugin.desktop
%{_datadir}/apps/*/
%{tde_docdir}/HTML/en/*/
%{_datadir}/icons/hicolor/*/*/*
%{_mandir}/man*/*
%{tde_libdir}/*.so
%{tde_libdir}/*.la


%files devel
%{_includedir}/*.h
%{_includedir}/digikam/
%{_libdir}/*.so
%{_libdir}/*.la


%Changelog
* Sun Jul 08 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.6-3
- Fix man directory location
- Fix postinstall
- Fix description
- Add "BuildRequires: exiv2-devel"

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.6-2
- gcc 4.7 + libpng 1.5 patch for digikam (consolidated) [Bug #958]

* Sun Nov 06 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.6-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

