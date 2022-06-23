---
title: Editing
weight: 30
---


## Column Mode & Column Editor

Using `Alt + Mouse dragging` or `Alt + Shift + Arrow keys` to make a selection in column mode:

![](../images/columnMode.gif)

In column mode, typing will type the same thing in all the rows of the column.  If you copy/cut in column mode, then you copy/cut a rectangle of text, which can be pasted over an identical-sized rectangle elsewhere, or pasted into a separate document or separate application.  This is implemented for making working with rectangles of text (instead of whole lines of text) more convenient.

The Column Editor dialog, accessed via **Edit > Column Editor**, allows you to insert text or numbers in every row of the active Column Mode selection:

![](../images/columnEditor.gif)

* The `Text to Insert` will use the same text in every row.
* The `Number to Insert` will insert increasing numbers.
    * `Initial number` sets the starting number.
    * `Increase by` will change the step between numbers.  With a value of `0` (or if left empty), it will insert the same number every time.
    *  `Repeat` will repeat the same number _n_ times.  Defaults to 1 if left blank.
    * `☐ Leading zeros` will cause all the numbers to have the same number of digits, by adding leading zeros for the smaller values
    * `Format` chooses between **Dec** (0-9), **Hex** (0-9,A-F), **Oct** (0-7), or **Bin** (0-1).
        Note: that the numerical boxes above are always in decimal, even if a different format is chosen for display.  (Example: to get `F`-`1F`, column-select 17 rows and set the initial number to `15` -- it will not allow `F`.)

## Multi-Editing

Multi-Editing mode allows you to make multiple cursor selections by using `Ctrl+Click` for each additional cursor.  This allows performing the same editing actions (typing, copy/cut/paste/delete, arrowing through the text) in multiple locations, even if they aren't lined up in a nice column, or even if there are lines between the cursors that you don't want to affect.

![](../images/multiEdit.gif)

