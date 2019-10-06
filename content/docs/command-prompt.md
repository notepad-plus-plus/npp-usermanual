---
title: Usage via the command prompt
linktitle: Command prompt
weight: 120
---

Notepad++ supports a few command line parameters to control its startup. The syntax is (case sensitive):

## Help usage

```
notepad++ [--help] [-multiInst] [-noPlugin] [-l<lang>] [-n<line>] [-c<column>]
  [-p<pos>] [-x<left-pos>] [-y<TopPos>] [-nosession] [-notabbar] [-ro]
  [-systemtray] [-loadingTime] [-alwaysOnTop] [-openSession] [-r]
  [-qn<EasterEggName> | -qt<Text> | -qf<ContentFileName>]
  [-qSpeed(1|2|3)] [-quickPrint]
  [filepath]
```


* `--help`: The help message for command line arguments. It will be shown before
  Notepad++'s launch.
* `-multiInst`: Launch another Notepad++ instance, so user can have several
  Notepad++ simultaneously.
* `-noPlugin`: Launch Notepad++ without loading any plugin.
* `-l`: Open file or display ghost typing with syntax highlighting of choice.
  *Language* is a short identifier string, of which the following are allowed:  
  `normal`, `php`, `c`, `cpp`, `cs`, `objc`, `d`, `java`, `rc`, `html`, `xml`,
  `makefile`, `pascal`, `batch`, `ini`, `nfo`, `asp`, `sql`, `vb`, `javascript`,
  `css`, `perl`, `python`, `lua`, `tex`, `cobol`, `fortran`, `bash`,
  `actionscript`, `nsis`, `tcl`, `lisp`, `scheme`, `asm`, `diff`, `props`,
  `postscript`, `ruby`, `smalltalk`, `vhdl`, `kix`, `autoit`, `Gui4Cli`,
  `powershell`, `caml`, `ada`, `verilog`, `matlab`, `haskell`, `inno`, `cmake`, `yaml`, `r` and `jsp`.
* `-n`: Scroll to indicated line (*LineNumber*) on `filepath`.
* `-c`: Scroll to indicated column (*ColumnNumber*) on `filepath`.
* `-p`: Scroll to indicated 0 base position (*Position*) on `filepath`.
* `-x`: Move Notepad++ to indicated left side position (*LeftPos*) on the screen.
* `-y`: Move Notepad++ to indicated top position (*TopPos*) on the screen.
* `-nosession`: Launch Notepad++ without previous session.
* `-notabbar`: Launch Notepad++ without tabbar.
* `-ro`: Make the `filepath` read only.
* `-systemtray`: Launch Notepad++ directly in system tray.
* `-loadingTime`: Display Notepad++ loading time.
* `-alwaysOnTop`: Make Notepad++ always on top.
* `-openSession`: Open a session. `filepath` must be a session file.
* `-openFoldersAsWorkspace`: Any folders listed as arguments will be opened as a workspace, rather than opening all the contained files individually (new to v7.8)
* `-r`: Open files recursively. This argument will be ignored if
  `filepath` contain no wildcard character.
* `-qn`: Launch ghost typing to display easter egg via its *EasterEggName*.
* `-qt`: Launch ghost typing to display a text via the given *Text*
* `-qf`: Launch ghost typing to display a file content via the file path *ContentFileName*
* `-qSpeed`: Ghost typing speed. Value from 1 to 3 for slow, fast and fastest
* `-quickPrint`: Print the file given as argument `filepath` then quit Notepad++
* `filepath`: file or folder name to open (absolute or relative path name)


The order of the options is not important.

For compatibility, Notepad++ will first try to identify the entire command line
as a filename, even if it is unquoted. It is however not recommended to do this,
always quote the filename.
