# Default version for this component
%define tde_pkg krecipes

# TDE variables
%define tde_version 14.0.0
%define tde_prefix /opt/trinity
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

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif



Name:			trinity-%{tde_pkg}
Summary:		Recipes manager for TDE
Version:		1.0beta2
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

# MYSQL support
BuildRequires:	mysql-devel

# POSTGRESQL support
BuildRequires:	postgresql-devel

# SQLITE support
BuildRequires:	sqlite-devel

%description
Krecipes is a TDE application designed to manage recipes. It can help you to
do your shopping list, search through your recipes to find what you can do
with available ingredients and a diet helper. It can also import or export
recipes from files in various format (eg RecipeML or Meal-Master) or from
databases.

%if 0%{?pclinuxos}
%debug_package
%endif

##########

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
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --docdir=%{tde_tdedocdir} \
  --libdir=%{tde_libdir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility \
  \
  --with-sqlite \
  --with-mysql \
  --with-postgresql

%__make %{?_smp_mflags} || %__make


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{tde_pkg}


%clean
%__rm -rf %{buildroot}


%post
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done


%postun
for f in crystalsvg hicolor ; do
  touch --no-create %{tde_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{tde_datadir}/icons/${f} || :
done


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_bindir}/krecipes
%{tde_datadir}/applnk/Utilities/krecipes.desktop
%{tde_datadir}/apps/krecipes/
%{tde_datadir}/icons/crystalsvg/*/mimetypes/krecipes_file.png
%{tde_datadir}/icons/hicolor/*/apps/krecipes.png
%{tde_datadir}/mimelnk/application/x-krecipes-backup.desktop
%{tde_datadir}/mimelnk/application/x-krecipes-recipes.desktop
%lang(da) %{tde_tdedocdir}/HTML/da/
%lang(en) %{tde_tdedocdir}/HTML/en/
%lang(es) %{tde_tdedocdir}/HTML/es/
%lang(et) %{tde_tdedocdir}/HTML/et/
%lang(pt) %{tde_tdedocdir}/HTML/pt/
%lang(sv) %{tde_tdedocdir}/HTML/sv/


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 1.0beta2-1
- Initial release for TDE 14.0.0
