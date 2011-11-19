# Default version for this component
%define kdecomp kde-style-qtcurve
%define version 0.55.2
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
Summary:	This is a set of widget styles for Trinity based apps
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

Patch0:		kde-style-qtcurve-1.6.2-libsuffix.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext


%description
This package together with gtk2-engines-qtcurve aim to provide a unified look
and feel on the desktop when using KDE and Gnome applications.

This package is most useful when installed together with 
gtk2-engines-qtcurve.


%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
sed -i CMakeLists.txt \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"

export CXXFLAGS="-I${QTINC} ${CXXFLAGS}"
	
%__mkdir build
cd build
%cmake \
	-DKDE3PREFIX=%{_prefix} \
	..

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_libdir}/plugins/styles/qtcurve.so
%{_datadir}/apps/QtCurve/Agua.qtcurve
%{_datadir}/apps/QtCurve/Agua_II.qtcurve
%{_datadir}/apps/QtCurve/Curve.qtcurve
%{_datadir}/apps/QtCurve/Flat.qtcurve
%{_datadir}/apps/QtCurve/Human.qtcurve
%{_datadir}/apps/QtCurve/Inverted.qtcurve
%{_datadir}/apps/QtCurve/Klearlooks.qtcurve
%{_datadir}/apps/QtCurve/Milk.qtcurve
%{_datadir}/apps/QtCurve/Murrine.qtcurve
%{_datadir}/apps/QtCurve/Ozone.qtcurve
%{_datadir}/apps/QtCurve/Plastic.qtcurve
%{_datadir}/apps/QtCurve/Silk.qtcurve
%{_datadir}/apps/kdisplay/color-schemes/QtCurve.kcsrc


%Changelog
* Sat Nov 19 2011 Francois Andriot <francois.andriot@free.fr> - 0.55.2-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
