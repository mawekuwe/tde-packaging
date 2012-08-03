# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Summary:   	Rio Karma tools
Name:      	trinity-libkarma
Version:   	0.1.2
Release:   	2%{?dist}%{?_variant}
License:   	GPLv2+
Group:     	System/Libraries
Url:	   	http://www.freakysoft.de/html/libkarma/

Source:   	http://www.freakysoft.de/libkarma/libkarma-%{version}.tar.gz
Source2:	http://bobcopeland.com/karma/banshee/preferences.fdi
Source3:	http://bobcopeland.com/karma/banshee/multimedia-player-rio-karma.png
Source4:	karma-sharp.dll.config

# [libkarma] Fix installation directories
Patch1:		libkarma-0.1.2-fix_installation.patch

BuildRoot: 	%{_tmppath}/%name-root

BuildRequires: mono-devel
BuildRequires: taglib-devel
BuildRequires: libusb-devel
BuildRequires: zlib-devel

Obsoletes:		trinity-libkarma-libs < %{version}-%{release}
Provides:		trinity-libkarma-libs = %{version}-%{release}

Provides:		libkarma = %{version}-%{release}

%description
Rio Karma access library


%package devel
Summary:   	Rio Karma development files
Group:     	Development/C
Requires:	%{name} = %{version}-%{release}
Provides:	libkarma-devel = %{version}-%{release}

%description devel
Rio Karma development files


%package -n trinity-karma-sharp
Summary:   	Rio Karma C# bindings
Group:     	Development/Other
Requires:	%{name} = %{version}-%{release}

Obsoletes:	karma-sharp < %{version}-%{release}
Provides:	karma-sharp = %{version}-%{release}

%description -n trinity-karma-sharp
Rio Karma C# bindings


%prep
%setup -q -n libkarma-%{version}
%patch1 -p1 -b .fixdir

%build
# Do *NOT* use LIBDIR variable, it is used for internal purpose !!!
%__make \
  DESTDIR=%{?buildroot} \
  PREFIX=%{tde_prefix} \
  LIB=%{_lib}
  

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p $RPM_BUILD_ROOT

%__make install \
  DESTDIR=%{?buildroot} \
  PREFIX=%{tde_prefix} \
  LIB=%{_lib} \
  CHOWNPROG=/bin/true \
  CHGRPPROG=/bin/true


install -m 644 -D libkarma.fdi %buildroot%_sysconfdir/hal/fdi/information/20-rio-karma.fdi
install -m 644 -D %SOURCE2 %buildroot%_sysconfdir/hal/fdi/policy/preferences.fdi
install -m 644 -D %SOURCE3 %buildroot%{tde_datadir}/icons/hicolor/32x32/devices/multimedia-player-rio-karma.png

cat > README%{?dist} << EOF
For automatic mounting, add the following line to your
/etc/fstab. Otherwise gnome-volume-manager will refuse to mount the
device, as it doesn't know about the Karma's proprietary filesystem.

/dev/disk/by-id/usb-Rio_Rio_Karma_0000000000000000-part2    /media/karma    omfs    user,noauto    0   0

EOF

install -m 644 -D %SOURCE4 %buildroot%{tde_libdir}/karma-sharp/karma-sharp.dll.config

# Removes doc
%__rm -rf %{?buildroot}%{tde_docdir}/libkarma/


%post
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
/sbin/ldconfig || :

%postun
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
/sbin/ldconfig || :

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog THANKS TODO README%{?dist}
%config(noreplace) %_sysconfdir/hal/fdi/information/20-rio-karma.fdi
%config(noreplace) %_sysconfdir/hal/fdi/policy/preferences.fdi
%{tde_bindir}/riocp
%{tde_bindir}/chprop
%{tde_mandir}/man1/*.1*
%attr(4755,root,root) %{tde_bindir}/karma_helper
%{tde_datadir}/icons/hicolor/32x32/devices/multimedia-player-rio-karma.png
%{tde_libdir}/libkarma.so.0*

%files devel
%defattr(-,root,root)
%{tde_includedir}/libkarma/
%{tde_libdir}/libkarma.a
%{tde_libdir}/libkarma.so

%files -n trinity-karma-sharp
%defattr(-,root,root)
%{tde_libdir}/karma-sharp/*
%{tde_libdir}/pkgconfig/karma-sharp.pc




%changelog
* Fri Aug 03 2012 Francois Andriot <francois.andriot@free.fr> 0.1.2-2
- Add support for MGA2 and MDV2011
- Removes 'libs' subpackage
- Fix installation directories

* Mon Apr 30 2012 Francois Andriot <francois.andriot@free.fr> 0.1.2-1
- Build for RHEL 5, RHEL 6, Fedora 15, Fedora 16, Fedora 17
- Based on 'libkarma-0.1.2-1mdv2011.0'

