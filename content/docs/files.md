---
title: Working with Files
weight: 9
---

# Working with Files

A "file" is the basic unit of what is edited in Notepad++, but that term actually covers multiple related concepts.  Primarily, the "file" is the series of bytes stored on a disk or other storage medium and accessed through your computer's filesystem; and pedantically, if the document you are editing has never been saved to the filesystem, it's not technically a file, though common usage applies that term to unsaved documents as well.  The "document" refers to the text being edited, whether it's a new, unsaved document, or whether it's a document that's been previously saved as a file on the filesystem.  And finally, in Notepad++, each document is presented in a [Tab](../other-resources/#tabs) in one of the two [Views](../views/) of the Notepad++ user interface, which are the graphical containers which Notepad++ uses to manipulate files and other documents, though many users think of the user interface element as the "file" as well.

## File Menu

The **File** menu contains many of the normal file-operation actions found in most applications.  Notepad++ also includes other custom actions which are useful to understand.

- **New**: Creates a new document, and displays that empty document in a Tab in the active View.
- **Open**: Opens an existing file from the filesystem, and displays that document in a Tab in the active View.
- **Open Containing Folder >**:
    - **Explorer**: Opens an instance of the Windows Explorer, starting in the folder (also known as the "directory") which contains the active file.
    - **cmd**: Opens an instance of Windows' `cmd.exe`, starting in the folder which contains the active file.
    - **Folder as Workspace**: Opens the active file's folder in Notepad++'s [Folder as Workspace](../session/#folder-as-workspace) panel.
- **Open in Default Viewer**: This will make use of the Windows "filetype association" for the active file (based on the file extension).
    - It does the equivalent of double-clicking on a file in Windows Explorer.
    - If the document has never been saved as a file, this action will be grayed out and the menu entry cannot be used.
    - If the filetype has no associated default action in Windows, this action will be grayed out and the menu entry cannot be used.
    - If the filetype is associated with Notepad++, and would thus just re-open the file in Notepad++, this action will be grayed out and the menu entry cannot be used.
- **Open Folder as Workspace**: Opens the active file's folder in Notepad++'s [Folder as Workspace](../session/#folder-as-workspace) panel.
- **Reload from Disk**: This will re-read the bytes of the file from the filesystem, replacing the current contents of the documented being edited with the last-saved version (and thus losing any changes that might have been made in Notepad++).
    - If you have [**Settings > Preferences > MISC > File Status Auto-detection**](../preferences/#misc) turned on, you Notepad++ can automatically run the equivalent of this command for you, without you having to use this menu entry.
    - Any [bookmarks](../searching/#manipulating-bookmarks) or [token styling](../searching/#marking-with-a-color-style-and-highlighting) that you previously had set will be cleared.
    - Any [change history](../editing/#change-history) recorded for the file will be reset, and the file will appear with no change-history margin colors.
- **Save**: Saves the current document to the filesystem using the same filename.
    - If the document does not currently have a file associated with it, this action will be grayed out and the menu entry cannot be used.  Use **File > Save As** instead.
- **Save As**: Saves the current document to the filesystem, prompting for the new filename to use.
    - If the document had previously been saved to a file, this will create as new copy of the file, and Notepad++ will continue working with the document associated with the new file, leaving the old file with the contents that were last saved.
- **Save a Copy As**: Saves the current document to the filesystem, prompting for the new filename to use.
    - The new file will be saved, but Notepad++ will continue to work with the document associated with the original filename.  So this action effectively creates a backup of the file, but allows you to continue working with the previous file, whereas **Save As** uses the original as the backup and allows you to keep working with the new file.
    - Normally during execution of this command, the new file created is not opened into a Notepad++ editing tab. To open the new file as part of the process, hold down the <kbd>Shift</kbd> key while pressing the **Save** button in the **Save As** dialog.
- **Save All**: Saves all documents that are currently open in either of Notepad++'s two Views.
- **Rename**: Prompts for a new name to give to the current document.
    - If the document is associated with a file, Notepad++ will open a standard Windows dialog to save the file under a new name on the filesystem, and the old filename will no longer exist.
    - If the document is a new, unsaved document, it will change the name displayed in the Tab for the current document.  If you later do a **Save As**, it will use that as the default suggested name in the **Save As** dialog.
- **Close**: Closes the active document, prompting to save if it has been modified since it was opened or created.
- **Close All**: Closes all the documents that are open in the current instance of Notepad++, prompting to save if one or more files has been modified since they were opened or created.
    - In the prompt dialog, **Yes** will save the file, **No** will close it without saving (you will _lose_ any changes), **Cancel** will stop Notepad++ from closing all the files.
    - If there are multiple files that you are prompted for, you will also get **Yes to All** to save all changed files, and **No to All** to lose changes from all changed files.
- **Close Multiple Documents >**:
    - **Close All but Active Document**: Closes all open documents, except the document that is actively being edited.
    - **Close All but Pinned Documents**: Closes all open documents, unless their tab has been pinned.
    - **Close All to the Left**: Closes all the open documents that are to the left of the active document on the current View's tab bar.
    - **Close All to the Right**: Closes all the open documents that are to the right of the active document on the current View's tab bar.
    - **Close All Unchanged**: Closes all open documents that have not been edited since they were last opened or created.
- **Move to Recycle Bin**: Closes the active document, and moves the underlying file to the Windows Recycle Bin.  If the document has no underlying file, this action will be grayed out and the menu entry cannot be used.
- **Load Session...**: Loads all the files from a saved [Session file](../session/#sessions).
- **Save Session...**: Saves the current session (list of opened files) to a [Session file](../session/#sessions).
- **Print**: Opens a **Print** dialog to print the file, as described in the [Printing](#printing) section.
- **Print Now**: Prints the active file without showing the **Print** dialog, using the default printer and other default settings of the **Print** dialog.
- **Recent Files >**: The list of recently-closed files that Notepad++ has edited.
    - If [**Settings > Preferences > Recent Files History**] is set to use a sub-menu, the recent files will be in that sub-menu, otherwise they will be in the main **File** menu.
    - Clicking on a file entry will open that file.
    - **Restore Recent Closed File**: Opens the file that was most recently closed, which is at the top of the list of Recent Files.
    - **Open All Recent Files**: Opens all the files from the list.
    - **Empty Recent Files List**: Removes all the files from the Recent Files list.
- **Exit**: Closes the Notepad++ application.
    - If you have [**Settings > Preferences > Backup**]() `☑ Remember current session for next launch` checkmarked, Notepad++ will save the current list of files to the session.  The only files that will be remembered for the next launch of Notepad++ will be those files that are currently open in Notepad++.
    - If you do not have [**Settings > Preferences > Backup**]() `☐ Enable session snapshot and periodic backup` checkmarked, Notepad++ will prompt you whether to save any files that have been changed, following the same rules as **Close All**, described above.  If you do have that setting checkmarked, unsaved documents will also be included in the session file even if they don't have an underlying file.

### File-Type Filters

For the **Save As** and similar dialogs, there is a **Save as Type** pulldown field.  For the **Open** dialog (and similar), there is a pulldown file-type field to the right of the **File name** entry.  Those pulldowns serve to filter the list of files in the dialog based on the file type.  The filter's list of file types will include all of the languages in the [**Language** menu](../programing-languages/) and the extensions for those types, as defined in the [Style Configurator](../preferences/#style-configurator)). Starting in v8.7, the filter will also include the various [User Defined Language](../user-defined-language-system/) file types and extensions as well.

For the **Save As** dialog, the `☐ Append extension checkbox` described in the [Preference Toggles in Other Dialogs](preferences/#preference-toggles-in-other-dialogs) will allow the dialog to automatically add the _first_ extension in the list for the active filter.  If you want a different extension for that type, or if that option is not checkmarked, you can always type the filename with extension to explicitly define the extension you want for the file you are currently saving.  (So normally, doing **Save As** filtered for C++ will automatically add the `.cpp` extension; but if you want it to be `.cxx` or `.h`, you can just type that as part of the **File name** entry rather than letting Notepad++ auto-append the extension.)

### Alternates to File Menu

Many of the actions from the **File** menu have multiple ways to access them, as described in the [User Interface](../user-interface/) and in other appropriate User Manual sections.

For example,
- **File > Open** has many ways of accomplishing the same thing:
    - The default [keyboard shortcut](../preferences/#shortcut-mapper) is <kbd>Ctrl+N</kbd>.
    - The [toolbar](../user-interface/#toolbar) has an icon **New**.
    - The [menu bar](../user-interface/#menu-bar) can have a `+` icon to create a new file.
    - You can double-click in the empty space in the [tab bar](../user-interface/#tabs).
    - You can use the right-click menu of the [system tray icon](../user-interface/#system-tray)
- **File > Close** also has many ways of accomplishing the same thing:
    - The default [keyboard shortcut](../preferences/#shortcut-mapper) is <kbd>Ctrl+W</kbd>.
    - The [toolbar](../user-interface/#toolbar) has an icon **Close**.
    - The [menu bar](../user-interface/#menu-bar) can have an `X` icon to close the active file.
    - The [User Interface > Tabs](../user-interface/#tabs) section explains three more:
        - You can click the `X` of a given tab's title to close it, if [**Settings > Preferences > General > Tab Bar > Show close button**](../preferences/#general) is set.
        - You can double-click on the tab's title to close it, if [**Settings > Preferences > General > Tab Bar > ☐ Double click to close document**](../preferences/#general) is set.
        - You can middle-click on the tab's title to close it.
    - You can use the [right-click menu](../user-interface/#tab-bar-right-click-menu) of the tab's title.

In general, it's redundant to explain all the alternate methods in multiple locations in the Manual, so if you are looking for a way to perform an action from the **File** menu in some other location, you can use your browser's **Find in Page** feature (often <kbd>Ctrl+F</kbd> or similar) to search the [User Interface](../user-interface/) page for the action you are looking for.  And studying that page will allow you to familiarize yourself with the various locations where such features might be found.

## Printing

The **File > Print** action will pull up a Windows-standard print dialog, from which you can choose your printer and send your text to the selected printer.  Normally, it will print the whole document, but you can use the print dialog to choose only certain pages; if you have an active selection in the editor, only the selected text will be printed.

The printing of the text is affected by the [**Settings > Preferences > Print**](../preferences/#print) settings, where you can decide things like whether or not to include line numbers in the printout, margin widths, extra text to print in the header and/or footer of every page, and the **Colour Options** will determine how your [Style Configurator theme's colors](../preferences/#style-configurator) will be propagated to the printed output.  It is up to you as the user to decide which printing settings are best to meet your needs, and will look best on your printed medium of choice.  Please note that with any themes with colored backgrounds, some of those colors will be printed to the background of your printed page unless you choose one of the **Colour Options** that does not print the background color; but with darker themes, which use light text on dark backgrounds, if you _don't_ have it print the background color, then it will be very light text on your white paper.  If you have a printer which allows you to print to PDF, that is a good way to see what the printout will really look like without using the paper and ink (and if you don't have a PDF printer available, your favorite search engine will show you plenty of commercial and freeware PDF printers by searching for something like "windows PDF printer" or "print to PDF").

