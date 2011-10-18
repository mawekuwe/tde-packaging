%define oname kickoff-i18n
%define name kde3-%{oname}
Name: %{name}
Summary: Kickoff translations
Version: 1.0
Release: %mkrel 10
Group: System/Internationalization
License: GPL
URL: http://www.mandriva.com
Source0: %oname-%version.tar.bz2
Patch0:  kickoff-i18n-1.0-uz-po.patch
Patch1:  kickoff-i18n-1.0-tr-po.patch
BuildRoot: %_tmppath/%name-%version-%release-buildroot
BuildArch: noarch
BuildRequires: kdelibs-devel
Obsoletes: %{oname}
Provides: %{oname} = %{version}-%{release}

%description
kickoff translations

%prep
%setup -q -n %oname-%version
%patch0 -p1
%patch1 -p1

%build
./configure \
    --prefix=%_kde3_prefix \
    --datadir=%_kde3_datadir

make clean
%make

%install
rm -fr %buildroot
%makeinstall_std

%find_lang kickoff

%clean
rm -fr %buildroot

%files -f kickoff.lang
%defattr(-,root,root,-)
