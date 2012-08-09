%define _prefix /opt/trinity

Name:           tqca
Version:        1.0
Release:        r14.1%{?dist}

Summary:        TQt Cryptographic Architecture

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://delta.affinix.com/qca
Source0:        %{name}-r14.tar.gz
Patch0:         qca-1.0-mach.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch1:			tqca-1.0-fix_tqt3_detection.patch

BuildRequires:  tqt3-devel
BuildRequires:  tqtinterface-devel

%description
Taking a hint from the similarly-named Java Cryptography Architecture,
QCA aims to provide a straightforward and cross-platform crypto API,
using Qt datatypes and conventions. QCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
application!

%package        devel
Summary:        Qt Cryptographic Architecture development files
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
This packages contains the development files for QCA

%prep
%setup -q -n dependencies/tqca
%patch0 -p0 -b .mach
%patch1 -p1
perl -pi -e 's,target\.path=\$PREFIX/lib,target.path=\$PREFIX/%{_lib},g' qcextra


%build
./configure \
  --prefix=%{_prefix}

sed -i -e /strip/d Makefile
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/*.so


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 1.0-11
- fix build

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-10
- Autorebuild for GCC 4.3

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.0-9
- fix license tag

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.0-8
- rebuild

* Sat Apr 08 2006 Aurelien Bompard <gauret[AT]free.fr> 1.0-7
- disable stripping (bug 186648)

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 1.0-6
- rebuild for FC5

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.0-5
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Jan 13 2005 Aurelien Bompard <gauret[AT]free.fr> 0:1.0-3
- fix Category
- fix build on x86_64

* Thu Jan 13 2005 Aurelien Bompard <gauret[AT]free.fr> 0:1.0-0.fdr.2
- clean up comments to fix %%postun scriptlet.

* Mon Nov 22 2004 Aurelien Bompard <gauret[AT]free.fr> 0:1.0-0.fdr.1
- Initial RPM release.
