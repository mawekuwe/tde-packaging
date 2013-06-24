# Default version for this component
%define kdecomp abakus
%define version 0.91
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/kde3


Name:		trinity-%{kdecomp}
Summary:	Calculator for TDE
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Source0:	%{kdecomp}-3.5.12.tar.gz

Patch0:		abakus-0.91-link-dcop.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	scons

%description
AbaKus is a complex calculator, which provides
many different kinds of calculations.
Think of it as bc (the command-line calculator) with a nice GUI.
It also gives information about mathematical variables and
has the user-friendly menu options of a normal KDE application.

%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1

%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"
export CXXFLAGS="-I%{_includedir}/tqt"

./configure
	
%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}%{_prefix}


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
%{_bindir}/*
%{_datadir}/apps/*/
%{_datadir}/icons/*/*/*/*
%{tde_docdir}/HTML/*/*/
%{_datadir}/applnk/Utilities/abakus.desktop

%changelog
* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.91-1
- Initial build for RHEL 6 and Fedora 15
- Import to GIT
