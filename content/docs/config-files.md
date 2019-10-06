---
title: Configuration File Syntax
linktitle: config-files
weight: 115
---

# Configuration File Syntax

Notepad++ offers a comprehensive user interface to review or change most of its settings. However, there are some special cases, among which:

* Using synthesized macros to send commands with parameters to a Scintilla component
* Adding keywords to a language, because the new language version isn't matched yet
* Some settings have been left out of the user interface
* You'd like to edit a session file so as to quick add/remove a file
* You wish to customise the Context Menu

## Editing Configuration Files

**ALWAYS BACKUP THE FILE TO BE EDITED**. If you make a mistake, Notepad++ may erase the whole contents and replace it with useless defaults. This is probably the worst that can happen, but it does happen.

If changes are made in the Notepad++ UI to settings which are stored in configuration files, those will be written to disk when you exit Notepad++ _after_ any file saves you do.  Thus, if you are going to edit a Notepad++ configuration file _with_ Notepad++ (and why would you want to edit it with anything else?), you will need to be careful.  The safest sequence when editing a configuration file:

1. Close _all_ active instances of Notepad++
2. Open _one_ instance of Notepad++
3. Edit the configuration file
4. Save
5. Exit Notepad++
6. Reload Notepad++
7. The changes will now be in effect.


## General format considerations

Configuration files are xml files. An xml file is made of nodes, which may contain nodes recursively, which may contain tags. Both nodes and tags may have attributes. **Their order and capitalisation must be kept strictly**. The ordering of tags usually doesn't matter, except when it orders menu items, in which case the ordering is part of the configuration. It also happens that some ordering must be identical across different files.

Nodes and tags come in two forms: a short `<Node/>` form and a long `<Node>`...`</Node>` form. The former is to be used if and only if the node is empty or the tag has no content - there may be attributes though.

All configuration files xml structure is contained in a single `<NotepadPlus>` node. There must be exactly one such node per file, and it should be topmost.

All integer attribute values are written between double quotes, like in "15". Since xml only knows about strings, anything must be written as a string, which is delimited by double quotes.


### Valid keys

The use of the Windows key as a modifier is not supported by Scintilla.

The complete list of base virtual key code is to be found on [keys.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/keys.h). Because of this reliance on OS defined virtual keys, various letters obtained by combining diacritics with a main key (like the german ß or spanish ñ) cannot be used.

Left and right versions of modifiers are not distinguished. A special case is the AltGr key on various european keyboards, which translates to Ctrl+Alt rather than plain Alt.

Keys producing double byte character codes are not supported if they don't fit in the virtual key list.


## User interface settings: config.xml

Syntax highlighting will be covered in the specific section with this name.

Below the standard `<NotepadPlus>` node, the following sections are defined:

1. `<GUIConfigs>`: user interface settings
2. `<FindHistory>`: most of the latest state of the Find/Replace dialog box.
3. `<History>`: the list of recently used files.

### `<GUIConfigs>`

This area contains most of the items that can be adjusted from the Preferences dialog. It is thoroughly commented for the most part.

There could be two reasons to edit this section:

1. it may contain settings that are not yet configurable from a dialog. This would happen for intermediate or candidate releases.
2. it may be useful to run a script for custom installation of Notepad++ by a system administrator.


The tag contains a large number of `<GUIConfig>` tags. All of them have a "name" attribute. Any other contents or extra attributes they may have is controlled by the "name" attribute, as discussed in the individual sections below. Each section lists attributes and their possible values, then contents if applicable. Usually, thee is no need for extra explanation, as the name / attribute pair closely match the corresponding Preferences widget caption.

GUIConfig tags without contents may be auto-closing or not, this seems to be immaterial.


#### ToolBar

1. "visible": "yes"/"no" attribute
2. "show": any of "hide","standard", "large" and "small".

#### StatusBar

Contents are either of show or hide.


#### TabBar

A sequence of "yes"/"no" attributes:

1. dragAndDrop
2. drawTopBar
3. drawInactiveTab
4. reduce
5. closeButton
6. doubleClick2Close
7. vertical
8. multiline
9. hide

#### ScintillaViewSplitter

Contents are either of horizontal or vertical.


#### UserDefineDlg

1. "position" is either of docked or undocked

Contents are either of show or hide.

#### TabSetting

This is the default value for all languages not receiving special treatment through **Settings &gt; Preferences &gt; Language  &gt; Tab Settings**.

1. "tabSize": conversion factor
2. replaceBySpaces": "yes"/"no"

#### AppPosition

1. "x"
2. "y"
3. "width"
4. "height"
5. "isMaximized": "yes"/"no", other are numbers of pixels.

#### ScintillaPrimaryView

1. "lineNumberMargin": either of show or hide
2. "bookmarkMargin": either of show or hide
3. "folderMarkStyle": either of single, arrow, circle or box
4. "indentGuideLine": either of show or hide
5. "currentLineHilitingShow": either of show or hide
1. "Wrap": "yes" / "no"
1. "edge": "yes" / "no"
1. "edgNbColumn": number of columns&gt;
1. "wrapSymbolShow": either of show or hide
1. "zoom": a signed integer, the number of points to add for current magnification.
1. "whiteSpaceShow": either of show or hide
1. "eolShow": either of show or hide
1. "disableAdvancedScrolling": either of "yes" or "no" (default)
1. "borderWidth": width in pixels.


