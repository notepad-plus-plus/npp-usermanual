# Contribution


## Pull Requests (PR)

Your pull requests are welcome to suggest changes to the user manual.

### Guidelines for pull requests

* *KISS* - Keep It Simple, Stupid.  Fewer changes per PR are better.
* Respect Notepad++ User Manual style.
* It is best if there is an open [issue](../../issues) before making changes and submitting a PR, so that you can ask whether your idea is worth incorporating before spending the effort on.
* You will need to create a fork to make changes.  Create a new branch in your fork for each PR, keeping each PR independent of others you submit.

If these guidelines and style guide are not followed, or if the reviewers otherwise do not believe the submitted changes are appropriate, you may be asked to make changes to your PR, or your PR may be rejected.  If you do not make requested changes, the reviewers may edit or reject the PR.  We reserve the right to reject a PR for any reason, not just for a reason explicitly enumerated in this document.

## Style Guide

* First and foremost, when editing, keep it similar to what's already in that document.  
  * Do not arbitrarily change an existing style choice (like `-` vs `*` for bulleted lists, or `_..._` vs `*...*` for italics) without a good technical reason
  * If you are fixing an actual Markdown _error_ that causes the final user manual documentation to render incorrectly, that is allowed (and encouraged).

* When referencing a menu item, like **File > Open**, make it bold, and use `>` as the separator-character between different levels.  <!-- This follows Microsoft documentation style for the separator character, so will make it more familiar to Windows users. -->

* When referencing a setting in a dialog box, make it bold.  Examples:
    * On the **Settings > Preferences > Backup** page, please enable **☑ Remember Current Session For Next Launch**"
    * Use the checkbox **Search > Find > Search Mode: ☑ Regular Expression** to enable regular expressions in your search

* For text that you want to indicate as user-entered (such as regular expressions or values entered into dialog box prompts), and for filenames and directories, use backticks to set the `monospaced / code` formatting.

* Special symbols may be entered by pasting in Unicode characters.  Please stick to common characters that are likely to be rendered on a variety of platforms with a variety of fonts.

* Images should be used sparingly.  If they are needed, keep the filesize small and place the image file in the `content/docs/images/` directory.

* Changes to the theme (whether it's just slight edits or a completely new theme, or anything in between) will not be accepted unless you have worked with the owner to make sure that the changes to the theme are necessary or appropriate.

## Cross-Links

* To link from one page in the user-manual docs to the top of another page, use the syntax `[link name](../page/)` .  *Note* that in the link syntax, `page` does _not_ include the `.md` extension.

* To link to an anchor (like a heading) in another file, use `[link name](../page/#anchor)` ; or use `[link name](#anchor)` to link to an anchor (heading) in the same file.  The anchor names are the lower-case version of the section headers, with spaces replaced by hyphens.  

* Example: from the [Themes](content/docs/themes/) page, you can link to the [**Preferences > Style Configurator**](content/docs/preferences/#style-configurator) using the syntax `[**Preferences > Style Configurator**](../preferences/#style-configurator)`.

## Keep PRs independent

If you are making multiple PRs, please make sure you keep them separate.  If you make a first change to change A to B and submit it as PR #N, then using the same branch (or a new branch that started from the first branch) and change C to D and submit as PR #M, then PR #M will contain the same changes as #N, in addition to the new changes.  This will mean that if #N is rejected, #M will likely be rejected as well (because they contain the same changes that were rejected); and if #N is accepted (possibly with changes from the maintainers), then #M might come in conflict with #N; this also makes it harder to evaluate specifically what was intended for PR #M.

The best way to avoid this problem is to 
1. Fork from the main repository, or sync your existing fork with the main repository using GitHub's **Fetch Upstream > Fetch and Merge** feature
2. Before making any new changes, create a branch specific to the one issue you are trying to fix
3. Make those changes and submit a new PR from the _branch_ back to the main repository
4. If you want to make changes for another issue before the PR from step#3 was accepted and merged, create a new branch from your unmodified fork, so that it's starting from the same state that the main repository is currently in
5. Make the changes in the new branch, and submit a PR from that branch to the main repository
6. Now your PRs from #3 and #5 are independent, and #5 won't repeat or interfere with the changes from #3

If PRs are not kept independent, they may be rejected.
