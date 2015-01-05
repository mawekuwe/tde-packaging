#
# spec file for package tde-i18n (version R14.0.0)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http:/www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%define tde_version 14.0.0
%define tde_pkg tde-i18n
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}

# Builds all supported languages (not unsupported ones)
%if "%{?TDE_LANGS}" == ""
%define TDE_LANGS ar bg bn ca cs da de el en_GB es et fi fr he hi hu is it ja lt nl nb nn pa pl pt pt_BR ro ru sk sl sr sv ta tr uk zh_CN zh_TW
%endif


Name:			trinity-%{tde_pkg}
Version:		%{tde_version}
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Vendor:			Trinity Project
Summary:		Internationalization support for Trinity
Group:			User Interface/Desktops

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

BuildArch:		noarch

# Speed build options
%define debug_package %{nil}
%define __spec_install_post %{nil}
AutoReq: no

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	findutils
BuildRequires:	gettext
BuildRequires:	cmake

%description
%{summary}.

%package Afrikaans
Summary:		Afrikaans(af) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-af = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Afrikaans < %{version}-%{release}
Provides:	 trinity-kde-i18n-Afrikaans = %{version}-%{release}
%description Afrikaans
%{summary}.

%package Arabic 
Summary:		Arabic(ar) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-ar = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Arabic < %{version}-%{release}
Provides:	 trinity-kde-i18n-Arabic = %{version}-%{release}
%description Arabic
%{summary}.

%package Azerbaijani
Summary:		Azerbaijani(az) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-az = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Arabic < %{version}-%{release}
Provides:	 trinity-kde-i18n-Arabic = %{version}-%{release}
%description Azerbaijani
%{summary}.

%package Belarusian
Summary:		Belarusian(be) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-be = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Belarusian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Belarusian = %{version}-%{release}
%description Belarusian
%{summary}.

%package Bulgarian
Summary:		Bulgarian(bg) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-bg = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Bulgarian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Bulgarian = %{version}-%{release}
%description Bulgarian
%{summary}.

%package Bengali
Summary:		Bengali(bn) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-bn = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Bengali < %{version}-%{release}
Provides:	 trinity-kde-i18n-Bengali = %{version}-%{release}
%description Bengali
%{summary}.

%package Tibetan
Summary:		Tibetan(bo) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-bo = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Tibetan < %{version}-%{release}
Provides:	 trinity-kde-i18n-Tibetan = %{version}-%{release}
%description Tibetan
%{summary}.

%package Breton
Summary:		Breton(br) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-br = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Breton < %{version}-%{release}
Provides:	 trinity-kde-i18n-Breton = %{version}-%{release}
%description Breton
%{summary}.

%package Bosnian
Summary:		Bosnian(bs) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-bs = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Bosnian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Bosnian = %{version}-%{release}
%description Bosnian
%{summary}.

%package Catalan
Summary:		Catalan(ca) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-ca = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Catalan < %{version}-%{release}
Provides:	 trinity-kde-i18n-Catalan = %{version}-%{release}
%description Catalan
%{summary}.

%package Czech
Summary:		Czech(cs) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-cs = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Czech < %{version}-%{release}
Provides:	 trinity-kde-i18n-Czech = %{version}-%{release}
%description Czech
%{summary}.

%package Cymraeg
Summary:		Cymraeg language support for TDE
Group:			User Interface/Desktops
Obsoletes:	 trinity-kde-i18n-Cymraeg < %{version}-%{release}
Provides:	 trinity-kde-i18n-Cymraeg = %{version}-%{release}
%description Cymraeg
%{summary}.

%package Welsh
Summary:		Welsh(cy) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-cy = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Welsh < %{version}-%{release}
Provides:	 trinity-kde-i18n-Welsh = %{version}-%{release}
%description Welsh
%{summary}.

%package Danish
Summary:		Danish(da) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-da = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Danish < %{version}-%{release}
Provides:	 trinity-kde-i18n-Danish = %{version}-%{release}
%description Danish
%{summary}.

%package German
Summary:		German(de) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-de = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-German < %{version}-%{release}
Provides:	 trinity-kde-i18n-German = %{version}-%{release}
%description German
%{summary}.

