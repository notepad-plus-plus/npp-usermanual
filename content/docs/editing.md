---
title: Editing
weight: 10
---

## Caret and Cursor

When editing in Notepad++, the insertion point in the editing window where your text will be typed is called the "caret", and is indicated by either a vertical bar or a box around the insertion location, depending on [Caret settings](../preferences/#editing-1). This is separate from the mouse cursor, which is the graphical pointer that moves freely as you move your mouse, not limited to the editing window, and can be used for changing the caret location and for interacting with the rest of the user interface. (Some also call the "caret" the "typing cursor" or "[text insertion/selection cursor](https://en.wikipedia.org/wiki/Caret_navigation)" or sometimes just the "cursor".  The name "caret" comes from the "[proofreader's caret](https://en.wikipedia.org/wiki/Caret_(proofreading))" `‸` or `^`, which is used to indicate where text needs to be inserted in a manuscript. The Notepad++ user interface and this manual both try to disambiguate the two by using "caret" for the typing cursor and "cursor" for the mouse cursor.)

## Typing Mode

As with many other text editors and other Windows applications, Notepad++ allows two different typing modes: "insertion mode" and "overwrite mode".
- In insertion mode, text is typed at the position of the caret, and any characters that came after the caret remain after the caret.  For example: if you had `ab‸cd` (where `‸` indicates the typing caret, not the literal `‸` character), then typing `xyz` would end up with `abxyz‸cd`.
- In overwrite mode, also known as "type over mode", text is typed at the position of the caret, and any characters that came after the caret will be overwritten.  For example: if you had `ab‸cd` (where `‸` indicates the typing caret, not the literal `‸` character), then typing `xyz` would end up with `abxyz‸`, with the `cd` no longer being there.

While in insertion mode, the caret-position indicator will be either a vertical bar (like `|`) or a shaded box (like `▒`), depending on [**Settings > Preferences > Editing 1 > Caret Settings**](../preferences/#editing-1).  When in overwrite mode, the caret-position indicator will be an underline (like `_`).  The speed of the blinking for the caret-position indicator can also be set in the same preferences section.

To toggle between insertion mode and overwrite mode, use the <kbd>Insert</kbd> key on your keyboard.  Alternatively, if the [Status Bar](../user-interface/#status-bar) is not hidden using **[Settings > Preferences > General](../preferences/#general) > Status Bar > `☐ Hide`**, one field in the Status Bar will show `INS` or `OVR` to indicate the typing mode, and clicking on that indicator will toggle the mode.

## Selection modes & Column Editor

Notepad++ has two modes for selecting text: stream selection and column mode selection.

Normally when you select text by <kbd>LeftClick+Drag</kbd> with the mouse, or <kbd>Shift+Arrow</kbd> key commands, you make what is called a stream selection.  In this mode, the text that is selected is contiguous, left-to-right, top-to-bottom.  There is another mode of selection called column mode that you can enter in order to select text that isn't contiguous horizontally, but rather vertically; column mode is also referred to as column-block, rectangular selection, or rectangular block selection, because it makes a rectangle of selected text.

Most users are accustomed to stream selection mode, because it behaves similarly to other applications.  But to clarify _exiting_ stream selection: If you have a stream selection, and click in the text (whether inside or outside the current selection) without using the <kbd>Ctrl</kbd> or <kbd>Shift</kbd> modifiers, then you will no longer have a stream selection, and your typing [caret](#caret-and-cursor "typing/insertion cursor") will move to wherever in the text that you clicked; similarly, using the keyboard to arrow or <kbd>PageUp</kbd>/<kbd>PageDown</kbd> away from the text, you will no longer have a stream selection, and your typing [caret](#caret-and-cursor "typing/insertion cursor") will move as appropriate for the movement key you used.  Either way, if you made your selection from left-to-right, then the typing [caret](#caret-and-cursor "typing/insertion cursor") will end up on the right side of the old selection when you exit selection mode; similarly, if you made your selection from right-to-left, the typing [caret](#caret-and-cursor "typing/insertion cursor") will end up on the left side of the old selection when you exit selection mode.

Whether you are in Column-Mode selection, or have a multiple-stream selection using Multi-Edit, the row or sub-selection that was added to the selection most-recently will be considered the "main selection"; certain actions (like the [**Edit > Blank Operations > Trim ...**](#edit) actions, below) will only work on the "main selection" instead of the whole selection; as of v8.6, **[Global Styles](/preferences/#global-styles) > Multi-selected text colour** and **Multi-edit carets colour** were added, so the earlier portions of the selection will use those colors, whereas the "main selection" will use the original **Selected text colour** and **Caret colour** -- so setting those text colours to different colours will help you quickly tell whether the selection is the "main selection" or one of the other portions of the multi-select or column selection.

The next sub-sections will provide more detail for the Column Mode selection, as that is the mode that needs more clarification for users unaccustomed to rectangular selection.

### Entering Column Mode

On the **Edit** menu is an entry **Column Mode** which when executed opens a text box window that explains the basics of column mode selection of text:

There are 3 ways to switch to column-select mode:

1. (Keyboard and Mouse)  Hold Alt while left-click dragging

2. (Keyboard only)  Hold Alt+Shift while using arrow keys

3. (Keyboard or Mouse)  Put [caret](#caret-and-cursor "typing/insertion cursor") at desired start of column block position, then execute the **Begin/End Select in Column Mode** command; move [caret](#caret-and-cursor "typing/insertion cursor") to desired end of column block position, then execute the **Begin/End Select in Column Mode** command again.

Other ways to enter column-mode exist, e.g. try Alt+Shift+PageDown, but knowing the intricacies of these -- what works and what doesn't -- takes some practice on the part of the user.

When column-selecting with the mouse, once you stop making a column mode selection by letting up on the mouse's left click button, the only way to then alter the shape of the rectangular selection is with the keyboard (<kbd>Alt+Shift+Arrows</kbd>).

To help you understand, here is an animation of using <kbd>Alt+LeftClick+Drag</kbd> or <kbd>Alt+Shift+Arrows</kbd> to make a selection in column mode:

![](../images/columnMode.gif)

### Leaving Column Mode

As soon as you make a [caret](#caret-and-cursor "typing/insertion cursor") movement that doesn't intentionally keep you in column mode, your selection mode returns to the stream selection mode (such as hitting an arrow key without also holding <kbd>Alt+Shift</kbd>).  Alternatively, hitting the <kbd>Esc</kbd> key will also leave Column Mode.

When you do leave Column Mode, the typing [caret](#caret-and-cursor "typing/insertion cursor") will be at the last corner of your selection. Thus, if you made your column selection from upper left to lower right of the rectangle, the [caret](#caret-and-cursor "typing/insertion cursor") will be in the lower right after you leave Column Mode; if you did your column selection from upper right to lower left, the [caret](#caret-and-cursor "typing/insertion cursor") will be in the lower left; if you do the column selection from lower left to upper right, then the [caret](#caret-and-cursor "typing/insertion cursor") will end up in the upper right; and if you do the column selection from lower right to upper left, then the [caret](#caret-and-cursor "typing/insertion cursor") will end up in the upper left.

### Editing In Column Mode

In column mode, typing will type the same thing in all the rows of the column.  If you copy/cut in column mode, then you copy/cut a rectangle of text, which can be pasted over an identical-sized rectangle elsewhere, or pasted into a separate document or separate application.  This is implemented for making working with rectangles of text (instead of whole lines of text) more convenient.

In column mode selection, when text is copied/cut, artificial line-ending characters are introduced into the text.  Thus, pasting in column mode can sometimes lead to surprising results, especially when you simply want the text inserted as if it isn't a column block.  Example: You copy a column block that spans 10 lines and then move the [caret](#caret-and-cursor "typing/insertion cursor") to column 1 on an empty line in your document and perform the paste.  The first line of the data from the paste ends up fine, but for the remaining lines, the paste has pushed existing text on subsequent lines to the right before inserting the new columns.  The solution here is to first (before the paste), use the Enter key to insert enough blank lines in the document so that the paste won't do this.

### Column Editor Dialog

The Column Editor dialog, accessed via **Edit > Column Editor**, allows you to insert text or numbers in every row of the active Column Mode selection:

![](../images/columnEditor.gif)

- The **Text to Insert** will use the same text in every row.
- The **Number to Insert** will insert increasing numbers.
    - **Initial number** sets the starting number.
    - **Increase by** will change the step between numbers.  With a value of `0` (or if left empty), it will insert the same number every time.
    - **Repeat** will repeat the same number _n_ times.  Defaults to 1 if left blank.
    - **Leading** is a pull-down selector that will allow choosing between no leading characters, leading zeros, or leading spaces.

        None | Zeros | Spaces
        ---|---|---
        ![](../images/colEdit-LeadingNone.png) | ![](../images/colEdit-LeadingZeros.png) | ![](../images/colEdit-LeadingSpaces.png)

        _examples shown with **View > Show Symbol > Show Spaces and Tab** to make the leading/trailing spaces obvious._

        (Prior to v8.5.2, the only option was a checkbox for **☐ Leading zeros**, so unchecked was equivalent to "None" and checkmarked was equivalent to "Zeros")

    - **Format** chooses between **Dec** (decimal: `0`-`9`), **Hex** (hexadecimal: `0`-`9`,`A`-`F`), **Oct** (octal: `0`-`7`), or **Bin** (binary: `0`-`1`).
        - In v8.8.5 and earlier, the numerical boxes above are always in decimal, even if a different format is chosen for display.  (Example: to get `F`-`1F`, column-select 17 rows and set the initial number to `15` -- it will not allow `F`.)
        - Starting in v8.8.6, the numerical boxes above are always in the format selected.  (Example: so if **Hex** is chosen, you would enter `B` in the **Increase by** to count using every eleventh hexadecimal number ⇒ `1`, `C`, `17`, `22`, `2D`, ...)
        - Starting in v8.8.6, there is a selector to choose whether hexadecimal will use Upper Case `A-F` or Lower Case `a-f` when outputting the numbers.

## Multi-Editing

Multi-Editing mode (available via mouse usage only) allows you to make multiple [caret](#caret-and-cursor "typing/insertion cursor")s by using <kbd>Ctrl+Click</kbd> for each additional [caret](#caret-and-cursor "typing/insertion cursor").  This allows performing the same editing actions (typing, copy/cut/paste/delete, arrowing through the text) in multiple locations, even if they aren't lined up in a nice column, or even if there are lines between the [caret](#caret-and-cursor "typing/insertion cursor")s that you don't want to affect.  You may place as many additional [caret](#caret-and-cursor "typing/insertion cursor")s as you want.

In addition to placing additional [caret](#caret-and-cursor "typing/insertion cursor")s, you may also make multiple selections.  After making an initial selection, do a <kbd>Ctrl+Click+Drag</kbd> operation to place a second selection in another location.  You may create as many such selections as you'd like.  A primary use for this type of selection might be so that you can copy several selections with one command, or to replace multiple selections with the same content if you begin typing or do a paste.

Starting in v8.6.1, if you <kbd>Ctrl+Click</kbd> at a previous multi-[caret](#caret-and-cursor "typing/insertion cursor") location, or <kbd>Ctrl+Click</kbd> within a previous multi-selection region, that [caret](#caret-and-cursor "typing/insertion cursor") or selection region will be removed, while leaving other portions of your multi-selection still active.  (This effectively allows you to "undo" a _portion_ of the multi-selection without having to redo everything, and is useful in complex multi-selections when you accidentally <kbd>Ctrl+Clicked</kbd> in the wrong place or changed your mind.)

Multi-Editing mode is only available when stream selection(s) are active; it doesn't work in conjunction with column-block selection.  Unlike stream selections, where with Multi-editing you can define two or more selections simultaneously, with column mode there can be only one active selection at a time.

Before v8.6, whether or not you can use Multi-Editing mode was determined by the [**Settings > Preferences > Editing > ☑ Enable Multi-Editing (Ctrl+Mouse click/selection)**](../preferences/#editing-2) checkbox: with it checkmarked, <kbd>Ctrl+Click</kbd> will add [caret](#caret-and-cursor "typing/insertion cursor") locations; with it not checkmarked, Multi-Editing is disabled.  In v8.6 - v8.6.2, Multi-Editing is always on, and that option was been removed; starting in v8.6.3, that option was returned, but is now at [**Settings > Preferences > Editing 2 > ☑ Enable Multi-Editing (Ctrl+Mouse click/selection)**](../preferences/#editing-2).

Starting in v8.6, Multi-Edit became the default, and was significantly enhanced.  The [Multi-Editing HowTo](#multi-editing-howto) (below) gives a tutorial in how to use this improved feature, including the new [**Edit** menu](#edit-menu) **...Multi-Select...** commands.

With the improved Multi-Edit, Column Mode selections are treated more like Multi-Edit selections; in order to disable this treatment in v8.6.1-v8.6.2, create the [zero-byte config file](../config-files/#other-configuration-files) `noColumnToMultiSelect.xml`; starting in v8.6.3, instead of a zero-byte file, there is a second option in the [**Editing 2**](../preferences/#editing-2) preferences to **☐ Enable Column Selection to Multi-Editing**.  (See the [warning (below)](#column-mode-to-multi-edit-warning).)

### Multi-Editing HowTo

The animation below is the demo of the feature that was published on the [v8.6 release announce](https://notepad-plus-plus.org/news/v86-20thyearanniversary/):

![multiedit](https://github.com/notepad-plus-plus/notepad-plus-plus/assets/90293/79b59d65-6862-4e5d-b2c2-1d19d0f2f551)

Here is a step-by-step guide that shows you how to transform from
```bash
# var1, var2, object1, object2, object3, flag1, flag2
```
to
```javascript
obj.var1 = param["var1"]
obj.var2 = param["var2"]
obj.object1 = param["object1"]
obj.object2 = param["object2"]
obj.object3 = param["object3"]
obj.flag1 = param["flag1"]
obj.flag2 = param["flag2"]
```
Once you understand how it work this part, the remain demo should be intuitive & easy to follow.

#### Step 1
Copy the line from `var1` to `flag2` and paste it, and add another comma at the end

![image](https://github.com/notepad-plus-plus/notepad-plus-plus/assets/90293/724c867f-78de-4086-9adc-9d5a5cf48481)


#### Step 2
Select the first `,` of `var1,`

![image](https://github.com/notepad-plus-plus/notepad-plus-plus/assets/90293/e544ff80-6758-449e-b762-d443471c22dd)


#### Step 3
Run **Edit > Multi-Select Next > Match Case Only** command 6 times.
Note: You can always run this command via the menu, but it'll be much easier to use the shortcut (I assigned ***Ctrl-E*** to it).
You can assign any available shortcut to **Multi-Select Next > Match Case Only** command via [Shortcut Mapper](../preferences/#shortcut-mapper).

![image](https://github.com/notepad-plus-plus/notepad-plus-plus/assets/90293/0ac09902-0abb-4b11-8c83-bfdaa0b1c69b)

#### Step 4
Type <kbd>DELETE</kbd> twice and then <kbd>ENTER</kbd> once, then <kbd>ArrowUp</kbd> to move all [caret](#caret-and-cursor "typing/insertion cursor")s up.

![image](https://github.com/notepad-plus-plus/notepad-plus-plus/assets/90293/de872b16-6b18-42cf-b993-93cb7370be63)


#### Step 5
Type `obj.`

![image](https://github.com/notepad-plus-plus/notepad-plus-plus/assets/90293/5f960695-a0d8-4f40-93b6-8eee3e164bba)

#### Step 6
Use <kbd>Ctrl+ArrowRight</kbd> to move the [caret](#caret-and-cursor "typing/insertion cursor")s to the end of the words.

![image](https://github.com/notepad-plus-plus/notepad-plus-plus/assets/90293/56aee7fc-cdc7-4603-9332-a9148ae882ef)

#### Step 7
Type ` = param[""]`

![image](https://github.com/notepad-plus-plus/notepad-plus-plus/assets/90293/66fb36a1-042e-4d88-88cf-b8f4278c3e79)


#### Step 8
Put your [caret](#caret-and-cursor "typing/insertion cursor") after `obj.` of the 1st line, the <kbd>Alt+Shift+ArrowDown</kbd> to the last line.
(Or you can use <kbd>Ctrl+ArrowLeft</kbd> to move [caret](#caret-and-cursor "typing/insertion cursor")s after `obj.` column.)

![image](https://github.com/notepad-plus-plus/notepad-plus-plus/assets/90293/d92f4e4a-1cd4-40c5-9990-43136db901f3)


#### Step 9
Use <kbd>Ctrl+Shift+ArrowRight</kbd> to multi-select the words, then copy them (<kbd>Ctrl+C</kbd>).

![image](https://github.com/notepad-plus-plus/notepad-plus-plus/assets/90293/abecd307-10ef-4ebb-b0fd-3670bbde9aed)

#### Step 10
Move all [caret](#caret-and-cursor "typing/insertion cursor")s to right by using <kbd>ArrowRight</kbd> to between `""`, then paste (<kbd>Ctrl+V</kbd>).

![image](https://github.com/notepad-plus-plus/notepad-plus-plus/assets/90293/5e91706b-96fe-4adb-80c1-6fb2aaf1d6f9)

#### Step 11
Use what you learned from Steps 1 through 10 to continue trying to mimic the behavior of the demo animation.

### Column-Mode to Multi-Edit Warning

When Notepad++ 8.6.3-and-newer converts a Column-Mode selection to a Multi-Edit selection, it honors the order of the selection: if your column selection was made from the bottom to the top, then, when it gets converted to Multi-Edit selection, the order of the Multi-Edit selection will be from the bottom to the top.

For example:
1. Create the file:
   ```
   abc
   def
   ghi
   ```
2. Put the cursor after the `g` and use <kbd>Alt+Shift+arrows</kbd> to select the column including `g`, `d`, and `a` from bottom to top.  This gives a normal column selection.
3. Cut that text, to put the column into the clipboard.
4. <kbd>ArrowRight</kbd> then <kbd>ArrowLeft</kbd> to convert from Column-mode to Multi-Edit.
5. Paste the text (<kbd>Ctrl+V</kbd>).
6. Your file now looks like:
   ```
   gbc
   def
   ahi
   ```

This might be non-intuitive behavior from your perspective, but it makes internal sense, because Multi-Edit honors the order you do things in for the list of selections, and you started your column at the bottom, so the `g` came before the `a`.  It is something to understand, if you are using the Column-Mode to Multi-Edit conversion feature of Notepad++.  If you want to have access to the Column-Mode-to-Multi-Edit conversion, but this behavior confuses you too much, then it is recommended that you always start Column-Mode selections from the top, rather than from the bottom.

## Dual View
To create Dual View, drag and drop any tab that you want it to be in another view (or right click on the tab) then choose "Move to Other View" command from the popup context menu.
Once you've got 2 views, you can move files between 2 views by drag-and-dropping.

![](../images/move2view.gif)

You can find more on moving to other views or instances in the [Views > Move / Clone](../views/#move-clone) section, and more on manipulating tabs through the tab bar in [Other Resources > Tabs](../other-resources/#tabs).

## Clone Document
Drag and drop any tab that you want to clone (or right click on the tab) then choose "Clone to Other View" command from the popup context menu.
The cloned document is the same document as its original one, but with the separated views.

![](../images/clonedDoc.gif)

You can find more on cloning to other views or instances in the [Views > Move / Clone](../views/#move-clone) section, and more on manipulating tabs through the tab bar in [Other Resources > Tabs](../other-resources/#tabs).

## Virtual Space

When editing a text document in Notepad++, there is potentially a blank area beyond the end of each line, which has no characters (not even space characters), because it's past the end-of-line characters.  By default, if you tried to click in that empty space, the [caret](#caret-and-cursor "typing/insertion cursor") (typing cursor) would move to the end of the line, instead of being placed where you clicked.  However, if you enabled **[Settings > Preferences > Editing 1](../preferences/#editing-1) > `☐ Enable virtual space`**, then if you clicked in that empty space, Notepad++ would place the [caret](#caret-and-cursor "typing/insertion cursor") there, beyond the end of the line; if you then typed some text, Notepad++ would fill the empty space between the end of the line and the [caret](#caret-and-cursor "typing/insertion cursor") with spaces, and the text you typed would go after those spaces.  (The Virtual Space feature was added in Notepad++ v8.4.3, so if you have an older Notepad++, you would need to upgrade to use this feature.)

This Virtual Space feature, however, does not influence blank space beyond the last line of the document: if you have fewer lines on your document than your screen allows, or if you enabled **[Settings > Preferences > Editing 1](../preferences/#editing-1) > `☐ Enable scrolling beyond last line`**, there could be empty space visible below the last numbered line in the Notepad++ document.  However, whatever the state of the Virtual Space option, if you click in the empty space below the last line, the [caret](#caret-and-cursor "typing/insertion cursor") will just go to the last line, and you cannot access any Virtual Space there -- so you cannot click a few lines below the end and start typing, and have Notepad++ fill in with blank lines or spaces. (You could, however, just hit <kbd>Enter</kbd> from the end of the last line, and you will then be able to continue your document into what used to be empty space.)

## Character Panel

The Character Panel, accessed through the **Edit > Character Panel** menu entry, allows the user to interact with the first 256 characters in the active [Encoding or Character set](../encoding/).

When opened, the Character Panel will be by default a docked window on the right-hand side of the Notepad++ main window, entitled `ASCII Codes Insertion Panel`. (This is a bit of a misnomer since ASCII is defined as values 0 - 127 and the panel shows values in the range  0 - 255.)

This panel contains a grid-like control that has five columns: `Value`, `Hex`, `Character`, `HTML Name`, `HTML Decimal` and `HTML Hexadecimal`.  The HTML columns show the various HTML entity formats for each character: `HTML Name` is the named entity, like `&quot;`.  `HTML Decimal` (or `HTML Code` in older versions) is the decimal entity, like `&#34;`.  And `HTML Hexadecimal` (new to v8.5.2) is the hexadecimal entity, like `&#x22;`.  (All three of those examples refer to the ASCII double quote `"` character.)

If input focus is moved to a line in the Character Panel and Enter is pressed, the character from the `Character` column will be inserted at the current position in the document being edited.  If the mouse is used there is more flexibility: an item from the grid that is double-clicked will be inserted.  For example, when double-clicking `&quot;` from the `HTML Name` column on the line of value 34, `&quot;` (as literal text) will be inserted at the current position in the active document -- so this can be used to insert the character number in decimal or hexadecimal, the character itself, or the HTML entity (named or decimal or hexadecimal) into the document being edited.

When Notepad++ is told to interpret a file as ANSI or any of the Character Sets (described in the [**Encoding**-menu docs](../encoding/)), the Character Panel shows information about the 256 8-bit character numbers (that is, the `Value`) for the character set selected.  Note that for all character sets, the 0-127 character values always represent the same character (the ASCII character); character values from 128-255 are character-set specific as to which character each value represents.  The panel offers an easy way to see value and character equivalence, and insert characters that don't exist on your keyboard.

When Notepad++ is told to interpret a file as Unicode (the entries starting with `UTF-8` or `UTF-16` in the [**Encoding** menu](../encoding/)), the Character Panel will show the same characters for values 128-255 as the default codepage character set on the user's system (viewable as `Current ANSI codepage` in the **? > Debug Info** menu entry).  In this case, for values 128-255, the `Value` column is meaningless -- only the `Character` shown is important.  If this panel is used to insert the character into the active document, the correct Unicode character bytes will be used instead of the value as in the simpler ANSI case.  For values from 0-127, the character/value pair _is_ meaningful, because for this range the ANSI set of characters -- the true ASCII set -- line up with the same characters and values in the Unicode set.

## Change History

Notepad++ has a column in the margin section which indicates which lines have been changed since the file was last loaded, controlled by a checkbox in [**Settings > Preferences > Margins/Border/Edge**](../preferences/#margins-border-edge) with the background color set by the [**Settings > Style Configurator > Global Styles > Change History margin**](../preferences/#global-styles) (new to v8.4.6)

![](../images/ChangeHistoryColors.png)

- When the file is first loaded (or a new file is created), no lines have a color in that margin column.
- If a line is changed (added or edited) since the most recent load or save, it will be orange. (This is `Modified but unsaved` in the image.)
- After the changes to the file are saved, any lines that have been changed since the file was loaded will be green. (This is `Modified but saved` in the image.)
    - _Note_: In v8.4.6 - v8.5.4, if you tell Notepad++ to reload the file from disk, _all_ lines would be green.  Multiple saves will leave those lines green, even if they weren't changed since the previous save.  The only way to get back to having no color in the margin is to close the file and reload it (easy enough to do with **File > Close** followed by **File > Recent Files > Restore Recent Closed Files**, or with default shortcuts, use <kbd>Ctrl+W</kbd> then <kbd>Ctrl+Shift+T</kbd>).  Starting in v8.5.5, reloading the file from disk will reset the Change History margin back to un-colored rather than all-green.
- If the file is saved, if you use **Undo** to go back to the previous modified state, it will be a pale green (some call it "olive" or "yellow-green").  (This is `Revert to modified` in the image.)
- If the file is saved, if you use **Undo** to go back to the original state of that line (the text it had when the file was originally loaded), it will be a pale blue (some call it "cyan"). (This is `Revert to original` in the image.)

## Edit Menu

The top of the **Edit** menu features typical editing commands which any Windows user should be familiar with:

* **Undo** - reverts the text to its content before the previous operation; can be used one or more times consecutively to step back through a document's textual history
* **Redo** - if **Undo** was executed previously, this will reinstate the change(s) previously undone; may be executed multiple times
* **Cut** - will remove any selected text from the document and place it on the Windows clipboard
* **Copy** - will put a copy of any selected text on the Windows clipboard; document content is unaltered
* **Paste** - if the Windows clipboard contains text, this will insert a copy of that text at the point of the [caret](#caret-and-cursor "typing/insertion cursor"); if text is selected when this command is executed, the selected text will be replaced by the text from the clipboard; if the clipboard does not contain text, nothing will happen
* **Delete** - will remove any selected text from the document
* **Select All** - selects all text in the document into a stream selection

Below the common editing commands are two that (each) allow text to be selected in two distinct steps:

* **Begin/End Select**
* **Begin/End Select in Column Mode**

Normally text selection is a dedicated process -- once a selection is started, the only thing you can do is to complete it, before moving on to other actions.  But sometimes it is useful to do other things, in particular document navigation actions, between defining the starting point of a selection and actually bringing the selection into existence.

The **Begin/End Select** commands are useful when making huge selections of text; rather than holding Shift while using arrow keys or the mouse to select text, and be at the mercy of the system scroll speed as you watch the viewport scroll interminably to locate the far-away ending point for the selection you started, you can use the **Begin/End Select** feature.  Execute **Begin/End Select** once to set a starting point of a future selection, then use a [caret](#caret-and-cursor "typing/insertion cursor") movement command(s) (example: Ctrl+End to move quickly to the end of a document), and finally run **Begin/End Select** a second time to create a text selection between the two far-away document positions.

After you use **Begin/End Select** the first time to set the starting point, the menu item for the command will appear "checkmarked" to let you know that you have started the process, and need to execute the command a second time to define the selection end point and show the text as selected.

**Begin/End Select in Column Mode** works very similarly to the normal version of the command, with the exception being that when the two-stage command is completed, a column mode selection will be made rather than a stream selection.  If you execute the first part of one of the commands, and then change your mind about the type of selection needed, you must complete the in-progress command before you will be allowed to begin the one of the opposite type.  (New to v8.5.)

Below the **Begin/End Select** entries, there are a number of sub-menus to the **Edit** menu, which group together various categories of editing-related commands, and a few other editing commands in the main **Edit** menu.

* **Insert >** ⇒ submenu with actions that insert the date and time (new to v8.1.4)
    * **Date Time (short)** ⇒ like `12:46 PM 8/21/2021` (new to v8.1.4)
    * **Date Time (long)** ⇒ like `12:46 PM Saturday, August 21, 2021`) (new to v8.1.4)
    * **Date Time (custom)** ⇒ can insert a date with a customized format, as defined in the [**Settings > Preferences > Multi-Instance & Date**](../preferences/#multi-instance-and-date) dialog
* **Copy to Clipboard >** ⇒ submenu with actions that copy current filename, path, or directory name to the clipboard
* **Indent >** ⇒ submenu with actions that increase or decrease the current line's indentation, based on [the syntax language's](../preferences/#language) tab/indent settings
    - **Increase Line Indent** ⇒ Inserts a tab or equivalent number of spaces at the beginning of the line (any whitespace already at the beginning of the line will still be there, coming _after_ the new tab or spaces that was inserted)
    - **Decrease Line Indent** ⇒ Removes a tab or equivalent number of spaces at the beginning of the line (if there aren't enough leading space characters to remove an entire tabwidth, all the leading space characters will be removed)
* **Convert Case to >** ⇒ submenu with actions that change the case of the selected text
    - **Uppercase** ⇒ convert to all uppercase: `StArT mIxEd` ⇒ `START MIXED`
    - **lowercase** ⇒ convert to all lowercase: `StArT mIxEd` ⇒ `start mixed`
    - **Proper Case** ⇒ first character of every word is made uppercase, all others made lowercase: `isCharAlpha NMumericW` ⇒ `Ischaralpha Nmumericw`
    - **Proper Case (blend)** ⇒ first character of every word is made uppercase, all others left alone: `isCharAlpha NMumericW` ⇒ `IsCharAlpha NMumericW`
    - **Sentence case** ⇒ first character of each sentence is made uppercase, all others made lowercase: `tHis Is A Sentence. iS tHis Second?` ⇒ `This is a sentence. Is this second?`
    - **Sentence case (blend)** ⇒ first character of each sentence is made uppercase, all others left alone: `tHis Is A Sentence. iS tHis Second?` ⇒ `THis Is A Sentence. IS tHis Second?`
    - **iNVERT cASE** ⇒ any that were uppercase are changed to lowercase, and any that were lowercase are changed to uppercase: `StArT mIxEd` ⇒ `sTaRt MiXeD`
    - **ranDOm CasE** ⇒ each character gets a random case: `StArT mIxEd` ⇒ `StaRt mIxeD`
* **Line Operations >** ⇒ submenu with actions that typically work on lines (also known as "rows") of your document
    * There is a method for duplicating data:
        * **Duplicate Current Line**: Duplicates the current line. (Prior to v8.6, if a selection was active it would duplicate just that selection, but starting in v8.6, selection state is ignored for this menu command; if you want the old behavior, the <kbd>Ctrl+D</kbd> shortcut is, by default, still assigned to the selection-aware duplication, under `SCI_SELECTIONDUPLICATE` in the [Shortcut Mapper](../preferences/#shortcut-mapper).)
    * There are two versions of the Remove Duplicates functionality:
        * **Remove Duplicate Lines**: leaves only the first instance of any full lines that have more than one copy anywhere in the active file; acts upon the line set spanned by the current selection, or the entire file if no active selection
            - _Note_: Because of the way it's implemented, this command also clears all bookmarks.
        * **Remove Consecutive Duplicate Lines**: will only remove duplicates that are on the lines immediately following the first instance (still keeping the first instance); acts upon the line set spanned by the current selection, or the entire file if no active selection
            - _Note_: Because of the way it's implemented, this command does not clear all bookmarks.  However, if a bookmarked line is one of the consecutive duplicate lines removed, that bookmark will remain on the old line number (which means it is now bookmarking whatever text used to be _after_ that line).
        * NOTE: Duplicates removal is performed with the assumption that all line-endings in the file are uniform and match the current selection for the file being edited -- the quickest way to check that selection is to glance at the status bar, where the current line-ending type is shown either as `Windows (CR LF)`, `Unix (LF)` or `Macintosh (CR)`.  It might be desirable to check the line-ending types in your file before executing a sorting operation, and use the **Edit > EOL Conversion >** choices or right-click on the Status Bar's EOL indicator to fix the line endings if necessary.
    * There are methods for splitting lines and joining lines together:
        * **Split Lines**: will insert a line-ending into a long line(s): if there is one or more [Vertical Edge](../preferences/#margins-border-edge) value specified, it will split at the right-most Vertical Edge; otherwise, it will split at the current size of the editor window.  It operates on the lines spanned by the current stream selection or the single line of the [caret](#caret-and-cursor "typing/insertion cursor") if no stream selection is currently active.
        * **Join Lines**: will combine the lines touched by the active stream selection by replacing line-endings with a single space character. It requires an active stream selection that spans two or more lines.
    * There are commands for removing lines
        * **Remove empty lines**: will remove all lines containing no characters from the entire document
        * **Remove empty lines (Containing Blank characters)**: will remove all lines containing no characters from the entire document; if a line contains only space or tab characters that line will be removed as well
    * There are commands for changing the order of existing lines:
        * **Move Up Current Line**: will swap the current line with the line above it, effectively moving the line of the [caret](#caret-and-cursor "typing/insertion cursor") up one row in the document; if a selection spanning lines is active upon invocation, it will move those lines touched by the selection up as a group
        * **Move Down Current Line**: will swap the current line with the line below it, effectively moving the line of the [caret](#caret-and-cursor "typing/insertion cursor") down one row in the document; if a selection spanning lines is active upon invocation, it will move those lines touched by the selection down as a group
        * **Reverse Line Order**: will take the selected lines (or all of the lines of the current document if no active selection) and will order them reversely (i.e. flipped) from their existing order (added in v8.0.0)
        * **Randomize Line Order**: will take the selected lines (or all of the lines of the current document if no active selection) and place them in an unpredictable order
    * There are a variety of sorting algorithms:
        * **Ascending** means smallest to largest (A-Z)
        * **Descending** means largest to smallest (Z-A)
        * **Lexicographically** (or **Lex.**) means based on character codepoint, comparing one character at a time:
            * All uppercase letters will sort before any lowercase letter, so uppercase `Z` will sort before lowercase `a`
            * The sequence `10` will sort before `2`, because it sorts character-by-character of each collection of characters, and the character `1` comes before the character `2`
        * **Ignoring case** means that lowercase `a` will sort the same as uppercase `A`, and both will come before either `Z` or `z`
        * **Locale Order** provides an alphabetical sort which incorporates language-sensitive rules so that words and phrases will generally be sorted as expected. (New to v8.8.1.)
        * **As Integers** means that `10` will sort as being bigger than `2`
            - Note that sorting as integers will sort IP addresses (like `192.168.0.1` and `8.8.8.8`) reasonably (as `8.8.8.8` before `192.168.0.1`).
            - Note that if you have the same non-numeric prefixes on your numbers (like `xyz9` and `xyz11`), it will sort the numeric portion as integers.
            - Note that if you have right-aligned numbers, with leading spaces before numbers of different lengths, the spaces will change the ordering from what you expect:
                ```
                   1
                  10
                 100
                1000
                ```
                will be sorted as
                ```
                 100
                  10
                   1
                1000
                ```
                because integers prefixed by spaces come before integers without spaces (because spaces are lexicographically earlier than digits; in this example, that means `1000` is last, because it had no space prefix), but integers prefixed with one space will be sorted before integers prefixed with two spaces.
        * **As Decimals (Comma)** means it will recognize `10,234` and `9,876` as decimal numbers and sort them numerically
        * **As Decimals (Dot)** means it will recognize `10.234` and `9.876` as decimal numbers and sort them numerically
        * NOTE: Except for **Locale** sorts, which do not impose this restriction, sorting is performed with the assumption that all line-endings in the file are uniform and match the current selection for the file being edited -- the quickest way to check that selection is to glance at the status bar, where the current line-ending type is shown either as `Windows (CR LF)`, `Unix (LF)` or `Macintosh (CR)`.  It might be desirable to check the line-ending types in your file before executing a sorting operation, and use the **Edit > EOL Conversion >** choices or right-click on the Status Bar's EOL indicator to fix the line endings if necessary.
        * NOTE: If a [Column Mode](./#selection-modes-column-editor) selection is active, the sort will re-order all the lines included in the selection, but the sort key (the text that decides the sort order) will be limited to what is inside the column selection. If the column selection is zero-width (that is, it contains no text, consisting only of a caret extending through multiple lines), the sort key for each line begins with the character to the right of the caret in that line and extends to the end of the line. This column-selection-based sort will be a "stable sort": if the keys are identical on two lines, then the order of those two lines will not change, even if text outside of the selected key columns is different. Except for **Locale** sorts, which do not impose this restriction, column selections will not always work as expected if the text within or to the left of the selection contains tab characters, characters comprised of varying numbers of bytes (such as non-ASCII characters in Unicode documents), or characters of varying widths (such as when a proportional font is in use).
        * NOTE: **Locale** sorts are based on the current user locale (and preferred sort order, for locales which support more than one), which can be set in the **Region** applet in Windows **Control Panel**. Most users will never need to change those settings, but some multi-lingual users might find that different settings are required when working in different languages. There is no need to close Notepad++ after changing the user locale: the new locale takes effect immediately upon being saved in the Windows dialog. **Locale** sorts are stable sorts which use the user locale and the NORM_LINGUISTIC_CASING, LINGUISTIC_IGNORECASE and SORT_DIGITSASNUMBERS flags described for [LCMapStringEx](https://learn.microsoft.com/en-us/windows/win32/api/winnls/nf-winnls-lcmapstringex) to generate sort keys.
* **Comment/Uncomment >** ⇒ submenu with actions that add or remove comment syntax, based on the file's **Language** selection.
  This makes use of the `commentLine`, `commentStart`, and `commentEnd` attributes of the active Language as defined in [langs.xml](../config-files/#keyword-lists-langsxml) to define the characters to use for making or clearing line comments (`commentLine`) and block comments (`commentStart` and `commentEnd`):
    - The **Single line** comment commands all use the string defined as `commentLine` as the prefix for each commented line.
    - The **Block Comment/Uncomment** commands put the `commentStart` string before the selected text, and the `commentEnd` string after the selected text.
      If the `commentStart` and `commentEnd` attributes are not defined, the **Block** commands will instead individually prefix each line of the block with the `commentLine` string.
    - Some languages have multiple block comment syntaxes, but Notepad++'s **Comment/Uncomment** commands can only implement one.  You can edit your `langs.xml` to define the strings that _you_ want to use.
    - If your language currently is missing one or more of those attributes in the `langs.xml`, you can edit `langs.xml` following the advice in ["Editing Configuration Files"](../config-files/#editing-configuration-files) and add in those attributes for your language; after saving and restarting Notepad++, the **Comment/Uncomment** commands will use the strings you defined.
* **Auto-Completion >** ⇒ submenu with actions that manually trigger [auto-completion](../auto-completion/) of function name, word, function parameter, and pathname.  While the automatic completion is affected by [**Preferences > Auto-Completion** settings](../preferences/#auto-completion) for setting minimum number of characters, and enabling which of the completions happen automatically, when you manually trigger one of the auto-completion actions through this menu or keyboard shortcut equivalents, completion will happen regardless of those settings (so you can manually trigger when there's fewer characters than the auto-trigger threshold, or you can manually trigger function completion when only word completion is active).
* **EOL Conversion >** ⇒ submenu with actions that convert line endings between Windows (`CR LF`), Unix (`LF`), and old Macintosh (`CR`) values; these operations affect all of the lines of the current file
    * If your file has mixed line endings (some `CR LF` and some `LF`, for example), you can use this menu to fix it: if the desired line-ending is not greyed out, you can just select it, and any mixed line-endings will be converted to the chosen line ending; if the desired line-ending is greyed out, select one of the other line-endings, then switch back to the desired line-ending selection, and any mixed line-endings will be converted to the final line-ending choice.
* **Blank Operations >** ⇒ submenu with actions that trim or convert spaces and tab characters.
    * _NOTE: All the **Blank Operations** commands will default to doing a global change through the whole document.  Starting in Notepad++ v8.4.9, if there is a single active stream selection, the **Blank Operation** change will only apply to the selected text; if there is a multi-stream selection, then only the last selection added to the multi-stream (the "main selection") will be affected; if there is a column-mode selection, no trimming or tab-conversion will occur._
    * **Trim Trailing Space**: removes any space or tab characters occurring at the end of a line, after any non-whitespace characters
    * **Trim Leading Space**: removes any space or tab characters occurring at the beginning of a line, before any non-whitespace characters
    * **Trim Leading and Trailing Spaces**: combines the functionalities of **Trim Trailing Space** and **Trim Leading Space** into one command
    * **EOL to Space**: replaces line-ending characters with a single space character (similar to **Join Lines** functionality, but acts upon the entire file rather than the active selection); note: "EOL" means "End Of Line" -- in other words, line-ending characters
    * **Trim Both and EOL to Space**: performs a combined **Trim Leading and Trailing Spaces** and **EOL to Space** operation (known as **Remove Unnecessary Blank and EOL** before v8.4.9; the newer phrase **Trim Both** is shorthand for **Trim Both Leading and Trailing Spaces**)
        - Note about Trim-related commands: the trim occurs for the line of the selection, even if the selection doesn't include those leading and/or trailing spaces.  _Example:_ if the line is some spaces, the text `words here`, and some more spaces, then even if the selection is just `words`, the trims will happen on the leading and/or trailing spaces, based on which menu command was chosen.
    * **TAB to Space**: replaces any tab characters with their equivalent number of spaces
    * **Space to TAB (All)**: consolidates space characters into an equivalent number of tab characters, wherever the spaces occur
    * **Space to TAB (Leading)**: consolidates space characters into an equivalent number of tab characters, but only where they occur before the first non-whitespace character on a line
        - Note about TAB-related commands: the "equivalent number" of spaces (or tab characters) is based on the [**Settings > Preferences > Language > Tab Settings > Tab Size**](../preferences/#language) for the active language of the current file, and will be enough spaces to take you to the next "tab stop".

            If the current language has a tab setting of 4 spaces per tab, then the tab stops are at 1, 5, 9, 13, and so on.

            If you have a tab at column 1, 2, 3, or 4, it will be wide enough so that the next character will be at column 5; and if you convert tabs to spaces, it will replace it with 4, 3, 2, or 1 space (respectively), so that the next character will still be at column 5.

            Similarly, tabs at columns 5, 6, 7, or 8 will be displayed as wide as (or converted to spaces as) 4, 3, 2, or 1 spaces (respectively), so that the next character will be at column 9.

            These examples are shown in the screenshot below, where [**View > Show Symbol > Whitespace and Tab**](../views/#show-symbol) shows the tabs as an orange arrow (`→`) and the spaces as an orange middot (`·`); the left shows it with tab characters; the right shows it with those tabs converted to spaces:

            ![](../images/edit-tab-stops.png)

            If you want a specific number of space characters to replace each tab character, instead of the above-described fill-to-tabstop behavior, you should use a replacement operation in Extended or Regular Expression search mode to replace `\t` with the number of space characters you desire.

* **Paste Special >** ⇒ submenu with actions that pastes HTML or RTF, and special versions of copy/cut/paste which handle NULL and other binary characters
    * Note: The HTML and RTF actions paste the HTML and RTF source code from the HTML or RTF entries in the Windows Clipboard; it does _not_ apply HTML or RTF formatting to what appears to be plain text in the Notepad++ editor window.
* **On Selection >** ⇒ submenu with actions that use the currently-selected text as a filename or folder to open, or as a term for an internet search.  (Custom commands using the current selection can be added to the **Run** menu, using the [`<UserDefinedCommands>` section of `shortcuts.xml`](../config-files/#userdefinedcommands).)
* **Multi-Select All >** ⇒ submenu with actions that work with the current selection or word under the [caret](#caret-and-cursor "typing/insertion cursor")
    - **Ignore Case & Whole Word** ⇒ If nothing is selected, it will determine the current word under the [caret](#caret-and-cursor "typing/insertion cursor"), and do a Multi-Select which finds all matches which match that string regardless of case, and regardless of whether the other matches are a whole word or not.  If a word or string is selected, it will Multi-Select all the strings which match the current selection.
    - **Match Case Only** ⇒ If nothing is selected, it will determine the current word under the [caret](#caret-and-cursor "typing/insertion cursor"), and do a Multi-Select which finds all matches of that word, as long as the case exactly matches.  If a word or substring is selected, it will Multi-Select all the strings which match that selection, paying attention to case.
    - **Whole Word Only** ⇒ If nothing is selected, it will determine the current word under the [caret](#caret-and-cursor "typing/insertion cursor"), and do a Multi-Select which finds all whole-word matches, regardless of case.  If a word is selected, it will Multi-Select all the whole-words which match that selection, ignoring case.
    - **Match Case & Whole Word** ⇒ If nothing is selected, it will determine the current word under the [caret](#caret-and-cursor "typing/insertion cursor"), and do a Multi-Select which finds all whole-word matches which match that string, including case.  If a word is selected, it will do a Multi-Select which finds all whole-word matches which match that string, including case.
* **Multi-Select Next >** ⇒ submenu with actions that add one more instance to the current multi-select
    - Each submenu entry will be analogous to the **Multi-Select All** described above, but will only add a single match to the Multi-Selection (the next to occur after the current selection), rather than all matches.
* **Undo the Latest Added Multi-Select** ⇒ If you have a Multi-Selection active, this command will take out the most-recently added substring.  (For example, if you had the text `the quick brown fox jumped over the lazy dog` and Multi-Selected `quick` then `dog`, then ran this command, your selection would only include `quick`.)
* **Skip Current & Go to Next Multi-Select** ⇒ If you have text selected, this command will unselect the current string, and Multi-Select the first instance _after_ this one that matches what had been selected.
* **Column Mode...** ⇒ dialog explaining [Column Mode](./#selection-modes-column-editor)
* **Column Editor** ⇒ runs the [Column Editor](./#selection-modes-column-editor) dialog, described above
* **Character Panel** ⇒ toggles the [Character Panel](#character-panel), described above
* **Clipboard History** ⇒ allows you to re-access recent copy/paste values (double-click a row to paste that value)
* **Read-Only in Notepad++ >** Sub-menu actions control Notepad++'s read-only flag. (Converted to sub-menu in v8.8.6.)
    - **Read-Only on Current Document**: Toggles Notepad++'s read-only flag on the active file buffer.
        - If you click this menu entry, it will add a checkmark `✔` to the menu entry and Notepad++ will not allow the file to be edited (that is, it is currently read-only for Notepad++).  If you click this menu entry when there is already a checkmark `✔`, the checkmark will be removed and Notepad++ will no longer consider this file read-only.
            - When a file is locked, the file's tab will have either a greyed-out disk icon ([original-style icons](../preferences/#tab-bar) in [Light Mode](../preferences/#dark-mode)) or a lock symbol (with [alternate icons](../preferences/#tab-bar) or in [Dark Mode](../preferences/#dark-mode)).
        - The state of this Notepad++ read-only flag is saved in the [session](../session/) file, so it will be remembered the next time the session is used.
        - *Note*: this toggle does _not_ affect the Windows Operating System's read-only attribute on the file; if Windows has marked this file as read-only, this menu entry will be greyed out and you cannot toggle it by clicking on it.  See the **Read-Only Attribute in Windows** (below) for more on the OS flag.
        - In v8.8.1 and earlier, this was called **Set Read-Only**, and was directly in the top-level **Edit** menu rather than a submenu.
        - In v8.8.2-v8.8.5, this was called **Read-Only in Notepad++**, and was directly in the top-level **Edit** menu rather than a submenu.
    - **Read-Only for All Documents**:
        - Sets the read-only status on all documents, rather than just the active document.  (Equivalent to checkmarking **Read-Only on Current Document** for each open document.)
    - **Clear Read-Only for All Documents**:
        - Clears the read-only status on all documents.  (Equivalent to clearing **Read-Only on Current Document** for each open document.)
* **Read-Only Attribute in Windows** ⇒ toggles the Windows Operating System (OS) read-only attribute on a file.
    - When a file is locked in Windows, this menu-entry will have a checkmark `✔`, and the tab will have an icon of a disk with an `F` ([original-style icons](../preferences/#tab-bar) in [Light Mode](../preferences/#dark-mode)) or a lock with an `F` (with [alternate icons](../preferences/#tab-bar) or in [Dark Mode]](../preferences/#dark-mode)) (new to v8.8.2).
    - In v8.8.1 and earlier, this was called **Clear Read-Only Flag**
        - You cannot set the OS read-only flag using this menu in Notepad++; it has to be done through the OS (though Notepad++ scripting plugins are able to ask the OS to set the OS read-only flag on the file, like in [this example in the Community Forum](https://community.notepad-plus-plus.org/post/67312)).
        - Once the OS read-only flag has been cleared, this menu option will be greyed out and clicking on it will do nothing.
        - If you use the OS to set the flag on a file that is open in Notepad++, and [**Settings > Preferences > MISC > File Status Auto-Detection**](../preferences/#misc) has been checked, then Notepad++ will notice that it is now a read-only file, and not allow you to edit the file.
        - If you use the OS to set the flag on a file that is open in Notepad++, but [**Settings > Preferences > MISC > File Status Auto-Detection**](../preferences/#misc) has been unchecked, then Notepad++ will _not_ notice that it was changed to read-only by the OS, and will blindly allow you to continue making changes; however, when you try to save and it sees that the file is read-only according to the OS, Notepad++ will notify you that you cannot save, and ask if you'd like to launch Notepad++ in Administrator mode to try to make the changes (if you do, the changes you made may be lost).
        - The current file's tab will have the "locked" icon (either the greyed-out disk icon by default, or a padlock icon if [Dark Mode](../preferences/#dark-mode) is active or if [**Settings > Preferences > General > ☑ Alternate icons**](../preferences/#general) has been checked on) whether the Windows OS read-only attribute is set, or the Notepad++ read-only flag has been set, or both.  The "locked" icon will change to a normal icon once neither the Windows OS read-only attribute nor the Notepad++ read-only flag are set (or equivalently, once both flags are cleared).

## Other Editing Commands and Shortcuts

There are also around a hundred editor commands that are accessible from keyboard shortcuts (though not all have a keyboard shortcut assigned by default).  Many of those commands are _not_ in the **Edit** menu (or any other Notepad++ menu).  These commands are listed in the [**Shortcut Mapper**](../preferences/#shortcut-mapper)'s **Scintilla commands** tab, and you can use the **Shortcut Mapper** to edit the assignments (add shortcuts or remove shortcuts) for these commands, whether they currently have a shortcut or not.

They have somewhat cryptic names, but if you look at the portion of the name to the right of the `SCI_` prefix, it does give you a hint.  For example, `SCI_CUT` shows the shortcuts for the traditional Cut command, and `SCI_LINECUT` will cut the whole current line, rather than just the selection.  The ones that have `LINE` in the name work on complete lines; if it has `CHAR` in the name, it works on individual characters; if it has `WORD` in the name, it works on whole words; and if it has `WORDPART` in the name, it works on partial words (also called "subwords", like `MyCoolFunction` has the three subwords `My`, `Cool`, and `Function`); if it has `PARA` in the name, it works on paragraphs (a paragraph ends with two consecutive newlines -- so a blank line between paragraphs);  `HOME`, `END`, `PAGEUP`, and `PAGEDOWN` correspond to the motions often associated with those keys on your keyboard.  If it has `CUT`, `COPY`, `PASTE`, and `SELECT` in the name, it indicates a variant of the normal editor actions of cutting, copying, pasting, and selecting text; if it has <kbd>DELETE</kbd> or `DEL` in the name, it will delete what is indicated in the rest of the name; if it has `EXTEND` in the name, it "extends" the selection (adds to the selection; these are usually the `Shift+`-modified commands for growing the selection).  That should be enough to help you understand the basics of what each of those commands do.

The Scintilla project, which Notepad++ uses to implement these traditional editor commands, has [documentation](https://www.scintilla.org/ScintillaDoc.html) for those  commands: you can look at the `SCI_xxxx` in the shortcut mapper, then search for that text on [their ScintillaDoc page](https://www.scintilla.org/ScintillaDoc.html) to find out more about that command.

But with so many commands, and the fact that no documentation set is likely to ever explain _everything_ in the way that makes the most sense to you (what makes sense to one user might be really confusing to another), it might be fruitful to play with some of those commands to see for yourself what they do.  (Notepad++ doesn't let you edit text while the **Shortcut Mapper** is open: one possible method of doing this experimentation is to have two instances of Notepad++ running, and have the **Shortcut Mapper** open to the **Scintilla commands** in one instance, and play with using them in the editor in the other Notepad++ instance.)

### Scintilla SCI_xxx "Keyboard Commands"

Scintilla's documentation on the "[Keyboard Commands](https://www.scintilla.org/ScintillaDoc.html#KeyboardCommands)" can be rather sparse, and skips some of their commands, so the following table attempts to summarize each of those commands:

Message                        | Description
-------------------------------|-------------
`SCI_BACKTAB`                  | In the middle of text, moves [caret](#key "typing cursor") [one tab](#key "TAB character or ℕ space characters") earlier; if at the first non-space character on a line, un-indents by [one tab](#key "TAB character or ℕ space characters")
`SCI_CANCEL`                   | Cancels autocompletions or calltips; if there are multiple selections, gets rid of all but the main selection; if there is a rectangle selection, gets rid of the selection and places [caret](#key "typing cursor") at the end of the rectangle (last corner selected)
`SCI_CHARLEFT`                 | Moves [caret](#key "typing cursor") one character left
`SCI_CHARLEFTEXTEND`           | Moves [caret](#key "typing cursor") one character left, extending normal stream-mode selection
`SCI_CHARLEFTRECTEXTEND`       | Moves [caret](#key "typing cursor") one character left, extending rectangle (column-mode) selection
`SCI_CHARRIGHT`                | Moves [caret](#key "typing cursor") one character right
`SCI_CHARRIGHTEXTEND`          | Moves [caret](#key "typing cursor") one character right, extending normal stream-mode selection
`SCI_CHARRIGHTRECTEXTEND`      | Moves [caret](#key "typing cursor") one character right, extending rectangle (column-mode) selection
`SCI_DELETEBACK`               | Moves [caret](#key "typing cursor") one character back, deleting the character it moved over (normal <kbd>Backspace</kbd> action); if [caret](#key "typing cursor") was at the beginning of the line, it will delete the newline and merge the current line with the previous line
`SCI_DELETEBACKNOTLINE`        | Moves [caret](#key "typing cursor") one character back, deleting the character it moved over, unless [caret](#key "typing cursor") is at the beginning of a line
`SCI_DELLINELEFT`              | Deletes line from [caret](#key "typing cursor") to beginning of line ([caret](#key "typing cursor") will be at beginning of the line)
`SCI_DELLINERIGHT`             | Deletes line from [caret](#key "typing cursor") to end of line ([caret](#key "typing cursor") will be at the end of the line)
`SCI_DELWORDLEFT`              | Deletes from [caret](#key "typing cursor") to the beginning of the current [word](#key "sequence of alphanumeric characters or of punctuation characters"); if [caret](#key "typing cursor") was after a space character, th to the beginning of the previous [word](#key "sequence of alphanumeric characters or of punctuation characters")
`SCI_DELWORDRIGHT`             | Deletes from [caret](#key "typing cursor") to the end of the current [word](#key "sequence of alphanumeric characters or of punctuation characters"), plus any horizontal whitespace that comes after
`SCI_DELWORDRIGHTEND`          | [‼️](#key "not in Shortcut Mapper") If a plugin sends this message, it deletes from [caret](#key "typing cursor") to the end of the current [word](#key "sequence of alphanumeric characters or of punctuation characters"), not including any horizontal whitespace that comes after
`SCI_DOCUMENTEND`              | Moves [caret](#key "typing cursor") to end of document
`SCI_DOCUMENTENDEXTEND`        | Moves [caret](#key "typing cursor") to end of document, extending normal stream-mode selection
`SCI_DOCUMENTSTART`            | Moves [caret](#key "typing cursor") to start of document
`SCI_DOCUMENTSTARTEXTEND`      | Moves [caret](#key "typing cursor") to start of document, extending normal stream-mode selection
`SCI_EDITTOGGLEOVERTYPE`       | Toggles Overtype/Insert mode
`SCI_FORMFEED`                 | Adds the formfeed (U+000C) character at the current character (and moves [caret](#key "typing cursor") after the new character)
`SCI_HOME`                     | Moves [caret](#key "typing cursor") to the beginning of the current line
`SCI_HOMEDISPLAY`              | Moves [caret](#key "typing cursor") to the beginning of the wrapped-portion of the line (when in line-wrap mode), otherwise moves it to the beginning of the full line
`SCI_HOMEDISPLAYEXTEND`        | Moves [caret](#key "typing cursor") to the beginning of the wrapped-portion of the line (when in line-wrap mode), otherwise moves it to the beginning of the full line; either way, extending normal stream-mode selection
`SCI_HOMEEXTEND`               | Moves [caret](#key "typing cursor") to the beginning of the current line, extending normal stream-mode selection
`SCI_HOMERECTEXTEND`           | Moves [caret](#key "typing cursor") to the beginning of the current line, extending rectangle (column-mode) selection
`SCI_HOMEWRAP`                 | Works like `SCI_HOMEDISPLAY`, except when [caret](#key "typing cursor") is at the beginning of the wrapped-portion of the line, in which case it acts like `SCI_HOME`
`SCI_HOMEWRAPEXTEND`           | Works like `SCI_HOMEDISPLAYEXTEND`, except when [caret](#key "typing cursor") is at the beginning of the wrapped-portion of the line, in which case it acts like `SCI_HOMEEXTEND`
`SCI_VCHOME`                   | Works like `SCI_HOME`, except goes to the first non-blank character of the line instead of beginning of the line (ie, it honors indentation); when already at indented-beginning, executes `SCI_HOME` instead
`SCI_VCHOMEDISPLAY`            | Works like `SCI_HOMEDISPLAY`, except goes to the first non-blank character (indented beginning); when already at indented beginning, executes `SCI_HOMEDISPLAY` instead
`SCI_VCHOMEDISPLAYEXTEND`      | Works like `SCI_HOMEDISPLAYEXTEND`, except goes to the first non-blank character (indented beginning); when already at indented beginning, executes `SCI_HOMEDISPLAYEXTEND` instead
`SCI_VCHOMEEXTEND`             | Works like `SCI_HOMEEXTEND`, except goes to the first non-blank character (indented beginning); when already at indented beginning, executes `SCI_HOMEEXTEND` instead
`SCI_VCHOMERECTEXTEND`         | Works like `SCI_HOMERECTEXTEND`, except goes to the first non-blank character (indented beginning); when already at indented beginning, executes `SCI_HOMERECTEXTEND` instead
`SCI_VCHOMEWRAP`               | Works like `SCI_HOMEWRAP`, except goes to the first non-blank character (indented beginning); when already at indented beginning, executes `SCI_HOMEWRAP` instead
`SCI_VCHOMEWRAPEXTEND`         | Works like `SCI_HOMEWRAPEXTEND`, except goes to the first non-blank character (indented beginning); when already at indented beginning, executes `SCI_HOMEWRAPEXTEND` instead
`SCI_LINECOPY`                 | Copies full current line (including any newline ending) to clipboard
`SCI_LINECUT`                  | Cuts full current line (including any newline ending) to clipboard
`SCI_LINEDEDENT`               | [‼️](#key "not in Shortcut Mapper") If a plugin sends this message, it selects the entire line, un-indents the current line by [one tab](#key "TAB character or ℕ space characters"), and moves [caret](#key "typing cursor") to the beginning of the line
`SCI_LINEDELETE`               | Deletes full current line (including any newline ending), without affecting clipboard
`SCI_LINEDOWN`                 | Moves [caret](#key "typing cursor") down one line
`SCI_LINEDOWNEXTEND`           | Moves [caret](#key "typing cursor") down one line, extending normal stream-mode selection
`SCI_LINEDOWNRECTEXTEND`       | Moves [caret](#key "typing cursor") down one line, extending rectangle (column-mode) selection
`SCI_LINEDUPLICATE`            | Duplicates full current line (putting newline ending between old and new), without affecting clipboard
`SCI_LINEEND`                  | Moves [caret](#key "typing cursor") to the end of the current line
`SCI_LINEENDDISPLAY`           | Moves [caret](#key "typing cursor") to the end of the wrapped-portion of the line (when in line-wrap mode), otherwise moves it to the end of the full line
`SCI_LINEENDDISPLAYEXTEND`     | Moves [caret](#key "typing cursor") to the end of the wrapped-portion of the line (when in line-wrap mode), otherwise moves it to the end of the full line
`SCI_LINEENDEXTEND`            | Moves [caret](#key "typing cursor") to the end of the current line, extending normal stream-mode selection
`SCI_LINEENDRECTEXTEND`        | Moves [caret](#key "typing cursor") to the end of the current line, extending rectangle (column-mode) selection
`SCI_LINEENDWRAP`              | Works like `SCI_LINEENDDISPLAY`, except when [caret](#key "typing cursor") is at the beginning of the wrapped-portion of the line, in which case it acts like `SCI_LINEEND`
`SCI_LINEENDWRAPEXTEND`        | Works like `SCI_LINEENDDISPLAYEXTEND`, except when [caret](#key "typing cursor") is at the beginning of the wrapped-portion of the line, in which case it acts like `SCI_LINEENDEXTEND`
`SCI_LINEINDENT`               | [‼️](#key "not in Shortcut Mapper") If a plugin sends this message, it selects the entire line, indents the current line by [one tab](#key "TAB character or ℕ space characters"), and moves [caret](#key "typing cursor") to the beginning of the line
`SCI_LINEREVERSE`              | [‼️](#key "not in Shortcut Mapper") If a plugin sends this message, it will reverse the line order in a multi-line selection
`SCI_LINESCROLLDOWN`           | Scrolls viewport down one line (so that one more line is visible at the bottom, one less at the top)
`SCI_LINESCROLLUP`             | Scrolls viewport up one line (so that one more line is visible at the top, one less at the bottom)
`SCI_LINETRANSPOSE`            | Swaps [caret](#key "typing cursor") line with the line above (does nothing if [caret](#key "typing cursor") is on the first line of the document)
`SCI_LINEUP`                   | Moves [caret](#key "typing cursor") up one line
`SCI_LINEUPEXTEND`             | Moves [caret](#key "typing cursor") up one line, extending normal stream-mode selection
`SCI_LINEUPRECTEXTEND`         | Moves [caret](#key "typing cursor") up one line, extending rectangle (column-mode) selection
`SCI_LOWERCASE`                | Converts all uppercase characters of the current selection to lowercase
`SCI_MOVESELECTEDLINESDOWN`    | Moves all the lines included in the current selection down one line (so one line from below the selection moves to before the selection); does nothing if the selection includes the last line of the document
`SCI_MOVESELECTEDLINESUP`      | Moves all the lines included in the current selection up one line (so one line from above the selection moves to after the selection); does nothing if the selection includes the first line of the document
`SCI_NEWLINE`                  | Adds a newline sequence after the current [caret](#key "typing cursor") (and moves [caret](#key "typing cursor") after, following indentation rules)
`SCI_PAGEDOWN`                 | Moves [caret](#key "typing cursor") down one page of text (or to the end of the document, if a full page movement isn't possible)
`SCI_PAGEDOWNEXTEND`           | Moves [caret](#key "typing cursor") down one page of text (or to the end of the document, if a full page movement isn't possible), extending normal stream-mode selection
`SCI_PAGEDOWNRECTEXTEND`       | Moves [caret](#key "typing cursor") down one page of text (or to the end of the document, if a full page movement isn't possible), extending rectangle (column-mode) selection
`SCI_PAGEUP`                   | Moves [caret](#key "typing cursor") up one page of text (or to the beginning of the document, if a full page movement isn't possible)
`SCI_PAGEUPEXTEND`             | Moves [caret](#key "typing cursor") up one page of text (or to the beginning of the document, if a full page movement isn't possible), extending normal stream-mode selection
`SCI_PAGEUPRECTEXTEND`         | Moves [caret](#key "typing cursor") up one page of text (or to the beginning of the document, if a full page movement isn't possible), extending rectangle (column-mode) selection
`SCI_PARADOWN`                 | Moves [caret](#key "typing cursor") to the beginning of the next [paragraph](#key "separated by blank line(s)")
`SCI_PARADOWNEXTEND`           | Moves [caret](#key "typing cursor") to the beginning of the next [paragraph](#key "separated by blank line(s)"), extending the normal stream-mode selection
`SCI_PARAUP`                   | Moves [caret](#key "typing cursor") to the beginning of the current [paragraph](#key "separated by blank line(s)") if inside a [paragraph](#key "separated by blank line(s)"), or to the beginning of the previous [paragraph](#key "separated by blank line(s)") if [caret](#key "typing cursor") is not in a [paragraph](#key "separated by blank line(s)") or already at the beginning of the current [paragraph](#key "separated by blank line(s)")
`SCI_PARAUPEXTEND`             | Moves [caret](#key "typing cursor") to the beginning of the current [paragraph](#key "separated by blank line(s)") if inside a [paragraph](#key "separated by blank line(s)"), or to the beginning of the previous [paragraph](#key "separated by blank line(s)") if [caret](#key "typing cursor") is not in a [paragraph](#key "separated by blank line(s)") or already at the beginning of the current [paragraph](#key "separated by blank line(s)"), extending the normal stream-mode selection
`SCI_SCROLLTOEND`              | Scrolls the viewport to the end of the document, without changing the active selection
`SCI_SCROLLTOSTART`            | Scrolls the viewport to the beginning of the document, without changing the active selection
`SCI_SELECTIONDUPLICATE`       | Duplicates the current selection (so there are two copies where there used to be one)
`SCI_STUTTEREDPAGEDOWN`        | Moves [caret](#key "typing cursor") to the last line of the current page, or to the last line of the next page if [caret](#key "typing cursor") is already there
`SCI_STUTTEREDPAGEDOWNEXTEND`  | Moves [caret](#key "typing cursor") to the last line of the current page, or to the last line of the next page if [caret](#key "typing cursor") is already there, extending normal stream-mode selection
`SCI_STUTTEREDPAGEUP`          | Moves [caret](#key "typing cursor") to the first line of the current page, or to the first line of the previous page if [caret](#key "typing cursor") is already there
`SCI_STUTTEREDPAGEUPEXTEND`    | Moves [caret](#key "typing cursor") to the first line of the current page, or to the first line of the previous page if [caret](#key "typing cursor") is already there, extending normal stream-mode selection
`SCI_TAB`                      | In the middle or at the end of a line of text, inserts a tab character or a tab-width set of spaces; at the beginning of the line, indents entire line by entire tab character or tab-width
`SCI_UPPERCASE`                | Converts all lowercase characters of the current selection to uppercase
`SCI_VERTICALCENTRE`[caret](#key "typing cursor")      | Scrolls the viewport so the line with the [caret](#key "typing cursor") is centered in the viewport
`SCI_WORDLEFT`                 | Moves [caret](#key "typing cursor") to beginning of current [word](#key "sequence of alphanumeric characters or of punctuation characters"), or beginning of the previous [word](#key "sequence of alphanumeric characters or of punctuation characters") if [caret](#key "typing cursor") is in whitespace or already at the beginning of a [word](#key "sequence of alphanumeric characters or of punctuation characters")
`SCI_WORDLEFTEND`              | Moves [caret](#key "typing cursor") to end of previous [word](#key "sequence of alphanumeric characters or of punctuation characters")
`SCI_WORDLEFTENDEXTEND`        | Moves [caret](#key "typing cursor") to end of previous [word](#key "sequence of alphanumeric characters or of punctuation characters"), extending the normal stream-mode selection
`SCI_WORDLEFTEXTEND`           | Moves [caret](#key "typing cursor") to beginning of current [word](#key "sequence of alphanumeric characters or of punctuation characters"), or beginning of the previous [word](#key "sequence of alphanumeric characters or of punctuation characters") if [caret](#key "typing cursor") is in whitespace or already at the beginning of a [word](#key "sequence of alphanumeric characters or of punctuation characters"), extending the normal stream-mode selection
`SCI_WORDPARTLEFT`             | Same as `SCI_WORDLEFT`, except will also stop for each part of a [CamelCase](#key) or [underscore_separated](#key) word, as well
`SCI_WORDPARTLEFTEXTEND`       | Same as `SCI_WORDLEFTEXTEND`, except will also stop for each part of a [CamelCase](#key) or [underscore_separated](#key) word, as well
`SCI_WORDPARTRIGHT`            | Same as `SCI_WORDRIGHT`, except will also stop for each part of a [CamelCase](#key) or [underscore_separated](#key) word, as well
`SCI_WORDPARTRIGHTEXTEND`      | Same as `SCI_WORDRIGHTEXTEND`, except will also stop for each part of a [CamelCase](#key) or [underscore_separated](#key) word, as well
`SCI_WORDRIGHT`                | Moves [caret](#key "typing cursor") to beginning of next [word](#key "sequence of alphanumeric characters or of punctuation characters")
`SCI_WORDRIGHTEND`             | Moves [caret](#key "typing cursor") to end of this [word](#key "sequence of alphanumeric characters or of punctuation characters"), or end of next [word](#key "sequence of alphanumeric characters or of punctuation characters") if the [caret](#key "typing cursor") is already at the end of a [word](#key "sequence of alphanumeric characters or of punctuation characters")
`SCI_WORDRIGHTENDEXTEND`       | Moves [caret](#key "typing cursor") to end of this [word](#key "sequence of alphanumeric characters or of punctuation characters"), or end of next [word](#key "sequence of alphanumeric characters or of punctuation characters") if the [caret](#key "typing cursor") is already at the end of a [word](#key "sequence of alphanumeric characters or of punctuation characters"), extending normal stream-mode selection
`SCI_WORDRIGHTEXTEND`          | Moves [caret](#key "typing cursor") to beginning of next [word](#key "sequence of alphanumeric characters or of punctuation characters"), extending the normal stream-mode selection

<a name="key">**Key**</a>:
- ‼️ = Not available in Notepad++ [Shortcut Mapper](../preferences/#shortcut-mapper), as of v8.8.1.  However, plugins (including the scripting plugins like PythonScript or NppExec) can send these messages to the editor, even though keyboard shortcuts cannot.
- "caret" = The typing cursor, which is the text insertion point; see "[Caret and Cursor](#caret-and-cursor)".
- "word" = A sequence of alphanumeric characters or a sequence of punctuation characters; transitions between alphanumeric and punctuation are a transition between words, just like spaces separate words.
- "paragraph" = One or more lines with no [blank lines](#key) between, separated by one or more [blank lines](#key).
- "blank lines" = Lines consisting of no characters other than the newline, or only whitespace characters (like spaces and tabs).
- "one tab" = One tab character, or the appropriate number of space characters, depending on the [indentation settings](../preferences/#indentation) for the active language.
- "CamelCase" = Words that have embedded capital letters, like `CamelCase` or `lowerThenUpper`; for those examples, the "parts" would be `Camel` and `Case` or `lower` and `Then` and `Upper`
- "underscore_separated" = Words that have embedded underscore separators, like `underscore_separated`; for that example, the "parts" would be `underscore` and `separated`


### Context Awareness

Certain keyboard-shortcuts for editing commands are "context aware", meaning that they behave differently whether there is an active selection or not.  For example,

- <kbd>Tab</kbd> will insert a tab character or spaces (depending on [per-language settings](../preferences/#language)) when typing normally, but if you have a selection, it will indent the text by one tab-stop.
- <kbd>Shift+Delete</kbd> will cut the current selection, or if there is no selection, it will delete the current line (assuming you have not changed the shortcut <kbd>Shift+DEL</kbd> from `SCI_CUT` to anything else; if you do, this functionality will _not_ be accessible). (Yes, it cuts to the clipboard if there's a selection, but deletes the line without affecting the clipboard if there is a selection.) (The no-selection variant is new to v8.6.)
- <kbd>Ctrl+C</kbd> will copy the current selection, or if there is no selection, it will copy the current line (assuming you have not changed the shortcut <kbd>Ctrl+C</kbd> from `SCI_COPY` to anything else; if you do, this functionality will _not_ be accessible). (The no-selection variant is new to v8.6.)
- <kbd>Ctrl+X</kbd> will cut the current selection, or if there is no selection, it will cut the current line (assuming you have not changed the shortcut <kbd>Ctrl+X</kbd> from `SCI_CUT` to anything else; if you do, this functionality will _not_ be accessible). (The no-selection variant is new to v8.6.)


Again, this manual will not enumerate all the context-aware commands.  The ones listed above have been deemed especially useful, or are mentioned because they were added to give Notepad++ behavior that is similar to other popular text editors and coding environments.

In v8.6.1, you can disable the context-aware "line copy / cut / delete" feature, by creating the [zero-byte config file](../config-files/#other-configuration-files) `disableLineCopyCutDelete.xml`.  This zero-byte config file was eliminated in v8.6.2, so the feature could not be disabled in that version.  And in v8.6.3, **[Settings > Preferences > Editing](../preferences/#editing-1) > ☐ Enable Copy/Cut Line without selection** was added to be able to control this behavior using the Preferences dialog.

### Drag-and-Drop Move or Copy

A "drag-and-drop" action on an active selection can be used for moving or copying that selection.

![](../images/dragAndDrop.gif)

- Moving text: Make a selection of the text you wish to move. Left-click on the selection and drag the selected text to its desired new location in the document and release the left mouse button.  During dragging, the mouse cursor will change to a box with a dashed outline to indicate that a move operation will take place when the mouse is released.  If you change your mind and wish to abort the move, simply press the <kbd>Esc</kbd> key while you still have the left-mouse button pressed.  While the dragging is occurring, if you decide you'd rather make a copy of the text, simply start pressing the <kbd>Ctrl</kbd> key, and it will be converted into a copy-action as described below.

- Copying text: Make a selection of the text you wish to copy.  Left-click on the selection and start dragging the selected text to the location where you want the duplicate version of the text to be placed.  At some point after starting the drag operation, start pressing the <kbd>Ctrl</kbd> key.  When you've reached your desired destination, release the left mouse button and then release the <kbd>Ctrl</kbd> key.  When you start dragging, the mouse cursor will change to a box with a dashed outline; when you add the <kbd>Ctrl</kbd> key, the mouse cursor will add a smaller box with a `+` sign in it, to indicate that a copy operation will take place when the mouse is released.  If you change your mind and wish to abort the copy, simply press the <kbd>Esc</kbd> key while you still have the left-mouse button pressed.

- _Notes:_

    - When copying text, it is important that no modifier keys (<kbd>Shift</kbd>, <kbd>Ctrl</kbd>, <kbd>Alt</kbd>, or other region-specific modifiers) are depressed/held when you _start_ dragging the text.  This will initially seem like a move operation, but adding in the <kbd>Ctrl</kbd> key **after** the drag has been started will turn it into a copy (and the mouse cursor will change accordingly).

    - These techniques work well with column-block selections, but with multiple stream selections perhaps less so: the multiple selections will be "jammed" together with no intervening delimiter at the destination position in the document.  Of course, if the multiple selections were all full lines, they will still be full lines at their destination, so for this specific case the mouse move/copy is judged to work very well.



## Printing

_The documentation on printing the active document has been moved to [Working with Files > Printing](../files/#printing)._
