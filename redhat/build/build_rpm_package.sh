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

# Determines if we are running an i386 or x86_64 distro
if [ "$(rpm -q --qf '%{arch}\n' kernel | tail -n 1)" = "i686" ]; then
	ARGS="${ARGS} --target=i686"
fi

[ -d "${BUILDDIR}" ] || mkdir -p "${BUILDDIR}"

RPMDIR="$(rpm -E %{_rpmdir}.tde-${TDE_VERSION})"

rpmbuild -ba \
  --define "_specdir ${TEMPDIR}" \
  --define "_sourcedir ${TEMPDIR}" \
  --define "_builddir ${BUILDDIR}" \
  --define "_buildrootdir ${BUILDROOTDIR}" \
  --define "_rpmdir ${RPMDIR}" \
  --define "tde_version ${TDE_VERSION}" \
  --define "tde_prefix /opt/trinity" \
  --define "preversion ${PREVERSION}" \
  ${ARGS} \
  "${SPECFILE}"
RET=$?

# Removes BUILDDIR if build succeeded
if [ ${RET} -eq 0 ]; then
  rm -rf "${BUILDDIR}/"*${PKGNAME}-${VERSION}*
fi

rm -rf "${TEMPDIR}"

exit $RET
