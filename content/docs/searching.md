---
title: Searching
weight: 40
---

There are multiple methods to search (and replace) text in files. You can also mark search results with a bookmark on their lines, or highlight the textual results themselves.  Generating a count of matches is also possible.

There are three main built-in search mechanisms: the standard (dialog-based) Find / Replace / Find In Files / Mark, the dialog-free Next / Previous search-navigation, and the Incremental Search.

All keyboard shortcuts mentioned below are the default values, but are configurable in the [Shortcut Mapper](../preferences/#shortcut-mapper).  You can see the active shortcut for any menu item in the menu entry, or in the Shortcut Mapper.

## Dialog-based Searching

There is a "Find" dialog box. This dialog box has one tab for each of the following features:

* **Find** tab: Gives access to searching and counting.\
  It can be invoked directly with **Search > Find** or the keyboard shortcut `Ctrl+F`.

* **Replace** tab: Similar to **Find** tab, but allows you to replace the matched text after it's found.\
  It can be invoked directly with **Search > Replace** or the keyboard shortcut `Ctrl+H`.

* **Find in Files** tab: Allows you to search and replace in multiple files with one action. The files used for the operation are specified by a directory.\
  It can be invoked directly with **Search > Find in Files** or the keyboard shortcut `Ctrl+Shift+F`.

* **Find in Projects** tab: Similar to **Find in Files**, but Project Panel files are used instead of files from a directory.\
  It can be invoked over the context menu of the first line of a Project Panel.

* **Mark** tab: Allows you to highlight all occurrences of the search target in the current document permanently.\
  It can be invoked directly with **Search > Mark** or the keyboard shortcut `Ctrl+M`.

*Note:*  Prior to v8.1.3, doing any of those keystrokes (`Ctrl+F`, `Ctrl+H`, `Ctrl+Shift+F`, or `Ctrl+M`) once would open the Find dialog or bring it into focus; from the main dialog, hitting `Ctrl+F` would re-center the dialog (no matter which tab of the dialog you were on); but you could not use the shortcuts for the other tabs to switch between the tabs.  In v8.1.3 through v8.3.2, once the dialog was active and in focus, hitting the keystrokes would switch between the tabs on that dialog; however, these versions of Notepad++ would _not_ re-center the dialog if you hit `Ctrl+F` again.  Starting in v8.3.3, the first hit of one of those shortcuts would bring up the dialog or bring it into focus; from there, hitting one of the _other_ shortcuts would change tabs in the dialog (as with v8.1.3), but hitting the shortcut for the tab you are already on will re-center the dialog (so `Ctrl+F, Ctrl+F` will center the Find dialog, `Ctrl+H, Ctrl+H` will re-center the Replace dialog, and so on), giving you the full functionality of both tab-switching and dialog-centering.

*Note:*  Use of some "Find" family features can cause the window to close after a successful search (one or more "hits").  Some users dislike this and wish for the "Find" window to always remain open.  This may be achieved by use of the optional setting: **Preferences > Searching > Find dialog remains open after search that outputs to results window**.

*Note:*  Search option choices made by the user are remembered across invocations of Notepad++.

### Find / Replace tabs

All the dialog-based have certain features in common, though some are disabled under certain circumstances.

* **Find what** edit box with dropdown history: this is the text you are searching for
* **Replace with** edit box with dropdown history: this is the text that will replace what was matched

* **☐ In selection**: If you have a region of text selected, and **In selection** is enabled, it will only **Count**, **Replace All**, or **Mark All** within that selection of text, rather than in the whole document (other buttons, such as **Find Next**, will continue to work on the whole document)
* **☐ Backward direction**: normally, searches go forward (down the page); with this option, they will go backward (up the page)
* **☐ Match whole word only**: if enabled, searches will only match if the result is a whole word (so "it" will not be found inside "hitch").  
    * For ASCII text (text that only has newlines, tabs, and characters with codepoints 32 - 126):
        - If the left and right characters of your search string are both "word characters" (letters, numbers, underscore, and [optionally](https://npp-user-manual.org/docs/preferences/#delimiter "NPP User Manual: Delimiter settings") additional characters set by your preferences), then **Match whole word only** will only allow a match if the characters to the left and right of the match are _non_-word-characters or spaces or the beginning or ending of the line.
        - If the left and right characters of your search string are both non-word characters (so _not_ letters, numbers, underscore, and [optionally](https://npp-user-manual.org/docs/preferences/#delimiter "NPP User Manual: Delimiter settings") additional characters set by your preferences), then the text to the left and right of your match must be word charcters, spaces, and/or beginning or ending of the line.
        - If the left of your search string is a word character and the right is not (or vice versa), then the characters to the left and right must be of the opposite type, or be spaces, or be the beginning/ending of a line.
    * For non-ASCII text, the general concepts are the same; however, some edge cases may behave differently than you expect, and with thousands of possible Unicode characters and millions of combinations of pairs of Unicode characters, this manual _cannot_ contain a full description.
    * With either ASCII or full Unicode text, if you want _full_ control of what counts as a "word" or a "word boundary", use **Search Mode** = **Regular Expression** instead of using **Normal** with **Match whole word only**: regular expressions allow you full and precise control of what is allowed before and after what _you_ consider a "whole word", rather than relying on someone else's definition.

* **☐ Match case**: if enabled, searches must match in case (so a search for "it" will not find "It" or "IT").  The regular expression `i` flag will override this checkbox, where `(?i)` will make the search case insensitive, and `(?-i)` will make the search case sensitive.
* **☐ Wrap Around**: if enabled, when the search reaches the end of the document, it will wrap around to the beginning and continue searching

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
    * **☐** The unlabeled checkbox near the **Find Next** button changes the single **Find Next** button into two buttons with **▲** and **▼ Find Next** triangle arrows (or **<<** and **>>** buttons before v7.8), which mean "search backward / find previous" and "search forward / find next".  Hovering over this checkbox with the mouse will, after a slight pause in movement, pop up a tooltip indicating "2 find buttons mode" to remind you of what the checkbox is for.
* **Count**: Counts how many matches are in the entire document, or in the specified direction, or possibly "In Selection", and shows that count in the message section at the bottom of the dialog box
* **Find All in All Opened Documents**: Lists all the search-results in a new **Search results** window; searches through all the file buffers currently open in Notepad++
* **Find All in Current Document**: Lists all the search-results in a new **Search results** window; only searches the active document buffer
* **Close**: Closes the search dialog

* **Replace**: Replaces the currently-selected match.  (If no match is currently selected, it behaves like **Find Next** and just highlights the next match in the specified direction)
    * On the **Replace** tab, there is an up-down arrow button **⇅** near the **Find what** and **Replace with** inputs which swaps the values of those two inputs, to make it easy to do the opposite replacement of the one that's active.  Please note that not all [regular expression substitution escapes](#substitutions) will have the same meaning when swapped into the search expression. (The swap feature was added in v8.2.1.)
* **Replace All**: With **☑ Wrap Around** ticked, it makes one pass through the active document, from the very top to the very bottom, and replaces all occurrences found.  With **☐ Wrap Around** unticked, it searches from the caret to the end of the file (if **☐ Backward direction** is unticked) or from the beginning of the file to the caret (if **☑ Backward direction** is ticked) and replaces all occurrences found in that region.
    * NOTE: for regular expressions, this will be equivalent to running the regular expression multiple times, which is _not_ the same as running with the /g global flag enabled that is available in the regular expression engines of some programming-languages.
    * To clarify the **Replace All** results, depending on the condition of the various settings:

        Previous<br>Selection | Wrap Around | Backward Direction | In Selection | Range
        :-:|:-:|:-:|:-:|:----
        NO |OFF|OFF|OFF|From  CARET location      to  END of file
        YES|OFF|OFF|OFF|From  START of selection  to  END of file
        NO |OFF|ON |OFF|From  START of file       to  CARET location
        YES|OFF|ON |OFF|From  START of file       to  END of selection
        YES|-/-|-/-|ON |From  START of selection  to  END of selection
        -/-|ON |-/-|OFF|From  START of file       to  END of file

        _The **Previous Selection** column indicates that a range of text has been selected already. The **Wrap Around** and **Backward Direction** and **In Selection** columns refer to the setting of the checkboxes described above. The **Range** column describes the range of the document that is affected by the **Replace All**. A value of "-/-" means that the setting does not influence the outcome for that combination of conditions._

* **Replace All in All Opened Documents**: same as **Replace All**, but goes through all the documents open in Notepad++, not just the active document.

The above actions may be initiated via mouse by pressing the appropriate button, or via special `Alt` key combinations.  With focus on one of the Find dialog windows, press and release the `Alt` key.  This will cause Notepad++ to underline a single character in the text of *most* of the buttons.  Pressing Alt and one of the underlined characters will be the same as pressing the same button with the mouse, i.e., the chosen action will be initiated.  The Alt technique works for controls other than buttons as well, e.g., a checkbox control can be ticked/unticked via pressing its Alt key command.

**Find Next** has a special way of being invoked by keyboard control.  Pressing Enter when the Find dialog has input focus will initiate the **Find Next** command in the direction indicated by **Backward direction**.  Pressing Shift+Enter when the Find dialog has input focus will run the **Find Next** in the ***opposite*** direction as that indicated by **Backward direction**.  Hovering over the **Find Next** button with the mouse will, after a slight delay, pop up a tool tip indicating *Use Shift+Enter to search in the opposite direction* as a reminder of this capability.

When a find-family function is invoked via the Search menu, toolbar, or keyboard combination, the word at the caret (or the selected text, if any) is automatically copied into the **Find what** edit box.  This behavior cannot be disabled; it always happens.  To avoid this in a limited way, use the mouse ONLY to move input focus from an editing tab buffer to an already-open Find dialog, or make sure your caret is not "touching" a word and that there is no active selection when invoking the find-family command.  Aside:  This auto-copy feature can be exploited to get multi-line data into the **Find what** edit box, something that it is not possible to do via only typing into the box.  Simply select the multi-line text that you want to search for, and then call up the Find dialog via one of its functions.  The selected text will appear as usual in the **Find what** box.  The line-ending character(s) won't be visible, but they will be there and will be matched when a search/replace action is initiated.

A valid **Find what** edit box entry length ranges from 1 to 2046 characters.  A valid **Replace with** edit box entry length ranges from 0 to 2046 characters.  Any text entered/pasted into these boxes beyond the 2046th character is simply ignored when an action is invoked.  Note that a replacement operation with a zero-length **Replace with** box entry is effectively a deletion of the matched text.

Selecting **Search Mode** of **Regular expression** will cause the **Match whole word only** option to become deselected and disabled.  A possible workaround to allow doing this type of searches is to add `\b` to the beginning and end of your regular expression **Find what** text.

The **Find what** and **Replace with** edit boxes have a dropdown arrow which allows the user to repeat searches conducted previously.  For a given run of Notepad++, the search history can grow rather large; when Notepad++ is exited, it only saves the last 10 items in the history by default; number of search/replace terms retained may be changed by editing the `config.xml` configuration file, per [Preferences for Advanced Users](../preferences/#preferences-for-advanced-users).  The **Find in Files** tab's **Filters** and **Directory** text boxes have this "history" feature as well.  This history can be activated by clicking on the down-arrow with the mouse (or, equivalently, pressing Alt+down) to "drop down" the box, or directly (without dropping) by using the down (and/or up) keys -- be careful though, sometimes when editing a control with the history feature, a user will accidentally hit an up or down arrow key when they really mean to press left or right arrow; this unfortunately wipes out the search/replace expression (as those are edited most often) that was being worked on and replaces it with some different text from the history buffer.  Unwanted items in the histories may be removed by dropping-down the box, highlighting the item to be removed, and pressing the Delete key (requires version 7.9.3 or later).

The **In selection** option will automatically be chosen by Notepad++ if a Find dialog window is opened when more than 1024 characters occur in the active selection.  The selected text will also be placed in the **Find what** box.  Running a **Count** or **Replace All** action without making other changes to the search parameters will result in *Count: 1 match* or *Replace All: 1 occurrence was replaced*, respectively, which is likely not what was intended.  The proper resolution for this situation is to change the **Find what** text if the intention is to search within-selection, or deselect **In selection** if the intention is to search for a fairly long block of text.

The status bar area of the Find dialog keeps the user informed of what occurred during an action.  For example, it might say *Mark: 1 match* or *Find: Invalid regular expression*.  Colors are used in the status bar for emphasis:  red for some sort of error; green or blue for various success or general information.

**Important remark**: When the regular expression search mode is invoked, the red alert error message "Find: Invalid regular expression" appears **ONLY** when you hit the **Find Next** button. All other possible actions lead to simply notify you that no result occurs, whereas, in fact, your search regular expression is just malformed. So, always do a **Find Next** search first, to test the validity of your regular expression input.

Notepad++ uses a flashing of the Find dialog window and the main Notepad++ window itself (when the Find dialog is not open) to indicate that search text has not been found (or possibly that a **Wrap around** in the search has occurred).  In general, if a search results in no matches, and the Find dialog window is open, that window will flash briefly as a failure indication.  If the Find dialog window is NOT open, and a failed search is initiated (e.g. via **Find Next** on the **Search** menu), the main Notepad++ window will flash briefly, again, as an indicator of the lack of success.  With the Find dialog window closed, but with **Wrap around** previously activated, a search that causes a wrap at an end of the file to occur will also cause the Notepad++ main window to flash.  In addition, audible feedback will be provided if a **Find Next** or **Replace** action results in the **Find what** text not being encountered; the sound can be muted using the **Mute all sounds** option in [**Preferences > MISC**](../preferences/#misc).

If a search action is invoked by keyboard command with the Find dialog window open and input focus in the editing window, an unsuccessful search will result in input focus being changed to the Find window.  Presumably, the user would want to conduct a different search at this point?

*Disclaimer:*  It is Notepad++'s design intention to fulfill some basic searching/replacing capability.  As such, Notepad++ searching is not infinitely flexible and capable of meeting all needs.  For such power needs, please turn to external tools, some of which integrate well with Notepad++.  Integrating well means that after such tools produce results, they can tell Notepad++ which files to open and which line and column numbers to move the caret to, in order to work with matched results.  Examples of such power file/text searching tools might be:  "GrepWin", "PowerGREP", "FileSeek", "Everything" and many others.

### Find in Files tab

Find in Files allows both finding and replacing. You can choose an extension filter (**Filters:**), the containing folder (**Directory:**), and whether to also process hidden files or subfolders.  

The **Filters** list is a space-separated list of wildcard expressions that cmd.exe can understand, like `*.doc foo.*`.   

* Wildcards can include `*` for zero or more of any character, and `?` for exactly one of any character.
* Most characters work as literals.  However, space is used as the separator, and thus cannot be used as a literal in your filter.  Some punctuation characters have special meanings (like the `?` and `*` wildcards, or the `!` exclusion or `!+\` for recursive exclusion), and cannot be used as literals.  Also, the `;` causes problems, so even though Microsoft _allows_ it in file and path names, using a `;` in the **Filters** box will not work as you might hope.  If you want to match a space or a semicolon `;` or other problematic-punctuation in your file or folder for your **Filter** (whether for inclusion or exclusion), then use the `*` and/or `?` wildcards instead.  (So `x?y.txt` will match the file `x;y.txt` or `x y.txt` (with a space between `x` and `y`).)  And sorry, no, you cannot use quotes around a path-with-spaces to allow the spaces to work as literals: the space is a separator in this field.
* If you have a blank filter, it is implied to be `*.*`.  
* As of Notepad++ v7.8.2, you can also exclude certain file patterns by prefixing the filter with a `!`; 
for example, **Filters:  `!*.bin *.*`** will exclude files matching `*.bin` from the search results, but include any other filename.  (Before v7.8.7, if you had at least one exclusion in your filter, you needed to have at least one inclusion in your filter, otherwise it excluded files from the 0 matched inclusion files, resulting in no files matched, which probably isn't what you wanted.  This was fixed in v7.8.7, so now you can have a lone exclusion like `!*.bin` and have it match any file not ending in `.bin`.)  
* As of Notepad++ v8.2, you can also exclude particular folders from the search: Exclusion operator is alway `!` at the begining. In order to distinguish folder from file, `\` should be used as prefix of the folder name/pattern, following `!`. That allows the exclusion of the directories under the root directory you want to search (the 1st level of matched directories).
If users need to exclude folders with the same name (or names matched the specific pattern) in all levels, the `+` should be put between `!` and `\` to exclude them recursively. For example:
    * `!\tests` will not search any files in the `tests` folder
    * `!\bin*` will not search any files in the `bin` folder or `bin64` folder (or any other directory that matches `bin*`)
    * `!+\log*` will _recursively_ not search any files in folders that start with log (so directories like `.\log`, `.\logs`, `.\other\logfiles`, `.\many\layers\deep\log` will all be excluded from the search)
    
    *Note*: "inclusion of folder" is not allowed, and such pattern will be ignored
    
* As of Notepad++ v8.2, if you hover your cursor over the **Filters:** label, a helpful popup will show example syntax for you
* Please also note that the PathMatchSpec() Windows API is being used for the **Filters**, as its behavior departs from cmd.exe wildcard parsing sometimes.  

The **Directory** is the containing folder for where to search.  It has three options that affect its behavior:

* **☐ Follow current doc** ⇒ if enabled, it will default to searching the folder that contains the current active document (this sets the `fifFolderFollowsDoc` in `config.xml`).
* **☐ In all sub-folders** ⇒ if enabled, it will recursively search sub-folders of the given folder.
* **☐ In hidden folders** ⇒ if enabled, it will search hidden sub-folders as well as normally-visible sub-folders.

### Find in Projects tab

Find in Projects allows both finding and replacing. The files used for this operations are specified by the following check marks:

* **☐ Project Panel 1** ⇒ if enabled, all files listed in Project Panel 1 will be included into the search/replace operation
* **☐ Project Panel 2** ⇒ if enabled, all files listed in Project Panel 2 will be included into the search/replace operation
* **☐ Project Panel 3** ⇒ if enabled, all files listed in Project Panel 3 will be included into the search/replace operation.

Only Project Panels which are currently open can be searched. The checkmarks of Project Panels which are not currently open are grayed out.

The **Filters** list works the same way as described in the previous **Find in Files** section.

### Mark tab

The Mark tab from the Find/Replace dialog will perform searches similar to the Find tab, in the current document or selection:

* When **Bookmark line** is checked, a bookmark is dropped on each line where an individual hit occurs.  In the case where an individual hit spans multiple lines, each line in the span will receive the bookmark.

* Otherwise, the matched pattern is highlighted according to the Settings -&gt; Style Configurator -&gt; Global Styles , Find Mark Style setting.  (See also [Style Configurator](../preferences/#style-configurator).)

In either case, the **Mark All** button will perform the marking.  Similar to [**Replace All**](#find-replace), **Mark All** will search from the beginning of the document to the end if **Wrap Around** is ticked; if **Wrap Around** is not ticked, it will mark from the caret position to the end of the file (if **Backward direction** is not ticked) or from the beginning of the file to the caret position (if **Backward direction** is ticked).

To control whether highlighting or bookmarks accumulate over successive searches, use the **Clear all marks** button to remove marks, or check **Purge for each search** for this action to be performed automatically on each search.  When the **Clear all marks** button is pressed, any marked text will have the marking background coloring removed; additionally, any bookmarks previously set will be removed if the **Bookmark line** checkbox is checked.

Once some text in a document is marked, it may be copied to the clipboard by pressing the **Copy Marked Text** button.  This feature is also invocable from the Search menu, and in order to be used in a macro, the Search menu version of this copy command must be used.

Highlighting is also available in Incremental search, and the style setting is Settings -&gt; Style Configurator -&gt; Global Styles , Incremental Highlighting instead.

#### Bookmarks vs Marks

Bookmarks and Marks are two slightly different things, though the **Mark** tab can affect both.  A Mark will highlight the individual match(es) in the text; a Bookmark affects the whole line, and is usually displayed as a circle (`●`) in the margin (though [**Settings > Preferences > Margin/Border/Edge**](../preferences/#margins-border-edge) has a `☐ Display bookmark` toggle that will influence whether Bookmarks have that circle indicator or not).

Bookmarks, whether visible or not, have a menu that can control and navigate Bookmarks.  This menu is accessible either as **Search > Bookmark** or by right clicking in the Bookmark portion of the margin (between the line number and the text, if line numbers are displayed).  This menu has options to toggle the state of the current line's Bookmark, to navigate to the next or previous Bookmark, to clear all Bookmarks, to cut or copy Bookmarked lines, to paste over (replace) Bookmarked lines, to delete Bookmarked (or non-Bookmarked) lines, or to invert all the Bookmarks (so all lines with a Bookmark have the Bookmark removed, and all lines without a Bookmark have a Bookmark added).

### Search results window

After running one or more **Find All in ...** commands, a new **Search results** window appears, and within it is placed a **Search results** tab.  The **Search results** window may be opened and/or given input focus by using the menu command **Search > Search Results Window** or the F7 keyboard shortcut.  *Note:*  That menu command will seem to not do anything if there haven't been any **Find All in ...** commands run since Notepad++ was opened.

*Definition:*  **Find All in ...** commands include:

|*Which **Find All in ...** command*| *Find window owner tab*|
|-----------------------------------|------------------------|
|Find All in All Opened Documents   | **Find**               |
|Find All in Current Document       | **Find**               |
|Find All                           | **Find in Files**      |
|Find All                           | **Find in Projects**   |

The **Search results** window by default appears docked at the bottom of the Notepad++ main window.  Like other such windows, it can be moved or even be a free-floating window.

From **Find All in ...** searches, three types of sections are added to the **Search results** window.  First is a line describing what was searched for, how many total matches (known as "hits") occurred (this is also shown in the title bar for the window, for the most recently-occurring search), and how many files had matches.  Second is a line that shows the filename with the matches and the count of matches for that file (this type will be repeated if the search found multiple files with matches).  Last comes the details about the matches found, including line number and the line contents with the matched text emphasized.  The default emphasis is red text on a yellow background, but this may be changed in the Style Configurator's "Search result" Language area.

When Notepad++ populates the **Search results** window, it does so using one line for each match found by the search.  Note that this can and often does end with the same source file line being repeated multiple times in the output.  An example of this would be if you are searching for "the" in the line of text that reads "Now is the time for all good men to come to the aid of their country"; the **Search results** window would list the line twice, once with the word "the" called out in red text with a yellow background, and a second time with "the" in "their" similarly emphasized.

When the **Search results** window has input focus, the currently active line has a different background color, much like how the main editor window does by default.  Unlike the main editor window, where the current-line background feature may be turned off, the **Search results** window always has a background highlight for its active line.

Use the up and down arrows to navigate within the **Search results** window when it has input focus.  Double-clicking with the mouse or hitting ENTER when input focus is on a specific match will move the editor window to that match and cause its text to be selected.

Other ways to navigate back to an editor window via the **Search results** window matches include the **Search** menu items **Next Search Result** (keyboard: F4) and **Previous Search Result** (keyboard: Shift+F4).  These can be invoked regardless of where input focus is in Notepad++.

The *Delete* key can be used to delete individual results, file matches or whole search matches in the **Search results** window, depending on which type of line is active when the key is pressed.  As the result history is hierarchical, that is, tree-like, pressing *Delete* when in a higher-level element of the tree removes that whole branch.  Thus:

|*Pressing Delete when **Search results** active line starts with...*| *What is removed*                                                                              |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
|the text: "Search"                                               | that "Search" line, all pathname lines under it, and all "Line" lines under the pathname lines |
|a pathname                                                       | that pathname line and all "Line" lines under it                                                |
|the text: "Line"                                                 | only that line                                                                                 |

Multiple searches will be listed under separate headers, which are "foldable", so you can hide or unhide results from previous searches.  When you run a new search, previous searches are folded closed.

If the source file lines are judged by Notepad++ to be too long when they are copied to be placed in the **Search results** window, they will be truncated and **...** will be added at the end.  In this case, matched text occurring in the line after the **...** position will not be emphasized.  However, using a method to return to the editor window (e.g. pressing Enter) will result in the correct selection of matching text there.  The length limit is 1024 characters; this includes the match line number information and other formatting.

If a search is conducted such that a match which spans two or more lines occurs, only the contents of the *FIRST* line of that match will be copied into the **Search results** window.  However, using a method to return to the editor window (e.g. pressing Enter) will result in the correct selection of multi-line matching text there.

#### *RightClick* commands in the client area of a **Search results** window's tab

##### Copying text from the **Search results** window

There are two ways to copy exact text from the **Search results** window:  Make sure input focus is in the **Search results** window by selecting some text and use the keyboard's *Ctrl+c*, or use the mouse's *RightClick* to invoke the context menu and select **Copy**.  These two copy mechanisms produce identical results.  Another choice is to use the context menu's **Copy Selected Line(s)** command; this type of copy can be thought of as a "Copy Special".  It copies the text of ENTIRE LINES from the results, WITHOUT any search information (called "metadata") being included in what is copied.

Here's a more detailed description of what happens for *RightClick* > **Copy Selected Line(s)**:

First, if the user makes a selection of text in the **Search results** window and copies it this way, only the lines of text touched (even partially) by the selection are part of the copy.  All other text with information about the search (pathname, line number, etc.) is *not* copied, even if part of the selection.  Secondly, if there is no active selection when the *RightClick* > **Copy Selected Line(s)** is invoked, results depend upon what exactly is under the cursor during the *RightClick*:

| *RightClick* item     | What gets copied when *RightClick* > **Copy Selected Line(s)** is run |
|-----------------------|-----------------------------------------------------------------------------------------------------|
|a line with line # info|the entire line of the *RightClick* but without line number text                                     |
|a pathname header line |all the lines for that single file without pathname or line number text                              |
|a "search" header line |all the lines for that search (1 or more files) without search header, pathname or line number text  |

*Tip*:  It is possible to select and copy a rectangular selection of data from the **Search results** window.  This is done using the usual Shift+Alt+arrow keys or by holding Alt+LeftClick and dragging with the mouse.  This is really only practical when using the *Ctrl+c* method of copying; *RightClick* > **Copy Selected Line(s)** only copies entire lines, and this copy will only copy the single full line at the top/bottom of the column block.

There is a capability to copy a list of the files that contained hits from past searches (v8.0.0 and later).  The **Copy Pathname(s)** context menu command will copy to the clipboard the full pathnames of all files appearing in **Search results**.

##### Other commands

There are some commands that don't need a lot of explanation; these are:

* **Collapse all**
* **Uncollapse all**
* **Select all**
* **Clear all**
* **Open all**

The **Search results** window/tab accumulates results from every **Find All in ...** search the user does; the results from old searches remain until the user removes them.  Individual results can be deleted with the *Delete* key, or all previous results can be deleted by invoking **Clear all**.  Stale results can be removed to reduce visual clutter, or when it is desired that a follow-on action should not be affected by old results.  An example of this would be the **Open all** command which opens *all* files listed in the **Search results** tab that have previously had hits.  If the search history in **Search results** is really long, it may not be desirable to open all files listed there, so using **Clear all** before doing some new searches (with the intent to **Open all** afterwards) may be the thing to do.

The **Select all** command is self-explanatory:  *ALL* text in the **Search results** tab will be selected

The contents of the **Search results** tab are in the form of a tree.  When Notepad++ adds to the result history, it does so in an uncollapsed way, that is, the user can see all of the information from the recently-added search.  However, before adding new results, Notepad++ will collapse all previous result data; perhaps it is deciding that the most-recent search is the most important?

The user can collapse/uncollapse "branches" of this tree.  To collapse, click with the mouse on the little box symbol with an interior `-`, found to the left of each line.  After doing so, that part of the tree will be collapsed (removed from view) and the first line of the branch (remaining visible) will then show a `+` in the box symbol.  To uncollapse an individual item that has previously been collapsed (either by the user or by Notepad++'s automatic mechanism), simply click the box symbol with the `+`.  That branch will then be expanded and again shown.

The **Collapse all** and **Uncollapse all** commands perform the corresponding actions on *ALL* elements of the entire result history in the **Search results** window at once.  Perhaps a better name for **Uncollapse all** would have been the more-conventional "Expand all"?

##### Searching in previously-found results (secondary searching)

Perhaps you have done a search and your results are in a tab in the **Search results** window.  Now you'd like to conduct a search but with a scope of only the files that have previous matches.  Or maybe you want to look only in the *lines* matched by previous searches, not only the matched files, tightening the search criteria even more.  Can you do this sort of second-level searching with Notepad++?  Yes, by *RightClick*ing the **Search results** window client area and selecting **Find in these search results...**.

Selecting **Find in these search results...** will cause a window to pop up, and this window looks much like the standard **Find** window, but is stripped down a bit.  Once you input your search parameters and choose **Find All**, a *new* **Search results** tab will open (in the **Search results** window) with the results of the "refined" search.

The popup window has a parameter not available in the searches described earlier:  **☐ Search only in found lines**.  Checking this box limits the search to lines that appear in matched files in the parent **Search results** window.  Unchecking the box will cause the new search to examine previously matched files in their entirety.  When a search has been limited to previously-found lines, its results will indicate this by using this type of output:  `Search "___" (__ hits in __ files - Line Filter Mode: only display the filtered results)` as opposed to the normally seen:  `Search "___" (__ hits in __ files)`

*Tip:*  Use the *RightClick* option **Clear all** to limit the scope of these types of searches (before invoking the secondary search!) -- remember: a **Find in these search results...** search will look in files matched by ALL previous searches whose results are still present in the parent **Search results** tab.

*Tip:*  Since the newly opened **Search results** window also has a *RightClick* menu, you may do another **Find in these search results...** based upon the new results, focusing your search for some bit of data even more.  This type of refinement may be repeated as much as desired.  [Note that the title bar of the window does *not* show the hit count of the currently active tab, but rather shows the hit count of the *first* **Search results** tab of the window.]

*Note:*  The commands that switch input focus to the **Search results** window always activate the *first* **Search results** tab, not any additional **Search results** tabs that may have been created.

*Note:*  The contents of the **Search results** window are discarded upon Notepad++ shutdown.  If there is data of importance there it should be copied, using one of the methods above, and saved in a more-permanent location.

##### Search results configuration options

There are currently two ways to configure the **Search results** window behavior, both located in the mouse's *RightClick* context menu:

* **Word wrap long lines**
* **Purge for every search**

These are checkmarkable menu items; invoke the menu item once to turn the feature on (checkmark will appear on the menu) and run it again to turn it off (checkmark no longer appears). These configuration settings are remembered by Notepad++ until their states are again changed by the user.

When **Word wrap long lines** is turned on (enabled), the **Search results** window text will wrap at the right edge, and be continued on the next visible line.  With the feature off, the window will have a horizontal scrollbar so that the rightmost text on long lines may be scrolled into the user's view.  This feature was introduced in Notepad++ version 7.9(.0).

By default, the **Search results** window accumulates all of your prior **Find All in ...** type searches.  When a new search is executed, old results get collapsed so that only the most-recent results are fully visible at the top of the window.  The old searches remain toward the bottom of the window for possible future reference by expanding them. One use for retaining results from prior searches is to do several different searches, and then execute **Open All** command from the window's right-click context menu -- this will open all files hit by any previous series of possibly disparate searches.

To some users these older results accumulating are an annoyance -- their data may become out of date quickly with changes to files -- so Notepad++ 7.9.6 and higher support a setting that, after turned on, removes any old search data from the window before populating it with new.  The setting is set/cleared by right-clicking anywhere in the **Search results** window, causing the context menu to appear; a checkable menu item entitled **Purge for every search** is present in this menu.  After turning the feature on, which will cause its menu item to have a checkmark, running a search will purge old results.

## Dialog-free search/mark actions

### Searching

The following commands, available through the Search menu or keyboard shortcuts, perform a search without invoking a dialog, because they search for the previous search target or for a word or selection in the current document:

* **Find Next / Find Previous** Repeat searching the current search target, either down or up.

* **Next Search Result / Previous Search Result** Jump to the next or previous search result recorded in the Search Results Window. The Search Results Window is created in response to any of the dialog-based **Find All** commands. If it exists, you can use  **Search  -&gt;  Search Results Window** to make it visible and to switch the input focus between the Search Results Window and the current document.

* **Find (volatile) Next / Find (volatile) Previous** Attempt to find the word the caret is in, or the selected text, down or up. The searched word or selection is not remembered in the find history, and the search will not be repeatable with **Find Next / Find Previous**. That's why it's called volatile.

* **Select and Find Next / Select and Find Previous** Attempt to find the word the caret is in, or the selected text, down or up. The searched word or selection is remembered in the find history, and the search can be repeated with **Find Next / Find Previous**.

All dialog-free search actions do preserve the current search options set in the Find dialog like Match case or Wrap around.

### Marking with a color/style and Highlighting

Use the Mark All or Unmark All submenus of the Search menu to mark/unmark all occurrences of the selected text or word the caret is in if there is no active selection.  You have a choice of five different colors/styles (numbered 1 through 5) in which to mark text in this manner. Mark One submenu options (version 7.9.6 and later) work similarly, but only on the single occurrence of selected text or caret word.

The settings for each of the 5 available colors/styles are Settings -&gt; Style Configurator -&gt; Global Styles , Mark style #.

If you've highlighted some groups of text in this manner, and you wish to copy those sections, the Copy Styled Text submenu of the Search menu will allow you to do that.  Quick search for previously marked text is possible via the Jump Up or Jump Down submenu choices.

Note: Unfortunately, the Mark All submenu name can cause some confusion between an identically-named action button in the Mark tab of the Find family dialog.  The two types of "marking" are different but do share some features.  For example, the Copy Styled Text submenu commands will allow you to copy text that has been styled with number 1 through 5 styling OR text that has been marked using the Mark tab of Find.

You can also cause all occurrences of the word at the caret to get dynamically highlighted if you enable Smart Highlighting; the mark style then is Settings -&gt; Style Configurator -&gt; Global Styles , Smart Highlighting. You may choose there whether the matching should be sensitive to case.

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
* The **<** and **>** buttons navigate backward and forward through the search results (wrapping around when it reaches the end or start of the document).
* If the **☐ Highlight all** checkbox is not checked, it will only highlight the current match; if it is checked, all matches will be highlighted.
* If the **☐ Match case** checkbox is checked, the results will only match if case is exactly the same, otherwise case doesn't matter.
* To the right of those checkboxes, a message about the results will occur: either the number of matches, a message that indicates that you've wrapped around to the top or bottom of the document, or "Phrase not found" if there are no matches.  When there are no matches, the **Find** box also changes color.

## Comparison between "Select and Find Next" and "Find Next (Volatile)"

This section is aimed to clear the confusion about these 2 similar commands.

Both commands "Select and Find Next" (Ctrl+F3) and "Find Next (Volatile)" (Ctrl+Alt+F3) does the same thing (almost): select the current word (on which caret is) then jump to the next occurrence.

However, there is a slight difference between these 2 commands: "Select and Find Next" remembers the searched word, "Find Next (Volatile)" does not.

Here's an example:

If you do "Select and Find Next" command for word word1 then you can always use "Find Next" command (F3) or "Find Previous" command (Shift+F3) to search word1, even the caret is on word2.

If your caret is on word word2, "Find Next (Volatile)" will search the next word2. Now if you move your caret on word word3 and do "Find Next (Volatile)", it will search next word3, and word2 is forgotten.

## Extended Search Mode

In extended mode, these escape sequences (a backslash followed by a single character and optional material) have special meaning, and will not be interpreted literally.

* `\n`:  the Line Feed control character LF (ASCII 0x0A)
* `\r`:  The Carriage Return control character CR (ASCII 0x0D)
* `\t`:  the TAB control character (ASCII 0x09)
* `\0`:  the NUL control character (ASCII 0x00)
* `\\`:  the literal backslash character (ASCII 0x5C)
* `\b`:  the binary representation of a byte, made of 8 digits which are either 1's or 0's. †
* `\o`:  the octal representation of a byte, made of 3 digits in the 0-7 range
* `\d`:  the decimal representation of a byte, made of 3 digits in the 0-9 range
* `\x`:  the hexadecimal representation of a byte, made of 2 digits in the 0-9, A-F/a-f range.
* `\u`:  The hexadecimal representation of a two-byte character, made of 4 digits in the 0-9, A-F/a-f range. In Unicode builds, finds a Unicode character (for instance, `\u2020` matches the `†` char, in an UTF-8 encoded file). In ANSI builds, finds characters requiring two bytes, like in the Shift-JIS encoding. †

†NOTE: While some of these Extended Search Mode escape sequences look like regular expression escape sequences, they are not identical.  Ones marked with † are different from or not available in regular expressions.

## Regular Expressions

Notepad++ regular expressions use the Boost regular expression library v1.78 (as of NPP v8.2), which is based on PCRE (Perl Compatible Regular Expression) syntax, only departing from it in very minor ways. Complete documentation on the precise implementation is to be found on the Boost pages for [search syntax](https://www.boost.org/doc/libs/1_78_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html) and [replacement syntax](https://www.boost.org/doc/libs/1_78_0/libs/regex/doc/html/boost_regex/format/boost_format_syntax.html)

The Notepad++ Community has a [FAQ on other resources for regular expressions](https://notepad-plus-plus.org/community/topic/15765/faq-desk-where-to-find-regex-documentation).

Note: Starting in v7.8.7, regex backward search is disallowed due to sometimes surprising results. If you really need this feature, please see [**Allow regex backward search**](../preferences/#preferences-for-advanced-users) to learn how to enable this option.

### Regex Special Characters

In a regular expression (shortened into regex throughout), special characters interpreted are:

#### Single-character matches

* `.` or `\C` ⇒ Matches any character. If you check the box which says **. matches newline**, the dot match any character, including newline sequences.  With the option unchecked, then `.` will only match characters within a line, and not the newline sequences (`\r` or `\n`).

* `\X` ⇒ Matches a single non-combining character followed by any number of combining characters. This is useful if you have a Unicode encoded text with accents as separate, combining characters.  For example, the letter `ǭ̳̚`, with four combining characters after the `o`, can be found either with the regex `(?-i)o\x{0304}\x{0328}\x{031a}\x{0333}` or with the shorter regex `\X`.

* `\$` , `\(` , `\)` , `\*` , `\+` , `\.` , `\?` , `\[` , `\]` , `\\` , `\|` ⇒ Prefixing a special character with `\` to "escape" the character allows you to search for a literal character when the regular expression syntax would otherwise have that character have a special meaning as a regex meta-character.   
    * The characters `$ ( ) * + . ? [ ] \ |` all have special meaning to the regex engine in normal circumstances; to get them to match as a literal (or to show up as a literal in the substitution), you will have to prefix them with the `\` character.  
    * There are also other characters which are special only in certain circumstances (any time a charcter is used with a non-literal meaning throughout the Regular Expression section of this manual); if you want to match one of those sometimes-special characters as literal character _in those situations_, those sometimes-special characters will also have to be escaped _in those situations_ by putting a `\` before it.  
    * _Please note_: if you escape a normal character, it will sometimes _gain_ a special meaning; this is why so many of the syntax items listed in this section have a `\` before them.

##### Match by character code

It is possible to match any character using its character code.  This allows searching for any character, even if you cannot type it into the FIND box, or the FIND box doesn't seem to match your emoji that you want to search for.  If you are using an ANSI encoding in your document (that is, using a character set like Windows 1252), you can use any character code with a decimal codepoint from 0 to 255.  If you are using Unicode (one of the UTF-8 or UTF-16 encodings), you can actually match any Unicode character.  These notations require knowledge of hexadecimal or octal versions of the character code.  (You can find such character code information on most web pages about ASCII, or about your selected character set, and about UTF-8 and UTF-16 representations of Unicode characters.)

* `\0ℕℕℕ` ⇒ A single byte character whose code in octal is ℕℕℕ, where each ℕ is an octal digit.  (That's the number `0`, not the letter `o` or `O`.)  This notation works for for codepoints 0-255 (`\0000` - `\0377`), which covers the full ANSI character set range, or the first 256 Unicode characters. For example, `\0101` looks for the letter `A`, as 101 in octal is 65 in decimal, and 65 is the character code for `A` in ASCII, in most of the character sets, and in Unicode.

* `\xℕℕ` ⇒ Specify a single character with code ℕℕ, where each ℕ is a hexadecimal digit. What this stands for depends on the text encoding. This notation works for for codepoints 0-255 (`\x00` - `\xFF`), which covers the full ANSI character set range, or the first 256 Unicode characters.  For instance, `\xE9` may match an `é` or a `θ` depending on the character set (also known as the "code page") in an ANSI encoded document.

These next two only work with Unicode encodings (so the various UTF-8 and UTF-16 encodings).

* `\x{ℕℕℕℕ}` ⇒ Like `\xℕℕ`, but matches a full 16-bit Unicode character, which is any codepoint from U+0000 to U+FFFF.

* `\x{ℕℕℕℕ}\x{ℕℕℕℕ}` ⇒ For Unicode characters above U+FFFF, in the range U+10000 to U+10FFFF, you need to break the single 5-digit or 6-digit hex value and encode it into two 4-digit hex codes; these two codes are the "surrogate codes" for the character.  For example, to search for the `🚂` STEAM LOCOMOTIVE character at U+1F682, you would search for the surrogate codes `\x{D83D}\x{DE82}`.
    - If you want to know the surrogate codes for a give character, search the internet for "surrogate codes for _character_" (where _charcter_ is the fancy Unicode character you need the codes for); the surrogate codes are equivalent to the two-word UTF-16 encoding for those higher characters, so UTF-16 tables will also work for looking this up.  Any site or tool that you are likely to be using to find the U+###### for a given Unicode character will probably already give you the surrogate codes or UTF-16 words for the same character; if not, find a tool or site that does.
    - You _can_ compute it yourself from the character code, but only if you are comfortable with hexadecimal and binary.  Skip the following bullets if you are prone to mathematics-based PTSD.
        - Start with your Unicode U+######, calling the hexadecimal digits as `PPWXYZ`.
        - The `PP` digits indicate the plane.  subtract one and convert to the 4 binary bits `pppp` (so `PP`=`01` becomes `0000`, `PP`=`0F` becomes `1110`, and `PP`=`10` becomes `1111`)
        - Convert each of the other digits into 4 bits (`W` as `wwww`, `X` as `xxvv`, `Y` as `yyyy`, and `Z` as `zzzz`; you will see momentarily why two different characters used in `xxvv`)
        - Write those 20 bits in sequence: `ppppwwwwxxvvyyyyzzzz`
        - Group into two equal groups: `ppppwwwwxx` and `vvyyyyzzzz` (you can see that the `X` ⇒ `xxvv` was split between the two groups, hence the notation)
        - Before the first group, insert the binary digits `110110` to get `110110ppppwwwwxx`, and split into the nibbles `1101 10pp ppww wwxx`.  Convert those nibbles to hex: it will give you a value from `\x{D800}` thru `\x{DBFF}`; this is the High Surrogate code
        - Before the second group, insert the binary digits `110111` to get `110111vvyyyyzzzz`, and split into the nibbles `1101 11vv yyyy zzzz`.  Convert those nibbles to hex: it will give you a value from `\x{DC00}` thru `\x{DFFF}`; this is the Low Surrogate code
        - Combine those into the final `\x{ℕℕℕℕ}\x{ℕℕℕℕ}` for searching.
    - For more on this, see the Wikipedia article on [Unicode Planes](https://en.wikipedia.org/wiki/Plane_(Unicode)), and the discussion in the Notepad++ Community Forum about how to [search for non-ASCII characters](https://community.notepad-plus-plus.org/post/66322)

##### Collating Sequences

*  `[[.`_col_`.]]` ⇒ The character the _col_ "[collating sequence](https://www.boost.org/doc/libs/1_70_0/libs/regex/doc/html/boost_regex/syntax/collating_names.html)" stands for. For instance, in Spanish, `ch` is a single letter, though it is written using two characters. That letter would be represented as `[[.ch.]]`. This trick also works with symbolic names of control characters, like `[[.BEL.]]` for the character of code 0x07. See also the discussion on character ranges.

##### Control characters

* `\a` ⇒ The BEL control character 0x07 (alarm).

* `\b` ⇒ The BS control character 0x08 (backspace). This is only allowed inside a character class definition. Otherwise, this means "a word boundary".

* `\e` ⇒ The ESC control character 0x1B.

* `\f` ⇒ The FF control character 0x0C (form feed).

* `\n` ⇒ The LF control character 0x0A (line feed). This is the regular end of line under Unix systems.

* `\r` ⇒ The CR control character 0x0D (carriage return). This is part of the DOS/Windows end of line sequence CR-LF, and was the EOL character on Mac 9 and earlier. OSX and later versions use `\n`.

* `\t` ⇒ The TAB control character 0x09 (tab, or hard tab, horizontal tab).

* `\c☒` ⇒ The control character obtained from character ☒ by stripping all but its 6 lowest order bits. For instance, `\c1`, `\cA` and `\ca` all stand for the SOH control character 0x01.  You can think of this as "\c means ctrl", so `\cA` is the character you would get from hitting Ctrl+A in a terminal.

##### Special Control escapes

* `\R` ⇒ Any newline sequence.  Specifically, the atomic group `(?>\r\n|\n|\x0B|\f|\r|\x85|\x{2028}|\x{2029})`.  Please note, this sequence might match one or two characters, depending on the text.  Because its length is variable-width, it cannot be used in lookbehinds.  Because it expands to a parentheses-based group with an alternation sequence, it cannot be used inside a character class.  If you accidentally attempt to put it in a character class, it will be interpreted like any other literal-character escape (where `\☒` is used to make sure that the next character is literal) meaning that the `R` will be taken as a literal `R`, without any special meaning.  For example, if you try `[\t\R]`: you may be intendeng to say, "match any single character that's a tab or a newline", but what you are actually saying is "match the tab or a literal R"; to get what you probably intended, use `[\t\v]` for "a tab or any vertical spacing character", or `[\t\r\n]` for "a tab or carriage return or newline but not any of the weird verticals".

#### Ranges or kinds of characters

##### Character Classes

* `[`_set_`]`  ⇒ This indicates a _set_ of characters, for example, `[abc]` means any of the literal characters `a`, `b` or `c`. You can also use ranges by doing a hyphen between characters, for example `[a-z]` for any character from `a` to `z`.  You can use a collating sequence in character ranges, like in `[[.ch.]-[.ll.]]` (these are collating sequence in Spanish).

* `[^`_set_`]`  ⇒ The complement of the characters in the _set_. For example, `[^A-Za-z]` means any character except an alphabetic character.  Care should be taken with a complement list, as regular expressions are always multi-line, and hence `[^ABC]*` will match until the first `A`, `B` or `C` (or `a`, `b` or `c` if match case is off), including any newline characters. To confine the search to a single line, include the newline characters in the exception list, e.g. `[^ABC\r\n]`.

   Please note that the complement of a character set is often many more characters than you expect: `(?-s)[^x]+` will match 1 or more instances of any non-`x` character, including newlines: the `(?-s)` [search modifier](#search-modifier) turns off "dot matches newlines", but the `[^x]` is _not_ a dot `.`, so that class is still allowed to match newlines.

* `[[:`_name_`:]]` or `[[:☒:]]` ⇒ The whole character class named _name_.  For many, there is also a single-letter "short" class name, ☒.  Please note: the `[:`_name_`:]` and `[:☒:]` must be inside a character class `[...]` to have their special meaning.

    | short | full name      | description | equivalent character class |
    |:-----:|:--------------:|:------------|----------------------------|
    |       | alnum          | letters and digits | |
    |       | alpha          | letters | |
    | h     | blank          | spacing which is not a line terminator | `[\t\x20\xA0]`|
    |       | cntrl          | control characters | `[\x00-\x1F\x7F\x81\x8D\x8F\x90\x9D]` |
    | d     | digit          | digits | |
    |       | graph          | graphical character, so essentially any character except for control chars, `\0x7F`, `\x80` | |
    | l     | lower          | lowercase letters | |
    |       | print          | printable characters | `[\s[:graph:]]` |
    |       | punct          | punctuation characters | `[!"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]` <!-- ` -->|
    | s     | space          | whitespace (word or line separator) | `[\t\n\x0B\f\r\x20\x85\xA0\x{2028}\x{2029}]` |
    | u     | upper          | uppercase letters |  |
    |       | unicode        | any character with code point above 255 | `[\x{0100}-\x{FFFF}]` |
    | w     | word           | word characters | `[_\d\l\u]` |
    |       | xdigit         | hexadecimal digits | `[0-9A-Fa-f]` |

    Note that letters include any unicode letters (ASCII letters, accented letters, and letters from a variety of other writing systems); digits include ASCII numeric digits, and anything else in Unicode that's classified as a digit (like superscript numbers ¹²³...).

    Note that those character class names may be written in upper or lower case without changing the results.  So `[[:alnum:]]` is the same as `[[:ALNUM:]]` or the mixed-case `[[:AlNuM:]]`.

    As stated earlier, the `[:`_name_`:]` and `[:☒:]` (note the single brackets) must be a part of a surrounding character class.  However, you _may_ combine them inside one character class, such as `[_[:d:]x[:upper:]=]`, which is a character class that would match any digit, any uppercase, the lowercase `x`, and the literal `_` and `=` characters.  These named classes won't always appear with the double brackets, but they will always be inside of a character class.

    If the `[:`_name_`:]` or `[:☒:]` are accidentally _not_ contained inside a surrounding character class, they will lose their special meaning.  For example, `[:upper:]` is the character class matching `:`, `u`, `p`, `e`, and `r`; whereas `[[:upper:]]` is similar to `[A-Z]` (plus other unicode uppercase letters)

* `[^[:`_name_`:]]` or `[^[:☒:]]` ⇒ The complement of character class named _name_ or ☒ (matching anything _not_ in that named class).  This uses the same long names, short names, and rules as mentioned in the previous description.

* Character classes may _not_ contain parentheses-based groups of any kind, including the special escape `\R` (which expands to a parentheses-based group when evaluated, even though `\R` doesn't look like it contains parentheses).

##### Character Properties

These properties behave similar to named character classes, but cannot be contained inside a character class.

*  `\p☒` or `\p{`_name_`}` ⇒ Same as `[[:☒:]]` or `[[:`_name_`:]]`, where ☒ stands for one of the short names from the table above, and _name_ stands for one of the full names from above. For instance, `\pd` and `\p{digit}` both stand for a digit, just like the escape sequence `\d` does.

*  `\P☒` or `\P{`_name_`}` ⇒ Same as `[^[:☒:]]` or `[^[:`_name_`:]]` (not belonging to the class _name_).

##### Character escape sequences

`\☒` ⇒ Where ☒ is one of `d`, `l`, `s`, `u`, `w`, `h`, `v`, described below.  These single-letter escape sequences are each equivalent to a class from above.  The lower-case escape sequence means it matches that class; the upper-case escape sequence means it matches the negative of that class.  (Unlike the properties, these can be used both inside or outside of a character class.)

| Description]     | Escape Sequence | Positive Class | Negative Escape Sequence | Negative Class |
|:-----------------|:----------------|:---------------|:-------------------------|:---------------|
| digits           | `\d`            | `[[:digit:]]`  | `\D`                     | `[^[:digit:]]` |
| lowercase        | `\l`            | `[[:lower:]]`  | `\L`                     | `[^[:lower:]]` |
| space chars      | `\s`            | `[[:space:]]`  | `\S`                     | `[^[:space:]]` |
| uppercase        | `\u`            | `[[:upper:]]`  | `\U`                     | `[^[:upper:]]` |
| word chars       | `\w`            | `[[:word:]]`   | `\W`                     | `[^[:word:]]`  |
| horizontal space | `\h`            | `[[:blank:]]`  | `\H`                     | `[^[:blank:]]` |
| vertical space   | `\v`            | see below      | `\V`                     |                |

> Vertical space: This encompasses the LF, VT, FF, CR , NEL control characters and the LS and PS format characters : 0x000A (line feed), 0x000B (vertical tabulation), 0x000C (form feed), 0x000D (carriage return), 0x0085 (next line), 0x2028 (line separator) and 0x2029 (paragraph separator).  There isn't a named class which matches.

_Note_: despite its similarity to `\v`, even though `\R` matches certain veritcal space characters, it is _not_ a character-class-equivalent escape sequence (because it evaluates to a parentheses`()`-based expression, not a class-based expression).  So while `\d`, `\l`, `\s`, `\u`, `\w`, `\h`, and `\v` are all equivalent to a character class and can be included inside another bracket`[]`-based character class, the `\R` is _not_ equivalent to a character class, and _cannot_ be included inside a bracketed`[]` character-class.

##### Equivalence Classes

* `[[=`_char_`=]]` ⇒ All characters that differ from _char_ by case, accent or similar alteration only. For example `[[=a=]]` matches any of the characters: `a`, `À`, `Á`, `Â`, `Ã`, `Ä`, `Å`, `A`, `à`, `á`, `â`, `ã`, `ä` and `å`.


#### Multiplying operators

* `+`  ⇒ This matches 1 or more instances of the previous character, as many as it can. For example, `Sa+m` matches `Sam`, `Saam`, `Saaam`, and so on.  `[aeiou]+` matches consecutive strings of vowels.

* `*`  ⇒ This matches 0 or more instances of the previous character, as many as it can. For example, `Sa*m` matches `Sm`, `Sam`, `Saam`, and so on.

* `?` ⇒ Zero or one of the last character. Thus `Sa?m` matches `Sm` and `Sam`, but not `Saam`.

* `*?` ⇒ Zero or more of the previous group, but minimally: the shortest matching string, rather than the longest string as with the "greedy" operator. Thus, `m.*?o` applied to the text `margin-bottom: 0;` will match `margin-bo`, whereas `m.*o` will match `margin-botto`.

* `+?` ⇒ One or more of the previous group, but minimally.

* `{ℕ}` ⇒ Matches ℕ copies of the element it applies to (where ℕ is any decimal number).

* `{ℕ,}` ⇒ Matches ℕ or more copies of the element it applies to.

* `{ℕ,ℙ}` ⇒ Matches ℕ to ℙ copies of the element it applies to, as much it can (where ℙ ≥ ℕ).

* `{ℕ,}?` or `{ℕ,ℙ}?` ⇒ Like the above, but minimally.

* `*+` or `?+` or `++` or `{ℕ,}+` or `{ℕ,ℙ}+` ⇒ These so called "possessive" variants of greedy repeat marks do not backtrack. This allows failures to be reported much earlier, which can boost performance significantly. But they will eliminate matches that would require backtracking to be found. As an example:

    When regex `“.*”` is run against the text `“abc”x` :

        “  matches “
        .* matches abc”x
        ”  cannot match $ ( End of line ) => Backtracking

        “  matches “
        .* matches abc”
        ”  cannot match letter x => Backtracking

        “  matches “
        .* matches abc
        ”  matches ” => 1 overall match “abc”

    When regex `“.*+”`, with a possessive quantifier, is run against the text `“abc”x` :

        “   matches “
        .*+ matches abc”x ( catches all remaining characters )
        ” cannot match $ ( End of line )

    Notice there is no match at all for the possessive version, because the possessive repeat factor prevents from backtracking to a possible solution


#### Anchors
Anchors match a zero-length position in the line, rather than a particular character.


* `^` ⇒ This matches the start of a line (except when used inside a set, see above).

* `$`  ⇒ This matches the end of a line.

* `\<`  ⇒ This matches the start of a word using Scintilla's definitions of words.

* `\>`  ⇒ This matches the end of a word using Scintilla's definition of words.

* `\b` ⇒ Matches either the start or end of a word.

* `\B` ⇒ Not a word boundary. It represents any location between two word characters or between two non-word characters.

* `\A` or `` \` `` ⇒ Matches the start of the file.

* `\z` or `\'` ⇒ Matches the end of the file.

* `\Z` ⇒ Matches like `\z` with an optional sequence of newlines before it. This is equivalent to `(?=\v*\z)`, which departs from the traditional Perl meaning for this escape.

* `\G` ⇒ This "Continuation Escape" matches the end of the previous match.  In **Find All** or **Replace All** circumstances, this will allow you to anchor your next match at the end of the previous match.  If it is the first match of a **Find All** or **Replace All**, and any time you use a single **Find Next** or **Replace**, the "end of previous match" is defined to be the start of the search area -- the beginning of the document, or the current cursor position, or the start of the highlighted text.



#### Capture Groups and Backreferences

* `(`_subset_`)` ⇒ _Numbered Capture Group_: Parentheses mark a _subset_ of the regular expression, also known as a _subset_ expression or capture group. The string matched by the contents of the parentheses (indicated by _subset_ in this example) can be re-used with a backreference or as part of a replace operation; see [Substitutions](#substitutions), below. Groups may be nested.

* `(?<name>`_subset_`)` or `(?'name'`_subset_`)` or `(?(name)`_subset_`)` ⇒ _Named Capture Group_: Names the value matched by _subset_ as group _name_.  Please note that group names are case-sensitive.

* `\ℕ`, `\gℕ`, `\g{ℕ}`, `\g<ℕ>`, `\g'ℕ'`, `\kℕ`, `\k{ℕ}`, `\k<ℕ>` or `\k'ℕ'` ⇒ _Numbered Backreference:_ These syntaxes match the ℕth capture group earlier in the same expression.  (Backreferences are used to refer to the capture group contents only in the search/match expression; see the [Substitution Escape Sequences](#substitution-escape-sequences) for how to refer to capture groups in substitutions/replacements.)

    A regex can have multiple subgroups, so `\2`, `\3`, etc can be used to match others (numbers advance left to right with the opening parenthesis of the group).  You can have as many capture groups as you need, and are not limited to only 9 groups (though some of the syntax variants can only reference groups 1-9; see the notes below, and use the syntaxes that explicitly allow multi-digit ℕ if you have more than 9 groups)

    * Example: `([Cc][Aa][Ss][Ee]).*\1` would match a line such as `Case matches Case` but not `Case doesn't match cASE`.

    * `\gℕ`, `\g{ℕ}`, `\g<ℕ>`, `\g'ℕ'`, `\kℕ`, `\k{ℕ}`, `\k<ℕ>` or `\k'ℕ'` ⇒ These forms can handle any non-zero ℕ.

        * For positive ℕ, it matches the ℕth subgroup, even if ℕ has more than one digit.  `\g10` matches the contents from the 10th capture group, _not_ the contents from the first capture group followed by the literal `0`.

            * If you want to match a literal number after the contents of the ℕth capture group, use one of the forms that has braces, brackets, or quotes, like `\g{ℕ}` or `\k'ℕ'` or `\k<ℕ>`: For example, `\g{2}3` matches the contents of the second capture group, followed by a literal 3, whereas `\g23` would match the contents of the twenty-third capture group.

            * For clarity, it is highly recommended to always use the braces or brackets form for multi-digit ℕ


        * For negative ℕ, groups are counted backwards relative to the last group, so that `\g{-1}` is the last matched group, and `\g{-2}` is the next-to-last matched group.


            * Please, note the difference between absolute and relative backreferences. For instance, an exact four-letters word palindrome can be matched with :

                * the regex `(?-i)\b(\w)(\w)\g{2}\g{1}\b`, when using absolute (positive) coordinates

                * the regex `(?-i)\b(\w)(\w)\g{-1}\g{-2}\b`, when using relative (negative) coordinates

    * `\ℕ` ⇒ This form can only have ℕ as digits 1-9, so if you have more than 9 capture groups, you will have to use one of the other numbered backreference notations, listed in the next bullet point.

        Example: the expression `\10` matches the contents of the first capture group `\1` followed by the literal character `0`", _not_ the contents of the 10th group.

* `\g{name}`, `\g<name>`, `\g'name'`, `\k{name}`, `\k<name>` or `\k'name'` ⇒ _Named Backreference_: The string matching the subexpression named _name_.


#### Readability enhancements

* `(?:`_subset_`)` ⇒ A grouping construct for the _subset_ expression that doesn't count as a subexpression (doesn't get numbered or named), but just groups things for easier reading of the regex, or for using a quantified amount of that group, with a quantifier located right after that grouping construct.

* `(?#`_comment_`)` ⇒ Comments. The whole group is for humans only and will be ignored in matching text.

Using the x flag modifier (see section below) is also a good way to improve readability in complex regular expressions.


#### Search modifiers
The following constructs control how matches condition other matches, or otherwise alter the way search is performed.

* `\Q` ⇒ Starts verbatim mode (Perl calls it "quoted"). In this mode, all characters are treated as-is, the only exception being the `\E` end verbatim mode sequence.

* `\E` ⇒ Ends verbatim mode. Thus, `\Q\*+\Ea+` matches `\*+aaaa`.

* `(?enable-disable)` or `(?enable-disable:subpattern)` ⇒ There are four flags, described below, which can be applied to a regex or subgroup.  The _enable_ term can be made up of 0-4 of the flags described below; the _disable_ term can be made up of 0-4 of the flags described below. Any flags in _enable_ will be enabled (turned on); any flags in _disable_ will be disabled (turned off).  (Remember, it does not make sense to include the same flag in both the _enable_ and _disable_ terms.)  If there are no _disable_ flags, the `-` is not necessary; if there are no _enable_ flags, then the `-` will come immediately after the `?`: `(?-...)`.  If there is a subpattern, then the flags only apply for the contents of the subpattern; without a subpattern, there is no `:` separator, and the flags apply for the remainder of the current regex, or until the next flags are set.

    * `i` ⇒ case insensitive (default: set by **☐ Match case** dialog option)
    * `m` ⇒ ^ and $ match embedded newlines (default: on)
    * `s` ⇒ dot matches newline (default: as per **☐ . matches newline** dialog option)
    * `x` ⇒ Ignore non-escaped whitespace in regex (default: off).  Any whitespace that you need to match must be escaped

    Examples:

    * `blah(?i-s)foobar` ⇒ enables case insensitivity and disables dot-matches-newline for the rest of the regular expression: thus expression `blah` is run under the default rules (set by the dialog), whereas expression `foobar` will be case-insensitive and dot will not match newline.
    * `(?i-s:subpattern)` ⇒ enables case insensitivity and disables dot-matches-newline, but just for the `subpattern`
    * `(?-i)caseSensitive(?i)cAsE inSenSitive` ⇒ disables case insensitivity (makes it case-sensitive) for the portion of the regex indicated by `caseSensitive`, and re-enables case-insensitive matching for the rest of the regex
    * `(?m:justHere)` ⇒ `^` and `$` will match on embedded newlines, but just for the contents of this subgroup `justHere`
    * `(?x)` ⇒ Allow extra whitespace in the expression for the remainder of the regex

    Please note that turning off "dot matches newline" with `(?-s)` will _not_ affect character classes: `(?-s)[^x]+` will match 1 or more instances of any non-`x` character, including newlines, even though the `(?-s)` [search modifier](#search-modifier) turns off "dot matches newlines" (the `[^x]` is _not_ a dot `.`, so is still allowed to match newlines).

* `(?|expression)` ⇒ If an alternation expression has parenthetical subexpressions in some of its alternatives, you may want the subexpression counter not to be altered by what is in the other branches of the alternation. This construct will just do that.

    For example, you get the following subexpression counter values:

~~~
#      before  ---------------branch-reset----------- after
/ (?x) ( a )  (?| x ( y ) z | (p (q) r) | (t) u (v) ) ( z )
#      1            2         2  3        2     3     4
~~~


    Without the branch reset, `(y)` would be group 3, and `(p(q)r)` would be group 4, and `(t)` would be group 5. With the branch reset, they both report as group 2.

### Control flow
Normally, a regular expression parses from left to right linearly. But you may need to change this behavior.


* `|` ⇒ The alternation operator, which allows matching either of a number of options.  For example, `one|two|three` will match either of `one`, `two` or `three`. Matches are attempted from left to right. Use `(?:)` to match an empty string in such a construct.

*  `(?ℕ)` ⇒ Refers to ℕth subexpression. If ℕ is negative, it will use the ℕth subexpression from the end.

    Please, note the difference between subexpressions and back-references. For instance, using a similar structure to the one, when searching for a four-letters word being a palindrome, this time, both regexes just find a four-letters word, because each subexpression, signed or not, refers to the regex itself, enclosed in each group and NOT to the present value of each group!

    * the regex `(?-i)\b(\w)(\w)(?2)(?1)\b` find a four-letter word, when using absolute coordinates

    * the regex `(?-i)\b(\w)(\w)(?-1)(?-2)\b` find a four-letter word, when using relative coordinates

    Actually, these two regexes could be simplified to `(?-i)\b(\w)(\w)\w\w\b`, assuming that group 1 and 2 are still needed in replacement

*  `(?0)` or `(?R)` ⇒ Backtrack to start of pattern.

*  `(?&name)` or `(?P>name)` ⇒ Backtrack to subexpression named _name_.

    * If a non-signed subexpression is located OUTSIDE the parentheses of the group to which it refers, it is called a subroutine call

    * If a non-signed subexpression is located INSIDE the parentheses of the group to which it refers, it is called a recursive call

*  `(?(assertion)YesPattern|NoPattern)` ⇒ Conditional Expressions

    If the _assertion_ is true, then _YesPattern_ will be used for matching the text; if the _assertion_ is false, then _NoPattern_ will be used for matching the text.

    _YesPattern_ and _NoPattern_ are any valid regex patterns.

    The _assertion_ will always be inside parentheses; this is emphasized by including the parentheses in the list of supported _assertion_ syntax, below:

    * `(ℕ)` ⇒ true if ℕth unnamed group was previously defined

    * `(<name>)` or `('name')` ⇒ true if group called _name_ was previously defined

    *  `(?=lookahead)` ⇒ true if the _lookahead_ expression matches

    *  `(?!lookahead)` ⇒ true if the _lookahead_ expression does not match

    *  `(?<=lookbehind)` ⇒ true if the _lookbehind_ expression matches

    *  `(?<!lookbehind)` ⇒ true if the _lookbehind_ expression does not match

    *  `(R)` ⇒ true if inside a recursion

    *  `(Rℕ)` ⇒ true if in a recursion to subexpression numbered ℕ

    *  `(R&name)` ⇒ true if in a recursion to named subexpression _name_

    Note: These are all still _inside_ the conditional expression.

    Do not confuse the assertions that control a conditional expression (here) with the assertions that are part of the pattern matching (the [Assertions](#assertions) section, below).  Here, if the assertion is used to decide which expression is used; below, the assertion decides whether the pattern is matching or not.

    Note: PCRE doesn't treat recursion expressions like Perl does:

    > In PCRE (like Python, but unlike Perl), a recursive subpattern call  is
always treated as an atomic group. That is, once it has matched some of
the subject string, it is never re-entered, even if it contains untried
alternatives  and  there  is a subsequent matching failure.

*  `(?>pattern)` ⇒ Independent sub-expression

    Match _pattern_ independently of surrounding patterns. Search will never backtrack into independent sub-expression.

    Independent sub-expressions are typically used to improve performance, because only the best possible match for pattern will be considered; if this doesn't allow the expression as a whole to match then no match is found at all.

    It can also be used to keep the logic for Conditional Expressions (above) correct, preventing an unexpected path to the wrong alternate being used.  For example, when using a group-number as the conditional assertion, `(?(ℕ)YesPattern|NoPattern)`:

    * The regex `(?:(100)|\d{3}) apples (?(1)YesPattern|NoPattern)` does not use the independent sub-expression, so it will find `100 apples NoPattern`, even though you expected `YesPattern` to be used when `100` was matched.  Why? If `YesPattern` failed, the search will backtrack to the beginning and try next alternative, where `100` matches `\d{3}`, but that means that `?(1)` does _not_ match so the conditional expression uses `NoPattern`.

    * Instead, you can use the independent sub-expression to prevent backtracking, by using the regex `(?>(100)|\d{3}) apples (?(1)YesPattern|NoPattern)`.  Now, if `YesPattern` fails, it cannot backtrack to use the `\d{3}`, thus preventing it from accidentally using `100 apples NoPattern`, so with `100` it will either match `100 apples YesPattern` or the whole expression will fail.

*  `\K` ⇒ Resets matched text at this point. For instance, matching `foo\Kbar` will not match `bar`. It will match `foobar`, but will pretend that only `bar` matches. Useful when you wish to replace only the tail of a matched subject and groups are clumsy to formulate.

    It is also useful if you would need a look-behind assertion which would contain a non-fixed length pattern (see further on). As variable-length lookbehind is not allowed in Boost's regular expressions, you can use the `\K` syntax, instead. For instance, the non-allowed syntax `(?-i)(?<=\d+)abc` can be replaced with the correct syntax `(?-i)\d+\Kabc` which matches the exact string `abc` only if preceded by, at least, one digit.

#### Assertions
These special groups consume no characters. Their successful matching counts, but when they are done, matching starts over where it left.

* `(?=pattern)` ⇒ positive lookahead: If _pattern_ matches, backtrack to start of _pattern_. This allows using logical AND for combining regexes.

    * The expression `(?=.*[[:lower:]])(?=.*[[:upper:]]).{6,}` tries finding a lowercase letter anywhere. On success it backtracks and searches for an uppercase letter. On yet another success, it checks whether the subject has at least 6 characters.

    * `q(?=u)i` doesn't match `quit`, because the assertion `(?=u)` matches the `u` but does not consume the `u`, as matching `u` consumes zero characters, so then trying to match `i` in the pattern fails, because it is still comparing against the `u` in the text being searched.

* `(?!pattern)` ⇒ negative lookahead: Matches if lookahead _pattern_ didn't match.

* `(?<=pattern)` ⇒ positive lookbehind: This assertion matches if _pattern_ matches before the current token.

* `(?<!pattern)` ⇒ negative lookbehind: This assertion matches if _pattern_ does not match before the current token.

    * NOTE: In the lookbehind assertions, _pattern_ has to be of fixed length, so that the regex engine knows where to test the assertion.  Use `\K` (above) for the equivalent of variable-length lookbehind.

### Substitutions

Substitution expressions (the contents of the **Replace with** entry) use similar syntax to the search expression, with the additional features described below.

All characters are treated as literals except for `$`, `\`, `(`, `)`, `?`, and `:`.

#### Substitution Escape Sequences

In substitutions, in addition to allowing the [Control Characters](#control-characters), [Non ASCII characters](#non-ascii-characters), and [Character escape sequences](#character-escape-sequences) from search expressions, the following additional escape sequences are recognized:

*  `\l` ⇒ Causes next character to output in lowercase

*  `\L` ⇒ Causes next characters to be output in lowercase, until a `\E` is found.

*  `\u` ⇒ Causes next character to output in uppercase

*  `\U` ⇒ Causes next characters to be output in uppercase, until a `\E` is found.

*  `\E` ⇒ Puts an end to forced case mode initiated by `\L` or `\U`.

*  `$&`, `$MATCH`, `${^MATCH}`, `$0`, `${0}` ⇒ The whole matched text.

*  `` $` `` <!-- `: dont remove this comment; it fixes UDL highlighting of this paragraph -->, `$PREMATCH`, `${^PREMATCH}` ⇒ The text between the previous and current match, or the text before the match if this is the first one.

*  `$'`, `$POSTMATCH`, `${^POSTMATCH}` ⇒ Everything that follows current match.

*  `$^N`, `$LAST_SUBMATCH_RESULT`, `${^LAST_SUBMATCH_RESULT}` ⇒ Returns what the last matching subexpression matched.

*  `$+`, `$LAST_PAREN_MATCH`, `${^LAST_PAREN_MATCH}` ⇒ Returns what matched the last subexpression in the pattern, if that subexpression is currently matched by the regex engine.

*  `$$` or `\$` ⇒ Returns literal `$` character.

*  `$ℕ`, `${ℕ}`, `\ℕ` ⇒ Returns what matched the ℕth subexpression (numbered capture group), where ℕ is a positive integer (1 or larger).  If ℕ is greater than 9, use `${ℕ}`.

    * Please note: the `\g...` and `\k...`  [backreference](#capture-groups-and-backreferences) syntaxes only work in the search expression, and are _not_ designed or intended to work in the substitution/replacement expression.

*  `$+{name}` ⇒ Returns what matched subexpression named _name_ (named capture group).

If not described in this section, `\` followed by any character will output that literal character.

#### Substitution Grouping

The parentheses `(` and `)` are used for creating lexical groups, and are not part of the output text.  To output literal parentheses, use `\(` and `\)`.

#### Substitution Conditionals

If you want to make decisions during the replacement (conditional replacement), use one of these variants of the conditional syntax below.

* `?ℕYesPattern:NoPattern`: where `ℕ` is a decimal number (one or more decimal digits), and `YesPattern` and `NoPattern` are replacement expressions.  If the ℕth numbered group from the search expression was matched, the `YesPattern` will be used as the output; if not, the `NoPattern` will be used instead.  `YesPattern` cannot start with any digits (0-9) in this version of the syntax, because the digits will be interpreted as part of `ℕ` instead of part of `YesPattern`; if `YesPattern` needs to start with one or more digits, use the `?{ℕ}` variant of the syntax, below.
    * For example: `?1george\($1\):gracie` ⇒ if the first group from the search was matched, then use the literal text `george`, followed by the contents of the first match inside literal parentheses; if the first group does not match, use the literal text `gracie`.
* `?{ℕ}YesPattern:NoPattern`: where `ℕ` here can be one or more decimal digit, `YesPattern` and `NoPattern` are replacement expressions, as above.  This syntax variant will work even if `YesPattern` needs to start with one or more digits, because the braces around `ℕ` separate it from `YesPattern`.
    * For example: `?{13}1george\(${13}\):2gracie` ⇒ if the thirteenth group from the search was matched, then use the literal text `1george`, followed by the contents of the thirteenth match inside literal parentheses; if the thirteenth group does not match, use the literal text `2gracie`.
* `?{name}YesPattern:NoPattern`: where _name_ is the name of a named-match-group, and `YesPattern` and `NoPattern` are replacement expressions, as above.
    * For example: `?{comedian}george\($+{comedian}\):gracie` ⇒ if the group named _comedian_ from the search was matched, then use the literal text `george`, followed by the contents of the named group inside literal parentheses; if the named group does not match, use the literal text `gracie`.

By placing the expression inside parentheses, you can separate the conditional from the surrounding replacement: `a=?1george:gracie=b` would output `a=george` or `a=gracie=b`, whereas `a=(?1george:gracie)=b` shows when the conditional ends, so would be `a=george=b` or `a=gracie=b`.

Remember, to include literal parentheses, question marks, or colons in conditional substitution expressions, make sure to escape them as `\(` or `\)` or `\?` or `\:`.

### Zero length matches

In normal or extended mode, there would be no point in looking for text of length 0; however, in regular expression mode, this can often happen. For example, to add something at the beginning of a line, you'll search for "^" and replace with whatever is to be added.

Notepad++ would select the match, but there is no sensible way to select a stretch zero character long. When this happens, a tooltip very similar to function call tips is displayed instead, with a caret pointing upwards to the empty match.


### Examples

These examples are meant to help better show what the complex regex syntax will accomplish.  Many of these examples, written by Georg Dembowski, have been in previous versions of the documentation for years; they have been updated to match with the modern Notepad++ v7.7 regular expression syntax.

**IMPORTANT**

*  You have to check the box "regular expression" in search &amp; replace dialog

*  When copying the strings out of here, pay close attention not to have additional spaces before or after them! Otherwise, the tested regex will not match anything!

#### Example 0
How to replace/delete full lines according to a regex pattern?
Let's say you wish to delete all the lines in a file that contain the word "unused", without leaving blank lines in their stead. This means you need to locate the line, remove it all, and additionally remove its terminating newline.

So, you'd want to do this:

* Find: `^.*?unused.*?$\R`
* Replace with: nothing, not even a space

The regular expression **appears** to always work  is to be read like this:

*  assert the start of a line

*  match some characters, stopping as early as required for the expression to match

*  the string you search in the file, "unused"

*  more characters, again stopping at the earliest necessary for the expression to match

*  assert line ends

*  A newline character or sequence


Remember that `.*` gobbles everything to the end of line if **☐ . matches newline** is off, and everything to the end of file if the option is on!

Well, why is **appears** above in bold letters? Because this expression assumes each line ends with an end of line sequence. This is almost always true, and may fail for the last line in the file. It won't match and won't be deleted.

But the remedy is fairly simple: we translate in regex parlance that the newline should match if it is there. So the correct expression actually is:

* Find: `^.*?unused.*?$\R?`

This is because `?` makes it match 0 or 1 `\R`.

#### Example 1
You use a MediaWiki (like Wikipedia) and want to make all headings one level higher, so a H2 becomes a H1 etc.

*  Search `^=(=)`

*  Replace with `\1`

*  Click **Replace all**

You do this to find all headings2...9 (two equal sign characters are required) which begin at line beginning (^) and to replace the two equal sign characters by only the last of the two, so eliminating one and having one remaining.


*  Search `=(=)$`

*  Replace with `\1`

*  Click **Replace all**

You do this to find all headings2...9 (two equal sign characters are required) which end at line ending ($) and to replace the two equal sign characters by only the last of the two, so eliminating one and having one remaining.

`== title ==` became `= title =`

You're done :-)


#### Example 2
You have a document with a lot of dates, which are in date format `dd.mm.yy` and you'd like to transform them to sortable format `yy-mm-dd`. Don't be afraid by the length of the search term – it's long, but consisting of pretty easy and short parts.

Do the following:


*  Search `([^0-9.])([0123][0-9])\.([01][0-9])\.([0-9][0-9])([^0-9.])` or

   Search `(\s)([0123][0-9])\.([01][0-9])\.([0-9][0-9])(\s)`

*  Replace with `\1\4-\3-\2\5`

*  Click **Replace all**


You do this to fetch:

*  the day, whose first number can only be 0, 1, 2 or 3

*  the month, whose first number can only be 0 or 1

*  but only if the separator is a literal dot and not any standard character ( `\.` versus `.` )

*  but only if no numbers are surrounding the date, as then it might be an IP address instead of a date


and to write all of this in the opposite order, except for the surroundings. Pay attention: Whatever SEARCH matches will be deleted and only replaced by the stuff in the REPLACE field, thus it is mandatory to have the surroundings in the REPLACE field as well!

Outcome:

*  `31.12.97` became `97-12-31`

*  `14.08.05` became `05-08-14`

*  the IP address `14.13.14.14` did not change


You're done :-)


#### Example 3
You have printed in windows a file list using `dir /a-d /b/s /-p > filelist.txt` to the file filelist.txt and want to make local URLs out of them.

*  Open `filelist.txt` with Notepad++

*  Search `\\`

*  Replace with `/`

*  Click **Replace all**.

    This changes the Windows path separator char `\` into the URL path separator char `/`


* Search `\x20`

* Replace `%20`

* Click **Replace all** to change any space character into the `%20` syntax

    According on your requirements, you can similarly change any possible symbol `! # $ % & ' ( ) + , - ; = @ [ ] ^ { } ~` with the appropriate `%ℕℕ` expression

*  Search `^(?=.)`

*  Replace with `file:///`

*  Click **Replace all**

    This adds file:/// to the beginning of all non-empty lines

After this sequence, `C:\!\Test A.csv` became `file:///C:/!/Test%20A.csv`.

You're done :-)


#### Example 4

Let’s suppose you need a comma delimited table from the table, below :

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

Then use the following regex S/R :

*  Search for: `(?-i)[\u\d]\K\x20(?=[\u\d])`

*  Replace with: `,`

*  Hit **Replace All**


~~~
[Final Data]
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

You’re done :-)


#### Example 5
How to recognize a balanced expression, in mathematics or in programming?

First, let's give some example data:

~~~
[Sample Test Start]

((((ab(((cd((()))))ef))))))
0000  000  00100000  00000•
1234  567  89098765  43210


((ab((((cd(((ef(()))))gh))))ijkl))))
00  0000  000  1110000  0000    00••
12  3456  789  0109876  5432    10


((((((ab(cd(ef((()))))gh)ijkl)))mn)))))
000000  0  0  01110000  0    000  00•••
123456  7  8  90109876  5    432  10


((01ab(cd(ef23gh(ij45kl)mn)op((qr67st)uv\wx)34)yz))128956)abc
12    3  4      5      4  3  45      4     3  2  10      •

[[@ab[cd{ef@gh{ij@kl}mn]op((qr@st}uv@x]34yz])12@56)[cdedf]
                          12                1     0

((12ab(cd{ef34gh{ij56kl}mn}123}op((qr78stu)v\wx34)yz)12905126]
12    3                          45       4      3  2
••

[[@ab[cd{ef@gh{ij@kl}mn}123]op((qr@stu)v@x34)yz]12@5@6]
                              12      1     0
[Sample Test End]
~~~

For instance, let’s try to build a regular expression that finds the largest range of text with well-balanced parentheses!

First, some typographic conventions:

* Let Sp be a starting parenthesis. So, its regex syntax is the escaped form `\(`, or simply `(` if inside a character class

* Let Ep be an ending parenthesis. So, its regex syntax is the escaped form `\)`, or simply `)` if inside a character class

* Let Ac be any single allowed character, including EOF character(s), different from EP and SP. So, its regex syntax is the negative class character `[^EpSp]`, i.e., the negative class character `[^()]`

* Let R0 be a recursion to the whole matched pattern. By convention, in PCRE, its regex syntax is `(?0)` or `(?R)`

* Let R1 be a recursion to the group 1 pattern. By convention, in PCRE, its regex syntax is `(?1)`

* Now , let Bb be a well-balanced block, containing an Ep....Sp construction, itself possibly composed with, both, Ac characters and an other Bb, at any level greater than level 0

    This Bb block can be represented by the symbolic regex, below ( Blank chars are ignored, for readability ) :

        Sp ( Ac+ | R0 )* Ep

    This syntax may be improved as `Bb = Sp (?: Ac++ | R0 )* Ep`, using, both :

* A non-capturing group, surrounding the two alternatives

* A possessive quantifier relative to the Ac character, to be similar to the atomic state of recursions, in PCRE.

    It is important to point out that, if you would use the greedy form `Ac+`, instead of `Ac++`, the last match would be, wrongly, all the file contents, even against a very short text! Again, the advantage of not allowing backtracking reduces combinations and avoids the catastrophic backtracking process :-)

Now, more precisely, between the Sp and Ep parentheses, you may meet:

* Nothing, hence the star quantifier, after the non-capturing group

* A non-null range of allowed chars, so the atomic group Ac++

* Another well-balanced Bb construction which can be verified, in turn, by the recursion feature R0

On the other hand, any subject text scanned can be defined, either, as:

* A combination of successive syntaxes  Ac*  Bb  Ac*  Bb  Ac*  Bb, ended with a last Ac*. So, in the symbolic regex syntax, this can be written as (?: Ac* Bb)+ Ac*

* A non-null range of allowed chars, when the subject text does NOT contain any Ep and Sp parenthesis, so the Ac+ symbolic syntax, only ( By extension, a text without parentheses is, obviously, a well-balanced parentheses text... as it contains no parenthesis ! )

This implies that the general symbolic regex is `(?: Ac* Bb )+ Ac* | Ac+`

Now, by substituting the above value of the well-balanced Bb construction, in our final expression, we get our final symbolic regex expression :

    (?: Ac* ( Sp (?: Ac++ | R1 )* Ep ) )+ Ac* | Ac+
            \ ---------------------- /
                     Group 1

Note, however, that we just had to add two parentheses to define a new group #1 , which embeds the Bb construction,. Indeed, during the recursion process, it must refer, specifically, to that group #1 and NOT recurse to the whole regex pattern. Hence, the R1 notation, instead of the R0 notation!

Finally, we can get something more legible if we use the free-spacing mode to identify the components of our regex and rewrite this expression with the correct regex syntax:

    (?x) (?: [^()]*  (  \(  (?:  [^()]++  |  (?1)  )*  \)  )  )+  [^()]*  |  [^()]+

Note that, with the free-spacing mode, you may, as well, insert comments and split the regex on several lines, leading, for instance, to the following text:

    (?x)                  #  FREE-SPACING mode
    (?:                   #  Start of the FIRST NON-CAPTURING group
        [^()]*            #      Any range, possibly NUL, of ALLOWED characters
        (                 #      Start of CAPTURING group #1
            \(            #          STARTING parenthesis
            (?:           #          Start of the SECOND NON-CAPTURING group
                [^()]++   #              Any NON-NULL ATOMIC range of ALLOWED characters,
                |         #              OR
                (?1)      #              A RECURSION, using the regex pattern of group #1
            )*            #          End of the SECOND NON-CAPTURING group, repeated 0 or MORE times
            \)            #          ENDING parenthesis
        )                 #      End of the CAPTURING group 1
    )+                    #  End of the FIRST NON-CAPTURING group, repeated 1 or MORE times
    [^()]*                #  Any range, possibly NUL, of ALLOWED characters
    |                     #  OR
    [^()]+                #  Any NON-NULL range of ALLOWED characters,

If we reduce the syntax of this recursive regular expression to its minimum, we get :

    (?:[^()]*(\((?:[^()]++|(?1))*\)))+[^()]*|[^()]+

But it is about as hard to decrypt as a badly indented piece of code without a comment and with unpromising, unclear identifiers.

#### Example 6

This example gives more insight into using independent sub-expressions to prevent back-tracking when using Conditional Expressions.

Given the file:
```
  5 apples in a box
100 apples in a box
200 apples in a barrel
250 apples in a box
500 apples in a barrel
```

We want to match when there are 250 or fewer apples only when they are in a box; if there are more apples than 250, it should only match in a barrel.  Thus, `200 apples in a barrel` should _not_ match.

First we need to construct Conditional Expression for apples container:

    (?('LEQ250')in a box|in a barrel)

The `('LEQ250')` refers to some Capture Group which will catch quantity of apples comparing with our condition:

    (?:(?'LEQ250'\d{1,2}|1\d\d|2[0-4]\d|250)|\d+)\D

The trick here is that if we have alternatives in this Capture Group, we can't allow search to back-track to try a different alternative from the condition when the conditional fails.  Thus, we need to use an Independent sub-expression:

    (?>(?:(?'LEQ250'\d{1,2}|1\d\d|2[0-4]\d|250)|\d+)\D)

But if we use Independent sub-expression we have other two problems:

1. we have possibility for spaces appear before digits `\h*`
2. we need to check where number ends `\D`

Alternatives and Multiplying Operators need backtracking and so must be resolved inside the Independent sub-expression.  In our example `\h*\d` is definitive - `\h*` always stops before non-space (and a digit `\d` is not a space), but if you need to include some alternatives or multiplying operators inside your capture group, then include all of them, to give the Independent sub-expression the possibility to backtrack within itself.

It is better to check for the end in a more general form, in order to not include patterns not needed for Capture Group inside Independent sub-expression; thus, we will use the positive lookahead (?=\D) Assertion.

As a result we have the following regexp:

    ^\h*(?>(?:(?'LEQ250'\d{1,2}|1\d\d|2[0-4]\d|250)|\d+)(?=\D)) apples (?('LEQ250')in a box|in a barrel)

With this expression, our search results are

```
File1 (4 hits)
Line 1: 5 apples in a box
Line 2: 100 apples in a box
Line 4: 250 apples in a box
Line 5: 500 apples in a barrel
```

If we didn't use the Independent sub-expression, and instead used the regex

    ^\h*(?:(?:(?'LEQ250'\d{1,2}|1\d\d|2[0-4]\d|250)|\d+)(?=\D)) apples (?('LEQ250')in a box|in a barrel)

Our search results would incorrectly match line 3 (`200 apples in a barrel`):

```
File1 (5 hits)
Line 1: 5 apples in a box
Line 2: 100 apples in a box
Line 3: 200 apples in a barrel
Line 4: 250 apples in a box
Line 5: 500 apples in a barrel
```

## Searching actions when recorded as macros

The Find family of actions can be recorded in a macro to make them easy to name and later replay via the **Macro** menu or an assigned keyboard shortcut.  Somewhat unfortunately, **Find what** and **Replace with** text is hardwired into the macro when it is created, and isn't something the user can change when the macro runs, but often this isn't a significant limitation.

Note, however, that Find-related actions are recorded a bit differently than other Notepad++ actions, so we'll discuss them a bit more in-depth here.  Typically, Notepad++ will record a step in a macro every time a user does something in the Notepad++ user interface.  The Find family of actions is more "coordinated" where macro recording is concerned.

The macro recorder only records when an actual Find family action (e.g. **Replace**, **Find All in Current Document**, etc.) occurs.  Thus you can tweak a future action's parameters (e.g. **Match case**, **Wrap around**, etc.) all you'd like, and all of that fiddling doesn't get remembered.  At the point where you perform an action, then a snapshot is taken of all of the parameters and the action, and this is logged in the macro memory as a proper macro sequence.

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

| 1702-Bit-Weight |Binary-Bit-Weight  | Meaning (equivalent option ticked) |
|----------------:|------------------:|:-----------------------------------|
| 1               | 0000000001        | Match whole word only              |
| 2               | 0000000010        | Match case                         |
| 4               | 0000000100        | Purge for each search              |
| 16              | 0000010000        | Bookmark line                      |
| 32              | 0000100000        | In all sub-folders                 |
| 64              | 0001000000        | In hidden folders                  |
| 128             | 0010000000        | In selection                       |
| 256             | 0100000000        | Wrap around                        |
| 512             | 1000000000        | Backward direction (*)             |

*: **Backward direction** ticked means 512 is _not_ included; unticked means 512 _is_ included.

> Let's see how the example value 515 used above is decoded:

> lParam="515" (decimal) = 203 (hex) = 10 0000 0011 (binary) = 512 + 2 + 1 = (***not*** Backward direction + Match case + Match whole word only).  Thus, this would represent a forward-from-caret-towards-end-of-file search of exact case specified, with the additional qualifier that the match text must be bracketed by non-word characters.


Finally appears a **1701** message which encodes the Find family action to perform in **lParam**, which, when executed will conduct the action using all of the information encoded in the prior messages; let's do a **Replace in Files**, which has an integer value of 1660, for purposes of an example:

`<Action type="3" message="1701" wParam="0" lParam="1660" sParam="" />`

| 1701-Value | Meaning (equivalent button press)   |
|-----------:|-------------------------------------|
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


Here is a complete example (that could occur in *shortcuts.xml*) and how it is interpreted:

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

Finally, let's consider the 1702 message.  Its pertinent part is lParam="786".  The best way to break that down into its component parts is to convert the number to binary and then determine how the one-bits in the binary contribute to the meaning.  786 in binary is 1100010010 (= 512 + 256 + 16 + 2), which breaks down as follows, and then reading the 1702 table from earlier we get the contributors to functionality:

* `1000000000` = 512 - Backward direction _disabled_ (thus forward direction from caret toward bottom end of file)

* `0100000000` = 256 - Wrap around

* `0000010000` = 16 - Bookmark line

* `0000000010` = 2 - Match case

Note that in this example we seem to have conflicting search parameters:  We have a direction encoded, as well as a Wrap around, which nullifies the need for a direction.  This is not a problem, as the Wrap around option will take precedence, just like in a non-macro'd interactive searching operation.
