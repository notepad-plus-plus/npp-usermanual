---
title: Upgrading
linktitle: Upgrading
weight: 180
---

Notepad++ is an actively maintained piece of software, and new versions come fast. There are basically four ways to keep abreast of changes:

## Auto-Trigger
If you used installation package when you originally installed, the Auto Update feature is active by default. Every 15 days auto-updater (WinGUp) will be launched for checking, and you will be notified if a new version is available. You are presented with the option of installing that newer version.

## Upgrade On-Demand
Using the **? > Update Notepad++** menu command. This will check whether there is a new version and whether the safety delay is over. If so, you are presented with the opportunity to download and install the newer version.

### Updater Dialog

The Updater dialog is launched for either Auto-Trigger or for Upgrade On-Demand.

If there is no auto-triggered update available, the dialog will just inform you of this (but see [No New Version Found](#no-new-version-found-safety-delay)).

If there is a new version, the Updater dialog will allow you to choose:
- **Yes**: Run the update.
    - It will download the updater, ask if it's okay to close Notepad++, and the updater will run, asking you to confirm your settings, and update Notepad++.
- **Yes (Silent)**: Run a truly-silent upgrade of Notepad++.  (New to v8.6.9.)
    - It will close the running Notepad++ (and all instances in multi-instance mode), do the update (without requiring clicking all the **Next** buttons to keep the same installed-options as you already have), and automatically run an instance of the updated Notepad++ -- so a true "upgrade and continue" experience.
- **No**: Don't run the installer at this time.
- **Never**: Don't run the installer at this time, and don't ask again in the future.
    - See also: [**Settings > Preferences > MISC** > ☐ Enable Notepad++ auto-updater](../preferences/#misc)


## Upgrade Manually
Going to the main website and downloading the latest installer and running it yourself.  You can watch the [Announcements](https://community.notepad-plus-plus.org/category/1/announcements) category in the [Notepad++ Community Forum](https://community.notepad-plus-plus.org/) to see when new release-candidates or final versions are released.

## No New Version Found: Safety Delay
There are two reasons that would cause there to be no new version found during an auto-triggered upgrade check or an on-demand upgrade check:

First, there might not be a new version.

Second, if there is a new version available, it may not have been triggered for auto-update yet. In order to avoid to spreading a new version which contains regressions or critical bugs, we wait for users' feedback before triggering the auto-update, often one to two weeks.  If a critical bug or regression is found, the auto-update will _not_ be triggered for that release. On the other hand, after a reasonable delay, if we are confident there are no critical issues, the auto-update will be triggered.  This safety delay prevents bad bugs or regressions from being widely spread throughout the Notepad++ user-base, limiting the exposure to those users who are watching for release announcements and are willing to manually upgrade Notepad++.

The safety delay will never prevent you from downloading the installer or portable zip package yourself.

## WinGUp Project
The [WinGUp](http://wingup.org/) project was started for the need of Notepad++ for upgrading Notepad++ automatically.  It has since become a more generic solution for updating purposes. [This project has been forked](https://github.com/notepad-plus-plus/wingup) for more Notepad++ specific need so Plugin Admin can share its basic functionalities.

## Download Zip Package
Going to the main website and downloading the latest zipped archive.  You can then use it as a separate portable version (which isn't technically upgrading, but will allow to try out a new version before upgrading), or compare its files to another installed or portable version, so you can decide how and when to upgrade.

### Upgrading a Portable Edition

If you have a portable edition of Notepad++, unzipping the contents from the new zipfile into your old directory will overwrite some of your configuration files, including `config.xml`, which will mean you will lose your customized settings.  A recommended workflow for upgrading a portable edition (with dummy directories; you can choose whatever directories are convenient):

1. Starting condition:
    - Your original installation is in `c:\PortableNpp\`
    - You have the ComparePlus plugin, or otherwise understand how to compare contents of similar files
    - You have read and understood the [Online UserManual section on Editing Configuration Files](https://npp-user-manual.org/docs/config-files/#editing-configuration-files)
    - Make sure you have recently exited Notepad++ and restarted it, without having made any configuration changes in the GUI since restarting it, as per "Editing Configuration Files".
2. Unzip the new portable zipfile into `c:\PortableNpp.new\`
3. Compare each of the following configuration files.  Look for any settings that are in the New but not in the Old, and copy them over.
    - **Optional**: For some, the updates in the configuration files usually just give access to new features which you might not care about (like a new right-click menu action); in that case, it is up to you to decide whether you want to bring over the new features or not.
    - **Overwrite**: For these configuration files, users rarely customize them.  Unless you know that you have, it's generally safe to just overwrite it with the new copy.
    - **Model**: For these configuration files, you will be comparing your raw file with the new `.model.` version.  These are files that are often customized, so when you are comparing, you will want to be careful to bring over the new features (things that are in the new `.model.`) without getting rid of your customizations.

    | Old (`c:\PortableNpp\...`) | New (`c:\PortableNpp.new\...`) | Notes |
    |-----|-----|-------|
    | `...\config.xml` | `...\config.xml` | |
    | `...\contextMenu.xml` | `...\contextMenu.xml` | Optional |
    | `...\shortcuts.xml` | `...\shortcuts.xml` | Optional |
    | `...\toolbarIcons.xml` | `...\toolbarIcons.xml` | Optional |
    | `...\langs.xml` | `...\langs.model.xml` | Model |
    | `...\stylers.xml` | `...\stylers.model.xml` | Model |
    | `...\themes\___.xml` | `...\themes\____.xml` | Overwrite ¹ |
    | `...\autoCompletion\___.xml` | `...\autoCompletion\____.xml` | Overwrite |
    | `...\localization\___.xml` | `...\localization\____.xml` | Overwrite |
    | `...\functionList\___.xml` | `...\functionList\____.xml` | Overwrite |
    | `...\userDefineLangs\___.xml` | `...\userDefineLangs\____.xml` | Overwrite |

    - ¹: If you are using a specific theme, it's more likely that you will have customized that theme's file.  Please do a full comparison on that theme file, but you can probably get away with just overwriting the old theme files.

4. After updating the config files, then you can exit Notepad++, copy the `notepad++.exe` and `plugins\config\nppPluginList.dll` from the old to the new, and restart Notepad++ to start using your upgraded portable edition.

_Note: a similar procedure can be used when you think your installed copy of Notepad++ has themes or syntax highlighting configuration that is missing compared to a fresh install or portable, except you would use `%AppData%\Notepad++\____.xml` and/or `C:\Program Files\Notepad++\____.xml` as the **Old** location, instead of a portable location._
