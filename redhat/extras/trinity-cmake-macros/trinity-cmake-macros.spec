Name:           trinity-cmake-macros
Version:        1.0
Release:        1%{?dist}
Summary:        Rpmbuild macros for cmake utility

Group:          Development/Utilities
License:        GPL
URL:            http://www.trinitydesktop.org/
Source0:        macros.cmake

Requires:       cmake

%description
This is the cmake macros for rpmbuild.
It was originally written for Fedora, but can be used on openSUSE too.


%prep


%build


%install
rm -rf $RPM_BUILD_ROOT
%__install -D -m 644 "%{SOURCE0}" %{?buildroot}%{_sysconfdir}/rpm/macros.cmake


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_sysconfdir}/rpm/macros.cmake


%changelog
* Mon Sep 29 2014 François Andriot <francois.andriot@free.fr> - 1.0-1
- Initial build for openSUSE
