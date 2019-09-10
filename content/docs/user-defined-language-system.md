---
title: User Defined Languages
weight: 20
---

## What are User Defined Languages

Notepad++ comes prepackaged with many Language lexers, which apply syntax highlighting to source code or textual data.  However, not every possible language or formatting style is available.  Enter the **U**ser **D**efined **L**anguages (or "UDL" for short): the UDL interface allows the user to define rules for formatting normal text, keywords, comments, numbers; to define delimiters (like quotes around strings or parentheses around lists) which will cause text between those delimiters to be formatted; and to define symbols or keywords that can be used to allow folding (on-demand hiding and unhiding of blocks of code or text).

## UDL Dialog Box or Window

The **Languages** menu on the menu-bar includes the list of builtin languages, and below those are a separator followed by **Define Your Language...** and a list of any UDL that have been already defined.

Using **Languages > Define Your Language...** will bring up a dialog box (which can be docked as a pane in the Notepad++ Window, or can be a floating dialog box).

The main pulldowns and buttons are available, whichever configuration tab is active:
* **User Language** pulldown lists all the existing UDL will allow you to select the UDL you would like to edit or examine.  There is a special entry for the default UDL, called **User Defined Language** here (though it shows up in the Notepad++ **Languages** menu as **User-Defined**), which can be used as a template for other UDL.
* **Create New** will copy the default **User Defined Language** stylings and rules to a new name
* **Save As** will copy the currently-selected UDL, with all its stylings and rules, to a new name
* **Import...** will [import](#import-a-udl) a UDL XML file into your current instance ([see below](#import-a-udl))
* **Export...** will save the UDL XML file to a location of your choosing; you can then share this with others, so that they can [import](#import-a-udl) your UDL for their own use
* **Dock** or **Undock** will toggle whether the UDL dialog is a standalone dialog, or docked in the Notepad++ window.
* ...

When a UDL other than the default **User Defined Language** is seelcted in the pulldown, the following will also be available:
* **Rename** will rename the existing UDL (only visible when a UDL other than the default **User Defined Language** is selected)
*  ...

Ivan Radić has created the definitive guide to the nuts and bolts of UDL version 2.1, which is available at [https://ivan-radic.github.io/udl-documentation/](https://ivan-radic.github.io/udl-documentation/).  He explains the details of what each of the tabs in the **User Defined Language** dialog box will do, and how to use them to style your various keywords.

### Import a UDL

The internet has plenty of Notepad++ UDL xml files.  Once you have the XML, you can then import it into your Notepad++, so that you can use that UDL yourself.  There are two main ways to do this:

1. Copy the XML into the [appropriate `userDefineLangs` subfolder](#udl-file-locations). Exit all instances of Notepad++ and reload, then the new UDL will be available.

2. Use the **Import...** button, navigate to the source XML, and the UDL will be immediately available.

## UDL File Locations

Individual UDL files are stored in one of two `userDefineLangs` subfolders.  Each XML file in that folder is used to define one or more UDL.

1. `%AppData%\Notepad++\userDefineLangs`: this is the default location for most Notepad++ installations
2. `<notepad++_directory>\userDefineLangs`: this is the location for portable versions, or if you turned on "local configuration mode" (or disabled `%AppData%`) during the installation.  `<notepad++_directory>` refers to whatever folder the `notepad++.exe` application executable is located.

If you created or imported a UDL using the **User Defined Languages** dialog inside Notepad++, they will be in the `userDefineLang.xml` file.  This single file often holds multiple UDL definitions.

1. `%AppData%\Notepad++\userDefineLang.xml`: this is the default location for most Notepad++ installations
2. `<notepad++_directory>\userDefineLang.xml`: this is the location for portable or "local configuration mode" versions, as described above

## UDL and Themes

... 
<!--
## shared UDL files

At one time, there was a wiki-maintained list of externally-available UDL definition files
[UDL List](http://docs.notepad-plus-plus.org/index.php/User_Defined_Language_Files#Contributing_new_user_defined_language_files)

But it's gone, so hide this code for now.  Someday, something similar may be maintained
-->
