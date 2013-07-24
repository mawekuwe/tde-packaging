# Default version for this component
%define tde_pkg qt4-tqt-theme-engine
%define tde_version 14.0.0

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		TDE theme engine for Qt4
Version:		0.1
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	qt4-devel

%description
TDE theme engine for Qt4


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

# Fix compilation with 'lib64'
%if "%_lib" == "lib64"
%__sed -i */*.pro -e "s|/opt/trinity/lib|/opt/trinity/lib64|g"
%endif

# Fix TDE include directory
%__sed -i */*.pro -e "s|INCLUDEPATH += /opt/trinity/include|INCLUDEPATH += /opt/trinity/include/tde|"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

if [ -x "%{_libdir}/qt4/bin/qmake" ]; then
  export PATH="%{_libdir}/qt4/bin:${PATH}"
fi

# Use QT4's qmake
qmake


# Not SMP SAFE !
%__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install INSTALL_ROOT=%{buildroot}

# Unwanted files (-devel ?)
%__rm -f %{?buildroot}%{_libdir}/libtdeqt4interface.so


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_libdir}/libtdeqt4interface.so.1
%{_libdir}/libtdeqt4interface.so.1.0
%{_libdir}/libtdeqt4interface.so.1.0.0
%{_qt4_plugindir}/styles/libsimplestyleplugin.so


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.1-1
- Initial release for TDE 14.0.0
