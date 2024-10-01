---
title: Themes
weight: 160
---

## What are Themes

Themes are pre-defined sets of formatting rules, which often try to use a consistent color scheme between languages.  You may choose your theme using the [**Preferences > Style Configurator** dialog](../preferences/#style-configurator).

Notepad++ comes packaged with a default theme (called "Default (stylers.xml)") and a number of other themes to start with.  You may customize any of those themes using the Style Configurator dialog, or by editing the underlying XML files.

Theme XML files are stored in `%AppData%\Notepad++\Themes` for a normal installation, or in the `Themes\` subdirectory of your Notepad++ installation directory (if you chose local configuration during installation or if you are using a portable version of Notepad++, it will only be in the installation or portable directory).  If you edit the files directly, you must exit all instances of Notepad++ and reload for the changes to take place.  (Also, if you made changes in the Style Configurator _and_ by editing the file, the two sets of changes will be in conflict, and you might not get what you want.  Stick with one method of editing at a time.)

The `stylers.xml` and other Theme files store the colors, font and bold/italic/underline settings, and user-defined extensions and user-defined keywords for each of the built-in syntax-highlighting languages.  All of these can be customized -- either in the selected theme, or by creating a new theme and switching to that new theme before editing it.

## Editing and Creating Themes

The easiest way to edit an existing theme is to use the [Style Configurator](../preferences/#style-configurator) to edit the various styles.  

But you can also edit the underlying XML file: `stylers.xml` (the default theme) is in the main configuration directory; all the other themes have their own file in the `Themes\` subdirectory.  [Config Files > Highlighting schemes: `stylers.xml`](../config-files/#highlighting-schemes-stylersxml) has the details on the XML format for themes, to help with manually editing it.

The easiest way to create a new theme is to copy an existing theme file to a new name in the `%AppData%\Notepad++\Themes\` directory (or equivalent), reload Notepad++, and then use the Style Configurator to edit the color and font settings (or edit the XML file directly, and reload).  For the "existing theme file" to copy from: for creating "light" theme, the best idea (to make sure it's as up-to-date as possible, to list all the current syntax highlighting languages and styles) is to copy `stylers.model.xml` from your installation directory and put the renamed copy in your `%AppData%\Notepad++\Themes\` directory; for creating a "dark" theme, start from a copy of `Themes\DarkModeDefault.xml`.

(You have to exit Notepad++ and rerun the application to see a new theme that you've copied into your Themes directory, or to see any updates you've made by manually editing the XML file(s).)

## Sharing Themes

You may share a theme (or someone may share with you) in a similar method to creating a new theme: copy the theme file, give it an appropriate name, and put it in your `Themes\` subdirectory: it's the same whether you are sharing across multiple users on the same computer, sharing across local computers, or sharing over the internet.

Aside from the Themes that ship with Notepad++ when you install it, there is also an official [Notepad++ Themes Collection on GitHub](https://github.com/notepad-plus-plus/nppThemes), where you can make your Theme publically available, or grab a Theme that others have shared.

## Keeping Stylers/Themes Up-To-Date

When you install/update Notepad++, the installer will populate `<installation_dir>\Themes\*.xml` with the most recent copies of the standard Themes, and will overwrite the `<installation_dir>\stylers.model.xml` to make sure that the source of the default theme contains all the appropriate [syntax-highlighting languages](../programming-languages/) and all the most-recent general interface styles in Style Configurator's [**Global Styles**](../preferences/#global-styles).  

However, except for a new installation (where you don't already have `%AppData%\Notepad++\stylers.xml`), your copy of the the default theme and any themes you have in the `%AppData%\Notepad++\Themes` will _not_ be updated or overwritten (because the Developer doesn't want you to lose any customizations).  If you use the default theme, and have not customized any styles in the Style Configurator, then the easiest way to update the default theme is to exit Notepad++, delete `%AppData%\Notepad++\stylers.xml`, and restart Notepad++, which will recreate your `stylers.xml` from the most-recent `stylers.model.xml`; however, if you had any Style Configurator customizations (including colors, fonts, or per-language user-defined extensions or user-defined keywords), they _will_ be lost if you delete `stylers.xml`.

When a new version of Notepad++ is released, the Developer ensures `stylers.model.xml` and `Themes\DarkModeDefault.xml` are up-to-date, but the Developer relies on volunteers to submit PR to update the other themes, so many of them can be missing languages or specific styles.  So if you want to update a Theme that's missing languages or specific styles, or if you want to edit `stylers.xml` without losing any of your customizations, then you will want to open up your `stylers.xml` or other theme's XML simultaneously with `stylers.model.xml`; you can then go section-by-section and line-by-line (the ComparePlug plugin could be helpful for this), and copy over any of the `<LexerType...>` sections that don't exist in yours (note they may be in a different order), or any `<WordsStyle...>` missing from a `<LexerType...>` or any `<WidgetStyle...>` that is missing from your `<GlobalStyles>` section.  This can be a tedious process, so if you're willing to install the PythonScript plugin, you can find a script in the Notepad++ Community Forum's "[Config Files Need Updating, Too](https://community.notepad-plus-plus.org/topic/26049/config-files-need-updating-too)" post, which will automate the process of keeping your themes (and default language keywords) up-to-date.
