#!/bin/bash

WORKERS=$(getconf _NPROCESSORS_ONLN)
TDE_VERSION="${1:-14.0.0}"

LOCKFILE="/tmp/lock.${0##*/}"
while [ -e "${LOCKFILE}" ]; do
  echo "Waiting for lock file '${LOCKFILE}' to vanish."
  sleep 3
done

ARCH="$(rpm -E %{_target_cpu})"
RPMDIR=$(rpm -E %{_rpmdir}.tde-${TDE_VERSION})

[ -d "${RPMDIR}/noarch" ] || mkdir -p "${RPMDIR}/noarch"
[ -d "${RPMDIR}/${ARCH}" ] || mkdir -p "${RPMDIR}/${ARCH}"

if [ -x /usr/sbin/urpmi ]; then
  REPOUPDATE='(cd ${RPMDIR}; genhdlist2 --clean --allow-empty noarch & genhdlist2 --clean --allow-empty ${ARCH} & wait; sudo urpmi.update rpmbuild.${ARCH} rpmbuild.noarch)'
elif [ -x /usr/bin/zypper ]; then
  REPOUPDATE='(cd ${RPMDIR}; createrepo --workers=${WORKERS} ${ARCH} & createrepo --workers=${WORKERS} noarch & wait; sudo zypper refresh rpmbuild.${ARCH} rpmbuild.noarch)'
elif [ -x /usr/bin/yum ]; then
  if [ "$(rpm -E %dist)" = ".el5" ]; then
    REPOUPDATE='(cd ${RPMDIR}; createrepo ${ARCH} & createrepo noarch & wait; sudo yum clean all --disablerepo="*" --enablerepo="rpmbuild*")'
  else
    REPOUPDATE='(cd ${RPMDIR}; createrepo --workers=${WORKERS} ${ARCH} & createrepo --workers=${WORKERS} noarch & wait; sudo yum clean all --disablerepo="*" --enablerepo="rpmbuild*")'
  fi
elif [ -x /usr/bin/apt-get ]; then
  REPOUPDATE='(cd ${RPMDIR}; genpkglist $PWD noarch & genpkglist $PWD ${ARCH} & wait; genbasedir $PWD i586 x86_64 noarch; sudo apt-get update)'
fi

eval "${REPOUPDATE}; rm -f ${LOCKFILE}" || exit 1
