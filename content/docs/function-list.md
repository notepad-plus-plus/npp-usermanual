---
title: Function List
weight: 80
---

## What is Function List
Function List Panel is a zone to display all the functions (or method) found in the current file. The user can use the Function List Panel to access a function definition quickly by double clicking function item on the list. Function List can be customized to list the functions for whichever language. For customizing Function List to recognize your favorite language, please check below.


Function list contains a search engine (by using regular expression) and a panel to display the search result (function list). It is designed to be as generic as possible, and allows user to modify the way to search, or to add new parser for any programming language.
In order to make function list work for your language (if not supported), you should modify `functionList.xml`. It can be found in `%APPDATA%\notepad++\` or in the Notepad++ installed directory if you use zip package.

## How to customize function list
In parser node it contains:

- `id`: uniq ID for this parser
- `displayName`: reserved for future use.
- `comment`: Optional. you can make a regular expression in this attribute in order to identify comment zones. The identified zones will be ignored by search.

There are 3 kinds of parsers: function parser, class parser and mix parser.
Define a function parser if the language has only functions to parse (for example C).
Define a class parser if the language has functions "defined" in a class, but no function defined outside of a class (for example Java).
Define a mix parser if you have function "defined" both inside and ouside of a class in a file (for example C++).

A function parser contains only a function node.
A class parser contains only a classRange node.
A mix parser contains both function and classRange nodes.

### Function parser
In function node it contains:

- `mainExpr`: it's the regex to get the whole string which contains all the informations you need.
- `displayMode`: reserved for future use.
- `functionName`: define a or several regular expression to get the function name from the result of "mainExpr" attribute of "function" node.
    - `nameExpr`: 1..N
        - `expr`: here you define the regular expression to find the function name.

- `className`: define a or several regular expression to get the class name from the result of "mainExpr".
    - `nameExpr`: 1..N
        - `expr`: here you define the regular expression to find the function name.

Both `functionName` and `className` nodes are optional.
If `functionName` and `className` are absent, then the found string by `mainExpr` regular expression will be processed as function name, and the class name won't be used.


The nodes `functionName` and `className` have the same structure, and they have the same parsing behaviour. For example, in the `functionName` node, we got 2 `nameExpr` nodes:
If the function parser find the first result by `mainExpr` attribute, then it will use the first `nameExpr` to search in the first result, if found (the 2nd result), then it will use the 2nd `nameExpr` to search in the 2nd result. If found, then the function name is solved.

### Class parser
In classRange node it contains:

- `mainExr`: the main whole string to serach
- `displayMode`: reserved for future use.
- `openSymbole` & `closeSymbole`: they are optional. if defined, then the parser will determinate the zone of this class. It find first `openSymbole` from the first character of found string by mainExpr attribute. then it determinates the end of class by `closeSymbole` found. The algorithm deals with the several levels of imbrication. for example: `\{\{\{\}\{\}\}\{\}\}`
- `className`: 1 (or more) `nameExpr` node for determinating class name (from the result of `mainExpr` searching).
- `function`: search in the class zone by using `mainExpr` attribute and the `functionName` nodes.

### Mix parser
Mix Parser contains Class parser (`classRange` node) and Function parser (`function` node).
Class parser will be applied firstly to find class zones, then function parser will be applied on non-class zones.

### Link to Language
Once you finish to defined your parser, you can associate it with Notepad++ internal language id (or with file extension), in order to make it works with the language you want. All you need to do is add association node(s) into associationMap node.

In `associationMap`, it contains:

- `association`: 1 or several nodes to make associations between defined parsers and languages.
    - `langID`: Notepad++ internal language ID.
    - `userDefinedLangName`: User Defined Language Name. It makes association between User Defined Language and the parser. If langID is present, this attribute will be ignored.
    - `ext`: File name extesion (should contain `.`). If `langID` or `userDefinedLangName` is present, this attribute will be ignored.
    - `id`: Parser ID.

## Contribute your enhanced functionList.xml

You're welcome to contribute your new or enhanced parser by creating PR on [Notepad++ GitHub page](https://github.com/notepad-plus-plus/notepad-plus-plus). 
The following sections describe how to prepare your PR according the different situations.

### Unit tests

To avoid the regression, running the unit tests before you submit your modification is important. Here are the steps to run unit tests:

1. Make sure you copy your modified functionList.xml into `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\bin\`
2. Open powershell, go to `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\` to run `.\unitTestLauncher.ps1`.
3. Once you see "All tests are passed.", you can submit your PR.

### Unit test file is absent

It could be that you're creating a new language parser for function list, or you're enhancing an existing language parser but the file `unitTest` doesn't exists. In both cases you should:

1. Add the directory with language name in lowercase into `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\`.
2. Add your new test file as `unitTest` into the new added directory.
3. Open `cmd` go to `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\`, run the command `..\..\bin\notepad++.exe -export=functionList -l[langName] .\[langName]\unitTest`
4. A file named `unitTest.result.json` will be generated. Rename it as `unitTest.expected.result`.
5. Run unit tests (check above [Unit tests](#unit-tests) section) to make sure your `functionList.xml` won't cause any regression.

### Unit test file is present

If you're improving an existing parser, and `unitTest` is present, then you should:

1. Run unit tests (check above [Unit tests](#unit-tests) section) to make sure your `functionList.xml` won't cause any regression.
2. Modify the file `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\langName]\unitTest` according your enhancement. Generally, you don't remove content but you add the content in this file.
3. Open `cmd` go to `[YOUR_SOURCES_DIR]\notepad-plus-plus\PowerEditor\Test\FunctionList\`, run the command `..\..\bin\notepad++.exe -export=functionList -l[langName] .\[langName]\unitTest`
4. A file named `unitTest.result.json` will be generated. Remove `unitTest.expected.result` and Rename `unitTest.result.json` to `unitTest.expected.result`.
