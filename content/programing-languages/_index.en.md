---
title: Programming Languages
weight: 10
---

Notepad++ can distinguish between different languages source code can be written in. This is useful to allow certain modifications and visual aids to be applied specifically designed for that language. For example, a language could distinguish certain keywords that have to be differently interpreted, and as such it can be useful to distinguish these keywords using another color or font. The language also determines the folding behavior (see Folding) and how to handle comments (see Commenting).

Notepad++ offers a lot of languages that can be selected, and has a few methods to add your own as will be discussed.
By default Notepad++ will try to guess the language of a document by the extension of the filename (if it is a file) or the default setting if it is a new document (see Preferences). To select another language, simply select it from the Language menu. The language of the currently active document is visible in the status bar in the first section (see Status Bar). By default a language can have multiple keywords, divided in certain categories. It also determines the symbols used for comments and what extensions are associated with it by default. You can supplement the keywords and the list of extensions using the Styler Configurator, it also allows you to change the colors used to print the text.

If you like to define your own language, you can do so by two means. The most simple and straightforward method is to make user of a User Defined Language (see User Defined Languages), but you can also create your own external lexer (see External Lexers). This is more flexible but also a lot more difficult to make.
