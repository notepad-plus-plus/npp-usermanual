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
    *  `Repeat` will will repeat the same number _n_ times.  Defaults to 1 if left blank.
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
* `Line Operations >` ⇒ submenu with actions that move or edit the current line; remove blank lines; and a variety of sorting algorithms.  For the sorting algorithms:
    * "Ascending" means smallest to largest (A-Z)
    * "Descending" means largest to smallest (Z-A)
    * "Lexicographically" means based on character codepoint, comparing one character at a time:
        * uppercase `Z` will sort before lowercase `a`
        * `10` will come before `2`, because it sorts character-by-character of each collection of characters
    * "As Integers" means that `10` will sort as being bigger than `2`
    * "As Decimals (Comma)" means it will recognize `10,234` and `9,876` as decimal numbers and sort them numerically
    * "As Decimals (Dot)" means it will recognize `10.234` and `9.876` as decimal numbers and sort them numerically
    * "Randomly" means that the selected lines will be placed in a random order, not determined by the characters or values on the line (added in v7.9)
* `Comment/Uncomment >` ⇒ submenu with actions that add or remove comment syntax, based on the file's **Language** selection
* `Auto-Completion >` ⇒ submenu with actions that trigger auto-completion of function name, word, function parameter, and pathname, affected by [**Preferences > Auto-Completion** settings](../preferences/#auto-completion)
* `EOL Conversion >` ⇒ submenu with actions that convert line endings between Windows (`CRLF`), Unix (`LF`), and old Macintosh (`CR`) values
* `Blank Operations >` ⇒ submenu with actions that trim or convert spaces and TABs
* `Paste Special >` ⇒ submenu with actions that pastes HTML or RTF , and special versions of copy/cut/paste which handle NULL and other binary characters
    * Note: The HTML and RTF actions paste the HTML and RTF source code from the HTML or RTF entries in the Windows Clipboard; it does _not_ apply HTML or RTF formatting to what appears to be plain text in the Notepad++ editor window.
* `On Selection >` ⇒ submenu with actions that use the currently-selected text as a filename or folder to open, or as a term for an internet search.  (Custom commands using the current selection can be added to the **Run** menu, using the [`<UserDefinedCommands>` section of `shortcuts.xml`](../config-files/#userdefinedcommands).)
* `Column Mode...` ⇒ dialog explaining [Column Mode](./#column-mode-column-editor)
* `Column Editor` ⇒ runs the [Column Editor](./#column-mode-column-editor) dialog, described above
* `Character Panel` ⇒ maps the 255 8-bit code points to their character for the given encoding
* `Clipboard History` ⇒ allows you to re-access recent copy/paste values (double-click a row to paste that value)
* `Set Read-Only` or `Clear Read-Only Flag` ⇒ toggles whether the active file is set to Read-Only mode or not
