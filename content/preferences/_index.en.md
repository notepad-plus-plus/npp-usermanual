---
title: Preferences
weight: 100
---

Control many the aspects of Notepad++. They are divided in three main groups: Preferences, Style Configurator and Shortcut Mapper.

The Shortcut Mapper is a list of keyboard shortcuts to everything that can have one in Notepad++. Styler Configurator allows changing the visual appearance of anything that has a colour or a font. The Preferences dialog manages everything else. While there are various aspects in Notepad++ that are not configurable, you may not even notice them.

## Preferences

## Style Configurator

The Style Configurator dialog has three regions: Select theme, language and style selection lists, and the style defition.  

The "Select theme:" pulldown allows you to select which theme you want.  [Themes](../themes/_index.en.md) are pre-defined sets of formatting rules, which often try to use a consistent color scheme between languages.

The "Language:" selection list lets you select whether you want to set the formatting for "Global Styles", or a specific [programming language](../programming-languages/_index.en.md) that you want to set the highlighting for.  The "Style:" selection list lets you select which highlighting rule for the given language.  On all but "Language: Global Styles", there will also be a "Default ext." box, which is an un-editable list of the default file extensions associated with that Language; and the "User ext." box, where you can add a user-defined list of additional extensions (space separated, don't use the . in the extension), which says which other extensions you want to apply this language's formatting to.  There is no specific entry called "Normal text" or "Plain text": to edit the colors for a plain text file (like `.txt`), use the "Global Styles" language.

The final section will reiterate which language and style are selected, and allow you to set colors and fonts.  The Colour Style allows you to choose the Foreground or Background colour by clicking on the colored box.  The Font Style allows you to pick the font, size, and bold/italic/underline settings (if Font name or Font size are left blank, they will inherit from the Global Styles: Default Style.  Under the "Language: Global Styles" with "Style: Global override", there are also a series of checkboxes for "Enable global xxx", which will mean that Notepad++ will use the Global override setting for that attribute, rather than using the per-language styling settings for that attribute.

Some language/style combinations (like Perl > INSTRUCTION WORD) will additionally have a list of default keywords (not editable) and user-defined keywords (which allow you to add new keywords to apply this style to).

The Save & Close button will save the settings and close the dialog.  The Cancel button will exit the dialog without updating the style settings.  The Transparency checkbox will allow you apply transparency to the Style Configurator dialog box.

### Configuration file: `stylers.xml`

If you prefer to edit XML instead of using the GUI, you may use the `stylers.xml` configuration file to edit the default theme, or `themes\blah.xml` to edit theme "blah".  

The `<LexerStyles>` contains a `<LexerType>` for each programming language -- where the `desc=` attribute matches the name in the list of Languages from the GUI.  Each of those contains one or more `<WordsStyle>` tags, where teh `Name=` attribute matches the entries in the GUI's list of Styles for that language; the WordsStyle are usually empty tags (`<WordsStyle .../>`), but can contain values (`<WordsStyle...>user1 user2 ...</WordsStyle>`) if there is an associated list of user-defined keywords for that style.  There is also a `<GlobalStyles>` section, with `<WidgetStyle>` entries, corresponding to the elements of the "Global Styles" in the GUI.

### Common Syntax Highlighting Problems

If you find that when a particular programming language is selected from the Languages menu, but no syntax highlighting is applied, check which theme you are using in the Style Configurator dialog.  If your selected them does not include settings for a given programming language, it cannot apply the highlighting.  You can edit the theme's XML file, pasting in the appropriate `<LexerType>` from a different theme (or the default `stylers.xml`) into your theme file; save the file, exit and reload Notepad++; now, the language should be listed in your theme's Style Configurator languages list, and you should be able to set the colors to match the other languages in your theme.

If you change a color in your Style Configurator, but the color doesn't change in the editor, it may be that you don't have the right language lexer selected: in the main Notepad++ window, the lower-left of the status bar will list the active lexer, or you can check the Language menu for which entry has the `•` to indicate it's selected.

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

### Configuration file: `shortcuts.xml`

If you prefer to edit XML instead of using the GUI to modify shortcuts, you may edit the `shortcuts.xml` file.  The keyboard shortcuts are defined as attributes of the `<macro>`, `<command>`, `<plugincommand>`, and `<scintkey>` tags.  The `Key=` attribute is the decimal value for the keycode associated with the key you want to hit.  The `Ctrl=`, `Alt=`, `Shift=` attributes have values of either "yes" or "no", and either enable or disable the modifier for that key.

### Common Shortcut Mapper Problems

With the introduction of the message area<!-- TODO: "in v7.5.xxx" or whenever it was introduced -->, it is easy to see when a conflict exists between shortcuts.  All you have to do is pick the entry that you _don't_ want to use the conflicted shortcut, and either Clear or Modify the shortcut so there is no longer a conflict.