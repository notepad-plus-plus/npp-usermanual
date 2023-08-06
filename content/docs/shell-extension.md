---
title: Right Click - Edit With Notepad++
weight: 190
---

## Shell Extension

Notepad++ installs with a Shell Extension -- a DLL which adds menu commands to the Windows Explorer right-click context menu.  If you choose to install it (and the Notepad++ installer does install it), then any file you right-click on will show an entry named “Edit with Notepad++” with the Notepad++ icon.

### Installation

Under normal circumstances, the Shell Extension was installed when you installed Notepad++.

Please note that to install or remove the extension, you most likely need to use Administrator privileges.  And after you install or remove it, it is sometimes required to restart the Explorer process. For this you can reboot, logout and log back in or use the task manager to kill explorer (Windows NT and up) and restart it again. You can do this by hitting Ctrl+Alt+Shift+Del.

If the Shell Extension is already installed, the Notepad++ installer/updater might not be able to update or overwrite it, so you might first have to uninstall it and restart Explorer.

#### Location and Name

If you used the installer to get Notepad++, then the Shell Extension file will exist as a DLL in your Notepad++ installation folder hierarchy: in versions before Notepad++ v8.5.1, it will be in the same directory as notepad++.exe, named as `NppShell_##.dll` (with ## being something like `01` - `06`); in Notepad++ v8.5.1 and later, it is now found in the `contextMenu\` subfolder of the Notepad++ installation, and is named plainly `NppShell.dll`.

#### Portable Notepad++

If you didn't use the installer, the DLL does not come with the portable edition.  The reason that portable Notepad++ does not ship with the Shell Extension is that registering a DLL usually requires administrative privileges, and is inherently non-portable.  Also, there may be subtle issues that arise because the application is not in the expected directory.

However, if you want to try to see if the Shell Extension will work for your particular portable circumstances, you are allowed (though success is not guaranteed or warrantied): you could download the installer, rename it to a `.zip`, and extract the Shell Extension DLL from that zip archive, which you can put in the correct location for your portable edition -- that is, alongside notepad++.exe for older versions, and in the `contextMenu\` subdirectory (which you may have to create yourself) for v8.5.1 and newer.  You would then have to register the DLL, as described below.

#### Manual Installation / Registration

If your installation process had problems with installing or updating the Shell Extension, or if you want to try the experiment of using the Shell Extension with your portable edition of Notepad++, you can manually register the DLL.  Registering the DLL may require elevating to elevated privileges.

**To Install / Register**: Open a command shell (`cmd.exe` or PowerShell or your favorite alternative command line environment) in the same directory where the Shell Extension DLL resides.  Run one of the commands listed below.  Some users have had more success with one or the other, so if you get an error with one, you may have to try another to get it to work.  (In these commands, `NppShell.dll` is shown, but if you are using an older Notepad++, use the name that came with your version of Notepad++.)

- `regsvr32 /i NppShell.dll` ⇒ This was the method recommended before Notepad++ v8.5.1
- `regsvr32 NppShell.dll` ⇒ This has been successful for some users on v8.5.1 and newer, for whom the `/i` version did not work

**To Uninstall / Unregister**: use the command below which corresponds to the install/register command you used above:

- `regsvr32 /U /i NppShell.dll`
- `regsvr32 /U NppShell.dll`

### Difficulties

It should be noted that the Shell Extension can have difficulty loading a file into Notepad++ if Notepad++ is in Admin mode.

In Windows 11, Microsoft significantly changed how Shell Extensions must be coded to get them to show up in the _main_ right-click menu.  In Notepad++ v8.5.1, Notepad++ has been working on improving its Shell Extension to get it to show **Edit with Notepad++** in the main right-click menu in Win 11, but different builds of Win 11 have subtly different behaviors.  If you are not seeing the entry, you might try using `Shift+F10` or `Shift+RightClick` instead of a normal `RightClick` to see if that shows the old-style Windows context-menu, and you might want to explore the alterntatives mentioned below.

## Alternatives

Notepad++ has [Settings > Preferences > File Association](../preferences/#file-association) which will add a Windows file-association, so that the default action when you double-click a particular type of file will be to open that file in Notepad++.  If you have Administrator privileges, that setting may be an alternative option for you.

If you are willing to edit your registry[†](#registry-edit-warning "edit your registry at your own risk"), there are some more options:

### Manual "Edit with Notepad++" Action

You can manually add an "Edit with Notepad++" action to your registry using your favorite registry-editing method[†](#registry-edit-warning "edit your registry at your own risk").  You could save the appropriate script below as a `.reg` file and run it, and it will update your registry for you.  Or you can use `regedit.exe` to use the GUI to edit the keys and values mentioned in the `.reg` files.  (To remove the manual entry, just remove the keys that are populated by these scripts or that you populated in regedit.)

#### SINGLE USER

This `.reg` adds the entry for a single user, and should not require administrative privileges:
```
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Classes\*\shell\Notepad++]
@="Edit With Notepad++"
"Icon"="C:\\Program Files\\Notepad++\\notepad++.exe,0"

