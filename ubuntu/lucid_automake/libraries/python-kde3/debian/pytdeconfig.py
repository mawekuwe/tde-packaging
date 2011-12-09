# import the sipconfig.py for the normal or the debug build

import sys

if getattr(sys, "pydebug", False):
    try:
        from pytdeconfig_d import *
    except ImportError, msg:
        raise ImportError, 'No module named pytdeconfig; package python-kde3-dbg not installed'
else:
    from pytdeconfig_nd import *
