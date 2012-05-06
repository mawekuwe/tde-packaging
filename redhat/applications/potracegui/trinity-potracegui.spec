# Default version for this component
%define kdecomp potracegui
%define version 1.3
%define release 1

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


Name:		trinity-%{kdecomp}
Summary:	KDE frontend for potrace [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Multimedia

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
A KDE interface for the commandline tracing tools potrace and/or autotrace. It
supports drag and drop as well as all image types recognized by KDE, which are
a lot more than the 4 recognized by the potrace commandline tool. Loading of
remote files (web, ftp, ...) is also supported.  


%prep
unset QTDIR; . /etc/profile.d/qt.sh
%setup -q -n applications/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
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

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/potracegui
%{_datadir}/applnk/Utilities/potracegui.desktop
%{_datadir}/apps/potracegui/potraceguiui.rc
%{tde_docdir}/HTML/en/potracegui/common
%{tde_docdir}/HTML/en/potracegui/index.cache.bz2
%{tde_docdir}/HTML/en/potracegui/index.docbook
%{_datadir}/icons/hicolor/16x16/apps/potracegui.png
%{_datadir}/icons/hicolor/32x32/apps/potracegui.png
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/potracegui.mo


%Changelog
* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 1.3-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

