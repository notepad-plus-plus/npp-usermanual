---
title: Shell Extension
weight: 130
---

By default the Notepad++ installer comes with a Shell extension. This is not really part of the Notepad++ program but very useful. If you choose to install it, then any file you rightclick on will show an entry named “Edit with Notepad++” with the Notepad++ icon.

Please note that to install or remove the extension, it sometimes is required to restart the Explorer process. For this you can reboot, logout and log back in or use the task manager to kill explorer (Windows NT and up) and restart it again. You can do this by hitting Ctrl+Alt+Shift+Del.

If the Shell extension is already installed, the Notepad++ installer cannot update or overwrite it, you first have to uninstall it and restart Explorer.

If you issue the install command for the dll, which is regsvr32 /i NppShell_01.dll, a dialog box will pop up from which various details of the behaviour of the extension can be tweaked. The trailing number will increase as versions go.
