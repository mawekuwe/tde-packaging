# -*- mode: makefile; coding: utf-8 -*-
# Copyright © 2003 Colin Walters <walters@debian.org>
# Copyright © 2006 Marc Dequènes (Duck) <Duck@DuckCorp.org>
#
# Description: manage Python public modules build
#   This class is designed to work with Python packages using the
#   'distutils' build system and comply to the new policy established
#   during summer 2006.  Use of the debhelper class to make use of the
#   new dh_python is strongly advised.  (This is still left as optional
#   in line with CDBS' flexible behavior.)
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
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02111-1307 USA.
#

# This class provides rules for old and new Python policy.  Leaving
# DEB_PYTHON_SYSTEM unset selects the old behavior.  The pysupport and
# pycentral methods are available to comply with new policy.  Don't forget
# to update your 'debian/control'.  (Build-Depends are correctly generated
# if you are using the auto control generation feature.)

# Once all old-style packages are removed before etch, some of the old
# can be refactored or removed.


_cdbs_scripts_path ?= /usr/lib/cdbs
_cdbs_rules_path ?= /usr/share/cdbs/1/rules
_cdbs_class_path ?= /usr/share/cdbs/1/class

ifndef _cdbs_class_python_distutils
_cdbs_class_python_distutils = 1

include $(_cdbs_rules_path)/buildcore.mk$(_cdbs_makefile_suffix)
include $(_cdbs_class_path)/langcore.mk$(_cdbs_makefile_suffix)


# check python system
cdbs_use_xs_field := $(shell grep -q "^XS-Python-Version:" debian/control && echo yes)
cdbs_selected_pycompat := $(shell if [ -e debian/pycompat ]; then cat debian/pycompat; fi)
cdbs_pycompat = $(cdbs_selected_pycompat)
ifeq (pysupport, $(DEB_PYTHON_SYSTEM))
  cdbs_python_support_path = usr/share/python-support/$(DEB_PYTHON_MODULE_PACKAGE)
  ifeq (, $(cdbs_selected_pycompat))
    cdbs_pycompat = 2
  endif # use pycompat
  # warning pysupport compatibility mode
  ifneq (, $(cdbs_use_xs_field))
    $(warning WARNING:  Use of XS-Python-Version and XB-Python-Version fields in debian/control is deprecated with pysupport method; use debian/pyversions if you need to specify specific versions.)
  endif # use XS field (compat)
else
  ifeq (pycentral, $(DEB_PYTHON_SYSTEM))
    ifeq (, $(cdbs_selected_pycompat))
      cdbs_pycompat = 2
    endif # use pycompat
  else
    ifneq (, $(DEB_PYTHON_SYSTEM))
      $(error unsupported Python system: $(DEB_PYTHON_SYSTEM) (select either pysupport or pycentral))
    else
      ifneq (, $(cdbs_use_xs_field))
        $(error package uses the new Python policy; DEB_PYTHON_SYSTEM must be set to "pysupport" or "pycentral")
      endif
      ifneq (, $(cdbs_selected_pycompat))
        ifeq (yes, $(shell expr $(cdbs_selected_pycompat) \> 1 >/dev/null && echo yes))
          $(error package uses the new Python policy; DEB_PYTHON_SYSTEM must be set to "pysupport" or "pycentral")
        endif
      endif # use pycompat
    endif # unknown method
  endif # pycentral
endif # pysupport


ifndef DEB_PYTHON_SYSTEM
DEB_PYTHON_COMPILE_VERSION = 
DEB_PYTHON_VERSIONS = 2.1 2.2 2.3 2.4 2.5
else
# default package is the first one declared in 'debian/control'
# (override if necessary)
DEB_PYTHON_MODULE_PACKAGE = $(firstword $(filter-out %-doc %-dev %-common, $(DEB_PACKAGES)))
DEB_PYTHON_PRIVATE_MODULES_DIRS =
endif

# common variables
DEB_PYTHON_SETUP_CMD = setup.py
DEB_PYTHON_CLEAN_ARGS = -a
DEB_PYTHON_BUILD_ARGS = --build-base="$(CURDIR)/$(DEB_BUILDDIR)/build"
DEB_PYTHON_INSTALL_ARGS_ALL = --no-compile -O0


ifndef DEB_PYTHON_SYSTEM
########################### old policy method ###########################

