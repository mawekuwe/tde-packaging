%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%define tde_version 14.0.0

# Always install under standard prefix
%define tde_prefix /usr

%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

Name:		trinity-python-tqt
Version:	3.18.1
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:	GPL

Summary:	TQt bindings for Python
Group:		System Environment/Libraries

Obsoletes:		trinity-PyQt
Obsoletes:		trinity-python-qt3

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz
Patch0:		python-tqt-14.0.0-ftbfs.patch

BuildRequires:	gcc-c++
BuildRequires:	trinity-tqtinterface-devel >= %{version}
BuildRequires:	trinity-tqscintilla-devel

%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version}
BuildRequires:	sip-devel
%endif
%if 0%{?mdkversion} || 0%{?mgaversion}
BuildRequires:	python-sip
%endif

# TDE specific building variables
BuildRequires:	cmake >= 2.8
BuildRequires:	trinity-tqt3-devel >= 3.5.0
Requires:		trinity-tqt3 >= 3.5.0


%description
Python binding module that allows use of TQt X Window toolkit v3.
You can use it to create portable graphics-capable scripts (there
are PyQt versions for Linux, Windows and MacOS X).

At this moment PyQt offers a vast subset of TQt API. There are
some minor issues related to the differences between C++ and Python
(types, etc), but usually you'll be able to write code pretty much the
same way in both languages (with syntax differences, of course)

%files
%defattr(-,root,root,-)
%doc NEWS README
%{python_sitearch}/qt.so
%{python_sitearch}/qtcanvas.so
%{python_sitearch}/qtnetwork.so
%{python_sitearch}/qtsql.so
%{python_sitearch}/qttable.so
%{python_sitearch}/qtui.so
%{python_sitearch}/qtxml.so

##########

%package gl
Summary:	TQt OpenGL bindings for Python
Requires:	%{name} = %{version}-%{release}

%description gl
Python binding module that allows use of the OpenGL facilities
offered by the TQt X Window toolkit v3. You can use it to create
portable graphics-capable scripts (there are PyQt versions for
Linux, Windows and MacOS X).

%files gl
%defattr(-,root,root,-)
%{python_sitearch}/qtgl.so

##########

%package tqtext
Summary:	TQt extensions for PyQt
Requires:	%{name} = %{version}-%{release}

%description tqtext
PyQt Extensions. Contains:

* QScintilla: a featureful TQt source code editing component based
              on Scintilla.

%files tqtext
%defattr(-,root,root,-)
%{python_sitearch}/qtext.so

##########

%package -n trinity-pytqt-tools
Summary:	pyuic and pylupdate for TQt

%description -n trinity-pytqt-tools
pyuic is the PyQt counterpart for TQt's uic. It takes an XML
user interface file and generates Python code.

pylupdate is the counterpart for TQt's lupdate. It updates TQt
Linguist translation files from Python code.

%files -n trinity-pytqt-tools
%{_bindir}/pylupdate
%{_bindir}/pyuic

##########

%package devel
Summary:	TQt bindings for Python - Development files
Requires:	%{name} = %{version}-%{release}

%description devel
Development .sip files with definitions of PyQt classes. They
are needed to build PyQt, but also as building blocks of other
packages based on them, like PyKDE.

%files devel
%defattr(-,root,root,-)
%{python_sitearch}/pyqtconfig.py
%{_datadir}/sip/tqt/

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
%patch0 -p1 -b .ftbfs


%build
unset QTDIR QTINC QTLIB

mkdir build
cd build
echo yes | python ../configure.py \
	-c -n %{_includedir}/tqscintilla \
	-q /usr/share/tqt3 \
	-y tqt-mt \
	-o %{_libdir} -u -j 10 \
	-d %{python_sitearch} \
	-v %{_datadir}/sip/tqt \
	-w \
	CXXFLAGS_RELEASE="" CXXFLAGS="${RPM_OPT_FLAGS} -I%{_includedir}/tqt" STRIP=""

%__make


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

%__install -d %{?buildroot}%{_datadir}/sip/
%__cp -rf sip/* %{?buildroot}%{_datadir}/sip/tqt/


%clean
%__rm -rf %{?buildroot}


%changelog
* Thu Feb 16 2012 Francois Andriot <francois.andriot@free.fr> - 14.0.0-1
- Initial release for TDE R14, using 'tqt3' instead of 'qt3'

