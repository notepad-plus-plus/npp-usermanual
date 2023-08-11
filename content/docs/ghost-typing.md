---
title: Ghost Typing
weight: 200
---

Ghost typing can be used to launch Notepad++ with an auto-typing text. Use command line arguments **-qn**, **-qt** or **-qf** to trigger it.

## Syntax

### Main Ghost Typing Modes

Use one of these three command-line options to enable the various modes of ghost typing.

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