%package Greek
Summary:		Greek(el) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-el = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Greek < %{version}-%{release}
Provides:	 trinity-kde-i18n-Greek = %{version}-%{release}
%description Greek
%{summary}.

%package British
Summary:		British(en_GB) English support for TDE
Group:			User Interface/Desktops
Provides: %{name}-en_GB = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-British < %{version}-%{release}
Provides:	 trinity-kde-i18n-British = %{version}-%{release}
%description British
%{summary}.

%package Esperanto
Summary:		Esperanto(eo) support for TDE
Group:			User Interface/Desktops
Provides: %{name}-eo = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Esperanto < %{version}-%{release}
Provides:	 trinity-kde-i18n-Esperanto = %{version}-%{release}
%description Esperanto
%{summary}.

%package Spanish
Summary:		Spanish(es) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-es = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Spanish < %{version}-%{release}
Provides:	 trinity-kde-i18n-Spanish = %{version}-%{release}
%description Spanish
%{summary}.

%package Estonian
Summary:		Estonian(et) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-et = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Estonian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Estonian = %{version}-%{release}
%description Estonian
%{summary}.

%package Basque
Summary:		Basque(eu) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-eu = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Basque < %{version}-%{release}
Provides:	 trinity-kde-i18n-Basque = %{version}-%{release}
%description Basque
%{summary}.

%package Farsi
Summary:		Farsi(fa) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-fa = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Farsi < %{version}-%{release}
Provides:	 trinity-kde-i18n-Farsi = %{version}-%{release}
%description Farsi
%{summary}.

%package Finnish
Summary:		Finnish(fi) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-fi = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Finnish < %{version}-%{release}
Provides:	 trinity-kde-i18n-Finnish = %{version}-%{release}
%description Finnish
%{summary}.

%package Faroese
Summary:		Faroese(fo) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-fo = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Faroese < %{version}-%{release}
Provides:	 trinity-kde-i18n-Faroese = %{version}-%{release}
%description Faroese
%{summary}.

%package French
Summary:		French(fr) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-fr = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-French < %{version}-%{release}
Provides:	 trinity-kde-i18n-French = %{version}-%{release}
%description French
%{summary}.

%package Frisian
Summary:		Frisian(fy) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-fy = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Frisian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Frisian = %{version}-%{release}
%description Frisian
%{summary}.

%package Irish
Summary:		Irish(ga) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-ga = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Irish < %{version}-%{release}
Provides:	 trinity-kde-i18n-Irish = %{version}-%{release}
%description Irish
%{summary}.

%package Galician
Summary:		Galician(gl) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-gl = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Galician < %{version}-%{release}
Provides:	 trinity-kde-i18n-Galician = %{version}-%{release}
%description Galician
%{summary}.

%package Hebrew
Summary:		Hebrew(he) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-he = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Hebrew < %{version}-%{release}
Provides:	 trinity-kde-i18n-Hebrew = %{version}-%{release}
%description Hebrew
%{summary}.

%package Hindi
Summary:		Hindi(hi) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-hi = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Hindi < %{version}-%{release}
Provides:	 trinity-kde-i18n-Hindi = %{version}-%{release}
%description Hindi
%{summary}.

%package Croatian
Summary:		Croatian(hr) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-hr = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Croatian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Croatian = %{version}-%{release}
%description Croatian
%{summary}.

%package Hungarian
Summary:		Hungarian(hu) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-hu = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Hungarian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Hungarian = %{version}-%{release}
%description Hungarian
%{summary}.

%package Indonesian
Summary:		Indonesian(id) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-id = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Indonesian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Indonesian = %{version}-%{release}
%description Indonesian
%{summary}.

%package Icelandic
Summary:		Icelandic(is) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-is = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Icelandic < %{version}-%{release}
Provides:	 trinity-kde-i18n-Icelandic = %{version}-%{release}
%description Icelandic
%{summary}.

%package Italian
Summary:		Italian(it) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-it = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Italian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Italian = %{version}-%{release}
%description Italian
%{summary}.

