%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define tde_version 14.0.0
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

Name:		trinity-python-tqt
Version:	3.18.1
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
License:	GPL

Summary:	TQt bindings for Python
Group:		System Environment/Libraries

#Obsoletes:		PyQt
Obsoletes:		trinity-PyQt
Obsoletes:		trinity-python-qt3

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

Patch1:		python-tqt-14.0.0-sip4_tqt.patch

BuildRequires:	gcc-c++
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tqscintilla-devel

# SIP
BuildRequires:	trinity-sip4-tqt-devel >= 4.10.5
Requires:		trinity-sip4-tqt >= 4.10.5

# TDE specific building variables
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
%dir %{python_sitearch}/python_tqt
%{python_sitearch}/python_tqt/__init__.py*
%{python_sitearch}/python_tqt/qt.so
%{python_sitearch}/python_tqt/qtcanvas.so
%{python_sitearch}/python_tqt/qtnetwork.so
%{python_sitearch}/python_tqt/qtsql.so
%{python_sitearch}/python_tqt/qttable.so
%{python_sitearch}/python_tqt/qtui.so
%{python_sitearch}/python_tqt/qtxml.so

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
%{python_sitearch}/python_tqt/qtgl.so

##########

%package tqtext
Summary:	TQt extensions for PyQt
Requires:	%{name} = %{version}-%{release}

%description tqtext
PyQt Extensions. Contains:

* TQScintilla: a featureful TQt source code editing component based
              on Scintilla.

%files tqtext
%defattr(-,root,root,-)
%{python_sitearch}/python_tqt/qtext.so

##########

%package -n trinity-pytqt-tools
Summary:	pyuic and pylupdate for TQt

%description -n trinity-pytqt-tools
pyuic is the PyQt counterpart for TQt's uic. It takes an XML
user interface file and generates Python code.

pylupdate is the counterpart for TQt's lupdate. It updates TQt
Linguist translation files from Python code.

%files -n trinity-pytqt-tools
%{tde_bindir}/pylupdate
%{tde_bindir}/pyuic

##########

%package devel
Summary:	TQt bindings for Python - Development files
Requires:	%{name} = %{version}-%{release}
Requires:	trinity-pytqt-tools = %{version}-%{release}

%description devel
Development .sip files with definitions of PyQt classes. They
are needed to build PyQt, but also as building blocks of other
packages based on them, like PyTDE.

%files devel
%defattr(-,root,root,-)
%{python_sitearch}/python_tqt/pyqtconfig.py*
%{_datadir}/sip/tqt/

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
%patch1 -p1 -b .sip4tqt


%build
unset QTDIR QTINC QTLIB

mkdir build
cd build

# WTF ? CentOS 6 !
cp -rf ../pyuic3 ../pylupdate3 

echo yes | python ../configure.py \
	-c -n %{_includedir}/tqscintilla \
	-q %{_datadir}/tqt3 \
	-y tqt-mt \
	-o %{_libdir} -u -j 10 \
	-d %{python_sitearch}/python_tqt \
	-v %{_datadir}/sip/tqt \
	-b %{tde_bindir} \
	-w \
	CXXFLAGS_RELEASE="" CXXFLAGS="${RPM_OPT_FLAGS} -I%{_includedir}/tqt" STRIP=""

%__make


%install
%__rm -rf %{?buildroot}
%__make install DESTDIR=%{?buildroot} -C build

%__install -d %{?buildroot}%{_datadir}/sip/
%__cp -rf sip/* %{?buildroot}%{_datadir}/sip/tqt/

# Dummy file to make a Python module
touch %{?buildroot}%{python_sitearch}/python_tqt/__init__.py


%clean
%__rm -rf %{?buildroot}%{python_sitearch}/python_tqt/__init__.py


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 3.18.1-1
- Initial release for TDE R14.0.0
