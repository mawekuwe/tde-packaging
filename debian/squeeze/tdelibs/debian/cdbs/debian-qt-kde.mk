ifndef _cdbs_bootstrap
_cdbs_scripts_path ?= /usr/lib/cdbs
_cdbs_rules_path ?= /usr/share/cdbs/1/rules
_cdbs_class_path ?= /usr/share/cdbs/1/class
endif

ifndef _cdbs_class_debian-qt-kde
_cdbs_class_debian-qt-kde := 1

common-build-arch:: debian/stamp-man-pages
debian/stamp-man-pages:
	if ! test -d debian/man/out; then mkdir -p debian/man/out; fi
	for f in $$(find debian/man -name '*.sgml'); do \
		docbook-to-man $$f > debian/man/out/`basename $$f .sgml`.1; \
	done
	for f in $$(find debian/man -name '*.man'); do \
		soelim -I debian/man $$f \
		> debian/man/out/`basename $$f .man`.`head -n1 $$f | awk '{print $$NF}'`; \
	done
	touch debian/stamp-man-pages

clean::
	rm -rf debian/man/out
	-rmdir debian/man
	rm -f debian/stamp-man-pages

endif

common-build-arch common-build-indep:: debian/stamp-kde-apidox
debian/stamp-kde-apidox:
	$(if $(DEB_KDE_APIDOX),+$(DEB_MAKE_INVOKE) apidox)
	touch $@

common-install-arch common-install-indep:: common-install-kde-apidox
common-install-kde-apidox::
	$(if $(DEB_KDE_APIDOX),+$(DEB_MAKE_INVOKE) install-apidox DESTDIR=$(DEB_DESTDIR))

clean::
	rm -f debian/stamp-kde-apidox
