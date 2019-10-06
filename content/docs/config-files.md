---
title: Configuration File Syntax
linktitle: config-files
weight: 115
---

## Configuration File Syntax

\-----------------------------


</p><p>Notepad++ offers a comprehensive user interface to review or change most of its settings. However, there are some special cases, among which:
</p>
<ul>
<li> Using synthesized macros to send commands with parameters to a Scintilla component;
</li>
<li> Adding keywords to a language, because the new language version isn't matched yet;
</li>
<li> Some settings have been left out of the user interface;
</li>
<li> You'd like to edit a session file so as to quick add/remove a file
</li>
<li> You wish to customise the <a href="http://docs.notepad-plus-plus.org/index.php/Context_Menu" title="Context Menu">Context Menu</a>;
</li>
<li> There are probably other reasons.
</li>
</ul>
<p>You will want to review <a href="http://docs.notepad-plus-plus.org/index.php/Configuration_Files" title="Configuration Files">Configuration Files</a> in order to know where is what, and <a href="http://docs.notepad-plus-plus.org/index.php/Configuration_File_Editing" title="Configuration File Editing">Configuration File Editing</a>, specially if you contemplate using Notepad++ to modify its own configuration files.
</p><p><b>ALWAYS BACKUP THE FILE TO BE EDITED</b>. If you make a mistake, Notepad++ may erase the whole contents and replace it with useless defaults. This is probably the worst that can happen, but it does happen.
</p>
<div id="toc" class="toc"><div id="toctitle"><h2>Contents</h2></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#General_format_considerations">1 General format considerations</a>
<ul>
<li class="toclevel-2 tocsection-2"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Valid_keys">1.1 Valid keys</a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-3"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#User_interface_settings:_config.xml">2 User interface settings: config.xml</a>
<ul>
<li class="toclevel-2 tocsection-4"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CGUIConfigs.3E">2.1 &lt;GUIConfigs&gt;</a>
<ul>
<li class="toclevel-3 tocsection-5"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#ToolBar">2.1.1 ToolBar</a></li>
<li class="toclevel-3 tocsection-6"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#StatusBar">2.1.2 StatusBar</a></li>
<li class="toclevel-3 tocsection-7"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#TabBar">2.1.3 TabBar</a></li>
<li class="toclevel-3 tocsection-8"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#ScintillaViewSplitter">2.1.4 ScintillaViewSplitter</a></li>
<li class="toclevel-3 tocsection-9"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#UserDefineDlg">2.1.5 UserDefineDlg</a></li>
<li class="toclevel-3 tocsection-10"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#TabSetting">2.1.6 TabSetting</a></li>
<li class="toclevel-3 tocsection-11"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#AppPosition">2.1.7 AppPosition</a></li>
<li class="toclevel-3 tocsection-12"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#ScintillaPrimaryView">2.1.8 ScintillaPrimaryView</a></li>
<li class="toclevel-3 tocsection-13"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#ScintillaSecundaryView">2.1.9 ScintillaSecundaryView</a></li>
<li class="toclevel-3 tocsection-14"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Auto-detection">2.1.10 Auto-detection</a></li>
<li class="toclevel-3 tocsection-15"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#CheckHistoryFiles">2.1.11 CheckHistoryFiles</a></li>
<li class="toclevel-3 tocsection-16"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#TrayIcon">2.1.12 TrayIcon</a></li>
<li class="toclevel-3 tocsection-17"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#RememberLastSession">2.1.13 RememberLastSession</a></li>
<li class="toclevel-3 tocsection-18"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#NewDocDefaultSettings">2.1.14 NewDocDefaultSettings</a></li>
<li class="toclevel-3 tocsection-19"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#langExcluded">2.1.15 langExcluded</a></li>
<li class="toclevel-3 tocsection-20"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Print">2.1.16 Print</a></li>
<li class="toclevel-3 tocsection-21"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Backup">2.1.17 Backup</a></li>
<li class="toclevel-3 tocsection-22"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#TaskList">2.1.18 TaskList</a></li>
<li class="toclevel-3 tocsection-23"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#SaveOpenFileInSameDir">2.1.19 SaveOpenFileInSameDir</a></li>
<li class="toclevel-3 tocsection-24"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#noUpdate">2.1.20 noUpdate</a></li>
<li class="toclevel-3 tocsection-25"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#MaitainIndent">2.1.21 MaitainIndent</a></li>
<li class="toclevel-3 tocsection-26"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#MRU">2.1.22 MRU</a></li>
<li class="toclevel-3 tocsection-27"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#URL">2.1.23 URL</a></li>
<li class="toclevel-3 tocsection-28"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#globalOverride">2.1.24 globalOverride</a></li>
<li class="toclevel-3 tocsection-29"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#auto-completion">2.1.25 auto-completion</a></li>
<li class="toclevel-3 tocsection-30"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#sessionExt">2.1.26 sessionExt</a></li>
<li class="toclevel-3 tocsection-31"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#SmartHighLight">2.1.27 SmartHighLight</a></li>
<li class="toclevel-3 tocsection-32"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#SmartHighLightCaseSensitive">2.1.28 SmartHighLightCaseSensitive</a></li>
<li class="toclevel-3 tocsection-33"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#TagsMatchHighLight">2.1.29 TagsMatchHighLight</a></li>
<li class="toclevel-3 tocsection-34"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#MenuBar">2.1.30 MenuBar</a></li>
<li class="toclevel-3 tocsection-35"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Caret">2.1.31 Caret</a></li>
<li class="toclevel-3 tocsection-36"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#ScintillaGlobalSettings">2.1.32 ScintillaGlobalSettings</a></li>
<li class="toclevel-3 tocsection-37"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#openSaveDir">2.1.33 openSaveDir</a></li>
<li class="toclevel-3 tocsection-38"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#titleBar">2.1.34 titleBar</a></li>
<li class="toclevel-3 tocsection-39"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#styleTheme">2.1.35 styleTheme</a></li>
<li class="toclevel-3 tocsection-40"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#delimiterSelection">2.1.36 delimiterSelection</a></li>
<li class="toclevel-3 tocsection-41"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#MISC">2.1.37 MISC</a></li>
<li class="toclevel-3 tocsection-42"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#DockingManager">2.1.38 DockingManager</a></li>
</ul>
</li>
<li class="toclevel-2 tocsection-43"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CFindHistory.3E">2.2 &lt;FindHistory&gt;</a></li>
<li class="toclevel-2 tocsection-44"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CHistory.3E">2.3 &lt;History&gt;</a></li>
<li class="toclevel-2 tocsection-45"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CProjectPanels.3E">2.4 &lt;ProjectPanels&gt;</a></li>
<li class="toclevel-2 tocsection-46"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CFileEditViewHistory.3E">2.5 &lt;FileEditViewHistory&gt;</a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-47"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Keyboard_shortcuts:_shortcuts.xml">3 Keyboard shortcuts: shortcuts.xml</a>
<ul>
<li class="toclevel-2 tocsection-48"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CInternalCommands.3E">3.1 &lt;InternalCommands&gt;</a></li>
<li class="toclevel-2 tocsection-49"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CMacros.3E">3.2 &lt;Macros&gt;</a>
<ul>
<li class="toclevel-3 tocsection-50"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Search_.2F_Replace_encoding">3.2.1 Search / Replace encoding</a></li>
</ul>
</li>
<li class="toclevel-2 tocsection-51"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CUserDefinedCommands.3E">3.3 &lt;UserDefinedCommands&gt;</a></li>
<li class="toclevel-2 tocsection-52"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CPluginCommands.3E">3.4 &lt;PluginCommands&gt;</a></li>
<li class="toclevel-2 tocsection-53"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CScintillaKeys.3E">3.5 &lt;ScintillaKeys&gt;</a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-54"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Built-in_language_features">4 Built-in language features</a>
<ul>
<li class="toclevel-2 tocsection-55"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Keyword_lists:_langs.xml">4.1 Keyword lists: langs.xml</a></li>
<li class="toclevel-2 tocsection-56"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Highlighting_schemes:_stylers.xml">4.2 Highlighting schemes: stylers.xml</a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-57"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#The_context_menu">5 The context menu</a></li>
<li class="toclevel-1 tocsection-58"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Toolbar_icons">6 Toolbar icons</a></li>
<li class="toclevel-1 tocsection-59"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Session_files">7 Session files</a></li>
<li class="toclevel-1 tocsection-60"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#User_defined_languages:_userDefineLang.xml">8 User defined languages: userDefineLang.xml</a>
<ul>
<li class="toclevel-2 tocsection-61"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CSettings.3E">8.1 &lt;Settings&gt;</a></li>
<li class="toclevel-2 tocsection-62"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CKeywordLists.3E">8.2 &lt;KeywordLists&gt;</a></li>
<li class="toclevel-2 tocsection-63"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CStyles.3E">8.3 &lt;Styles&gt;</a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-64"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Autocompletion.2C_aka_API.2C_files">9 Autocompletion, aka API, files</a>
<ul>
<li class="toclevel-2 tocsection-65"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Names">9.1 Names</a></li>
<li class="toclevel-2 tocsection-66"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Sorting">9.2 Sorting</a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-67"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Workspace_files">10 Workspace files</a></li>
<li class="toclevel-1 tocsection-68"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#FunctionList">11 FunctionList</a>
<ul>
<li class="toclevel-2 tocsection-69"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Associations">11.1 Associations</a></li>
<li class="toclevel-2 tocsection-70"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#Parsers">11.2 Parsers</a>
<ul>
<li class="toclevel-3 tocsection-71"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3Cfunction.3E_parsers">11.2.1 &lt;function&gt; parsers</a></li>
<li class="toclevel-3 tocsection-72"><a href="http://docs.notepad-plus-plus.org/index.php/Editing_Configuration_Files#.3CclassRange.3E_parsers">11.2.2 &lt;classRange&gt; parsers</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>

