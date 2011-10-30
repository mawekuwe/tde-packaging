# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity

# Builds all supported languages (not unsupported ones)
%if "%{?KDE_LANGS}" == ""
%define KDE_LANGS ar bg bn ca cs da de el en_GB es et fi fr he hi hu is it ja lt nl nb nn pa pl pt pt_BR ro ru sk sl sr sv ta tr uk zh_CN zh_TW
%endif


Name:		trinity-kde-i18n
Summary:	Internationalization support for Trinity
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# GFDL, with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
License:	GFDL
Group:		User Interface/Desktops
BuildArch:	noarch

# Speed build options
%define debug_package %{nil}
%define __spec_install_post %{nil}
AutoReq: no

Source0:	kde-i18n-%{version}.tar.gz

# Patch for 'kdesu': the message was modified in 'kdebase' package
Patch0:		kde-i18n-kdesu.patch

# Patch to translate 'Open Terminal Here' desktop shortcut
Patch1:		trinity-kde-i18n-fr-openterminalhere.patch

BuildRequires:	findutils
BuildRequires:	gettext
BuildRequires:	trinity-arts-devel
BuildRequires:	trinity-kdelibs-devel

%description
%{summary}.

%package Afrikaans
Summary: Afrikaans(af) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-af = %{version}-%{release}
Requires: kde-filesystem
%description Afrikaans
%{summary}.

%package Arabic 
Summary: Arabic(ar) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-ar = %{version}-%{release}
Requires: kde-filesystem
%description Arabic
%{summary}.

%package Azerbaijani
Summary: Azerbaijani(az) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-az = %{version}-%{release}
Requires: kde-filesystem
%description Azerbaijani
%{summary}.

%package Belarusian
Summary: Belarusian(be) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-be = %{version}-%{release}
Requires: kde-filesystem
%description Belarusian
%{summary}.

%package Bulgarian
Summary: Bulgarian(bg) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-bg = %{version}-%{release}
Requires: kde-filesystem
%description Bulgarian
%{summary}.

%package Bengali
Summary: Bengali(bn) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-bn = %{version}-%{release}
Requires: kde-filesystem
%description Bengali
%{summary}.

%package Tibetan
Summary: Tibetan(bo) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-bo = %{version}-%{release}
Requires: kde-filesystem
%description Tibetan
%{summary}.

%package Breton
Summary: Breton(br) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-br = %{version}-%{release}
Requires: kde-filesystem
%description Breton
%{summary}.

%package Bosnian
Summary: Bosnian(bs) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-bs = %{version}-%{release}
Requires: kde-filesystem
%description Bosnian
%{summary}.

%package Catalan
Summary: Catalan(ca) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-ca = %{version}-%{release}
Requires: kde-filesystem
%description Catalan
%{summary}.

%package Czech
Summary: Czech(cs) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-cs = %{version}-%{release}
Requires: kde-filesystem
%description Czech
%{summary}.

%package Cymraeg
Summary: Cymraeg language support for KDE3
Group: User Interface/Desktops
Requires: kde-filesystem
%description Cymraeg
%{summary}.

%package Welsh
Summary: Welsh(cy) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-cy = %{version}-%{release}
Requires: kde-filesystem
%description Welsh
%{summary}.

%package Danish
Summary: Danish(da) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-da = %{version}-%{release}
Requires: kde-filesystem
%description Danish
%{summary}.

%package German
Summary: German(de) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-de = %{version}-%{release}
Requires: kde-filesystem
%description German
%{summary}.

%package Greek
Summary: Greek(el) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-el = %{version}-%{release}
Requires: kde-filesystem
%description Greek
%{summary}.

%package British
Summary: British(en_GB) English support for KDE3
Group: User Interface/Desktops
Provides: %{name}-en_GB = %{version}-%{release}
Requires: kde-filesystem
%description British
%{summary}.

%package Esperanto
Summary: Esperanto(eo) support for KDE3
Group: User Interface/Desktops
Provides: %{name}-eo = %{version}-%{release}
Requires: kde-filesystem
%description Esperanto
%{summary}.

%package Spanish
Summary: Spanish(es) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-es = %{version}-%{release}
Requires: kde-filesystem
%description Spanish
%{summary}.

%package Estonian
Summary: Estonian(et) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-et = %{version}-%{release}
Requires: kde-filesystem
%description Estonian
%{summary}.

