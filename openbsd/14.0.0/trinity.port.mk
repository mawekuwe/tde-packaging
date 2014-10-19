### General information

TDE_VERSION=	14.0.0
TDE_PREFIX=		/opt/trinity

HOMEPAGE=		http://www.trinitydesktop.org/
MAINTAINER=		François Andriot <francois.andriot@free.fr>

PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes

FLAVORS=debug
FLAVOR?=

### General build options

PKG_CONFIG_PATH=/opt/trinity/lib/pkgconfig:/usr/X11R6/lib/pkgconfig:/usr/local/lib/pkgconfig:/usr/lib/pkgconfig

BUILD_DEPENDS=	devel/gmake \
				devel/cmake \
				textproc/gsed \
				shells/bash

### CMAKE related build options

CMAKE_INCLUDE_PATH=/usr/include:/usr/local/include:/usr/X11R6/include
CMAKE_LIBRARY_PATH=/usr/lib:/usr/local/lib:/usr/X11R6/lib

# Build Flags
TDE_FLAGS=${CXXFLAGS} \
	-I${WRKDIST}/libltdl -I/usr/X11R6/include -I/usr/local/include \
	-L/usr/X11R6/lib -L/usr/local/lib \
	 -Wl,-lc -pthread

.if ${FLAVOR:Mdebug}
CMAKE_BUILD_TYPE=Debug
TDE_FLAGS+= -g
.else
CMAKE_BUILD_TYPE=RelWithDebInfo
TDE_FLAGS+= -DNDEBUG
.endif

# Custom configure commands
TDE_BUILD_ENV=\
	export TDEDIR="${TDE_PREFIX}"; \
	export PATH="${TDE_PREFIX}/bin:${PATH}"; \
	export PKG_CONFIG_PATH="${PKG_CONFIG_PATH}"; \
	export CFLAGS="${TDE_FLAGS}"; \
	export CXXFLAGS="${TDE_FLAGS} -Wl,-lstdc++";

TDE_CMAKE_CONFIGURE=\
	${TDE_BUILD_ENV} \
	export CMAKE_INCLUDE_PATH="${CMAKE_INCLUDE_PATH}"; \
	export CMAKE_LIBRARY_PATH="${CMAKE_LIBRARY_PATH}"; \
	cd ${WRKDIST} && mkdir build && cd build && cmake .. \
		-DCMAKE_BUILD_TYPE="${CMAKE_BUILD_TYPE}" \
		-DCMAKE_C_FLAGS="${TDE_FLAGS}" \
		-DCMAKE_CXX_FLAGS="${TDE_FLAGS} -Wl,-lstdc++" \
		-DCMAKE_SKIP_RPATH=OFF \
		-DCMAKE_INSTALL_RPATH="${TDE_PREFIX}/lib" \
		-DCMAKE_VERBOSE_MAKEFILE=ON \
		-DCMAKE_EXTRA_INCLUDE_FILES="pthread.h" \
		\
		-DTDEDIR="${TDE_PREFIX}" \
		-DCMAKE_INSTALL_PREFIX="${TDE_PREFIX}" \
		-DBIN_INSTALL_DIR="${TDE_PREFIX}/bin" \
		-DSHARE_INSTALL_PREFIX="${TDE_PREFIX}/share" \
		-DDOC_INSTALL_DIR="${TDE_PREFIX}/share/doc" \
		-DINCLUDE_INSTALL_DIR="${TDE_PREFIX}/include/tde" \
		-DLIB_INSTALL_DIR="${TDE_PREFIX}/lib" \
		-DPLUGIN_INSTALL_DIR="${TDE_PREFIX}/lib/trinity" \
		-DPKGCONFIG_INSTALL_DIR="${TDE_PREFIX}/lib/pkgconfig"

TDE_AUTOTOOLS_CONFIGURE=\
	${TDE_BUILD_ENV} \
	cd ${WRKDIST} && ./configure \
		--prefix=${TDE_PREFIX} \
		--exec-prefix=${TDE_PREFIX} \
		--bindir=${TDE_PREFIX}/bin \
		--libdir=${TDE_PREFIX}/lib \
		--includedir=${TDE_PREFIX}/include \
		--datadir=${TDE_PREFIX}/share \
		\
		--enable-shared \
		--disable-static \
		--disable-dependency-tracking \
		--disable-debug \
		--enable-final \
		--enable-new-ldflags \
		--enable-closure \
		--enable-rpath \
		--disable-gcc-hidden-visibility \



### Custom build targets for CMAKE
tde-cmake-rmbuild:
	rm -rf "${WRKDIST}/build"

tde-cmake-build:
	${TDE_BUILD_ENV} \
	cd "${WRKDIST}/build" && gmake ${MAKE_FLAGS} || gmake

tde-cmake-install:
	${TDE_BUILD_ENV} \
	cd "${WRKDIST}/build" && gmake install

### Custom build targets for AUTOTOOLS
tde-autotools-prepare:
	cp -f "/usr/local/share/aclocal/libtool.m4" "${WRKDIST}/admin/libtool.m4.in"
	cp "/usr/local/share/libtool/config/ltmain.sh" "${WRKDIST}/admin/ltmain.sh"
	gsed -i "${WRKDIST}/admin/acinclude.m4.in" -e "s|/usr/include/tqt|${LOCALBASE}/include/tqt|g"
	cd "${WRKDIST}" && gmake -f "admin/Makefile.common"

tde-autotools-build:
	${TDE_BUILD_ENV} \
	cd "${WRKDIST}" && gmake ${MAKE_FLAGS} || gmake

tde-autotools-install:
	${TDE_BUILD_ENV} \
	cd "${WRKDIST}" && gmake install
