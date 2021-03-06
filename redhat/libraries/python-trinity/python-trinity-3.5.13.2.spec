%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif
%define tde_version 3.5.13.2

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

%define __arch_install_post %{nil}


Name:		trinity-python-trinity
Summary:	Trinity bindings for Python [Trinity]
Version:	3.16.3
Release:	%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
#URL:		http://www.simonzone.com/software/pykdeextensions
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

# Fix include subdirectory 'tde' instead of 'kde'
Patch1:		python-trinity-3.5.13.2-fix_tde_includedir.patch
# Fix "is private" FTBFS using SIP >= 4.15
Patch2:		python-trinity-3.5.13.2-fix_is_private.patch

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

# PYTHON support
BuildRequires:	python
BuildRequires:	python-qt3-devel

# SIP support
%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
# RHEL 4/5 comes with old version, so we brought ours ...
BuildRequires:	trinity-sip-devel
%endif
%if 0%{?mgaversion} || 0%{?mdkversion}
BuildRequires:	python-sip
%endif
%if 0%{?rhel} >= 6 || 0%{?fedora}
BuildRequires:	sip-devel
%endif
%if 0%{?suse_version}
BuildRequires:	python-sip-devel
%endif

Obsoletes:	python-trinity < %{version}-%{release}
Provides:	python-trinity = %{version}-%{release}

%description
Python binding module that provides wide access to the Trinity API,
also known as PyTDE. Using this, you'll get (for example) classes
from kio, kjs, khtml and kprint.


%package devel
Summary:		Trinity bindings for Python - Development files and scripts [Trinity]
Group:			Development/Libraries
Requires:		%{name} = %{version}-%{release}

Obsoletes:	python-trinity-devel < %{version}-%{release}
Provides:	python-trinity-devel = %{version}-%{release}

%description devel
Development .sip files with definitions of PyTDE classes. They
are needed to build PyTDE, but also as building blocks of other
packages based on them. 
The package also contains kdepyuic, a wrapper script around python-qt3's 
user interface compiler.


%package doc
Summary:		Documentation and examples for PyTDE [Trinity]
Group:			Development/Libraries

Obsoletes:	python-trinity-doc < %{version}-%{release}
Provides:	python-trinity-doc = %{version}-%{release}

%description doc
General documentation and examples for PyTDE providing programming
tips and working code you can use to learn from.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
%patch1 -p1 -b .inc
%patch2 -p1 -b .private


%build
unset QTDIR QTINC QTLIB
. /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export LD_RUN_PATH="%{tde_libdir}"
export KDEDIR=%{tde_prefix}

export DH_OPTIONS

export PYTHONPATH=%{python_sitearch}/trinity-sip:%{python_sitearch}/python-qt3

%__python configure.py \
	-k %{tde_prefix} \
	-L %{_lib} \
	-v %{_datadir}/sip/trinity

# Shitty hack to add LDFLAGS
%if 0%{?mgaversion} || 0%{?mdkversion}
%__sed -i */Makefile \
	-e "/^LIBS = / s|$| -lpython2.7 -lDCOP -lkdecore -lkdefx -lkdeui -lkresources -lkabc -lkparts -lkio|"
%endif

# Shitty hack to fix issue with SIP >= 4.15
%__sed -i "kfile/sipkfilepart0.cpp" \
  -e "s| KFileIconView::selectionMode(| KFileView::selectionMode(|g" \
  -e "s| KFileIconView::clear()| KFileView::clear()|g" \
  -e "s| KFileDetailView::selectionMode(| KFileView::selectionMode(|g" \
  -e "s| KFileDetailView::clear()| KFileView::clear()|g"
  

%__make %{_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Install documentation
%__mkdir_p %{buildroot}%{tde_tdedocdir}/HTML/en/
%__cp -rf doc %{buildroot}%{tde_tdedocdir}/HTML/en/python-trinity/


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
%{tde_bindir}/kdepyuic
# The SIP files are outside TDE's prefix
%{_datadir}/sip/trinity/

%files doc
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/en/python-trinity/


%changelog
* Fri Aug 16 2013 Francois Andriot <francois.andriot@free.fr> - 3.6.13-5
- Build for Fedora 19

* Mon Jun 03 2013 Francois Andriot <francois.andriot@free.fr> - 3.16.3-4
- Initial release for TDE 3.5.13.2

* Tue Oct 02 2012 Francois Andriot <francois.andriot@free.fr> - 3.16.3-3
- Initial release for TDE 3.5.13.1
