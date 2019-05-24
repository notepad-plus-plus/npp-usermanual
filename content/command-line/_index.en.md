---
title: Command Line
weight: 120
---

Notepad++.exe [-multiInst] [-noPlugin] [-ro] [-nosession] [-notabbar] [-n##] [-l$$$] [FILES]
Notepad++ supports a few command line parameters to control its startup. The following options are supported (they are case sensitive):

-nline number
Line number to go to for each file opened.
-c
Start editing in Column mode.
--help
Displays this list, i.e. all the command line switches
-loadingTime
Displays the loading time of all files Notepad++ is started with. The result is displayed in a message box, with a 0.01 second resolution.
-multiInst
allow Notepad++ to start more than one instance. By default, if Notepad++ is already started files wil lbe opened in that instance, but this option will start a new one.
-noPlugin
Do not load any plugins. If you suspect a defunct plugin or you just do not wish to load them, add this option.
-ro
Any file now opened will be opened in Read only mode.
-nosession
Do not load the previous session if Notepad++ is started. Do not save the session on exit either.
-notabbar
Hide the Tab Bar, even if the settings say otherwise.
-systemtray
Start Notepad++ minimised in the system tray, aka notification area
-xline number
Specify the horizontal position (in pixels) at which Notepad++ main window is to open.
-yline number
Specify the vertical position (in pixels) at which Notepad++ main window is to open.
-llanguage short name
Language to set for each file opened. $$$ is a short identifier string, of which the following are allowed:

normal, php, c, cpp, cs, objc, d, java, rc, html, xml, makefile, pascal, batch, ini, nfo, asp, sql, vb, javascript, css, perl, python, lua, tex, cobol, fortran, bash, actionscript, nsis, tcl, lisp, scheme, asm, diff, props, postscript, ruby, smalltalk, vhdl, kix, autoit, Gui4Cli, powershell, caml, ada, verilog, matlab, haskell, inno, cmake, yaml,r, jsp
Files
Anything else will be interpreted as a filename. Always quote your filename to allow the path to contain spaces, otherwise Notepad++ will split the single path into multiple paths at each space.
 

The order of the options is not important.

For compatibility, Notepad++ will first try to identify the entire command line as a filename, even if it is unquoted. It is however not recommended to do this, always quote the filename.
