# Copied from 'fedora-live-kde-base.ks'

%include fedora-live-base.ks
repo --name=trinity --baseurl=http://trinity.mangafrance.com/f$releasever/trinity-3.5.13/RPMS/$basearch
repo --name=trinity-noarch --baseurl=http://trinity.mangafrance.com/f$releasever/trinity-3.5.13/RPMS/noarch
repo --name=trinity-extras --baseurl=http://trinity.mangafrance.com/f$releasever/trinity-extras/RPMS/$basearch
repo --name=trinity-extras-noarch --baseurl=http://trinity.mangafrance.com/f$releasever/trinity-extras/RPMS/noarch

%packages

### The KDE-Desktop

trinity-desktop


### fixes

# make sure alsaunmute is there
alsa-utils

# make sure gnome-packagekit doesn't end up the KDE live images
-gnome-packagekit*

%end


%post

# create /etc/sysconfig/desktop (needed for installation)
cat > /etc/sysconfig/desktop <<EOF
DESKTOP="KDE"
DISPLAYMANAGER="/opt/trinity/bin/kdm"
EOF

# make oxygen-gtk the default GTK+ 2 theme for root (see #683855, #689070)
cat > /root/.gtkrc-2.0 << EOF
include "/usr/share/themes/oxygen-gtk/gtk-2.0/gtkrc"
include "/etc/gtk-2.0/gtkrc"
gtk-theme-name="oxygen-gtk"
EOF

# add initscript
cat >> /etc/rc.d/init.d/livesys << EOF

if [ -e /usr/share/icons/hicolor/96x96/apps/fedora-logo-icon.png ] ; then
    # use image also for kdm
    mkdir -p /usr/share/apps/kdm/faces
    cp /usr/share/icons/hicolor/96x96/apps/fedora-logo-icon.png /usr/share/apps/kdm/faces/fedora.face.icon
fi

# make liveuser use KDE
echo "/opt/trinity/bin/startkde" > /home/liveuser/.xsession
chmod a+x /home/liveuser/.xsession
chown liveuser:liveuser /home/liveuser/.xsession

# set up autologin for user liveuser
sed -i 's/#AutoLoginEnable=true/AutoLoginEnable=true/' /opt/trinity/share/config/kdm/kdmrc
sed -i 's/#AutoLoginUser=fred/AutoLoginUser=liveuser/' /opt/trinity/share/config/kdm/kdmrc

# set up user liveuser as default user and preselected user
sed -i 's/#PreselectUser=Default/PreselectUser=Default/' /opt/trinity/share/config/kdm/kdmrc
sed -i 's/#DefaultUser=johndoe/DefaultUser=liveuser/' /opt/trinity/share/config/kdm/kdmrc

# add liveinst.desktop to favorites menu
mkdir -p /home/liveuser/.trinity/share/config/

# show liveinst.desktop on desktop and in menu
sed -i 's/NoDisplay=true/NoDisplay=false/' /usr/share/applications/liveinst.desktop

# chmod +x ~/Desktop/liveinst.desktop to disable KDE's security warning
chmod +x /usr/share/applications/liveinst.desktop

# copy over the icons for liveinst to hicolor
cp /usr/share/icons/gnome/16x16/apps/system-software-install.png /usr/share/icons/hicolor/16x16/apps/
cp /usr/share/icons/gnome/22x22/apps/system-software-install.png /usr/share/icons/hicolor/22x22/apps/
cp /usr/share/icons/gnome/24x24/apps/system-software-install.png /usr/share/icons/hicolor/24x24/apps/
cp /usr/share/icons/gnome/32x32/apps/system-software-install.png /usr/share/icons/hicolor/32x32/apps/
cp /usr/share/icons/gnome/48x48/apps/system-software-install.png /usr/share/icons/hicolor/48x48/apps/
cp /usr/share/icons/gnome/256x256/apps/system-software-install.png /usr/share/icons/hicolor/256x256/apps/
touch /usr/share/icons/hicolor/

# Create user Desktop directory
mkdir -p /home/liveuser/Desktop

# make sure to set the right permissions and selinux contexts
chown -R liveuser:liveuser /home/liveuser/
restorecon -R /home/liveuser/

# don't use prelink on a running KDE live image
sed -i 's/PRELINKING=yes/PRELINKING=no/' /etc/sysconfig/prelink

EOF

%end
