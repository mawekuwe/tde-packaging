#!/bin/bash

KLAMAV_DIR=${HOME}/.klamav

if [ ! -d ${KLAMAV_DIR}/database -o ! -d ${KLAMAV_DIR}/quarantine ]; then
   mkdir -p ${KLAMAV_DIR}/{database,quarantine}
fi

if [ ! -f ${KLAMAV_DIR}/database/main.cvd -o ! -f ${KLAMAV_DIR}/database/daily.cvd ]; then
   cp -f /var/lib/clamav/* ${KLAMAV_DIR}/database
fi

klamav-real
