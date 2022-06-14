---
title: Configuration Files Details
linktitle: config-files
weight: 115
---

# Configuration Files

Notepad++ offers a comprehensive user interface to review or change most of its settings. However, there are some special cases where it is worthwhile to edit the configuration files directly, including:

* Customizing the Context Menu
* Editing previously-recorded macros, or crafting new macros manually
* Adding keywords to a language, because the new language version isn't matched yet

Please note that Notepad++ writes the configuration files when it exits, which is why the [Editing Configuration Files](#editing-configuration-files) section below says that Notepad++ may overwrite your changes.  But this also means that, when you make a change using Notepad++ menus and dialogs (like changing a preference, or saving a macro), your change will not be written to the configuration file until Notepad++ exits.  So if you open up the configuration file after you have changed the preference but before you have exited Notepad++, you will _not_ see that change reflected in the file yet.  Do not be surprised by this.

## Configuration Files Location

In a standard installation, the configuration files go in `%AppData%\Notepad++\`.  (For a refresher course on `%AppData%`, see the [Community Forum FAQ's `%AppData%` entry](https://community.notepad-plus-plus.org/topic/15740/faq-desk-what-is-appdata).)

In a portable installation, the configuration files go in the same directory as the `notepad++.exe` executable.  (An installation is treated as "portable" if the zero-byte `doLocalConf.xml` file is present alongside the `notepad++.exe` executable.  The **?** menu's **Debug Info** will show `Local mode: ON` for a portable version.)

If you enable the [Cloud settings](../preferences/#cloud), some configuration files will go in the defined directory (including `contextMenu.xml`, `shortcuts.xml`, `userDefineLang.xml`, `langs.xml`, `stylers.xml`, and `config.xml`;
the `userDefineLang\` subfolder can be placed there as well, though it won't be created by default when the Cloud settings folder is first populated).

There is a [command-line option](../command-prompt/) `-settingsDir` which will set a new directory for the configuration file location (added in v7.9.2).

If the `-settingsDir` option is set, that configuration file directory will take priority over any other configuration file directory. If the Cloud directory setting is defined and enabled, that will take priority over the portable or standard configuration file directory. If `doLocalConf.xml` is present, the portable configuration file location will take priority over the `%AppData%\Notepad++\` directory.  If none of the other configuration file directories are active, then the standard configuration file directory is `%AppData%\Notepad++\`.

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

The `config.xml` file may be overwritten by Notepad++ on exit, even if you follow this procedure, so that sequence won't reliably work for `config.xml`.  To edit `config.xml`, close all instances of Notepad++; edit `config.xml` in some "other" editor and save; reload Notepad++ and the changes should take effect.  (For the "other" editor, you _could_ use something like Windows' builtin notepad.exe.  But it would be better if you had another portable Notepad++ somewhere on your machine, and use that portable Notepad++ to edit your main Notepad++'s `config.xml`, thus never having to use a non-Notepad++ editor: so close your main Notepad++, run the portable Notepad++ and open your main `config.xml`, edit and save, exit the portable Notepad++, then re-run the main Notepad++, and everything should be updated.)

## Configuration Files during Upgrades

When you use the installer to upgrade your existing copy of Notepad++ (either manually, or through the **?**-menu's **Upgrade Notepad++**, or through Notepad++'s auto-update feature), the installer will avoid overwriting configuration files that you have customized -- this is to prevent you losing your preferred settings and customizations.  

However, this means that occasionally, updated functionList parsing files or themes, or new keywords in langs.xml, or new default contextMenu or shortcuts entries might not be added to your local copy of Notepad++.  So if you upgrade and keep your existing configuration, it is a good idea to occasionally compare your configuration files to the "standard/default" configuration files: some of the config files come with `*.model.xml` versions in the installation directory, which show you the default settings for those files; for other configuration files, you could [download](https://notepad-plus-plus.org/downloads/) a portable zipfile of the same version you are using, and compare the config files from the portable to your installed; and you can always look in the [source code repository](https://github.com/notepad-plus-plus/notepad-plus-plus/) for the various configuration files.  (You can use two [Views](../views/) to look at the files side-by-side, and the [synchronized scrolling feature](../views/#synchronized-scrolling) can help keep the copies aligned; plugins such as the Compare plugin are designed to show differences between files as well.)

For the `config.xml` (which contains the settings from the GUI's **Settings > Preferences** dialog), if Notepad++ has a setting that it doesn't find defined in your current `config.xml`, it will apply the default value compiled in the program, and the next time it writes `config.xml` it will write that default value in `config.xml`.  Once it gets written, future changes to that default value will not override the value already in your file, even when you upgrade Notepad++.  `config.xml` will only get a default value for a setting in three situations: 1) on a new installation (running the installer when there isn't a previous Notepad++, or when there isn't a `config.xml` file and/or settings directory for the active user); 2) when you run Notepad++, and there is no `config.xml` (either because there isn't a `config.xml` file and/or settings file for the current user, or the `config.xml` has been deleted), so Notepad++ writes a complete `config.xml` with all default values; 3) when your `config.xml` is missing the attribute/value pair for a given setting.

## The context menu: `contextMenu.xml`

<!-- http://web.archive.org/web/20190518131311/http://docs.notepad-plus-plus.org/index.php/Context_Menu -->

The context menu does not have a GUI-based editor; you just need to edit the file.  As a result, the **Settings > Edit Popup Context Menu** entry exists to make it easy for you to access this config file.

All menu commands can be added to the Context Menu, including plugin commands:

* To add a built-in command, you may provide the main menu name (as it appears in the main menu bar) as the value of the MenuEntryName attribute and the command's item name (as it appears in the menu) as the value of the MenuItemName attribute. The MenuEntryName attribute must reference an entry on the main menu bar and must be an ancestor of the MenuItemName attribute, regardless of its depth.
    * For example, `<Item MenuEntryName="Edit" MenuItemName="Cut"/>` will add a context-menu entry that calls the **Edit** menu's **Cut** entry.
* Alternately, to add a built-in command, you may instead provide the menu command ID via the `id` attribute.  The command ID values for a given menu can be found in your localization file (like [english.xml](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/english.xml)), which will map the localized text you see in the menu to the command ID, or in [menuCmdID.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/menuCmdID.h).
    * For example, `<Item id="42001"/>` will add a context-menu entry that calls the **Edit > Cut** action by its command ID.
    * **NOTE**: `<Item id="0"/>` has a special meaning: it acts as a horizonal separator line -- that's how you can get a line between groups in the context menu.
* To add a plugin command, you need to provide the plugin's menu item name (as it appears in the Plugins menu) as the value of the PluginEntryName attribute and the command's menu item name (as it appears in the plugin's sub-menu) as the value of the PluginCommandItemName attribute.
    * For example: `<Item PluginEntryName="MIME Tools" PluginCommandItemName="Base64 Encode" />` will add a context-menu entry that calls **Plugins > MIME Tools > Base64 Encode**

Note that the menu names and menu item names (whether built-in or plugin names) that you use in the should be in English, not in a translated language. The Shortcut Mapper can help you find the English name of plugin commands; simply switch to English localization for the raw name of built-in commands; or you can look at the [english.xml](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/english.xml) that shipped with your distribution.

By default, each `<Item>` will be rendered in the top level of the context menu with a localized name matching the normal menu entry, unless overridden by the attributes described next.

### Grouping items into sub-menus

Each `<Item>` will go in the first level of the context menu.  This can be overridden by adding a `FolderName="name_of_submenu"` attribute to consecutive items, so that they will be grouped into a sub-menu with that name. Specifying "" is the same as leaving the FolderName attribute out. Note that sub-menus do not nest - you cannot add a sub-menu to a sub-menu. Non-Latin characters are supported.

### Overriding a menu item name

Each `<Item>` will use the same text as the main menu entry uses, as defined by your current localization.  This can be overridden by adding an `ItemNameAs="new_name_for_the_item"` attribute, so that the new name will be displayed instead of the standard one.  This is useful when the name is lengthy, as it makes the Context Menu unwieldy otherwise. Non-Latin characters are supported.

## Keyboard shortcuts: `shortcuts.xml`

Defines keyboard shortcuts for various types of commands.  The shortcuts are most-easily defined in the various tabs of the [**Settings > Shortcut Mapper**](../preferences/#shortcut-mapper).

This file has the following nodes:

1. `<InternalCommands>`: Keyboard shortcuts for Notepad++ menu commands that have been remapped by the.  (Commands that use their default shortcuts are not listed here.)
1. `<Macros>`: Keyboard shortcuts for the macros listed in the lower part of the [**Macro**](../macros/) menu.  Also defines what commands those macros execute.
1. `<UserDefinedCommands>`: Keyboard shortcuts for the Run menu entries.  Also defines what actions those entries take.
1. `<PluginCommands>`: Keyboard shortcuts for plugin commands that have been remapped.  (Commands that use their default shortcuts are not listed here.)
1. `<ScintillaKeys>`: Keyboard shortcuts for Scintilla commands, most of which relate to selecting text and moving around in the editor. (Commands that use their default shortcuts are not listed here.)

The definitions of the `<Macros>` and `<UserDefinedCommands>` are generally all that benefit from manual editing of the `shortcuts.xml`.  It is much safer to edit the shortcuts using the [**Shortcut Mapper**](../preferences/#shortcut-mapper)

### Virtual Key Number

All the types of commands in `shortcuts.xml` have a `key` attribute, which uses the Windows virtual key number as the value.  This is _not_ necessarily the same as the ASCII code or Unicode codepoint.  In standard English locales, the virtual key usually lines up with the ASCII code for the character, but that is not universally true.  The complete list of base virtual key code is to be found on [keys.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/keys.h). Because of this reliance on OS-defined virtual keys, many letters in your native alphabet cannot be used, though for characters that are entered directly with a key on your keyboard, it may be possible (with some effort) to determine the virtual key number for the key.  (Some hints are given in the Notepad++ Community Forum at [this post](https://community.notepad-plus-plus.org/post/43733) and [this other post](https://community.notepad-plus-plus.org/post/43888).)

### `<Macros>`

When not empty, this node is made of `<Macro>` nodes, each of which represents an individual macro. Each `<Macro>` holds a non-empty list of `<Action>` tags which represent individual macro steps. These steps are either Scintilla commands or Notepad++ commands, not raw keystrokes. For more details on macro recording, see [Macros](../macros/).

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

The full list of Scintilla messages for `type=0` and `type=1` Scintilla messages, as well as a concise documentation, can be found in [Scintilla.iface](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/scintilla/include/Scintilla.iface).  More details on those messages can be found in the [Scintilla Docs](https://scintilla.org/ScintillaDoc.html).  You can use any Scintilla message that does not return a value, that passes an integer in `wParam`, and uses either an integer or string in `lParam`.  There are some messages that require strings in the `wParam`, or various data structures in one or both parameters: those will not work in a macro.  (For more on the messaging system, see [Plugin Communication](../plugin-communication/).)

The `wParam` command IDs for `type=2` Notepad++ messages can be found as the `IDM` constants in the source file [menuCmdID.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/menuCmdID.h), or you can look at the `localization\English.xml` (or your language of choice), which lists the `<Item id="...">` next to the text of the command; the value of the `id` attribute is the "command ID".

For `type=3` search-and-replace macros, see the detailed description in ["Searching > Searching actions when recorded as macros"](../searching/#searching-actions-when-recorded-as-macros).

If your automation task requires conditional execution, counters, variables, using the results of one action to influence the next, or other complex behavior, the macro system will not be sufficient for your needs: you will need a [Plugin](../plugins/): there are scripting plugins available in [Plugins Admin](../plugins/#install-using-plugins-admin) that allow automating Notepad++ with the full power of a variety of programming languages behind them, or you might find a pre-existing plugin that already accomplishes your automation task, or you could write your own plugin).

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

The run command may contain any valid command for the <abbr title="Operating System: Generally Windows.  If you use Notepad++ in a Linux WINE environment or similar, could you create a pull request clarifying whether it's windows-style command syntax or linux-style command syntax.">Windows OS</abbr>.  If you use a command that can be found in your PATH (like `cmd.exe`), then you don't need to specify the full path to the command.  If it's not in your path, then you _should_ specify the full path.  Note that Windows will launch your default browser if you put a URL in this. If the command, or one of its arguments, has an embedded space, then put quotes around it (like you would for any command line environment).  For example, `<Command name="Run Putty" ... >"c:\program files\putty\putty.exe" -ssh -load "my session"</Command>` shows the quotes around the executable and one of the arguments, because both have spaces.

There are a number of Notepad++-specific variables available, which are accessed in the form `$(VARIABLE_NAME)`, which can be used to supply portions of the command entry.

Variable            | Description                       | Example
--------------------|:---                               |:---
FULL_CURRENT_PATH   | The full path to the active file  | `E:\My Web\main\welcome.html`
CURRENT_DIRECTORY   | The active file's directory       | `E:\My Web\main`
FILE_NAME           | The active file's name            | `welcome.html`
NAME_PART           | The filename without extension    | `welcome`
EXT_PART            | The extension (with the `.`)      | `.html`
CURRENT_WORD        | the active selection in Notepad++, or the word under the cursor |
CURRENT_LINE        | the line number where the cursor is currently located in the editor window | `1`
CURRENT_LINESTR     | the text of the current line (added v8.3.2)  | `The quick brown fox jumps over the lazy dog`
CURRENT_COLUMN      | the column number where the cursor is currently located in the editor window | `5`
NPP_DIRECTORY       | the directory where the `notepad++.exe` executable is located | `c:\Program Files\notepad++`
NPP_FULL_FILE_PATH  | the full path to the `notepad++.exe` | `c:\Program Files\notepad++\notepad++.exe`

If you want access to a Windows environment variable (like `TMP`), use the standard `%`-notation for windows variables (like `%TMP%`).

## User Interface settings: `config.xml`

The following sections are defined:

1. `<GUIConfigs>`: user interface settings (usually set in the [**Settings > Preferences**](../preferences/#preferences)).
2. `<FindHistory>`: most of the latest state of the Find/Replace dialog box.
3. `<History>`: the list of recently used files.
3. `<ProjectPanels>`: associates workspace files with a given project panel

There are some non-UI options for advanced users, please check [**Preferences for Advanced Users**](../preferences/#preferences-for-advanced-users) to get more details.


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

The order of the `ext` list here determines the order of extensions in the file-type pulldowns of the Windows-common-dialogs like **Open**, **Save**, and **Save As** dialogs. When using the [old-style dialogs](../preferences/#default-directory), the automatically-added extension will be the first extension from this `ext` list.  As of v7.8.7, the new-style dialogs will also automatically add the first extension.

The `commentLine`, `commentStart`, and `commentEnd` attributes are used by the [Edit Menu](../editing/#edit-menu)'s **Comment/Uncomment** actions for adding or removing the comment syntax to the selected lines of text.  These are independent of the selected [programming **Language**](../programing-languages/)'s syntax lexer, so changing these attributes will _not_ affect what code sections will get highlighted as comments by the active syntax highlighter.  (Because of the way the Scintilla library that Notepad++ uses for the lexers, in order to change what gets highlighted as a comment, one would need to edit and re-compile the lexer for the chosen and then rebuild the Notepad++ project; in other words, it would have to be changed by the developers for a new release, not changed by the user in the `langs.xml` configuration file.)  These attributes can only define one type of line and block comments; if your language has multiple types of either, you will have to choose the _one_ type that you'd like Comment/Uncomment to work with.

## Highlighting schemes: `stylers.xml`

This file sets the color scheme for the default theme.  The other themes are stored in `themes\*.xml`, which follow the same format at `stylers.xml`.  In general, use [**Settings > Style Configurator**](../preferences/#style-configurator) for easier maintenance of styles.

Each lexer type has its own `<LexerType>` section, with multiple `<WordsStyle>` entries.  Each lexer from the **Language** menu has it's own list of available `<WordsStyle>` entries.  Trying to add a new `<WordsStyle>` to a lexer to try to get more categories of keywords will _not_ be successful, because the underlying code which does the syntax highlighting has no internal rules for mapping the entries found to that style.

If you have added user-defined keywords in the [**Settings > Style Configurator**](../preferences/#style-configurator), they will be stored as the contents of the `<WordsStyle>`, as a space-separated list (for example, `<WordsStyle>fancyKeyword1 fancyKeyword2</WordsStyle>`).

The `<WordsStyle>` `fontStyle` attribute encodes the setting of the **Bold**, **Italic**, and **Underline** checkboxes from the **Styler** dialog, using the sum of **Italic**=1, **Bold**=2, and **Underline**=4 (so something with all three checkboxes set would have `fontStyle="7"`).

The `<WordsStyle>` `colorStyle` attribute decides whether to use the defined colors from `fgColor` and `bgColor` attributes, or to use the default color setting (from **Settings > Style Configurator > Global Styles > Default Style**).  The attribute should be set to one of the following:

* No `colorStyle` attribute: this style will use both the `fgColor` and `bgColor` attributes from this `<WordsStyle>` item (standard behavior)
* Set `colorStyle="2"`: this style will inherit the foreground color from the Default style, and use the `bgColor` value as the background color (equivalent to right-clicking the foreground color in the UDL styler dialog box)
* Set `colorStyle="1"`: this style will inherit the background color from the Default style, and use the `fgColor` value as the background color (equivalent to right-clicking the background color in the UDL styler dialog box)
* Set `colorStyle="0"`: this style will inherit both the foreground and background colors from the Default style (equivalent to right-clicking both the foreground and background colors in the UDL styler dialog box)


## `Function List`

Defines what counts as a "function" for **View > Function List**.  There are some comments in the file(s), and lots of examples of the builtin languages, which you can customize.
From v7.9.1 the file structure of function list parsers have been changed, so please follow one of sections below according your Notepad++ version.

### v7.9.1 and later versions

The `functionList` folder contains a separate XML file (function list parse rule) for each language's function list capability.
Each function list parse rule links to a language with the language default name. For example the file name of php language parse rule is `php.xml`, the file name of Java language parse rule is `java.xml`, Check [overrideMap.xml](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/functionList/overrideMap.xml) for the naming list of all supported programming languages.

[overrideMap.xml](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/functionList/overrideMap.xml) is optional. When you need to override a default parser rule or to define a function list parser for your User Defined Language (UDL), you modify this file.

* Override a default parser rule examples
```
<association id= "anotherPhpParser.xml"			 langID= "1" />
<association id= "myPerlRule.xml"			 langID= "21"/>
```
If 2 above lines are in *overrideMap.xml*, function list will load your parsers `anotherPhpParser.xml` and `myPerlRule.xml` instead of loaoding `php.xml` and `perl.xml` while showing PHP and Perl function list respectively.

* Define your UDL example
```
<association id= "krl.xml"				userDefinedLangName="KRL"/>
```
Here you define a parser rule file name for your KRL UDL. While you open a file which is recognized as KRL file, then function list engin will load `functionList\krl.xml` to show the KRL function list. If you have no KRL UDL defined in your Notepad++, you have to define a dummy one (with the name "KRL") to make it work.

The `functionList\`_languagename_`.xml` parser file itself, whether it's for a builtin language or a UDL-based language, requires the structure `<NotepadPlus><functionList><parser...>...</parser></functionList></NotepadPlus>`, where the attributes and contents of the `<parser>` are described in the documents section about [How to Customize Function List](../function-list/#how-to-customize-function-list).  You can look at any of the [default parser files](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/functionList/) for examples of working Function List configurations.

### v7.9 and previous versions

The `functionList.xml` config file contains XML entries for each language's function list definition, as well as a map that tells Notepad++ which section of the XML is applied to each file type.

If you want to add **Function List** capability for your User Defined Language (UDL), you can.  You need to add two groups of information:

1. In the `<associationMap>` section, you need to add lines like the following

        <association id="fn_udl_example"          userDefinedLangName="ExampleUDL"     />
        <association id="fn_udl_example"          ext=".ex"                            />
        <association id="fn_udl_example"          ext=".exudl"                         />

    where `fn_udl_example` is a name unique to this UDL.  It is best to define it both
    based on `userDefinedLangName=...` (which must match the name you saved for your UDL) and on extension `ext=...` (which must match the extension(s) of your UDL type, with one extension per entry).

2. In the `<parsers>` section, add a parser, with a similar format to all the builtin parsers shown. An example would be

        <parser
            id="fn_udl_example"
            displayName="Example UDL Name (UDL)"
            commentExpr="((--.*?$))"
        >
            <function
                mainExpr="^[\s]*(private[\s]+)?(procedure|function)[\s]*[\w_]+"
                displayMode="$functionName"
            >
                <functionName>
                    <nameExpr expr="^[\s]*(private[\s]+)?(procedure|function)[\s]*[\w_]+" />
                </functionName>
            </function>
        </parser>

    where the `fn_udl_example` must match the `<association id>`.  The `displayName` sets what shows in the **Function List** window header.  The `...Expr` values are all defined in [regular expression syntax](../searching/#regular-expressions).

### Upgrading old Function List entries

If you previously had a v7.9-or-earlier style function list entry in `functionList.xml`, and you want to use it in a v7.9.1-or-later Notepad++, you can extract the pieces to the right locations in the new multi-file format:

1. Open the old `functionList.xml`
2. Open the `functionList\overrideMap.xml`
3. Copy the `<association...>` tag from the old `functionList.xml` to the `functionList\overrideMap.xml`, and place near the end of the `<associationMap>` section.  Make sure it follows the rules for v7.9.1-or-later `<association>` tag syntax
4. Open the `functionList\blah.xml` for your particular language
   * If you don't have `blah.xml` yet, copy one of the v7.9.1-or-newer language's XML files to `blah.xml`, and remove the whole `<parser...> ... </parser>` section
5. Copy the `<parer...>...</parser>` section from the old `functionList.xml` to the `functionList\blah.xml`
   * Please note that the `blah.xml` should _not_ contain a `<parsers>` section, _just_ the `<parser>` section.  It will cause problems with the Function List if you wrap it in the `<parsers>...</parsers>` block.  Make sure it ends up with the v7.9.1-or-newer structure described above.

## Toolbar Icon Customization: `toolbarIcons.xml`

This configuration file allows you to override the current toolbar icons.  (New to v8.4.2)  This allows you do define your own set of icons to use on the toolbar, and is useful (for example) if none of the five different icon sets available through **Settings > Preferences > General > Toolbar** are sufficient for your needs.

Aside from the `toolbarIcons.xml` file, you need to create icons.  You will populate and place the configuration file and icon files as described below:

1. Put the file `toolbarIcons.xml` (Note 1) in the main configuration folder (Note 2).
2. Create a new sub-folder called `toolbarIcons\` in that same folder.
3. Edit the file `toolbarIcons.xml`: put the icon set name you want in the `icoFolderName` attribute (Note 3).
   for example: `<ToolBarIcons icoFolderName="myAwesomeIcons" />`
4. Go into `toolbarIcons\` folder and create a new folder with the exact name of the icon set name you provided in `icoFolderName`, for example `[toolbarIcons.xml's folder]\toolbarIcons\myAwesomeIcons\`.
5. Put all your customized icons into `[toolbarIcons.xml's folder]\toolbarIcons\myAwesomeIcons\`.
6. Now it is the magic moment: Relaunch Notepad++ and you'll see your icon set instead of the default icons.
   - This overrides the icons for any of the **Settings > Preferences > General > Toolbar** icon-set selections.
   - If you have **Settings > Preferences > General > Toolbar** set to any of the three "small" choices, it will scale the icon to 16x16; if you use one of the two "large" choices, it will scale to 32x32.  So if you are going to use a "large" icon set, you should make sure the icons are defined as 32x32.
   - The [v8.4.2 release page](https://notepad-plus-plus.org/news/v842-released/) allows you to download a bundle that contains the legacy 32x32 icon set along with the necessary `toolbarIcons.xml`; unzip that bundle into the directory described on that page (equivalent to the main configuration folder [Note 2]), restart Notepad++, and you will have the old 32x32 "standard (large)" icons back.
   - Troubleshooting: if you started Notepad++ with one of the "small" choices selected but have 32x32 icons in your custom icons, it will scale them to 16x16, which is fine for small modes; but if you switch to a "large" option, it might scale the 16x16 back to 32x32 rather than using the true-32x32 from the icon file, which makes for a pixelated ("klunky") large icon: if this happens, leave it with "large" selected, then exit Notepad++ completely and restart: on the subsequent starts, it will use the full 32x32 resolution.

_Notes_:

* Note 1: The content of `toolbarIcons.xml` is as follows:
    ```xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <NotepadPlus>
        <ToolBarIcons icoFolderName="myAwesomeIcons" />
    </NotepadPlus>
    ```
    
* Note 2: This is the same folder descibed in [Configuration Files Locations](#configuration-files-location) where `config.xml` goes, and will generally be the `%APPDATA%\Notepad++\` directory, unless you are using local configuration or cloud configuration or overriding the configuration directory with `-settingsDir`.

* Note 3: If the `icoFolderName` value is an empty string, the path of icons will be `[toolbarIcons.xml's folder]\toolbarIcons\default\` folder.

### Set of Icons

For each of the 45 toolbar icons that can be customized, use the specific file name listed below.  (Some toolbar buttons have two icons, one for when the button is enabled and one when the button is disabled.)

| index |  Normal icon             |  Disabled icon                  |
|-------|--------------------------|---------------------------------|
|1      |  new.ico                 |                                 |
|2      |  open.ico                |                                 |
|3      |  save.ico                |  save_disabled.ico              |
|4      |  save-all.ico            |  save-all_disabled.ico          |
|5      |  close.ico               |                                 |
|6      |  close-all.ico           |                                 |
|7      |  print.ico               |                                 |
|8      |  cut.ico                 |  cut_disabled.ico               |
|9      |  copy.ico                |  copy_disabled.ico              |
|10     |  paste.ico               |  paste_disabled.ico             |
|11     |  undo.ico                |  undo_disabled.ico              |
|12     |  redo.ico                |  redo_disabled.ico              |
|13     |  find.ico                |                                 |
|14     |  replace.ico             |                                 |
|15     |  zoom-in.ico             |                                 |
|16     |  zoom-out.ico            |                                 |
|17     |  sync-vertical.ico       |                                 |
|18     |  sync-horizontal.ico     |                                 |
|19     |  word-wrap.ico           |                                 |
|20     |  all-chars.ico           |                                 |
|21     |  indent-guide.ico        |                                 |
|22     |  udl-dlg.ico             |                                 |
|23     |  doc-map.ico             |                                 |
|24     |  doc-list.ico            |                                 |
|25     |  function-list.ico       |                                 |
|26     |  folder-as-workspace.ico |                                 |
|27     |  monitoring.ico          |  monitoring_disabled.ico        |
|28     |  record.ico              |  record_disabled.ico            |
|29     |  stop-record.ico         |  stop-record_disabled.ico       |
|30     |  playback.ico            |  playback_disabled.ico          |
|31     |  playback-multiple.ico   |  playback-multiple_disabled.ico |
|32     |  save-macro.ico          |  save-macro_disabled.ico        |

It's not necessary to have a complete set of 45 icons in the directory: any icons not in the directory will just use the built-in icon instead.

You can have multiple icon set directories; to switch between icon sets, you just edit the `icoFolderName`, save the config file, and relaunch Notepad++.

## Other Configuration Files

* `autoCompletion\*.xml`: files for defining per-language [auto-completion](../auto-completion/#auto-completion-file-format).  This config folder _must_ go in the Notepad++ installation folder; it will not be recognized in the `%AppData%\Notepad++` hierarchy or in the cloud settings folder.

* `doLocalConf.xml`: this will only exist on local installations of Notepad++ (when you tell the installer to not use `%AppData%`, or when you install from the zipfile).  This is a zero-byte file that is just used as an indicator to `notepad++.exe` to not go looking for `%AppData%`.

* `nativeLang.xml`: if you make a selection in the [**Settings > Preferences > General > Localization**](../preferences/#general), Notepad++ will copy the appropriate `localization\*.xml` to `nativeLang.xml`.

* `session.xml`: stores the current [session](../session/) information.  Overwritten on every exit of Notepad++ if [**Settings > Preferences > Backup > Remember current session for next launch**](../preferences/#backup) is enabled.  If you want sessions that you control, use **File > Save Session...** to save it; the file is safe to edit; and you can reload that session at any time using **File > Load Session...**.

* `userDefineLang.xml`: see [the **User Defined Languages** doc](../user-defined-language-system/).

* `enableSelectFgColor.xml`: this is a zero-byte file that is just used as an indicator to the [**Settings > Style Configurator > Global Styles > Selected text colour**](../preferences/#global-styles) to honor the foreground color, not just the background color.  (Available on v8.0.0 and newer.)
