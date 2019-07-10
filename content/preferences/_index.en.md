---
title: Preferences
weight: 100
---

Control many the aspects of Notepad++. They are divided in three main groups: Preferences, Style Configurator and Shortcut Mapper.

The Shortcut Mapper is a list of keyboard shortcuts to everything that can have one in Notepad++. Styler Configurator allows changing the visual appearance of anything that has a colour or a font. The Preferences dialog manages everything else. While there are various aspects in Notepad++ that are not configurable, you may not even notice them.

## Preferences

## Style Configurator

## Shortcut Mapper

The Shortcut Mapper dialog presents five tabs: 
1. `Main menu`: used for items in the main Notepad++ menu items, like File, Edit, Search, View, Encoding, Language, Settings, Run, and ? (Help/About) menus.
2. `Macros`: used for items in the Macros menu
3. `Run commands`: used for user-added items in the Run menu.  (The **Run...** menu entry shortcut is defined in the `Main Menu` tab)
4. `Plugin commands`: used for actions from the Plugins menu.
5. `Scintilla commands`: used for all the Scintilla actions, thus allowing editing of shortcuts for all the editor commands.

Each tab consists of an area for selecting the command to shortcut, a message area, a Filter input, and buttons to Modify, Clear, Delete, and Close.  

When selecting the command, there are generally two columns: Name and Shortcut.  The Name matches the menu item (or the name of the Scintilla message).  The Shortcut shows the current-assigned shortcut (if any).  The `Main menu` tab has an additional Category column, which tells which menu category the command falls under.  The `Plugin commands` tab has an additional Plugin column, which tells which plugin DLL the shortcut applies to.

The message area will tell you if there are "no shortcut conflicts for this item" (when the shortcut for the selected action is not used anywhere else; or it will give you the name of the tab, followed by the Name for the action, which uses the same shortcut as the currently-selected action.  

The Filter input allows you to enter a piece of literal text, and it will filter all the Names in the active tab for a given text substring, only listing the Names that contain that literal substring, ignoring case.  There are no regular expression or wildcard syntax interpretations in the Filter.

Use the Modify button to edit the existing shortcut or to create a shortcut for an entry that has none.  The resulting dialog will show the Name of the active action.  There are checkboxes to enable the CTRL, ALT, and SHIFT key-modifiers.  The main key in the shortcut is defined by the pulldown menu.  Hitting OK will apply the added or changed shortcut and leave the dialog.  Cancel will undo your changes and leave the dialog.  (Please note that if you are using some localizations, the key you select [might not match](https://notepad-plus-plus.org/community/topic/17679/using-caret-circumflex-key-for-a-shortcut/10) <!-- TODO = this link should really refer to a submitted issue request, rather than a forum-topic --> what key you type: whatever key in your locale uses the same keycode as the standard US english keyboard will be the actual key.)  In the `Scintilla commands` tab, you can actually assign more than one shortcut to a given Scintilla command, so there is an extra pane listing existing shortcuts, and additional Add and Remove buttons.

Use the Clear button to remove the existing shortcut for a given entry.

The Delete button is usually disabled.  However, in the `Macros` and `Run commands` menu, the Delete button will be enabled, and it will remove the selected entry from the menu -- so it will not only not have a shortcut, but it won't be in the menu the next time you run Notepad++.

The Close button will close the dialog box.

If you prefer to edit XML instead of using the GUI to modify shortcuts, you may edit the `shortcuts.xml` file.  The keyboard shortcuts are defined as attributes of the `<macro>`, `<command>`, `<plugincommand>`, and `<scintkey>` tags.  The `Key=` attribute is the decimal value for the keycode associated with the key you want to hit.  The `Ctrl=`, `Alt=`, `Shift=` attributes have values of either "yes" or "no", and either enable or disable the modifier for that key.
