# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 3

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


Name:			trinity-kdeadmin
Summary:		Administrative tools for TDE
Version:		%{?version}
Release:		%{?release}%{?dist}%{?_variant}

License:		GPLv2
Group:			User Interface/Desktops
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.trinitydesktop.org/

Prefix:			%{_prefix}

Source0: kdeadmin-%{version}.tar.gz
Source1: kuser.pam
Source2: kuser.pamd
Source5: kpackagerc
Source6: ksysvrc
Source7: kuserrc

# [kdeadmin/knetworkconf] Add RHEL 5, RHEL 6, Fedora 15, Fedora 16
Patch0:		kdeadmin-3.5.13-add_rhel_fedora.patch

Requires: trinity-kdelibs
Requires: pkgconfig
Requires: usermode-gtk

BuildRequires: trinity-kdelibs-devel
BuildRequires: rpm-devel

%description
The kdeadmin package includes administrative tools for the K Desktop
Environment (KDE) including:
kcron, kdat, knetworkconf, kpackage, ksysv, kuser.


%prep
%setup -q -n kdeadmin
%patch0 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i admin/acinclude.m4.in \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g" \
  -e "s,kde_htmldir='.*',kde_htmldir='%{tde_docdir}/HTML',g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
   --enable-new-ldflags \
   --disable-dependency-tracking \
   --disable-rpath \
   --with-rpm \
   --enable-final \
   --enable-closure \
   --with-private-groups \
   --with-extra-includes=%{_includedir}/tqt

%__make %{?_smp_mflags}

%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

comps="kcron kdat knetworkconf kpackage ksysv kuser"
%__mkdir_p	%{buildroot}%{_datadir}/config \
			%{buildroot}/etc/security/console.apps \
			%{buildroot}/etc/pam.d \
			%{buildroot}%{_sbindir}

%__install -p -m644 %{SOURCE5} %{SOURCE6} %{SOURCE7} %{buildroot}%{_datadir}/config/

# Run kuser through consolehelper
%__install -p -m644 %{SOURCE1} %{buildroot}/etc/security/console.apps/kuser
%__install -p -m644 %{SOURCE2} %{buildroot}/etc/pam.d/kuser
%__mv %{buildroot}%{_bindir}/kuser %{buildroot}%{_sbindir}
%__ln_s consolehelper %{buildroot}%{_bindir}/kuser

# locale's
%find_lang %{name} || touch %{name}.lang
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}/$HTML_DIR ]; then
for lang_dir in %{buildroot}/$HTML_DIR/* ; do
  if [ -d $lang_dir ]; then
    lang=$(basename $lang_dir)
    echo "%lang($lang) $HTML_DIR/$lang/*" >> %{name}.lang
    # replace absolute symlinks with relative ones
    pushd $lang_dir
      for i in *; do
        [ -d $i -a -L $i/common ] && ln -nsf ../common $i/common
      done
    popd
  fi
done
fi

# rpmdocs
for dir in $comps ; do
  for file in AUTHORS ChangeLog README TODO ; do
    test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
  done
done

%post
for icon_theme in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${icon_theme} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${icon_theme} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :

%postun
for icon_theme in crystalsvg hicolor locolor ; do
  touch --no-create %{_datadir}/icons/${icon_theme} 2> /dev/null ||:
  gtk-update-icon-cache -q %{_datadir}/icons/${icon_theme} 2> /dev/null ||:
done
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :


%clean
%__rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%doc rpmdocs/*
%{_bindir}/*
%{_sbindir}/*
%config(noreplace) /etc/pam.d/*
%config(noreplace) /etc/security/console.apps/*
%{_datadir}/config*/*
%{_datadir}/mimelnk/*/*.desktop
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/apps/*
%{_datadir}/applications/kde/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*
%{_datadir}/service*/*.desktop
%{tde_libdir}/*
%{_libdir}/pkgconfig/*.pc


%changelog
* Wed Jan 11 2012 Francois Andriot <francois.andriot@free.fr> - 3.5.13-3
- Add knetworkconf support for RHEL 5, RHEL 6, Fedora 15, Fedora 16
- Remove 'consolehelper' macro
- Enables all kdeadmin components in RHEL (no more exclude some tools)
- Spec file cleanup

* Fri Nov 25 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-2
- Fix HTML directory location

* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Fri Oct 28 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT

