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
* **Create New** will copy the default **User Defined Language** stylings and rules to a new name.
* **Save As** will copy the currently-selected UDL, with all its stylings and rules, to a new name.
* **Import...** will [import](#import-a-udl) a UDL XML file into your current instance ([see below](#import-a-udl)).
* **Export...** will save the UDL XML file to a location of your choosing; you can then share this with others, so that they can [import](#import-a-udl) your UDL for their own use.
* **Dock** or **Undock** will toggle whether the UDL dialog is a standalone dialog, or docked in the Notepad++ window.
* **☐ Ignore Case** will make the various keywords ignore case while matching.
* **☐ Transparency** (when not docked) will make the dialog box semi-transparent; the slider bar changes from virtually invisible (all the way to the left) to mostly opaque (all the way to the right); if you want it completely opaque (no transparency), uncheck the box.

When a UDL other than the default **User Defined Language** is seelcted in the pulldown, the following will also be available:
* **Rename** will rename the currently-selected UDL.
* **Remove** will delete the currently-selected UDL.
* **Ext.: ____** will accept a list of zero or more extensions (without the period).  Files that match these extensions will be interpreted as belonging to the currently-selected UDL, and will be styled appropriately.  These extensions override the default extensions for pre-defined **Languages**, so if your UDL's extension conflicts with another language's extension, the UDL will take priority.

### UDL Configuration Tabs

Ivan Radić has created the definitive guide to the nuts and bolts of UDL version 2.1, which is available at [https://ivan-radic.github.io/udl-documentation/]().  He explains the details of what each of the tabs in the **User Defined Language** dialog box will do, and how to use them to style your various keywords.  However, these descriptions will give you an overview of what each tab is for.

* The **Folder & Default** tab allows setting the default style, setting up keywords (or characters) that will allow code folding, and setting up styles for those keywords.  The **Open**, **Middle**, and **Close** boxes under each folding-type define the triggers for the start, middle, and end of folding.  For example, with `if`, `else`, and `endif`, it will define fold regions so that you can fold from `if` to `else`, from `else` to `endif`, and (assuming there is no `else` clause) from `if` to `endif`.  **Folding in comment** allows comments to include folding; **Folding in code 1 style** allows the triggers to be touching something else (so with a trigger of `{`, it will match `if{` or `if {`), whereas **Folding in code 2 style** requires there be whitespace around the trigger (so `if{` would _not_ match an **Open**-trigger of `{`).

* The **Keywords List** tab allows defining eight (8) different groups of keywords, so you can style different groups of words differently (like builtin functions vs. flow control keywords).  Separate each keyword by a space (and that means that spaces are not allowed in keywords unless you put quotes around the phrase).  If **☐ Prefix Mode** is enabled for a given group, that means that it will match anything that _starts_ with your string (so a keyword of `for` would match `for`, `forth`, and `format` if that option is enabled).

    As a point of interest, you shouldn't have a given keyword in more than one keyword-group _or_ folder-group.  If you want `if`/`else`/`endif` to cause block-folding, do not also put them in one of your keyword-groups.

* The **Comment & Number** tab allows setting styles for comments and for numbers.  
    * **Line Comment Position** allows you to decide whether "line comments" can start anywhere on the line, must start at the beginning, or can only start after whitespace.
    * **☐ Allow folding of comments** will enable comments to be foldable.
    * **Comment line style** defines the style  for "line comments" -- comments that proceed from the opening-trigger to the end of the line.
    * **Comment style** defines the style for multiline-comments.
    * **Number style** defines the style for numbers
        ... TODO ... how much detail to I want to replicate from Ivan here?

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

... TODO ...

<!--
## shared UDL files

At one time, there was a wiki-maintained list of externally-available UDL definition files
[UDL List](http://docs.notepad-plus-plus.org/index.php/User_Defined_Language_Files#Contributing_new_user_defined_language_files)

But it's gone, so hide this code for now.  Someday, something similar may be maintained
-->
