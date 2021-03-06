%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define tde_version 3.5.13.2

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

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-pytdeextensions
Summary:	Python packages to support TDE applications (scripts) [Trinity]
Version:	0.4.0
Release:	%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.simonzone.com/software/pykdeextensions

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz


# [pykdeextensions] Fix hardcoded path to Guidance python libraries [Bug #999]
Patch2:		pykdeextensions-3.5.13.2-fix_extra_module_dir.patch
# [pykdeextensions] Fix include directory search location
Patch5:		pykdeextensions-3.5.13.2-fix_include_dir.patch

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

# Python stuff
BuildRequires:	python-qt3-devel
BuildRequires:	trinity-python-trinity-devel

Requires:		trinity-libpythonize0 = %{version}-%{release}

Obsoletes:		trinity-pykdeextensions < %{version}-%{release}
Provides:		trinity-pykdeextensions = %{version}-%{release}


%description
PyTDE Extensions is a collection of software and Python packages
to support the creation and installation of TDE applications.


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_datadir}/apps/pykdeextensions/
%{tde_tdedocdir}/HTML/en/pykdeextensions/
%{python_sitearch}/*

##########

%package -n trinity-libpythonize0
Summary:		Python packages to support KDE applications (library) [Trinity]	
Group:			Environment/Libraries

%description -n trinity-libpythonize0
PyTDE Extensions is a collection of software and Python packages
to support the creation and installation of KDE applications.

This package contains the libpythonize library files.

%post -n trinity-libpythonize0
/sbin/ldconfig

%postun -n trinity-libpythonize0
/sbin/ldconfig

%files -n trinity-libpythonize0
%defattr(-,root,root,-)
%{tde_libdir}/libpythonize.so.*

##########

%package -n trinity-libpythonize0-devel
Summary:		Python packages to support KDE applications (development) [Trinity]
Group:			Development/Libraries
Requires:		trinity-libpythonize0 = %{version}-%{release}

%description -n trinity-libpythonize0-devel
PyTDE Extensions is a collection of software and Python packages
to support the creation and installation of TDE applications.

This package contains the libpythonize development files.

%post -n trinity-libpythonize0-devel
/sbin/ldconfig

%postun -n trinity-libpythonize0-devel
/sbin/ldconfig

%files -n trinity-libpythonize0-devel
%defattr(-,root,root,-)
%{tde_tdeincludedir}/*.h
%{tde_libdir}/libpythonize.la
%{tde_libdir}/libpythonize.so

##########

%package devel
Summary:		Meta-package to install all pytdeextensions development files
Group:			Development/Libraries
Requires:		%{name}-devel = %{version}-%{release}
Requires:		trinity-libpythonize0-devel = %{version}-%{release}

%description devel
%{summary}

%files devel

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
%patch2 -p1 -b .extramodule
%patch5 -p1 -b .incdir

# Changes library directory to 'lib64'
# Also other fixes for distributions ...
for f in src/*.py; do
  %__sed -i "${f}" \
    -e "s|%{tde_prefix}/lib/|%{tde_libdir}/|g" \
    -e "s|/usr/lib/pyshared/python\*|%{python_sitearch}|g" \
    -e "s|'pykde-dir=',None,|'pykde-dir=','%{python_sitearch}',|g" \
    -e "s|self.pykde_dir = None|self.pykde_dir = \"%{python_sitearch}\"|g" \
    -e "s|%{tde_includedir}/kde|%{tde_tdeincludedir}|g" \
    -e 's|"/kde"|"/tde"|'
done

# Do not look for 'libpython2.x.so' (from -devel) package.
# Instead look for versioned runtime library.
LIBPYTHON="$(readlink %{_libdir}/libpython2.*.so)"
if [ -f "%{_libdir}/${LIBPYTHON}" ]; then
  %__sed -i "src/kdedistutils.py" \
    -e "s|#define LIB_PYTHON \".*\"|#define LIB_PYTHON \"%{_libdir}/${LIBPYTHON}\"|"
fi

# Set PyQt directory to actual directory
%__sed -i "src/kdedistutils.py" \
  -e "s|'pyqt-dir=','%{python_sitearch}'|'pyqt-dir=','%{python_sitearch}/python-qt3'|g" \
  -e "s|self.pyqt_dir = \"%{python_sitearch}\"|self.pyqt_dir = \"%{python_sitearch}/python-qt3\"|g"


%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PYTHONPATH=%{python_sitearch}/trinity-sip:%{python_sitearch}/python-qt3

%__mkdir_p build
./setup.py build_libpythonize

%install
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export PYTHONPATH=%{python_sitearch}/trinity-sip:%{python_sitearch}/python-qt3

# Avoids 'error: byte-compiling is disabled.' on Mandriva/Mageia
export PYTHONDONTWRITEBYTECODE=

%__rm -rf %{buildroot}

./setup.py install \
	--root=%{buildroot} \
	--prefix=%{tde_prefix} \
	--install-clib=%{tde_libdir} \
	--install-cheaders=%{tde_tdeincludedir} \
   -v

# Removes BUILDROOT directory reference in installed files
for f in \
	%{buildroot}%{tde_libdir}/libpythonize.la \
	%{buildroot}%{tde_datadir}/apps/pykdeextensions/app_templates/kcontrol_module/src/KcontrolModuleWidgetUI.py \
	%{buildroot}%{tde_datadir}/apps/pykdeextensions/app_templates/kdeutility/src/KDEUtilityDialogUI.py \
; do
	%__sed -i "${f}" -e "s|%{buildroot}||g"
:
done

# Moves PYTHON libraries to distribution directory
%__mkdir_p %{buildroot}%{python_sitearch}
%__mv -f %{buildroot}%{tde_prefix}/lib/python*/site-packages/* %{buildroot}%{python_sitearch}
%__rm -rf %{buildroot}%{tde_prefix}/lib/python*/site-packages

# Removes useless files
%__rm -rf %{?buildroot}%{tde_libdir}/*.a

# Fix permissions on include files
%__chmod 644 %{?buildroot}%{tde_tdeincludedir}/*.h


%clean
%__rm -rf %{buildroot}


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 0.4.0-5
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 0.4.0-4
- Initial release for TDE 3.5.13.2

* Tue Oct 02 2012 Francois Andriot <francois.andriot@free.fr> - 0.4.0-3
- Initial release for TDE 3.5.13.1
