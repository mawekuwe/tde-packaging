# -*- mode: makefile; coding: utf-8 -*-
# Copyright © 2002,2003 Colin Walters <walters@debian.org>
# Description: Defines some useful variables, but no rules
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

ifndef _cdbs_rules_buildvars
_cdbs_rules_buildvars = 1

CDBS_VERSION = something

# Common useful variables
DEB_SOURCE_PACKAGE := $(strip $(shell egrep '^Source: ' debian/control | cut -f 2 -d ':'))
DEB_VERSION := $(shell dpkg-parsechangelog | egrep '^Version:' | cut -f 2 -d ' ')
DEB_NOEPOCH_VERSION := $(shell echo $(DEB_VERSION) | cut -d: -f2-)
DEB_UPSTREAM_VERSION := $(shell echo $(DEB_NOEPOCH_VERSION) | sed 's/-[^-]*$$//')
DEB_ISNATIVE := $(shell dpkg-parsechangelog | egrep '^Version:' | perl -ne 'print if not /^Version:\s*.*-/;')

# Split into arch/indep packages
ifneq ($(DEB_INDEP_PACKAGES),cdbs)
DEB_INDEP_PACKAGES := $(filter-out $(DONT_BUILD), $(strip $(shell $(_cdbs_scripts_path)/list-packages indep)))
DEB_ARCH_PACKAGES := $(filter-out $(DONT_BUILD), $(filter-out $(DEB_INDEP_PACKAGES),$(strip $(shell $(_cdbs_scripts_path)/list-packages same))))
endif
# Split into normal and udeb packages
ifeq ($(DEB_UDEB_PACKAGES),)
DEB_PACKAGES = $(filter-out $(DONT_BUILD), $(filter-out %-udeb, $(DEB_ARCH_PACKAGES) $(DEB_INDEP_PACKAGES)))
DEB_UDEB_PACKAGES = $(filter-out $(DONT_BUILD),$(filter %-udeb, $(DEB_ARCH_PACKAGES) $(DEB_INDEP_PACKAGES)))
else
DEB_PACKAGES = $(filter-out $(DONT_BUILD), $(filter-out $(DEB_UDEB_PACKAGES), $(DEB_ARCH_PACKAGES) $(DEB_INDEP_PACKAGES)))
endif
# Too much bother for now.  If someone complains we'll fix it.
#DEB_ARCH_UDEB_PACKAGES = $(filter %-udeb, $(DEB_ARCH_PACKAGES))
#DEB_INDEP_UDEB_PACKAGES = $(filter %-udeb, $(DEB_INDEP_PACKAGES))
# A handy list of every package, udeb or not
DEB_ALL_PACKAGES = $(filter-out $(DONT_BUILD),$(DEB_PACKAGES) $(DEB_UDEB_PACKAGES))
DEB_INDEP_REGULAR_PACKAGES = $(filter-out $(DONT_BUILD), $(filter-out $(DEB_UDEB_PACKAGES),$(DEB_INDEP_PACKAGES)))
DEB_ARCH_REGULAR_PACKAGES = $(filter-out $(DONT_BUILD), $(filter-out $(DEB_UDEB_PACKAGES),$(DEB_ARCH_PACKAGES)))

DEB_DBG_PACKAGES = $(filter-out $(DONT_BUILD), $(filter %-dbg, $(DEB_ARCH_PACKAGES) $(DEB_INDEP_PACKAGES)))

# Some support for srcdir != builddir builds.
# These are relative to the root of the package
DEB_SRCDIR ?= .
DEB_BUILDDIR ?= $(strip $(DEB_SRCDIR))

# Miscellaneous bits
DEB_ARCH = $(shell dpkg --print-architecture)
DEB_HOST_GNU_TYPE ?= $(shell dpkg-architecture -qDEB_HOST_GNU_TYPE)
DEB_HOST_GNU_SYSTEM ?= $(shell dpkg-architecture -qDEB_HOST_GNU_SYSTEM)
DEB_HOST_GNU_CPU ?= $(shell dpkg-architecture -qDEB_HOST_GNU_CPU)
DEB_HOST_ARCH ?= $(shell dpkg-architecture -qDEB_HOST_ARCH)
DEB_HOST_ARCH_CPU ?= $(shell dpkg-architecture -qDEB_HOST_ARCH_CPU)
DEB_HOST_ARCH_OS ?= $(shell dpkg-architecture -qDEB_HOST_ARCH_OS)
DEB_BUILD_GNU_TYPE ?= $(shell dpkg-architecture -qDEB_BUILD_GNU_TYPE)
DEB_BUILD_GNU_SYSTEM ?= $(shell dpkg-architecture -qDEB_BUILD_GNU_SYSTEM)
DEB_BUILD_GNU_CPU ?= $(shell dpkg-architecture -qDEB_BUILD_GNU_CPU)
DEB_BUILD_ARCH ?= $(shell dpkg-architecture -qDEB_BUILD_ARCH)
DEB_BUILD_ARCH_CPU ?= $(shell dpkg-architecture -qDEB_BUILD_ARCH_CPU)
DEB_BUILD_ARCH_OS ?= $(shell dpkg-architecture -qDEB_BUILD_ARCH_OS)

ifeq ($(words $(DEB_ALL_PACKAGES)),1)
	DEB_DESTDIR = $(CURDIR)/debian/$(strip $(DEB_ALL_PACKAGES))/
else
	DEB_DESTDIR = $(CURDIR)/debian/tmp/
endif

CDBS_BUILD_DEPENDS := $(CDBS_BUILD_DEPENDS), cdbs (>= 0.4.23-1.1)

endif
