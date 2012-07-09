# Default version for this component
%define kdecomp dolphin

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_datadir}/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:		trinity-%{kdecomp}
Summary:	File manager for TDE focusing on usability 
Version:	0.9.2
Release:	5%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext


%description
Dolphin focuses on being only a file manager.
This approach allows to optimize the user
interface for the task of file management.


%prep
%setup -q -n applications/%{kdecomp}

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

# TDE 3.5.12: dirty hack to prevent duplicate line in file 'd3lphin.desktop'
sed -i "%{buildroot}%{_datadir}/applications/kde/d3lphin.desktop" \
	-e "/^Name\[pa\].*/d"

desktop-file-install --vendor ""                \
    --delete-original                           \
    --dir %{buildroot}%{_datadir}/applications/ \
    %{buildroot}%{_datadir}/applications/kde/d3lphin.desktop


## File lists
# HTML (1.0)
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}$HTML_DIR ]; then
for lang_dir in %{buildroot}$HTML_DIR/* ; do
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

# Makes 'media_safelyremove.desktop' an alternative
%__mv -f %{buildroot}%{_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop %{buildroot}%{_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_d3lphin
%__ln_s /etc/alternatives/media_safelyremove.desktop_d3lphin %{buildroot}%{_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop

%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
alternatives --install \
  %{_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop \
  media_safelyremove.desktop_d3lphin \
  %{_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_d3lphin \
  10


%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
if [ $1 -eq 0 ]; then
  alternatives --remove \
    media_safelyremove.desktop_d3lphin \
    %{_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_d3lphin
fi


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/apps/*/
%doc %lang(en) %{tde_docdir}/HTML/en/*/
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/locale/*/*/d3lphin.mo


%Changelog
* Sun Jul 08 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.2-5
- Add alternatives with 'kio-umountwrapper'

* Tue May 01 2012 Francois Andriot <francois.andriot@free.fr> - 0.9.2-4
- Rebuild for Fedora 17
- Fix HTML installation directory

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.2-3
- Rebuilt for TDE 3.5.13 on RHEL 6, RHEL 5 and Fedora 15

* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.2-2
- Import to GIT

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.2-1
- Correct macro to install under "/opt", if desired

* Thu Jun 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.2-0
- Initial build for RHEL 6.0
- Based on FC7 'Dolphin 0.8.2-2" SPEC file.

