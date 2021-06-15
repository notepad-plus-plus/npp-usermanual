# Contribution


## Pull Requests (PR)

Your pull requests are welcome to suggest changes to the user manual.

### Guidelines for pull requests

* *KISS* - Keep It Simple, Stupid.  Fewer changes per PR are better.
* Respect Notepad++ User Manual style.
* It is best if there is an open [issue](/notepad-plus-plus/npp-usermanual/issues) before making changes and submitting a PR, so that you can ask whether your idea is worth incorporating before spending the effort on
* You will need to create a fork to make changes.  Create a new branch in your fork for each PR.

If these guidelines and style guide are not followed, or if the reviewers otherwise do not believe the submitted changes are appropriate, you may be asked to make changes to your PR, or your PR may be rejected.  If you do not make requested changes, the reviewers may edit or reject the PR.  We reserve the right to reject a PR for any reason, not just for a reason explicitly enumerated in this document.

## Style Guide

* First and foremost, when editing, keep it similar to what's already in that document.

* When referencing a menu item, like **File > Open**, make it bold, and use `>` as the separator-character between different levels.  <!-- This follows Microsoft documentation style for the separator character, so will make it more familiar to Windows users. -->

* When referencing a setting in a dialog box, make it bold.  Examples:
    * On the **Settings > Preferences > Backup** page, please enable **☑ Remember Current Session For Next Launch**"
    * Use the checkbox **Search > Find > Search Mode: ☑ Regular Expression** to enable regular expressions in your search

* For text that you want to indicate as user-entered (such as regular expressions or values entered into dialog box prompts), and for filenames and directories, use backticks to set the `monospaced / code` formatting.

* Special symbols may be entered by pasting in Unicode characters.  Please stick to common characters that are likely to be rendered on a variety of platforms with a variety of fonts.

* Images should be used sparingly.  If they are needed, keep the filesize small and place the image file in the `content/docs/images/` directory.

## Cross-Links

* To link from one page in the user-manual docs to the top of another page, use the syntax `[link name](../page/)` .  *Note* that in the link syntax, `page` does _not_ include the `.md` extension.

* To link to an anchor (like a heading) in another file, use `[link name](../page/#anchor)` ; or use `[link name](#anchor)` to link to an anchor (heading) in the same file.  The anchor names are the lower-case version of the section headers, with spaces replaced by hyphens.  

* Example: from the [Themes](content/docs/themes/) page, you can link to the [**Preferences > Style Configurator**](content/docs/preferences/#style-configurator) using the syntax `[**Preferences > Style Configurator**](../preferences/#style-configurator)`.
