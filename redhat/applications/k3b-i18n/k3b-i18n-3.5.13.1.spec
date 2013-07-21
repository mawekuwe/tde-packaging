# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE 3.5.13 specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/kde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}


Name:		trinity-k3b-i18n
Summary:	Locale files for K3B
Version:	1.0.5
Release:	2%{?dist}%{?_variant}

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

Source0: k3b-i18n-3.5.13.1.tar.gz

BuildRequires:	trinity-tdelibs-devel >= 3.5.13.1
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

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
%setup -q -n k3b-i18n-3.5.13.1


# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i "admin/acinclude.m4.in" \
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt3.sh
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"

./configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --datadir=%{tde_datadir} \
  --docdir=%{tde_tdedocdir} \
  --includedir=%{tde_tdeincludedir} \
  --libdir=%{tde_libdir} \
  --mandir=%{tde_mandir} \
  --disable-rpath \
  --with-extra-includes=%{tde_includedir}/tqt \
  --enable-closure

%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%__rm -rf %{buildroot}%{tde_datadir}/locale/af
%__rm -rf %{buildroot}%{tde_datadir}/locale/ar
%__rm -rf %{buildroot}%{tde_datadir}/locale/bg
%__rm -rf %{buildroot}%{tde_datadir}/locale/br
%__rm -rf %{buildroot}%{tde_datadir}/locale/bs
%__rm -rf %{buildroot}%{tde_datadir}/locale/ca
%__rm -rf %{buildroot}%{tde_datadir}/locale/cs
%__rm -rf %{buildroot}%{tde_datadir}/locale/cy
%__rm -rf %{buildroot}%{tde_datadir}/locale/en_GB
%__rm -rf %{buildroot}%{tde_datadir}/locale/eu
%__rm -rf %{buildroot}%{tde_datadir}/locale/fa
%__rm -rf %{buildroot}%{tde_datadir}/locale/fi
%__rm -rf %{buildroot}%{tde_datadir}/locale/ga
%__rm -rf %{buildroot}%{tde_datadir}/locale/gl
%__rm -rf %{buildroot}%{tde_datadir}/locale/he
%__rm -rf %{buildroot}%{tde_datadir}/locale/hi
%__rm -rf %{buildroot}%{tde_datadir}/locale/hu
%__rm -rf %{buildroot}%{tde_datadir}/locale/is
%__rm -rf %{buildroot}%{tde_datadir}/locale/ja
%__rm -rf %{buildroot}%{tde_datadir}/locale/ka
%__rm -rf %{buildroot}%{tde_datadir}/locale/km
%__rm -rf %{buildroot}%{tde_datadir}/locale/lt
%__rm -rf %{buildroot}%{tde_datadir}/locale/mk
%__rm -rf %{buildroot}%{tde_datadir}/locale/ms
%__rm -rf %{buildroot}%{tde_datadir}/locale/nb
%__rm -rf %{buildroot}%{tde_datadir}/locale/nds
%__rm -rf %{buildroot}%{tde_datadir}/locale/ne
%__rm -rf %{buildroot}%{tde_datadir}/locale/nn
%__rm -rf %{buildroot}%{tde_datadir}/locale/pa
%__rm -rf %{buildroot}%{tde_datadir}/locale/rw
%__rm -rf %{buildroot}%{tde_datadir}/locale/se
%__rm -rf %{buildroot}%{tde_datadir}/locale/sk
%__rm -rf %{buildroot}%{tde_datadir}/locale/sr
%__rm -rf %{buildroot}%{tde_datadir}/locale/sr@Latn
%__rm -rf %{buildroot}%{tde_datadir}/locale/ta
%__rm -rf %{buildroot}%{tde_datadir}/locale/tr
%__rm -rf %{buildroot}%{tde_datadir}/locale/uz
%__rm -rf %{buildroot}%{tde_datadir}/locale/uz@cyrillic
%__rm -rf %{buildroot}%{tde_datadir}/locale/zh_CN
%__rm -rf %{buildroot}%{tde_datadir}/locale/zh_TW


%clean
%__rm -rf %{buildroot}


%files da
%defattr(-,root,root,-)
%lang(da) %{tde_tdedocdir}/HTML/da/k3b
%lang(da) %{tde_datadir}/locale/da/LC_MESSAGES/*.mo

%files de
%defattr(-,root,root,-)
%lang(de) %{tde_tdedocdir}/HTML/de/k3b
%lang(de) %{tde_datadir}/locale/de/LC_MESSAGES/*.mo

%files el
%defattr(-,root,root,-)
#%lang(el) %{tde_tdedocdir}/HTML/el/k3b
%lang(el) %{tde_datadir}/locale/el/LC_MESSAGES/*.mo

%files es
%defattr(-,root,root,-)
%lang(es) %{tde_tdedocdir}/HTML/es/k3b
%lang(es) %{tde_datadir}/locale/es/LC_MESSAGES/*.mo

%files et
%defattr(-,root,root,-)
%lang(et) %{tde_tdedocdir}/HTML/et/k3b
%lang(et) %{tde_datadir}/locale/et/LC_MESSAGES/*.mo

%files fr
%defattr(-,root,root,-)
%lang(fr) %{tde_tdedocdir}/HTML/fr/k3b
%lang(fr) %{tde_datadir}/locale/fr/LC_MESSAGES/*.mo

%files it
%defattr(-,root,root,-)
%lang(it) %{tde_tdedocdir}/HTML/it/k3b
%lang(it) %{tde_datadir}/locale/it/LC_MESSAGES/*.mo

%files nl
%defattr(-,root,root,-)
%lang(nl) %{tde_tdedocdir}/HTML/nl/k3b
%lang(nl) %{tde_datadir}/locale/nl/LC_MESSAGES/*.mo

%files pl
%defattr(-,root,root,-)
%lang(pl) %{tde_tdedocdir}/HTML/pl/k3b
%lang(pl) %{tde_datadir}/locale/pl/LC_MESSAGES/*.mo

%files pt
%defattr(-,root,root,-)
%lang(pt) %{tde_tdedocdir}/HTML/pt/k3b
%lang(pt) %{tde_datadir}/locale/pt/LC_MESSAGES/*.mo

%files ptbr
%defattr(-,root,root,-)
%lang(pt_BR) %{tde_tdedocdir}/HTML/pt_BR/k3b
%lang(pt_BR) %{tde_datadir}/locale/pt_BR/LC_MESSAGES/*.mo

%files ru
%defattr(-,root,root,-)
%lang(ru) %{tde_tdedocdir}/HTML/ru/k3b
%lang(ru) %{tde_datadir}/locale/ru/LC_MESSAGES/*.mo

%files sv
%defattr(-,root,root,-)
%lang(sv) %{tde_tdedocdir}/HTML/sv/k3b
%lang(sv) %{tde_datadir}/locale/sv/LC_MESSAGES/*.mo

%files uk
%defattr(-,root,root,-)
%lang(uk) %{tde_tdedocdir}/HTML/uk/k3b
%lang(uk) %{tde_datadir}/locale/uk/LC_MESSAGES/*.mo



%changelog
* Wed Oct 03 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.5-2
- Initial release for TDE 3.5.13.1

* Thu May 10 2012 Francois Andriot <francois.andriot@free.fr> - 1.0.5-1
- Initial release for TDE 3.5.13