$(warning =======================================================)
$(warning Your package does not conform to the new Python policy.)
$(warning Please consider updating.  Here is some documentation:)
$(warning   http://wiki.debian.org/DebianPython/NewPolicy)
$(warning   http://wiki.debian.org/DebianPythonFAQ)
$(warning =======================================================)

# make: *** No rule to make target `voodoo'.  Stop.
DEB_PYTHON_REAL_LIB_PACKAGES = $(strip $(filter $(patsubst %,python%%,$(DEB_PYTHON_VERSIONS)),$(filter-out $(DEB_PYTHON_PACKAGES_EXCLUDE),$(DEB_ALL_PACKAGES))))
# If no versioned python library packages found, grab all simpler ones
ifeq (,$(DEB_PYTHON_REAL_LIB_PACKAGES))
DEB_PYTHON_SIMPLE_PACKAGES = $(strip $(filter python-%,$(filter-out $(DEB_PYTHON_PACKAGES_EXCLUDE),$(DEB_ALL_PACKAGES))))
endif

cdbs_python_ver = $(filter-out -%,$(subst -, -,$(patsubst python%,%,$(cdbs_curpkg))))

common-build-arch common-build-indep:: common-build-impl
common-build-impl::
	cd $(DEB_SRCDIR) && python$(DEB_PYTHON_COMPILE_VERSION) $(DEB_PYTHON_SETUP_CMD) build $(DEB_PYTHON_BUILD_ARGS)


# See if this package doesn't appear to need to be compiled by multiple
# Python versions.
ifeq (,$(DEB_PYTHON_REAL_LIB_PACKAGES))
common-install-arch common-install-indep:: common-install-impl
common-install-impl::
	cd $(DEB_SRCDIR) && python$(DEB_PYTHON_COMPILE_VERSION) $(DEB_PYTHON_SETUP_CMD) install --root=$(DEB_DESTDIR) $(DEB_PYTHON_INSTALL_ARGS_ALL) $(DEB_PYTHON_INSTALL_ARGS_$(cdbs_curpkg))
else
$(patsubst %,install/%,$(DEB_PYTHON_REAL_LIB_PACKAGES)) :: install/% :
	cd $(DEB_SRCDIR) && python$(cdbs_python_ver) $(DEB_PYTHON_SETUP_CMD) install --root=$(CURDIR)/debian/$(cdbs_curpkg) $(DEB_PYTHON_INSTALL_ARGS_ALL) $(DEB_PYTHON_INSTALL_ARGS_$(cdbs_curpkg))
endif

$(patsubst %,install/%,$(DEB_PYTHON_SIMPLE_PACKAGES)) :: install/% :
	cd $(DEB_SRCDIR) && python $(DEB_PYTHON_SETUP_CMD) install --root=$(CURDIR)/debian/$(cdbs_curpkg) $(DEB_PYTHON_INSTALL_ARGS_ALL) $(DEB_PYTHON_INSTALL_ARGS_$(cdbs_curpkg))

# This class can optionally utilize debhelper's "dh_python" command.  Just
# be sure you include debhelper.mk before including this file.
ifdef _cdbs_rules_debhelper

DEB_DH_PYTHON_ARGS = $(addprefix -V ,$(DEB_PYTHON_COMPILE_VERSION)) $(DEB_DH_PYTHON_ARGS_ALL) $(DEB_DH_PYTHON_ARGS_$(cdbs_curpkg))
DH_PYTHON2 = $(if $(wildcard /usr/bin/dh_python2),dh_python2,dh_python)

$(patsubst %,binary-install/%,$(DEB_PACKAGES)) :: binary-install/%:
	${DH_PYTHON2} -p$(cdbs_curpkg) $(DEB_DH_PYTHON_ARGS)
endif


# Ignore errors from this rule.  In a tarball build, the file may not
# exist.
ifeq (,$(DEB_PYTHON_REAL_LIB_PACKAGES))
clean::
	-python$(DEB_PYTHON_COMPILE_VERSION) $(DEB_PYTHON_SETUP_CMD) clean $(DEB_PYTHON_CLEAN_ARGS)
else
clean:: $(patsubst %,python-cleanbuilddir/%,$(DEB_PYTHON_REAL_LIB_PACKAGES))

$(patsubst %,python-cleanbuilddir/%,$(DEB_PYTHON_REAL_LIB_PACKAGES)) :: python-cleanbuilddir/% : 
	-python$(cdbs_python_ver) $(DEB_PYTHON_SETUP_CMD) clean $(DEB_PYTHON_CLEAN_ARGS)
endif

else
########################## new policy methods ###########################

# Calculate cdbs_python_build_versions
cdbs_python_module_arch := $(strip $(shell perl -e '$$/=""; $$_=(grep {/^Package: $(DEB_PYTHON_MODULE_PACKAGE)$$/m;} (<>))[0]; /^Architecture: (.*)$$/m && print $$1' debian/control))
cdbs_python_current_version := $(shell pyversions -vd)
ifeq (all, $(cdbs_python_module_arch))
  # check if current is in build versions
  ifneq ($(cdbs_python_current_version), $(filter $(cdbs_python_current_version), $(shell pyversions -vr)))
    cdbs_python_compile_version := $(firstword $(strip $(sort $(shell pyversions -vr))))
    cdbs_python_build_versions := $(cdbs_python_compile_version)
  else
    cdbs_python_build_versions := $(cdbs_python_current_version)
  endif
else
cdbs_python_build_versions := $(shell pyversions -vr)
endif # archall

# check if build is possible
ifeq (, $(cdbs_python_build_versions))
ifeq (pysupport, $(DEB_PYTHON_SYSTEM))
$(error invalid setting in debian/pyversions)
else
$(error invalid setting for XS-Python-Version)
endif # system selected
endif # build versions empty


# Declare Build-Deps for packages using this file
CDBS_BUILD_DEPENDS := $(CDBS_BUILD_DEPENDS), debhelper (>= 5.0.37.2), cdbs (>= 0.4.43)
ifeq (all, $(cdbs_python_module_arch))
  ifneq (, $(cdbs_python_compile_version))
    CDBS_BUILD_DEPENDS := $(CDBS_BUILD_DEPENDS), python$(cdbs_python_compile_version)-dev, python (>= 2.3.5-11)
  else
    CDBS_BUILD_DEPENDS := $(CDBS_BUILD_DEPENDS), python-dev (>= 2.3.5-11)
  endif
else
CDBS_BUILD_DEPENDS := $(CDBS_BUILD_DEPENDS), python-all-dev (>= 2.3.5-11)
endif
ifeq (pysupport, $(DEB_PYTHON_SYSTEM))
CDBS_BUILD_DEPENDS := $(CDBS_BUILD_DEPENDS), python-support (>= 0.3.2)
else
CDBS_BUILD_DEPENDS := $(CDBS_BUILD_DEPENDS), python-central (>= 0.6)
endif


cdbs_python_current_binary := $(shell pyversions -d)
cdbs_python_binary = $(if $(call cdbs_streq,$(cdbs_python_current_binary),$(1)),python,$(1))

# build stage
common-build-arch common-build-indep:: $(addprefix python-build-stamp-, $(cdbs_python_build_versions))
python-build-stamp-%:
ifeq (all, $(cdbs_python_module_arch))
	cd $(DEB_SRCDIR) && $(call cdbs_python_binary,python$(cdbs_python_compile_version)) $(DEB_PYTHON_SETUP_CMD) build $(DEB_PYTHON_BUILD_ARGS)
else
	cd $(DEB_SRCDIR) && $(call cdbs_python_binary,python$*) $(DEB_PYTHON_SETUP_CMD) build $(DEB_PYTHON_BUILD_ARGS)
endif # archall detection
	touch $@


# install stage
ifeq (all, $(cdbs_python_module_arch))
common-install-arch common-install-indep:: python-install-py
python-install-py:
	cd $(DEB_SRCDIR) && $(call cdbs_python_binary,python$(cdbs_python_compile_version)) $(DEB_PYTHON_SETUP_CMD) install --root=$(DEB_DESTDIR) $(DEB_PYTHON_INSTALL_ARGS_ALL)
else
common-install-arch common-install-indep:: $(addprefix python-install-, $(cdbs_python_build_versions))
python-install-%:
	cd $(DEB_SRCDIR) && $(call cdbs_python_binary,python$*) $(DEB_PYTHON_SETUP_CMD) install --root=$(DEB_DESTDIR) $(DEB_PYTHON_INSTALL_ARGS_ALL)
endif # archall detection


# clean stage
clean:: $(addprefix python-clean-, $(cdbs_python_build_versions))
python-clean-%:
ifeq (all, $(cdbs_python_module_arch))
	-cd $(DEB_SRCDIR) && $(call cdbs_python_binary,python$(cdbs_python_compile_version)) $(DEB_PYTHON_SETUP_CMD) clean $(DEB_PYTHON_CLEAN_ARGS)
else
	-cd $(DEB_SRCDIR) && $(call cdbs_python_binary,python$*) $(DEB_PYTHON_SETUP_CMD) clean $(DEB_PYTHON_CLEAN_ARGS)
endif # archall detection

clean::
ifeq (, $(cdbs_selected_pycompat))
	echo "$(cdbs_pycompat)" >debian/pycompat
endif # use pycompat
	rm -f python-build-stamp-*

endif


########################## all policy methods ###########################

# Calling setup.py clean may create .pyc files, so we need a final cleanup
# pass here.
clean::
	find . -name '*.pyc' -exec rm '{}' ';'

endif
