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
    * [pulldown]: Set the language for the Notepad++ user interface.
        * This copies one of the XML files from the `localization` folder to `nativeLang.xml`.
        * _NOTE_: After upgrading to a new version of Notepad++, you may need to refresh the `nativeLang.xml`: change the **Localization** to another language, then change it back immediately to your preferred language.
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

* **Caret Settings**: sets the width (in pixels) of the typing caret, as well as how fast it blinks
* **Multi-Editing Settings**: allows multiple selections not necessarily contiguous with each other by using Ctrl+Mouse click on the selection(s)
* **Folder Margin Style**: if the active Language lexer allows for code folding, these determine
    * `☐ simple`: shows a `-` if that section is not folded, or a `+` if it is.
    * `☐ arrow`: shows a `▼` if that section is not folded, or a `▶` if it is.
    * `☐ circle tree`: shows a `⊖` with a line to the end of the section if that section is not folded, or a `⊕` if it is folded
    * `☐ box tree`: shows a `⊟` with a line to the end of the section if that section is not folded, or a `⊞` if it is folded
* **Vertical Edge Settings**
    * This will allow one or more vertical edges to be displayed while editing your file, to help with line lengths or positioning text.  This edge indicator can either be a vertical line, or a background shading beyond the edge.  The colour of the line or background shading will be taken from **Settings > Style Configurator > Global Styles > Edge Color: Forground colour**.
    * Multiple Vertical Edges: There is one box, which accepts zero or more numbers (as of v7.8.6):
        * If the box is empty, there are no vertical edges.
        * If there is one number ℕ in the box, there will be one vertical edge, after the column for the ℕth character.
        * If there is more than one number (separated by whitespace), then there will be a vertical edge at each of the given character columns.
        * `☐ Background mode`: the vertical edge is usually a vertical line; if this option is enabled, the vertical edge will be indicated by styling the _background_ of the text to the right of the edge.
    * Single Vertical Edge: in older versions of Notepad++, there was only a single vertical edge available, with more toggled options (v7.8.5 and earlier):
        * `☐ Show vertical edge`: shows a vertical edge at the specified location, often used to indicate the right margin for manually setting the number of characters per line
        * `☐ Line mode`: the vertical edge is indicated by a solid vertical line
        * `☐ Background mode`: the vertical edge is indicated by styling the _background_ of the text to the right of the edge
        * `Number of columns: __ `: sets where the vertical edge will be, in numbers of columns (characters) from the left edge of the page
* **Border Width**
    * [number-slider]: sets the width (in pixels) of the border around each view's text editor; technically, it's the gap between the light and dark portions of the sunken border, so a width of 0 will still have the light and dark lines for the sunken edge
    * `☐ No edge`: will remove the entire border, including the light and dark bars, so it no longer appears sunken
* **Line Wrap**: sets how lines will be wrapped (when **View > Word Wrap** is enabled)
    * `☐ Default`: wraps from the last visible column to the first visible column column
    * `☐ Aligned`: wraps from the last visible column to the same indent as the start of the unwrapped line
    * `☐ Indent`: wraps from the last visible column to the next level of indent compared to the start of the unwrapped line
* `☐ Display line number`: shows the line numbers to the left of the text
* `☐ Display bookmark`: shows a large shaded circle next to all rows that contain a bookmark
* `☐ Enable current line highlighting`: will change the styling of the current line of text to **Settings > Style Configurator > Global Styles > Current line background color** style's `Background colour` (ignoring the `Foreground colour` for that style)
* `☐ Enable smooth font`: enables a font-smoothing algorithm from Windows, which may affect how smooth fonts are on some displays
* `☐ Enable scrolling beyond last line`: allows you to scroll (with scroll bar or mouse wheel) so that up to a page of blank space _after_ the last line is visible.  (Disabled, scrolling to the end will put the last line of text as the bottom line in the window, when there are more lines of text than are visible in the window)
* `☐ Disable advanced scrolling feature (if you have touchpad problem)`: designed to help if you have a problem with your touchpad

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
    * "old style" has "Quick Access", "Desktop", and others as icon-buttons along the left; it will also allow using Unix-style backslashes as a path separator, rather than Windows-style forward slashes; it will auto-apply the selected file-type's extension to the file (so typing a filename of `blah` when a file type of "Normal text file (.txt)" is selected will save `blah.txt`).
    * "new style" does not have the icon-buttons (instead, Windows presents those in the tree, similar to other drives and folders); it will not understand Unix-style backslashes as path separators; in older Notepad++ versions, even when a file-type is selected in the new-style dialog, the user was required to specify the desired file extension, but as of Notepad++ v7.8.7, extensions will be automatically added based on the selected file type.
