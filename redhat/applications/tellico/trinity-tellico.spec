# Default version for this component
%define kdecomp tellico
%define version 1.3.2.1
%define release 3

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	Icollection manager for books, videos, music [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://periapsis.org/tellico/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz


# [tellico] Fix compilation with GCC 4.7 [Bug #958]
Patch1:		tellico-3.5.13-fix_gcc47_compilation.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

Requires:	%{name}-data = %{version}-%{release}
Requires:	%{name}-scripts = %{version}-%{release}

%description
Tellico is a collection manager for TDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections; with unlimited
user-defined fields allowed. Automatically formatted names, sorting by any
property, filters, automatic ISBN validation and full customization for
printing or display through XSLT files are some of the features present. It
can import CSV, RIS, BibTeX, and BibTeXML files; and export CSV, HTML, BibTeX,
BibTeXML, and PilotDB. Tellico can also import data from Amazon, IMDb, CDDB,
or any US-MARC compliant z39.50 server.

The files are stored in XML format, avoiding the need for database server.
It also makes it easy for other softwares to use the Tellico data.


%package data
Group:		Applications/Utilities
Summary:	collection manager for books, videos, music [data] [Trinity]

%description data
Tellico is a collection manager for TDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections; with unlimited
user-defined fields allowed. Automatically formatted names, sorting by any
property, filters, automatic ISBN validation and full customization for
printing or display through XSLT files are some of the features present. It
can import CSV, RIS, BibTeX, and BibTeXML files; and export CSV, HTML, BibTeX,
BibTeXML, and PilotDB. Tellico can also import data from Amazon, IMDb, CDDB,
or any US-MARC compliant z39.50 server.

The files are stored in XML format, avoiding the need for database server.
It also makes it easy for other softwares to use the Tellico data.

This package contains the architecture independent files, such data files and
documentation.

%package scripts
Group:		Applications/Utilities
Summary:	collection manager for books, videos, music [scripts] [Trinity]

%description scripts
Tellico is a collection manager for TDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections; with unlimited
user-defined fields allowed. Automatically formatted names, sorting by any
property, filters, automatic ISBN validation and full customization for
printing or display through XSLT files are some of the features present. It
can import CSV, RIS, BibTeX, and BibTeXML files; and export CSV, HTML, BibTeX,
BibTeXML, and PilotDB. Tellico can also import data from Amazon, IMDb, CDDB,
or any US-MARC compliant z39.50 server.

The files are stored in XML format, avoiding the need for database server.
It also makes it easy for other softwares to use the Tellico data.

This package contains the scripts to import data from external sources, such
as websites. As the format of the data may change, these scripts are provided
as a separate package which can be updated through debian-volatile.


%prep
%setup -q -n applications/%{kdecomp}
%patch1 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Add svg icons to xdg directories
%__install -D -c -p -m 644 -T icons/tellico.svg %{?buildroot}%{_datadir}/icons/hicolor/scalable/apps/tellico.svg
%__install -D -c -p -m 644 -T icons/tellico_mime.svg %{?buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-tellico.svg

# Remove  dead symlink from French translation
%__rm %{?buildroot}%{tde_docdir}/HTML/fr/tellico/common


%find_lang %{kdecomp}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%{_bindir}/tellico
#%{_datadir}/pixmaps
%{_datadir}/applications
%{_datadir}/config/tellicorc

%files data
%defattr(-,root,root,-)
%{_datadir}/apps/tellico/*.xsl
%{_datadir}/apps/tellico/*.xml
%{_datadir}/apps/tellico/*.png
%{_datadir}/apps/tellico/entry-templates
%{_datadir}/apps/tellico/*.py*
%{_datadir}/apps/tellico/pics
%{_datadir}/apps/tellico/report-templates
%{_datadir}/apps/tellico/tellico.dtd
%{_datadir}/apps/tellico/tellico.tips
%{_datadir}/apps/tellico/tellico2html.js
%{_datadir}/apps/tellico/tellicoui.rc
%{_datadir}/apps/tellico/welcome.html
%{_datadir}/config.kcfg
%{tde_docdir}/HTML/*/tellico/
%{_datadir}/icons
%{_datadir}/apps/mime
%{_datadir}/mimelnk
%{_datadir}/apps/kconf_update/tellico-1-3-update.pl
%{_datadir}/apps/kconf_update/tellico-rename.upd
%{_datadir}/apps/kconf_update/tellico.upd

%files scripts
%defattr(-,root,root,-)
%{_datadir}/apps/tellico/data-sources
%{_datadir}/apps/tellico/z3950-servers.cfg


%Changelog
* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 1.3.2.1-3
- Fix compilation with GCC 4.7 [Bug #958]

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 1.3.2.1-2
- Fix HTML directory location

* Thu Nov 24 2011 Francois Andriot <francois.andriot@free.fr> - 1.3.2.1-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
