.include </usr/ports/x11/trinity/trinity.port.mk>

VERSION=		0.9
REVISION=		1
PKGNAME=		trinity-dbus_1_tqt-${VERSION}
PREFIX=			${TDE_PREFIX}

CATEGORIES=		x11/trinity
COMMENT=		dbus TQT Interface

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/dependencies/
DISTNAME=		trinity-dbus-1-tqt-14.0.0~pre114+faf70d2c
EXTRACT_SUFX=	.tar.gz

BUILD_DEPENDS= 	devel/gmake \
				devel/cmake \
				x11/dbus \
				x11/trinity/dependencies/tqtinterface

LIB_DEPENDS=	x11/dbus

SHARED_LIBS +=  dbus-1-tqt                0.0


do-configure: tde-cmake-rmbuild
	${TDE_CMAKE_CONFIGURE}

do-build: tde-cmake-build

do-install: tde-cmake-install

.include <bsd.port.mk>