%package Basque
Summary: Basque(eu) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-eu = %{version}-%{release}
Requires: kde-filesystem
%description Basque
%{summary}.

%package Farsi
Summary: Farsi(fa) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-fa = %{version}-%{release}
Requires: kde-filesystem
%description Farsi
%{summary}.

%package Finnish
Summary: Finnish(fi) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-fi = %{version}-%{release}
Requires: kde-filesystem
%description Finnish
%{summary}.

%package Faroese
Summary: Faroese(fo) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-fo = %{version}-%{release}
Requires: kde-filesystem
%description Faroese
%{summary}.

%package French
Summary: French(fr) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-fr = %{version}-%{release}
Requires: kde-filesystem
%description French
%{summary}.

%package Frisian
Summary: Frisian(fy) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-fy = %{version}-%{release}
Requires: kde-filesystem
%description Frisian
%{summary}.

%package Irish
Summary: Irish(ga) language support for KDE3
Group: User Interface/Desktops
Obsoletes: kde-i18n-Gaeilge < %{version}
Provides: %{name}-ga = %{version}-%{release}
Requires: kde-filesystem
%description Irish
%{summary}.

%package Galician
Summary: Galician(gl) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-gl = %{version}-%{release}
Requires: kde-filesystem
%description Galician
%{summary}.

%package Hebrew
Summary: Hebrew(he) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-he = %{version}-%{release}
Requires: kde-filesystem
%description Hebrew
%{summary}.

%package Hindi
Summary: Hindi(hi) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-hi = %{version}-%{release}
Requires: kde-filesystem
%description Hindi
%{summary}.

%package Croatian
Summary: Croatian(hr) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-hr = %{version}-%{release}
Requires: kde-filesystem
%description Croatian
%{summary}.

%package Hungarian
Summary: Hungarian(hu) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-hu = %{version}-%{release}
Requires: kde-filesystem
%description Hungarian
%{summary}.

%package Indonesian
Summary: Indonesian(id) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-id = %{version}-%{release}
Requires: kde-filesystem
%description Indonesian
%{summary}.

%package Icelandic
Summary: Icelandic(is) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-is = %{version}-%{release}
Requires: kde-filesystem
%description Icelandic
%{summary}.

%package Italian
Summary: Italian(it) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-it = %{version}-%{release}
Requires: kde-filesystem
%description Italian
%{summary}.

%package Japanese
Summary: Japanese(ja) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-ja = %{version}-%{release}
Requires: kde-filesystem
%description Japanese
%{summary}.

%package Korean
Summary: Korean(ko) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-ko = %{version}-%{release}
Requires: kde-filesystem
%description Korean
%{summary}.

%package Kurdish
Summary: Kurdish(ku) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-ku = %{version}-%{release}
Requires: kde-filesystem
%description Kurdish
%{summary}.

%package Lao
Summary: Lao(lo) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-lo = %{version}-%{release}
Requires: kde-filesystem
%description Lao
%{summary}.

%package Lithuanian
Summary: Lithuanian(lt) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-lt = %{version}-%{release}
Requires: kde-filesystem
%description Lithuanian
%{summary}.

%package Latvian
Summary: Latvian(lv) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-lv = %{version}-%{release}
Requires: kde-filesystem
%description Latvian
%{summary}.

%package Maori
Summary: Maori(mi) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-mi = %{version}-%{release}
Requires: kde-filesystem
%description Maori
%{summary}.

%package Macedonian
Summary: Macedonian(mk) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-mk = %{version}-%{release}
Requires: kde-filesystem
%description Macedonian
%{summary}.

%package Maltese
Summary: Maltese(mt) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-mt = %{version}-%{release}
Requires: kde-filesystem
%description Maltese
%{summary}.

%package Dutch
Summary: Dutch(nl) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-nl = %{version}-%{release}
Requires: kde-filesystem
%description Dutch
%{summary}.

%package Norwegian
Summary: Norwegian(no) (Bokmaal) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-no = %{version}-%{release}
Requires: kde-filesystem
%description Norwegian
%{summary}.

%package Norwegian-Nynorsk
Summary: Norwegian(nn) (Nynorsk) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-nn = %{version}-%{release}
Requires: kde-filesystem
%description Norwegian-Nynorsk
%{summary}.

%package Occitan
Summary: Occitan(oc) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-oc = %{version}-%{release}
Requires: kde-filesystem
%description Occitan
%{summary}.

