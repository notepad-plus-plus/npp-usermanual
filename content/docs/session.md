---
title: Sessions, Workspaces, and Projects
linktitle: sessions
weight: 50
---

# Sessions, Workspaces, and Projects

There are three built-in "multiple file management" systems available natively in Notepad++.

* [Sessions](#sessions) = a set of files that can be opened with one action.
* [Folder as Workspace](#folder-as-workspace) = a tree-based interface to easily access the files in a given Windows directory.
* [Project Panels](#project-panels) = a tree-based interface to access related files that aren't necessarily grouped in the same Windows directory structure.

There are also various [plugins](../plugins) available that might help manage sessions or workspaces, or serve similar purposes but with a different feature set compared to these built-in features.

## Sessions

Sessions are a set of files to be opened in Notepad++.  Using sessions, you can open a set of files with one action.  They do not have to be in the same directory or even on the same drive.

The session file stores the paths of the open files, the active file (and which view, see the section about Multi-View), the current selection and position in the file, the current bookmarks (see Bookmarks) and the current language (see the section about Languages).  When you load the session, all of that information is loaded back into Notepad++.

* **File > Load Session...** can be used to load an existing session.
* **File > Save Session...** can be used to save the currently-open files as a session.

Session files are XML, and are identical in format to the [`session.xml` config file](../config-files/#other-configuration-files).
The [MISC preferences](../preferences/#misc) include an option to set a file extension that will automatically be opened equivalently to **Load Session**, even if you use **File > Open** to access that session; that extension will also be the default when you **Save Session**[¹](#FN1 "Footnote ¹").

You can also load a session file using the [`-openSession` command line argument](../command-prompt).

*Note*: As of Notepad++ v8.2, the loaded session is saved automatically on exit of Notepad++, if the [Multi-instance settings](../preferences/#multi-instance-and-date) is **not** set to "Default (Mono-instance)".

## Folder as Workspace

This feature allows you to use a tree-based interface to easily access the files in a given directory.  When you drag a folder from Windows Explorer onto Notepad++, this feature will be activated (unless overridden by the ["... folder dropping" option](../preferences/#default-directory)).

You can also load a Folder as Workspace using the [`-openFoldersAsWorkspace` command line argument](../command-prompt).

If you right-click in the Folder as Workspace panel, you can add more directories to the current Workspace.

Double-clicking on a file from the tree-view will open it as a new tab in the Notepad++ editor (or will activate that tab if it's already open).  Closing the tab for a file from the Project will not remove it from the Folder as Workspace panel, so it's easy to re-open that file.

## Project Panels

The Project Panels are similar to the [Folder as Workspace](#folder-as-workspace) panel, but allow you to organize the tree view to your liking, rather than being forced to follow the Windows filesystem hiearchy.

Double-clicking on a file from the tree-view will open it as a new tab in the Notepad++ editor (or will activate that tab if it's already open).  Closing the tab for a file from the Project will not remove it from the Project panel, so it's easy to re-open that file.

There are three Project Panels available from the **View > Project** sub-menu.  The three Project Panels can be individually docked or floated.

In each panel, you can open one Workspace file.  Using the **Workspace** button on the Project Panel, or right clicking on the Workspace's name in the tree view, you can perform a variety of actions, enumerated below.  The [MISC preferences](../preferences/#misc) include an option to set a file extension that will automatically be opened equivalently to the **Open Workspace** command, even if you use **File > Open** to access that Workspace file; that extension will also be the default when you **Save Workspace**[¹](#FN1 "Footnote ¹").

Each Workspace can house one or more Projects.  Clicking the **Edit** button on the Project Panel, or right clicking on the Project name, will give you administrative options for the selected Project, enumerated below.  In each Project, you can select individual files or the contents of whole Windows Directories to be added to the Project, and you can reorder the files.  If you add a Folder to the Project, you are _not_ creating a Windows directory anywhere: you are creating a container inside the Notepad++ Project item; the files listed in a folder have not moved.  To reiterate: Project Folders are independent of the filesystem, and are just hierarchical containers for this feature of Notepad++.

You can move a file from one place in the Project panel into a different Folder or Project by dragging the file within the Project Panel and dropping it on the name of the Project or Folder you want the file to move into.  Other than that, there aren't other drag-and-drop features in the Project Panel.

Project files always contain file paths relative to the location of the project file itself. Thus, if a project file is stored in a filesystem folder which is part of a project, it is very easy to move that folder to another location on the hard disk. If the project file is loaded from its new location it will still work.

### Project Panel Specifics

For any entry in the Project Panel tree view, right clicking will give you the available actions on that specific entry.

* On a Workspace:
    * New Workspace = close the existing Workspace (if one is open for this Project Panel) and create an empty Workspace for this Project Panel.
    * Open Workspace = close the existing Workspace (if one is open for this Project Panel) and open the selected Workspace file.
    * Reload Workspace = re-read the XML file for the active Workspace (it may have been edited externally).
    * Save = save any changes in the Projects, files, and Folders of the active Workspace configuration.
    * Save As = save the active Workspace in a new Windows filesystem location.
    * Save As Copy = save the active Workspace in a new Windows filesystem location, keeping the old Workspace file as well.
    * Add New Project = add a new Project container to the active Workspace.
* On a Project entry:
    * Move Up / Move Down = reorder the selected Project relative to other Projects in the Workspace.
    * Rename = change the name of the Project.
    * Add Folder = create a new container to go in this Project.
    * Add Files = use a Windows **Open** dialog to select one or more files to add to the Project's tree.
    * Add Files from Directory = add all the files from that Windows directory into the Project.
        * Please note: this does _not_ create a new Folder entry in your Project.
* On a Folder entry:
    * Has all the same actions as on the Project entry, but everything is relative to this Folder instead of relative to the Project.
* On a File entry:
    * Move Up / Move Down = reorder the selected file relative to other files or Folders in the containing Project or Folder.
    * Rename = changes the name of the file in the list.
        * This action does _not_ change the underlying file.
        * If the new name does not exist as a file, it will show a little error symbol on the file icon in the tree.
        * If the new name does exist as a file, the old file will still exist but will no longer be a part of this Project.
    * Remove = removes the file from the Project.
        * This action does _not_ change the underlying file.
    * Modify File Path = similar to rename, changes the file in the list, but also allows you to change what Windows directory is being referenced.
        * This action does _not_ change the underlying file.
        * If the new name does not exist as a file, it will show a little error symbol on the file icon in the tree.
        * If the new name does exist as a file, the old file will still exist but will no longer be a part of this Project.

## Differences Between Projects and Folder as Workspace

In contrast to the Folder as Workspace feature, Projects are not bound to the content of a certain folder on the hard disk. Instead, it is possible to put together files and folders from various locations on the hard disk into one Project. It is even possible to create Folders in a project which actually don’t exist on the hard disk and add files from various locations to them.  With projects, it is possible to combine files and folders into a totally virtual structure. This can speed up accessing files which are logically related to each other but are widely spread over the hard disk.

<hr>

**Footnotes**

<a name="FN1">¹</a>: if you set the Session or Workspace extensions, you will find it difficult to edit the XML for the given Session or Workspace file inside Notepad++.  To do that, you can temporarily clear that preference setting, edit the file, then set the extension preference again.
