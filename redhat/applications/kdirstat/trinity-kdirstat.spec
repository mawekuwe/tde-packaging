# Default version for this component
%define kdecomp kdirstat
%define version 2.4.4
%define release 2

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	graphical disk usage display with cleanup facilities [Trinity]
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

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext


%description
KDirStat (KDE Directory Statistics) is a small utility program that sums
up disk usage for directory trees, very much like the Unix 'du' command.
It displays the disk space used up by a directory tree, both numerically
and graphically.  It is network transparent (i.e., you can use it to sum
up FTP servers), and comes with predefined and user configurable cleanup
actions.  You can directly open a directory branch in Konqueror or the
shell of your choice, compress it to a .tar.bz2 archive, or define your
own cleanup actions. 


%prep
%setup -q -n applications/%{kdecomp}

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
    --with-extra-includes=%{_includedir}/tqt:%{tde_includedir}

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%find_lang %{kdecomp} || touch %{kdecomp}.lang



%clean
%__rm -rf %{buildroot}


%post
for f in hicolor locolor; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done

%postun
for f in hicolor locolor; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%{_bindir}/kdirstat
%{_datadir}/applnk/Utilities/kdirstat.desktop
%{_datadir}/apps/kconf_update/fix_move_to_trash_bin.pl
%{_datadir}/apps/kconf_update/kdirstat.upd
%{_datadir}/apps/kdirstat
%{tde_docdir}/HTML/en/kdirstat
%{_datadir}/icons/hicolor/*/apps/kdirstat.png
%{_datadir}/icons/locolor/*/apps/kdirstat.png


%Changelog
* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 2.4.4-2
- Rebuilt for Fedora 17
- Fix post and postun

* Wed Nov 30 2011 Francois Andriot <francois.andriot@free.fr> - 2.4.4-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