[HKEY_CURRENT_USER\SOFTWARE\Classes\*\shell\Notepad++\command]
@="\"C:\\Program Files\\Notepad++\\notepad++.exe\" \"%1\""
```
(If your installation is not in `c:\Program Files\Notepad++`, you will have to adjust that script.)

#### ALL USERS

This `.reg` adds the entry for all users on a machine, and will require administrative privileges:

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\Notepad++]
@="Edit With Notepad++"
"Icon"="C:\\Program Files\\Notepad++\\notepad++.exe,0"

[HKEY_CLASSES_ROOT\*\shell\Notepad++\command]
@="\"C:\\Program Files\\Notepad++\\notepad++.exe\" \"%1\""
```
(If your installation is not in `c:\Program Files\Notepad++`, you will have to adjust that script.)

### Windows 11 Right-Click Workarounds

Windows 11 hides the old right click menu, so even with a normal installation or if you've manually added those associations, the **Edit with Notepad++** might not be visible for you in Windows 11; though starting with v8.5.1, the installer should put the action in the main Windows 11 right-click menu again. If you don't see the entry, the Windows right click menu contains a **Show More Options** action which will bring up the classic right click context menu with the old actions; this can also be accessed using the <kbd>Shift+F10</kbd> shortcut or <kbd>Shift+RightClick</kbd> on a file instead of right-clicking, depending on which build of Win 11 you are using.

If that is not sufficient for you, https://www.tomshardware.com/how-to/windows-11-classic-context-menus describes a possible method of changing your registry[†](#registry-edit-warning "edit your registry at your own risk") to get the classic right click context menu by default again in Windows 11.

If you would rather have it in your modern Windows 11 right click, and are willing to lose Windows's "pin to home" feature, the following `.reg` files might bring **Edit with Notepad++** to your Windows 11 right click[†](#registry-edit-warning "edit your registry at your own risk"):

**Single User**
```
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Classes\*\shell\pintohome]
"MUIVerb"="Edit with Notepad++"

[HKEY_CURRENT_USER\SOFTWARE\Classes\*\shell\pintohome\command]
@="\"C:\\Program Files\\Notepad++\\notepad++.exe\" \"%1\""
```
(If your installation is not in `c:\Program Files\Notepad++`, you will have to adjust that script.)

**All Users** (requires admin privileges)
```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\pintohome]
"MUIVerb"="Edit with Notepad++"

[HKEY_CLASSES_ROOT\*\shell\pintohome\command]
@="\"C:\\Program Files\\Notepad++\\notepad++.exe\" \"%1\""
```
(If your installation is not in `c:\Program Files\Notepad++`, you will have to adjust that script.)

In v8.5, the Notepad++ installer would automatically add this `pintohome` workaround on Windows 11, as long as no other app is currently using the `pintohome` command; if there is already something else in that registry slot, Notepad++ will not overwrite it.  However, since this got rid of the Windows native "pin to home" feature for some Windows 11 users, v8.5.1 undid that change; instead, the installer was updated to add to the main Windows 11 right click, rather than being being relegated to the **Show More Options** sub-menu.


### Registry Edit Warning

_**† Warning**: editing your registry can be dangerous; edit your registry at your own risk; the developers of Notepad++ and contributors to this documentation cannot and will not be held responsible for mistakes made during registry changes or unintendended consequences of such edits_
