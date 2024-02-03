---
title: User Interface
weight: 175
---

## Tabs

- The tab bar settings can be found at [**Settings > Preferences > General > Tab Bar**](../preferences/#general), including the option to **Hide** the tab bar.

- To switch between first and last tab, use <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + ```MOUSEWHEEL``` on tabs. ```MOUSEWHEEL``` up will take to first tab while down will take to last tab.
  ![tabNavFirstLast](../images/tabNavFirstLast.gif)

- To switch and activate next/previous tab, there are multiple options:
  1. Use <kbd>Ctrl</kbd> + ```MOUSEWHEEL``` on tabs. ```MOUSEWHEEL``` up will take to previous tab while down will take next tab.
  2. Use <kbd>Ctrl</kbd> + <kbd>Page Up</kbd> for next tab and <kbd>Ctrl</kbd> + <kbd>Page Down</kbd> for previous tab.
  3. Use <kbd>Ctrl</kbd> + <kbd>Tab</kbd> for next tab and <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Tab</kbd> for previous tab. Using use <kbd>Ctrl</kbd> + <kbd>Tab</kbd> or <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Tab</kbd> while MRU is enabled provides great user experience. To enable MRU you can follow `Settings->Preferences->MISC.->Document Switcher`, then checkmark both `Enable` and `Enable MRU Behavior`.
  ![tabNavNextPrev](../images/tabNavNextPrev.gif)

- To move tab from one position to other position:
  1. Use <kbd>Shift</kbd> + ```MOUSEWHEEL``` on tabs. ```MOUSEWHEEL``` up will move currently selected tab to previous position while down will move to next position.
  2. Use <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Page Up</kbd> for previous position and <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Page Down</kbd> for next position.
  ![tabNavMoveRtLft](../images/tabNavMoveRtLft.gif)

- To move a tab from one View to the other, you can use the techniques described in the [Editing > Dual View](../editing/#dual-view) section or [Views > Move / Clone](../views/#move-clone) section, including:
  1. Use the menus: **View > Move/Clone Current Document > Move to Other View**.
  2. Right Click on the tab's title and select **Move to Other View**.
  3. Drag the tab's title into the editing pane for that same tab and select **Move to Other View**.
  4. If the other View is already visible, drag the tab's title into the editing pane of the other View, and it will move.
  ![move2view](../images/move2view.gif)

- To clone a tab from one View into the other, you can use the techniques described in the [Editing > Clone Document](../editing/#dual-view) or [Views > Move / Clone](../views/#move-clone) section section, including:
  1. Use the menus: **View > Move/Clone Current Document > Clone to Other View**.
  2. Right Click on the tab's title and select **Clone to Other View**.
  3. Drag the tab's title into the editing pane for that same tab and select **Clone to Other View**.
  ![clonedDoc](../images/clonedDoc.gif)

- To create a new file tab using the tab bar:
  1. If there is empty area to the right of the last tab in the tab bar, double click there and a new tab will be created.
  ![tabNavNewDoubleClick](../images/tabNavNewDoubleClick.gif)

- To close a tab using the tab bar:
  1. If **Settings > Preferences > General > Tab Bar > Show close button on each tab** is checked, you can click the red ☒ on that tab to close that tab.
  2. If **Settings > Preferences > General > Tab Bar > Double click to close document** is checked, you can double-click the tab's title to close that tab.
  ![tabNavCloseXDblClick](../images/tabNavCloseXDblClick.gif)

### Tab Bar Right Click Menu

When you right click on the title for a tab, you get a context menu for manipulating that tab.

- `Close`: Closes this file's tab.
- `Close Mutiple Tabs >`:
  - `Close All But This`: Closes all files except this file.
  - `Close All to the Left`: Closes all files that are to the right of this file on the tab bar.
  - `Close All to the Right`: Closes all files that are to the left of this file on the tab bar.
  - `Close All Unchanged`: Closes all files that do not have unsaved changes (leaves only files that have unsaved changes).
- `Save`: Saves the file (disabled/greyed out if there are no unsaved changes).
- `Save As`: Allows you to save the current file under a new name.
- `Open Into >`:
  - `Open Containing Folder in Explorer`: Opens this file's folder in the Windows Explorer.
  - `Open Containing Folder in cmd`: Opens this file's folder in the `cmd` command prompt.
  - `Open Containing Folder as Workspace`: Opens this file's folder as a [Folder as Workspace](../session/#folder-as-workspace).
  - `Open in Default Viewer`: Opens this file in the default Windows, using the same rules as the [**File > Open in Default Viewer** menu action](../files/#file-menu).
- `Rename`: Renames this file.
- `Move to Recyle Bin`: Deletes the current file (placing it safely in Window's Recycle Bin).
- `Reload`: Reloads this file from disk.
- `Print`: Prints this file.
- `Read-Only`: Sets this file's Notepad++\-specific read-only flag (see more in the [**Edit** menu description](../editing/#edit-menu)).
- `Clear Read-Only Flag`: Clears this file's read-only flag for the Windows OS (see more in the [**Edit** menu description](../editing/#edit-menu)).
- `Copy to Clipboard >`
  - `Copy Full File Path`: Copies the full file path (drive, directory, and filename) to the Windows Clipboard.
  - `Copy Filename`: Copies just the filename (no drive or directory) to the Windows Clipboard.
  - `Copy Current Dir. Path`: Copies the file's directory (drive and directory, but not the  filename) to the Windows Clipboard.
- `Move Document >`
  - `Move to Start`: Moves the tab to be the first in the list of active tabs for the current view. (New to v8.6.1.)
  - `Move to End`: Moves the tab to be the last in the list of active tabs for the current view. (New to v8.6.1.)
  - `Move to Other View`: Moves the tab from one view to the other.
  - `Clone to Other View`: Makes a tab for the same file in the other view.
  - `Move to New Instance`: Moves the tab from this Notepad++ instance to a newly-created instance (only works on named files that have no unsaved changes).
  - `Open in New Instance`: Makes a tab in a new Notepad++ instance which contains the same file as this tab (only works on named files that have no unsaved changes).
- `Apply Color to Tab >` (new to v8.4.6)
  - `Apply Color #`: Applies the indicated color to the highlight portion of the tab bar.  (Applying a different color will _change_ the color, not combine the colors together.  Each tab can only have one color.)
  - `Remove Color`: Removes the color of the tab, returning to the default color scheme.

## Menu Bar

The menu bar of Notepad++ has a variety of menus, including **File** (for generic file operations like open and close), [**Edit**](../editing#edit-menu), [**Search**](../searching/), and [**View**](../views/), **Encoding** (which affects how the bytes of the file are interpreted as text -- whether ANSI or UTF-8 or similar), **Language** (for [syntax highlighting](../programming-languages/)), [**Settings**](../preferences/), **Tools** (with a couple of built-in utilities), [**Macro**](../macros/), [**Run**](../config-files/#userdefinedcommands) (for running external commands), [**Plugins**](../plugins/), and the **Window** menu (for accessing open files already open in Notepad++).

It also contains the **?** menu, which is a **Help**-style menu, including actions that list the [command line arguments](../command-prompt/); actions that take you to the Notepad++ [home page](https://notepad-plus-plus.org/), the [project page](https://github.com/notepad-plus-plus/notepad-plus-plus), this [user manual](/), and the [Community Forum](https://community.notepad-plus-plus.org); actions for the updater and proxy; the **Debug Info** (which is critical information when asking for help at the Community Forum or when creating a feature request or bug report at the [project page](https://github.com/notepad-plus-plus/notepad-plus-plus/issues)) and **About**.

At the far right of the menu bar there are also icons `+` (to create a New file), `▼` (to choose from the open files), and `X` (which closes the active tab).  (Before v8.4.3, only the `X` existed in that area of the menu bar.  Starting in v8.4.5, these can be made hidden using [Settings > Preferences > General > Menu](../preferences/#general).)

## Toolbar

There is a toolbar which has icons for various common tasks.  The toolbar settings can be found at [**Settings > Preferences > General > Toolbar**](../preferences/#general), including the option to **Hide** the toolbar.  If you do not understand the icon, hovering over that icon will show the underlying action.

## Tools Menu

This menu contains commands related to running [cryptographic hash functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function) , including [MD5](https://en.wikipedia.org/wiki/MD5),
[SHA-1](https://en.wikipedia.org/wiki/SHA-1), and the SHA-256 and SHA-512 algorithms from [SHA-2](https://en.wikipedia.org/wiki/SHA-2).  (SHA-1 and SHA-512 were added in v8.5.5.)  These are useful for comparing the hashes for downloaded files to offically-published hashes, and for generating those hashes for files that you are publishing.

For each function, there are 3 commands:

- **Generate** - You can enter text in the upper field, and it will give you the hash output in the other field.  You can copy those results to the Clipboard through the button.  You can optionally checkmark **☑ Treat each line as a separate string** to get N different hashes for N different strings at the same time, rather than a single hash that covers the entire input text.
- **Generate from Files** - Will calculate the hashes for one or more selected files.
- **Generate from Selection into Clipboard** - Will use the text that is currently selected, calculate the hash, and put the hash results in the Clipboard.

## Document Switcher

The Document Switcher feature (which can be enabled or disabled using the **[Settings > Preferences > MISC](../preferences/#misc) > Document Switcher** settings) can be used to quickly switch between all the open files in the active View.

When you hold the <kbd>Ctrl</kbd> key and then press and release the <kbd>Tab</kbd> key, the Document Switcher appears as a popup with a yellow background, showing the current list of tabs for the active View (or a partial list, if there are too many tabs); the popup will remain until you release the <kbd>Ctrl</kbd> key.  One tab in the list will be selected (displayed in bold), indicating which tab will be made activate when all keys have been released.  With the Document Switcher on screen, repeated press and release of the <kbd>Tab</kbd> key will move the selection (bold highlight) downward on the screen, to the next tab name in the list.  When the desired tab is selected (bold), release all keys to activate that selected tab.

The first tab to be selected when you start the Document Switcher depends on the **[Settings > Preferences > MISC](../preferences/#misc) > Document Switcher > Enable MRU behavior** checkbox: When not checkmarked, the first-selected tab will be the tab to the right of the currently-active tab (or the first tab in the View, if the currently-active tab is the last in the View).  When that setting is checkmarked, the first-selected tab will be the tab that was active just before the current tab was activated (the "most recently used" tab).

The order of the list of tabs matches the left-to-right order of the tab bar for the active View, when not in MRU mode.  When in MRU mode, it matches the "most recently used" order, with the most recent at the top of the list, and the least recent at the bottom.

When cycling through the tabs in the Document Switcher, if the bottom entry in the list is reached and you again press and release <kbd>Tab</kbd>, the selection will move to the top of the list (that is, the bold highlight will move to the top of the list); or, if the list was too long to entirely be displayed, the <kbd>Tab</kbd> will scroll the Document Switcher, so the next entry down will be made visible and will be selected (displayed as bold), and the entry that was previous at the top of the list will scroll out of the visible popup.

If you hold down <kbd>Shift</kbd> (while still holding the <kbd>Ctrl</kbd> key to keep you in Document Switcher mode), and then press and release the <kbd>Tab</kbd>, it will cause the selection (bold highlight) to move to the previous entry in the tab list, rather than the next.  (And in the long list scenario, it would scroll to the next tab above the top in the list, making that visible and scrolling the bottom tab in the list out of the visible popup.)

The Document Switcher functionality can also be achieved using the just mouse (if you have a scroll wheel): Right-click in the editing area for a tab and hold the mouse button, then begin scrolling the mouse wheel (in either direction) to display the Document Switcher popup, and continued scrolling of the scroll wheel will change the selected tab in the list.  Releasing the right mouse button will cause the currently-selected tab to be activated in the current View.

If you <kbd>Ctrl+Tab</kbd> and then promptly release _both_ keys, it will immediately switch to the first-selected tab and will leave Document Switcher mode (since you released the <kbd>Ctrl</kbd> key).  Depending on how promptly you release, this may just briefly flash the yellow-background popup, not giving you a chance to read the popup's list of tabs.
