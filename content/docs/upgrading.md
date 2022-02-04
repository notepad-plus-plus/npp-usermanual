---
title: Upgrading
linktitle: Upgrading
weight: 150
---

Notepad++ is an actively maintained piece of software, and new versions come fast. There are basically four ways to keep abreast of changes:

## Auto-Trigger
If you used installation package when you originally installed, the Auto Update feature is enabled by default. Every 15 days auto-updater (WinGUp) will be launched for checking, and you will be notified if a new version is available. You are presented with the option of installing that newer version.

## Upgrade On-Demand
Using the **? > Update Notepad++** menu command. This will check whether there is a new version and whether the safety delay is over. If so, you are presented with the opportunity to download and install the newer version.

## Upgrade Manually
Going to the main website and downloading the latest installer and running it yourself.  You can watch the [Announcements](https://community.notepad-plus-plus.org/category/1/announcements) category in the [Notepad++ Community Forum](https://community.notepad-plus-plus.org/) to see when new release-candidates or final versions are released.

## Download Zip Package
Going to the main website and downloading the latest zipped archive.  You can then use it as a separate portable version, or compare its files to another installed or portable version, so you can decide how and when to upgrade.

## No New Version Found: Safety Delay
There are two reasons that would cause there to be no new version found during an auto-triggered upgrade check or an on-demand upgrade check: 

First, there might not be a new version.  

Second, if there is a new version available, it may not have been triggered for auto-update yet. In order to avoid to spreading a new version which contains regressions or critical bugs, we wait for users' feedback before triggering the auto-update, often one to two weeks.  If a critical bug or regression is found, the auto-update will _not_ be triggered for that release. On the other hand, after a reasonable delay, if we are confident there are no critical issues, the auto-update will be triggered.  This safety delay prevents bad bugs or regressions from being widely spread throughout the Notepad++ user-base, limiting the exposure to those users who are watching for release announcements and are willing to manually upgrade Notepad++.

The safety delay will never prevent you from downloading the installer or portable zip package yourself.

## WinGUp Project
The [WinGUp](http://wingup.org/) project was started for the need of Notepad++ for upgrading Notepad++ automatically.  It has since become a more generic solution for updating purposes. [This project has been forked](https://github.com/notepad-plus-plus/wingup) for more Notepad++ specific need so Plugin Admin can share its basic functionalities.
