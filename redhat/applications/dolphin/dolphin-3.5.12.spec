# Default version for this component
%define kdecomp dolphin
%define version 0.9.2
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/kde3


Name:		trinity-%{kdecomp}
Summary:	File manager for KDE focusing on usability 
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Source0:	%{kdecomp}-3.5.12.tar.gz

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

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
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
%make_install

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
%doc AUTHORS ChangeLog COPYING TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/apps/*/
%{tde_docdir}/HTML/en/*/
%{_datadir}/icons/hicolor/128x128/apps/*.png
%{_datadir}/icons/hicolor/??x??/apps/*.png
%{_datadir}/locale/*/*/d3lphin.mo


%Changelog
* Tue Sep 14 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.2-2
- Import to GIT

* Mon Aug 22 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.2-1
- Correct macro to install under "/opt", if desired

* Thu Jun 30 2011 Francois Andriot <francois.andriot@free.fr> - 0.9.2-0
- Initial release for RHEL 6.0
- Based on FC7 'Dolphin 0.8.2-2" SPEC file.

