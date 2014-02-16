# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
bakus/abakus-14.0.0.spec
%if "%{?tde_prefix}" != "/usr"
bakus/abakus-14.0.0.spec
%define _variant .opt
bakus/abakus-14.0.0.spec
%endif
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
# TDE 3.5.13 specific building variables
bakus/abakus-14.0.0.spec
%define tde_bindir %{tde_prefix}/bin
bakus/abakus-14.0.0.spec
%define tde_datadir %{tde_prefix}/share
bakus/abakus-14.0.0.spec
%define tde_docdir %{tde_datadir}/doc
bakus/abakus-14.0.0.spec
%define tde_includedir %{tde_prefix}/include
bakus/abakus-14.0.0.spec
%define tde_libdir %{tde_prefix}/%{_lib}
bakus/abakus-14.0.0.spec
%define tde_mandir %{tde_datadir}/man
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%define tde_tdeappdir %{tde_datadir}/applications/kde
bakus/abakus-14.0.0.spec
%define tde_tdedocdir %{tde_docdir}/tde
bakus/abakus-14.0.0.spec
%define tde_tdeincludedir %{tde_includedir}/tde
bakus/abakus-14.0.0.spec
%define tde_tdelibdir %{tde_libdir}/trinity
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%define _docdir %{tde_docdir}
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
Name:           trinity-knoda
bakus/abakus-14.0.0.spec
Version:        0.8.3
bakus/abakus-14.0.0.spec
Release:        1%{?dist}%{?_variant}
bakus/abakus-14.0.0.spec
Summary:        A database frontend for TDE.
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
Group:          Applications/Productivity
bakus/abakus-14.0.0.spec
License:        GPLv2+
bakus/abakus-14.0.0.spec
URL:            http://sourceforge.net/projects/knoda/
bakus/abakus-14.0.0.spec
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
Source0:        http://downloads.sourceforge.net/project/knoda/knoda/0.8.3/knoda-0.8.3.tar.bz2
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
Patch1:			knoda-0.8.3-trinity.patch
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
BuildRequires:	desktop-file-utils
bakus/abakus-14.0.0.spec
BuildRequires:	trinity-tdelibs-devel
bakus/abakus-14.0.0.spec
BuildRequires:	hk_classes-devel
bakus/abakus-14.0.0.spec
Requires:		hk_classes
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%description
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%package devel
bakus/abakus-14.0.0.spec
Summary:  	Development files for %{name}
bakus/abakus-14.0.0.spec
Group: 		Development/Libraries
bakus/abakus-14.0.0.spec
Requires: 	%{name} = %{version}-%{release}
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%description devel
bakus/abakus-14.0.0.spec
%{summary}
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%if 0%{?suse_version}
bakus/abakus-14.0.0.spec
%debug_package
bakus/abakus-14.0.0.spec
%endif
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%prep
bakus/abakus-14.0.0.spec
%setup -q -n knoda-%{version}
bakus/abakus-14.0.0.spec
%patch1 -p1 -b .trinity
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
# Ugly hack to modify TQT include directory inside autoconf files.
bakus/abakus-14.0.0.spec
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
bakus/abakus-14.0.0.spec
%__sed -i admin/acinclude.m4.in \
bakus/abakus-14.0.0.spec
  -e "s|/usr/include/tqt|%{tde_includedir}/tqt|g" \
bakus/abakus-14.0.0.spec
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_tdedocdir}/HTML'|g"
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
bakus/abakus-14.0.0.spec
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
bakus/abakus-14.0.0.spec
%__make -f "admin/Makefile.common"
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%build
bakus/abakus-14.0.0.spec
unset QTDIR; . /etc/profile.d/qt3.sh
bakus/abakus-14.0.0.spec
export PATH="%{tde_bindir}:${PATH}"
bakus/abakus-14.0.0.spec
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
export KDEDIR="%{tde_prefix}"
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%configure \
bakus/abakus-14.0.0.spec
	--prefix=%{tde_prefix} \
bakus/abakus-14.0.0.spec
	--exec-prefix=%{tde_prefix} \
bakus/abakus-14.0.0.spec
	--disable-dependency-tracking \
bakus/abakus-14.0.0.spec
	--disable-rpath \
bakus/abakus-14.0.0.spec
	--with-extra-includes=%{tde_includedir}/tqt \
bakus/abakus-14.0.0.spec
	--with-qt-libraries=${QTLIB:-${QTDIR}/%{_lib}} \
bakus/abakus-14.0.0.spec
	--bindir=%{tde_bindir} \
bakus/abakus-14.0.0.spec
	--libdir=%{tde_libdir} \
bakus/abakus-14.0.0.spec
	--datadir=%{tde_datadir} \
bakus/abakus-14.0.0.spec
	--includedir=%{tde_tdeincludedir} 
bakus/abakus-14.0.0.spec
  
