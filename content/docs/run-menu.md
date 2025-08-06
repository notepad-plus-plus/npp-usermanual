---
title: Running External Commands
linktitle: run-menu
weight: 100
---

The **Run** menu allows you to run arbitrary external commands from inside Notepad++, and to save the commands into new entries in the **Run** menu and even to assign keyboard shortcuts to those saved commands.  Because of the variable syntax (defined in the [Configuration Files Details > User Defined Commands](../config-files/#userdefinedcommands) section of this manual), you can even use the filename or the current selected text or similar as arguments to the programs. [That section of the manual](../config-files/#userdefinedcommands) also describes the underlying format of how saved **Run**-menu commands are stored in the `shortcuts.xml` config file.

## Dialog

The **Run > Run...** menu entry launches the **Run...** dialog, which is the way to run a new command.

You can type any command that you could type from the Windows OS **Run** dialog (`Win+R` or **Start Menu > Run**).  If you prefix the command with `cmd.exe /c` (making sure to use appropriate syntax), it will run the command in an old Windows command prompt window; prefixing with `cmd.exe /k` will run it in the command prompt window and will keep the window open after the command is done.  If you use a valid PowerShell command starting with `powershell.exe`, it will run the command in the PowerShell environment.

The **Program to Run** entry field allows you to type the command to run.  If the command is not in your PATH, you will need to use `c:\full\path\to\application.exe`.  If you need a path that has spaces in it, make sure to use quotes around the path, like `"c:\program files\myapp\myapplication.exe" "d:\some other\file name\as argument.txt"` (following `cmd.exe` argument quoting rules).  The pulldown for this entry remembers previous commands you've run in this instance of Notepad++.  The `...` button allows you to browse for the program executable to run.  The `+` button allows you to easily insert any of the [user-defined command variables](../config-files/#variables-for-run-commands) into your command (new to v8.8.4).

The **Run** button actually runs the command.

The **Save...** button brings up a dialog to save the command you've typed as a named entry for the **Run** menu.  You can also assign the saved command a keyboard shortcut for use inside Notepad++ in that sub-dialog.  **OK** will save the command (with the shortcut you defined); **Cancel** will abort the process, so the command doesn't get saved.

The **Cancel** button (or the upper right X in the dialog) will allow you to exit the dialog without running the command.  This is useful if you've changed your mind about running the external process, or if you just wanted to **Save** the command but not immediately run it.

## Running Saved Commands

If you've saved commands, they will show up underneath the **Run...** entry in the **Run** menu.  You can execute those commands by clicking on them.

## Manage Shortcuts

**Run > Modify Shortcut / Delete Command** will allow you to add or change or delete the shortcut for a command, or remove the command from the **Run** menu, using the [Shortcut Mapper](../preferences/#shortcut-mapper) interface.  But in short: stay on the **Run Commands** tab of the **Shortcut Mapper** to deal with the **Run** menu entries; **Modify** will allow you to add or edit a shortcut; **Clear** will remove the shortcut but leave the command in the menu; **Delete** will completely remove the command from the menu; **Close** will exit the **Shortcut Mapper** dialog.

## Example Usage

### Run the Current File with its default association

The Windows OS defines default file associations based on the file extension.  If you run the command
```
"$(FULL_CURRENT_PATH)"
```
the OS will take the saved contents of the file and run them based on the file extension (so a `.bat` file would run as normal, a `.csv` might launch a spreadsheet program, a `.py` file might run your installed Python interpreter, and so on).

### Additional Browser Options

The Run menu can be an alternative to the **View** menu's [**View Current File In...**](../views/#view-current-file-in) submenu: if you don't like the browser selection available, you can use the `"$(FULL_CURRENT_PATH)"` shown earlier to run your `.html` file with your default browser (whatever browser Windows uses when you double-click a `.html` file).  If you want even more options, define additional commands like `"c:\program files\alternate browser\browser.exe" "$(FULL_CURRENT_PATH)"` to load the active file in whatever browser you want.

### Enter Fancy Characters

If you don't have a fancy Unicode keyboard, or if you want to be able to enter emojis, you could save a run menu command that runs `charmap.exe` to run windows built-in character map.  Or if you have a super-fancy emoji keyboard app, you could run `"c:\program files\super fancy emoji keyboard\emojikeyboard.exe"` to launch that keyboard from inside Notepad++.

### Run your makefile

If you are editing source code, you might want to have a shortcut that will run `make` or `nmake` or `gmake` or similar build program in the current directory.

### Getting External Help

You could define **Run** menu entries to allow you to get help.  For example, running the command `https://en.wikipedia.org/wiki/Special:Search?search=$(CURRENT_WORD)` will look up the currently selected word (or the word where your [caret](#caret-and-cursor "typing/insertion cursor") is if you don't have a selection) in Wikipedia using your default browser.  Or running `https://docs.python.org/3/search.html?check_keywords=yes&amp;q=$(CURRENT_WORD)` will look up the current word in the Python 3 online documentation.

### A Filename in Your Text

If your [caret](#caret-and-cursor "typing/insertion cursor") or selection is on the name of a file in your text, you can open that file in the current Notepad++ instance by running:
```
"$(NPP_DIRECTORY)\notepad++.exe" "$(CURRENT_WORD)"
```

Or, if you want to force it to open in a new instance, use:
```
"$(NPP_DIRECTORY)\notepad++.exe" "$(CURRENT_WORD)" -nosession -multiInst
```

### You Are Limited Only By Your Imagination

If you can run it from `cmd.exe` or `powershell.exe` in a single command line, you can run it from here.  Let your imagination run wild.

## Going Beyond Single-Line Commands

If a single-line command isn't sufficient for your needs, you may want to consider one of the following options:

1. Write a batch file: writing a windows `.bat` or `.cmd` or `.ps1` file using cmd.exe or powershell syntax will allow you to specify a group of commands; you can then just use the **Run > Run...**  to call that batch file to do your more complicated task.  You can pass any of the [special variables](../config-files/#userdefinedcommands) as arguments to this batch file.

2. Use the [NppExec plugin](https://github.com/d0vgan/nppexec/): this plugin can be installed from the **Plugins > Plugins Admin** interface, and gives you access to a custom batch language, but with extended features that give you access to all the [special variables](../config-files/#userdefinedcommands) plus extra access to the internals of the Notepad++ interface.  This also allows you to view the output of commands in an embedded interactive console window that can be docked in Notepad++.  (Does not use the **Run** menu.)

3. Use [PythonScript](https://github.com/bruderstein/PythonScript) or [LuaScript](https://github.com/dail8859/LuaScript) or [jN Notepad++](https://github.com/sieukrem/jn-npp-plugin/wiki) plugins (or similar) to write a script in your favorite programming language (and all those languages should give you access to any feature of that language, plus a way to access applications that live on your filesystem).  These may provide interactive console windows to give you even more flexibility. (Does not use the **Run** menu.)

## Security is Your Responsibility

This menu allows you to run arbitrary programs from your PC.  Please ensure that you use paths to known safe applications.  Understand that you are solely responsible for what happens when you run an external application from Notepad++, and the developers of and contributors to Notepad++ are not responsible for or liable for external commands or the results of running them.
