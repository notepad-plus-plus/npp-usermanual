---
title: Extend functionality with plugins
linktitle: Plugins
weight: 90
---

## What is a plugin
Notepad++ is very extensible using so called plugins. Plugins are small or big additions to Notepad++ to enhance its functionality. Notepad++ comes bundled with a few plugins (when using the installer, you can choose which ones to add), but you can always add your own or remove some. The plugins are located in the Plugins directory in the main Notepad++ installation directory. They are DLL files and simply removing or adding them is enough.


## How to install a plugin

### Install using Plugins Admin
The Plugins Admin allows you to easily install plugins that are in the Plugins List.  To do so, place a check mark next to the Plugin(s) you wish to install, then select Install.

### Install plugin manually
If the plugin you want to install is not listed in the Plugins Admin, you may still install it manually.  The plugin (in the DLL form) should be placed in the \plugins subfolder of the Notepad++ Install Folder, under the subfolder with the same name of plugin binary name without file extension.
For example, if the plugin you want to install named `myAwesomePlugin.dll`, you should install it with the following path:
`%PROGRAMFILES(x86)%\Notepad++\plugins\myAwesomePlugin\myAwesomePlugin.dll`

Once you installed the plugin, you can use (and you may configure) it via the menu "Plugins".

## How to develop a plugin

### Getting started - Make your plugin in less 10 minutes (C++)

Here are the instructions to make your first Notepad++ plugin in less 10 minutes, by following 6 steps:

1. Download and unzip the latest release of [Notepad++ Plugin Template](https://github.com/npp-plugins/plugintemplate/releases).
2. Open `NppPluginTemplate.vcproj` in your Visual Studio.
3. Define your plugin name in `PluginDefinition.h`
4. Define your plugin commands number in `PluginDefinition.h`
5. Customize plugin commands names and associated function name (and the other stuff, optional) in `PluginDefinition.cpp`.
6. Define the associated functions.
You are guided by the following comments in both [PluginDefinition.h](https://github.com/npp-plugins/plugintemplate/blob/master/src/PluginDefinition.h) and [PluginDefinition.cpp](https://github.com/npp-plugins/plugintemplate/blob/master/src/PluginDefinition.cpp) files:

```
//-- STEP 1. DEFINE YOUR PLUGIN NAME --//
//-- STEP 2. DEFINE YOUR PLUGIN COMMAND NUMBER --//
//-- STEP 3. CUSTOMIZE YOUR PLUGIN COMMANDS --//
//-- STEP 4. DEFINE YOUR ASSOCIATED FUNCTIONS --//
```
A good sample illustrates better the whole picture than a detailed documentation. You can check [Notepad++ Plugin Demo](https://github.com/npp-plugins/plugindemo/releases) to learn how to make some commands more complex. 

However, the knowledge of Notepad++ plugin system is required, if you want to accomplish some sophisticated plugin commands.

You can use [Plugin development forum](https://notepad-plus-plus.org/community/category/5/plugin-development) for any technical questions/answers and the announcement your new plugin.


### In other languages

* [Delphi](https://sourceforge.net/projects/npp-plugins/files/DelphiPluginTemplate/DelphiPluginTemplate%202.0%20UNICODE/DelphiPluginTemplate2.zip/download)
* [C#](https://github.com/kbilsted/NotepadPlusPlusPluginPack.Net)
* [Ada](https://notepad-plus-plus.org/assets/files/NppHelloAdaDemo.zip)


## Plugins Admin
Built-in **Plugins Admin** shows the list of available plugins, allows users to install new plugins and to update/remove installed plugins.
It needs **Plugin List** (see next section) to work.

## Plugin List
A list in JSON format wrapped in a dll contains the most poplular Notepad++ plugins. This list which is maintained by the team, is also an open source project hosted in the GitHub: https://github.com/notepad-plus-plus/nppPluginList/ 
Any plugin is welcome to join in the list.

### Test your plugins' installation/update locally
For testing your plugin for listing, installation, removal and update under Plugin Admin, you need Notepad++ binary in debug mode [32-bit](https://notepad-plus-plus.org/pluginListTestTools/notepad++.debug.x86.zip) or [64-bit](https://notepad-plus-plus.org/pluginListTestTools/notepad++.debug.x64.zip), the latest version of wingup [32-bit](https://notepad-plus-plus.org/pluginListTestTools/wingup.release.x32.zip) or [64-bit](https://notepad-plus-plus.org/pluginListTestTools/wingup.release.x64.zip) and nppPluginList.json (you should rename it from pl.x64.json or pl.x86.json, according your plugin's architecture). Replace notepad++.exe and GUP.exe of your Notepad++ installation by downloaded ones, copy `pl.x64.json` or `pl.x86.json` to `%PROGRAMDATA%\Notepad++\plugins\Config\nppPluginList.json` (or `<NPP_INST_DIR>\plugins\Config\nppPluginList.json` - see New Plugins Home), then you're all set - the menu item "Plugin Admin" will be under menu "Plugin" of your debug mode notepad++.exe. Launch this command will launch the Plugin Admin dialog and the rest should be intuitive.

### Rules for adding your plugins into list

1. Architecture: your 32-bits plugin should be added to [pl.x86.json](https://github.com/notepad-plus-plus/nppPluginList/blob/master/src/pl.x86.json), 64-bits plugin should be added to [pl.x64.json](https://github.com/notepad-plus-plus/nppPluginList/blob/master/src/pl.x64.json).
2. Unicity: the value of **folder-name** of your plugin should be unique in the list. it means if there's already another same name plugin in the list, you have to rename your plugin's folder-name (and your plugin). Keep in mind that your plugin binary name (w/o the extension .dll) should be always the same as the folder-name, otherwise your plugins won't be loaded.
3. Security: the value of **id** is plugin package's (zip file) finger print in SHA-256. This id is checked with the downloaded dll to avoid [MITM](https://en.wikipedia.org/wiki/Man-in-the-middle_attack). You can use Notepad++ to get your plugin's SHA-256 hash (Menu: `Tools->SHA-256>Generate from files...`) or some online sha256 generators.
4. Update info: the value of **version** is exact the version of your plugin binary version which you want to be deployed. This version will compare with installed plugin's version to decide if update should be applied. Please check [Microsoft's document about binary version](https://docs.microsoft.com/en-us/windows/desktop/menurc/versioninfo-resource) for setting the version correctly onto your DLL.
5. Download location: the value of **repository** is the URL where Plugin Admin can download the plugin to install/update it.
6. Packaging: Only zip package is supported. Your plugin (DLL) should have the same name as the **folder-name** and the plugin DLL file should be placed at the root level of the ZIP file. Otherwise Plugin Admin won't install it. Any additionals files (dll or data) can be placed at the root level or in an arbitrary subfolder.

### Do your PR to join plugin list
Once your test has been done, and everything is ok, you can fork and do your PR on: https://github.com/notepad-plus-plus/nppPluginList/. Only the json part you should modify. The json file will be built into the a binary (nppPluginList.dll), which will be signed (for thes sake of security) and be included in the official distribution. 

### Questions & support
Ask your questions here: https://notepad-plus-plus.org/community/topic/16789/support-for-plugins-admin-npppluginlist-round-2