* `☐ Open all files of folder instead of launching Folder as Workspace on folder dropping`: when enabled, if you drag a folder from a Windows Explorer window, Notepad++ will open all the files individually; when disabled, Notepad++ will use the Folder as Workspace feature when you drag the folder into Notepad++

### Recent Files History

These change how the list of recent files (also known as the Most Recently Used list, or "MRU") is displayed in the File menu

* `☐ Don't check at launch time`: will skip checking whether files in the MRU exist at launch time.
    * this is useful if you have files on a network drive which intermittently isn't visible, and want files to remain in the MRU
    * this is also useful if you like knowing what files were previously edited, even after you've deleted those files from the folder
* `Max number of entries`: show the _n_ most recent files in the list
* `☐ In Submenu`: will show the recent files in a "Recent Files" submenu of the File menu, rather than directly in the file menu
* `☐ Only File Name`: will show just the file name, without the drive or path
* `☐ Full File Name Path`: will show the full path, including drive, path, and file name
* `☐ Customize Maximum Length`: will only list the first _n_ characters from the full file path

### File Association

This allows associating certain file types to be always opened (by Windows double-click, and similar) by Notepad++.

Select the name of the filetype in the left column; select one of the extensions in the middle column; use the right arrow `→` to add the extension to the Registered Extensions list on the right.  (You can only do one extension at a time.)

To unregister an extension, click it in the right column, and use the left arrow `←` to remove it from the Registered Extensions column.

**Note**: For this section to work, please run Notepad++ in Administrator mode, since it is modifying the registry.

### Language

This affects the display of the main Language menu, and also affects the per-language tab settings.

* **Language Menu**:
    * `☐ Make language menu compact` will make submenus for languages that start with the same letter
        * Under normal circumstances, this makes the list of items in the **Language** menu much shorter: the standard 80+ languages will be reduced to about 20 submenus and a few standalone **Language** menu entries
        * For example, Perl and Python syntax highlighting would be selected through **Language&nbsp;>&nbsp;P** submenu, rather than directly from the language menu
    * `Available items ⇄ Disabled items`: by moving a language into the `Disabled items` column, it will no longer show up in the **Language** menu list
        * If you have moved items to Disabled Items _and_ have enabled `☑ Make language menu compact`, there may end up being empty letter-based subfolders in the **Language Menu**
* **Tab settings**:
    * `[Default]` sets the tab behavior for the "default" condition
    * `normal` sets the tab behavior for plain text
    * other selections will choose which syntax-language the tab settings are being changed
    * `☐ Use default value`: not visible on the `[Default]` selection.  For other languages, will use the values from the `[Default]` selection for that particular language
    * `Tab size : ___`: sets the width of the tab character, or the number of spaces to use instead of a tab
    * `☐ Replace by space`: when set, hitting TAB will insert that number of spaces; when not set, TAB will insert the literal ASCII TAB character
