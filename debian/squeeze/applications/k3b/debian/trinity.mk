# -*- mode: makefile; coding: utf-8 -*-
# Copyright © 2003 Christopher L Cheney <ccheney@debian.org>
# Description: A class for KDE packages; sets KDE environment variables, etc
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# 02111-1307 USA.

_cdbs_scripts_path ?= /usr/lib/cdbs
_cdbs_rules_path ?= /usr/share/cdbs/1/rules
_cdbs_class_path ?= /usr/share/cdbs/1/class

ifndef _cdbs_class_kde
_cdbs_class_kde := 1

# for dh_icons
CDBS_BUILD_DEPENDS   := $(CDBS_BUILD_DEPENDS), debhelper (>= 5.0.7ubuntu4)

include $(_cdbs_rules_path)/buildcore.mk$(_cdbs_makefile_suffix)

ifdef _cdbs_tarball_dir
DEB_BUILDDIR = $(_cdbs_tarball_dir)/obj-$(DEB_BUILD_GNU_TYPE)
else
DEB_BUILDDIR = obj-$(DEB_BUILD_GNU_TYPE)
endif

include $(_cdbs_class_path)/autotools.mk$(_cdbs_makefile_suffix)

export kde_cgidir  = \$${libdir}/cgi-bin
export kde_confdir = \$${sysconfdir}/trinity
export kde_htmldir = \$${datadir}/doc/kde/HTML

ifeq (,$(findstring noopt,$(DEB_BUILD_OPTIONS)))
	cdbs_kde_enable_final = $(if $(DEB_KDE_ENABLE_FINAL),--enable-final,)
endif

ifneq (,$(findstring nostrip,$(DEB_BUILD_OPTIONS)))
	cdbs_kde_enable_final =
	cdbs_kde_enable_debug = --enable-debug=yes
else
	cdbs_kde_enable_debug = --disable-debug
endif

ifneq (,$(findstring debug,$(DEB_BUILD_OPTIONS)))
	cdbs_kde_enable_debug = --enable-debug=full
endif

cdbs_configure_flags += --with-qt-dir=/usr/share/qt3 --disable-rpath --with-xinerama --without-arts $(cdbs_kde_enable_final) $(cdbs_kde_enable_debug)

DEB_AC_AUX_DIR = $(DEB_SRCDIR)/admin
DEB_CONFIGURE_INCLUDEDIR = "/opt/trinity/include/tde"
DEB_COMPRESS_EXCLUDE = .dcl .docbook -license .tag .sty .el

$(patsubst %,binary-install/%,$(DEB_PACKAGES)) :: binary-install/%:
	if test -x /usr/bin/dh_icons; then dh_icons -p$(cdbs_curpkg) $(DEB_DH_ICONCACHE_ARGS); fi

cleanbuilddir::
	-$(if $(call cdbs_streq,$(DEB_BUILDDIR),$(DEB_SRCDIR)),,rm -rf $(DEB_BUILDDIR))

common-build-arch common-build-indep:: debian/stamp-kde-apidox
debian/stamp-kde-apidox:
	$(if $(DEB_KDE_APIDOX),+$(DEB_MAKE_INVOKE) apidox)
	touch $@

common-install-prehook-impl::
	mkdir -p po
	-XGETTEXT=/usr/bin/kde-xgettext EXTRACTATTR=/usr/bin/extractattr sh $(DEB_SRCDIR)/admin/cvs.sh extract-messages	
	-for file in po/*pot; do \
		sed "s/charset=CHARSET/charset=UTF-8/" -i $$file; \
	done

common-install-arch common-install-indep:: common-install-kde-apidox
common-install-kde-apidox::
	$(if $(DEB_KDE_APIDOX),+$(DEB_MAKE_INVOKE) install-apidox DESTDIR=$(DEB_DESTDIR))

clean::
	rm -f debian/stamp-kde-apidox
	rm -rf po/*.pot

# This is a convenience target for calling manually.  It's not part of
# the build process.
buildprep: clean apply-patches
	$(MAKE) -f admin/Makefile.common dist
	debian/rules clean

endif
