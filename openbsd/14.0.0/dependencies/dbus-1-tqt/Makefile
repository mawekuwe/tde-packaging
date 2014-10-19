.include </usr/ports/x11/trinity/trinity.port.mk>

PKGNAME=		trinity-dbus_1_tqt-${VERSION}
VERSION=		0.9${PREVERSION}
PREVERSION=		~pre120+0add2f9a

COMMENT=		dbus TQT Interface
CATEGORIES=		x11/trinity/dependencies
HOMEPAGE=		http://www.trinitydesktop.org/
MAINTAINER=		François Andriot <francois.andriot@free.fr>

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/dependencies/
DISTNAME=		trinity-dbus-1-tqt-${TDE_VERSION}${PREVERSION}
EXTRACT_SUFX=	.tar.gz

PREFIX=			${TDE_PREFIX}

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
