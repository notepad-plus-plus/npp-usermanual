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

To toggle between insertion mode and overwrite mode, use the <kbd>Insert</kbd> key on your keyboard.  Alternatively, if the [Status Bar](../user-interface/#status-bar) is visible, it will show `INS` or `OVR` to indicate the typing mode, and clicking that indicator will toggle the mode.

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

* The **Text to Insert** will use the same text in every row.
* The **Number to Insert** will insert increasing numbers.
    * **Initial number** sets the starting number.
    * **Increase by** will change the step between numbers.  With a value of `0` (or if left empty), it will insert the same number every time.
    * **Repeat** will repeat the same number _n_ times.  Defaults to 1 if left blank.
    * **Leading** is a pull-down selector that will allow choosing between no leading characters, leading zeros, or leading spaces.

        None | Zeros | Spaces
        ---|---|---
        ![](../images/colEdit-LeadingNone.png) | ![](../images/colEdit-LeadingZeros.png) | ![](../images/colEdit-LeadingSpaces.png)
        _examples shown with **View > Show Symbol > Show Spaces and Tab** to make the leading spaces obvious._

        (Prior to v8.5.2, the only option was a checkbox for **☐ Leading zeros**, so unchecked was equivalent to "None" and checkmarked was equivalent to "Zeros")

    * **Format** chooses between **Dec** (0-9), **Hex** (0-9,A-F), **Oct** (0-7), or **Bin** (0-1).
        _Note_: the numerical boxes above are always in decimal, even if a different format is chosen for display.  (Example: to get `F`-`1F`, column-select 17 rows and set the initial number to `15` -- it will not allow `F`.)

## Multi-Editing

Multi-Editing mode (available via mouse usage only) allows you to make multiple [caret](#caret-and-cursor "typing/insertion cursor")s by using <kbd>Ctrl+Click</kbd> for each additional [caret](#caret-and-cursor "typing/insertion cursor").  This allows performing the same editing actions (typing, copy/cut/paste/delete, arrowing through the text) in multiple locations, even if they aren't lined up in a nice column, or even if there are lines between the [caret](#caret-and-cursor "typing/insertion cursor")s that you don't want to affect.  You may place as many additional [caret](#caret-and-cursor "typing/insertion cursor")s as you want.

In addition to placing additional [caret](#caret-and-cursor "typing/insertion cursor")s, you may also make multiple selections.  After making an initial selection, do a <kbd>Ctrl+Click+Drag</kbd> operation to place a second selection in another location.  You may create as many such selections as you'd like.  A primary use for this type of selection might be so that you can copy several selections with one command, or to replace multiple selections with the same content if you begin typing or do a paste.

Starting in v8.6.1, if you <kbd>Ctrl+Click</kbd> at a previous multi-[caret](#caret-and-cursor "typing/insertion cursor") location, or <kbd>Ctrl+Click</kbd> within a previous multi-selection region, that [caret](#caret-and-cursor "typing/insertion cursor") or selection region will be removed, while leaving other portions of your multi-selection still active.  (This effectively allows you to "undo" a _portion_ of the multi-selection without having to redo everything, and is useful in complex multi-selections when you accidentally <kbd>Ctrl+Clicked</kbd> in the wrong place or changed your mind.)

Multi-Editing mode is only available when stream selection(s) are active; it doesn't work in conjunction with column-block selection.  Unlike stream selections, where with Multi-editing you can define two or more selections simultaneously, with column mode there can be only one active selection at a time.

Before v8.6, whether or not you can use Multi-Editing mode was determined by the [**Settings > Preferences > Editing > ☑ Enable Multi-Editing (Ctrl+Mouse click/selection)**](../preferences/#editing-2) checkbox: with it checkmarked, <kbd>Ctrl+Click</kbd> will add [caret](#caret-and-cursor "typing/insertion cursor") locations; with it not checkmarked, Multi-Editing is disabled.  In v8.6 - v8.6.2, Multi-Editing is always on, and that option was been removed; starting in v8.6.3, that option was returned, but is now at [**Settings > Preferences > Editing 2 > ☑ Enable Multi-Editing (Ctrl+Mouse click/selection)**](../preferences/#editing-2).

Starting in v8.6, Multi-Edit became the default, and was significantly enhanced.  The [Multi-Editing HowTo](#multi-editing-howto) (below) gives a tutorial in how to use this improved feature, including the new [**Edit** menu](#edit-menu) **...Multi-Select...** commands.

With the improved Multi-Edit, Column Mode selections are treated more like Multi-Edit selections; in order to disable this treatment, create the [zero-byte config file](../config-files/#other-configuration-files) `noColumnToMultiSelect.xml` (in v8.6.1-v8.6.2); going forward, instead of a zero-byte file, there is a second option in the [**Editing 2**](../preferences/#editing-2) preferences to **☐ Enable Column Selection to Multi-Editing**.

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

The Character Panel, accessed through the **Edit > Character Panel** menu entry, allows the user to interact with the first 256 characters in the active [Encoding or Character set](../preferences/#encoding-menu).

When opened, the Character Panel will be by default a docked window on the right-hand side of the Notepad++ main window, entitled `ASCII Codes Insertion Panel`. (This is a bit of a misnomer since ASCII is defined as values 0 - 127 and the panel shows values in the range  0 - 255.)

This panel contains a grid-like control that has five columns: `Value`, `Hex`, `Character`, `HTML Name`, `HTML Decimal` and `HTML Hexadecimal`.  The HTML columns show the various HTML entity formats for each character: `HTML Name` is the named entity, like `&quot;`.  `HTML Decimal` (or `HTML Code` in older versions) is the decimal entity, like `&#34;`.  And `HTML Hexadecimal` (new to v8.5.2) is the hexadecimal entity, like `&#x22;`.  (All three of those examples refer to the ASCII double quote `"` character.)

If input focus is moved to a line in the Character Panel and Enter is pressed, the character from the `Character` column will be inserted at the current position in the document being edited.  If the mouse is used there is more flexibility: an item from the grid that is double-clicked will be inserted.  For example, when double-clicking `&quot;` from the `HTML Name` column on the line of value 34, `&quot;` (as literal text) will be inserted at the current position in the active document -- so this can be used to insert the character number in decimal or hexadecimal, the character itself, or the HTML entity (named or decimal or hexadecimal) into the document being edited.

When Notepad++ is told to interpret a file as ANSI or any of the Character Sets (described in the [**Encoding**-menu docs](../preferences/#encoding-menu)), the Character Panel shows information about the 256 8-bit character numbers (that is, the `Value`) for the character set selected.  Note that for all character sets, the 0-127 character values always represent the same character (the ASCII character); character values from 128-255 are character-set specific as to which character each value represents.  The panel offers an easy way to see value and character equivalence, and insert characters that don't exist on your keyboard.

When Notepad++ is told to interpret a file as Unicode (the entries starting with `UTF-8` or `UTF-16` in the [**Encoding** menu](../preferences/#encoding-menu)), the Character Panel will show the same characters for values 128-255 as the default codepage character set on the user's system (viewable as `Current ANSI codepage` in the **? > Debug Info** menu entry).  In this case, for values 128-255, the `Value` column is meaningless -- only the `Character` shown is important.  If this panel is used to insert the character into the active document, the correct Unicode character bytes will be used instead of the value as in the simpler ANSI case.  For values from 0-127, the character/value pair _is_ meaningful, because for this range the ANSI set of characters -- the true ASCII set -- line up with the same characters and values in the Unicode set.

## Change History

Notepad++ has a column in the margin section which indicates which lines have been changed since the file was last loaded, controlled by a checkbox in [**Settings > Preferences > Margins/Border/Edge**](../preferences/#margins-border-edge) with the background color set by the [**Settings > Style Configurator > Global Styles > Change History margin**](../preferences/#global-styles) (new to v8.4.6)

![](../images/ChangeHistoryColors.png)

- When the file is first loaded (or a new file is created), no lines have a color in that margin column.
- If a line is changed (added or edited) since the most recent load or save, it will be orange. (This is `Modified but unsaved` in the image.)
- After the changes to the file are saved, any lines that have been changed since the file was loaded will be green. (This is `Modified but saved` in the image.)
    - _Note_: If you tell Notepad++ to reload the file from disk, _all_ lines will be green.
    - Multiple saves will leave those lines green, even if they weren't changed since the previous save.
    - The only way to get back to having no color in the margin is to close the file and reload it (easy enough to do with **File > Close** followed by **File > Recent Files > Restore Recent Closed Files**, or with default shortcuts, use <kbd>Ctrl+W</kbd> then <kbd>Ctrl+Shift+T</kbd>).
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
        * **Remove Consecutive Duplicate Lines**: will only remove duplicates that are on the lines immediately following the first instance (still keeping the first instance); acts upon the line set spanned by the current selection, or the entire file if no active selection
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
        * **As Integers** means that `10` will sort as being bigger than `2`
        * **As Decimals (Comma)** means it will recognize `10,234` and `9,876` as decimal numbers and sort them numerically
        * **As Decimals (Dot)** means it will recognize `10.234` and `9.876` as decimal numbers and sort them numerically
        * NOTE: Sorting is performed with the assumption that all line-endings in the file are uniform and match the current selection for the file being edited -- the quickest way to check that selection is to glance at the status bar, where the current line-ending type is shown either as `Windows (CR LF)`, `Unix (LF)` or `Macintosh (CR)`.  It might be desirable to check the line-ending types in your file before executing a sorting operation, and use the **Edit > EOL Conversion >** choices or right-click on the Status Bar's EOL indicator to fix the line endings if necessary.
        * NOTE: If a [Column Mode](./#selection-modes-column-editor) selection is active, the sort will re-order all the lines included in the selection, but the sort key (the text that decides the sort order) will be limited to what is inside the column selection. This column-selection-based sort will be a "stable sort": if the keys are identical on two lines, then the order of those two lines will not change, even if text outside of the selected key columns is different.
* **Comment/Uncomment >** ⇒ submenu with actions that add or remove comment syntax, based on the file's **Language** selection.  This makes use of the `commentLine`, `commentStart`, and `commentEnd` attributes of the active Language as defined in [langs.xml](../config-files/#keyword-lists-langsxml) to define the characters to use for making or clearing line comments (`commentLine`) and block comments (`commentStart` and `commentEnd`).
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
* **Set Read-Only** ⇒ toggles Notepad++'s read-only flag on the active file buffer.
    * If you click this menu entry once, it will add a checkmark `✔` to the menu entry, to show that it's currently read-only for Notepad++.  If you click this menu entry when there is already a checkmark `✔`, the checkmark will be removed and Notepad++ will no longer consider this file read-only.
    * The state of this Notepad++ read-only flag is saved in the [session](../session/) file, so it will be remembered the next time the session is used.
    * *Note*: this toggle does _not_ affect the Windows Operating System's read-only attribute on the file; if Windows has marked this file as read-only, this menu entry will be greyed out and you cannot toggle it by clicking on it.  See the **Clear Read-only Flag** (below) for more on the OS flag.
* **Clear Read-Only Flag** ⇒ clears the Windows Operating System (OS) read-only attribute on a file.
    * Once the OS read-only flag has been cleared, this menu option will be greyed out and clicking on it will do nothing.
    * You cannot set the OS read-only flag using this menu in Notepad++; it has to be done through the OS (though Notepad++ scripting plugins are able to ask the OS to set the OS read-only flag on the file, like in [this example in the Community Forum](https://community.notepad-plus-plus.org/post/67312)).
    * If you use the OS to set the flag on a file that is open in Notepad++, and [**Settings > Preferences > MISC > File Status Auto-Detection**](../preferences/#misc) has been checked, then Notepad++ will notice that it is now a read-only file, and not allow you to edit the file.
    * If you use the OS to set the flag on a file that is open in Notepad++, but [**Settings > Preferences > MISC > File Status Auto-Detection**](../preferences/#misc) has been unchecked, then Notepad++ will _not_ notice that it was changed to read-only by the OS, and will blindly allow you to continue making changes; however, when you try to save and it sees that the file is read-only according to the OS, Notepad++ will notify you that you cannot save, and ask if you'd like to launch Notepad++ in Administrator mode to try to make the changes (if you do, the changes you made may be lost).
    * The current file's tab will have the "locked" icon (either the greyed-out disk icon by default, or a padlock icon if [Dark Mode](../preferences/#dark-mode) is active or if [**Settings > Preferences > General > ☑ Alternate icons**](../preferences/#general) has been checked on) whether the Windows OS read-only attribute is set, or the Notepad++ read-only flag has been set, or both.  The "locked" icon will change to a normal icon once neither the Windows OS read-only attribute nor the Notepad++ read-only flag are set (or equivalently, once both flags are cleared).

## Other Editing Commands and Shortcuts

There are also around a hundred editor commands that are accessible from keyboard shortcuts (though not all have a keyboard shortcut assigned by default).  Many of those commands are _not_ in the **Edit** menu (or any other Notepad++ menu).  These commands are listed in the [**Shortcut Mapper**](../preferences/#shortcut-mapper)'s **Scintilla commands** tab, and you can use the **Shortcut Mapper** to edit the assignments (add shortcuts or remove shortcuts) for these commands, whether they currently have a shortcut or not.

They have somewhat cryptic names, but if you look at the portion of the name to the right of the `SCI_` prefix, it does give you a hint.  For example, `SCI_CUT` shows the shortcuts for the traditional Cut command, and `SCI_LINECUT` will cut the whole current line, rather than just the selection.  The ones that have `LINE` in the name work on complete lines; if it has `CHAR` in the name, it works on individual characters; if it has `WORD` in the name, it works on whole words; and if it has `WORDPART` in the name, it works on partial words (also called "subwords", like `MyCoolFunction` has the three subwords `My`, `Cool`, and `Function`); if it has `PARA` in the name, it works on paragraphs (a paragraph ends with two consecutive newlines -- so a blank line between paragraphs);  `HOME`, `END`, `PAGEUP`, and `PAGEDOWN` correspond to the motions often associated with those keys on your keyboard.  If it has `CUT`, `COPY`, `PASTE`, and `SELECT` in the name, it indicates a variant of the normal editor actions of cutting, copying, pasting, and selecting text; if it has <kbd>DELETE</kbd> or `DEL` in the name, it will delete what is indicated in the rest of the name; if it has `EXTEND` in the name, it "extends" the selection (adds to the selection; these are usually the `Shift+`-modified commands for growing the selection).  That should be enough to help you understand the basics of what each of those commands do.

The Scintilla project, which Notepad++ uses to implement these traditional editor commands, has [documentation](https://www.scintilla.org/ScintillaDoc.html) for those  commands: you can look at the `SCI_xxxx` in the shortcut mapper, then search for that text on [their ScintillaDoc page](https://www.scintilla.org/ScintillaDoc.html) to find out more about that command.

But with so many commands, and the fact that no documentation set is likely to ever explain _everything_ in the way that makes the most sense to you (what makes sense to one user might be really confusing to another), it might be fruitful to play with some of those commands to see for yourself what they do.  (Notepad++ doesn't let you edit text while the **Shortcut Mapper** is open: one possible method of doing this experimentation is to have two instances of Notepad++ running, and have the **Shortcut Mapper** open to the **Scintilla commands** in one instance, and play with using them in the editor in the other Notepad++ instance.)

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
