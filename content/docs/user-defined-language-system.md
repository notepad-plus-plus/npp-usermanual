---
title: User Defined Languages
weight: 20
---

## What are User Defined Languages

Notepad++ comes prepackaged with many Language lexers, which apply syntax highlighting to source code or textual data.  However, not every possible language or formatting style is available.  Enter the **U**ser **D**efined **L**anguages (or "UDL" for short): the UDL interface allows the user to define rules for formatting normal text, keywords, comments, numbers; to define delimiters (like quotes around strings or parentheses around lists) which will cause text between those delimiters to be formatted; and to define symbols or keywords that can be used to allow folding (on-demand hiding and unhiding of blocks of code or text).

## UDL Dialog Box or Window

The **Languages** menu on the menu-bar includes the list of built-in languages, and below those are a separator followed by **Define Your Language...** and a list of any UDL that have been already defined.

Using **Languages > Define Your Language...** will bring up a dialog box (which can be docked as a pane in the Notepad++ Window, or can be a floating dialog box).

The main pulldowns and buttons are available, whichever configuration tab is active:

* **User Language** pulldown lists all the existing UDL will allow you to select the UDL you would like to edit or examine.  There is a special entry for the default UDL, called **User Defined Language** here (though it shows up in the Notepad++ **Languages** menu as **User-Defined**), which can be used as a template for other UDL.
* **Create New** will copy the default **User Defined Language** stylings and rules to a new name.
* **Save As** will copy the currently-selected UDL, with all its stylings and rules, to a new name.
* **Import...** will [import](#import-a-udl) a UDL XML file into your current instance ([see below](#import-a-udl)).
* **Export...** will save a UDL XML file to a location of your choosing; you can then share this with others, so that they can [import](#import-a-udl) your UDL for their own use.
* **Dock** or **Undock** will toggle whether the UDL dialog is a standalone dialog, or docked in the Notepad++ window.
* **☐ Ignore Case** will make the various keywords ignore case while matching.
* **☐ Transparency** (when not docked) will make the dialog box semi-transparent; the slider bar changes from virtually invisible (all the way to the left) to mostly opaque (all the way to the right); if you want it completely opaque (no transparency), uncheck the box.

When a UDL other than the default **User Defined Language** is selected in the pulldown, the following will also be available:

* **Rename** will rename the currently-selected UDL.
* **Remove** will delete the currently-selected UDL.
* **Ext.: ____** will accept a list of zero or more extensions (without the period).  Files that match these extensions will be interpreted as belonging to the currently-selected UDL, and will be styled appropriately.  These extensions override the default extensions for pre-defined **Languages**, so if your UDL's extension conflicts with another language's extension, the UDL will take priority.  For example **Ext.: `md mkdn`** will associate `file.mkdn` or `something.md` with your selected UDL.

### UDL Configuration Tabs

Ivan Radić has created the definitive guide to the nuts and bolts of UDL version 2.1, which is available at [https://ivan-radic.github.io/udl-documentation/](https://ivan-radic.github.io/udl-documentation/).  He explains the details of what each of the tabs in the **User Defined Language** dialog box will do, and how to use them to style your various keywords.  However, these descriptions will give you an overview of what each tab is for.

* The **Folder & Default** tab allows setting the default style, setting up keywords (or characters) that will allow code folding, and setting up styles for those keywords.  The **Open**, **Middle**, and **Close** boxes under each folding-type define the triggers for the start, middle, and end of folding.  For example, with `if`, `else`, and `endif`, it will define fold regions so that you can fold from `if` to `else`, from `else` to `endif`, and (assuming there is no `else` clause) from `if` to `endif`.  **Folding in comment** allows comments to include folding; **Folding in code 1 style** allows the triggers to be touching something else (so with a trigger of `{`, it will match `if{` or `if {`), whereas **Folding in code 2 style** requires there be whitespace around the trigger (so `if{` would _not_ match an **Open**-trigger of `{`).

* The **Keywords List** tab allows defining eight (8) different groups of keywords, so you can style different groups of words differently (like built-in functions vs. flow control keywords).  Separate each keyword by a space (and that means that spaces are not allowed in keywords unless you put quotes around the phrase).  If **☐ Prefix Mode** is enabled for a given group, that means that it will match anything that _starts_ with your string (so a keyword of `for` would match `for`, `forth`, and `format` if that option is enabled).

    As a point of interest, you shouldn't have a given keyword in more than one keyword-group _or_ folder-group.  If you want `if`/`else`/`endif` to cause block-folding, do not also put them in one of your keyword-groups.

* The **Comment & Number** tab allows setting styles for comments and for numbers.
    * **Line Comment Position** allows you to decide whether "line comments" can start anywhere on the line, must start at the beginning, or can start anywhere on the line as long as it's only whitespace before the comment.
    * **☐ Allow folding of comments** will enable comments to be foldable.
    * **Comment line style** defines the style  for "line comments" -- comments that proceed from the opening-trigger to the end of the line.
    * **Comment style** defines the style for multiline-comments.
    * **Number style** defines the style for numbers.  The various **Prefix**es, **Suffix**es, and **Extra**s allow you to define extra numeric representations (useful for hexadecimal, binary, octal and similar representations, as well as for defining currency as a number).  The **Range** allows you to define a syntax for ranges, so that two numbers with a listed token in between will still be treated as a number.  (However, there may be conflicts if the **Range** setting matches one from **Operators & Delimiters**

* The **Operators & Delimiters** tab allows setting styles for operators and for delimiter pairs
    * **Operators 1** and **Operators 2** define two groups of operators (usually math and math-like operators).  The first defines operators that will be matched even if they are touching other characters (allowing `1+2`), whereas the second defines operators that must contain spaces to be recognized (like `1 + 2`).
    * The various **Delimiter** styles are pairs of **Open** and **Close** characters, where those characters and whatever comes between them will be styled per the rules defined for that entry.  This is useful for styling strings, parenthesized parameter lists, bracketed expressions, and anything else where it can have a .  The **Escape** entry allows defining a way of "escaping" the character so that the delimiter pair is not prematurely closed (such as `"` / `\` / `"` allowing `"this \" is an embedded quote character inside a string, escaped by the backslash"`).

### Import a UDL

The internet has plenty of Notepad++ UDL xml files.  Once you have the XML, you can then import it into your Notepad++, so that you can use that UDL yourself.  There are two main ways to do this:

1. Copy the XML into the [appropriate `userDefineLangs` subfolder](#udl-file-locations). Exit all instances of Notepad++ and reload, then the new UDL will be available.

2. Use the **Import...** button, navigate to the source XML, and the UDL will be immediately available.

The differences between those two methods are when the UDL will be available to Notepad++, and which config file will hold that UDL, per [UDL File Locations](#udl-file-locations).

## UDL File Locations

Individual UDL files are stored in one of two `userDefineLangs` subfolders.  Each XML file in that folder is used to define one or more UDL.

1. `%AppData%\Notepad++\userDefineLangs`: this is the default location for most Notepad++ installations
2. `<notepad++_directory>\userDefineLangs`: this is the location for portable versions, or if you turned on "local configuration mode" (or disabled `%AppData%`) during the installation.  `<notepad++_directory>` refers to whatever folder the `notepad++.exe` application executable is located.

If you created or imported a UDL using the **User Defined Languages** dialog inside Notepad++, they will be in the `userDefineLang.xml` file.  This single file often holds multiple UDL definitions.

1. `%AppData%\Notepad++\userDefineLang.xml`: this is the default location for most Notepad++ installations
2. `<notepad++_directory>\userDefineLang.xml`: this is the location for portable or "local configuration mode" versions, as described above

## UDL and Themes

The User Defined Languages are (mostly) _not_ affected by your [active theme](../preferences/#style-configurator).  This means that if you change theme (including going to [Dark Mode](../preferences/#dark-mode) which changes the theme to `DarkModeDefault`), you might have to edit your UDL colors to be readable.  The UDL doesn't override most of the settings in the [Style Configurator's "Global Styles"](../preferences/#global-styles) settings for the active theme, so some of the settings might make your UDL colors hard to read: 

* the UDL overrides the foreground color for text, and the background color for text (if transparency is not activated); however, the UDL does _not_ override the background color for spaces or the blank space that fills the unused portions of the editor view, so if your UDL default background does not match the theme's default background, the UDL-based document may look strange
* the UDL does not override the **Selected text colour** or **current line background**, so if your UDL's colors do not provide good contrast with these settings from the theme, selected text will be hard to read

Since you can set the colors of a UDL to whatever you want, you can manually make it match your theme.  In all, it is best to set the UDL's **Folder & Default > Default Style** to match the foreground and background colors of your active theme, which should balance well with the other of the theme's Global Styles settings.  Further, setting keywords groups and numbers and comments and operators to match the settings for the keywords, numbers, and comments of the other languages that you use in your active theme will help make UDL files fit the active theme better.

If you don't want to override the foreground and/or background text color for some parts of your UDL, activate transparency. This enables to create an UDL that works for multiple themes. For example activate transparency for background and foreground color of your UDL default style. Then activate transparency for background color of your keywords too and select a foreground color for your keywords that works for multiple themes.

If you want to define multiple UDL using the same basic color scheme as your active theme, you can start by setting the colors of the default **User Defined Language**, then **Create New** for each UDL that you want to match that scheme, customizing the rules for each new UDL.  (As soon as you exit Notepad++, the changes to the default UDL will be lost, but all the themes that you created from that will keep the colors they inherited.)

## User Defined Languages Collection

Throughout the history of Notepad++, many UDL files have been created by Notepad++ users and made publicly available.  There is once again a centralized [User Defined Languages Collection](https://github.com/notepad-plus-plus/userDefinedLanguages).

https://github.com/notepad-plus-plus/userDefinedLanguages

This central Collection is a convenient location for UDL-users to find new UDL files, and for UDL-authors to share their UDL files with the whole Notepad++ community.  The Collection includes instructions for how to use the files, as well as how to submit new UDL to the Collection.

## UDL Configuration File Contents

It is intended that UDL are edited using the GUI dialog boxes.  However, if you are the type of user who likes to configure Notepad++ through the configuration files, it is possible.  Please see the [Configuration Files Details](https://npp-user-manual.org/docs/config-files/#editing-configuration-files) for a description of the sequence for properly editing any of the config files, including the UDL definition files.

Most of the settings in the UDL definition files correspond directly to the names seen in the **User Defined Languages** dialog box, or the **Styler** sub-dialog.  The `<KeywordLists>` section defines the keywords or symbols for each highlighting category.  The `<Styles>` section defines the text styling (color, font, weight, and decoration) for each highlighting category.  The `<WordsStyle>` `fontStyle` attribute encodes the setting of the **Bold**, **Italic**, and **Underline** checkboxes from the **Styler** dialog, using the sum of **Italic**=1, **Bold**=2, and **Underline**=4 (so something with all three checkboxes set would have `fontStyle="7"`).  The `nesting` attribute similarly encodes the various nesting checkboxes from the **Styler** dialog with a sum of the values below, and indicate which styles will nest properly inside the active style:

| Checkbox    | Value |   | Checkbox  | Value  |   | Checkbox     | Value    |
|-------------|------:|---|-----------|-------:|---|--------------|---------:|
| Delimiter 1 | 1     |   | Keyword 1 | 1024   |   | Comment      | 256      |
| Delimiter 2 | 2     |   | Keyword 2 | 2048   |   | Comment Line | 512      |
| Delimiter 3 | 4     |   | Keyword 3 | 4096   |   | Operators 1  | 16777216 |
| Delimiter 4 | 8     |   | Keyword 4 | 8192   |   | Operators 2  | 33554432 |
| Delimiter 5 | 16    |   | Keyword 5 | 16384  |   | Numbers      | 67108864 |
| Delimiter 6 | 32    |   | Keyword 6 | 32768  |   |              |          |
| Delimiter 7 | 64    |   | Keyword 7 | 65536  |   |              |          |
| Delimiter 8 | 128   |   | Keyword 8 | 131072 |   |              |          |

The `<WordsStyle>` `colorStyle` attribute decides whether to use the defined colors from `fgColor` and `bgColor` attributes, or to use the default color setting (from **Settings > Style Configurator > Global Styles > Default Style**, _not_ from the UDL's default style).  The attribute should be set to one of the following:

* No `colorStyle` attribute: this style will use both the `fgColor` and `bgColor` attributes from this `<WordsStyle>` item (standard behavior)
* Set `colorStyle="2"`: this style will inherit the foreground color from the Default style, and use the `bgColor` value as the background color (equivalent to right-clicking the foreground color in the UDL styler dialog box)
* Set `colorStyle="1"`: this style will inherit the background color from the Default style, and use the `fgColor` value as the foreground color (equivalent to right-clicking the background color in the UDL styler dialog box)
* Set `colorStyle="0"`: this style will inherit both the foreground and background colors from the Default style (equivalent to right-clicking both the foreground and background colors in the UDL styler dialog box)