#### ScintillaSecundaryView

This setting is no longer in use, as version 5.7.1 has removed individual view options.


#### Auto-detection

Contents either yes or `<tt/>`n`</tt>`.


#### CheckHistoryFiles

Contents either yes or `<tt/>`n`</tt>`.


#### TrayIcon

Contents either yes or `<tt/>`n`</tt>`.


#### RememberLastSession

Contents either yes or `<tt/>`n`</tt>`.


#### NewDocDefaultSettings

1. "format": either of 0 (CR+LF for DOS/Windows), 1 (LF for Unix/Mac OSX) or 2 (CR for Mac OD 9 and earlier).
1. "encoding": either of 0 (ANSI), 1 (UTF-8 with BOM), 2 (UCS-2 BE with BOM), 3 (UCS2 LE with BOM), 4 (UTF-8 without BOM), 5 (7-bit ASCII), 6 (UCS-2 BE without BOM) or 7 (UCS-2 LE without BOM).
1. "lang": the 0-based lexer number for the default language. As a result, this cannot be an user defined language, use the extension instead. The number follows the list as displayed in the corresponding tab: 0 for normal text, 1 for PHP, 2 for C and so on.
1. "openAnsiAsUTF8": "yes" / "no"


#### langExcluded

The various gr`<n>` attributes are byte masks. Supported languages seem to be arranged by groups of 8, and the mask summarises which languages in each group are excluded.

1. "gr0":
1. "gr1":
1. "gr2":
1. "gr3":
1. "gr4":
1. "gr5":
1. "gr6":
1. "gr7":
1. "langMenuCompact": "yes" / "no"


#### Print

1. "lineNumber": "yes" / "no"
1. printOption": either of 0 (WYSIWYG), 1 (invert colour), 2 (B &amp; W) or 3 (WYSIWYG without a background)
1. "headerLeft": text for the designated area
1. "headerMiddle": text for the designated area
1. "headerRight": text for the designated area
1. "headerFontName": name of font
1. "headerFontStyle": as per style font flags
1. "headerFontSize": size of font
1. "footerLeft": text for the designated area
1. "footerMiddle": text for the designated area
1. "footerRight": text for the designated area
1. "footerFontName": name of font
1. "footerFontStyle": as per style font flags
1. "footerFontSize": size of font
1. "marginLeft": size in centimeters
1. "marginTop": size in centimeters
1. "marginRight": size in centimeters
1. "marginBottom": size in millimeters


#### Backup

1. "action": either of 0 (none), 1 (simple) or 2 (verbose).
1. "useCustumDir": "yes" / "no"
1. "dir": directory name
1. "isSnapshotMode": "yes" / "no". Defaults to yes.
1. "snapshotBackupTiming": number of milliseconds between snapshots (default is 7,000).


#### TaskList

Contents are "yes" / "no".


#### SaveOpenFileInSameDir

Contents are "yes" / "no".


#### noUpdate

1. "intervaDays": number of days to wait to update to next version
1. "nextUpateDate": yyyymmdd representation of date to fire auto-update

<p>Contents are "yes" / "no"


#### MaitainIndent

Contents are "yes" / "no". This flag controls whether any indent is to be copied from the current line when Enter is hit.


#### MRU

Contents are "yes" / "no".


#### URL

