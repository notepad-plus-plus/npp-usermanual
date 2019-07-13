---
title: Preferences
weight: 100
---

Control many the aspects of Notepad++. They are divided in three main groups: Preferences, Style Configurator and Shortcut Mapper.

The Shortcut Mapper is a list of keyboard shortcuts to everything that can have one in Notepad++. Styler Configurator allows changing the visual appearance of anything that has a colour or a font. The Preferences dialog manages everything else. While there are various aspects in Notepad++ that are not configurable, you may not even notice them.

## Preferences

For the descriptions below, if it's a checkbox `☐`, the description applies if the checkbox is enabled.  (For options where the opposite behavior might not be obvious, it may also explicitly describe what the unchecked behavior is.)

### General

These affect the user interface (localization, toolbar, tab bar, and more).

* **Localization**:
    * [pulldown]: Set the lanugage for the Notepad++ user interface
* **Toolbar**:
    * `☐ Hide`: the icon-based toolbar will be hidden
    * `Small icons` / `Big icons` / `Standard icons`: will change the icon size
* **Document List Panel**:
    * `☐ Show`: will show the Doc Switcher panel, which can be used to quickly switch between documents
    * `☐ Disable extension column`: If enabled, the Doc Switcher panel will _not_ have the second column showing extensions (instead, the extension will be part of the Name column)
* **Tab Bar**:
    * `☐ Hide`: the tab bar for the open files will not be visible
    * `☐ Multi-line`: if there are enough tabs, they will wrap to a second line
    * `☐ Vertical`: have the tabs on their side on the left, rather than along the top
    * `☐ Reduce`: make the tab bar vertical region and font size smaller
    * `☐ Lock (no drag and drop)`: prevent the reordering of tabs by drag-and-drop on the tab bar (unselected, drag-and-drop on the tab bar will reorder tabs)
    * `☐ Darken inactive tags`: change the fill-colour on inactive tabs to a darker colour
    * `☐ Draw a coloured bar on active tab`: indicate the active tab by adding a coloured bar
    * `☐ Show close button on each tab`: add the close button to each tab's entry on the tab bar
    * `☐ Double click to close document`: allows double-clicking on the tab to close the file
    * `☐ Exit on close the last tab`: if the last tab is closed, Notepad++ will exit (unselected, Notepad++ instead has one new file open)
* `☐ Show status bar`: there will be a Status Bar along the bottom of the Notepad++ window, showing file type, cursor location, line-ending style, encoding, and INS/DEL mode.
* `☐ Hide menu bar (use Alt or F10 key to toggle)`: sets the main menu bar (File, Edit, Search, ...) invisible; once invisible, it can be made temporarily visible by using the Alt or F10 key

### Editing

These influence editing (carets, code-folding, line wrapping, and more).

### New Document

These define properties of new documents (end-of-line format, encoding, and syntax language).

