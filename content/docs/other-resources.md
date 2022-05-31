---
title: Other Resources
weight: 160
---


## Notepad Replacement
Notepad is a default text editor shipped with Windows. You may want to use Notepad++ instead of Notepad. However, there's no obvious way to do it.
From the version 7.5.9 onward, you can run the following command to make Notepad++ replace Notepad (run in `cmd.exe` with Administrator privileges)[†](#registry-edit-warning):

```batch
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v "Debugger" /t REG_SZ /d "\"%ProgramFiles(x86)%\Notepad++\notepad++.exe\" -notepadStyleCmdline -z" /f
```

Note that you may need to use `%ProgramFiles%\Notepad++\` to substitute for `%ProgramFiles(x86)%\Notepad++\` if you have Notepad++ 64-bit installed, or use other path if your Notepad++ is installed in a non-default location.

Use the the following comment to undo the replacement:
```batch
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v "Debugger" /f
```

This has historically worked from Windows 7 through Windows 10.  However, Microsoft has changed things in Windows 11 , and this may not work for you.

### Registry Edit Warning

_**† Warning**: editing your registry can be dangerous; edit your registry at your own risk; the developers of Notepad++ and contributors to this documentation cannot and will not be held responsible for mistakes made during registry changes or unintendended consequences of such edits_

## Explorer Right-Click menu

When you install Notepad++ normally, Notepad++ will add an **Edit with Notepad++** Explorer Right Click action for all file types. (This is separate from any file types that you use the [Settings > Preferences > File Association](../preferences/#file-association) or other Windows-standard means to "associate" that file type with Notepad++.) 

### Missing "Edit with Notepad++" Action

If you are missing this feature, you can add it to your registry using your favorite method.  One such method is to save the following as a `.reg` file and run it[†](#registry-edit-warning):

**Single User**
```
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Classes\*\shell\Notepad++]
@="Edit With Notepad++"

[HKEY_CURRENT_USER\SOFTWARE\Classes\*\shell\Notepad++\command]
@="\"C:\\Program Files\\Notepad++\\notepad++.exe\" \"%1\""
```
(If your installation is not in `c:\Program Files\Notepad++`, you will have to adjust that script.)

**All Users** (requires admin privileges)
```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\Notepad++]
@="Edit With Notepad++"

[HKEY_CLASSES_ROOT\*\shell\Notepad++\command]
@="\"C:\\Program Files\\Notepad++\\notepad++.exe\" \"%1\""
```
(If your installation is not in `c:\Program Files\Notepad++`, you will have to adjust that script.)

### Windows 11 Right-Click Workarounds

Windows 11 hides the old right click menu, so even with a normal installation or if you've manually added those associations, the **Edit with Notepad++** might not be visible for you in Windows 11.  The right click menu contains a **Show More Options** action which will bring up the old-style right click context menu with the old actions; this can also be accessed using the default <kbd>Shift+F10</kbd> shortcut on a file instead of right-clicking.

If that is not sufficient for you, https://www.tomshardware.com/how-to/windows-11-classic-context-menus describes a possible method of changing your registry[†](#registry-edit-warning) to get the old right click context menu by default again in Windows 11.  

If you would rather have it in your modern Windows 11 right click, the following `.reg` files might bring **Edit with Notepad++** to your Windows 11 right click[†](#registry-edit-warning):

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


## Notepad++ Cheat sheet

### Tabs
- To switch between first and last tab, use <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + ```MOUSEWHEEL``` on tabs. ```MOUSEWHEEL``` up will take to first tab while down will take to last tab.
  ![tabNavFirstLast](../images/tabNavFirstLast.gif)

- To switch and activate next/previous tab, there are multiple options:
  1. Use <kbd>Ctrl</kbd> + ```MOUSEWHEEL``` on tabs. ```MOUSEWHEEL``` up will take to previous tab while down will take next tab.
  2. Use <kbd>Ctrl</kbd> + <kbd>Page Up</kbd> for next tab and <kbd>Ctrl</kbd> + <kbd>Page Down</kbd> for previous tab.
  3. Use <kbd>Ctrl</kbd> + <kbd>Tab</kbd> for next tab and <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Tab</kbd> for previous tab. Using use <kbd>Ctrl</kbd> + <kbd>Tab</kbd> or <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Tab</kbd> while MRU is enabled provides great user experience. To enable MRU you can follow `Settings->Preferences->MISC.->Document Switcher`, then tick both `Enable` and `Enable MRU Behavior`.
  ![tabNavNextPrev](../images/tabNavNextPrev.gif)
  
- To move tab from one position to other position:
  1. Use <kbd>Shift</kbd> + ```MOUSEWHEEL``` on tabs. ```MOUSEWHEEL``` up will move currently selected tab to previous position while down will move to next position.
  2. Use <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Page Up</kbd> for previous position and <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Page Down</kbd> for next position.
  ![tabNavMoveRtLft](../images/tabNavMoveRtLft.gif)

- To move a tab from one View to the other, you can use the techniques described in the [Editing > Dual View](../editing/#dual-view) section, including:
  1. Use the menus: **View > Move/Clone Current Document > Move to Other View**
  2. Right Click on the tab's title and select **Move to Other View**
  3. Drag the tab's title into the editing pane for that same tab and select **Move to Other View**
  4. If the other View is already visible, drag the tab's title into the editing pane of the other View, and it will move
  ![move2view](../images/move2view.gif)
	
- To clone a tab from one View into the other, you can use the techniques described in the [Editing > Clone Document](../editing/#dual-view) section, including:
  1. Use the menus: **View > Move/Clone Current Document > Clone to Other View**
  2. Right Click on the tab's title and select **Clone to Other View**
  3. Drag the tab's title into the editing pane for that same tab and select **Clone to Other View**
  ![clonedDoc](../images/clonedDoc.gif)
	
- To create a new file tab using the tab bar:
  1. If there is empty area to the right of the last tab in the tab bar, double click there and a new tab will be created
  ![tabNavNewDoubleClick](../images/tabNavNewDoubleClick.gif)

- To close a tab using the tab bar:
  1. If **Settings > Preferences > General > Tab Bar > Show close button on each tab** is checked, you can click the red ☒ on that tab to close that tab
  2. If **Settings > Preferences > General > Tab Bar > Double click to close document** is checked, you can double-click the tab's title to close that tab
  ![tabNavCloseXDblClick](../images/tabNavCloseXDblClick.gif)
