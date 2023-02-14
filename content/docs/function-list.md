---
title: Function List
weight: 80
---

## What is Function List
The Function List Panel is a zone to display all the functions (or methods) found in the current file. The user can double-click the function name in the Function List Panel to move to that function in the editor. You can customize the Function List to enhance an existing language or to add a currently-unsupported language by following the instructions found below.

Function List uses a regular-expression (regex) search engine to parse the active file and look for functions (or methods); it displays the results from the regular-expression search in the Function List panel.  It is designed to be as generic as possible, and allows user to modify the way to search, or to add new parser for any programming language.  

In order to make Function List work for your language, you should modify (or add) the XML file of the languge. The XML files for different languages can be found in `%APPDATA%\notepad++\functionList`; if you use the portable (zip) package, then it will instead be in the `functionList` folder located in Notepad++ installation directory.  The `overrideMap.xml` file (in that same folder as the language XML file) is used to map the name of the language to the XML file that defines the Function List rule for that language, as described in the [function list config files](../config-files/#function-list) section of the manual. 

## How to customize Function List

To customize the Function List, you need to edit the XML file for the language you are defining.  This section describes the structure and requirements for each XML element.

The `<parser>` node accepts the three attributes:

- `id`: Unique ID for this parser.
- `displayName`: Reserved for future use.
- `comment`: Optional. You can make a regular expression in this attribute in order to identify comment zones. The identified zones will be ignored by search, so that it will not find commented-out functions.

There are 3 kinds of parsers: function parser, class parser, and mixed parser.

* Define a function parser if the language has only functions to parse (for example C).
    * A function parser contains only a `<function>` node.
* Define a class parser if the language has functions "defined" in a class, but no function defined outside of a class (for example Java).
    * A class parser contains only a `<classRange>` node.
* Define a mixed parser if you have function "defined" both inside and ouside of a class in a file (for example C++).
    * A mixed parser contains both`<function>` and `<classRange>` nodes.

_Notes on regular expressions for parsers_:

Other than the caveats below, the function list regular expressions follow the same syntax spelled out in the docs on [Searching: Regular Expressions](../searching/#regular-expressions):

- The parser does not accept **regular expresion look behind operations** in the expressions.
- The parser can only search for function names, it will not do **regular expression replacement or modification** (so you cannot add text to the matching names)
- You _may_ use the `(?x)` modifier to allow additional whitespace and `#`-prefixed comments in your regular expression, as described in the docs on [regex search modifiers](../searching/#search-modifiers)

### Function parser
The `<function>` node accepts the following attributes and contained elements:

- `mainExpr` (_attribute_): The regex to get the whole string which contains all the informations you need.
- `displayMode` (_attribute_): Reserved for future use.
- `functionName` (_element_): Define one or more regular expressions to get the function name from the result of "mainExpr" attribute of "function" node.
    - `nameExpr` (_element_): Use one "nameExpr" element for each function-name pattern.  (This allows multiple regex patterns for matching different syntaxes of function definition).
        - `expr` (_attribute_): This is where you define the regular expression to find the function name.
- `className` (_element_): Define one or more regular expressions to get the class name from the result of "mainExpr".  (You _can_ have classes, even if it's not a class parser.)
    - `nameExpr` (_element_): Use one "nameExpr" element for each function-name pattern.
        - `expr` (_attribute_): This is where you define the regular expression to find the class name.

Both `functionName` and `className` nodes are optional.  If `functionName` and `className` are absent, then the string found by the `mainExpr` regular expression will be processed as the function name, and the class name won't be used.

The nodes `functionName` and `className` have the same structure, and they have the same parsing behaviour. For example, if in the `functionName` node, we have two `nameExpr` nodes: If the function parser finds a match using the first `mainExpr` attribute, then it will use that match; otherwise, it will search using the second `nameExpr`, and use that match if found; finally, if none of the `mainExpr` regex match the text, no function will be found.

### Class parser
The `<classRange>` node accepts the following attributes and contained elements:

- `mainExr` (_attribute_): The main whole string to search.
- `displayMode` (_attribute_): Reserved for future use.
- `openSymbole` & `closeSymbole` (_attribute_): They are optional. If defined, then the parser will determine the zone of this class: it find first `openSymbole` from the first character of the string found by "mainExpr" attribute; then it determines the end of class by `closeSymbole` found.  The algorithm deals with the several levels of nesting. For example: `\{\{\{\}\{\}\}\{\}\}`
- `className` (_element_): Contains one or more `nameExpr` nodes for determining class name (from the result of `mainExpr` searching).
- `function` (_element_): Finds functions inside the class zone by using the expressions found in the `mainExpr` attribute and the `functionName` nodes.
    - _Note_: This `function` node looks similar to the `function` node in the **Function parser** above, but it _is different_, and has slightly different contents.
    - `mainExpr` (_attribute_): The regex to get the whole string which contains all the informations you need.
    - `functionName` (_element_): The wrapper for digging into and finding the text for the function name
        - `functionNameExpr` (_element_): The element for the function name of a function inside a class.  Please note that it uses the `functionNameExpr` element instead of the `nameExpr` element in the **Function parser**.  Yes, it's confusing.
            - `expr` (_attribute_): this is where you put the regular expression defines what should match to be used in displaying the function name in the Function List panel.

_Please Note_: an empty class (one without any functions) will _not_ display in the Function List panel.  Thus, if you have no `<function>` elements defined in your `<classRange>` node, you will _never_ see your class.  And if you have a `<function>` defined, but it doesn't match any functions inside your class, the class will not be displayed in the FunctionList panel.  In the FunctionList panel, the class is a container, and it will never display on its own if there is no function to display inside of it. 

### Mixed parser
A mixed parser contains a Class parser (`classRange` node) and a Function parser (`function` node).  The Class parser will be applied first to find class zones, then the Function parser will be applied on non-class zones.

## Manually verify that your parser works for you
Once you finish defining your parser, save and name the file as the language name with `xml` as file extension in `functionList` folder in order to make it works with the language you want. (Check [overrideMap.xml](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/functionList/overrideMap.xml) for the naming list of all supported programming languages.)  Then load a file that uses that parser, and make sure it finds all the functions that you expect, in the appropriate classes.

## Use your own personal function list definition for a built-in language
If you do not like the results of the default Function List parser that ships with Notepad++ for a particular language, feel free to write your parser rule then save with a unique filename (like `my_languagename.xml`).  (_Note_: if you edit the existing `languagename.xml`, the next update may erase your changes.)  Use your [overrideMap.xml](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/functionList/overrideMap.xml) in the functionList directory to override the default mapping of functionList parser rule files, or to add a mapping to new UDL parser rule files, as described in the [function list config files](../config-files/#function-list) section of the manual. 

## Validating Function List defintion files

If you are developing a Function List definition file and would like to be able to validate that you have correct XML syntax while you are doing so, you can see the instructions in the [Notepad++ Community "Validating Config-File XML" FAQ](https://community.notepad-plus-plus.org/topic/24136/faq-desk-validating-config-file-xml).

## Contribute your new or enhanced parser rule to the Notepad++ codebase

If you have added or updated the parser definition file for one of Notepad++'s built-in languages, you are welcome to contribute your file to the Notepad++ codebase by creating "Pull Request" (also called a "PR") on the [Notepad++ GitHub page](https://github.com/notepad-plus-plus/notepad-plus-plus).  (A "Pull Request" is just the GitHub mechanism for requesting that code you write be added to a project.)

**Please Note**: You only need to create a Pull Request if you want your Function List definition to be bundled as part of the Notepad++ codebase going forward, so that everyone who downloads Notepad++ gets your Function List definition.  If you do not need to contribute your Function List definition to everyone, then you do not need to read anything below this paragraph.

- If you created a Function List for your own UDL, you do not need to create a Pull Request using the link above, because user-created UDLs and their Function List definitions are not distributed as part of Notepad++.  You do not need to read any further.

- If you just edited one of the pre-existing Function List definitions for your own personal use, and you don't want to share it with anyone else, you do not need to create a Pull Request using the link above because you are not sharing it with others.  You do not need to read any further.

- This Pull Request can be used to update the Function List for a language that already has a Function List definition, but you just want to make it better for everyone; or it can be for a new definition file for one of the builtin lexer languages that does not yet have a function list definition.  If it does not not meet one of these requirements, you do not need to read any further.

If you still want to believe you should be submitting your Function List parser to the Notepad++ codebase at this point, please follow the steps below to create and verify your Unit Tests and then submit the Pull Request.

### Unit tests

To avoid creating regressions in the Notepad++ codebase, it is important to run the unit tests before you submit your PR.  This procedure is meant for users who are comfortable with the development environment (forking a repository, running unit tests, creating pull requests, and the like), or who are willing to do the research to learn how to do this. If you do not follow these unit test steps, it is likely that your PR will be rejected and your function list definition will not be distributed with Notepad++.  If you do not know how to do this, or cannot do the research on other sites to learn how, then you are not yet ready to submit your Function List definition to be part of the Notepad++ codebase.

Here are the steps to run unit tests:

1. Create or sync your fork of the Notepad++ repository.
2. Make sure you copy your modified function-list parser definition (xml file) into `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\bin\functionList\`.
3. Open PowerShell, go to `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\` to run `.\unitTestLauncher.ps1`.
4. Once you see "All tests are passed.", you can submit your PR.

#### Unit test file is absent

It could be that you're creating a new language parser for function list, or you're enhancing an existing language parser but the file `unitTest` doesn't exists. In both cases you should:

1. Add the directory with language name in lowercase into `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\`.
2. Add your new test file as `unitTest` into the new added directory.
3. Open `cmd` go to `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\`, run the command `..\..\bin\notepad++.exe -export=functionList -l[langName] .\[langName]\unitTest`
4. A file named `unitTest.result.json` will be generated. Rename it as `unitTest.expected.result`.
5. Run unit tests (check above [Unit tests](#unit-tests) section) to make sure your parser rule (xml file) won't cause any regression.

#### Unit test file is present

If you're improving an existing parser, and `unitTest` is present, then you should **modify the existing unitTest file** or **add a new unitTest file**. If your modification of the parser is for covering few more cases, then you can add these case into the existing unitTest file. Otherwise if the modification is for covering the other categories and you have to add a lot of functions to test, you can just leave the current unitTest file as it is, and add your new unitTest file. 

**- Modify the existing unitTest file**

1. Run unit tests (check above [Unit tests](#unit-tests) section) to make sure your parser rule (xml file) won't cause any regression.
2. Modify the file `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\[langName]\unitTest` according your enhancement. Generally, you don't remove content but you add the content in this file.
3. Open `cmd` go to `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\`, run the command `..\..\bin\notepad++.exe -export=functionList -l[langName] .\[langName]\unitTest`
4. A file named `unitTest.result.json` will be generated. Remove `unitTest.expected.result` and Rename `unitTest.result.json` to `unitTest.expected.result`.

**- Add a new unitTest file**

1. Run unit tests (check above [Unit tests](#unit-tests) section) to make sure your parser rule (xml file) won't cause any regression.
2. Add a directory into `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\[langName]\`, the name of directory is arbitrary but should be relevant to the category of the test. Name your unit test file as `unitTest` and copy it into the directory you just created.
3. Open `cmd` go to `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\`, run the command `..\..\bin\notepad++.exe -export=functionList -l[langName] .\[langName]\[yourTestDir2]\unitTest`
4. A file named `unitTest.result.json` will be generated in the created directory `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\[langName]\[yourTestDir2]\`. Rename `unitTest.result.json` in the created directory  to `unitTest.expected.result`.

### Create and Submit your Pull Request

As noted in the ["Contributing" rules for Notepad++](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/CONTRIBUTING.md), "All Pull Requests ... need to be attached to a issue on GitHub."  So the first step is to create an issue which requests that the function list definition be improved (if it was already there) or added (if it was not yet there); in your issue, be sure to explain that you have the Function List definition ready, and will be submitting a Pull Request.  The second step is to use the GitHub interface to create the Pull Request from your fork into the main repository.  The final step is to wait for and respond to feedback from the developers as needed, until such time as your PR is accepted or rejected.
