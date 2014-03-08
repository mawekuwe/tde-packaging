# If TDE is built in a specific prefix (e.g. /opt/trinity), the release will be suffixed with ".opt".
%if "%{?tde_prefix}" != "/usr"
%define _variant .opt
%endif

%define tde_version 14.0.0

# TDE specific building variables
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}

%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

%define _docdir %{tde_docdir}

Name:		trinity-tdevelop
Summary:	Integrated Development Environment for C++/C
Version:	%{tde_version}
Release:	%{?!preversion:1}%{?preversion:0_%{preversion}}%{?dist}%{?_variant}

License:	GPLv2
Group:		Development/Tools

Vendor:		Trinity Project
Packager:	Francois Andriot <francois.andriot@free.fr>
URL:		http://www.trinitydesktop.org/

Prefix:		%{tde_prefix}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	%{name}-%{version}%{?preversion:~%{preversion}}.tar.gz
Source1:	ftp://129.187.206.68/pub/unix/ide/tdevelop/c_cpp_reference-2.0.2_for_KDE_3.0.tar.bz2

# [c_cpp_ref] Fix library directories detection
Patch1: c_cpp_reference-2.0.2-config.patch

# [c_cpp_ref] Fix installation of 'asm' files
Patch4:	c_cpp_reference-2.0.2-install.patch

Requires: %{name}-libs = %{version}-%{release}


Requires: make
Requires: perl
Requires: flex >= 2.5.4
Requires:	trinity-tqt3-designer >= 3.5.0
Requires:	trinity-tqt3-devel >= 3.5.0
Requires: gettext
Requires: ctags

BuildRequires:	cmake >= 2.8
BuildRequires:	trinity-tqtinterface-devel >= %{tde_version}
BuildRequires:	trinity-arts-devel >= 1:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdesdk-devel >= %{tde_version}
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	db4-devel
%endif
BuildRequires:	flex
# FIXME: No CVS support in tdevelop? This is going to suck...
# Requires kdesdk3.
BuildRequires:	subversion-devel
BuildRequires:	neon-devel

# LDAP support
%if 0%{?suse_version}
BuildRequires:	openldap2-devel
%else
BuildRequires:	openldap-devel
%endif

#ACL support
BuildRequires:	libacl-devel

Obsoletes:	trinity-tdevelop < %{version}-%{release}
Provides:	trinity-tdevelop = %{version}-%{release}

%description
The TDevelop Integrated Development Environment provides many features
that developers need as well as providing a unified interface to programs
like gdb, the C/C++ compiler, and make. TDevelop manages or provides:

All development tools needed for C++ programming like Compiler,
Linker, automake and autoconf; KAppWizard, which generates complete,
ready-to-go sample applications; Classgenerator, for creating new
classes and integrating them into the current project; File management
for sources, headers, documentation etc. to be included in the
project; The creation of User-Handbooks written with SGML and the
automatic generation of HTML-output with the KDE look and feel;
Automatic HTML-based API-documentation for your project's classes with
cross-references to the used libraries; Internationalization support
for your application, allowing translators to easily add their target
language to a project;

tdevelop also includes WYSIWYG (What you see is what you get)-creation
of user interfaces with a built-in dialog editor; Debugging your
application by integrating KDbg; Editing of project-specific pixmaps
with KIconEdit; The inclusion of any other program you need for
development by adding it to the "Tools"-menu according to your
individual needs.

