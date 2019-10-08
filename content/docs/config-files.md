---
title: Configuration Files
linktitle: config-files
weight: 115
---

# Configuration Files

Notepad++ offers a comprehensive user interface to review or change most of its settings. However, there are some special cases where it is worthwhile to edit the configuration files directly, including:

* Customizing the Context Menu
* Editing previously-recorded macros, or crafting new macros manually
* Adding keywords to a language, because the new language version isn't matched yet

The underlying XML files are all found in `%AppData%\notepad++\` (or, for zip-based local installations, in the notepad++ executable directory) unless otherwise noted.

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

## The context menu: `contextMenu.xml`

<!-- http://web.archive.org/web/20190518131311/http://docs.notepad-plus-plus.org/index.php/Context_Menu -->

The context menu does not have a GUI-based editor; you just need to edit the file.  As a result, the **Settings > Edit Popup Context Menu** entry exists to make it easy for you to access this config file.

All menu commands can be added to the Context Menu, including plugin commands:

* To add a built-in command, you need to provide the main menu name (as it appears in the main menu bar) as the value of the MenuEntryName attribute and the command's item name (as it appears in the menu) as the value of the MenuItemName attribute. The MenuEntryName attribute must reference an entry on the main menu bar and must be an ancestor of the MenuItemName attribute, regardless of its depth.
* To add a plugin command, you need to provide the plugin's menu item name (as it appears in the Plugins menu) as the value of the PluginEntryName attribute and the command's menu item name (as it appears in the plugin's sub-menu) as the value of the PluginCommandItemName attribute.

Note that the value you add should be in English, not in a translated language. The Shortcut Mapper will help you find the English name of plugin commands; simply switch to English localization for the raw name of built-in commands. If you wish to use IDs, they can be found in [menuCmdID.h](https://github.com/notepad-plus-plus/notepad-plus-plus/trunk/PowerEditor/src/menuCmdID.h), or can be found in your localization file.

### Grouping items into sub-menus

If you add a `FolderName="name_of_submenu"` attribute to consecutive items, they will be grouped into a sub-menu with that name. Specifying "" is the same as leaving the FolderName attribute out. Note that sub-menus do not nest - you cannot add a sub-menu to a sub-menu. Non-Latin characters are supported.

### Overriding a menu item name

If you add an `ItemNameAs="new_name_for_the_item"` attribute, the new name will be displayed instead of the standard one, which you'd get from the menu bar or its sub-menus. This is useful when the name is lengthy, as it makes the Context Menu unwieldy otherwise. Non-Latin characters are supported.

## Keyboard shortcuts: `shortcuts.xml`

Defines keyboard shortcuts for various types of commands.  The shortcuts are most-easily defined in the various tabs of the [**Settings > Shortcut Mapper**](../preferences/#shortcut-mapper).

This file has the following nodes:

1. `<InternalCommands>`: Keyboard shortcuts for Notepad++ menu commands that have been remapped by the.  (Commands that use their default shortcuts are not listed here.)
1. `<Macros>`: Keyboard shortcuts for the macros listed in the lower part of the [**Macro**](../macros/) menu.  Also defines what commands those macros execute.
1. `<UserDefinedCommands>`: Keyboard shortcuts for the Run menu entries.  Also defines what actions those entries take.
1. `<PluginCommands>`: Keyboard shortcuts for plugin commands that have been remapped.  (Commands that use their default shortcuts are not listed here.)
1. `<ScintillaKeys>`: Keyboard shorcuts for Scintilla commands, most of which relate to selecting text and moving around in the editor. (Commands that use their default shortcuts are not listed here.)

The definitions of the `<Macros>` and `<UserDefinedCommands>` are generally all that benefit from manual editing of the `shortcuts.xml`.  It is much safer to edit the shortcuts using the [**Shortcut Mapper**](../preferences/#shortcut-mapper)

### Virtual Key Number

All the types of commands in `shortcuts.xml` have a `key` attribute, which uses the Windows virtual key number as the value.  This is _not_ necessarily the same as the ASCII code or Unicode codepoint.  In standard English locales, the virtual key usually lines up with the ASCII code for the character, but that is not universally true.  The complete list of base virtual key code is to be found on [keys.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/keys.h). Because of this reliance on OS-defined virtual keys, many letters in your native alphabet cannot be used, though for characters that are entered directly with a key on your keyboard, it may be possible (with some effort) to determine the virtual key number for the key.  (Some hints are given in the Notepad++ Community Forum at [this post](https://community.notepad-plus-plus.org/post/43733) and [this other post](https://community.notepad-plus-plus.org/post/43888).)

### `<Macros>`

When not empty, this node is made of `<Macro>` nodes, each of which represents an individual macro. Each `<Macro>` holds a nonempty list of `<Action>` tags which represent individual macro steps. These steps are either Scintilla commands or Notepad++ commands, not raw keystrokes. For more details on macro recording, see [Macros](../macros/).

**Attributes for the `<Macro>` node**

Position | Name | Value format | Meaning
:--------|:-----|:-------------|:---
1  | name | string       | The name of the macro. Several macros may have the same name
2  |  Ctrl  |  "yes"/"no"  |  The key being mapped to has the Control modifier
3  |  Alt  |  "yes"/"no"  |  The key being mapped to has the Alt modifier
4  |  Shift  |  "yes"/"no"  |  The key being mapped to has the Shift modifier
5  |  Key  |  integer  |  The base virtual key number, in the 1..255 range

Although it is possible for several macros to share the same name or shortcut, this practice is highly discouraged.

**Attributes for the `<Action>` tag**


Position | Name | Value format | Meaning
:--------|:-----|:-------------|:---
1  | type  |  integer  | `0` for Scintilla messages that do not pass a string as second parameter
   |       |           | `1` for Scintilla messages that pass a string as second parameter
   |       |           | `2` for Notepad++ defined commands
   |       |           | `3` for search and replace recording
2  | message  |  integer  | `0` if `type=2`, otherwise use the message id
3  | wParam  |  integer  |  Command id when `type=2` or `type=3`, else actual first parameter of the message. Use `0` if the message or command doesn't require a wParam.
4  | lParam  |  integer |  `0` unless `type=0` and the second parameter of the message is actually used, or scalar value used when `type=3`.
5  | sParam  |  string  |  `""` unless `type=1` or `type=3`, in which case this is the string pointed by the second parameter of the message.

The full list of Scintilla messages for `type=0` and `type=1`, as well as a concise documentation, can be found in [Scintilla.iface](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/scintilla/include/Scintilla.iface).  More details on those messages can be found in the [Scintilla Docs](https://scintilla.org/ScintillaDoc.html).

The `wParam` command IDs for `type=1` can be found as the `IDM` constants in the source file [menuCmdID.h](https://github.com/notepad-plus-plus/notepad-plus-plus/trunk/PowerEditor/src/menuCmdID.h), or you can look at the `localization\English.xml` (or your language of choice), which lists the `<Item id="...">` next to the text of the command; the value of the `id` attribute is the "command ID".

For `type=3` search-and-replace macros, see the detailed description in ["Searching > Searching actions when recorded as macros"](../searching/#searching-actions-when-recorded-as-macros).

You can use any Scintilla or Windows message that does not return a value, that passes an integer in `wParam`, and either an integer or string in `lParam`.  There are some messages that require strings in the `wParam`, or various data structures: those will not work in a macro.

For more on the messaging system, see [Plugin Communication](../plugin-communication/).

### `<UserDefinedCommands>`

When not empty, this node contains `<Command>` tags, which have the command string as contents. Their order is reflected in the Run menu, otherwise it doesn't matter.


**Attributes for the `<Command>` tag**


Position | Name | Value format | Meaning
:--------|:-----|:-------------|:---
1  |  name  |  string  |  The name of the Run command.
2  |  Ctrl  |  "yes"/"no"  |  The key mapped to has the Control modifier
3  |  Alt  |  "yes"/"no"  |  The key mapped to has the Alt modifier
4  |  Shift  |  "yes"/"no"  |  The key mapped to has the Shift modifier
5  |  Key  |  integer  |  The base virtual key number, in the 1 - 255 range

Although it is possible for several commands to have the same name, this is confusing and thus discouraged.

The run command may contain any valid command for the <abbr title="Operating System: Generally Windows.  If you use Notepad++ in a Linux WINE environment or similar, could you create a pull request clarifying whether it's windows-style command syntax or linux-style command syntax.">Windows OS</abbr>.  Thus, if you enter a URL, Windows will launch your default browser with that URL.
The commands use the same syntax and helper environment variables as explained in [TBD](#404-Not-Found "TBD: was External Programs NppWiki++ page; need to incorporate that in the new docset").  Use the concatenation characters as appropriate to have the OS execute several commands in a row.

## User Interface settings: `config.xml`

The following sections are defined:

1. `<GUIConfigs>`: user interface settings (usually set in the [**Settings > Preferences**](../preferences/#preferences)).
2. `<FindHistory>`: most of the latest state of the Find/Replace dialog box.
3. `<History>`: the list of recently used files.
3. `<ProjectPanels>`: associates workspace files with a given project panel


## Keyword lists: `langs.xml`


This file contains the keyword lists for syntax highlighting languages.

**Attributes for the `<Language>` node**

Position | Name | Value format | Meaning
:--------|:-----|:-------------|:---
1  |  name  |  string  |  The name of the language.
2  |  ext  |  string  |  The list of file extensions associated to this language by default. Lists are space separated, without leading periods.
3  |  commentLine  |  string  |  The character(s) that prelude a comment extending to the end of the physical line. Use "" if the feature is not supported.
4  |  commentStart  |  string  |  The character(s) that start a block comment. Use "" if the feature is not supported.
5  |  commentEnd  |  string  |  The character(s) that end a block comment. Use "" if the feature is not supported.
6  |  exclude  |  "yes"/"no"  |  Set to yes" to remove from the Language menu, else "no" or no attribute.
7  |  tabSettings  |  integer  |  If present, the value encodes the number of spaces a tab is equivalent to: value + 128 if the Replace tabs vy spaces is checked, else raw value. The default value of 4 is used if attribute is absent.

Inside each of the languages, you _could_ add keywords.  However, it's better to use [**Settings > Style Configurator**](../preferences/#style-configurator) and make use of the user-defined keywords box for a given category (when available).  These user-defined keywords are stored in [`stylers.xml`](#highlighting-schemes-stylers-xml) (described below).

## Highlighting schemes: `stylers.xml`

This file sets the color scheme for the default theme.  The other themes are stored in `themes\*.xml`, which follow the same format at `stylers.xml`.  In general, use [**Settings > Style Configurator**](../preferences/#style-configurator) for easier maintenance of styles.

Each lexer type has it's own `<LexerType>` section, with multiple `<WordsStyle>` entries.  Each lexer from the **Language** menu has it's own list of available `<WordsStyle>` entries.  Trying to add a new `<WordsStyle>` to a lexer to try to get more categories of keywords will _not_ be successful, because the underlying code which does the syntax highlighting has no internal rules for mapping the entries found to that style.

If you have added user-defined keywords in the [**Settings > Style Configurator**](../preferences/#style-configurator), they will be stored as the contents of the `<WordsStyle>`, as a space-separated list (for example, `<WordsStyle>fancyKeyword1 fancyKeyword2</WordsStyle>`).

## Other Configuration Files

* `userDefineLang.xml`: see [in the User-defined Languages doc](../user-defined-language-system/).

* Autocompletion, aka API, files: see [Auto-completion: Auto-completion File Format](http://localhost:1313/docs/auto-completion/#auto-completion-file-format)

* `session.xml`: stores session information
