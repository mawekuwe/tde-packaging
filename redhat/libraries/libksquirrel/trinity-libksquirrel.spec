# Default version for this component
%define kdecomp libksquirrel
%define version 0.8.0
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
Summary:	Trinity image viewer
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Patch0:		libksquirrel-3.5.13-detect_netpbm.patch
Patch1:		libksquirrel-3.5.13-fix_docdir.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	gettext-devel
BuildRequires:	transfig
BuildRequires:	netpbm-progs
%if 0%{?fedora}  >= 15
BuildRequires:	xmedcon-devel
BuildRequires:	djvulibre
%endif

%description
Runtime libraries for KSquirrel.


%package devel
Group:		Development/Libraries
Summary:	Trinity image viewer
Requires:	%{name}

%description devel
Development libraries for KSquirrel.


%package tools
Summary:	Trinity image viewer
Group:		Environment/Libraries
Requires:	%{name}

%description tools
Tools for KSquirrel.


%prep
%setup -q -n libraries/%{kdecomp}
%patch0 -p1
%patch1 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
sed -i admin/acinclude.m4.in \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common" cvs


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%clean
%__rm -rf %{buildroot}


%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING LICENSE README
%{_libdir}/ksquirrel-libs/*.so.*
%{_libdir}/*.so.*
%{_datadir}/ksquirrel-libs

%files devel
%defattr(-,root,root,-)
%{_includedir}/ksquirrel-libs
%{_libdir}/ksquirrel-libs/*.la
%{_libdir}/ksquirrel-libs/*.so
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/ksquirrellibs.pc
%{_docdir}/ksquirrel-libs

%files tools
%defattr(-,root,root,-)
%{_bindir}/*


%Changelog
* Sun Nov 20 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.0-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
