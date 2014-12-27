#
# Regular cron jobs for the libr package
#
0 4	* * *	root	[ -x /usr/bin/libr_maintenance ] && /usr/bin/libr_maintenance
