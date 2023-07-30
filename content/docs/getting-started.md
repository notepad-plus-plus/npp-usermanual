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

The installer will likely require Administrative privileges in order to install Notepad++ (and later, to update Notepad++ or install or update plugins, or anything else that requires writing to the installation directory).  If you do not have Administrative privileges, you either need to tell the installer to use a location where you _do_ have write permission (though that may still ask for Administrator privileges), or you may choose not use the installer and instead run a portable edition from a directory where you have write permission.

By default, the installer will use `%AppData%\Notepad++` to [store your settings](../config-files/#configuration-files-location); but when you use the installer to install to a directory other than "Program Files", you can choose the installation option "Don't use %APPDATA%" to instead use a "[local configuration](../config-files/#configuration-files-location)".

The installer should also install the [Shell Extension](../shell-extension/) to add **Edit with Notepad++** to the Windows Right-Click context menu.  (Your specific version or translation may use a different phrasing for that entry.)

If you are doing managed installation or otherwise want to control the installer from the command line, the installer has a few [command line options](../command-prompt/#installer-options).

The installed version of Notepad++ can be removed using the standard Windows OS's "Add/Remove Programs" interface for removing installed programs (or similar, depending on your OS version).

## Install Notepad++ from 7z or zip

These instructions will allow you to run a portable or mini-portable (also called "minimalist"), without requiring administrative privileges.

1. Create a new folder somewhere that you have write-permission
2. Unzip the content into the new folder
3. Run Notepad++ from the new folder

For the all portable editions, everything (the application, settings, and plugins) is stored in one folder hierarchy.  And by default, the portable editions do not mess with operating system settings (so no file associations or **Edit with Notepad++** context-menu entries) -- if you want such with a portable edition, you will have to set it up manually.

The main portable 7z or zip editions contain all the themes, user defined languages, auto-completions, localizations, and default plugins and Plugins Admin tool that come with the installed version of Notepad++.

The minimalist / mini-portable edition only comes with the default light-mode and dark-mode theme, the default English localization, and no plugins or Plugins Admin.  However, you can separately download any of the non-included config files that you want from the main Notepad++ source repository, and you can still [install plugins manually](../plugins/#install-plugin-manually).

The portable editions of Notepad++ can be removed by deleting the directory they came in.  If you manually set up and file associations or context-menu entries in the OS, it is your responsibility to remove them yourself.

## "Program Files" Restrictions

Windows is particular about what goes into "Program Files", and restricts permissions there, usually requiring Administrator Privilege to install or edit there.

When Notepad++ is placed in "Program Files" (whether through the installer or through unzipping a portable edition there), it intentionally does _not_ honor the [doLocalConf.xml](../config-files/#other-configuration-files) that comes from the "Do not Use %APPDATA%" setting or unzipping a portable edition there or manually creating the file, and will instead use your `%AppData%\Notepad++` directory for [storing settings](../config-files/#configuration-files-location) despite that file being there.
