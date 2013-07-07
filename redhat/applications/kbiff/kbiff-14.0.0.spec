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

Name:           trinity-kbiff
Version:        3.9
Release:        1%{?dist}%{?_variant}
Summary:        An NMAP frontend for TDE

Group:          Applications/Internet
License:        GPLv2+
URL:            http://sourceforge.net/projects/knmap/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        http://ftp.de.debian.org/debian/pool/main/k/kbiff/kbiff_3.9.orig.tar.bz2

Patch0:			kbiff-3.9-trinity.patch


BuildRequires:	desktop-file-utils
BuildRequires:	trinity-tdelibs-devel
Requires:		nmap

%description


%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

%prep
%setup -q -n kbiff-%{version}
%patch0 -p1 -b .trinity

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

%configure \
	--prefix=%{tde_prefix} \
	--exec-prefix=%{tde_prefix} \
	--disable-dependency-tracking \
	--disable-rpath \
	--with-extra-includes=%{tde_includedir}/tqt \
	--with-qt-libraries=${QTLIB:-${QTDIR}/%{_lib}} \
	--bindir=%{tde_bindir} \
	--libdir=%{tde_libdir} \
	--datadir=%{tde_datadir} \
	--includedir=%{tde_tdeincludedir} \
	--mandir=%{tde_mandir}
  
%__make %{?_smp_mflags} LIBTOOL=$(which libtool)


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

# Useless files ..
%__rm -f %{?buildroot}%{tde_libdir}/*.a
%__rm -f %{?buildroot}%{tde_tdelibdir}/*.a

%find_lang kbiff

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

%files -f kbiff.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{tde_bindir}/kbiff
%{tde_libdir}/libkdeinit_kbiff.la
%{tde_libdir}/libkdeinit_kbiff.so
%{tde_tdelibdir}/kbiff.la
%{tde_tdelibdir}/kbiff.so
%{tde_datadir}/applnk/Internet/kbiff.desktop
%{tde_datadir}/apps/kbiff/pics/delete.png
%{tde_datadir}/apps/kbiff/pics/mailbox.png
%{tde_datadir}/apps/kbiff/pics/mini-newmail.png
%{tde_datadir}/apps/kbiff/pics/mini-noconn.png
%{tde_datadir}/apps/kbiff/pics/mini-nomail.png
%{tde_datadir}/apps/kbiff/pics/mini-oldmail.png
%{tde_datadir}/apps/kbiff/pics/mini-stopped.png
%{tde_datadir}/apps/kbiff/pics/newmail.png
%{tde_datadir}/apps/kbiff/pics/noconn.png
%{tde_datadir}/apps/kbiff/pics/nomail.png
%{tde_datadir}/apps/kbiff/pics/oldmail.png
%{tde_datadir}/apps/kbiff/pics/playsound.png
%{tde_datadir}/apps/kbiff/pics/stopped.png
%lang(de) %{tde_tdedocdir}/HTML/de/
%lang(en) %{tde_tdedocdir}/HTML/en/
%lang(es) %{tde_tdedocdir}/HTML/es/
%lang(fr) %{tde_tdedocdir}/HTML/fr/
%{tde_datadir}/icons/hicolor/*/apps/kbiff.png
%{tde_datadir}/icons/locolor/*/apps/kbiff.png
%{tde_mandir}/man1/kbiff.1*


%changelog
* Mon Apr 08 2013 Francois Andriot <francois.andriot@free.fr> - 3.9-1
- Initial release for TDE 3.5.13.2
