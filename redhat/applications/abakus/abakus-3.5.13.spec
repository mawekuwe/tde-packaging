# Default version for this component
%define kdecomp abakus

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

Name:		trinity-%{kdecomp}
Summary:	Calculator for TDE
Version:	0.91
Release:	3%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel >= 3.5.13
BuildRequires:	trinity-tdelibs-devel >= 3.5.13
BuildRequires:	trinity-tdebase-devel >= 3.5.13
BuildRequires:	desktop-file-utils
BuildRequires:	scons
BuildRequires:	bison

%description
AbaKus is a complex calculator, which provides
many different kinds of calculations.
Think of it as bc (the command-line calculator) with a nice GUI.
It also gives information about mathematical variables and
has the user-friendly menu options of a normal TDE application.

%prep
%setup -q -n applications/%{kdecomp}

%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export CXXFLAGS="-I%{tde_includedir}/tqt"

# We are using a specific (non-autotool) configure script.
./configure

%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}%{tde_prefix}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_bindir}/abakus
%{tde_datadir}/apps/abakus/
%{tde_datadir}/icons/hicolor/*/apps/abakus.png
%{tde_tdedocdir}/HTML/en/abakus/
%{tde_datadir}/applnk/Utilities/abakus.desktop

%changelog
* Wed Apr 25 2012 Francois Andriot <francois.andriot@free.fr> - 0.91-3
- Fix postinstall

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.91-2
- Rebuilt for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15

* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.91-1
- Initial release for RHEL 6 and Fedora 15
- Import to GIT
