# Default version for this component
%define tde_pkg sip4-tqt
%define tde_version 14.0.0

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

Name:		trinity-%{tde_pkg}
Version:	4.10.5
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:	GPL
Summary:	Python/C++ bindings generator runtime library
Group:		System Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}

# TDE specific building variables
BuildRequires:	python
BuildRequires:	trinity-tqt3-devel >= 3.5.0

%description
SIP is a tool for generating bindings for C++ classes with some ideas
borrowed from SWIG, but capable of tighter bindings because of its
specificity towards C++ and Python.

%files
%defattr(-,root,root,-)
%dir %{python_sitearch}/sip4_tqt
%{python_sitearch}/sip4_tqt/sip.so
%{python_sitearch}/sip4_tqt/sipconfig.py*
%{python_sitearch}/sip4_tqt/sipdistutils.py*
%{python_sitearch}/sip4_tqt/__init__.py*

##########

%package devel
Summary:		Python/C++ bindings generator development files
Group:			Development/Libraries
Requires:		%{name} = %{version}-%{release}

%description devel
SIP is a tool for generating bindings for C++ classes with some ideas
borrowed from SWIG, but capable of tighter bindings because of its
specificity towards C++ and Python.

SIP was originally designed to generate Python bindings for KDE and so
has explicit support for the signal slot mechanism used by the Qt/KDE
class libraries.

Features:
- connecting TQt signals to Python functions and class methods
- connecting Python signals to TQt slots
- overloading virtual member functions with Python class methods
- protected member functions
- abstract classes
- enumerated types
- global class instances
- static member functions.

This package contains the code generator tool and the development headers
needed to develop Python bindings with sip.

%files devel
%defattr(-,root,root,-)
%{tde_bindir}/sip
%{tde_includedir}/sip.h

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

mkdir build
cd build
python ../configure.py \
	-b %{tde_bindir} \
	-d %{python_sitearch}/sip4_tqt \
	-e %{tde_includedir} \
	-u STRIP="" \
	CFLAGS="${RPM_OPT_FLAGS} -I%{_includedir}/tqt -I%{_includedir}/tqt3 -I${PWD}/../sipgen" \
	CFLAGS_RELEASE="" \
	CXXFLAGS="${RPM_OPT_FLAGS} -I%{_includedir}/tqt -I%{_includedir}/tqt3 -I${PWD}/../sipgen" \
	CXXFLAGS_RELEASE=""


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

# Dummy file to allow loading as a module
touch %{?buildroot}%{python_sitearch}/sip4_tqt/__init__.py


%clean
%__rm -rf %{?buildroot}


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 4.10.5-1
- Initial release for TDE R14, using 'tqt3' instead of 'qt3'
