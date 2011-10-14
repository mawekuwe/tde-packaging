%define	major 1
%define	libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	A program to allow arbitrary access to device files
Name:		resmgr
Version:	1.0
Release:	%mkrel 14
License:	GPLv2
Group:		System/Servers
URL: 		http://www.lst.de/~okir/resmgr/
Source:		ftp://ftp.lst.de/pub/people/okir/%{name}/%{name}-%{version}.tar.bz2
Source1:	resmgr.init
Source2:	resmgr.conf
Source3:	desktopdev
Patch0: 	resmgr-1.0-syslog.patch 
Patch1: 	resmgr-va_list.patch
Patch2: 	resmgr-glibc28.diff
Patch3: 	resmgr-linkage_fix.diff
Patch4: 	resmgr-permission_fix.diff
Requires(post): rpm-helper
Requires(preun): rpm-helper
BuildRequires:	pam-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The resource manager is a framework to give user applications access
to certain device files. The resource manager daemon can be configured
to give certain users access to different resource classes.

It supports hotplugging devices (i.e. new devices can be added to
and removed from resource classes at run time), and it provides
transparent access to the raw SCSI device corresponding to
a CD writer or a scanner.

%package -n	%{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries

%description -n	%{libname}
The resource manager is a framework to give user applications access
to certain device files. The resource manager daemon can be configured
to give certain users access to different resource classes.

It supports hotplugging devices (i.e. new devices can be added to
and removed from resource classes at run time), and it provides
transparent access to the raw SCSI device corresponding to
a CD writer or a scanner.

%package -n	%{develname}
Summary:	Development headers and libraries for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname resmgr 1 -d}

%description -n	%{develname}
The resource manager is a framework to give user applications access
to certain device files. The resource manager daemon can be configured
to give certain users access to different resource classes.

It supports hotplugging devices (i.e. new devices can be added to
and removed from resource classes at run time), and it provides
transparent access to the raw SCSI device corresponding to
a CD writer or a scanner.

%prep

%setup -q
%patch0 -p1 -b .syslog
%patch1 -p1 -b .va_list
%patch2 -p0 -b .glibc28
%patch3 -p0 -b .linkage_fix
%patch4 -p0 -b .permission_fix

%build
%make CFLAGS="%{optflags} -D_GNU_SOURCE" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

%makeinstall_std LIBDIR=%{buildroot}/%{_lib} PAMDIR=%{buildroot}/%{_lib}/security

ln -sf libresmgr.so.* %{buildroot}/%{_lib}/libresmgr.so
install -m755 %{SOURCE1} -D %{buildroot}%{_initrddir}/%{name}
mkdir -p %{buildroot}/usr/sbin/
ln -s ../..%{_initrddir}/%{name} %{buildroot}%{_sbindir}/rc%{name}
# install config file
install -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}.conf
install -c -m755 %{SOURCE3} -D %{buildroot}%{_sysconfdir}/udev/agents.d/usb/desktopdev

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO ANNOUNCE
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_initrddir}/%{name}
%{_sysconfdir}/udev/agents.d/usb/desktopdev
%{_sbindir}/rc%{name}
/sbin/%{name}
/sbin/%{name}d
%{_mandir}/man*/*

%files -n %{libname}
%defattr(-,root,root)
/%{_lib}/*.so.*
/%{_lib}/security/*

%files -n %{develname}
%defattr(-,root,root)
/%{_lib}/*.so
%{_includedir}/%{name}.h


%changelog
* Mon Jul 18 2011 Tim Williams <tim@my-place.org.uk> 1.0-14mdv2010.2
+ Rebuild for Trinity

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0-13mdv2010.0
+ Revision: 426907
- rebuild

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-12mdv2009.1
+ Revision: 317576
- use %%ldflags

* Fri Jul 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-11mdv2009.0
+ Revision: 238350
- fix linkage
- fix errors in the init script
- fix permissions (for strip + debug packaging)

* Fri Jul 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-10mdv2009.0
+ Revision: 238102
- added P1 from pld
- fix build, P2 + -D_GNU_SOURCE

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-8mdv2008.1
+ Revision: 179431
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 01 2007 Adam Williamson <awilliamson@mandriva.org> 1.0-7mdv2008.0
+ Revision: 57363
- rebuild for 2008
- new devel policy
- spec clean


* Mon Jul 31 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-07-31 20:51:47 (42877)
- Increase release number

* Mon Jul 31 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-07-31 20:50:48 (42876)
- Fix for http://qa.mandriva.com/show_bug.cgi?id=23968 ( wrong init services )

* Wed Jul 26 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-07-26 03:39:04 (42167)
- Moved to subversion
- Added patch from Jan Ciger to fix syslog defines

* Wed Jul 26 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-07-26 03:11:36 (42165)
- import resmgr-1.0-4mdk

* Wed Jan 18 2006 Olivier Blin <oblin@mandriva.com> 1.0-4mdk
- fix pam files installation on x86_64
- buildrequire pam-devel
- drop hotplug requirement

* Sat Aug 27 2005 Olivier Blin <oblin@mandriva.com> 1.0-3mdk
- move hotplug script to in udev agents.d directory
- update Source4 to explain how it should be handled with udev

* Sun Jun 12 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0-2mdk
- rebuild
- fix requires
- do not mark init file as config file
- %%{1}mdv2007.0

* Fri May 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0-1mdk
- initial mdk release (based on suse package)

