# Default version for this component
%define kdecomp kio-umountwrapper

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
Summary:	progress dialog for safely removing devices in Trinity.
Version:	0.2
Release:	3%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://frode.kde.no/misc/kio_umountwrapper/

Prefix:		%{_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{kdecomp}-3.5.13.tar.gz
Source1:	media_safelyremove.desktop


BuildRequires: tqtinterface-devel
BuildRequires: trinity-kdelibs-devel
BuildRequires: trinity-kdebase-devel
BuildRequires: desktop-file-utils


%description
Wrapper around kio_media_mountwrapper.
Provides a progress dialog for Safely Removing of devices in Trinity.



%prep
unset QTDIR; . /etc/profile.d/qt.sh
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
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"

%configure \
	--disable-rpath \
    --with-extra-includes=%{_includedir}/tqt \
    --enable-closure

%__make %{?_smp_mflags}


%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}

%__install -D -m 644 %{SOURCE1} %{?buildroot}%{_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_kio-umountwrapper
#%__install -D -m 644 %{SOURCE1} %{?buildroot}%{_datadir}/apps/dolphin/servicemenus/media_safelyremove.desktop_kio-umountwrapper
%__install -D -m 644 %{SOURCE1} %{?buildroot}%{_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_kio-umountwrapper


%clean
%__rm -rf %{buildroot}

%post
for f in konqueror d3lphin; do
  alternatives --install \
    %{_datadir}/apps/${f}/servicemenus/media_safelyremove.desktop \
    media_safelyremove.desktop_${f} \
    %{_datadir}/apps/${f}/servicemenus/media_safelyremove.desktop_kio-umountwrapper \
    20
done

  
%postun
if [ $1 -eq 0 ]; then
  for f in konqueror d3lphin; do
    alternatives --remove \
      media_safelyremove.desktop_${f} \
      %{_datadir}/apps/${f}/servicemenus/media_safelyremove.desktop_kio-umountwrapper
  done
fi

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/kio_umountwrapper
%{_datadir}/apps/konqueror/servicemenus/media_safelyremove.desktop_kio-umountwrapper
#%{_datadir}/apps/dolphin/servicemenus/media_safelyremove.desktop_kio-umountwrapper
%{_datadir}/apps/d3lphin/servicemenus/media_safelyremove.desktop_kio-umountwrapper

%Changelog
* Sun Jul 08 2012 Francois Andriot <francois.andriot@free.fr> - 0.2-3
- Add 'desktop' file, to make this program useful :-)

* Wed May 02 2012 Francois Andriot <francois.andriot@free.fr> - 0.2-2
- Rebuilt for Fedora 17
- Removes post and postun

* Sat Dec 03 2011 Francois Andriot <francois.andriot@free.fr> - 0.2-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16

