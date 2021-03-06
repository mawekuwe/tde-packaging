#!/bin/bash -ex

# Usage: build_rpm_package.sh <TDE_PACKAGE> [TDE_VERSION]
# Example: build_rpm_package.sh tdebase 14.0.0


PKGNAME="${1##*/}"
TDE_VERSION="${2:-14.0.0}"

SPECFILE=$(get_specfile.sh ${PKGNAME} ${TDE_VERSION})
SOURCES=$(get_source_files.sh ${PKGNAME} ${TDE_VERSION})
TARBALL=$(get_latest_tarball_filename.sh ${PKGNAME} ${TDE_VERSION} || :)
VERSION=$(get_latest_tarball_version.sh ${PKGNAME} ${TDE_VERSION} || :)
case "${VERSION}" in *~pre*) PREVERSION="${VERSION#*~}";; esac

DIST="$(rpmdist.sh --dist)"
BUILDDIR="/dev/shm/BUILD${DIST}.$(uname -i)"
BUILDROOTDIR="/dev/shm/BUILDROOT${DIST}.$(uname -i)"
LOGFILE=/tmp/log.${COMP##*/}

TEMPDIR="$(mktemp -d)"
cp -f ${SPECFILE} ${SOURCES} ${TARBALL} "${TEMPDIR}"

### Check for patches

# 1. Check if there is a big, monolithic patch
PATCHDIR="${SPECFILE%/*}/patches"
BIGPATCH="${PATCHDIR}/${PKGNAME}-${TDE_VERSION}.patch"
if [ -r "${BIGPATCH}" ]; then
  cp -f "${BIGPATCH}" "${TEMPDIR}/one.patch"
fi

# 2. Check if there are small, local patches
PATCHDIR="${SPECFILE%/*}/patches/${TDE_VERSION}"
PATCHLIST="${PATCHDIR}/patches.list"
if [ -r "${PATCHLIST}" ]; then
  while read l; do
    APPLY=""
    case "${l}" in
      ""|"#"*);;
     *"opensuse"*) [ -r /etc/SuSE-release ] && APPLY=1;;
     *) APPLY=1;;
    esac
    
    if [ "${APPLY}" ]; then
      if [ -r "${PATCHDIR}/${l}" ]; then
        echo "Applying patch '${l}'..."
        cat "${PATCHDIR}/${l}" >>"${TEMPDIR}/one.patch"
      else
        echo "ERROR: invalid patch '${l}' !!"
        exit 3
      fi
    fi
  done < "${PATCHLIST}"
fi

if [ -r "${TEMPDIR}/one.patch" ]; then
  sed -i "${TEMPDIR}/"*.spec \
      -e "/^Source0:/ s/$/\nPatch0: one.patch/" \
      -e "/%setup/ s/$/\n%patch0 -p1/"
fi

[ -d "${BUILDDIR}" ] || mkdir -p "${BUILDDIR}"

RPMDIR="$(rpm -E %{_rpmdir}.tde-${TDE_VERSION})"
SRPMDIR="$(rpm -E %{_srcrpmdir}.tde-${TDE_VERSION})"

rpmbuild -ba \
  --define "_specdir ${TEMPDIR}" \
  --define "_sourcedir ${TEMPDIR}" \
  --define "_builddir ${BUILDDIR}" \
  --define "_buildrootdir ${BUILDROOTDIR}" \
  --define "_rpmdir ${RPMDIR}" \
  --define "_srcrpmdir ${SRPMDIR}" \
  --define '_build_create_debug 1' \
  --define "vendor Trinity\ Desktop" \
  --define "packager Francois\ Andriot\ <francois.andriot@free.fr>" \
  --define "tde_version ${TDE_VERSION}" \
  --define "tde_prefix /opt/trinity" \
  --define "preversion ${PREVERSION:-}" \
  --define "tde_patch 1" \
  --define "with_akode 1" \
  --define "with_jack 1" \
  --define "with_lame 1" \
  --define "with_mad 1" \
  --define "with_mpeg 1" \
  --define "with_xine 1" \
  --define "with_xscreensaver 1" \
  "${TEMPDIR}/${SPECFILE##*/}"
RET=$?

# Removes BUILDDIR if build succeeded
if [ ${RET} -eq 0 ]; then
  rm -rf "${BUILDDIR}/"*${PKGNAME}-${VERSION}*
fi

rm -rf "${TEMPDIR}"

exit $RET
