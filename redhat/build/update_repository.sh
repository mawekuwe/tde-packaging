#!/bin/bash

WORKERS=$(getconf _NPROCESSORS_ONLN)

LOCKFILE="/tmp/lock.${0##*/}"
while [ -e "${LOCKFILE}" ]; do
  echo "Waiting for lock file '${LOCKFILE}' to vanish."
  sleep 3
done

if [ -x /usr/sbin/urpmi ]; then
  REPOUPDATE='(cd $(rpm -E %{_rpmdir}); genhdlist2 --clean --allow-empty noarch; genhdlist2 --clean --allow-empty $(uname -i); sudo urpmi.update rpmbuild.$(uname -i) rpmbuild.noarch)'
elif [ -x /usr/bin/zypper ]; then
  REPOUPDATE='(cd $(rpm -E %{_rpmdir}); createrepo --workers=${WORKERS} $(uname -i); createrepo --workers=${WORKERS} noarch; sudo zypper refresh rpmbuild.$(uname -i) rpmbuild.noarch)'
elif [ -x /usr/bin/yum ]; then
  REPOUPDATE='(cd $(rpm -E %{_rpmdir}); createrepo $(uname -i); createrepo noarch; sudo yum clean all --disablerepo="*" --enablerepo="rpmbuild*")'
elif [ -x /usr/bin/apt-get ]; then
  REPOUPDATE='(cd $(rpm -E %{_rpmdir}); genpkglist $PWD noarch; genpkglist $PWD i586; genpkglist $PWD x86_64; genbasedir $PWD i586 x86_64 noarch; sudo apt-get update)'
fi

eval "${REPOUPDATE}; rm -f ${LOCKFILE}"|| exit 1
