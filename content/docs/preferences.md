---
title: Preferences
weight: 100
---

There are three main dialogs for editing preferences and other user-defined settings: [Preferences](#Preferences), [Style Configurator](#style-configurator) and [Shortcut Mapper](#shortcut-mapper).  The Shortcut Mapper is a list of keyboard shortcuts to everything that can have one in Notepad++. Styler Configurator allows changing the visual appearance of anything that has a colour or a font. The Preferences dialog manages most other user-settings.  While there are various aspects in Notepad++ that are not configurable, you may not even notice them.

For settings not covered by the three main dialogs, there are [other toggles and settings](#other-toggles-and-settings) which can be found in various dialogs, menus, and configuration files.

As noted in the [Configuration Files](../config-files) documentation, Notepad++ writes the configuration files when it exits, which means that, when you make a change using Notepad++ menus and dialogs described below, your change will _not_ be written to the configuration file until Notepad++ exits.

## Preferences

For the descriptions below, if it's a checkbox `☐`, the description applies if the checkbox is enabled.  (For options where the opposite behavior might not be obvious, it may also explicitly describe what the unchecked behavior is.)

### General

These affect the user interface (localization, toolbar, tab bar, and more).

* **Localization**:
    * [pulldown]: Set the language for the Notepad++ user interface.
        * This copies one of the XML files from the `localization\` folder to `nativeLang.xml`.
        * To make changes to your localization, edit the language file `localization\<languagename>.xml`, as per the instructions in the [Binary Translation](../binary-translation/) section.
        * _NOTE_: After making changes to the XML file in the `localization` directory, or after upgrading to a new version of Notepad++, you need to refresh the `nativeLang.xml`: use the **Localization** drop-down to change the **Localization** to another language then change it back immediately to your preferred language, or skip the "another language" step and just click on the preferred language -- either way ends up with copying the file to `nativeLang.xml` and immediately updating Notepad++'s text for menus and dialogs.  (Unlike many configuration files, exiting Notepad++ and restarting the application will _not_ bring in the new settings from an edited `localization\<languagename>.xml`; you _must_ re-choose the desired **Localization** for the changes to be applied.)
* **Toolbar**:
    * `☐ Hide`: the icon-based toolbar will be hidden
    * There is a radio-button set of choices for the icons (updated v8.0.0)
        * `Fluent UI: small`: uses small versions of the Fluent UI icons
        * `Fluent UI: large`: uses large versions of the Fluent UI icons
        * `Filled Fluent UI: small`: uses small versions of the Fluent UI icons, in a filled (or reverse-video) style
        * `Filled Fluent UI: large`: uses large versions of the Fluent UI icons, in a filled (or reverse-video) style
        * `Standard icons: small`: these are the small version of the traditional (pre-v8.0.0) icons
* **Document List Panel**:  (This section removed in v8.1.5.)
    * `☐ Disable extension column`: Prior to v8.1.5, if enabled, the [Document List](../views/#panels) panel will _not_ have the second column showing extensions (instead, the extension will be part of the Name column); in v8.1.5, this is controlled by right-clicking in the headers of the Document List panel.
    * `☐ Show`: Prior to v8.1.3, this checkmark would toggle the Document List panel; in v8.1.3 and after, this is now controlled by the [View menu's "Document List" entry](../views/#panels)
* **Tab Bar**:
    * `☐ Hide`: the tab bar for the open files will not be visible
    * `☐ Multi-line`: if there are enough tabs, they will wrap to a second line
    * `☐ Vertical`: have the tabs on their side on the left, rather than along the top
    * `☐ Reduce`: make the tab bar vertical region and font size smaller
    * `☐ Alternate icons`: change the "saved"/"edited"/"read-only" icons from blue/red/grey disk-icons to checkmark/pencil/lock symbols, respectively
      * The alternate icons option is designed to improve the user experience for visually-impaired users, and any who prefer different symbols rather than different colors to distinguish the status of each file. 
      * _Note_: In [Dark Mode](#dark-mode), the "saved" symbol (either the blue disk or the green checkmark) will _not_ be shown; the "edited" and "read-only" icons will be.
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
* **Line Wrap**: sets how lines will be wrapped (when **View > Word Wrap** is enabled)
    * `☐ Default`: wraps from the last visible column to the first visible column column
    * `☐ Aligned`: wraps from the last visible column to the same indent as the start of the unwrapped line
    * `☐ Indent`: wraps from the last visible column to the next level of indent compared to the start of the unwrapped line
* **Current Line Indicator**: Determines how the current line will be indicated.  
    - `☐ None` : no indicator for which line is the current line.
    - `☐ Highlight Background` : indicate the current line by highlighting the normal background color with the **Settings > Style Configurator > Global Styles > Current line background color** style's `Background colour`
    - `☐ Frame` : indicate the current line by drawing a rectangle frame around the text of the current line, using the color defined by **Settings > Style Configurator > Global Styles > Current line background color** style's `Background colour`, and with the rectangle-line thickness defined by the **Width** slider
        - **Width**: slider is used to set the width (in pixels) for the lines of the rectangle Frame for the current line
    - (In v8.4 and earlier, this multi-control section was just listed as `☐ Enable current line highlighting` in the list of checkboxes, and was the equivalent of `☐` being **None** and ☑ being **Highlight Background**.)
* `☐ Make current level folding/unfolding commands toggleable`: enables the feature that causes the [**View** menu](../views/#folding)'s **Collapse/Uncollapse Current Level** commands to both toggle the state of folding for the current level (so doing the command twice will undo the action); when not checkmarked, the **Collapse** will only cause the current level to fold, and **Uncollapse** will only cause the current level to unfold (new to v8.4.2)
* `☐ Enable Multi-Editing`: allows multiple selections not necessarily contiguous with each other by using Ctrl+Mouse click on the selection(s) (was known as **Multi-Editing Settings** prior to v7.9.2)
* `☐ Enable smooth font`: enables a font-smoothing algorithm from Windows, which may affect how smooth fonts are on some displays
* `☐ Enable scrolling beyond last line`: allows you to scroll (with scroll bar or mouse wheel) so that up to a page of blank space _after_ the last line is visible.  (Disabled, scrolling to the end will put the last line of text as the bottom line in the window, when there are more lines of text than are visible in the window)
* `☐ Keep selection when right-click outside of selection`: prevents right-click from canceling active selection (added v7.9)
* `☐ Disable advanced scrolling feature (if you have touchpad problem)`: designed to help if you have a problem with your touchpad

### Dark Mode

The Dark Mode feature (added in v8.0.0) is controlled here.

* `☐ Enable Dark Mode`: enables Dark Mode, where the UI is set to dark background with light text  
    * When you check this checkbox (☑):
      * it will change the active theme to `DarkModeDefault`
        * _Reminder_: changing the theme does _not_ change your UDL colors, as discussed in the [UDL and Themes](../user-defined-language-system/#udl-and-themes) section.  If your UDL was colored to match some other theme, the colors will likely mismatch, and you will need to edit the UDL colors to make it match the DarkModeDefault theme.
      * it will change the coloring of the menu bar and toolbar (if visible)
        * _Note_: In v8.0 - v8.1.1, you must exit Notepad++ completely and restart for full Dark Mode.  In v8.1.2 and newer, that is no longer necessary.
      * it may change your [General > Toolbar](#General) settings to use one of the **Fluent UI** icon sets: if you already had a Fluent icon set selected, it will keep it; if you had the **Standard icons: small** selected, it will change to **Fluent UI: small** icons
      * When you run in Dark Mode, the saved-file icon will not show up on your Tab Bar, whether or not you have [Alternate Icons](#General "General > Tab Bar > Alternate Icons") checked.  However, a read-only file or an edited file will still show their icons (either different colored disks, or the lock icon and pencil icon, depending on Alternate Icons setting).
    * When you uncheck this checkbox (☐):
      * it will change the active theme to `Default (stylers.xml)`
        * _Note_: this is true even if you previously had a different theme selected before trying out Dark Mode.  If you would like a different theme, you will have to manually change to that theme.
      * it will change the coloring of the menu bar and toolbar (if visible)
        * _Note_: You must exit Notepad++ completely and restart in order to get the rest of the UI (like the top title bar) to be fully out of Dark Mode.
      * it will leave your [Toolbar](#General) settings with the same icon set as you had when you were in Dark Mode
* Tones: allow you to change the tone of the Dark Mode (new to v8.1.2)
   * _Note_: Dark Mode Tones affect most of the user interface, including main menus and toolbars and most of the dialogs, as of v8.1.3. (In v8.1.2, the Tones affected the menus and the Find/Replace/Mark dialog, but not the other dialogs.)  The menu pull-downs, as well as Windows-defined dialog boxes like **Open** and **Save**, have their colors defined by operating system settings, and Notepad++ Dark Mode settings _will not_ affect them.
   * `☐ Black tone`, `☐ Black tone`, `☐ Black tone`, `☐ Black tone`, `☐ Black tone`, `☐ Black tone`, `☐ Black tone` => The dark color has a hint of that colored tone
   * `☐ Customized tone` => allows you to configure the tones of the individual components of the Dark Mode (even to the point of not being Dark anymore):
     * `Top` => choose the color of the menu bar and tool bar
     * `Menu hot track` => choose the color of the active menu bar entry
     * `Active` => choose the color of the active tab on the tab bar
     * `Main` => choose the color of the inactive tab(s) on the tab bar, as well as background colors for most dialog boxes
     * `Error` => choose the color for the error indicator on the Incremental Search bar
     * `Text` => choose the color for the menu bar entry names, and other normal text for most dialog boxes
     * `Darker text` => choose the color for the darker text for most dialog boxes
     * `Disabled text` => choose the color for disabled items in most dialog boxes (often referred to as "greyed out" or "disabled")
     * `Edge` => choose the color for the vertical separator bars on tab bars (in the main window and in dialogs), and other edges (like the boxes around color selectors)
     * `Link` => choose the color for link text in dialog boxes (for example the hyperlink URL in the User Defined Languages dialog) (new to v8.1.3)

### Margins / Border / Edge

These define the margin style, border width, and edge settings.  (This page is new in v7.9.2; in v7.9.1 and earlier, these settings were in the [Editing](#editing) page of the preferences.

* **Folder Margin Style**: if the active Language lexer allows for code folding, these determine
    * `☐ Simple`: shows a `-` if that section is not folded, or a `+` if it is.
    * `☐ Arrow`: shows a `▼` if that section is not folded, or a `▶` if it is.
    * `☐ Circle tree`: shows a `⊖` with a line to the end of the section if that section is not folded, or a `⊕` if it is folded
    * `☐ Box tree`: shows a `⊟` with a line to the end of the section if that section is not folded, or a `⊞` if it is folded
    * `☐ None`: shows no symbols and hides that column, even for lexers that allow code folding
        - The [View menu folding commands](../views/#folding) still work, even when the Folder Margin Style is set to None
* **Border Width**
    * [number-slider]: sets the width (in pixels) of the border around each view's text editor; technically, it's the gap between the light and dark portions of the sunken border, so a width of 0 will still have the light and dark lines for the sunken edge
    * `☐ No edge`: will remove the entire border, including the light and dark bars, so it no longer appears sunken
* **Vertical Edge Settings**
    * This will allow one or more vertical edges to be displayed while editing your file, to help with line lengths or positioning text.  This edge indicator can either be a vertical line, or a background shading beyond the edge.  The colour of the line or background shading will be taken from **Settings > Style Configurator > Global Styles > Edge Color: Foreground colour**.
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
* **Line Number**:
    * `☐ Display`: shows the line numbers to the left of the text (renamed in v7.9.2, known as **Editing** > `☐ Display line number`)
    * `☐ Dynamic width`: the line number display will adjust its width based on the number of digits needed (this matches the behavior prior to v7.9.2)
    * `☐ Constant width`: the line number display will have enough width for any line number in the document (new to v7.9.2)
* `☐ Display bookmark`: shows a large shaded circle next to all rows that contain a bookmark
* **Padding**: (new to v8.0.0)
    * **Left** will add _N_ pixels of padding between the left edge of the editor pane and the actual text (this is beyond the space allocated for the line numbering, and beyond the space allocated for the folding column).  A bigger number leaves more of a gap, and thus less room for actual text.
    * **Right** will add _N_ pixels of padding between the right edge of the editor pane and the actual text.  A bigger number leaves more of a gap, and thus less room for actual text.
    * The **Distraction Free** setting changes the borders when [**Distraction Free Mode**](../views/#application-views) is active; a bigger number means more of the screen width is allocated to distraction free text, and a smaller number means less of the screen width is allocated to distraction free text.

### New Document

These define properties of new documents (end-of-line format, encoding, and syntax language).

* **Format (Line ending)**:
    * `Windows (CR LF)` / `Unix (LF)` / `Macintosh (CR)`: newly-created files will use the normal Windows-style line ending, Unix/Linux/*nix-style line ending, or old Mac-style line ending.  (Please note that modern MacOS X uses Unix-style line endings.)
* **Encoding**
    * `ANSI`: characters are represented by a single 8-bit byte, and there are only 256 available code points
    * `UTF-8`: this can encode any of the Unicode characters; it uses a single 8-bit byte for codepoints under 128, and two or more bytes for other characters
        * `☐ Apply to opened ANSI files`: if you open an ANSI file, this allows it to be "upgraded" to UTF-8
    * `UTF-8 with BOM`: this is the same as UTF-8 encoding, but saves the file with an extra Unicode character U+FEFF (which is encoded as 3 bytes in the file), which some applications use as an indication that it's a UTF-8 file
    * `UTF-16 Big Endian with BOM`: this encodes characters (even those with codepoints under 128) with exactly two bytes. "Big Endian" refers to the order the two bytes will be written to disk (with most-signficant byte first)  (Prior to v8.0.0, it was shown as `UCS-2`)
    * `UTF-16 Little Endian with BOM`: this encodes characters (even those with codepoints under 128) with exactly two bytes. "Little Endian" refers to the order the two bytes will be written to disk (with least-signficant byte first) (Prior to v8.0.0, it was shown as `UCS-2`)
    * The final drop-down allows picking one of the old-style character sets (similar to using the main Notepad++ menu to select **Encoding > character sets ...**)
* **Default Language**: this pulldown sets whether new files will apply the styling for Normal Text, or use one of the programming-language syntax highlighting rules

### Default Directory

These affect open and save operations.

* **Default Directory**:
    * `Follow current document`: open/save dialogs will default to the current directory for the current file
    * `Remember last used directory`: open/save dialogs will remember the last directory you used in the dialog on subsequent uses of the dialogs (regardless of where the current file is located).  _Note_: the last used directory will only be updated when the **Open** or **Save** option is selected; if you **Cancel** or escape out of dialog, the last used directory will not be updated and will keep its previous value.
    * `___ ...`: this entry box with no label allows you to browse to a default directory, and all open/save dialogs will start in that directory
* `☐ Open all files of folder instead of launching Folder as Workspace on folder dropping`: when enabled, if you drag a folder from a Windows Explorer window, Notepad++ will open all the files individually; when disabled, Notepad++ will use the Folder as Workspace feature when you drag the folder into Notepad++

### Recent Files History

These change how the list of recent files is displayed in the File menu.  

* `☐ Don't check at launch time`: will skip checking whether files in the Recent Files History list exist at launch time.
    * this is useful if you have files on a network drive which intermittently isn't visible, and want files to remain in the Recent Files History list
    * this is also useful if you like knowing what files were previously edited, even after you've deleted those files from the folder
* `Max number of entries`: show the _n_ most recent files in the list
* `☐ In Submenu`: will show the recent files in a "Recent Files" submenu of the File menu, rather than directly in the file menu
* `☐ Only File Name`: will show just the file name, without the drive or path
* `☐ Full File Name Path`: will show the full path, including drive, path, and file name
* `☐ Customize Maximum Length`: will only list the first _n_ characters from the full file path

_Note_: Please understand that the Recent Files History shows the history of files recently _closed_, not recently _opened_.

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
    * `Tab size : ___`: sets the width of the tab stop.  If the text uses literal TAB characters (`Replace by space` is turned off), pressing the Tab key will insert one TAB character in the file, but Notepad++ will _display_ that character as a gap with a width of up to that many space characters.  If the text is replacing TABs with spaces, pressing the Tab key will insert enough literal spaces so that the next character will start at the beginning of the next tab stop.
    * `☐ Replace by space`: when set, hitting the TAB key will insert that number of spaces; when not set, the TAB key will insert the literal ASCII TAB character
    * For example: if `Tab size` is set to 4, and your line starts with one character, hitting the Tab key will either insert the single TAB character in the file which will be _displayed_ as a gap the equivalent width of 3 spaces to bring the total characters up to a multiple of the tab size (tab size of 4, minus a single real character already there, means 3 character positions left to fill with the gap of this single TAB character), or (if `Replace by space` is turned on) will insert 3 literal space characters instead of the TAB character; either way, the next character on the line will start in the 5th column of the line.
* `☐ Treat backslash as escape character for SQL`: this affects the **Language > SQL** handling of the `\` backslash character
    (Note: this option moved from [MISC Preferences](#misc) in v7.8.1)

### Highlighting

Affects highlighting of selected text.

* **Style All Occurrences of Token** (previously **Mark All**)
    * _Note_: this section of the preferences was renamed v8.1.4; it was known as **Mark All** in v8.0 - v8.1.3
    * `☐ Match case`: Mark All will be case-sensitive
    * `☐ Match whole word only`: Mark All will require a whole "word" (sequence of "word characters", as defined in the **Delimiter** preferences)
    * This setting section applies to the **Search** menu's **Mark All** submenu entries, and the equivalent [right-click Context Menu](../config-files/#the-context-menu-contextmenu-xml)'s **Style all occurrences of token** submenu entries, for applying "Style Tokens" to specific text.
* **Smart Highlighting**
    * `☐ Enable`: if you select a piece of text, Smart Highlighting will color all matching pieces of text.  It will use the style defined in **Style Configurator > Global Styles > Smart Highlighting**
    * `☐ Highlight another view`: Smart Highlighting will also apply to the other "view" (when you have documents open in both of Notepad++ view panes)
    * `Matching: ☐ Match case`: Smart Highlighting will be case-sensitive
    * `Matching: ☐ Match whole word only`: Smart Highlighting will require a whole "word" (sequence of "word characters", as defined in the **Delimiter** preferences)
    * `Matching: ☐ Use Find dialog settings`
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

### Searching

Affects the operations found in the **Find** dialog tabs.

* `☐ Don't fill find field in Find dialog with selected word`: when enabled, **Find** command will _not_ replace the **Find What** text with the currently-selected text; when disabled (default), the **Find What** text _will_ be replaced (added v7.8.3)
* `☐ Use Monospaced font in Find dialog (Need to restart Notepad++)`: changes the font from standard proportional font to a monospaced font in the text boxes in the **Find** dialog; requires restarting Notepad++ to change (added v7.8.1)
* `☐ Find dialog remains open after search that outputs to results window`: successful file-level searches cause the **Find** window to close; selecting this option keeps the window open always (added v7.9)
* `☐ Confirm Replace All in All Opened Documents`: when enabled, **Replace All in All Opened Documents** will ask for confirmation (added v7.9)
* `☐ Replace: Don't move to the following occurrence`: when enabled and a match is selected, **Replace** will make the indicated substitution, but then will NOT automatically move the caret to the subsequent match (added v8.0.0)

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
          * Every time you do a manual save, or every time you close the file while leaving Notepad++ open, this periodic backup of the file will be deleted
          * If there is a Notepad++ crash or Windows crash, it is possible for you to lose data
        * Periodic Backup file naming:
          *  For _named_ files (existing or saved files that have recent edits): the name of the backup file (in the listed directory) is `filename.ext@yyyy-mm-dd_hhmmss`, where `filename.ext` is from the main file.  As soon as you manually save the file (so it’s written to disk in the real location), the backup goes away, because the purpose of the periodic backup is to save a copy of a file that you’ve edited but not saved. The timestamp part of the periodic-backup-name is based on the first automatic save after the last manual save. Example: if you saved a file at 8:10:00am, the backup would go away; then, at 8:12:30am, you type something but don’t save, so sometime within N seconds of that (8:12:30+N) it will periodic-backup-save and make a file with a timestamp about then – something like `filename.ext@2021-06-23_081234`. If you left for a while (or exited Notepad++ and reloaded) and came back at 12:34:56pm and typed another character, it would do it’s periodic-backup-save on that file again so the last-modified time of the backup would be updated), but the name of the periodic-backup file will remain the same.
          *  For _unnamed_ files (new files that haven't been saved): the name of the backup file (in the listed directory) is `new NNN@yyyy-mm-dd_hhmmss`, where `new NNN` matches the name listed in the tab title. Since `new NNN` files are by definition not manually saved, the timestamp in the periodic-backup filename is based on when it did the first periodic-backup-save for that unnamed file.
* **Backup on save**
    * `☐ None`: no additional backup will be performed when the file is saved
    * `☐ Simple backup`: it will save a copy of the file, with the same name and extension, but with `.bak` appended.
      * if the `Custom Backup Directory` is turned on and defined, it will save the simple backup in that defined directory; for example, if it is set as `c:\myCustomBackupFolder\`, then the file `c:\path\to\file.txt` will save its simple backup as `c:\myCustomBackupFolder\file.txt.bak`
        * _Note_: if you are editing two files with the same name which are in separate directories (like `c:\path\a.txt` and `c:\other\a.txt`), the Custom Backup directory will only contain _one_ backup file (`a.txt.bak`) , with the contents of whichever file was saved most recently.  Turning off `Custom Backup Directory` will eliminate this problem, because then the backup of a file will reside in the same directory as the original, so there will not be name conflicts on the backups.
      * if the `Custom Backup Directory` is not turned on and defined, it will save the simple backup in the same directory as the original file; for example, saving `c:\path\to\file.txt` will save its simple backup as `c:\path\to\file.txt.bak`
    * `☐ Verbose backup`: it will save a copy of the file, with a date-and-timestamp added to the filename (in the format `yyyy-mm-dd_hhmmss`) as well as the `.bak` extension.
      * if the `Custom Backup Directory` is turned on and defined, it will save it in that directory; for example, if it is set as `c:\myCustomBackupFolder\`, then the file `c:\path\to\file.txt file` would be backed up as `c:\myCustomBackupFolder\file.txt.2021-06-28_073650.bak`
        * _Note_: if you are editing multiple files with the same name which are in separate directories (like `c:\path\a.txt` and `c:\other\a.txt`), the Custom Backup directory will contain verbose backup files for nearly all individual saves; however, if it happens that both files were saved within the same second (by being really fast, or using Save All), then only_one_ backup file will exist with that timestamp (`a.txt.2021-06-28-073722.bak`), with the contents of whichever file happened to be saved last in that second.  Turning off `Custom Backup Directory` will eliminate this problem, because then the backups of a file will reside in the same directory as the original, so there will not be name conflicts on the backups.
      * if the `Custom Backup Directory` is not turned on and defined, it will save it in `.\nppBackup\` subdirectory of the file's current directory; for example, saving `c:\path\to\file.txt` will create a backup called `c:\path\to\nppBackup\file.txt.2021-06-28_073650.bak`
    * `☐ Custom Backup Directory`: leave blank to put the backup in the same directory as the file; set to a directory to have all files backed up to one directory

#### Important backup information

This bears repeating: with `☐ Enable session snapshot and periodic backup` on, Notepad++ will allow you to exit with unsaved changes without asking you to save, and unless an error occurs, the next time you run Notepad++, your unsaved changes will still be there.  Notepad++ has been coded in such a way as to make this periodic backup as reliable as possible.  However, there are crashes and errors possible outside of Notepad++'s control, and there is no guarantee or warranty that your unsaved data will remain after a crash or other major system error.  Once you manually save, the periodic backup is deleted.  The builtin periodic backup should not be considered a long-term backup option, and unsaved changes in files should always be considered as volatile and unsaved.

Backup on save is the long-term backup solution built into Notepad++: simple backup will just keep one copy that matches the most recent save of the file; verbose backup keeps multiple copies with date stamps.  The location of backup-on-save backup files is described above.

If you are editing mission-critical files: Your data is your responsibility.  It is recommended to always use dedicated backup software in addition to any periodic-backup or backup-on-save features you have enabled.  You may want to look into the AutoSave plugin (available through **Plugins > Plugins Admin**) for better control of automated-saving while changes are being made -- though if you install that plugin, understand that you have to configure it before it will automatically save your file(s) for you.  Using cloud-based folders may provide backup and/or revision history.  A dedicated revision control system, such as git or subversion, will provide control over your version history.

### Auto-Completion

Sets options for [auto-completion](../auto-completion/) of text, including word completion, syntax completion, and automatically pairing certain punctuation pairs and html/xml tags.

* **Auto-Completion**
    * `☐ Enable auto-completion on each input`: a dropdown selection will appear as you type; arrow keys will select various choices, TAB or ENTER will accept a choice, ESC will cancel auto-completion
        * `☐ Function completion`: will auto-complete function names only, based on the keywords in the active [auto-completion file](../auto-completion/)
        * `☐ Word completion`: will auto-complete words only, based on words that already exist in the current file
        * `☐ Function and word completion`: will auto-complete both function names and words
    * `From the _n_th character`: must type at least _n_ characters before the auto
        * if `☐ Enable auto-completion on each input` is disabled, the _n_th character will be disabled (greyed out)
    * `☐ Ignore numbers`: won't try to auto-complete when typing numbers
    * **Insert Selection**: v8.2.1 added a new section
        * `☐ TAB`: toggles whether or not TAB will accept your choice
        * `☐ ENTER`: toggles whether or not ENTER will accept your choice
        * v8.2 and earlier behaved as if both have checkmarks; v8.2.1 and later defaults to having TAB checkmarked but ENTER _not_ checkmarked, so the default behavior has changed.
    * `☐ Function parameters hint on input`: for applicable programming languages, will provide hints on what to type in a function parameter list
    * Please note that if you use [**Edit > Auto-Completion > ...** menu entries](https://npp-user-manual.org/docs/editing/#edit-menu) to activate the completion features, you can force function or word or parameter completion, even when those checkboxes are turned off in the settings, and even if there aren't enough characters typed to trigger the auto-completion.
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

### Multi-Instance and Date

The **Multi-Instance** settings determine whether multiple instances of Notepad++ can be run simultaneously.

* `☐ Open session in a new instance (and save session automatically on exit)`: each session will open in a new instance, but multiple files can be opened in each session.  "Opening a session" can be done either by using **File > Load session...**, or (if you have set the [MISC > Session File ext](#misc)) by opening a file with that extension. From Notepad++ v8.2, the loaded session in the new instance will be saved automatically while the instance exiting, if this option is set.
* `☐ Always in multi-instance mode`: every time you open a file from Windows, it will open a new instance of Notepad++.
* `☐ Default (mono-instance)`: every time you open a file from Windows, it will go into the single Notepad++ instance.  If you open a session file while Notepad++ is already open, the files from that session will be opened in addition to the files you already have open.

**WARNING**: If you select anything other than `Default (mono-instance)`, changed settings in one instance will _not_ influence the settings in the other instance, and only the changed settings in the _last_ instance closed will be saved to disk.

The **Customize insert Date Time** settings will allow you to customize the time format inserted by [**Edit > Insert > Date Time (customized)**](../editing/#edit-menu).  The 

* `☐ Reverse default date time order (short & long formats)`: if checked, the short and long formats will insert the date then the time; if unchecked, the short and long formats will insert the time then the date.
* `Custom Format`: Enter in the format string that will define the date and time display desired when inserting the customized time. 

Format | Description | Example
---|---|---
--- | _Day_ | ---
d | Day of the month as digits without leading zeros for single-digit days. | 1, 31
dd | Day of the month as digits with leading zeros for single-digit days. | 01, 31
ddd | Abbreviated day of the week | Mon
dddd | Day of the week | Monday
--- | _Month_ | ---
M | Month as digits without leading zeros for single-digit months. | 1
MM | Month as digits with leading zeros for single-digit months. | 01
MMM | Abbreviated month | Nov
MMMM | Full month | November
--- | _Year_ | ---
y | Year represented only by the last digit. | 9
yy | Year represented only by the last two digits. A leading zero is added for single-digit years. | 99
yyyy | Year represented by a full four or five digits | 1999
g, gg | Period/era string formatted | B.C., A.D.
--- | _Time_ | ---
h | Hours with no leading zero for single-digit hours; 12-hour clock | 1, 11
hh | Hours with leading zero for single-digit hours; 12-hour clock | 01, 11
H | Hours with no leading zero for single-digit hours; 24-hour clock | 1, 23
HH | Hours with leading zero for single-digit hours; 24-hour clock | 01, 23
m | Minutes with no leading zero for single-digit minutes | 9, 59
mm | Minutes with leading zero for single-digit minutes | 09, 59
s | Seconds with no leading zero for single-digit seconds | 9, 59
ss | Seconds with leading zero for single-digit seconds | 09, 59
t | One character time marker string | A, P
tt | Multi-character time marker string | AM, PM




### Delimiter

Sets the characters that are considered part of a "word" for quick selections using double-click, [Smart Highlighting](#highlighting), or the "match whole word only" in a normal search expression.  It is also used for [auto-completion](../auto-completion/#create-auto-completion-definition-files).  This setting does _not_ affect a [regular expression](../searching/#regular-expressions)'s interpretation of a word character or word boundary.

* **Word character list**
    * `☐ Use default Word character list as it is`: for Smart Highlighting (see above) or the Normal search mode in the Find and Replace dialogs, will use the normal alphanumeric rules for determining what constitutes a word for "Match Whole Word Only"
        * The default "word characters" include anything that Unicode considers alphanumeric, plus the underscore "_" character.
            * Includes: standard Latin characters, accented characters, letter-like symbols, superscript digits, and enclosed (circled) digits
            * Excludes: punctuation, mathematical operators, box drawing, arrows, emoji, or other such symbols.
    * `☐ Add your character as part of word`: sometimes, the default "word character list" isn't sufficient for you; if you want other characters to be considered in "whole word only", add them here
        * The value should be a string consisting of all the additional characters you would like to be included as a "word character".
        * Spaces are liable to cause problems, and are not recommended to be present in this entry.  If you try to add a space, the dialog box will show a warning message.
* **Delimiter selection settings**
    * If you define open and close characters, Ctrl + MouseDoubleClick will select everything inside that delimiter pair
    * `☐ Allow on several lines`: Ctrl + MouseDoubleClick will work across multiple lines, instead of just on a single line

### Cloud & Link

* **Settings on cloud**: Allows saving your settings to the cloud instead of in the normal `%AppData%` or program-install folders.  More information can be found in the [Config files location](../config-files/#configuration-files-location)
    * `☐ No Cloud`: saves settings in the normal location
    * `☐ Set your cloud location path here`: settings will go in the given directory, which is assumed to be in a folder that's synced to your cloud-provider

* **Clickable Link Settings**: Affects behavior of URLs in your document.  (Moved in v7.9.2; previously in the [Misc](#misc) settings)
    * `☐ Enable`: text that appears to be a URL will allow you to double-click to open that URL in your default browser.  When you hover over the URL, it will change to the style defined in **Style Configurator > Global Styles > URL hovered**
    * `☐ No underline`: will remove the underline normally present on a link
    * `☐ Enable fullbox mode`: the background color and foreground color will change on hoverover; when disabled, just the foreground color will change (new to v7.9.2)
    * `URI Customized Schemes`: Space-separated list of additional schemes to recognize as URLs (new to v7.9.2). The schemes `ftp:// http:// https:// mailto: file://` are always recognized, no matter what the contents of this setting, so they do not need to be included in this entry box.




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
* **File Status Auto-Detection**
    * [dropdown]
        * `Enable`: for the active file only, will check periodically to see if the file has been updated on disk, and will prompt to ask if you want to reload the file from the disk, or keep the version that's currently in Notepad++
        * `Enable for all open files`: for all active files, check periodically to see if the file has been updated on disk
        * `Disable`: will not check to see if the file has been updated on disk
    * `☐ Update silently`: instead of prompting, will automatically reload the file from disk
    * `☐ Scroll to the last line after update`: will scroll to the end of the file after reloading from disk (otherwise, the cursor and scrolled-location stays where it was before the update)
* `☐ Enable Notepad++ auto-updater`: will automatically download updates from the official website, once the development team has decided it's time to push an update to users.  If disabled, you will have to manually download the installer from the official website yourself.
* `☐ Mute all sounds`: enable/disable sound feedback (example: if a search action in [**Find / Replace dialog**](../searching/#dialog-based-searching) results in the text not being encountered).
* `☐ Autodetect character encoding`: when opening a new file, try to algorithmically determine what character encoding should be used
* `☐ Minimize to system tray`: place the Notepad++ icon on the system tray (instead of the task bar) when the Notepad++ window is minimized
* `☐ Show only filename in title bar`: use just the file name (instead of the full path) of the active file in the Notepad++ title bar
* `☐ Use DirectWrite (May improve rendering special characters, need to restart Notepad++)`: enables DirectWrite drawing (added in v7.8.8)
  * DirectWrite will help in displaying characters even if the active font doesn't have a glyph
  * The modified rendering may affect the clarity or readability of the characters for some users or systems (for some users, it increases readability; for others, it decreases readability).  As with all settings, 
* `☐ Enable Save All confirm dialog`: when Save All command is issued, will pop up a dialog to confirm you really want to save all: **Yes** will Save All; **No** will not save all _this time_, but will ask again next time; **Cancel** will save all _and_ will uncheck this preference so that Save All will stop asking for confirmation in the future
* `Session file ext.`: populate with a file extension (without the `.`).  When you open a file with this extension (whether from Windows file associations, or from the Notepad++ **File > Open** or similar), Notepad++ will treat the file as a session file, and open the files from that session, rather than showing and editing the contents of the file.  This will honor the [Multi-Instance](#multi-instance) settings.
* `Workspace file ext.`: populate with a file extension (without the `.`).  When you open a file with this extension (whether from Windows file associations, or from the Notepad++ **File > Open** or similar), Notepad++ will treat the file as a workspace file, and open that workspace, rather than showing and editing the contents of the file.  This will honor the [Multi-Instance](#multi-instance) settings.

## Style Configurator

The Style Configurator dialog has three regions: Select theme, language and style selection lists, and the style definition.

The "Select theme:" pulldown allows you to select which theme you want.  [Themes](../themes/) are pre-defined sets of formatting rules, which often try to use a consistent color scheme between languages.

The "Language:" selection list lets you select whether you want to set the formatting for "Global Styles", or a specific [programming language](../programing-languages/) that you want to set the highlighting for.  The "Style:" selection list lets you select which highlighting rule for the given language.

On all but "Language: Global Styles", there will also be a "Default ext." box, which is an un-editable list of the default file extensions associated with that Language; and the "User ext." box, where you can add a user-defined list of additional extensions (space separated, don't use the . in the extension), which says which other extensions you want to apply this language's formatting to.  There is no specific entry called "Normal text" or "Plain text": to edit the colors for a plain text file (like `.txt`), use the "Global Styles" language.  (Please note that any changes you make in the Style Configurator dialog box for a specific language only applies to that language and only applies to the selected [theme](../themes/): if you add a user-defined extension to a language in the `Default (stylers.xml)` theme, it will not affect the list of user-defined extensions for that language in any of the other themes.)

The final section will reiterate which language and style are selected, and allow you to set colors and fonts.  The Colour Style allows you to choose the Foreground or Background colour by clicking on the colored box. You can also make the style's Foreground or Background colour ignored, by right-clicking on the colored box (you'll see the additional diagonal stripes on the colored box) - in this case the default background/foreground colour will be used.  The Font Style allows you to pick the font, size, and bold/italic/underline settings.  If Font name or Font size are left blank, they will inherit from the Global Styles: Default Style.  If you right-click a colour, you will see diagonal stripes across the colour, indicating it is set to "inherit", meaning that it will take that colour from the Default Style.  Under the "Language: Global Styles" with "Style: Global override", there are also a series of checkboxes for "Enable global xxx", which will mean that Notepad++ will use the Global override setting for that attribute, rather than using the per-language styling settings for that attribute.

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
* Selected text colour [background only] ⇒ Selected text will be indicated with this background. If [Preferences > Highlighting > Smart Highlighting](#highlighting) is enabled, the "Smart Highlighting" style (below) will be coloured overtop of the "Selected text colour". If the [configuration file `enableSelectFgColor.xml`](../config-files#other-configuration-files) exists (and you have v8.0.0 or newer), "Selected text colour" will honor the foreground colour as well.
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
* Document map [background and foreground] ⇒ The foreground color will be semi-transparently overlayed over the miniature version of text that's currently visible in the editor; the background color will be semi-transparently overlayed over the miniature version of the text that isn't currently visible in the editor (this style is new to v8.1.5).

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

The `<LexerStyles>` section contains a `<LexerType>` tag for each programming language -- where the `desc=` attribute matches the name in the list of Languages from the GUI.  Each of those contains one or more `<WordsStyle>` tags, where the `Name=` attribute matches the entries in the GUI's list of Styles for that language; the WordsStyle are usually empty tags (`<WordsStyle .../>`), but can contain values (`<WordsStyle...>user1 user2 ...</WordsStyle>`) if there is an associated list of user-defined keywords for that style.  (If the language's lexer is not programmed to make use of extra keywords for a given style, filling in values there will _not_ make those keywords styled; the lexer must be programmed to use the user-defined keywords for that to work.  You can tell whether a lexer will handle user-defined keywords for a given style if the Style Configurator shows a User-defined Keywords box for the given lexer language and style.)

There is also a `<GlobalStyles>` section, with `<WidgetStyle>` entries corresponding to the elements of the "Global Styles" in the GUI.

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

Use the Modify button to edit the existing shortcut or to create a shortcut for an entry that has none.  The resulting dialog will show the Name of the active action.  There are checkboxes to enable the CTRL, ALT, and SHIFT key-modifiers.  The main key in the shortcut is defined by the pulldown menu.  Hitting OK will apply the added or changed shortcut and leave the dialog.  Cancel will undo your changes and leave the dialog.  (Please note that if you are using some localizations, the key you select [might not match](https://notepad-plus-plus.org/community/topic/17679/using-caret-circumflex-key-for-a-shortcut/10) <!-- TODO = this link should really refer to a submitted issue request, rather than a forum-topic --> what key you type: whatever key in your locale uses the same keycode as the standard US English keyboard will be the actual key.)  

In the `Scintilla commands` tab, you can actually assign more than one shortcut to a given Scintilla command, so there is an extra pane listing existing shortcuts, and additional Add and Remove buttons.  For more on the meaning of the `SCI_xxxx` names in the `Scintilla commands` tab, see the section on [Other Editing Commands and Shortcuts](../editing/#other-editing-commands-and-shortcuts).

Use the Clear button to remove the existing shortcut for a given entry.

The Delete button is usually disabled.  However, in the `Macros` and `Run commands` menu, the Delete button will be enabled, and it will remove the selected entry from the menu -- so it will not only not have a shortcut, but it won't be in the menu the next time you run Notepad++.

The Close button will close the dialog box.

_Please Note_: Notepad++ honors standard Windows behavior with keystrokes for menu accelerators: typing `Alt` with the first letter (or underlined letter) for a main menu entry will open that menu.  (Because the `X` on the right of the menu bar, which closes the active tab, was created as a menu action on the main menu bar with the name "X", it's accelerator is therefore `Alt+X`.)  If you want to define `Alt+`_Letter_ for some other action, you may do so using the Shortcut Mapper, and that accelerator will no longer work for the menu, but will instead access the action you mapped it to; undefining that new Mapper entry will allow Windows to treat that sequence as the accelerator again.  Shortcut Mapper cannot change or clear the Windows accelerator for a menu entry -- it can just preempt that accelerator key to use for something else.

### Configuration file: `shortcuts.xml`

If you prefer to edit XML instead of using the GUI to modify shortcuts, you may edit the `shortcuts.xml` file.  The keyboard shortcuts are defined as attributes of the `<Macro>`, `<Command>`, `<PluginCommand>`, and `<ScintKey>` tags.  The `Key=` attribute is the decimal value for the keycode associated with the key you want to hit.  The `Ctrl=`, `Alt=`, `Shift=` attributes have values of either "yes" or "no", and either enable or disable the modifier for that key.

### Common Shortcut Mapper Problems

With the introduction of the message area, it is easy to see when a conflict exists between shortcuts.  All you have to do is pick the entry that you _don't_ want to use the conflicted shortcut, and either Clear or Modify the shortcut so there is no longer a conflict.

## Other Toggles and Settings

Not all preferences are handled in dialogs, and those toggles and settings are described here.

### Other Settings-menu Entries

* **Settings > Import > Import Plugins...** will ask you to navigate to a plugin DLL anywhere on your filesystem; it will then copy that DLL into the appropriate folder so that the next time you run Notepad++, the application will load that DLL as a plugin (assuming it is a valid plugin DLL).  This is an alternate way to install a single-DLL plugin, rather than the [other installation methods](../plugins/#how-to-install-a-plugin) of using Plugins Admin or manually putting the DLL and associated files in the right location.  (This menu entry will not work on its own if the plugin requires more files than just its DLL.)

* **Settings > Import > Import Style Themes...** will ask you to navigate to a style theme XML file, and will put it in the appropriate folder so that the next time you run Notepad++, the application will include it when you use the [Style Configurator](../preferences/#style-configurator), the new theme will be listed in the "Select theme:" pulldown.

* **Settings > Edit popup ContextMenu** will open the [`contextMenu.xml` configuration file](../config-files/#the-context-menu-contextmenu-xml), so that you can edit your context menu, following the advice for [editing configuration files](../config-files/#editing-configuration-files).

### Preference Toggles in Other Dialogs

* The **Save Session** dialog will have a `☐ Save Folder as Workspace` checkbox, which will be active (able to be toggled) when you have a **Folder as Workspace** opened.  If the checkbox is checked, the current **Folder as Workspace** will be included in the saved session; otherwise, the session will not include any **Folder as Workspace** information.  (Requires Notepad++ v7.9.3 or newer.)

* When saving a new file or otherwise running the **Save As** dialog, there is an `☐ Append extension` checkbox.  If checked, Notepad++ will automatically append the first extension listed in the selected **Save as type**; otherwise, the extension must be manually included in the **File name** field.  (This toggle is new to v8.0.0, and replaces the **Preferences > MISC > ☐ Set Save dialog file extension filter to `*.*`** or **Set Save dialog file extension filter to `.*` for Normal Text** preferences for setting the save dialog file extension to `*.*` that were present in prior v7.9.1-v7.9.5; in v7.9.1, that `*.*` option replaced the setting in the Default Directory section called **Use new style dialog** which influenced how extensions were added or not as it toggled the Save As dialog from an ancient Windows Save-As dialog to a somewhat more modern dialog.)

### Menu-based Settings

The following are settings or preferences that are stored and modified by menu entries rather than dialog boxes.

#### View Menu

The View menu contains many toggles that affect Notepad++, many of which decide whether certain features of the application are visible or not.  Some of these that are remembered from one run of Notepad++ to the next (similar to dialog-based settings), and others that are specific to the current run of Notepad++.  These toggles and actions are described more in the [Views](../views/) section of this manual.

#### Encoding Menu

These entries influence the file encoding of the active file -- how the underlying bytes of the file are interpreted as glyphs, and how the characters you enter are saved as underlying bytes.  The [New Document](#new-document) preferences will influence which Encoding is selected for a new file, and the [MISC > Autodetect character encoding](#misc) preference will affect what encoding will be selected when the file is first read from disk.

The major encodings are `ANSI` which is really a family of 8-bit encodings based on the active [Windows Code Page](https://en.wikipedia.org/wiki/Windows_code_page), [`UTF-8`](https://en.wikipedia.org/wiki/UTF-8), which uses variable-width multi-byte sequences to represent Unicode characters, [`UTF-16`](https://en.wikipedia.org/wiki/UTF-16) which uses two-byte Big Endian or Little Endian sequences to represent Unicode characters (these were listed as `UCS-2` in v7.9.5 and earlier), and the various `Character sets`, which allow you to use international 8-bit sets of characters that provide a limited set of glyphs.

The `... with BOM` entries indicate that it uses the Unicode [Byte Order Mark](https://en.wikipedia.org/wiki/Byte_order_mark "BOM") at the start of the file to indicate the correct byte order (big endian or little endian), and in the case of UTF-8, to make it unambiguous that the file is meant to be a UTF-8 Unicode file rather than another 8-bit encoding.

The `Convert to ...` entries below the separator line will change the encoding (the underlying bytes stored on disk) of the active file, without changing the glyphs.  So if you just have the Euro currency symbol `€` in your file, it will be stored as byte 0x80 if you `Convert to ANSI` (and are in a Western-European codepage in Windows), as the three-byte sequence 0xE2 0x82 0xAC if you `Convert to UTF-8`, and as the two byte sequence 0x20 0xAC if you `Convert to UTF-16 BE BOM` (known as `Convert to UCS-2 BE BOM` in v7.9.5 and earlier).

The entries above the separator line (without `Convert to` in the name) show the file's active encoding or character set.  If you change that setting manually, it will leave the bytes in the file the same and change the glyph that is shown.  For example, if you enter the `€` in a UTF-8 encoded file, and then manually select `Encoding > ANSI`, suddenly those characters will look something like `â‚¬` (depending on the active Windows code page); this is because UTF-8 `€` is the three bytes 0xE2 0x82 0xAC, and those three bytes represent three characters when interpreted as ANSI.  Or, if you are starting with a character set of **Western European > OEM-US** (the old DOS box-drawing character set) with the `▓` grey box, if you change to character set to **Western European > Windows-1252**, it will become the `²` superscript 2.

In general, if you want the glyph to stay the same and change the bytes on the disk, then use the `Convert to...` entries; whereas if the glyphs shown don't match what you think the bytes of the data should represent, you probably need to use one of the upper entries to change the interpretation of the bytes.

#### Language Menu

This menu shows the active syntax highlighter lexer (including [User Defined Languages](../user-defined-language-system/)), and allows you to change the syntax highlighter for the current file.  The syntax highlighting colors are set in the [Style Configurator](#style-configurator) or in the [UDL dialog](../user-defined-language-system/#udl-dialog-box-or-window).

### Preferences for Advanced Users

The following settings are for rather specific needs and could cause some confusion if they are enabled. As a result they are not set via UI but in `config.xml`. Note that you should close Notepad++ then edit `config.xml` following the best practices in the [Editing Configuration Files](../config-files/#editing-configuration-files) section to prevent your modification from being erased or overwritten when Notepad++ exits.

* Allow regex backward search: Backward regex searching is forbidden by default (starting in v7.8.7) due to sometimes surprising results. However, if this feature is needed, you can set `regexBackward4PowerUser` attribute to `yes` in the `FindHistory` tag of `config.xml` to enable this option:
```
<FindHistory nbMaxFindHistoryPath="10" nbMaxFindHistoryFilter="10" nbMaxFindHistoryFind="10" nbMaxFindHistoryReplace="10" matchWord="no" matchCase="no" wrap="yes" directionDown="yes" fifRecuisive="yes" fifInHiddenFolder="no" fifFilterFollowsDoc="no" fifFolderFollowsDoc="no" searchMode="0" transparencyMode="1" transparency="150" dotMatchesNewline="no" isSearch2ButtonsMode="yes" "regexBackward4PowerUser"="yes">
```
Simply add `"regexBackward4PowerUser"="yes"` if this option is absent.

* Change the number of expressions that can be saved in the [Find/Replace](../searching/) dialog's Find, Replace, Filters, and Directory fields.  They are set in the `<FindHistory ...>` tag inside `config.xml`, using the attributes:
    * `nbMaxFindHistoryFind` => changes the number of **Find what** entries that are saved in the history (0 .. 30, default = 10)
    * `nbMaxFindHistoryReplace` => changes the number of **Replace with** entries that are saved in the history (0 .. 30, default = 10)
    * `nbMaxFindHistoryPath` => changes the number of **Directory** entries that are saved in the history (0 .. 30, default = 10)
    * `nbMaxFindHistoryFilter` => changes the number of **Filter(s)** entries that are saved in the history (0 .. 20, default = 10)

* Changing the command-line interpreter used: by default, **File > Open Containing Folder > cmd** will launch the `cmd.exe` command-line interpreter.  If you have a preferred command-line interpreter (such as `powershell`), you can add another `<GUIConfig...>` tag inside the `<GUIConfigs>` section:
```
<GUIConfig name="commandLineInterpreter">powershell</GUIConfig>
```
If your command-line interpreter is not in your path, make sure to include the drive and folder in the contents of that tag.  If there are spaces, make sure to use quotes around the path:
```
<GUIConfig name="commandLineInterpreter">"c:\path\with spaces\to\cli.exe"</GUIConfig>
```
