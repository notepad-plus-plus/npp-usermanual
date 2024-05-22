---
title: Ghost Typing
weight: 200
---

Ghost typing can be used to launch Notepad++ with an auto-typing text. Use command line arguments **-qn**, **-qt** or **-qf** to trigger it.

## Syntax

### Main Ghost Typing Modes

Use one of these three [command-line options](../command-prompt/) to enable the various modes of ghost typing.

`notepad++.exe -qn="EasterEggName"`

**-qn**: ghost typing text is derived from a builtin easter egg text.

***EasterEggName***: the name of easter egg.  Quotes are required if the name contains a space.

Use `-qn=random` to randomly select an easter egg quote. Other than that, we encourage examining
the source code to discover more easter egg quotes.


`notepad++.exe -qt="Text" [-qSpeedX] [-lLang]`

**-qt**: ghost typing text is derived from the string passed to this option.

***Text***: given text. Quotes are required if there are spaces in the text.


`notepad++.exe -qf="ContentFilePath" [-qSpeedX] [-lLang]`

**-qf**: quote by file.

***ContentFilePath***: The path of file, absolute or relative. If there are spaces in the directory or filename, use quotes around the whole path.  The content (in ASCII or Unicode) of the file will be shown.

### Ghost Typing Options

These options apply to any of the ghost typing modes, unless otherwise mentioned.

**-qSpeed*****X*** : optional; ignored when using -qn. Use this flag if you want to control your display speed. ***X*** could be 1 (slow), 2 (fast) or 3 (fastest).

**-l*****Lang*** : optional; ignored when using -qn. It will make ghost typing apply the syntax highlighting of the specified ***Lang***.

## Samples

`notepad++.exe -qn=random`

`notepad++.exe -qn="Bill Gates"`

`notepad++.exe -qt="Test of ghost typing example." -qSpeed1`

`notepad++.exe -qf="myFile.txt"`

`notepad++.exe -qf="myVeryLongFile.txt" -qSpeed3`

`notepad++.exe -qf="C:\my folder\my poetries.txt"`

`notepad++.exe -qt="#hulk { height: 200%; width: 200%; color: green; }" -lcss`

## Historical Syntax

The syntax listed above is valid for Notepad++ v8 and newer.  If you have a v7.x version of Notepad++, please download the [last offline User Manual that contains Notepad++ v7.x details](https://github.com/notepad-plus-plus/npp-usermanual/releases/download/3.6/nppUserManual.zip)

## More on the Easter Eggs

As indicated above, the idea is that you go hunting for the Easter Eggs in the [source code](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/).  However, that's a lot to search through, so you can reveal the spoilers below to narrow down the search space.

{{< details "Warning: Spoilers" >}}
[This file](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/Notepad_plus.cpp) might help you narrow down the search space.  And if you [search the Community Forum](https://community.notepad-plus-plus.org/search?matchWords=all&in=titlesposts&showAs=posts&replies=&repliesFilter=atleast&timeFilter=newer&timeRange=&sortBy=timestamp&sortDirection=desc&term=Easter%20Eggs), you might be able to find a [list](https://community.notepad-plus-plus.org/topic/25803/an-updated-list-of-notepad-easter-eggs/ "Like Here") of Easter Eggs, but any such static list will eventually fall out-of-date.
{{< /details >}}

Aside from the command-line options above, you can also type the name of the Easter Egg in Notepad++, then select that name, then activate the **About Notepad++** dialog using the **?** menu or the default <kbd>F1</kbd> keyboard shortcut -- with the name selected, instead of actually opening the dialog, Notepad++ will create a new docuemnt tab, and will do the Ghost Typing for the selected Easter Egg name (or a random choice).  This **About Notepad++**-based interface to the Easter Eggs can be turned off using the [`noEasterEggs.xml` zero-byte config file](../config-files/#other-configuration-files).
