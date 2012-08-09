# Default version for this component
%define kdecomp kde-style-qtcurve

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
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-style-qtcurve
Summary:	This is a set of widget styles for Trinity based apps
Version:	0.55.2
Release:	2%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

Patch0:		kde-style-qtcurve-1.6.2-libsuffix.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-tdelibs-devel
BuildRequires:	trinity-tdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

Obsoletes:		trinity-kde-style-qtcurve

%description
This package together with gtk2-engines-qtcurve aim to provide a unified look
and feel on the desktop when using TDE and Gnome applications.

This package is most useful when installed together with 
gtk2-engines-qtcurve.


%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i CMakeLists.txt \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"

export CXXFLAGS="-I${QTINC} -I%{tde_tdeincludedir} ${CXXFLAGS}"

%if 0%{?rhel} || 0%{?fedora}
%__mkdir_p build
cd build
%endif

%cmake \
	-DKDE3PREFIX=%{tde_prefix} \
	..

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


%clean
%__rm -rf %{buildroot}



%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_tdelibdir}/plugins/styles/qtcurve.so
%{tde_datadir}/apps/QtCurve/Agua.qtcurve
%{tde_datadir}/apps/QtCurve/Agua_II.qtcurve
%{tde_datadir}/apps/QtCurve/Curve.qtcurve
%{tde_datadir}/apps/QtCurve/Flat.qtcurve
%{tde_datadir}/apps/QtCurve/Human.qtcurve
%{tde_datadir}/apps/QtCurve/Inverted.qtcurve
%{tde_datadir}/apps/QtCurve/Klearlooks.qtcurve
%{tde_datadir}/apps/QtCurve/Milk.qtcurve
%{tde_datadir}/apps/QtCurve/Murrine.qtcurve
%{tde_datadir}/apps/QtCurve/Ozone.qtcurve
%{tde_datadir}/apps/QtCurve/Plastic.qtcurve
%{tde_datadir}/apps/QtCurve/Silk.qtcurve
%{tde_datadir}/apps/kdisplay/color-schemes/QtCurve.kcsrc


%Changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.55.2-2
- Rebuilt for Fedora 17
- Removes post and postun

* Sat Nov 19 2011 Francois Andriot <francois.andriot@free.fr> - 0.55.2-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
