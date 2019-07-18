---
title: Other Resources
weight: 160
---


## Notepad Replacement
Notepad is a default text editor shipped with Windows. You may want to use Notepad++ instead of Notepad. However, there's no obvious way to do it.
From the version 7.5.9 you can run the following command to make Notepad++ replace Notepad (run in cmd.exe with Administrator privileges):

```batch
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v "Debugger" /t REG_SZ /d "\"%ProgramFiles(x86)%\Notepad++\notepad++.exe\" -notepadStyleCmdline -z" /f
```

Note that you may need to use "%ProgramFiles%\Notepad++\" to substitute for "%ProgramFiles(x86)%\Notepad++\" if you have Notepad++ 64-bit installed, or use other path if your Notepad++ is installed in a non-default location.


Use the the following comment to undo the replacement:
```batch
reg delete "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v "Debugger" /f
```
## Notepad++ Cheat sheet
