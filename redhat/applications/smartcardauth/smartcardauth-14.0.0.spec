#
# spec file for package smartcardauth (version R14.0.0)
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
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%define tde_epoch 2
%define tde_version 14.0.0
%define tde_pkg smartcardauth
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
Version:	1.0
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}
Summary:	SmartCard Login and LUKS Decrypt, Setup Utility
Group:		Applications/System
URL:		http://www.trinitydesktop.org/

%if 0%{?suse_version}
License:	GPL-2.0+
%else
License:	GPLv2+
%endif

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	autoconf automake libtool m4
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	fdupes

# SUSE desktop files utility
%if 0%{?suse_version}
BuildRequires:	update-desktop-files
%endif

%if 0%{?opensuse_bs} && 0%{?suse_version}
# for xdg-menu script
BuildRequires:	brp-check-trinity
%endif

#BuildRequires:	perl-PAR-Packer
%if 0%{?mgaversion} || 0%{?mdkversion}
Requires:		perl-pcsc-perl
%endif
%if 0%{?rhel} || 0%{?fedora}
Requires:		pcsc-perl
%endif
%if 0%{?suse_version}
Requires:		perl-pcsc
%endif

# DB4/DB5 support
%if 0%{?rhel} || 0%{?fedora} || 0%{?suse_version} >= 1220 || 0%{?mdkversion} || 0%{?mgaversion}
%define with_db 1
%if 0%{?mgaversion} || 0%{?mdkversion}
%if 0%{?pclinuxos}
BuildRequires:  db4-devel
%else
BuildRequires:  db5-devel
%endif
%endif
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
BuildRequires:  libdb-devel
BuildRequires:  libdb-cxx-devel
%endif
%if 0%{?suse_version}
BuildRequires:  libdb-4_8-devel
%endif
%if 0%{?rhel} && 0%{?rhel} <= 6
BuildRequires:  db4-devel
%endif
%endif

# PAM support
BuildRequires:	pam-devel


%description
This utility will allow you to set up your computer to accept a SmartCard as an authentication source for:
- Your encrypted LUKS partition
- TDE, including automatic login, lock, and unlock features

It is designed to work with any ISO 7816-1,2,3,4 compliant smartcard
Examples of such cards are:
- The Schlumberger MultiFlex
- The ACS ACOS5 / ACOS6 series of cryptographic ISO 7816 cards

If a card is chosen that has PKSC support, such as the ACOS cards, this utility can run
simultaneously with the certificate reading program(s) to provide single sign on
in addition to the PKCS certificate functionality


##########

%if 0%{?pclinuxos} || 0%{?suse_version} && 0%{?opensuse_bs} == 0
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__sed -i "Makefile" \
	-e "s|/usr/lib/perl5/Chipcard|%{_libdir}/perl5/vendor_perl/Chipcard|g"


%build
export PATH="%{tde_bindir}:${PATH}"

export CFLAGS="${CXXFLAGS} ${RPM_OPT_FLAGS}"
export CXXFLAGS="${CXXFLAGS} ${RPM_OPT_FLAGS}"

./build_ckpasswd


%install
export PATH="%{tde_bindir}:${PATH}"
%__rm -rf %{buildroot}

%__install -D -m 755 scriptor_standalone.pl %{buildroot}%{tde_bindir}/scriptor.pl
%__install -D -m 755 src/ckpasswd %{buildroot}%{tde_bindir}/smartauthckpasswd
#%__install -D -m 755 src/ckpasswd %{buildroot}%{tde_bindir}/smartauthmon
%__ln_s smartauthckpasswd %{buildroot}%{tde_bindir}/smartauthmon
%__cp -Rp usr/*  %{buildroot}%{tde_prefix}

%__mkdir_p %{buildroot}%{_sysconfdir}
%__cp -Rp etc/* %{buildroot}%{_sysconfdir}

echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_datadir}/applications/smartcardauth.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_datadir}/applications/smartcardrestrict.desktop"


%clean
%__rm -rf %{buildroot}


%post
update-desktop-database %{tde_tdeappdir} > /dev/null
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun
update-desktop-database %{tde_tdeappdir} > /dev/null
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc gpl.txt
%{_sysconfdir}/init/smartauthlogin.conf
%{_sysconfdir}/smartauth/
%{tde_bindir}/cryptosmartcard.sh
%{tde_bindir}/scriptor.pl
%{tde_bindir}/setupcard.sh
%{tde_bindir}/setupslavecard.sh
%{tde_bindir}/smartauth.sh
%{tde_bindir}/smartauthckpasswd
%{tde_bindir}/smartauthmon
%{tde_datadir}/applications/smartcardauth.desktop
%{tde_datadir}/applications/smartcardrestrict.desktop
%{tde_datadir}/icons/hicolor/16x16/apps/smartcardauth.png
%{tde_datadir}/icons/hicolor/32x32/apps/smartcardauth.png
%{tde_datadir}/initramfs-tools/hooks/cryptlukssc


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2:1.0-1
- Initial release for TDE 14.0.0
