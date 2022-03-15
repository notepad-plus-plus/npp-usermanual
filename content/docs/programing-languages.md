---
title: Programming Languages
weight: 10
---

## Supported Programming Languages

Almost 80 Programming Languages are supported by Notepad++:

|              |                    |                        |               |               |
|--------------|--------------------|------------------------|---------------|---------------|
| ActionScript | Ada                | ASN.1                  | ASP           | Assembly      |
| AutoIt       | AviSynth scripts   | BaanC                  | batch files   | Blitz Basic   |
| C            | C#                 | C++                    | Caml          | CMake         |
| Cobol        | CoffeeScript       | Csound                 | CSS           | D             |
| Diff         | Erlang             | escript                | Forth         | Fortran       |
| FreeBASIC    | Gui4Cli            | Haskell                | HTML          | INI files     |
| Intel HEX    | Inno Setup scripts | Java                   | JavaScript    | JSON          |
| JSP          | KiXtart            | LaTeX                  | LISP          | Lua           |
| Makefile     | Matlab             | MMIX                   | Nim           | nnCron        |
| NSIS scripts | Objective-C        | OScript                | Pascal        | Perl          |
| PHP          | PostScript         | PowerShell             | PureBasic     | Python        |
| R            | Rebol              | Registry script (.reg) | Resource file | Ruby          |
| Rust         | Scheme             | Shell script           | Smalltalk     | SPICE         |
| SQL          | Swift              | S-Record               | Tcl           | Tektronix HEX |
| TeX          | txt2tags           | Visual Basic           | Visual Prolog | VHDL          |
| Verilog      | XML                | YAML                   |               |               |


For these languages, Notepad++ supports [syntax highlighting](../preferences/#style-configurator) (customizable),
syntax folding, [auto-completion](../auto-completion/) (customizable),
[function list](../function-list/) (customizable via PCRE in xml file).

If your beloved language is not in the list above, you can define it yourself easily, by using the 
[User Defined Languages System](../user-defined-language-system/).  If that doesn't meet your needs, 
you could write (or have someone else write) a [lexer plugin](../plugins/#building-a-lexer-plugin).

Please note that in Notepad++ v8.3 and newer, Notepad++ will no longer perform syntax highlighting 
\on files that are over 200MB -- this prevents extreme performance slowdown caused by trying to 
syntax highlight extremely large files.
