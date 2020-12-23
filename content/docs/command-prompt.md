---
title: Usage via the command prompt
linktitle: Command prompt
weight: 120
---

Notepad++ supports various case-sensitive command line parameters
to control its startup and affect its behavior.

## Help usage

```
notepad++ [--help] [-multiInst] [-noPlugin] [-l<Language>] [-L<langCode]
  [-n<line>] [-c<column>] [-p<pos>] [-x<left-pos>] [-y<TopPos>]
  [-nosession] [-notabbar] [-ro] [-systemtray] [-loadingTime]
  [-alwaysOnTop] [-openSession] [-r]
  [-qn<EasterEggName> | -qt<Text> | -qf<ContentFileName>]
  [-qSpeed(1|2|3)] [-quickPrint]
  [-settingsDir="d:\your settings dir\"] [-openFoldersAsWorkspace]
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
* `-L`: Apply indicated localization, *langCode* is browser language code
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
* `-r`: Open files recursively. This argument will be ignored if `filepath` contain no wildcard character.
* `-qn`: Launch ghost typing to display easter egg via its *EasterEggName*.
* `-qt`: Launch ghost typing to display a text via the given *Text*
* `-qf`: Launch ghost typing to display a file content via the file path *ContentFileName*
* `-qSpeed`: Ghost typing speed. Value from 1 to 3 for slow, fast and fastest
* `-quickPrint`: Print the file given as argument `filepath` then quit Notepad++
* `settingsDir="d:\your settings dir\"`: Override the default settings dir
* `-openFoldersAsWorkspace`: Any folders listed as arguments will be opened as a workspace, rather than opening all the contained files individually (new to v7.8)
* `filepath`: file or folder name to open (absolute or relative path name)


The order of the options is not important.  Brackets indicate that the options
are not required, and are _not_ part of the command-line argument.  The number
of hyphens is significant, and the options are case sensitive.

For compatibility, Notepad++ will first try to identify the entire command line
as a filename, even if it is unquoted. It is however not recommended to do this,
as you should always quote the filename.

This help usage list can be accessed inside Notepad++ using the `--help` command
line argument, or using the **?**-menu's **Command Line Arguments** entry.

## Additional Options

There are other Notepad++ command-line options which aren't included in the help
usage list.  These are intended for advanced usage or other special circumstances.

* `-notepadStyleCmdline`: When you follow the instructions in
  [Other Resources > Notepad Replacement](../other-resources/#notepad-replacement),
  to replace Windows' builtin `notepad.exe` with Notepad++, Windows will try to pass `/p` or `/P` as
  a command-line option when you try to print the file from the Explorer Context menu.
  Enabling this option allows Notepad++ to recognize that option, and convert it internally
  to the official `-quickPrint` option.
* `-z`: Strips out any command line arguments found after this option. Aside from its use
  in the [Notepad Replacement](../other-resources/#notepad-replacement), this can be used
  to pass options to plugins, by placing the plugin's options after the `-z` in the command
  line, and having the plugin parse through the command line to determine if the option is present.
  An example of this technique can be found in
  [this Notepad++ Community Forum post](https://community.notepad-plus-plus.org/post/52805),
  where a script run using the PythonScript plugin is able to use a command-line option
  to affect the script's behavior.
