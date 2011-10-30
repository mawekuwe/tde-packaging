# Default version for this component
%if "%{?version}" == ""
%define version 3.5.13
%endif
%define release 1

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?_prefix}" != "/usr"
%define _variant .opt
%define _docdir %{_prefix}/share/doc
%endif

# TDE 3.5.13 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_libdir %{_libdir}/trinity
%define tde_includedir %{_includedir}/kde


Name:	 trinity-kdebindings
Summary: TDE bindings to non-C++ languages
Version: %{?version}
Release: %{?release}%{?dist}%{_variant}

License: GPLv2
Group:   User Interface/Desktops

Vendor:  Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: kdebindings-%{version}.tar.gz

# RedHat Legacy patches (from Fedora)
Patch1: kdebindings-3.5.6-libgcj.patch

BuildRequires: desktop-file-utils
BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: zlib-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: trinity-arts-devel
BuildRequires: glib-devel gtk+-devel
BuildRequires: gtk2-devel
%define perl_ver        %{expand:%%(eval `perl -V:version`; echo $version)}
%define perl_vendorarch %{expand:%%(eval `perl -V:installvendorarch`; echo $installvendorarch)}
%define perl_vendorlib  %{expand:%%(eval `perl -V:installvendorlib`; echo $installvendorlib)}
%define perl_man3dir    %{expand:%%(eval `perl -V:installman3dir`; echo $installman3dir)}

Requires: trinity-kdelibs
Requires: trinity-kdebase
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%define python_ver %{expand:%%(%{__python} -c "import sys ; print sys.version[:3]")}
%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

## dcoppython
BuildRequires: python-devel
Provides: %{name}-dcoppython = %{version}-%{release}

