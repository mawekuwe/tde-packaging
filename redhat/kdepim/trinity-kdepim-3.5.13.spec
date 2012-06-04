# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: cmake >= 2.8
%define tde_docdir %{_docdir}/kde
%define tde_libdir %{_libdir}/trinity

# KDEPIM specific features
%if 0%{?fedora}
%define with_gnokii 1
%else
%define with_gnokii 0
%endif


Name:		trinity-kdepim
Version:	3.5.13
Release:	6%{?dist}%{?_variant}
License:	GPL
Group:		Applications/Productivity

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
Summary:	PIM (Personal Information Manager) applications

Prefix:		%{_prefix}

Source0:	kdepim-%{version}.tar.gz

# [kdepim] Fix compilation with GCC 4.7 [Bug #958]
Patch1:		kdepim-3.5.13-fix_gcc47_compilation.patch
# [tdepim] Reverse patch from GIT hash 33e649c9. [Bug #406] [Commit #2d5f15c8]
Patch2:		kdepim-3.5.13-fix_check_mail.patch
# [tdepim] Fix kmail composer crash [Bug #953]
Patch3:		kdepim-3.5.13-fix_composer_crash.patch
# [tdepim] Fix KMail counting of unread messages in the system tray icon [Commit #40c435e5]
Patch4:		kdepim-3.5.13-fix_systray_count.patch
# [tdepim] Fix knotes not appearing on the desktop when a session is restored. [Bug #987] [Commit #533f494f]
Patch5:		kdepim-3.5.13-fix_knotes_after_restored.patch
# [tdepim] Fix knotes to not close notes during saving session. [Bug #987] [Commit #c48253af]
Patch6:		kdepim-3.5.13-fix_knotes_on_suspend.patch
# [tdepim] Fix linear alphabet string errors [Bug 635] [Commit #80bc593e]
Patch7:		kdepim-3.5.13-fix_linear_alphabet.patch
# [tdepim] Fix infinite loop on IMAP4 authentication failure [Bug #1007]
Patch8:		kdepim-3.5.13-fix_kio_imap4_infinite_loop.patch
# [tdepim] Fix infinite loop on kmime_utils addquotes
Patch9:		kdepim-3.5.13-fix_kio_imap4_addquotes.patch
Patch10:	kdepim-3.5.13-fix_segv.patch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	gpgme-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	flex
BuildRequires:	libical-devel
BuildRequires:	boost-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	libXcomposite-devel
BuildRequires:	pcre-devel
BuildRequires:	glib2-devel
BuildRequires:	gcc-c++ make

BuildRequires:	libcaldav-devel
BuildRequires:	libcarddav-devel

%if 0%{?with_gnokii}
BuildRequires:	gnokii-devel
%endif

%if 0%{?fedora} >= 15
BuildRequires:	flex-static
%endif
%if 0%{?rhel} >= 0 && 0%{?rhel} <= 5
BuildRequires:	trinity-libcurl-devel
%else
BuildRequires:	curl-devel
%endif

Requires:	trinity-kdelibs
Requires:	libcaldav
Requires:	libcarddav

%description
PIM (Personal Information Manager) applications.


%package devel
Requires:	%{name}
Summary:	%{name} - Development files
Group: Development/Libraries
%description devel
Development files for %{name}.


%prep
%setup -q -n kdepim
%patch1 -p1 -b .gcc47
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1 -b .addquotes
%patch10 -p1 -b .segv


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{_libdir}/pkgconfig"
export CMAKE_INCLUDE_PATH="%{_includedir}:%{_includedir}/tqt"
export LD_LIBRARY_PATH="%{_libdir}"

%__mkdir build
cd build
%cmake \
  -DWITH_ARTS=ON \
  -DWITH_SASL=ON \
  -DWITH_NEWDISTRLISTS=ON  \
%if 0%{?with_gnokii}
  -DWITH_GNOKII=ON \
%else
  -DWITH_GNOKII=OFF \
%endif
  -DWITH_EXCHANGE=ON \
  -DWITH_EGROUPWARE=ON \
  -DWITH_KOLAB=ON \
  -DWITH_SLOX=ON \
  -DWITH_GROUPWISE=ON \
  -DWITH_FEATUREPLAN=ON \
  -DWITH_GROUPDAV=ON \
  -DWITH_BIRTHDAYS=ON \
  -DWITH_NEWEXCHANGE=ON \
  -DWITH_SCALIX=ON \
  -DWITH_CALDAV=ON \
  -DWITH_CARDDAV=ON \
  -DWITH_INDEXLIB=ON \
  -DBUILD_ALL=ON \
  ..

%__make  %{?_smp_mflags}

%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

%clean
%__rm -rf %{?buildroot}

%post
for f in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${f} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${f} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/applnk/.hidden/*
%{_datadir}/applnk/*/*
%{_datadir}/apps/*
%{_datadir}/autostart/*.desktop
%{_datadir}/config/*
%{_datadir}/icons/*
%exclude %{_datadir}/icons/default.kde
%{_datadir}/services/*
%{_datadir}/mimelnk/application/*
%{_datadir}/config.kcfg/*
%{_libdir}/lib*.so.*
%{tde_libdir}/*.so
%{tde_libdir}/*.la
%{tde_libdir}/plugins/designer/*.so
%{tde_libdir}/plugins/designer/*.la
%{_datadir}/servicetypes/*
%{_libdir}/kconf_update_bin/*
%{_libdir}/libakregatorprivate.so
%{_libdir}/libkmailprivate.so
%{_libdir}/libkmobiledevice.so
%{tde_docdir}/HTML/en/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*
%exclude %{_libdir}/libakregatorprivate.so
%exclude %{_libdir}/libkmailprivate.so
%exclude %{_libdir}/libkmobiledevice.so
%{_datadir}/cmake/*.cmake

%changelog
* Sun May 27 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-5
- Fix KMail counting of unread messages in the system tray icon [Commit #40c435e5]
- Fix knotes not appearing on the desktop when a session is restored. [Bug #987] [Commit #533f494f]
- Fix knotes to not close notes during saving session. [Bug #987] [Commit #c48253af]
- Fix linear alphabet string errors [Bug 635] [Commit #80bc593e]
- Fix infinite loop on IMAP4 authentication failure [Bug #1007]

* Wed Apr 25 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Fix compilation with GCC 4.7 [Bug #958]
- Reverse patch from GIT hash 33e649c9. [Bug #406] [Commit #2d5f15c8]
- Fix kmail composer crash [Bug #953]

* Sun Nov 27 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Add missing files '*.la'

* Fri Nov 04 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Updates BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Mon Sep 05 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.12-0
- Import to GIT