%package Polish
Summary: Polish(pl) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-pl = %{version}-%{release}
Requires: kde-filesystem
%description Polish
%{summary}.

%package Portuguese
Summary: Portuguese(pt) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-pt = %{version}-%{release}
Requires: kde-filesystem
%description Portuguese
%{summary}.

%package Punjabi
Summary: Punjabi(pa) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-pa = %{version}-%{release}
Requires: kde-filesystem
%description Punjabi
%{summary}.

%package Brazil
Summary: Brazil(pt_BR) Portuguese language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-pt_BR = %{version}-%{release}
Requires: kde-filesystem
%description Brazil
%{summary}.

%package Romanian
Summary: Romanian(ro) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-ro = %{version}-%{release}
Requires: kde-filesystem
%description Romanian
%{summary}.

%package Russian
Summary: Russian(ru) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-ru = %{version}-%{release}
Requires: kde-filesystem
%description Russian
%{summary}.

%package Slovak
Summary: Slovak(sk) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-sk = %{version}-%{release}
Requires: kde-filesystem
%description Slovak
%{summary}.

%package Slovenian
Summary: Slovenian(sl) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-sl = %{version}-%{release}
Requires: kde-filesystem
%description Slovenian
%{summary}.

%package Serbian
Summary: Serbian(sr) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-sr = %{version}-%{release}
Requires: kde-filesystem
%description Serbian
%{summary}.

%package Swedish
Summary: Swedish(sv) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-sv = %{version}-%{release}
Requires: kde-filesystem
%description Swedish
%{summary}.

%package Tamil
Summary: Tamil(ta) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-ta = %{version}-%{release}
Requires: kde-filesystem
%description Tamil
%{summary}.

%package Tajik
Summary: Tajik(tg) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-tg = %{version}-%{release}
Requires: kde-filesystem
%description Tajik
%{summary}.

%package Thai
Summary: Thai(th) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-th = %{version}-%{release}
Requires: kde-filesystem
%description Thai
%{summary}.

%package Turkish
Summary: Turkish(tr) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-tr = %{version}-%{release}
Requires: kde-filesystem
%description Turkish
%{summary}.

%package Ukrainian
Summary: Ukrainian(uk) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-uk = %{version}-%{release}
Requires: kde-filesystem
%description Ukrainian
%{summary}.

%package Venda
Summary: Venda(ven) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-ven = %{version}-%{release}
Requires: kde-filesystem
%description Venda
%{summary}.

%package Vietnamese
Summary: Vietnamese(vi) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-vi = %{version}-%{release}
Requires: kde-filesystem
%description Vietnamese
%{summary}.

%package Walloon
Summary: Walloon(wa) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-wa = %{version}-%{release}
Requires: kde-filesystem
%description Walloon
%{summary}.

%package Xhosa
Summary: Xhosa(xh) (a Bantu language) support for KDE3
Group: User Interface/Desktops
Provides: %{name}-xh = %{version}-%{release}
Requires: kde-filesystem
%description Xhosa
%{summary}.

%package Chinese
Summary: Chinese(zh_CN) (Simplified Chinese) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-zh_CN = %{version}-%{release}
Requires: kde-filesystem
%description Chinese
%{summary}.

%package Chinese-Big5
Summary: Chinese(zh_TW) (Big5) language support for KDE3
Group: User Interface/Desktops
Provides: %{name}-tz_TW = %{version}-%{release}
Requires: kde-filesystem
%description Chinese-Big5
%{summary}.



%prep
%setup -q -n kde-i18n

for l in %{KDE_LANGS}; do
  for f in kde-i18n-${l}-*.tar.bz2; do
    tar xjf ${f}
  done
done

%patch0
%patch1


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

for l in %{KDE_LANGS}; do
  for f in kde-i18n-${l}-*/; do
    if [ -d "${f}" ] && [ -x "${f}/configure" ] ; then 
      pushd ${f}
      %configure --prefix=%{_prefix}
      %{__make} %{?_smp_mflags}
      popd
    fi
  done
done

%install
rm -rf %{?buildroot}
export PATH="%{_bindir}:${PATH}"

for l in %{KDE_LANGS}; do
  for f in kde-i18n-${l}-*/; do
    if [ -d "${f}" ] && [ -r "${f}/Makefile" ] ; then 
      pushd ${f}

      # Thales: dirty hack to remove directory 'common' from install list (else it fails to install)
      if [ -r docs/Makefile ]; then
        sed -i docs/Makefile -e "s,^\(SUBDIRS =.*\)common\(.*\)$,\1 \2,"
      fi

      %__make install DESTDIR=%{?buildroot}
      popd
    fi
  done
