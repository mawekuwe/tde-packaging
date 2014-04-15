#!/bin/bash

PKGFILE="packages$(rpm -E %dist)"

# Under Mageia/Mandriva, do not forget to enable "Tainted" and "Nonfree" repositories !
if [ -x /usr/sbin/urpmi ]; then
  if [ "$(uname -i)" = "x86_64" ]; then
    PKGS="$(<${PKGFILE})"
  else
    PKGS="$(sed -e "s|lib64|lib|" ${PKGFILE} | sort -u)"
  fi

  sudo urpmi ${PKGS} 2>&1
fi