Contents are either of 0 (don't enable clickable links), 1 (enable with underline) or 2 (enable without underline).


#### globalOverride

1. "fg": "yes" / "no"
1. "bg": "yes" / "no"
1. "font": "yes" / "no"
1. "fontSize": "yes" / "no"
1. "bold"yes" / "no"
1. "italic"yes" / "no"
1. "underline"yes" / "no"


#### auto-completion

1. "autoCAction": either of 0 (disabled), 1 (enabled for functions),  2 (enabled for words) or 3 (both words and functions).
1. "triggerFromNbChar": number of characters after which the list will pop up
1. "funcParams": "yes" / "no" (enable call tips)


#### sessionExt

Contents are the extension, if any.


#### SmartHighLight

Contents are "yes" / "no".


#### SmartHighLightCaseSensitive

Contents are "yes" / "no".


#### TagsMatchHighLight

1. "TagAttrHighLight": "yes" / "no"
1. "HighLightNonHtmlZone": "yes" / "no"

<p>Contents are "yes" / "no".


#### MenuBar

Contents are either of show or hide.


#### Caret

1. "width": in pixels
1. "blinkRate": an integer, the number of milliseconds during which the caret is shown, then hidden. The two intervals are equal.


#### ScintillaGlobalSettings

1. "enableMultipleSelection": "yes" / "no"


#### openSaveDir

1. "value": 0 to disable, 1 to enable.
1. "defaultDirPath": fixed starting path for open/save dialogs


#### titleBar

1. "short": "yes" / "no"


#### styleTheme

1. "path": path to current theme file


#### delimiterSelection

1. "leftmostDelimiter": ASCII code of the character limiting the selection on the left (default is 40 for '(')
1. "rightmostDelimiter": ASCII code of the character limiting the selection on the right (drfault is 41 for ')')
1. "delimiterSelectionOnEntireDocument": "yes" to alow text on multiple contiuous lines to be selected, otherwise "no" (default).


#### MISC

1. "fileSwitcherWithoutExtColumn": "yas"/"no" (default).
1. "backslashEscapeCharacterFprSQL"&nbsp;: "yes" / "no" (default is yes).


#### DockingManager

The following values are the width of left/right side windows and the height of top/bottom window will take:

1. "leftWidth": size in pixels, 0 is allowed
1. "rightWidth": size in pixels, 0 is allowed
1. "topHeight": size in pixels, 0 is allowed
1. "bottomHeight": size in pixels, 0 is allowed

<p>Contents are a possibly empty sequence of `<FloatingWindow>` auto-closed tags, followed by a possibly empty sequence of `<PluginDlg>` tags, followed by at least 4 auto-closed `<ActiveTabs>` tags, one for each of the 4 predefined positions, plus one for each undocked window.

A `<FloatingWindow>` tag defines the position, width and height of a detached (floating) window&nbsp;:

1. "cont": a container identifier, matching the one for an `<ActiveTabs>` subsequent tag.
1. "x": position x in pixels
1. "y": position y in pixels
1. "width": in pixels
1. "height": in pixels

<p>A `<PluginDlg>` tag has no contents and the following attributes:

1. "pluginName": the name of the plugin. Seems to be "dummy" for the search results window, and "Notepad++::InternalFunction" for other dockable windows.
1. "id": command id of the command to run at startup for the plugin, -1 if none. The dock manager records this information whenever a plugin opens a dockable window. "id" is 44070 for the vertical file switcher, 44084 for Function List and 44081/2/3 for the project panels.
1. "curr": current docking position
1. "prev": previous docking position, -1 if none
1. "isVisible": "yes" / "no".

<p>An `<ActiveTabs>` tag has the following attributes:

1. "cont": either 0 (left), 1 (top), 2 (right), 3 (bottom) or anything above 4 (undocked, corresponds to a `<FloatingWindow>` tag).
1. "ActiveTab": the cont attribute actually refers to a tabbed container for possibly several windows. The value is -1 when container is empty. Otherwise, it is the active tab for the container.


### `<FindHistory>`

Here are the attributes of the node:


 Attributes for the `<FindHistory>` node


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> nbMaxFindHistoryPath </td>
<td> integer </td>
<td> Maximal number of search folders being remembered
</td></tr>
<tr>
<td> 2 </td>
<td> nbMaxFindHistoryFilter </td>
<td> integer </td>
<td> Maximum number of filter strings remembered
</td></tr>
<tr>
<td> 3 </td>
<td> nbMaxFindHistoryFind </td>
<td> integer</td>
<td>  Maximum number of search patterns being remembered
</td></tr>
<tr>
<td> 4 </td>
<td> nbMaxFindHistoryReplace </td>
<td> integer </td>
<td> Maximum number of replace patterns being remembered
</td></tr>
<tr>
<td> 5 </td>
<td> matchWord= "</td>
<td> "yes"/"no" </td>
<td> State of the Whole words checkbox ("yes" = checked)
</td></tr>
<tr>
<td> 6 </td>
<td> matchCase </td>
<td>"yes"/"no" </td>
<td> State of the Match case checkbox ("yes" = checked)
</td></tr>
<tr>
<td> 7 </td>
<td> wrap </td>
<td>"yes"/"no" </td>
<td> State of the Wrap around  checkbox ("yes" = checked)
</td></tr>
<tr>
<td> 8 </td>
<td> directionDown </td>
<td>"yes"/"no" </td>
<td> Search direction ("yes" = the Down radio button is checked)
</td></tr>
<tr>
<td> 9 </td>
<td> fifRecuisive </td>
<td>"yes"/"no" </td>
<td> State of the In all subfolders checkbox ("yes" = checked)
</td></tr>
<tr>
<td> 10 </td>
<td> fifInHiddenFolder </td>
<td>"yes"/"no" </td>
<td> State of the In hidden folders checkbox ("yes" = checked)
</td></tr>
<tr>
<td> 11 </td>
<td> dlgAlwaysVisible </td>
<td>"yes"/"no" </td>
<td> "yes" if the dialog cannot be obscured, else "no"
</td></tr>
<tr>
<td> 12 </td>
<td> fifFilterFollowsDoc </td>
<td> "yes"/"no" </td>
<td> "yes" if the search filter should change with the active document, else "no"
</td></tr>
<tr>
<td> 13 </td>
<td> fifFolderFollowsDoc </td>
<td> "yes"/"no" </td>
<td> "yes" if the search path should change with the active document, else "no"
</td></tr>
<tr>
<td> 14 </td>
<td> searchMode </td>
<td> integer </td>
<td> <p>

* 0 for Normal mode
* 1 for Extended mode
* 2 for Regular expression mode

<p>
</td></tr>
<tr>
<td> 15 </td>
<td> transparencyMode </td>
<td> integer </td>
<td> <p>

* 0 if the Transparency checkbox is clear
* 1 if it is checked, and the On lose focus radio button is checked
* 2 if it is checked, and the Always radio button is checked

<p>
</td></tr>
<tr>
<td> 16 </td>
<td> transparency </td>
<td> integer </td>
<td> In the 1..255 range. The smaller it is, the less visible the dialog box is when transparency applies.
</td></tr></tbody></table>
<p>Note that, as of 6.6.6, the attributes 11 to 13 are not individually configurable through user interface. The "Follow Doc" checkbox allows to set 12 and 13 to a common value however. Also note that the state of the Mark line, Style found token , Purge for each search and In selection checkboxes is not remembered in this file - they are not persistent.

Inside this node are tags that describe the contents of the 4 combo boxes in the dialog. They are all short tags with a name attribute. They appear in the following order:

1. `<Path>` tags
1. `<Filter>` tags
1. `<Find>` tags
1. `<Replace>` tags

<p>The lists are simply contiguous. The number of `<Path>` tags should not be greater than the nbMaxFindHistoryPath enclosing attribute, and similarly for the other tags.


### `<History>`

This node has a nbMaxFile integer attribute, the maximal number of files being remembered. The node is short, i.e. auto-closed, if there is no remembered file (new documents don't count). Otherwise, it has `<File>` tags with a filename attribute. Again, their number should not exceed the nbMaxFile enclosing attribute.


### `<ProjectPanels>`

Yhis tag contains `<ProjectPanel>` tags. `<ProjectPanel>` is autoclosing and has two mandatory attributes:

1. <i>id</i>: the number of the panel. Valid values are 1, 2 and 3. Each of the valid IDs must be mentioned only once.
1. <i>workspaceFile</i>: the absolute path to the worspace file holding the corresponding panel's contents, or "" if not in use.


### `<FileEditViewHistory>`

This is used to keep fold and bookmark states so as torestore them upon re-opening the file. Attribute are:

1. FileEditViewHistoryRestoreEnabled: "True" or "False".
1. nbMaxFile: 20 by default
1. activeMainIndex: 0 (not fully implemented)

<p>Follow `<File>` tags similar to those in the session file. However fold state is not recorded there.

Please note that the (invisible as of 6.6.6) checkbox for enabling view restore for individual files should not be checked wihile "Remember last session" is.

## Keyboard shortcuts: shortcuts.xml

This file has the following nodes:

1. `<InternalCommands>`: Notepad++ menu commands that were remapped
1. `<Macros>`: Current macro set as it appears in the lower part of the Macro menu
1. `<UserDefinedCommands>`: Contents of the Run menu
1. `<PluginCommands>`: plugin commands that were remapped.
1. `<ScintillaKeys>`: basic Scintilla commands, most of which relate to selecting text and moving around in the editor.

<p>The format of the contents of these nodes is detailed below. The user interface provided by Notepad++ is such that only the `<Macros>` section might need editing, under normal circumstances.


### `<InternalCommands>`

When not empty, the node contains `<Shortcut>` tags, the order of which doesn't matter.


 Attributes for the `<Shortcut>` node


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> id </td>
<td> integer </td>
<td> The command id associated with the menu entry. The complete list of these is to be found in the menuCmdIds.h source file.
</td></tr>
<tr>
<td> 2 </td>
<td> Ctrl </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Control modifier
</td></tr>
<tr>
<td> 3 </td>
<td> Alt </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Alt modifier
</td></tr>
<tr>
<td> 4 </td>
<td> Shift </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Shift modifier
</td></tr>
<tr>
<td> 5 </td>
<td> Key </td>
<td> integer </td>
<td> The base virtual key number, in the 1.255 range
</td></tr></tbody></table>

### `<Macros>`

When not empty, this node is made of `<Macro>` nodes, each of which represents an individual macro. Each `<Macro>` holds a nonempty list of `<Action>` tags which represent individual macro steps. These steps are either Scintilla commands or Notepad++ commands, not raw keystrokes. For more details on macro recording, see [Macros](../macros/).

The order of `<Macro>` nodes is reflected in the lower part of the Macro menu, and is otherwise not important. Order of `<Action>` tags, in contrast, is usually crucial.


 Attributes for the `<Macro>` node


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> name </td>
<td> string </td>
<td> The name of the macro. Several macros may have the same name
</td></tr>
<tr>
<td> 2 </td>
<td> Ctrl </td>
<td> "yes"/"no" </td>
<td> The key being mapped to has the Control modifier
</td></tr>
<tr>
<td> 3 </td>
<td> Alt </td>
<td> "yes"/"no" </td>
<td> The key being mapped to has the Alt modifier
</td></tr>
<tr>
<td> 4 </td>
<td> Shift </td>
<td> "yes"/"no" </td>
<td> The key being mapped to has the Shift modifier
</td></tr>
<tr>
<td> 5 </td>
<td> Key </td>
<td> integer </td>
<td> The base virtual key number, in the 1..255 range
</td></tr></tbody></table>
<p>Although it is possible for several macros to share the same shortcut, this practice is highly discouraged.


 Attributes for the `<Action>` tag


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> type </td>
<td> integer </td>
<td> <p>
* 0 for Scintilla messages that do not pass a string as second parameter
* 1 for Scintilla messages that pass a string as second parameter
* 2 for Notepad++ defined commands
* 3 for search and replace recording

<p>
</td></tr>
<tr>
<td> 2 </td>
<td> message </td>
<td> integer </td>
<td> 0 if type=2, else message id. The complete list of message ids can be found in the [Scintilla.iface](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/scintilla/include/Scintilla.iface) source file.
</td></tr>
<tr>
<td> 3 </td>
<td> wParam </td>
<td> integer </td>
<td> Command id when type=2 or 3, else actual first parameter of the message. Use 0 if not used.
</td></tr>
<tr>
<td> 3 </td>
<td> lParam </td>
<td> integer</td>
<td> 0 unless type=0 and the second parameter of the message is actually used, or scalar value used when type is 3.
</td></tr>
<tr>
<td> 4 </td>
<td> sParam </td>
<td> string </td>
<td> "" unless type=1 or 3, in which case this is the string pointed by the second parameter of the message
</td></tr></tbody></table>
<p>Thus, global properties cannot be modified in this manner, because the corresponding messages pass a string in the first parameter. Any Scintilla or Windows message that does not return a value, passes an integer in wParam and either an integer or string in lParam will do. The full list of Scintilla messages, as well as a concise documentation, can be found in `<source folder>`\Scintilla/include/Scintillla.iface.


#### Search / Replace encoding

Single search and replace operations are encoded as a series of actions with type = 3. These are described in ["Searching actions when recorded as macros"](../searching/#searching-actions-when-recorded-as-macros).


### `<UserDefinedCommands>`

When not empty, this node contains `<Command>` tags, which have the command string as contents. Their order is reflected in the Run menu, otherwise it doesn't matter.


 Attributes for the `<Command>` tag


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> name </td>
<td> string </td>
<td> The name of the Run command. Several commands may have the same name
</td></tr>
<tr>
<td> 2 </td>
<td> Ctrl </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Control modifier
</td></tr>
<tr>
<td> 3 </td>
<td> Alt </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Alt modifier
</td></tr>
<tr>
<td> 4 </td>
<td> Shift </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Shift modifier
</td></tr>
<tr>
<td> 5 </td>
<td> Key </td>
<td> integer </td>
<td> The base virtual key number, in the 1.255 range
</td></tr></tbody></table>
<p>Use the ^ or | concatenation character as appropriate to have the OS execute several commands in a row. The commands use the same syntax and helper environment variables as explained in [External Programs](#404-Not-Found "TBD").


### `<PluginCommands>`

When not empty, this node is made of auto-closed `<PluginCommand>` tags. Their order doesn't matter.


 Attributes for the `<PluginCommmand>` tag


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> moduleName </td>
<td> string </td>
<td> The name with extension of the dll that contains the plugin
</td></tr>
<tr>
<td> 2 </td>
<td> internalID </td>
<td> integer </td>
<td> The command number in the plugin. This can be assessed by counting the position of the corresponding menu item in the plugin submenu (separators count for one entry). Then substract 1 as ID's start at zero.
</td></tr>
<tr>
<td> 3 </td>
<td> Ctrl </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Control modifier
</td></tr>
<tr>
<td> 4 </td>
<td> Alt </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Alt modifier
</td></tr>
<tr>
<td> 5 </td>
<td> Shift </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Shift modifier
</td></tr>
<tr>
<td> 6 </td>
<td> Key </td>
<td> integer </td>
<td> The base virtual key number, in the 1.255 range
</td></tr></tbody></table>
<p>The order in which TextFX functions are loaded is not obvious from the menu layout. However, you can compute the internalID of a function as follows:

1. Go to **Settings &gt; Shortcut Mapper &gt; Plugin commands**
1. Note the index of the function you are after
1. Substract the index for I:TEXTFX NULL FUNCTION. This depends on what plugins you have and in which order they were loaded.
1. Add 2 to the result to get the correct internalID.

<p>A similar method will work for other plugins, but the value to substract is the index of the first entry for the plugin, and you must not add any correction. Remember that a separator is just another entry.


### `<ScintillaKeys>`

When it is not empty, this node contains `<ScintKey>` and `<NextKey>`  tags. Each `<ScintKey>` tag correspond to a Scintilla command being remapped. The order of these tags doesn't matter.

When a Scintilla command has several keyboard bindings, the first one to be defined is stored in a `<ScintKey>` tag. The extra bindings are stored in `<NextKey>` tags that follow the main `<ScintKey>`, in the order defined by the list on the left of the Modify dialog for the entry.


 Attributes for the `<ScintKey>` tag


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> ScintId </td>
<td> integer </td>
<td> The id of the message being remapped
</td></tr>
<tr>
<td> 2 </td>
<td> menuCmdID </td>
<td> integer </td>
<td> The command number associated to the message, if there is any. Use 0 if this message is not a Notepad++ menu command
</td></tr>
<tr>
<td> 3 </td>
<td> Ctrl </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Control modifier
</td></tr>
<tr>
<td> 4 </td>
<td> Alt </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Alt modifier
</td></tr>
<tr>
<td> 5 </td>
<td> Shift </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Shift modifier
</td></tr>
<tr>
<td> 6 </td>
<td> Key </td>
<td> integer </td>
<td> The base virtual key number, in the 1.255 range
</td></tr></tbody></table>
<p>`<NextKey>` tags have the same structure as a `<ScintKey>`, except that the first two attributes are not defined - they would be redundant.


## Built-in language features


### Keyword lists: langs.xml

This file, inside the mandatory `<NotepadPlus>` tag, contains a single `<Languages>` node, made of `<Language>` nodes.

Each `<Language>` node has one or more `<Keywords>` tags. These tags have a name attribute. They contain keyword lists, which are space separated and sorted lists of keywords. The intervening space is not required between two keywords if one ends in a non letter character and so starts the next one.

The order of the `<Language>` tags is reflected in the Language menu. Otherwise it doesn't matter. It is however suggested to keep them/the menu sorted.


 Attributes for the `<Language>` node


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> name </td>
<td> string </td>
<td> The name of the language.
</td></tr>
<tr>
<td> 2 </td>
<td> ext </td>
<td> string </td>
<td> The list of file extensions associated to this language by default. Lists are space separated, without leading periods.
</td></tr>
<tr>
<td> 3 </td>
<td> commentLine </td>
<td> string </td>
<td> The character(s) that prelude a comment extending to the end of the physical line. Use "" if the feature is not supported.
</td></tr>
<tr>
<td> 4 </td>
<td> commentStart </td>
<td> string </td>
<td> The character(s) that start a block comment. Use "" if the feature is not supported.
</td></tr>
<tr>
<td> 5 </td>
<td> commentEnd </td>
<td> string </td>
<td> The character(s) that end a block comment. Use "" if the feature is not supported.
</td></tr>
<tr>
<td> 6 </td>
<td> exclude </td>
<td> "yes"/"no" </td>
<td> Set to yes" to remove from the Language menu, else "no" or no attribute.
</td></tr>
<tr>
<td> 7 </td>
<td> tabSettings </td>
<td> integer </td>
<td> If present, the value encodes the number of spaces a tab is equivalent to: value + 128 if the Replace tabs vy spaces is checked, else raw value. The default value of 4 is used if attribute is absent.
</td></tr></tbody></table>

### Highlighting schemes: stylers.xml

The mandatory `<NotepadPlus>` node contains a `<LexerTypes>` and a `<GlobalStyles>` node. The `<LexerTypes>` node contains `<LexerType>` nodes whose order and name must match the `<Language>` nodes found in langs.xml. The `<ClobalStyles>` node behaves like a special `<LexerType>`.

The user interface in **Settings &gt; Styler Configurator** is so complete as to make manual edits for this file unneeded, under normal circumstances.

The attributes of a `<LexerType>` node are:

1. name: a string, the language name
1. desc: a string, displayed in the status bar when this lexer is being used.
1. ext: a string, the list of user defined file extensions to associate with the lexer. The lists are space separated, without leading periods.

<p>Each `<LexerType>` contains one or more `<WordStyle>` tag. Their order and style ID must not be changed, as they reflect the internal lexer's code.


 Attributes for the `<WordStyle>` tag


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> name </td>
<td> string </td>
<td> The name of the style being defined, usually in upper case
</td></tr>
<tr>
<td> 2 </td>
<td> styleID  </td>
<td> integer </td>
<td> The internal Scintilla style ID. Do not change this attribute unless you recompile SciLexer.dll and perform corresponding changes in its code
</td></tr>
<tr>
<td> 3 </td>
<td> fgColor </td>
<td> hex integer </td>
<td> The RGB representation of the foreground color to use for this sort of token
</td></tr>
<tr>
<td> 4 </td>
<td> bgColor </td>
<td> hex integer </td>
<td>  The RGB representation of the background color to use for this sort of token
</td></tr>
<tr>
<td> 5 </td>
<td> fontName </td>
<td> string </td>
<td> The name of the font face to display this token with. Use "" for default font.
</td></tr>
<tr>
<td> 6 </td>
<td> fontStyle </td>
<td> integer </td>
<td> Flags or'ed together to summarise the properties of the font (bold=1, italic=2, underlined=4).
</td></tr>
<tr>
<td> 7 </td>
<td> fontSize </td>
<td> integer </td>
<td> Size in points of the font to be used to display this token. Use "" for default size.
</td></tr>
<tr>
<td> 8 </td>
<td> keywordClass </td>
<td> string </td>
<td> Use this style to display words from the word list with the same name in langs.xml. Do not specify if not applicable.
</td></tr></tbody></table>
<p>The `<WordStyle>` tags in the `<GlobalStyles>` node describe elements for which some of the attributes above do not apply, like font data for the Fold margin. In that event, they are left out. They have usually no contents, and as such come in short form.

However, if custom keywords are added to the language, the list of space separated words is the contents, and the tag takes a long form instead.

The same considerations apply to theme files, which are alternates stylers.xml.


## The context menu

The way to customise the [Context Menu](#404-Not-Found TBD) is explained in detail there.


## Toolbar icons

The way to customise [Toolbar Icons](#404-Not-Found TBD) is explained in detail there.


## Session files

There may be as many session files as you like, but, if remembering the current session is enabled, the session.xml will always record this data when Notepad++ terminates normally.

Inside the `<NotepadPlus>` node, there is only one `<Session>` node. It has one activeView attribute, which is "0" if the main view was holding the active document buffer, and "1" if the secondary view did.

The `<Session>` node has a `<MainView>` and `<SubView>` node, which have the same structure. They have an activeID integer attribute which is the index of the active tab for the view. This is 0 if the view does not exist.

Each view node has zero or more `<File>` tags. If the view has no files, the node is auto-closed. Since the active index relates to the order in which the File tags are listed, it is best not to change that order.


 Attributes for the `<File>` tag


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> firstVisibleLine </td>
<td> integer </td>
<td> 0-based index of the first visible line
</td></tr>
<tr>
<td> 2 </td>
<td> xOffset </td>
<td> integer </td>
<td> 0-based offset of the first visible character on an given line
</td></tr>
<tr>
<td> 3 </td>
<td> scrollWidth </td>
<td> integer </td>
<td> reference width in pixels to compute the horizontal thumb width
</td></tr>
<tr>
<td> 4 </td>
<td> startPos </td>
<td> integer </td>
<td> position of first styled character
</td></tr>
<tr>
<td> 5 </td>
<td> endPos </td>
<td> integer </td>
<td> position of the last styled character
</td></tr>
<tr>
<td> 6 </td>
<td> lang </td>
<td> string </td>
<td> Name of the language being used to highlight the document
</td></tr>
<tr>
<td> 7 </td>
<td> filename </td>
<td> string </td>
<td> full path and name of file
</td></tr></tbody></table>
<p>When a file does not have bookmarks or collapsed fold points, the corresponding File tag is auto-closed. Otherwise, it contains zero or more  auto-closed tags having a "line" attribute, the value of which is the **0-based** line number of the marker, and zero or more `<Fold>` tags with a 0-based "line" number for each collapsed fold point. Hidden lines are not being recorded as of v6.6.6.


## User defined languages: userDefineLang.xml

(requires in-depth review, wait till UDL 3.0 perhaps)

The User Define Language panel should make it useless to edit this file, under normal circumstances.

The mandatory `<NotepadPlus>` node may have one or more `<UserLang>` nodes.

The `<UserLang>` nodes have two attributes:

1. name: a string, the language name
1. ext: a string, the space separated list of file extensions associated to this lexer, without leading period

<p>These nodes have three nodes, the structure of which is described below:

1. `<Settings>`
1. `<Keywords>`
1. `<WordStyle>`


### `<Settings>`

This node has:

1. A `<Global>` auto-closed tag, with
1. caseIgnore,a "yes"/"no" attribute. Set to "yes" if the language is case insensitive, else "no".
1. escapeChar: this attribute is a string at most one character long. If absent or empty, the language does not support an escape character. Otherwise features the escape character.

1. A `<TreatAsSymbol>` auto-closed tag, with two "yes"/"no" attributes, comment and commentLine. They reflect the state of the corresponding checkbox.
1. A `<Prefix>` tag, with 4 "yes"/"no" attributes named words1 to words4. They reflect the prefix status of each word group.


### `<KeywordLists>`

They reflect the various lists on the panel. Its `<Keywords>` tags have the same format as their counterparts in langs.xml.


### `<Styles>`

This node has `<WordStyle>` tags which have the same function and format as their counterparts in stylers.xml.


## Autocompletion, aka API, files

API files are located in the plugins\APIs\ subfolder of the Notepad++ installation folder. These files are optional: you need only one for each language for which you'll use [Auto Completion](../auto-completion/) or calltips. They are also supported for User Defined Languages, and bear the name `<Language name>`.xml.

Under the usual `<NotepadPlus>` tag is a `<AutoComplete>` tag. It has an optional, unused "language" attribute, which you can use for any descriptive purpose.

The contents of a `<AutoComplete>` start with an autoclosing `<Environment>` tag, with the following attributes:

1. ignoreCase: "no" if the language is case sensitive, else "yes" (default).
1. startFunc: the character(s) which start the parameter list. Default is "(".
1. stopFunc: the character(s) which end the parameter list. Default is ")".
1. paramSeparator: the character(s) which separate parameters. Defaults to ",".
1. terminal: the character(s) which mark the end of a prototype, when the language allows C-style separate prototyping. Defaults to ";". Leave it out if the language does not support separate prototyping, or set it to some illegal character.
1. additionalWordChar: character(s) that may be part of words and which are not a lower or upper case letter, a digit or the underscore. The value is a string with all these extra characters, in any order and without separators. The string is empty by default.

<p>NOTE: Spaces can't be used as the character for the attributes and additionalWordChar is still not working (Notepad++ v.6.5.2) but maybe in future releases...

<br>
Any attribute can be omitted, and the `<Environment>` tag as well. The practice is not recommended though.

Following is a list of `<KeyWord>` tags. They are either auto-closing, for keywords that are not routines, or not when they are. Each such tag has a mandatory "name" attribute, the keyword/routine name to recognise. The list **must be sorted according to this attribute and the value of the `<Environment>` ignoreCase attribute**. See subsections below for more on keyword names and sorting.

When a `<KeyWord>` tag is not auto-closing, it must have a second attribute, "func", set to "yes". The contents are a nonempty, unsorted list of `<Overload>` tags, each of which describes a possible signature for the routine. `<Overload>` has a "retVal" attribute, which you would set to the initial comment in the call tip. In C/C++, this traditionally would be the return type; "" is a permitted value. Furthermore, the `<Overload>` tag has an optional "descr" attribute, which can be used to add a description of the function. Tip: You can use &amp;#x0a; to insert line breaks.

An `<Overload>` tag contains one or more parameter description, sorted in occurrence order. Such description is represented by an auto-closing `<Param>` tag with a "name" attribute. This may contain a parameter name or other useful comments.

The parameter names (actually any text you like, it may even mention a parameter name), return value and description have to fit into an internal buffer, truncation occurs otherwise. For any given function, all text, plus 2 bytes per parameter, plus 24 bytes if 2 overloads or more, can't spill over 2,043 bytes. Remember that a byte is a byte, so formatting whitespace competes with actual text.

A typical example of entry could be this:

<pre>       `<KeyWord name="cos" func="yes" >`
           `<Overload retVal="{double}" descr="Cosine of x" >`
               `<Param name="x, radians" />`
           `</Overload>`
       `</KeyWord>`
</pre>
<p>resulting in the following call tip:

<pre>{double} cos (x, radians)
Cosine of x
</pre>
<p>Remember that the call tip shows up when you type the opening parenthesis after the routine name. Default "(" or whatever set with startFunc in the `<Environment>` tag.


### Names

For both call tips and autocompletion to work, keywords must be words, ie identifiers most languages would readily accept. This means that only the 26 Latin alphabet letters in either lower or upper case (no diacritics), digits and the underscore are safe to use. Additional allowed characters will work if they are not whitespace. Autocompletion may cope with spaces or blanks, call tips won't. This is a Scintilla limitation.


### Sorting

The `<KeyWord>` tag list must be sorted by "name" in ascending order. **Failure to do so will result in a non working file, without a warning**.

Now which sorting, case sensitive or insensitive? It depends on the value of the ignoreCase `<Environment>` attribute. If set to "yes", use case insensitive sorting, which considers all letters to be in upper case. Otherwise, use case sensitive sorting.

The simplest way to build a new file might be this:

1. in a new document, list all keywords to be recognised;
1. use TextFX to sort the list with the right ordering;
1. Using the Column Editor, add &lt;KeyWord name=" in front of each line.
1. Using extended mode replace, add "/&gt; at the end of all lines. Or use TextFX's Insert (Clipboard) through lines;
1. Add some fancy character ('+' is a good candidate) to the end of lines that represent functions;
1. Using extended mode, replace /&gt;+\r\n by &gt;\r\n\t`<Overload retVal="">`\r\n\t`</Overload>`\r\n`</KeyWord>`\r\n You may prefer using TextFX's Find/Replace;
1. Now manually add text and extra overloads. Reindent as applicable;
1. Save and test your file;
1. Sloppy work, test again (recursive, beware of infinite loops).


## Workspace files

The project maneger stores its contents in workspace files, which may bear any name or extension.

Inside the `<NotepadPlus>` usual tag are `<Project>` tags, which may contain any mix and match of `<Folder>` and `<File>` tags, all with a mandatory <i>name</i> attribute. A `<Folder>` can have the same sort of contents as a `<Project>`. `<File>` is autoclosing.

There are two sorts of names, file names and other names. The latter are arbitrary, while the fie names, only found as <i>name</i> attribute for `<File>`, refer to a path relative to where the workspace file is. As a result, moving a workspace file is not recommended, because all files are lost track of.


## FunctionList

This section describes the contents of the functionList.xml file, which defines parsing rules used for building the source item tree displayed by the [Function List](../function-list/) feature. Active contents appear inside a `<functionList>` tag inside the ubiquitous `<NotepadPlus>` tag.


### Associations

First comes an `<associationMap>` tag, which contains one or more `<association/>`. Each `<association/>` has two attributes: langID and id.
The former is a built-in language ID, the list of which is included in the default functionList.xml. The second is a name of your choice. The meaning of the tag is that the parser with said name applies to source files highlighted as the language with langID identifier. If several associations reference the same language, the topmost one wins.

Instead of a langID, you can specify an ext attribute, which is a string containing a single extension for files the parser will apply to - so you need as many associations to the same parser id as there are extensions it applies to. Files without an extension are associated with ext=""; otherwise the string must have a leading dot.


### Parsers

Next comes a `<parsers>` tag containing one or more `<parser>` tags.

Parsers come in two basic flavors: classRange or function. A parser may contain either one, or both.

A parser has an id (which is supposed to match the id of some `<association/>`), a displayName, which will be shown on he panel, and a commentExpr regular expression. Areas matched by this expressions will be ignored in parsing anything else.


#### `<function>` parsers

A `<function>` has a single attribute, mainExpr, which is a regular expression matching the declaring part of the function, up to the start of its body. The default file adds a displayMode attribute to most `<function>` and `<classsRange>` parsers, but it does not appear to be used anywhere as of v6.6.6.

It contains a single `<functionName>` container tag, which contains one or more `<funcNameExpr/>` tag(s). Each of these has a single expr attribute, which is a regular expression. To find the name of a function, each expr attributes is searched in turn in the data mainExpr matched. First non empty result displays as the function name.


#### `<classRange>` parsers

The attributes and nested tags of a `<classRange>` parser mostly parallel those of a `<function>` parser, except that there are some extra attributes.

The class header is whatever matches its mainExpr attribute. To extract the class name from this data, the `<className>` nested container tag is parsed. Each of its `<nameExpr/>` nested tags has an expr attribute, a regular expression that extracts the name from the header. `<classRange>` also has a displayMode attribute that does not seem to be in use.

The `<classRange>` tag has two additional attributes, openSymbole and closeSymbole. Both are regular expressions which determine where the class body starts and ends. A function whose header is found inside a class body belongs to the class and its tree item has the class tree item as its parent.

