---
title: Binary Translation
weight: 140
---

Notepad++ supports multi-language functionality by means of a translated xml file (based on the official [english.xml](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/english.xml) translation).

### Creating or Editing a translation

Maybe Notepad++ doesn't currently have the language you would like to use.  Or maybe, Notepad++ has been updated recently but the translation file is one or more versions behind, so some of the text isn't in your selected language.  Maybe the official Notepad++ translation for a language doesn't match your particular usage of that language.  Or sometimes, you just want to have some fun rewording things for your own amusement.  

The process of teaching Notepad++ a new language is virtually identical to editing an existing language, and both processes are described here:

1. Download the master copy of [english.xml](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/english.xml) and save it into the `%APPDATA%\Notepad++\localization\` or `Notepad++_Install_Dir\localization\` directory (see [Configuration Files Location](../config-files/#configuration-files-location)).  Create the `localization\` directory first, if it doesn't already exist.
    * This will be used as the source for a new translation, and a reference when you are editing an existing language.
3. This step depends on whether you are editing an existing language translation, or creating a new translation from scratch:
    1. For an existing translation: Download the most recent copy of the existing language translation from the [localization portion of the code repository](https://github.com/notepad-plus-plus/notepad-plus-plus/tree/master/PowerEditor/installer/nativeLang) and save it into the same folder as `localization\english.xml`.
        * _Note_: If you are wanting to change the English text for your own use, please edit `localization\english_customizable.xml` instead of `localization\english.xml`, since `english.xml` is meant to exist as an "absolute reference" with the official names of each of the text entries.
    2. For a new translation for a language that Notepad++ doesn't already have: Copy `localization\english.xml` to `localization\<yourlanguagename>.xml`
4. Edit `localization\<yourlanguagename>.xml`
    1. Make sure the initial `<?xml ... ?>` tag indicates `encoding="utf-8"`.
    2. Update the `<Native-Langue...>` tag near the top of the file:
        * Make sure the `name="___"` attribute matches your language's native name.  This is the name that will show up in the [Preference](../preferences/#general) dialog's **Localization** pulldown
        * Make sure the `filename="___.xml"` matches your language name
        * Make sure `version="8.1.1"` matches the most-recent Notepad++ version number.  It should already match, if you downloaded the most recent `english.xml` as described above.
    3. Edit the `name="..."` attributes as appropriate for the language you are editing.
        * _Note_: Do _not_ change any of the `id="###"` or `subMenuId="xxx"` attributes, as those are used to map the text in the `name="..."` attribute to the right piece of text in Notepad++.  If you change those, the localization file will not work properly.
        * You may use XML character entities for characters.  (_Note_: unlike HTML, XML only has 5 [predefined named entities](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references#Predefined_entities_in_XML "XML Entity List"); all other characters require [numeric or hexadecimal entities](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references#Character_reference_overview).)
        * If the encoding was properly set (above), you may insert Unicode characters directly.
        * When possible, keep the translated text about the same length (in characters) as the original English; this will help make sure the translation will fit in menus and dialog boxes which were designed to fit the official English text.
5. To see the changes take effect, save the file, then go to [**Settings > Preferences > General > Localization**](../preferences/#general) and select `<yourlanguagename>` from the pulldown menu: this will copy `localization\<yourlanguagename>.xml` to `nativeLang.xml` and will immediately update the Notepad++ application to use the text from your saved XML file.
    * _Note_: If you do not see the right language in the pulldown, you need to make sure you put the XML file(s) in the right directory, as explained above.
    * You may actually do the process of saving the file then selecting **Localization** = `<yourlanguagename>` throughout your development of the translation, to be able to see the changes you make as you go.

### Share your translation

If you have updated an existing translation to match the most recent version of Notepad++, or if you have created a translation for a new language that isn't currently available in Notepad++, you may want to request that it get added to the Notepad++ codebase, so that it will be distributed with the next version of the application.  To do so, create your own fork of the [codebase](https://github.com/notepad-plus-plus/notepad-plus-plus/) and make a Pull Request to ask that your translation be added to the main repository; if you do not know how to make Pull Requests, see the GitHub documentation; or you may create an [issue](https://github.com/notepad-plus-plus/notepad-plus-plus/issues) asking for the tranlsation to be updated, and attach your XML file to the issue.  Before making any Pull Request, please read and understand and follow the [Rules for Contributing to Notepad++'s codebase](https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/CONTRIBUTING.md).

### Available translations

<div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/taiwaneseMandarin.xml" target="_blank"> <img src="/docs/images/flags/fTaiwan.png" alt="" border="0" /><br/> Taiwanese Mandarin</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/french.xml" target="_blank"><img src="/docs/images/flags/fFrance.png" alt="" border="0" /><br/> French</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/spanish.xml" target="_blank"><img src="/docs/images/flags/fSpain.png" alt="" border="0" /><br/> Spanish</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/hungarian.xml" target="_blank"><img src="/docs/images/flags/fHungary.png" alt="" border="0" /><br/> Hungarian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/russian.xml" target="_blank"><img src="/docs/images/flags/fRussia.png" alt="" border="0" /><br/> Russian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/dutch.xml" target="_blank"><img src="/docs/images/flags/fNetherlands.png" alt="" border="0" /><br/> Dutch</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/hongKongCantonese.xml" target="_blank"><img src="/docs/images/flags/fHongKong.png" alt="" border="0" /><br/> Hongkonger</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/uyghur.xml" target="_blank"><img src="/docs/images/flags/fEastTurkestan.png" alt="" border="0" /><br/> Uyghur</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/chineseSimplified.xml" target="_blank"><img src="/docs/images/flags/fChina.png" alt="" border="0" /><br/> Chinese Simplified</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/polish.xml" target="_blank"><img src="/docs/images/flags/fPoland.png" alt="" border="0" /><br/> Polish</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/german.xml" target="_blank"><img src="/docs/images/flags/fGermany.png" alt="" border="0" /><br/> German</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/italian.xml" target="_blank"><img src="/docs/images/flags/fItaly.png" alt="" border="0" /><br/> Italian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/danish.xml" target="_blank"><img src="/docs/images/flags/fDenmark.png" alt="" border="0" /><br/> Danish</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/czech.xml" target="_blank"><img src="/docs/images/flags/fCzech.png" alt="" border="0" /><br/> Czech</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/slovenian.xml" target="_blank"><img src="/docs/images/flags/fSlovenia.png" alt="" border="0" /><br/> Slovenian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/slovak.xml" target="_blank"><img src="/docs/images/flags/fSlovakia.png" alt="" border="0" /><br/> Slovak</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/ukrainian.xml" target="_blank"><img src="/docs/images/flags/fUkraine.png" alt="" border="0" /><br/> Ukrainian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/turkish.xml" target="_blank"><img src="/docs/images/flags/fTurkey.png" alt="" border="0" /><br/> Turkish</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/brazilian_portuguese.xml" target="_blank"><img src="/docs/images/flags/fBrazil.png" alt="" border="0" /><br/> Brazilien Portuguese</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/norwegian.xml" target="_blank"><img src="/docs/images/flags/fNorway.png" alt="" border="0" /><br/> Norwegian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/swedish.xml" target="_blank"><img src="/docs/images/flags/fSweden.png" alt="" border="0" /><br/> Swedish</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/catalan.xml" target="_blank"><img src="/docs/images/flags/fCatalunya.png" alt="" border="0" /><br/> Catalan</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/greek.xml" target="_blank"><img src="/docs/images/flags/fGreece.png" alt="" border="0" /><br/> Greek</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/lithuanian.xml" target="_blank"><img src="/docs/images/flags/fLithuania.png" alt="" border="0" /><br/> Lithuanian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/galician.xml" target="_blank"><img src="/docs/images/flags/fGalicia.png" alt="" border="0" /><br/> Galician</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/finnish.xml" target="_blank"><img src="/docs/images/flags/fFinland.png" alt="" border="0" /><br/> Finnish</a>
</div>


<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/arabic.xml" target="_blank"><img src="/docs/images/flags/fPalestinie.png" alt="" border="0" /><br/> Arabic</a>
</div>


<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/romanian.xml" target="_blank"><img src="/docs/images/flags/fRomania.png" alt="" border="0" /><br/> Romanian</a>
</div>


<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/extremaduran.xml" target="_blank"><img src="/docs/images/flags/fExtremadura.png" alt="" border="0" /><br/> Extremaduran</a>
</div>


<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/korean.xml" target="_blank"><img src="/docs/images/flags/fKorea.png" alt="" border="0" /><br/> Korean</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/hebrew.xml" target="_blank"><img src="/docs/images/flags/fIsrael.png" alt="" border="0" /><br/> Hebrew</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/portuguese.xml" target="_blank"><img src="/docs/images/flags/fPortugal.png" alt="" border="0" /><br/> Portuguese</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/farsi.xml" target="_blank"><img src="/docs/images/flags/fIran.png" alt="" border="0" /><br/> Farsi</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/samogitian.xml" target="_blank"><img src="/docs/images/flags/fSamogitia.png" alt="" border="0" /><br/> Samogitian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/bulgarian.xml" target="_blank"><img src="/docs/images/flags/fBulgaria.png" alt="" border="0" /><br/> Bulgarian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/indonesian.xml" target="_blank"><img src="/docs/images/flags/fIndonesia.png" alt="" border="0" /><br/> Indonesian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/albanian.xml" target="_blank"><img src="/docs/images/flags/fAlbania.png" alt="" border="0" /><br/> Albanian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/japanese.xml" target="_blank"><img src="/docs/images/flags/fJapan.png" alt="" border="0" /><br/> Japanese</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/croatian.xml" target="_blank"><img src="/docs/images/flags/fCroatia.png" alt="" border="0" /><br/> Croatian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/georgian.xml" target="_blank"><img src="/docs/images/flags/fGeorgia.png" alt="" border="0" /><br/> Georgian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/basque.xml" target="_blank"><img src="/docs/images/flags/fBasque.png" alt="" border="0" /><br/> Basque</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/aranese.xml" target="_blank"><img src="/docs/images/flags/fValdAran.png" alt="" border="0" /><br/> Aranese</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/spanish_ar.xml" target="_blank"><img src="/docs/images/flags/fArgentine.png" alt="" border="0" /><br/> Spanish (Argentina)</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/belarusian.xml" target="_blank"><img src="/docs/images/flags/fBelarus.png" alt="" border="0" /><br/> Belarusian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/serbian.xml" target="_blank"><img src="/docs/images/flags/fSerbia.png" alt="" border="0" /><br/> Serbian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/nynorsk.xml" target="_blank"><img src="/docs/images/flags/fNorway.png" alt="" border="0" /><br/> Nynorsk</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/thai.xml" target="_blank"><img src="/docs/images/flags/fThailand.png" alt="" border="0" /><br/> Thai</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/malay.xml" target="_blank"><img src="/docs/images/flags/fMalaysia.png" alt="" border="0" /><br/> Malay</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/occitan.xml" target="_blank"><img src="/docs/images/flags/fOccitanie.png" alt="" border="0" /><br/> Occitan</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/friulian.xml" target="_blank"><img src="/docs/images/flags/fFriuli.png" alt="" border="0" /><br/> Friulian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/luxembourgish.xml" target="_blank"><img src="/docs/images/flags/fLuxembourgish.png" alt="" border="0" /><br/> Luxembourgish</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/tagalog.xml" target="_blank"><img src="/docs/images/flags/fPhilippines.png" alt="" border="0" /><br/> Tagalog</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/uzbek.xml" target="_blank"><img src="/docs/images/flags/fUzbekistan.png" alt="" border="0" /><br/> Uzbek</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/kazakh.xml" target="_blank"><img src="/docs/images/flags/fKazakhstan.png" alt="" border="0" /><br/> Kazakh</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/afrikaans.xml" target="_blank"><img src="/docs/images/flags/fSouthAfrica.png" alt="" border="0" /><br/> Afrikaans</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/kyrgyz.xml" target="_blank"><img src="/docs/images/flags/fKyrgyzstan.png" alt="" border="0" /><br/> Kyrgyz</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/macedonian.xml" target="_blank"><img src="/docs/images/flags/fMacedonia.png" alt="" border="0" /><br/> Macedonian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/latvian.xml" target="_blank"><img src="/docs/images/flags/fLatvian.png" alt="" border="0" /><br/> Latvian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/tamil.xml" target="_blank"><img src="/docs/images/flags/fIndia.png" alt="" border="0" /><br/> Tamil</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/azerbaijani.xml" target="_blank"><img src="/docs/images/flags/fAzerbaijan.png" alt="" border="0" /><br/> Azerbaijani</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/bosnian.xml" target="_blank"><img src="/docs/images/flags/fBosnia.png" alt="" border="0" /><br/> Bosnian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/esperanto.xml" target="_blank"><img src="/docs/images/flags/fEsperanto.png" alt="" border="0" /><br/> Esperanto</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/ligurian.xml" target="_blank"><img src="/docs/images/flags/fLiguria.png" alt="" border="0" /><br/> Ligurian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/hindi.xml" target="_blank"><img src="/docs/images/flags/fIndia.png" alt="" border="0" /><br/> Hindi</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/sardinian.xml" target="_blank"><img src="/docs/images/flags/fSardinia.png" alt="" border="0" /><br/> Sardinian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/telugu.xml" target="_blank"><img src="/docs/images/flags/fIndia.png" alt="" border="0" /><br/> Telugu</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/aragonese.xml" target="_blank"><img src="/docs/images/flags/fAragon.png" alt="" border="0" /><br/> Aragonese</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/sinhala.xml" target="_blank"><img src="/docs/images/flags/fSriLanka.png" alt="" border="0" /><br/> Sinhala</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/marathi.xml" target="_blank"><img src="/docs/images/flags/fIndia.png" alt="" border="0" /><br/> Marathi</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/mongolian.xml" target="_blank"><img src="/docs/images/flags/fMongolia.png" alt="" border="0" /><br/> Mongolian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/welsh.xml" target="_blank"><img src="/docs/images/flags/fWales.png" alt="" border="0" /><br/> Welsh</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/kannada.xml" target="_blank"><img src="/docs/images/flags/fIndia.png" alt="" border="0" /><br/> Kannada</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/urdu.xml" target="_blank"><img src="/docs/images/flags/fPakistan.png" alt="" border="0" /><br/> Urdu</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/gujarati.xml" target="_blank"><img src="/docs/images/flags/fIndia.png" alt="" border="0" /><br/> Gujarati</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/estonian.xml" target="_blank"><img src="/docs/images/flags/fEstonia.png" alt="" border="0" /><br/> Estonian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/bengali.xml" target="_blank"><img src="/docs/images/flags/fIndia.png" alt="" border="0" /><br/> Bengali</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/punjabi.xml" target="_blank"><img src="/docs/images/flags/fIndia.png" alt="" border="0" /><br/> Punjabi</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/corsican.xml" target="_blank"><img src="/docs/images/flags/fCorsica.png" alt="" border="0" /><br/> Corsican</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/breton.xml" target="_blank"><img src="/docs/images/flags/fBrittany.png" alt="" border="0" /><br/> Breton</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/kurdish.xml" target="_blank"><img src="/docs/images/flags/fKurdistan.png" alt="" border="0" /><br/> Kurdish</a>
</div>
<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/irish.xml" target="_blank"><img src="/docs/images/flags/fIreland.png" alt="" border="0" /><br/> Irish</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/venetian.xml" target="_blank"><img src="/docs/images/flags/fVeneto.png" alt="" border="0" /><br/> Venetian</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/nepali.xml" target="_blank"><img src="/docs/images/flags/fNepal.png" alt="" border="0" /><br/> Nepali</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/zulu.xml" target="_blank"><img src="/docs/images/flags/fZululand.png" alt="" border="0" /><br/> Zulu</a>
</div>

<div align="center" style="margin: 20px; display: inline-block;">
<a href="https://github.com/notepad-plus-plus/notepad-plus-plus/blob/master/PowerEditor/installer/nativeLang/abkhazian.xml" target="_blank"><img src="/docs/images/flags/fAbkhazia.png" alt="" border="0" /><br/> Abkhazian</a>
</div>

</div>
