# Default version for this component
%define kdecomp guidance
%define version 0.8.0svn20080103
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

%define __arch_install_post %{nil}

Name:		trinity-%{kdecomp}
Summary:	collection of KDE system administration tools for GNU/Linux [Trinity]
Version:	%{?version}
Release:	%{?release}%{?dist}%{?_variant}

License:	GPLv2+
Group:		Applications/Utilities

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.simonzone.com/software/guidance

Prefix:    %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	kde-guidance-3.5.13.tar.gz

BuildRequires:	tqtinterface-devel
BuildRequires:	trinity-kdelibs-devel
BuildRequires:	trinity-kdebase-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext

BuildRequires:	trinity-pykdeextensions
BuildRequires:	chrpath
Requires:		python-trinity
Requires:		%{name}-backends
Requires:		hwdata
Requires:		python >= 2.5

%if "%{_prefix}" == "/usr"
Conflicts:	guidance-power-manager
Conflicts:	kde-guidance-powermanager
%endif

%description
Guidance currently consists of four programs designed to help you
look after your system:
 o  userconfig - User and Group administration
 o  serviceconfig - Service/daemon administration
 o  mountconfig - Disk and filesystem administration
 o  displayconfig - Screen and display configuration
 o  wineconfig - Wine configuration

These tools are available in KDE Control Center, System Settings 
or can be run as standalone applications.



%package backends
Group:		Applications/Utilities
Summary:	collection of system administration tools for GNU/Linux [Trinity]
Requires:	hwdata
Requires:	python >= 2.5

%description backends
This package contains the platform neutral backends used in the
Guidance configuration tools.


%package powermanager
Group:		Applications/Utilities
Summary:	HAL based power manager applet [Trinity]
Requires:	%{name} = %{version}-%{release}

%description powermanager
A power management applet to indicate battery levels and perform hibernate or
suspend using HAL.


%prep
%setup -q -n applications/kde-guidance


%build
export PATH="%{_bindir}:${PATH}"
export LDFLAGS="-L%{_libdir} -I%{_includedir}"
./setup.py build



%install
export PATH="%{_bindir}:${PATH}"
%__rm -rf %{buildroot}
./setup.py install \
	--prefix=%{_prefix} \
	--root=%{buildroot}

%find_lang %{kdecomp} || touch %{kdecomp}.lang