%package Japanese
Summary:		Japanese(ja) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-ja = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Japanese < %{version}-%{release}
Provides:	 trinity-kde-i18n-Japanese = %{version}-%{release}
%description Japanese
%{summary}.

%package Korean
Summary:		Korean(ko) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-ko = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Korean < %{version}-%{release}
Provides:	 trinity-kde-i18n-Korean = %{version}-%{release}
%description Korean
%{summary}.

%package Kurdish
Summary:		Kurdish(ku) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-ku = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Kurdish < %{version}-%{release}
Provides:	 trinity-kde-i18n-Kurdish = %{version}-%{release}
%description Kurdish
%{summary}.

%package Lao
Summary:		Lao(lo) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-lo = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Lao < %{version}-%{release}
Provides:	 trinity-kde-i18n-Lao = %{version}-%{release}
%description Lao
%{summary}.

%package Lithuanian
Summary:		Lithuanian(lt) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-lt = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Lithuanian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Lithuanian = %{version}-%{release}
%description Lithuanian
%{summary}.

%package Latvian
Summary:		Latvian(lv) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-lv = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Latvian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Latvian = %{version}-%{release}
%description Latvian
%{summary}.

%package Maori
Summary:		Maori(mi) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-mi = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Maori < %{version}-%{release}
Provides:	 trinity-kde-i18n-Maori = %{version}-%{release}
%description Maori
%{summary}.

%package Macedonian
Summary:		Macedonian(mk) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-mk = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Macedonian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Macedonian = %{version}-%{release}
%description Macedonian
%{summary}.

%package Maltese
Summary:		Maltese(mt) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-mt = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Maltese < %{version}-%{release}
Provides:	 trinity-kde-i18n-Maltese = %{version}-%{release}
%description Maltese
%{summary}.

%package Dutch
Summary:		Dutch(nl) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-nl = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Dutch < %{version}-%{release}
Provides:	 trinity-kde-i18n-Dutch = %{version}-%{release}
%description Dutch
%{summary}.

%package Norwegian
Summary:		Norwegian(no) (Bokmaal) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-no = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Norwegian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Norwegian = %{version}-%{release}
%description Norwegian
%{summary}.

%package Norwegian-Nynorsk
Summary:		Norwegian(nn) (Nynorsk) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-nn = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Norwegian-Nynorsk < %{version}-%{release}
Provides:	 trinity-kde-i18n-Norwegian-Nynorsk = %{version}-%{release}
%description Norwegian-Nynorsk
%{summary}.

%package Occitan
Summary:		Occitan(oc) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-oc = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Occitan < %{version}-%{release}
Provides:	 trinity-kde-i18n-Occitan = %{version}-%{release}
%description Occitan
%{summary}.

%package Polish
Summary:		Polish(pl) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-pl = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Polish < %{version}-%{release}
Provides:	 trinity-kde-i18n-Polish = %{version}-%{release}
%description Polish
%{summary}.

%package Portuguese
Summary:		Portuguese(pt) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-pt = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Portuguese < %{version}-%{release}
Provides:	 trinity-kde-i18n-Portuguese = %{version}-%{release}
%description Portuguese
%{summary}.

%package Punjabi
Summary:		Punjabi(pa) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-pa = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Punjabi < %{version}-%{release}
Provides:	 trinity-kde-i18n-Punjabi = %{version}-%{release}
%description Punjabi
%{summary}.

%package Brazil
Summary:		Brazil(pt_BR) Portuguese language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-pt_BR = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Brazil < %{version}-%{release}
Provides:	 trinity-kde-i18n-Brazil = %{version}-%{release}
%description Brazil
%{summary}.

%package Romanian
Summary:		Romanian(ro) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-ro = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Romanian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Romanian = %{version}-%{release}
%description Romanian
%{summary}.

%package Russian
Summary:		Russian(ru) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-ru = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Russian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Russian = %{version}-%{release}
%description Russian
%{summary}.

%package Slovak
Summary:		Slovak(sk) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-sk = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Slovak < %{version}-%{release}
Provides:	 trinity-kde-i18n-Slovak = %{version}-%{release}
%description Slovak
%{summary}.

