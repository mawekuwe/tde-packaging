# Default version for this component
%define kdecomp kbarcode

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/kde
%define tde_tdeincludedir %{tde_includedir}/kde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-%{kdecomp}
Summary:	barcode and label printing application for Trinity
Version:	2.0.6
Release:	1%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.kbarcode.net

Prefix:    %{tde_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [kbarcode] Fix 'format not a string literal' error [Commit #14ba7d8a]
Patch1:		kbarcode-3.5.13-fix_format_not_a_string_literal.patch
# [kbarcode] Fix FTBFS [Commit #62777d27]
Patch2:		kbarcode-3.5.13-fix_ftbfs.patch
# [kbarcode] Fix remaining string format errors [Commit #b8dc3f57]
Patch3:		kbarcode-3.5.13-fix_remaining_string_literal.patch


BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-tdelibs-devel
BuildRequires:	trinity-tdebase-devel
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
different data sources, including SQL databases, CSV files and the KDE address
book.

Additionally it is a simple barcode generator (similar to the old xbarcode you
might know). All major types of barcodes like EAN, UPC, CODE39 and ISBN are
supported. Even complex 2D barcodes are supported using third party tools. The
generated barcodes can be directly printed or you can export them into images
to use them in another application.


%prep
%setup -q -n applications/%{kdecomp}
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i "admin/acinclude.m4.in" \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --disable-rpath \
  --with-extra-includes=%{_includedir}/tqt

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%find_lang %{kdecomp} || touch %{kdecomp}.lang



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


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{tde_bindir}/kbarcode
%{tde_tdelibdir}/kfile_kbarcode.la
%{tde_tdelibdir}/kfile_kbarcode.so
%{tde_tdeappdir}/kbarcode-batch.desktop
%{tde_tdeappdir}/kbarcode-editor.desktop
%{tde_tdeappdir}/kbarcode-label.desktop
%{tde_tdeappdir}/kbarcode-single.desktop
%{tde_tdeappdir}/kbarcode.desktop
%{tde_datadir}/apps/kbarcode/
%{tde_datadir}/icons/hicolor/*/actions/barcode.png
%{tde_datadir}/icons/hicolor/*/actions/kbarcodeellipse.png
%{tde_datadir}/icons/hicolor/*/actions/kbarcodegrid.png
%{tde_datadir}/icons/hicolor/*/actions/kbarcodelinetool.png
%{tde_datadir}/icons/hicolor/*/actions/kbarcoderect.png
%{tde_datadir}/icons/hicolor/*/apps/kbarcode.png
%{tde_datadir}/services/kfile_kbarcode.desktop


%Changelog
* Wed Nov 30 2011 Francois Andriot <francois.andriot@free.fr> - 2.0.6-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
