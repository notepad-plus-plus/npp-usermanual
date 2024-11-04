---
title: Other Resources
weight: 210
---

## Restartable App

Windows 10 and Windows 11 have a "restartable apps" feature (**Windows Start Button > Settings > Accounts > Sign In Options > Restart Apps**) which automatically saves the state of various "restartable apps" when you log out of Windows then back in.  Starting with v8.5.8, Notepad++ is now a "restartable app" -- so if you log out or reboot with Notepad++ running, and have that Windows setting active, then when you next log in, Notepad++ will reload right where you were.  If you would like to _disable_ Notepad++ from being restartable, add an empty [config file](../config-files/#other-configuration-files) called `noRestartAutomatically.xml` into `%APPDATA%\Notepad++\` (for normal installations) or the Notepad++ installation directory (for other configuration settings).

## Notepad++ Cheat sheet

The "Notepad++ Cheat Sheet" has been moved to become the [User Interface](../user-interface) page, including

- <a href="../user-interface/#tabs" id="tabs">Tabs</a>
- <a href="../user-interface/#tab-bar-right-click-menu" id="tab-bar-right-click-menu">Tab Bar Right Click Menu</a>
- <a href="../user-interface/#menu-bar" id="menu-bar">Menu Bar</a>
- <a href="../user-interface/#toolbar" id="toolbar">Toolbar</a>
- <a href="../user-interface/#tools-menu" id="tools-menu">Tools Menu</a>

## Explorer Right-Click menu
<a name="missing-edit-with-notepad-action"></a>
<a name="windows-11-right-click-workarounds"></a>

To get Notepad++ as the default application for a given filetype, you can use the [**Settings > Preferences > File Association**](../preferences/#file-association); or you can use the Windows OS's built-in **Open With** right-click menu to pick Notepad++ either one time or as the default double-click command.  Or you can use the **Edit with Notepad** action from the [shell extension (Right Click Context Entry)](../shell-extension/) that Notepad++ normally installs for you, or follow the list of ["Alternatives"](../shell-extension/#alternatives) on that page of the User Manual.

## Notepad Replacement

Windows ships with the simple Notepad (`notepad.exe`) text editor as the default editor for text-based files. As a Notepad++ user, you probably want to set up Windows so that it usually uses Notepad++ for various filetypes instead. 

The _right_ way to use Notepad++ for a given filetype, from the Windows OS perspective, is to use the [Explorer Right-Click menu](#explorer-right-click-menu), especially using Windows' **Open With** to always use Notepad++ and/or pick it on a one-time-only basis, or using the **Edit with Notepad++** entry that Notepad++ installs for you, or following the ["Alternatives"](../shell-extension/#alternatives) described elsewhere.

However, there are rare circumstances (such as where some other application has an "edit this file in Notepad" button, but doesn't let you customize the application), where it might be useful to trick Windows into running Notepad++ instead of `notepad.exe`.  This requires an edit to the registry[†](#registry-edit-warning) that you should only perform if you really understand what you're doing, and only if you fully understand everything that's explained here, and all the implications of what you are doing. (Really, it would be better to ask if the other application could add a setting to customize the text editor it launches, rather than doing this hack.)

If you are certain you want to do this hack, rather than just associating filetypes with Notepad++ or using **Edit With Notepad++** or Windows' **Open With** feature, the explanation of how to implement this hack will follow, though it is not recommended usage.

### Registry Edit Warning

_**† Warning**: editing your registry can be dangerous; edit your registry at your own risk; the developers of Notepad++ and contributors to this documentation cannot and will not be held responsible for mistakes made during registry changes or unintendended consequences of such edits_

### Implement the Notepad Replacement Hack

You can run the following commands to edit the registry following command to make Notepad++ replace Notepad (run in `cmd.exe` with Administrator privileges)[†](#registry-edit-warning), or use `regedit` directly to set the same keys and values described below.

For Windows 7 - Windows 10, use the following command:

```batch
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v "Debugger" /t REG_SZ /d "\"%ProgramFiles%\Notepad++\notepad++.exe\" -notepadStyleCmdline -z" /f
```

Note that you may need to use `%ProgramFiles(x86)%\Notepad++\` to substitute for `%ProgramFiles%\Notepad++\` if you have Notepad++ 32-bit installed, or use other path if your Notepad++ is installed in a non-default location.

For Windows 11 onward: first uninstall Notepad (just right-click on the Notepad shortcut in **Start Menu** and select **Uninstall**), and then run the commands below:

```batch
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe\0" /v Debugger /t REG_SZ /d "\"%ProgramFiles%\Notepad++\notepad++.exe\" -notepadStyleCmdline -z" /f

reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe\1" /v Debugger /t REG_SZ /d "\"%ProgramFiles%\Notepad++\notepad++.exe\" -notepadStyleCmdline -z" /f

reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe\2" /v Debugger /t REG_SZ /d "\"%ProgramFiles%\Notepad++\notepad++.exe\" -notepadStyleCmdline -z" /f

reg delete HKCR\Applications\notepad.exe /v NoOpenWith /f
```

**Note**: Windows 11 introduced UWP version of Notepad that use the same technique as described (but with undocumented [UseFilter](https://www.geoffchappell.com/studies/windows/win32/ntdll/api/rtl/rtlexec/openimagefileoptionskey.htm)) to replace the built-in Notepad. As UWP apps are started differently than regular apps, they cannot be replaced the same way and UWP Notepad must be uninstalled. Otherwise it would start when opening text files or when run from **Start Menu**. What\`s more, to be able to again use built-in Notepad (now redirected to Notepad++) to open text files the `NoOpenWith` registry value must be removed (based on [How to Restore Old Classic Notepad in Windows 11](https://www.winhelponline.com/blog/restore-old-classic-notepad-windows/)).

#### Undo the Notepad Replacement Hack

For Windows 7 - Windows 10, use the the following command to undo the replacement:

```batch
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v Debugger /f
```

For Windows 11 onward: reinstall Notepad (launch **Microsoft Store** via **Start Menu**, search "Windows Notepad", select it and then click on **Install** button) and then run the commands below:

```batch
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe\0" /v Debugger /f
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe\1" /v Debugger /f
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe\2" /v Debugger /f
reg add HKCR\Applications\notepad.exe /v NoOpenWith /t REG_SZ /f
```
