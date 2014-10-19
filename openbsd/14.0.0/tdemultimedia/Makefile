.include </usr/ports/x11/trinity/trinity.port.mk>

PKGNAME=		trinity-tdemultimedia-${VERSION}
VERSION=		${TDE_VERSION}${PREVERSION}
PREVERSION=		~pre234+f6ce5119

COMMENT=		Trinity Desktop Environment, multimedia applications
CATEGORIES=		x11/trinity
HOMEPAGE=		http://www.trinitydesktop.org/
MAINTAINER=		François Andriot <francois.andriot@free.fr>

MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/
DISTNAME=		trinity-tdemultimedia-${TDE_VERSION}${PREVERSION}
EXTRACT_SUFX=	.tar.gz

PREFIX=			${TDE_PREFIX}

LIB_DEPENDS =	x11/trinity/tdelibs \
		x11/trinity/dependencies/arts \
		audio/libogg \
		audio/flac \
		audio/libvorbis \
		audio/cdparanoia \
		audio/taglib \
		audio/mpg123 \
		gstreamer->=0.10,<0.11:multimedia/gstreamer-0.10/core \
		devel/libtool,-ltdl \
		multimedia/libtheora \
		audio/akode \
		multimedia/xine-lib

RUN_DEPENDS =	graphics/xanim \
		devel/desktop-file-utils \
		x11/gtk+2,-guic

SEPARATE_BUILD =	flavored
CONFIGURE_ENV +=	aktion_has_xanim=yes

WANTLIB += FLAC>=8 GL ICE SM X11 Xcursor Xdamage Xext Xfixes Xft Xi
WANTLIB += Xinerama Xmu Xrandr Xrender Xt Xv Xxf86dga Xxf86vm akode
WANTLIB += avutil c cdda_interface cdda_paranoia
WANTLIB += drm expat ffi fontconfig freetype glib-2.0 gmodule-2.0
WANTLIB += gobject-2.0 gstreamer-0.10 gthread-2.0 jpeg lcms
WANTLIB += ltdl m mad mng ogg ossaudio pcre
WANTLIB += pcreposix png pthread sndio stdc++ tag theora util
WANTLIB += vorbis vorbisenc vorbisfile xcb xine xml2 z

SHARED_LIBS +=  arts_akode                0.0
SHARED_LIBS +=  arts_audiofile            0.0
SHARED_LIBS +=  arts_xine                 0.0
SHARED_LIBS +=  artsbuilder               0.0
SHARED_LIBS +=  artsgui                   0.0
SHARED_LIBS +=  artsgui_idl               0.0
SHARED_LIBS +=  artsgui_kde               0.0
SHARED_LIBS +=  artsmidi                  0.0
SHARED_LIBS +=  artsmidi_idl              0.0
SHARED_LIBS +=  audiocdplugins            1.0
SHARED_LIBS +=  kcddb                     1.0
SHARED_LIBS +=  noatun                    3.0
SHARED_LIBS +=  noatuncontrols            3.0
SHARED_LIBS +=  noatuntags                3.0
SHARED_LIBS +=  tdemidlib                 0.0
SHARED_LIBS +=  arts_mpeglib-0.3.0        0.3
SHARED_LIBS +=  arts_mpeglib              0.3
SHARED_LIBS +=  arts_splay                0.0

do-configure: tde-autotools-prepare
	${TDE_AUTOTOOLS_CONFIGURE} \
		--with-arts \
		--with-cdparanoia \
		--with-flac \
		--with-theora \
		--with-vorbis \
		--with-gstreamer \
		--without-lame \
		--with-akode \
		--without-musicbrainz \
		--with-taglib \
		--with-xine

do-build: tde-autotools-build

do-install: tde-autotools-install

.include <bsd.port.mk>