# Fix building directories stored inside .py files
for f in %{buildroot}%{_datadir}/apps/guidance/*.py; do
	%__sed -i "${f}" -e "s|%{buildroot}||g"
done

##### MAIN PACKAGE INSTALLATION 
# install icons to right place
%__mkdir_p %{buildroot}%{_datadir}/icons/crystalsvg/32x32/apps
%__mv -f %{buildroot}%{_datadir}/apps/guidance/pics/hi32-app-daemons.png \
	%{buildroot}%{_datadir}/icons/crystalsvg/32x32/apps/daemons.png
%__mv -f %{buildroot}%{_datadir}/apps/guidance/pics/kcmpartitions.png \
	%{buildroot}%{_datadir}/icons/crystalsvg/32x32/apps/disksfilesystems.png
%__mv -f %{buildroot}%{_datadir}/apps/guidance/pics/hi32-user.png \
	%{buildroot}%{_datadir}/icons/crystalsvg/32x32/apps/userconfig.png
%__mv -f %{buildroot}%{_datadir}/apps/guidance/pics/hi32-display.png \
	%{buildroot}%{_datadir}/icons/crystalsvg/32x32/apps/displayconfig.png
%__mv -f %{buildroot}%{_datadir}/apps/guidance/pics/32-wine.png \
	%{buildroot}%{_datadir}/icons/crystalsvg/32x32/apps/wineconfig.png
%__install -D -p -m0644 kde/wineconfig/pics/16x16/wineconfig.png \
	%{buildroot}%{_datadir}/icons/crystalsvg/16x16/apps/wineconfig.png

# fix binary-or-shlib-defines-rpath
chrpath -d %{buildroot}%{tde_libdir}/kcm_*.so.*

# fix executable-not-elf-or-script
%__chmod 0644 %{buildroot}%{_datadir}/apps/guidance/pics/kdewinewizard.png

# move python modules in %{python_sitearch}
%__mkdir_p %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/SMBShareSelectDialog.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/SimpleCommandRunner.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/displayconfig.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/displayconfigwidgets.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/fuser.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/fuser_ui.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/grubconfig.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/ktimerdialog.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/mountconfig.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/servertestdialog.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/serviceconfig.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/sizeview.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/unixauthdb.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/userconfig.py %{buildroot}%{python_sitearch}/%{name}
%__mv -f %{buildroot}%{_datadir}/apps/guidance/wineconfig.py %{buildroot}%{python_sitearch}/%{name}

# fix the link properly
%__rm -f %{buildroot}%{_bindir}/*
%__ln_s -f %{python_sitearch}/%{name}/displayconfig.py %{buildroot}%{_bindir}/displayconfig
%__ln_s -f %{python_sitearch}/%{name}/mountconfig.py %{buildroot}%{_bindir}/mountconfig
%__ln_s -f %{python_sitearch}/%{name}/serviceconfig.py %{buildroot}%{_bindir}/serviceconfig
%__ln_s -f %{python_sitearch}/%{name}/userconfig.py %{buildroot}%{_bindir}/userconfig
%__ln_s -f %{python_sitearch}/%{name}/wineconfig.py %{buildroot}%{_bindir}/wineconfig
%__ln_s -f %{python_sitearch}/%{name}/grubconfig.py %{buildroot}%{_bindir}/grubconfig

# put this here since gnome people probably don't want it by default
%__ln_s -f %{_python_sitearch}/guidance-backends-trinity/displayconfig-restore.py %{buildroot}%{_bindir}/displayconfig-restore

# fix script-not-executable
%__chmod 0755 %{buildroot}%{python_sitearch}/%{name}/fuser.py
%__chmod 0755 %{buildroot}%{python_sitearch}/%{name}/grubconfig.py

# Moves libraries
%__mv -f %{buildroot}%{tde_libdir}/*.so.* %{buildroot}%{_libdir}
%__mv -f %{buildroot}%{tde_libdir}/*.so %{buildroot}%{_libdir}
%__mv -f %{buildroot}%{tde_libdir}/*.la %{buildroot}%{_libdir}
%__mv -f %{buildroot}%{tde_libdir}/*.a %{buildroot}%{_libdir}

%__mv -f %{buildroot}%{_datadir}/applications/kde/displayconfig.desktop %{buildroot}%{_datadir}/applications/kde/guidance-displayconfig.desktop

##### BACKENDS INSTALLATION
# install displayconfig-hwprobe.py script
%__install -D -p -m0755 displayconfig/displayconfig-hwprobe.py \
	%{buildroot}%{python_sitearch}/trinity-guidance-backends/displayconfig-hwprobe.py

%__mv -f %{buildroot}%{_libdir}/python*/site-packages/ixf86misc.so %{buildroot}%{python_sitearch}
%__mv -f %{buildroot}%{_libdir}/python*/site-packages/xf86misc.py* %{buildroot}%{python_sitearch}/trinity-guidance-backends
%__mv -f %{buildroot}%{_datadir}/apps/guidance/MicroHAL.py %{buildroot}%{python_sitearch}/trinity-guidance-backends
%__mv -f %{buildroot}%{_datadir}/apps/guidance/ScanPCI.py %{buildroot}%{python_sitearch}/trinity-guidance-backends
%__mv -f %{buildroot}%{_datadir}/apps/guidance/infimport.py %{buildroot}%{python_sitearch}/trinity-guidance-backends
%__mv -f %{buildroot}%{_datadir}/apps/guidance/displayconfigabstraction.py %{buildroot}%{python_sitearch}/trinity-guidance-backends
%__mv -f %{buildroot}%{_datadir}/apps/guidance/displayconfig-restore.py %{buildroot}%{python_sitearch}/trinity-guidance-backends
%__mv -f %{buildroot}%{_datadir}/apps/guidance/drivedetect.py %{buildroot}%{python_sitearch}/trinity-guidance-backends
%__mv -f %{buildroot}%{_datadir}/apps/guidance/execwithcapture.py %{buildroot}%{python_sitearch}/trinity-guidance-backends
%__mv -f %{buildroot}%{_datadir}/apps/guidance/wineread.py %{buildroot}%{python_sitearch}/trinity-guidance-backends
%__mv -f %{buildroot}%{_datadir}/apps/guidance/winewrite.py %{buildroot}%{python_sitearch}/trinity-guidance-backends
%__mv -f %{buildroot}%{_datadir}/apps/guidance/xorgconfig.py %{buildroot}%{python_sitearch}/trinity-guidance-backends

%__rm -f %{buildroot}%{_datadir}/apps/guidance/MonitorsDB
%__ln_s -f /usr/share/hwdata/MonitorsDB %{buildroot}%{_datadir}/apps/guidance/MonitorsDB



##### POWERMANAGER INSTALLATION
# install icon to right place
%__install -D -p -m0644 kde/powermanager/pics/battery-charging-100.png \
		%{buildroot}%{_datadir}/icons/hicolor/22x22/apps/power-manager.png