## ruby
BuildRequires: ruby-devel >= 1.8, ruby
Provides: %{name}-ruby = %{version}-%{release}
%{!?ruby_arch: %define ruby_arch %(ruby -rrbconfig -e 'puts Config::CONFIG["archdir"]')}
%{!?ruby_sitelib: %define ruby_sitelib %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}
%{!?ruby_sitearch: %define ruby_sitearch %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')}

## java
%if 0%{?rhel} && 0%{?rhel} < 6
BuildRequires: java-1.4.2-gcj-compat-devel libgcj-devel gcc-java
%else
BuildRequires: java-devel >= 1.4.2
%endif
%define java_home %{_usr}/lib/jvm/java
%define _with_java --with-java=%{java_home}
Provides: %{name}-java = %{version}-%{release}

%description
KDE/DCOP bindings to non-C++ languages

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: trinity-kdelibs-devel 
%description devel
Development files for the KDE bindings.

## dcopperl
%package dcopperl
Summary: DCOP Bindings for Perl 
Group:   Development/Libraries
%description dcopperl
Perl bindings to the DCOP interprocess communication protocol used by KDE


%prep
%setup -q -n kdebindings
%patch1 -p1 -b .libgcj

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
sed -i admin/acinclude.m4.in \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g"

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f admin/Makefile.common


%build
unset QTDIR || : ; source /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

unset JAVA_HOME ||:
%{?java_home:JAVA_HOME=%{java_home}; export JAVA_HOME}

# sip/PyQt/PyKDE built separately, not here
export DO_NOT_COMPILE="$DO_NOT_COMPILE python"

%configure \
  --includedir=%{tde_includedir} \
  --disable-rpath \
  --enable-new-ldflags \
  --disable-debug --disable-warnings \
  --disable-dependency-tracking \
  --with-extra-libs=%{_libdir} \
  --with-pythondir=%{_usr} \
  --enable-closure \
  --disable-final \
  %{?_with_java} %{!?_with_java:--without-java} \
  %{?_enable_qscintilla} %{!?_enable_qscintilla:--disable-qscintilla} \
  --with-extra-includes=%{_includedir}/tqt


pushd dcopperl
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL INSTALLDIRS=vendor

# Ugly hack to add TQT include directory in Makefile
sed -i Makefile \
  -e "s,^\(INC = .*\),\1 -I%{_includedir}/tqt,"

%__make OPTIMIZE="$RPM_OPT_FLAGS" ||:
popd

# smoke/ not smp-safe
%__make -C smoke

# The rest is smp-safe
%__make %{?_smp_mflags} PYTHON=%{__python}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf $RPM_BUILD_ROOT

%__make install DESTDIR=%{?buildroot} \
  PYTHON=%{__python}

desktop-file-install \
  --vendor="" \
  --add-category="Qt" \
  --add-category="KDE" \
  --add-category="Utility" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications/kde \
  $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/*.desktop ||:

## File lists
# perl
find $RPM_BUILD_ROOT -type f -a \( -name perllocal.pod -o -name .packlist \
  -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'

find $RPM_BUILD_ROOT%{perl_vendorarch} -type f -print | \
        sed "s@^$RPM_BUILD_ROOT@@g" >> %{name}-dcopperl.list
find $RPM_BUILD_ROOT%{perl_vendorlib} -type f -print | \
        sed "s@^$RPM_BUILD_ROOT@@g" >> %{name}-dcopperl.list
if [ "$(cat %{name}-dcopperl.list)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"; exit 1
fi

# locale's
%find_lang %{name} || touch %{name}.lang
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d $RPM_BUILD_ROOT$HTML_DIR ]; then
for lang_dir in $RPM_BUILD_ROOT$HTML_DIR/* ; do
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
for dir in dcopperl dcoppython kalyptus %{?_with_java:kdejava qtjava} kjsembed korundum qtruby qtsharp smoke; do
  for file in AUTHORS ChangeLog README TODO ; do
    test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
  done
done

%clean
%__rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig ||:
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database >& /dev/null ||:

%postun
/sbin/ldconfig ||:
touch --no-create %{_datadir}/icons/hicolor ||:
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2> /dev/null ||:
update-desktop-database >& /dev/null ||:


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%doc rpmdocs/*
%{_bindir}/*
%{tde_libdir}/*
%{_libdir}/lib*.la
%{_libdir}/lib*.so.*
%{_datadir}/appl*/*/*.desktop
%{_datadir}/apps/embedjs/
%{_datadir}/apps/kate/scripts/*
%{_datadir}/apps/kjsembed/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/service*/*.desktop
%{_mandir}/man1/*
%{python_sitearch}/*
#%{_libdir}/python%{python_ver}/*.py*
%if "%{?_with_java:1}" == "1"
%{_libdir}/java
%{_libdir}/jni/*.so.*
%endif
#%{ruby_sitearch}/*
#%{ruby_sitelib}/K*
#%{ruby_sitelib}/Qt*
%{_usr}/lib/ruby/*/*
%{ruby_arch}/*.so.*
%doc %lang(en) %{_docdir}/HTML/en/javalib/*

# Excludes 'kjscmd' (conflicts with 'kdelibs' from RHEL6)
%if "%{?_prefix}" == "/usr"
%exclude %{_bindir}/kjscmd
%endif
%exclude %{_mandir}/man1/kjscmd*


%files dcopperl -f %{name}-dcopperl.list
%defattr(-,root,root,-)
%doc dcopperl/AUTHORS dcopperl/Changes dcopperl/README dcopperl/TODO
%{perl_man3dir}/DCOP.3pm.gz

%files devel
%defattr(-,root,root,-)
%{tde_includedir}/*
%{_libdir}/lib*.so
%if "%{?_with_java:1}" == "1"
%{_libdir}/jni/*.so
%{_libdir}/jni/*.la
%endif
%{ruby_arch}/*.so
%{ruby_arch}/*.la

%changelog
* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sat Sep 03 2011 Francois Andriot <francois.andriot@free.fr - 3.5.13-0
- Import to GIT
- Built with future TDE version (3.5.13 + cmake + QT3.3.8d)
