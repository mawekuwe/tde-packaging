# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

Name:			trinity-kdebluetooth
Version:		1.0_beta9_r769275
Release:		1%{?dist}%{?_variant}

Summary:		The TDE Bluetooth Framework

License:		GPLv2+
Group:			Applications/Communications
URL:			http://bluetooth.kmobiletools.org/

Source0:		kdebluetooth_1.0~beta9~r769275.orig.tar.gz
Patch0:			kdebluetooth-1.0_beta8-gcc43.patch
Patch1:			kdebluetooth_1.0~beta9~r769275-0ubuntu1.diff.gz
Patch2:			kdebluetooth-trinity.patch

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:	lockdev-devel
BuildRequires:	xmms-devel
BuildRequires:	bluez-libs-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdepim-devel
BuildRequires:	openobex-devel >= 1.1
BuildRequires:	libusb-devel
BuildRequires:	pkgconfig
Buildrequires:	libidn-devel
Buildrequires:	dbus-qt-devel
BuildRequires:	obexftp-devel
BuildRequires:	automake >= 1.6.1
BuildRequires:	autoconf >= 2.52
Requires:		%{name}-libs = %{version}-%{release}
Requires:		%{_bindir}/kdesu



%description
The KDE Bluetooth Framework is a set of tools built on top of Linux'
Bluetooth (Bluez) stack. The goal is to provide easy access to the most
common Bluetooth profiles and to make data exchange with Bluetooth
enabled devices as straightforward as possible.


%package libs
Summary: Base libraries for %{name}
Group:	 System Environment/Libraries
Obsoletes:		%{name} < %{version}-%{release}

%if 0%{?fedora} >= 8
Provides:		dbus-bluez-pin-helper
%endif


%description libs
KDE Bluetooth framework libraries.


%package devel
Summary: Development files for %{name}
Group:	 Development/Libraries
Requires: trinity-kdelibs-devel
Requires: bluez-libs-devel
Requires: %{name}-libs = %{version}-%{release}


%description devel
KDE Bluetooth framework development libraries and headers.


%prep
%setup -q -n kdebluetooth-1.0~beta9~r769275
%patch0 -p1
%patch1 -p1
%patch2 -p1

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
if [ -r "/usr/share/libtool/config/ltmain.sh" ]; then
  %__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
else
  %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
fi
%__make -f "admin/Makefile.common"


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"
export CXXFLAGS="-fpermissive"

unset QTDIR || : ; . /etc/profile.d/qt.sh
%configure \
	--with-bluetooth-libraries=%{_libdir}	\
	--disable-rpath							\
	--enable-new-ldflags					\
	--disable-debug							\
	--disable-dependency-tracking			\
	--enable-final							\
	--enable-closure						\
	--with-extra-includes=%{_includedir}/tqt

make %{?_smp_mflags} LIBTOOL=/usr/bin/libtool


%install
export PATH="%{_bindir}:${PATH}"
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

