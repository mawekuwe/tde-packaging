# Default version for this component
%define tdecomp tqscintilla
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

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tdecomp}
Summary:		TQt source code editing component based on Scintilla
Version:		1.7.1
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Development/Tools

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
Url:		http://www.riverbankcomputing.co.uk/qscintilla/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

# Fix FTBFS when using TQT3
Patch0:		tqscintilla-14.0.0-ftbfs.patch

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

%description
Scintilla is a free source code editing component. It has features found
in standard editing components, as well as features especially useful
when editing and debugging source code.

TQScintilla is a port or Scintilla to the TQt GUI toolkit.


%package designer
Summary:        TQScintilla designer plugin 
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}
Requires:       trinity-tqt3-designer

%description designer
%{summary}.

%package devel
Summary:        TQScintilla Development Files
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       trinity-tqt3-devel 

%description devel
%{summary}.

%package doc
Summary:        TQScintilla Documentation
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}
%patch0 -p1 -b .ftbfs

%__sed -i "designer/designer.pro" \
  -e "s|\$(QTDIR)|%{_libdir}/tqt3|" \
  -e "s|# DESTDIR|DESTDIR|"

( cd qt; tqmake "DESTDIR=$PWD/../tmplib" )
( cd designer; tqmake )


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%__make %{?_smp_mflags} -C qt
%__make %{?_smp_mflags} -C designer


%install
unset QTDIR QTINC QTLIB
export QTDIR=%{_libdir}/tqt3
%__rm -rf $RPM_BUILD_ROOT

# Installs the QT part
%__make INSTALL_ROOT=$RPM_BUILD_ROOT -C qt install

# Installs supplementary headers
for i in include/*.h; do
	%__install -D -m 644 $i %{buildroot}${QTINC}/private/${i##*/}
done

# Installs the HTML documentation
for i in doc/html/*; do
	%__install -D -m 644 $i %{buildroot}%{tde_docdir}/HTML/en/%{name}/${i##*/}
done

# Installs the Designer plugin
for i in designer/*.so; do
	%__install -D -m 644 $i %{buildroot}${QTDIR}/plugins/designer/${i##*/}
done

# Installs libraries
%__mkdir_p %{buildroot}%{_libdir}
%__mv -f tmplib/* %{buildroot}%{_libdir}

# Fix private headers location
%__mv -f %{buildroot}/private %{buildroot}%{_includedir}/tqt3
%__mv -f %{buildroot}%{_includedir}/tqt3 %{buildroot}%{_includedir}/tqscintilla

%clean
%__rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE NEWS README
%{_libdir}/libqscintilla.so.*
%{_datadir}/tqt3/translations/*.qm

%files designer
%defattr(-,root,root,-)
%{_libdir}/tqt3/plugins/designer/*.so

%files devel
%defattr(-,root,root,-)
%doc doc/html doc/Scintilla example
%{_includedir}/tqscintilla/*.h
%{_includedir}/tqscintilla/private/*.h
%{_libdir}/libqscintilla.so

%files doc
%defattr(-,root,root,-)
%{tde_docdir}/HTML/en/%{name}

%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 1.7.1-1
- Initial release for TDE 14.0.0
