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

# TDE 3.5.12 specific building variables
BuildRequires: autoconf automake libtool m4
%define tde_docdir %{_docdir}/kde
%define tde_includedir %{_includedir}/kde
%define tde_libdir %{_libdir}/trinity


Name:    trinity-kdeedu
Summary: Educational/Edutainment applications
Version: %{?version}
Release: %{?release}%{?dist}%{?_variant}

License: GPLv2
Group:   Amusements/Games

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: kdeedu-%{version}.tar.gz

Provides: kdeedu3 = %{version}-%{release}

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Requires: %{name}-libs = %{version}-%{release}

BuildRequires: desktop-file-utils
BuildRequires: trinity-kdelibs-devel
BuildRequires: python-devel python
BuildRequires: boost-devel
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
BuildRequires: ocaml(compiler)
%else
BuildRequires: ocaml
%endif
#BuildRequires: ocaml-facile-devel


%description
Educational/Edutainment applications, including:
* blinken: Simon Says Game
* kalzium: Periodic Table of Elements
* kanagram: Letter Order Game
* kbruch: Exercise Fractions
* keduca: Tests and Exams
* kgeography: Geography Trainer
* khangman: Hangman Game
* kig: Interactive Geometry
* kiten: Japanese Reference/Study Tool
* klatin: Latin Reviser
* klettres: French alphabet tutor
* kmplot: Mathematical Function Plotter
* kpercentage: Excersie Percentages
* kstars: Desktop Planetarium
* ktouch: Touch Typing Tutor
* kturtle: Logo Programming Environment
* kverbos: Study Spanish Verbforms
* kvoctrain: Vocabulary Trainer
* kwordquiz: Vocabulary Trainer

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Provides: kdeedu3-devel = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
%description devel
%{summary}.

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-kdelibs
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%setup -q -n kdeedu

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
sed -i admin/acinclude.m4.in \
  -e "s,/usr/include/tqt,%{_includedir}/tqt,g"

%if 0%{?rhel} > 0
rm -rf doc/kgeography kgeography
perl -pi -e "s|kgeography||" subdirs
%endif

%__cp "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh"
%__make -f "admin/Makefile.common"


%build
unset QTDIR || : ; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

# Fix link with kparts
export CXXFLAGS="${CXXFLAGS} -lkparts"

%if 0%{?fedora}
export CXXFLAGS="${CXXFLAGS} -fpermissive"
%endif

%configure \
   --enable-new-ldflags \
   --disable-dependency-tracking \
   --disable-rpath \
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 15
   --enable-kig-python-scripting \
%else
   --disable-kig-python-scripting \
%endif
   --disable-debug \
   --disable-warnings \
   --enable-final \
   --enable-closure \
   --includedir=%{_includedir}/kde \
   --disable-ocamlsolver \
   --with-extra-includes=%{_includedir}/tqt


%__make \
  OCAMLLIB=$(ocamlc -where) FACILELIB=$(ocamlc -where)


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

# locale's
%find_lang %{name} || touch %{name}.lang
HTML_DIR=$(kde-config --expandvars --install html)
if [ -d %{buildroot}$HTML_DIR ]; then
for lang_dir in %{buildroot}$HTML_DIR/* ; do
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
for dir in blinken k* ; do
  for file in AUTHORS ChangeLog README TODO ; do
    test -s  "$dir/$file" && install -p -m644 -D "$dir/$file" "rpmdocs/$dir/$file"
  done
done


%clean
%__rm -rf %{buildroot}


%post
for i in crystalsvg hicolor locolor ; do
 touch --no-create %{_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{_datadir}/icons/$i 2>/dev/null || :
done
update-desktop-database >& /dev/null ||:

%postun
for i in crystalsvg hicolor locolor ; do
 touch --no-create %{_datadir}/icons/$i 2>/dev/null || :
 gtk-update-icon-cache --quiet %{_datadir}/icons/$i 2>/dev/null || :
done
update-desktop-database >& /dev/null ||:

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README COPYING
%doc rpmdocs/*
%{_bindir}/*
%{_datadir}/applications/kde/*
# FIXME
%{_datadir}/applnk/Edutainment/
%{_datadir}/apps/*
%config %{_datadir}/config*/*
%{_datadir}/mimelnk/*/*
%{_datadir}/icons/crystalsvg/*/*/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/icons/locolor/*/*/*
%{_datadir}/services/*
%{tde_libdir}/*
%doc %lang(en) %{_docdir}/HTML/en/*

%files libs
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*
%{_libdir}/lib*.la

%files devel
%defattr(-,root,root,-)
%doc libkdeedu/AUTHORS libkdeedu/README
%{tde_includedir}/*
%{_libdir}/lib*.so


%changelog
* Sun Oct 30 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-1
- Initial release for RHEL 6, RHEL 5 and Fedora 15

* Sat Sep 09 2011 Francois Andriot <francois.andriot@free.fr> - 3.5.13-0
- Import to GIT