for DESK_PATH in applications/kde applnk/Utilities ; do
	desktop-file-install												\
		--mode=644														\
		--vendor=""														\
		--dir=$RPM_BUILD_ROOT%{_datadir}/applications/kde				\
		--remove-category="Network"										\
		--add-category="System"											\
		--delete-original												\
		$RPM_BUILD_ROOT%{_datadir}/$DESK_PATH/*.desktop ||:
done

touch %{name}.lang
PROG_LIST="kbluelock kbluemon kbluetooth kinputwizard
			kcm_btpaired  kio_bluetooth kio_obex2 kio_sdp
			libkbluetooth kdebluetooth"
for PROG in $PROG_LIST ; do
	%find_lang $PROG && cat $PROG.lang >> %{name}.lang	||:
done

rm -f $RPM_BUILD_ROOT/%{_datadir}/applnk/Settings/Network/Bluetooth/.directory

rm -f ${RPM_BUILD_ROOT}%{_libdir}/*.a
rm -f ${RPM_BUILD_ROOT}%{_libdir}/kde3/*.a

%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor 2> /dev/null ||:


%postun
/sbin/ldconfig
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor 2> /dev/null ||:


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL README
%{_bindir}/kblue*
%{_bindir}/kbtobexclient
%{_bindir}/kioobex_start
%{_bindir}/kinputwizard
%{_datadir}/applications/kde/*.desktop
%{_datadir}/applnk/.hidden/*.desktop
%{_datadir}/apps/konqsidebartng/virtual_folders/services/*.desktop
%{_datadir}/apps/*/*
%{_datadir}/autostart/*
%{_datadir}/desktop-directories/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mimelnk/bluetooth/
%{_datadir}/service*/*
%lang(ca) %{_docdir}/HTML/ca/kdebluetooth/
%lang(da) %{_docdir}/HTML/da/kdebluetooth/
%lang(en) %{_docdir}/HTML/en/kdebluetooth/
%lang(es) %{_docdir}/HTML/es/kdebluetooth/
%lang(et) %{_docdir}/HTML/et/kdebluetooth/
%lang(fr) %{_docdir}/HTML/fr/kdebluetooth/
%lang(it) %{_docdir}/HTML/it/kdebluetooth/
%lang(nl) %{_docdir}/HTML/nl/kdebluetooth/
%lang(pt) %{_docdir}/HTML/pt/kdebluetooth/
%lang(ru) %{_docdir}/HTML/ru/kdebluetooth/
%lang(sv) %{_docdir}/HTML/sv/kdebluetooth/


