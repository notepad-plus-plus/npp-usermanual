---
title: Function List
weight: 80
---

## What is Function List
The Function List Panel is a zone to display all the functions (or methods) found in the current file. The user can double-click the function name in the Function List Panel to move to that function in the editor. You can customize the Function List to enhance an existing language or to add a currently-unsupported language by following the instructions found below.

Function List uses a regular-expression (regex) search engine to parse the active file and look for functions (or methods); it displays the results from the regular-expression search in the Function List panel.  It is designed to be as generic as possible, and allows user to modify the way to search, or to add new parser for any programming language.  

In order to make Function List work for your language (if not supported), you should modify (or add) the xml file of the languge. The XML files for different languages can be found in `%APPDATA%\notepad++\functionList` or in the `functionList` folder located in Notepad++ installation directory if you use the portable (zip) package.

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

* The parser does not accept **regular expresion look behind operations** in the expressions.
* The parser can only search for function names, it will not do **regular expression replacement or modification** (so you cannot add text to the matching names)
* You _may_ use the `(?x)` modifier to allow additional whitespace and `#`-prefixed comments in your regular expression

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

### Test your parser
Once you finish defining your parser, save and name the file as the language name with `xml` as file extension in `functionList` folder in order to make it works with the language you want. Check [overrideMap.xml](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/functionList/overrideMap.xml) for the naming list of all supported programming languages.

If you're not happy about the existing parser rule, you can write your parser rule then save with a unique filename (like `my_languagename.xml`).  (_Note_: if you edit the existing `languagename.xml`, the next update may erase your changes.)  Use your [overrideMap.xml](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/functionList/overrideMap.xml) in the functionList directory to override the default mapping of functionList parser rule files, or to add a mapping to new UDL parser rule files.

## Contribute your new or enhanced parser rule

You're welcome to contribute your new or enhanced parser by creating PR on [Notepad++ GitHub page](https://github.com/notepad-plus-plus/notepad-plus-plus). 
The following sections describe how to prepare your PR according the different situations.

### Unit tests

To avoid the regression, running the unit tests before you submit your modification is important. Here are the steps to run unit tests:

1. Make sure you copy your modified parser rule (xml file) into `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\bin\functionList\`
2. Open PowerShell, go to `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\` to run `.\unitTestLauncher.ps1`.
3. Once you see "All tests are passed.", you can submit your PR.

### Unit test file is absent

It could be that you're creating a new language parser for function list, or you're enhancing an existing language parser but the file `unitTest` doesn't exists. In both cases you should:

1. Add the directory with language name in lowercase into `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\`.
2. Add your new test file as `unitTest` into the new added directory.
3. Open `cmd` go to `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\`, run the command `..\..\bin\notepad++.exe -export=functionList -l[langName] .\[langName]\unitTest`
4. A file named `unitTest.result.json` will be generated. Rename it as `unitTest.expected.result`.
5. Run unit tests (check above [Unit tests](#unit-tests) section) to make sure your parser rule (xml file) won't cause any regression.

### Unit test file is present

If you're improving an existing parser, and `unitTest` is present, then you should **modify the existing unitTest file** or **add a new unitTest file**. If your modification of parser is for covering few more cases, then you can add these case into the existing unitTest file. Otherwise if the modification is for covering the other categories and you have to add a lot of functions to test, you can just leave the current unitTest file as it is, and add your new unitTest file. 

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

