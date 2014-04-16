#!/bin/bash -x

TDE_VERSION=${1:-14.0.0}
ARCH=$(rpm -E %_target_cpu)
RPMDIR=$(rpm -E %{_rpmdir}.tde-${TDE_VERSION})

# RHEL / CentOS / Fedora
if [ -x /usr/bin/yum ]; then
  cat <<EOF >/tmp/rpmbuild-tde.repo
[rpmbuild.${ARCH}]
name=rpmbuild.${ARCH}
baseurl=file://${RPMDIR}/${ARCH}
enabled=1
gpgcheck=0

[rpmbuild.noarch]
name=rpmbuild.noarch
baseurl=file://${RPMDIR}/noarch
enabled=1
gpgcheck=0
EOF
  sudo mv -f /tmp/rpmbuild-tde.repo /etc/yum.repos.d/
fi

# Mageia / Mandriva
if [ -x /usr/sbin/urpmi ]; then
  sudo urpmi.removemedia -y "rpmbuild"
  sudo urpmi.addmedia rpmbuild.${ARCH} ${RPMDIR}/${ARCH}
  sudo urpmi.addmedia rpmbuild.noarch ${RPMDIR}/noarch
fi
