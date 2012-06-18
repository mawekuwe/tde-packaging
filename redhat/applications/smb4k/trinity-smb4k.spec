# Default version for this component
%define kdecomp smb4k
%define version 0.9.4
%define release 2

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
Summary:	A Samba (SMB) share advanced browser for Trinity
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

# [smb4k] Fix compilation with GCC 4.7 |Commit #b4c7fd48]
Patch1:		smb4k-3.5.13-fix_gcc47_compilation.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-arts-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext


%description
Smb4K is a SMB (Windows) share browser for KDE. It uses the Samba software 
suite to access the SMB shares of the local network neighborhood. Its purpose
is to provide a program that's easy to use and has as many features as 
possible.


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

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}




%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{_datadir}/icons/crystalsvg || :
/sbin/ldconfig || :

%postun
touch --no-create %{_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{_datadir}/icons/crystalsvg || :
/sbin/ldconfig || :


%files
%defattr(-,root,root,-)
%{_bindir}/smb4k
%{_bindir}/smb4k_cat
%{_bindir}/smb4k_kill
%{_bindir}/smb4k_mount
%{_bindir}/smb4k_mv
%{_bindir}/smb4k_umount
%{_includedir}/*.h
%{_libdir}/libsmb4kcore.la
%{_libdir}/libsmb4kcore.so
%{_libdir}/libsmb4kcore.so.2
%{_libdir}/libsmb4kcore.so.2.0.0
%{_libdir}/libsmb4kdialogs.la
%{_libdir}/libsmb4kdialogs.so
%{tde_libdir}/konqsidebar_smb4k.la
%{tde_libdir}/konqsidebar_smb4k.so
%{tde_libdir}/libsmb4kconfigdialog.la
%{tde_libdir}/libsmb4kconfigdialog.so
%{tde_libdir}/libsmb4knetworkbrowser.la
%{tde_libdir}/libsmb4knetworkbrowser.so
%{tde_libdir}/libsmb4ksearchdialog.la
%{tde_libdir}/libsmb4ksearchdialog.so
%{tde_libdir}/libsmb4ksharesiconview.la
%{tde_libdir}/libsmb4ksharesiconview.so
%{tde_libdir}/libsmb4kshareslistview.la
%{tde_libdir}/libsmb4kshareslistview.so
%{_datadir}/applications/kde/smb4k.desktop
%{_datadir}/apps/konqsidebartng/add/smb4k_add.desktop
%{_datadir}/apps/smb4k/smb4k_shell.rc
%{_datadir}/apps/smb4knetworkbrowserpart/smb4knetworkbrowser_part.rc
%{_datadir}/apps/smb4ksharesiconviewpart/smb4ksharesiconview_part.rc
%{_datadir}/apps/smb4kshareslistviewpart/smb4kshareslistview_part.rc
%{_datadir}/config.kcfg/smb4k.kcfg
%{tde_docdir}/HTML/en/smb4k
%{_datadir}/icons/crystalsvg/*/apps/smb4k.png
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/smb4k.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/smb4k.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/smb4k.mo
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/smb4k.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/smb4k.mo
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/smb4k.mo


%Changelog
* Sun Apr 06 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.4-2
- Rebuild for Fedora 17
- Fix compilation with GCC 4.7 |Commit #b4c7fd48]

* Wed Nov 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.4-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
