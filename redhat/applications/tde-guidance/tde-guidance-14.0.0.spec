# Default version for this component
%define tde_pkg tde-guidance
%define tde_version 14.0.0

# REMOVE KDELIBS4-DEVEL before building !!!!

%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_appdir %{tde_datadir}/applications

%define tde_tdeappdir %{tde_appdir}/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

%define __arch_install_post %{nil}

Name:			trinity-%{tde_pkg}
Summary:		A collection of system administration tools for Trinity
Version:		0.8.0svn20080103
Release:		%{?!preversion:8}%{?preversion:7_%{preversion}}%{?dist}%{?_variant}

License:		GPLv2+
Group:			Applications/Utilities

Vendor:			Trinity Project
Packager:		Francois Andriot <francois.andriot@free.fr>
URL:			http://www.simonzone.com/software/guidance

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	trinity-pytdeextensions
BuildRequires:	trinity-libpythonize0-devel
BuildRequires:	trinity-python-trinity
BuildRequires:	chrpath
BuildRequires:	gcc-c++

# SIP support
BuildRequires:	sip4-tqt-devel >= 4.10.5
Requires:		sip4-tqt >= 4.10.5

# PYTHON-QT support
BuildRequires:	python-tqt-devel
BuildRequires:	trinity-python-trinity-devel
BuildRequires:	trinity-pytqt-tools

Requires:		python-tqt
Requires:		trinity-python-trinity
Requires:		trinity-pytdeextensions
Requires:		python
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
Requires:		hwdata
%endif

Requires:		%{name}-backends = %{version}-%{release}

# POWERMANAGER support (requires HAL)
#define with_powermanager 1

Obsoletes:		trinity-guidance < %{version}-%{release}
Provides:		trinity-guidance = %{version}-%{release}

%description
Guidance currently consists of four programs designed to help you
look after your system:
 o  userconfig - User and Group administration
 o  serviceconfig - Service/daemon administration
 o  mountconfig - Disk and filesystem administration
 o  wineconfig - Wine configuration

These tools are available in Trinity Control Center, System Settings 
or can be run as standalone applications.

