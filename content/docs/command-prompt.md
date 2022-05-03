---
title: Usage via the command prompt
linktitle: Command prompt
weight: 120
---

Notepad++ supports various case-sensitive command line parameters
to control its startup and affect its behavior.

## Help usage

```
notepad++ [--help] [-multiInst] [-noPlugin] 
  [-l<Language>] [-udl="My UDL Name"]
  [-L<langCode>]
  [-n<line>] [-c<column>] [-p<pos>] [-x<left-pos>] [-y<TopPos>]
  [-nosession] [-notabbar] [-ro] [-systemtray] [-loadingTime]
  [-alwaysOnTop] [-openSession] [-r]
  [-qn="Easter Egg Name" | -qt="Text to Type" | -qf="D:\path to\file"]
  [-qSpeed(1|2|3)] [-quickPrint]
  [-settingsDir="d:\your settings dir\"] [-openFoldersAsWorkspace]
  [-titleAdd="additional title bar text"]
  [-pluginMessage="text for plugin(s)"]
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
* `-udl="My UDL Name"`: Open file with User Defined Language (UDL) syntax 
  highlighting `My UDL Name` active.  If the UDL name does not conain spaces, the
  quote marks aren't required around the name (like `-udl=MyUDL`). The UDL name
  should match an existing UDL.  Mutually exclusive with `-l` (UDL will take priority 
  over standard syntax highlighter).  (new to v8.1.2)
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
* `-qn="Easter Egg Name"`: Launch [ghost typing](../ghost-typing/) to display easter egg via its *Easter Egg Name*.
* `-qt="Text to Type"`: Launch [ghost typing](../ghost-typing/) to display a text via the given *Text to Type*
* `-qf="D:\path to\file"`: Launch [ghost typing](../ghost-typing/) to display a file content via the file path *D:\path to\file*
* `-qSpeed(1|2|3)`: [Ghost typing](../ghost-typing/) speed. Value from 1 to 3 for slow, fast, and fastest
* `-quickPrint`: Print the file given as argument `filepath` then quit Notepad++
* `-settingsDir="d:\your settings dir\"`: Override the default settings dir (new to v7.9.2)
* `-openFoldersAsWorkspace`: Any folders listed as arguments will be opened as a workspace, rather than opening all the contained files individually (new to v7.8)
* `-titleAdd="additional title bar text"`: Add a dash and a space and the supplied text to the right side of the application title bar (new to v8.0.0)
* `-pluginMessage="text for plugin(s)"`: if plugin developers need extra command line arguments, then users can add this option, and the plugin will be [notified](../plugin-communication/#notepad-notifications) that it can parse that string for extra information
* `filepath`: file or folder name to open (absolute or relative path name)

The order of the options is not important.  Brackets indicate that the options
are not required, and are _not_ part of the command-line argument.  The number
of hyphens is significant, and the options are case sensitive.

For compatibility, Notepad++ will first try to identify the entire command line
as a filename, even if it is unquoted. It is however not recommended to do this,
as you should always quote the filename.

This help usage list can be accessed inside Notepad++ using the `--help` command
line argument, or using the **?**-menu's **Command Line Arguments** entry.

### Additional Options

There are other Notepad++ command-line options which aren't included in the help
usage list.  These are intended for advanced usage or other special circumstances.

* `-notepadStyleCmdline`: When you follow the instructions in
  [Other Resources > Notepad Replacement](../other-resources/#notepad-replacement),
  to replace Windows' builtin `notepad.exe` with Notepad++, Windows will try to pass `/p` or `/P` as
  a command-line option when you try to print the file from the Explorer Context menu.
  Enabling this option allows Notepad++ to recognize that option, and convert it internally
  to the official `-quickPrint` option.
* `-z`: Strips out any command line arguments found after this option. Its only intended and 
  supported use is for the [Notepad Replacement](../other-resources/#notepad-replacement)

## Installer Options

The Notepad++ [installer executable](../getting-started/#installer) accepts the [three NSIS command-line options](https://nsis.sourceforge.io/Which_command_line_parameters_can_be_used_to_configure_installers):

* `/S` : silent installation
* `/NCRC`: skips the installer's CRC check
* `/D=c:\blah` or `/D=c:\path with spaces\blah` : overrides the default installation directory.
    * Do _not_ put quotes around the path, even when there are spaces.
    * Because it allows spaces in the path, this option **must** be the last argument on the installer command line, if included.
