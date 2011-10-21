# TODO
# - for some unknown reason to me it creates dead symlinks instead of libtqt shared library
#   libtool: install: /usr/bin/install -c -p .libs/libtqt.so.4.2.0 /tmp/xxx/usr/lib64/libtqt.so.4.2.0
#   /usr/bin/install: cannot stat `.libs/libtqt.so.4.2.0': No such file or directory
#   workarounded in spec r1.2 commit
#
# Conditional build:
%bcond_with		qt4     # Enable Qt4 support (this will disable all Qt3 support)

%define epoch_kdelibs 30000000

Summary:	Interface and abstraction library for Qt and Trinity
Name:		libtqtinterface
Version:	3.5.12
Release:	%mkrel 1
#Epoch:          %epoch_kdelibs
License:	GPL v2
Group:		Graphical desktop/KDE3
Source0:	http://mirror.its.uidaho.edu/pub/trinity/releases/%{version}/dependencies/tqtinterface-%{version}.tar.gz
# Source0-md5:	361c45961184f01f95d3b771138c8229
Patch0:         tqt-comments.patch
Patch1:         tqglobal-comments.patch
Patch2: 	tqt-r1217318.diff
URL:		http://trinity.pearsoncomputing.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	qt3-devel
BuildRequires:	sed >= 4.0
#BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRoot: %_tmppath/%name-%version-%release-root


%description
This package includes libraries that abstract the underlying Qt system
from the actual Trinity code, allowing easy, complete upgrades to new
versions of Qt.

It also contains various functions that have been removed from newer
versions of Qt, but are completely portable and isolated from other
APIs such as Xorg. This allows the Trinity project to efficiently
perform certain operations that are infeasible or unneccessarily
difficult when using pure Qt4 or above.

%package devel
Summary:	Header files for libtqtinterface library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtqtinterface
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libtqtinterface library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtqtinterface.

%prep
%setup -qc
mv dependencies/tqtinterface/* .
%patch0 -p0
%patch1 -p0
%patch2 -p2

# libtool copy
rm -r libltdl
%{__sed} -i -e '/ltdl.m4/d' Makefile.am.in

# remove copy of QtCore and QtGui devel headers
rm -r qtinterface/qt4 qtinterface/tqt4
%{__sed} -i -e /tqt4/d qtinterface/Makefile.am

%build
make -f admin/Makefile.common cvs

QTDIR=%qt3dir ; export QTDIR;
PATH=%{qt3dir}/bin:$PATH; export PATH;
export xdg_menudir=%_sysconfdir/xdg/kde/menus

%configure_kde3 \
        --includedir=%{_kde3_includedir}/tqt \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	%{?with_qt4:--enable-qt4}

%{__make} \
	LIBTOOL="%{_bindir}/libtool -v"

%install
rm -rf $RPM_BUILD_ROOT
# force -j1 or USE_QTX is replaced _after_ file is installed
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \

# --disable-static did not work, rm it again
#rm $RPM_BUILD_ROOT%{_libdir}/libtqt.a

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_kde3_libdir}/libtqt.so.*.*.*
%attr(755,root,root) %{_kde3_libdir}/libtqt.a
%ghost %attr(755,root,root) %{_kde3_libdir}/libtqt.so.4

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_kde3_bindir}/convert_qt_tqt1
%attr(755,root,root) %{_kde3_bindir}/convert_qt_tqt2
%attr(755,root,root) %{_kde3_bindir}/convert_qt_tqt3
%attr(755,root,root) %{_kde3_bindir}/dcopidl-tqt
%attr(755,root,root) %{_kde3_bindir}/dcopidl2cpp-tqt
%attr(755,root,root) %{_kde3_bindir}/dcopidlng-tqt
%attr(755,root,root) %{_kde3_bindir}/mcopidl-tqt
%attr(755,root,root) %{_kde3_bindir}/moc-tqt
%attr(755,root,root) %{_kde3_bindir}/tqt-replace
%attr(755,root,root) %{_kde3_bindir}/tqt-replace-stream
%dir %{_kde3_includedir}/tqt
%{_kde3_includedir}/tqt/tq*.h
%{_kde3_libdir}/libtqt.la
%{_kde3_libdir}/libtqt.so

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* Wed Feb 1 2011 Tim Williams <tim@my-place.org.uk> 1:3.5.12-1mvf2010.2
+ Rewrite for MDV 2010.2
+ Spec based on revision 1.4 from PLD linux
+ Add tqt-comments.patch, tqglobal-comments.patch. My compiler doesn't like // comments.
