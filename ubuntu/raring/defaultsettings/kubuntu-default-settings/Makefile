FPACKAGE = kubuntu-default-settings-trinity
VERSION = 5.03

WALLPAPER_DIR = $(DESTDIR)/usr/share/wallpapers
SOUNDS_DIR = $(DESTDIR)/usr/share/sounds
KICKER_DIR = $(DESTDIR)/usr/share/apps/kicker
KONQ_TILES_DIR = $(DESTDIR)/usr/share/apps/konqueror/tiles
TDM_THEME_DIR = $(DESTDIR)/opt/trinity/share/apps/tdm/themes/kubuntu-trinity
TDM_THEME_NO_USERLIST_DIR = $(DESTDIR)/opt/trinity/share/apps/tdm/themes/kubuntu-no-userlist-trinity
TDM_OVERRIDE = $(DESTDIR)/etc/default/tdm-trinity.d/
TDM_SETTINGS_DIR = $(DESTDIR)/etc/trinity/tdm/
KSPLASH_THEME_DIR = $(DESTDIR)/opt/trinity/share/apps/ksplash/Themes/kubuntu
SETTINGS_DIR = $(DESTDIR)/usr/share/kubuntu-default-settings-trinity
CURSOR_DIR = $(DESTDIR)/usr/share/icons/contrastlarge

build:

clean:

install:
	mkdir -p "$(TDM_SETTINGS_DIR)"
	install -m644 backgroundrc "$(TDM_SETTINGS_DIR)"
	install -m644 tdmdistrc "$(TDM_SETTINGS_DIR)"

	mkdir -p "$(WALLPAPER_DIR)"
	install -m644 artwork/kubuntu-wallpaper.png  "$(WALLPAPER_DIR)"
	install -m644 artwork/kubuntu-wallpaper.png.desktop  "$(WALLPAPER_DIR)"
	install -m644 artwork/kubuntu-intrepid-wallpaper.jpg  "$(WALLPAPER_DIR)"
	install -m644 artwork/kubuntu-hardy-wallpaper.jpg  "$(WALLPAPER_DIR)"

	mkdir -p "$(WALLPAPER_DIR)/Air"
	install -m644 artwork/intrepid_wallpapers/Air/1024x768.jpg "$(WALLPAPER_DIR)/Air"
	install -m644 artwork/intrepid_wallpapers/Air/1280x1024.jpg "$(WALLPAPER_DIR)/Air"
	install -m644 artwork/intrepid_wallpapers/Air/1280x800.jpg "$(WALLPAPER_DIR)/Air"
	install -m644 artwork/intrepid_wallpapers/Air/1440x900.jpg "$(WALLPAPER_DIR)/Air"
	install -m644 artwork/intrepid_wallpapers/Air/1600x1200.jpg "$(WALLPAPER_DIR)/Air"
	install -m644 artwork/intrepid_wallpapers/Air/1920x1080.jpg "$(WALLPAPER_DIR)/Air"
	install -m644 artwork/intrepid_wallpapers/Air/1920x1200.jpg "$(WALLPAPER_DIR)/Air"

	mkdir -p "$(SOUNDS_DIR)"
	install -m644 artwork/kubuntu-login.ogg  "$(SOUNDS_DIR)"

	mkdir -p "$(KONQ_TILES_DIR)"
	install -m644 artwork/kubuntu-konqueror-background.png  "$(KONQ_TILES_DIR)"
	install -m644 artwork/kubuntu-konqueror-background-classic.png  "$(KONQ_TILES_DIR)"

	mkdir -p "$(KICKER_DIR)/pics"
	install -m644 artwork/kubuntu-kmenu-side.png  "$(KICKER_DIR)/pics/"
	install -m644 artwork/kubuntu-kmenu-side-tile.png  "$(KICKER_DIR)/pics/"
	mkdir -p "$(KICKER_DIR)/wallpapers"
	install -m644 artwork/kubuntu-panel.png  "$(KICKER_DIR)/wallpapers/"

	mkdir -p "$(TDM_THEME_DIR)"
	install -m644 artwork/tdm-theme/*  "$(TDM_THEME_DIR)"

	mkdir -p "$(TDM_THEME_NO_USERLIST_DIR)"
	install -m644 artwork/tdm-theme-cartoon-no-userlist/*  "$(TDM_THEME_NO_USERLIST_DIR)"

	mkdir -p "$(KSPLASH_THEME_DIR)"
	install -m644 artwork/ksplash/*  "$(KSPLASH_THEME_DIR)"
	ln -s /usr/share/wallpapers/kubuntu-wallpaper.jpg "$(KSPLASH_THEME_DIR)/Background.jpg"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/metabar/themes/kubuntu"
	install -m644 artwork/metabar/*  "$(SETTINGS_DIR)/kde-profile/default/share/apps/metabar/themes/kubuntu"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/amarok/themes/kubuntu"
	install -m644 artwork/amarok/*  "$(SETTINGS_DIR)/kde-profile/default/share/apps/amarok/themes/kubuntu"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/konversation/themes/oxygen"
	install -m644 artwork/konversation/*  "$(SETTINGS_DIR)/kde-profile/default/share/apps/konversation/themes/oxygen"

	mkdir -p "$(DESTDIR)/etc"
	install -m644 kde-profile/kderc "$(DESTDIR)/etc"
	install -m644 kde-profile/kde4rc "$(DESTDIR)/etc"
	install -m644 kde-profile/kde-user-profile "$(DESTDIR)/etc"

	mkdir -p "$(DESTDIR)/etc/qt3"
	install -m644 qt-rc-files/*rc "$(DESTDIR)/etc/qt3"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/config/"
	install -m644 kde-rc-files/*rc "$(SETTINGS_DIR)/kde-profile/default/share/config/"
	install -m644 kde-rc-files/uiserver "$(SETTINGS_DIR)/kde-profile/default/share/config/"
	install -m644 kde-rc-files/kdeglobals "$(SETTINGS_DIR)/kde-profile/default/share/config/"
	install -m644 kde-rc-files/cryptodefaults "$(SETTINGS_DIR)/kde-profile/default/share/config/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/tdedisplay/color-schemes/"
	install -m644 colour-schemes/*rc "$(SETTINGS_DIR)/kde-profile/default/share/apps/tdedisplay/color-schemes/"

	mkdir -p "$(CURSOR_DIR)/cursors"
	install -m644 cursors/index.theme "$(CURSOR_DIR)/"
	mkdir -p "$(CURSOR_DIR)cursors/"
	install -m644 cursors/contrastlarge/cursors/* "$(CURSOR_DIR)/cursors/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/konqueror/"
	install -m644 ui-rc-files/konqueror.rc "$(SETTINGS_DIR)/kde-profile/default/share/apps/konqueror/"
#	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/konversation/"
#	install -m644 ui-rc-files/konversationui.rc "$(SETTINGS_DIR)/kde-profile/default/share/apps/konversation/"
	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/kopete/"
	install -m644 ui-rc-files/kopetechatwindow.rc "$(SETTINGS_DIR)/kde-profile/default/share/apps/kopete/"
	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/gwenview/"
	install -m644 ui-rc-files/gwenviewui.rc "$(SETTINGS_DIR)/kde-profile/default/share/apps/gwenview/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/konqueror/servicemenus/"
	mkdir -p "$(DESTDIR)/usr/bin"
	install -m644 konqueror-profile/konq_plugins.xml "$(SETTINGS_DIR)/kde-profile/default/share/apps/konqueror/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/16x16/actions/"
	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/22x22/actions/"
	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/32x32/actions/"
	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/48x48/actions/"
	install -m644 artwork/throbber/16x16/kde.png "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/16x16/actions/"
	install -m644 artwork/throbber/22x22/kde.png "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/22x22/actions/"
	install -m644 artwork/throbber/32x32/kde.png "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/32x32/actions/"
	install -m644 artwork/throbber/48x48/kde.png "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/48x48/actions/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/64x64/actions/"
	install -m644 kaffeine/fileopen64.png "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/64x64/actions/fileopen.png"
	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/128x128/actions/"
	install -m644 kaffeine/fileopen128.png "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/128x128/actions/fileopen.png"
	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/icons/crystalsvg/scalable/actions/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/kaffeine/"
	install -m644 kaffeine/wizard_stamp_v0.7.1 "$(SETTINGS_DIR)/kde-profile/default/share/apps/kaffeine"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/kpdfpart/"
	install -m644 kpart-rc-files/part.rc "$(SETTINGS_DIR)/kde-profile/default/share/apps/kpdfpart/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/gvimagepart/"
	install -m644 kpart-rc-files/gvimagepart.rc "$(SETTINGS_DIR)/kde-profile/default/share/apps/gvimagepart/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/ark/"
	install -m644 kpart-rc-files/ark_part.rc "$(SETTINGS_DIR)/kde-profile/default/share/apps/ark/"
	install -m644 kpart-rc-files/ark_part_readonly.rc "$(SETTINGS_DIR)/kde-profile/default/share/apps/ark/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/ksvg/"
	install -m644 kpart-rc-files/ksvgplugin.rc "$(SETTINGS_DIR)/kde-profile/default/share/apps/ksvg/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/tdehtml/"
	install -m644 kpart-rc-files/tdehtml_browser.rc "$(SETTINGS_DIR)/kde-profile/default/share/apps/tdehtml/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/mimelnk/application/"
	install -m644 mimelnk/x-tar.desktop "$(SETTINGS_DIR)/kde-profile/default/share/mimelnk/application/"
	install -m644 mimelnk/x-tarz.desktop "$(SETTINGS_DIR)/kde-profile/default/share/mimelnk/application/"
	install -m644 mimelnk/x-tbz.desktop "$(SETTINGS_DIR)/kde-profile/default/share/mimelnk/application/"
	install -m644 mimelnk/x-tgz.desktop "$(SETTINGS_DIR)/kde-profile/default/share/mimelnk/application/"
	install -m644 mimelnk/x-zip.desktop "$(SETTINGS_DIR)/kde-profile/default/share/mimelnk/application/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/konqiconview/kpartplugins/"
	install -m644 kpart-plugins/dirfilterplugin.rc "$(SETTINGS_DIR)/kde-profile/default/share/apps/konqiconview/kpartplugins/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/tdewallet/"
	install -m644 tdewallet-default-wallet/kdewallet.kwl "$(SETTINGS_DIR)/kde-profile/default/share/apps/tdewallet/"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/default/share/apps/kwin/"
	install -m644 artwork/window-decoration-gradient.png "$(SETTINGS_DIR)/kde-profile/default/share/apps/kwin/"
	install -m644 artwork/window-decoration-gradient-inactive.png "$(SETTINGS_DIR)/kde-profile/default/share/apps/kwin/"

	install -m644 gtk-qt-engine-rc-files/gtkrc-2.0-kde "$(SETTINGS_DIR)/.gtkrc-2.0-kde"
	install -m644 gtk-qt-engine-rc-files/gtk-qt-engine.rc.sh "$(SETTINGS_DIR)/gtk-qt-engine.rc.sh"
	install -m644 hal/hal-policy-ntfs-config-write-policy.fdi "$(SETTINGS_DIR)/hal-policy-ntfs-config-write-policy.fdi"

	mkdir -p "$(SETTINGS_DIR)/kde-profile/lesser-visual-impairment/share/config/"
	cp -r accessibility/lesser-visual-impairment/* "$(SETTINGS_DIR)/kde-profile/lesser-visual-impairment/share/config/"
	mkdir -p "$(SETTINGS_DIR)/kde-profile/moderate-visual-impairment/share/config/"
	cp -r accessibility/moderate-visual-impairment/* "$(SETTINGS_DIR)/kde-profile/moderate-visual-impairment/share/config/"
	mkdir -p "$(SETTINGS_DIR)/kde-profile/minor-motor-difficulties/share/config/"
	cp -r accessibility/minor-motor-difficulties/* "$(SETTINGS_DIR)/kde-profile/minor-motor-difficulties/share/config/"
	mkdir -p "$(SETTINGS_DIR)/kde-profile/motor-difficulties-pointing-devices/share/config/"
	cp -r accessibility/motor-difficulties-pointing-devices/* "$(SETTINGS_DIR)/kde-profile/motor-difficulties-pointing-devices/share/config/"
	mkdir -p "$(SETTINGS_DIR)/kde-profile/motor-difficulties-pointing-devices/share/Autostart/"
	ln -s /usr/bin/kmousetool "$(SETTINGS_DIR)/kde-profile/motor-difficulties-pointing-devices/share/Autostart/kmousetool"

	mkdir -p "$(DESTDIR)/etc/kubuntu-default-settings-trinity"
	install -m644 kde-hidden/hidden-media "$(DESTDIR)/etc/kubuntu-default-settings-trinity/"
	install -m644 kde-hidden/directory-media "$(DESTDIR)/etc/kubuntu-default-settings-trinity/"
	install -m644 kde-hidden/directory-home "$(DESTDIR)/etc/kubuntu-default-settings-trinity/"

	#mkdir -p "$(SETTINGS_DIR)/kde4-profile/default/share/apps/desktoptheme/slim-glow"
	#cp -rf kde4/artwork/desktoptheme/* "$(SETTINGS_DIR)/kde4-profile/default/share/apps/desktoptheme/slim-glow/"

	mkdir -p "$(SETTINGS_DIR)/kde4-profile/default/share/config"
	install -m644 kde4/kde-rc-files/*rc "$(SETTINGS_DIR)/kde4-profile/default/share/config/"
	install -m644 kde4/kde-rc-files/cryptodefaults "$(SETTINGS_DIR)/kde4-profile/default/share/config/"

	mkdir -p "$(DESTDIR)/usr/lib/kde4/etc/kde4/"
	install -m644 kde4/kde-rc-files/kdeglobals "$(DESTDIR)/usr/lib/kde4/etc/kde4/"