done

# make symlinks relative
pushd %{buildroot}%{_docdir}/HTML
for lang in *; do
  if [ -d $lang ]; then
    pushd $lang
    for i in */*/*; do
      if [ -d $i -a -L $i/common ]; then
        rm -f $i/common
        ln -sf ../../../docs/common $i
      fi
    done

    for i in */*; do
      if [ -d $i -a -L $i/common ]; then
        rm -f $i/common
        ln -sf ../../docs/common $i
      fi
    done

    for i in *; do
      if [ -d $i -a -L $i/common ]; then
        rm -f $i/common
        ln -sf ../docs/common $i
      fi
    done

    popd
  fi
done
popd   

# remove zero-length file
find %{buildroot}%{_docdir}/HTML -size 0 -exec rm -f {} \;

# See http://fedoraproject.org/wiki/Languages (???)
rm -f %{buildroot}%{_datadir}/locale/*/flag.png
# And also the 'desktop.entry' (???)
rm -f %{buildroot}%{_datadir}/locale/*/entry.desktop

# remove obsolete KDE 3 application data translations
rm -rf %{buildroot}%{_datadir}/apps

%clean
rm -rf %{buildroot}

%if "%( grep -w af <<< '%{KDE_LANGS}' )" != ""
%files Afrikaans
%defattr(-,root,root,-)
%lang(af) %{_datadir}/locale/af/LC_MESSAGES/*
%lang(af) %{_datadir}/locale/af/charset
%lang(af) %{_docdir}/HTML/af/
%endif

%if "%( grep -w ar <<< '%{KDE_LANGS}' )" != ""
%files Arabic 
%defattr(-,root,root,-)
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/*
%lang(ar) %{_datadir}/locale/ar/charset
%endif

%if "%( grep -w az <<< '%{KDE_LANGS}' )" != ""
%files Azerbaijani
%defattr(-,root,root,-)
%lang(az) %{_datadir}/locale/az/LC_MESSAGES/*
%lang(az) %{_datadir}/locale/az/charset
%endif

%if "%( grep -w be <<< '%{KDE_LANGS}' )" != ""
%files Belarusian
%defattr(-,root,root,-)
%lang(be) %{_datadir}/locale/be/LC_MESSAGES/*
%lang(be) %{_datadir}/locale/be/charset
%endif

%if "%( grep -w bg <<< '%{KDE_LANGS}' )" != ""
%files Bulgarian
%defattr(-,root,root,-)
%lang(bg) %{_datadir}/locale/bg/LC_MESSAGES/*
%lang(bg) %{_datadir}/locale/bg/charset
%endif

%if "%( grep -w bn <<< '%{KDE_LANGS}' )" != ""
%files Bengali
%defattr(-,root,root,-)
%lang(bn) %{_datadir}/locale/bn/LC_MESSAGES/*
%lang(bn) %{_datadir}/locale/bn/charset
%endif

%if "%( grep -w bo <<< '%{KDE_LANGS}' )" != ""
%files Tibetan
%defattr(-,root,root,-)
%lang(bo) %{_datadir}/locale/bo/LC_MESSAGES/*
%lang(bo) %{_datadir}/locale/bo/charset
%endif

%if "%( grep -w br <<< '%{KDE_LANGS}' )" != ""
%files Breton
%defattr(-,root,root,-)
%lang(br) %{_datadir}/locale/br/LC_MESSAGES/*
%lang(br) %{_datadir}/locale/br/charset
%endif

%if "%( grep -w bs <<< '%{KDE_LANGS}' )" != ""
%files Bosnian
%defattr(-,root,root,-)
%lang(bs) %{_datadir}/locale/bs/LC_MESSAGES/*
%lang(bs) %{_datadir}/locale/bs/charset
%endif

%if "%( grep -w ca <<< '%{KDE_LANGS}' )" != ""
%files Catalan
%defattr(-,root,root,-)
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/*
%lang(ca) %{_datadir}/locale/ca/charset
%lang(ca) %{_docdir}/HTML/ca/
%endif

%if "%( grep -w cs <<< '%{KDE_LANGS}' )" != ""
%files Czech
%defattr(-,root,root,-)
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/*
%lang(cs) %{_datadir}/locale/cs/charset
%lang(cs) %{_docdir}/HTML/cs/
%endif

%if "%( grep -w cy <<< '%{KDE_LANGS}' )" != ""
%files Welsh
%defattr(-,root,root,-)
%lang(cy) %{_datadir}/locale/cy/LC_MESSAGES/*
%lang(cy) %{_datadir}/locale/cy/charset
%endif

%if "%( grep -w da <<< '%{KDE_LANGS}' )" != ""
%files Danish
%defattr(-,root,root,-)
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/*
%lang(da) %{_datadir}/locale/da/charset
%lang(da) %{_datadir}/locale/da/da.compendium
%lang(da) %{_docdir}/HTML/da/
%endif

%if "%( grep -w de <<< '%{KDE_LANGS}' )" != ""
%files German
%defattr(-,root,root,-)
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*
%lang(de) %{_datadir}/locale/de/charset
%lang(de) %{_docdir}/HTML/de/
%endif

%if "%( grep -w el <<< '%{KDE_LANGS}' )" != ""
%files Greek
%defattr(-,root,root,-)
%lang(el) %{_datadir}/locale/el/LC_MESSAGES/*
%lang(el) %{_datadir}/locale/el/charset
%endif

%if "%( grep -w en_GB <<< '%{KDE_LANGS}' )" != ""
%files British
%defattr(-,root,root,-)
%lang(en_GB) %{_datadir}/locale/en_GB/LC_MESSAGES/*
%lang(en_GB) %{_datadir}/locale/en_GB/charset
%lang(en_GB) %{_docdir}/HTML/en_GB/
%endif

%if "%( grep -w eo <<< '%{KDE_LANGS}' )" != ""
%files Esperanto
%defattr(-,root,root,-)
%lang(eo) %{_datadir}/locale/eo/LC_MESSAGES/*
%lang(eo) %{_datadir}/locale/eo/charset
%endif

%if "%( grep -w es <<< '%{KDE_LANGS}' )" != ""
%files Spanish
%defattr(-,root,root,-)
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*
%lang(es) %{_datadir}/locale/es/charset
%lang(es) %{_docdir}/HTML/es/
%endif

%if "%( grep -w et <<< '%{KDE_LANGS}' )" != ""
%files Estonian
%defattr(-,root,root,-)
%lang(et) %{_datadir}/locale/et/LC_MESSAGES/*
%lang(et) %{_datadir}/locale/et/charset
%lang(et) %{_docdir}/HTML/et/
%endif

%if "%( grep -w eu <<< '%{KDE_LANGS}' )" != ""
%files Basque
%defattr(-,root,root,-)
%lang(eu) %{_datadir}/locale/eu/LC_MESSAGES/*
%lang(eu) %{_datadir}/locale/eu/charset
%endif

%if "%( grep -w fa <<< '%{KDE_LANGS}' )" != ""
%files Farsi
%defattr(-,root,root,-)
%lang(fa) %{_datadir}/locale/fa/LC_MESSAGES/*
%lang(fa) %{_datadir}/locale/fa/charset
%endif

%if "%( grep -w fi <<< '%{KDE_LANGS}' )" != ""
%files Finnish
%defattr(-,root,root,-)
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/*
%lang(fi) %{_datadir}/locale/fi/charset
%lang(fi) %{_docdir}/HTML/fi/
%endif

%if "%( grep -w fo <<< '%{KDE_LANGS}' )" != ""
%files Faroese
%defattr(-,root,root,-)
%lang(fo) %{_datadir}/locale/fo/LC_MESSAGES/*
%lang(fo) %{_datadir}/locale/fo/charset
%endif

%if "%( grep -w fr <<< '%{KDE_LANGS}' )" != ""
%files French
%defattr(-,root,root,-)
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*
%lang(fr) %{_datadir}/locale/fr/charset
%lang(fr) %{_datadir}/locale/fr/nbsp_gui_fr.txt
%lang(fr) %{_datadir}/locale/fr/relecture_*
%lang(fr) %{_docdir}/HTML/fr/
%endif

%if "%( grep -w fy <<< '%{KDE_LANGS}' )" != ""
%files Frisian
%defattr(-,root,root,-)
%lang(fy) %{_datadir}/locale/fy/LC_MESSAGES/*
%lang(fy) %{_datadir}/locale/fy/charset
%endif

%if "%( grep -w ga <<< '%{KDE_LANGS}' )" != ""
%files Irish
%defattr(-,root,root,-)
%lang(ga) %{_datadir}/locale/ga/LC_MESSAGES/*
%lang(ga) %{_datadir}/locale/ga/charset
%endif

%if "%( grep -w gl <<< '%{KDE_LANGS}' )" != ""
%files Galician
%defattr(-,root,root,-)
%lang(gl) %{_datadir}/locale/gl/LC_MESSAGES/*
%lang(gl) %{_datadir}/locale/gl/charset
%endif

%if "%( grep -w he <<< '%{KDE_LANGS}' )" != ""
%files Hebrew
%defattr(-,root,root,-)
%lang(he) %{_datadir}/locale/he/LC_MESSAGES/*
%lang(he) %{_datadir}/locale/he/charset
%lang(he) %{_docdir}/HTML/he/
%endif

%if "%( grep -w hi <<< '%{KDE_LANGS}' )" != ""
%files Hindi
%defattr(-,root,root,-)
%lang(hi) %{_datadir}/locale/hi/LC_MESSAGES/*
%lang(hi) %{_datadir}/locale/hi/charset
%endif

%if "%( grep -w hr <<< '%{KDE_LANGS}' )" != ""
%files Croatian
%defattr(-,root,root,-)
%lang(hr) %{_datadir}/locale/hr/LC_MESSAGES/*
%lang(hr) %{_datadir}/locale/hr/charset
%lang(hr) %{_docdir}/HTML/hr/
%endif

%if "%( grep -w hu <<< '%{KDE_LANGS}' )" != ""
%files Hungarian
%defattr(-,root,root,-)
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/*
%lang(hu) %{_datadir}/locale/hu/charset
%lang(hu) %{_docdir}/HTML/hu/
%endif

%if "%( grep -w id <<< '%{KDE_LANGS}' )" != ""
%files Indonesian
%defattr(-,root,root,-)
%lang(id) %{_datadir}/locale/id/LC_MESSAGES/*
%lang(id) %{_datadir}/locale/id/charset
%lang(id) %{_docdir}/HTML/id/
%endif

%if "%( grep -w is <<< '%{KDE_LANGS}' )" != ""
%files Icelandic
%defattr(-,root,root,-)
%lang(is) %{_datadir}/locale/is/LC_MESSAGES/*
%lang(is) %{_datadir}/locale/is/charset
%endif

%if "%( grep -w it <<< '%{KDE_LANGS}' )" != ""
%files Italian
%defattr(-,root,root,-)
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/*
%lang(it) %{_datadir}/locale/it/charset
%lang(it) %{_docdir}/HTML/it/
%endif

%if "%( grep -w ja <<< '%{KDE_LANGS}' )" != ""
%files Japanese
%defattr(-,root,root,-)
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/*
%lang(ja) %{_datadir}/locale/ja/charset
%lang(ja) %{_docdir}/HTML/ja/
%endif

%if "%( grep -w ko <<< '%{KDE_LANGS}' )" != ""
%files Korean
%defattr(-,root,root,-)
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/*
%lang(ko) %{_datadir}/locale/ko/charset
%lang(ko) %{_docdir}/HTML/ko/
%endif

%if "%( grep -w ku <<< '%{KDE_LANGS}' )" != ""
%files Kurdish
%defattr(-,root,root,-)
%lang(ku) %{_datadir}/locale/ku/LC_MESSAGES/*
%lang(ku) %{_datadir}/locale/ku/charset
%lang(ku) %{_docdir}/HTML/ku/
%endif

%if "%( grep -w lao <<< '%{KDE_LANGS}' )" != ""
%files Lao
%defattr(-,root,root,-)
%lang(lo) %{_datadir}/locale/lo/LC_MESSAGES/*
%lang(lo) %{_datadir}/locale/lo/charset
%lang(lo) %{_docdir}/HTML/lo/
%endif

%if "%( grep -w lt <<< '%{KDE_LANGS}' )" != ""
%files Lithuanian
%defattr(-,root,root,-)
%lang(lt) %{_datadir}/locale/lt/LC_MESSAGES/*
%lang(lt) %{_datadir}/locale/lt/charset
%endif

%if "%( grep -w lv <<< '%{KDE_LANGS}' )" != ""
%files Latvian
%defattr(-,root,root,-)
%lang(lv) %{_datadir}/locale/lv/LC_MESSAGES/*
%lang(lv) %{_datadir}/locale/lv/charset
%endif

%if "%( grep -w mi <<< '%{KDE_LANGS}' )" != ""
%files Maori
%defattr(-,root,root,-)
%lang(mi) %{_datadir}/locale/mi/LC_MESSAGES/*
%lang(mi) %{_datadir}/locale/mi/charset
%endif

%if "%( grep -w mk <<< '%{KDE_LANGS}' )" != ""
%files Macedonian
%defattr(-,root,root,-)
%lang(mk) %{_datadir}/locale/mk/LC_MESSAGES/*
%lang(mk) %{_datadir}/locale/mk/charset
%endif

%if "%( grep -w mt <<< '%{KDE_LANGS}' )" != ""
%files Maltese
%defattr(-,root,root,-)
%lang(mt) %{_datadir}/locale/mt/LC_MESSAGES/*
%lang(mt) %{_datadir}/locale/mt/charset
%endif

%if "%( grep -w nl <<< '%{KDE_LANGS}' )" != ""
%files Dutch
%defattr(-,root,root,-)
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/*
%lang(nl) %{_datadir}/locale/nl/charset
%lang(nl) %{_docdir}/HTML/nl/
%endif

%if "%( grep -w nb <<< '%{KDE_LANGS}' )" != ""
%files Norwegian
%defattr(-,root,root,-)
%lang(nb) %{_datadir}/locale/nb/LC_MESSAGES/*
%lang(nb) %{_datadir}/locale/nb/charset
%lang(nb) %{_datadir}/locale/nb/README
#%lang(nb) %{_docdir}/HTML/nb/
%endif

%if "%( grep -w nn <<< '%{KDE_LANGS}' )" != ""
%files Norwegian-Nynorsk
%defattr(-,root,root,-)
%lang(nn) %{_datadir}/locale/nn/LC_MESSAGES/*
%lang(nn) %{_datadir}/locale/nn/charset
#%lang(nn) %{_docdir}/HTML/nn/
%endif

%if "%( grep -w oc <<< '%{KDE_LANGS}' )" != ""
%files Occitan
%defattr(-,root,root,-)
%lang(oc) %{_datadir}/locale/oc/LC_MESSAGES/*
%lang(oc) %{_datadir}/locale/oc/charset
%endif

%if "%( grep -w pa <<< '%{KDE_LANGS}' )" != ""
%files Punjabi
%defattr(-,root,root,-)
%lang(pa) %{_datadir}/locale/pa/LC_MESSAGES/*
%lang(pa) %{_datadir}/locale/pa/charset
%endif

%if "%( grep -w pl <<< '%{KDE_LANGS}' )" != ""
%files Polish
%defattr(-,root,root,-)
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/*
%lang(pl) %{_datadir}/locale/pl/charset
%lang(pl) %{_docdir}/HTML/pl/
%endif

%if "%( grep -w pt <<< '%{KDE_LANGS}' )" != ""
%files Portuguese
%defattr(-,root,root,-)
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/*
%lang(pt) %{_datadir}/locale/pt/charset
%lang(pt) %{_docdir}/HTML/pt/
%endif

%if "%( grep -w pt_BR <<< '%{KDE_LANGS}' )" != ""
%files Brazil
%defattr(-,root,root,-)
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/*
%lang(pt_BR) %{_datadir}/locale/pt_BR/charset
%lang(pt_BR) %{_docdir}/HTML/pt_BR/
%endif

%if "%( grep -w ro <<< '%{KDE_LANGS}' )" != ""
%files Romanian
%defattr(-,root,root,-)
%lang(ro) %{_datadir}/locale/ro/LC_MESSAGES/*
%lang(ro) %{_datadir}/locale/ro/charset
%lang(ro) %{_docdir}/HTML/ro/
%endif

%if "%( grep -w ru <<< '%{KDE_LANGS}' )" != ""
%files Russian
%defattr(-,root,root,-)
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/*
%lang(ru) %{_datadir}/locale/ru/charset
%lang(ru) %{_docdir}/HTML/ru/
%endif

%if "%( grep -w sk <<< '%{KDE_LANGS}' )" != ""
%files Slovak
%defattr(-,root,root,-)
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/*
%lang(sk) %{_datadir}/locale/sk/charset
%lang(sk) %{_docdir}/HTML/sk/
%endif

%if "%( grep -w sl <<< '%{KDE_LANGS}' )" != ""
%files Slovenian
%defattr(-,root,root,-)
%lang(sl) %{_datadir}/locale/sl/LC_MESSAGES/*
%lang(sl) %{_datadir}/locale/sl/charset
%lang(sl) %{_docdir}/HTML/sl/
%endif

%if "%( grep -w sr <<< '%{KDE_LANGS}' )" != ""
%files Serbian
%defattr(-,root,root,-)
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/*
%lang(sr) %{_datadir}/locale/sr/charset
%lang(sr) %{_docdir}/HTML/sr/
%endif

%if "%( grep -w sv <<< '%{KDE_LANGS}' )" != ""
%files Swedish
%defattr(-,root,root,-)
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/*
%lang(sv) %{_datadir}/locale/sv/charset
%lang(sv) %{_docdir}/HTML/sv/
%endif

%if "%( grep -w ta <<< '%{KDE_LANGS}' )" != ""
%files Tamil
%defattr(-,root,root,-)
%lang(ta) %{_datadir}/locale/ta/LC_MESSAGES/*
%lang(ta) %{_datadir}/locale/ta/charset
%endif

%if "%( grep -w tg <<< '%{KDE_LANGS}' )" != ""
%files Tajik
%defattr(-,root,root,-)
%lang(tg) %{_datadir}/locale/tg/LC_MESSAGES/*
%lang(tg) %{_datadir}/locale/tg/charset
%endif

%if "%( grep -w th <<< '%{KDE_LANGS}' )" != ""
%files Thai
%defattr(-,root,root,-)
%lang(th) %{_datadir}/locale/th/LC_MESSAGES/*
%lang(th) %{_datadir}/locale/th/charset
%endif

%if "%( grep -w tr <<< '%{KDE_LANGS}' )" != ""
%files Turkish
%defattr(-,root,root,-)
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/*
%lang(tr) %{_datadir}/locale/tr/charset
%lang(tr) %{_docdir}/HTML/tr/
%endif

%if "%( grep -w uk <<< '%{KDE_LANGS}' )" != ""
%files Ukrainian
%defattr(-,root,root,-)
%lang(uk) %{_docdir}/HTML/uk/
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/*
%lang(uk) %{_datadir}/locale/uk/charset
%endif

%if "%( grep -w ven <<< '%{KDE_LANGS}' )" != ""
%files Venda
%defattr(-,root,root,-)
%lang(ven) %{_datadir}/locale/ven/LC_MESSAGES/*
%lang(ven) %{_datadir}/locale/ven/charset
%endif

%if "%( grep -w vi <<< '%{KDE_LANGS}' )" != ""
%files Vietnamese
%defattr(-,root,root,-)
%lang(vi) %{_datadir}/locale/vi/LC_MESSAGES/*
%lang(vi) %{_datadir}/locale/vi/charset
%endif

%if "%( grep -w wa <<< '%{KDE_LANGS}' )" != ""
%files Walloon
%defattr(-,root,root,-)
%lang(wa) %{_datadir}/locale/wa/LC_MESSAGES/*
%lang(wa) %{_datadir}/locale/wa/charset
%endif

%if "%( grep -w xh <<< '%{KDE_LANGS}' )" != ""
%files Xhosa
%defattr(-,root,root,-)
%lang(xh) %{_datadir}/locale/xh/LC_MESSAGES/*
%lang(xh) %{_datadir}/locale/xh/charset
%lang(xh) %{_docdir}/HTML/xh/
%endif

%if "%( grep -w zh_CN <<< '%{KDE_LANGS}' )" != ""
%files Chinese
%defattr(-,root,root,-)
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/*
%lang(zh_CN) %{_datadir}/locale/zh_CN/charset
%lang(zh_CN) %{_docdir}/HTML/zh_CN/
%endif

%if "%( grep -w zh_TW <<< '%{KDE_LANGS}' )" != ""
%files Chinese-Big5
%defattr(-,root,root,-)
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/*
%lang(zh_TW) %{_datadir}/locale/zh_TW/charset
%lang(zh_TW) %{_docdir}/HTML/zh_TW/
%endif

%changelog
* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sun Dec 19 2010 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Initial version (French language only)
- Based on RHEL SPEC file 'kde-i18n'
- Add 'patch0' to reflect modifications in 'kdesu' from 'kdebase' package
- Import to GIT