%files
%defattr(-,root,root,-)
%{tde_bindir}/tdevassistant
%{tde_bindir}/tdevdesigner
%{tde_bindir}/tdevelop
%{tde_bindir}/tdevelop-htdig
%{tde_bindir}/tdevprj2tdevelop
%{tde_bindir}/tdevprofileeditor
%{tde_libdir}/tdeconf_update_bin/tdev-gen-settings-tdeconf_update
%{tde_tdeappdir}/tdevassistant.desktop
%{tde_tdeappdir}/tdevdesigner.desktop
%{tde_tdeappdir}/tdevelop.desktop
%{tde_tdeappdir}/tdevelop_c_cpp.desktop
%{tde_tdeappdir}/tdevelop_tde_cpp.desktop
%{tde_tdeappdir}/tdevelop_ruby.desktop
%{tde_tdeappdir}/tdevelop_scripting.desktop
%{tde_tdelibdir}/tdeio_chm.la
%{tde_tdelibdir}/tdeio_chm.so
%{tde_tdelibdir}/tdeio_csharpdoc.la
%{tde_tdelibdir}/tdeio_csharpdoc.so
%{tde_tdelibdir}/tdeio_perldoc.la
%{tde_tdelibdir}/tdeio_perldoc.so
%{tde_tdelibdir}/tdeio_pydoc.la
%{tde_tdelibdir}/tdeio_pydoc.so
%{tde_tdelibdir}/libdocchmplugin.la
%{tde_tdelibdir}/libdocchmplugin.so
%{tde_tdelibdir}/libdoccustomplugin.la
%{tde_tdelibdir}/libdoccustomplugin.so
%{tde_tdelibdir}/libdocdevhelpplugin.la
%{tde_tdelibdir}/libdocdevhelpplugin.so
%{tde_tdelibdir}/libdocdoxygenplugin.la
%{tde_tdelibdir}/libdocdoxygenplugin.so
%{tde_tdelibdir}/libdoctdevtocplugin.la
%{tde_tdelibdir}/libdoctdevtocplugin.so
%{tde_tdelibdir}/libdocqtplugin.la
%{tde_tdelibdir}/libdocqtplugin.so
%{tde_tdelibdir}/libkchmpart.la
%{tde_tdelibdir}/libkchmpart.so
%{tde_tdelibdir}/libtdevabbrev.la
%{tde_tdelibdir}/libtdevabbrev.so
%{tde_tdelibdir}/libtdevadaproject.la
%{tde_tdelibdir}/libtdevadaproject.so
%{tde_tdelibdir}/libtdevadasupport.la
%{tde_tdelibdir}/libtdevadasupport.so
%{tde_tdelibdir}/libtdevantproject.la
%{tde_tdelibdir}/libtdevantproject.so
%{tde_tdelibdir}/libtdevappview.la
%{tde_tdelibdir}/libtdevappview.so
%{tde_tdelibdir}/libtdevappwizard.la
%{tde_tdelibdir}/libtdevappwizard.so
%{tde_tdelibdir}/libtdevastyle.la
%{tde_tdelibdir}/libtdevastyle.so
%{tde_tdelibdir}/libtdevautoproject.la
%{tde_tdelibdir}/libtdevautoproject.so
%{tde_tdelibdir}/libtdevbashsupport.la
%{tde_tdelibdir}/libtdevbashsupport.so
%{tde_tdelibdir}/libtdevbookmarks.la
%{tde_tdelibdir}/libtdevbookmarks.so
%{tde_tdelibdir}/libtdevclassview.la
%{tde_tdelibdir}/libtdevclassview.so
%{tde_tdelibdir}/libtdevcppsupport.la
%{tde_tdelibdir}/libtdevcppsupport.so
%{tde_tdelibdir}/libtdevcsharpsupport.la
%{tde_tdelibdir}/libtdevcsharpsupport.so
%{tde_tdelibdir}/libtdevctags2.la
%{tde_tdelibdir}/libtdevctags2.so
%{tde_tdelibdir}/libtdevcustompcsimporter.la
%{tde_tdelibdir}/libtdevcustompcsimporter.so
%{tde_tdelibdir}/libtdevcustomproject.la
%{tde_tdelibdir}/libtdevcustomproject.so
%{tde_tdelibdir}/libtdevdccoptions.la
%{tde_tdelibdir}/libtdevdccoptions.so
%{tde_tdelibdir}/libtdevdebugger.la
%{tde_tdelibdir}/libtdevdebugger.so
%{tde_tdelibdir}/libtdevdesignerpart.la
%{tde_tdelibdir}/libtdevdesignerpart.so
%{tde_tdelibdir}/libtdevdiff.la
%{tde_tdelibdir}/libtdevdiff.so
%{tde_tdelibdir}/libtdevdistpart.la
%{tde_tdelibdir}/libtdevdistpart.so
%{tde_tdelibdir}/libtdevdocumentation.la
%{tde_tdelibdir}/libtdevdocumentation.so
%{tde_tdelibdir}/libtdevdoxygen.la
%{tde_tdelibdir}/libtdevdoxygen.so
%{tde_tdelibdir}/libtdeveditorchooser.la
%{tde_tdelibdir}/libtdeveditorchooser.so
%{tde_tdelibdir}/libtdevfilecreate.la
%{tde_tdelibdir}/libtdevfilecreate.so
%{tde_tdelibdir}/libtdevfilegroups.la
%{tde_tdelibdir}/libtdevfilegroups.so
%{tde_tdelibdir}/libtdevfilelist.la
%{tde_tdelibdir}/libtdevfilelist.so
%{tde_tdelibdir}/libtdevfileselector.la
%{tde_tdelibdir}/libtdevfileselector.so
%{tde_tdelibdir}/libtdevfileview.la
%{tde_tdelibdir}/libtdevfileview.so
%{tde_tdelibdir}/libtdevfilter.la
%{tde_tdelibdir}/libtdevfilter.so
%{tde_tdelibdir}/libtdevfortransupport.la
%{tde_tdelibdir}/libtdevfortransupport.so
%{tde_tdelibdir}/libtdevfpcoptions.la
%{tde_tdelibdir}/libtdevfpcoptions.so
%{tde_tdelibdir}/libtdevfullscreen.la
%{tde_tdelibdir}/libtdevfullscreen.so
%{tde_tdelibdir}/libtdevgccoptions.la
%{tde_tdelibdir}/libtdevgccoptions.so
%{tde_tdelibdir}/libtdevgrepview.la
%{tde_tdelibdir}/libtdevgrepview.so
%{tde_tdelibdir}/libtdevjavasupport.la
%{tde_tdelibdir}/libtdevjavasupport.so
%{tde_tdelibdir}/libtdevtdelibsimporter.la
%{tde_tdelibdir}/libtdevtdelibsimporter.so
%{tde_tdelibdir}/libtdevkonsoleview.la
%{tde_tdelibdir}/libtdevkonsoleview.so
%{tde_tdelibdir}/libtdevmakeview.la
%{tde_tdelibdir}/libtdevmakeview.so
%{tde_tdelibdir}/libtdevopenwith.la
%{tde_tdelibdir}/libtdevopenwith.so
%{tde_tdelibdir}/libtdevpartexplorer.la
%{tde_tdelibdir}/libtdevpartexplorer.so
%{tde_tdelibdir}/libtdevpascalproject.la
%{tde_tdelibdir}/libtdevpascalproject.so
%{tde_tdelibdir}/libtdevpascalsupport.la
%{tde_tdelibdir}/libtdevpascalsupport.so
%{tde_tdelibdir}/libtdevperlsupport.la
%{tde_tdelibdir}/libtdevperlsupport.so
%{tde_tdelibdir}/libtdevpgioptions.la
%{tde_tdelibdir}/libtdevpgioptions.so
%{tde_tdelibdir}/libtdevphpsupport.la
%{tde_tdelibdir}/libtdevphpsupport.so
%{tde_tdelibdir}/libtdevpythonsupport.la
%{tde_tdelibdir}/libtdevpythonsupport.so
%{tde_tdelibdir}/libtdevqt4importer.la
%{tde_tdelibdir}/libtdevqt4importer.so
%{tde_tdelibdir}/libtdevqtimporter.la
%{tde_tdelibdir}/libtdevqtimporter.so
%{tde_tdelibdir}/libtdevquickopen.la
%{tde_tdelibdir}/libtdevquickopen.so
%{tde_tdelibdir}/libtdevrbdebugger.la
%{tde_tdelibdir}/libtdevrbdebugger.so
%{tde_tdelibdir}/libtdevregexptest.la
%{tde_tdelibdir}/libtdevregexptest.so
%{tde_tdelibdir}/libtdevreplace.la
%{tde_tdelibdir}/libtdevreplace.so
%{tde_tdelibdir}/libtdevrubysupport.la
%{tde_tdelibdir}/libtdevrubysupport.so
%{tde_tdelibdir}/libtdevscripting.la
%{tde_tdelibdir}/libtdevscripting.so
%{tde_tdelibdir}/libtdevscriptproject.la
%{tde_tdelibdir}/libtdevscriptproject.so
%{tde_tdelibdir}/libtdevsnippet.la
%{tde_tdelibdir}/libtdevsnippet.so
%{tde_tdelibdir}/libtdevsqlsupport.la
%{tde_tdelibdir}/libtdevsqlsupport.so
%{tde_tdelibdir}/libtdevtexttools.la
%{tde_tdelibdir}/libtdevtexttools.so
%{tde_tdelibdir}/libtdevtipofday.la
%{tde_tdelibdir}/libtdevtipofday.so
%{tde_tdelibdir}/libtdevtools.la
%{tde_tdelibdir}/libtdevtools.so
%{tde_tdelibdir}/libtdevtrollproject.la
%{tde_tdelibdir}/libtdevtrollproject.so
%{tde_tdelibdir}/libtdevuichooser.la
%{tde_tdelibdir}/libtdevuichooser.so
%{tde_tdelibdir}/libtdevvalgrind.la
%{tde_tdelibdir}/libtdevvalgrind.so
%{tde_tdelibdir}/libtdevvcsmanager.la
%{tde_tdelibdir}/libtdevvcsmanager.so
%{tde_datadir}/apps/tdeconf_update/
%{tde_datadir}/apps/tdevabbrev/
%{tde_datadir}/apps/tdevadaproject/tdevadaproject.rc
%{tde_datadir}/apps/tdevadasupport/tdevadasupport.rc
%{tde_datadir}/apps/tdevantproject/tdevantproject.rc
%{tde_datadir}/apps/tdevappoutputview/tdevmakeview.rc
%{tde_datadir}/apps/tdevappwizard/
%{tde_datadir}/apps/tdevassistant/tdevassistantui.rc
%{tde_datadir}/apps/tdevastyle/tdevpart_astyle.rc
%{tde_datadir}/apps/tdevautoproject/tdevautoproject.rc
%{tde_datadir}/apps/tdevbashsupport/tdevbashsupport.rc
%{tde_datadir}/apps/tdevclassview/
%{tde_datadir}/apps/tdevcppsupport/
%{tde_datadir}/icons/hicolor/*/actions/breakpoint_add.png
%{tde_datadir}/icons/hicolor/*/actions/breakpoint_delete.png
%{tde_datadir}/icons/hicolor/*/actions/breakpoint_delete_all.png
%{tde_datadir}/icons/hicolor/*/actions/breakpoint_edit.png
%{tde_datadir}/icons/hicolor/*/actions/ktip.png
%{tde_datadir}/icons/hicolor/*/apps/tdevassistant.png
%{tde_datadir}/icons/hicolor/*/apps/tdevdesigner.png
%{tde_datadir}/icons/hicolor/*/apps/tdevelop.png
%{tde_datadir}/icons/locolor/*/actions/tdevelop_tip.png
%{tde_datadir}/mimelnk/application/x-tdevelop.desktop
%{tde_datadir}/services/chm.protocol
%{tde_datadir}/services/csharpdoc.protocol
%{tde_datadir}/services/docchmplugin.desktop
%{tde_datadir}/services/doccustomplugin.desktop
%{tde_datadir}/services/docdevhelpplugin.desktop
%{tde_datadir}/services/docdoxygenplugin.desktop
%{tde_datadir}/services/doctdevtocplugin.desktop
%{tde_datadir}/services/docqtplugin.desktop
%{tde_datadir}/services/kchmpart.desktop
%{tde_datadir}/services/tdevabbrev.desktop
%{tde_datadir}/services/tdevadaproject.desktop
%{tde_datadir}/services/tdevadasupport.desktop
%{tde_datadir}/services/tdevantproject.desktop
%{tde_datadir}/services/tdevappoutputview.desktop
%{tde_datadir}/services/tdevappwizard.desktop
%{tde_datadir}/services/tdevastyle.desktop
%{tde_datadir}/services/tdevautoproject.desktop
%{tde_datadir}/services/tdevbashsupport.desktop
%{tde_datadir}/services/tdevbookmarks.desktop
%{tde_datadir}/services/tdevclassview.desktop
%{tde_datadir}/services/tdevcppsupport.desktop
%{tde_datadir}/services/tdevcsharpsupport.desktop
%{tde_datadir}/services/tdevcsupport.desktop
%{tde_datadir}/services/tdevctags2.desktop
%{tde_datadir}/services/tdevcustomproject.desktop
%{tde_datadir}/services/tdevdccoptions.desktop
%{tde_datadir}/services/tdevdebugger.desktop
%{tde_datadir}/services/tdevdesigner_part.desktop
%{tde_datadir}/services/tdevdiff.desktop
%{tde_datadir}/services/tdevdistpart.desktop
%{tde_datadir}/services/tdevdocumentation.desktop
%{tde_datadir}/services/tdevdoxygen.desktop
%{tde_datadir}/services/tdeveditorchooser.desktop
%{tde_datadir}/services/tdevfilecreate.desktop
%{tde_datadir}/services/tdevfilegroups.desktop
%{tde_datadir}/services/tdevfilelist.desktop
%{tde_datadir}/services/tdevfileselector.desktop
%{tde_datadir}/services/tdevfileview.desktop
%{tde_datadir}/services/tdevfilter.desktop
%{tde_datadir}/services/tdevfortransupport.desktop
%{tde_datadir}/services/tdevfpcoptions.desktop
%{tde_datadir}/services/tdevfullscreen.desktop
%{tde_datadir}/services/tdevg77options.desktop
%{tde_datadir}/services/tdevgccoptions.desktop
%{tde_datadir}/services/tdevgppoptions.desktop
%{tde_datadir}/services/tdevgrepview.desktop
%{tde_datadir}/services/tdevjavasupport.desktop
%{tde_datadir}/services/tdevtdeautoproject.desktop
%{tde_datadir}/services/tdevtdelibsimporter.desktop
%{tde_datadir}/services/tdevkonsoleview.desktop
%{tde_datadir}/services/tdevmakeview.desktop
%{tde_datadir}/services/tdevopenwith.desktop
%{tde_datadir}/services/tdevpartexplorer.desktop
%{tde_datadir}/services/tdevpascalproject.desktop
%{tde_datadir}/services/tdevpascalsupport.desktop
%{tde_datadir}/services/tdevpcscustomimporter.desktop
%{tde_datadir}/services/tdevperlsupport.desktop
%{tde_datadir}/services/tdevpgf77options.desktop
%{tde_datadir}/services/tdevpghpfoptions.desktop
%{tde_datadir}/services/tdevphpsupport.desktop
%{tde_datadir}/services/tdevpythonsupport.desktop
%{tde_datadir}/services/tdevqt4importer.desktop
%{tde_datadir}/services/tdevqtimporter.desktop
%{tde_datadir}/services/tdevquickopen.desktop
%{tde_datadir}/services/tdevrbdebugger.desktop
%{tde_datadir}/services/tdevregexptest.desktop
%{tde_datadir}/services/tdevreplace.desktop
%{tde_datadir}/services/tdevrubysupport.desktop
%{tde_datadir}/services/tdevscripting.desktop
%{tde_datadir}/services/tdevscriptproject.desktop
%{tde_datadir}/services/tdevsnippet.desktop
%{tde_datadir}/services/tdevsqlsupport.desktop
%{tde_datadir}/services/tdevtexttools.desktop
%{tde_datadir}/services/tdevtipofday.desktop
%{tde_datadir}/services/tdevtmakeproject.desktop
%{tde_datadir}/services/tdevtools.desktop
%{tde_datadir}/services/tdevtrollproject.desktop
%{tde_datadir}/services/tdevuichooser.desktop
%{tde_datadir}/services/tdevvalgrind.desktop
%{tde_datadir}/services/tdevvcsmanager.desktop
%{tde_datadir}/services/perldoc.protocol
%{tde_datadir}/services/pydoc.protocol
%{tde_datadir}/servicetypes/tdevelopappfrontend.desktop
%{tde_datadir}/servicetypes/tdevelopcodebrowserfrontend.desktop
%{tde_datadir}/servicetypes/tdevelopcompileroptions.desktop
%{tde_datadir}/servicetypes/tdevelopcreatefile.desktop
%{tde_datadir}/servicetypes/tdevelopdifffrontend.desktop
%{tde_datadir}/servicetypes/tdevelopdocumentationplugins.desktop
%{tde_datadir}/servicetypes/tdeveloplanguagesupport.desktop
%{tde_datadir}/servicetypes/tdevelopmakefrontend.desktop
%{tde_datadir}/servicetypes/tdeveloppcsimporter.desktop
%{tde_datadir}/servicetypes/tdevelopplugin.desktop
%{tde_datadir}/servicetypes/tdevelopproject.desktop
%{tde_datadir}/servicetypes/tdevelopquickopen.desktop
%{tde_datadir}/servicetypes/tdevelopsourceformatter.desktop
%{tde_datadir}/servicetypes/tdevelopvcsintegrator.desktop
%{tde_datadir}/servicetypes/tdevelopversioncontrol.desktop
%{tde_datadir}/apps/tdevcsharpsupport/tdevcsharpsupport.rc
%{tde_datadir}/apps/tdevctags2/tdevpart_ctags2.rc
%{tde_datadir}/apps/tdevcustomproject/tdevcustomproject.rc
%{tde_datadir}/apps/tdevdebugger/
%{tde_datadir}/apps/tdevdesigner/tdevdesigner_shell.rc
%{tde_datadir}/apps/tdevdesignerpart/tdevdesigner_part.rc
%{tde_datadir}/apps/tdevdesignerpart/tdevdesigner_part_sh.rc
%{tde_datadir}/apps/tdevdiff/tdevdiff.rc
%{tde_datadir}/apps/tdevdistpart/tdevpart_distpart.rc
%{tde_datadir}/apps/tdevdocumentation/
%{tde_datadir}/apps/tdevdoxygen/tdevdoxygen.rc
%{tde_datadir}/apps/tdevelop/
%{tde_datadir}/apps/tdevfilecreate/
%{tde_datadir}/apps/tdevfilelist/tdevfilelist.rc
%{tde_datadir}/apps/tdevfilter/tdevfilter.rc
%{tde_datadir}/apps/tdevfortransupport/tdevfortransupport.rc
%{tde_datadir}/apps/tdevfullscreen/tdevpart_fullscreen.rc
%{tde_datadir}/apps/tdevgrepview/
%{tde_datadir}/apps/tdevjavasupport/tdevjavasupport.rc
%{tde_datadir}/apps/tdevmakeview/tdevmakeview.rc
%{tde_datadir}/apps/tdevpartexplorer/tdevpartexplorer.rc
%{tde_datadir}/apps/tdevpascalproject/tdevpascalproject.rc
%{tde_datadir}/apps/tdevpascalsupport/tdevpascalsupport.rc
%{tde_datadir}/apps/tdevperlsupport/tdevperlsupport.rc
%{tde_datadir}/apps/tdevphpsupport/tdevphpsupport.rc
%{tde_datadir}/apps/tdevphpsupport/phpfunctions
%{tde_datadir}/apps/tdevpythonsupport/tdevpythonsupport.rc
%{tde_datadir}/apps/tdevquickopen/tdevpart_quickopen.rc
%{tde_datadir}/apps/tdevrbdebugger/
%{tde_datadir}/apps/tdevregexptest/tdevregexptest.rc
%{tde_datadir}/apps/tdevreplace/tdevpart_replace.rc
%{tde_datadir}/apps/tdevrubysupport/tdevrubysupport.rc
%{tde_datadir}/apps/tdevrubysupport/pics/ruby_config.png
%{tde_datadir}/apps/tdevrubysupport/pics/ruby_run.png
%{tde_datadir}/apps/tdevscripting/tdevscripting.rc
%{tde_datadir}/apps/tdevscriptproject/tdevscriptproject.rc
%{tde_datadir}/apps/tdevsnippet/tdevpart_snippet.rc
%{tde_datadir}/apps/tdevsqlsupport/tdevsqlsupport.rc
%{tde_datadir}/apps/tdevtipofday/tdevpart_tipofday.rc
%{tde_datadir}/apps/tdevtipofday/tips
%{tde_datadir}/apps/tdevtools/tdevpart_tools.rc
%{tde_datadir}/apps/tdevtrollproject/tdevtrollproject.rc
%{tde_datadir}/apps/tdevvalgrind/tdevpart_valgrind.rc
%{tde_datadir}/apps/tdeio_pydoc/tde_pydoc.py*
%{tde_datadir}/config/tdevassistantrc
%{tde_datadir}/config/tdeveloprc
%{tde_datadir}/desktop-directories/tde-development-tdevelop.directory
%{tde_tdedocdir}/HTML/en/tdevelop/
%{tde_libdir}/libd.so.0
%{tde_libdir}/libd.so.0.0.0
%{tde_libdir}/libkinterfacedesigner.so.0
%{tde_libdir}/libkinterfacedesigner.so.0.0.0
%{tde_tdelibdir}/libtdevvisualboyadvance.la
%{tde_tdelibdir}/libtdevvisualboyadvance.so
%{tde_datadir}/apps/tdevdesignerpart/pics/
%{tde_datadir}/apps/tdevvisualboyadvance/tdevpart_visualboyadvance.rc
%{tde_tdedocdir}/HTML/en/tde_app_devel/
%{tde_datadir}/mimelnk/text/x-fortran.desktop
%{tde_datadir}/services/tdevvisualboyadvance.desktop
%{tde_tdedocdir}/HTML/en/tdevdesigner/
%{tde_datadir}/applnk/.hidden/tde_app_devel.desktop
%{tde_tdedocdir}/HTML/en/tdevassistant/
 
%post
for f in hicolor locolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

%postun
for f in hicolor locolor ; do
  touch --no-create %{tde_datadir}/icons/$f 2> /dev/null ||:
  gtk-update-icon-cache -q %{tde_datadir}/icons/$f 2> /dev/null ||:
done
update-desktop-database %{tde_datadir}/applications > /dev/null 2>&1 || :

##########

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name}-libs = %{version}-%{release}

Obsoletes:	trinity-kdevelop-devel < %{version}-%{release}
Provides:	trinity-kdevelop-devel = %{version}-%{release}

%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{tde_libdir}/lib*.so
%{tde_libdir}/lib*.la
%{tde_includedir}/*

%post devel
/sbin/ldconfig || :

%postun devel
/sbin/ldconfig || :

##########

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-tdelibs >= %{tde_version}
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{version}-%{release}

Obsoletes:	trinity-kdevelop-libs < %{version}-%{release}
Provides:	trinity-kdevelop-libs = %{version}-%{release}

%description libs
%{summary}.

%files libs
%defattr(-,root,root,-)
%{tde_libdir}/libdesignerintegration.so.0
%{tde_libdir}/libdesignerintegration.so.0.0.0
%{tde_libdir}/libdocumentation_interfaces.so.0
%{tde_libdir}/libdocumentation_interfaces.so.0.0.0
%{tde_libdir}/libgdbmi_parser.so.0
%{tde_libdir}/libgdbmi_parser.so.0.0.0
%{tde_libdir}/libtdevbuildbase.so.0
%{tde_libdir}/libtdevbuildbase.so.0.0.0
%{tde_libdir}/libtdevbuildtoolswidgets.so.0
%{tde_libdir}/libtdevbuildtoolswidgets.so.0.0.0
%{tde_libdir}/libtdevcatalog.so.0
%{tde_libdir}/libtdevcatalog.so.0.0.0
%{tde_libdir}/libtdevcppparser.so.0
%{tde_libdir}/libtdevcppparser.so.0.0.0
%{tde_libdir}/libtdevelop.so.1
%{tde_libdir}/libtdevelop.so.1.0.0
%{tde_libdir}/libtdevextras.so.0
%{tde_libdir}/libtdevextras.so.0.0.0
%{tde_libdir}/libtdevpropertyeditor.so.0
%{tde_libdir}/libtdevpropertyeditor.so.0.0.0
%{tde_libdir}/libtdevqmakeparser.so.0
%{tde_libdir}/libtdevqmakeparser.so.0.0.0
%{tde_libdir}/libtdevshell.so.0
%{tde_libdir}/libtdevshell.so.0.0.0
%{tde_libdir}/libtdevwidgets.so.0
%{tde_libdir}/libtdevwidgets.so.0.0.0
%{tde_libdir}/liblang_debugger.so.0
%{tde_libdir}/liblang_debugger.so.0.0.0
%{tde_libdir}/liblang_interfaces.so.0
%{tde_libdir}/liblang_interfaces.so.0.0.0
%{tde_libdir}/libprofileengine.so.0
%{tde_libdir}/libprofileengine.so.0.0.0

%post libs
/sbin/ldconfig || :

%postun libs
/sbin/ldconfig || :

##########

%if 0%{?suse_version} || 0%{?pclinuxos}
%debug_package
%endif

##########

%prep
%setup -q -n %{name}-%{version}%{?preversion:~%{preversion}} -a 1
%patch1 -p0 -b .config
%patch4 -p1

%__cp -f "/usr/share/aclocal/libtool.m4" "admin/libtool.m4.in"
%__cp -f "/usr/share/libtool/config/ltmain.sh" "admin/ltmain.sh" || %__cp -f "/usr/share/libtool/ltmain.sh" "admin/ltmain.sh"

%__rm -rf c_cpp_reference-2.0.2_for_KDE_3.0/admin
%__cp -ar admin c_cpp_reference-2.0.2_for_KDE_3.0/
%__make -C c_cpp_reference-2.0.2_for_KDE_3.0 -f admin/Makefile.common cvs


%build
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

# Specific path for RHEL4
if [ -d /usr/X11R6 ]; then
  export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -I/usr/X11R6/include -L/usr/X11R6/%{_lib}"
fi

# c references
pushd c_cpp_reference-2.0.2_for_KDE_3.0
%configure \
  --prefix=%{tde_prefix} \
  --exec-prefix=%{tde_prefix} \
  --bindir=%{tde_bindir} \
  --libdir=%{tde_libdir} \
  --datadir=%{tde_datadir} \
  --includedir=%{tde_tdeincludedir} \
  --with-extra-libs=%{tde_libdir}
popd

if ! rpm -E %%cmake|grep -q "cd build"; then
  %__mkdir_p build
  cd build
fi

# Warning: GCC visibility causes FTBFS [Bug #1285]
%cmake \
  -DCMAKE_BUILD_TYPE="RelWithDebInfo" \
  -DCMAKE_C_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS} -DNDEBUG" \
  -DCMAKE_SKIP_RPATH=OFF \
  -DCMAKE_INSTALL_RPATH="%{tde_libdir}" \
  -DCMAKE_VERBOSE_MAKEFILE=ON \
  -DWITH_GCC_VISIBILITY=OFF \
  \
  -DBIN_INSTALL_DIR=%{tde_bindir} \
  -DINCLUDE_INSTALL_DIR=%{tde_tdeincludedir} \
  -DLIB_INSTALL_DIR=%{tde_libdir} \
  -DSHARE_INSTALL_PREFIX=%{tde_datadir} \
  \
  -DWITH_BUILDTOOL_ALL=ON \
  -DWITH_LANGUAGE_ALL=ON \
  -DWITH_VCS_ALL=OFF \
  -DBUILD_ALL=ON \
  ..

%__make %{?_smp_mflags} || %__make

# c references
cd ..
%__make %{?_smp_mflags} -C c_cpp_reference-2.0.2_for_KDE_3.0

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot} -C build
%__make install DESTDIR=%{buildroot} -C c_cpp_reference-2.0.2_for_KDE_3.0

# Moves C reference to correct location
%__mv -f %{?buildroot}%{tde_tdedocdir}/HTML/en/kdevelop/reference %{?buildroot}%{tde_tdedocdir}/HTML/en/tdevelop/
%__rm -rf %{?buildroot}%{tde_tdedocdir}/HTML/en/kdevelop


%clean
%__rm -rf %{buildroot}


%changelog
* Fri Jul 05 2013 Francois Andriot <francois.andriot@free.fr> - 14.0.0-1
- Initial release for TDE 14.0.0
