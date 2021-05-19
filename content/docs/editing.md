---
title: Editing
weight: 30
---


## Column Mode & Column Editor
Using `Alt + Mouse dragging` or `Alt + Shift + Arrow keys` to switch to column mode:

![](/docs/images/columnMode.gif)

The Column Editor dialog allows you to insert text or numbers in every row of the active Column Mode selection:

![](/docs/images/columnEditor.gif)

* The `Text to Insert` will use the same text in every row.
* The `Number to Insert` will insert increasing numbers.
    * `Initial number` sets the starting number.
    * `Increase by` will change the step between numbers.  With a value of `0` (or if left empty), it will insert the same number every time.
    *  `Repeat` will repeat the same number _n_ times.  Defaults to 1 if left blank.
    * `☐ Leading zeros` will cause all the numbers to have the same number of digits, by adding leading zeros for the smaller values
    * `Format` chooses between **Dec** (0-9), **Hex** (0-9,A-F), **Oct** (0-7), or **Bin** (0-1).
        Note: that the numerical boxes above are always in decimal, even if a different format is chosen for display.  (Example: to get `F`-`1F`, column-select 17 rows and set the initial number to `15` -- it will not allow `F`.)

## Multi-Editing
Using `CTRL + Mouse clicking` if Multi-Editing mode is enabled.
To enable Multi-Editing mode:

![](/docs/images/multiEdit.gif)


## Dual View
To create Dual View, drag and drop any tab that you want it to be in another view (or right click on the tab) then choose "Move to Other View" command from the popup context menu.
Once you've got 2 views, you can move files between 2 views by drag-and-dropping.

![](/docs/images/move2view.gif)

## Clone Document
Drag and drop any tab that you want to clone (or right click on the tab) then choose "Clone to Other View" command from the popup context menu.
The cloned document is the same document as its original one, but with the separated views.

![](/docs/images/clonedDoc.gif)

## Edit Menu

Aside from the normal undo/redo/copy/paste entries, there are a number of sub-menus to the **Edit** menu, which group together various categories of editing-related commands, and a few other editing commands in the main **Edit** menu.

