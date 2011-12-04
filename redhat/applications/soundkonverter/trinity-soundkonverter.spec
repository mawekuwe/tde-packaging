# Default version for this component
%define kdecomp soundkonverter
%define version 0.3.8
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	audio converter frontend for Trinity
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Application/Multimedia

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://potracegui.sourceforge.net

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils


%description
soundKonverter is a frontend to various audio converters.

The key features are:
 - Audio conversion
 - Replay Gain calculation
 - CD ripping

soundKonverter supports reading and writing tags for many formats, so the tags
are preserved when converting files.

It comes with an Amarok script.

See 'soundkonverter-amarok' package for more informations.

See README.Debian for more informations on supported formats.


%package amarok
Summary:		audio converter frontend for Trinity (Amarok script)
Group:			Application/Multimedia
Requires:		%{name} = %{version}-%{release}
Requires:		trinity-amarok

%description amarok
Amarok script for soundKonverter. It allows you to easily transcode files when
transferring them to your media device.

See the 'soundkonverter-trinity' package for more information.


%prep
unset QTDIR; . /etc/profile.d/qt.sh
%setup -q -n applications/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i "admin/acinclude.m4.in" \
	-e "s,/usr/include/tqt,%{_includedir}/tqt,g" \
	-e "s,kde_htmldir='.*',kde_htmldir='%{tde_docdir}/HTML',g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt:/usr/include/cdda \
    --enable-closure
   
%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{kdecomp}

%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/soundkonverter
%{_bindir}/userscript.sh
%{_datadir}/applications/kde/soundkonverter.desktop
%{_datadir}/apps/konqueror/servicemenus/audiocd_extract_with_soundkonverter.desktop
%{_datadir}/apps/soundkonverter
%exclude %{_datadir}/apps/soundkonverter/amarokscript/README
%exclude %{_datadir}/apps/soundkonverter/amarokscript/soundKonverter.rb
%{tde_docdir}/HTML/en/soundkonverter/common
%{tde_docdir}/HTML/en/soundkonverter/index.cache.bz2
%{tde_docdir}/HTML/en/soundkonverter/index.docbook
%{_datadir}/icons/hicolor/*/apps/soundkonverter*.png
%{_datadir}/mimelnk/application/x-la.soundkonverter.desktop
%{_datadir}/mimelnk/application/x-ofc.soundkonverter.desktop
%{_datadir}/mimelnk/application/x-ofr.soundkonverter.desktop
%{_datadir}/mimelnk/application/x-ofs.soundkonverter.desktop
%{_datadir}/mimelnk/application/x-shorten.soundkonverter.desktop
%{_datadir}/mimelnk/audio/amr.soundkonverter.desktop
%{_datadir}/mimelnk/audio/x-ape.soundkonverter.desktop
%{_datadir}/mimelnk/audio/x-bonk.soundkonverter.desktop
%{_datadir}/mimelnk/audio/x-pac.soundkonverter.desktop
%{_datadir}/mimelnk/audio/x-tta.soundkonverter.desktop
%{_datadir}/mimelnk/audio/x-wavpack-correction.soundkonverter.desktop
%{_datadir}/mimelnk/audio/x-wavpack.soundkonverter.desktop
%{_datadir}/mimelnk/video/x-flv.soundkonverter.desktop

%files amarok
%defattr(-,root,root,-)
%{_datadir}/apps/soundkonverter/amarokscript/README
%{_datadir}/apps/soundkonverter/amarokscript/soundKonverter.rb


%Changelog
* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.3.8-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

