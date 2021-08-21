---
title: Plugin Communication
linktitle: plugin-communication
weight: 92
---

## Plugin Communication: Messages and Notifications

[Plugins](../plugins/) need to communicate with Notepad++ to get information from it or to instruct it to do some task.
This is done by using messages and notifications.

Message and notifications share a similar interface. Where messages are sent by using Windows [SendMessage](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendmessage) api, notifications are sent by Notepad++ using [`WM_NOTIFY`](https://docs.microsoft.com/en-us/windows/win32/controls/wm-notify) messages.

These same techniques can also be used for editing [macros](../macros/) (some of which use messages to control Notepad++), or when using one of the scripting plugins (which effectively make your script a mini-plugin).

### Why both messages _and_ notifications?

Basically, a message may have a return value, and is usually thought as a query, though it can also command actions inside Notepad++.
A notification, on the other hand, simply informs of some event and is more usually thought as a command.
The extra content of the messages and notifications are different from each other, and are described in their respective sections below.

## Notepad++ messages

To send a message to Notepad++ you send its window handle together with the message ID, and two parameters, known as wParam and lParam.
The values placed in those two parameters depend on the message, and are explained below.
In cases when either wParam, lParam or both are not used, they must be set to 0.

The message IDs for each of these named messages, as well as the enums used with these messages, can be found in the source code in [Notepad_plus_msgs.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/MISC/PluginsManager/Notepad_plus_msgs.h).

You can also communicate to the Scintilla editor instances inside Notepad++ by using the Scintilla messages, which are [documented at the Scintilla website](https://www.scintilla.org/ScintillaDoc.html), and the values can be found in [Scintilla.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/scintilla/include/Scintilla.h). Note, you need to use one of the two Scintilla handles as the first parameter to SendMessage api function.

The general layout of the following messages look like this

> _MESSAGE NAME_ >_Description_
>
> _Parameters:_ >_wParam [in/out]_ >_lParam [in/out]_
>
> _Return value_

**MESSAGE NAME** gets replaced by a concrete Notepad++ message like NPPM_ACTIVATEDOC.

**Description** informs about the usage of the message and provides additional information if needed.

**wParam** and **lParam** are the parameters to be provided

**in/out** indicates whether this is an input or output parameter, meaning in case of output Notepad++ will copy some information into the provided buffer

**Return value** is the value returned by the SendMessage api call.

---

---

#### **NPPM_ACTIVATEDOC**

_Switches to the document by the given view and index._

**Parameters**:

_wParam [in]_
: int iView, which must bei eihter 0 (main view) or 1 (second view).

_lParam [in]_
: int index2Activate

**Return value**:
: Returns True

---

#### **NPPM_ADDTOOLBARICON** (**NPPM_ADDTOOLBARICON_DEPRECATED** in v8.0)

_Deprecated in v8.0. Use NPPM_ADDTOOLBARICON_FORDARKMODE instead. Does not support
the Darkmode icons._

_Adds an icon to the toolbar.
This function only makes sense if called on response to NPPN_TBMODIFICATION notification.
cmdID must be a command function id which the plugin registered via getFuncsArray previously.
icon is a pointer to the toolbarIcons structure._

**Parameters**:

_wParam [in]_
: INT cmdID

_lParam [in]_
: toolbarIcons\* icon

```
struct toolbarIconsWithDarkMode {
	HBITMAP	hToolbarBmp;
	HICON	hToolbarIcon;
};
```

**Return value**:
: Returns True

---

#### **NPPM_ADDTOOLBARICON_FORDARKMODE**

_Adds an icon to the toolbar.
This function only makes sense if called on response to NPPN_TBMODIFICATION notification.
cmdID must be a command function id which the plugin registered via getFuncsArray previously.
icon is a pointer to the toolbarIconsWithDarkMode structure._

_(Added in v8.0, replacing old NPPM_ADDTOOLBARICON)_

**Parameters**:

_wParam [in]_
: INT cmdID

_lParam [in]_
: toolbarIconsWithDarkMode\* icon

```
struct toolbarIconsWithDarkMode {
	HBITMAP	hToolbarBmp;
	HICON	hToolbarIcon;
	HICON	hToolbarIconDarkMode;
};
```

**Return value**:
: Returns True

---

#### **NPPM_ALLOCATECMDID**

_Obtains a number of consecutive menu item IDs for creating menus dynamically, with the guarantee of these IDs not clashing with any other plugins._

**Parameters**:

_wParam [in]_
: int, requested number of IDs.

_lParam [out]_
: int, pointer to allocated range.

**Return value**:
: Returns 0 on failure, nonzero on success

---

#### **NPPM_ALLOCATEMARKER**

_Obtains a number of consecutive marker IDs dynamically, with the guarantee of these IDs not clashing with any other plugins._

**Parameters**:

_wParam [in]_
: int numberOfMarkers

_lParam [out]_
: int \* firstMarkerID

**Return value**:
: Returns 0 on failure, nonzero on success.

---

#### **NPPM_ALLOCATESUPPORTED**

_Use to identify if subclassing is necessary_

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns True always

---

#### **NPPM_CREATESCINTILLAHANDLE**

_A plugin can create a Scintilla for its usage by sending this message to Notepad++.
The handle should be destroyed by NPPM_DESTROYSCINTILLAHANDLE message while exit the plugin._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: HWND pluginWindowHandle,
If set (non NULL), it will be the parent window of this created Scintilla handle, otherwise the parent window is Notepad++.

**Return value**:
: Returns the created Scintilla handle.

---

#### **NPPM_DECODESCI**

_Changes current buffer view to ansi.
view must be either 0 = main view or 1 = second view._

**Parameters**:

_wParam [in]_
: INT view

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns The new encoding mode.

---

#### **NPPM_DESTROYSCINTILLAHANDLE**

_If plugin called NPPM_CREATESCINTILLAHANDLE to create a Scintilla handle, it should call this message to destroy this handle while it exit._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: HWND scintillaHandle2Destroy

**Return value**:
: Returns True

---

#### **NPPM_DISABLEAUTOUPDATE**

_Disables the auto update functionality of Notepad++._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns True

---

#### **NPPM_DMMGETPLUGINHWNDBYNAME**

_Retrieves the dialog handle corresponds to the windowName and moduleName.
You may need this message if you want to communicate with another plugin "dockable" dialog._

**Parameters**:

_wParam [in]_
: const TCHAR \* windowName

_lParam [in]_
: const TCHAR \* moduleName

**Return value**:
: Returns NULL if moduleName is NULL. If windowName is NULL, then the first found window handle which matches with the moduleName will be returned

---

#### **NPPM_DMMHIDE**

_Hides the dialog which was previously regeistered by NPPM_DMMREGASDCKDLG._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: HWND hDlg,
is the handle of your dialog which should be hidden.

**Return value**:
: Returns True

---

#### **NPPM_DMMREGASDCKDLG**

_From v4.0, Notepad++ supports the dockable dialog feature for the plugins.
Pass the necessary dockingData to Notepad++ in order to make your dialog dockable.
Minimum informations which needs to be filled out are hClient, pszName, dlgID, uMask and pszModuleName.
Notice that rcFloat and iPrevCont shouldn't be filled. They are used internally_

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: tTbData \* dockingData

```
typedef struct {
	HWND        hClient;   // client Window Handle
	const TCHAR *pszName;  // name of plugin (shown in window)
	int         dlgID;     // a funcItem provides the function pointer to start a dialog. Please parse here these ID

	// user modifications
	UINT        uMask;       // mask params: look to above defines
	HICON       hIconTab;    // icon for tabs
	const TCHAR *pszAddInfo; // for plugin to display additional informations

	// internal data, do not use !!!
	RECT          rcFloat;        // floating position
	int           iPrevCont;      // stores the privious container (toggling between float and dock)
	const TCHAR*  pszModuleName;  // it's the plugin file name. It's used to identify the plugin
} tTbData;
```

**Return value**:
: Returns True

---

#### **NPPM_DMMSHOW**

_Shows the dialog which was previously regeistered by NPPM_DMMREGASDCKDLG._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: HWND hDlg,
is the handle of your dialog which should be shown.

**Return value**:
: Returns True

---

#### **NPPM_DMMUPDATEDISPINFO**

_Updates (redraw) the dialog._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: HWND hDlg,
is the handle of the dialog which should be updated.

**Return value**:
: Returns True

---

#### **NPPM_DMMVIEWOTHERTAB**

_Shows the plugin dialog with the given name.
name should be the same value as previously used to register the dialog._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: TCHAR\* name

**Return value**:
: Returns True

---

#### **NPPM_DOCLISTDISABLECOLUMN**

_Sets the extension column in Document List panel.
If disableOrNot is True, extension column is hidden otherwise it is visible._

_Known as `NPPM_DOCSWITCHERDISABLECOLUMN` in v8.1.2 and earlier._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: BOOL disableOrNot

**Return value**:
: Returns True

---

#### **NPPM_DOOPEN**

_Switches or openes a file with given fullPathName2Open._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: TCHAR \* fullPathName2Open

**Return value**:
: Returns The return value is True (1) if the operation is successful, otherwise False (0).

---

#### **NPPM_ENCODESCI**

_Changes current buffer view to utf8.
view must be either 0 = main view or 1 = second view._

**Parameters**:

_wParam [in]_
: INT view

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns The new encoding mode.

---

#### **NPPM_GETAPPDATAPLUGINSALLOWED**

_Retrieves the information whether plugins are loadable from %APPDATA%._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns True if loading plugins from %APPDATA% is allowed, False otherwise

---

#### **NPPM_GETBUFFERENCODING**

_Retrieves the encoding from the document with the given bufferID._

**Parameters**:

_wParam [in]_
: int bufferID

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns -1 on error, otherwise the encoding number. (see enum UniMode)

---

#### **NPPM_GETBUFFERFORMAT**

_Gets the current format of the document with given bufferID._

**Parameters**:

_wParam [in]_
: int bufferID

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns -1 on error, otherwise documents format (see formatType).

---

#### **NPPM_GETBUFFERIDFROMPOS**

_Gets the document buffer ID from the given position._

**Parameters**:

_wParam [in]_
: int position, is 0 based

_lParam [in]_
: int view, which should be either 0 (main view) or 1 (second view)

**Return value**:
: Returns 0 if given position is invalid, otherwise the document buffer ID.

---

#### **NPPM_GETBUFFERLANGTYPE**

_Retrieves the language type of the document with the given bufferID._

**Parameters**:

_wParam [in]_
: int bufferID

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns -1 on error, otherwise a value from enum LangType.
Please see the enum LangType for all possible values.

---

#### **NPPM_GETCURRENTBUFFERID**

_Returns the buffer ID of the active document._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns the buffer ID of the active document.

---

#### **NPPM_GETCURRENTCOLUMN**

_Retrieves the column of the caret._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns the current, 0-based, column position of the caret.

---

#### **NPPM_GETCURRENTDIRECTORY**

_Retrieves the directory path of current document.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use._

**Parameters**:

_wParam [in]_
: size_t directoryPathLen

_lParam [out]_
: TCHAR \* directoryPath

**Return value**:
: Returns True on success and False if provided directoryPath buffer is not large enough

---

#### **NPPM_GETCURRENTDOCINDEX**

_Retrieves the current index of the current view._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int iView, which must bei eihter 0 (main view) or 1 (second view).

**Return value**:
: Returns -1 if the view is invisible (hidden), otherwise is the current index.

---

#### **NPPM_GETCURRENTLANGTYPE**

_Retrieves the language type of the current document._

**Parameters**:

_wParam [ in ]_
: int, must be zero.

_lParam [ out ]_
: int \* langType, pointer to the buffer receiving the language type of the current document
Please see the enum LangType for all possible values.

**Return value**
: Returns always True

---

#### **NPPM_GETCURRENTLINE**

_Retrieves the line of the caret._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns the current, 0-based, line position of the caret.

---

#### **NPPM_GETCURRENTNATIVELANGENCODING**

_Retrieves the code page associated with the current localisation of Notepad++._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns As of v6.6.6, returned values are 1252 (ISO 8859-1), 437 (OEM US) or 950 (Big5).

---

#### **NPPM_GETCURRENTSCINTILLA**

_Retrieves the current Scintilla view_

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [out]_
: int \* currentEdit, pointer to the buffer receiving the current view.
The returned value can be one of the following:

```
	Value        Meaning
	  0          The main view
	  1          The second view
	 -1          In case of an error
```

**Return value**:
: Returns always True

---

#### **NPPM_GETCURRENTVIEW**

_Retrieves the current used view. _

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns Either 0 when main view is active or 1 if secondary view is active.

---

#### **NPPM_GETCURRENTWORD**

_Retrieves the word containing the caret.
User is responsible to allocate a buffer which is large enough._

**Parameters**:

_wParam [in]_
: size_t currentWordLen

_lParam [out]_
: TCHAR \* currentWord

**Return value**:
: Returns True on success and False if provided currentWord buffer is not large enough

---

#### **NPPM_GETEDITORDEFAULTBACKGROUNDCOLOR**

_Retrieves the current editor default background color._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns The color as integer with hex format being 0x00bbggrr

---

#### **NPPM_GETEDITORDEFAULTFOREGROUNDCOLOR**

_Retrieves the current editor default foreground._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns The color as integer with hex format being 0x00bbggrr

---

#### **NPPM_GETENABLETHEMETEXTUREFUNC**

_Returns if visual style of the background of a dialog window is enabled or not._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns A proc address or NULL

---

#### **NPPM_GETEXTPART**

_Retrieves the extension of the filename of the current document.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use._

**Parameters**:

_wParam [in]_
: size_t extensionLen

_lParam [out]_
: TCHAR \* extension

**Return value**:
: Returns True on success and False if provided extension buffer is not large enough

---

#### **NPPM_GETFILENAME**

_Retrieves the file name of current document.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use._

**Parameters**:

_wParam [in]_
: size_t fileNameLen

_lParam [out]_
: TCHAR \* fileName

**Return value**:
: Returns True on success and False if provided fileName buffer is not large enough

---

#### **NPPM_GETFILENAMEATCURSOR**

_Retrieves the filename at the current caret position.
Note, while this message has been created, and is used internally, to retrieve a filename at the current caret position, it does return anything which fulfils the requirements, even single words._

**Parameters**:

_wParam [in]_
: INT length

_lParam [out]_
: TCHAR\* buffer

**Return value**:
: Returns True if the size of the provided buffer is large enough, False otherwise.

---

#### **NPPM_GETFULLCURRENTPATH**

_Retrieves the full path of the current document.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use._

**Parameters**:

_wParam [in]_
: size_t fullPathLen

_lParam [out]_
: TCHAR \* fullPath

**Return value**:
: Returns True on success and False if provided fullPath buffer is not large enough

---

#### **NPPM_GETFULLPATHFROMBUFFERID**

_Gets the full path file name from the given bufferID.
First call should be made with buffer set to NULL to retrieve the actual size needed.
Second call is sent with correctly allocated buffer, +1 for trailing null, to retrieve the full path file name._

**Parameters**:

_wParam [in]_
: int bufferID

_lParam [out]_
: TCHAR \* buffer

**Return value**:
: Returns -1 if bufferID does not exist, otherwise the number of chars copied/to copy.

---

#### **NPPM_GETLANGUAGEDESC**

_Retrieves the description of the current language used.
First call should be made with buffer set to NULL to retrieve the actual size needed.
Second call is sent with correctly allocated buffer to retrieve the description._

**Parameters**:

_wParam [in]_
: int langTypeID

_lParam [out]_
: TCHAR\* buffer

**Return value**:
: Returns The number of characters needed or copied

---

#### **NPPM_GETLANGUAGENAME**

_Retrieves the name of the current language used.
First call should be made with buffer set to NULL to retrieve the actual size needed.
Second call is sent with correctly allocated buffer to retrieve the language name._

**Parameters**:

_wParam [in]_
: int langTypeID

_lParam [out]_
: TCHAR\* buffer

**Return value**:
: Returns The number of characters needed or copied

---

#### **NPPM_GETLINENUMBERWIDTHMODE**

_Get line number margin width in dynamic width mode (LINENUMWIDTH_DYNAMIC) or constant width mode (LINENUMWIDTH_CONSTANT)_

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns the line number margin width mode, either the LINENUMWIDTH_DYNAMIC or LINENUMWIDTH_CONSTANT value.

---

#### **NPPM_GETMENUHANDLE**

_Retrieves either the plugin or the main menu handle of Notepad++._

**Parameters**:

_wParam [in]_
: int whichMenu, which can be 0 (plugin menu) or 1 (main menu)

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns the requested menu handle.

---

#### **NPPM_GETNAMEPART**

_Retrieves the part of filename, without extension, of the current document.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use._

**Parameters**:

_wParam [in]_
: size_t namePartLen

_lParam [out]_
: TCHAR \* namePart

**Return value**:
: Returns True on success and False if provided namePart buffer is not large enough

---

#### **NPPM_GETNBOPENFILES**

_Retrieves the number of files currently open_

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: Integer of one of the following values:

```
	Value        Meaning
	  0          the total number of files opened in Notepad++
	  1          number of files opened in the main view
	  2          number of files opened in the second view
```

**Return value**:
: Returns number of open files

---

#### **NPPM_GETNBSESSIONFILES**

_Retrieves the number of files to load in the session sessionFileName.
sessionFileName should be a full path name of an xml file._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: const TCHAR \* sessionFileName

**Return value**:
: Returns 0 if sessionFileName is NULL or an empty string else the number of files.

---

#### **NPPM_GETNBUSERLANG**

_Retrieves the number of user defined languages and, optionally, the starting menu id.
Note, udlID is optional, if not used set it to 0, otherwise an integer pointer is needed to retrieve the menu identifier._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [out]_
: INT\* udlID

**Return value**:
: Returns The number of user defined languages identified

---

#### **NPPM_GETNPPDIRECTORY**

_Retrieves the full path of the directory where the Notepad++ binary is located.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use._

**Parameters**:

_wParam [in]_
: size_t nppDirLen

_lParam [out]_
: TCHAR \* nppDir

**Return value**:
: Returns True on success and False if provided nppDir buffer is not large enough

---

#### **NPPM_GETNPPFULLFILEPATH**

_Retrieves the full path of the Notepad++ executable._

**Parameters**:

_wParam [in]_
: INT length

_lParam [out]_
: TCHAR\* buffer

**Return value**:
: Returns True if the provided buffer size was big enough to write the full path to it, False otherwise.

---

#### **NPPM_GETNPPVERSION**

_Retrieves the current Notepad++ version.
The value is made up of 2 parts: the major version (the high word) and minor version (the low word).
For example, 4.7.5 is encoded like:
HIWORD(version) == 4
LOWORD(version) == 75
Note that this message is supported by the v4.7 or higher version. Earlier versions return 0._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns a LONG value containing the current version.

---

#### **NPPM_GETOPENFILENAMES**

_Retrieves the open files of both views.
User is responsible to allocate an big enough fileNames array._

**Parameters**:

_wParam [out]_
: TCHAR \*\* fileNames,
receives the full path names of all the opened files in Notepad++

_lParam [in]_
: int nbFile,
is the size of the fileNames array. Get this value by using NPPM_NBOPENFILES message with constant ALL_OPEN_FILES, then allocate fileNames array with this value.

**Return value**:
: Returns The number of files copied into fileNames array.

---

#### **NPPM_GETOPENFILENAMESPRIMARY**

_Retrieves the open files of the main view.
User is responsible to allocate an big enough fileNames array._

**Parameters**:

_wParam [out]_
: TCHAR \*\* fileNames,
receives the full path names of the opened files in the primary view

_lParam [in]_
: int nbFile,
is the size of the fileNames array. Get this value by using NPPM_NBOPENFILES message with constant PRIMARY_VIEW, then allocate fileNames array with this value.

**Return value**:
: Returns The number of files copied into fileNames array.

---

#### **NPPM_GETOPENFILENAMESSECOND**

_Retrieves the open files of the secondary view.
User is responsible to allocate an big enough fileNames array._

**Parameters**:

_wParam [out]_
: TCHAR \*\* fileNames,
receives the full path names of the opened files in the second view

_lParam [in]_
: int nbFile,
is the size of your fileNames array. You should get this value by using NPPM_NBOPENFILES message with constant SECOND_VIEW, then allocate fileNames array with this value.

**Return value**:
: Returns The number of files copied into fileNames array.

---

#### **NPPM_GETPLUGINHOMEPATH**

_Retrieves the plugin home root path.
First call should be made with length set to 0 and buffer set to NULL to retrieve the actual size of the path. Second call sends the correct length and allocated buffer, both +1 for trailing NULL, to get the path name._

**Parameters**:

_wParam [in]_
: SIZE_T length

_lParam [out]_
: TCHAR\* buffer

**Return value**:
: Returns the number of TCHAR copied to buffer without trailing NULL.

---

#### **NPPM_GETPLUGINSCONFIGDIR**

_Retrieves the path of the plugin config directory.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use._

**Parameters**:

_wParam [in]_
: int strLen

_lParam [out]_
: TCHAR \*pluginsConfDir

**Return value**:
: Returns True

---

#### **NPPM_GETPOSFROMBUFFERID**

_Gets 0-based document position from given buffer ID, which is held in the 30 lowest bits of the return value on success.
Bit 30 indicates which view has the buffer (clear for main view, set for sub view)._

**Parameters**:

_wParam [in]_
: int bufferID

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns -1 if bufferID doesn't exist else the position.

---

#### **NPPM_GETSETTINGSONCLOUDPATH**

_Get settings on cloud path. It's useful if plugins want to store its settings on Cloud, if this path is set. (added v7.9.2)._

_First call should be made with buffer set to NULL to retrieve the actual size needed.
Second call is sent with correctly allocated buffer, +1 for trailing null, to retrieve the full path file name._

**Parameters**:

_wParam [in]_
: size_t strLen,
maximum bytes to read for the path string, including the final NULL byte

_lParam [out]_
: TCHAR \*settingsOnCloudPath,
the path for cloud settings obtained by this message

**Return value**:
: Returns the length of the path string

---

#### **NPPM_GETSESSIONFILES**

_Retrieves the files' full path name from a session file._

**Parameters**:

_wParam [out]_
: TCHAR \*\* sessionFileArray,
the array in which the files' full path of the same group are written.
To allocate the array with the proper size, send message NPPM_GETNBSESSIONFILES.

_lParam [in]_
: const TCHAR \* sessionFileName,
the path to the session file from which you retrieve the files

**Return value**:
: Returns True

---

#### **NPPM_GETSHORTCUTBYCMDID**

_Gets the mapped plugin command shortcut. May be called after getting NPPN_READY notification._

**Parameters**:

_wParam [in]_
: int cmdID

_lParam [out]_
: ShortcutKey \* sk, which is defined as

```
struct ShortcutKey {
	bool _isCtrl;
	bool _isAlt;
	bool _isShift;
	UCHAR _key;
}
```

**Return value**:
: Returns True if this function call is successful and shortcut is enable, otherwise False

---

#### **NPPM_GETWINDOWSVERSION**

_Retrieves the windows operating system version._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns a value of enum winVer. Possible values are

- WV_UNKNOWN
- WV_WIN32S
- WV_95
- WV_98
- WV_ME
- WV_NT
- WV_W2K
- WV_XP
- WV_S2003
- WV_XPX64
- WV_VISTA

---

#### **NPPM_HIDEMENU**

_Either hides or shows the menubar._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: BOOL hideOrNot

**Return value**:
: Returns the previous status before this operation.

---

#### **NPPM_HIDESTATUSBAR**

_Either hides or shows the statusbar._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: BOOL hideOrNot

**Return value**:
: Returns the previous status before this operation.

---

#### **NPPM_HIDETABBAR**

_Either hides or shows the tabbar._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: BOOL hideOrNot

**Return value**:
: Returns the previous status before this operation.

---

#### **NPPM_HIDETOOLBAR**

_Either hides or shows the toolbar._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: BOOL hideOrNot

**Return value**:
: Returns the previous status before this operation.

---

#### **NPPM_ISDOCLISTSHOWN**

_Checks the visibility of the Document List panel._

_Known as `NPPM_ISDOCSWITCHERSHOWN` in v8.1.2 and earlier._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns True if the Document List panel is currently shown, False otherwise

---

#### **NPPM_ISMENUHIDDEN**

_Retrieves the current status of menubar._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns True if the menubar is hidden, False otherwise.

---

#### **NPPM_ISSTATUSBARHIDDEN**

_Retrieves the current status of the statusbar._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns True if the status bar is hidden, False otherwise.

---

#### **NPPM_ISTABBARHIDDEN**

_Retrieves the current status of tabbar._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns True if the tabbar is hidden, False otherwise.

---

#### **NPPM_ISTOOLBARHIDDEN**

_Retrieves the current status of toolbar._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns True if the toolbar is hidden, False otherwise.

---

#### **NPPM_LAUNCHFINDINFILESDLG**

_Triggers the Find in files dialog._

**Parameters**:

_wParam [in]_
: TCHAR \* dir2Search or NULL

_lParam [in]_
: TCHAR \* filter or NULL

**Return value**:
: Returns True

---

#### **NPPM_LOADSESSION**

_Opens all files of same session in Notepad++ via a xml format session file sessionFileName._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: const TCHAR \* sessionFileName

**Return value**:
: Returns True

---

#### **NPPM_MAKECURRENTBUFFERDIRTY**

_Makes the current document dirty, aka sets the save state to unsaved._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns True

---

#### **NPPM_MENUCOMMAND**

_Calls all possible Notepad++ menu commands._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int commandID,
see menuCmdID.h for all possible values.

**Return value**:
: Returns True

---

#### **NPPM_MODELESSDIALOG**

_For each created dialog in your plugin, you should register it (and unregister while destroy it) to Notepad++ by using this message.
If this message is ignored, then your dialog won't react with the key stroke messages such as TAB key.
For the good functioning of your plugin dialog, you're recommended to not ignore this message._

**Parameters**:

_wParam [in]_
: int op,
the operation mode.
MODELESSDIALOGADD is to register and
MODELESSDIALOGREMOVE is to unregister.

_lParam [in]_
: HWND hDlg,
is the handle of the dialog to be registered

**Return value**:
: Returns True

---

#### **NPPM_MSGTOPLUGIN**

_Allows the communication between 2 plugins.
For example, plugin X can execute a command of plugin Y if plugin X knows the command ID and the file name of plugin Y._

**Parameters**:

_wParam [in]_
: TCHAR \* destModuleName,
is the complete module name (with the extesion .dll) of plugin with which you want to communicate (plugin Y).

_lParam [out]_
: CommunicationInfo \* info

```
struct CommunicationInfo {
	long internalMsg;
	const TCHAR * srcModuleName;
	void * info; // defined by plugin
};
```

: _internalMsg_ is an integer defined by plugin Y, known by plugin X, identifying the message being sent.
: _srcModuleName_ is the complete module name (with the extesion .dll) of caller(plugin X).
: _info_ is defined by plugin, the informations to be exchanged between X and Y. It's a void pointer so it should be defined by plugin Y and known by plugin X.
The returned value is TRUE if Notepad++ found the plugin by its module name (destModuleName), and pass the info (communicationInfo) to the module. The returned value is FALSE if no plugin with such name is found.

**Return value**:
: Returns True if Notepad++ found the plugin by its module name (destModuleName), and pass the info (communicationInfo) to the module, False otherwise.

---

#### **NPPM_RELOADBUFFERID**

_Reloads the document with the given bufferID.
If doAlertOrNot is True, then a message box will display to ask user to reload the document, otherwise document will be loaded without asking user._

**Parameters**:

_wParam [in]_
: int bufferID

_lParam [in]_
: BOOL doAlertOrNot

**Return value**:
: Returns True on success, False otherwise

---

#### **NPPM_RELOADFILE**

_Reloads the file indicated by filePathName2Reload._

**Parameters**:

_wParam [in]_
: BOOL withAlert,
if True then an alert message box will be launched.

_lParam [in]_
: TCHAR \*filePathName2Reload

**Return value**:
: Returns True

---

#### **NPPM_REMOVESHORTCUTBYCMDID**

_Removes the assigned shortcut mapped to cmdID._

**Parameters**:

_wParam [in]_
: int32 cmdID

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns True if function call is successful, False otherwise.

---

#### **NPPM_SAVEALLFILES**

_Saves all opened documents._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns True

---

#### **NPPM_SAVECURRENTFILE**

_Saves the current document._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int, must be zero.

**Return value**:
: Returns True

---

#### **NPPM_SAVECURRENTFILEAS**

_Saves the current file.
saveAsCopy must be either 0 to save, or 1 to save a copy of the current filename._

**Parameters**:

_wParam [in]_
: int saveAsCopy

_lParam [in]_
: TCHAR\* filename

**Return value**:
: Returns True on success, False otherwise

---

#### **NPPM_SAVECURRENTSESSION**

_Saves the current opened files in Notepad++ as a group of files (session) as an xml file.
The xml full path name has to be provided by sessionFileName._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: const TCHAR \*sessionFileName

**Return value**:
: Returns True

---

#### **NPPM_SAVEFILE**

_Saves a specific file.
filename must be the full file path for the file to be saved._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: const TCHAR\* filename

**Return value**:
: Returns True on success False otherwise

---

#### **NPPM_SAVESESSION**

_Creates an session file for a defined set of files.
sessionInfo is a pointer to sessionInfo structure.
Note, contrary to NPPM_SAVECURRENTSESSION, which saves the current opened files, this call can be used to freely define any file which should be part of a session._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: sessionInfo\*

**Return value**:
: Returns On success a TCHAR\* to full path of the session filename to be saved or NULL otherwise

---

#### **NPPM_SETBUFFERENCODING**

_Sets the document encoding for the given bufferID.
Can only be done on new, unedited files._

**Parameters**:

_wParam [in]_
: int bufferID

_lParam [in]_
: UniMode encoding

**Return value**:
: Returns True on success, False otherwise.

---

#### **NPPM_SETBUFFERFORMAT**

_Sets format to the document with the given bufferID._

**Parameters**:

_wParam [in]_
: int bufferID

_lParam [in]_
: formatType format

**Return value**:
: Returns True on success, False otherwise.

---

#### **NPPM_SETBUFFERLANGTYPE**

_Sets the language type of the document based on the given bufferID.
See enum LangType for valid values, L_USER and L_EXTERNAL are not supported._

**Parameters**:

_wParam [in]_
: int bufferID

_lParam [in]_
: LangType type2Set

**Return value**:
: Returns True on success, False otherwise.

---

#### **NPPM_SETCURRENTLANGTYPE**

_Sets a new language type to the current used document._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int langType, please see the enum LangType for all possible values.

**Return value**:
: Returns True

---

#### **NPPM_SETEDITORBORDEREDGE**

_Extends the Scintilla window with an extra style.
If value is True adds an additional sunken edge style to the Scintilla window else it removes the extended style from the window. See MSDN Extended Window Styles for more information._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: BOOL value

**Return value**:
: Returns True

---

#### **NPPM_SETLINENUMBERWIDTHMODE**

_Set line number margin width in dynamic width mode (LINENUMWIDTH_DYNAMIC) or constant width mode (LINENUMWIDTH_CONSTANT).
It may help some plugins to disable non-dynamic line number margins width to have a smooth visual effect while vertical scrolling the content in Notepad++_

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: int widthMode, must be one of the values LINENUMWIDTH_DYNAMIC or LINENUMWIDTH_CONSTANT.

**Return value**:
: Returns True on success, False on failure

---

#### **NPPM_SETMENUITEMCHECK**

_Sets or removes the check on a menu item._

**Parameters**:

_wParam [in]_
: int cmdID,
is the command ID which corresponds to the menu item

_lParam [in]_
: BOOL doCheck

**Return value**:
: Returns True

---

#### **NPPM_SETSMOOTHFONT**

_Uses underlying Scintilla command SCI_SETFONTQUALITY to manage the font quality.
If value is True, this message sets SC_EFF_QUALITY_LCD_OPTIMIZED else SC_EFF_QUALITY_DEFAULT_

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: BOOL value

**Return value**:
: Returns True

---

#### **NPPM_SETSTATUSBAR**

_Sets value in the specified field of a statusbar._

**Parameters**:

_wParam [in]_
: int field, possible values are

```
STATUSBAR_DOC_TYPE      0
STATUSBAR_DOC_SIZE      1
STATUSBAR_CUR_POS       2
STATUSBAR_EOF_FORMAT    3
STATUSBAR_UNICODE_TYPE  4
STATUSBAR_TYPING_MODE   5
```

_lParam [out]_
: TCHAR \* value, pointer to the new value.

**Return value**:
: Returns 0 on failure, nonzero on success

---

#### **NPPM_SHOWDOCLIST**

_Show or hide the Document List panel.
If toShowOrNot is True, the Document List panel is shown otherwise it is hidden._

_Known as `NPPM_SHOWDOCSWITCHER` in v8.1.2 and earlier._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: BOOL toShowOrNot

**Return value**:
: Returns True

---

#### **NPPM_SWITCHTOFILE**

_Switches to the document which matches with the given filePathName2switch._

**Parameters**:

_wParam [in]_
: int, must be zero.

_lParam [in]_
: TCHAR \*filePathName2switch

**Return value**:
: Returns True

---

#### **NPPM_TRIGGERTABBARCONTEXTMENU**

_Triggers the tabbar context menu for the given view and index._

**Parameters**:

_wParam [in]_
: int whichView

_lParam [in]_
: int index2Activate

**Return value**:
: Returns True

---

## Notepad++ notifications

A notification is sent using a [WM_NOTIFY](https://docs.microsoft.com/en-us/windows/win32/controls/wm-notify) message and therefore uses the [NMHDR structure](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-nmhdr).

The three structure fields are, basically, three integer values.
**hwndFrom** and **idFrom** holding the provided information of the notification.
The integers might be pointers to structures/arrays, which, if present, are documented.
**code** is always set to the ID of the Notification.

The notification IDs for each of these named notifications can be found in the source code in [Notepad_plus_msgs.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/MISC/PluginsManager/Notepad_plus_msgs.h).

Most of the time **_hwndFrom_** is set to **hwndNpp** which represents the window handle of the current Notepad++ instance.
**BufferID**, mostly used in **_idFrom_**, refers to an ID which uniquely identifies a document
A **0** (NULL) in either **_hwndFrom_** or **_idFrom_** indicate that the field is unused.

The general layout of the following notifications look like this

**NOTIFICATION NAME**
_Description_

**Fields**
: _code_
: _hwndFrom_
: _idFrom_

**NOTIFICATION NAME** gets replaced by a concrete Notepad++ notification like NPPN_READY.
**Description** informs about the usage of the notification and provides additional information if needed.
**Fields** are the parameters to be provided by the notification.

---

---

#### **NPPN_BEFORESHUTDOWN**

_To notify plugins that Npp shutdown has been triggered, files have not been closed yet_

**Fields:**

    code: 		NPPN_BEFORESHUTDOWN
    hwndFrom:	hwndNpp
    idFrom:		0

---

#### **NPPN_BUFFERACTIVATED**

_To notify plugins that a buffer was activated (put to foreground)._

**Fields:**

    code:		NPPN_BUFFERACTIVATED
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_CANCELSHUTDOWN**

_To notify plugins that Npp shutdown has been cancelled_

**Fields:**

    code:		NPPN_CANCELSHUTDOWN
    hwndFrom:	hwndNpp
    idFrom:		0

---

#### **NPPN_DOCORDERCHANGED**

_To notify plugins that document order is changed_

**Fields:**

    code:		NPPN_DOCORDERCHANGED
    hwndFrom:	newIndex
    idFrom:		BufferID

---

#### **NPPN_FILEBEFORECLOSE**

_To notify plugins that the current file is about to be closed_

**Fields:**

    code:		NPPN_FILEBEFORECLOSE
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_FILEBEFOREDELETE**

_To notify plugins that file is to be deleted_

**Fields:**

    code:		NPPN_FILEBEFOREDELETE
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_FILEBEFORELOAD**

_To notify plugins that the current file is about to be loaded_

**Fields:**

    code:		NPPN_FILEBEFORELOAD
    hwndFrom:	hwndNpp
    idFrom:		NULL

---

#### **NPPN_FILEBEFOREOPEN**

_To notify plugins that the current file is about to be opened_

**Fields:**

    code:		NPPN_FILEBEFOREOPEN
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_FILEBEFORERENAME**

_To notify plugins that file is to be renamed_

**Fields:**

    code:		NPPN_FILEBEFORERENAME
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_FILEBEFORESAVE**

_To notify plugins that the current file is about to be saved_

**Fields:**

    code:		NPPN_FILEBEFORESAVE
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_FILECLOSED**

_To notify plugins that the current file is just closed_

**Fields:**

    code:		NPPN_FILECLOSED
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_FILEDELETED**

_To notify plugins that file has been deleted_

**Fields:**

    code:		NPPN_FILEDELETED
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_FILEDELETEFAILED**

_To notify plugins that file deletion has failed_

**Fields:**

    code:		NPPN_FILEDELETEFAILED
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_FILELOADFAILED**

_To notify plugins that file open operation failed_

**Fields:**

    code:		NPPN_FILELOADFAILED
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_FILEOPENED**

_To notify plugins that the current file is just opened_

**Fields:**

    code:		NPPN_FILEOPENED
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_FILERENAMECANCEL**

_To notify plugins that file rename has been cancelled_

**Fields:**

    code:		NPPN_FILERENAMECANCEL
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_FILERENAMED**

_To notify plugins that file has been renamed_

**Fields:**

    code:		NPPN_FILERENAMED
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_FILESAVED**

_To notify plugins that the current file is just saved_

**Fields:**

    code:		NPPN_FILESAVED
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_LANGCHANGED**

_To notify plugins that the language in the current doc is just changed._

**Fields:**

    code:		NPPN_LANGCHANGED
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---

#### **NPPN_READONLYCHANGED**

_To notify plugins that current document change the readonly status,_

**Fields:**

    code:		NPPN_READONLYCHANGED
    hwndFrom:	BufferID
    idFrom:		docStatus, either one or the combination of the following values
    			DOCSTATUS_READONLY    1
    			DOCSTATUS_BUFFERDIRTY 2

---

#### **NPPN_READY**

_To notify plugins that all the procedures of launchment of notepad++ are done._

**Fields:**

    code:		NPPN_READY
    hwndFrom:	hwndNpp
    idFrom:		0

---

#### **NPPN_SHORTCUTREMAPPED**

_To notify plugins that plugin command shortcut is remapped._

**Fields:**

    code:		NPPN_SHORTCUTREMAPPED
    hwndFrom:	ShortcutKeyStructurePointer, which is defined as
    			struct ShortcutKey {
    				bool _isCtrl
    				bool _isAlt
    				bool _isShift
    				UCHAR _key
    			}

    idFrom:		cmdID, the ID of the command shortcut

---

#### **NPPN_SHUTDOWN**

_To notify plugins that Notepad++ is about to be shutdowned._

**Fields:**

    code:		NPPN_SHUTDOWN
    hwndFrom:	hwndNpp
    idFrom:		0

---

#### **NPPN_SNAPSHOTDIRTYFILELOADED**

_To notify plugins that a snapshot dirty file is loaded on startup_

**Fields:**

    code:		NPPN_SNAPSHOTDIRTYFILELOADED
    hwndFrom:	NULL
    idFrom:		BufferID

---

#### **NPPN_TBMODIFICATION**

_To notify plugins that toolbar icons can be registered_

**Fields:**

    code:		NPPN_TBMODIFICATION
    hwndFrom:	hwndNpp
    idFrom:		0

---

#### **NPPN_WORDSTYLESUPDATED**

_To notify plugins that user initiated a WordStyleDlg change._

**Fields:**

    code:		NPPN_WORDSTYLESUPDATED
    hwndFrom:	hwndNpp
    idFrom:		BufferID

---
