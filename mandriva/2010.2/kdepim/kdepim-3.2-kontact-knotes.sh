#!/bin/sh

if [ -x /usr/bin/kontact ] && [ ! -z $(/sbin/pidof kontact) ]; then
		kontact --module knotes 
else
		knotes $*
fi

