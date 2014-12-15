# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_version 14.0.0

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Summary: 		a TQt/TDE based RSS podcast and video aggregator
Name:			trinity-kitty 
Version:		0.9.2
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

License:		GPL
Group:			Applications/Network

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org

Source:			kitty_0.9.2.orig.tar.gz
Patch1:			kitty_0.9.2-2.1.diff.gz
Patch2:			kitty-14.0.0-ftbfs.patch

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	automake
BuildRequires:	libtool


%description
Kitty is a simple graphical podcast and video podcast client which allows
you to tune in, watch, download and bookmark podcasts and video podcasts.

%files
%defattr(-,root,root,-)
%{tde_bindir}/kitty
%{tde_datadir}/applnk/Utilities/kitty.desktop
%{tde_datadir}/apps/kitty/
%{tde_tdedocdir}/HTML/en/kitty/
%{tde_datadir}/icons/hicolor/*/apps/kitty.png

%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun 
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n kitty-0.9.2.orig
%patch1 -p1
patch -p1 < debian/patches/00_am_edit.patch
patch -p1 < debian/patches/01_qsizepolicy.patch

rm -rf admin
~/tde/tde_r14/experimental/qt3-tqt3/convert_existing_qt3_app_to_tqt3
~/tde/tde_r14/experimental/kde-tde/convert_existing_kde3_app_to_tde
cp -rf ~/tde/tde_r14/main/common/admin/ .

mv src/khtml_kget_cancel.png src/tdehtml_kget_cancel.png
mv src/khtml_kget.png src/tdehtml_kget.png

%patch2 -p1

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f admin/Makefile.common


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --includedir=%{tde_includedir} \
  --datadir=%{tde_datadir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --disable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility

%__make %{?_smp_mflags} || %__make


%install
%__rm -rf %{buildroot} 
%__make install DESTDIR=%{buildroot}



%clean
%__rm -rf %{buildroot} 


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.9.2-1
- Initial release for TDE 14.0.0
