# Default version for this component
%define tde_pkg kscope
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

%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:           trinity-%{tde_pkg}
Version:        1.6.2
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:        source editing environment for TDE 

Group:          Applications/Internet
License:        GPLv2+
URL:            http://kscope.sourceforge.net
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext
Requires:		cscope

%description
KScope is a TDE front-end to Cscope. It provides a source-editing environment
for large C projects. KScope is focused on source editing and analysis.

KScope is built around an efficient mechanism for code-navigation, which
allows the user to run queries on the code.

The types of queries KScope can run include:
* Get all references to a symbol
* Find the definition of a symbol
* Find all functions called by or calling to a function
* Find an EGrep pattern
* Find all files #including some file

These queries are handled by an underlying Cscope process. KScope simply
serves as a front-end to this process, feeding it with queries, and parsing
its output into result lists. The items in those lists can later be selected
to open an editor at the matching line.

Main Features:
* Multiple editor windows (using your favourite TDE editor)
* Project management
* Front-end to most Cscope queries
* Tag list for every open editor
* Call-tree window
* Session management, including saving and restoring queries
* Works with externally-built cscope.out files


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --enable-gcc-hidden-visibility
  
%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{tde_pkg}


%clean
%__rm -rf $RPM_BUILD_ROOT


%post
for i in hicolor locolor ; do
 touch --no-create %{tde_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{tde_datadir}/icons/$i 2>/dev/null || :
done


%postun
for i in hicolor locolor ; do
 touch --no-create %{tde_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{tde_datadir}/icons/$i 2>/dev/null || :
done


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{tde_bindir}/kscope
%{tde_datadir}/applnk/Development/kscope.desktop
%{tde_datadir}/apps/kscope/
%{tde_tdedocdir}/HTML/en/kscope/
%{tde_datadir}/icons/hicolor/*/apps/kscope.png
%{tde_datadir}/icons/locolor/*/apps/kscope.png


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 1.6.2-1
- Initial release for TDE 14.0.0
