# Some distribution already provides this package.
#  Mageia 3

%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

# Always install under standard prefix
%define tde_prefix /usr

%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

Name:		trinity-sip4-tqt
Epoch:		2
Version:	14.0.0
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:	GPL
Summary:	Python/C++ bindings generator runtime library
Group:		System Environment/Libraries

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{version}

# TDE specific building variables
BuildRequires:	cmake >= 2.8
BuildRequires:	trinity-tqt3-devel >= %{version}

%description

##########

%package -n python-sip
Summary:	Python/C++ bindings generator runtime library
Epoch:		2

%description -n python-sip
SIP is a tool for generating bindings for C++ classes with some ideas
borrowed from SWIG, but capable of tighter bindings because of its
specificity towards C++ and Python.

%post -n python-sip
/sbin/ldconfig || :

%postun -n python-sip
/sbin/ldconfig || :

%files -n python-sip
%defattr(-,root,root,-)
%{python_sitearch}/sip.so
%{python_sitearch}/sipconfig.py
%{python_sitearch}/sipdistutils.py


##########

%package -n python-sip-devel
Summary:		Python/C++ bindings generator development files
Group:			Development/Libraries
Requires:		python-sip = %{version}-%{release}

%description -n python-sip-devel
SIP is a tool for generating bindings for C++ classes with some ideas
borrowed from SWIG, but capable of tighter bindings because of its
specificity towards C++ and Python.

SIP was originally designed to generate Python bindings for KDE and so
has explicit support for the signal slot mechanism used by the Qt/KDE
class libraries.

Features:
- connecting Qt signals to Python functions and class methods
- connecting Python signals to Qt slots
- overloading virtual member functions with Python class methods
- protected member functions
- abstract classes
- enumerated types
- global class instances
- static member functions.

This package contains the code generator tool and the development headers
needed to develop Python bindings with sip.

%post -n python-sip-devel
/sbin/ldconfig || :

%postun -n python-sip-devel
/sbin/ldconfig || :

%files -n python-sip-devel
%defattr(-,root,root,-)
%{_bindir}/sip
%{_includedir}/python*/sip.h

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

mkdir build
cd build
python ../configure.py \
	-d %{python_sitearch} \
	-u STRIP="" \
	CFLAGS="${RPM_OPT_FLAGS} -I%{_includedir}/tqt -I%{_includedir}/tqt3" \
	CFLAGS_RELEASE="" \
	CXXFLAGS="${RPM_OPT_FLAGS} -I%{_includedir}/tqt -I%{_includedir}/tqt3" \
	CXXFLAGS_RELEASE=""


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

%clean
%__rm -rf %{?buildroot}


%changelog
* Thu Feb 16 2012 Francois Andriot <francois.andriot@free.fr> - 14.0.0-1
- Initial build for TDE R14, using 'tqt3' instead of 'qt3'
