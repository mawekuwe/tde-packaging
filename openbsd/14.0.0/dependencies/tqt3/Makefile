PKGNAME=		trinity-tqt3-${VERSION}
VERSION=		3.5.0
DISTNAME=		trinity-tqt3-14.0.0~pre216+d9d3dd45
EXTRACT_SUFX=	.tar.gz

CATEGORIES=		x11/trinity/dependencies
MASTER_SITES=	http://nuc.vtf/tde/tde-tarballs/14.0.0/main/dependencies/

HOMEPAGE=		http://www.trinitydesktop.org/
MAINTAINER=		François Andriot <francois.andriot@free.fr>

SHARED_LIBS =
SHARED_LIBS += tqtdesignercore      1.0
SHARED_LIBS += tqteditor            1.0
SHARED_LIBS += tqassistantclient    1.0
SHARED_LIBS += tqt-mt               35.0
SHARED_LIBS += tqui                 1.0

PROGRAMS3=designer findtr moc qt20fix qtrename140 uic
PROGRAMS=assistant linguist lrelease lupdate qm2ts qmake qtconfig 

# XXX be sure to update the yqt3.port.mk version after a qt bump.
QT_PLUGINS=		plugins-${LIBtqt-mt_VERSION:R}

FLAVORS=debug
FLAVOR?=

# GPL/QPL
PERMIT_PACKAGE_CDROM=	Yes

# For qsettings to write its setup
PORTHOME=	${WRKDIST}

LIB_DEPENDS=	graphics/png \
				graphics/libmng

WANTLIB=	GL GLU ICE SM X11>=10 Xcursor Xext Xft Xi Xinerama \
			Xmu png mng \
			Xrandr Xrender fontconfig freetype jpeg lcms m stdc++ z

BUILD_DEPENDS=	print/cups,-libs \
				devel/gmake


MULTI_PACKAGES+=-main -html -mysql -postgresql -sqlite2


# DEBUG flavor
.if ${FLAVOR:Mdebug}
CONFIGURE_ARGS+=-debug
PKGDEBUG=-debug
.else
PKGDEBUG=
.endif

.include <bsd.port.arch.mk>


# MAIN package
PKGNAME-main=		trinity-tqt3-mt-${VERSION}
REVISION-main= 		1
COMMENT-main=		C++ X11 GUI toolkit
WANTLIB-main=		${WANTLIB} pthread c


# MYSQL package
PKGNAME-mysql=		trinity-tqt3-mysql-${VERSION}
REVISION-mysql= 	1
COMMENT-mysql=		MySQL plugin for tqt3
.if ${BUILD_PACKAGES:M-mysql}
CONFIGURE_ARGS+= -I${LOCALBASE}/include/mysql -L${LOCALBASE}/lib/mysql -plugin-sql-mysql
.else
CONFIGURE_ARGS+=-no-sql-mysql
.endif
LIB_DEPENDS-mysql=	${LIB_DEPENDS} ${BUILD_PKGPATH} databases/mysql
WANTLIB-mysql=		${WANTLIB} mysqlclient tqt-mt


# POSTGRESQL package
PKGNAME-postgresql=	trinity-tqt3-postgresql-${VERSION}
REVISION-postgresql= 	1
COMMENT-postgresql=	PostgresSQL plugin for tqt3
.if ${BUILD_PACKAGES:M-postgresql}
BUILD_DEPENDS+=databases/postgresql,-server
CONFIGURE_ARGS+= -I${LOCALBASE}/include/postgresql \
	    -I${LOCALBASE}/include/postgresql/server \
	    -L${LOCALBASE}/lib \
	    -I${LOCALBASE}/include -plugin-sql-psql
.else
CONFIGURE_ARGS+=-no-sql-psql
.endif
LIB_DEPENDS-postgresql=	${LIB_DEPENDS} ${BUILD_PKGPATH} databases/postgresql
WANTLIB-postgresql=	${WANTLIB} pq


