# Created by: Bill Fumerola <billf@chc-chimes.com>
# $FreeBSD$

PORTNAME=	htdig
PORTVERSION=	3.2.0.b6
PORTREVISION=	5
CATEGORIES=	textproc www x11/trinity
MASTER_SITES=	http://downloads.sourceforge.net/project/htdig/htdig/3.2.0b6/
DISTNAME=	htdig-3.2.0b6

MAINTAINER=	ports@FreeBSD.org
COMMENT=	WWW indexing and searching system

PERMIT_PACKAGE_CDROM=	Yes

CONFIGURE_STYLE=gnu
GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--with-config-dir=${PREFIX}/etc/htdig \
		--with-default-config-file=${PREFIX}/etc/htdig/htdig.conf \
		--with-common-dir=${PREFIX}/share/htdig/common \
		--with-database-dir=${PREFIX}/share/htdig/database \
		--with-cgi-bin-dir=${PREFIX}/www/cgi-bin \
		--with-search-dir=${PREFIX}/www/data \
		--with-image-dir=${PREFIX}/www/icons/htdig \
		--with-image-url-prefix=/icons/htdig \
		--with-ssl
USES=		libtool
USE_LDCONFIG=	yes

OPTIONS_DEFINE=	APACHE DOCS
OPTIONS_DEFAULT=	APACHE

APACHE_USE=	APACHE=22+
APACHE_CONFIGURE_ON=	--with-apache=${LOCALBASE}/sbin
APACHE_PLIST_DIRSTRY=	www/cgi-bin www/data www/icons

PORTDOCS=	*


.include <bsd.port.mk>
