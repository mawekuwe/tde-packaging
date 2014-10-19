.include </usr/ports/x11/trinity/trinity.port.mk>

PKGNAME=		trinity-arts-${VERSION}
VERSION=		1.5.10${PREVERSION}
PREVERSION=		~pre134+62defb77

COMMENT=		aRts (analog realtime synthesizer) - the TDE sound system
CATEGORIES=		x11/trinity/dependencies
HOMEPAGE=		http://www.trinitydesktop.org/
MAINTAINER=		François Andriot <francois.andriot@free.fr>

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/dependencies/
DISTNAME=		trinity-arts-${TDE_VERSION}${PREVERSION}
EXTRACT_SUFX=	.tar.gz

PREFIX=			${TDE_PREFIX}

BUILD_DEPENDS= 	devel/gmake \
				devel/cmake \
				x11/trinity/dependencies/tqtinterface

LIB_DEPENDS=	devel/libaudiofile \
                devel/glib2 \
                audio/libvorbis \
                audio/libogg \
                audio/libmad \
				x11/trinity/dependencies/tqtinterface

WANTLIB = glib-2.0 audiofile mad ogg vorbis

SHARED_LIBS +=  artsc                     0.0
SHARED_LIBS +=  artscbackend              0.0
SHARED_LIBS +=  artsdsp                   0.0
SHARED_LIBS +=  artsdsp_st                0.0
SHARED_LIBS +=  artsflow                  1.0
SHARED_LIBS +=  artsflow_idl              1.0
SHARED_LIBS +=  artsgslplayobject         0.0
SHARED_LIBS +=  artswavplayobject         0.0
SHARED_LIBS +=  gmcop                     1.0
SHARED_LIBS +=  kmedia2                   1.0
SHARED_LIBS +=  kmedia2_idl               1.0
SHARED_LIBS +=  mcop                      1.0
SHARED_LIBS +=  mcop_mt                   1.0
SHARED_LIBS +=  qtmcop                    1.0
SHARED_LIBS +=  soundserver_idl           1.0


do-configure: tde-cmake-rmbuild
	${TDE_CMAKE_CONFIGURE} \
		-DINCLUDE_INSTALL_DIR="${TDE_PREFIX}/include/tde/arts" \
		\
		-DWITH_ALSA=OFF \
		-DWITH_AUDIOFILE=ON \
		-DWITH_VORBIS=ON \
		-DWITH_MAD=ON \
		-DWITH_ESOUND=OFF \
		-DWITH_JACK=OFF \
		-DWITH_SNDIO=ON

do-build: tde-cmake-build

do-install: tde-cmake-install


.include <bsd.port.mk>
