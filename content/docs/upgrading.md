---
title: Upgrading
linktitle: Upgrading
weight: 180
---

Notepad++ is an actively maintained piece of software, and new versions come fast. There are basically four ways to keep abreast of changes:

## Auto-Trigger
If you used installation package when you originally installed, the Auto Update feature is active by default. Every 15 days auto-updater (WinGUp) will be launched for checking, and you will be notified if a new version is available. You are presented with the option of installing that newer version.

Depending on the [**Settings > Preferences > MISC** > Auto-updater](../preferences/#misc) dropdown choice, auto-triggered update will either be disabled, or will prompt you when you first launch Notepad++, or will prompt you when you exit out of Notepad++.

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



## Upgrade Manually
Going to the main website and downloading the latest installer and running it yourself.  You can watch the [Announcements](https://community.notepad-plus-plus.org/category/1/announcements) category in the [Notepad++ Community Forum](https://community.notepad-plus-plus.org/) to see when new release-candidates or final versions are released.

<a name="new-version-available-but-auto-updater-find-nothing" reasonLink="https://github.com/notepad-plus-plus/wingup/blob/21e375caf17360fb86f757612052d5a785261d96/src/winmain.cpp#L780" reasonDesc="wingup links to this anchor, so it needs to always exist, even though the safety-delay header has been rephrased"></a>

## No New Version Found: Safety Delay

There are two reasons that would cause there to be no new version found during an auto-triggered upgrade check or an on-demand upgrade check:

First, there might not be a new version.

Second, if there is a new version available, it may not have been triggered for auto-update yet. In order to avoid to spreading a new version which contains regressions or critical bugs, we wait for users' feedback before triggering the auto-update, often one to two weeks.  If a critical bug or regression is found, the auto-update will _not_ be triggered for that release. On the other hand, after a reasonable delay, if we are confident there are no critical issues, the auto-update will be triggered.  This safety delay prevents bad bugs or regressions from being widely spread throughout the Notepad++ user-base, limiting the exposure to those users who are watching for release announcements and are willing to manually upgrade Notepad++.

The safety delay will never prevent you from downloading the installer or portable zip package yourself by [downloading and upgrading manually](#upgrade-manually).

## WinGUp Project
The [WinGUp](http://wingup.org/) project was started for the need of Notepad++ for upgrading Notepad++ automatically.  It has since become a more generic solution for updating purposes. [This project has been forked](https://github.com/notepad-plus-plus/wingup) for more Notepad++ specific need so Plugin Admin can share its basic functionalities.

## Download Zip Package
Going to the main website and downloading the latest zipped archive.  You can then use it as a separate portable version (which isn't technically upgrading, but will allow to try out a new version before upgrading), or compare its files to another installed or portable version, so you can decide how and when to upgrade.

### Upgrading a Portable Edition

If you have a portable edition of Notepad++, unzipping the contents from the new zipfile into your old directory will overwrite some of your configuration files, including `config.xml`, which will mean you will lose your customized settings.  A recommended workflow for upgrading a portable edition (with dummy directories; you can choose whatever directories are convenient):

1. Starting condition:
    - Your original installation is in `c:\PortableNpp\`
        - For these instructions, this is assumed to be where you want the upgraded copy of Notepad++ to end up.
        - These instructions will refer to this as "the Destination".
    - You have the ComparePlus plugin, or otherwise understand how to compare contents of similar files.
    - You have read and understood the [Online UserManual section on Editing Configuration Files](https://npp-user-manual.org/docs/config-files/#editing-configuration-files).
    - Make sure you have recently exited Notepad++ and restarted it, without having made any configuration changes in the GUI since restarting it, as per "Editing Configuration Files".
    - You have already backed up `c:\PortableNpp\` so that you can easily undo any accidental changes.
2. Unzip the new portable zipfile into `c:\PortableNpp.temp\`
    - This is just being used to temporarily store the new version of Notepad++.
    - These instructions will refer to this as the "Temporary" version.
3. Compare each of the following configuration files.  Look for any settings that are in the "Temporary" but not in the "Destination", and copy those settings over inside each file.
    - If you find a config file that exists in the "Temporary" but not in the "Destination", and it's not listed below, it could be a new configuration file that these instructions haven't been updated to include that, so you should copy that file over.
    - **Key**:
        - **Compare**: `config.xml` should always be compared, to make sure old choices are kept and new options are included.
        - **Keep**: The `session.xml` file and `backup\` folder's files should always be kept in your "Destination" directory.  Do not overwrite them or delete them.  (The "Temporary" directory from the Portable unzip will not include that file or directory, but they are included in this list so you don't accidentally delete or overwrite them.)
        - **Optional**: For some config files, the updates usually just give access to new features which you might not care about (like a new right-click menu action); in that case, it is up to you to decide whether you want to bring over the new features or not.
        - **Overwrite**: For these configuration files, users rarely customize them.  Unless you know that you have, it's generally safe to just overwrite it with the new copy.  If you know you have customized them (for example, if you've customized your chosen Theme in the Style Configurator¹), you will need to compare them and merge.
        - **Model**: For these configuration files, you will be comparing your raw "Destination" file with the new `.model.` version in the "Temporary" location.  These are files that are often customized, so when you are comparing, you will want to be careful to bring over the new features (things that are in the new `.model.`) without getting rid of your customizations.  The `.model.` files should also be copied over into the "Destination" directory.
        - **Zero-byte file**: These configuration files are 0 bytes.  If your "Destination" does not have the file, it can be copied from the "Temporary" to the "Destination".

    | Destination (`c:\PortableNpp\...`) | Temporary (`c:\PortableNpp.temp\...`) | Notes |
    |-----|-----|-------|
    | `...\config.xml` | `...\config.xml` | Compare |
    | `...\session.xml` | _(does not exist)_ | Keep |
    | `...\backup\*.*` | _(does not exist)_ | Keep |
    | `...\contextMenu.xml` | `...\contextMenu.xml` | Optional |
    | `...\shortcuts.xml` | `...\shortcuts.xml` | Optional |
    | `...\toolbarIcons.xml` | `...\toolbarIcons.xml` | Optional |
    | `...\langs.xml` | `...\langs.model.xml` | Model |
    | `...\stylers.xml` | `...\stylers.model.xml` | Model |
    | `...\*_example.xml` | `...\*_example.xml` | Overwrite |
    | `...\themes\___.xml` | `...\themes\____.xml` | Overwrite ¹ |
    | `...\autoCompletion\___.xml` | `...\autoCompletion\____.xml` | Overwrite |
    | `...\localization\___.xml` | `...\localization\____.xml` | Overwrite |
    | `...\functionList\___.xml` | `...\functionList\____.xml` | Overwrite |
    | `...\userDefineLangs\___.xml` | `...\userDefineLangs\____.xml` | Overwrite |
    | `...\updater\*.*` | `...\updater\*.*` | Overwrite |
    | `...\change.log` | `...\change.log` | Overwrite |
    | `...\license.txt` | `...\license.txt` | Overwrite |
    | `...\doLocalConf.xml` | `...\doLocalConf.xml` | Zero-byte file |
    | `...\nppLog*Issue.xml` | `...\nppLog*Issue.xml` | Zero-byte file |

    - ¹: If you are using a specific theme, it's more likely that you will have customized that theme's file.  Please do a full comparison on that theme file, but you can probably get away with just overwriting the other "Destination" theme files using the copies in the "Temporary" directory.

4. After updating the config files, then you can exit Notepad++, copy the `notepad++.exe` and `plugins\config\nppPluginList.dll` from the "Temporary" to the "Destination", and restart Notepad++ to start using your upgraded portable edition which resides in the "Destination" directory.

The "portable" versions of Notepad++ assume you are willing to do some things manually in order to get your true portability.  If this procedure seems to complicated for you, and you would rather use something more automatic like the installer: You _can_ use the installer to put Notepad++ in any directory you want, not just in the Program Files hierarchy; and you can tell the installer that you don't want to use AppData, which will put the configuration files in the same directory that the executable goes in, which makes it _nearly_ portable (though the installer might have added hooks to make it easy for you to open files using the installed copy of Notepad++, which goes against the spirit of truly-portable software).

_Note: a similar procedure can be used when you think your installed copy of Notepad++ has themes or syntax highlighting configuration that is missing compared to a fresh install or portable: in that case, you would use `%AppData%\Notepad++\____.xml` and/or `C:\Program Files\Notepad++\____.xml` as the "Destination" location, instead of using a portable directory.  See [Configuration Files during Upgrades](../config-files/#configuration-files-during-upgrades)._

## Upgrading Plugins

Neither the installer/updater nor manually upgrading your portable edition will affect (nearly all of) your plugins, though upgrading either edition should update the `nppPluginList.dll` used to determine what plugins the **Plugins Admin**.  After upgrading Notepad++ by any means, you should go to [**Plugins > Plugins Admin > Updates**](../plugins/#install-using-plugins-admin) to check to see if any of your plugins should be updated.  (To clarify: The installer may also update any of the default plugins, including NppExport, NppConverter, and MIME Tools; however, if you don't use the installer, those can be upgraded using **Plugins Admin**'s **Updates** tab, as well.)
