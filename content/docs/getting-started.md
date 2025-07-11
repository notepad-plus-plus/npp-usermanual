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

For all the portable editions, everything (the application, settings, and plugins) is stored in one folder hierarchy.  And by default, the portable editions do not mess with operating system settings (so no file associations or **Edit with Notepad++** context-menu entries) -- if you want such with a portable edition, you will have to set it up manually.

The main portable 7z or zip editions contain all the themes, user defined languages, auto-completions, localizations, and default plugins and Plugins Admin tool that come with the installed version of Notepad++.

The minimalist / mini-portable edition only comes with the default light-mode and dark-mode theme, the default English localization, and no plugins or Plugins Admin.  However, you can separately download any of the non-included config files that you want from the main Notepad++ source repository, and you can still [install plugins manually](../plugins/#install-plugin-manually).

The portable editions of Notepad++ can be removed by deleting the directory they came in.  If you manually set up file associations or context-menu entries in the OS, it is your responsibility to remove them yourself.

## "Program Files" Restrictions

Windows is particular about what goes into "Program Files", and restricts permissions there, usually requiring Administrator Privilege to install or edit there.

When Notepad++ is placed in "Program Files" (whether through the installer or through unzipping a portable edition there), it intentionally does _not_ honor the [doLocalConf.xml](../config-files/#other-configuration-files) that comes from the "Do not Use %APPDATA%" setting or unzipping a portable edition there or manually creating the file, and will instead use your `%AppData%\Notepad++` directory for [storing settings](../config-files/#configuration-files-location) despite that file being there.

## Notepad++ Self-Signed Certificate Authority for Binaries

Notepad++ has always had difficulty getting a Certificate Authority to issue a code-signing certificate to "Notepad++" instead of to an individual, since Notepad++ is not a registered business.  In the lead-up to [v8.8.2 release](https://notepad-plus-plus.org/news/8.8.2-available-in-1-week-without-certificate/), Don was unable to get a signing certificate for "Notepad++", so v8.8.2 was released unsigned.  However, having the installer and executables and DLLs unsigned causes issues with installing Notepad++, and many virus scanners will give a "false positive" virus warning because of the missing signature.

To rectify this, there is now a self-signed Notepad++ Root Certificate Authority (CA) certificate.  Starting with v8.8.3, this Root CA certificate is used to create a signing certificate for Notepad++'s installer and other binaries.   Since this is not one of the "traditional" Certificate Authority entities, the Notepad++ Root CA certificate is not already included in your Windows installation, unlike the "big name" authorities.

Assuming you trust the download connection, and trust Notepad++ to correctly issue signing certificates to itself for signing Notepad++ binaries, the following instructions can be followed so that your computer is made aware that signatures coming from the Notepad++ Root CA are valid:
1. Download the x509 CA root certificate from https://notepad-plus-plus.org/nppRoot.crt
2. Open the certificate in the built-in Windows certificate viewer
    - Usually, double-clicking the downloaded `nppRoot.crt` file is sufficient.
    - Alternately, right clicking and choosing **Open** can also open it.
    - Under unusual circumstances, right clicking and choosing **Open With**, then choosing `Crypto Shell Extensions` is required.
3. Once it's open
    - The **General** tab will say something akin to "This CA Root certificate is not trusted" at this point.  That is expected, because you have not yet told Windows to trust it.
    - On the **General** tab, click **Install Certificate**
    - Pick `Current User` and click **Next**
    - _Don't_ pick `Automatically select...`, because that will default to "Intermediate Certification Authorities", which isn't sufficient level of trust for Windows.
    - Instead, pick `Place all certificates in the following store`, and **Browse...** to `Trusted Root Certification Authorities`, then click **Ok** then **Next**
    - On the next page, with a summary of what you are doing, you can click **Finish**
    - Windows will pop up a security warning, because you are putting it in the Trusted Root CA . Make sure you understand the implications of moving forward with YES.
    - Once you see "The import was successful", you can close that popup with **OK**
    - You can also close the Certificate at this point.
4. If you open the certificate again, the **General** tab now shows the certificate's purpose, and the **Certification Path** tab will show it's trusted.
5. If you ever want to _remove_ that Trusted Root CA certificate (for example, if you stop trusting Notepad++'s certification/signature):
    - Use `Win+R` to bring up **Run** dialog, and run `certmgr.msc` .
    - Navigate to `Trusted Root Certification Authorities` > `Certificates` .
    - Scroll down until you find `Notepad++ Root Certificate`, and right click on it, then **Delete** and **Yes**.

Two more hints, if you are having trouble locating the certificate after you think you've installed it per the instructions above:
1. If you accidentally picked `Local Machine` instead of `Current User` in step 3, then `certgr.msc` will not be able to see/remove it; you would have to use `certlm.msc` instead (and may have to give UAC permission).
2. In either `certmgr.msc` or `certlm.msc`, you can search for Notepad++ certificates by using **Action > Find Certificates...**
    - **Find In** = `All certificate stores`
    - **Contains** = `Notepad++`
    - **Look in Field** = `Issued By` or `Issued To` (the two might give different results, so may need to try both)
    - Click **Find Now**

Also, Notepad++ publishes a "Revocation List" to invalidate older certificates.
- Download the file from https://notepad-plus-plus.org/nppRevoke.crl (if your browser just shows the contents, do a **Save As**, or come back to this page, and use the right-click **Save Link As** or equivalent).
- From inside `certmgr.msc` with the **Trusted Root Certification Authorities > Certificates** selected, **Actions > All Tasks > Import**, and navigate to the `nppRevoke.crl`.  This will revoke any certificates from that list.

### Current Root Certificate Authority Details

- Download links:
    - Primary Location: https://notepad-plus-plus.org/nppRoot.crt
    - Secondary Location: the Notepad++ GitHub repository
        - GitHub repo page: https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/nppRoot.crt
            - From here, you can use the "raw" buttons in the browser to get the raw contents or save the raw contents to disk.  You cannot just "save link as" on the github.com URL and download a valid certificate.
        - Raw (downloadable) link: https://raw.githubusercontent.com/notepad-plus-plus/notepad-plus-plus/refs/heads/master/nppRoot.crt
            - This URL can be directly downloaded (with the caveat found in the note, below)
    - Tertiary Location: https://npp-user-manual.org/docs/certs/nppRoot.crt
        - _Note_: If you would like to cross-verify that the certificates are all the same, you can grab the certificate from each of those locations, and compare to each other and the values published below.
- **Name**: `Notepad++ Root Certificate`
- **Serial Number**: `63a633d265f1ffed66c5c67cbd9b7189`
- **Thumbprint**: `C80539FF7076D22E73A01F164108DAFBF06E45E4`
- **Created**: `2025-07-09`
- **Expires**: `2055-07-09`
    - Please note: the dates are based on the time in France.  Depending on your timezone, the date shown in your certificate viewer may show a different day.

Please note: the notepad-plus-plus.org and npp-user-manual.org hosts may require that you respond to an "I am a human, not a robot" page, or otherwise do a human-verification before it allows you to see any pages on those websites, let alone download a file, so if you've never visited the main sites, just following those direct links (or trying to save-link-target-as) may be blocked.  The hosts may also require that javascript be enabled in your browser as part of their not-a-robot check, so command-line based downloaders (`Invoke-WebRequest` or `wget` or similar) or standalone file-download utilities (that don't have a fully-featured web browser behind them) might also be blocked.  If you are blocked, go to https://notepad-plus-plus.org and https://npp-user-manual.org in your browser, and make sure that you get access to the website; for as long as the hosts/providers cache your "I am a human" credentials, the direct URLs should work after that, at least in that browser.
