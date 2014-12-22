#!/bin/bash

FEDORA=0
RHEL=0
MGA=0
DIST=""

if [ -r /etc/redhat-release ]; then
  read a b c d e f g < /etc/redhat-release
elif [ -r /etc/SuSE-release ]; then
  a="opensuse"
fi

case $a in
  # Mageia release 1 (Official) for x86_64
  Mageia*)
	DIST=".mga${c}"
#	MDKVERSION="201002"
  ;;
  # Mandriva Linux release 2011.0 (Official) for x86_64
  Mandriva*)
	DIST=".mdv${d}"
	MDKVERSION="201100"
  ;;
  # CentOS release 5.7 (Final)
  # CentOS Linux release 6.0 (Final)
  CentOS*)
    if [ $c = "release" ]; then
      RHEL="${d%%.*}"; DIST=".el${RHEL}"
    else
      RHEL="${c%%.*}"; DIST=".el${RHEL}"
    fi
  ;;
  
  "Red")
    RHEL="${g%%.*}"; DIST=".el${RHEL}"
  ;;
  # Fedora release 15 (Lovelock)
  Fedora*) FEDORA="${c}"; DIST=".fc${FEDORA}";;
  # Opensuse
  opensuse)
    DIST=".oss$((read l; read a b c; echo ${c//./}) </etc/SuSE-release)"
  ;;
  # PCLinuxOS
  #PCLinuxOS) PCLINUXOS="${c}"; DIST=".pclos${c}";;
  PCLinuxOS) PCLINUXOS="${c}"; DIST=".pclos";;

  *) echo "distrib non reconnue !! $a";;
esac

case "$1" in
  "--dist") echo $DIST;;
  "--rhel") echo $RHEL;;
  "--fedora") echo $FEDORA;;
  "--mdkversion") echo $MDKVERSION;;
  "--pclinuxos") echo $PCLINUXOS;;
esac