%files libs
%defattr(-,root,root,-)
%{_libdir}/*.la
%{_libdir}/*.so.*
%{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_libdir}/kdebluetooth/


%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Sun Feb 12 2012 Francois Andriot <francois.andriot@free.fr> - 1.0_beta9_r769275-1
- Initial version for TDE 3.5.13
- Updates base version to 1.0_beta9_r769275 (taken from Ubuntu Hardy)
- Fix autotools detection

* Tue Apr  1 2008 Rex Dieter <rdieter@fedoraproject.org> - 1.0-0.41.beta8
- -devel: Requires: kdelibs3-devel

* Sun Jan  6 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.40.beta8
- Fix build with gcc 4.3.

* Sun Dec  9 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.0-0.39.beta8
- Require kdesu in main package.

* Sun Dec 08 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.0-0.38.beta8
- BR: kdelibs3-devel kdepim3-devel
- drop Requires: kdebase (?)

* Wed Nov 08 2007 Gilboa Davara <gilboad[AT]gmail.com> 1.0-0.37.beta8
- Missing BR: automake, autoconf.

* Wed Nov 08 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-36.beta8
- Move BRs to main package to fix mock breakage.

* Wed Nov 07 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-35.beta8
- Fix multi-lib conflicts (#341731).

* Sat Oct 06 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-34.beta8
- Beta8. (First official release since beta3)
- Remove redundant beta3 patches.
- LANG support by Ville Skytta.
- Virtual provides: dbus-bluez-pin-helper.

* Sun Aug 26 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-33.beta3
- Re-Fix the license tag.

* Sun Aug 26 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-32.beta3
- Fixed license tag.
- Re-enable PPC64.

* Tue Jul 31 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-31.beta3
- Fix error in ExcludeArch.

* Tue Jul 31 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-30.beta3
- ExcludeArch ppc64 (obexftp, again)

* Mon Jul 30 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-29.beta3
- ExcludeArch ppc/ppc64 (obexftp missing.)

* Sun Jul 15 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-28.beta3
- Fix %%dist... again...

* Thu Jul 12 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-27.beta3
- Add missing touch /icon/hicolor.
- Menu items: Remove only-in-KDE.
- BR: Remove libutempter-devel.
- Fix project URL and source URL.
- Add missing %%dist.

* Sun Jul 08 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-26.beta3
- Remove the Nokia N70 patch. (Doesn't seem to work.)
- OBEX Object push fix.

* Sun Jul 08 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-25.beta3
- Adopted Ville Skyttä b2 patch to b3. (Hopefully) re-enable Nokia N7x obex support.
- Patch out "Configure services". (Disabled in B3)

* Mon Jun 25 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-24.beta3
- Added hex encoding patch by Thomas Davis.
- Removed --enable-irmcsynckonnector (deprecated in b3)
- Add missing docs. (Removed by mistake in b23)
- Known issue - services menu doesn't seem to work. (Requires debugging / upstream )

* Tue Jun 12 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0.0-23.beta3
- Beta3.
- Remove pin-helper. (No longer needed - beta3 has dbus support.)
- Added BR dbus-qt.
- Added BR obexftp-devel.
- Remove b2 patches.

* Sat May 26 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0-0.22.beta2
- Use the bluez_pinhelper wrapper instead of modified bluez-utils.
- Remove %%dist.
- *rc should not be marked as config.
- Prevent RPM from owning Network/Peripherals.

* Mon Apr 23 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0-0.21.beta2
- Patch list clean-up.
- Add Nokia obex detection patch.
- Fix 64bit compile due to bad default in configure. (with_bluetooth_dir)
- Missing BR: libtempter-devel.
- Missing BT: libidn-devel.
- Added: kbluepin wrapper - configure kbluepin as the old-style pin helper.

* Wed Apr 04 2007 Gilboa Davara <gilboad[AT]gmail.com> 1-0-0.20.beta2
- Re-merge Ville Skytta's latest .spec. (Got dropped by mistake)
- Summery, description clean-up.

* Thu Mar 29 2007 Gilboa Davara <gilboad[AT]gmail.com> 1.0-0.19.beta2
- Spec file clean-up.

* Fri Oct 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0-0.18.beta2
- BR: gettext
- include locales

* Tue Oct 17 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0-0.17.beta2
- kdebluetooth-1.0_beta2

* Fri Sep 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0-0.16.20060908svn
- kdebluetoooth-20060908svn

* Thu Jul 13 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0-0.15.20060621svn
- put svn at end of Release tag (per packaging guidelines)

* Wed Jun 21 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0-0.14.svn20060621
- kdebluetooth-20060621svn, fixes
	compile error kdebluetooth libkobex obex.h not found (kde bug #94572)

* Tue Jun 20 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0-0.13.svn20060620
- kdebluetooth-svn20060620, (re)fixes
	konqueror bluetooth:/ returns error "Bad URL" (kde bug #123607)
- --disable-dependency-tracking
- own %%_datadir/applnk/Settings/Network

* Mon Jun 19 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0-0.12.svn20060619
- document svn tarball creation
- Requires: kdebase (for kcm bits, applnk dir ownership)
- desktop-file-install --add-only-show-in=KDE

* Mon Jun 19 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0-0.11.svn20060619
- kdebluetooth-svn20060619, making most patches obsolete

* Fri Apr 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0-0.10.beta1
- -devel: Requires: qt-devel bluez-libs-devel
- include libirmcsynckonnector.so in main pkg
- .desktop: --remove-category=Network --add-category=System
- remove zero length files
- fix default hcid start/top command

* Mon Apr 17 2006 Rex Dieter <rexdieter[AT]users.sf.net> 1.0-0.9.beta1
- konqueror bluetooth:/ returns error "Bad URL" (kde bug #123607)

* Tue Mar 28 2006 Rex Dieter 1.0-0.8.beta1
- BR: kdepim-devel (for kitchensync)
- kdebluetooth-1.0_beta1-gcc41.patch

* Thu Mar 23 2006 Rex Dieter 1.0-0.7.beta1
- cleanup openobex patch
- fixup .desktop file(s)

* Wed Mar 22 2006 Rex Dieter 1.0-0.6.beta1
- cleanup for Extras
- %%post: ldconfig, fdo icon spec

* Mon Mar 06 2006 Rex Dieter 1.0-0.5.beta1
- respin

* Mon Mar 21 2005 Rex Dieter 1.0-0.3.beta1
- --enable-irmcsynckonnector

* Mon Mar 21 2005 Rex Dieter 1.0-0.1.beta1
- 1.0_beta1

* Wed Dec 29 2004 Rex Dieter <rexdieter[AT]users.sf.net> 0.0-0.1.cvs20050110
- first try

