---
title: Auto-completion
weight: 70
---

## What is Auto-completion

Notepad++ offers automatic completion of various sorts of text after you have entered an initial substring (or prefix), which can save you having to type all of a long word (and potentially save you mistyping it). For instance, if you're coding in JavaScript and type `syn`, Notepad++ can present `synchronized` (a JavaScript keyword) as a suggestion. You accept the suggestion by typing the completion key (see "[Automatic completion](#automatic-completion)", below), and the word is completed within your buffer as if you'd typed it all out. If the suggested word is not what you want, keep typing.

If more than one word in the list of candidate words matches what you've typed, Notepad++ will present a list containing the words; the highlighted word in the list is the one that will be selected on the completion key, but you can use the Down- & Up-arrow keys, or PageDown & PageUp, to move through the list; or, type Esc to dismiss the list.

There are three sets of candidate words that Notepad++ uses to create suggestions; these are referred to as "words", "functions" and "system paths".

## Function completion

"Functions" are pre-defined and loaded along with the lexer that corresponds to the computer language of the file. (The lexer defines the syntax coloring; the auto-completion file specifies the names of the functions.) Typically these function words include language keywords (which technically are not functions) such as `switch` in C and similar languages or `lambda` in Python, and some set of standard library function names such as `assert` or `fdopen` in C.

These function lists are stored in auto-completion definition files, each named according to its language. (The words in these files do not necessarily include all the keywords listed in the lexer definitions.) These files can specify which of the words are keywords and which are functions; functions support an additional completion feature, "parameter hint."  Both the functions and keywords from this file are considered "Function completion" throughout this documentation.

### Parameter hints

The auto-complete definition file can specify if a keyword is a function. When a function name has been typed in, followed by the opening parenthesis used to enclose the function's arguments, Notepad++ will automatically, or manually, display a hint (a.k.a. a "call tip"): a small tooltip-style box opens with text containing a description of the function. While the actual text shown is up to the author of the definition file, typically this would show, at minimum, a keyword for each of the parameters taken by the function call. This may save you a trip to the function's documentation to remember what those parameters are.

Notepad++ will display the hint automatically when the open-parenthesis is typed, if that option is selected in the Auto-Completion settings. The user can also select the "Function parameters hint" from the menu or by keystroke (default: `Ctrl+Shift+Space`), when the cursor is between the opening and closing parentheses of the function call. And again, the hint can be dismissed with Esc.

## Word completion

"Words" are taken from the current file—everywhere in the current file, comments and code. Any word two or more characters long is added to the list. This includes numbers, but numbers with decimal points are split into two different "words."

## Path completion

Different from function and word completion which can be triggered automatically after 1 (or X) keystroke(s), Path completion needs to be triggered manually, by using shortcut (default: `Ctrl+Alt+Space`) or via menu command **Edit > Auto-Completion > Path Completion** after typing the drive (for example "C:"). If the string on the left of cursor is not part of one of the system paths, the path list won't appear.

## How to make it work

### Automatic completion

