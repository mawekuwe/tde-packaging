DEFAULT_BACKGROUND=desktop-background

INSTALL=install -m 0644
BACKGROUNDS=$(wildcard backgrounds/*.png backgrounds/*.jpg backgrounds/*.svg backgrounds/*.tga)
EMBLEMS=$(wildcard emblems/*png emblems/*icon)
SPLASH=$(wildcard splash/*.png)
PIXMAPS=$(wildcard pixmaps/*.png)
DESKTOPFILES=$(wildcard *.desktop)

all:
#	make -C usplash/moreblue-orbit

clean:
#	make -C usplash/moreblue-orbit clean

install:
	# splashy theme
	mkdir -p $(DESTDIR)/usr/share/splashy/themes/moreblue-orbit
	$(INSTALL) $(wildcard splashy/moreblue-orbit/*) $(DESTDIR)/usr/share/splashy/themes/moreblue-orbit
	# usplash theme
#	make -C usplash/moreblue-orbit install DESTDIR=$(CURDIR)/debian/usplash-theme-debian-desktop/usr/lib/usplash
	# background files
	mkdir -p $(DESTDIR)/usr/share/images/desktop-base
	$(INSTALL) $(BACKGROUNDS) $(DESTDIR)/usr/share/images/desktop-base
	cd $(DESTDIR)/usr/share/images/desktop-base && ln -s $(DEFAULT_BACKGROUND) default
	# splash files
	$(INSTALL) $(SPLASH) $(DESTDIR)/usr/share/images/desktop-base
	# emblems
	mkdir -p $(DESTDIR)/usr/share/icons/hicolor/48x48/emblems
	$(INSTALL) $(EMBLEMS) $(DESTDIR)/usr/share/icons/hicolor/48x48/emblems/
	# desktop files
	mkdir -p $(DESTDIR)/usr/share/desktop-base
	$(INSTALL) $(DESKTOPFILES) $(DESTDIR)/usr/share/desktop-base/
	# pixmaps files
	mkdir -p $(DESTDIR)/usr/share/pixmaps
	$(INSTALL) $(PIXMAPS) $(DESTDIR)/usr/share/pixmaps/
	# KDM theme
	mkdir -p $(DESTDIR)/etc/default/kdm.d
	$(INSTALL) kdm-theme/kdm.d/10_desktop-base $(DESTDIR)/etc/default/kdm.d
	mkdir -p $(DESTDIR)/usr/share/apps/kdm/themes/debian-moreblue
	$(INSTALL) $(wildcard kdm-theme/debian-moreblue/*) $(DESTDIR)/usr/share/apps/kdm/themes/debian-moreblue
	mkdir -p $(DESTDIR)/usr/share/apps/kdm/themes/moreblue-orbit
	$(INSTALL) $(wildcard kdm-theme/moreblue-orbit/*) $(DESTDIR)/usr/share/apps/kdm/themes/moreblue-orbit
	mkdir -p $(DESTDIR)/usr/share/apps/kdm/themes/nightly
	$(INSTALL) $(wildcard kdm-theme/nightly/*) $(DESTDIR)/usr/share/apps/kdm/themes/nightly
	# KSPLASH theme
	mkdir -p $(DESTDIR)/usr/share/apps/ksplash/Themes/debian-moreblue-default
	$(INSTALL) $(wildcard ksplash-theme/debian-moreblue-default/*) $(DESTDIR)/usr/share/apps/ksplash/Themes/debian-moreblue-default
	mkdir -p $(DESTDIR)/usr/share/apps/ksplash/Themes/debian-moreblue-moodin
	$(INSTALL) $(wildcard ksplash-theme/debian-moreblue-moodin/*) $(DESTDIR)/usr/share/apps/ksplash/Themes/debian-moreblue-moodin
	mkdir -p $(DESTDIR)/usr/share/apps/ksplash/Themes/moreblue-orbit-default
	$(INSTALL) $(wildcard ksplash-theme/moreblue-orbit-default/*) $(DESTDIR)/usr/share/apps/ksplash/Themes/moreblue-orbit-default
	mkdir -p $(DESTDIR)/usr/share/apps/ksplash/Themes/moreblue-orbit-moodin
	$(INSTALL) $(wildcard ksplash-theme/moreblue-orbit-moodin/*) $(DESTDIR)/usr/share/apps/ksplash/Themes/moreblue-orbit-moodin
	mkdir -p $(DESTDIR)/usr/share/apps/ksplash/Themes/nightly-default
	$(INSTALL) $(wildcard ksplash-theme/nightly-default/*) $(DESTDIR)/usr/share/apps/ksplash/Themes/nightly-default
	mkdir -p $(DESTDIR)/usr/share/apps/ksplash/Themes/nightly-moodin
	$(INSTALL) $(wildcard ksplash-theme/nightly-moodin/*) $(DESTDIR)/usr/share/apps/ksplash/Themes/nightly-moodin
	# KDE setup
	mkdir -p $(DESTDIR)/etc/trinity
	$(INSTALL) profiles/kde-profile/kdeglobals $(DESTDIR)/etc/trinity
	mkdir -p $(DESTDIR)/etc/trinity/kdm
	$(INSTALL) profiles/kde-profile/kdm/backgroundrc $(DESTDIR)/etc/trinity/kdm
	mkdir -p $(DESTDIR)/usr/share/desktop-base/profiles/kde-profile/share/config
	$(INSTALL) $(wildcard profiles/kde-profile/share/config/*) $(DESTDIR)/usr/share/desktop-base/profiles/kde-profile/share/config
	# XFCE setup; uses the more general XDG
	mkdir -p $(DESTDIR)/usr/share/desktop-base/profiles/xdg-config/xfce4/mcs_settings
	$(INSTALL) $(wildcard profiles/xdg-config/xfce4/mcs_settings/*) $(DESTDIR)/usr/share/desktop-base/profiles/xdg-config/xfce4/mcs_settings
	mkdir -p $(DESTDIR)/usr/share/desktop-base/profiles/xdg-config/xfce4-session
	$(INSTALL) $(wildcard profiles/xdg-config/xfce4-session/*) $(DESTDIR)/usr/share/desktop-base/profiles/xdg-config/xfce4-session
	# GNOME background descriptor
	mkdir -p $(DESTDIR)/usr/share/gnome-background-properties
	$(INSTALL) gnome-backgrounds.xml $(DESTDIR)/usr/share/gnome-background-properties/debian.xml

