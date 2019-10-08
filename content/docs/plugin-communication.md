---
title: Plugin Communication
linktitle: plugin-communication
weight: 92
---

## Plugin Communication: Messages and Notifications

When writing a [plugin](../plugins/), you need to communicate with the Notepad++ application, to get information from it or instruct it to do some task.  This is done using messages and notifications.

These same techniques can also be used for editing [macros](../macros/) (some of which use messages to control Notepad++), or when using one of the scripting plugins (which effectively make your script a mini-plugin).

### Why both messages <i>and</i> notifications?

Basically, a message may have a return value, and is usually thought as a query, though it can also command actions inside Notepad++. A notification simply informs of some event, and is more usually thought as a command.  However, a notification is sent using a Windows message, [`WM_NOTIFY`](https://docs.microsoft.com/en-us/windows/win32/controls/wm-notify), so the interface is similar.  The extra content of the messages and notifications are different from each other, and are described in their respective sections, below.

## Notepad++ messages

When a message is sent to Notepad++, you send the message ID, and two parameters – known as wParam and lParam. The values placed in those two parameters depend on the message, and are explained below.

The message IDs for each of these named messages can be found in the source code in [Notepad_plus_msgs.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/MISC/PluginsManager/Notepad_plus_msgs.h).

You can also communicate to the Scintilla editor instances inside Notepad++ by using the Scintilla messages, which are [documented at the Scintilla website](https://www.scintilla.org/ScintillaDoc.html), and the values can be found in [Scintilla.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/scintilla/include/Scintilla.h).

<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETCURRENTSCINTILLA
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>
<p>[out] int * currentEdit
</p>
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  currentEdit indicates the current Scintilla view&nbsp;:
<ul>
<li> 0 is the main Scintilla view
</li>
<li> 1 is the second Scintilla view.
</li>
</ul>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETCURRENTLANGTYPE
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] int * langType
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  langType indicates the language type of current Scintilla view document&nbsp;: please see the enum LangType in "PluginInterface.h" for all possible value.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_SETCURRENTLANGTYPE
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] int langTypeToSet
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  langTypeToSet is used to set the language type of current Scintilla view document&nbsp;: please see the enum LangType in "PluginInterface.h" for all possible value.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETFULLCURRENTPATH
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] size_t fullPathLen
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] TCHAR * fullPath
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  fullPath receives the full path of current Scintilla view document. User is responsible to allocate (or use automatic variable) a buffer with an enough size. MAX_PATH is suggested to use.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETCURRENTDIRECTORY
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] size_t directoryPathLen
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] TCHAR * directoryPath
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  directoryPath receives the directory path of current Scintilla view document. User is responsible to allocate (or use automatic variable) a buffer with an enough size. MAX_PATH is suggested to use.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETFILENAME
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] size_t fileNameLen
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] TCHAR * fileName
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  fileName receives the file name of current Scintilla view document. User is responsible to allocate (or use automatic variable) a buffer with an enough size. MAX_PATH is suggested to use.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETNAMEPART
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] size_t namePartLen
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] TCHAR * namePart
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  namePart receives the part of name (without extension) of current Scintilla view document. User is responsible to allocate (or use automatic variable) a buffer with an enough size. MAX_PATH is suggested to use.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETEXTPART
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] size_t extensionLen
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] TCHAR * extension
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  extension receives the part of extension of current Scintilla view document. User is responsible to allocate (or use automatic variable) a buffer with an enough size. MAX_PATH is suggested to use.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETCURRENTWORD
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] size_t currentWordLen
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] TCHAR * currentWord
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  currentWord receives the word on which cursor is currently of current Scintilla view document. User is responsible to allocate (or use automatic variable) a buffer with an enough size. MAX_PATH is suggested to use.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETNPPDIRECTORY
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] size_t nppDirLen
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] TCHAR * nppDir
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  nppDir receives the full path of directory where located Notepad++ binary. User is responsible to allocate (or use automatic variable) a buffer with an enough size. MAX_PATH is suggested to use.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETNBOPENFILES
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] int nbType
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  The return value depends on nbType&nbsp;: <br>

 nbType

 Meaning
