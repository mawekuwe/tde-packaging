.include </usr/ports/x11/trinity/trinity.port.mk>

PKGNAME=		trinity-libart-lgpl-${VERSION}
VERSION=		2.3.22${PREVERSION}
PREVERSION=		~pre6+634771a9

COMMENT=		Library of functions for 2D graphics
CATEGORIES=		x11/trinity/dependencies
HOMEPAGE=		http://www.trinitydesktop.org/
MAINTAINER=		François Andriot <francois.andriot@free.fr>

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/dependencies/
DISTNAME=		trinity-libart-lgpl-${TDE_VERSION}${PREVERSION}
EXTRACT_SUFX=	.tar.gz

PREFIX=			${TDE_PREFIX}

SHARED_LIBS +=        art_lgpl_2              5.21

CONFIGURE_STYLE ?=      autoconf
AUTOCONF_VERSION ?=     2.69
USE_GMAKE ?=            Yes
CONFIGURE_ARGS +=       --disable-dependency-tracking

SHARED_ONLY =           Yes

.include <bsd.port.mk>
