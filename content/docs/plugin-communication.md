---
title: Plugin Communication
linktitle: plugin-communication
weight: 120
---


## Plugin Communication: Messages and Notifications

[Plugins](../plugins/) need to communicate with Notepad++ to get information from it or to instruct it to do some task.
This is done by using messages and notifications.

Message and notifications share a similar interface.  Where messages are sent by using Windows [SendMessage](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendmessage) api, notifications are sent by Notepad++ using [`WM_NOTIFY`](https://docs.microsoft.com/en-us/windows/win32/controls/wm-notify) messages.

These same techniques can also be used for editing [macros](../macros/) (some of which use messages to control Notepad++), or when using one of the scripting plugins (which effectively make your script a mini-plugin).  External applications (such as AutoHotKey) can also make use of these messages to automate Notepad++.

### Why both messages *and* notifications?

Basically, a message may have a return value, and is usually thought as a query, though it can also command actions inside Notepad++.
A notification, on the other hand, simply informs of some event and is more usually thought as a command.
The extra content of the messages and notifications are different from each other, and are described in their respective sections below.

## Notepad++ messages

To send a message to Notepad++ you send its window handle together with the message ID, and two parameters, known as wParam and lParam.
The values placed in those two parameters depend on the message, and are explained below.
In cases when either wParam, lParam or both are not used, they must be set to 0.

The message IDs for each of these named messages, as well as the enums used with these messages, can be found in the source code in [Notepad_plus_msgs.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/MISC/PluginsManager/Notepad_plus_msgs.h).

{{< expand "Aside: interpreting #defines" >}}
If you are writing your plugin in C++ or similar languages, you should just include the `Notepad_plus_msgs.h` to get all the constants; but if you are using a different language for your plugin or other message-interface, you will need to translate those `#define` statements to constants or values appropriate to your language.

When reading the `#define` for the various `NPPM_` constants, you need to notice that `NPPMSG` is defined as `(WM_USER + 1000)` near the top of the file, and you need to know that [`WM_USER`](https://learn.microsoft.com/en-us/windows/win32/winmsg/wm-user) is the Windows standard constant with a value of `0x0400` (1024).  You may need to look up other `#define` values from elsewhere in the header file in order to fully resolve some of the values.  For example, `#define NPPM_SAVEALLFILES (NPPMSG + 39)` is really the integer 1024 + 1000 + 39 = 2063, so that is the value you need to use when defining your version of the `NPPM_SAVEALLFILES` constant.
{{< /expand >}}

You can also communicate to the Scintilla editor instances inside Notepad++ by using the Scintilla messages, which are [documented at the Scintilla website](https://www.scintilla.org/ScintillaDoc.html), and the values can be found in [Scintilla.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/scintilla/include/Scintilla.h). Note, you need to use one of the two Scintilla handles as the first parameter to SendMessage api function.

#### **Message Key**

The general layout of the following messages look like this

>[ID Number] **MESSAGE NAME**
>
>*Description*
>
>**Parameters**:
>
>*wParam [in/out]*
>
>*lParam [in/out]*
>
>**Return value**:

where:

- **[ID Number]** is the integer value of the Notepad++ message
- **MESSAGE NAME** is the name of the Notepad++ message constant (like `NPPM_ACTIVATEDOC`).
- **Description** informs about the usage of the message and provides additional information if needed.
- **Parameters** called **wParam** and **lParam** are to be provided as the arguments to the notification.
- **[in/out]** indicates whether this is an input or output Parameter.  In the case of an output Parameter, Notepad++ will copy some information into the buffer provided as that Parameter
- **Return value** is the value returned by the SendMessage api call.

---
---

#### [2052] **NPPM_ACTIVATEDOC**
*Switches to the document by the given view and index.*

**Parameters**:

*wParam [in]*
: int iView, which must be either 0 (main view) or 1 (second view).

*lParam [in]*
: int index2Activate

**Return value**:
: Returns True

---

#### [2065] **NPPM_ADDTOOLBARICON** [DEPRECATED]
*Deprecated in v8.0.  Use NPPM_ADDTOOLBARICON_FORDARKMODE instead.  Does not support
the Darkmode icons.*

*`NPPM_ADDTOOLBARICON_DEPRECATED`: Adds an icon to the toolbar.
This function only makes sense if called on response to NPPN_TBMODIFICATION notification.
cmdID must be a command function id which the plugin registered via getFuncsArray previously.
icon is a pointer to the toolbarIcons structure.*

**Parameters**:

*wParam [in]*
: INT cmdID

*lParam [in]*
: toolbarIcons* icon
~~~
struct toolbarIconsWithDarkMode {
	HBITMAP	hToolbarBmp;
	HICON	hToolbarIcon;
};
~~~

**Return value**:
: Returns True

---

#### [2125] **NPPM_ADDTOOLBARICON_FORDARKMODE**
*Adds an icon to the toolbar.
This function only makes sense if called on response to NPPN_TBMODIFICATION notification.
cmdID must be a command function id which the plugin registered via getFuncsArray previously.
icon is a pointer to the toolbarIconsWithDarkMode structure.*

*(Added in v8.0, replacing old NPPM_ADDTOOLBARICON)*

**Parameters**:

*wParam [in]*
: INT cmdID

*lParam [in]*
: toolbarIconsWithDarkMode* icon
~~~
struct toolbarIconsWithDarkMode {
	HBITMAP	hToolbarBmp;
	HICON	hToolbarIcon;
	HICON	hToolbarIconDarkMode;
};
~~~

**Return value**:
: Returns True

---

#### [2105] **NPPM_ALLOCATECMDID**
*Obtains a number of consecutive menu item IDs for creating menus dynamically, with the guarantee of these IDs not clashing with any other plugins.*

**Parameters**:

*wParam [in]*
: int, requested number of IDs.

*lParam [out]*
: int, pointer to allocated range.

**Return value**:
: Returns 0 on failure, nonzero on success

---

#### [2137] **NPPM_ALLOCATEINDICATOR**
*Obtains a number of consecutive indicator IDs dynamically, with the guarantee of these IDs not clashing with Notepad++'s own internal indicator usage, nor usage by any other plugins that use this API to allocate their needed indicators. (new to v8.5.6)*

**Parameters**:

*wParam [in]*
: int, numberOfIndicators.

*lParam [out]*
: int, pointer to firstIndicatorID.

**Return value**
: Returns 0 on failure, nonzero on success

**Other information**
: If successful, `(*firstIndicatorID)+0` thru `(*firstIndicatorID)+numberOfIndicators-1` are the indicator numbers that have been set as reserved for use by the caller.

---

#### [2106] **NPPM_ALLOCATEMARKER**
*Obtains a number of consecutive marker IDs dynamically, with the guarantee of these IDs not clashing with any other plugins.*

**Parameters**:

*wParam [in]*
: int numberOfMarkers

*lParam [out]*
: int * firstMarkerID

**Return value**:
: Returns 0 on failure, nonzero on success.

---

#### [2104] **NPPM_ALLOCATESUPPORTED**
*Use to identify if subclassing is necessary*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns True always

---

#### [2134] **NPPM_CREATELEXER**
*Returns the ILexer pointer created by Lexilla.
Calls the lexilla `CreateLexer()` function; allows plugins
to set the lexer for a Scintilla instance created by
NPPM_CREATESCINTILLAHANDLE*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: const TCHAR * lexer_name, the name of the lexer

**Return value**:
: Returns the ILexer pointer created by Lexilla.

---

#### [2044] **NPPM_CREATESCINTILLAHANDLE**
*A plugin can create a Scintilla for its usage by sending this message to Notepad++.
The handle should be destroyed by NPPM_DESTROYSCINTILLAHANDLE message while exit the plugin.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: HWND pluginWindowHandle,
If set (non NULL), it will be the parent window of this created Scintilla handle, otherwise the parent window is Notepad++.

**Return value**:
: Returns the created Scintilla handle.

---

#### [2136] **NPPM_DARKMODESUBCLASSANDTHEME**
*Add support for generic dark mode.*
*(New to v8.5.4)*

**Parameters**:

*wParam [in]*
: ULONG dmFlags : values in `namespace NppDarkMode` (below)

*lParam [in]*
: HWND pluginWindowHandle,

**Return value**:
: Returns The new encoding mode.

**Other information**:

- Docking panels don't need to call NPPM_DARKMODESUBCLASSANDTHEME for main hwnd.

- Subclassing is applied automatically unless DWS_USEOWNDARKMODE flag is used.

- Might not work properly in C# plugins.

- `dmFlags` values in `NppDarkMode` namespace:

```
	namespace NppDarkMode
	{
		// Standard flags for main parent after its children are initialized.
		constexpr ULONG dmfInit =               0x0000000BUL;

		// Standard flags for main parent usually used in NPPN_DARKMODECHANGED.
		constexpr ULONG dmfHandleChange =       0x0000000CUL;
	};
```

**Examples:**

- after controls initializations in WM_INITDIALOG, in WM_CREATE or after CreateWindow:

```
auto success = static_cast<ULONG>(::SendMessage(nppData._nppHandle, NPPM_DARKMODESUBCLASSANDTHEME, static_cast<WPARAM>(NppDarkMode::dmfInit), reinterpret_cast<LPARAM>(mainHwnd)));
```

- handling dark mode change:

```
extern "C" __declspec(dllexport) void beNotified(SCNotification * notifyCode)

	switch (notifyCode->nmhdr.code)
	{
		case NPPN_DARKMODECHANGED:
		{
			::SendMessage(nppData._nppHandle, NPPM_DARKMODESUBCLASSANDTHEME, static_cast<WPARAM>(dmfHandleChange), reinterpret_cast<LPARAM>(mainHwnd));
			::SetWindowPos(mainHwnd, nullptr, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOZORDER | SWP_FRAMECHANGED); // to redraw titlebar and window
			break;
		}
	}
```

---

#### [2051] **NPPM_DECODESCI**
*Changes current buffer view to ansi.
view must be either 0 = main view or 1 = second view.*

**Parameters**:

*wParam [in]*
: INT view

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns The new encoding mode.

---

#### [2045] **NPPM_DESTROYSCINTILLAHANDLE**
*If plugin called NPPM_CREATESCINTILLAHANDLE to create a Scintilla handle, it should call this message to destroy this handle while it exit.*
*Not this message is deprecated. It is kept for the compatibility. Notepad++ will deallocate every createed Scintilla control on exit, this message returns TRUE but does nothing.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: HWND scintillaHandle2Destroy

**Return value**:
: Returns True

---

#### [2119] **NPPM_DISABLEAUTOUPDATE**
*Disables the auto update functionality of Notepad++.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns True

---

#### [2067] **NPPM_DMMGETPLUGINHWNDBYNAME**
*Retrieves the dialog handle corresponds to the windowName and moduleName.
You may need this message if you want to communicate with another plugin "dockable" dialog.*

**Parameters**:

*wParam [in]*
: const TCHAR * windowName

*lParam [in]*
: const TCHAR * moduleName

**Return value**:
: Returns NULL if moduleName is NULL. If windowName is NULL, then the first found window handle which matches with the moduleName will be returned

---

#### [2055] **NPPM_DMMHIDE**
*Hides the dialog which was previously regeistered by NPPM_DMMREGASDCKDLG.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: HWND hDlg,
is the handle of your dialog which should be hidden.

**Return value**:
: Returns True

---

#### [2057] **NPPM_DMMREGASDCKDLG**
*From v4.0, Notepad++ supports the dockable dialog feature for the plugins.
Pass the necessary dockingData to Notepad++ in order to make your dialog dockable.
Minimum informations which needs to be filled out are hClient, pszName, dlgID, uMask and pszModuleName.
Notice that rcFloat and iPrevCont shouldn't be filled. They are used internally*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: tTbData * dockingData
~~~
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
~~~
**Return value**:
: Returns True

---

#### [2054] **NPPM_DMMSHOW**
*Shows the dialog which was previously regeistered by NPPM_DMMREGASDCKDLG.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: HWND hDlg,
is the handle of your dialog which should be shown.

**Return value**:
: Returns True

---

#### [2056] **NPPM_DMMUPDATEDISPINFO**
*Updates (redraw) the dialog.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: HWND hDlg,
is the handle of the dialog which should be updated.

**Return value**:
: Returns True

---

#### [2059] **NPPM_DMMVIEWOTHERTAB**
*Shows the plugin dialog with the given name.
name should be the same value as previously used to register the dialog.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: TCHAR* name

**Return value**:
: Returns True

---

#### [2113] **NPPM_DOCLISTDISABLEEXTCOLUMN**
*Sets the extension column in Document List panel.
If disableOrNot is True, extension column is hidden otherwise it is visible.*

*Known as `NPPM_DOCSWITCHERDISABLECOLUMN` in v8.1.2 and earlier.*
*Known as `NPPM_DOCLISTDISABLECOLUMN` in v8.1.3 - v8.1.4.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: BOOL disableOrNot

**Return value**:
: Returns True

---

#### [2126] **NPPM_DOCLISTDISABLEPATHCOLUMN**
*Sets the path column in Document List panel. (New to v8.1.5)
If disableOrNot is True, path column is hidden otherwise it is visible.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: BOOL disableOrNot

**Return value**:
: Returns True

---

#### [2101] **NPPM_DOOPEN**
*Switches or openes a file with given fullPathName2Open.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: TCHAR * fullPathName2Open

**Return value**:
: Returns The return value is True (1) if the operation is successful, otherwise False (0).

---

#### [2050] **NPPM_ENCODESCI**
*Changes current buffer view to utf8.
view must be either 0 = main view or 1 = second view.*

**Parameters**:

*wParam [in]*
: INT view

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns The new encoding mode.

---

#### [2111] **NPPM_GETAPPDATAPLUGINSALLOWED**
*Retrieves the information whether plugins are loadable from %APPDATA%.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns True if loading plugins from %APPDATA% is allowed, False otherwise

---

#### [2135] **NPPM_GETBOOKMARKID**
*Returns the bookmark marker ID.
This allows plugins to choose an ID different from the bookmark marker ID, or to intentionally make use of the bookmark marker ID.
The plugin authors are encouraged to use this API (instead of using the static number from Notepad++ source code) to get bookmark marker ID dynamically.
It garantees plugins get always the right bookmark marker ID even it's been changed through the different Notepad++ versions. (New to v8.4.7)*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns the bookmark ID value as an integer


---


#### [2090] **NPPM_GETBUFFERENCODING**
*Retrieves the encoding from the document with the given bufferID.*

**Parameters**:

*wParam [in]*
: UINT_PTR bufferID

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns -1 on error, otherwise the encoding number. Here are the possible values (enum UniMode):
~~~
0: ANSI
1: UTF-8 with BOM
2: UTF-16 Big Ending with BOM
3: UTF-16 Little Ending with BOM
4: UTF-8 without BOM
5: uni7Bit
6: UTF-16 Big Ending without BOM
7: UTF-16 Little Ending without BOM
~~~
---

#### [2092] **NPPM_GETBUFFERFORMAT**
*Gets the current EOL format of the document with given bufferID.*

**Parameters**:

*wParam [in]*
: UINT_PTR bufferID

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns -1 on error, otherwise documents EOL format type. Here are the possible values (EOL formatType):
~~~
0: Windows (CRLF)
1: Macos (CR)
2: Unix (LF)
3. Unknown
~~~

---

#### [2083] **NPPM_GETBUFFERIDFROMPOS**
*Gets the document buffer ID from the given position.*

**Parameters**:

*wParam [in]*
: int position, is 0 based

*lParam [in]*
: int view, which should be either 0 (main view) or 1 (second view)

**Return value**:
: Returns 0 if given position is invalid, otherwise the document buffer ID.

---

#### [2088] **NPPM_GETBUFFERLANGTYPE**
*Retrieves the language type of the document with the given bufferID.*

**Parameters**:

*wParam [in]*
: UINT_PTR bufferID

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns -1 on error, otherwise a value from enum LangType.
Please see the enum LangType for all possible values.

---

#### [2084] **NPPM_GETCURRENTBUFFERID**
*Returns the buffer ID of the active document.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns the buffer ID of the active document.

---

#### [2133] **NPPM_GETCURRENTCMDLINE**
*Get the Current Command Line string. (New to v8.4.2).
Users should call it with commandLineStr as NULL to get the required number of TCHAR (not including the terminating nul character),
allocate commandLineStr buffer with the return value + 1, then call it again to get the current command line string.*

**Parameters**:

*wParam [in]*
: size_t strLen

*lParam [out]*
: TCHAR * commandLineStr

**Return value**:
: Returns the number of TCHAR copied/to copy.

---

#### [4033] **NPPM_GETCURRENTCOLUMN**
*Retrieves the column of the caret.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns the current, 0-based, column position of the caret.

---

#### [4026] **NPPM_GETCURRENTDIRECTORY**
*Retrieves the directory path of current document.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use.*

**Parameters**:

*wParam [in]*
: size_t directoryPathLen

*lParam [out]*
: TCHAR * directoryPath

**Return value**:
: Returns True on success and False if provided directoryPath buffer is not large enough

---

#### [2047] **NPPM_GETCURRENTDOCINDEX**
*Retrieves the current index of the current view.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int iView, which must bei eihter 0 (main view) or 1 (second view).

**Return value**:
: Returns -1 if the view is invisible (hidden), otherwise is the current index.

---

#### [2029] **NPPM_GETCURRENTLANGTYPE**
*Retrieves the language type of the current document.*

**Parameters**:

*wParam [ in ]*
: int, must be zero.

*lParam [ out ]*
: int * langType, pointer to the buffer receiving the language type of the current document
Please see the enum LangType for all possible values.


**Return value**
: Returns always True

---

#### [4032] **NPPM_GETCURRENTLINE**
*Retrieves the line of the caret.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns the current, 0-based, line position of the caret.

---

#### [4036] **NPPM_GETCURRENTLINESTR**
*Retrieves the text of the current line.
User is responsible to allocate a buffer which is large enough.*

**Parameters**:

*wParam [in]*
: size_t strLen

*lParam [out]*
: TCHAR * strLine

**Return value**:
: Returns True on success and False if provided strLine buffer is not large enough

---

#### [2130] **NPPM_GETCURRENTMACROSTATUS**
*Gets the current macro status (idle, recording, stopped, and playing back) as an enumeration class object. (Added v8.3.3)*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: An object of the enumeration class MacroStatus, with values:
- `MacroStatus::Idle` - means macro is not in use and it's empty
- `MacroStatus::RecordInProgress` - macro is currently being recorded
- `MacroStatus::RecordingStopped` - macro recording has been stopped
- `MacroStatus::PlayingBack` - macro is currently being played back

---

#### [2103] **NPPM_GETCURRENTNATIVELANGENCODING**
*Retrieves the code page associated with the current localisation of Notepad++.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns As of v6.6.6, returned values are 1252 (ISO 8859-1), 437 (OEM US) or 950 (Big5).


---

#### [2028] **NPPM_GETCURRENTSCINTILLA**
*Retrieves the current Scintilla view*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [out]*
: int * currentEdit, pointer to the buffer receiving the current view.
The returned value can be one of the following:

~~~
	Value        Meaning
	  0          The main view
	  1          The second view
	 -1          In case of an error
~~~

**Return value**:
: Returns always True

---

#### [2112] **NPPM_GETCURRENTVIEW**
*Retrieves the current used view. *

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns Either 0 when main view is active or 1 if secondary view is active.

---

#### [4030] **NPPM_GETCURRENTWORD**
*Retrieves the word containing the caret.
User is responsible to allocate a buffer which is large enough.*

**Parameters**:

*wParam [in]*
: size_t currentWordLen

*lParam [out]*
: TCHAR * currentWord

**Return value**:
: Returns True on success and False if provided currentWord buffer is not large enough

---

#### [2132] **NPPM_GETDARKMODECOLORS**
*Retrieves the colors used in Dark Mode.
User is responsible to allocate a buffer which is large enough.
(Added v8.4.1)*

**Parameters**:

*wParam [in]*
: size_t cbSize - must be filled with `sizeof(NppDarkMode::Colors)`

*lParam [out]*
: NppDarkMode::Colors* returnColors - must be a pre-allocated NppDarkMode::Colors struct

**Return value**:
: Returns True on success and False if provided currentWord buffer is not large enough

**Data Structure**
:
```
namespace NppDarkMode
{
    struct Colors
    {
        COLORREF background = 0;
        COLORREF softerBackground = 0;
        COLORREF hotBackground = 0;
        COLORREF pureBackground = 0;
        COLORREF errorBackground = 0;
        COLORREF text = 0;
        COLORREF darkerText = 0;
        COLORREF disabledText = 0;
        COLORREF linkText = 0;
        COLORREF edge = 0;
    };
}
```

---

#### [2115] **NPPM_GETEDITORDEFAULTBACKGROUNDCOLOR**
*Retrieves the current editor default background color.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns The color as integer with hex format being 0x00bbggrr

---

#### [2114] **NPPM_GETEDITORDEFAULTFOREGROUNDCOLOR**
*Retrieves the current editor default foreground.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns The color as integer with hex format being 0x00bbggrr

---

#### [2069] **NPPM_GETENABLETHEMETEXTUREFUNC** [DEPRECATED]
*Deprecated v8.4.9: Use EnableThemeTexture from uxtheme.h instead.*

*`NPPM_GETENABLETHEMETEXTUREFUNC_DEPRECATED`: Returns if visual style of the background of a dialog window is enabled or not.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns A proc address or NULL

---

#### [2127] **NPPM_GETEXTERNALLEXERAUTOINDENTMODE**
*Get ExternalLexerAutoIndentMode for an installed external programming language.
Puts that mode in the output object. (Added v8.3.3)*

**Parameters**:

*wParam [in]*
: const tChar\* languageName, the name of the language to get

*lParam [out]*
: ExternalLexerAutoIndentMode &autoIndentMode, an object of the enumeration class ExternalLexerAutoIndentMode, with values:
- `ExternalLexerAutoIndentMode::Standard` => 0
- `ExternalLexerAutoIndentMode::C_Like`   => 1
- `ExternalLexerAutoIndentMode::Custom`   => 2


**Return value**:
: TRUE for successful searches, otherwise FALSE.

---

#### [4029] **NPPM_GETEXTPART**
*Retrieves the extension of the filename of the current document.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use.*

**Parameters**:

*wParam [in]*
: size_t extensionLen

*lParam [out]*
: TCHAR * extension

**Return value**:
: Returns True on success and False if provided extension buffer is not large enough

---

#### [4027] **NPPM_GETFILENAME**
*Retrieves the file name of current document.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use.*

**Parameters**:

*wParam [in]*
: size_t fileNameLen

*lParam [out]*
: TCHAR * fileName

**Return value**:
: Returns True on success and False if provided fileName buffer is not large enough

---

#### [4035] **NPPM_GETFILENAMEATCURSOR**
*Retrieves the filename at the current caret position.
Note, while this message has been created, and is used internally, to retrieve a filename at the current caret position, it does return anything which fulfils the requirements, even single words.*

**Parameters**:

*wParam [in]*
: INT length

*lParam [out]*
: TCHAR* buffer

**Return value**:
: Returns True if the size of the provided buffer is large enough, False otherwise.

---

#### [4025] **NPPM_GETFULLCURRENTPATH**
*Retrieves the full path of the current document.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use.*

**Parameters**:

*wParam [in]*
: size_t fullPathLen

*lParam [out]*
: TCHAR * fullPath

**Return value**:
: Returns True on success and False if provided fullPath buffer is not large enough

---

#### [2082] **NPPM_GETFULLPATHFROMBUFFERID**
*Gets the full path file name from the given bufferID.
First call should be made with buffer set to NULL to retrieve the actual size needed.
Second call is sent with correctly allocated buffer, +1 for trailing null, to retrieve the full path file name.*

**Parameters**:

*wParam [in]*
: UINT_PTR bufferID

*lParam [out]*
: TCHAR * buffer

**Return value**:
: Returns -1 if bufferID does not exist, otherwise the number of chars copied/to copy.

---

#### [2108] **NPPM_GETLANGUAGEDESC**
*Retrieves the description of the current language used.
First call should be made with buffer set to NULL to retrieve the actual size needed.
Second call is sent with correctly allocated buffer to retrieve the description.*

**Parameters**:

*wParam [in]*
: int langTypeID

*lParam [out]*
: TCHAR* buffer

**Return value**:
: Returns The number of characters needed or copied

---


#### [2107] **NPPM_GETLANGUAGENAME**
*Retrieves the name of the current language used.
First call should be made with buffer set to NULL to retrieve the actual size needed.
Second call is sent with correctly allocated buffer to retrieve the language name.*

**Parameters**:

*wParam [in]*
: int langTypeID

*lParam [out]*
: TCHAR* buffer

**Return value**:
: Returns The number of characters needed or copied

---

#### [2124] **NPPM_GETLINENUMBERWIDTHMODE**
*Get line number margin width in dynamic width mode (LINENUMWIDTH_DYNAMIC) or constant width mode (LINENUMWIDTH_CONSTANT)*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns the line number margin width mode, either the LINENUMWIDTH_DYNAMIC or LINENUMWIDTH_CONSTANT value.

---

#### [2049] **NPPM_GETMENUHANDLE**
*Retrieves either the plugin or the main menu handle of Notepad++.*

**Parameters**:

*wParam [in]*
: int whichMenu, which can be 0 (plugin menu) or 1 (main menu)

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns the requested menu handle.

---

#### [4028] **NPPM_GETNAMEPART**
*Retrieves the part of filename, without extension, of the current document.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use.*

**Parameters**:

*wParam [in]*
: size_t namePartLen

*lParam [out]*
: TCHAR * namePart

**Return value**:
: Returns True on success and False if provided namePart buffer is not large enough

---

#### [2031] **NPPM_GETNBOPENFILES**
*Retrieves the number of files currently open*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: Integer of one of the following values:
~~~
	Value        Meaning
	  0          the total number of files opened in Notepad++
	  1          number of files opened in the main view
	  2          number of files opened in the second view
~~~

**Return value**:
: Returns number of open files

---

#### [2037] **NPPM_GETNBSESSIONFILES**
*Retrieves the number of files to load in the session sessionFileName.
sessionFileName should be a full path name of an xml file.*

**Parameters**:

*wParam [out]*
: BOOL* isValidXML, if the lParam pointer is null, then this parameter will be ignored. TRUE if XML is valid, otherwise FALSE. (added in v8.6)

*lParam [in]*
: const TCHAR * sessionFileName

**Return value**:
: Returns 0 if sessionFileName is an empty string/NULL, or XML session file is corrupted/invalid, else the number of files.

---

#### [2046] **NPPM_GETNBUSERLANG**
*Retrieves the number of user defined languages and, optionally, the starting menu id.
Note, udlID is optional, if not used set it to 0, otherwise an integer pointer is needed to retrieve the menu identifier.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [out]*
: INT* udlID

**Return value**:
: Returns The number of user defined languages identified

---

#### [4031] **NPPM_GETNPPDIRECTORY**
*Retrieves the full path of the directory where the Notepad++ binary is located.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use.*

**Parameters**:

*wParam [in]*
: size_t nppDirLen

*lParam [out]*
: TCHAR * nppDir

**Return value**:
: Returns True on success and False if provided nppDir buffer is not large enough

---

#### [4034] **NPPM_GETNPPFULLFILEPATH**
*Retrieves the full path of the Notepad++ executable.*

**Parameters**:

*wParam [in]*
: INT length

*lParam [out]*
: TCHAR* buffer

**Return value**:
: Returns True if the provided buffer size was big enough to write the full path to it, False otherwise.

---

#### [2074] **NPPM_GETNPPVERSION**
*Retrieves the current Notepad++ version.
The value is made up of 2 parts: the major version (the high word) and minor version (the low word).
Note that this message is supported by the v4.7 or higher version; earlier versions return 0.
v8.4.1 adds the ability to pad the result to make comparisons between versions like 8.4.1 and 8.5 easier
(without the padding, they would have been 8|41 and 8|5, and since 5 is less than 41, it would have incorrectly shown up
as 8.5 coming before 8.41; with the padding flag on, they will be 8|410 and 8|500, so 8.5 will properly
come after 8.4.1).*

**Parameters**:

*wParam [in]*
: Boolean ADD_ZERO_PADDING, will add zero padding, as per the tables below:
~~~
ADD_ZERO_PADDING == TRUE

    version  | HIWORD | LOWORD
    -----------------------------
    8.9.6.4  | 8      | 964
    9        | 9      | 0
    6.9      | 6      | 900
    6.6.6    | 6      | 660
    13.6.6.6 | 13     | 666


ADD_ZERO_PADDING == FALSE

    version  | HIWORD | LOWORD
    -----------------------------
    8.9.6.4  | 8      | 964
    9        | 9      | 0
    6.9      | 6      | 9
    6.6.6    | 6      | 66
    13.6.6.6 | 13     | 666
~~~

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns a LONG value containing the current version.

---

#### [2032] **NPPM_GETOPENFILENAMES**
*Retrieves the open files of both views.
User is responsible to allocate an big enough fileNames array.*

**Parameters**:

*wParam [out]*
: TCHAR ** fileNames,
receives the full path names of all the opened files in Notepad++

*lParam [in]*
: int nbFile,
is the size of the fileNames array. Get this value by using NPPM_GETNBOPENFILES message with constant ALL_OPEN_FILES, then allocate fileNames array with this value.

**Return value**:
: Returns The number of files copied into fileNames array.

---

#### [2041] **NPPM_GETOPENFILENAMESPRIMARY**
*Retrieves the open files of the main view.
User is responsible to allocate an big enough fileNames array.*

**Parameters**:

*wParam [out]*
: TCHAR ** fileNames,
receives the full path names of the opened files in the primary view

*lParam [in]*
: int nbFile,
is the size of the fileNames array. Get this value by using NPPM_GETNBOPENFILES message with constant PRIMARY_VIEW, then allocate fileNames array with this value.


**Return value**:
: Returns The number of files copied into fileNames array.

---

#### [2042] **NPPM_GETOPENFILENAMESSECOND**
*Retrieves the open files of the secondary view.
User is responsible to allocate an big enough fileNames array.*

**Parameters**:

*wParam [out]*
: TCHAR ** fileNames,
receives the full path names of the opened files in the second view

*lParam [in]*
: int nbFile,
is the size of your fileNames array. You should get this value by using NPPM_GETNBOPENFILES message with constant SECOND_VIEW, then allocate fileNames array with this value.

**Return value**:
: Returns The number of files copied into fileNames array.

---

#### [2121] **NPPM_GETPLUGINHOMEPATH**
*Retrieves the plugin home root path.
First call should be made with length set to 0 and buffer set to NULL to retrieve the actual size of the path. Second call sends the correct length and allocated buffer, both +1 for trailing NULL, to get the path name.*

**Parameters**:

*wParam [in]*
: SIZE_T length

*lParam [out]*
: TCHAR* buffer

**Return value**:
: Returns the number of TCHAR copied to buffer without trailing NULL.

---

#### [2070] **NPPM_GETPLUGINSCONFIGDIR**
*Retrieves the path of the plugin config directory.
User is responsible to allocate a buffer which is large enough.
MAX_PATH is suggested to use.*

**Parameters**:

*wParam [in]*
: int strLen

*lParam [out]*
: TCHAR *pluginsConfDir

**Return value**:
: Returns True

---

#### [2081] **NPPM_GETPOSFROMBUFFERID**
*Gets 0-based document position from given buffer ID, which is held in the 30 lowest bits of the return value on success.
Bit 30 indicates which view has the buffer (clear for main view, set for sub view).*

**Parameters**:

*wParam [in]*
: UINT_PTR bufferID

*lParam [in]*
: int priorityView,
is main view (0), or sub view (1). So the search will check into the view of choice. However if the given bufferID cannot be found in the chosen view, the other view will be searched.  

**Return value**:
: Returns -1 if bufferID doesn't exist else the position.

---
#### [2122] **NPPM_GETSETTINGSONCLOUDPATH**
*Get settings on cloud path. It's useful if plugins want to store its settings on Cloud, if this path is set.*

*First call should be made with buffer set to NULL to retrieve the actual size needed.
Second call is sent with correctly allocated buffer, +1 for trailing null, to retrieve the full path file name.*


**Parameters**:

*wParam [in]*
: size_t strLen,
maximum bytes to read for the path string, including the final NULL byte

*lParam [out]*
: TCHAR *settingsOnCloudPath,
the path for cloud settings obtained by this message

**Return value**:
: Returns the length of the path string

---

#### [2038] **NPPM_GETSESSIONFILES**
*Retrieves the files' full path name from a session file.*

**Parameters**:

*wParam [out]*
: TCHAR ** sessionFileArray,
the array in which the files' full path of the same group are written.
To allocate the array with the proper size, send message NPPM_GETNBSESSIONFILES.

*lParam [in]*
: const TCHAR * sessionFileName,
the path to the session file from which you retrieve the files

**Return value**:
: Returns True

---

#### [2100] **NPPM_GETSHORTCUTBYCMDID**
*Gets the mapped plugin command shortcut. May be called after getting NPPN_READY notification.*

**Parameters**:

*wParam [in]*
: int cmdID

*lParam [out]*
: ShortcutKey * sk, which is defined as
~~~
struct ShortcutKey {
	bool _isCtrl;
	bool _isAlt;
	bool _isShift;
	UCHAR _key;
}
~~~

**Return value**:
: Returns True if this function call is successful and shortcut is enable, otherwise False

---

#### [2066] **NPPM_GETWINDOWSVERSION**
*Retrieves the windows operating system version.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
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

#### [2096] **NPPM_HIDEMENU**
*Either hides or shows the menubar.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: BOOL hideOrNot

**Return value**:
: Returns the previous status before this operation.

---

#### [2098] **NPPM_HIDESTATUSBAR**
*Either hides or shows the statusbar.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: BOOL hideOrNot

**Return value**:
: Returns the previous status before this operation.

---

#### [2075] **NPPM_HIDETABBAR**
*Either hides or shows the tabbar.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: BOOL hideOrNot

**Return value**:
: Returns the previous status before this operation.

---

#### [2094] **NPPM_HIDETOOLBAR**
*Either hides or shows the toolbar.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: BOOL hideOrNot

**Return value**:
: Returns the previous status before this operation.

---

#### [2129] **NPPM_ISAUTOINDENTON**
*Checks the current Use Auto-Indentation setting in Notepad++ Preferences.  (Added v8.3.3)*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: TRUE if Auto-Indentation is on, FALSE otherwise.

---

#### [2110] **NPPM_ISDOCLISTSHOWN**
*Checks the visibility of the Document List panel.*

*Known as `NPPM_ISDOCSWITCHERSHOWN` in v8.1.2 and earlier.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns True if the Document List panel is currently shown, False otherwise

---

#### [2131] **NPPM_ISDARKMODEENABLED**
*Notepad++ Dark Mode is enable.  (Added v8.4.1)*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: TRUE when Notepad++ Dark Mode is enable, FALSE when it is not.

---

#### [2097] **NPPM_ISMENUHIDDEN**
*Retrieves the current status of menubar.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns True if the menubar is hidden, False otherwise.


---

#### [2099] **NPPM_ISSTATUSBARHIDDEN**
*Retrieves the current status of the statusbar.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns True if the status bar is hidden, False otherwise.

---

#### [2076] **NPPM_ISTABBARHIDDEN**
*Retrieves the current status of tabbar.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns True if the tabbar is hidden, False otherwise.

---

#### [2095] **NPPM_ISTOOLBARHIDDEN**
*Retrieves the current status of toolbar.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns True if the toolbar is hidden, False otherwise.


---

#### [2053] **NPPM_LAUNCHFINDINFILESDLG**
*Triggers the Find in files dialog.*

**Parameters**:

*wParam [in]*
: TCHAR * dir2Search or NULL

*lParam [in]*
: TCHAR * filter or NULL

**Return value**:
: Returns True

---

#### [2058] **NPPM_LOADSESSION**
*Opens all files of same session in Notepad++ via a xml format session file sessionFileName.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: const TCHAR * sessionFileName

**Return value**:
: Returns True

---

#### [2068] **NPPM_MAKECURRENTBUFFERDIRTY**
*Makes the current document dirty, aka sets the save state to unsaved.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns True

---

#### [2072] **NPPM_MENUCOMMAND**
*Calls all possible Notepad++ menu commands.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int commandID,
see menuCmdID.h for all possible values.

**Return value**:
: Returns True

---

#### [2036] **NPPM_MODELESSDIALOG**
*For each modeless dialog created in your plugin, you should register it (and unregister it when you destroy it) by using this message.
If this message is not used, then your dialog won't react with the key stroke messages such as `Ctrl-C`, `Ctrl-V` or `TAB` key, so it is
highly recommended that you use this for all modeless dialogs in your plugin.*

**Parameters**:

*wParam [in]*
: int op,
the operation mode.
Use the value `MODELESSDIALOGADD` to register and `MODELESSDIALOGREMOVE` to unregister (both are defined in `Notepad_plus_msgs.h`).

*lParam [in]*
: HWND hDlg,
is the handle of the dialog to be registered

**Return value**:
: Returns the hadle of the dialog (hDlg) to be registered/unregistered on success, NULL on failure

---

#### [2071] **NPPM_MSGTOPLUGIN**
*Allows the communication between 2 plugins.
For example, plugin X can execute a command of plugin Y if plugin X knows the command ID and the file name of plugin Y.*

**Parameters**:

*wParam [in]*
: TCHAR * destModuleName,
is the complete module name (with the extesion .dll) of plugin with which you want to communicate (plugin Y).

*lParam [out]*
:  CommunicationInfo * info
~~~
struct CommunicationInfo {
	long internalMsg;
	const TCHAR * srcModuleName;
	void * info; // defined by plugin
};
~~~
: *internalMsg* is an integer defined by plugin Y, known by plugin X, identifying the message being sent.
: *srcModuleName* is the complete module name (with the extesion .dll) of caller(plugin X).
: *info* is defined by plugin, the informations to be exchanged between X and Y. It's a void pointer so it should be defined by plugin Y and known by plugin X.
The returned value is TRUE if Notepad++ found the plugin by its module name (destModuleName), and pass the info (communicationInfo) to the module. The returned value is FALSE if no plugin with such name is found.

**Return value**:
: Returns True if Notepad++ found the plugin by its module name (destModuleName), and pass the info (communicationInfo) to the module, False otherwise.

---

#### [2085] **NPPM_RELOADBUFFERID**
*Reloads the document with the given bufferID.
If doAlertOrNot is True, then a message box will display to ask user to reload the document, otherwise document will be loaded without asking user.*

**Parameters**:

*wParam [in]*
: UINT_PTR bufferID

*lParam [in]*
: BOOL doAlertOrNot

**Return value**:
: Returns True on success, False otherwise

---

#### [2060] **NPPM_RELOADFILE**
*Reloads the file indicated by filePathName2Reload.*

**Parameters**:

*wParam [in]*
: BOOL withAlert,
if True then an alert message box will be launched.

*lParam [in]*
: TCHAR *filePathName2Reload

**Return value**:
: Returns True

---

#### [2120] **NPPM_REMOVESHORTCUTBYCMDID**
*Removes the assigned shortcut mapped to cmdID.*

**Parameters**:

*wParam [in]*
: int32 cmdID

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns True if function call is successful, False otherwise.

---

#### [2063] **NPPM_SAVEALLFILES**
*Saves all opened documents.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns FALSE when no file needs to be saved, else TRUE if there is at least one file saved.

---

#### [2062] **NPPM_SAVECURRENTFILE**
*Saves the current document.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int, must be zero.

**Return value**:
: Returns True

---

#### [2102] **NPPM_SAVECURRENTFILEAS**
*Saves the current file.
saveAsCopy must be either 0 to save, or 1 to save a copy of the current filename.*

**Parameters**:

*wParam [in]*
: int saveAsCopy

*lParam [in]*
: TCHAR* filename

**Return value**:
: Returns True on success, False otherwise

---

#### [2040] **NPPM_SAVECURRENTSESSION**
*Saves the current opened files in Notepad++ as a group of files (session) as an xml file.
The xml full path name has to be provided by sessionFileName.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: const TCHAR *sessionFileName

**Return value**:
: Returns True

---

#### [2118] **NPPM_SAVEFILE**
*Save the file (opened in Notepad++) with the given filename.
filename must be the full file path for the file to be saved.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: const TCHAR* filename

**Return value**:
: Returns True on success False on filename not found

---

#### [2039] **NPPM_SAVESESSION**
*Creates an session file for a defined set of files.
sessionInfo is a pointer to sessionInfo structure.
Note, contrary to NPPM_SAVECURRENTSESSION, which saves the current opened files, this call can be used to freely define any file which should be part of a session.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: sessionInfo*

**Return value**:
: Returns On success a TCHAR* to full path of the session filename to be saved or NULL otherwise

---

#### [2091] **NPPM_SETBUFFERENCODING**
*Sets the document encoding for the given bufferID.
Can only be done on new, unedited files.*

**Parameters**:

*wParam [in]*
: UINT_PTR bufferID

*lParam [in]*
: UniMode encoding - see **NPPM_GETBUFFERENCODING** enum UniMode valid values

**Return value**:
: Returns True on success, False otherwise.

---

#### [2093] **NPPM_SETBUFFERFORMAT**
*Sets EOL format to the document with the given bufferID.*

**Parameters**:

*wParam [in]*
: UINT_PTR bufferID

*lParam [in]*
: formatType format - see **NPPM_GETBUFFERFORMAT** for valid values of EOL formatType

**Return value**:
: Returns True on success, False otherwise.

---

#### [2089] **NPPM_SETBUFFERLANGTYPE**
*Sets the language type of the document based on the given bufferID.
See enum LangType for valid values, L_USER and L_EXTERNAL are not supported.*

**Parameters**:

*wParam [in]*
: UINT_PTR bufferID

*lParam [in]*
: LangType type2Set

**Return value**:
: Returns True on success, False otherwise.

---

#### [2030] **NPPM_SETCURRENTLANGTYPE**
*Sets a new language type to the current used document.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int langType, please see the enum LangType for all possible values.

**Return value**:
: Returns True

---

#### [2117] **NPPM_SETEDITORBORDEREDGE**
*Extends the Scintilla window with an extra style.
If value is True adds an additional sunken edge style to the Scintilla window else it removes the extended style from the window. See MSDN Extended Window Styles for more information.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: BOOL value

**Return value**:
: Returns True

---

#### [2128] **NPPM_SETEXTERNALLEXERAUTOINDENTMODE**
*Set ExternalLexerAutoIndentMode for an installed external programming language. (Added v8.3.3)*

**Parameters**:

*wParam [in]*
: const tChar\* languageName, the name of the language to set

*lParam [in]*
: ExternalLexerAutoIndentMode autoIndentMode, an object of the enumeration class ExternalLexerAutoIndentMode, where you supply one of the following values:
- `ExternalLexerAutoIndentMode::Standard` => 0
- `ExternalLexerAutoIndentMode::C_Like`   => 1
- `ExternalLexerAutoIndentMode::Custom`   => 2

**Return value**:
: TRUE for successful searches, otherwise FALSE.

---

#### [2123] **NPPM_SETLINENUMBERWIDTHMODE**
*Set line number margin width in dynamic width mode (LINENUMWIDTH_DYNAMIC) or constant width mode (LINENUMWIDTH_CONSTANT).
It may help some plugins to disable non-dynamic line number margins width to have a smooth visual effect while vertical scrolling the content in Notepad++*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: int widthMode, must be one of the values LINENUMWIDTH_DYNAMIC or LINENUMWIDTH_CONSTANT.

**Return value**:
: Returns True on success, False on failure

---

#### [2064] **NPPM_SETMENUITEMCHECK**
*Sets or removes the check on a item of plugin menu and of tab bar (if any).*

**Parameters**:

*wParam [in]*
: int pluginCmdID,
is the plugin command ID which corresponds to the plugin menu item

*lParam [in]*
: BOOL doCheck

**Return value**:
: Returns True

---

#### [2116] **NPPM_SETSMOOTHFONT**
*Uses underlying Scintilla command SCI_SETFONTQUALITY to manage the font quality.
If value is True, this message sets SC_EFF_QUALITY_LCD_OPTIMIZED else SC_EFF_QUALITY_DEFAULT*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: BOOL value

**Return value**:
: Returns True

---

#### [2048] **NPPM_SETSTATUSBAR**
*Sets value in the specified field of a statusbar.*

**Parameters**:

*wParam [in]*
: int field, possible values are
~~~
STATUSBAR_DOC_TYPE      0
STATUSBAR_DOC_SIZE      1
STATUSBAR_CUR_POS       2
STATUSBAR_EOF_FORMAT    3
STATUSBAR_UNICODE_TYPE  4
STATUSBAR_TYPING_MODE   5
~~~

*lParam [out]*
: TCHAR * value, pointer to the new value.

**Return value**:
: Returns 0 on failure, nonzero on success

---

#### [2109] **NPPM_SHOWDOCLIST**
*Show or hide the Document List panel.
If toShowOrNot is True, the Document List panel is shown otherwise it is hidden.*

*Known as `NPPM_SHOWDOCSWITCHER` in v8.1.2 and earlier.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: BOOL toShowOrNot

**Return value**:
: Returns True

---

#### [2061] **NPPM_SWITCHTOFILE**
*Switches to the document which matches with the given filePathName2switch.*

**Parameters**:

*wParam [in]*
: int, must be zero.

*lParam [in]*
: TCHAR *filePathName2switch

**Return value**:
: Returns True

---

#### [2073] **NPPM_TRIGGERTABBARCONTEXTMENU**
*Triggers the tabbar context menu for the given view and index.*

**Parameters**:

*wParam [in]*
: int whichView

*lParam [in]*
: int index2Activate

**Return value**:
: Returns True

---

## Notepad++ notifications

A notification is sent using a [WM_NOTIFY](https://docs.microsoft.com/en-us/windows/win32/controls/wm-notify) message and therefore uses the [NMHDR structure](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-nmhdr).

The notification carries three Fields in the notification structure, each of which holds an integer value.  The ***code*** Field integer is always the notification number.  The ***hwndFrom*** and ***idFrom*** Field integers _normally_ refer to the Notepad++ window handle **hwndNpp** and the Notepad++ buffer identifier **BufferID**; however, they can also be pointers to data structures, in which case, the description of that particular Notification will describe the structure, or call out a common c/c++ data type, or otherwise describe the usage of that Field for that Notification.

The notification IDs for each of these named notifications can be found in the source code in [Notepad_plus_msgs.h](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/src/MISC/PluginsManager/Notepad_plus_msgs.h).

#### **Notification Key**

The general layout of the following notifications look like this

> [ID Number] **NOTIFICATION NAME**
>
> *Description*
>
> **Fields**
> : *code*:
> : *hwndFrom*:
> : *idFrom*:

- **[ID Number]** is the integer value for that notification
- **NOTIFICATION NAME** is the Notepad++ notification constant name (like `NPPN_READY`)
- **Description** informs about the usage of the notification and provides additional information if needed.
- **Fields** are the parameters to be provided by the notification.
    - ***hwndFrom*** normally holds the **hwndNpp**, which means that the window handle for the current Notepad++ window is passed as that argument.  If it is shown as a `0` or `NULL`, then that notification does not use this Field.  If it is something else, a full description will be provided.
    - ***idFrom*** normally holds the **BufferID**, which means that the buffer identification integer for the current editor buffer is passed as that argument.  If it is shown as `0` or `NULL`, then that notification does not use this Field.  If it is something else, a full description will be provided.

---
---

#### [1019] **NPPN_BEFORESHUTDOWN**
*To notify plugins that Notepad++ shutdown has been triggered, files have not been closed yet*

**Fields:**

	code: 		NPPN_BEFORESHUTDOWN
	hwndFrom:	hwndNpp
	idFrom:		0

---

#### [1010] **NPPN_BUFFERACTIVATED**
*To notify plugins that a buffer was activated (put to foreground).*

**Fields:**

	code:		NPPN_BUFFERACTIVATED
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1020] **NPPN_CANCELSHUTDOWN**
*To notify plugins that Notepad++ shutdown has been canceled*

**Fields:**

	code:		NPPN_CANCELSHUTDOWN
	hwndFrom:	hwndNpp
	idFrom:		0

---

#### [1028] **NPPN_CMDLINEPLUGINMSG**
*To notify plugins that the new argument for plugins (via `-pluginMessage="YOUR_PLUGIN_ARGUMENT"` in [command line](../command-prompt/)) is available. (New to v8.4.2).*

**Fields:**

	code:		NPPN_CMDLINEPLUGINMSG
	hwndFrom:	hwndNpp
	idFrom:		pluginMessage, where pluginMessage is pointer of type wchar_t

---

#### [1027] **NPPN_DARKMODECHANGED**
*To notify plugins that Dark Mode was changed (either enabled or disabled).
(Added v8.4.1)*

**Fields:**

	code:		NPPN_DARKMODECHANGED
	hwndFrom:	hwndNpp
	idFrom:		0

---

#### [1017] **NPPN_DOCORDERCHANGED**
*To notify plugins that document order is changed*

**Fields:**

	code:		NPPN_DOCORDERCHANGED
	hwndFrom:	newIndex
	idFrom:		BufferID

---

#### [1029] **NPPN_EXTERNALLEXERBUFFER**
*To notify lexer plugins that the buffer (in idFrom) is just applied to a external lexer. (New to v8.5).*

**Fields:**

	code:		NPPN_EXTERNALLEXERBUFFER
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1003] **NPPN_FILEBEFORECLOSE**
*To notify plugins that the current file is about to be closed*

**Fields:**

	code:		NPPN_FILEBEFORECLOSE
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1024] **NPPN_FILEBEFOREDELETE**
*To notify plugins that file is to be deleted*

**Fields:**

	code:		NPPN_FILEBEFOREDELETE
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1014] **NPPN_FILEBEFORELOAD**
*To notify plugins that the current file is about to be loaded*

