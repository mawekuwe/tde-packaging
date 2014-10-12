.include </usr/ports/x11/trinity/trinity.port.mk>

VERSION=		2.3.22
REVISION=		1
PKGNAME=		trinity-libart-lgpl-${VERSION}
PREFIX=			${TDE_PREFIX}

CATEGORIES=		x11/trinity
COMMENT=		Library of functions for 2D graphics

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/dependencies/
DISTNAME=		trinity-libart-lgpl-14.0.0~pre6+634771a9
EXTRACT_SUFX=	.tar.gz

SHARED_LIBS +=        art_lgpl_2              5.21

CONFIGURE_STYLE ?=      autoconf
AUTOCONF_VERSION ?=     2.69
USE_GMAKE ?=            Yes
CONFIGURE_ARGS +=       --disable-dependency-tracking

SHARED_ONLY =           Yes

.include <bsd.port.mk>