* `☐ Treat backslash as escape character for SQL`: this affects the **Language > SQL** handling of the `\` backslash character
    (Note: this option moved from [MISC Preferences](#misc) in v7.8.1)

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

Sets options for [auto-completion](../auto-completion/) of text, including word completion, syntax completion, and automatically pairing certain punctuation pairs and html/xml tags.

* **Auto-Completion**
    * `☐ Enable auto-completion on each input`: a dropdown selection will appear as you type; arrow keys will select various choices, TAB or ENTER will accept a choice, ESC will cancel auto-completion
        * `☐ Function completion`: will auto-complete function names only
        * `☐ Word completion`: will auto-complete words only
        * `☐ Function and word completion`: will auto-complete both function names and words
        * `From the _n_th character`: must type at least _n_ characters before the auto
            * if `☐ Enable auto-completion on each input` is disabled, the _n_th character will be disabled (greyed out)
        * `☐ Ignore numbers`: won't try to auto-complete when typing numbers
    * `☐ Function parameters hint on input`: for applicable programming languages, will provide hints on what to type in a function parameter list
* **Auto-Insert**
    * Will automatically insert the closing item for any of the enabled default pairs, or the three manually-chosen matched pairs
        * `☐ ()`
        * `☐ []`
        * `☐ {}`
        * `☐ ""`
        * `☐ ''`
        * `☐ html/xml close tag`
        * `Matched pair [1,2,3]: __ __`: define the open and close character(s) for three user-defined pairs
* `☐ Auto-indent`: when making a new line, automatically indent (following TAB or space settings for the active Language) based on the indent of the previous line
    (note: this setting was in the [MISC preferences](#misc) prior to v7.8.3)

### Multi-Instance

Determines whether multiple instances of Notepad++ can be run simultaneously.

* `☐ Open session in a new instance of Notepad++`: each session will open in a new instance, but multiple files can be opened in each session.  "Opening a session" can be done either by using **File > Load session...**, or (if you have set the [MISC > Session File ext](#misc)) by opening a file with that extension.
* `☐ Always in multi-instance mode`: every time you open a file from Windows, it will open a new instance of Notepad++
* `☐ Default (mono-instance)`: every time you open a file from Windows, it will go into the single Notepad++ instance.  If you open a session file while Notepad++ is already open, the files from that session will be opened in addition to the files you already have open.

**WARNING**: If you select anything other than `Default (mono-instance)`, changed settings in one instance will _not_ influence the settings in the other instance, and only the changed settings in the _last_ instance closed will be saved to disk.

### Delimiter

Sets the characters that are considered part of a "word" for quick selections using double-click, [Smart Highlighting](#highlighting), or the "match whole word only" in a normal search expression.  It is also used for [auto-completion](../auto-completion/#create-auto-completion-definition-files).  This setting does _not_ affect a [regular expression](../searching/#regular-expressions)'s interpretation of a word character or word boundary.

* **Word character list**
    * `☐ Use default Word character list as it is`: for Smart Highlighting (see above) or the Normal search mode in the Find and Replace dialogs, will use the normal alphanumeric rules for determining what constitutes a word for "Match Whole Word Only"
        * The default "word characters" inlcude anything that Unicode considers alphanumeric, plus the underscore "_" character.
            * Includes: standard Latin characters, accented characters, letterlike symbols, superscript digits, and enclosed (circled) digits
            * Excludes: punctuation, mathematical operators, box drawing, arrows, emoji, or other such sybols.
    * `☐ Add your character as part of word`: sometimes, the default "word character list" isn't sufficient for you; if you want other characters to be considered in "whole word only", add them here
        * The value should be a string consisting of all the additional characters you would like to be included as a "word character".
        * Spaces are liable to cause problems, and are not recommended to be present in this entry.  If you try to add a space, the dialog box will show a warning message.
* **Delimiter selection settings**
    * If you define open and close characters, Ctrl + MouseDoubleClick will select everything inside that delimiter pair
    * `☐ Allow on several lines`: Ctrl + MouseDoubleClick will work across multiple lines, instead of just on a single line

### Cloud

Allows saving your settings to the cloud instead of in the normal `%AppData%` or program-install folders.
* `☐ No Cloud`: saves settings in the normal location
* `☐ Set your cloud location path here`: settings will go in the given directory, which is assumed to be in a folder that's synced to your cloud-provider


### Search Engine

Set your search engine for "Search on Internet" command (found in the **Edit > On Selection** menu, or in the right-click context menu).  It will search for the word under the cursor (or for the whole selection, if a selection is made).

If you want to specify a search engine not listed, type the full URL, with the text `$(CURRENT_WORD)` as the placeholder for the search term (as shown in the example in the Preferences dialog box)

### MISC.

A variety of settings that didn't fit elsewhere

* **Document Switcher**
    * `☐ Enable`: hitting Ctrl+TAB will allow you to easily switch through all the open documents
    * `☐ Enable MRU behavior`: it will default to selecting the most-recently-used file (or "MRU", for short) in the Ctrl+TAB list
* **Document Peeker**
    * `☐ Peek on tab`: if you hover over an inactive tab, it will give you a tiny "peek" at the document (a ultra-tiny font preview, similar to the document map), in a small popup near the tab bar
    * `☐ Peek on document map`: if you hover over an inactive tab, it will change the Document Map (**View > Document Map**) pane to show the preview of that tab, rather than of the active document
* **Clickable Link Settings**
    * `☐ Enable`: text that appears to be a URL will allow you to double-click to open that URL in your default browser.  When you hover over the URL, it will change to the style defined in **Style Configurator > Global Styles > URL hovered**
    * `☐ No underline`: will remove the underline normally present on a link
* **File Status Auto-Detection**
    * [dropdown]
        * `Enable`: for the active file only, will check periodically to see if the file has been updated on disk, and will prompt to ask if you want to reload the file from the disk, or keep the version that's currently in Notepad++
        * `Enable for all open files`: for all active files, check periodically to see if the file has been updated on disk
        * `Disable`: will not check to see if the file has been updated on disk
    * `☐ Update silently`: instead of prompting, will automatically reload the file from disk
    * `☐ Scroll to the last line after update`: will scroll to the end of the file after reloading from disk (otherwise, the cursor and scrolled-location stays where it was before the update)
* `☐ Autodetect character encoding`: when opening a new file, try to algorithmically determine what character encoding should be used
* `☐ Minimize to system tray`: place the Notepad++ icon on the system tray (instead of the task bar) when the Notepad++ window is minimized
* `☐ Show only filename in title bar`: use just the file name (instead of the full path) of the active file in the Notepad++ title bar
* `☐ Enable Notepad++ auto-updater`: will automatically download updates from the official website, once the development team has decided it's time to push an update to users.  If disabled, you will have to manually download the installer from the official website yourself.
* `☐ Don't fill find field in Find dialog with selected word`: when enabled, **Find** command will _not_ replace the **Find What** text with the currently-selected text; when disabled (default), the **Find What** text _will_ be replaced (added v7.8.3)
* `☐ Use Monospaced font in Find dialog (Need to restart Notepad++)`: changes the font from standard proportional font to a monospaced font in the text boxes in the **Find** dialog; requires restarting Notepad++ to change (added v7.8.1)
* `Session file ext.`: populate with a file extension (without the `.`).  When you open a file with this extension (whether from Windows file associations, or from the Notepad++ **File > Open** or similar), Notepad++ will treat the file as a session file, and open the files from that session, rather than showing and editing the contents of the file.  This will honor the [Multi-Instance](#multi-instance) settings.
* `Workspace file ext.`: populate with a file extension (without the `.`).  When you open a file with this extension (whether from Windows file associations, or from the Notepad++ **File > Open** or similar), Notepad++ will treat the file as a workspace file, and open that workspace, rather than showing and editing the contents of the file.  This will honor the [Multi-Instance](#multi-instance) settings.

## Style Configurator

The Style Configurator dialog has three regions: Select theme, language and style selection lists, and the style defition.

The "Select theme:" pulldown allows you to select which theme you want.  [Themes](../themes/_index.en.md) are pre-defined sets of formatting rules, which often try to use a consistent color scheme between languages.

The "Language:" selection list lets you select whether you want to set the formatting for "Global Styles", or a specific [programming language](../programming-languages/_index.en.md) that you want to set the highlighting for.  The "Style:" selection list lets you select which highlighting rule for the given language.  On all but "Language: Global Styles", there will also be a "Default ext." box, which is an un-editable list of the default file extensions associated with that Language; and the "User ext." box, where you can add a user-defined list of additional extensions (space separated, don't use the . in the extension), which says which other extensions you want to apply this language's formatting to.  There is no specific entry called "Normal text" or "Plain text": to edit the colors for a plain text file (like `.txt`), use the "Global Styles" language.

The final section will reiterate which language and style are selected, and allow you to set colors and fonts.  The Colour Style allows you to choose the Foreground or Background colour by clicking on the colored box.  The Font Style allows you to pick the font, size, and bold/italic/underline settings.  If Font name or Font size are left blank, they will inherit from the Global Styles: Default Style.  If you right-click a colour, you will see diagonal stripes across the colour, indicating it is set to "inherit", meaning that it will take that colour from the Default Style.  Under the "Language: Global Styles" with "Style: Global override", there are also a series of checkboxes for "Enable global xxx", which will mean that Notepad++ will use the Global override setting for that attribute, rather than using the per-language styling settings for that attribute.

Some language/style combinations (like Perl > INSTRUCTION WORD) will additionally have a list of default keywords (not editable) and user-defined keywords (which allow you to add new keywords to apply this style to).

The Save & Close button will save the settings and close the dialog.  The Cancel button will exit the dialog without updating the style settings.  The Transparency checkbox will allow you apply transparency to the Style Configurator dialog box.

### Global Styles

Unlike most of the other items listed in the "Languages" column, which are language or file-type specific, the "Global Styles" set the default stylings for all types of documents using the active theme.  Except for the "Global override" style, a style for a particular language will override a "Global Style" setting.

Some of these styles apply to the background only, some apply to the foreground only, and some apply to both.  <!-- For styles that only have one available colour, the other will be disabled (greyed out). -->

* Global override [background and foreground] ⇒ This style has a series of checkboxes, which allow you to choose which attributes of the override-style will apply to everything; any that are enabled will override even the per-language settings; any that are not enabled will not use the global-override settings for that attribute.
* Default style [background and foreground] ⇒ This sets the base font and colours for all languages -- so any unstyled text will use these settings.
* Indent guideline style [background and foreground] ⇒ If **View > Show Symbol > Show Indent Guide** is enabled, there will be a thin dotted line every for every level of indent.  The foreground sets the colour of the dots; the background sets the colour of the non-dot portion.
* Brace highlight style [background and foreground] ⇒ If you have text like `( blah )` or `[ blah ]` or `{ blah }` and move the cursor onto one of the opening or closing parentheses, brackets, or braces, both the opening and closing character in the pair will be highlighted per this style.
* Bad brace colour [background and foreground] ⇒ If you have a single unmatched or mismatched parenthesis `()`, bracket `[]`, or curly-brace `{}`, with the cursor at that character, it will be highlighted as a "bad brace style" instead of using the "brace highlight style".
* Current line background colour [background only] ⇒ The line containing the active editing cursor will be marked using this background style.
* Selected text colour [background only] ⇒ Selected text will be indicated with this background. If [Preferences > Highlighting > Smart Highlighting](#highlighting) is enabled, the "Smart Highlighting" style (below) will be coloured overtop of the "Selected Text Colour".
* Caret colour [foreground only] ⇒ This sets the colour for the current-text-position cursor ("caret"), which will either be `|` for insert mode or `_` for overwrite mode.
* Edge colour [foreground only] ⇒ Colour for the vertical edge from [Preferences > Editing](#editing).  If the Vertical Edge Settings are enabled as Background Mode, this style's "foreground" colour will be used as the background colour for text that's beyond the edge.
* Line number margin [background and foreground] ⇒ If "Display line number" is enabled in [Preferences > Editing](#editing), this sets the style for those line numbers.
* Fold [background and foreground] ⇒ If a given language has folding, this will give the colour for the folding symbols (`⊞ ⊟ │ └`) when the cursor is _not_ inside that folding-area
* Fold active [foreground only] ⇒ If a given language has folding, this will give the colour for the folding symbols (`⊞ ⊟ │ └`) when the cursor _is_ inside that folding-area
* Fold margin [background and foreground] ⇒ If a given language has folding, this will give the colours for the margin-region; it will be coloured with a checkerboard-like pattern (a dense version of `░`)
* White space symbol [foreground only] ⇒ If **View > Show Symbol** settings have whitespace shown, then the tabs and whitespace symbols will use this foreground colour.
* Smart Highlighting [background only] ⇒ If [Smart Highlighting](#highlighting) is enabled and active, this colour will be applied to all matches.  This background colour has approximately 60% transparency compared to other backgrounds also applied on the same text, so the exact colour seen will depend on other styles for this text, combined with this setting.  (For example, if you have a highlight of green RGB=[0,255,0], with a white RGB=[255,255,255] background, the actual colour will be RGB=[155,255,155].)
* Find Mark Style [background only] ⇒ If you have used the **Search > Mark** dialog to mark text, this style will be applied to the background.  Like the "Smart Highlighting" style, this background has about 60% transparency, so the exact colour seen will depend on other styles for this text, combined with this setting.
* Mark Style 1 [background only] ⇒ If you select text, then use **Search > Mark All > Using 1st Style**, it will use this background colour for all text matching the current selection.
* Mark Style 2 [background only] ⇒ If you select text, then use **Search > Mark All > Using 2nd Style**, it will use this background colour for all text matching the current selection.
* Mark Style 3 [background only] ⇒ If you select text, then use **Search > Mark All > Using 3rd Style**, it will use this background colour for all text matching the current selection.
* Mark Style 4 [background only] ⇒ If you select text, then use **Search > Mark All > Using 4th Style**, it will use this background colour for all text matching the current selection.
* Mark Style 5 [background only] ⇒ If you select text, then use **Search > Mark All > Using 5th Style**, it will use this background colour for all text matching the current selection.
* Incremental highlighting all [background only] ⇒ If you use the "Highlight all" feature of the **Search > Incremental Search**, the results will be coloured based on this style.
* Tags match highlighting [background only] ⇒ If [Preferences > Highlighting > Highlight Matching Tags](#highlighting) is enabled, this background colour will be used for the opening and closing HTML/XML tags.
* Tag attribute [background only] ⇒ If [Preferences > Highlighting > Highlight Matching Tags](#highlighting) is enabled, this background colour will be used for attributes inside the HTML/XML tags.
* Active tab focused indicator [foreground only] ⇒  If [Preferences > General > Draw a coloured bar on active tab](#highlighting) is enabled, this foreground colour will be used for drawing a thick bar along the long edge of the tab name of the active tab in the active view, to emphasize active tab
* Active tab unfocused indicator [foreground only] ⇒ If [Preferences > General > Draw a coloured bar on active tab](#highlighting) is enabled, and if both editor views are visible, this foreground colour will be used for drawing a thick bar along the long edge of the tab name of the other inactive view's active tab.
* Active tab text [foreground only] ⇒ Selects the colour to be used for the filename displayed in the titlebar of the active tab.
* Inactive tabs [background and foreground] ⇒ Selects the colour to be used for the filename displayed in the titlebars of all inactive tabs.
* URL hovered [foreground only] ⇒ If [Preferences > MISC. > Clickable Link](#misc) is enabled, when your cursor is hovering over a URL, the URL's foreground colour will follow this setting.

### Search result styles

The "Search result" styles is another set of styles which are not language or file-type specific.  Instead, they are the styles that are applied in the **Search > Search Results Window**.

Some of these styles apply to the background only, some apply to the foreground only, and some apply to both.

* Search Header [background and foreground] ⇒ The first line of every group of search results tells what the search term was used, how many matches there were, and how many of the searched files contain matches are listed in this style.
* File Header [background and foreground] ⇒ For each file in a group of search results, the file name and how many matches were in that file are listed in this style.
* Line Number [background and foreground] ⇒ For each line with a match, the line number of that match will be formatted according to this style.
* Hit Word [background and foreground] ⇒ The matching word will be formatted using this style inside the search results.
* Selected Line [background and foreground] ⇒ <!-- This appears to not affect things in v7.7.1; should this be filed as a bug; this was discussed in a recent forum post, though I cannot find it right now -->
* Current line background [background only] ⇒ As you click on lines in the search results window, this style will be used to set the background colour of the search-result-window line that was clicked.

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

With the introduction of the message area, it is easy to see when a conflict exists between shortcuts.  All you have to do is pick the entry that you _don't_ want to use the conflicted shortcut, and either Clear or Modify the shortcut so there is no longer a conflict.