Whether or not you can use Multi-Editing mode is determined by the [Settings > Preferences > Editing > ☑ Enable Multi-Editing (Ctrl+Mouse click/selection](../preferences/#editing) checkbox: with it checkmarked, `Ctrl+Click` will add cursor locations; with it not checkmarked, Multi-Editing is disabled.


## Dual View
To create Dual View, drag and drop any tab that you want it to be in another view (or right click on the tab) then choose "Move to Other View" command from the popup context menu.
Once you've got 2 views, you can move files between 2 views by drag-and-dropping.

![](../images/move2view.gif)

## Clone Document
Drag and drop any tab that you want to clone (or right click on the tab) then choose "Clone to Other View" command from the popup context menu.
The cloned document is the same document as its original one, but with the separated views.

![](../images/clonedDoc.gif)

## Edit Menu

Aside from the normal undo/redo/copy/paste entries, there are a number of sub-menus to the **Edit** menu, which group together various categories of editing-related commands, and a few other editing commands in the main **Edit** menu.

* `Insert >` ⇒ submenu with actions that insert the date and time (new to v8.1.4)
    * `Date Time (short)` ⇒ like `12:46 PM 8/21/2021` (new to v8.1.4)
    * `Date Time (long)` ⇒ like `12:46 PM Saturday, August 21, 2021`) (new to v8.1.4)
    * `Date Time (custom)` ⇒ can insert a date with a customized format, as defined in the [**Settings > Preferences > Multi-Instance & Date**](../preferences/#multi-instance-and-date) dialog
* `Copy to Clipboard >` ⇒ submenu with actions that copy current filename, path, or directory name to the clipboard
* `Indent >` ⇒ submenu with actions that increase or decrease the current line's indentation, based on [the syntax language's](../preferences/#language) tab/indent settings
* `Convert Case to >` ⇒ submenu with actions that change the case of the selected text (all UPPERCASE, all lowercase, and various mixed-case settings)
* `Line Operations >` ⇒ submenu with actions that typically work on lines (also known as "rows") of your document
    * There is a method for duplicating data:
        * `Duplicate Current Line`: duplicates the current line if no selection is active, or duplicates the selected text if a selection is active
    * There are two versions of the Remove Duplicates functionality:
        * `Remove Duplicate Lines`: leaves only the first instance of any full lines that have more than one copy anywhere in the active file; acts upon the line set spanned by the current selection, or the entire file if no active selection
        * `Remove Consecutive Duplicate Lines`: will only remove duplicates that are on the lines immediately following the first instance (still keeping the first instance); acts upon the line set spanned by the current selection, or the entire file if no active selection
        * NOTE: Duplicates removal is performed with the assumption that all line-endings in the file are uniform and match the current selection for the file being edited -- the quickest way to check that selection is to glance at the status bar, where the current line-ending type is shown either as `Windows (CR LF)`, `Unix (LF)` or `Macintosh (CR)`.  It might be desirable to check the line-ending types in your file before executing a sorting operation, and use the `Edit > EOL Conversion >` choices or right-click on the Status Bar's EOL indicator to fix the line endings if necessary.
    * There are methods for splitting lines and joining lines together:
        * `Split Lines`: will insert a line-ending into a long line(s): if there is one or more [Vertical Edge](../preferences/#margins-border-edge) value specified (requires v7.9.3 or later), it will split at the right-most Vertical Edge; otherwise, it will split at the current size of the editor window.  It operates on the lines spanned by the current stream selection or the single line of the caret if no stream selection is currently active.
        * `Join Lines`: will combine the lines touched by the active stream selection by replacing line-endings with a single space character. It requires an active stream selection that spans two or more lines.
    * There are commands for removing lines
        * `Remove empty lines`: will remove all lines containing no characters from the entire document
        * `Remove empty lines (Containing Blank characters)`: will remove all lines containing no characters from the entire document; if a line contains only space or tab characters that line will be removed as well
    * There are commands for changing the order of existing lines:
        * `Move Up Current Line`: will swap the current line with the line above it, effectively moving the line of the caret up one row in the document; if a selection spanning lines is active upon invocation, it will move those lines touched by the selection up as a group
        * `Move Down Current Line`: will swap the current line with the line below it, effectively moving the line of the caret down one row in the document; if a selection spanning lines is active upon invocation, it will move those lines touched by the selection down as a group
        * `Reverse Line Order`: will take the selected lines (or all of the lines of the current document if no active selection) and will order them reversely (i.e. flipped) from their existing order (added in v8.0.0)
        * `Randomize Line Order`: will take the selected lines (or all of the lines of the current document if no active selection) and place them in an unpredictable order (added in v7.9 as "Sort Lines Randomly"; renamed in v8.0.0)
    * There are a variety of sorting algorithms:
        * `Ascending` means smallest to largest (A-Z)
        * `Descending` means largest to smallest (Z-A)
        * `Lexicographically` (or `Lex.`) means based on character codepoint, comparing one character at a time:
            * All uppercase letters will sort before any lowercase letter, so uppercase `Z` will sort before lowercase `a`
            * The sequence `10` will sort before `2`, because it sorts character-by-character of each collection of characters, and the character `1` comes before the character `2`
        * `Ignoring case` means that lowercase `a` will sort the same as uppercase `A`, and both will come before either `Z` or `z`
        * `As Integers` means that `10` will sort as being bigger than `2`
        * `As Decimals (Comma)` means it will recognize `10,234` and `9,876` as decimal numbers and sort them numerically
        * `As Decimals (Dot)` means it will recognize `10.234` and `9.876` as decimal numbers and sort them numerically
        * NOTE: Sorting is performed with the assumption that all line-endings in the file are uniform and match the current selection for the file being edited -- the quickest way to check that selection is to glance at the status bar, where the current line-ending type is shown either as `Windows (CR LF)`, `Unix (LF)` or `Macintosh (CR)`.  It might be desirable to check the line-ending types in your file before executing a sorting operation, and use the `Edit > EOL Conversion >` choices or right-click on the Status Bar's EOL indicator to fix the line endings if necessary.
        * NOTE: If a [Column Mode](./#column-mode-column-editor) selection is active, the sort will re-order all the lines included in the selection, but the sort key (the text that decides the sort order) will be limited to what is inside the column selection. If the keys are identical on two lines, then the order of those two lines will not change (even if text outside of the selected key columns is different).
* `Comment/Uncomment >` ⇒ submenu with actions that add or remove comment syntax, based on the file's **Language** selection.  This makes use of the `commentLine`, `commentStart`, and `commentEnd` attributes of the active Language as defined in [langs.xml](../config-files/#keyword-lists-langsxml) to define the characters to use for making or clearing line comments (`commentLine`) and block comments (`commentStart` and `commentEnd`).
* `Auto-Completion >` ⇒ submenu with actions that manually trigger [auto-completion](../auto-completion/) of function name, word, function parameter, and pathname.  While the automatic completion is affected by [**Preferences > Auto-Completion** settings](../preferences/#auto-completion) for setting minimum number of characters, and enabling which of the completions happen automatically, when you manually trigger one of the auto-completion actions through this menu or keyboard shortcut equivalents, completion will happen regardless of those settings (so you can manually trigger when there's fewer characters than the auto-trigger threshold, or you can manually trigger function completion when only word completion is enabled).
* `EOL Conversion >` ⇒ submenu with actions that convert line endings between Windows (`CRLF`), Unix (`LF`), and old Macintosh (`CR`) values; these operations affect all of the lines of the current file
    * If your file has mixed line endings (some `CRLF` and some `LF`, for example), you can use this menu to fix it: if the desired line-ending is not greyed out, you can just select it, and any mixed line-endings will be converted to the chosen line ending; if the desired line-ending is greyed out, select one of the other line-endings, then switch back to the desired line-ending selection, and any mixed line-endings will be converted to the final line-ending choice.
* `Blank Operations >` ⇒ submenu with actions that trim or convert spaces and tab characters on ALL lines of the current file
    * `Trim Trailing Space`: removes any space or tab characters occurring at the end of a line, after any non-whitespace characters
    * `Trim Leading Space`: removes any space or tab characters occurring at the beginning of a line, before any non-whitespace characters
    * `Trim Leading and Trailing Spaces`: combines the functionalities of `Trim Trailing Space` and `Trim Leading Space` into one command
    * `EOL to Space`: replaces line-ending characters with a single space character (similar to `Join Lines` functionality, but acts upon the entire file rather than the active selection); note: "EOL" means "End Of Line" -- in other words, line-ending characters
    * `Remove Unnecessary Blank and EOL`: performs a combined `Trim Leading and Trailing Spaces` and `EOL to Space` operation
    * `TAB to Space`: replaces any tab characters with their equivalent number of spaces
    * `Space to TAB (All)`: consolidates space characters into an equivalent number of tab characters, wherever the spaces occur
    * `Space to TAB (Leading)`: consolidates space characters into an equivalent number of tab characters, but only where they occur before the first non-whitespace character on a line
    * NOTE about TAB-related commands: the "equivalent number" of spaces (or tab characters) is based on the [Settings > Preferences > Language > Tab Settings: Tab Size](../preferences/#language) for the active language of the current file
* `Paste Special >` ⇒ submenu with actions that pastes HTML or RTF, and special versions of copy/cut/paste which handle NULL and other binary characters
    * Note: The HTML and RTF actions paste the HTML and RTF source code from the HTML or RTF entries in the Windows Clipboard; it does _not_ apply HTML or RTF formatting to what appears to be plain text in the Notepad++ editor window.
* `On Selection >` ⇒ submenu with actions that use the currently-selected text as a filename or folder to open, or as a term for an internet search.  (Custom commands using the current selection can be added to the **Run** menu, using the [`<UserDefinedCommands>` section of `shortcuts.xml`](../config-files/#userdefinedcommands).)
* `Column Mode...` ⇒ dialog explaining [Column Mode](./#column-mode-column-editor)
* `Column Editor` ⇒ runs the [Column Editor](./#column-mode-column-editor) dialog, described above
* `Character Panel` ⇒ maps the 255 8-bit code points to their character for the given encoding
* `Clipboard History` ⇒ allows you to re-access recent copy/paste values (double-click a row to paste that value)
* `Set Read-Only` ⇒ toggles Notepad++'s read-only flag on the active file buffer.
    * If you click this menu entry once, it will add a checkmark `✔` to the menu entry, to show that it's currently read-only for Notepad++.  If you click this menu entry when there is already a checkmark `✔`, the checkmark will be cleared and Notepad++ will no longer consider this file read-only.
    * The state of this Notepad++ read-only flag is saved in the [session](../session/) file, so it will be remembered the next time the session is used.
    * *Note*: this toggle does _not_ affect the Windows Operating System's read-only attribute on the file; if Windows has marked this file as read-only, this menu entry will be greyed out and you cannot toggle it by clicking on it.  See the `Clear Read-only Flag` (below) for more on the OS flag.
* `Clear Read-Only Flag` ⇒ clears the Windows Operating System (OS) read-only attribute on a file.  
    * Once the OS read-only flag has been cleared, this menu option will be greyed out and clicking on it will do nothing.  
    * You cannot set the OS read-only flag using this menu in Notepad++; it has to be done through the OS (though Notepad++ scripting plugins are able to ask the OS to set the OS read-only flag on the file, like in [this example in the Community Forum](https://community.notepad-plus-plus.org/post/67312)).
    * If you use the OS to set the flag on a file that is open in Notepad++, and [**Settings > Preferences > MISC > File Status Auto-Detection**](../preferences/#misc) has been enabled, then Notepad++ will notice that it is now a read-only file, and not allow you to edit the file.
    * If you use the OS to set the flag on a file that is open in Notepad++, but [**Settings > Preferences > MISC > File Status Auto-Detection**](../preferences/#misc) has been disabled, then Notepad++ will _not_ notice that it was changed to read-only by the OS, and will blindly allow you to continue making changes; however, when you try to save and it sees that the file is read-only according to the OS, Notepad++ will notify you that you cannot save, and ask if you'd like to launch Notepad++ in Administrator mode to try to make the changes (if you do, the changes you made may be lost).
    * The current file's tab will have the "locked" icon (either the greyed-out disk icon by default, or the padlock icon if [**Settings > Preferences > General > ☑ Alternate icons**](../preferences/#general) has been checked on) whether the Windows OS read-only attribute is set, or the Notepad++ read-only flag has been set, or both.  The "locked" icon will change to a normal icon once neither the Windows OS read-only attribute nor the Notepad++ read-only flag are set (or equivalently, once both flags are cleared).

## Other Editing Commands and Shortcuts

There are also around a hundred editor commands that are accessible from keyboard shortcuts (though not all have a keyboard shortcut assigned by default).  Many of those commands are _not_ in the **Edit** menu (or any other Notepad++ menu).  These commands are listed in the [**Shortcut Mapper**](../preferences/#shortcut-mapper)'s **Scintilla commands** tab, and you can use the **Shortcut Mapper** to edit the assignments (add shortcuts or remove shortcuts) for these commands, whether they currently have a shortcut or not.

They have somewhat cryptic names, but if you look at the portion of the name to the right of the `SCI_` prefix, it does give you a hint.  For example, `SCI_CUT` shows the shortcuts for the traditional Cut command, and `SCI_LINECUT` will cut the whole current line, rather than just the selection.  The ones that have `LINE` in the name work on complete lines; if it has `CHAR` in the name, it works on individual characters; if it has `WORD` in the name, it works on whole words; and if it has `WORDPART` in the name, it works on partial words (also called "subwords", like `MyCoolFunction` has the three subwords `My`, `Cool`, and `Function`); if it has `PARA` in the name, it works on paragraphs (a paragraph ends with two consecutive newlines -- so a blank line between paragraphs);  `HOME`, `END`, `PAGEUP`, and `PAGEDOWN` correspond to the motions often associated with those keys on your keyboard.  If it has `CUT`, `COPY`, `PASTE`, and `SELECT` in the name, it indicates a variant of the normal editor actions of cutting, copying, pasting, and selecting text; if it has `DELETE` or `DEL` in the name, it will delete what is indicated in the rest of the name; if it has `EXTEND` in the name, it "extends" the selection (adds to the selection; these are usually the `Shift+`-modified commands for growing the selection).  That should be enough to help you understand the basics of what each of those commands do.

The Scintilla project, which Notepad++ uses to implement these traditional editor commands, has [documentation](https://www.scintilla.org/ScintillaDoc.html) for those  commands: you can look at the `SCI_xxxx` in the shortcut mapper, then search for that text on [their ScintillaDoc page](https://www.scintilla.org/ScintillaDoc.html) to find out more about that command.  

But with so many commands, and the fact that no documentation set is likely to ever explain _everything_ in the way that makes the most sense to you (what makes sense to one user might be really confusing to another), it might be fruitful to play with some of those commands to see for yourself what they do.  (Notepad++ doesn't let you edit text while the **Shortcut Mapper** is open: one possible method of doing this experimentation is to have two instances of Notepad++ running, and have the **Shortcut Mapper** open to the **Scintilla commands** in one instance, and play with using them in the editor in the other Notepad++ instance.)

## Printing

The **File > Print** action will pull up a Windows-standard print dialog, from which you can choose your printer and send your text to the selected printer.  Normally, it will print the whole document, but you can use the print dialog to choose only certain pages; if you have an active selection in the editor, only the selected text will be printed.  

The printing of the text is affected by the [**Settings > Preferences > Print**](../preferences/#print) settings, where you can decide things like whether or not to include line numbers in the printout, margin widths, extra text to print in the header and/or footer of every page, and the Colour Options will determine how your [Style Configurator theme's colors](../preferences/#style-configurator) will be propagated to the printed output.  It is up to you as the user to decide which printing settings are best to meet your needs, and will look best on your printed medium of choice.  Please note that with any themes with colored backgrounds, some of those colors will be printed to the background of your printed page unless you choose one of the Colour Options that does not print the background colour; but with darker themes, which use light text on dark backgrounds, if you _don't_ have it print the background colour, then it will be very light text on your white paper.  If you have a printer which allows you to print to PDF, that is a good way to see what the printout will really look like without using the paper and ink (and if you don't have a PDF printer available, your favorite search engine will show you plenty of commerical and freeware PDF printers by searching for something like "windows pdf printer" or "print to pdf").  
