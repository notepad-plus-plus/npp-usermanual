---
title: Plugins
weight: 90
---

Notepad++ is very extensible using so called plugins. Plugins are small or big additions to Notepad++ to enhance its functionality. Notepad++ comes bundled with a few plugins (when using the installer, you can choose which ones to add), but you can always add your own or remove some. The plugins are located in the Plugins directory in the main Notepad++ installation directory. They are DLL files and simply removing or adding them is enough.

When Notepad++ starts, it looks into its Plugins configuration folder and loads whatever dll it finds. Later, you can add plugins using the Settings -> Import -> Import plugins menu. Be careful to make sure your version of Notepad++ is up-to-date enough for new plugins and that the plugin is compatible with Notepad++ (some very old plugins will not work with newer versions of Notepad++, it is up to the developer of the plugin to add support or not).

Currently, Notepad++ can be found in an (older) ANSI version and the newer Unicode version. The plugin has to match this version, otherwise it will not work (Notepad++ will warn you about this). Plugins can be found anywhere on the internet, but a large can be found in the Notepad++ Plugins project on SourceForge.net: http://sourceforge.net/projects/npp-plugins/. There is even a plugin, called Plugin Manager, which works out the installation details and version management for you.

If a plugin misbehaves, Notepad++ will go out of its way to prevent the failure from propagating so as to avoid any loss of data. In such a case, you will be presented with information about the plugin reporting a problem. Making this information available on the Plugin Development forum will help removing the cause of the problem as soon as possible.