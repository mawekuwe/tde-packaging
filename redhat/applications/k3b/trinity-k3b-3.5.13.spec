# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:    trinity-k3b
Summary: CD/DVD burning application
Version: 3.5.13
Release: 4%{?dist}%{?_variant}

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if "%{?_prefix}" == "/usr"
Obsoletes: k3b
%endif

Group:   Applications/Archiving
License: GPLv2+

Source0: k3b-%{version}.tar.gz
Source2: k3brc

# Legacy RedHat / Fedora patches
# manual bufsize (upstream?)
Patch4: k3b-1.0.4-manualbufsize.patch

# RHEL6: Fix K3B icon
Patch106: trinity-k3b-icons.patch

# [k3b] Fix compilation with GCC 4.7 [Bug #958]
Patch108:	k3b-3.5.13-fix_Range_r_3-gcc47.patch

BuildRequires: trinity-kdelibs-devel
BuildRequires: desktop-file-utils
BuildRequires: alsa-lib-devel
BuildRequires: audiofile-devel
BuildRequires: dbus-tqt-devel hal-devel
BuildRequires: flac-devel
BuildRequires: gettext
BuildRequires: libdvdread-devel
BuildRequires: libmpcdec-devel
BuildRequires: libmusicbrainz-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
BuildRequires: taglib-devel
BuildRequires: zlib-devel

Obsoletes: k3b-extras < 0:1.0-1
Provides:  k3b-extras = %{version}-%{release} 

Requires(post): coreutils
Requires(postun): coreutils

Requires: %{name}-libs = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}

Requires: cdrecord mkisofs
Requires: cdrdao
Requires: dvd+rw-tools

%description
K3b provides a comfortable user interface to perform most CD/DVD
burning tasks. While the experienced user can take influence in all
steps of the burning process the beginner may find comfort in the
automatic settings and the reasonable k3b defaults which allow a quick
start.

%package common
Summary:  Common files of %{name}
Group:    Applications/Archiving
Requires: %{name} = %{version}-%{release}
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
BuildArch: noarch
%endif
%description common
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Group:   System Environment/Libraries
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Files for the development of applications which will use %{name} 
Group: Development/Libraries
Requires: %{name}-libs = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q -a 0 -n applications/k3b

# set in k3brc too 
%patch4 -p1 -b .manualbufsize
%patch106 -p1 -b .desktopfile
%patch108 -p1


# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

CFLAGS="%optflags -fno-strict-aliasing" \
CXXFLAGS="%optflags -fno-strict-aliasing" \
%configure \
  --includedir=%{_includedir}/k3b \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final \
  --with-k3bsetup=no \
  --without-cdrecord-suid-root \
  --with-oggvorbis \
  --with-flac \
  --with-external-libsamplerate \
  --with-libdvdread \
  --with-musicbrainz \
  --with-sndfile \
  --without-ffmpeg --without-lame --without-libmad \
  --with-musepack \
  --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}
%__install -D -m 644 -p %{SOURCE2} %{buildroot}%{_datadir}/config/k3brc

# remove the .la files
%__rm -f %{buildroot}%{_libdir}/libk3b*.la 

# remove i18n for Plattdeutsch (Low Saxon)
#%__rm -fr %{buildroot}%{_datadir}/locale/nds


%check
export PATH="%{_bindir}:${PATH}"
desktop-file-validate %{buildroot}%{_datadir}/applications/kde/k3b.desktop


%clean
%__rm -rf %{buildroot}


%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post common
touch --no-create %{_datadir}/icons/hicolor ||:

%postun common
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor &> /dev/null
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null
fi

%posttrans common
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null


%files
%defattr(-,root,root,-)
%doc AUTHORS README COPYING TODO ChangeLog
%{_bindir}/k3b
%{tde_libdir}/*.so
%{tde_libdir}/*.la
%{tde_docdir}/HTML/en/k3b

%files common
%defattr(-,root,root,-)
%{_datadir}/applications/kde/*.desktop
%{_datadir}/applnk/.hidden/*.desktop
%{_datadir}/apps/k3b/
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/videodvd.desktop
%{_datadir}/config/k3brc
%{_datadir}/mimelnk/application/x-k3b.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/services/kfile_k3b.desktop
%{_datadir}/services/videodvd.protocol
%{_datadir}/sounds/k3b_*.wav

%files libs
%defattr(-,root,root,-)
%{_libdir}/libk3b.so.3*
%{_libdir}/libk3bdevice.so.5*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/libk3b.so
%{_libdir}/libk3bdevice.so


%changelog
* Wed May 09 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-4
- Removes i18 files (built separately)

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Rebuilt for Fedora 17
- Fix compilation with GCC 4.7 [Bug #958]

* Sat Nov 05 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Updates BuildRequires

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sun Sep 11 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
