# Default version for this component
%define tde_pkg kbarcode
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
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:			trinity-%{tde_pkg}
Summary:		barcode and label printing application for Trinity
Version:		2.0.6
Release:		%{?!preversion:5}%{?preversion:4_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.kbarcode.net

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz


BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext


%description
KBarcode is a barcode and label printing application for Trinity. It can be used
to print everything from simple business cards up to complex labels with
several barcodes (e.g. article descriptions).

KBarcode comes with an easy to use WYSIWYG label designer, a setup wizard,
batch import of data for batch printing labels (directly from the delivery
note), thousands of predefined labels, database management tools and
translations in many languages. Even printing more than 10.000 labels in one
go is no problem for KBarcode. Data for printing can be imported from several
different data sources, including SQL databases, CSV files and the TDE address
book.

Additionally it is a simple barcode generator (similar to the old xbarcode you
might know). All major types of barcodes like EAN, UPC, CODE39 and ISBN are
supported. Even complex 2D barcodes are supported using third party tools. The
generated barcodes can be directly printed or you can export them into images
to use them in another application.


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif


%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  \
  --disable-dependency-tracking \
  --disable-debug \
  --enable-new-ldflags \
  --enable-final \
  --enable-closure \
  --enable-rpath \
  --disable-gcc-hidden-visibility \
  \
  --with-extra-includes=%{_includedir}/pcre

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%find_lang %{tde_pkg}



%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
update-desktop-database %{tde_appdir} &> /dev/null

%postun
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :
update-desktop-database %{tde_appdir} &> /dev/null


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_bindir}/kbarcode
%{tde_tdelibdir}/tdefile_kbarcode.la
%{tde_tdelibdir}/tdefile_kbarcode.so
%{tde_tdeappdir}/kbarcode-batch.desktop
%{tde_tdeappdir}/kbarcode-editor.desktop
%{tde_tdeappdir}/kbarcode-single.desktop
%{tde_tdeappdir}/kbarcode.desktop
%{tde_datadir}/mimelnk/application/kbarcode-label.desktop
%{tde_datadir}/apps/kbarcode/
%{tde_datadir}/icons/hicolor/*/actions/barcode.png
%{tde_datadir}/icons/hicolor/*/actions/kbarcodeellipse.png
%{tde_datadir}/icons/hicolor/*/actions/kbarcodegrid.png
%{tde_datadir}/icons/hicolor/*/actions/kbarcodelinetool.png
%{tde_datadir}/icons/hicolor/*/actions/kbarcoderect.png
%{tde_datadir}/icons/hicolor/*/apps/kbarcode.png
%{tde_datadir}/services/tdefile_kbarcode.desktop
%{tde_tdedocdir}/HTML/en/kbarcode/


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2.0.6-5
- Initial release for TDE 14.0.0
