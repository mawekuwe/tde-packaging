# Default version for this component
%define kdecomp basket
%define version 1.0.3.1
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
Summary:	Taking care of your ideas.
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils

BuildRequires: gpgme-devel
BuildRequires: trinity-kdepim-devel

%description
This application is mainly an all-purpose notes taker. It provide several baskets where
to drop every sort of items: text, rich text, links, images, sounds, files, colors,
application launcher... Objects can be edited, copied, dragged... So, you can arrange
them as you want ! This application can be used to quickly drop web objects (link, text,
images...) or notes, as well as to free your clutered desktop (if any). It is also useful
to collect informations for a report. Those data can be shared with co-workers by exporting
baskets to HTML.


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
    --with-extra-includes=%{_includedir}/tqt \
    --disable-static

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
/sbin/ldconfig

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
/sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/*
%{_datadir}/applications/*/*.desktop
%{_datadir}/apps/*/
%{_datadir}/icons/*/*/*/*
%{_datadir}/locale/*/*/*.mo
%{tde_docdir}/HTML/en/*/
%{_datadir}/services/*.desktop
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/services/*/*.desktop
%{_datadir}/config/magic/*.magic
%{_libdir}/*.so
%{_libdir}/*.la
%{tde_libdir}/*.so
%{tde_libdir}/*.la



%Changelog
* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 1.0.3.1-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