%__install -D -p -m0644 kde/powermanager/pics/*.png \
		%{buildroot}%{_datadir}/apps/guidance/pics/

# install desktop file
%__install -D -p -m0644 powermanager/guidance-power-manager.desktop \
		%{buildroot}%{_datadir}/autostart/guidance-power-manager.desktop

# copy python modules in PYSUPPORT_PATH
%__mkdir_p %{buildroot}%{python_sitearch}/trinity-guidance-powermanager
%__cp %{buildroot}%{python_sitearch}/trinity-guidance-backends/MicroHAL.py %{buildroot}%{python_sitearch}/trinity-guidance-powermanager
%__mv -f %{buildroot}%{_datadir}/apps/guidance/guidance-power-manager.py %{buildroot}%{python_sitearch}/trinity-guidance-powermanager
%__mv -f %{buildroot}%{_datadir}/apps/guidance/powermanage.py %{buildroot}%{python_sitearch}/trinity-guidance-powermanager
%__mv -f %{buildroot}%{_datadir}/apps/guidance/gpmhelper.py %{buildroot}%{python_sitearch}/trinity-guidance-powermanager
%__mv -f %{buildroot}%{_datadir}/apps/guidance/powermanager_ui.py %{buildroot}%{python_sitearch}/trinity-guidance-powermanager
%__cp powermanager/guidance_power_manager_ui.py %{buildroot}%{python_sitearch}/trinity-guidance-powermanager
%__cp powermanager/notify.py %{buildroot}%{python_sitearch}/trinity-guidance-powermanager
%__cp powermanager/tooltip.py %{buildroot}%{python_sitearch}/trinity-guidance-powermanager

# generate guidance-power-manager script
cat <<EOF >%{buildroot}%{_bindir}/guidance-power-manager
#!/bin/sh
export PYTHONPATH=%{python_sitearch}/trinity-guidance-backends
%{python_sitearch}/trinity-guidance-powermanager/guidance-power-manager.py &
EOF
chmod +x %{buildroot}%{_bindir}/guidance-power-manager

# fix script-not-executable
chmod 0755 %{buildroot}%{python_sitearch}/trinity-guidance-powermanager/powermanage.py
chmod 0755 %{buildroot}%{python_sitearch}/trinity-guidance-powermanager/gpmhelper.py


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

find %{buildroot} -name "*.egg-info" -exec rm -f {} \;


%clean
%__rm -rf %{buildroot}


%post
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
/sbin/ldconfig || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
/sbin/ldconfig || :


%files -f %{kdecomp}.lang
%defattr(-,root,root,-)
%doc ChangeLog COPYING README TODO
%{_bindir}/displayconfig
%{_bindir}/displayconfig-restore
%{_bindir}/grubconfig
%{_bindir}/mountconfig
%{_bindir}/serviceconfig
%{_bindir}/userconfig
%{_bindir}/wineconfig
%{_libdir}/*.so.*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_datadir}/apps/guidance
%{python_sitearch}/trinity-guidance
%{_datadir}/applications/kde/*.desktop
%{tde_docdir}/HTML/en/guidance
%{_datadir}/icons/crystalsvg/*/*/*.png
%exclude %{_datadir}/icons/crystalsvg/*/*/*.svg
#%{python_sitearch}/guidance-*.egg-info
%exclude /etc/X11/Xsession.d/40guidance-displayconfig_restore

%files -n trinity-guidance-backends
%defattr(-,root,root,-)
%{python_sitearch}/trinity-guidance-backends
%{python_sitearch}/ixf86misc.so
%{_datadir}/apps/guidance/vesamodes
%{_datadir}/apps/guidance/extramodes
%{_datadir}/apps/guidance/widescreenmodes
%{_datadir}/apps/guidance/Cards+
%{_datadir}/apps/guidance/pcitable
%{_datadir}/apps/guidance/MonitorsDB


%files powermanager
%defattr(-,root,root,-)
%{_bindir}/guidance-power-manager
%{python_sitearch}/trinity-guidance-powermanager
%{_datadir}/icons/hicolor/22x22/apps/power-manager.png
%{_datadir}/apps/guidance/pics/ac-adapter.png
%{_datadir}/apps/guidance/pics/battery*.png
%{_datadir}/apps/guidance/pics/processor.png
%{_datadir}/autostart/guidance-power-manager.desktop


%Changelog
* Thu Dec 01 2011 Francois Andriot <francois.andriot@free.fr> - 0.8.0svn20080103-1
- Initial build for RHEL 5, RHEL 6, Fedora 15, Fedora 16
