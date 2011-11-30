# Default version for this component
%define kdecomp knowit
%define version 0.10
%define release 1

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
Summary:	Tool for managing notes [Trinity]
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
KnowIt is a tool for managing notes which are organized in
tree-like hierarchy. It is similar to TuxCards,
but KDE-based, and requires Trinity.


%prep
%setup -q -n applications/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g" \
  -e "s,kde_htmldir='.*',kde_htmldir='%{tde_docdir}/HTML',g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
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

%__mkdir_p %{buildroot}%{_datadir}/applications/kde
%__mv %{buildroot}%{_datadir}/applnk/Applications/knowit.desktop %{buildroot}%{_datadir}/applications/kde/knowit.desktop
%__rm -r %{buildroot}%{_datadir}/applnk


%find_lang %{kdecomp}



%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%{_bindir}/knowit
%{_datadir}/applications/kde/knowit.desktop
%{_datadir}/apps/knowit/knowitui.rc
%{_datadir}/apps/knowit/tips
%{tde_docdir}/HTML/en/knowit/common
%{tde_docdir}/HTML/en/knowit/index.cache.bz2
%{tde_docdir}/HTML/en/knowit/index.docbook
%{tde_docdir}/HTML/en/knowit/screenshot.png
%{_datadir}/icons/hicolor/*/apps/knowit.png


%Changelog
* Wed Nov 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.10-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
