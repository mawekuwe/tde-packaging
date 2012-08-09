# Default version for this component
%define kdecomp krename
%define version 3.0.14
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{tde_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_includedir %{tde_includedir}/kde
%define tde_libdir %{tde_libdir}/kde3


Name:		trinity-%{kdecomp}
Summary:	A KDE batch file renaming utility. 
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Source0:	%{kdecomp}-3.5.12.tar.gz

BuildRequires: tqtinterface-devel
BuildRequires: trinity-tdelibs-devel
BuildRequires: trinity-tdebase-devel
BuildRequires: desktop-file-utils
BuildRequires: imlib-devel

%description
KRename is a powerful batch renamer for KDE 3.x. It allows you to easily rename hundreds or
even more files in one go. The filenames can be created by parts of the original filename,
numbering the files or accessing hundreds of informations about the file, like creation date
or Exif informations of an image. 

%prep
%setup -q -n applications/%{kdecomp}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{tde_includedir}/tqt \
    --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%make_install


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/*
%{tde_datadir}/applications/*/*.desktop
%{tde_datadir}/apps/*/
%{tde_tdedocdir}/HTML/en/*/
%{tde_datadir}/icons/*/*/*/*
%{tde_datadir}/locale/*/*/*.mo


%Changelog
* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 3.0.14-2
- Import to GIT

* Wed Aug 24 2011 Francois Andriot <francois.andriot@free.fr> - 3.0.14-1
- Correct macro to install under "/opt", if desired

* Sun Aug 14 2011 Francois Andriot <francois.andriot@free.fr> - 3.0.14-0
- Initial build for RHEL 6.0

