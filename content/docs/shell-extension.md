---
title: Shell Extension
weight: 130
---

Historically, Notepad++ has come with a Shell extension. This is not really part of the Notepad++ program but very useful. If you choose to install it (and the Notepad++ installer does install it), then any file you rightclick on will show an entry named “Edit with Notepad++” with the Notepad++ icon.

Please note that to install or remove the extension, it sometimes is required to restart the Explorer process. For this you can reboot, logout and log back in or use the task manager to kill explorer (Windows NT and up) and restart it again. You can do this by hitting Ctrl+Alt+Shift+Del.

If the Shell extension is already installed, the Notepad++ installer cannot update or overwrite it, you first have to uninstall it and restart Explorer.

To manually install the DLL (which resides in your Notepad++ installation folder), use `regsvr32 /i NppShell_01.dll`: a dialog box will pop up from which various details of the behaviour of the extension can be tweaked.

It should be noted that the Shell extension can have difficulty loading a file into Notepad++ if Notepad++ is in Admin mode.  As Windows appears to be moving away from shell extensions for the operating system interface, the developer [has indicated](https://github.com/notepad-plus-plus/notepad-plus-plus/issues/8786#issuecomment-1432115846) that the NppShell_01.dll extension may be deprecated in favor of a different solution.
