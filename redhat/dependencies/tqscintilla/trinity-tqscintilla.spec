# Default version for this component
%define kdecomp libtqscintilla
%define version 1.7.1
%define release 1

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

%global qtdir	%(qmake -query QT_INSTALL_PREFIX)
%global qtdata	%(qmake -query QT_INSTALL_DATA)
%global qtinc	%{qtdir}/include
%global qtlib	%{qtdir}/lib


Name:		%{kdecomp}
Summary:	TQt source code editing component based on Scintilla
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Development/Tools

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
Url:		http://www.riverbankcomputing.co.uk/qscintilla/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# This file is a GIT snapshot
Source0:	tqscintilla-master.tar.gz

# Fix FTBFS
Patch0:		tqscintilla-ftbfs.patch

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

%description
Scintilla is a free source code editing component. It has features found
in standard editing components, as well as features especially useful
when editing and debugging source code.

TQScintilla is a port or Scintilla to the TQt GUI toolkit.


%package designer
Summary:        TQScintilla designer plugin 
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}
Requires:       qt-designer
%description designer
%{summary}.

%package devel
Summary:        TQScintilla Development Files
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       qt-devel 
%description devel
%{summary}.

%package doc
Summary:        TQScintilla Documentation
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
%description doc
%{summary}.

%prep
%setup -q -n tqscintilla-master
%patch0 -p1

# Ugly hack to modify TQT include directory inside autoconf files.
# If TQT detection fails, it fallbacks to TQT4 instead of TQT3 !
%__sed -i */*.pro \
	-e "s|/usr/include/tqt|%{_includedir}/tqt|g"

( cd qt; qmake "DESTDIR=$PWD/../tmplib" )
( cd designer; qmake )


%build
unset QTDIR; . /etc/profile.d/qt.sh
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%__make %{?_smp_mflags} -C qt
%__make %{?_smp_mflags} -C designer


%install
%__rm -rf $RPM_BUILD_ROOT

# Installs the QT part
%__make INSTALL_ROOT=$RPM_BUILD_ROOT -C qt install

# Installs supplementary headers
for i in include/*.h; do
	%__install -D -m 644 $i %{buildroot}${QTINC}/private/${i##*/}
done

# Installs the HTML documentation
for i in doc/html/*; do
	%__install -D -m 644 $i %{buildroot}%{tde_docdir}/HTML/en/%{name}/${i##*/}
done

# Installs the Designer plugin
for i in designer/*.so; do
	%__install -D -m 644 $i %{buildroot}${QTDIR}/plugins/designer/${i##*/}
done

# Installs libraries
for i in tmplib/*; do 
	%__install -D $i %{buildroot}%{_libdir}/${i##*/}
done

%clean
%__rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE NEWS README
%{_libdir}/*.so.*
%{qtdir}/translations/*.qm

%files designer
%defattr(-,root,root,-)
%{qtdir}/plugins/designer/*.so

%files devel
%defattr(-,root,root,-)
%doc doc/html doc/Scintilla example
%{qtinc}/*.h
%{qtinc}/private/*.h
%{_libdir}/*.so

%files doc
%defattr(-,root,root,-)
%{tde_docdir}/HTML/en/%{name}

%changelog
* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 1.7.1-3
- respin (BuildID)

* Sat Aug 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 1.7.1-2
- License: GPLv2+

* Mon Dec 11 2006 Rex Dieter <rexdieter[AT]users.sf.net> - 1.7.1-1
- QScintilla-1.71-gpl-1.7.1

* Thu Nov 09 2006 Rex Dieter <rexdieter[AT]users.sf.net> - 1.7-1
- QScintilla1-1.71-gpl-1.7 (#214192)

* Sun Sep 03 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.6-3.3
- FC6 rebuild.
- Export flags.

* Mon Feb 13 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.6-3.2
- FC5 Rebuild.

* Tue Jan 31 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.6-3.1
- Rebuild for FC5.

* Wed Sep 14 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 1.6-3
- Fix permissions in prep, not in install.

* Tue Sep 13 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 1.6-2
- Fix permissions on doc files to be 0644.

* Sun Sep 11 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 1.6-1
- Update to 1.65-gpl-1.6
- Use the patch from Aurelien Bompard to build sanely in buildroot
- Include docs and examples for the -devel package

* Sat Aug 27 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 1.5.1-1
- Adapt for Fedora Extras
- Drop 0-Epoch
- Make specfile simpler
- Move .so to devel

* Mon Mar 09 2005 Rex Dieter 0:1.5.1-0.0.kde
- 1.5.1

* Thu Sep 16 2004 Rex Dieter <rexdieter at sf.net> 0:1.4-0.1.kde
- updated designer-incpath patch: don't require an already installed
  qscintilla-devel
- BuildConflicts: qscintilla-devel != %%version

* Thu Sep 16 2004 Rex Dieter <rexdieter at sf.net> 0:1.4-0.0.kde
- 1.4
- include designer plugin
- Prereq: %%qtdir

* Fri May 28 2004 Rex Dieter <rexdieter at sf.net> 0:1.3-0.fdr.0
- 1.3

* Thu Mar 11 2004 Rex Dieter <rexdieter at sf.net> 0:1.2-0.fdr.6
- dynamically determine version for qt dependancy.

* Wed Mar 10 2004 Rex Dieter <rexdieter at sf.net> 0:1.2-0.fdr.5
- (re)build against qt-3.3.1

* Wed Dec 03 2003 Rex Dieter <rexdieter at sf.net> 0:1.2-0.fdr.4
- remove extraneous macros
- (re)build against qt-3.2.3

* Mon Nov 10 2003 Rex Dieter <rexdieter at sf.net> 0:1.2-0.fdr.3
- (re)build against qt-3.2.2

* Wed Sep 17 2003 Rex Dieter <rexdieter at sf.net> 0:1.2-0.fdr.2
- use Epoch's in Requires

* Tue Aug 19 2003 Rex Dieter <rexdieter at sf.net> 0:1.2-0.fdr.1
- 1.2

