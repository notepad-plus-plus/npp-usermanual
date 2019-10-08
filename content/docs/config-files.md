---
title: Configuration Files Syntax
linktitle: config-files
weight: 115
---

# Syntax for the XML-based Configuration Files

Notepad++ offers a comprehensive user interface to review or change most of its settings. However, there are some special cases where it is worthwhile to edit the configuration files directly, including:

* Customizing the Context Menu
* Editing previously-recorded macros, or crafting new macros manually
* Adding keywords to a language, because the new language version isn't matched yet

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


## User Interface settings: `config.xml`

The following sections are defined:

1. `<GUIConfigs>`: user interface settings (usually set in the [**Settings > Preferences**](../preferences/#preferences).
2. `<FindHistory>`: most of the latest state of the Find/Replace dialog box.
3. `<History>`: the list of recently used files.
3. `<ProjectPanels>`: associates workspace files with a given project panel


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
2  | message  |  integer  | `0` if type=2, otherwise use the message id.
3  | wParam  |  integer  |  Command id when type=2 or type=3, else actual first parameter of the message. Use `0` if the message or command doesn't require a wParam used.
4  | lParam  |  integer |  `0` unless type=0 and the second parameter of the message is actually used, or scalar value used when type=3.
5  | sParam  |  string  |  `""` unless type=1 or type=3, in which case this is the string pointed by the second parameter of the message

The full list of Scintilla messages for `type=0` and `type=1`, as well as a concise documentation, can be found in [Scintilla.iface](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/scintilla/include/Scintilla.iface).  More details on those messages can be found in the [Scintilla Docs](https://scintilla.org/ScintillaDoc.html).

The `wParam` command IDs for `type=1` can be found as the `IDM` constants in the source file [menuCmdID.h](https://github.com/notepad-plus-plus/notepad-plus-plus/trunk/PowerEditor/src/menuCmdID.h), or you can look at the `localization\English.xml` (or your language of choice), which lists the `<Item id="...">` next to the text of the command; the value of the `id` attribute is the "command ID".

You can use any Scintilla or Windows message that does not return a value, that passes an integer in wParam, and either an integer or string in lParam.  There are some messages that require strings in the wParam, or various data structures; those will not work in a macro.

For more on the messaging system, see [Plugin Communication](../plugin-communication/).

For type=3 search-and-replace macros, see the detailed description in ["Searching > Searching actions when recorded as macros"](../searching/#searching-actions-when-recorded-as-macros).

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

The run command is any valid command for the <abbr title="Operating System: Generally Windows.  If you use Notepad++ in a Linux WINE environment or similar, could you create a pull request clarifying whether it's windows-style command syntax or linux-style command syntax.">Windows OS</abbr>.  Thus, if you enter a URL, Windows will launch your default browser with that URL.
The commands use the same syntax and helper environment variables as explained in [TBD](#404-Not-Found "TBD: was External Programs NppWiki++ page; need to incorporate that in the new docset").  Use the concatenation characters as appropriate to have the OS execute several commands in a row.

# PETER HERE #

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

