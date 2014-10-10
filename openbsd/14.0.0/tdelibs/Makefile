.include </usr/ports/x11/trinity/trinity.port.mk>

VERSION=		${TDE_VERSION}
REVISION=		1
PKGNAME=		trinity-tdelibs-${VERSION}
PREFIX=			${TDE_PREFIX}

CATEGORIES=		x11/trinity
COMMENT=		TDE Libraries

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/
DISTNAME=		trinity-tdelibs-14.0.0~pre899+9a6735bb
EXTRACT_SUFX=	.tar.gz

RUN_DEPENDS=	devel/desktop-file-utils \
				x11/gtk+2,-guic

BUILD_DEPENDS=	devel/imake \
				devel/gmake \
				devel/cmake

LIB_DEPENDS+=	x11/trinity/dependencies/tqtinterface,-main \
				x11/trinity/dependencies/arts \
				x11/trinity/dependencies/dbus-tqt \
				x11/trinity/dependencies/dbus-1-tqt \
				x11/trinity/dependencies/libart-lgpl

LIB_DEPENDS+=	archivers/bzip2 \
				devel/libidn \
				devel/pcre \
				graphics/jasper \
				graphics/openexr \
				graphics/tiff \
				net/avahi \
				print/cups \
				print/freetype \
				sysutils/gamin \
				sysutils/upower \
				textproc/aspell/core \
				textproc/libxslt>=1.0.10

SHARED_LIBS +=  DCOP                      14.0
SHARED_LIBS +=  artskde                   1.2
SHARED_LIBS +=  connectionmanager         0.0
SHARED_LIBS +=  katepartinterfaces        0.0
SHARED_LIBS +=  kglib                     0.0
SHARED_LIBS +=  kjava                     1.0
SHARED_LIBS +=  kjs                       1.2
SHARED_LIBS +=  networkstatus             0.0
SHARED_LIBS +=  tdeabc                    1.2
SHARED_LIBS +=  tdeabc_dir                1.0
SHARED_LIBS +=  tdeabc_file               1.0
SHARED_LIBS +=  tdeabc_ldaptdeio          1.0
SHARED_LIBS +=  tdeabc_net                1.0
SHARED_LIBS +=  tdecore                   14.0
SHARED_LIBS +=  tdednssd                  1.0
SHARED_LIBS +=  tdefakes                  14.0
SHARED_LIBS +=  tdefx                     14.0
SHARED_LIBS +=  tdehtml                   14.0
SHARED_LIBS +=  tdeimproxy                0.0
SHARED_LIBS +=  tdeio                     14.0
SHARED_LIBS +=  tdemdi                    1.0
SHARED_LIBS +=  tdemdi2                   1.0
SHARED_LIBS +=  tdemediaplayer            0.0
SHARED_LIBS +=  tdemid                    0.0
SHARED_LIBS +=  tdenewstuff               1.0
SHARED_LIBS +=  tdentlm                   0.0
SHARED_LIBS +=  tdeparts                  2.1
SHARED_LIBS +=  tdeprint                  14.0
SHARED_LIBS +=  tdeprint_management       14.0
SHARED_LIBS +=  tderandr                  0.0
SHARED_LIBS +=  tderesources              1.2
SHARED_LIBS +=  tdersync                  0.0
SHARED_LIBS +=  tdesasl                   1.2
SHARED_LIBS +=  tdescreensaver            14.0
SHARED_LIBS +=  tdescript                 0.0
SHARED_LIBS +=  tdespell                  14.0
SHARED_LIBS +=  tdespell2                 1.0
SHARED_LIBS +=  tdesu                     14.0
SHARED_LIBS +=  tdetexteditor             0.0
SHARED_LIBS +=  tdeui                     14.0
SHARED_LIBS +=  tdeunittest               1.0
SHARED_LIBS +=  tdeutils                  1.2
SHARED_LIBS +=  tdewalletbackend          1.0
SHARED_LIBS +=  tdewalletclient           1.0
SHARED_LIBS +=  vcard                     0.0

post-patch:
	cd ${WRKDIST}; \
	gsed -i cmake/install_apidox \
	        cmake/generate_apidox \
	        kate/data/mel.xml \
	        kdoctools/update-entities.sh \
	        tderandr/libtderandr.cc \
	     -e "s|/bin/bash|${LOCALBASE}/bin/bash|g"; \


do-configure: tde-cmake-rmbuild
	${TDE_CMAKE_CONFIGURE} \
		-DDBUS_SYSTEM_CONF_DIRECTORY="${LOCALBASE}/share/dbus-1/system-services" \
		\
		-DWITH_ALL_OPTIONS=ON \
		-DWITH_ARTS=ON \
		-DWITH_ALSA=OFF \
		-DWITH_LIBART=ON \
		-DWITH_LIBIDN=ON \
		-DWITH_SSL=ON \
		-DWITH_CUPS=ON \
		-DWITH_LUA=OFF \
		-DWITH_TIFF=ON \
		-DWITH_JASPER=ON \
		-DWITH_OPENEXR=ON \
		-DWITH_UTEMPTER=OFF \
		-DWITH_ELFICON=OFF \
		-DWITH_AVAHI=ON \
		-DWITH_PCRE=ON \
		-DWITH_INOTIFY=OFF \
		-DWITH_GAMIN=ON \
		-DWITH_TDEHWLIB=OFF \
		-DWITH_TDEHWLIB_DAEMONS=OFF \
		-DWITH_HAL=OFF \
		-DWITH_DEVKITPOWER=OFF \
		-DWITH_LOGINDPOWER=OFF \
		-DWITH_UPOWER=ON \
		-DWITH_UDISKS=OFF \
		-DWITH_UDISKS2=OFF \
		-DWITH_CONSOLEKIT=ON \
		-DWITH_NETWORK_MANAGER_BACKEND=OFF \
		-DWITH_SUDO_TDESU_BACKEND=OFF \
		-DWITH_OLD_XDG_STD=OFF \
		-DWITH_LZMA=ON \
		-DWITH_LIBBFD=OFF \
		-DWITH_XRANDR=ON \
		-DWITH_XCOMPOSITE=ON \
		-DWITH_KDE4_MENU_SUFFIX=OFF \
		\
		-DWITH_ASPELL=ON \
		-DWITH_HSPELL=OFF \
		-DWITH_TDEICONLOADER_DEBUG=OFF \
		..

do-build: tde-cmake-build

do-install: tde-cmake-install
	# Remove setuid bit
	chmod 0755 ${PREFIX}/bin/fileshareset
	chmod 0755 ${PREFIX}/bin/kgrantpty
	chmod 0755 ${PREFIX}/bin/kpac_dhcp_helper

.include <bsd.port.mk>
