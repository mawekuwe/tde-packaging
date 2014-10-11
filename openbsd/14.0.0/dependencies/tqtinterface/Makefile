.include </usr/ports/x11/trinity/trinity.port.mk>

VERSION=		${TDE_VERSION}
REVISION=		1
PKGNAME=		trinity-tqtinterface-${VERSION}
PREFIX=			${LOCALBASE}

CATEGORIES=		x11/trinity

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/dependencies/
DISTNAME=		trinity-tqtinterface-14.0.0~pre185+b79cc765
EXTRACT_SUFX=	.tar.gz

BUILD_DEPENDS= 	devel/gmake \
				devel/cmake \
				x11/trinity/dependencies/tqt3,-main

SHARED_LIBS=			tqt                       4.2

MULTI_PACKAGES=	-main -devel

# Main package
PKGNAME-main=			trinity-tqtinterface-${VERSION}
COMMENT-main=			Trinity QT intefarce
RUN_DEPENDS-main=		textproc/gsed \
						shells/bash \
						x11/trinity/dependencies/tqt3,-main
LIB_DEPENDS-main=		x11/trinity/dependencies/tqt3,-main

# Development package
PKGNAME-devel=			trinity-tqtinterface-devel-${VERSION}
COMMENT-devel=			development files for Trinity QT interface
LIB_DEPENDS-devel=		${BUILD_PKGPATH},-main
RUN_DEPENDS-devel=		x11/trinity/dependencies/tqt3,-main

# Build
do-configure: tde-cmake-rmbuild
	${TDE_CMAKE_CONFIGURE} \
		-DQTDIR="${LOCALBASE}/share/tqt3" \
		-DQT_INCLUDE_DIR="${LOCALBASE}/include/tqt3" \
		-DQT_LIBRARY_DIR="${LOCALBASE}/lib" \
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
