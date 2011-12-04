# Default version for this component
%define kdecomp smartcardauth
%define version 1.0
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
Summary:	SmartCard Login and LUKS Decrypt, Setup Utility
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/System

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Patch0:		smartcardauth-3.5.13-ftbfs.patch

BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils

#BuildRequires:	perl-PAR-Packer
Requires:		pcsc-perl

%description
This utility will allow you to set up your computer to accept a SmartCard as an authentication source for:
- Your encrypted LUKS partition
- TDE3.x, including automatic login, lock, and unlock features

It is designed to work with any ISO 7816-1,2,3,4 compliant smartcard
Examples of such cards are:
- The Schlumberger MultiFlex
- The ACS ACOS5 / ACOS6 series of cryptographic ISO 7816 cards

If a card is chosen that has PKSC support, such as the ACOS cards, this utility can run
simultaneously with the certificate reading program(s) to provide single sign on
in addition to the PKCS certificate functionality


%prep
unset QTDIR; . /etc/profile.d/qt.sh
%setup -q -n applications/%{kdecomp}
%patch0 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i "src/Makefile" \
	-e "s,/usr/include/tqt,%{_includedir}/tqt,g" \
	-e "s,/usr/include/qt3,${QTINC},g"

%__sed -i "Makefile" \
	-e "s|/usr/lib/perl5/Chipcard|/usr/lib64/perl5/vendor_perl/Chipcard|g"

%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

./build_ckpasswd


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}

%__install -D -m 755 scriptor_standalone.pl %{buildroot}%{_bindir}/scriptor.pl
%__install -D -m 755 src/ckpasswd %{buildroot}%{_bindir}/smartauthckpasswd
#%__install -D -m 755 src/ckpasswd %{buildroot}%{_bindir}/smartauthmon
%__ln_s smartauthckpasswd %{buildroot}%{_bindir}/smartauthmon
%__cp -Rp usr/*  %{buildroot}%{_prefix}

%__mkdir_p %{buildroot}%{_sysconfdir}
%__cp -Rp etc/* %{buildroot}%{_sysconfdir}


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :


%files
%defattr(-,root,root,-)
%doc gpl.txt
%{_sysconfdir}/init/smartauthlogin.conf
%{_sysconfdir}/smartauth/smartauth.sh.in
%{_sysconfdir}/smartauth/smartauthmon.sh.in
%{_bindir}/cryptosmartcard.sh
%{_bindir}/scriptor.pl
%{_bindir}/setupcard.sh
%{_bindir}/setupslavecard.sh
%{_bindir}/smartauth.sh
%{_bindir}/smartauthckpasswd
%{_bindir}/smartauthmon
%{_datadir}/applications/smartcardauth.desktop
%{_datadir}/applications/smartcardrestrict.desktop
%{_datadir}/icons/hicolor/16x16/apps/smartcardauth.png
%{_datadir}/icons/hicolor/32x32/apps/smartcardauth.png
%{_datadir}/initramfs-tools/hooks/cryptlukssc


%Changelog
* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 1.0-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