* `Copy to Clipboard >` ⇒ submenu with actions that copy current filename, path, or directory name to the clipboard
* `Indent >` ⇒ submenu with actions that increase or decrease the current line's indentation, based on [the syntax language's](../preferences/#language) tab/indent settings
* `Convert Case to >` ⇒ submenu with actions that change the case of the selected text (all UPPERCASE, all lowercase, and various mixed-case settings)
* `Line Operations >` ⇒ submenu with actions that typically work on lines (also known as "rows") of your document
    * There is a method for duplicating data:
        * `Duplicate Current Line` : duplicates the current line if no selection is active, or duplicates the selected text if a selection is active
    * There are two versions of the Remove Duplicates functionality:
        * `Remove Duplicate Lines`: leaves only the first instance of any full lines that have more than one copy anywhere in the active file; acts upon the line set spanned by the current selection, or the entire file if no active selection
        * `Remove Consecutive Duplicate Lines`: will only remove duplicates that are on the lines immediately following the first instance (still keeping the first instance); acts upon the line set spanned by the current selection, or the entire file if no active selection
        * NOTE: Duplicates removal is performed with the assumption that all line-endings in the file are uniform and match the current selection for the file being edited -- the quickest way to check that selection is to glance at the status bar, where the current line-ending type is shown either as `Windows (CR LF)`, `Unix (LF)` or `Macintosh (CR)`.  It might be desirable to check the line-ending types in your file before executing a sorting operation, and use the `Edit > EOL Conversion >` choices or right-click on the Stataus Bar's EOL indicator to fix the line endings if necessary.
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
        * NOTE: Sorting is performed with the assumption that all line-endings in the file are uniform and match the current selection for the file being edited -- the quickest way to check that selection is to glance at the status bar, where the current line-ending type is shown either as `Windows (CR LF)`, `Unix (LF)` or `Macintosh (CR)`.  It might be desirable to check the line-ending types in your file before executing a sorting operation, and use the `Edit > EOL Conversion >` choices or right-click on the Stataus Bar's EOL indicator to fix the line endings if necessary.
        * NOTE: If a [Column Mode](./#column-mode-column-editor) selection is active, the sort will re-order all the lines included in the selection, but the sort key (the text that decides the sort order) will be limited to what is inside the column selection. If the keys are identical on two lines, then the order of those two lines will not change (even if text outside of the selected key columns is different).
* `Comment/Uncomment >` ⇒ submenu with actions that add or remove comment syntax, based on the file's **Language** selection
* `Auto-Completion >` ⇒ submenu with actions that trigger auto-completion of function name, word, function parameter, and pathname, affected by [**Preferences > Auto-Completion** settings](../preferences/#auto-completion)
* `EOL Conversion >` ⇒ submenu with actions that convert line endings between Windows (`CRLF`), Unix (`LF`), and old Macintosh (`CR`) values; these operations affect all of the lines of the current file
    * If your file has mixed line endings (some `CRLF` and some `LF`, for example), you can use this menu to fix it: if the desired line-ending is not greyed out, you can just select it, and any mixed line-endings will be converted to the chosen line ending; if the desired line-ending is greyed out, select one of the other line-endings, then switch back to the desired line-ending selection, and any mixed line-endings will be converted to the final line-ending choice.
* `Blank Operations >` ⇒ submenu with actions that trim or convert spaces and tab characters on ALL lines of the current file
    * `Trim Trailing Space`: removes any space or tab characters occurring at the end of a line, after any non-whitespace characters
    * `Trim Leading Space`: removes any space or tab characters occurring at the beginning of a line, before any non-whitespace characters
    * `Trim Leading and Trailing Spaces`: combines the functionalities of `Trim Trailing Space` and `Trim Leading Space` into one command
    * `EOL to Space`: replaces line-ending characters with a single space character (similar to `Join Lines` functionality, but acts upon the entire file rather than the active selection); note: "EOL" means "End Of Line" -- in other words, line-ending characters
    * `Remove Unnecessary Blank and EOL` : performs a combined `Trim Leading and Trailing Spaces` and `EOL to Space` operation
    * `TAB to Space` : replaces any tab characters with their equivalent number of spaces
    * `Space to TAB (All)` : consolidates space characters into an equivalent number of tab characters, wherever the spaces occur
    * `Space to TAB (Leading)` : consolidates space characters into an equivalent number of tab characters, but only where they occur before the first non-whitespace character on a line
    * NOTE about TAB-related commands: the "equivalent number" of spaces (or tab characters) is based on the [Settings > Preferences > Language > Tab Settings: Tab Size](../preferences/#language) for the active language of the current file
* `Paste Special >` ⇒ submenu with actions that pastes HTML or RTF , and special versions of copy/cut/paste which handle NULL and other binary characters
    * Note: The HTML and RTF actions paste the HTML and RTF source code from the HTML or RTF entries in the Windows Clipboard; it does _not_ apply HTML or RTF formatting to what appears to be plain text in the Notepad++ editor window.
* `On Selection >` ⇒ submenu with actions that use the currently-selected text as a filename or folder to open, or as a term for an internet search.  (Custom commands using the current selection can be added to the **Run** menu, using the [`<UserDefinedCommands>` section of `shortcuts.xml`](../config-files/#userdefinedcommands).)
* `Column Mode...` ⇒ dialog explaining [Column Mode](./#column-mode-column-editor)
* `Column Editor` ⇒ runs the [Column Editor](./#column-mode-column-editor) dialog, described above
* `Character Panel` ⇒ maps the 255 8-bit code points to their character for the given encoding
* `Clipboard History` ⇒ allows you to re-access recent copy/paste values (double-click a row to paste that value)
* `Set Read-Only` or `Clear Read-Only Flag` ⇒ toggles whether the active file is set to Read-Only mode or not
