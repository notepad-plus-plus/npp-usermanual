---
title: Ghost Typing
weight: 145
---

Ghost typing can be used to launch Notepad++ with an auto-typing text. Use command line arguments **-qn**, **-qt** or **-qf** to trigger it.

## Syntax

`notepad++.exe -qnEasterEggName`

**-qn**: quote by name.

***EasterEggName***: the name of easter egg. Use %20 to replace space character.


`notepad++.exe -qtText [-qSpeedX] [-lLang]`

**-qt**: quote by text.

***Text***: given text. Use %20 to replace space character.


`notepad++.exe -qfContentFilePath [-qSpeedX] [-lLang]`

**-qf**: quote by file.

***ContentFilePath***: The path of file, absolute or relative. Use %20 to replace space character in ContentFilePath. The content (in ASCII or Unicode) of the file will be shown.

**-qSpeed*****X*** : optional, won't be applied on -qn. Use this flag if you want to control your display speed. X could be 1 (slow), 2 (fast) or 3 (fastest).

**-l*****Lang*** : optional, won't be applied on -qn. It will make ghost typing apply the syntax highlighting of Lang of your choice.

## Samples

`notepad++.exe -qnrandom`

`notepad++.exe -qnBill%20Gates`

`notepad++.exe -qtTest%20of%20ghost%20typing%20example. -qSpeed1`

`notepad++.exe -qfmyFile.txt`

`notepad++.exe -qfmyVeryLongFile.txt -qSpeed3`

`notepad++.exe -qfC:\my%20folder\my%20poetries.txt`

`notepad++.exe -qt#hulk%20{%20height:%20200%;%20width:%20200%;%20color:%20green;%20} -lcss`
