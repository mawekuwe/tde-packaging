Many of the Mandriva TDE packages don't currently build without manual intervention.
This is largely being caused by automake/autoconf issues which i'm expecting to be
solved by the cmake migration in Trinity 3.5.13. Therefore, rather than spend a lot
of time trying to fix an obsolete build process, i've got a procedure to work around
the problem so that working Trinity packages can be built.

The build problem is caused compilation failures at a number of points in the build
process, with the linker being unable to find various QT classes. This is being
caused by an option in the compilation command "-Wl,--as-needed", this option only
gets added to the compilation options when the build process is initiated by
rpmbuild, if I use the ./configure command with the same options and build the
sources manually, then this option is never added and the packages compile normally.
Therefore, it is being added by something in the rpmbuild process. So, the current
build procedure is:

1) execute
       rpmbuild -ba <spec file>
   as normal.
2) If the build process crashes with the qt linking errors, switch to the build
   directory to perform a manual build.
3) ensure /opt/kde3/bin is in the PATH environment variable.
4) re-run ./configure, using the options stored in the config.log file.
5) start make again. You might need to do a "make clean" if the build still fails
   with the same error.
6) return to the SPEC's directory and execute
       rpmbuild -bi --short-circuit=i <spec file>
   followed by
       rpmbuild -ba --short-circuit=i <spec file>
7) You should now have the RPM packages.
