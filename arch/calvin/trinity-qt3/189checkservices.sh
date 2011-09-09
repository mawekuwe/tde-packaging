#!/bin/bash

IP_ADDRESS_1=97.64.229.82
IP_ADDRESS_2=97.64.229.83

STATUS_1=0
STATUS_2=0

CURDATE=$('date')

netcat -z ${IP_ADDRESS_1} 80
if [ $? -eq 0 ]
then
    STATUS_1=1
else
    sleep 5
    netcat -z ${IP_ADDRESS_1} 80
    if [ $? -eq 0 ]
    then
        STATUS_1=1
    else
        echo "Interface 1 is DOWN"
    fi
fi

netcat -z ${IP_ADDRESS_2} 80
if [ $? -eq 0 ]
then
    STATUS_2=1
else
    sleep 5
    netcat -z ${IP_ADDRESS_2} 80
    if [ $? -eq 0 ]
    then
        STATUS_2=1
    else
        echo "Interface 2 is DOWN"
    fi
fi

if [[ STATUS_1 == 0 ]]; then
    mail -s "[SERVICE FAILURE NOTIFICATION] pearsoncomputing.net" kb9vqf@pearsoncomputing.net < "The network interface ${IP_ADDRESS_1}:80 failed to respond on ${CURDATE}"
fi

if [[ STATUS_2 == 0 ]]; then
    mail -s "[SERVICE FAILURE NOTIFICATION] pearsoncomputing.net" kb9vqf@pearsoncomputing.net < "The network interface ${IP_ADDRESS_2}:80 failed to respond on ${CURDATE}"
fi