**Fields:**

	code:		NPPN_FILEBEFORELOAD
	hwndFrom:	hwndNpp
	idFrom:		NULL

---

#### [1006] **NPPN_FILEBEFOREOPEN**
*To notify plugins that the current file is about to be opened*

**Fields:**

	code:		NPPN_FILEBEFOREOPEN
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1021] **NPPN_FILEBEFORERENAME**
*To notify plugins that file is to be renamed*

**Fields:**

	code:		NPPN_FILEBEFORERENAME
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1007] **NPPN_FILEBEFORESAVE**
*To notify plugins that the current file is about to be saved*

**Fields:**

	code:		NPPN_FILEBEFORESAVE
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1005] **NPPN_FILECLOSED**
*To notify plugins that the current file is just closed*

**Fields:**

	code:		NPPN_FILECLOSED
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1026] **NPPN_FILEDELETED**
*To notify plugins that file has been deleted*

**Fields:**

	code:		NPPN_FILEDELETED
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1025] **NPPN_FILEDELETEFAILED**
*To notify plugins that file deletion has failed*

**Fields:**

	code:		NPPN_FILEDELETEFAILED
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1015] **NPPN_FILELOADFAILED**
*To notify plugins that file open operation failed*

**Fields:**

	code:		NPPN_FILELOADFAILED
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1004] **NPPN_FILEOPENED**
*To notify plugins that the current file is just opened*

