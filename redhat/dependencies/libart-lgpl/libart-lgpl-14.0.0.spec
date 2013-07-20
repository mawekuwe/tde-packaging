# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_version 14.0.0

%define tde_bindir %{tde_prefix}/bin
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_datadir %{tde_prefix}/share

%define tde_tdeincludedir %{tde_includedir}/tde

%define _docdir %{tde_datadir}/doc


Name:           trinity-libart-lgpl
Version:        2.3.22
Release:		%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

Summary:        Library of functions for 2D graphics - runtime files

Group:          System Environment/Libraries
License:        LGPLv2+

Vendor:			Trinity Project
URL:			http://www.trinitydesktop.org/
Packager:		Francois Andriot <francois.andriot@free.fr>

Prefix:			%{tde_prefix}
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:		%{name}-%{tde_version}%{?preversion:~%{preversion}}.tar.gz

BuildRequires:  trinity-tqt3-devel >= 3.5.0
BuildRequires:  trinity-tqtinterface-devel >= %{tde_version}

%description
A library of functions for 2D graphics supporting a superset of the
PostScript imaging model, designed to be integrated with graphics, artwork,
and illustration programs. It is written in optimized C, and is fully
compatible with C++. With a small footprint of 10,000 lines of code, it is
especially suitable for embedded applications.


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%{tde_libdir}/libart_lgpl_2.so.2
%{tde_libdir}/libart_lgpl_2.so.2.3.21

##########

%package        devel
Summary:        Library of functions for 2D graphics - development files
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
A library of functions for 2D graphics supporting a superset of the
PostScript imaging model, designed to be integrated with graphics, artwork,
and illustration programs. It is written in optimized C, and is fully
compatible with C++. With a small footprint of 10,000 lines of code, it is
especially suitable for embedded applications.

%post devel
/sbin/ldconfig

%postun devel
/sbin/ldconfig

%files devel
%defattr(-,root,root,-)
%{tde_bindir}/libart2-config
%{tde_libdir}/libart_lgpl_2.a
%{tde_libdir}/libart_lgpl_2.la
%{tde_libdir}/libart_lgpl_2.so
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_affine.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_alphagamma.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_bpath.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_config.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_filterlevel.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_gray_svp.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_misc.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_pathcode.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_pixbuf.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_point.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_rect.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_rect_svp.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_rect_uta.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_render.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_render_gradient.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_render_mask.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_render_svp.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_rgb.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_rgb_a_affine.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_rgb_affine.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_rgb_bitmap_affine.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_rgb_pixbuf_affine.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_rgb_rgba_affine.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_rgb_svp.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_rgba.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_svp.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_svp_intersect.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_svp_ops.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_svp_point.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_svp_render_aa.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_svp_vpath.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_svp_vpath_stroke.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_svp_wind.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_uta.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_uta_ops.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_uta_rect.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_uta_svp.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_uta_vpath.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_vpath.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_vpath_bpath.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_vpath_dash.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/art_vpath_svp.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/libart-features.h
%{tde_tdeincludedir}/libart-2.0/libart_lgpl/libart.h
%{tde_libdir}/pkgconfig/libart-2.0.pc

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{tde_version}%{?preversion:~%{preversion}}

%__cp -f "/usr/share/aclocal/libtool.m4" "libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "ltmain.sh"
autoreconf -fiv


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export LDFLAGS="-L%{tde_libdir} -I%{tde_includedir}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig:${PKG_CONFIG_PATH}"

%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --disable-rpath \
  --enable-new-ldflags \
  --enable-closure \
  --disable-debug --disable-warnings \
  --enable-final
  
%__make %{?_smp_mflags}


%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT


%clean
%__rm -rf $RPM_BUILD_ROOT



%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 2.3.22-1
- Initial build for TDE 14.0.0
