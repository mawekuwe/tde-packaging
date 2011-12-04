# Default version for this component
%define kdecomp python-trinity
%define version 3.16.3
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


Name:		%{kdecomp}
Summary:	Trinity bindings for Python [Trinity]
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

## RHEL/Fedora patches
Patch0:		python-trinity-3.5.13-install_directories.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	python
BuildRequires:	PyQt-devel


%description
Python binding module that provides wide access to the Trinity API,
also known as PyKDE. Using this, you'll get (for example) classes
from kio, kjs, khtml and kprint.


%package devel
Summary:		Trinity bindings for Python - Development files and scripts [Trinity]
Group:			Development/Libraries

%description devel
Development .sip files with definitions of PyKDE classes. They
are needed to build PyKDE, but also as building blocks of other
packages based on them. 
The package also contains kdepyuic, a wrapper script around PyQt's 
user interface compiler.


%package doc
Summary:		Documentation and examples for PyKDE [Trinity]
Group:			Development/Libraries

%description doc
General documentation and examples for PyKDE providing programming
tips and working code you can use to learn from.


%prep
%setup -q -n libraries/%{kdecomp}
%patch0 -p0

# Hack to get TQT include files under /opt
%__sed -i "configure.py" \
	-e "s,/usr/include/tqt,%{_includedir}/tqt,g"

%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%__python configure.py \
	-k %{_prefix} \
	-L %{_lib} \
	-v %{_datadir}/sip/trinity
%__make %{_smp_mflags}

%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Install documentation
%__mkdir_p %{buildroot}%{tde_docdir}/HTML/en
%__cp -rf doc %{buildroot}%{tde_docdir}/HTML/en/%{name}



%clean
%__rm -rf %{buildroot}



%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{python_sitearch}/*.so
%{python_sitearch}/dcop*.py*
%{python_sitearch}/pykde*.py*

%files devel
%defattr(-,root,root,-)
%{_bindir}/kdepyuic
%{_datadir}/sip/trinity

%files doc
%defattr(-,root,root,-)
%{tde_docdir}/HTML/en/%{name}


%Changelog
* Fri Dec 02 2011 Francois Andriot <francois.andriot@free.fr> - 3.16.3-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
