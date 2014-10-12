.include </usr/ports/x11/trinity/trinity.port.mk>

VERSION=		${TDE_VERSION}
REVISION=		1
PKGNAME=		trinity-tdebase-${VERSION}
PREFIX=			${TDE_PREFIX}

CATEGORIES=		x11/trinity
COMMENT=		Trinity Base Programs

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/
DISTNAME=		trinity-tdebase-14.0.0~pre1318+cc12a51c
EXTRACT_SUFX=	.tar.gz

RUN_DEPENDS=	devel/desktop-file-utils \
				x11/gtk+2,-guic

BUILD_DEPENDS=	devel/imake \
				devel/gmake \
				devel/cmake

LIB_DEPENDS+=	x11/trinity/dependencies/tqtinterface,-main \
				x11/trinity/dependencies/arts \
				x11/trinity/tdelibs

LIB_DEPENDS+=	openldap-client->=2,<3:databases/openldap \
				security/cyrus-sasl2 \
				devel/libusb-compat \
				devel/glib2 \
				devel/libconfig \
				net/samba>=3 \
				x11/xscreensaver


SHARED_LIBS +=  kasbar                    1.0
SHARED_LIBS +=  kateinterfaces            0.0
SHARED_LIBS +=  kateutils                 0.0
SHARED_LIBS +=  khotkeys_shared           1.0
SHARED_LIBS +=  kickermain                1.0
SHARED_LIBS +=  kickoffsearch_interfaces  0.0
SHARED_LIBS +=  konq                      4.2
SHARED_LIBS +=  konqsidebarplugin         1.2
SHARED_LIBS +=  ksgrd                     1.2
SHARED_LIBS +=  ksplashthemes             0.0
SHARED_LIBS +=  taskbar                   1.2
SHARED_LIBS +=  taskmanager               1.0
SHARED_LIBS +=  tdecorations              1.0
SHARED_LIBS +=  tdefontinst               0.0
SHARED_LIBS +=  qtkde                     0.0

MULTI_PACKAGES=	-main -konsole -tdm -tdeio-pim-plugins

# Main package
PKGNAME-main=	trinity-tdebase-${VERSION}
COMMENT-main=	
LIB_DEPENDS-main=		x11/trinity/tdelibs
RUN_DEPENDS-main=		x11/trinity/tdebase,-konsole \
						x11/trinity/tdebase,-tdm

# Konsole package
PKGNAME-konsole=		trinity-konsole-${VERSION}
COMMENT-konsole=		X terminal emulator for TDE
LIB_DEPENDS-konsole=	x11/trinity/tdelibs
#RUN_DEPENDS-konsole=	x11/trinity/tdebase,-main

# tdeio-pim-plugins
PKGNAME-tdeio-pim-plugins=	trinity-tdeio-pim-plugins-${VERSION}
COMMENT-tdeio-pim-plugins=	PIM TDEIOslaves from tdebase
LIB_DEPENDS-tdeio-pim-plugins=	x11/trinity/tdelibs

# TDM package
PKGNAME-tdm=			trinity-tdm-${VERSION}
COMMENT-tdm=			X Display manager for TDE
LIB_DEPENDS-tdm=		x11/trinity/tdelibs
#RUN_DEPENDS-tdm=		x11/trinity/tdebase,-main


post-patch:
	cd ${WRKDIST}; \
	gsed -i starttde r14-xdg-update migratekde3 \
	     -e "s| sed| gsed|g"; \
	gsed -i "tdm/kfrontend/gentdmconf.c" \
	     -e "s|. /etc/X11/Xsession|exec \$$session|"

do-configure: tde-cmake-rmbuild
	${TDE_CMAKE_CONFIGURE} \
		-DXSCREENSAVER_DIR="${LOCALBASE}/share/xscreensaver" \
		-DHTDIG_SEARCH_BINARY="${LOCALBASE}/bin/htdig" \
		\
		-DWITH_ALL_OPTIONS=ON \
		-DWITH_SASL=ON \
		-DWITH_LDAP=ON \
		-DWITH_SAMBA=ON \
		-DWITH_OPENEXR=ON \
		-DWITH_XCOMPOSITE=ON \
		-DWITH_XCURSOR=ON \
		-DWITH_XFIXES=ON \
		-DWITH_XRANDR=ON \
		-DWITH_XRENDER=ON \
		-DWITH_LIBCONFIG=ON \
		-DWITH_PCRE=ON \
		-DWITH_XTEST=ON \
		-DWITH_XSCREENSAVER=ON \
		-DWITH_LIBART=ON \
		-DWITH_LIBUSB=ON \
		-DWITH_LIBRAW1394=OFF \
		-DWITH_SUDO_TDESU_BACKEND=OFF \
		-DWITH_SUDO_KONSOLE_SUPER_USER_COMMAND=OFF \
		-DWITH_PAM=OFF \
		-DWITH_SHADOW=OFF \
		-DWITH_XDMCP=ON \
		-DWITH_XINERAMA=ON \
		-DWITH_ARTS=ON \
		-DWITH_I8K=ON \
		-DWITH_SENSORS=OFF \
		-DWITH_HAL=OFF \
		-DWITH_TDEHWLIB=OFF \
		-DWITH_UPOWER=ON \
		-DWITH_ELFICON=OFF \
		-DWITH_KDESKTOP_LOCK_BACKTRACE=OFF \
		\
		-DBUILD_ALL=ON \
		-DBUILD_TSAK=OFF \
		-DBUILD_TDEKBDLEDSYNC=OFF \
		..

do-build: tde-cmake-build

do-install: tde-cmake-install

post-install:
	chmod 0755 ${PREFIX}/bin/kcheckpass
	chmod 0755 ${PREFIX}/bin/tdesud

.include <bsd.port.mk>