%package Slovenian
Summary:		Slovenian(sl) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-sl = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Slovenian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Slovenian = %{version}-%{release}
%description Slovenian
%{summary}.

%package Serbian
Summary:		Serbian(sr) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-sr = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Serbian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Serbian = %{version}-%{release}
%description Serbian
%{summary}.

%package Swedish
Summary:		Swedish(sv) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-sv = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Swedish < %{version}-%{release}
Provides:	 trinity-kde-i18n-Swedish = %{version}-%{release}
%description Swedish
%{summary}.

%package Tamil
Summary:		Tamil(ta) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-ta = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Tamil < %{version}-%{release}
Provides:	 trinity-kde-i18n-Tamil = %{version}-%{release}
%description Tamil
%{summary}.

%package Tajik
Summary:		Tajik(tg) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-tg = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Tajik < %{version}-%{release}
Provides:	 trinity-kde-i18n-Tajik = %{version}-%{release}
%description Tajik
%{summary}.

%package Thai
Summary:		Thai(th) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-th = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Thai < %{version}-%{release}
Provides:	 trinity-kde-i18n-Thai = %{version}-%{release}
%description Thai
%{summary}.

%package Turkish
Summary:		Turkish(tr) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-tr = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Turkish < %{version}-%{release}
Provides:	 trinity-kde-i18n-Turkish = %{version}-%{release}
%description Turkish
%{summary}.

%package Ukrainian
Summary:		Ukrainian(uk) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-uk = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Ukrainian < %{version}-%{release}
Provides:	 trinity-kde-i18n-Ukrainian = %{version}-%{release}
%description Ukrainian
%{summary}.

%package Venda
Summary:		Venda(ven) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-ven = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Venda < %{version}-%{release}
Provides:	 trinity-kde-i18n-Venda = %{version}-%{release}
%description Venda
%{summary}.

%package Vietnamese
Summary:		Vietnamese(vi) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-vi = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Vietnamese < %{version}-%{release}
Provides:	 trinity-kde-i18n-Vietnamese = %{version}-%{release}
%description Vietnamese
%{summary}.

%package Walloon
Summary:		Walloon(wa) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-wa = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Walloon < %{version}-%{release}
Provides:	 trinity-kde-i18n-Walloon = %{version}-%{release}
%description Walloon
%{summary}.

%package Xhosa
Summary:		Xhosa(xh) (a Bantu language) support for TDE
Group:			User Interface/Desktops
Provides: %{name}-xh = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Xhosa < %{version}-%{release}
Provides:	 trinity-kde-i18n-Xhosa = %{version}-%{release}
%description Xhosa
%{summary}.

%package Chinese
Summary:		Chinese(zh_CN) (Simplified Chinese) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-zh_CN = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Chinese < %{version}-%{release}
Provides:	 trinity-kde-i18n-Chinese = %{version}-%{release}
%description Chinese
%{summary}.

%package Chinese-Big5
Summary:		Chinese(zh_TW) (Big5) language support for TDE
Group:			User Interface/Desktops
Provides: %{name}-tz_TW = %{version}-%{release}
Obsoletes:	 trinity-kde-i18n-Chinese-Big5 < %{version}-%{release}
Provides:	 trinity-kde-i18n-Chinese-Big5 = %{version}-%{release}
%description Chinese-Big5
%{summary}.



%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"

(
for l in %{TDE_LANGS}; do
  for f in tde-i18n-${l}/; do
    if [ -d "${f}" ]; then 
      pushd ${f}
      if ! rpm -E %%cmake|grep -q "cd build"; then
        %__mkdir_p build
        cd build
      fi
      
      %cmake \
        -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
        -DCMAKE_VERBOSE_MAKEFILE=ON \
        \
        -DCMAKE_INSTALL_PREFIX="%{tde_prefix}" \
        -DBIN_INSTALL_DIR="%{tde_bindir}" \
        -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}" \
        -DLIB_INSTALL_DIR="%{tde_libdir}" \
        -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig" \
        -DSHARE_INSTALL_PREFIX="%{tde_datadir}" \
        \
        -DBUILD_ALL=ON \
        -DBUILD_DOC=ON \
        -DBUILD_DATA=ON \
        -DBUILD_MESSAGES=ON \
      ..

      # Run the build process in background
      ( %__make -j4 || %__make || echo TDE_Error ) &
      
      # Do not build more than 4 languages at the same time
      while [ $(jobs | wc -l) -ge 4 ]; do sleep 3; done
      popd
    fi
  done
