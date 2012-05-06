# Default version for this component
%define kdecomp piklab
%define version 0.15.2
%define release 3

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%define _mandir %{_datadir}/man
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	IDE for PIC-microcontroller development [Trinity]
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

# [piklab] Fix compilation with GCC 4.7 [Bug #958]
Patch1:		piklab-3.5.13-fix_gcc47_compilation.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	readline-devel

%description
Piklab is an integrated development environment for applications based on
Microchip PIC and dsPIC microcontrollers similar to the MPLAB environment.

Support for several compiler and assembler toolchains is integrated. The
GPSim simulator, the ICD1 programmer, the ICD2 debugger, the PICkit1 and
PICkit2 programmers, the PicStart+ programmer, and most direct programmers
are supported. A command-line programmer and debugger are also available.


%prep
%setup -q -n applications/%{kdecomp}
%patch1 -p1

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
    --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# Incorrect extension on manpage
%__mv -f %{buildroot}%{_mandir}/man1/piklab.1x %{buildroot}%{_mandir}/man1/piklab.1

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
%{_bindir}/piklab
%{_bindir}/piklab-coff
%{_bindir}/piklab-hex
%{_bindir}/piklab-prog
%{_datadir}/applications/kde/piklab.desktop
%{_datadir}/apps/katepart/syntax/asm-pic.xml
%{_datadir}/apps/katepart/syntax/coff-c-pic.xml
%{_datadir}/apps/katepart/syntax/coff-pic.xml
%{_datadir}/apps/katepart/syntax/jal-pic.xml
%{_datadir}/apps/piklab
%{tde_docdir}/HTML/en/piklab
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/mimelnk/application/x-piklab.desktop
%{_mandir}/man1/piklab-coff.1
%{_mandir}/man1/piklab-hex.1
%{_mandir}/man1/piklab-prog.1
%{_mandir}/man1/piklab.1


%Changelog
* Sun Apr 06 2012 Francois Andriot <francois.andriot@free.fr> - 0.15.2-3
- Fix MAN directory location
- Fix compilation with GCC 4.7 [Bug #958]

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 0.15.2-2
- Fix HTML directory location

* Thu Nov 24 2011 Francois Andriot <francois.andriot@free.fr> - 0.15.2-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
