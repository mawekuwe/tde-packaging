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


Name:		trinity-kcmautostart
Summary:	Manage applications automatic startup.
Version:	1.0
Release:	1%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kcmautostart-3.5.13.tar.gz

# [kcmautostart] Fix FTBFS with TDE 3.5.13
Patch1:		kcmautostart-3.5.13-ftbfs.patch
# [kcmautostart] Add French support
Patch2:		kcmautostart-3.5.13-add_french.patch

BuildRequires: tqtinterface-devel
BuildRequires: trinity-arts-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++

Requires:		trinity-kdebase

%description
%{summary}

%prep
%setup -q -a 0 -n applications/kcmautostart
%patch1 -p1
%patch2 -p1

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
    --with-extra-includes=%{_includedir}/tqt \
    --disable-static

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{tde_libdir}/kcm_autostart.la
%{tde_libdir}/kcm_autostart.so
%{_datadir}/applications/kde/autostart.desktop
%{tde_docdir}/HTML/en/autostart/common
%{tde_docdir}/HTML/en/autostart/index.cache.bz2
%{tde_docdir}/HTML/en/autostart/index.docbook
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/autostart.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/autostart.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/autostart.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/autostart.mo
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/autostart.mo


%Changelog
* Thu May 10 2012 Francois Andriot <francois.andriot@free.fr> - 1.0-1
- Initial build for TDE 3.5.13
