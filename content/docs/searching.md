---
title: Searching
weight: 40
---

There are multiple methods to search (and replace) text in files. You can also mark search results with a bookmark on their lines, or highlight the textual results themselves.  Generating a count of matches is also possible.

There are three main built-in search mechanisms: the standard (dialog-based) Find / Replace / Find In Files / Mark, the dialog-free Next / Previous search-navigation, and the Incremental Search.

All keyboard shortcuts mentioned below are the default values, but are configurable in the [Shortcut Mapper](../preferences/#shortcut-mapper).  You can see the active shortcut for any menu item in the menu entry, or in the Shortcut Mapper.

## Dialog-based Searching

The most powerful set of searching features is found in the standard dialog-based Find / Replace / Find In Files / Mark dialog.  This dialog is generically known as the "Find" dialog or window.  The dialog has one tab for each of the forementioned searching-related features.

The **Find** tab (accessible using **Search > Find** or the keyboard shortcut Ctrl+F) gives access to searching and counting.  The **Replace** tab (**Search > Replace** or Ctrl+H) is similar, but allows you to also replace the matched text after it's found.  The **Find in Files** tab (**Search > Find in Files** or Ctrl+Shift+F) allows you to search and replace in multiple files with one action.  The **Mark** tab (**Search > Mark...**) allows you to apply redmarking (a red background to matched text) to certain sections of text and/or "bookmarks" to the lines that matched text is found upon.

*Note:*  Although a keyboard command can open and/or move input focus to one of the four tabs of the "Find" window, once this input focus is achieved, there is no possibility to switch to another of the tabs via the keyboard; the mouse must be used, or the window closed (via the *Escape* key) and the alternate tab's keyboard command then invoked

*Note:*  Use of some "Find" family features can cause the window to close.  Some users dislike this and wish for the "Find" window to always remain open.  This may be achieved by editing `config.xml` and looking for the `dlgAlwaysVisible=` parameter.  It defaults to `dlgAlwaysVisible="no"` but may be set to `dlgAlwaysVisible="yes"` to keep the "Find" window open and always available for user interaction.

*Note:*  Search option choices made by the user are remembered across invocations of Notepad++.

### Find / Replace

All the dialog-based have certain features in common, though some are disabled under certain circumstances.

* **Find what** edit box with dropdown history: this is the text you are searching for
* **Replace with** edit box with dropdown history: this is the text that will replace what was matched

* **☐ In selection**: If you have a region of text selected, and **In selection** is enabled, it will only **Count**, **Replace All**, or **Mark All** within that selection of text, rather than in the whole document (other buttons, such as **Find Next**, will continue to work on the whole document)
* **☐ Backward direction**: normally, searches go forward (down the page); with this option, they will go backward (up the page)
* **☐ Match whole word only**: if enabled, searches will only match if the result is a whole word (so "it" will not be found inside "hitch")
* **☐ Match case**: if enabled, searches must match in case (so a search for "it" will not find "It" or "IT")
* **☐ Wrap Around**: if enabled, if the search reaches the end of the document, it will wrap around to the beginning and continue searching

* **Search Mode**: this determines how the text in the **Find what** and **Replace with** will be treated
    * **☐ Normal**: all text is treated literally.
    * **☐ Extended (\n, \r, \t, \0, \x...)**: use certain "wildcards", as described in [Extended Search Mode (below)](#extended-search-mode)
    * **☐ Regular Expression**: uses the Boost regular expression engine to perform very power search and replace actions, as explained in [Regular Expressions (below)](#regular-expressions)
        * **☐ . matches newline**: in regular expressions, with this disabled, the regular expression `.` matches any character except the line-ending characters (carriage-return and/or linefeed); with this enabled, `.` also matches the line-ending characters.  As an alternative to using this checkbox, begin the **Find what** box text with `(?-s)` to obtain the unchecked behavior of **. matches newline**, or with `(?s)` to get its checked behavior.

* **☐ Transparency**: these settings affect the dialog box.  Normally, the dialog box is opaque (can't see the text beneath), but with these settings, it can be made semi-transparent (can partially see the text beneath)
    * **☐ On losing focus**: if this is chosen, the dialog will be opaque when you are actively in the dialog box, but if you click in the Notepad++ window, the dialog will become semi-transparent
    * **☐ Always**: if this is chosen, the dialog will be semi-transparent, even when you are actively in the dialog box
    * Slider Bar: sliding it right makes the dialog more opaque; sliding it left makes it more transparent.
        * Be careful when sliding it to the extreme left: you might not be able to see the dialog box anymore
        * By (temporarily) setting it to **Always**, you can see how transparent the dialog will be while moving the slider, which can help prevent making it too transparent to see.

The various action buttons available include:

* **Find Next**: Finds the next matching text
    * **☐** This checkbox changes the single **Find Next** button into **<<** and **>>** buttons, which are "Search backward" and "Search forward" (hovering over this checkbox with the mouse will, after a slight pause in movement, pop up a tooltip indicating "2 find buttons mode")
* **Count**: Counts how many matches are in the entire document, or possibly "In Selection", and shows that count in the message section at the bottom of the dialog box
* **Find All in All Opened Documents**: Lists all the search-results in a new **Find result** window; searches through all the file buffers currently open in Notepad++
* **Find All in Current Document**: Lists all the search-results in a new **Find result** window; only searches the active document buffer
* **Close**: Closes the search dialog

* **Replace**: Replaces the currently-selected match.  (If no match is currently selected, it behaves like **Find Next** and just highlights the next match in the specified direction)
* **Replace All**: Replaces all matches from the active location onward (following the **Backward direction** and **Wrap around** settings as appropriate).
    * NOTE: for regular expressions, this will be equivalent to running the regular expression multiple times, which is _not_ the same as running with the /g global flag enabled that is available in some programming-languages' regular expression engines.
* **Replace All in All Opened Documents**: same as **Replace All**, but goes through all the documents open in Notepad++, not just the active document.

The above actions may be initiated via mouse by pressing the appropriate button, or via special Alt keycombinations.  With focus on one of the Find dialog windows, press and release the Alt key.  This will cause Notepad++ to underline a single character in the text of *most* of the buttons.  Pressing Alt and one of the underlined characters will be the same as pressing the same button with the mouse, i.e., the chosen action will be initiated.  The Alt technique works for controls other than buttons as well, e.g., a checkbox control can be ticked/unticked via pressing its Alt key command.

**Find Next** has a special way of being invoked by keyboard control.  Pressing Enter when the Find dialog has input focus will initiate the **Find Next** command in the direction indicated by **Backward direction**.  Pressing Shift+Enter when the Find dialog has input focus will run the **Find Next** in the ***opposite*** direction as that indicated by **Backward direction**.  Hovering over the **Find Next** button with the mouse will, after a slight delay, pop up a tool tip indicating *Use Shift+Enter to search in the opposite direction* as a reminder of this capability.

When a find-family function is invoked via the Search menu, toolbar, or keyboard combination, the word at the caret (or the selected text, if any) is automatically copied into the **Find what** edit box.  This behavior is not disableable; it always happens.  To avoid this in a limited way, use the mouse ONLY to move input focus from an editing tab buffer to an already-open Find dialog, or make sure your caret is not "touching" a word and that there is no active selection when invoking the find-family command.  Aside:  This auto-copy feature can be exploited to get multi-line data into the **Find what** edit box, something that it is not possible to do via only typing into the box.  Simply select the multi-line text that you want to search for, and then call up the Find dialog via one of its functions.  The selected text will appear as usual in the **Find what** box.  The line-ending character(s) won't be visible, but they will be there and will be matched when a search/replace action is initiated.

A valid **Find what** edit box entry length ranges from 1 to 2046 characters.  A valid **Replace with** edit box entry length ranges from 0 to 2046 characters.  Any text entered/pasted into these boxes beyond the 2046th character is simply ignored when an action is invoked.  Note that a replacement operation with a zero-length **Replace with** box entry is effectively a deletion of the matched text.

Selecting **Search Mode** of **Regular expression** will cause the **Match whole word only** option to become deselected and disabled.  A possible workaround to allow doing this type of searches is to add `\b` to the beginning and end of your regular expression **Find what** text.

The **Find what** and **Replace with** edit boxes have a dropdown arrow which allows the user to repeat searches conducted previously.  The default number of search/replace terms retained is 10, but this may be changed by editing a configuration file.  The **Find in Files** tab's **Filters** and **Directory** text boxes have this "history" feature as well.  This history can be activated by clicking on the down-arrow with the mouse, or by using the down (and/or up) keys -- be careful though, sometimes when editing a control with the history feature, a user will accidentally hit an up or down arrow key when they really mean to press left or right arrow; this unfortunately wipes out the search/replace expression (as those are edited most often) that was being worked on and replaces it with some different text from the history buffer.

The **In selection** option will automatically be chosen by Notepad++ if a Find dialog window is opened when more than 1024 characters occur in the active selection.  The selected text will also be placed in the **Find what** box.  Running a **Count** or **Replace All** action without making other changes to the search parameters will result in *Count: 1 match* or *Replace All: 1 occurrence was replaced*, respectively, which is likely not what was intended.  The proper resolution for this situation is to change the **Find what** text if the intention is to search within-selection, or deselect **In selection** if the intention is to search for a fairly long block of text.

The status bar area of the Find dialog keeps the user informed of what occurred during an action.  For example, it might say *Mark: 1 match* or *Find: Invalid regular expression*.  Colors are used in the status bar for emphasis:  red for some sort of error; green or blue for various success or general information.

Notepad++ uses a flashing of the Find dialog window and the main Notepad++ window itself (when the Find dialog is not open) to indicate that search text has not been found (or possibly that a **Wrap around** in the search has occurred).  In general, if a search results in no matches, and the Find dialog window is open, that window will flash briefly as a failure indication.  If the Find dialog window is NOT open, and a failed search is initiated (e.g. via **Find Next** on the **Search** menu), the main Notepad++ window will flash briefly, again, as an indicator of the lack of success.  With the Find dialog window closed, but with **Wrap around** previously activated, a search that causes a wrap at an end of the file to occur will also cause the Notepad++ main window to flash.  In addition, the system error bell will sound if a **Find Next** or **Replace** action results in the **Find what** text not being encountered; the bell is not disableable.

If a search action is invoked by keyboard command with the Find dialog window open and input focus in the editing window, an unsuccessful search will result in input focus being changed to the Find window.  Presumably, the user would want to conduct a different search at this point?

*Disclaimer:*  It is Notepad++'s design intention to fulfill some basic searching/replacing capability.  As such, Notepad++ searching is not infinitely flexible and capable of meeting all needs.  For such power needs, please turn to external tools, some of which integrate well with Notepad++.  Integrating well means that after such tools produce results, they can tell Notepad++ which files to open and which line and column numbers to move the caret to, in order to work with matched results.  Examples of such power file/text searching tools might be:  "GrepWin", "PowerGREP", "Fileseek", "Everything" and many others.

#### "Find result" Window

After running one or more **Find All in ...** commands, a new **Find result** window appears, and within it is placed a **Find result** tab.  The **Find result** window may be opened and/or given input focus by using the menu command **Search > Search Results Window** or the F7 keyboard shortcut.  *Note:*  That menu command will seem to not do anything if there haven't been any **Find All in ...** commands run since Notepad++ was opened.

*Definition:*  **Find All in ...** commands include:

|*Which **Find All in ...** command*| *Find window owner tab*|
|-----------------------------------|------------------------|
|Find All in All Opened Documents   | **Find**               |
|Find All in Current Document       | **Find**               |
|Find All                           | **Find in Files**      |

The **Find result** window by default appears docked at the bottom of the Notepad++ main window.  Like other such windows, it can be moved or even be a free-floating window.

From **Find All in ...** searches, three types of sections are added to the Find result window.  First is a line describing what was searched for, how many total matches (known as "hits") occurred (this is also shown in the title bar for the window, for the most recently-occurring search), and how many files had matches.  Second is a line that shows the filename with the matches and the count of matches for that file (this type will be repeated if the search found multiple files with matches).  Last comes the details about the matches found, including line number and the line contents with the matched text emphasized.  The default emphasis is red text on a yellow background, but this may be changed in the Style Configurator's "Search result" Language area.

When Notepad++ populates the **Find result** window, it does so using one line for each match found by the search.  Note that this can and often does end with the same source file line being repeated multiple times in the output.  An example of this would be if you are searching for "the" in the line of text that reads "Now is the time for all good men to come to the aid of their country"; the **Find result** window would list the line twice, once with the word "the" called out in red text with a yellow background, and a second time with "the" in "their" similarly emphasized.

When the **Find result** window has input focus, the currently active line has a different background color, much like how the main editor window does by default.  Unlike the main editor window, where the current-line background feature may be turned off, the **Find result** window always has a background highlight for its active line.

Use the up and down arrows to navigate within the **Find result** window when it has input focus.  Double-clicking with the mouse or hitting ENTER when input focus is on a specific match will move the editor window to that match and cause its text to be selected.

Other ways to navigate back to an editor window via the **Find result** window matches include the **Search** menu items **Next Search Result** (keyboard: F4) and **Previous Search Result** (keyboard: Shift+F4).  These can be invoked regardless of where input focus is in Notepad++.

The *Delete* key can be used to delete individual results, file matches or whole search matches in the **Find result** window, depending on which type of line is active when the key is pressed.  As the result history is hierarchical, that is, tree-like, pressing *Delete* when in a higher-level element of the tree removes that whole branch.  Thus:

|*Pressing Delete when **Find result** active line starts with...*| *What is removed*                                                                              |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
|the text: "Search"                                               | that "Search" line, all pathname lines under it, and all "Line" lines under the pathname lines |
|a pathname                                                       | that pathame line and all "Line" lines under it                                                |
|the text: "Line"                                                 | only that line                                                                                 |

Multiple searches will be listed under separate headers, which are "foldable", so you can hide or unhide results from previous searches.  When you run a new search, previous searches are folded closed.

If the source file lines are judged by Notepad++ to be too long when they are copied to be placed in the **Find result** window, they will be truncated and **...** will be added at the end.  In this case, matched text occurring in the line after the **...** position will not be emphasized.  However, using a method to return to the editor window (e.g. pressing Enter) will result in the correct selection of matching text there.  The length limit is 1024 characters; this includes the match line number information and other formatting.

If a search is conducted such that a match which spans two or more lines occurs, only the contents of the *FIRST* line of that match will be copied into the **Find result** window.  However, using a method to return to the editor window (e.g. pressing Enter) will result in the correct selection of multi-line matching text there.

##### *RightClick* commands in the client area of a **Find result** window's tab

###### Copying text from the **Find result** window

There are two ways to copy text from the **Find result** window:  Make sure input focus is in the **Find result** window by selecting some text and use the keyboard's *Ctrl+c* or the mouse's *RightClick* to invoke the context menu and select **Copy** from that.  Somewhat surprisingly, these two copy mechanisms produce vastly different results.

When *Ctrl+c* is used, it is very straightforward:  Whatever text is selected is copied, simply and exactly.  If nothing is selected when *Ctrl+c* is pressed (and the **Find result** window has input focus of course), nothing is copied to the clipboard.

When the mouse's *RightClick* > **Copy** is used, however, it is more complicated.  Basically, this type of copy can be thought of as a "Copy Special".  It copies the text of ENTIRE LINES from the results, WITHOUT any search information (called "metadata") being included in what is copied.

Here's a more detailed description of what happens for *RightClick* > **Copy**:

First, if the user makes a selection of text in the **Find result** window and copies it this way, only the lines of text touched (even partially) by the selection is part of the copy.  All other text with information about the search (pathame, line number, etc.) is *not* copied, even if part of the selection.  Secondly, if there is no active selection when the *RightClick* > **Copy** is invoked, results depend upon what exactly is *RightClick*'ed upon:

|*RightClick*'ed item     |What gets copied when *RightClick* > **Copy** is run |
|-----------------------|-----------------------------------------------------------------------------------------------------|
|a line with line # info|the entire line of the *RightClick* but without line number text                                     |
|a pathname header line |all the lines for that single file without pathname or line number text                              |
|a "search" header line |all the lines for that search (1 or more files) without search header, pathname or line number text  |

*Tip*:  It is possible to select and copy a rectangular selection of data from the **Find result** window.  This is done using the usual Shift+Alt+arrow keys or via Alt+LeftClick->drag with the mouse.  This is really only practical when using the *Ctrl+c* method of copying; RightClick > **Copy** only copies entire lines, and this copy will only copy the single full line at the top/bottom of the column block.

###### Other commands

There are some commands that don't need a lot of explanation; these are:

* **Collapse all**
* **Uncollapse all**
* **Select all**
* **Clear all**
* **Open all**

The **Find result** window/tab accumulates results from every **Find All in ...** search the user does; the results from old searches remain until the user removes them.  Individual results can be deleted with the *Delete* key, or all previous results can be deleted by invoking **Clear all**.  Stale results can be removed to reduce visual clutter, or when it is desired that a follow-on action should not be affected by old results.  An example of this would be the **Open all** command which opens *all* files listed in the **Find result** tab that have previously had hits.  If the search history in **Find result** is really long, it may not be desireable to open all files listed there, so using **Clear all** before doing some new searches (with the intent to **Open all** afterwards) may be the thing to do.

The **Select all** command is self-explanatory:  *ALL* text in the **Find result** tab will be selected

The contents of the **Find result** tab are in the form of a tree.  When Notepad++ adds to the result history, it does so in an uncollapsed way, that is, the user can see all of the information from the recently-added search.  However, before adding new results, Notepad++ will collapse all previous result data; perhaps it is deciding that the most-recent search is the most important?

The user can collapse/uncollapse "branches" of this tree.  To collapse, click with the mouse on the little box symbol with an interior `-`, found to the left of each line.  After doing so, that part of the tree will be collapsed (removed from view) and the first line of the branch (remaining visible) will then show a `+` in the box symbol.  To uncollapse an individual item that has previously been collapsed (either by the user or by Notepad++'s automatic mechanism), simply click the box symbol with the `+`.  That branch will then be expanded and again shown.

The **Collapse all** and **Uncollapse all** commands perform the corresponding actions on *ALL* elements of the entire result history in the **Find result** window at once.  Perhaps a better name for **Uncollapse all** would have been the more-conventional "Expand all"?

###### Searching in previously-found results (secondary searching)

Perhaps you have done a search and your results are in a tab in athe **Find result** window.  Now you'd like to conduct a search but with a scope of only the files that have previous matches.  Or maybe you want to look only in the *lines* matched by previous searches, not only the matched files, tightening the search criteria even more.  Can you do this sort of second-level searching with Notepad++?  Yes, by *RightClick*'ing the **Find result** window client area and selecting **Find in this found results...**.

Selecting **Find in this found results...** will cause a window to pop up, and this window looks much like the standard **Find** window, but is stripped down a bit.  Once you input your search parameters and choose **Find All**, a *new* **Find result** tab will open (in the **Find result** window) with the results of the "refined" search.

The popup window has a parameter not available in the searches decribed earlier:  **☐ Search only in found lines**.  Checking this box limits the search to lines that appear in matched files in the parent **Find result** window.  Unchecking the box will cause the new search to examine previously matched files in their entirety.  When a search has been limited to previously-found lines, its results will indicate this by using this type of output:  `Search "___" (__ hits in __ files - Line Filter Mode: only display the filtered results)` as opposed to the normally seen:  `Search "___" (__ hits in __ files)`

*Tip:*  Use the *RightClick* option **Clear all** to limit the scope of these types of searches (before invoking the secondary search!) -- remember: a **Find in this found results...** search will look in files matched by ALL previous searches whose results are still present in the parent **Find result** tab.

*Tip:*  Since the newly opened **Find result** window also has a *RightClick* menu, you may do another **Find in this found results...** based upon the new results, focusing your search for some bit of data even more.  This type of refinement may be repeated as much as desired.  [Note that the title bar of the window does *not* show the hit count of the currently active tab, but rather shows the hit count of the *first* **Find result** tab of the window.]

*Note:*  The commands that switch input focus to the **Find result** window always activate the *first* **Find result** tab, not any additional **Find result** tabs that may have been created.

*Note:*  The contents of the **Find result** window are discarded upon Notepad++ shutdown.  If there is data of importance there it should be copied, using one of the methods above, and saved in a more-permanent location.

### Find in Files

Find in Files allows both finding and replacing. You can choose an extension filter (**Filters:**), the containing folder (**Directory:**), and whether to also process hidden files or subfolders. The filter list is a space separated list of wildcard expressions that cmd.exe can understand, like "*.doc", "*.*" or "foo.*". Note however that the PathMatchSpec() Windows API is being used, as its behaviour departs from cmd.exe wildcard parsing sometimes.

How the default filter and folder change is controlled by the fifFilterFollowsDoc and fifFolderFollowsDoc settings in config.xml. There is a Follow current doc checkbox to set both parameters to both true or both false.

### Highlighting and bookmarking

The Mark tab from the Find/Replace dialog will perform searches similar to the Find tab, in the current document or selection:

* When **Bookmark line** is checked, a bookmark is dropped on each line where an individual hit occurs.  In the case where an individual hit spans multiple lines, each line in the span will receive the bookmark.

* Otherwise, the matched pattern is highlighted according to the Settings -&gt; Styler Configurator -&gt; Global Styles , Find Mark Style setting.  (See also [Style Configurator](../preferences/#style-configurator).)

In either case, the Mark All button will perform the marking.

To control whether highlighting or bookmarks accumulate over successive searches, use the **Clear all marks** button to remove marks, or check **Purge for each search** for this action to be performed automatically on each search.  When the **Clear all marks** button is pressed, any marked text will have the marking background coloring removed; additionally, any bookmarks previously set will be removed if the **Bookmark line** checkbox is checked.

Highlighting is also available in Incremental search, and the style setting is Settings -&gt; Styler Configurator -&gt; Global Styles , Incremental Highlighting instead.

## Dialog-free search/mark actions

### Searching

The following commands, available through the Search menu or keyboard shortcuts, perform a search without invoking a dialog, because they reuse the previous pattern or find it in the current document:

* Find Next / Find Previous repeat the current search, either down or up.

* Go to Next Found / Go to Previous found jump to a place recorded on the search result window. You can use  Search  -&gt;  Found Results Window to toggle the visibility of this window, which allows a more visual navigation.

* Find (volatile) Next / Find (volatile) Previous attempt to find the word the caret is in, or the selected text, down or up. Note that this does not interfere with ordinary search - it is really volatile.

* Select and Find Next / Select and Find Previous select the word the caret is in if no text is selected, and then find the next/previous occurence of selected text. This will also set this word as the current search target, so that Find Next or Find Previous will lose its previous target and look for the selected word again.  However, other search parameters, e.g. Match case or Wrap around, will remain in force as last set.

Please note that "selected" refers to the contents of the active stream selection. This also applies to the selected part of the caret line when a rectangular area is selected.

### Highlighting

Use the Mark All or Unmark All submenus of the Search menu to mark all occurrences of the word the caret is in. The settings for each of the 5 available styles are Settings -&gt; Styler Configurator -&gt; Global Styles , Mark style #. You can also cause all occurrences of the word at the caret to get dynamically highlighted if you enable Smart Highlighting; the mark style then is Settings -&gt; Styler Configurator -&gt; Global Styles , Smart Highlighting. You may choose there whether the matching should be sensitive to case.
You enable smart highlighting through Settings -&gt; Preferences -&gt; MISC -&gt; Smart highlighting, Enable smart highlighting. By default, the highlighting is case insensitive, which may be a problem sometimes. Then just toggle Settings -&gt; Preferences -&gt; MISC -&gt; Highlighting is case sensitive on.  (See also [Style Configurator](../preferences/#style-configurator) and [Preferences](../preferences/#preferences).)


## Finding characters in a specific range

While regular expressions provide for specifying a range (or multiple ranges) of characters using the  [start....end] pattern, this is sometimes awkward when the start or end character isn't easily typed in. Notepad++ provides a specific dialog, available using Find -&gt; Find Characters in range....

A custom range of characters can be asked for, as well as either half of the 0..255 range: ASCII covers the lower half, non-ASCII covers the upper part. Note that entries should be in decimal notation, and that values above 255 are not handled in a useful way.

Search may proceed up or down, and optionally wraps around. Hit Find to perform it. Close dialog using either the dedicated button, the close button on the title bar or the Esc key.

## Incremental Search

Incremental search is similar to the searching capabilities found in your favorite web browser (like Firefox or Chrome).  You can launch it from the **Search > Incremental Search** menu, or the keyboard shortcut (Ctrl+Alt+I).

This command will show a small region at the bottom of the Notepad++, which has a few simple features.

* The **✗** allows you to close out of Incremental Search.
* The **Find** box is where you type your literal search term.
* The **<** and **>** buttons navigate backward and forward thourgh the search results (wrapping around when it reaches the end or start of the document).
* If the **☐ Highlight all** checkbox is not checked, it will only highlight the current match; if it is checked, all matches will be highlighted.
* If the **☐ Match case** checkbox is checked, the results will only match if case is exactly the same, otherwise case doesn't matter.
* To the right of those checkboxes, a message about the results will occur: either the number of matches, a message that indicates that you've wrapped around to the top or bottom of the document, or "Phrase not found" if there are no matches.  When there are no matches, the **Find** box also changes colour.

## Comparison between "Select and Find Next" and "Find Next (Volatile)"

This section is aimed to clear the confusion about these 2 similar commands.

Both commands "Select and Find Next" (Ctrl+F3) and "Find Next (Volatile)" (Ctrl+Alt+F3) does the same thing (almost): select the current word (on which caret is) then jump to the next occurrence.

However, there is a slight difference between these 2 commands: "Select and Find Next" remembers the searched word, "Find Next (Volatile)" does not.

Here's an example:

If you do "Select and Find Next" command for word word1 then you can always use "Find Next" command (F3) or "Find Previous" command (Shif+F3) to search word1, even the caret is on word2.

If your caret is on word word2, "Find Next (Volatile)" will search the next word2. Now if you move your caret on word word3 and do "Find Next (Volatile)", it will search next word3, and word2 is forgotten.

## Extended Search Mode

In extended mode, these escape sequences (a backslash followed by a single character and optional material) have special meaning, and will not be interpreted literally.

* `\n`:  the Line Feed control character LF (ASCII 0x0A)
* `\r`:  The Carriage Return control character CR (ASCII 0x0D)
* `\t`:  the TAB control character (ASCII 0x09)
* `\0`:  the NUL control character (ASCII 0x00) †
* `\\`:  the literal backalash character (ASCII 0x05C)
* `\b`:  the binary representation of a byte, made of 8 digits which are either 1's or 0's. †
* `\o`:  the octal representation of a byte, made of 3 digits in the 0-7 range
* `\d`:  the decimal representation of a byte, made of 3 digits in the 0-9 range
* `\x`:  the hexadecimal representation of a byte, made of 2 digits in the 0-9, A-F/a-f range.
* `\u`:  The hexadecimal representation of a two byte character, made of 4 digits in the 0-9, A-F/a-f range. In Unicode builds, finds a Unicode character. In ANSI builds, finds characters requiring two bytes, like in the Shift-JIS encoding. †

†NOTE: While some of these Extended Search Mode escape sequences look like regular expression escape sequences, they are not identical.  Ones marked with † are different from or not available in regular expressions.

## Regular Expressions

Notepad++ regular expressions use the Boost regular expression library v1.70, which is based on PCRE (Perl Compatible Regular Expression) syntax, only departing from it in very minor ways. Complete documentation on the precise implementation is to be found on the Boost pages for [search syntax](https://www.boost.org/doc/libs/1_70_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html) and [replacement syntax](https://www.boost.org/doc/libs/1_70_0/libs/regex/doc/html/boost_regex/format/boost_format_syntax.html)

The Notepad++ Community has a [FAQ on other resources for regular expressions](https://notepad-plus-plus.org/community/topic/15765/faq-desk-where-to-find-regex-documentation).

### Regex Special Characters

In a regular expression (shortened into regex throughout), special characters interpreted are:

#### Single-character matches

* **.** or **\C** ⇒ Matches any character. If you check the box which says ". matches newline", the dot will indeed do that, enabling the "any" character to run over multiple lines. With the option unchecked, then **.** will only match characters within a line, and not the line ending characters (**\r** and **\n**)

* **\X** ⇒ Matches a single non-combining characer followed by any number of combining characters. This is useful if you have a Unicode encoded text with accents as separate, combining characters.

* **\\_Г_**  ⇒ This allows you to use a character _Г_ that would otherwise have a special meaning. For example, **\\[** would be interpreted as _[_ and not as the start of a character set. Adding the backslash (this is called _escaping_) can work the other way round, too, as it makes special a character that otherwise isn't: for instance, **\d** stands for "a digit", while "d" is just an ordinary letter.


##### Non ASCII characters

* **\x**_nn_ ⇒ Specify a single chracter with code _**nn**_. What this stands for depends on the text encoding. For instance, **\xE9** may match an é or a θ depending on the code page in an ANSI encoded document.

* **\x{**_nnnn_**}** ⇒ Like above, but matches a full 16-bit Unicode character. If the document is ANSI encoded, this construct is invalid.

* **\O**_nnn_ ⇒ A single byte character whose code in octal is _nnn_.  (That's an uppercase letter O, not the number 0)

*  **[[._collating sequence_.]]** ⇒ The character the _collating sequence_ stands for. For instance, in Spanish, "ch" is a single letter, though it is written using two characters. That letter would be represented as **[[.ch.]]**. This trick also works with symbolic names of control characters, like **[[.BEL.]]** for the character of code 0x07. See also the discussion on character ranges.



##### Control characters

* **\a** ⇒ The BEL control character 0x07 (alarm).

*  **\b** ⇒ The BS control character 0x08 (backspace). This is only allowed inside a character class definition. Otherwise, this means "a word boundary".

*  **\e** ⇒ The ESC control character 0x1B.

*  **\f** ⇒ The FF control character 0x0C (form feed).

*  **\n** ⇒ The LF control character 0x0A (line feed). This is the regular end of line under Unix systems.

*  **\r** ⇒ The CR control character 0x0D (carriage return). This is part of the DOS/Windows end of line sequence CR-LF, and was the EOL character on Mac 9 and earlier. OSX and later versions use \n.

*  **\R** ⇒ Any newline character.

* **\t** ⇒ The TAB control character 0x09 (tab, or hard tab, horizontal tab).

*  **\c**_character_ ⇒ The control character obtained from _character_ by stripping all but its 6 lowest order bits. For instance, **\c1**, **\cA** and **\ca** all stand for the SOH control character 0x01.  You can think of this as "\c means ctrl", so "\cA" is the character you would get from hitting Ctrl+A in a terminal.

#### Ranges or kinds of characters

* **[**...**]**  ⇒ This indicates a set of characters, for example, **[abc]** means any of the characters _a_, _b_ or _c_. You can also use ranges, for example **[a-z]** for any lower case character.  You can use a collating sequence in character ranges, like in **[[.ch.]-[.ll.]]** (these are collating sequence in Spanish).

* **[^**...**]**  ⇒ The complement of the characters in the set. For example, **[^A-Za-z]** means any character except an alphabetic character.  Care should be taken with a complement list, as regular expressions are always multi-line, and hence **[^ABC]*** will match until the first A,B or C (or a, b or c if match case is off), including any newline characters. To confine the search to a single line, include the newline characters in the exception list, e.g. **[^ABC\r\n]**.

* **[[:_name_:]]** ⇒ The whole character class named _name_.  Most of the time, there is a single letter escape sequence for them - see below. ⇒ Recognised classes are:

    *  alnum&nbsp;: ASCII letters and digits
    *  alpha&nbsp;: ASCII letters
    *  blank&nbsp;: spacing which is not a line terminator
    *  cntrl&nbsp;: control characters
    *  d , digit&nbsp;: decimal digits
    *  graph&nbsp;: graphical character
    *  l , lower&nbsp;: lowercase letters
    *  print&nbsp;: printable characters
    *  punct&nbsp;: punctuation characters: , " ' ? ! ; : # $ % &amp; ( ) * + - / &lt; &gt; = @ [ ] \ ^ _ { } | ~
    *  s , space&nbsp;: whitespace
    *  u , upper&nbsp;: uppercase letters
    *  unicode&nbsp;: any character with code point above 255
    *  w , word&nbsp;: word character
    *  xdigit&nbsp;: hexadecimal digits

*  **\p**_short name_ or **\p{**_name_**}** ⇒ Same as **[[:_name_:]]**. For instance, **\pd** and **\p{digit}** both stand for a digit, **\d**.

*  **\P**_short name_ or **\P{**_name_**}** ⇒ Same as **[^[:_name_:]]** (not belonging to the class _name_). ⇒ Note that Unicode categories like in \p{Sc} or \p{Currency_Symbol}, they are flagged as an invalid regex in v6.6.6. This is because support would draw a large library in, which would have other uses.

* **\d** ⇒ A digit in the 0-9 range, same as **[[:digit:]]**.

* **\D** ⇒ Not a digit. Same as **[^[:digit]]**.

* **\l** ⇒ A lowercase letter. Same as [a-z] or [[:lower:]]. ⇒ _NOTE_: this will fall back on "a word character" if the "Match case" search option is off.

* **\L** ⇒ Not a lower case letter. See note above.

* **\u** ⇒ An uppercase letter. Same as **[[:uper:]]**. See note about lower case letters.

* **\U** ⇒ Not an uppercase letter. Same note applies.

*  **\w** ⇒ A word character, which is a letter, digit or underscore. This appears not to depend on what the Scintilla component considers as word characters. Same as **[[:word:]]**.

* **\W** ⇒ Not a word character. Same as&nbsp;:alnum: with the addition of the underscore.

* **\s** ⇒ A spacing character: space, EOLs and tabs count. Same as **[[:space:]]**.

* **\S** ⇒ Not a space.

* **\h** ⇒ Horizontal spacing. This only matches space, tab and line feed.

* **\H** ⇒ Not horizontal whitespace.

* **\v** ⇒ Vertical whitespace. This encompasses the The VT, FF and CR control characters: 0x0B (vertical tab), 0x0D (carriage return) and 0x0C (form feed).

* **\V** ⇒ Not vertical whitespace.

* **[[=**_primary key_**=]]** ⇒ All characters that differ from _primary key_ by case, accent or similar alteration only. For example **[[=a=]]** matches any of the characters: a, À, Á, Â, Ã, Ä, Å, A, à, á, â, ã, ä and å.



#### Multiplying operators

* **+**  ⇒ This matches 1 or more instances of the previous character, as many as it can. For example, **Sa+m** matches _Sam_, _Saam_, _Saaam_, and so on.  **[aeiou]+** matches consecutive strings of vowels.

* **&#x2a;**  ⇒ This matches 0 or more instances of the previous character, as many as it can. For example, **Sa&#x2a;m** matches _Sm_, _Sam_, _Saam_, and so on.

* **?** ⇒ Zero or one of the last character. Thus **Sa?m** matches _Sm_ and _Sam_, but not _Saam_.

* **&#x2a;?** ⇒ Zero or more of the previous group, but minimally: the shortest matching string, rather than the longest string as with the "greedy" ***** operator. Thus, **m.*?o** applied to the text _margin-bottom: 0;_ will match _margin-bo_, whereas **m.*o** will match _margin-botto_.

* **+?** ⇒ One or more of the previous group, but minimally.

* **{_n_}** ⇒ Matches _n_ copies of the element it applies to.

* **{_n_,**} ⇒ Matches _n' or more copies of the element it applies to._

* **{_m_,_n_**} ⇒ Matches _m_ to _n_ copies of the element it applies to, as much it can.

* **{**_n_**,}?** or **{**_m_**,**_n_**}?** ⇒ Like the above, but match as few copies as they can. Compare with **&#x2a;?** and friends.

* **&#x2a;+** or **?+** or **++** or **{**_n_**,}+** or **{**_m_**,**_n_**}+** ⇒ These so called "possessive" variants of greedy repeat marks do not backtrack. This allows failures to be reported much earlier, which can boost performance significantly. But they will eliminate matches that would require backtracking to be found. ⇒ Example: matching ".*" against _"abc"x_ will find "abc", because
    *  " then abc"x then $ fails
    *  " then abc" then x fails
    *  " then abc then " succeeds.

However, matching "*+" against _"abc"x_ will fail, because the possessive repeat factor prevented backtracking.

#### Anchors
Anchors match a position in the line, rather than a particular character.


* **^** ⇒ This matches the start of a line (except when used inside a set, see above).

* **$**  ⇒ This matches the end of a line.

* **\\&lt;**  ⇒ This matches the start of a word using Scintilla's definitions of words.

* **\\&gt;**  ⇒ This matches the end of a word using Scintilla's definition of words.

* **\b** ⇒ Matches either the start or end of a word.

* **\B** ⇒ Not a word boundary.

* **\A** or **\\'** ⇒ The start of the matching string.

* **\z** or **\\`** ⇒ The end of the matching string.

* **\Z** ⇒ Matches like **\z** with an optional sequence of newlines before it. This is equivalent to **(?=\v*\z)**, which departs from the traditional Perl meaning for this escape.

* **\\G** ⇒ This "Continuation Escape" matches the end of the previous match.  In **Find All** or **Replace All** circumstances, this will allow you to anchor your next match at the end of the previous match.  If it is the first match of a **Find All** or **Replace All**, and any time you use a single **Find Next** or **Replace**, the "end of previous match" is defined to be the start of the search area -- the beginning of the document, or the current cursor position, or the start of the highlighted text.



#### Groups

* **(**...**)** ⇒ &lt;Parentheses mark a subset of the regular expression. The string matched by the contents of the parentheses **( )** can be re-used as a backreference or as part of a replace operation; see Substitutions, below.  ⇒ Groups may be nested.

* **(?&lt;_some name_&gt;...)** or **(?'_some name_'...)** or **(?(_some name_)...)** ⇒ Names this group _some name_.

* **\g**__n__ or **\g{**_n_**}** ⇒ The _n_-th subexpression, aka parenthesised group. Uing the second form has some small benefits, like _n_ being more than 9, or disambiguating when _n_ might be followed by digits. When _n' is negative, groups are counted backwards, so that **\g-2** is the second last matched group._

* **\g{_something_}** or **\k&lt;_something_&gt;** ⇒ The string matching the subexpression named _something_.

* **\**_digit_ ⇒ _Backreference:_ **\1** matches an additional occurence of a text matched by an earlier part of the regex. Example: This regular expression:  **([Cc][Aa][Ss][Ee]).*\1** would match a line such as _Case matches Case_ but not _Case doesn't match cASE_.  A regex can have multiple subgroups, so **\2**, **\3**, etc can be used to match others (numbers advance left to right with the opening parenthesis of the group). So \\_n_ is a synonym for **\g**_n_, but doesn't support the extension syntax for the latter.


#### Readability enhancements

* **(:**...**)** ⇒ A grouping construct that doesn't count as a subexpression, just grouping things for easier reading of the regex.

* **(?#**...**)** ⇒ Comments. The whole group is for humans only and will be ignored in matching text.


Using the x flag modifier (see section below) is also a good way to improve readability in complex regular expressions.


#### Search modifiers
The following constructs control how matches condition other matches, or otherwise alter the way search is performed.

* **\\Q** ⇒ Starts verbatim mode (Perl calls it "quoted"). In this mode, all characters are treated as-is, the only exception being the **\\E** end verbatim mode sequence.

* **\\E** ⇒ Ends verbatim mode. Ths, "\\Q\\*+\\Ea+" matches "\\*+aaaa".

* **(?:_flags_-_not-flags_ ...)** or **(?:_flags_-_not-flags_:...)** ⇒ Applies flags and not-flags to search inside the parentheses. Such a construct may have flags and may have not-flags - if it has neither, it is just a non-marking group, which is just a readability enhancer. The following flags are known:

    * **i**&nbsp;: case insensitive (default: off)
    * **m**&nbsp;: ^ and $ match embedded newlines (default: as per ". matches newline")
    * **s**:  dot matches newline (default: as per ". matches newline")
    * **x**: Ignore unescaped whitespace in regex (default: off)

* **(?|_expression using the alternation | operator_)** ⇒ If an alternation expression has subexpressions in some of its alternatives, you may want the subexpression counter not to be altered by what is in the other branches of the alternation. This construct will just do that.

    * For example, you get the following subexpressioncounter values:

~~~
# before  ---------------branch-reset----------- after
/ ( a )  (?| x ( y ) z | (p (q) r) | (t) u (v) ) ( z ) /x

# 1            2         2  3        2     3     4
~~~


    * Without the construct, (p(q)r) would be group #3, and (t) group #5. With the constuct, they both report as group #2.

### Control flow
Normally, a regular expression parses from left to right linerly. But you may need to change this behaviour.


* **|** ⇒ The alternation operator, which allows matching either of a number of options, like in&nbsp;: one|two|three to match either of "one", "two" or "three". Matches are attempted from left to right. Use **(?:)** to match an empty string in such a construct.

*  **(?**_n_**)** or **_(?**_signed-n_**)** ⇒ Refers to subexpression #_n_. When a sign is present, go to the _signed-n_-th expression.

*  **(?0)** or **(?R)** ⇒ Backtrack to start of pattern.

*  **(?&amp;_name_)** ⇒ Backtrack to subexpression named _name_.

*  **(?**__assertion__yes-pattern_**|**_no-pattern_**)** ⇒ Mathes _yes-pattern_ if assertion is true, and _no-pattern_ otherwise if provided. Supported assertions are:

*  **(?=**_assert_**)** (positive lookahead)

*  **(?!_assert_)**  (negative lookahead)

*  **(?(R))**   (true if inside a recursion)

*  **(?(R**_n_**)**  (true if in a recursion to subexpression numbered _n_)


PCRE doesn't treat recursion expressions like Perl does:

~~~
In PCRE (like Python, but unlike Perl), a recursive subpattern call  is
always treated as an atomic group. That is, once it has matched some of
the subject string, it is never re-entered, even if it contains untried
alternatives  and  there  is a subsequent matching failure.
~~~

*  **\K** ⇒ Resets matched text at this point. For instance, matching "foo\Kbar" will not match bar". It will match "foobar", but will pretend that only "bar" matches. Useful when you wish to replace only the tail of a matched subject and groups are clumsy to formulate.



#### Assertions
These special groups consume no characters. Their successful matching counts, but when they are done, matching starts over where it left.


* **(?=_pattern_)** ⇒ If _pattern_ matches, backtrack to start of _pattern_. This allows using logical AND for combining regexes.
    * For instance,

~~~
(?=.*[[:lower:]])(?=.*[[:upper:]]).{6,}

~~~

    * tries finding a lowercase letter anywhere. On success it backtracks and searches for an uppercase letter. On yet another success, it checks whether the subject has at least 6 characters.

    * '"q(?=u)i" doesn't match "quit", because, as matching 'u' consumes 0 characters, matching "i" in the pattern fails at "u" i the subject.

* **(?!_pattern_)** ⇒ Matches if _pattern_ didn't match.

* **(?&lt;=_pattern_)** ⇒ Asserts that _pattern_ matches before some token.

*  (?&lt;_pattern_) ⇒ Asserts that _pattern_ does not match before some token.
    * NOTE: _pattern_ has to be of fixed length, so that the regex engine knows where to test the assertion.

*  **(?&gt;_pattern_)** ⇒ Match pattern independently of surrounding patterns, and don't backtrack into it. Failure to match will cause the whole subject not to match.



### Substitutions

*  **\a**,**\e**,**\f**,**\n**,**\r**,**\t**,**\v** ⇒ The corresponding control character, respectively BEL, ESC, FF, LF, CR, TAB and VT.

*  **\C**_character_" or **\x**_nn_ or **\x**_nnnn_ ⇒ Like in search patterns, respectively the control character with the same low order bits, the character with code __nn_ and the character with code _nnnn_ (requires Unicode encoding).

*  **\l** ⇒ Causes next character to output in lowercase

*  **\L** ⇒ Causes next characters to be output in lowercase, until a **\E** is found.

*  **\u** ⇒ Causes next character to output in uppercase

*  **\U** ⇒ Causes next characters to be output in uppercase, until a **\E** is found.

*  **\E** ⇒ Puts an end to forced case mode initiated by **\L** or **\U**.

*  **$&amp;**, **$MATCH**, **${^MATCH}** ⇒ The whole matched text.

*  **$`**, **$PREMATCH**, **${^PREMATCH}** ⇒ The text between the previous and current match, or the text before the match if this is the first one.

*  **$"**, $POSTMATCH, ${$POSTMATCH} ⇒ Everything that follows current match.

*  **$LAST_SUBMATCH_RESULT**, **$^N** ⇒ Returns what the last matching subexpression matched.

*  **$+**, **$LAST_PAREN_MATCH** ⇒ Returns what matched the last subexpression in the pattern.

*  **$$** ⇒ Returns $.

*  **$_n_**, **${_n_}**, **\_n_** ⇒ Returns what matched the subexpression numbered _n_. Negative indices are not alowed.

*  **$+{_name_}** ⇒ Returns what matched subexpression named _name_.



### Zero length matches
While, in normal or extended mode, there would be no point in looking for text of length 0, this can very normally happen with regula expressions. For instance, to add something at the beginning of a line, you'll search for "^" and replace with whatever is to be added.

Notepad++ would select the match, bt there is no sensible way to select a stretch zero character long. Whe this happens, a tooltip very similar to function call tips is displayed instea, with a caret pointing upwards to the empty match.


### Examples
These examples come from an earlier version of this page:
Notepad++ RegExp Help, by Author&nbsp;: Georg Dembowski

_Add more examples using advanced features of PCRE_

**IMPORTANT**

*  You have to check the box "regular expression" in search &amp; replace dialog

*  When copying the strings out of here, pay close attention not to have additional spaces in front of them! Then the RegExp will not work!

#### Example 0
How to replace/delete full lines according to a regex pattern?
Let's say you wish to delete all the lines in a file that contain the word "unused", without leaving blank lines in their stead. This means you need to locate the line, remove it all, and additionally remove its terminating newline.

So, you'd want to do this::
Find: ^.*?unused.*?$\R
Replace with: nothing, not even a space
The regular expression **appears** to always work  is to be read like this:


*  assert the start of a line

*  match some characters, stopping as early as required for the expression to match

*  the string you search in the file, "unused"

*  more characters, again stopping at the earliest necessary for the expression to match

*  assert line ends

*  A newline character or sequence


Remember that .* gobbles everything to the end of line if ". matches newline" is off, and to the end of file if the option is on!

Well, why is **appears** above in bold letters? Because this expression assumes each line ends with an end of line sequence. This is almost always true, and may fail for the last line in the file. It won't match and won't be deleted.

But the remedy is fairly simle: we translate in regex parlance that the newline should match if it is there. So the correct expression actually is:



~~~
^.*?unused.*?$\R?

~~~



#### Example 1
You use a MediaWiki (e.g. Wikipedia, Wikitravel) and want to make all headings one "level higher", so a H2 becomes a H1 etc.

*  Search ^=(=)

*  Replace with \1

*  Click "Replace all"

You do this to find all headings2...9 (two equal sign characters are required) which begin at line beginning (^) and to replace the two equal sign characters by only the last of the two, so eleminating one and having one remaining.



*  Search =(=)$

*  Replace with \1

*  Click "Replace all"

You do this to find all headings2...9 (two equal sign characters are required) which end at line ending ($) and to replace the two equal sign characters by only the last of the two, so eleminating one and having one remaining.



== title == became = title =, you're done&nbsp;:-)


#### Example 2
You have a document with a lot of dates, which are in German date format (dd.mm.yy) and you'd like to transform them to sortable format (yy-mm-dd). Don't be afraid by the length of the search term – it's long, but consiting of pretty easy and short parts.

Do the following:


*  Search ([^0-9])([0123][0-9])\.([01][0-9])\.([0-9][0-9])([^0-9])

*  Replace with \1\4-\3-\2\5

*  Click "Replace all"


You do this to fetch


*  the day, whose first number can only be 0, 1, 2 or 3

*  the month, whose first number can only be 0 or 1

*  but only if the separator is . and not 'any character' ( . versus \. )

*  but only if no numbers are sourrounding the date, as then it might be an IP address instead of a date


and to write all of this in the opposite order, except for the surroundings. Pay attention: Whatever SEARCH matches will be deleted and only replaced by the stuff in the REPLACE field, thus it is mandatory to have the surroundings in the REPLACE field as well!

Outcome:


*  31.12.97 became 97-12-31

*  14.08.05 became 05-08-14

*  the IP address 14.13.14.14 did not change


You're done&nbsp;:-)


#### Example 3
You have printed in windows a file list using dir /b/s &gt;filelist.txt to the file filelist.txt and want to make local URLs out of them.

*  Open filelist.txt with Notepad++

*  Search \\

*  Replace with /

*  Click "Replace all" to change windows path separator char \  into URL path separator char /


*  Search ^(.*)$

*  Replace with file:///\1

*  Click "Replace all" to add file:/// in the beginning of all lines



According on your requirements, preceed to escape some characters like space to&nbsp;%20 etc.
C:\!\aktuell.csv became file:///C:/!/aktuell.csv

You're done&nbsp;:-)


#### Example 4
Another Search Replace Example



~~~
[Data]
AS AF AFG 004 Afghanistan
EU AX ALA 248 Åland Islands
EU AL ALB 008 Albania, People's Socialist Republic of
AF DZ DZA 012 Algeria, People's Democratic Republic of
OC AS ASM 016 American Samoa
EU AD AND 020 Andorra, Principality of
AF AO AGO 024 Angola, Republic of
NA AI AIA 660 Anguilla
AN AQ ATA 010 Antarctica (the territory South of 60 deg S)
NA AG ATG 028 Antigua and Barbuda
SA AR ARG 032 Argentina, Argentine Republic
AS AM ARM 051 Armenia
NA AW ABW 533 Aruba
OC AU AUS 036 Australia, Commonwealth of

~~~



*  Search for: ([A-Z]+) ([A-Z]+) ([A-Z]+) ([0-9]+) (.*)

*  Replace with: \1,\2,\3,\4,\5

*  Hit "Replace All"


Final Data:



~~~
AS,AF,AFG,004,Afghanistan
EU,AX,ALA,248,Åland Islands
EU,AL,ALB,008,Albania, People's Socialist Republic of
AF,DZ,DZA,012,Algeria, People's Democratic Republic of
OC,AS,ASM,016,American Samoa
EU,AD,AND,020,Andorra, Principality of
AF,AO,AGO,024,Angola, Republic of
NA,AI,AIA,660,Anguilla
AN,AQ,ATA,010,Antarctica (the territory South of 60 deg S)
NA,AG,ATG,028,Antigua and Barbuda
SA,AR,ARG,032,Argentina, Argentine Republic
AS,AM,ARM,051,Armenia
NA,AW,ABW,533,Aruba
OC,AU,AUS,036,Australia, Commonwealth of

~~~



#### Example 5
How to recognize a balanced expression, in mathematics or in programming?

Let's first explicitly describe what we wish to match. An expression is balanced if and only if all areas delineatd by parentheses contain a balanced expression. Like in: 1+f(x+g())-h(2).

This leads to define the following kinds of groups:
_balanced_&nbsp;::= _no_paren_ _paren_ ... _no_paren_

_no_paren_ = **[^()]*** -- a possibly empty group of characters without a single parenthesis

_paren_&nbsp;::= **(** _balanced_ **)**

Can we represent this as a regex? We cannot as-is.

The first hurdle is that there is no primitive construct to represent an alternating sequence of tokens. A common trick then is to represent the sequence as a repetition of the repeating pattern - here, _no_paren_ followed by _paren_ -, with any odd stuff at the end added.

So we have a more manageable, although slightly more complex, representation:

_balanced_&nbsp;::= _simple_***** _no_paren_

_simple_&nbsp;::= _no_paren_ _paren_

_no_paren_&nbsp;::= **[^()]***

_paren_ = **(** _balanced_ **)**



A second hurdle is that parentheses are not ordinary characters. That's ok, we'll escape them as **\(** and **\)** respectively.

The third one is more interesting. How do we represent the whole of an expression inside a nested sub-expression? This smacks of recursion. PCRE has recursion. The simplest form of it is tgoing back to the start of the search pattern - not the searched text! - and doing it again. It writes as **(?R)**. You remember seeing this one in the main list, right?

So:


*  we know how to match a _no_paren_. It will be nicer to give it an explicit name. This we'll do in the embelishments section below.

*  we jusrtr discovered how to write a _paren_: **\((?R)\)**


This gives us the following hard to read, but correct regex:



~~~
([^()]*\((?R)\))*[^()]*

~~~


Try it, it works. But it is about as hard to decrypt as a badly indented piece of code without a comment and with unpromising, unclear identifiers. This is only one of the reasons why old Perl earned itself the rare qualifier of "write-only language".


##### Embellishments
First of all, let's add some spacing so that we can identify the components of the regex. Spacing can be added using the x modifier flag, which is off by default.

So we can write something more legible:



~~~
(?x:  ([^ ( ) ]* \( (?R) \) )* [^()]* )

~~~


Now let's add some commenting



~~~
(?x:  ([^ ( ) ]* \( (?# The next group means "start matching the
beginning of the regex")(?R) \) )* [^()]* )

~~~

## Searching actions when recorded as macros

The Find family of actions can be recorded in a macro to make them easy to name and later replay via the **Macro** menu or an assigned keycombination.  Somewhat unfortunately, **Find what** and **Replace with** text is hardwired into the macro when it is created, and isn't something the user can change when the macro runs, but often this isn't a significant limitation.

Note, however, that Find-related actions are recorded a bit differently than other Notepad++ actions, so we'll discuss them a bit more in-depth here.  Typically, Notepad++ will record a step in a macro every time a user does something in the Notepad++ user interface.  The Find family of actions is more "coordinated" where macro recording is concerned.

The macro recorder only records when an actual Find family action (e.g. **Replace**, **Find All in Current Document**, etc.) occurs.  Thus you can tweak a future action's parameters (e.g. **Match case**, **Wrap around**, etc.) all you'd like, and all of that fiddling doesn't get remembered.  At the point where you peform an action, then a snapshot is taken of all of the parameters and the action, and this is logged in the macro memory as a proper macro sequence.

While the user can simply record and use Find family macros, one can also edit those macros later to change or add to their functionality, so it is helpful to know the details of the macro sequences that were previously recorded.  While the details of how macros in general are recorded and stored in *shortcuts.xml* is discussed elsewhere, here are the details of what happens when Notepad++ saves a recorded Find family macro:

First comes a **1700** message which carries out some initialization of the Find engine:

`<Action type="3" message="1700" wParam="0" lParam="0" sParam="" />`

Next is a **1601** message with the **Find what** text in the **sParam** field; in this example we search for "it":

`<Action type="3" message="1601" wParam="0" lParam="0" sParam="it" />`

Following that is a **1625** message with the **Search mode** in **lParam**, with possible values of 0=**Normal** / 1=**Extended** / 2=**Regular expression**; let's show **Regular expression** in this example:

`<Action type="3" message="1625" wParam="0" lParam="2" sParam="" />`

After that, if a type of replacement operation is being performed, is a **1602** message with **sParam** holding the **Replace with** text; here we'll make that "IT":

`<Action type="3" message="1602" wParam="0" lParam="0" sParam="IT" />`

Moving on, next, if performing a **Find All** (really a Find-in-Files) or a **Replace in Files**, is a **1653** message containing the base **Directory** for the search in **sParam**:

`<Action type="3" message="1653" wParam="0" lParam="0" sParam="C:\Program Files\Notepad++\" />`

Also when doing a **Find All** or a **Replace in Files**, will be a **1652** message containing the **Filters** for the search in **sParam**:

`<Action type="3" message="1652" wParam="0" lParam="0" sParam="*.*" />`

Next will be a **1702** message that contains a bit-weighted number in **lParam** that represents the "checkbox" option parameters for the action (more on this later, for now we will just use 515 in the example, and present the bit-weight table):

`<Action type="3" message="1702" wParam="0" lParam="515" sParam="" />`

| 1702-Bit-Weight |Binary-Bit-Weight | Meaning (equivalent option ticked) |
|-----------------|------------------|------------------------------------|
| 1               |0000000001        | Match whole word only              |
| 2               |0000000010        | Match case                         |
| 4               |0000000100        | Purge for each search              |
| 16              |0000010000        | Bookmark line                      |
| 32              |0000100000        | In all sub-folders                 |
| 64              |0001000000        | In hidden folders                  |
| 128             |0010000000        | In selection                       |
| 256             |0100000000        | Wrap around                        |
| 512             |1000000000        | Backward direction (unticked!)     |

Finally appears a **1701** message which encodes the Find family action to perform in **lParam**, which, when executed will conduct the action using all of the information encoded in the prior messages; let's do a **Replace in Files**, which has an integer value of 1660, for purposes of an example:

`<Action type="3" message="1701" wParam="0" lParam="1660" sParam="" />`

| 1701-Value | Meaning (equivalent button press)   |
|------------|-------------------------------------|
| 1          | Find Next                           |
| 1608       | Replace                             |
| 1609       | Replace All                         |
| 1614       | Count                               |
| 1615       | Mark All                            |
| 1633       | Clear all marks                     |
| 1635       | Replace All in All Opened Documents |
| 1636       | Find All in All Opened Documents    |
| 1641       | Find All in Current Document        |
| 1656       | Find All (in Files)                 |
| 1660       | Replace in Files                    |

So really the only tricky part is the 1702 message and how its encoding works.

Let's see how the example value 515 used above is decoded:

lParam="515" (decimal) = 203 (hex) = 10 0000 0011 (binary) = 512 + 2 + 1 = (***not*** Backward direction + Match case + Match whole word only).  Thus, this would represent a forward-from-caret-towards-end-of-file search of exact case specified, with the additional qualifier that the match text must be bracketed by non-word characters.

Finally, let's present a complete example (that could occur in *shortcuts.xml*) and how it is interpreted:

    <Macro name='Book Mark lines NOT containing ABC' Ctrl="no" Alt="no" Shift="no" Key="0">
        <Action type="3" message="1700" wParam="0" lParam="0" sParam="" />
        <Action type="3" message="1601" wParam="0" lParam="0" sParam="^(?-s)(?!.*ABC).*" />
        <Action type="3" message="1625" wParam="0" lParam="2" sParam="" />
        <Action type="3" message="1702" wParam="0" lParam="786" sParam="" />
        <Action type="3" message="1701" wParam="0" lParam="1615" sParam="" />
    </Macro>

First we have our initializing 1700 message.

Following that in the 1601 message's sParam field is a regular expression that will match lines that do not contain "ABC": `^(?-s)(?!.*ABC).*`

The search type for "Regular expression" appears next as lParam="2" in the 1625 message.

Skipping the 1702 message for the moment, the 1701 message has lParam="1615" which, from the 1701 table, means "Mark All".

Finally, let's consider the 1702 message.  Its pertinent part is lParam="786".  The best way to break that down into its component parts is to convert the number to binary and then determine how the one-bits in the binary contribute to the meaning.  786 in binary is 1100010010, which breaks down as follows, and then reading the 1702 table from earlier we get the contributors to functionality:

* `1000000000` - not Backward direction (thus forward direction from caret toward bottom end of file)

* `0100000000` - Wrap around

* `0000010000` - Bookmark line

* `0000000010` - Match case

Note that in this example we seem to have conflicting search parameters:  We have a direction encoded, as well as a Wrap around, which nullifies the need for a direction.  This is not a problem, as the Wrap around option will take precedence, just like in a non-macro'd interactive searching operation.