done
) 2>&1 | tee /tmp/rpmbuild.$$

if grep -qw TDE_Error /tmp/rpmbuild.$$; then
  echo "Error while building. See '/tmp/rpmbuild.$$'"
  exit 1
fi

wait
rm -f /tmp/rpmbuild.$$


%install
%__rm -rf %{?buildroot}
export PATH="%{tde_bindir}:${PATH}"

for l in %{TDE_LANGS}; do
  for f in tde-i18n-${l}/; do
    %__make install DESTDIR="%{?buildroot}" -C "${f}/build"
  done
done


# remove zero-length file
find "%{buildroot}%{tde_tdedocdir}/HTML" -size 0 -exec rm -f {} \;

# remove obsolete KDE 3 application data translations
%__rm -rf "%{buildroot}%{tde_datadir}/apps"


%clean
%__rm -rf %{buildroot}

%if "%( grep -w af <<< '%{TDE_LANGS}' )" != ""
%files Afrikaans
%defattr(-,root,root,-)
%{tde_datadir}/locale/af/*
%{tde_tdedocdir}/HTML/af/
%endif

%if "%( grep -w ar <<< '%{TDE_LANGS}' )" != ""
%files Arabic 
%defattr(-,root,root,-)
%{tde_datadir}/locale/ar/*
%endif

%if "%( grep -w az <<< '%{TDE_LANGS}' )" != ""
%files Azerbaijani
%defattr(-,root,root,-)
%{tde_datadir}/locale/az/*
%endif

%if "%( grep -w be <<< '%{TDE_LANGS}' )" != ""
%files Belarusian
%defattr(-,root,root,-)
%{tde_datadir}/locale/be/*
%endif

%if "%( grep -w bg <<< '%{TDE_LANGS}' )" != ""
%files Bulgarian
%defattr(-,root,root,-)
%{tde_datadir}/locale/bg/*
%endif

%if "%( grep -w bn <<< '%{TDE_LANGS}' )" != ""
%files Bengali
%defattr(-,root,root,-)
%{tde_datadir}/locale/bn/*
%endif

%if "%( grep -w bo <<< '%{TDE_LANGS}' )" != ""
%files Tibetan
%defattr(-,root,root,-)
%{tde_datadir}/locale/bo/*
%endif

%if "%( grep -w br <<< '%{TDE_LANGS}' )" != ""
%files Breton
%defattr(-,root,root,-)
%{tde_datadir}/locale/br/*
%endif

%if "%( grep -w bs <<< '%{TDE_LANGS}' )" != ""
%files Bosnian
%defattr(-,root,root,-)
%{tde_datadir}/locale/bs/*
%endif

%if "%( grep -w ca <<< '%{TDE_LANGS}' )" != ""
%files Catalan
%defattr(-,root,root,-)
%{tde_datadir}/locale/ca/*
%{tde_tdedocdir}/HTML/ca/
%endif

%if "%( grep -w cs <<< '%{TDE_LANGS}' )" != ""
%files Czech
%defattr(-,root,root,-)
%{tde_datadir}/locale/cs/*
%{tde_tdedocdir}/HTML/cs/
%endif

%if "%( grep -w cy <<< '%{TDE_LANGS}' )" != ""
%files Welsh
%defattr(-,root,root,-)
%{tde_datadir}/locale/cy/*
%endif

%if "%( grep -w da <<< '%{TDE_LANGS}' )" != ""
%files Danish
%defattr(-,root,root,-)
%{tde_datadir}/locale/da/*
%{tde_tdedocdir}/HTML/da/
%endif

%if "%( grep -w de <<< '%{TDE_LANGS}' )" != ""
%files German
%defattr(-,root,root,-)
%{tde_datadir}/locale/de/*
%{tde_tdedocdir}/HTML/de/
%endif

%if "%( grep -w el <<< '%{TDE_LANGS}' )" != ""
%files Greek
%defattr(-,root,root,-)
%{tde_datadir}/locale/el/*
%endif

%if "%( grep -w en_GB <<< '%{TDE_LANGS}' )" != ""
%files British
%defattr(-,root,root,-)
%{tde_datadir}/locale/en_GB/*
%{tde_tdedocdir}/HTML/en_GB/
%endif

%if "%( grep -w eo <<< '%{TDE_LANGS}' )" != ""
%files Esperanto
%defattr(-,root,root,-)
%{tde_datadir}/locale/eo/*
%endif

%if "%( grep -w es <<< '%{TDE_LANGS}' )" != ""
%files Spanish
%defattr(-,root,root,-)
%{tde_datadir}/locale/es/*
%{tde_tdedocdir}/HTML/es/
%endif

%if "%( grep -w et <<< '%{TDE_LANGS}' )" != ""
%files Estonian
%defattr(-,root,root,-)
%{tde_datadir}/locale/et/*
%{tde_tdedocdir}/HTML/et/
%endif

%if "%( grep -w eu <<< '%{TDE_LANGS}' )" != ""
%files Basque
%defattr(-,root,root,-)
%{tde_datadir}/locale/eu/*
%endif

%if "%( grep -w fa <<< '%{TDE_LANGS}' )" != ""
%files Farsi
%defattr(-,root,root,-)
%{tde_datadir}/locale/fa/*
%endif

%if "%( grep -w fi <<< '%{TDE_LANGS}' )" != ""
%files Finnish
%defattr(-,root,root,-)
%{tde_datadir}/locale/fi/*
%{tde_tdedocdir}/HTML/fi/
%endif

%if "%( grep -w fo <<< '%{TDE_LANGS}' )" != ""
%files Faroese
%defattr(-,root,root,-)
%{tde_datadir}/locale/fo/*
%endif

%if "%( grep -w fr <<< '%{TDE_LANGS}' )" != ""
%files French
%defattr(-,root,root,-)
%{tde_datadir}/locale/fr/*
%{tde_tdedocdir}/HTML/fr/
%endif

%if "%( grep -w fy <<< '%{TDE_LANGS}' )" != ""
%files Frisian
%defattr(-,root,root,-)
%{tde_datadir}/locale/fy/*
%endif

%if "%( grep -w ga <<< '%{TDE_LANGS}' )" != ""
%files Irish
%defattr(-,root,root,-)
%{tde_datadir}/locale/ga/*
%endif

%if "%( grep -w gl <<< '%{TDE_LANGS}' )" != ""
%files Galician
%defattr(-,root,root,-)
%{tde_datadir}/locale/gl/*
%endif

%if "%( grep -w he <<< '%{TDE_LANGS}' )" != ""
%files Hebrew
%defattr(-,root,root,-)
%{tde_datadir}/locale/he/*
%{tde_tdedocdir}/HTML/he/
%endif

%if "%( grep -w hi <<< '%{TDE_LANGS}' )" != ""
%files Hindi
%defattr(-,root,root,-)
%{tde_datadir}/locale/hi/*
%endif

%if "%( grep -w hr <<< '%{TDE_LANGS}' )" != ""
%files Croatian
%defattr(-,root,root,-)
%{tde_datadir}/locale/hr/*
%{tde_tdedocdir}/HTML/hr/
%endif

%if "%( grep -w hu <<< '%{TDE_LANGS}' )" != ""
%files Hungarian
%defattr(-,root,root,-)
%{tde_datadir}/locale/hu/*
%{tde_tdedocdir}/HTML/hu/
%endif

%if "%( grep -w id <<< '%{TDE_LANGS}' )" != ""
%files Indonesian
%defattr(-,root,root,-)
%{tde_datadir}/locale/id/*
%{tde_tdedocdir}/HTML/id/
%endif

%if "%( grep -w is <<< '%{TDE_LANGS}' )" != ""
%files Icelandic
%defattr(-,root,root,-)
%{tde_datadir}/locale/is/*
%endif

%if "%( grep -w it <<< '%{TDE_LANGS}' )" != ""
%files Italian
%defattr(-,root,root,-)
%{tde_datadir}/locale/it/*
%{tde_tdedocdir}/HTML/it/
%endif

%if "%( grep -w ja <<< '%{TDE_LANGS}' )" != ""
%files Japanese
%defattr(-,root,root,-)
%{tde_datadir}/locale/ja/*
%{tde_tdedocdir}/HTML/ja/
%endif

%if "%( grep -w ko <<< '%{TDE_LANGS}' )" != ""
%files Korean
%defattr(-,root,root,-)
%{tde_datadir}/locale/ko/*
%{tde_tdedocdir}/HTML/ko/
%endif

%if "%( grep -w ku <<< '%{TDE_LANGS}' )" != ""
%files Kurdish
%defattr(-,root,root,-)
%{tde_datadir}/locale/ku/*
%{tde_tdedocdir}/HTML/ku/
%endif

%if "%( grep -w lao <<< '%{TDE_LANGS}' )" != ""
%files Lao
%defattr(-,root,root,-)
%{tde_datadir}/locale/lo/*
%{tde_tdedocdir}/HTML/lo/
%endif

%if "%( grep -w lt <<< '%{TDE_LANGS}' )" != ""
%files Lithuanian
%defattr(-,root,root,-)
%{tde_datadir}/locale/lt/*
%endif

%if "%( grep -w lv <<< '%{TDE_LANGS}' )" != ""
%files Latvian
%defattr(-,root,root,-)
%{tde_datadir}/locale/lv/*
%endif

%if "%( grep -w mi <<< '%{TDE_LANGS}' )" != ""
%files Maori
%defattr(-,root,root,-)
%{tde_datadir}/locale/mi/*
%endif

%if "%( grep -w mk <<< '%{TDE_LANGS}' )" != ""
%files Macedonian
%defattr(-,root,root,-)
%{tde_datadir}/locale/mk/*
%endif

%if "%( grep -w mt <<< '%{TDE_LANGS}' )" != ""
%files Maltese
%defattr(-,root,root,-)
%{tde_datadir}/locale/mt/*
%endif

%if "%( grep -w nl <<< '%{TDE_LANGS}' )" != ""
%files Dutch
%defattr(-,root,root,-)
%{tde_datadir}/locale/nl/*
%{tde_tdedocdir}/HTML/nl/
%endif

%if "%( grep -w nb <<< '%{TDE_LANGS}' )" != ""
%files Norwegian
%defattr(-,root,root,-)
%{tde_datadir}/locale/nb/*
#%{tde_tdedocdir}/HTML/nb/
%endif

%if "%( grep -w nn <<< '%{TDE_LANGS}' )" != ""
%files Norwegian-Nynorsk
%defattr(-,root,root,-)
%{tde_datadir}/locale/nn/*
#%{tde_tdedocdir}/HTML/nn/
%endif

%if "%( grep -w oc <<< '%{TDE_LANGS}' )" != ""
%files Occitan
%defattr(-,root,root,-)
%{tde_datadir}/locale/oc/*
%endif

%if "%( grep -w pa <<< '%{TDE_LANGS}' )" != ""
%files Punjabi
%defattr(-,root,root,-)
%{tde_datadir}/locale/pa/*
%endif

%if "%( grep -w pl <<< '%{TDE_LANGS}' )" != ""
%files Polish
%defattr(-,root,root,-)
%{tde_datadir}/locale/pl/*
%{tde_tdedocdir}/HTML/pl/
%endif

%if "%( grep -w pt <<< '%{TDE_LANGS}' )" != ""
%files Portuguese
%defattr(-,root,root,-)
%{tde_datadir}/locale/pt/*
%{tde_tdedocdir}/HTML/pt/
%endif

%if "%( grep -w pt_BR <<< '%{TDE_LANGS}' )" != ""
%files Brazil
%defattr(-,root,root,-)
%{tde_datadir}/locale/pt_BR/*
%{tde_tdedocdir}/HTML/pt_BR/
%endif

%if "%( grep -w ro <<< '%{TDE_LANGS}' )" != ""
%files Romanian
%defattr(-,root,root,-)
%{tde_datadir}/locale/ro/*
%{tde_tdedocdir}/HTML/ro/
%endif

%if "%( grep -w ru <<< '%{TDE_LANGS}' )" != ""
%files Russian
%defattr(-,root,root,-)
%{tde_datadir}/locale/ru/*
%{tde_tdedocdir}/HTML/ru/
%endif

%if "%( grep -w sk <<< '%{TDE_LANGS}' )" != ""
%files Slovak
%defattr(-,root,root,-)
%{tde_datadir}/locale/sk/*
%{tde_tdedocdir}/HTML/sk/
%endif

%if "%( grep -w sl <<< '%{TDE_LANGS}' )" != ""
%files Slovenian
%defattr(-,root,root,-)
%{tde_datadir}/locale/sl/*
%{tde_tdedocdir}/HTML/sl/
%endif

%if "%( grep -w sr <<< '%{TDE_LANGS}' )" != ""
%files Serbian
%defattr(-,root,root,-)
%{tde_datadir}/locale/sr/*
%{tde_tdedocdir}/HTML/sr/
%endif

%if "%( grep -w sv <<< '%{TDE_LANGS}' )" != ""
%files Swedish
%defattr(-,root,root,-)
%{tde_datadir}/locale/sv/*
%{tde_tdedocdir}/HTML/sv/
%endif

%if "%( grep -w ta <<< '%{TDE_LANGS}' )" != ""
%files Tamil
%defattr(-,root,root,-)
%{tde_datadir}/locale/ta/*
%endif

%if "%( grep -w tg <<< '%{TDE_LANGS}' )" != ""
%files Tajik
%defattr(-,root,root,-)
%{tde_datadir}/locale/tg/*
%endif

%if "%( grep -w th <<< '%{TDE_LANGS}' )" != ""
%files Thai
%defattr(-,root,root,-)
%{tde_datadir}/locale/th/*
%endif

%if "%( grep -w tr <<< '%{TDE_LANGS}' )" != ""
%files Turkish
%defattr(-,root,root,-)
%{tde_datadir}/locale/tr/*
%{tde_tdedocdir}/HTML/tr/
%endif

%if "%( grep -w uk <<< '%{TDE_LANGS}' )" != ""
%files Ukrainian
%defattr(-,root,root,-)
%{tde_tdedocdir}/HTML/uk/
%{tde_datadir}/locale/uk/*
%endif

%if "%( grep -w ven <<< '%{TDE_LANGS}' )" != ""
%files Venda
%defattr(-,root,root,-)
%{tde_datadir}/locale/ven/*
%endif

%if "%( grep -w vi <<< '%{TDE_LANGS}' )" != ""
%files Vietnamese
%defattr(-,root,root,-)
%{tde_datadir}/locale/vi/*
%endif

%if "%( grep -w wa <<< '%{TDE_LANGS}' )" != ""
%files Walloon
%defattr(-,root,root,-)
%{tde_datadir}/locale/wa/*
%endif

%if "%( grep -w xh <<< '%{TDE_LANGS}' )" != ""
%files Xhosa
%defattr(-,root,root,-)
%{tde_datadir}/locale/xh/*
%{tde_tdedocdir}/HTML/xh/
%endif

%if "%( grep -w zh_CN <<< '%{TDE_LANGS}' )" != ""
%files Chinese
%defattr(-,root,root,-)
%{tde_datadir}/locale/zh_CN/*
%{tde_tdedocdir}/HTML/zh_CN/
%endif

%if "%( grep -w zh_TW <<< '%{TDE_LANGS}' )" != ""
%files Chinese-Big5
%defattr(-,root,root,-)
%{tde_datadir}/locale/zh_TW/*
%{tde_tdedocdir}/HTML/zh_TW/
%endif

%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 14.0.0-1
- Initial release for TDE 14.0.0