The completion list can be triggered automatically as you type, via settings in [**Settings > Preferences > Auto-Completion**](../preferences/#auto-completion): Auto-Completion is enabled by a checkbox. Additionally there is a setting **From X th character**, accepting a the minimum length of a prefix needed before the completion list is shown (some people like 2, some 3, some 4...); and, there is a setting to specify which candidates should be used: words, functions, or both.

With auto-completion enabled, after typing a prefix of at least the minimum length, a list is presented with all the available words from the selected list(s) that match what's been typed. (If none match, no list is shown.) The list may be a single entry long, or it may contain multiple items which require navigation, but either way you can select the match and, it is hoped, save yourself some typing.  You can use arrow keys (or the mouse) to navigate through the entries in the popup; hitting the completion key or double-clicking on the choice will select that choice and enter it as if you had just typed the whole word; hitting the `Esc` key will exit the auto-completion popup _without_ choosing one of the suggestions.

If instead of selecting, you keep typing, items that no longer match will be removed from the list, and it will disappear entirely once you've typed a string that matches none of the selections. (Note that if you dismiss the list with Esc, and then keep typing, and what you type continues to match wordlist entries, then the list will reappear.)

#### Completion key

In v8.2 and earlier, both the `Tab` and `Enter` keys would be accepted as the completion key, without a configuration option to affect it.  For v8.2.1 through v8.3, the default active completion key is `Tab`, though you can use [preferences](../preferences/#auto-completion) to set whether `Tab` is active, `Enter` is active, or both are active as completion key.  Subsequent versions (v8.3.1 and newer) have both completion keys active by default, but the [preferences](../preferences/#auto-completion) will still allow the user to select which completion key(s) to have active.  (_Note_: as with other [configuration file settings](../config-files/), upgrades will **not** overwrite a setting in an existing config.xml, so your choices made or saved in v8.2.1 through v8.3.0 will remain active through future upgrades; the defaults listed will only apply on new installations, or if there is no setting for `insertSelectedItemUseENTER` or `insertSelectedItemUseTAB` in the config.xml, or if the config.xml file has been deleted or otherwise doesn't exist and needs to be regenerated.)

### Manual completion

If auto completion is turned off, you can manually force the completion of what you've typed, limiting the selection to either the list of functions or the list of words. By default, these functions are bound to `Ctrl+Space` (functions) or `Ctrl+Enter` (words); they are also available in the [Edit menu](../editing/#edit-menu). Typing one of these keystrokes or using those menu commands attempts an immediate completion: if there is a single matching entry in the wordlist, that entry is used, with no display of a list. If there are multiple matching entries, the list is displayed just as if auto-completion were triggered at the same point.

Note: Manual "Function completion" (currently) shows a list of all the functions in the wordlist, even if they don't match the current prefix—unless no function matches the prefix, in which case no list is shown. Manual "Word completion" shows only the matching words.

### Auto-insertion

Some characters traditionally work in pairs, so that it makes sense to ask an editor to type them in pairs when an opening bracket is being typed - the extra closing brace being disposable.

Through [**Settings > Preferences > Auto-Completion**](../preferences/#auto-completion), the **Auto-Insert** options allow selection of any or all of five predefined characters—parenthesis, bracket, brace, double-quote and single quote (apostrophe)—to be automatically matched. Not only that, three custom pairs of characters may be specified. For instance, you might use Unicode open- and close- double quotes; with this feature, you can have both characters inserted when you type the opening quote mark. (Only single characters are allowed in these fields.)

In each case, when the opening character is typed, the closing character will automatically be inserted, with the cursor placed between the two.

Additionally, Auto-Insert supports automatic HTML & XML tag closure. With this enabled, when editing HTML or XML files, after you type an opening tag, such as `<div>`, the program will automatically match it with the closing `</div>`, with the cursor placed between the two tags so that content can be added. Matching will work even if attributes are entered while typing the opening tag. And if the opening tag is terminated with a slash (`/`) —such as `<hr/>` —then no matching tag is inserted. (In the case of `<hr>` entered without a slash, a matching close tag will still be inserted, even if unnecessary, for both HTML and XML editing. Consider this a push towards XML correctness in your HTML code.)

### Displayed Completion List

When you use [Manual Completion](#manual-completion), the list will only show the items that were manually triggered -- so either only the word list or only the function list.  If [Automatic completion](#automatic-completion) is triggered, the list will show both words and functions that match.  As of v8.3.1, the completion list will use the <i>fx</i> icon to help the user tell the difference between the "[Function completion](#function-completion)" items (keywords and functions from the configuration file will get the <i>fx</i> icon) and "[Word completion](#word-completion)" items (words from the active document will _not_ have the icon).

## Auto-completion Settings

The main auto-completion settings are found at [**Settings > Preferences > Auto-Completion**](../preferences/#auto-completion).

The keyboard shortcuts for manual completion can be adjusted in [**Settings > Shortcut Mapper**](../preferences/#shortcut-mapper), in the **Main menu** tab, in the **Category** = **Edit**; you can filter on `completion` to easily find them.

## Create auto-completion definition files

Notepad++ uses XML configuration files to define the per-language function and parameter auto-completion.  Those AutoComplete files are located in the `autoCompletion` subdirectory of the Notepad++ install folder.  (In older versions, Notepad++ v7.6.1 and earlier, they were found in the `plugins\APIs` subdirectory of the intstall folder.)

The syntax of AutoComplete files is simple, but does have a few rules, most importantly correct syntax and proper sorting. If the syntax is incorrect, the XML file will fail to load and AutoComplete will be disabled.

Improper sorting (see below) can cause the AutoComplete function to behave erratic, causing it to fail on certain words.

The basic character set used to recognize keywords is made of letters `a-z`, `A-Z`, digits `0-9`, and the underscore `_`.  Punctuation might work for auto-completion; however, if you want to use the parameter hints, you should not use punctuation in the keyword name.

Syntax:

    <?xml version="1.0" encoding="Windows-1252" ?>
    <NotepadPlus>
       <AutoComplete language="C++">
           <Environment ignoreCase="no" startFunc="(" stopFunc=")" paramSeparator="," terminal=";" additionalWordChar = "."/>
           <KeyWord name="abs" func="yes">
               <Overload retVal="int" descr="Returns absolute value of given integer">
                   <Param name="int number" />
               </Overload>
           </KeyWord>
       </AutoComplete>
    </NotepadPlus>

A small example of how the XML file is built is given above. `<NotepadPlus>`, `<AutoComplete>` and `<Environment>` elements are singleton elements: there should be only one of each, and all of them should be present for correctness, although it is allowed to remove the `<Environment>` element. Doing so will default all values to the ones given in the above example.

For keywords that are not functions, the `<KeyWord>` tag is autoclosing and only has the `name` attribute. To indicate a keyword can be displayed in a calltip, add the attribute `func="yes"`. In this case, the `<KeyWord>` tag is a node and contains other tags.

Then, for each overload of the function, an `<Overload>` element should be added, which specifies the behavior and the parameters of the function. A function must have at least one `<Overload>` or it will not be displayed as a calltip.  Multiple `<Overload>` elements allow there to be different sets of parameters for a given function.  The `retVal` attribute must be present and specifies the type of the return value, but the `descr` attribute is optional and describes the functions behavior, like a comment. You can add newlines in the description if you wish to do so. For each parameter the function takes, a `<Param>` element can be added. The `name` attribute must be present and specifies the type of the parameters and/or any name of the parameter.

In the `<AutoComplete>` element you can add the `language` attribute, but it is not used by Notepad++; you can add it for completeness if you wish and can take any string you want.

### Auto-completion File Format

<!-- in the old NppWiki++, this was a section of the "Editing Configuration Files" page, but I [pryrt] don't see an equivalent page in the new npp-usermanual, so I'm putting it here for now -->

Auto-complete files files are located in the `autoCompletion\` subfolder of the Notepad++ installation folder (unlike some config files, these will _not_ work in the `%AppData%\Notepad++\` hierarchy). These files are optional: you need only one for each language for which you'll use Auto Completion or calltips. They are also supported for User Defined Languages, and bear the name `<Language name>.xml`.

Note: Create a `normal.xml` AutoComplete file for adding custom suggestions to the default language, Normal Text \[i.e., language set to "None (Normal Text)"\].

Under the usual `<NotepadPlus>` tag is a `<AutoComplete>` tag. It has an optional, unused `language` attribute, which you can use for any descriptive purpose.

The contents of a `<AutoComplete>` start with an autoclosing `<Environment>` tag, with the following attributes:

1. `ignoreCase`: `"no"` if the language is case sensitive, else `"yes"` (default).
2. `startFunc`: the character(s) which start the parameter list. Default is `"("`.
3. `stopFunc`: the character(s) which end the parameter list. Default is `")"`.
4. `paramSeparator`: the character(s) which separate parameters. Defaults to `","`.
5. `terminal`: the character(s) which mark the end of a prototype, when the language allows C-style separate prototyping. Defaults to `";"`. Leave it out if the language does not support separate prototyping, or set it to some illegal character.
6. `additionalWordChar`: character(s) that may be part of words and which are not a lower or upper case letter, a digit or the underscore. The value is a string with all these extra characters, in any order and without separators. The string is empty by default.

NOTE: Spaces can't be used as the character for the attributes.

Any attribute can be omitted, and the `<Environment>` tag as well. The practice is not recommended though.

Following is a list of `<KeyWord>` tags. They are either auto-closing, for keywords that are not routines, or not when they are. Each such tag has a mandatory `name` attribute, the keyword/routine name to recognise. The list **must be sorted according to this attribute and the value of the `<Environment>` ignoreCase attribute**. See subsections below for more on keyword names and sorting.

When a `<KeyWord>` tag is not auto-closing, it must have a second attribute, `func="yes"`. The contents are a nonempty, unsorted list of `<Overload>` tags, each of which describes a possible signature for the routine. `<Overload>` has a `retVal` attribute, which you would set to the initial comment in the call tip. In C/C++, this traditionally would be the return type; `""` is a permitted value. Furthermore, the `<Overload>` tag has an optional `descr` attribute, which can be used to add a description of the function. Tip: You can use `&#x0a;` to insert line breaks.

An `<Overload>` tag contains one or more parameter description, sorted in occurrence order. Such description is represented by an auto-closing `<Param>` tag with a "name" attribute. This may contain a parameter name or other useful comments.

The parameter names (actually any text you like, it may even mention a parameter name), return value and description have to fit into an internal buffer, truncation occurs otherwise. For any given function, all text, plus 2 bytes per parameter, plus 24 bytes if 2 overloads or more, can't spill over 2,043 bytes. Remember that a byte is a byte, so formatting whitespace competes with actual text.

A typical example of entry could be this:

    <KeyWord name="cos" func="yes" >
       <Overload retVal="{double}" descr="Cosine of x" >
           <Param name="x, radians" />
       </Overload>
    </KeyWord>

resulting in the following call tip:

    {double} cos (x, radians)
    Cosine of x

Remember that the call tip shows up when you type the opening parenthesis after the routine name. Default `"("` or whatever set with startFunc in the `<Environment>` tag.

#### Names
For both call tips and autocompletion to work, keywords must be words, ie identifiers most languages would readily accept. This means that only the 26 Latin alphabet letters in either lower or upper case (no diacritics), digits and the underscore are safe to use. Additional allowed characters will work if they are not whitespace. Autocompletion may cope with spaces or blanks, call tips won't. This is a Scintilla limitation.

#### Sorting

The `<KeyWord>` tag list must be sorted by `name` in ascending order. **Failure to do so will result in a non working file, without a warning.**

Now which sorting, case sensitive or insensitive? It depends on the value of the ignoreCase `<Environment>` attribute. If set to `"yes"`, use case insensitive sorting, which considers all letters to be in upper case. Otherwise, use case sensitive sorting.

The simplest way to build a new file might be this:

1. in a new document, list all keywords to be recognised;
2. sort the list with the right ordering;
3. Using the Column Editor, add `<KeyWord name="` in front of each line.
4. Using extended mode search-and-replace, add `"/>` at the end of all lines.
5. Add some fancy character (`+` is a good candidate) to the end of lines that represent functions;
6. Using extended mode, replace `/>+\r\n` by `>\r\n\t<Overload retVal="">\r\n\t</Overload>\r\n</KeyWord>\r\n`
7. Now manually add text and extra overloads. Re-indent as applicable;
8. Save and test your file;
9. Sloppy work, test again (recursive, beware of infinite loops).

For case sensitive sorting, you can use Notepad++'s **Edit > Line Operations > Sort Lexicographically Ascending**, or any generic ASCII/ANSI sorter that sorts on the byte value of the characters. Simply put, this means the underscore character is between uppercase and lowercase letters.

For case insensitive sorting, treat lowercase letters as uppercase, that is, subtract 32 from each lowercase byte value; this means the underscore must come both after uppercase and lowercase letters.  Unfortunately, Notepad++'s **Edit > Line Operations > Sort Lexicographically Ascending** does case-sensitive sorting, and will not work for this purpose.
