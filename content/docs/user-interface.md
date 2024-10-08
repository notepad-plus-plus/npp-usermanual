---
title: User Interface
weight: 175
---

## Tabs

The keyboard shortcuts described in this section are the default [**Settings > Shortcut Mapper**](../preferences/#shortcut-mapper) settings; if the Shortcut Mapper has been modified, the keystrokes may be different.

The ```MOUSEWHEEL``` commands described require that the mouse pointer be hovered over the Tab Bar.

If the description says it will "wrap", it means that if you try to go beyond the last tab, it will next go to the first tab; and if you try to go before the first tab, it will next go to the last tab.  If the descriptions says it does "not wrap", then trying to go beyond the last tab or before the first tab will just stay at the last or first tab without wrapping.

- The tab bar settings can be found at [**Settings > Preferences > General > Tab Bar**](../preferences/#general), including the options to **Hide** the tab bar or to **Lock** the tab bar (so that tabs will not be movable from the Tab Bar, though they can still be reordered using keyboard shortcuts or menus).

- To switch between first and last tab, use <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + ```MOUSEWHEEL``` on tabs. ```MOUSEWHEEL``` up will take to first tab while down will take to last tab.
  ![tabNavFirstLast](../images/tabNavFirstLast.gif)

- To switch and activate next/previous tab, there are multiple options:
  1. Use <kbd>Ctrl</kbd> + ```MOUSEWHEEL``` on tabs. ```MOUSEWHEEL``` up will take to previous tab while down will take next tab. This method will wrap around.
  2. Use <kbd>Ctrl</kbd> + <kbd>Page Up</kbd> for next tab and <kbd>Ctrl</kbd> + <kbd>Page Down</kbd> for previous tab. This method will wrap as well.
  3. Use <kbd>Ctrl</kbd> + <kbd>Tab</kbd> for next tab and <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Tab</kbd> for previous tab. Using use <kbd>Ctrl</kbd> + <kbd>Tab</kbd> or <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Tab</kbd> while MRU is enabled provides great user experience. To enable MRU you can follow `Settings->Preferences->MISC.->Document Switcher`, then checkmark both `Enable` and `Enable MRU Behavior`.
  ![tabNavNextPrev](../images/tabNavNextPrev.gif)

- To move tab from one position to other position:
  1. Use <kbd>Shift</kbd> + ```MOUSEWHEEL``` on tabs. ```MOUSEWHEEL``` up will move currently selected tab to previous position while down will move to next position. This will wrap.  
      - If the Tab Bar is locked (using [**Tab Bar > Lock** preferences](../preferences/#general)), then <kbd>Shift</kbd> + ```MOUSEWHEEL``` will just activate the next or previous tab (without wrapping).
  2. Use <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Page Up</kbd> for previous position and <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Page Down</kbd> for next position. This will not wrap.
      - This will move the tab order even if the Tab Bar is locked.
  ![tabNavMoveRtLft](../images/tabNavMoveRtLft.gif)

- If there are more tabs than are visible on the Tab Bar, you can scroll the Tab Bar, to be able to see more
  1. Use ```MOUSEWHELL``` to scroll: "up" will scroll so you can see earlier Tabs in the list, "down" will scroll so you can see later Tabs in the list.
  2. There will also be ⏴⏵ arrow buttons: ⏴ will scroll so you can see earlier Tabs in the list, ⏵ will scroll so you can see later Tabs in the list.  (For a normal horizontal Tab Bar, the arrow buttons will be on the right of the Tab Bar; for a vertical Tab Bar, they will be at the bottom of the Tab Bar.)

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
- `Close Multiple Tabs >`:
  - `Close All But This`: Closes all files except this file.
  - `Close All to the Left`: Closes all files that are to the right of this file on the tab bar.
  - `Close All to the Right`: Closes all files that are to the left of this file on the tab bar.
  - `Close All Unchanged`: Closes all files that do not have unsaved changes (leaves only files that have unsaved changes).
- `Save`: Saves the file (disabled/grayed out if there are no unsaved changes).
- `Save As`: Allows you to save the current file under a new name.
- `Open Into >`:
  - `Open Containing Folder in Explorer`: Opens this file's folder in the Windows Explorer.
  - `Open Containing Folder in cmd`: Opens this file's folder in the `cmd` command prompt.
  - `Open Containing Folder as Workspace`: Opens this file's folder as a [Folder as Workspace](../session/#folder-as-workspace).
  - `Open in Default Viewer`: Opens this file in the default Windows, using the same rules as the [**File > Open in Default Viewer** menu action](../files/#file-menu).
- `Rename`: Renames this file.
- `Move to Recycle Bin`: Deletes the current file (placing it safely in Window's Recycle Bin).
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
  - Starting in v8.7, these colors can be user-defined using the [**Style Configurator > Global Styles > Tab color _n_** and **Tab color dark mode _n_**](../preferences/#global-styles) background color settings.

## Menu Bar

The menu bar of Notepad++ has a variety of menus, including **File** (for generic file operations like open and close), [**Edit**](../editing#edit-menu), [**Search**](../searching/), and [**View**](../views/), **Encoding** (which affects how the bytes of the file are interpreted as text -- whether ANSI or UTF-8 or similar), **Language** (for [syntax highlighting](../programming-languages/)), [**Settings**](../preferences/), **Tools** (with a couple of built-in utilities), [**Macro**](../macros/), [**Run**](../config-files/#userdefinedcommands) (for running external commands), [**Plugins**](../plugins/), and the **Window** menu (for accessing open files already open in Notepad++).

It also contains the **?** menu, which is a **Help**-style menu, including actions that list the [command line arguments](../command-prompt/); actions that take you to the Notepad++ [home page](https://notepad-plus-plus.org/), the [project page](https://github.com/notepad-plus-plus/notepad-plus-plus), this [user manual](/), and the [Community Forum](https://community.notepad-plus-plus.org); actions for the updater and proxy; the **Debug Info** (which is critical information when asking for help at the Community Forum or when creating a feature request or bug report at the [project page](https://github.com/notepad-plus-plus/notepad-plus-plus/issues)) and **About**.

At the far right of the menu bar there are also icons `+` (to create a New file), `▼` (to choose from the open files), and `X` (which closes the active tab).  (Before v8.4.3, only the `X` existed in that area of the menu bar.  Starting in v8.4.5, these can be made hidden using [Settings > Preferences > General > Menu](../preferences/#general).)

## Toolbar

There is a toolbar which has icons for various common tasks, which each run a specific menu action.  If you hover your mouse over that icon, it will show its name.  The toolbar actions include:

- **New** ⇒ [**File > New**](../files/#file-menu): Creates a new file.
- **Open** ⇒ [**File > Open**](../files/#file-menu): Opens an existing file.
- **Save** ⇒ [**File > Save**](../files/#file-menu): Saves the active file.
- **Save All** ⇒ [**File > Save All**](../files/#file-menu): Saves all active files.
- **Close** ⇒ [**File > Close**](../files/#file-menu): Closes the active file.
- **Close All** ⇒ [**File > Close ALl**](../files/#file-menu): Closes all open files.
- **Print** ⇒ [**File > Print**](../files/#printing): Launch the Print dialog.
- **Cut** ⇒ [**Edit > Cut**](../editing/#edit-menu): Cuts the selected text or line to the clipboard.
- **Copy** ⇒ [**Edit > Copy**](../editing/#edit-menu): Copies the selected text or line to the clipboard.
- **Paste** ⇒ [**Edit > Paste**](../editing/#edit-menu): Pastes the clipboard contents.
- **Undo** ⇒ [**Edit > Undo**](../editing/#edit-menu): Reverts the text to its content before the previous operation.
- **Redo** ⇒ [**Edit > Redo**](../editing/#edit-menu): Re-applies that action that was just reverted due to an Undo.
- **Find** ⇒ [**Search > Find**](../searching/#find-replace-tabs): Launches the **Find** dialog.
- **Replace** ⇒ [**Search > Replace**](../searching/#find-replace-tabs): Launches the **Replace** dialog.
- **Zoom In** ⇒ [**View > Zoom > Zoom In**](views/#zoom): Temporarily enlarge the visible rendering of the text (does not change anything in the file).
- **Zoom Out** ⇒[**View > Zoom > Zoom In**](views/#zoom): Temporarily shrink the visible rendering of the text (does not change anything in the file).
- **Synchronize Vertical Scrolling** ⇒ [**View > Synchronize Vertical Scrolling**](../views/#synchronized-scrolling): Toggle locking of the two views together, vertically.
- **Synchronize Horizontal Scrolling** ⇒ [**View > Synchronize Horizontal Scrolling**](../views/#synchronized-scrolling): Toggle locking of the two views together, horizontally.
- **Word Wrap** ⇒ [**View > Word Wrap**](../views/#wrapping): Toggle whether or not long lines will be wrapped in the display.
- **Show All Characters** ⇒ [**View > Show Symbol > Show All Characters**](../views/#show-symbol): Toggle showing all special characters.
    - Starting in v8.6.9, there is a drop-down menu available from this toolbar icon.  Clicking the button will still toggle from showing all to showing none.  But if you click the drop-down instead (or right click anywhere on the icon), you will see the full [**View > Show Symbol**](../views/#show-symbol) submenu, from which you can manually select which special characters to show and which not to.
- **Show Indent Guide** ⇒ [**View > Show Symbol > Show All Characters**](../views/#show-symbol): Toggle dotted vertical line `⸽` showing tabstops.
- **Define Your Language** ⇒ [**Language > User Defined Language > Define Your Language**](..//user-defined-language-system/): Toggles dialog to define a User Defined Language ("UDL").
- **Document Map** ⇒ [**View > Document Map**](/views/#panels): Toggles display of the Document Map panel.
- **Document List** ⇒ [**View > Document List**](/views/#panels): Toggles display of the Document List panel.
- **Function List** ⇒ [**View > Function List**](/views/#panels): Toggles display of the [Function List](../function-list/) panel.
- **Folder as Workspace** ⇒ [**View > Folder as Workspace**](/views/#panels): Toggles display of the [Folder as Workspace](/session/#folder-as-workspace) panel.
- **Monitoring (tail -f)** ⇒ [**View > Monitoring (tail -f)**](/views/#live-file-monitoring): Toggles the Live File Monitoring feature, which updates the file as its changed by another external process.
- **Start Recording** ⇒ [**Macro > Start Recording**](../macros/#record-a-macro): Starts recording actions in Notepad++ as a macro.
- **Stop Recording** ⇒ [**Macro > Stop Recording**](../macros/#record-a-macro): Stops recording actions in Notepad++ as a macro. 
- **Playback** ⇒ [**Macro > Playback**](../macros/#play-a-recorded-macro): Plays back a recorded macro. 
- **Run a Macro Multiple Times...** ⇒ [**Macro > Run a Macro Multiple Times...**](../macros/#play-a-recorded-macro-multiple-times): Plays back a recorded macro multiple times. 
- **Save Current Recorded Macro...** ⇒ [**Macro > Save Current Recorded Macro...**](../macros/#save-a-recorded-macro): Saves a recorded macro to a named slot in the **Macro** menu. 

Plugins can put additional buttons on the toolbar, to perform actions provided by those plugins.

The toolbar settings can be found at [**Settings > Preferences > General > Toolbar**](../preferences/#general), including the option to **Hide** the toolbar.  And you can customize the icons used for those buttons, as described in [Toolbar Icon Customization](config-files/#toolbar-icon-customization-toolbaricons-xml).

## Tools Menu

This menu contains commands related to running [cryptographic hash functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function) , including [MD5](https://en.wikipedia.org/wiki/MD5),
[SHA-1](https://en.wikipedia.org/wiki/SHA-1), and the SHA-256 and SHA-512 algorithms from [SHA-2](https://en.wikipedia.org/wiki/SHA-2).  (SHA-1 and SHA-512 were added in v8.5.5.)  These are useful for comparing the hashes for downloaded files to officially-published hashes, and for generating those hashes for files that you are publishing.

For each function, there are 3 commands:

- **Generate** - You can enter text in the upper field, and it will give you the hash output in the other field.  You can copy those results to the Clipboard through the button.  You can optionally checkmark **☑ Treat each line as a separate string** to get N different hashes for N different strings at the same time, rather than a single hash that covers the entire input text.
- **Generate from Files** - Will calculate the hashes for one or more selected files.
- **Generate from Selection into Clipboard** - Will use the text that is currently selected, calculate the hash, and put the hash results in the Clipboard.

## Document Switcher

The Document Switcher feature (which can be enabled or disabled using the **[Settings > Preferences > MISC](../preferences/#misc) > Document Switcher** settings) can be used to quickly switch between all the open files.

When you hold the <kbd>Ctrl</kbd> key and then press and release the <kbd>Tab</kbd> key, the Document Switcher appears as a popup with a yellow background, showing the current list of tabs (or a partial list, if there are too many tabs); the popup will remain until you release the <kbd>Ctrl</kbd> key.  One tab in the list will be shown in bold, indicating which tab will be made activate when all keys have been released.  With the Document Switcher on screen, repeated press and release of the <kbd>Tab</kbd> key will move the bold indicator downward on the screen, to the next tab name in the list.  When the desired tab is bold, release all keys to activate that tab.

The first tab to be shown in bold when you start the Document Switcher depends on the **[Settings > Preferences > MISC](../preferences/#misc) > Document Switcher > Enable MRU behavior** checkbox: When not checkmarked, the first tab name in bold will be the tab to the right of the currently-active tab (or the first tab in the tab bar, if the currently-active tab is the last in the tab bar; or the first tab in the other View, if the currently-active tab is the last in the active View); in this mode, the order of the tabs in the Document Switcher is the same as the order of the tabs in the tab bar, with the files from the active View above those from the alternate View when both Views are active.  When that setting is checkmarked, the first tab name in bold will be the tab that was active just before the current tab was activated (the "most recently used" tab); in this mode, the order of the tabs in the Document Switcher is the "most recently used" order, with the most recent at the top of the list, and the least recent at the bottom, with the tabs from both Views mixed together in usage order regardless of which View they are from.

When cycling through the tabs in the Document Switcher, if the bottom entry in the list is reached and you again press and release <kbd>Tab</kbd>, the bold indicator will move to the top of the list; or, if the list was too long to entirely be displayed, the <kbd>Tab</kbd> will scroll the Document Switcher, so the bold indicator will move to next entry down, and the entry that was previous at the top of the list will scroll out of the visible popup.

If you hold down <kbd>Shift</kbd> (while still holding the <kbd>Ctrl</kbd> key to keep you in Document Switcher mode), and then press and release the <kbd>Tab</kbd>, it will cause the bold indicator to move to the previous entry in the tab list, rather than the next.

The Document Switcher functionality can also be achieved using just the mouse (if you have a scroll wheel): Right-click in the editing area for a tab and hold the right mouse button, then begin scrolling the mouse wheel (in either direction) to display the Document Switcher popup; further scrolling of the scroll wheel will change which tab is shown in bold in the list. Releasing the right mouse button will cause the tab that is currently bold to be activated. An alternate way to activate a tab using the mouse, while the right mouse button is still held and the Document Switcher is displayed, is to left-click on one of the tab names from the list, which will immediately make that entry bold, activate the tab, and close the popup (even though you haven't let go of the right mouse button yet).

Some users have wondered about a "yellow flash" they have seen when using Notepad++: If you <kbd>Ctrl+Tab</kbd> and then promptly release _both_ keys, it will immediately switch to the tab that is first made bold and will leave Document Switcher mode (since you released the <kbd>Ctrl</kbd> key).  Depending on how promptly you release, this may just briefly flash the yellow-background popup, not giving you a chance to read the popup's list of tabs.
