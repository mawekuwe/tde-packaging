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

%define tde_tdeappdir %{tde_datadir}/applications/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:           trinity-kbibtex
Version:        0.2.3
Release:        1%{?dist}%{?_variant}
Summary:        A BibTeX editor for TDE

Group:          Applications/Internet
License:        GPLv2+
URL:            http://www.unix-ag.uni-kl.de/~fischer/kbibtex/download.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        http://www.unix-ag.uni-kl.de/~fischer/kbibtex/download/kbibtex-0.2.3.tar.bz2

Patch1:			kbibtex-0.2.3-trinity.patch

BuildRequires: trinity-tdelibs-devel

%description
KBibTeX is a BibTeX editor for KDE to edit bibliographies used with LaTeX.
KBibTeX is released under the GNU Public License (GPL) version 2 or any later version.

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

%prep
%setup -q -n kbibtex-%{version}
%patch1 -p1 -b .trinity

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"



%build
unset QTDIR; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

export KDEDIR="%{tde_prefix}"

export CPPFLAGS="${CPPFLAGS} -I%{tde_includedir}/tqt"

%configure \
	--prefix=%{tde_prefix} \
	--exec-prefix=%{tde_prefix} \
	--disable-dependency-tracking \
	--disable-rpath \
	--with-extra-includes=%{tde_includedir}/tqt \
	--with-qt-libraries=${QTLIB:-${QTDIR}/%{_lib}} \
	--bindir=%{tde_bindir} \
	--libdir=%{tde_libdir} \
	--mandir=%{tde_mandir} \
	--datadir=%{tde_datadir} \
	--includedir=%{tde_tdeincludedir} 
  
%__make %{?_smp_mflags} LIBTOOL=$(which libtool) || %__make LIBTOOL=$(which libtool)


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

# Useless files ..
%__rm -f %{?buildroot}%{tde_tdelibdir}/*.a

%find_lang kbibtex


%clean
rm -rf $RPM_BUILD_ROOT


%post
for i in hicolor ; do
 touch --no-create %{tde_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{tde_datadir}/icons/$i 2>/dev/null || :
done

%postun
for i in hicolor ; do
 touch --no-create %{tde_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{tde_datadir}/icons/$i 2>/dev/null || :
done


%files -f kbibtex.lang
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING NEWS README TODO ChangeLog
%{tde_bindir}/kbibtex
%{tde_tdelibdir}/libkbibtexpart.la
%{tde_tdelibdir}/libkbibtexpart.so
%{tde_tdeappdir}/kbibtex.desktop
%{tde_datadir}/apps/kbibtex/
%{tde_datadir}/apps/kbibtexpart/kbibtex_part.rc
%{tde_datadir}/apps/kbibtexpart/xslt/MARC21slim2MODS3.xsl
%{tde_datadir}/apps/kbibtexpart/xslt/MARC21slimUtils.xsl
%{tde_datadir}/apps/kbibtexpart/xslt/UNIMARC2MODS3.xsl
%{tde_datadir}/apps/kbibtexpart/xslt/html.xsl
%{tde_tdedocdir}/HTML/en/kbibtex/
%{tde_datadir}/icons/hicolor/*/apps/kbibtex.png
%{tde_datadir}/services/kbibtex_part.desktop
%{tde_mandir}/man1/kbibtex.1*


%changelog
* Fri Mar 29 2013 Francois Andriot <francois.andriot@free.fr> - 0.2.3-1
- Initial release for TDE 3.5.13.2
