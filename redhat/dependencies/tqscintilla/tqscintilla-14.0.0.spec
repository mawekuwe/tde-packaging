#
# spec file for package tqscintilla (version R14.0.0)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http:/www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%define tde_version 14.0.0
%define tde_pkg tqscintilla
%define tde_prefix /opt/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc

%if 0%{?mdkversion} || 0%{?mgaversion} || 0%{?pclinuxos}
%define libtqscintilla %{_lib}tqscintilla
%else
%define libtqscintilla libtqscintilla
%endif


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.7.1
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:	TQt source code editing component based on Scintilla
Group:		Development/Libraries/C and C++
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gcc-c++

%description
Scintilla is a free source code editing component. It has features found
in standard editing components, as well as features especially useful
when editing and debugging source code.

TQScintilla is a port or Scintilla to the TQt GUI toolkit.

##########

%package -n %{libtqscintilla}7
Summary:	TQt source code editing component based on Scintilla
Group:		Development/Libraries/C and C++
Provides:	libtqscintilla = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libtqscintilla}7
Scintilla is a free source code editing component. It has features found
in standard editing components, as well as features especially useful
when editing and debugging source code.

TQScintilla is a port or Scintilla to the TQt GUI toolkit.

%post -n %{libtqscintilla}7
/sbin/ldconfig

%postun -n %{libtqscintilla}7
/sbin/ldconfig

%files -n %{libtqscintilla}7
%defattr(-,root,root,-)
%doc ChangeLog LICENSE NEWS README
%{_libdir}/libqscintilla.so.7
%{_libdir}/libqscintilla.so.7.0
%{_libdir}/libqscintilla.so.7.0.1
%{_libdir}/tqt3/plugins/designer/*.so
%{_datadir}/tqt3/translations/*.qm

##########

%package -n %{libtqscintilla}-devel
Summary:	TQScintilla Development Files
Group:		Development/Libraries/C and C++
Provides:	libtqscintilla-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	%{libtqscintilla}7 = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	tqt3-devel >= 3.5.0

%description -n %{libtqscintilla}-devel
This package contains the development files for tqscintilla.

%post -n %{libtqscintilla}-devel
/sbin/ldconfig

%postun -n %{libtqscintilla}-devel
/sbin/ldconfig

%files -n %{libtqscintilla}-devel
%defattr(-,root,root,-)
%doc doc/Scintilla example
%{_includedir}/tqscintilla/
%{_libdir}/libqscintilla.so

##########

%package -n %{libtqscintilla}-doc
Summary:	TQScintilla Documentation
Group:		Development/Libraries/C and C++
Requires:	%{libtqscintilla}7 = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{libtqscintilla}-doc
This package contains the documentation for tqscintilla.

%files -n %{libtqscintilla}-doc
%defattr(-,root,root,-)
%{tde_docdir}/HTML/en/%{name}/

##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

# Fix perms
chmod -x doc/Scintilla/*
chmod -x example/*

# Fix path in project files
%__sed -i "qt/qscintilla.pro" \
  -e "s|^INCLUDEPATH = .*|INCLUDEPATH = . ../include ../src /usr/include/tqt /usr/include/tqt3|" \
  -e "s|^header.path = .*|header.path = %{_includedir}/tqt3|" \
  -e "s|^trans.path = .*|trans.path = %{_datadir}/tqt3/translations|"

%__sed -i "designer/designer.pro" \
  -e "s|\$(QTDIR)|%{_libdir}/tqt3|" \
  -e "s|# DESTDIR|DESTDIR|"

export QTDIR=%{_libdir}/tqt3
( cd qt; tqmake "DESTDIR=$PWD/../tmplib" )
( cd designer; tqmake )


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

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

# Installs the HTML documentation correctly
for i in doc/html/*; do
	%__install -D -m 644 $i %{buildroot}%{tde_docdir}/HTML/en/%{name}/${i##*/}
done
#__mkdir_p %{?buildroot}%{tde_docdir}/HTML/en/
#__mv -f %{?buildroot}%{_docdir} %{?buildroot}%{tde_docdir}/HTML/en/%{name}

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


# Fix permissions
chmod a-x %{buildroot}%{_includedir}/tqscintilla/*.h
chmod a-x %{buildroot}%{_includedir}/tqscintilla/*.h


%clean
%__rm -rf $RPM_BUILD_ROOT


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2:1.7.1-1
- Initial release for TDE 14.0.0
