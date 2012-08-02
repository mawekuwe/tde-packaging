# Default version for this component
%define kdecomp kde-systemsettings

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc

# Currently, menu files under /etc/xdg conflict with KDE4
%define _sysconfdir %{_prefix}/etc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-systemsettings
Summary:	easy to use control centre for TDE
Version:	0.0svn20070312
Release:	4%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Source1:	kde-settings-laptops.directory

Provides:	trinity-kde-systemsettings = %{version}-%{release}
Obsoletes:	trinity-kde-systemsettings < %{version}-%{release}

BuildRequires: tqtinterface-devel
BuildRequires: trinity-tdelibs-devel
BuildRequires: trinity-tdebase-devel
BuildRequires: desktop-file-utils

Requires:	trinity-guidance

%description
System preferences is a replacement for the TDE
Control Centre with an improved user interface.


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
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt \
    --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%__install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/desktop-directories/

%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{_datadir}/icons/crystalsvg || :

%postun
touch --no-create %{_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{_datadir}/icons/crystalsvg || :


%files
%defattr(-,root,root,-)
%doc README TODO
%{_sysconfdir}/xdg/menus/applications-merged/system-settings-merge.menu
%{_sysconfdir}/xdg/menus/system-settings.menu
%{_bindir}/systemsettings
%{_datadir}/applications/kde/audioencoding.desktop
%{_datadir}/applications/kde/defaultapplication.desktop
%{_datadir}/applications/kde/kcm_knetworkconfmodule_ss.desktop
%{_datadir}/applications/kde/laptoppowermanagement.desktop
%{_datadir}/applications/kde/medianotifications.desktop
%{_datadir}/applications/kde/systemsettings.desktop
%{_datadir}/apps/systemsettings/systemsettingsui.rc
%{_datadir}/config/systemsettingsrc
%{_datadir}/desktop-directories/*.directory
%{_datadir}/icons/crystalsvg/*/apps/systemsettings.png

%exclude %{_datadir}/applications/kde/kcmfontinst.desktop
%exclude %{_datadir}/desktop-directories/kde-settings-power.directory
%exclude %{_datadir}/desktop-directories/kde-settings-system.directory


%Changelog
* Wed Jul 11 2012 Francois Andriot <francois.andriot@free.fr> - 0.0svn20070312-4
- Fix XDG menu directory location (again)

* Sun Jul 08 2012 Francois Andriot <francois.andriot@free.fr> - 0.0svn20070312-3
- Updates 'Requires: trinity-guidance' to reflect package renaming

* Wed Dec 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.0svn20070312-2
- Fix XDG menu directory location

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.0svn20070312-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