# SQLITE2 package
PKGNAME-sqlite2=	trinity-tqt3-sqlite2-${VERSION}
REVISION-sqlite2= 	1
COMMENT-sqlite2=	sqlite2 plugin for tqt3
.if ${BUILD_PACKAGES:M-sqlite2}
CONFIGURE_ARGS+= -plugin-sql-sqlite
.else
CONFIGURE_ARGS+=-no-sql-sqlite
.endif
LIB_DEPENDS-sqlite2=	${LIB_DEPENDS} ${BUILD_PKGPATH} databases/sqlite
WANTLIB-sqlite2=	${WANTLIB} sqlite


# HTML package
COMMENT-html=		off-line html documentation for tqt3
FULLPKGNAME-html=	trinity-tqt3-html-${VERSION}
FULLPKGPATH-html=	x11/trinity/tqt3,-html
REVISION-html= 		1
LIB_DEPENDS-html=
WANTLIB-html=
PKG_ARCH-html=		*


# for manpages in MESSAGE
SUBST_VARS= QT_PLUGINS

DOCS=	FAQ LICENSE.GPL2 LICENSE.GPL3 README README-QT.TXT \
	changes-3* \
	README.immodule changes.immodule

NO_TEST=	Yes

# Build options.
USE_GROFF =	Yes
MAKE_ENV=	QTDIR="${WRKDIST}" \
			PATH="${WRKDIST}/bin:${PATH}" \
			EXTRA_SAMPLES="${EXTRA_SAMPLES}" \
			SYS_CXX="${CXX}" \
			SYS_CXXFLAGS="${CXXFLAGS}" \
			LD_LIBRARY_PATH="${WRKDIST}/lib"

MAKE_FLAGS=	DESIGNER_SUBDIR=dummy \
		LIBtqt-mt_VERSION=$(LIBtqt-mt_VERSION) \
		LIBtqui_VERSION=$(LIBtqui_VERSION) \
		LIBtqteditor_VERSION=$(LIBtqteditor_VERSION) \
		LIBtqassistantclient_VERSION=$(LIBtqassistantclient_VERSION) \
		LIBtqtdesignercore_VERSION=$(LIBtqtdesignercore_VERSION)

GMAKE=	cd ${WRKDIST} && gmake ${MAKE_ENV} ${MAKE_FLAGS}

# Configuration step.
CONFIGURE_ENV=	QTDIR="${WRKSRC}" \
				PATH=${WRKDIST}/bin:${PATH}; \
				LD_LIBRARY_PATH="${WRKDIST}/lib"

