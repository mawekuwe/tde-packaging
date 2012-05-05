# Default version for this component
%define kdecomp kiosktool
%define version 1.0
%define release 2

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
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}
Summary:	tool to configure the TDE kiosk framework

License:	GPLv2+
Group:		Applications/Multimedia

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/


Source0: %{kdecomp}-3.5.13.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gettext
BuildRequires: trinity-kdelibs-devel


%description
A Point&Click tool for system administrators to enable 
TDE's KIOSK features or otherwise preconfigure TDE for 
groups of users.


%prep
%setup -q -n applications/%{kdecomp}

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s|/usr/include/tqt|%{_includedir}/tqt|g" \
  -e "s|kde_htmldir='.*'|kde_htmldir='%{tde_docdir}/HTML'|g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"


%configure \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking --enable-final \
  --enable-closure \
  --with-extra-includes=%{_includedir}/tqt
  

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

## File lists
# locale's
%find_lang %{kdecomp}
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
touch --no-create %{_datadir}/icons/crystalsvg ||:
gtk-update-icon-cache -q %{_datadir}/icons/crystalsvg 2> /dev/null ||:
update-desktop-database >& /dev/null ||:

%postun
touch --no-create %{_datadir}/icons/crystalsvg ||:
gtk-update-icon-cache -q %{_datadir}/icons/crystalsvg 2> /dev/null ||:
update-desktop-database >& /dev/null ||:



%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%doc ChangeLog COPYING README TODO
%{_bindir}/kiosktool
%{_bindir}/kiosktool-kdedirs
%{_datadir}/applications/kde/kiosktool.desktop
%{_datadir}/apps/kiosktool/*.png
%{tde_docdir}/HTML/en/kiosktool/
%{_datadir}/icons/crystalsvg/*/apps/kiosktool.png
%{_datadir}/apps/kiosktool/kiosk_data.xml
%{_datadir}/apps/kiosktool/kiosktoolui.rc

%Changelog
* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 1.0-2
- Rebuilt for Fedora 17
- Fix post and postun

* Sat Nov 19 2011 Francois Andriot <francois.andriot@free.fr> - 1.0-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
