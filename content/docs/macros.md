---
title: Task automation with macros
linktitle: Macros
weight: 60
---

Notepad++ is capable of recording some of your actions you perform while editing
a document, and replaying those later on to avoid having to repeat that sequence
of actions. This is called a macro and can save a great deal of time. Macros
can be played once, or multiple times, even as long as is required to run through
an entire document. You can save them for later use and assign keystrokes to
them for fast access (See [Shortcut Mapper](../preferences/#shortcut-mapper)). 
Macros are sensitive to the current position of the cursor and will (normally 
speaking) operate relative to it.


## Record a macro

To record a macro, select **Macro > Start Recording** or press the  button on the
toolbar. Notepad++ will now keep track of the changes you make on a document or
certain actions you perform.

To stop recording, select **Macro > Stop Recording** or select the  button on the
toolbar. As an exception to most commands, you can toggle this behavior with a
special shortcut combination that is not listed in the menu but solely in the
Shortcut mapper (see [Shortcut Mapper](../preferences/#shortcut-mapper)). 
By default, this is the combination Ctrl-Shift-R.

After the recording is stopped, it will be stored in a temporary buffer. If you
haven't performed any actions during the recording, this buffer will be cleared. If you start
recording another macro without saving your earlier work, it will be lost.


## Play a recoded macro

To play the macro in the buffer, select **Macro > Playback** or press the button.
This will perform the macro once at the current position.


## Save a recorded macro

To save the macro in the buffer, select **Macro > Save current recorded macro** or
press the toolbar button. A dialog will pop up asking for a name of the macro and the
default key combination. These can later be changed (or deleted) using
**Macro > Modify Shortcut / Delete Macro**, which brings up the 
[**Settings > Shortcut Mapper**](../preferences/#shortcut-mapper) on the **Macros** tab.
When saved, the macro will be available in the bottom section of the **Macro** menu, or
from the pulldown in the dialog accessed from the **Macro > Run a Macro Multiple Times** 
menu entry.

As noted in the [Configuration Files](../config-files) documentation, Notepad++
writes the configuration files (including the macros) when it exits, which means that
after you save your macro, your new macro will _not_ be written to the `shortcuts.xml` 
configuration file until Notepad++ exits.  Thus, if you open `shortcuts.xml` after saving
the macro but before exiting Notepad++, you will _not_ be able to see your new macro yet.

## Play a recoded macro multiple times

To play the current macro in the buffer or any saved macro once or multiple
times, select **Macro > Run a Macro Multiple Times**... or press the button.
A dialog will pop up allowing you to select what macro to perform (buffer
macro or any saved macro) and how many times. You can also opt to perform the
macro until the cursor reaches the end of the current file (starting from
its current position).

Note that if no macros are available, this menu option is greyed out, and 
the dialog is inaccessible.


## Edit or delete an existing macro shortcut

To edit or delete an existing macro shortcut, you can use the Shortcut mapper,
which displays all shortcuts of all kinds, and allows changing or removing a key
binding. The interface is also available through the **Macro > Modify
shortcut / Delete macro** menu entry. 

The contents of a macro definition can be edited only in the `shortcuts.xml` 
file: there is no built-in interface in Notepad++.  For more information on
the details of how the macros are stored, and the syntax involved, see the 
[**Configuration Files Details**: **<Macros>** section](../config-files/#macros).
