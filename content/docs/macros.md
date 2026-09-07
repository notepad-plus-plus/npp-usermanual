---
title: Macros - Task Automation
linktitle: Macros
weight: 90
---

Notepad++ is capable of recording some of your actions you perform while editing
a document, and replaying those later on to avoid having to repeat that sequence
of actions. This is called a macro and can save a great deal of time. Macros
can be played once, or multiple times, even as long as is required to run through
an entire document. You can save them for later use and assign keystrokes to
them for fast access (See [Shortcut Mapper](../preferences/#shortcut-mapper)).
Macros are sensitive to the current position of the [caret](../editing/#caret-and-cursor "typing/insertion cursor") and will (normally
speaking) operate relative to it.


## Record a macro

To record a macro, select **Macro > Start Recording** or press the  button on the
toolbar. Notepad++ will now keep track of the changes you make on a document or
certain actions you perform.

To stop recording, select **Macro > Stop Recording** or select the  button on the
toolbar. As an exception to most commands, you can toggle this behavior with a
special shortcut combination that is not listed in the menu but solely in the
Shortcut mapper (see [Shortcut Mapper](../preferences/#shortcut-mapper)).
By default, this is the combination Ctrl-Shift-R.

After the recording is stopped, it will be stored in a temporary buffer. If you
haven't performed any actions during the recording, this buffer will be cleared. If you start
recording another macro without saving your earlier work, it will be lost.

### Macro Recording Limitations

Not all commands are macro recordable.  The following commands or actions should be recordable
(based on investigations in the source code, looking for the menu commands and underlying editor
commands that are in respective lookups for menu-recordable items).

{{< details "show menu items that should be macro-recordable" >}}

Those marked with `+` are macro-recordable; those marked with `-` are not.

| ? | Main Menu Location |
|---|--------------------|
| + | File > New |
| - | File > Open... |
| - | File > Open Containing Folder > Explorer |
| - | File > Open Containing Folder > cmd |
| - | File > Open Containing Folder > PowerShell |
| - | File > Open Containing Folder > Folder as Workspace |
| - | File > Open in Default Viewer |
| - | File > Open Folder as Workspace... |
| + | File > Reload from Disk |
| + | File > Save |
| - | File > Save As... |
| - | File > Save a Copy As... |
| + | File > Save All |
| - | File > Rename... |
| + | File > Close |
| + | File > Close All |
| + | File > Close Multiple Documents > Close All but Active Document |
| + | File > Close Multiple Documents > Close All but Pinned Documents |
| + | File > Close Multiple Documents > Close All to the Left |
| + | File > Close Multiple Documents > Close All to the Right |
| + | File > Close Multiple Documents > Close All Unchanged |
| - | File > Move to Recycle Bin |
| - | File > Load Session... |
| - | File > Save Session... |
| - | File > Print... |
| - | File > Print Now |
| - | File > Exit |
| + | Edit > Undo |
| + | Edit > Redo |
| + | Edit > Cut |
| + | Edit > Copy |
| + | Edit > Paste |
| + | Edit > Delete |
| + | Edit > Select All |
| + | Edit > Begin/End Select |
| + | Edit > Begin/End Select in Column Mode |
| + | Edit > Insert > Date Time (short) |
| + | Edit > Insert > Date Time (long) |
| + | Edit > Insert > Date Time (customized) |
| + | Edit > Copy to Clipboard > Copy Current Full File path |
| + | Edit > Copy to Clipboard > Copy Current Filename |
| + | Edit > Copy to Clipboard > Copy Current Dir. Path |
| + | Edit > Copy to Clipboard > Copy All Filenames |
| + | Edit > Copy to Clipboard > Copy All File Paths |
| + | Edit > Indent > Increase Line Indent |
| + | Edit > Indent > Decrease Line Indent |
| + | Edit > Convert Case to > UPPERCASE |
| + | Edit > Convert Case to > lowercase |
| + | Edit > Convert Case to > Proper Case |
| + | Edit > Convert Case to > Proper Case (blend) |
| + | Edit > Convert Case to > Sentence case |
| + | Edit > Convert Case to > Sentence case (blend) |
| + | Edit > Convert Case to > iNVERT cASE |
| + | Edit > Convert Case to > ranDOm CasE |
| + | Edit > Line Operations > Duplicate Current Line |
| + | Edit > Line Operations > Remove Duplicate Lines |
| + | Edit > Line Operations > Remove Consecutive Duplicate Lines |
| + | Edit > Line Operations > Split Lines |
| + | Edit > Line Operations > Join Lines |
| + | Edit > Line Operations > Move Up Current Line |
| + | Edit > Line Operations > Move Down Current Line |
| + | Edit > Line Operations > Remove Empty Lines |
| + | Edit > Line Operations > Remove Empty Lines (Containing Blank characters) |
| + | Edit > Line Operations > Insert Blank Line Above Current |
| + | Edit > Line Operations > Insert Blank Line Below Current |
| + | Edit > Line Operations > Reverse Line Order |
| + | Edit > Line Operations > Randomize Line Order |
| + | Edit > Line Operations > Sort Lines Lexicographically Ascending |
| + | Edit > Line Operations > Sort Lines Lex. Ascending Ignoring Case |
| + | Edit > Line Operations > Sort Lines In Locale Order Ascending |
| + | Edit > Line Operations > Sort Lines As Integers Ascending |
| + | Edit > Line Operations > Sort Lines As Decimals (Comma) Ascending |
| + | Edit > Line Operations > Sort Lines As Decimals (Dot) Ascending |
| + | Edit > Line Operations > Sort Lines By Length Ascending |
| + | Edit > Line Operations > Sort Lines Lexicographically Descending |
| + | Edit > Line Operations > Sort Lines Lex. Descending Ignoring Case |
| + | Edit > Line Operations > Sort Lines In Locale Order Descending |
| + | Edit > Line Operations > Sort Lines As Integers Descending |
| + | Edit > Line Operations > Sort Lines As Decimals (Comma) Descending |
| + | Edit > Line Operations > Sort Lines As Decimals (Dot) Descending |
| + | Edit > Line Operations > Sort Lines By Length Descending |
| + | Edit > Comment/Uncomment > Toggle Single Line Comment |
| + | Edit > Comment/Uncomment > Single Line Comment |
| + | Edit > Comment/Uncomment > Single Line Uncomment |
| + | Edit > Comment/Uncomment > Block Comment |
| - | Edit > Comment/Uncomment > Block Uncomment |
| - | Edit > Auto-Completion > Function Completion |
| - | Edit > Auto-Completion > Word Completion |
| - | Edit > Auto-Completion > Function Parameters Hint |
| - | Edit > Auto-Completion > Function Parameters Previous Hint |
| - | Edit > Auto-Completion > Function Parameters Next Hint |
| - | Edit > Auto-Completion > Path Completion |
| + | Edit > EOL Conversion > Windows (CR LF) |
| + | Edit > EOL Conversion > Unix (LF) |
| + | Edit > EOL Conversion > Macintosh (CR) |
| + | Edit > Blank Operations > Trim Trailing Space |
| + | Edit > Blank Operations > Trim Leading Space |
| + | Edit > Blank Operations > Trim Leading and Trailing Space |
| + | Edit > Blank Operations > EOL to Space |
| + | Edit > Blank Operations > Trim both and EOL to Space |
| + | Edit > Blank Operations > TAB to Space |
| + | Edit > Blank Operations > Space to TAB (All) |
| + | Edit > Blank Operations > Space to TAB (Leading) |
| - | Edit > Paste Special > Paste HTML Content |
| - | Edit > Paste Special > Paste RTF Content |
| - | Edit > Paste Special > Copy Binary Content |
| - | Edit > Paste Special > Cut Binary Content |
| - | Edit > Paste Special > Paste Binary Content |
| - | Edit > On Selection > Open File |
| - | Edit > On Selection > Open Containing Folder in Explorer |
| + | Edit > On Selection > Redact Selection █ (Shift: ●) |
| - | Edit > On Selection > Search on Internet |
| - | Edit > On Selection > Change Search Engine... |
| - | Edit > Multi-select All > Ignore Case  Whole Word |
| - | Edit > Multi-select All > Match Case Only |
| + | Edit > Multi-select All > Match Whole Word Only |
| + | Edit > Multi-select All > Match Case  Whole Word |
| + | Edit > Multi-select Next > Ignore Case  Whole Word |
| + | Edit > Multi-select Next > Match Case Only |
| + | Edit > Multi-select Next > Match Whole Word Only |
| + | Edit > Multi-select Next > Match Case  Whole Word |
| + | Edit > Undo the Latest Added Multi-Select |
| + | Edit > Skip Current  Go to Next Multi-select |
| - | Edit > Column Mode... |
| - | Edit > Column Editor... |
| - | Edit > Character Panel |
| - | Edit > Clipboard History |
| + | Edit > Read-Only in Notepad++ > Read-Only on Current Document |
| + | Edit > Read-Only in Notepad++ > Read-Only for All Documents |
| + | Edit > Read-Only in Notepad++ > Clear Read-Only for All Documents |
| + | Edit > Read-Only Attribute in Windows |
| - | Search > Find... |
| - | Search > Find in Files... |
| + | Search > Find Next |
| + | Search > Find Previous |
| + | Search > Select and Find Next |
| + | Search > Select and Find Previous |
| + | Search > Find (Volatile) Next |
| + | Search > Find (Volatile) Previous |
| - | Search > Replace... |
| - | Search > Incremental Search |
| - | Search > Search Results Window |
| - | Search > Next Search Result |
| - | Search > Previous Search Result |
| - | Search > Go to... |
| + | Search > Go to Matching Brace |
| + | Search > Select All In-between {} [] or () |
| - | Search > Mark... |
| - | Search > Change History > Go to Next Change |
| - | Search > Change History > Go to Previous Change |
| - | Search > Change History > Clear Change History |
| + | Search > Style All Occurrences of Token > Using 1st Style |
| + | Search > Style All Occurrences of Token > Using 2nd Style |
| + | Search > Style All Occurrences of Token > Using 3rd Style |
| + | Search > Style All Occurrences of Token > Using 4th Style |
| + | Search > Style All Occurrences of Token > Using 5th Style |
| + | Search > Style One Token > Using 1st Style |
| + | Search > Style One Token > Using 2nd Style |
| + | Search > Style One Token > Using 3rd Style |
| + | Search > Style One Token > Using 4th Style |
| + | Search > Style One Token > Using 5th Style |
| + | Search > Clear Style > Clear 1st Style |
| + | Search > Clear Style > Clear 2nd Style |
| + | Search > Clear Style > Clear 3rd Style |
| + | Search > Clear Style > Clear 4th Style |
| + | Search > Clear Style > Clear 5th Style |
| + | Search > Clear Style > Clear all Styles |
| + | Search > Jump Up > 1st Style |
| + | Search > Jump Up > 2nd Style |
| + | Search > Jump Up > 3rd Style |
| + | Search > Jump Up > 4th Style |
| + | Search > Jump Up > 5th Style |
| + | Search > Jump Up > Find Mark Style |
| + | Search > Jump Down > 1st Style |
| + | Search > Jump Down > 2nd Style |
| + | Search > Jump Down > 3rd Style |
| + | Search > Jump Down > 4th Style |
| + | Search > Jump Down > 5th Style |
| + | Search > Jump Down > Find Mark Style |
| + | Search > Copy Styled Text > 1st Style |
| + | Search > Copy Styled Text > 2nd Style |
| + | Search > Copy Styled Text > 3rd Style |
| + | Search > Copy Styled Text > 4th Style |
| + | Search > Copy Styled Text > 5th Style |
| + | Search > Copy Styled Text > All Styles |
| + | Search > Copy Styled Text > Find Mark Style |
| + | Search > Bookmark > Toggle Bookmark |
| + | Search > Bookmark > Next Bookmark |
| + | Search > Bookmark > Previous Bookmark |
| + | Search > Bookmark > Clear All Bookmarks |
| + | Search > Bookmark > Cut Bookmarked Lines |
| + | Search > Bookmark > Copy Bookmarked Lines |
| + | Search > Bookmark > Paste to (Replace) Bookmarked Lines |
| + | Search > Bookmark > Remove Bookmarked Lines |
| + | Search > Bookmark > Remove Non-Bookmarked Lines |
| + | Search > Bookmark > Inverse Bookmarks |
| - | Search > Find characters in range... |
| + | View > Always on Top |
| + | View > Toggle Full Screen Mode |
| - | View > Post-It |
| - | View > Distraction Free Mode |
| + | View > View Current File in > Firefox |
| + | View > View Current File in > Chrome |
| + | View > View Current File in > Edge |
| + | View > View Current File in > IE |
| - | View > Show Symbol > Show Space and Tab |
| - | View > Show Symbol > Show End of Line |
| - | View > Show Symbol > Show Non-Printing Characters |
| - | View > Show Symbol > Show Control Characters  Unicode EOL |
| - | View > Show Symbol > Show All Characters |
| - | View > Show Symbol > Show Indent Guide |
| - | View > Show Symbol > Show Wrap Symbol |
| - | View > Zoom > Zoom In (Ctrl+Mouse Wheel Up) |
| - | View > Zoom > Zoom Out (Ctrl+Mouse Wheel Down) |
| - | View > Zoom > Restore Default Zoom |
| - | View > Zoom > Synchronize Across Views |
| + | View > Move/Clone Current Document > Move to Other View |
| + | View > Move/Clone Current Document > Clone to Other View |
| + | View > Move/Clone Current Document > Move to New Instance |
| + | View > Move/Clone Current Document > Open in New Instance |
| + | View > Tab > 1st Tab |
| + | View > Tab > 2nd Tab |
| + | View > Tab > 3rd Tab |
| + | View > Tab > 4th Tab |
| + | View > Tab > 5th Tab |
| + | View > Tab > 6th Tab |
| + | View > Tab > 7th Tab |
| + | View > Tab > 8th Tab |
| + | View > Tab > 9th Tab |
| - | View > Tab > First Tab |
| - | View > Tab > Last Tab |
| + | View > Tab > Next Tab |
| + | View > Tab > Previous Tab |
| + | View > Tab > Move to Start |
| + | View > Tab > Move to End |
| + | View > Tab > Move Tab Forward |
| + | View > Tab > Move Tab Backward |
| - | View > Tab > Apply Color 1 |
| - | View > Tab > Apply Color 2 |
| - | View > Tab > Apply Color 3 |
| - | View > Tab > Apply Color 4 |
| - | View > Tab > Apply Color 5 |
| - | View > Tab > Remove Color |
| + | View > Word wrap |
| - | View > Focus on Another View |
| - | View > Hide Lines |
| + | View > Fold All |
| + | View > Unfold All |
| + | View > Fold Current Level |
| + | View > Unfold Current Level |
| + | View > Fold Level > 1 |
| + | View > Fold Level > 2 |
| + | View > Fold Level > 3 |
| + | View > Fold Level > 4 |
| + | View > Fold Level > 5 |
| + | View > Fold Level > 6 |
| + | View > Fold Level > 7 |
| + | View > Fold Level > 8 |
| + | View > Unfold Level > 1 |
| + | View > Unfold Level > 2 |
| + | View > Unfold Level > 3 |
| + | View > Unfold Level > 4 |
| + | View > Unfold Level > 5 |
| + | View > Unfold Level > 6 |
| + | View > Unfold Level > 7 |
| + | View > Unfold Level > 8 |
| - | View > Summary... |
| - | View > Project Panels > Project Panel 1 |
| - | View > Project Panels > Project Panel 2 |
| - | View > Project Panels > Project Panel 3 |
| - | View > Folder as Workspace |
| - | View > Document Map |
| - | View > Document List |
| - | View > Function List |
| + | View > Synchronize Vertical Scrolling |
| + | View > Synchronize Horizontal Scrolling |
| + | View > Text Direction RTL |
| + | View > Text Direction LTR |
| - | View > Monitoring (tail -f) |
| - | Encoding > ANSI |
| - | Encoding > UTF-8 |
| - | Encoding > UTF-8-BOM |
| - | Encoding > UTF-16 BE BOM |
| - | Encoding > UTF-16 LE BOM |
| - | Encoding > Character sets > Arabic > ISO 8859-6 |
| - | Encoding > Character sets > Arabic > OEM 720 |
| - | Encoding > Character sets > Arabic > Windows-1256 |
| - | Encoding > Character sets > Baltic > ISO 8859-4 |
| - | Encoding > Character sets > Baltic > ISO 8859-13 |
| - | Encoding > Character sets > Baltic > OEM 775 |
| - | Encoding > Character sets > Baltic > Windows-1257 |
| - | Encoding > Character sets > Celtic > ISO 8859-14 |
| - | Encoding > Character sets > Cyrillic > ISO 8859-5 |
| - | Encoding > Character sets > Cyrillic > KOI8-R |
| - | Encoding > Character sets > Cyrillic > KOI8-U |
| - | Encoding > Character sets > Cyrillic > Macintosh |
| - | Encoding > Character sets > Cyrillic > OEM 855 |
| - | Encoding > Character sets > Cyrillic > OEM 866 |
| - | Encoding > Character sets > Cyrillic > Windows-1251 |
| - | Encoding > Character sets > Central European > OEM 852 |
| - | Encoding > Character sets > Central European > Windows-1250 |
| - | Encoding > Character sets > Chinese > Big5 (Traditional) |
| - | Encoding > Character sets > Chinese > GB2312 (Simplified) |
| - | Encoding > Character sets > Eastern European > ISO 8859-2 |
| - | Encoding > Character sets > Greek > ISO 8859-7 |
| - | Encoding > Character sets > Greek > OEM 737 |
| - | Encoding > Character sets > Greek > OEM 869 |
| - | Encoding > Character sets > Greek > Windows-1253 |
| - | Encoding > Character sets > Hebrew > ISO 8859-8 |
| - | Encoding > Character sets > Hebrew > OEM 862 |
| - | Encoding > Character sets > Hebrew > Windows-1255 |
| - | Encoding > Character sets > Japanese > Shift-JIS |
| - | Encoding > Character sets > Korean > Windows 949 |
| - | Encoding > Character sets > Korean > EUC-KR |
| - | Encoding > Character sets > North European > OEM 861 : Icelandic |
| - | Encoding > Character sets > North European > OEM 865 : Nordic |
| - | Encoding > Character sets > Thai > TIS-620 |
| - | Encoding > Character sets > Turkish > ISO 8859-3 |
| - | Encoding > Character sets > Turkish > ISO 8859-9 |
| - | Encoding > Character sets > Turkish > OEM 857 |
| - | Encoding > Character sets > Turkish > Windows-1254 |
| - | Encoding > Character sets > Western European > ISO 8859-1 |
| - | Encoding > Character sets > Western European > ISO 8859-10 |
| - | Encoding > Character sets > Western European > ISO 8859-15 |
| - | Encoding > Character sets > Western European > OEM 850 |
| - | Encoding > Character sets > Western European > OEM 858 |
| - | Encoding > Character sets > Western European > OEM 860 : Portuguese |
| - | Encoding > Character sets > Western European > OEM 863 : French |
| - | Encoding > Character sets > Western European > OEM-US |
| - | Encoding > Character sets > Western European > Windows-1252 |
| - | Encoding > Character sets > Vietnamese > Windows-1258 |
| - | Encoding > Convert to ANSI |
| - | Encoding > Convert to UTF-8 |
| - | Encoding > Convert to UTF-8-BOM |
| - | Encoding > Convert to UTF-16 BE BOM |
| - | Encoding > Convert to UTF-16 LE BOM |
| - | Language > None (Normal Text) |
| - | Language > ActionScript |
| - | Language > Ada |
| - | Language > ASN.1 |
| - | Language > ASP |
| - | Language > Assembly |
| - | Language > AutoIt |
| - | Language > AviSynth |
| - | Language > BaanC |
| - | Language > Batch |
| - | Language > Blitzbasic |
| - | Language > C |
| - | Language > C# |
| - | Language > C++ |
| - | Language > Caml |
| - | Language > CMake |
| - | Language > COBOL |
| - | Language > CSound |
| - | Language > CoffeeScript |
| - | Language > CSS |
| - | Language > D |
| - | Language > Diff |
| - | Language > Erlang |
| - | Language > ErrorList |
| - | Language > Escape Sequence (ANSI) |
| - | Language > ESCRIPT |
| - | Language > Forth |
| - | Language > Fortran (free form) |
| - | Language > Fortran (fixed form) |
| - | Language > Freebasic |
| - | Language > GDScript |
| - | Language > Go |
| - | Language > Gui4Cli |
| - | Language > Haskell |
| - | Language > Hollywood |
| - | Language > HTML |
| - | Language > INI file |
| - | Language > Inno Setup |
| - | Language > Intel HEX |
| - | Language > Java |
| - | Language > JavaScript |
| - | Language > JSON |
| - | Language > JSON5 |
| - | Language > JSP |
| - | Language > KIXtart |
| - | Language > LISP |
| - | Language > LaTeX |
| - | Language > Lua |
| - | Language > Makefile |
| - | Language > Matlab |
| - | Language > Microsoft Transact-SQL |
| - | Language > MMIXAL |
| - | Language > MS-DOS Style |
| - | Language > Nim |
| - | Language > Nncrontab |
| - | Language > NSIS |
| - | Language > Objective-C |
| - | Language > OScript |
| - | Language > Pascal |
| - | Language > Perl |
| - | Language > PHP |
| - | Language > PostScript |
| - | Language > PowerShell |
| - | Language > Properties |
| - | Language > Purebasic |
| - | Language > Python |
| - | Language > R |
| - | Language > Raku |
| - | Language > REBOL |
| - | Language > Registry |
| - | Language > Resource file |
| - | Language > Ruby |
| - | Language > Rust |
| - | Language > SAS |
| - | Language > Shell |
| - | Language > Scheme |
| - | Language > Smalltalk |
| - | Language > Spice |
| - | Language > SQL |
| - | Language > Swift |
| - | Language > S-Record |
| - | Language > TCL |
| - | Language > Tektronix extended HEX |
| - | Language > TeX |
| - | Language > TOML |
| - | Language > txt2tags |
| - | Language > TypeScript |
| - | Language > Verilog |
| - | Language > VHDL |
| - | Language > Visual Basic |
| - | Language > Visual Prolog |
| - | Language > XML |
| - | Language > YAML |
| - | Language > Define your language... |
| - | Language > Open User Defined Language folder... |
| - | Language > Notepad++ User Defined Languages Collection |
| - | Language > User-Defined |
| - | Language > None (Normal Text) |
| - | Language > A > ActionScript |
| - | Language > A > Ada |
| - | Language > A > ASN.1 |
| - | Language > A > ASP |
| - | Language > A > Assembly |
| - | Language > A > AutoIt |
| - | Language > A > AviSynth |
| - | Language > B > BaanC |
| - | Language > B > Batch |
| - | Language > B > Blitzbasic |
| - | Language > C > C |
| - | Language > C > C# |
| - | Language > C > C++ |
| - | Language > C > Caml |
| - | Language > C > CMake |
| - | Language > C > COBOL |
| - | Language > C > CSound |
| - | Language > C > CoffeeScript |
| - | Language > C > CSS |
| - | Language > D > D |
| - | Language > D > Diff |
| - | Language > E > Erlang |
| - | Language > E > ErrorList |
| - | Language > E > Escape Sequence (ANSI) |
| - | Language > E > ESCRIPT |
| - | Language > F > Forth |
| - | Language > F > Fortran (free form) |
| - | Language > F > Fortran (fixed form) |
| - | Language > F > Freebasic |
| - | Language > G > GDScript |
| - | Language > G > Go |
| - | Language > G > Gui4Cli |
| - | Language > H > Haskell |
| - | Language > H > Hollywood |
| - | Language > H > HTML |
| - | Language > I > INI file |
| - | Language > I > Inno Setup |
| - | Language > I > Intel HEX |
| - | Language > J > Java |
| - | Language > J > JavaScript |
| - | Language > J > JSON |
| - | Language > J > JSON5 |
| - | Language > J > JSP |
| - | Language > KIXtart |
| - | Language > L > LaTeX |
| - | Language > L > LISP |
| - | Language > L > Lua |
| - | Language > M > Makefile |
| - | Language > M > Matlab |
| - | Language > M > Microsoft Transact-SQL |
| - | Language > M > MMIXAL |
| - | Language > M > MS-DOS Style |
| - | Language > N > Nim |
| - | Language > N > Nncrontab |
| - | Language > N > NSIS |
| - | Language > O > Objective-C |
| - | Language > O > OScript |
| - | Language > P > Pascal |
| - | Language > P > Perl |
| - | Language > P > PHP |
| - | Language > P > PostScript |
| - | Language > P > PowerShell |
| - | Language > P > Properties |
| - | Language > P > Purebasic |
| - | Language > P > Python |
| - | Language > R > R |
| - | Language > R > Raku |
| - | Language > R > REBOL |
| - | Language > R > Registry |
| - | Language > R > Resource file |
| - | Language > R > Ruby |
| - | Language > R > Rust |
| - | Language > S > SAS |
| - | Language > S > Shell |
| - | Language > S > Scheme |
| - | Language > S > Smalltalk |
| - | Language > S > Spice |
| - | Language > S > SQL |
| - | Language > S > Swift |
| - | Language > S > S-Record |
| - | Language > T > TCL |
| - | Language > T > Tektronix extended HEX |
| - | Language > T > TeX |
| - | Language > T > TOML |
| - | Language > T > txt2tags |
| - | Language > T > TypeScript |
| - | Language > V > Visual Basic |
| - | Language > V > Visual Prolog |
| - | Language > V > VHDL |
| - | Language > V > Verilog |
| - | Language > XML |
| - | Language > YAML |
| - | Language > User Defined Language > Define your language... |
| - | Language > User Defined Language > Open User Defined Language folder... |
| - | Language > User Defined Language > Notepad++ User Defined Languages Collection |
| - | Language > User-Defined |
| - | Settings > Preferences... |
| - | Settings > Style Configurator... |
| - | Settings > Shortcut Mapper... |
| - | Settings > Import > Import plugin(s)... |
| - | Settings > Import > Import style theme(s)... |
| - | Settings > Edit Popup ContextMenu |
| - | Tools > MD5 > Generate... |
| - | Tools > MD5 > Generate from files... |
| - | Tools > MD5 > Generate from selection into clipboard |
| - | Tools > SHA-1 > Generate... |
| - | Tools > SHA-1 > Generate from files... |
| - | Tools > SHA-1 > Generate from selection into clipboard |
| - | Tools > SHA-256 > Generate... |
| - | Tools > SHA-256 > Generate from files... |
| - | Tools > SHA-256 > Generate from selection into clipboard |
| - | Tools > SHA-512 > Generate... |
| - | Tools > SHA-512 > Generate from files... |
| - | Tools > SHA-512 > Generate from selection into clipboard |
| - | Macro > Start Recording |
| - | Macro > Stop Recording |
| - | Macro > Playback |
| - | Macro > Save Current Recorded Macro... |
| - | Macro > Run a Macro Multiple Times... |
| - | Run > Run... |
| - | Run > Validate shortcuts.xml |
| - | Plugins > Open Plugins Folder... |
| - | Window > Sort By > Name A to Z |
| - | Window > Sort By > Name Z to A |
| - | Window > Sort By > Path A to Z |
| - | Window > Sort By > Path Z to A |
| - | Window > Sort By > Type A to Z |
| - | Window > Sort By > Type Z to A |
| - | Window > Sort By > Content Length Ascending |
| - | Window > Sort By > Content Length Descending |
| - | Window > Sort By > Modified Time Ascending |
| - | Window > Sort By > Modified Time Descending |
| - | Window > Windows... |
| - | Window > Recent Window |
| - | ? > Command Line Arguments... |
| - | ? > Notepad++ Home |
| - | ? > Notepad++ Project Page |
| - | ? > Notepad++ Online User Manual |
| - | ? > Notepad++ Community (Forum) |
| - | ? > Update Notepad++ |
| - | ? > Set Updater Proxy... |
| - | ? > Debug Info... |
| - | ? > About Notepad++ |
| + | ＋ |
| - | ▼ > Recent Window |
| + | ✕ |

{{< /details >}}

{{< details "show editing actions that should be macro-recordable" >}}

The following are all macro-recordable commands that are processed by the "Scintilla" library that Notepad++ uses for doing the various editing commands (copy, paste, select, and so on).  These are listed by the names of the internal constants, but most should be reasonably understandable.  If not, you can follow the link to the library's documentation for a given command.

| Command Constant |
|------------------|
| [SCI_REPLACESEL](https://scintilla.org/ScintillaDoc.html#SCI_REPLACESEL) |
| [SCI_ADDTEXT](https://scintilla.org/ScintillaDoc.html#SCI_ADDTEXT) |
| [SCI_INSERTTEXT](https://scintilla.org/ScintillaDoc.html#SCI_INSERTTEXT) |
| [SCI_APPENDTEXT](https://scintilla.org/ScintillaDoc.html#SCI_APPENDTEXT) |
| [SCI_SEARCHNEXT](https://scintilla.org/ScintillaDoc.html#SCI_SEARCHNEXT) |
| [SCI_SEARCHPREV](https://scintilla.org/ScintillaDoc.html#SCI_SEARCHPREV) |
| [SCI_GOTOLINE](https://scintilla.org/ScintillaDoc.html#SCI_GOTOLINE) |
| [SCI_GOTOPOS](https://scintilla.org/ScintillaDoc.html#SCI_GOTOPOS) |
| [SCI_SETSELECTIONMODE](https://scintilla.org/ScintillaDoc.html#SCI_SETSELECTIONMODE) |
| [SCI_CUT](https://scintilla.org/ScintillaDoc.html#SCI_CUT) |
| [SCI_COPY](https://scintilla.org/ScintillaDoc.html#SCI_COPY) |
| [SCI_PASTE](https://scintilla.org/ScintillaDoc.html#SCI_PASTE) |
| [SCI_CLEAR](https://scintilla.org/ScintillaDoc.html#SCI_CLEAR) |
| [SCI_CLEARALL](https://scintilla.org/ScintillaDoc.html#SCI_CLEARALL) |
| [SCI_SELECTALL](https://scintilla.org/ScintillaDoc.html#SCI_SELECTALL) |
| [SCI_SEARCHANCHOR](https://scintilla.org/ScintillaDoc.html#SCI_SEARCHANCHOR) |
| [SCI_LINEDOWN](https://scintilla.org/ScintillaDoc.html#SCI_LINEDOWN) |
| [SCI_LINEDOWNEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_LINEDOWNEXTEND) |
| [SCI_PARADOWN](https://scintilla.org/ScintillaDoc.html#SCI_PARADOWN) |
| [SCI_PARADOWNEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_PARADOWNEXTEND) |
| [SCI_LINEUP](https://scintilla.org/ScintillaDoc.html#SCI_LINEUP) |
| [SCI_LINEUPEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_LINEUPEXTEND) |
| [SCI_PARAUP](https://scintilla.org/ScintillaDoc.html#SCI_PARAUP) |
| [SCI_PARAUPEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_PARAUPEXTEND) |
| [SCI_CHARLEFT](https://scintilla.org/ScintillaDoc.html#SCI_CHARLEFT) |
| [SCI_CHARLEFTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_CHARLEFTEXTEND) |
| [SCI_CHARRIGHT](https://scintilla.org/ScintillaDoc.html#SCI_CHARRIGHT) |
| [SCI_CHARRIGHTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_CHARRIGHTEXTEND) |
| [SCI_WORDLEFT](https://scintilla.org/ScintillaDoc.html#SCI_WORDLEFT) |
| [SCI_WORDLEFTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_WORDLEFTEXTEND) |
| [SCI_WORDRIGHT](https://scintilla.org/ScintillaDoc.html#SCI_WORDRIGHT) |
| [SCI_WORDRIGHTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_WORDRIGHTEXTEND) |
| [SCI_WORDPARTLEFT](https://scintilla.org/ScintillaDoc.html#SCI_WORDPARTLEFT) |
| [SCI_WORDPARTLEFTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_WORDPARTLEFTEXTEND) |
| [SCI_WORDPARTRIGHT](https://scintilla.org/ScintillaDoc.html#SCI_WORDPARTRIGHT) |
| [SCI_WORDPARTRIGHTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_WORDPARTRIGHTEXTEND) |
| [SCI_WORDLEFTEND](https://scintilla.org/ScintillaDoc.html#SCI_WORDLEFTEND) |
| [SCI_WORDLEFTENDEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_WORDLEFTENDEXTEND) |
| [SCI_WORDRIGHTEND](https://scintilla.org/ScintillaDoc.html#SCI_WORDRIGHTEND) |
| [SCI_WORDRIGHTENDEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_WORDRIGHTENDEXTEND) |
| [SCI_HOME](https://scintilla.org/ScintillaDoc.html#SCI_HOME) |
| [SCI_HOMEEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_HOMEEXTEND) |
| [SCI_LINEEND](https://scintilla.org/ScintillaDoc.html#SCI_LINEEND) |
| [SCI_LINEENDEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_LINEENDEXTEND) |
| [SCI_HOMEWRAP](https://scintilla.org/ScintillaDoc.html#SCI_HOMEWRAP) |
| [SCI_HOMEWRAPEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_HOMEWRAPEXTEND) |
| [SCI_LINEENDWRAP](https://scintilla.org/ScintillaDoc.html#SCI_LINEENDWRAP) |
| [SCI_LINEENDWRAPEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_LINEENDWRAPEXTEND) |
| [SCI_DOCUMENTSTART](https://scintilla.org/ScintillaDoc.html#SCI_DOCUMENTSTART) |
| [SCI_DOCUMENTSTARTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_DOCUMENTSTARTEXTEND) |
| [SCI_DOCUMENTEND](https://scintilla.org/ScintillaDoc.html#SCI_DOCUMENTEND) |
| [SCI_DOCUMENTENDEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_DOCUMENTENDEXTEND) |
| [SCI_STUTTEREDPAGEUP](https://scintilla.org/ScintillaDoc.html#SCI_STUTTEREDPAGEUP) |
| [SCI_STUTTEREDPAGEUPEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_STUTTEREDPAGEUPEXTEND) |
| [SCI_STUTTEREDPAGEDOWN](https://scintilla.org/ScintillaDoc.html#SCI_STUTTEREDPAGEDOWN) |
| [SCI_STUTTEREDPAGEDOWNEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_STUTTEREDPAGEDOWNEXTEND) |
| [SCI_PAGEUP](https://scintilla.org/ScintillaDoc.html#SCI_PAGEUP) |
| [SCI_PAGEUPEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_PAGEUPEXTEND) |
| [SCI_PAGEDOWN](https://scintilla.org/ScintillaDoc.html#SCI_PAGEDOWN) |
| [SCI_PAGEDOWNEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_PAGEDOWNEXTEND) |
| [SCI_EDITTOGGLEOVERTYPE](https://scintilla.org/ScintillaDoc.html#SCI_EDITTOGGLEOVERTYPE) |
| [SCI_CANCEL](https://scintilla.org/ScintillaDoc.html#SCI_CANCEL) |
| [SCI_DELETEBACK](https://scintilla.org/ScintillaDoc.html#SCI_DELETEBACK) |
| [SCI_TAB](https://scintilla.org/ScintillaDoc.html#SCI_TAB) |
| [SCI_BACKTAB](https://scintilla.org/ScintillaDoc.html#SCI_BACKTAB) |
| [SCI_FORMFEED](https://scintilla.org/ScintillaDoc.html#SCI_FORMFEED) |
| [SCI_VCHOME](https://scintilla.org/ScintillaDoc.html#SCI_VCHOME) |
| [SCI_VCHOMEEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_VCHOMEEXTEND) |
| [SCI_VCHOMEWRAP](https://scintilla.org/ScintillaDoc.html#SCI_VCHOMEWRAP) |
| [SCI_VCHOMEWRAPEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_VCHOMEWRAPEXTEND) |
| [SCI_VCHOMEDISPLAY](https://scintilla.org/ScintillaDoc.html#SCI_VCHOMEDISPLAY) |
| [SCI_VCHOMEDISPLAYEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_VCHOMEDISPLAYEXTEND) |
| [SCI_DELWORDLEFT](https://scintilla.org/ScintillaDoc.html#SCI_DELWORDLEFT) |
| [SCI_DELWORDRIGHT](https://scintilla.org/ScintillaDoc.html#SCI_DELWORDRIGHT) |
| [SCI_DELWORDRIGHTEND](https://scintilla.org/ScintillaDoc.html#SCI_DELWORDRIGHTEND) |
| [SCI_DELLINELEFT](https://scintilla.org/ScintillaDoc.html#SCI_DELLINELEFT) |
| [SCI_DELLINERIGHT](https://scintilla.org/ScintillaDoc.html#SCI_DELLINERIGHT) |
| [SCI_LINECOPY](https://scintilla.org/ScintillaDoc.html#SCI_LINECOPY) |
| [SCI_LINECUT](https://scintilla.org/ScintillaDoc.html#SCI_LINECUT) |
| [SCI_LINEDELETE](https://scintilla.org/ScintillaDoc.html#SCI_LINEDELETE) |
| [SCI_LINETRANSPOSE](https://scintilla.org/ScintillaDoc.html#SCI_LINETRANSPOSE) |
| [SCI_LINEDUPLICATE](https://scintilla.org/ScintillaDoc.html#SCI_LINEDUPLICATE) |
| [SCI_LOWERCASE](https://scintilla.org/ScintillaDoc.html#SCI_LOWERCASE) |
| [SCI_UPPERCASE](https://scintilla.org/ScintillaDoc.html#SCI_UPPERCASE) |
| [SCI_LINESCROLLDOWN](https://scintilla.org/ScintillaDoc.html#SCI_LINESCROLLDOWN) |
| [SCI_LINESCROLLUP](https://scintilla.org/ScintillaDoc.html#SCI_LINESCROLLUP) |
| [SCI_DELETEBACKNOTLINE](https://scintilla.org/ScintillaDoc.html#SCI_DELETEBACKNOTLINE) |
| [SCI_HOMEDISPLAY](https://scintilla.org/ScintillaDoc.html#SCI_HOMEDISPLAY) |
| [SCI_HOMEDISPLAYEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_HOMEDISPLAYEXTEND) |
| [SCI_LINEENDDISPLAY](https://scintilla.org/ScintillaDoc.html#SCI_LINEENDDISPLAY) |
| [SCI_LINEENDDISPLAYEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_LINEENDDISPLAYEXTEND) |
| [SCI_LINEDOWNRECTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_LINEDOWNRECTEXTEND) |
| [SCI_LINEUPRECTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_LINEUPRECTEXTEND) |
| [SCI_CHARLEFTRECTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_CHARLEFTRECTEXTEND) |
| [SCI_CHARRIGHTRECTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_CHARRIGHTRECTEXTEND) |
| [SCI_HOMERECTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_HOMERECTEXTEND) |
| [SCI_VCHOMERECTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_VCHOMERECTEXTEND) |
| [SCI_LINEENDRECTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_LINEENDRECTEXTEND) |
| [SCI_PAGEUPRECTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_PAGEUPRECTEXTEND) |
| [SCI_PAGEDOWNRECTEXTEND](https://scintilla.org/ScintillaDoc.html#SCI_PAGEDOWNRECTEXTEND) |
| [SCI_SELECTIONDUPLICATE](https://scintilla.org/ScintillaDoc.html#SCI_SELECTIONDUPLICATE) |
| [SCI_COPYALLOWLINE](https://scintilla.org/ScintillaDoc.html#SCI_COPYALLOWLINE) |
| [SCI_VERTICALCENTRECARET](https://scintilla.org/ScintillaDoc.html#SCI_VERTICALCENTRECARET) |
| [SCI_MOVESELECTEDLINESUP](https://scintilla.org/ScintillaDoc.html#SCI_MOVESELECTEDLINESUP) |
| [SCI_MOVESELECTEDLINESDOWN](https://scintilla.org/ScintillaDoc.html#SCI_MOVESELECTEDLINESDOWN) |
| [SCI_SCROLLTOSTART](https://scintilla.org/ScintillaDoc.html#SCI_SCROLLTOSTART) |
| [SCI_SCROLLTOEND](https://scintilla.org/ScintillaDoc.html#SCI_SCROLLTOEND) |
| [SCI_SETVIRTUALSPACEOPTIONS](https://scintilla.org/ScintillaDoc.html#SCI_SETVIRTUALSPACEOPTIONS) |
| [SCI_SETCARETLINEBACKALPHA](https://scintilla.org/ScintillaDoc.html#SCI_SETCARETLINEBACKALPHA) |
| [SCI_NEWLINE](https://scintilla.org/ScintillaDoc.html#SCI_NEWLINE) |

{{< /details >}}



## Play a recorded macro

To play the macro in the buffer, select **Macro > Playback** or press the button.
This will perform the macro once at the current position.


## Save a recorded macro

To save the macro in the buffer, select **Macro > Save current recorded macro...** or
press the toolbar button. A dialog will pop up asking for a name of the macro and the
default key combination. These can later be changed (or deleted) using
**Macro > Modify Shortcut/Delete Macro...**, which brings up the
[**Settings > Shortcut Mapper**](../preferences/#shortcut-mapper) on the **Macros** tab.
When saved, the macro will be available in the bottom section of the **Macro** menu, or
from the pulldown in the dialog accessed from the **Macro > Run a Macro Multiple Times...**
menu entry.

As noted in the [Configuration Files](../config-files) documentation, Notepad++
writes the configuration files (including the macros) when it exits, which means that
after you save your macro, your new macro will _not_ be written to the `shortcuts.xml`
configuration file until Notepad++ exits.  Thus, if you open `shortcuts.xml` after saving
the macro but before exiting Notepad++, you will _not_ be able to see your new macro yet.

## Play a recorded macro multiple times

To play the current macro in the buffer or any saved macro once or multiple
times, select **Macro > Run a Macro Multiple Times...** or press the button.
A dialog will pop up allowing you to select what macro to perform (buffer
macro or any saved macro) and how many times. You can also opt to perform the
macro until the [caret](../editing/#caret-and-cursor "typing/insertion cursor") reaches the end of the current file (starting from
its current position).

Note that if no macros are available, this menu option is greyed out, and
the dialog is inaccessible.


## Edit or delete an existing macro shortcut

To edit or delete an existing macro shortcut, you can use the Shortcut mapper,
which displays all shortcuts of all kinds, and allows changing or removing a key
binding. The interface is also available through the **Macro > Modify
shortcut/Delete macro...** menu entry.

The contents of a macro definition can be edited only in the `shortcuts.xml`
file: there is no built-in interface in Notepad++.  For more information on
the details of how the macros are stored, and the syntax involved, see the
[**Configuration Files Details**: **<Macros>** section](../config-files/#macros).

Some information on the limitations of Macros and possible workarounds can be found in the community page [FAQ: Automating Notepad++](https://community.notepad-plus-plus.org/topic/25400/faq-automating-notepad).

## Macro Security

Starting in v8.9.6.2, the Run menu added extra security-warning that will notify you if the `shortcuts.xml` was modified manually or outside of Notepad++ (if your file was customized when you upgraded from a version before this to this version or later, the notification will also be used the first time you run a saved entry from the Run menu).  In v8.9.7, this protection was extended to also apply to the Macro menu.  You can read more in the [Config Files > shortucts.xml Security](../config-files/#shortcutsxml-security) section; but in brief, open `shortcuts.xml`, verify that your `<UserDefinedCommands>` and `<Macros>` entries look correct, then use **Run > Validate shortcuts.xml** to inform Notepad++ that everything looks reasonable.  (This security step prevents a malicious outside actor from overwriting your `shortcuts.xml` to include a malicious macro or run-menu command, by warning you when there's an unexpected change to the file.)
