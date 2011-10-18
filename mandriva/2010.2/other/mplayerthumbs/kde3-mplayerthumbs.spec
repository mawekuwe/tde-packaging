%define oname mplayerthumbs


Name: kde3-%{oname}
Version: 0.5b
Release: %mkrel 3
Summary: Thumbnail Generator for Video Files in KDE3 Konqueror, using MPlayer
Source0: http://xoomer.alice.it/rockman81/mplayerthumbs-%{version}.tar.bz2
Source1: sprocket1-large.png
Source2: sprocket1-medium.png
Source3: sprocket1-small.png
Patch0:  mplayerthumbs-0.5b-gcc-4.3.patch
Patch1:  make_preview_horizontal.patch
URL:     http://kde-apps.org/content/show.php?content=41180
Group:   Graphical desktop/KDE3
License: GPL
BuildRoot: %{_tmppath}/%{oname}-buildroot
Requires: mplayer
BuildRequires:	kde3-macros
BuildRequires:	kdelibs3-devel
BuildRequires:	libstdc++-devel


%description
%{oname} is a thumbnail generator for video files on KDE3 Konqueror.
Unlike the original konqueror plugin, it does not depend neither on xine nor
arts, instead it uses only mplayer.
You can take advantage of this on x86_64 systems, where you can use a 32bit
mplayer to load win32codecs. To configure the location of your mplayer binary
launch mplayerthumbsconfig.
Also it's faster than the xine plugin, since it can seek and play only a
limited number of frames.
It catches a random frame from 15% to 70%, checking also how contrasted is the
image, and dropping bad frames.


%prep
%setup -q -n %{oname}-%{version}
%patch0 -p0
%patch1 -p1
rm -rf src/sprocket*
cp -R %{SOURCE1} src
cp -R %{SOURCE2} src
cp -R %{SOURCE3} src

%build

%configure_kde3

%make

%install
%makeinstall_std
%find_lang videopreview && %__mv videopreview.lang %{oname}.lang

%clean
%__rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_kde3_bindir/mplayerthumbsconfig
%_kde3_libdir/kde3/videopreview.so
%_kde3_libdir/kde3/videopreview.la
%_kde3_appsdir/videothumbnail
%_kde3_datadir/config.kcfg/mplayerthumbs.kcfg
%_kde3_datadir/services/videopreview.desktop
%_kde3_docdir/*

%changelog
* Fri Jul 22 2011 Tim Williams <tim@my-place.org.uk> 0.5b-2mvt2010.2
- Build for Trinity

* Fri Jul 23 2010 Tim Williams <tim@my-place.org.uk> 0.5b-2mvt2010.1
- Build for MDV 2010.1

* Thu Dec 24 2009 Atilla ÖNTAŞ <atilla_ontas@mandriva.org> 0.5b-1mvt2010.0
 - Built for 2010.0

