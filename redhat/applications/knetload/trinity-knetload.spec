# Default version for this component
%define kdecomp knetload
%define version 2.3
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
Summary:	a network meter for Kicker [Trinity]
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
KNetLoad is a small network meter for Kicker (the KDE panel).  It shows
a recent history of network usage in the form of two configurable
diagrams in the system tray, one for incoming and one for outgoing
data.  These diagrams have settings for colours and various different
styles.

KNetLoad can monitor just about any network device.


%prep
%setup -q -n applications/%{kdecomp}

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
    --with-extra-includes=%{_includedir}/tqt

# SMP safe !
%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%find_lang %{kdecomp}



%clean
%__rm -rf %{buildroot}


%post
for f in crystalsvg locolor ; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done

%postun
for f in crystalsvg locolor ; do
  touch --no-create %{_datadir}/icons/${f} || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/${f} || :
done


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%{_bindir}/knetload
%{_datadir}/applications/kde/knetload.desktop
%{_datadir}/apps/knetload
%{_datadir}/icons/crystalsvg/*/apps/knetload.png
%{_datadir}/icons/locolor/*/apps/knetload.png


%Changelog
* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 2.3-2
- Rebuild for Fedora 17

* Wed Nov 30 2011 Francois Andriot <francois.andriot@free.fr> - 2.3-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