**Fields:**

	code:		NPPN_FILEOPENED
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1022] **NPPN_FILERENAMECANCEL**
*To notify plugins that file rename has been canceled*

**Fields:**

	code:		NPPN_FILERENAMECANCEL
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1023] **NPPN_FILERENAMED**
*To notify plugins that file has been renamed*

**Fields:**

	code:		NPPN_FILERENAMED
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1008] **NPPN_FILESAVED**
*To notify plugins that the current file is just saved*

**Fields:**

	code:		NPPN_FILESAVED
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1011] **NPPN_LANGCHANGED**
*To notify plugins that the language in the current doc is just changed.*

**Fields:**

	code:		NPPN_LANGCHANGED
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---

#### [1016] **NPPN_READONLYCHANGED**
*To notify plugins that current document changed the read-only status*

**Fields:**

	code:		NPPN_READONLYCHANGED
	hwndFrom:	BufferID
	idFrom:		docStatus, either one or the combination of the following values
				DOCSTATUS_READONLY    1
				DOCSTATUS_BUFFERDIRTY 2

---

#### [1001] **NPPN_READY**
*To notify plugins that all the procedures of the launch of Notepad++ are done.*

**Fields:**

	code:		NPPN_READY
	hwndFrom:	hwndNpp
	idFrom:		0

---

#### [1013] **NPPN_SHORTCUTREMAPPED**
*To notify plugins that plugin command shortcut is remapped.*

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

#### [1009] **NPPN_SHUTDOWN**
*To notify plugins that Notepad++ is about to be shut down.*

**Fields:**

	code:		NPPN_SHUTDOWN
	hwndFrom:	hwndNpp
	idFrom:		0

---

#### [1018] **NPPN_SNAPSHOTDIRTYFILELOADED**
*To notify plugins that a snapshot dirty file is loaded on startup*

**Fields:**

	code:		NPPN_SNAPSHOTDIRTYFILELOADED
	hwndFrom:	NULL
	idFrom:		BufferID

---

#### [1002] **NPPN_TBMODIFICATION**
*To notify plugins that toolbar icons can be registered*

**Fields:**

	code:		NPPN_TBMODIFICATION
	hwndFrom:	hwndNpp
	idFrom:		0

---

#### [1012] **NPPN_WORDSTYLESUPDATED**
*To notify plugins that user initiated a WordStyleDlg change.*

**Fields:**

	code:		NPPN_WORDSTYLESUPDATED
	hwndFrom:	hwndNpp
	idFrom:		BufferID

---
