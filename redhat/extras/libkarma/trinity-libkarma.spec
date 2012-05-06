%define _prefix /opt/trinity
%define _docdir %{_datadir}/doc
%define _mandir %{_datadir}/man

Summary:   	Rio Karma tools
Name:      	trinity-libkarma
Version:   	0.1.2
Release:   	1%{?dist}
License:   	GPLv2+
Group:     	System/Libraries
Url:	   	http://www.freakysoft.de/html/libkarma/
Source:   	http://www.freakysoft.de/libkarma/libkarma-%{version}.tar.gz
Source2: http://bobcopeland.com/karma/banshee/preferences.fdi
Source3: http://bobcopeland.com/karma/banshee/multimedia-player-rio-karma.png
Source4: karma-sharp.dll.config
BuildRoot: 	%{_tmppath}/%name-root
BuildRequires: mono-devel
BuildRequires: taglib-devel
BuildRequires: libusb-devel
BuildRequires: zlib-devel

Requires: %{name}-libs >= %version
%define _requires_exceptions libkarma

%description
Rio Karma access library

%package libs
Summary: Rio Karma access library
Group: System/Libraries

%description libs
Rio Karma access library


%package devel
Summary:   	Rio Karma development files
Group:     	Development/C
Requires:	%{name}-libs = %version

%description devel
Rio Karma development files


%package -n karma-sharp
Summary:   	Rio Karma C# bindings
Group:     	Development/Other
Requires:	%{name} = %version

%description -n karma-sharp
Rio Karma C# bindings


%prep
%setup -q -n libkarma-%{version}

%build
make PREFIX=$RPM_BUILD_ROOT/%_prefix

%install
rm -rf $RPM_BUILD_ROOT installed-docs
mkdir -p $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT/%_prefix CHOWNPROG=/bin/true CHGRPPROG=/bin/true
perl -pi -e "s^%buildroot^^" %buildroot%_prefix/lib/pkgconfig/karma-sharp.pc
%if %_lib != lib
mv %buildroot%_prefix/lib %buildroot%_libdir
perl -pi -e "s^/lib^/%_lib^" %buildroot%_libdir/pkgconfig/karma-sharp.pc
%endif


install -m 644 -D libkarma.fdi %buildroot%_sysconfdir/hal/fdi/information/20-rio-karma.fdi
install -m 644 -D %SOURCE2 %buildroot%_sysconfdir/hal/fdi/policy/preferences.fdi
install -m 644 -D %SOURCE3 %buildroot%_datadir/icons/hicolor/32x32/devices/multimedia-player-rio-karma.png

cat > README%{?dist} << EOF
For automatic mounting, add the following line to your
/etc/fstab. Otherwise gnome-volume-manager will refuse to mount the
device, as it doesn't know about the Karma's proprietary filesystem.

/dev/disk/by-id/usb-Rio_Rio_Karma_0000000000000000-part2    /media/karma    omfs    user,noauto    0   0

EOF

install -m 644 %SOURCE4 %buildroot%_libdir/karma-sharp/karma-sharp.dll.config

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc THANKS TODO README%{?dist}
%config(noreplace) %_sysconfdir/hal/fdi/information/20-rio-karma.fdi
%config(noreplace) %_sysconfdir/hal/fdi/policy/preferences.fdi
%_bindir/riocp
%_bindir/chprop
%_mandir/man1/*.1*
%attr(4755,root,root) %_bindir/karma_helper
%_datadir/icons/hicolor/32x32/devices/multimedia-player-rio-karma.png
%_docdir/libkarma

%files libs
%defattr(-,root,root)
%_libdir/libkarma.so.0*

%files devel
%defattr(-,root,root)
%_includedir/*
%_libdir/libkarma.a
%_libdir/libkarma.so

%files -n karma-sharp
%defattr(-,root,root)
%_libdir/karma-sharp/*
%_libdir/pkgconfig/karma-sharp.pc




%changelog
* Mon Apr 30 2012 Francois Andriot <francois.andriot@free.fr> 0.1.2-1
- Build for RHEL 5, RHEL 6, Fedora 15, Fedora 16, Fedora 17
- Based on 'libkarma-0.1.2-1mdv2011.0'

