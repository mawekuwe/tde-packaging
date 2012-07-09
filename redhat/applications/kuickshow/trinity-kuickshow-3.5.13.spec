# Default version for this component
%define kdecomp kuickshow

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
Summary:	Quick picture viewer for KDE 
Version:	0.8.13
Release:	4%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [kuickshow] Rename old tq methods that no longer need a unique name [Commit #8712ab46]
Patch0:		bp000-8712ab46.diff
# [kuickshow] Remove additional unneeded tq method conversions [Commit #28d9c774]
Patch1:		bp001-28d9c774.diff
# [kuickshow] Rename obsolete tq methods to standard names [Commit #bdeb8b3a]
Patch2:		bp002-bdeb8b3a.diff
# [kuickshow] Remove inadvertent renaming [Commit #d97e403f] [Bug #863]
Patch3:		bp003-d97e403f.diff

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils
BuildRequires: imlib-devel

%description
Kuickshow is a picture viewer for KDE. It displays the directory structure,
displaying images as thumbnails.
Clicking on an image shows the image in its normal size. 


%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

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
%__make install DESTDIR=%{?buildroot}


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

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/*
%{_datadir}/applications/*/*.desktop
%{_datadir}/apps/*/
%{_datadir}/icons/hicolor/*/*/*
%{_libdir}/lib[kt]deinit_%{kdecomp}.so
%{_libdir}/*.la
%{tde_libdir}/*.so
%{tde_libdir}/*.la
%{tde_docdir}/HTML/en/*/


%Changelog
* Mon Jul 09 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.13-3
- Removes conflict with 'kdegraphics'

* Sat May 05 2012 Francois Andriot <francois.andriot@free.fr> - 0.8.13-3
- Rename old tq methods that no longer need a unique name [Commit #8712ab46]
- Remove additional unneeded tq method conversions [Commit #28d9c774]
- Rename obsolete tq methods to standard names [Commit #bdeb8b3a]
- Remove inadvertent renaming [Commit #d97e403f] [Bug #863]

* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.13-2
- Import to GIT

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.13-1
- Correct macro to install under "/opt", if desired

* Sat Aug 13 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.13-0
- Initial build for RHEL 6.0

