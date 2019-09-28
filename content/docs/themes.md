---
title: Themes
weight: 110
---


Themes are pre-defined sets of formatting rules, which often try to use a consistent color scheme between languages.  You may choose your theme using the [**Preferences > Style Configurator** dialog](../preferences/#style-configurator).

Notepad++ comes packaged with a default theme and a number of other themes to start with.  You may customize any of those themes using the Style Configurator dialog, or by editing the underlying XML files.

Theme XML files are stored in `%AppData%\Notepad++\Themes` for a normal installation, or in the `Themes\` subdirectory of your Notepad++ installation directory if you chose local configuration during installation or if you are using a portable version of Notepad++.  If you edit the files directly, you must exit all instances of Notepad++ and reload for the changes to take place.  (Also, if you made changes in the Style Configurator _and_ by editing the file, the two sets of changes will be in conflict, and you might not get what you want.  Stick with one method of editing at a time.)

To create a new theme, copy an existing theme file to a new name in the same directory, reload Notepad++, and use the Style Configurator to edit the color and font settings (or edit the XML file directly, and reload).

You may share a theme in a similar method to creating a new theme: copy the theme file, give it an appropriate name, and put it in your `themes\` subdirectory: it's the same whether you are sharing across multiple users on the same computer, sharing across local computers, or sharing over the internet.