post-patch:
	# fix variables in 'qmake.conf'
	gsed -i ${WRKDIST}/mkspecs/*/qmake.conf \
		-e "s|^QMAKE_INCDIR_QT.*|QMAKE_INCDIR_QT		= /usr/local/include/tqt3|" \
		-e "s|\$\(QTDIR\)|${LOCALBASE}|g" \
		-e "s|-lqt|-ltqt|g" \
		-e "s|^QMAKE_CFLAGS		=.*|QMAKE_CFLAGS		= ${CXXFLAGS}|" \
		-e "s|^QMAKE_INCDIR		=.*|QMAKE_INCDIR		= ${LOCALBASE}/include|" \
		-e "s|^QMAKE_LIBDIR		=.*|QMAKE_LIBDIR		= ${LOCALBASE}/lib|" \
		-e "s|^QMAKE_RPATH		= .*|QMAKE_RPATH		=|" \
		-e "s|^QMAKE_STRIP             =.*|QMAKE_STRIP             =|" \
		-e "s|^QMAKE_STRIPFLAGS_LIB 	+=.*|QMAKE_STRIPFLAGS_LIB 	+=|" \
		-e "s|^QMAKE_MOC		=.*|QMAKE_MOC		= ${LOCALBASE}/bin/tqmoc|" \
		-e "s|^QMAKE_UIC		=.*|QMAKE_UIC		= ${LOCALBASE}/bin/tquic|" \
		-e "s|^QMAKE_INCDIR_QT		=.*|QMAKE_INCDIR_QT		= ${LOCALBASE}/include/tqt3|" \
		-e "s|^QMAKE_LIBDIR_QT		=.*|QMAKE_LIBDIR_QT		= ${LOCALBASE}/lib|"
	gsed -i ${WRKDIST}/mkspecs/openbsd-g++/qmake.conf \
		-e "s|^QMAKE_LFLAGS_SONAME	=.*|QMAKE_LFLAGS_SONAME	=|" \
		-e "s|^CONFIG			+= qt warn_on release link_prl|CONFIG			+= qt warn_on release link_prl thread|"
	echo "QMAKE_OPENBSD_SHLIBS	= 1" >>"${WRKDIST}/mkspecs/openbsd-g++/qmake.conf"

do-configure:
	cd ${WRKDIST} && echo yes | ./configure \
		${CONFIGURE_ARGS} \
		-I${X11BASE}/include/freetype2 \
		-I${LOCALBASE}/include \
		-L${WRKSRC}/lib \
		-L${LOCALBASE}/lib \
		\
		-prefix			"${LOCALBASE}" \
		-headerdir		"${LOCALBASE}/include/tqt3" \
		-libdir			"${LOCALBASE}/lib" \
		-plugindir		"${LOCALBASE}/lib/tqt3/plugins" \
		-datadir		"${LOCALBASE}/share/tqt3" \
		-docdir			"${LOCALBASE}/share/doc/tqt3" \
		-translationdir	"${LOCALBASE}/share/tqt3/translations" \
		-sysconfdir		"/etc/tqt3" \
		\
		-thread \
		-shared \
		-fast \
		-no-exceptions \
		-platform openbsd-g++ \
		\
		-no-pch \
		-cups \
		-stl \
		-ipv6 \
		\
		-sm \
		-xshape				\
		-xinerama			\
		-xcursor			\
		-xrandr				\
		-xrender			\
		-xft				\
		-tablet				\
		-xkb				\
		\
		-system-zlib			\
		-system-libpng			\
		-system-libmng			\
		-system-libjpeg			\
		-no-nas-sound		\
		\
		-enable-opengl			\
		-dlopen-opengl			\
		\
		-qt-gif				\
		-qt-imgfmt-mng \
		-qt-imgfmt-png			\
		-qt-imgfmt-jpeg			\
		-plugin-imgfmt-mng		\
		\
		-no-sql-odbc		\
		-no-sql-ibase		\
		-no-sql-sqlite3		\
		\
		-lfontconfig			\
		-inputmethod			\
		-glibmainloop \
		-v


# Build step.
do-build:
	# proceed
	${GMAKE} sub-src sub-plugins sub-tools

	# build tqtconv2ui
	${GMAKE} -C tools/designer/tools/tqtconv2ui

	# build tqvfb
	${GMAKE} -C tools/tqvfb

	# fix .prl files
	gsed -i ${WRKDIST}/lib/*.prl -e "s|${WRKDIST}|${LOCALBASE}/share/tqt3|g"


# Installation step.
pre-install:
	# Clean up patch residual files
	find ${WRKDIST} -name "*.orig" | xargs rm -f

do-install:
	# Installs 'libtqt-mt.so.3' library
	${GMAKE} -C src INSTALL_ROOT=${WRKINST} install_target

	# Installs all the remaining
	${GMAKE} INSTALL_ROOT=${WRKINST} install
	${GMAKE} INSTALL_ROOT=${WRKINST} plugins-install

	install -m755 ${WRKDIST}/bin/tqtrename140 ${WRKINST}${LOCALBASE}/bin
	install -m755 ${WRKDIST}/bin/tqt20fix ${WRKINST}${LOCALBASE}/bin
	install -m755 ${WRKDIST}/bin/tqtfindtr ${WRKINST}${LOCALBASE}/bin

	# install tqtconv2ui
	install -m755 ${WRKDIST}/bin/tqtconv2ui ${WRKINST}${LOCALBASE}/bin/tqtconv2ui

	# install tqvfb
	install -m755 ${WRKDIST}/tools/tqvfb/tqvfb ${WRKINST}${LOCALBASE}/bin/tqvfb
	
.include <bsd.port.mk>
