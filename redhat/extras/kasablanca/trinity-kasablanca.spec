# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

%define kdecomp kasablanca
%define tde_docdir %{_docdir}/kde

Name:		trinity-%{kdecomp}
Summary:	Graphical FTP client
Version:	0.4.0.2
Release:	1%{?dist}

License:	GPLv2+
Url:		http://kasablanca.berlios.de/ 
Source:		http://download.berlios.de/kasablanca/kasablanca-%{version}.tar.gz
Group:		Applications/Internet 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch1:		kasablanca-0.4.0.2-dt.patch
Patch2:		kasablanca-autotools.patch
Patch3:		kasablanca-0.4.0.2-ftbfs.patch

BuildRequires: desktop-file-utils
BuildRequires: gettext 
BuildRequires: trinity-kdelibs-devel
BuildRequires: openssl-devel
BuildRequires: libutempter-devel

%description
Kasablanca is an ftp client, among its features are currently: 
* ftps encryption via AUTH TLS
* fxp (direct server to server transfer), supporting alternative mode.
* advanced bookmarking system.
* fast responsive multithreaded engine.
* concurrent connections to multiple hosts.
* interactive transfer queue, movable by drag and drop.
* small nifty features, like a skiplist.


%prep
%setup -q -n %{kdecomp}-%{version}
%patch1 -p1 -b .dt
%patch2 -p1
%patch3 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

## Needed(?) for older/legacy setups, harmless otherwise
if pkg-config openssl ; then
	export CPPFLAGS="$CPPFLAGS $(pkg-config --cflags-only-I openssl)"
fi

%configure \
	--disable-rpath \
	--disable-debug --disable-warnings \
	--disable-dependency-tracking --enable-final \
	--with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf $RPM_BUILD_ROOT 

%__make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications/kde \
  --vendor="" \
  --add-category="Network" \
  --add-category="KDE" \
  --delete-original \
  $RPM_BUILD_ROOT%{_datadir}/applnk/*/*.desktop

## File lists
# locale's
%find_lang %{kdecomp} || touch %{kdecomp}.lang
# HTML (1.0)
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d $RPM_BUILD_ROOT$HTML_DIR ]; then
for lang_dir in $RPM_BUILD_ROOT$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
    # replace absolute symlinks with relative ones
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && rm -f $i/common && ln -sf ../common $i/common
      done
    popd
  fi
done
fi


%clean
%__rm -rf $RPM_BUILD_ROOT 


%post
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/hicolor &> /dev/null
  gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README 
%{_bindir}/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/apps/kasablanca/
%{_datadir}/config*/*
%{_datadir}/icons/hicolor/*/*/*
%{tde_docdir}/HTML/en/kasablanca

%changelog
* Sun Dec 04 2011 Francois Andriot <francois.andriot@free.fr> - 0.4.0.2-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
- Based on Fedora 12 Spec 'kasablanca-0.4.0.2-17'
