# fedora-livecd-tde.ks
#
# Description:
# - Fedora Livecd Spin with the Trinity Desktop Environment (TDE)
# - Based on 'fedora-livecd-kde.ks' provided by Fedora 15
#
# Maintainer(s):
# - Francois Andriot <francois.andriot@free.fr>

%include fedora-live-tde-base.ks
%include fedora-live-minimization.ks

%packages
# Additional packages that are not default in trinity-desktop but useful
trinity-desktop-extras
trinity-live-openbox

# Some TDE applications
trinity-amarok
trinity-digikam
trinity-dolphin
trinity-gtk-qt-engine
trinity-gwenview
trinity-k3b
trinity-kaffeine
trinity-kasablanca
trinity-kbookreader
trinity-kde-style-lipstik
trinity-kgtk-qt3
trinity-kio-umountwrapper
trinity-kwin-style-crystal
#trinity-knetworkmanager
trinity-konversation
trinity-kpowersave
trinity-ksensors
trinity-kstreamripper
trinity-smb4k
trinity-yakuake

# Some TDE translations
trinity-kde-i18n-French
#trinity-kde-i18n-German
#trinity-kde-i18n-Spanish
trinity-kde-i18n-Chinese-Big5


# Fedora stuff
fuse
liveusb-creator


### more desktop stuff
fedora-icon-theme
adwaita-cursor-theme
adwaita-gtk2-theme
adwaita-gtk3-theme

# use yum-presto by default
yum-presto

### space issues

# fonts (we make no bones about admitting we're english-only)
wqy-microhei-fonts	# a compact CJK font, to replace:
-un-core-dotum-fonts	# Korean
-vlgothic-fonts		# Japanese
-wqy-zenhei-fonts	# Chinese

-paratype-pt-sans-fonts	# Cyrillic (already supported by DejaVu), huge
#-stix-fonts		# mathematical symbols

# remove input methods to free space
-@input-methods
-scim*
-m17n*
-ibus*
-iok

# save some space (from @base)
-make
-nss_db

## avoid serious bugs by omitting broken stuff

%end

%post
%end
