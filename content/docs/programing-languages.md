---
title: Syntax Highlighting - Built-in Languages
weight: 70
---

## Supported Programming Languages

Around 90 Programming Languages are supported by Notepad++:

|                        |                        |                        |                        |                        |
|------------------------|------------------------|------------------------|------------------------|------------------------|
| ActionScript           | Ada                    | ASN.1                  | ASP                    | Assembly               |
| AutoIt                 | AviSynth               | BaanC                  | Batch                  | BlitzBasic             |
| C                      | C#                     | C++                    | CAML                   | CMake                  |
| COBOL                  | CoffeeScript           | Csound                 | CSS                    | D                      |
| Diff                   | Erlang                 | ErrorList              | ESCRIPT                | Forth                  |
| Fortran fixed form     | Fortran free form      | FreeBasic              | GDScript               | Go                     |
| Gui4Cli                | Haskell                | Hollywood              | HTML                   | ini                    |
| Inno Setup             | Intel HEX              | Internal Search        | Java                   | JavaScript             |
| json                   | json5                  | JSP                    | KiXtart                | LaTeX                  |
| Lisp                   | Lua                    | Makefile               | MATLAB                 | MMIXAL                 |
| mssql                  | NFO                    | Nim                    | Nncrontab              | NSIS                   |
| Objective-C            | OScript                | Pascal                 | Perl                   | PHP                    |
| PostScript             | PowerShell             | Properties file        | PureBasic              | Python                 |
| R                      | Raku                   | RC                     | REBOL                  | registry               |
| Ruby                   | Rust                   | SAS                    | S-Record               | Scheme                 |
| Shell                  | Smalltalk              | Spice                  | SQL                    | Swift                  |
| TCL                    | Tektronix extended HEX | TeX                    | TOML                   | txt2tags               |
| TypeScript             | Verilog                | VHDL                   | Visual Basic           | Visual Prolog          |
| XML                    | YAML                   |                        |                        |                        |