%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING README TODO
%{tde_bindir}/grubconfig
%{tde_bindir}/mountconfig
%{tde_bindir}/serviceconfig
%{tde_bindir}/userconfig
%{tde_bindir}/wineconfig
%attr(0644,root,root) %{tde_tdelibdir}/*.so
%attr(0644,root,root) %{tde_tdelibdir}/*.la
%{tde_datadir}/apps/guidance/
%{tde_tdeappdir}/*.desktop
%{tde_datadir}/icons/crystalsvg/*/*/*.png
%{tde_datadir}/icons/crystalsvg/*/*/*.svg
%{python_sitearch}/%{name}/SMBShareSelectDialog.py*
%{python_sitearch}/%{name}/SimpleCommandRunner.py*
%{python_sitearch}/%{name}/fuser.py*
%{python_sitearch}/%{name}/fuser_ui.py*
%{python_sitearch}/%{name}/grubconfig.py*
%{python_sitearch}/%{name}/mountconfig.py*
%{python_sitearch}/%{name}/serviceconfig.py*
%{python_sitearch}/%{name}/sizeview.py*
%{python_sitearch}/%{name}/unixauthdb.py*
%{python_sitearch}/%{name}/userconfig.py*
%{python_sitearch}/%{name}/wineconfig.py*
%{tde_tdedocdir}/HTML/en/guidance/


# Files from powermanager
%if 0%{?with_powermanager}
%exclude %{tde_datadir}/icons/hicolor/22x22/apps/power-manager.png
%exclude %{tde_datadir}/apps/guidance/pics/ac-adapter.png
%exclude %{tde_datadir}/apps/guidance/pics/battery*.png
%exclude %{tde_datadir}/apps/guidance/pics/processor.png
%endif

%post
touch --no-create %{tde_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/crystalsvg || :
/sbin/ldconfig || :

%postun
touch --no-create %{tde_datadir}/icons/crystalsvg || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/crystalsvg || :
/sbin/ldconfig || :

##########

%package backends
Group:			Applications/Utilities
Summary:		collection of system administration tools for GNU/Linux [Trinity]
%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
Requires:		hwdata
%endif
Requires:		python

Obsoletes:		trinity-guidance-backends < %{version}-%{release}
Provides:		trinity-guidance-backends = %{version}-%{release}

%description backends
This package contains the platform neutral backends used in the
Guidance configuration tools.

%files backends
%defattr(-,root,root,-)
%{python_sitearch}/%{name}/MicroHAL.py*
%{python_sitearch}/%{name}/drivedetect.py*
%{python_sitearch}/%{name}/wineread.py*
%{python_sitearch}/%{name}/winewrite.py*
%{python_sitearch}/%{name}/xf86misc.py*
%{python_sitearch}/ixf86misc.so

##########

%if 0%{?with_powermanager}

%package powermanager
Group:			Applications/Utilities
Summary:		HAL based power manager applet [Trinity]
Requires:		%{name} = %{version}-%{release}
Requires:		hal

Obsoletes:		trinity-guidance-powermanager < %{version}-%{release}
Provides:		trinity-guidance-powermanager = %{version}-%{release}

%if "%{tde_prefix}" == "/usr"
Conflicts:	guidance-power-manager
Conflicts:	kde-guidance-powermanager
%endif

%description powermanager
A power management applet to indicate battery levels and perform hibernate or
suspend using HAL.

%files powermanager
%defattr(-,root,root,-)
%{tde_bindir}/guidance-power-manager
%{python_sitearch}/%{name}/MicroHAL.py*
%{python_sitearch}/%{name}/guidance-power-manager.py*
%{python_sitearch}/%{name}/powermanage.py*
%{python_sitearch}/%{name}/gpmhelper.py*
%{python_sitearch}/%{name}/powermanager_ui.py*
%{python_sitearch}/%{name}/guidance_power_manager_ui.py*
%{python_sitearch}/%{name}/notify.py*
%{python_sitearch}/%{name}/tooltip.py*
%{tde_datadir}/icons/hicolor/22x22/apps/power-manager.png
%{tde_datadir}/apps/guidance/pics/ac-adapter.png
%{tde_datadir}/apps/guidance/pics/battery*.png
%{tde_datadir}/apps/guidance/pics/processor.png
%{tde_datadir}/autostart/guidance-power-manager.desktop

%post powermanager
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%postun powermanager
touch --no-create %{tde_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{tde_datadir}/icons/hicolor || :

%endif

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%if 0%{?rhel} || 0%{?mgaversion} || 0%{?mdkversion}
%__sed -i "userconfig/unixauthdb.py" \
  -e "s|self.first_uid = .*|self.first_uid = 500|" \
  -e "s|self.first_gid = .*|self.first_gid = 500|"
%endif


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
#export PYTHONPATH=%{python_sitearch}/python-tqt

# Avoids 'error: byte-compiling is disabled.' on Mandriva/Mageia
export PYTHONDONTWRITEBYTECODE=

# FTBFS on PCLOS ...
export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I%{tde_tdeincludedir} -I%{tde_includedir}"

# Specific path for RHEL4
if [ -d /usr/X11R6 ]; then
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
  %__sed -i "setup.py" -e "s|/usr/X11R6/lib|/usr/X11R6/%{_lib}|g"
fi

./setup.py build


%install
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export EXTRA_MODULE_DIR="%{python_sitearch}/%{name}"
export SIPTQT_DIR="%{python_sitearch}/sip4_tqt"
export PYTHONPATH="%{python_sitearch}/python-tqt"

# Support for 'sip4-tqt'
export PYTHONPATH="%{python_sitearch}/sip4_tqt:${PYTHONPATH}"

# For Mageia/Mandriva: Avoids 'error: byte-compiling must be disabled.
export PYTHONDONTWRITEBYTECODE=

%__rm -rf %{buildroot}
./setup.py install \
	--prefix=%{tde_prefix} \
	--root=%{buildroot}

# Fix temporary build directories remaining inside .py files
for f in %{buildroot}%{tde_datadir}/apps/guidance/*.py; do
	%__sed -i "${f}" -e "s|%{buildroot}||g"
done

##### MAIN PACKAGE INSTALLATION (based on Debian/Ubuntu packaging rules)
# install icons to right place
%__mkdir_p %{buildroot}%{tde_datadir}/icons/crystalsvg/32x32/apps
%__cp -f %{buildroot}%{tde_datadir}/apps/guidance/pics/hi32-app-daemons.png \
	%{buildroot}%{tde_datadir}/icons/crystalsvg/32x32/apps/daemons.png
%__cp -f %{buildroot}%{tde_datadir}/apps/guidance/pics/kcmpartitions.png \
	%{buildroot}%{tde_datadir}/icons/crystalsvg/32x32/apps/disksfilesystems.png
%__cp -f %{buildroot}%{tde_datadir}/apps/guidance/pics/hi32-user.png \
	%{buildroot}%{tde_datadir}/icons/crystalsvg/32x32/apps/userconfig.png
%__cp -f %{buildroot}%{tde_datadir}/apps/guidance/pics/32-wine.png \
	%{buildroot}%{tde_datadir}/icons/crystalsvg/32x32/apps/wineconfig.png
%__install -D -p -m0644 kde/wineconfig/pics/16x16/wineconfig.png \
	%{buildroot}%{tde_datadir}/icons/crystalsvg/16x16/apps/wineconfig.png

# fix binary-or-shlib-defines-rpath
chrpath -r %{tde_libdir} %{buildroot}%{tde_tdelibdir}/kcm_*.so

# fix executable-not-elf-or-script
%__chmod 0644 %{buildroot}%{tde_datadir}/apps/guidance/pics/kdewinewizard.png

# move python modules in %{python_sitearch} (/usr/lib/pythonXX/site-packages)
%__mkdir_p %{buildroot}%{python_sitearch}/%{name} 
%__mv -f %{buildroot}%{tde_datadir}/apps/guidance/*.py* %{buildroot}%{python_sitearch}/%{name}

# Generates the startup scripts
%__rm -f %{buildroot}%{tde_bindir}/*
%__ln_s -f %{python_sitearch}/%{name}/mountconfig.py %{buildroot}%{tde_bindir}/mountconfig
%__ln_s -f %{python_sitearch}/%{name}/serviceconfig.py %{buildroot}%{tde_bindir}/serviceconfig
%__ln_s -f %{python_sitearch}/%{name}/userconfig.py %{buildroot}%{tde_bindir}/userconfig
%__ln_s -f %{python_sitearch}/%{name}/wineconfig.py %{buildroot}%{tde_bindir}/wineconfig
%__ln_s -f %{python_sitearch}/%{name}/grubconfig.py %{buildroot}%{tde_bindir}/grubconfig

# fix script-not-executable
%__chmod 0755 %{buildroot}%{python_sitearch}/%{name}/fuser.py
%__chmod 0755 %{buildroot}%{python_sitearch}/%{name}/grubconfig.py

##### BACKENDS INSTALLATION

# The xf86misc stuff should not go under /opt/trinity bur under /usr !!!
%__mv -f %{buildroot}%{tde_libdir}/python*/site-packages/ixf86misc.so %{buildroot}%{python_sitearch}
%__mv -f %{buildroot}%{tde_libdir}/python*/site-packages/xf86misc.py* %{buildroot}%{python_sitearch}/%{name}

