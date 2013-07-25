#!/bin/bash

# This file can be sourced in your .bashrc

TDE_BASEDIR=~/tde
TDE_VERSION=14.0.0
TDE_GITBASESRC=${TDE_BASEDIR}/tde_r14
TDE_GITBASEPKG=${TDE_BASEDIR}/tde-packaging/redhat
TDE_TARBALLS=${TDE_BASEDIR}/tde-tarballs/${TDE_VERSION}

export PATH="${PATH}:${TDE_GITBASEPKG}"

# Distribution suffix (e.g: .el6 , .mga3 ...)
export DIST="$( "${TDE_GITBASEPKG}/rpmdist.sh" --dist )"

# Go to the RPMS folder
alias cdrpm='cd ~/rpmbuild/RPMS/RPMS${DIST}'

# Build a single tarball (execute from GIT directory)
alias tdp4='TARGET=14.0.0 SUFFIX=0 TARBALL_DIR=${TDE_TARBALLS}/main COMPRESS=gzip ${TDE_GITBASESRC}/scripts/create_tarball'

# Rebuild all tarballs
alias tdep3='(rm -rf ~/tde/tde-tarballs/3.5.13.2; cd ~/tde/tde_v3.5.13-sru; export SUFFIX=0; export COMPRESS=gzip; export TDE_REBRAND=1; ./scripts/create_all_tarballs)'
alias tdep4='(rm -rf ${TDE_TARBALLS}; cd ${TDE_GITBASESRC}; export SUFFIX=0; export COMPRESS=gzip; export TDE_REBRAND=1; ./scripts/create_all_tarballs)'

# Build a single package
alias cdp='cd ~/tde/tde-packaging/redhat'
alias grp3='./genrpm.sh -v 3.5.13.2 -a'
alias grp4='./genrpm.sh -v 14.0.0 -a'

# Check if tarballs are more recent than installed packages
checknew() {
  find ~/tde/tde-tarballs/14.0.0 -name "trinity-*.tar.gz" | while read f; do
    TAR="${f##*/}"
    NAME="${TAR%-*}"
    
    if rpm -q "${NAME}" &>/dev/null; then
      set $(rpm -q --qf "%{name} 14.0.0 %{release}" ${NAME} )
      B="$1-$2~${3#*_}"
      A=${TAR%.tar.gz}
      B=${B%.opt}
      B=${B%${DIST}}
      if [[ "$A" > "$B" ]]; then
        echo "Installed: $B"
        echo "Available: $A"
        echo
      fi
    fi
  done
}

# Build local repository metadata (Mageia)
alias cru='(cdrpm; genhdlist2 noarch; genhdlist2 $(uname -i); sudo urpmi.update rpmbuild.$(uname -i) rpmbuild.noarch)'
alias cruc='(cdrpm; genhdlist2 --clean noarch; genhdlist2 --clean $(uname -i); sudo urpmi.update rpmbuild.$(uname -i) rpmbuild.noarch)'

# Build local repository (RHEL)
alias cry='(cdrpm; createrepo $(uname -i); createrepo noarch; sudo yum clean all --disablerepo="*" --enablerepo="rpmbuild*")'
