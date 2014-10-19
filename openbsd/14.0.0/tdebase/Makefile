.include </usr/ports/x11/trinity/trinity.port.mk>

PKGNAME=		trinity-tdebase-${VERSION}
VERSION=		${TDE_VERSION}${PREVERSION}
PREVERSION=		~pre1377+891da4b8

COMMENT=		Trinity Base Programs
CATEGORIES=		x11/trinity
HOMEPAGE=		http://www.trinitydesktop.org/
MAINTAINER=		François Andriot <francois.andriot@free.fr>

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/
DISTNAME=		trinity-tdebase-${TDE_VERSION}${PREVERSION}
EXTRACT_SUFX=	.tar.gz

PREFIX=			${TDE_PREFIX}

RUN_DEPENDS=	devel/desktop-file-utils \
				x11/gtk+2,-guic

BUILD_DEPENDS=	devel/imake \
				devel/gmake \
				devel/cmake

LIB_DEPENDS+=	x11/trinity/dependencies/tqtinterface \
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
	# Remove setuid bit
	cd "${WRKINST}${TDE_PREFIX}/bin" && chmod 0755 kcheckpass tdesud
	# Default user face for TDM
	cd "${WRKINST}${TDE_PREFIX}/share/apps/tdm/pics/users" && cp -f "default2.png" ".default.face.icon"

.include <bsd.port.mk>
