# Default version for this component
%define kdecomp kpilot
%define version 0.7
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
Summary:	TDE Palm Pilot hot-sync tool
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

# Fix FTBFS
Patch0:		kpilot-3.5.13-ftbfs.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	pilot-link-devel
BuildRequires:	trinity-kdepim-devel

%description
KPilot is an application that synchronizes your Palm Pilot or similar device
(like the Handspring Visor) with your KDE desktop, much like the Palm HotSync
software does for Windows.  KPilot can back-up and restore your Palm Pilot
and synchronize the built-in applications with their KDE counterparts.


%prep
%setup -q -n applications/%{kdecomp}
%patch0 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
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
for f in hicolor locolor crystalsvg; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done
/sbin/ldconfig || :

%postun
for f in hicolor locolor crystalsvg; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done
/sbin/ldconfig || :


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%{_bindir}/kpalmdoc
%{_bindir}/kpilot
%{_bindir}/kpilotDaemon
%{_includedir}/kpilot
%{_libdir}/libkpilot.la
%{_libdir}/libkpilot.so
%{_libdir}/libkpilot.so.0
%{_libdir}/libkpilot.so.0.0.0
%{tde_libdir}/conduit_address.la
%{tde_libdir}/conduit_address.so
%{tde_libdir}/conduit_doc.la
%{tde_libdir}/conduit_doc.so
%{tde_libdir}/conduit_knotes.la
%{tde_libdir}/conduit_knotes.so
%{tde_libdir}/conduit_memofile.la
%{tde_libdir}/conduit_memofile.so
%{tde_libdir}/conduit_notepad.la
%{tde_libdir}/conduit_notepad.so
%{tde_libdir}/conduit_popmail.la
%{tde_libdir}/conduit_popmail.so
%{tde_libdir}/conduit_sysinfo.la
%{tde_libdir}/conduit_sysinfo.so
%{tde_libdir}/conduit_time.la
%{tde_libdir}/conduit_time.so
%{tde_libdir}/conduit_todo.la
%{tde_libdir}/conduit_todo.so
%{tde_libdir}/conduit_vcal.la
%{tde_libdir}/conduit_vcal.so
%{tde_libdir}/kcm_kpilot.la
%{tde_libdir}/kcm_kpilot.so
%{_datadir}/applications/kde/kpalmdoc.desktop
%{_datadir}/applications/kde/kpilot.desktop
%{_datadir}/applications/kde/kpilotdaemon.desktop
%{_datadir}/apps/kaddressbook/contacteditorpages/KPilotCustomFieldEditor.ui
%{_datadir}/apps/kconf_update/kpalmdoc.upd
%{_datadir}/apps/kconf_update/kpilot.upd
%{_datadir}/apps/kpilot
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/icons/crystalsvg/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/locolor/*/apps/*.png
%{_datadir}/services/*.desktop
%{_datadir}/servicetypes/kpilotconduit.desktop


%Changelog
* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 0.7-2
- Rebuild for Fedora 17

* Wed Nov 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.7-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
