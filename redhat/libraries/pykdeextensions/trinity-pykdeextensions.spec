# Default version for this component
%define kdecomp pykdeextensions
%define version 0.4.0
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
Summary:	Python packages to support KDE applications (scripts) [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.simonzone.com/software/pykdeextensions

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	PyQt-devel
BuildRequires:	python-trinity-devel

%description
PyKDE Extensions is a collection of software and Python packages
to support the creation and installation of KDE applications.


%package -n trinity-libpythonize0
Summary:		Python packages to support KDE applications (library) [Trinity]	
Group:			Environment/Libraries

%description -n trinity-libpythonize0
PyKDE Extensions is a collection of software and Python packages
to support the creation and installation of KDE applications.

This package contains the libpythonize library files.


%package -n trinity-libpythonize0-devel
Summary:		Python packages to support KDE applications (development) [Trinity]
Group:			Development/Libraries
Requires:		trinity-libpythonize0

%description -n trinity-libpythonize0-devel
PyKDE Extensions is a collection of software and Python packages
to support the creation and installation of KDE applications.

This package contains the libpythonize development files.


%prep
%setup -q -n libraries/%{kdecomp}

# Changes library directory to 'lib64'
for f in src/*.py; do
  %__sed -i "${f}" \
    -e "s,%{_prefix}/lib,%{_libdir},g" \
    -e "s,/usr/lib/pyshared/python2.6,%{python_sitearch},g" \
    -e "s|'pykde-dir=',None,|'pykde-dir=','%{python_sitearch}',|g" \
    -e "s|self.pykde_dir = None|self.pykde_dir = \"%{python_sitearch}\"|g" \
    -e "s|/usr/include/tqt|%{_includedir}/tqt|g"
done

%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

./setup.py build_libpythonize

%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
./setup.py install \
	--root=%{buildroot} \
	--prefix=%{_prefix} \
	--install-clib=%{_libdir} \
	--install-cheaders=%{tde_includedir}

# Removes BUILDROOT directory reference in installed files
for f in \
	%{buildroot}%{_libdir}/libpythonize.la \
	%{buildroot}%{_datadir}/apps/pykdeextensions/app_templates/kcontrol_module/src/KcontrolModuleWidgetUI.py \
	%{buildroot}%{_datadir}/apps/pykdeextensions/app_templates/kdeutility/src/KDEUtilityDialogUI.py \
; do
	%__sed -i "${f}" -e "s,%{buildroot},,g"
:
done

# Moves PYTHON libraries to distribution directory
%__mkdir_p %{buildroot}%{python_sitearch}
%__mv -f %{buildroot}%{_prefix}/lib/python*/site-packages/* %{buildroot}%{python_sitearch}
%__rm -rf %{buildroot}%{_prefix}/lib/python2.7/site-packages


%clean
%__rm -rf %{buildroot}


%post -n trinity-libpythonize0 -p /sbin/ldconfig
%postun -n trinity-libpythonize0 -p /sbin/ldconfig

%post -n trinity-libpythonize0-devel -p /sbin/ldconfig
%postun -n trinity-libpythonize0-devel -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_datadir}/apps/pykdeextensions
%{tde_docdir}/HTML/en/pykdeextensions
%{python_sitearch}/*

%files -n trinity-libpythonize0
%defattr(-,root,root,-)
%{_libdir}/libpythonize.so.*

%files -n trinity-libpythonize0-devel
%defattr(-,root,root,-)
%{tde_includedir}/*.h
%{_libdir}/libpythonize.a
%{_libdir}/libpythonize.la
%{_libdir}/libpythonize.so


%Changelog
* Thu Dec 01 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.0svn20080103-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
