#See here :http://wiki.mandriva.com/en/Underlinking#Problems_introduced_by_--no-undefined 
%define _disable_ld_no_undefined 1


%define	name	kde3-ktorrent
%define	oname	ktorrent
%define	version 3.5.12
%define	rel	1
%define kde3_miconsdir %_kde3_iconsdir/mini
%define kde3_liconsdir %_kde3_iconsdir/large
# Note that this package does not follow the library policy as the
# main package includes the libktorrent shared object. This is done
# because 1) the library is only used internally by ktorrent, and so
# it does never need to be installed separately, and 2) the %major
# follows %version, thus resulting in one unuseful library package
# in every ktorrent version upgrade. The only downside of not
# following the library policy on this particular package I know is
# rpmlint going nuts.
#
# Feel free to flame me if you do not like this...
# -Anssi

%define major %version

Summary:	BitTorrent program for KDE
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Group:		Networking/File transfer
License:	GPLv2+
Url:		http://ktorrent.org/
Source0:	http://ktorrent.org/downloads/%{version}/%{oname}-%{version}.tar.bz2
Patch0:		ktorrent-fix-KBytesPerSecToString.diff
Patch1:		ktorrent-php-path.patch
Patch2:		kde-3.5.10-acinclude.patch
#Patch3:		fix_autotools.patch
Patch7:                 kdebase-3.5.12-move-xdg-menu-dir.patch
Patch8:                 kdebase-3.5.12-config.patch
BuildRoot:	%{_tmppath}/%{oname}-%{version}-%{release}-buildroot
BuildRequires:	kde3-macros
%if %mdkversion < 201000
BuildRequires:	autoconf <= 1:2.63
%else
BuildRequires:	autoconf >= 1:2.65
%endif
BuildRequires:	automake >= 1.6.1
BuildRequires:	gmp-devel
BuildRequires:	kdelibs-devel
BuildRequires:	desktop-file-utils
Obsoletes:	%{_lib}ktorrent0 %{_lib}ktorrent2.1 %{_lib}ktorrent2.1.1
Obsoletes:	%{_lib}ktorrent2.1.2 %{_lib}ktorrent2.1.3

%description
KTorrent is a BitTorrent program for KDE. It's main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

%prep
%setup -q -n %{oname}-%{version}
%patch0
%patch1
%if %mdkversion >= 201000
%patch2 -p1
#%patch3 -p1
%endif

%patch7 -p0
%patch8 -p0

%build
PATH=%{qt3dir}/bin:%{_kde3_bindir}:$PATH; export PATH;
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/kde3/lib/
export xdg_menudir=%_sysconfdir/xdg/kde/menus
make -f admin/Makefile.common
%configure_kde3	--disable-debug \
		--enable-mt \
		--disable-static \
		--enable-shared \
		--disable-objprelink \
		--with-pic \
		--with-gnu-ld \
		--disable-embedded \
		--enable-fast-install=yes \
		--with-qt-dir=%{qt3dir} \
		--with-xinerama \
		--enable-final
%make
 
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

desktop-file-install --vendor="" \
	--add-category="P2P" \
	--dir %{buildroot}%_kde3_datadir/applications/kde \
	%{buildroot}%_kde3_datadir/applications/kde/ktorrent.desktop

install -m644 apps/ktorrent/hi16-app-ktorrent.png -D $RPM_BUILD_ROOT%kde3_miconsdir/%{oname}.png
install -m644 apps/ktorrent/hi32-app-ktorrent.png -D $RPM_BUILD_ROOT%_kde3_iconsdir/%{oname}.png
install -m644 apps/ktorrent/hi48-app-ktorrent.png -D $RPM_BUILD_ROOT%kde3_liconsdir/%{oname}.png

%find_lang %{oname}
rm -f $RPM_BUILD_ROOT%_kde3_libdir/libktorrent.{so,la}

#Fix Conflictss with kdelibs-common
rm -f $RPM_BUILD_ROOT%_kde3_datadir/mimelnk/application/x-bittorrent.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
/sbin/ldconfig
%update_menus
%update_desktop_database
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
/sbin/ldconfig
%clean_menus
%clean_desktop_database
%clean_icon_cache hicolor
%endif

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS README
%_kde3_bindir/*
%_kde3_libdir/kde3/*
%_kde3_libdir/libktorrent-2.2.6.so
%_kde3_datadir/services/*
%_kde3_datadir/servicetypes/*
%_kde3_datadir/apps/%{oname}
%_kde3_datadir/applications/kde/%{oname}.desktop
%_kde3_datadir/config.kcfg/*.kcfg
%_kde3_iconsdir/hicolor/scalable/apps/%{oname}.svgz
%kde3_miconsdir/%{oname}.png
%_kde3_iconsdir/%{oname}.png
%kde3_liconsdir/%{oname}.png
%_kde3_iconsdir/hicolor/*/apps/*.png
%_kde3_iconsdir/hicolor/*/mimetypes/*.png
%_kde3_iconsdir/hicolor/*/mimetypes/*.svgz
