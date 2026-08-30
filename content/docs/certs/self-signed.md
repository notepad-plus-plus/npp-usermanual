---
title: Historical Note > Self-Signed Certs
weight: 910
---

## Notepad++ Self-Signed Certificate Authority for Binaries

Notepad++ had issues with the code-signing certificate that Microsoft encourages applications to have.  If you are using v8.8.2 - v8.8.9, it is recommended that you immediately upgrade to the most recent version.  But you can read below for a historical explanation.

## Historical Explanation

Notepad++ has always had difficulty getting a Certificate Authority to issue a code-signing certificate to "Notepad++" instead of to an individual, since Notepad++ was not a registered business.  In the lead-up to [v8.8.2 release](https://notepad-plus-plus.org/news/8.8.2-available-in-1-week-without-certificate/), Don was unable to get a signing certificate for "Notepad++", so v8.8.2 was released unsigned.  However, having the installer and executables and DLLs unsigned causes issues with installing Notepad++, and many virus scanners will give a "false positive" virus warning because of the missing signature.  As of v8.8.7, the Notepad++ association has been registered with the appropriate government body, and GlobalSign has issued a certificate for Notepad++; from v8.8.7 through 8.8.9, Notepad++ is signed with both the GlobalSign-issued signing certificate as well as the self-signed certificate; from v8.9 onward, Notepad++ is only signed with the GlobalSign-issued certificate.

As a result of the period of not being able to have an externally-signed certificate, Notepad++ has a self-signed Root Certificate Authority (CA) certificate.  From v8.8.3 - v8.8.9, this Root CA certificate is used to create a signing certificate for Notepad++'s installer and other binaries (and starting with v8.8.7, such binaries are double-signed, with both the GlobalSign and self-signed signatures). Since the self-signed certificate is not one of the "traditional" Certificate Authority entities, the Notepad++ Root CA certificate is not already included in your Windows installation, unlike the "big name" authorities.

Security experts recommend _not_ adding the root certificate described below.  However, if you are dealing with binaries from v8.8.3 - v8.8.9, you may evaluate whether verifying the signature or not changing your root certificates is the "more secure" choice.

Assuming you trust the download connection, and trust Notepad++ to correctly issue signing certificates to itself for signing Notepad++ binaries, the following instructions can be followed so that your computer is made aware that signatures coming from the Notepad++ Root CA are valid:
1. Download the x509 CA root certificate from https://notepad-plus-plus.org/nppRoot.crt
2. Open the certificate in the built-in Windows certificate viewer
    - Usually, double-clicking the downloaded `nppRoot.crt` file is sufficient.
    - Alternately, right clicking and choosing **Open** can also open it.
    - Under unusual circumstances, right clicking and choosing **Open With**, then choosing `Crypto Shell Extensions` is required.
3. Once it's open
    - The **General** tab will say something akin to "This CA Root certificate is not trusted" at this point.  That is expected, because you have not yet told Windows to trust it.
    - On the **General** tab, click **Install Certificate**
    - Pick `Local Machine` and click **Next**
      - These instructions originally recommended `Current User` instead, because it doesn't require UAC/Admin permission.  But there are other issues when you do that, so it is now recommended to pick `Local Machine` to give the best chance of working.
    - _Don't_ pick `Automatically select...`, because that will default to "Intermediate Certification Authorities", which isn't sufficient level of trust for Windows.
    - Instead, pick `Place all certificates in the following store`, and **Browse...** to `Trusted Root Certification Authorities`, then click **Ok** then **Next**.
    - On the next page, with a summary of what you are doing, you can click **Finish**.
    - Windows will pop up a security warning, because you are putting it in the Trusted Root CA . Make sure you understand the implications of moving forward with YES.
    - Once you see "The import was successful", you can close that popup with **OK**.
    - You can also close the Certificate at this point.
4. If you open the certificate again, the **General** tab now shows the certificate's purpose, and the **Certification Path** tab will show it's trusted.
5. If you ever want to _remove_ that Trusted Root CA certificate (for example, if you stop trusting Notepad++'s certification/signature):
    - Use `Win+R` to bring up **Run** dialog, and run either `certmgr.msc` or `certlm.msc`.
      - If you chose `Current User` as the installation location above, use `certmgr.msc`.  But the recommendation above is to now use `Local Machine` if possible.
      - If you chose `Local Machine` as the installation location above, use `certlm.msc`.  You may need to use elevated UAC permission.
      - If you run the wrong msc, you will not be able to see the certificate.
    - Navigate to `Trusted Root Certification Authorities` > `Certificates` .
    - Scroll down until you find `Notepad++ Root Certificate`, and right click on it, then **Delete** and **Yes**.

Two more hints, if you are having trouble locating the certificate after you think you've installed it per the instructions above:
1. Remember that picking `Current User` or `Local Machine` decides whether you should use `certgr.msc` or `certlm.msc` , so run the right utility:
    - If you chose `Current User` as the installation location above, use `certmgr.msc`.  But the recommendation above is to now use `Local Machine` if possible.
    - If you chose `Local Machine` as the installation location above, use `certlm.msc`.  You may need to use elevated UAC permission.
    - If you run the wrong msc, you will not be able to see the certificate to verify or uninstall it.
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
