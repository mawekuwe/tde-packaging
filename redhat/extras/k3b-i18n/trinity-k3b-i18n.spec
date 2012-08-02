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


Name:    trinity-k3b-i18n
Summary: Locale files for K3B
Version: 1.0.5
Release: 1%{?dist}%{?_variant}

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

BuildArch:	noarch

# Speed build options
%define debug_package %{nil}
%define __spec_install_post %{nil}
AutoReq: no

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Group:   Applications/Archiving
License: GPLv2+

Source0: k3b-i18n-1.0.5.tar.bz2

# [kde-i18n] Fix automake detection
Patch1:		k3b-i18n-trinity.patch

BuildRequires: trinity-kdelibs-devel
BuildRequires: desktop-file-utils
BuildRequires: gettext

Requires(post): coreutils
Requires(postun): coreutils

Requires:	trinity-k3b


%description
K3b provides a comfortable user interface to perform most CD/DVD
burning tasks. While the experienced user can take influence in all
steps of the burning process the beginner may find comfort in the
automatic settings and the reasonable k3b defaults which allow a quick
start.

%package da
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: Danish (da) translations for K3B [Trinity]
%description da
This package contains the Danish translations for K3B.

%package de
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: German (de) translations for K3B [Trinity]
%description de
This package contains the German translations for K3B.

%package el
Group:   Applications/Archiving
Requires: trinity-k3b >= %{version}
Summary: Greek (el) translations for K3B [Trinity]
%description el
This package contains the greek translations for K3B.

%package es
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: Spanish (es) translations for K3B [Trinity]
%description es
This package contains the Spanish translations for K3B.

%package et
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: Estonian (et) translations for K3B [Trinity]
%description et
This package contains the Estonian translations for K3B.

%package fr
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: French (fr) translations for K3B [Trinity]
%description fr
This package contains the French translations for K3B.

%package it
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: Italian (it) translations for K3B [Trinity]
%description it
This package contains the Italian translations for K3B.

%package nl
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: Dutch (nl) translations for K3B [Trinity]
%description nl
This package contains the Dutch translations for K3B.

%package pl
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: Polish (pl) translations for K3B [Trinity]
%description pl
This package contains the Polish translations for K3B.

%package pt
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: Portuguese (pt) translations for K3B [Trinity]
%description pt
This package contains the Portuguese translations for K3B.

%package ptbr
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: Brazilian Portuguese (pt_BR) translations for K3B [Trinity]
%description ptbr
This package contains the Brazilian Portuguese translations for K3B.

%package ru
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: Russian (ru) translations for K3B [Trinity]
%description ru
This package contains the Russian translations for K3B.

%package sv
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: Swedish (sv) translations for K3B [Trinity]
%description sv
This package contains the Swedish translations for K3B.

%package uk
Group:   Applications/Archiving
Requires: trinity-k3b
Summary: Ukrainian (uk) translations for K3B [Trinity]
%description uk
This package contains the Ukrainian translations for K3B.


%prep
%setup -q -n k3b-i18n-%{version}

# set in k3brc too 
%patch1 -p1 -b .automake


# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i "admin/acinclude.m4.in" \
  -e "s|/opt/kde3|%{_prefix}|g" \
  -e "s|kde3/plugins|trinity/plugins|g" \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
  --target=%{_host}
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%clean
%__rm -rf %{buildroot}


%files da
%defattr(-,root,root,-)
%lang(da) %{tde_docdir}/HTML/da/k3b
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/*.mo

%files de
%defattr(-,root,root,-)
%lang(de) %{tde_docdir}/HTML/de/k3b
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*.mo

%files el
%defattr(-,root,root,-)
#%lang(el) %{tde_docdir}/HTML/el/k3b
%lang(el) %{_datadir}/locale/el/LC_MESSAGES/*.mo

%files es
%defattr(-,root,root,-)
%lang(es) %{tde_docdir}/HTML/es/k3b
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*.mo

%files et
%defattr(-,root,root,-)
%lang(et) %{tde_docdir}/HTML/et/k3b
%lang(et) %{_datadir}/locale/et/LC_MESSAGES/*.mo

%files fr
%defattr(-,root,root,-)
%lang(fr) %{tde_docdir}/HTML/fr/k3b
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*.mo

%files it
%defattr(-,root,root,-)
%lang(it) %{tde_docdir}/HTML/it/k3b
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/*.mo

%files nl
%defattr(-,root,root,-)
%lang(nl) %{tde_docdir}/HTML/nl/k3b
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/*.mo

%files pl
%defattr(-,root,root,-)
%lang(pl) %{tde_docdir}/HTML/pl/k3b
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/*.mo

%files pt
%defattr(-,root,root,-)
%lang(pt) %{tde_docdir}/HTML/pt/k3b
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/*.mo

%files ptbr
%defattr(-,root,root,-)
%lang(pt_BR) %{tde_docdir}/HTML/pt_BR/k3b
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/*.mo

%files ru
%defattr(-,root,root,-)
%lang(ru) %{tde_docdir}/HTML/ru/k3b
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/*.mo

%files sv
%defattr(-,root,root,-)
%lang(sv) %{tde_docdir}/HTML/sv/k3b
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/*.mo

%files uk
%defattr(-,root,root,-)
%lang(uk) %{tde_docdir}/HTML/uk/k3b
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/*.mo

%exclude %{_datadir}/locale/af
%exclude %{_datadir}/locale/ar
%exclude %{_datadir}/locale/bg
%exclude %{_datadir}/locale/br
%exclude %{_datadir}/locale/bs
%exclude %{_datadir}/locale/ca
%exclude %{_datadir}/locale/cs
%exclude %{_datadir}/locale/cy
%exclude %{_datadir}/locale/en_GB
%exclude %{_datadir}/locale/eu
%exclude %{_datadir}/locale/fa
%exclude %{_datadir}/locale/fi
%exclude %{_datadir}/locale/ga
%exclude %{_datadir}/locale/gl
%exclude %{_datadir}/locale/he
%exclude %{_datadir}/locale/hi
%exclude %{_datadir}/locale/hu
%exclude %{_datadir}/locale/is
%exclude %{_datadir}/locale/ja
%exclude %{_datadir}/locale/ka
%exclude %{_datadir}/locale/km
%exclude %{_datadir}/locale/lt
%exclude %{_datadir}/locale/mk
%exclude %{_datadir}/locale/ms
%exclude %{_datadir}/locale/nb
%exclude %{_datadir}/locale/nds
%exclude %{_datadir}/locale/ne
%exclude %{_datadir}/locale/nn
%exclude %{_datadir}/locale/pa
%exclude %{_datadir}/locale/rw
%exclude %{_datadir}/locale/se
%exclude %{_datadir}/locale/sk
%exclude %{_datadir}/locale/sr
%exclude %{_datadir}/locale/sr@Latn
%exclude %{_datadir}/locale/ta
%exclude %{_datadir}/locale/tr
%exclude %{_datadir}/locale/uz
%exclude %{_datadir}/locale/uz@cyrillic
%exclude %{_datadir}/locale/zh_CN
%exclude %{_datadir}/locale/zh_TW


%changelog
* Thu May 10 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.5-1
- Initial build for TDE 3.5.13
