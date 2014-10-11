VERSION=		1.5.10
REVISION=		1
PKGNAME=		trinity-arts-${VERSION}
PREFIX=			${TDE_PREFIX}

CATEGORIES=		x11/trinity
COMMENT=		aRts (analog realtime synthesizer) - the TDE sound system

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/dependencies/
DISTNAME=		trinity-arts-14.0.0~pre131+04e2524e
EXTRACT_SUFX=	.tar.gz

BUILD_DEPENDS= 	devel/gmake \
				devel/cmake \
				x11/trinity/dependencies/tqtinterface,-devel

LIB_DEPENDS=	devel/libaudiofile \
                devel/glib2 \
                audio/libvorbis \
                audio/libogg \
                audio/libmad \
				x11/trinity/dependencies/tqtinterface,-main \
				x11/trinity/dependencies/tqtinterface,-devel

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

.include </usr/ports/x11/trinity/trinity.port.mk>

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