* **Format (Line ending)**:
    * `Windows (CR LF)` / `Unix (LF)` / `Macintosh (CR)`: newly-created files will use the normal Windows-style line ending, Unix/Linux/*nix-style line ending, or old Mac-style line ending.  (Please note that modern MacOS X uses Unix-style line endings.)
* **Encoding**
    * `ANSI`: characters are represented by a single 8-bit byte, and there are only 256 available code points
    * `UTF-8`: this can encode any of the Unicode characters; it uses a single 8-bit byte for codepoints under 128, and two or more bytes for other characters
        * `☐ Apply to opened ANSI files`: if you open an ANSI file, this allows it to be "upgraded" to UTF-8
    * `UTF-8 with BOM`: this is the same as UTF-8 encoding, but saves the file with an extra Unicode character U+FEFF (which is encoded as 3 bytes in the file), which some applications use as an indication that it's a UTF-8 file
    * `UCS-2 Big Endian with BOM`: this encodes characters (even those with codepoints under 128) with exactly two bytes. "Big Endian" refers to the order the two bytes will be written to disk (with most-signficant byte first)
    * `UCS-2 Little Endian with BOM`: this encodes characters (even those with codepoints under 128) with exactly two bytes. "Little Endian" refers to the order the two bytes will be written to disk (with least-signficant byte first)
    * The final drop-down allows picking one of the old-style character sets (similar to using the main Notepad++ menu to select **Encoding > character sets ...**)
* **Default Language**: this pulldown sets whether new files will apply the styling for Normal Text, or use one of the programming-language syntax highlighting rules

### Default Directory

These affect open and save operations.

* **Default Directory**:
    * `Follow current document`: open/save dialogs will default to the current directory for the current file
    * `Remember last used directory`: open/save dialogs will remember the last directory you used in the dialog, and remain there (regardless of where the current file is located)
    * `___ ...`: this allows you to browse to a default directory, and all open/save dialogs will start in that directory
* `☐ Use new style dialog (without file extension feature & Unix style path capacity)`: Windows allows for two styles of open/save dialogs.
    * "old style" has "Quick Access", "Desktop", and others as icon-buttons along the left; it will auto-apply the selected file-type's extension to the file (so typing a filename of `blah` when a file type of "Normal text file (.txt)" is selected will save `blah.txt`); it will also allow using Unix-style backslashes as a path separator, rather than Windows-style forward slashes.
    * "new style" does not have the icon-buttons (instead, Windows presents those in the tree, similar to other drives and folders); even when a file-type is selected, the user is required to specify the desired file extension (thus the file-type selector is primarily for filtering what existing files are listed in the directory listing); and it will not understand Unix-style backslashes as path separators.
* `☐ Open all files of folder instead of launching Folder as Workspace on folder dropping`: when enabled, if you drag a folder from a Windows Explorer window, Notepad++ will open all the files individually; when disabled, Notepad++ will use the Folder as Workspace feature when you drag the folder into Notepad++

### Recent Files History

These change how the list of recent files is displayed in the File menu

### File Association

This allows associating certain file types to be always opened (by Windows double-click, and similar) by Notepad++.

Select the name of the filetype in the left column; select one of the extensions in the middle column; use the right arrow `→` to add the extension to the Registered Extensions list on the right.  (You can only do one extension at a time.)

To unregister an extension, click it in the right column, and use the left arrow `←` to remove it from the Registered Extensions column.

### Language

This affects the display of the main Language menu, and also affects the per-language tab settings.

* **Language Menu**:
    * `☐ Make language menu compact` will make submenus for languages that start with the same letter (so Perl and Python syntax highlighting would be selected through **Language > P** submenu, rather than directly from the language menu; this makes the list of items in the **Language** menu much shorter
    * `Available items ⇄ Disabled items`: by moving a language into the `Disabled items` column, it will no longer show up in the **Language** menu list
* **Tab settings**:
    * `[Default]` sets the tab behavior for the "default" condition
    * `normal` sets the tab behavior for plain text
    * other selections will choose which syntax-language the tab settings are being changed
    * `☐ Use default value`: not visible on the `[Default]` selection.  For other languages, will use the values from the `[Default]` selection for that particular language
    * `Tab size : ___`: sets the width of the tab character, or the number of spaces to use instead of a tab
    * `☐ Replace by space`: when set, hitting TAB will insert that number of spaces; when not set, TAB will insert the literal ASCII TAB character

### Highlighting

Affects highlighting of selected text.

* **Smart Highlighting**
    * `☐ Enable`: if you select a piece of text, Smart Highlighting will color all matching pieces of text.  It will use the style defined in **Style Configurator > Global Styles > Smart Highlighting**
    * `☐ Match case`: Smart Highlighting will be case-sensitive
    * `☐ Match whole word only`: Smart Highlighting will require a whole "word" (sequence of "word characters", as defined in the **Delimiter** preferences)
    * `☐ Use Find dialog settings`
    * `☐ Highlight another view`: Smart Highlighting will also apply to the other "view" (when you have documents open in both of Notepad++ view panes)
* **Highlight Matching Tags**
    * `☐ Enable`: in HTML/XML files, clicking in or highlighting in an opening or closing tag (between the angle brackets) will highlight both the opening and closing tag.  It will use the style defined in **Style Configurator > Global Styles > Tags match highlighting**
    * `☐ Highlight tag attributes`: any attributes inside the active tag will be highlighted using the style defined in **Style Configurator > Global Styles > Tags attribute**
    * `☐ Highlight comment/php/asp zone`


### Print

Affects how the text is formatted when sent to the printer

* `☐ Print line number`: will include line numbers when printed
* **Colour Options**
    * `☐ WYSIWYG`: same colours will apply to printing as you see in the editor
    * `☐ Invert`: black prints as white, light colour prints as dark, and vice versa
    * `☐ Black on White`: prints black text on white background, no highlighting
    * `☐ No background colour`: same as WYSIWYG, except no background colour is printed
* **Margin Setting (Unit:mm)**: define the page margins, in mm
* **Header and Footer**: define what will be printed in each page's header and footer sections
    * Click in one of the `Left part`, `middle part`, or `right part` for header or footer;
    * either type in text for literal text, or use the `Variable:` drop-down and `Add` button to add one of the variables at the current cursor position
        * Add **Full file name path** ⇒ `$(FULL_CURRENT_PATH)` in the input box ⇒ will print something like `c:\path\to\file.txt`
        * Add **File name** ⇒ `$(FILE_NAME)` in the input box ⇒ will print something like `file.txt`
        * Add **File directory** ⇒ `$(CURRENT_DIRECTORY)` in the input box ⇒ will print something like `c:\path\to`
        * Add **Page** ⇒ `$(CURRENT_PRINTING_PAGE)` in the input box ⇒ will print the current page number.  (Sorry, there is no total-number-of-pages variable, so you cannot do `page # of #`.)
        * Add **Short date format** ⇒ `$(SHORT_DATE)` in the input box ⇒ will print something like `m/dd/yyyy` (possibly locale-dependent)
        * Add **Long date format** ⇒ `$(LONG_DATE)` in the input box ⇒ will print something like `Day, Month ##, YYYY` (possibly locale-dependent)
        * Add **Time** ⇒ `$(TIME)` in the input box ⇒ will print something like `HH:MM AM` (possibly locale-dependent)
    * Font pulldown: use selected font for the header or footer (if left blank, use document's default font)
    * Font size pulldown: define font size for header or footer

### Backup

Defines whether or not to perform saving sessions, periodic backup, and backup on save.

* **Session snapshot and periodic backup**
    * `☐ Remember current session for next launch`: the current session is the current list of open files.  The next time you run Notepad++, it will open with that same list of files
    * `☐ Enable session snapshot and periodic backup`: this will auto-save your changed file once every N seconds to the listed directory (default to `%AppData%\Notepad++\backup\`).
        * It is not possible to select this option without `☐ Remember current session ...` also being active
        * This is also how you enable Notepad++ to remember unsaved changes
        * This will allow you to exit Notepad++ and resume, remembering changes to files that hadn't been intentionally saved
        * When you exit Notepad++ with unsaved changes, Notepad++ will _not_ ask you to save changes.  It will just keep the periodic backup file, and reload from there rather than from the normal disk location for the file
        * If you want Notepad++ to ask to you save edited files every time you close the file or exit Notepad++, do not enable this option.
        * This is _not_ a long-term backup option.
          * Every time you do a manual save, or close the file while leaving Notepad++ open, this periodic backup of the file will be deleted
          * If there is a Notepad++ crash or Windows crash, it is possible for you to lose data
* **Backup on save**
    * `☐ None`: no additional backup will be performed when the file is saved
    * `☐ Simple backup`: it will save a copy of the file, with the same name and extension, but with `.bak` appended.
    * `☐ Verbose backup`: it will save a copy of the file, with a date-and-timestamp added to the filename as well as the `.bak` extension.
        * if no `Custom Backup Directory` is defined, it will save it in `.\nppBackup\` subdirectory of the file's current directory, so `c:\path\to\file.txt` will create a backup `c:\path\to\nppBackup\file.txt.yyyy-mm-dd_hhmmss.bak`
    * `☐ Custom Backup Directory`: leave blank to put the backup in the same directory as the file; set to a directory to have all files backed up to one directory

#### Important backup information

This bears repeating: with `☐ Enable session snapshot and periodic backup` on, Notepad++ will allow you to exit with unsaved changes without asking you to save, and unless an error occurs, the next time you run Notepad++, your unsaved changes will still be there.  Notepad++ has been coded in such a way as to make this periodic backup as reliable as possible.  However, there are crashes and errors possible outside of Notepad++'s control, and there is no guarantee or warranty that your unsaved data will remain after a crash or other major system error.  Once you manually save, the periodic backup is deleted.  The builtin periodic backup should not be considered a long-term backup option, and unsaved changes in files should always be considered as volatile and unsaved.

Backup on save is the long-term backup solution built into Notepad++; simple backup will just keep one copy that matches the most recent save of the file; verbose backup keeps multiple copies with date stamps.

If you are editing mission-critical files: Always use dedicated backup software.  You may want to look into the AutoSave plugin (available through **Plugins > Plugins Admin**) for better control of automated-saving while changes are being made.  Using cloud-based folders may provide backup and/or revision history.  A dedicated revision control system, such as git or subversion, will provide control over your version history.

### Auto-Completion

Sets options for auto-completion of text, including word completion, syntax completion, and automatically pairing certain punctuation pairs and html/xml tags

### Multi-Instance

Determines whether multiple instances of Notepad++ can be run simultaneously.

* `☐ Open session in a new instance of Notepad++`: each session will open in a new instance, but multiple files can be opened in each session
* `☐ Always in multi-instance mode`: every time you open a file from Windows, it will open a new instance of Notepad++
* `☐ Default (mono-instance)`: every time you open a file from Windows, it will go into the single Notepad++ instance

**WARNING**: If you select anything other than `Default (mono-instance)`, changed settings in one instance will _not_ influence the settings in the other instance, and only the changed settings in the _last_ instance closed will be saved to disk.

### Delimiter

Sets the characters that are considered part of a "word" for quick selections using double-click and similar

### Cloud

Allows saving your settings to the cloud instead of in the normal `%AppData%` or program-install folders.

### Search Engine

Set your search engine for "Search on Internet" command

### MISC.

A variety of settings that didn't fit elsewhere

## Style Configurator

The Style Configurator dialog has three regions: Select theme, language and style selection lists, and the style defition.

The "Select theme:" pulldown allows you to select which theme you want.  [Themes](../themes/_index.en.md) are pre-defined sets of formatting rules, which often try to use a consistent color scheme between languages.

The "Language:" selection list lets you select whether you want to set the formatting for "Global Styles", or a specific [programming language](../programming-languages/_index.en.md) that you want to set the highlighting for.  The "Style:" selection list lets you select which highlighting rule for the given language.  On all but "Language: Global Styles", there will also be a "Default ext." box, which is an un-editable list of the default file extensions associated with that Language; and the "User ext." box, where you can add a user-defined list of additional extensions (space separated, don't use the . in the extension), which says which other extensions you want to apply this language's formatting to.  There is no specific entry called "Normal text" or "Plain text": to edit the colors for a plain text file (like `.txt`), use the "Global Styles" language.

The final section will reiterate which language and style are selected, and allow you to set colors and fonts.  The Colour Style allows you to choose the Foreground or Background colour by clicking on the colored box.  The Font Style allows you to pick the font, size, and bold/italic/underline settings (if Font name or Font size are left blank, they will inherit from the Global Styles: Default Style.  Under the "Language: Global Styles" with "Style: Global override", there are also a series of checkboxes for "Enable global xxx", which will mean that Notepad++ will use the Global override setting for that attribute, rather than using the per-language styling settings for that attribute.

Some language/style combinations (like Perl > INSTRUCTION WORD) will additionally have a list of default keywords (not editable) and user-defined keywords (which allow you to add new keywords to apply this style to).

The Save & Close button will save the settings and close the dialog.  The Cancel button will exit the dialog without updating the style settings.  The Transparency checkbox will allow you apply transparency to the Style Configurator dialog box.

### Configuration file: `stylers.xml`

If you prefer to edit XML instead of using the GUI, you may use the `stylers.xml` configuration file to edit the default theme, or `themes\blah.xml` to edit theme "blah".

The `<LexerStyles>` contains a `<LexerType>` for each programming language -- where the `desc=` attribute matches the name in the list of Languages from the GUI.  Each of those contains one or more `<WordsStyle>` tags, where teh `Name=` attribute matches the entries in the GUI's list of Styles for that language; the WordsStyle are usually empty tags (`<WordsStyle .../>`), but can contain values (`<WordsStyle...>user1 user2 ...</WordsStyle>`) if there is an associated list of user-defined keywords for that style.  There is also a `<GlobalStyles>` section, with `<WidgetStyle>` entries, corresponding to the elements of the "Global Styles" in the GUI.

### Common Syntax Highlighting Problems

If you find that when a particular programming language is selected from the Languages menu, but no syntax highlighting is applied, check which theme you are using in the Style Configurator dialog.  If your selected them does not include settings for a given programming language, it cannot apply the highlighting.  You can edit the theme's XML file, pasting in the appropriate `<LexerType>` from a different theme (or the default `stylers.xml`) into your theme file; save the file, exit and reload Notepad++; now, the language should be listed in your theme's Style Configurator languages list, and you should be able to set the colors to match the other languages in your theme.

If you change a color in your Style Configurator, but the color doesn't change in the editor, it may be that you don't have the right language lexer selected: in the main Notepad++ window, the lower-left of the status bar will list the active lexer, or you can check the Language menu for which entry has the `•` to indicate it's selected.

## Shortcut Mapper

The Shortcut Mapper dialog presents five tabs:
1. `Main menu`: used for items in the main Notepad++ menu items, like File, Edit, Search, View, Encoding, Language, Settings, Run, and ? (Help/About) menus.
2. `Macros`: used for items in the Macros menu
3. `Run commands`: used for user-added items in the Run menu.  (The **Run...** menu entry shortcut is defined in the `Main Menu` tab)
4. `Plugin commands`: used for actions from the Plugins menu.
5. `Scintilla commands`: used for all the Scintilla actions, thus allowing editing of shortcuts for all the editor commands.

Each tab consists of an area for selecting the command to shortcut, a message area, a Filter input, and buttons to Modify, Clear, Delete, and Close.

When selecting the command, there are generally two columns: Name and Shortcut.  The Name matches the menu item (or the name of the Scintilla message).  The Shortcut shows the current-assigned shortcut (if any).  The `Main menu` tab has an additional Category column, which tells which menu category the command falls under.  The `Plugin commands` tab has an additional Plugin column, which tells which plugin DLL the shortcut applies to.

The message area will tell you if there are "no shortcut conflicts for this item" (when the shortcut for the selected action is not used anywhere else; or it will give you the name of the tab, followed by the Name for the action, which uses the same shortcut as the currently-selected action.

The Filter input allows you to enter a piece of literal text, and it will filter all the Names in the active tab for a given text substring, only listing the Names that contain that literal substring, ignoring case.  There are no regular expression or wildcard syntax interpretations in the Filter.

Use the Modify button to edit the existing shortcut or to create a shortcut for an entry that has none.  The resulting dialog will show the Name of the active action.  There are checkboxes to enable the CTRL, ALT, and SHIFT key-modifiers.  The main key in the shortcut is defined by the pulldown menu.  Hitting OK will apply the added or changed shortcut and leave the dialog.  Cancel will undo your changes and leave the dialog.  (Please note that if you are using some localizations, the key you select [might not match](https://notepad-plus-plus.org/community/topic/17679/using-caret-circumflex-key-for-a-shortcut/10) <!-- TODO = this link should really refer to a submitted issue request, rather than a forum-topic --> what key you type: whatever key in your locale uses the same keycode as the standard US english keyboard will be the actual key.)  In the `Scintilla commands` tab, you can actually assign more than one shortcut to a given Scintilla command, so there is an extra pane listing existing shortcuts, and additional Add and Remove buttons.

Use the Clear button to remove the existing shortcut for a given entry.

The Delete button is usually disabled.  However, in the `Macros` and `Run commands` menu, the Delete button will be enabled, and it will remove the selected entry from the menu -- so it will not only not have a shortcut, but it won't be in the menu the next time you run Notepad++.

The Close button will close the dialog box.

### Configuration file: `shortcuts.xml`

If you prefer to edit XML instead of using the GUI to modify shortcuts, you may edit the `shortcuts.xml` file.  The keyboard shortcuts are defined as attributes of the `<Macro>`, `<Command>`, `<PluginCommand>`, and `<ScintKey>` tags.  The `Key=` attribute is the decimal value for the keycode associated with the key you want to hit.  The `Ctrl=`, `Alt=`, `Shift=` attributes have values of either "yes" or "no", and either enable or disable the modifier for that key.

### Common Shortcut Mapper Problems

With the introduction of the message area<!-- TODO: "in v7.5.xxx" or whenever it was introduced -->, it is easy to see when a conflict exists between shortcuts.  All you have to do is pick the entry that you _don't_ want to use the conflicted shortcut, and either Clear or Modify the shortcut so there is no longer a conflict.