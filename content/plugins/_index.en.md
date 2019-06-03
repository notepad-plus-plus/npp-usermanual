---
title: Plugins
weight: 90
---

## What is a plugin
Notepad++ is very extensible using so called plugins. Plugins are small or big additions to Notepad++ to enhance its functionality. Notepad++ comes bundled with a few plugins (when using the installer, you can choose which ones to add), but you can always add your own or remove some. The plugins are located in the Plugins directory in the main Notepad++ installation directory. They are DLL files and simply removing or adding them is enough.


## How to install a plugin
The plugin (in the DLL form) should be placed in the \plugins subfolder of the Notepad++ Install Folder, under the subfolder with the same name of plugin binary name without file extension.
For example, if the plugin you want to install named `myAwesomePlugin.dll`, you should install it with the following path:
`%PROGRAMFILES(x86)%\Notepad++\plugins\myAwesomePlugin\myAwesomePlugin.dll`

Once you installed the plugin, you can use (and you may configure) it via the menu "Plugins".

## How to develop a plugin

### Getting started - Make your plugin in less 10 minutes (C++)

Here are the instructions to make your first Notepad++ plugin in less 10 minutes, by following 6 steps:

1. Download and unzip [Notepad++ Plugin Template](https://github.com/npp-plugins/plugintemplate/archive/v3.zip).
2. Open NppPluginTemplate.vcproj in your Visual Studio.
3. Define your plugin name in PluginDefinition.h
4. Define your plugin commands number in PluginDefinition.h
5. Customize plugin commands names and associated function name (and the other stuff, optional) in PluginDefinition.cpp.
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
* [C#](http://sourceforge.net/projects/sourcecookifier/files/other%20plugins/NppPlugin.NET.v0.5.zip/download)
* [Ada](https://notepad-plus-plus.org/assets/files/NppHelloAdaDemo.zip)



## Plugins Admin
Built-in **Plugins Admin** shows the list of available plugins, allows users to install new plugins and to update/remove installed plugins.
A list in JSON format wrapped in a dll contains the most poplular Notepad++ plugins. This list which is maintained by the team, is also an open source project hosted in the GitHub: https://github.com/notepad-plus-plus/nppPluginList/ 
Any plugin is welcome to join in the list.

