# Default version for this component
%define kdecomp kchmviewer
%define version 3.1.2
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	CHM viewer for Trinity
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Patch0:		kchmviewer-3.5.13-ftbfs.patch

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils

%description
KchmViewer is a chm (MS HTML help file format) viewer, written in C++.
Unlike most existing CHM viewers for Unix, it uses Trolltech Qt widget
library, and does not depend on KDE or GNOME. However, it may be compiled
with full Trinity support, including Trinity widgets and KIO/KHTML. 

The main advantage of KchmViewer is non-English language support. Unlike
others, KchmViewer in most cases correctly detects help file encoding,
correctly shows tables of context of Russian, Korean, Chinese and Japanese
help files, and correctly searches in non-English help files (search for
MBCS languages - ja/ko/ch is still in progress).

Completely safe and harmless. Does not support JavaScript in any way,
optionally warns you before opening an external web page, or switching to
another help file. Shows an appropriate image for every TOC entry. 

KchmViewer Has complete chm index support, including multiple index entries,
cross-links and parent/child entries in index as well as Persistent bookmarks
support. Correctly detects and shows encoding of any valid chm file.


%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
  --disable-rpath \
  --with-x \
  --with-kde \
  --with-extra-includes=%{_includedir}/tqt \
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
touch --no-create %{_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{_datadir}/icons/crystalsvg || :

%postun
touch --no-create %{_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{_datadir}/icons/crystalsvg || :


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%doc ChangeLog COPYING FAQ README
%{_bindir}/kchmviewer
%exclude %{_libdir}/libchmfile.a
%exclude %{_libdir}/libkdeextra.a
%{tde_libdir}/kio_msits.la
%{tde_libdir}/kio_msits.so
%{_datadir}/applnk/kchmviewer.desktop
%{_datadir}/icons/crystalsvg/*/apps/kchmviewer.png
%{_datadir}/services/msits.protocol


%Changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 3.1.2-2
- Rebuilt for Fedora 17
- Fix post and postun
- Fix HTML directory location

* Sat Nov 19 2011 Francois Andriot <francois.andriot@free.fr> - 3.1.2-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