<table border="1">
<tbody><tr></tr>
<tr>
<td> ALL_OPEN_FILES </td>
<td>the total number of files opened in Notepad++
</td></tr>
<tr>
<td> PRIMARY_VIEW </td>
<td> the number of files opened in the primary view
</td></tr>
<tr>
<td> SECOND_VIEW </td>
<td> the number of files opened in the second view
</td></tr></tbody></table>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETOPENFILENAMES
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [out] TCHAR ** fileNames
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] int nbFile
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  nbFile is the size of your fileNames array. You should get this value by using NPPM_NBOPENFILES message with constant ALL_OPEN_FILES, then allocate fileNames array with this value.
<p>fileNames receives the full path names of all the opened files in Notepad++. User is responsible to allocate fileNames array with an enough size.
</p><p>The return value is the number of file full path names copied in fileNames array.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETOPENFILENAMESPRIMARY
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [out] TCHAR ** fileNames
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] int nbFile
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  nbFile is the size of your fileNames array. You should get this value by using NPPM_NBOPENFILES message with constant PRIMARY_VIEW, then allocate fileNames array with this value.
<p>fileNames receives the full path names of the opened files in the primary view. User is responsible to allocate fileNames array with an enough size. The return value is the number of file full path names copied in fileNames array.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETOPENFILENAMESSECOND
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [out] TCHAR ** fileNames
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] int nbFile
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  nbFile is the size of your fileNames array. You should get this value by using NPPM_NBOPENFILES message with constant SECOND_VIEW, then allocate fileNames array with this value.
<p>fileNames receives the full path names of the opened files in the second view. User is responsible to allocate fileNames array with an enough size.
</p><p>The return value is the number of file full path names copied in fileNames array.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_DOOPEN
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] TCHAR * fullPathName2Open
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  fullPathName2Open indicates the full file path name to be opened.
<p>The return value is TRUE (1) if the operation is successful, otherwise FALSE (0).
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_MODELESSDIALOG
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int op
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] HWND hDlg
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  For each created dialog in your plugin, you should register it (and unregister while destroy it) to Notepad++ by using this message. If this message is ignored, then your dialog won't react with the key stroke messages such as TAB key. For the good functioning of your plugin dialog, you're recommended to not ignore this message.
<p>hDlg is the handle of the dialog to be registed.
</p><p>op&nbsp;: the operation mode. MODELESSDIALOGADD is to register; MODELESSDIALOGREMOVE is to unregister.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_SAVECURRENTSESSION
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] const TCHAR *sessionFileName
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  You can save the current opened files in Notepad++ as a group of files (session) by using this message. Notepad++ saves the current opened files' full pathe names and their current stats in a xml file. The xml full path name is provided by sessionFileName.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_SAVESESSION
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] sessionInfo sessionInfomation
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  This message let plugins save a session file (xml format) by providing an array of full files path name. sessionInfomation is a structure defined as follows:
<dl>
<dt>&nbsp; TCHAR* sessionFilePathName;
</dt>
<dd> the full path name of session file to save
</dd>
<dt>&nbsp; int nbFile;
</dt>
<dd> the number of files in the session
</dd>
<dt>&nbsp; TCHAR** files;
</dt>
<dd> files' full path
</dd>
</dl>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETNBSESSIONFILES
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] const TCHAR * sessionFileName
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  This message return the number of files to load in the session sessionFileName. sessionFileName should be a full path name of an xml file. 0 is returned if sessionFileName is NULL or an empty string
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETSESSIONFILES
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [out] TCHAR ** sessionFileArray
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in]const TCHAR *
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Send this message to get files' full path name from a session file.
<p>sessionFileName is the session file from which you retrieve the files.
</p><p>sessionFileArray&nbsp;: the array in which the files' full path of the same group are written. You should send message NPPM_GETNBSESSIONFILES before to allocate this array with the proper size.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_LOADSESSION
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] const TCHAR * sessionFileName
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Open all files of same session in Notepad++ via a xml format session file sessionFileName.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_CREATESCINTILLAHANDLE
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] HWND pluginWindowHandle
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  A plugin can create a Scintilla for its usage by sending this message to Notepad++. The return value is created Scintilla handle. The handle should be destroyed by NPPM_DESTROYSCINTILLAHANDLE message while exit the plugin. If pluginWindowHandle is set (non NULL), it will be set as parent window of this created Scintilla handle, otherwise the parent window is Notepad++.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_DESTROYSCINTILLAHANDLE
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] HWND scintillaHandle2Destroy
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  If plugin called NPPM_DESTROYSCINTILLAHANDLE to create a Scintilla handle, it should call this message to destroy this handle while it exit.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETCURRENTDOCINDEX
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] int iView
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Sending this message to get the current index in the view that you indicates in iView&nbsp;: MAIN_VIEW or SUB_VIEW. Returned value is -1 if the view is invisible (hidden), otherwise is the current index.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_ACTIVATEDOC
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int iView
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] int index2Activate
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  When Notepad++ receives this message, it switches to iView (MAIN_VIEW or SUB_VIEW) as current view, then it switches to index2Activate from the current document.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETMENUHANDLE
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int whichMenu
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  This message help plugins to get the plugins menu handle of Notepad++, whichMenu must be NPPPLUGINMENU (0), or NPPMAINMENU (1) to return handle to the menu br in the main window. 0 is return on any other inut.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_RELOADFILE
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] BOOL withAlert
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] TCHAR *filePathName2Reload
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  This Message reloads the file indicated in filePathName2Reload. If withAlert is TRUE, then an alert message box will be launched.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_SWITCHTOFILE
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] TCHAR *filePathName2switch
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  When this message is received, Notepad++ switches to the document which matches with the given filePathName2switch.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETWINDOWSVERSION
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  The return value is windows version of enum winVer. The possible value is WV_UNKNOWN, WV_WIN32S, WV_95, WV_98, WV_ME, WV_NT, WV_W2K, WV_XP, WV_S2003, WV_XPX64 and WV_VISTA
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_SAVECURRENTFILE
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Send this message to Notepad++ to save the current document.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_SAVEALLFILES
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Send this message to Notepad++ to save all opened document.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETPLUGINSCONFIGDIR
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int strLen
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] TCHAR *pluginsConfDir
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  pluginsConfDir receives the directory path of plugin config files. User is responsible to allocate (or use automatic variable) a buffer with an enough size. MAX_PATH is suggested to use.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_SETMENUITEMCHECK
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int cmdID
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] BOOL doCheck
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Use this message to set/remove the check on menu item. cmdID is the command ID which corresponds to the menu item.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_LAUNCHFINDINFILESDLG
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] TCHAR * dir2Search
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] TCHAR * filtre
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  This message triggers the Find in files dialog. The fields Directory and filters are filled by respectively dir2Search and filtre if those parameters are not NULL or empty.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_DMMREGASDCKDLG
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] tTbData * dockingData
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  From v4.0, Notepad++ supports the dockable dialog feature for the plugins. This message passes the necessary data dockingData to Notepad++ in order to make your dialog dockable. Here is tTbData looks like this:
<dl>
<dt>&nbsp; HWND hClient;
</dt>
<dd> your dockable dialog handle.
</dd>
<dt>&nbsp; TCHAR *pszName;
</dt>
<dd> the name of your plugin dialog.
</dd>
<dt>&nbsp; int dlgID;
</dt>
<dd> index of menu entry where the dialog in question will be triggered.
</dd>
<dt>&nbsp; UINT uMask;
</dt>
<dd> contains the behaviour informations of your dialog. It can be one of the following value&nbsp;: DWS_DF_CONT_LEFT, DWS_DF_CONT_RIGHT, DWS_DF_CONT_TOP, DWS_DF_CONT_BOTTOM and DWS_DF_FLOATING combined (optional) with DWS_ICONTAB, DWS_ICONBAR and DWS_ADDINFO.
</dd>
<dt>&nbsp; HICON hIconTab;
</dt>
<dd> handle to the icon to display on the dialog's tab
</dd>
<dt>&nbsp; TCHAR *pszAddInfo;
</dt>
<dd> pointer to a string joined to the caption using " - ", if not NULL
</dd>
<dt>&nbsp; RECT rcFloat;
</dt>
<dd> Used internally, do not set
</dd>
<dt>&nbsp; int iPrevCont;
</dt>
<dd> Used internally, do not set
</dd>
<dt>&nbsp; const TCHAR *pszModuleName;
</dt>
<dd> the name of your plugin module (with extension .dll).
</dd>
</dl>
<p>Minimum informations you need to fill out before sending it by NPPM_DMMREGASDCKDLG message is hClient, pszName, dlgID, uMask and pszModuleName.
Notice that rcFloat and iPrevCont shouldn't be filled. They are used internally.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_DMMSHOW
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] HWND hDlg
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  This message is used for your plugin's dockable dialog. Send this message to show the dialog. hDlg is the handle of your dialog to be shown.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_DMMHIDE
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] HWND hDlg
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  This message is used for your plugin's dockable dialog. Send this message to hide the dialog. hDlg is the handle of your dialog to be hidden.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_DMMUPDATEDISPINFO
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] HWND hDlg
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  This message is used for your plugin's dockable dialog. Send this message to update (redraw) the dialog. hDlg is the handle of your dialog to be updated.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_DMMGETPLUGINHWNDBYNAME
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] const TCHAR * windowName
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] const TCHAR * moduleName
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  This message returns the dialog handle corresponds to the windowName and moduleName. You may need this message if you want to communicate with another plugin "dockable" dialog, by knowing its name and its plugin module name. If moduleName is NULL, then return value is NULL. If windowName is NULL, then the first found window handle which matches with the moduleName will be returned.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_MSGTOPLUGIN
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] TCHAR * destModuleName
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>   [in][out] CommunicationInfo * info
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  This message allows the communication between 2 plugins.
<p>For example, plugin X can execute a command of plugin Y if plugin X knows the command ID and the file name of plugin Y.
destModuleName is the complete module name (with the extesion .dll) of plugin with which you want to communicate (plugin Y).
communicationInfo is a poniter of structure type&nbsp;:
</p>
<dl>
<dt>&nbsp; long internalMsg;
</dt>
<dd> an integer defined by plugin Y, known by plugin X, identifying the message being sent.
</dd>
<dt>&nbsp; TCHAR * srcModuleName;
</dt>
<dd> the complete module name (with the extesion .dll) of caller(plugin X).
</dd>
<dt>&nbsp; void * info;
</dt>
<dd> defined by plugin, the informations to be exchanged between X and Y. It's a void pointer so it should be defined by plugin Y and known by plugin X.
</dd>
</dl>
<p>The returned value is TRUE if Notepad++ found the plugin by its module name (destModuleName), and pass the info (communicationInfo) to the module.
The returned value is FALSE if no plugin with such name is found.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_MENUCOMMAND
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] int commandID
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  This message allows plugins to call all the Notepad++ menu commands.
<p>commandID are the command ID used in Notepad++.
All the command ID are defined in menuCmdID.h.`
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_TRIGGERTABBARCONTEXTMENU
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int whichView
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] int index2Activate
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  This message switches to iView (MAIN_VIEW or SUB_VIEW) as current view, and it switchs to index2Activate from the current document. Finally it triggers the tabbar context menu for the current document.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETNPPVERSION
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  You can get Notepad++ version via this message. The return value is made up of 2 parts&nbsp;: the major version (the high word) and minor version (the low word).<br>For example, the 4.7.5 version will be&nbsp;:
<p>&nbsp; HIWORD(version) == 4
&nbsp; LOWORD(version) == 75
Note that this message is supported by the v4.7 or higher version. Earlier versions return 0.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_HIDETABBAR
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] BOOL hideOrNot
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  If hideOrNot == TRUE, then this message will hide the tabbar, otherwise it makes tabbar shown. The returned value is the previous status before this operation.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_ISTABBARHIDDEN
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  By sending this message, a plugin is able to tell the current status of tabbar from the returned value: TRUE if the tabbar is hidden, FALSE otherwise.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_HIDETOOLBAR
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] BOOL hideOrNot
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  If hideOrNot == TRUE, then this message will hide the toolbar, otherwises it makes tabbar shown. The returned value is the previous staus before this operation.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_ISTOOLBARHIDDEN
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Via this message plugin is able to know the current status of toolbar.
<p>TRUE if the toolbar is hidden, FALSE otherwise.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_HIDEMENU
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] BOOL hideOrNot
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  If hideOrNot == TRUE, then this message will hide the menu bar, otherwises it makes tabbar shown. The returned value is the previous staus before this operation.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_ISMENUHIDDEN
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Via this message plugin is able to know the current status of menu bar.
<p>TRUE if the menbar is hidden, FALSE otherwise.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_HIDESTATUSBAR
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] BOOL hideOrNot
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  If hideOrNot == TRUE, then this message will hide the status bar, otherwises it makes tabbar shown. The returned value is the previous staus before this operation.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_ISSTATUSBARHIDDEN
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Via this message plugin is able to know the current status of status bar.
<p>TRUE if the status bar is hidden, FALSE otherwise.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETSHORTCUTBYCMDID
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int cmdID
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] ShortcutKey * sk
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Get your plugin command current mapped shortcut into sk via cmdID. You may need it after getting NPPN_READY notification.
<p>Returned value&nbsp;: TRUE if this function call is successful and shorcut is enable, otherwise FALSE
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETPOSFROMBUFFERID
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int bufferID
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Get 0-based document position from given buffer ID, which is held in the 30 lowest bits of the return value on success.
<p>If bufferID doesn't exist, -1 is returned. Otherwise, the index part is valid, and bit 30 indicates which view has the buffer (clear for main view, set for sub view).
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETFULLPATHFROMBUFFERID
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int bufferID
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] TCHAR * fullFilePath
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Get full path file name from a given buffer ID.
<p>Return -1 if the bufferID non existing, otherwise the number of TCHAR copied/to copy.
User should call it with fullFilePath be NULL to get the number of TCHAR (not including the nul character), allocate fullFilePath with the return values + 1, then call it again to get full path file name
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETBUFFERIDFROMPOS
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int position
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] int view
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Get document buffer ID from given position.
<p>position is 0 based index, view should be MAIN_VIEW or SUB_VIEW.
Return value&nbsp;: 0 if given position is invalid, otherwise the document buffer ID.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETCURRENTBUFFERID
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Returns active document buffer ID
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_RELOADBUFFERID
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int bufferID
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] BOOL doAlertOrNot
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Reload the document by given buffer ID.
<p>if doAlertOrNot is TRUE, then a message box will display to ask user to reload the document, otherwise document will be loaded without asking user.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETBUFFERLANGTYPE
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Get document's language type from given buffer ID.
<p>Returns value&nbsp;: if error -1, otherwise language type (see LangType).
[in] int bufferID
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_SETBUFFERLANGTYPE
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int bufferID
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] LangType langType2Set
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Set language type of given buffer ID's document.
<p>Returns TRUE on success, FALSE otherwise.
L_USER and L_EXTERNAL are not supported.
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETBUFFERENCODING
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int bufferID
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Get document's encoding from given buffer ID.
<p>Returns value&nbsp;: if error -1, otherwise encoding number. enum UniMode - uni8Bit 0, uniUTF8 1, uni16BE 2, uni16LE 3, uniCookie 4, uni7Bit 5, uni16BE_NoBOM 6, uni16LE_NoBOM 7
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_SETBUFFERENCODING
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int bufferID
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] UniMode encoding
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Set given buffer ID's document encoding.
<p>Can only be done on new, unedited files
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETBUFFERFORMAT
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int bufferID
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Get document's format from given buffer ID.
<p>Returns value&nbsp;: if error -1, otherwise document's format (see formatType).
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_SETBUFFERFORMAT
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] int bufferID
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] formatType format
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Set format of given buffer ID's document.
<p>Returns TRUE on success, FALSE otherwise
</p>
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETCURRENTLINE
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Returns the caret current position 0-based line
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETCURRENTCOLUMN
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Returns the caret current position 0-based column
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_SAVECURRENTFILEAS
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] 0 to Save As, 1 to Save a Copy As
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] TCHAR* filename
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Performs a Save As (wParam == 0) or Save a Copy As (wParam == 1) on the current buffer, outputting to <i>filename</i>.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETCURRENTNATIVELANGENCODING
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Returns the code page associated with the current localisation of Notepad++. As of v6.6.6, returned values are 1252 (ISO 8859-1), 437 (OEM US) or 950 (Big5).
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_ALLOCATESUPPORTED
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Returns TRUE if NPPM_ALLOCATECMDID is supported. Use it to identify if subclassing is necessary.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_ALLOCATECMDID
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] Requested number of IDs
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] Pointer to allocated range as an int
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Allows a plugin to obtain a number of consecutive meni item IDs for creating menus dynamically, with the guarantee of these IDs not clashing with any other plugin's. Returns 0 on failure, nonzero on success.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_ALLOCATEMARKER
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] Requested number of IDs
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [out] Pointer to allocated range as an int
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Allows a plugin to obtain a number of consecutive arker IDs dynamically, with the guarantee of these IDs not clashing with any other plugin's. Returns 0 on failure, nonzero on success.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETLANGUAGENAME
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] The LangType identifier - an int actually
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in/out] TCHAR* Pointer to language name string.
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Returns the number of characters needed or copied. If lParam is null, size of the language name is copied. Use this to allocate a buffer to pass as lParam and get the language name copied therein. The terminating \0 isn't counted in the returned length.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETLANGUAGEDESC
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td>  [in] The LangType identifier - an int actually
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in/out] TCHAR* Pointer to language description string.
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Returns the number of characters needed or copied. If lParam is null, size of the language name is copied. Use this to allocate a buffer to pass as lParam and get the language description copied therein. The terminating \0 isn't counted in the returned length.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_SHOWDOCSWITCHER
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  [in] BOOL showItIfTrue
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Shows document switcher if lparam is true, hide it if false.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_ISDOCSWITCHERSHOWN
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Returns 0 if the document switcher is not currently shown, else non zero.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETAPPDATAPLUGINSALLOWED
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Returns true if loading plugins from&nbsp;%APPDATA is allowed, else returns false.
</td></tr></tbody></table>
<table border="1" width="100%">

<tbody><tr>
<td width="50%" rowspan="2" style="background:LightYellow;">  NPPM_GETGETCURRENTVIEW
</td>
<td width="10%" style="background:khaki"> wParam:
</td>
<td width="30%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td width="10%" style="background:khaki"> lParam:
</td>
<td>  0
</td></tr>
<tr>
<td colspan="3" style="background:#E8F8E8;">  Returns 0 when primary view is active, and 1 instead if secondary view is.
</td></tr></tbody></table>

## Notepad++ notifications

A notification is sent using a WM_NOTIFY message.  It holds the sender's control ID in its wParam, and a pointer to a notification parameter block in its lParam. The parameter block is a structure consisting of at least 3 integers, which indicate:

1. Handle of sender
2. Control ID of sender (duplicates wParam for historical reasons)
3. Notification code

Extra information, dependent on the notification code, may follow in the parameter block pointed to by lParam. Such information is documented in the Description field, if present.

The notification IDs for each of these named notifications can be found in the source code in [Notepad_plus_msgs.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/MISC/PluginsManager/Notepad_plus_msgs.h).

<table class="notifications" rules="rows" width="100%">
<tr>
<th width="40%" rowspan="2" style="background:LightYellow; text-align: left">Notification</th>
<th width="40%" style="text-align: left">hwndFrom</th>
<th width="20%" style="background:SeaShell; text-align: left"> idFrom </th></tr>
<tr>
<th colspan="2" style="background:#E8F8E8; text-align: left">  Description
</th></tr>
</tr>

<tbody>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_READY
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that all the procedures of launching notepad++ completed succesfully.
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_TBMODIFICATION
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that toolbar icons can be registered.
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_FILEBEFORECLOSE
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that the current file is about to be closed
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_FILECLOSED
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that the current file is just closed
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_FILEBEFOREOPEN
</td>
<td> hwndNpp
</td>
<td width="20%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that a file is being opened
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_FILEOPENED
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that the current file just opened
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_FILEBEFORESAVE
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that the current file is about to be saved
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_FILESAVED
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that the current file wass just saved
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_SHUTDOWN
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that Notepad++ is about to shut down.
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_BUFFERACTIVATED
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;">  activatedBufferID
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that a buffer was activated (put to foreground).
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_LANGCHANGED
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;">  currentBufferID
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that the language in the current doc just changed.
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_WORDSTYLESUPDATED
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;">  currentBufferID
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that user initiated a WordStyleDlg change.
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_SHORTCUTREMAPPED
</td>
<td>  ShortcutKeyStructurePointer
</td>
<td width="20%" style="background:SeaShell;">  cmdID
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that a plugin command shortcut is remapped.
<p>ShortcutKeyStructurePointer is type ShortcutKey *, cmdID has type int.
</p>
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_FILEBEFORELOAD
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;"> 0
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that the current file is about to be loaded
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_FILELOADFAILED
</td>
<td>  hwndNpp
</td>
<td width="20%" style="background:SeaShell;">  bufferID
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that file open operation failed
</td></tr>
</td></tr>

<tr>
<td rowspan="2" style="background:LightYellow;">  NPPN_DOCORDERCHANGED
</td>
<td>  newIndex
</td>
<td width="20%" style="background:SeaShell;">  bufferID
</td></tr>
<tr>
<td colspan="2" style="background:#E8F8E8;">  Notifies plugins that document order is changed, bufffer <i>bufferID</i> having index <i>newIndex</i>.
</td></tr>
</td>
</tr>
</tbody></table>

