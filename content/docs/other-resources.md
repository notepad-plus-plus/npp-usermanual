---
title: Other Resources
weight: 160
---


## Notepad Replacement
Notepad is a default text editor shipped with Windows. You may want to use Notepad++ instead of Notepad. However, there's no obvious way to do it.
From the version 7.5.9 onward, you can run the following command to make Notepad++ replace Notepad (run in `cmd.exe` with Administrator privileges):

```batch
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v "Debugger" /t REG_SZ /d "\"%ProgramFiles(x86)%\Notepad++\notepad++.exe\" -notepadStyleCmdline -z" /f
```

Note that you may need to use `%ProgramFiles%\Notepad++\` to substitute for `%ProgramFiles(x86)%\Notepad++\` if you have Notepad++ 64-bit installed, or use other path if your Notepad++ is installed in a non-default location.


Use the the following comment to undo the replacement:
```batch
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v "Debugger" /f
```

## Notepad++ Cheat sheet
### Tabs
- Tab navigation
  - To switch between first and last tab, use <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + ```MOUSEWHEEL``` on tabs. ```MOUSEWHEEL``` up will take to first tab while down will take to last tab.
  ![FirstAndLast](https://user-images.githubusercontent.com/14791461/35479755-b37a09fc-0424-11e8-9a5c-905bf18b957e.gif)
  
  
  - To switch and activate next/previous tab, there are multiple options:
	1. Use <kbd>Ctrl</kbd> + ```MOUSEWHEEL``` on tabs. ```MOUSEWHEEL``` up will take to previous tab while down will take next tab.
	2. Use <kbd>Ctrl</kbd> + <kbd>Page Up</kbd> for next tab and <kbd>Ctrl</kbd> + <kbd>Page Down</kbd> for previous tab.
	3. Use <kbd>Ctrl</kbd> + <kbd>Tab</kbd> for next tab and <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Tab</kbd> for previous tab. Using use <kbd>Ctrl</kbd> + <kbd>Tab</kbd> or <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Tab</kbd> while MRU is enabled provides great user experience. To enable MRU you can follow `Settings->Preferences->MISC.->Document Switcher`, then tick both `Enable` and `Enable MRU Behavior`.

	![ChangeOneByOne](https://user-images.githubusercontent.com/14791461/66017375-31cc3680-e4f8-11e9-8e05-b93b7adc7981.gif)
  
  
  - To move tab from one position to other position:
	1. Use <kbd>Shift</kbd> + ```MOUSEWHEEL``` on tabs. ```MOUSEWHEEL``` up will move currently selected tab to previous position while down will move to next position.
	2. Use <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Page Up</kbd> for previous position and <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Page Down</kbd> for next position.

	![MoveTabs](https://user-images.githubusercontent.com/14791461/66017596-1b72aa80-e4f9-11e9-9ff0-87632415bd91.gif)

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
