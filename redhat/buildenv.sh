#!/bin/bash

# This file can be sourced in your .bashrc

TDE_BASEDIR=~/tde
TDE_VERSION=14.0.0
TDE_GITBASESRC=${TDE_BASEDIR}/tde_r14
TDE_GITBASEPKG=${TDE_BASEDIR}/tde-packaging/redhat
TDE_TARBALLS=${TDE_BASEDIR}/tde-tarballs/${TDE_VERSION}

[ -d "${TDE_PACKAGING_DIR}" ] || export TDE_PACKAGING_DIR=~/tde/tde-packaging

export PATH="${PATH}:${TDE_GITBASEPKG}/build"

# Distribution suffix (e.g: .el6 , .mga3 ...)
export DIST="$( "${TDE_GITBASEPKG}/build/rpmdist.sh" --dist )"

# Go to the RPMS folder
alias cdrpm='cd ~/rpmbuild/RPMS/RPMS${DIST}'

# Build a single tarball (execute from GIT directory)
alias tdp4='TARGET=14.0.0 SUFFIX=0 TARBALL_DIR=${TDE_TARBALLS}/main COMPRESS=gzip ${TDE_GITBASESRC}/scripts/create_tarball'

# Rebuild all tarballs
if [ -x /usr/bin/pigz ]; then
  export TDE_COMPRESS=pigz
else
  export TDE_COMPRESS=gzip
fi
alias tdep3='(rm -rf ~/tde/tde-tarballs/3.5.13.2; cd ~/tde/tde_v3.5.13-sru; export SUFFIX=0; export COMPRESS=${TDE_COMPRESS:-gzip}; export TDE_REBRAND=1; ./scripts/create_all_tarballs)'
alias tdep4='(rm -rf ${TDE_TARBALLS}; cd ${TDE_GITBASESRC}; export SUFFIX=0; export COMPRESS=${TDE_COMPRESS:-gzip}; export TDE_REBRAND=1; ./scripts/create_all_tarballs)'

# Build a single package
alias cdp='cd ~/tde/tde-packaging/redhat'

grp3() {
  build_rpm_package.sh "${1}" "3.5.13.2"
}

grp4() {
  build_rpm_package.sh "${1}" "14.0.0"
}

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


do_optimizegraphics() {
  if ! (which optipng && which advdef && which pngout) ; then
    echo "Missing utility ! Check that 'optipng', 'advdef' and 'pngout' utilities are available !"
    return 1
  fi
  
  while read m; do
    if [ -d "${m}" ]; then
      pushd "${m}"
      if [ -r .optimizegraphics ]; then
        echo "Graphics are already optimized !"
      else
        optimizegraphics
        touch .optimizegraphics
      fi
      popd
    fi
  done < submodules
}

alias rr='rpm -qa --qf "%{name} %{buildhost}\n" | grep "\.vtf" | awk "{print \$1}"'

# Update main repository
alias tdu='(export GIT_ASKPASS=/bin/true; cd ~/tde/tde_r14; ./scripts/switch_all_submodules_to_head_and_clean)'

# Build local repository metadata (Mageia)
alias cru='(cdrpm; genhdlist2 --allow-empty-media noarch; genhdlist2 $(uname -i); sudo urpmi.update rpmbuild.$(uname -i) rpmbuild.noarch)'
alias cruc='(cdrpm; genhdlist2 --clean --allow-empty-media  noarch; genhdlist2 --clean $(uname -i); sudo urpmi.update rpmbuild.$(uname -i) rpmbuild.noarch)'

# Build local repository (RHEL)
alias cry='(cdrpm; createrepo $(uname -i); createrepo noarch; sudo yum clean all --disablerepo="*" --enablerepo="rpmbuild*")'
alias sy='sudo yum localinstall -y --nogpgcheck'

# Build local repository (openSUSE)
alias crz='(cdrpm; createrepo $(uname -i); createrepo noarch; sudo zypper refresh)'

# Build local repository (PCLOS)
alias cra='(cdrpm; genpkglist $PWD noarch; genpkglist $PWD i586; genpkglist $PWD x86_64; genbasedir $PWD i586 x86_64 noarch; sudo apt-get update)'
alias crac='(cdrpm; for i in i586 noarch x86_64; do cd $i; tdesortrpm.sh; cd -; done; rpmsign --addsign */RPMS.*/*.rpm; for i in i586 noarch x86_64; do for j in 3rdparty applications dependencies extras libraries main; do genpkglist $PWD/$i $j; done; done; for i in i586 noarch x86_64; do genbasedir $PWD/$i 3rdparty applications dependencies extras libraries main; done; sudo apt-get update)'
alias cras='(cdrpm; cd $(uname -i); rm -rf base; mkdir base; for i in 3rdparty applications dependencies extras libraries main; do genpkglist $PWD $i; done; genbasedir $PWD 3rdparty applications dependencies extras libraries main; cd ../noarch; rm -rf base; mkdir base; for i in applications dependencies extras main; do genpkglist $PWD $i; done; genbasedir $PWD applications dependencies extras main )'

# Reinstall packages (Mageia)
getrpmfromsrpm() {
  rpm -qa --qf "%{name} %{sourcerpm}\n"|grep "$1"|awk '{print $1}'
}
reinst() {
  sudo urpmi --replacepkgs --allow-force $(getrpmfromsrpm $1)
}
