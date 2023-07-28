---
title: Getting started
linktitle: Getting started
weight: 1
---

## What is Notepad++

Notepad++ is a text editor and source code editor for use under Microsoft Windows. It supports around 80 programming languages with syntax highlighting and code folding. It allows working with multiple open files in a single window, thanks to its tabbed editing interface.
Notepad++ is available under [GPL](http://www.gnu.org/licenses/gpl-3.0.html) and distributed as [free software](https://www.fsf.org/).

You may visit the Notepad++ website at https://notepad-plus-plus.org/

## Download Notepad++

Download the latest version of Notepad++ from https://notepad-plus-plus.org/downloads/

Determine whether your system requires the 64-bit or ARM 64-bit or 32-bit build of Notepad++, according to your machine and operating system, then choose the package you want to download for that architecture. Most users use the installer as it's the easiest route, however Notepad++ is also available in "portable" or "mini-portable" 7z and zip formats.


## Install Notepad++ using the installer

1. Download the installer
2. Run the executable binary and follow the installation flow

If you are doing managed installation or otherwise want to control the installer from the command line, the installer has a few [command line options](../command-prompt/#installer-options).

The installer will likely require Administrative privileges in order to install Notepad++ in Windows's standard "Program Files" location.  If you do not have Administrative privileges, you either need to find someone who does, or tell the installer to use a location where you _do_ have write permission, or run the portable edition from a directory where you have write permission.

When you use the installer to install to a directory other than "Program Files", you can choose an option in the installer to _not_ use the `%AppData%\Notepad++` folder for your configuration, and instead use the "[local configuration](../config-files/#configuration-files-location)".

The installer should also install the [Shell Extension](../shell-extension/) to add **Open with Notepad++** to the Windows Right-Click context menu.

## Install Notepad++ from 7z or zip

These instructions will allow you to run a portable or mini-portable (also called "minimalist"), without requiring administrative privileges.

1. Create a new folder somewhere that you have write-permission
2. Unzip the content into the new folder
3. Run Notepad++ from the new folder

In a portable edition, the [configuration files](../config-files/#configuration-files-location) will be stored in the same directory where you put `notepad++.exe`.

The portable editions do not automatically install Right-Click context menu, so you will not see **Open With Notepad++** on files unless you use Windows' **Open With** feature to permanently associate that type of file with your portable Notepad++, or use [Settings > Preferences > File Association](../preferences/#file-association), or use one of the [alternative right-click context menu](../shell-extension/#alternatives) registry edits.  (But if what you really want is to have Notepad++ "installed", but just not use the "Program Files" hierarchy, you can tell the installer to use a different directory for the installation.)

The mini-portable edition only includes the default theme and default Dark Mode theme, and only the English localization; it also does not include the autoCompletion files, functionList files, Plugins Admin, or the Notepad++ updater.  The full portable includes all the themes that ship with the Notepad++ installer, and has all localization files included.

## "Program Files" Restrictions

Windows is particular about what goes into "Program Files", and restricts permissions there, usually requiring Administrator Privilege to install or edit there.

Trying to set the "Don't use %APPDATA%" during installation while still installing in "Program Files", or putting the portable into "Program Files", or manually adding `doLocalConf.xml` to the installation in "Program Files", are not intended use cases.  Doing so may still result in `%AppData%` being used, due to file permissions and special OS handling of the "Program Files" hierarchy, and may expose other odd behaviors that wouldn't be seen if you weren't trying to "mix modes".  If you really don't want to use `%AppData%` for your configuration, do not use "Program Files" as your installation-location, or unzip the portable into a different directory, or always run using the `-settingsDir` [Command Line Argument](../command-prompt/) or Cloud settings to give an [alternative config-file location](../config-files/#configuration-files-location).
