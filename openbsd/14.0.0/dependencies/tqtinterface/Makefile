.include </usr/ports/x11/trinity/trinity.port.mk>

PKGNAME=		trinity-tqtinterface-${VERSION}
VERSION=		4.2.0${PREVERSION}
PREVERSION=		~pre188+15d1da6f

COMMENT=		Trinity QT intefarce
CATEGORIES=		x11/trinity/dependencies
HOMEPAGE=		http://www.trinitydesktop.org/
MAINTAINER=		François Andriot <francois.andriot@free.fr>

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/dependencies/
DISTNAME=		trinity-tqtinterface-${TDE_VERSION}${PREVERSION}
EXTRACT_SUFX=	.tar.gz

PREFIX=			${LOCALBASE}

BUILD_DEPENDS= 	devel/gmake \
				devel/cmake \
				x11/trinity/dependencies/tqt3,-main

SHARED_LIBS=	tqt                       4.2

RUN_DEPENDS=	textproc/gsed \
				shells/bash \
				x11/trinity/dependencies/tqt3,-main
LIB_DEPENDS=	x11/trinity/dependencies/tqt3,-main

# Build
do-configure: tde-cmake-rmbuild
	${TDE_CMAKE_CONFIGURE} \
		-DQTDIR="${LOCALBASE}/share/tqt3" \
		-DQT_INCLUDE_DIR="${LOCALBASE}/include/tqt3" \
		-DQT_LIBRARY_DIR="${LOCALBASE}/lib" \
		-DQT_LIBRARIES="tqt-mt" \
		\
		-DCMAKE_INSTALL_PREFIX="${LOCALBASE}" \
		-DPKGCONFIG_INSTALL_DIR="${LOCALBASE}/lib/pkgconfig" \
		-DINCLUDE_INSTALL_DIR="${LOCALBASE}/include/tqt" \
		-DLIB_INSTALL_DIR="${LOCALBASE}/lib" \
		-DBIN_INSTALL_DIR="${LOCALBASE}/bin" \
		\
		-DCMAKE_LIBRARY_PATH="${LOCALBASE}/lib" \
		-DCMAKE_INCLUDE_PATH="${LOCALBASE}/include" \
		\
		-DWITH_QT3="ON" \
		-DBUILD_ALL="ON" \
		-DUSE_QT3="ON" \
		..

do-build: tde-cmake-build

do-install: tde-cmake-install

post-install:
	# Install 'cmake' modules for development use
	mkdir -p "${WRKINST}${LOCALBASE}/share/cmake/Modules"
	for i in ${WRKDIST}/cmake/modules/*.cmake; do \
		install -m 644 "$$i" "${WRKINST}${LOCALBASE}/share/cmake/Modules"; \
	done
	# Fix path to 'bash'
	gsed -i ${WRKINST}/usr/local/bin/* \
	     -e "s|/bin/bash|/usr/local/bin/bash|" \
	     -e "s|sed |gsed |g"


.include <bsd.port.mk>