<h3>General format considerations</h3>
<p>Configuration files are xml files. An xml file is made of nodes, which may contain nodes recursively, which may contain tags. Both nodes and tags may have attributes. <b>Their order and capitalisation must be kept strictly</b>. The ordering of tags usually doesn't matter, except when it orders menu items, in which case the ordering is part of the configuration. It also happens that some ordering must be identical across different files.
</p><p>Nodes and tags come in two forms: a short &lt;Node/&gt; form and a long &lt;Node&gt;...&lt;/Node&gt; form. The former is to be used if and only if the node is empty or the tag has no content - there may be attributes though.
</p><p>All configuration files xml structure is contained in a single &lt;NotepadPlus&gt; node. There must be exactly one such node per file, and it should be topmost.
</p><p>All integer attribute values are written between double quotes, like in "15". Since xml only knows about strings, anything must be written as a string, which is delimited by double quotes.
</p>
<h4>Valid keys</h4>
<p>The use of the Windows key as a modifier is not supported by Scintilla.
</p><p>The complete list of base virtual key code is to be found on <a rel="nofollow" class="external text" href="http://notepad-plus.svn.sourceforge.net/viewvc/notepad-plus/trunk/PowerEditor/src/keys.h?view=markup">keys.h</a>. Because of this reliance on OS defined virtual keys, various letters obtained by combining diacritics with a main key (like the german ß or spanish ñ) cannot be used.
</p><p>Left and right versions of modifiers are not distinguished. A special case is the AltGr key on various european keyboards, which translates to Ctrl+Alt rather than plain Alt.
</p><p>Keys producing double byte character codes are not supported if they don't fit in the virtual key list.
</p>
<h3>User interface settings: config.xml</h3>
<p>Syntax highlighting will be covered in the specific section with this name.
</p><p>Below the standard &lt;NotepadPlus&gt; node, the following sections are defined:
</p>
<ol>
<li> &lt;GUIConfigs&gt;: user interface settings
</li>
<li> &lt;FindHistory&gt;: most of the latest state of the Find/Replace dialog box.
</li>
<li> &lt;History&gt;: the list of recently used files.
</li>
</ol>
<h4>&lt;GUIConfigs&gt;</h4>
<p>This area contains most of the items that can be adjusted from the Preferences dialog. It is thoroughly commented for the most part.
</p><p>There could be two reasons to edit this section:
</p>
<ol>
<li> it may contain settings that are not yet configurable from a dialog. This would happen for intermediate or candidate releases.
</li>
<li> it ma be useful to run a script for custom installation of Notepad++ by a system administrator.
</li>
</ol>
<p>The tag contains a large number of &lt;GUIConfig&gt; tags. All of them have a "name" attribute. Any other contents or extra attributes they may have is controlled by the "name" attribute, as discussed in the individual sections below. Each section lists attributes and their possible values, then contents if applicable. Usually, thee is no need for extra explanation, as the name / attribute pair closely match the corresponding Preferences widget caption.
</p><p>GUIConfig tags without contents may be auto-closing or not, this seems to be immaterial.
</p>
<h5>ToolBar</h5>
<ol>
<li> "visible": "yes"/"no" attribute
</li>
<li> "show": any of "hide","standard", "large" and "small".
</li>
</ol>
<h5>StatusBar</h5>
<p>Contents are either of show or hide.
</p>
<h5>TabBar</h5>
<p>A sequence of "yes"/"no" attributes:
</p>
<ol>
<li> dragAndDrop
</li>
<li> drawTopBar
</li>
<li> drawInactiveTab
</li>
<li> reduce
</li>
<li> closeButton
</li>
<li> doubleClick2Close
</li>
<li> vertical
</li>
<li> multiline
</li>
<li> hide
</li>
</ol>
<h5>ScintillaViewSplitter</h5>
<p>Contents are either of horizontal or vertical.
</p>
<h5>UserDefineDlg</h5>
<ol>
<li> "position" is either of docked or undocked
</li>
</ol>
<p>Contents are either of show or hide.
</p>
<h5>TabSetting</h5>
<p>This is the default value for all languages not receiving special treatment through Settings -&gt; Preferences -&gt; Language menu/Tab settings.
</p>
<ol>
<li>"tabSize": conversion factor
</li>
<li> replaceBySpaces": "yes"/"no"
</li>
</ol>
<h5>AppPosition</h5>
<ol>
<li> "x"
</li>
<li> "y"
</li>
<li> "width"
</li>
<li> "height"
</li>
<li> "isMaximized": "yes"/"no", other are numbers of pixels.
</li>
</ol>
<h5>ScintillaPrimaryView</h5>
<ol>
<li> "lineNumberMargin": either of show or hide
</li>
<li> "bookmarkMargin": either of show or hide
</li>
<li> "folderMarkStyle": either of single, arrow, circle or box
</li>
<li> "indentGuideLine": either of show or hide
</li>
<li> "currentLineHilitingShow": either of show or hide
</li>
<li> "Wrap": "yes" / "no"
</li>
<li> "edge": "yes" / "no"
</li>
<li> "edgNbColumn": number of columns&gt;
</li>
<li> "wrapSymbolShow": either of show or hide
</li>
<li> "zoom": a signed integer, the number of points to add for current magnification.
</li>
<li> "whiteSpaceShow": either of show or hide
</li>
<li> "eolShow": either of show or hide
</li>
<li> "disableAdvancedScrolling": either of "yes" or "no" (default)
</li>
<li> "borderWidth": width in pixels.
</li>
</ol>
<h5>ScintillaSecundaryView</h5>
<p>This setting is no longer in use, as version 5.7.1 has removed individual view options.
</p>
<h5>Auto-detection</h5>
<p>Contents either yes or &lt;tt/&gt;n&lt;/tt&gt;.
</p>
<h5>CheckHistoryFiles</h5>
<p>Contents either yes or &lt;tt/&gt;n&lt;/tt&gt;.
</p>
<h5>TrayIcon</h5>
<p>Contents either yes or &lt;tt/&gt;n&lt;/tt&gt;.
</p>
<h5>RememberLastSession</h5>
<p>Contents either yes or &lt;tt/&gt;n&lt;/tt&gt;.
</p>
<h5>NewDocDefaultSettings</h5>
<ol>
<li> "format": either of 0 (CR+LF for DOS/Windows), 1 (LF for Unix/Mac OSX) or 2 (CR for Mac OD 9 and earlier).
</li>
<li> "encoding": either of 0 (ANSI), 1 (UTF-8 with BOM), 2 (UCS-2 BE with BOM), 3 (UCS2 LE with BOM), 4 (UTF-8 without BOM), 5 (7-bit ASCII), 6 (UCS-2 BE without BOM) or 7 (UCS-2 LE without BOM).
</li>
<li> "lang": the 0-based lexer number for the default language. As a result, this cannot be an user defined language, use the extension instead. The number follows the list as displayed in the corresponding tab: 0 for normal text, 1 for PHP, 2 for C and so on.
</li>
<li> "openAnsiAsUTF8": "yes" / "no"
</li>
</ol>
<h5>langExcluded</h5>
<p>The various gr&lt;n&gt; attributes are byte masks. Supported languages seem to be arranged by groups of 8, and the mask summarises which languages in each group are excluded.
</p>
<ol>
<li> "gr0":
</li>
<li> "gr1":
</li>
<li> "gr2":
</li>
<li> "gr3":
</li>
<li> "gr4":
</li>
<li> "gr5":
</li>
<li> "gr6":
</li>
<li> "gr7":
</li>
<li> "langMenuCompact": "yes" / "no"
</li>
</ol>
<h5>Print</h5>
<ol>
<li> "lineNumber": "yes" / "no"
</li>
<li> printOption": either of 0 (WYSIWYG), 1 (invert colour), 2 (B &amp; W) or 3 (WYSIWYG without a background)
</li>
<li> "headerLeft": text for the designated area
</li>
<li> "headerMiddle": text for the designated area
</li>
<li> "headerRight": text for the designated area
</li>
<li> "headerFontName": name of font
</li>
<li> "headerFontStyle": as per style font flags
</li>
<li> "headerFontSize": size of font
</li>
<li> "footerLeft": text for the designated area
</li>
<li> "footerMiddle": text for the designated area
</li>
<li> "footerRight": text for the designated area
</li>
<li> "footerFontName": name of font
</li>
<li> "footerFontStyle": as per style font flags
</li>
<li> "footerFontSize": size of font
</li>
<li> "marginLeft": size in centimeters
</li>
<li> "marginTop": size in centimeters
</li>
<li> "marginRight": size in centimeters
</li>
<li> "marginBottom": size in millimeters
</li>
</ol>
<h5>Backup</h5>
<ol>
<li> "action": either of 0 (none), 1 (simple) or 2 (verbose).
</li>
<li> "useCustumDir": "yes" / "no"
</li>
<li> "dir": directory name
</li>
<li> "isSnapshotMode": "yes" / "no". Defaults to yes.
</li>
<li> "snapshotBackupTiming": number of milliseconds between snapshots (default is 7,000).
</li>
</ol>
<h5>TaskList</h5>
<p>Contents are "yes" / "no".
</p>
<h5>SaveOpenFileInSameDir</h5>
<p>Contents are "yes" / "no".
</p>
<h5>noUpdate</h5>
<ol>
<li> "intervaDays": number of days to wait to update to next version
</li>
<li> "nextUpateDate": yyyymmdd representation of date to fire auto-update
</li>
</ol>
<p>Contents are "yes" / "no"
</p>
<h5>MaitainIndent</h5>
<p>Contents are "yes" / "no". This flag controls whether any indent is to be copied from the current line when Enter is hit.
</p>
<h5>MRU</h5>
<p>Contents are "yes" / "no".
</p>
<h5>URL</h5>
<p>Contents are either of 0 (don't enable clickable links), 1 (enable with underline) or 2 (enable without underline).
</p>
<h5>globalOverride</h5>
<ol>
<li> "fg": "yes" / "no"
</li>
<li> "bg": "yes" / "no"
</li>
<li> "font": "yes" / "no"
</li>
<li> "fontSize": "yes" / "no"
</li>
<li> "bold"yes" / "no"
</li>
<li> "italic"yes" / "no"
</li>
<li> "underline"yes" / "no"
</li>
</ol>
<h5>auto-completion</h5>
<ol>
<li> "autoCAction": either of 0 (disabled), 1 (enabled for functions),  2 (enabled for words) or 3 (both words and functions).
</li>
<li> "triggerFromNbChar": number of characters after which the list will pop up
</li>
<li> "funcParams": "yes" / "no" (enable call tips)
</li>
</ol>
<h5>sessionExt</h5>
<p>Contents are the extension, if any.
</p>
<h5>SmartHighLight</h5>
<p>Contents are "yes" / "no".
</p>
<h5>SmartHighLightCaseSensitive</h5>
<p>Contents are "yes" / "no".
</p>
<h5>TagsMatchHighLight</h5>
<ol>
<li> "TagAttrHighLight": "yes" / "no"
</li>
<li> "HighLightNonHtmlZone": "yes" / "no"
</li>
</ol>
<p>Contents are "yes" / "no".
</p>
<h5>MenuBar</h5>
<p>Contents are either of show or hide.
</p>
<h5>Caret</h5>
<ol>
<li> "width": in pixels
</li>
<li> "blinkRate": an integer, the number of milliseconds during which the caret is shown, then hidden. The two intervals are equal.
</li>
</ol>
<h5>ScintillaGlobalSettings</h5>
<ol>
<li> "enableMultipleSelection": "yes" / "no"
</li>
</ol>
<h5>openSaveDir</h5>
<ol>
<li> "value": 0 to disable, 1 to enable.
</li>
<li> "defaultDirPath": fixed starting path for open/save dialogs
</li>
</ol>
<h5>titleBar</h5>
<ol>
<li> "short": "yes" / "no"
</li>
</ol>
<h5>styleTheme</h5>
<ol>
<li> "path": path to current theme file
</li>
</ol>
<h5>delimiterSelection</h5>
<ol>
<li>"leftmostDelimiter": ASCII code of the character limiting the selection on the left (default is 40 for '(')
</li>
<li>"rightmostDelimiter": ASCII code of the character limiting the selection on the right (drfault is 41 for ')')
</li>
<li>"delimiterSelectionOnEntireDocument": "yes" to alow text on multiple contiuous lines to be selected, otherwise "no" (default).
</li>
</ol>
<h5>MISC</h5>
<ol>
<li> "fileSwitcherWithoutExtColumn": "yas"/"no" (default).
</li>
<li> "backslashEscapeCharacterFprSQL"&nbsp;: "yes" / "no" (default is yes).
</li>
</ol>
<h5>DockingManager</h5>
<p>The following values are the width of left/right side windows and the height of top/bottom window will take:
</p>
<ol>
<li> "leftWidth": size in pixels, 0 is allowed
</li>
<li> "rightWidth": size in pixels, 0 is allowed
</li>
<li> "topHeight": size in pixels, 0 is allowed
</li>
<li> "bottomHeight": size in pixels, 0 is allowed
</li>
</ol>
<p>Contents are a possibly empty sequence of &lt;FloatingWindow&gt; auto-closed tags, followed by a possibly empty sequence of &lt;PluginDlg&gt; tags, followed by at least 4 auto-closed &lt;ActiveTabs&gt; tags, one for each of the 4 predefined positions, plus one for each undocked window.
</p><p>A &lt;FloatingWindow&gt; tag defines the position, width and height of a detached (floating) window&nbsp;:
</p>
<ol>
<li> "cont": a container identifier, matching the one for an &lt;ActiveTabs&gt; subsequent tag.
</li>
<li> "x": position x in pixels
</li>
<li> "y": position y in pixels
</li>
<li> "width": in pixels
</li>
<li> "height": in pixels
</li>
</ol>
<p>A &lt;PluginDlg&gt; tag has no contents and the following attributes:
</p>
<ol>
<li> "pluginName": the name of the plugin. Seems to be "dummy" for the search results window, and "Notepad++::InternalFunction" for other dockable windows.
</li>
<li> "id": command id of the command to run at startup for the plugin, -1 if none. The dock manager records this information whenever a plugin opens a dockable window. "id" is 44070 for the vertical file switcher, 44084 for Function List and 44081/2/3 for the project panels.
</li>
<li> "curr": current docking position
</li>
<li> "prev": previous docking position, -1 if none
</li>
<li> "isVisible": "yes" / "no".
</li>
</ol>
<p>An &lt;ActiveTabs&gt; tag has the following attributes:
</p>
<ol>
<li> "cont": either 0 (left), 1 (top), 2 (right), 3 (bottom) or anything above 4 (undocked, corresponds to a &lt;FloatingWindow&gt; tag).
</li>
<li> "ActiveTab": the cont attribute actually refers to a tabbed container for possibly several windows. The value is -1 when container is empty. Otherwise, it is the active tab for the container.
</li>
</ol>
<h4>&lt;FindHistory&gt;</h4>
<p>Here are the attributes of the node:
</p>

 Attributes for the &lt;FindHistory&gt; node


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> nbMaxFindHistoryPath </td>
<td> integer </td>
<td> Maximal number of search folders being remembered
</td></tr>
<tr>
<td> 2 </td>
<td> nbMaxFindHistoryFilter </td>
<td> integer </td>
<td> Maximum number of filter strings remembered
</td></tr>
<tr>
<td> 3 </td>
<td> nbMaxFindHistoryFind </td>
<td> integer</td>
<td>  Maximum number of search patterns being remembered
</td></tr>
<tr>
<td> 4 </td>
<td> nbMaxFindHistoryReplace </td>
<td> integer </td>
<td> Maximum number of replace patterns being remembered
</td></tr>
<tr>
<td> 5 </td>
<td> matchWord= "</td>
<td> "yes"/"no" </td>
<td> State of the Whole words checkbox ("yes" = checked)
</td></tr>
<tr>
<td> 6 </td>
<td> matchCase </td>
<td>"yes"/"no" </td>
<td> State of the Match case checkbox ("yes" = checked)
</td></tr>
<tr>
<td> 7 </td>
<td> wrap </td>
<td>"yes"/"no" </td>
<td> State of the Wrap around  checkbox ("yes" = checked)
</td></tr>
<tr>
<td> 8 </td>
<td> directionDown </td>
<td>"yes"/"no" </td>
<td> Search direction ("yes" = the Down radio button is checked)
</td></tr>
<tr>
<td> 9 </td>
<td> fifRecuisive </td>
<td>"yes"/"no" </td>
<td> State of the In all subfolders checkbox ("yes" = checked)
</td></tr>
<tr>
<td> 10 </td>
<td> fifInHiddenFolder </td>
<td>"yes"/"no" </td>
<td> State of the In hidden folders checkbox ("yes" = checked)
</td></tr>
<tr>
<td> 11 </td>
<td> dlgAlwaysVisible </td>
<td>"yes"/"no" </td>
<td> "yes" if the dialog cannot be obscured, else "no"
</td></tr>
<tr>
<td> 12 </td>
<td> fifFilterFollowsDoc </td>
<td> "yes"/"no" </td>
<td> "yes" if the search filter should change with the active document, else "no"
</td></tr>
<tr>
<td> 13 </td>
<td> fifFolderFollowsDoc </td>
<td> "yes"/"no" </td>
<td> "yes" if the search path should change with the active document, else "no"
</td></tr>
<tr>
<td> 14 </td>
<td> searchMode </td>
<td> integer </td>
<td> <p>
</p><ul>
<li> 0 for Normal mode
</li>
<li> 1 for Extended mode
</li>
<li> 2 for Regular expression mode
</li>
</ul>
<p></p>
</td></tr>
<tr>
<td> 15 </td>
<td> transparencyMode </td>
<td> integer </td>
<td> <p>
</p><ul>
<li> 0 if the Transparency checkbox is clear
</li>
<li> 1 if it is checked, and the On lose focus radio button is checked
</li>
<li> 2 if it is checked, and the Always radio button is checked
</li>
</ul>
<p></p>
</td></tr>
<tr>
<td> 16 </td>
<td> transparency </td>
<td> integer </td>
<td> In the 1..255 range. The smaller it is, the less visible the dialog box is when transparency applies.
</td></tr></tbody></table>
<p>Note that, as of 6.6.6, the attributes 11 to 13 are not individually configurable through user interface. The "Follow Doc" checkbox allows to set 12 and 13 to a common value however. Also note that the state of the Mark line, Style found token , Purge for each search and In selection checkboxes is not remembered in this file - they are not persistent.
</p><p>Inside this node are tags that describe the contents of the 4 combo boxes in the dialog. They are all short tags with a name attribute. They appear in the following order:
</p>
<ol>
<li> &lt;Path&gt; tags
</li>
<li> &lt;Filter&gt; tags
</li>
<li>&lt;Find&gt; tags
</li>
<li> &lt;Replace&gt; tags
</li>
</ol>
<p>The lists are simply contiguous. The number of &lt;Path&gt; tags should not be greater than the nbMaxFindHistoryPath enclosing attribute, and similarly for the other tags.
</p>
<h4>&lt;History&gt;</h4>
<p>This node has a nbMaxFile integer attribute, the maximal number of files being remembered. The node is short, i.e. auto-closed, if there is no remembered file (new documents don't count). Otherwise, it has &lt;File&gt; tags with a filename attribute. Again, their number should not exceed the nbMaxFile enclosing attribute.
</p>
<h4>&lt;ProjectPanels&gt;</h4>
<p>Yhis tag contains &lt;ProjectPanel&gt; tags. &lt;ProjectPanel&gt; is autoclosing and has two mandatory attributes:
</p>
<ol>
<li><i>id</i>: the number of the panel. Valid values are 1, 2 and 3. Each of the valid IDs must be mentioned only once.
</li>
<li><i>workspaceFile</i>: the absolute path to the worspace file holding the corresponding panel's contents, or "" if not in use.
</li>
</ol>
<h4>&lt;FileEditViewHistory&gt;</h4>
<p>This is used to keep fold and bookmark states so as torestore them upon re-opening the file. Attribute are:
</p>
<ol>
<li>FileEditViewHistoryRestoreEnabled: "True" or "False".
</li>
<li>nbMaxFile: 20 by default
</li>
<li>activeMainIndex: 0 (not fully implemented)
</li>
</ol>
<p>Follow &lt;File&gt; tags similar to those in the session file. However fold state is not recorded there.
</p><p>Please note that the (invisible as of 6.6.6) checkbox for enabling view restore for individual files should not be checked wihile "Remember last session" is.
</p>
<h3>Keyboard shortcuts: shortcuts.xml</h3>
<p>This file has the following nodes:
</p>
<ol>
<li> &lt;InternalCommands&gt;: Notepad++ menu commands that were remapped
</li>
<li> &lt;Macros&gt;: Current macro set as it appears in the lower part of the Macro menu
</li>
<li> &lt;UserDefinedCommands&gt;: Contents of the Run menu
</li>
<li> &lt;PluginCommands&gt;: plugin commands that were remapped.
</li>
<li> &lt;ScintillaKeys&gt;: basic Scintilla commands, most of which relate to <a href="http://docs.notepad-plus-plus.org/index.php/Moving_And_Selecting_Around" title="Moving And Selecting Around">Moving And Selecting Around</a>, that were remapped.
</li>
</ol>
<p>The format of the contents of these nodes is detailed below. The user interface provided by Notepad++ is such that only the &lt;Macros&gt; section might need editing, under normal circumstances.
</p>
<h4>&lt;InternalCommands&gt;</h4>
<p>When not empty, the node contains &lt;Shortcut&gt; tags, the order of which doesn't matter.
</p>

 Attributes for the &lt;Shortcut&gt; node


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> id </td>
<td> integer </td>
<td> The command id associated with the menu entry. The complete list of these is to be found in the menuCmdIds.h source file.
</td></tr>
<tr>
<td> 2 </td>
<td> Ctrl </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Control modifier
</td></tr>
<tr>
<td> 3 </td>
<td> Alt </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Alt modifier
</td></tr>
<tr>
<td> 4 </td>
<td> Shift </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Shift modifier
</td></tr>
<tr>
<td> 5 </td>
<td> Key </td>
<td> integer </td>
<td> The base virtual key number, in the 1.255 range
</td></tr></tbody></table>
<h4>&lt;Macros&gt;</h4>
<p>When not empty, this node is made of &lt;Macro&gt; nodes, each of which represents an individual macro. Each &lt;Macro&gt; holds a nonempty list of &lt;Action&gt; tags which represent individual macro steps. These steps are either Scintilla commands or Notepad++ commands, not raw keystrokes. For more details on macro recording, see <a href="http://docs.notepad-plus-plus.org/index.php/Macros" title="Macros">Macros</a>.
</p><p>The order of &lt;Macro&gt; nodes is reflected in the lower part of the Macro menu, and is otherwise not important. Order of &lt;Action&gt; tags, in contrast, is usually crucial.
</p>

 Attributes for the &lt;Macro&gt; node


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> name </td>
<td> string </td>
<td> The name of the macro. Several macros may have the same name
</td></tr>
<tr>
<td> 2 </td>
<td> Ctrl </td>
<td> "yes"/"no" </td>
<td> The key being mapped to has the Control modifier
</td></tr>
<tr>
<td> 3 </td>
<td> Alt </td>
<td> "yes"/"no" </td>
<td> The key being mapped to has the Alt modifier
</td></tr>
<tr>
<td> 4 </td>
<td> Shift </td>
<td> "yes"/"no" </td>
<td> The key being mapped to has the Shift modifier
</td></tr>
<tr>
<td> 5 </td>
<td> Key </td>
<td> integer </td>
<td> The base virtual key number, in the 1..255 range
</td></tr></tbody></table>
<p>Although it is possible for several macros to share the same shortcut, this practice is highly discouraged.
</p>

 Attributes for the &lt;Action&gt; tag


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> type </td>
<td> integer </td>
<td> <p>
</p><ul>
<li> 0 for Scintilla messages that do not pass a string as second parameter
</li>
<li> 1 for Scintilla messages that pass a string as second parameter
</li>
<li> 2 for Notepad++ defined commands
</li>
<li> 3 for search and replace recording
</li>
</ul>
<p></p>
</td></tr>
<tr>
<td> 2 </td>
<td> message </td>
<td> integer </td>
<td> 0 if type=2, else message id. The complete list of message ids can be found in the <a rel="nofollow" class="external text" href="http://scintilla.cvs.sourceforge.net/viewvc/scintilla/scintilla/include/Scintilla.iface?view=markup">Scintilla.iface</a> source file.
</td></tr>
<tr>
<td> 3 </td>
<td> wParam </td>
<td> integer </td>
<td> Command id when type=2 or 3, else actual first parameter of the message. Use 0 if not used.
</td></tr>
<tr>
<td> 3 </td>
<td> lParam </td>
<td> integer</td>
<td> 0 unless type=0 and the second parameter of the message is actually used, or scalar value used when type is 3.
</td></tr>
<tr>
<td> 4 </td>
<td> sParam </td>
<td> string </td>
<td> "" unless type=1 or 3, in which case this is the string pointed by the second parameter of the message
</td></tr></tbody></table>
<p>Thus, global properties cannot be modified in this manner, because the corresponding messages pass a string in the first parameter. Any Scintilla or Windows message that does not return a value, passes an integer in wParam and either an integer or string in lParam will do. The full list of Scintilla messages, as well as a concise documentation, can be found in &lt;source folder&gt;\Scintilla/include/Scintillla.iface.
</p>
<h5>Search / Replace encoding</h5>
<p>Single search and replace operations are encoded as a series of actions with type = 3. They follow a fixed sequence with optional middle extra actions, as shown here:
</p>
<ul>
<li> First coes
</li>
</ul>
<pre>&lt;Action type="3" message="1700" wParam="0" lParam="0" sParam="" /&gt;
</pre>
<p>which carries ouy some required initialisation.
</p>
<ul>
<li> then comes the search pattern in the sParam field:
</li>
</ul>
<pre>&lt;Action type="3" message="1601" wParam="0" lParam="0" sParam="searched" /&gt;
</pre>
<ul>
<li> then the search type, encoded in lParam:
</li>
</ul>
<pre>&lt;Action type="3" message="1625" wParam="0" lParam="0" sParam="" /&gt;
</pre>
<p>Search type is 0 for normal, 1 for extended, 2 for regexp.
</p>
<ul>
<li> then, if a replacement operation, the replace string as sParam:
</li>
</ul>
<pre>&lt;Action type="3" message="1602" wParam="0" lParam="0" sParam="replacing" /&gt;
</pre>
<ul>
<li> then, if performing a Find/Replace in Files, the root folder for the search, followed by the extension filter string, both in the sParam field:
</li>
</ul>
<pre>&lt;Action type="3" message="1653" wParam="0" lParam="0" sParam="C:\Program Files\Notepad++\" /&gt;
&lt;Action type="3" message="1652" wParam="0" lParam="0" sParam="*.*" /&gt;
</pre>
<ul>
<li> then comes an option list in lParam; the table below explains the flags this value is the sum of:
</li>
</ul>
<pre>&lt;Action type="3" message="1702" wParam="0" lParam="96" sParam="" /&gt;
</pre>
<ul>
<li> finally, the command to execute, in lParam.
</li>
</ul>
<pre>&lt;Action type="3" message="1701" wParam="0" lParam="1660" sParam="" /&gt;
</pre>
<p>Flag values when message = "1702":
</p>

 Yes/No option flags


 Value

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> Whole word matches only
</td></tr>
<tr>
<td> 2 </td>
<td> Case sensitive matches
</td></tr>
<tr>
<td> 4 </td>
<td> Clear styling on each Find All
</td></tr>
<tr>
<td> 8 </td>
<td> Stle found token checked
</td></tr>
<tr>
<td> 16 </td>
<td> Mark line checked
</td></tr>
<tr>
<td> 32 </td>
<td> Search in subfolders checked
</td></tr>
<tr>
<td> 64 </td>
<td> Search hidden items checked
</td></tr>
<tr>
<td> 128 </td>
<td> In selection checked
</td></tr>
<tr>
<td> 256 </td>
<td> Wrap search
</td></tr>
<tr>
<td> 512 </td>
<td> Search goes upwards
</td></tr></tbody></table>
<p><br>
</p>

 Command codes when message = "1701"


 Value

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> Find
</td></tr>
<tr>
<td> 1608 </td>
<td> Replace
</td></tr>
<tr>
<td> 1609 </td>
<td> Replace All
</td></tr>
<tr>
<td> 1614 </td>
<td> Count
</td></tr>
<tr>
<td> 1615 </td>
<td> Find All
</td></tr>
<tr>
<td> 1635 </td>
<td> Replace in all opened documents
</td></tr>
<tr>
<td> 1636 </td>
<td> Find in all opened documents
</td></tr>
<tr>
<td> 1641 </td>
<td> Find all in current document
</td></tr>
<tr>
<td> 1656 </td>
<td> Find in Files
</td></tr>
<tr>
<td> 1660 </td>
<td> Replace in FIles
</td></tr></tbody></table>
<h4>&lt;UserDefinedCommands&gt;</h4>
<p>When not empty, this node contains &lt;Command&gt; tags, which have the command string as contents. Their order is reflected in the Run menu, otherwise it doesn't matter.
</p>

 Attributes for the &lt;Command&gt; tag


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> name </td>
<td> string </td>
<td> The name of the Run command. Several commands may have the same name
</td></tr>
<tr>
<td> 2 </td>
<td> Ctrl </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Control modifier
</td></tr>
<tr>
<td> 3 </td>
<td> Alt </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Alt modifier
</td></tr>
<tr>
<td> 4 </td>
<td> Shift </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Shift modifier
</td></tr>
<tr>
<td> 5 </td>
<td> Key </td>
<td> integer </td>
<td> The base virtual key number, in the 1.255 range
</td></tr></tbody></table>
<p>Use the ^ or | concatenation character as appropriate to have the OS execute several commands in a row. The commands use the same syntax and helper environment variables as explained in <a href="http://docs.notepad-plus-plus.org/index.php/External_Programs" title="External Programs">External Programs</a>.
</p>
<h4>&lt;PluginCommands&gt;</h4>
<p>When not empty, this node is made of auto-closed &lt;PluginCommand&gt; tags. Their order doesn't matter.
</p>

 Attributes for the &lt;PluginCommmand&gt; tag


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> moduleName </td>
<td> string </td>
<td> The name with extension of the dll that contains the plugin
</td></tr>
<tr>
<td> 2 </td>
<td> internalID </td>
<td> integer </td>
<td> The command number in the plugin. This can be assessed by counting the position of the corresponding menu item in the plugin submenu (separators count for one entry). Then substract 1 as ID's start at zero.
</td></tr>
<tr>
<td> 3 </td>
<td> Ctrl </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Control modifier
</td></tr>
<tr>
<td> 4 </td>
<td> Alt </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Alt modifier
</td></tr>
<tr>
<td> 5 </td>
<td> Shift </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Shift modifier
</td></tr>
<tr>
<td> 6 </td>
<td> Key </td>
<td> integer </td>
<td> The base virtual key number, in the 1.255 range
</td></tr></tbody></table>
<p>The order in which TextFX functions are loaded is not obvious from the menu layout. However, you can compute the internalID of a function as follows:
</p>
<ol>
<li> Go to Settings -&gt; Shortcut mapper -&gt; Plugin commands
</li>
<li> Note the index of the function you are after
</li>
<li> Substract the index for I:TEXTFX NULL FUNCTION. This depends on what plugins you have and in which order they were loaded.
</li>
<li> Add 2 to the result to get the correct internalID.
</li>
</ol>
<p>A similar method will work for other plugins, but the value to substract is the index of the first entry for the plugin, and you must not add any correction. Remember that a separator is just another entry.
</p>
<h4>&lt;ScintillaKeys&gt;</h4>
<p>When it is not empty, this node contains &lt;ScintKey&gt; and &lt;NextKey&gt;  tags. Each &lt;ScintKey&gt; tag correspond to a Scintilla command being remapped. The order of these tags doesn't matter.
</p><p>When a Scintilla command has several keyboard bindings, the first one to be defined is stored in a &lt;ScintKey&gt; tag. The extra bindings are stored in &lt;NextKey&gt; tags that follow the main &lt;ScintKey&gt;, in the order defined by the list on the left of the Modify dialog for the entry.
</p>

 Attributes for the &lt;ScintKey&gt; tag


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> ScintId </td>
<td> integer </td>
<td> The id of the message being remapped
</td></tr>
<tr>
<td> 2 </td>
<td> menuCmdID </td>
<td> integer </td>
<td> The command number associated to the message, if there is any. Use 0 if this message is not a Notepad++ menu command
</td></tr>
<tr>
<td> 3 </td>
<td> Ctrl </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Control modifier
</td></tr>
<tr>
<td> 4 </td>
<td> Alt </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Alt modifier
</td></tr>
<tr>
<td> 5 </td>
<td> Shift </td>
<td> "yes"/"no" </td>
<td> The key mapped to has the Shift modifier
</td></tr>
<tr>
<td> 6 </td>
<td> Key </td>
<td> integer </td>
<td> The base virtual key number, in the 1.255 range
</td></tr></tbody></table>
<p>&lt;NextKey&gt; tags have the same structure as a &lt;ScintKey&gt;, except that the first two attributes are not defined - they would be redundant.
</p>
<h3>Built-in language features</h3>
<h4>Keyword lists: langs.xml</h4>
<p>This file, inside the mandatory &lt;NotepadPlus&gt; tag, contains a single &lt;Languages&gt; node, made of &lt;Language&gt; nodes.
</p><p>Each &lt;Language&gt; node has one or more &lt;Keywords&gt; tags. These tags have a name attribute. They contain keyword lists, which are space separated and sorted lists of keywords. The intervening space is not required between two keywords if one ends in a non letter character and so starts the next one.
</p><p>The order of the &lt;Language&gt; tags is reflected in the Language menu. Otherwise it doesn't matter. It is however suggested to keep them/the menu sorted.
</p>

 Attributes for the &lt;Language&gt; node


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> name </td>
<td> string </td>
<td> The name of the language.
</td></tr>
<tr>
<td> 2 </td>
<td> ext </td>
<td> string </td>
<td> The list of file extensions associated to this language by default. Lists are space separated, without leading periods.
</td></tr>
<tr>
<td> 3 </td>
<td> commentLine </td>
<td> string </td>
<td> The character(s) that prelude a comment extending to the end of the physical line. Use "" if the feature is not supported.
</td></tr>
<tr>
<td> 4 </td>
<td> commentStart </td>
<td> string </td>
<td> The character(s) that start a block comment. Use "" if the feature is not supported.
</td></tr>
<tr>
<td> 5 </td>
<td> commentEnd </td>
<td> string </td>
<td> The character(s) that end a block comment. Use "" if the feature is not supported.
</td></tr>
<tr>
<td> 6 </td>
<td> exclude </td>
<td> "yes"/"no" </td>
<td> Set to yes" to remove from the Language menu, else "no" or no attribute.
</td></tr>
<tr>
<td> 7 </td>
<td> tabSettings </td>
<td> integer </td>
<td> If present, the value encodes the number of spaces a tab is equivalent to: value + 128 if the Replace tabs vy spaces is checked, else raw value. The default value of 4 is used if attribute is absent.
</td></tr></tbody></table>
<h4>Highlighting schemes: stylers.xml</h4>
<p>The mandatory &lt;NotepadPlus&gt; node contains a &lt;LexerTypes&gt; and a &lt;GlobalStyles&gt; node. The &lt;LexerTypes&gt; node contains &lt;LexerType&gt; nodes whose order and name must match the &lt;Language&gt; nodes found in langs.xml. The &lt;ClobalStyles&gt; node behaves like a special &lt;LexerType&gt;.
</p><p>The user interface in Settings -&gt; Styler Configurator is so complete as to make manual edits for this file unneeded, under normal circumstances.
</p><p>The attributes of a &lt;LexerType node are:
</p>
<ol>
<li> name: a string, the language name
</li>
<li> desc: a string, displayed in the status bar when this lexer is being used.
</li>
<li> ext: a string, the list of user defined file extensions to associate with the lexer. The lists are space separated, without leading periods.
</li>
</ol>
<p>Each &lt;LexerType&gt; contains one or more &lt;WordStyle&gt; tag. Their order and style ID must not be changed, as they reflect the internal lexer's code.
</p>

 Attributes for the &lt;WordStyle&gt; tag


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> name </td>
<td> string </td>
<td> The name of the style being defined, usually in upper case
</td></tr>
<tr>
<td> 2 </td>
<td> styleID  </td>
<td> integer </td>
<td> The internal Scintilla style ID. Do not change this attribute unless you recompile SciLexer.dll and perform corresponding changes in its code
</td></tr>
<tr>
<td> 3 </td>
<td> fgColor </td>
<td> hex integer </td>
<td> The RGB representation of the foreground color to use for this sort of token
</td></tr>
<tr>
<td> 4 </td>
<td> bgColor </td>
<td> hex integer </td>
<td>  The RGB representation of the background color to use for this sort of token
</td></tr>
<tr>
<td> 5 </td>
<td> fontName </td>
<td> string </td>
<td> The name of the font face to display this token with. Use "" for default font.
</td></tr>
<tr>
<td> 6 </td>
<td> fontStyle </td>
<td> integer </td>
<td> Flags or'ed together to summarise the properties of the font (bold=1, italic=2, underlined=4).
</td></tr>
<tr>
<td> 7 </td>
<td> fontSize </td>
<td> integer </td>
<td> Size in points of the font to be used to display this token. Use "" for default size.
</td></tr>
<tr>
<td> 8 </td>
<td> keywordClass </td>
<td> string </td>
<td> Use this style to display words from the word list with the same name in langs.xml. Do not specify if not applicable.
</td></tr></tbody></table>
<p>The &lt;WordStyle&gt; tags in the &lt;GlobalStyles&gt; node describe elements for which some of the attributes above do not apply, like font data for the Fold margin. In that event, they are left out. They have usually no contents, and as such come in short form.
</p><p>However, if custom keywords are added to the language, the list of space separated words is the contents, and the tag takes a long form instead.
</p><p>The same considerations apply to theme files, which are alternates stylers.xml.
</p>
<h3>The context menu</h3>
<p>The way to customise the <a href="http://docs.notepad-plus-plus.org/index.php/Context_Menu" title="Context Menu">Context Menu</a> is explained in detail there.
</p>
<h3>Toolbar icons</h3>
<p>The way to customise toolbar icons is explained in detail <a href="http://docs.notepad-plus-plus.org/index.php/Toolbar_Customisation" title="Toolbar Customisation"> here</a>.
</p>
<h3>Session files</h3>
<p>There may be as many session files as you like, but, if remembering the current session is enabled, the session.xml will always record this data when Notepad++ terminates normally.
</p><p>Inside the &lt;NotepadPlus&gt; node, there is only one &lt;Session&gt; node. It has one activeView attribute, which is "0" if the main view was holding the active document buffer, and "1" if the secondary view did.
</p><p>The &lt;Session&gt; node has a &lt;MainView&gt; and &lt;SubView&gt; node, which have the same structure. They have an activeID integer attribute which is the index of the active tab for the view. This is 0 if the view does not exist.
</p><p>Each view node has zero or more &lt;File&gt; tags. If the view has no files, the node is auto-closed. Since the active index relates to the order in which the File tags are listed, it is best not to change that order.
</p>

 Attributes for the &lt;File&gt; tag


 Position

 Name

 Value format

 Meaning
<table border="1"><tbody><tr></tr>
<tr>
<td> 1 </td>
<td> firstVisibleLine </td>
<td> integer </td>
<td> 0-based index of the first visible line
</td></tr>
<tr>
<td> 2 </td>
<td> xOffset </td>
<td> integer </td>
<td> 0-based offset of the first visible character on an given line
</td></tr>
<tr>
<td> 3 </td>
<td> scrollWidth </td>
<td> integer </td>
<td> reference width in pixels to compute the horizontal thumb width
</td></tr>
<tr>
<td> 4 </td>
<td> startPos </td>
<td> integer </td>
<td> position of first styled character
</td></tr>
<tr>
<td> 5 </td>
<td> endPos </td>
<td> integer </td>
<td> position of the last styled character
</td></tr>
<tr>
<td> 6 </td>
<td> lang </td>
<td> string </td>
<td> Name of the language being used to highlight the document
</td></tr>
<tr>
<td> 7 </td>
<td> filename </td>
<td> string </td>
<td> full path and name of file
</td></tr></tbody></table>
<p>When a file does not have bookmarks or collapsed fold points, the corresponding File tag is auto-closed. Otherwise, it contains zero or more  auto-closed tags having a "line" attribute, the value of which is the <b>0-based</b> line number of the marker, and zero or more &lt;Fold&gt; tags with a 0-based "line" number for each collapsed fold point. Hidden lines are not being recorded as of v6.6.6.
</p>
<h3>User defined languages: userDefineLang.xml</h3>
<p>(requires in-depth review, wait till UDL 3.0 perhaps)
</p><p>The User Define Language panel should make it useless to edit this file, under normal circumstances.
</p><p>The mandatory &lt;NotepadPlus&gt; node may have one or more &lt;UserLang&gt; nodes.
</p><p>The &lt;UserLang&gt; nodes have two attributes:
</p>
<ol>
<li> name: a string, the language name
</li>
<li> ext: a string, the space separated list of file extensions associated to this lexer, without leading period
</li>
</ol>
<p>These nodes have three nodes, the structure of which is described below:
</p>
<ol>
<li> &lt;Settings&gt;
</li>
<li> &lt;Keywords&gt;
</li>
<li> &lt;WordStyle&gt;
</li>
</ol>
<h4>&lt;Settings&gt;</h4>
<p>This node has:
</p>
<ol>
<li> A &lt;Global&gt; auto-closed tag, with
<ol>
<li> caseIgnore,a "yes"/"no" attribute. Set to "yes" if the language is case insensitive, else "no".
</li>
<li> escapeChar: this attribute is a string at most one character long. If absent or empty, the language does not support an escape character. Otherwise features the escape character.
</li>
</ol>
</li>
<li> A &lt;TreatAsSymbol&gt; auto-closed tag, with two "yes"/"no" attributes, comment and commentLine. They reflect the state of the corresponding checkbox.
</li>
<li> A &lt;Prefix&gt; tag, with 4 "yes"/"no" attributes named words1 to words4. They reflect the prefix status of each word group.
</li>
</ol>
<h4>&lt;KeywordLists&gt;</h4>
<p>They reflect the various lists on the panel. Its &lt;Keywords&gt; tags have the same format as their counterparts in langs.xml.
</p>
<h4>&lt;Styles&gt;</h4>
<p>This node has &lt;WordStyle&gt; tags which have the same function and format as their counterparts in stylers.xml.
</p>
<h3>Autocompletion, aka API, files</h3>
<p>API files are located in the plugins\APIs\ subfolder of the Notepad++ installation folder. These files are optional: you need only one for each language for which you'll use <a href="http://docs.notepad-plus-plus.org/index.php/Auto_Completion" title="Auto Completion">Auto Completion</a> or calltips. They are also supported for User Defined Languages, and bear the name &lt;Language name&gt;.xml.
</p><p>Under the usual &lt;NotepadPlus&gt; tag is a &lt;AutoComplete&gt; tag. It has an optional, unused "language" attribute, which you can use for any descriptive purpose.
</p><p>The contents of a &lt;AutoComplete&gt; start with an autoclosing &lt;Environment&gt; tag, with the following attributes:
</p>
<ol>
<li> ignoreCase: "no" if the language is case sensitive, else "yes" (default).
</li>
<li> startFunc: the character(s) which start the parameter list. Default is "(".
</li>
<li> stopFunc: the character(s) which end the parameter list. Default is ")".
</li>
<li> paramSeparator: the character(s) which separate parameters. Defaults to ",".
</li>
<li> terminal: the character(s) which mark the end of a prototype, when the language allows C-style separate prototyping. Defaults to ";". Leave it out if the language does not support separate prototyping, or set it to some illegal character.
</li>
<li> additionalWordChar: character(s) that may be part of words and which are not a lower or upper case letter, a digit or the underscore. The value is a string with all these extra characters, in any order and without separators. The string is empty by default.
</li>
</ol>
<p>NOTE: Spaces can't be used as the character for the attributes and additionalWordChar is still not working (Notepad++ v.6.5.2) but maybe in future releases...
</p><p><br>
Any attribute can be omitted, and the &lt;Environment&gt; tag as well. The practice is not recommended though.
</p><p>Following is a list of &lt;KeyWord&gt; tags. They are either auto-closing, for keywords that are not routines, or not when they are. Each such tag has a mandatory "name" attribute, the keyword/routine name to recognise. The list <b>must be sorted according to this attribute and the value of the &lt;Environment&gt; ignoreCase attribute</b>. See subsections below for more on keyword names and sorting.
</p><p>When a &lt;KeyWord&gt; tag is not auto-closing, it must have a second attribute, "func", set to "yes". The contents are a nonempty, unsorted list of &lt;Overload&gt; tags, each of which describes a possible signature for the routine. &lt;Overload&gt; has a "retVal" attribute, which you would set to the initial comment in the call tip. In C/C++, this traditionally would be the return type; "" is a permitted value. Furthermore, the &lt;Overload&gt; tag has an optional "descr" attribute, which can be used to add a description of the function. Tip: You can use &amp;#x0a; to insert line breaks.
</p><p>An &lt;Overload&gt; tag contains one or more parameter description, sorted in occurrence order. Such description is represented by an auto-closing &lt;Param&gt; tag with a "name" attribute. This may contain a parameter name or other useful comments.
</p><p>The parameter names (actually any text you like, it may even mention a parameter name), return value and description have to fit into an internal buffer, truncation occurs otherwise. For any given function, all text, plus 2 bytes per parameter, plus 24 bytes if 2 overloads or more, can't spill over 2,043 bytes. Remember that a byte is a byte, so formatting whitespace competes with actual text.
</p><p>A typical example of entry could be this:
</p>
<pre>       &lt;KeyWord name="cos" func="yes" &gt;
           &lt;Overload retVal="{double}" descr="Cosine of x" &gt;
               &lt;Param name="x, radians" /&gt;
           &lt;/Overload&gt;
       &lt;/KeyWord&gt;
</pre>
<p>resulting in the following call tip:
</p>
<pre>{double} cos (x, radians)
Cosine of x
</pre>
<p>Remember that the call tip shows up when you type the opening parenthesis after the routine name. Default "(" or whatever set with startFunc in the &lt;Environment&gt; tag.
</p>
<h4>Names</h4>
<p>For both call tips and autocompletion to work, keywords must be words, ie identifiers most languages would readily accept. This means that only the 26 Latin alphabet letters in either lower or upper case (no diacritics), digits and the underscore are safe to use. Additional allowed characters will work if they are not whitespace. Autocompletion may cope with spaces or blanks, call tips won't. This is a Scintilla limitation.
</p>
<h4>Sorting</h4>
<p>The &lt;KeyWord&gt; tag list must be sorted by "name" in ascending order. <b>Failure to do so will result in a non working file, without a warning</b>.
</p><p>Now which sorting, case sensitive or insensitive? It depends on the value of the ignoreCase &lt;Environment&gt; attribute. If set to "yes", use case insensitive sorting, which considers all letters to be in upper case. Otherwise, use case sensitive sorting.
</p><p>The simplest way to build a new file might be this:
</p>
<ol>
<li> in a new document, list all keywords to be recognised;
</li>
<li> use TextFX to sort the list with the right ordering;
</li>
<li> Using the Column Editor, add &lt;KeyWord name=" in front of each line.
</li>
<li> Using extended mode replace, add "/&gt; at the end of all lines. Or use TextFX's Insert (Clipboard) through lines;
</li>
<li> Add some fancy character ('+' is a good candidate) to the end of lines that represent functions;
</li>
<li> Using extended mode, replace /&gt;+\r\n by &gt;\r\n\t&lt;Overload retVal=""&gt;\r\n\t&lt;/Overload&gt;\r\n&lt;/KeyWord&gt;\r\n You may prefer using TextFX's Find/Replace;
</li>
<li> Now manually add text and extra overloads. Reindent as applicable;
</li>
<li> Save and test your file;
</li>
<li> Sloppy work, test again (recursive, beware of infinite loops).
</li>
</ol>
<h3>Workspace files</h3>
<p>The project maneger stores its contents in workspace files, which may bear any name or extension.
</p><p>Inside the &lt;NotepadPlus&gt; usual tag are &lt;Project&gt; tags, which may contain any mix and match of &lt;Folder&gt; and &lt;File&gt; tags, all with a mandatory <i>name</i> attribute. A &lt;Folder&gt; can have the same sort of contents as a &lt;Project&gt;. &lt;File&gt; is autoclosing.
</p><p>There are two sorts of names, file names and other names. The latter are arbitrary, while the fie names, only found as <i>name</i> attribute for &lt;File&gt;, refer to a path relative to where the workspace file is. As a result, moving a workspace file is not recommended, because all files are lost track of.
</p>
<h3>FunctionList</h3>
<p>This section describes the contents of the functionList.xml file, which defines parsing rules used for building the source item tree displayed by the <a href="http://docs.notepad-plus-plus.org/index.php/Function_List" title="Function List">Function List</a> feature. Active contents appear inside a &lt;functionList&gt; tag inside the ubiquitous &lt;NotepadPlus&gt; tag.
</p>
<h4>Associations</h4>
<p>First comes an &lt;associationMap&gt; tag, which contains one or more &lt;association/&gt;. Each &lt;association/&gt; has two attributes: langID and id.
The former is a built-in language ID, the list of which is included in the default functionList.xml. The second is a name of your choice. The meaning of the tag is that the parser with said name applies to source files highlighted as the language with langID identifier. If several associations reference the same language, the topmost one wins.
</p><p>Instead of a langID, you can specify an ext attribute, which is a string containing a single extension for files the parser will apply to - so you need as many associations to the same parser id as there are extensions it applies to. Files without an extension are associated with ext=""; otherwise the string must have a leading dot.
</p>
<h4>Parsers</h4>
<p>Next comes a &lt;parsers&gt; tag containing one or more &lt;parser&gt; tags.
</p><p>Parsers come in two basic flavors: classRange or function. A parser may contain either one, or both.
</p><p>A parser has an id (which is supposed to match the id of some &lt;association/&gt;), a displayName, which will be shown on he panel, and a commentExpr regular expression. Areas matched by this expressions will be ignored in parsing anything else.
</p>
<h5>&lt;function&gt; parsers</h5>
<p>A &lt;function&gt; has a single attribute, mainExpr, which is a regular expression matching the declaring part of the function, up to the start of its body. The default file adds a displayMode attribute to most &lt;function&gt; and &lt;classsRange&gt; parsers, but it does not appear to be used anywhere as of v6.6.6.
</p><p>It contains a single &lt;functionName&gt; container tag, which contains one or more &lt;funcNameExpr/&gt; tag(s). Each of these has a single expr attribute, which is a regular expression. To find the name of a function, each expr attributes is searched in turn in the data mainExpr matched. First non empty result displays as the function name.
</p>
<h5>&lt;classRange&gt; parsers</h5>
<p>The attributes and nested tags of a &lt;classRange&gt; parser mostly parallel those of a &lt;function&gt; parser, except that there are some extra attributes.
</p><p>The class header is whatever matches its mainExpr attribute. To extract the class name from this data, the &lt;className&gt; nested container tag is parsed. Each of its &lt;nameExpr/&gt; nested tags has an expr attribute, a regular expression that extracts the name from the header. &lt;classRange&gt; also has a displayMode attribute that does not seem to be in use.
</p><p>The &lt;classRange&gt; tag has two additional attributes, openSymbole and closeSymbole. Both are regular expressions which determine where the class body starts and ends. A function whose header is found inside a class body belongs to the class and its tree item has the class tree item as its parent.
</p>
