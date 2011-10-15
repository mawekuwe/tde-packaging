#!/usr/bin/perl

# Copyright: MandrakeSoft, licensed under the GPL v2.
# modified by Laurent Montel <lmontel@mandrakesoft.com>

use strict;
use MDK::Common;

foreach my $file (@ARGV) {
    my $no_theme;
    # grep return 0 if a match is found
    $no_theme = 1 if `grep -q -s '^UseTheme=' $file` ;		
    substInFile {
        if (/SystemPath=(.*)$/) {
            my $result = $1;
            s!$!:/usr/X11R6/bin/! if $result !~ m!/usr/X11R6/bin/!;
        }
        if (/UserPath=(.*)$/) {
            my $result = $1;
            s!$!:/usr/X11R6/bin/! if $result !~ m!/usr/X11R6/bin/!;
        }
        s!^(Setup)=.*!$1=/etc/X11/xdm/Xsetup_0!;
        s!^(Startup)=.*!$1=/etc/X11/xdm/GiveConsole!;
        s!^(Reset)=.*!$1=/etc/X11/xdm/TakeConsole!;
		s!^(Xserver)=.*!$1=/etc/X11/xdm/Xservers\nServerVTs=-7\n!;
		if ($no_theme) {
			s!^(AuthComplain)=.*!$1=AuthComplain=false\nUseTheme=true\nTheme=/usr/share/mdk/dm!;
		} else {
			s!^(AuthComplain)=.*!AuthComplain=false!;
		}
		
    } $file;
}


