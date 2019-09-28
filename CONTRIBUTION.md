# Contribution


## Pull Requests

Your pull requests are welcome; however, they may not be accepted for various reasons.


### Guidelines for pull requests

1. Respect Notepad++ User Manuel style.
2. Create a new branch for each PR.

## Style Guide

1. First and foremost, when editing, keep it similar to what's already in that document.

2. When referencing a menu item, like **File > Open**, make it bold, and use > as the separator-character between different levels.  <!-- This follows Microsoft documentation style for the separator character, so will make it more familiar to Windows users. -->

3. When referencing a setting in a dialog box, make it bold.  Examples:
    * On the **Settings > Preferences > Backup** page, please enable **☑ Remember Current Session For Next Launch**"
    * Use the checkbox **Search > Find > Search Mode: ☑ Regular Expression** to enable regular expressions in your search

4. For text that you want to indicate as user-entered (such as regular expressions or values entered into dialog box prompts), and for filenames and directories, use backticks to set the `monospaced / code` formatting.

## Cross-Links

To properly link from one page in the user-manual docs to another, use the syntax `[link name](../page/)` to link to the top level, or `[link name](../page/#anchor)` to link to an anchor (like a heading) in another document.  Note that `page` does _not_ include the `.md` extension.  The anchor names are the lower-case version of the section headers, with spaces replaced by hyphens.  Thus, from the [Themes](content/docs/themes/) page, link to the [**Preferences > Style Configurator**](content/docs/preferences/#style-configurator) using the syntax `[**Preferences > Style Configurator**](../preferences/#style-configurator)