For these languages, Notepad++ supports [syntax highlighting](../preferences/#style-configurator) (customizable),
syntax folding, [auto-completion](../auto-completion/) (customizable),
[function list](../function-list/) (customizable via PCRE in xml file).

If your beloved language is not in the list above, you can define it yourself easily, by using the
[User Defined Languages System](../user-defined-language-system/).  If that doesn't meet your needs,
you could write (or have someone else write) a [lexer plugin](../plugins/#building-a-lexer-plugin).

Please note that in Notepad++ v8.3 and newer, Notepad++ has a feature will no longer perform syntax highlighting
on files that are over 200MB -- this prevents extreme performance slowdown caused by trying to
syntax highlight extremely large files.  This threshold is configurable in
[Settings > Preferences > Performance](../preferences/#performance) (starting in v8.4.7).

### Notes on Specific Languages

#### JavaScript

Internally, there are actually two entries for JavaScript: in the [Style Configurator](../preferences/#style-configurator),
these show up as "JavaScript" and "JavaScript (embedded)".  The first is for
standalone JavaScript files (usually with `.js` extension); the second is for when JavaScript is embedded in an HTML
file -- so you can actually have different color rules for when the JavaScript is inside HTML and when it's a separate
file.  (In the [`langs.xml`](../config-files/#keyword-lists-langsxml) and [`stylers.xml`](../config-files/#highlighting-schemes-stylersxml)
config files, the standalone uses `name="javascript.js"`.)

If you manually pick **Language > J > JavaScript**, the active file will use the standalone JavaScript settings.

#### ErrorList

The ErrorList language, available starting in v8.8.1, is useful for looking at logfiles, error output from compilers,
and colorful terminal outputs (like from the Windows PowerShell window or a Linux shell window), or anything else which
uses [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code). The syntax highlighting for this language will
 include coloring the various error outputs, as well as applying the _foreground_ color specified from ANSI escape codes
 (it will _not_ change the background color, even if the ANSI escape sequence does).

While this Language is active, if you toggle **[View > Show Symbol](../views/#show-symbol) > Show Control Characters &
Unicode EOL** (or **Show All Characters**, or use the [Toolbar](../user-interface/#toolbar) equivalents):
when control characters or all characters are
shown, then ANSI escape sequences will look like <kbd>ESC</kbd>`[31m`, and will take up space in the view; when control
character are not shown (or when **Show All Characters** is toggled off), then the entire escape sequence will be
hidden.  (This is different than in other lexers, where turning off the control character visibility would just hide the
 `ESC` character, but not the rest of the ANSI escape sequence.)
 
In v8.8.1, this defaulted to applying the ErrorList lexer to files ending in `.err` or `.log`; in v8.8.2, this was changed 
to be just for `.err` (since there are so many different types of `.log` files).  However, if you installed from v8.8.1 and 
updated to v8.8.2 or newer, the `.log` will _not_ be taken out of your default list of extensions; to fix that, you can edit 
`%AppData%\Notepad++\langs.xml` (or appropriate path depending on your [config file location](../config-files/#configuration-files-location)), 
search for `"errorlist"`, and remove `log` from the `ext="err log"` to become `ext="err"`, then save `langs.xml` and restart
Notepad++ (paying attention to the [editing configuration files](../config-files/#editing-configuration-files) instructions).
If you had installed Notepad++ before v8.8.1, and want access to the ErrorList lexer, you will need to see [Configuration Files
During Upgrades](../config-files/#configuration-files-during-upgrades).

#### MS-DOS Style

The **Language > M > MS-DOS Style**, which shows up in the [Style Configurator](../preferences/#style-configurator)
as **Language: `DOS Style`** and uses `*.nfo` as the default file extension, is intended for ASCII art.  
This Language assumes that the file will be using the old DOS box-drawing characters and similar, so defaults to 
OEM-US [encoding](../preferences/#encoding-menu).  It also changes the line spacing to help the characters properly meet, 
and hardcodes the Lucida Console font to make sure that they are presented correctly.
In older versions of the application, that font could not be changed (the 
**Style Configurator > Language: `DOS Style` > Style: `DEFAULT` > Font name: ___** is disabled); 
however, starting in v8.8.4, you can _manually_ edit the `stylers.xml` or your selected theme's XML if you add the `fontName` field to the XML:

1. Following the advice on [Editing Configuration Files](../config-files/#editing-configuration-files), edit `%AppData%\Notepad++\stylers.xml`
   or your theme's XML (paying attention to your setup's [Configuration Files Location](../config-files/#configuration-files-location)).
2. Go to the `<LexerType ...` entry with `name="nfo"` (easiest is to just search `name="nfo"`).
3. On the `<WordsStyle name="DEFAULT" ... />` line inside that tag, add the `fontName="xyz"` (where `xyz` is the name of your font).
    - If you don't remember the exact name of your font, just add `fontName=""` .
4. Save the file, exit Notepad++, and restart Notepad++
5. Now MS-DOS Style `*.nfo` files will use the `xyz` font.
    - Once you've set `fontName="xyz"` or `fontName=""` and restarted, the 
	  **Style Configurator > Language: `DOS Style` > Style: `DEFAULT` > Font name: ___** chooser will be enabled, and will 
	  allow you to change the font name from the GUI, so you can set it back to Lucida Console, or, if you didn't know your 
	  exact font name, you could choose the actual font name from the GUI rather than typing it from memory.

### Themes and Language Support

There are times when a particular Theme will not have been updated to include syntax highlighting for a given Language.
If a Language you need is missing in your chosen Theme, you can open `%AppData%\Notepad++\stylers.xml` (if you use the
default theme) or the appropriate `%AppData%\Notepad++\themes\______.xml` file for your Theme,
plus the `C:\Program Files\Notepad++\stylers.model.xml` (the locations of both those file can vary depending on your active
[Config Files Location](../config-files/#configuration-files-location) for `themes\______.xml`, and your `notepad++.exe` executable's
directory for the `stylers.model.xml`, if you are not using a default installation).  Search in `stylers.model.xml` for the
`<LexerType...>` section for the missing Language, and copy that over to the appropriate location in your `themes\______.xml`.
Close Notepad++ completely and re-run it: that Language should now be in the [Style Configurator](../preferences/#style-configurator)
for your active theme, though depending on how different your Theme's color scheme is compared to the Default Theme, the colors
may be jarring compared to your Theme's background color; but once it's in the Style Configurator, you may update the color scheme for
that Language in the Style Configurator. (If your Theme is a dark Theme, it might be better to copy from `themes\DarkModeDefault.xml`
instead of copying from `stylers.model.xml`.)

Similarly, the Style Configurator lists Default Keyword Lists for the styles of some languages: those are defined in `%AppData%\Notepad++\langs.xml`, and the defaults are in `C:\Program Files\Notepad++\langs.model.xml`.  If `langs.model.xml` has been updated, then you can copy the updated or added keyword lists from there into your `langs.xml`.

### Contribution: Enable Lexilla Lexer That Is Not Active In Notepad++

The [Lexilla library](https://github.com/ScintillaOrg/lexilla/) which Notepad++ uses for syntax highlighting has many languages available to it that Notepad++ doesn't yet provide in the **Language** menu and Style Configurator.  In general, just creating an [issue](https://github.com/notepad-plus-plus/notepad-plus-plus/issues) to request a language be enabled is not sufficient to get it added, because the developers don't have sufficient knowledge of all Lexilla-enabled languages to know if the addition was successful or not; you should put in the request if there's a language in Lexilla that you would like added to Notepad++, but, if possible, you could also put in the Pull Request.  (While it's not sufficient, creating the issue _is_ a [necessary first step](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/CONTRIBUTING.md), because the developer generally does not merge Pull Requests that aren't attached to an existing open issue.)

Creating a PR yourself to enable a not-yet-active lexer should only be attempted if you are familiar with the GitHub environment and the git system of version control, and are comfortable developing in C++.  If this is something that you are ready to do, the following are all pieces of the codebase that need to be updated in order to activate a currently-inactive lexer. For this description, "Xyz Pdq" will be the placeholder name of your language; you, of course, need to use your own language's name instead of the placeholder.

- `PowerEditor/src/MISC/PluginsManager/Notepad_plus_msgs.h`:
    - Need to add an `L_XYZPDQ` constant for your language to the end of the `enum LangType`
    - Insert it between the last real language in the list and `L_EXTERNAL`; **never** insert it before an already-existing language, as the position in the list gives it an integer that is used throughout the codebase and config files.
- `PowerEditor/src/menuCmdID.h`:
    - Add `#define IDM_LANG_XYZPDQ` between the last existing language and `IDM_LANG_EXTERNAL`, using the next integer for the value (the `L_XYZPDQ` from the enum should be in that same integer slot in the enum)
- `PowerEditor/src/ScintillaComponent/ScintillaEditView.h`
    - declare `setXyzPdqLexer()`
    - if it's a simple lexer, which just needs to define one or more keyword lists, you can define it here instead of in the `.cpp` below, just calling `setLexer(L_XYZPDQ, LIST_0 | LIST_1 | ...);`, similar to what was done for `setHollywoodLexer()`
    - An aside on the keyword lists: The `lexilla/Lexers/LexXyzPdq.cxx` will contain one or more `WordList` variables; usually in `LexerXyzPdq::WordListSet()`, you will see a mapping between the word list index and th `WordList` variable.  That index corresponds to the `LIST_#` constant used when calling `setLexer()`.
- `PowerEditor/src/ScintillaComponent/ScintillaEditView.cpp`
    - add the language to `LanguageNameInfo ScintillaEditView::_langNameInfoArray[]`, just before the `L_EXTERNAL` entry.  The table below describes that value that needs to go in each column of that data structure.

        | Column       | Example        | Description |
        |--------------|----------------|-------------|
        | `_langName`  | `xyzpdq`       | Unique string to identify the language.  Will be used as the `<Language name="xyzpdq" ... />` attribute in `langs.xml` |
        | `_shortName` | `Xyz Pdq`      | This is the text that appears in the **Languages** menu |
        | `_longName`  | `Xyz Pdq file` | This is the text that appears in the **Status Bar**'s file type field |
        | `_langID`    | `L_XYZPDQ`     | This is the `L_XYZPDQ` entry you added to the enum |
        | `_lexerID`   | `xyzpdq`       | This is the name of the lexer, as defined in the `lexilla/Lexers/LexXyzPdq.cxx`, in the `LexerModule` instantiation |

    - add your language to the big `switch` block in `ScintillaEditView::defineDocType()`; it should call `setXyzPdqLexer(); break`
    - add in the definition for your `setXyzPdqLexer()`
        - If it's just calling `setLexer()`, you can actually define it in the `.h`, as described above.
        - If it requires complicated logic, define it here, instead.
        - If the lexer includes SubStyle keyword capability, you can either initialize them in the optional end arguments of the `setLexer()` call (see `setLuaLexer()` and `setPythonLexer()` in the `.h` for examples of how to use those optional arguments), or your more-complicated definitions may call `populateSubStyleKeywords()` themselves, like `ScintillaEditView::setTypeScriptLexer()` does)
            - if you are unsure whether your language has substyles, just search the `lexilla/Lexers/LexXyzPdq.cxx` for the word `SubStyle`; with some digging in the code, you should be able to determine which Style the SubStyles get attached to, as well.
- `PowerEditor/src/Notepad_plus.cpp`:
    - in the switch in `Notepad_plus::menuID2LangType()`, add
        ```
        case IDM_LANG_XYZPDQ:
            return L_XYZPDQ;
        ```
- `PowerEditor/src/Parameters.cpp`:
    - in the switch in `NppParameters::langTypeToCommandID()`, add
        ```
        case L_XYZPDQ:
            id = IDM_LANG_XYZPDQ; break;
        ```
- `PowerEditor/src/Notepad_plus.rc`:
    - add a `MENUITEM` in the alphabetically correct place in both the `&Language` big-list, and the `&Language`/`POPUP "X"` per-letter version.
- `PowerEditor/src/NppCommands.cpp`:
    - `Notepad_plus::command()` has a huge switch; add `case IDM_LANG_XYZPDQ:` to the big list of similar `case IDM_LANG_...` entries

And add in config files:
- `PowerEditor/src/langs.model.xml`: add in your `<Language name="xyzpdq"...>` entry with its `<Keywords ...>` entries
    - the `name="instre1"` is the keyword list for `LIST_0`, `instre2` for `LIST_1`, and `type1`-`type7` are `LIST_2`-`LIST_8`; `substyle1`-`substyle8` are for the eight substyles that Notepad++ allows (if the lexer has enabled substyles, of course).
- `PowerEditor/src/stylers.model.xml` and all of the `PowerEditor/installer/themes/*.xml`: add in your `<LexerType name="xyzpdq"...>` with its `<WordsStyles>` entries
    - `lexilla/include/SciLexer.h` has `#define` for `#define SCI_XYZPDQ_* N` values; you will need to make sure you have a `<WordsStyle ... styleID="N" ...>` for each of those styles.

You should also include [autoCompletion](../auto-completion/) definition and [functionList](../function-list/) definition if you have them (they are optional, but highly recommended).  If you submit a functionList, please remember to also create the [unit tests](../function-list/#contribute-your-new-or-enhanced-parser-rule-to-the-notepad-codebase) required to accompany new functionList parsers.

Once you have thoroughly tested your code updates, and verified that it can properly syntax-highlight the newly-enabled language, then you can submit your PR to the [repository](https://github.com/notepad-plus-plus/notepad-plus-plus/) and link it to the issue that you had already created.

## Language Detection Priority

When opening an existing file, Notepad++ has an algorithm for trying to decide which language a given file is, with the following priorities:

1. A language defined at the [command line using `-l`](../command-prompt/) is applied.
2. If the file is in the active [session file](../session/) (the automatic `session.xml` or a manually-controlled session), it will use the language stored in that session.
3. If the file extension is a "known extension" (whether it's from the [Style Configurator](../preferences/#style-configurator)'s default extension list [in `langs.xml` or `langs.model.xml`] or user-defined extension list [from `stylers.xml` or `themes\<ThemeName>.xml`] for a built-in language, or the [User Defined Language](../user-defined-language-system/)'s extension settings [from `userDefineLang.xml` or `userDefineLangs\<UDLName>.xml`]), Notepad++ will use that language.
4. If the filename matches one of a few specific names, Notepad++ knows what language they should be:

    filename | language
    ---|---
    `makefile` | Makefile
    `GNUMakefile` | Makefile
    `CMakeLists.txt` | CMake
    `SConstruct` | Python
    `SConscript` | Python
    `wscript` | Python
    `Rakefile` | Ruby
    `Vagrantfile` | Ruby
    `crontab` | Shell Script
5. If the first line in the file gives a known hint as to the file type, it will use that.  This includes "prolog lines" starting with `<?xml` or `<?php` or `<html` or `<!DOCTPE html` or `<?`, or linux-style "shebang" lines like `#!/usr/bin/bash` which are looking for `sh` or `python` or `perl` or `php` or `ruby` or `node` to define the correct language.
6. It will use the default language only if none of the other rules have matched[.](# "There was a bug through v8.4.6 that made the default language apply on files without extensions, even if the first-line rule had already matched")

As Notepad++ goes through that list in order, it will stop as soon as it finds a matching language for the file.  And after Notepad++ has made its detection, you can override what it chose by using the **Language** menu (and when a session gets saved, the language will remember whatever language is currently active for that file for next time, as described in priority 2).

If you do a **Save As** on a file, it will use that same sequence for deciding the language, based on the new name and file contents.

Newly-created documents will assume the default language until they are saved.
