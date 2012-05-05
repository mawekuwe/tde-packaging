# Default version for this component
%define kdecomp kgtk-qt3
%define version 0.10.2
%define release 2

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
Summary:	Use KDE dialogs in Gtk apps
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext


%description
This is an LD_PRELOAD hack that allows most GTK
applications to use Trinity's file dialogs when run under Trinity.

The Gtk file chooser functions have been overridden to communicate
with this KDE module/application.

This package includes the kqt3-wrapper


%prep
%setup -q -n applications/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
find . -name CMakeLists.txt -exec sed -i {} \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g" \
  -e "s,/usr/bin/tmoc,%{_bindir}/tmoc,g" \
  -e "s,/usr/bin/uic-tqt,%{_bindir}/uic-tqt,g" \
  \;

%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir} -L${QTLIB} -lX11"

%__mkdir_p build
cd build
%cmake ..

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build


%find_lang kdialogd3 || touch %{kdecomp}.lang



%clean
%__rm -rf %{buildroot}


%files -f kdialogd3.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/kdialogd-wrapper
%{_bindir}/kdialogd3
%{_bindir}/kgtk-wrapper
%{_bindir}/kgtk2-wrapper
%{_bindir}/kqt3-wrapper
%{_libdir}/kgtk/libkgtk2.so
%{_libdir}/kgtk/libkqt3.so


%Changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.10.2-2
- Rebuilt for Fedora 17
- Removes post and postun

* Thu Dec 01 2011 Francois Andriot <francois.andriot@free.fr> - 0.10.2-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
