.include </usr/ports/x11/trinity/trinity.port.mk>

VERSION=		0.63
REVISION=		1
PKGNAME=		trinity-dbus-tqt-${VERSION}
PREFIX=			${TDE_PREFIX}

CATEGORIES=		x11/trinity
COMMENT=		Dbus TQT Interface

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/dependencies/
DISTNAME=		trinity-dbus-tqt-14.0.0~pre100+bc50efff
EXTRACT_SUFX=	.tar.gz

BUILD_DEPENDS= 	devel/gmake \
				devel/cmake \
				x11/dbus \
				x11/trinity/dependencies/tqtinterface,-main \
				x11/trinity/dependencies/tqtinterface,-devel

LIB_DEPENDS=	x11/dbus

SHARED_LIBS +=  dbus-tqt-1                0.0

do-configure: tde-cmake-rmbuild
	${TDE_CMAKE_CONFIGURE}

do-build: tde-cmake-build

do-install: tde-cmake-install

.include <bsd.port.mk>