%if 0%{?rhel} || 0%{?fedora} || 0%{?mgaversion} || 0%{?mdkversion}
%__rm -f %{buildroot}%{tde_datadir}/apps/guidance/MonitorsDB
%__ln_s -f /usr/share/hwdata/MonitorsDB %{buildroot}%{tde_datadir}/apps/guidance/MonitorsDB
%endif

%if 0%{?with_powermanager}
##### POWERMANAGER INSTALLATION
# install icon to right place
%__install -D -p -m0644 kde/powermanager/pics/battery-charging-100.png \
		%{buildroot}%{tde_datadir}/icons/hicolor/22x22/apps/power-manager.png
%__install -D -p -m0644 kde/powermanager/pics/*.png \
		%{buildroot}%{tde_datadir}/apps/guidance/pics/

# install desktop file
%__install -D -p -m0644 powermanager/guidance-power-manager.desktop \
		%{buildroot}%{tde_datadir}/autostart/guidance-power-manager.desktop

# copy python modules in PYSUPPORT_PATH
%__cp powermanager/guidance_power_manager_ui.py %{buildroot}%{python_sitearch}/%{name}
%__cp powermanager/notify.py %{buildroot}%{python_sitearch}/%{name}
%__cp powermanager/tooltip.py %{buildroot}%{python_sitearch}/%{name}

# generate guidance-power-manager script
cat <<EOF >%{?buildroot}%{tde_bindir}/guidance-power-manager
#!/bin/sh
export PYTHONPATH=%{python_sitearch}/%{name}:%{python_sitearch}/sip4-tqt
%{python_sitearch}/%{name}/guidance-power-manager.py &
EOF
chmod +x %{buildroot}%{tde_bindir}/guidance-power-manager

# fix script-not-executable
chmod 0755 %{buildroot}%{python_sitearch}/%{name}/powermanage.py
chmod 0755 %{buildroot}%{python_sitearch}/%{name}/gpmhelper.py

%else
%__rm -f %{buildroot}%{python_sitearch}/%{name}/gpmhelper.py*
%__rm -f %{buildroot}%{python_sitearch}/%{name}/guidance-power-manager.py*
%__rm -f %{buildroot}%{python_sitearch}/%{name}/guidance_power_manager_ui.py*
%__rm -f %{buildroot}%{python_sitearch}/%{name}/powermanage.py*
%__rm -f %{buildroot}%{python_sitearch}/%{name}/powermanager_ui.py*
%__rm -f %{buildroot}%{tde_datadir}/apps/guidance/powermanager_ui.ui

%endif

# Replace all '#!' calls to python with /usr/bin/python
# and make them executable
for i in `find %{buildroot} -type f`; do
	sed '1s,#!.*python[^ ]*\(.*\),#! /usr/bin/python\1,' \
		$i > $i.temp;
	if cmp --quiet $i $i.temp; then
		rm -f $i.temp;
	else
		mv -f $i.temp $i;
		chmod 755 $i;
		echo "fixed interpreter: $i";
	fi;
done

# Removes useless files
find %{buildroot} -name "*.egg-info" -exec rm -f {} \;
find %{buildroot}%{tde_libdir} -name "*.a" -exec rm -f {} \;


%clean
%__rm -rf %{buildroot}


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 0.8.0svn20080103-8
- Initial release for TDE 14.0.0