bakus/abakus-14.0.0.spec
%__make %{?_smp_mflags} LIBTOOL=$(which libtool)
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%install
bakus/abakus-14.0.0.spec
%__rm -rf $RPM_BUILD_ROOT
bakus/abakus-14.0.0.spec
%__make install DESTDIR=$RPM_BUILD_ROOT
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
# Useless files ..
bakus/abakus-14.0.0.spec
%__rm -f %{?buildroot}%{tde_libdir}/*.a
bakus/abakus-14.0.0.spec
%__rm -f %{?buildroot}%{tde_tdelibdir}/*.a
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%find_lang knoda
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%clean
bakus/abakus-14.0.0.spec
%__rm -rf $RPM_BUILD_ROOT
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%post
bakus/abakus-14.0.0.spec
for i in hicolor locolor ; do
bakus/abakus-14.0.0.spec
 touch --no-create %{tde_datadir}/icons/$i 2>/dev/null || :
bakus/abakus-14.0.0.spec
 gtk-update-icon-cache --quiet %{tde_datadir}/icons/$i 2>/dev/null || :
bakus/abakus-14.0.0.spec
done
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%postun
bakus/abakus-14.0.0.spec
for i in hicolor locolor ; do
bakus/abakus-14.0.0.spec
 touch --no-create %{tde_datadir}/icons/$i 2>/dev/null || :
bakus/abakus-14.0.0.spec
 gtk-update-icon-cache --quiet %{tde_datadir}/icons/$i 2>/dev/null || :
bakus/abakus-14.0.0.spec
done
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%files -f knoda.lang
bakus/abakus-14.0.0.spec
%defattr(-,root,root,-)
bakus/abakus-14.0.0.spec
%doc AUTHORS COPYING README ChangeLog
bakus/abakus-14.0.0.spec
%{tde_bindir}/knoda
bakus/abakus-14.0.0.spec
%{tde_bindir}/knoda-rt
bakus/abakus-14.0.0.spec
%{tde_libdir}/libhk_kdeclasses.la
bakus/abakus-14.0.0.spec
%{tde_libdir}/libhk_kdeclasses.so
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdedbdesignerpart.la
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdedbdesignerpart.so
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdeformpart.la
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdeformpart.so
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdegridpart.la
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdegridpart.so
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdemodulepart.la
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdemodulepart.so
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdeqbepart.la
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdeqbepart.so
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdequerypart.la
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdequerypart.so
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdereportpart.la
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdereportpart.so
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdetablepart.la
bakus/abakus-14.0.0.spec
%{tde_tdelibdir}/libhk_kdetablepart.so
bakus/abakus-14.0.0.spec
%{tde_datadir}/applnk/Office/knoda.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/apps/hk_kdeclasses/
bakus/abakus-14.0.0.spec
%{tde_datadir}/apps/knoda/
bakus/abakus-14.0.0.spec
%{tde_datadir}/config/magic/hk_classes.magic
bakus/abakus-14.0.0.spec
%{tde_tdedocdir}/HTML/en/knoda/
bakus/abakus-14.0.0.spec
%{tde_datadir}/icons/hicolor/*/apps/knoda.png
bakus/abakus-14.0.0.spec
%{tde_datadir}/icons/locolor/*/apps/knoda.png
bakus/abakus-14.0.0.spec
%{tde_datadir}/mimelnk/application/x-hk_classes-sqlite2.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/mimelnk/application/x-hk_classes-sqlite3.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/mimelnk/application/x-hk_connection.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/mimelnk/application/x-paradox.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/mimelnk/application/x-xbase.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/services/hk_kdedbdesignerpart.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/services/hk_kdeformpart.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/services/hk_kdegridpart.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/services/hk_kdemodulepart.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/services/hk_kdeqbepart.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/services/hk_kdequerypart.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/services/hk_kdereportpart.desktop
bakus/abakus-14.0.0.spec
%{tde_datadir}/services/hk_kdetablepart.desktop
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%files devel
bakus/abakus-14.0.0.spec
%defattr(-,root,root,-)
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeboolean.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdebutton.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdecolumn.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdecombobox.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdecsvexportdialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdecsvimportdialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdecsvimportdialogbase.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdedatasource.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdedate.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdedbdesignerpart.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdedbdesignerpartfactory.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdedblistview.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdedriverdialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdefilterdialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdefilterdialogbase.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdefinddialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdefinddialogbase.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeform.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeformdatasourcedialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeformdatasourcedialogbase.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeformfocus.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeformpart.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeformpartfactory.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeformpartwidget.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdegrid.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdegridcolumndialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdegridcolumndialogbase.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdegridpart.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdegridpartfactory.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeimage.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeindexeditwindow.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeinterpreterdialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdelabel.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdelineedit.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdememo.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdemessages.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdemodule.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdemodulepart.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdemodulepartfactory.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdenewpassworddialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdenewpassworddialogbase.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdepassworddialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeproperty.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdepropertybase.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeqbe.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeqbepart.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdeqbepartfactory.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdequery.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdequerypart.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdequerypartfactory.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdequerypartwidget.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdereport.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdereportdata.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdereportpart.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdereportpartfactory.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdereportpartwidget.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdereportproperty.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdereportpropertybase.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdereportsection.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdereportsectiondialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdereportsectiondialogbase.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kderowselector.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdesimpleform.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdesimplegrid.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdesimplereport.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdesubform.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdesubreportdialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdesubreportdialogbase.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdetable.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdetabledesign.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdetablepart.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdetablepartfactory.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdetablepartwidget.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdetoolbar.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdexmlexportdialog.h
bakus/abakus-14.0.0.spec
%{tde_tdeincludedir}/hk_kdexmlexportdialogbase.h
bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec

bakus/abakus-14.0.0.spec
%changelog
bakus/abakus-14.0.0.spec
* Mon Apr 08 2013 Francois Andriot <francois.andriot@free.fr> - 0.5b-1
bakus/abakus-14.0.0.spec
- Initial release for TDE 3.5.13.2
bakus/abakus-14.0.0.spec
