The startup behavior of Notepad++ can be adjusted with a few (0 sized) control files. Their absence or presence will control how Notepad++ acts:

doLocalConf.xml
If present, Notepad++ will use the installation directory for all configurations. If absent, %APPDATA% is used instead.
asNotepad.xml
If present, Notepad++ will act as Windows Notepad, meaning it will launch in multiple instances, hides the tab bar and will not load the previous session.
