# kindle-words

![Not Maintained](https://img.shields.io/badge/Maintenance%20Level-Not%20Maintained-yellow.svg)

<b>As of early 2023, it's likely the script doesn't work due to API changes.</b>

<br><hr><br>

![](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-blue)

> Do something useful with your Kindle notes :) This script extracts individual words from `My Clippings` file hidden on your Kindle e-reader, translates them using Google Translate and exports the pair "original word" → "translation" into a `.txt` file from which you can learn these words or import them into an application such as [Quizlet](https://quizlet.com/).

Script skips sentences, numbers, special characters, etc. — only single words are being translated. Words in desired language are skipped.

## Screenshots
![output](https://user-images.githubusercontent.com/6877391/111391325-ac6d1f80-86b4-11eb-9816-470e442a1034.png)
![macOS notification](https://user-images.githubusercontent.com/6877391/111626634-8e0b3f00-87ee-11eb-8b1c-0379db96bc8c.jpeg)
![nothing](https://user-images.githubusercontent.com/6877391/111667392-f40abd00-8814-11eb-9b66-9d9ec19b92d5.png)
![sets in Quizlet](https://user-images.githubusercontent.com/6877391/111392214-631dcf80-86b6-11eb-99c1-95ba4c997834.png)

## How to use

### Speed things up ⚡
`deep-translator` works very slowly with Google Translate so we need to do a little tweak first. Install the package and go to the location where `deep-translator` is installed:
```sh
pip install deep-translator
pip show deep-translator
```
Open `google_trans.py` & go to line 177. Edit:
```py
# sleep(2) # => ~ 33.33 mins to translate 1000 words
sleep(0.1) # => ~ 1.66 mins to translate 1000 words
```
Save.

### Windows
1. Connect your Kindle via USB cable to your computer.
2. Download `script.zip` from [Releases](https://github.com/vardecab/kindle-words/releases).
3. Go to the download location, unzip & run `script.exe`. 
4. Write source & target languages or wait if defaults (`en` & `pl`) are ok.
5. Write drive letter associated with Kindle or wait if default (`D`) is ok.
6. Wait a few minutes - words are being translated.
7. Go to `script\output\kindle-words_export.txt` to check exported file.
8. (optional) Add it to [Quizlet](https://quizlet.com/).
9. Voilà ✨

### macOS
1. Connect your Kindle via USB cable to your Mac.
2. Clone or download this repo.
3. Open Terminal/iTerm and install necessary packages (use `pip` or `pip3`):
```py
pip install inputimeout
pip install deep-translator 
pip install pync
pip install langdetect
```
3. Navigate to the folder you cloned/downloaded & run the script:
```sh
cd '/Users/USER/Downloads/kindle-words'
python script.py
``` 
4. Write source & target languages or wait if defaults (`en` & `pl`) are ok.
5. Write your Kindle's name or wait if default (`Kindle`) is ok.
6. Wait a few minutes - words are being translated.
7. Go to `output/kindle-words_export.txt` to check exported file.
8. (optional) Add it to [Quizlet](https://quizlet.com/).
9. Voilà ✨

## Roadmap
 
- 🎯 Dictionary definitions. (Need a different API)
- ✅ <del>Improve regex formula to better deal with words that have special characters.</del>
- ✅ <del>Extract single words from source file.</del>
- ✅ <del>Output list line by line.</del> 
- ✅ <del>Use API to translate words.</del>
- ✅ <del>Skip the same words on subsequent imports.</del>
- ❌ <del>Use DeepL rather than Google Translate.</del> (Requires paid subscription)

## Release History

- 1.6: Added backup functionality to save `My Clippings` file locally
- 1.5.2: Added one more rule to clean the data.
- 1.5.1: Fixed Windows 10 notifications bug.
- 1.5: Added language detection to skip translation of words already in desired language.
- 1.4: Added notifications for macOS & Windows.
- 1.3: Added support for macOS.
- 1.2.1: Added `try/except` to fix a `FileNotFoundError` error.
- 1.2: Fixed `io.open` bug; added some `try/except` to catch more errors; re-enabled `timeout_time`; added `last_word` export so it's easy to see which words are new and which are old. Published in [Releases](https://github.com/vardecab/kindle-words/releases).
- 1.1: Quite a big re-write: it now works properly with `My Clippings.txt` file from Kindle - all bugs are fixed. Initial run takes ~ 10 minutes to complete (depending on the size of your file) but afterwards it's usually < 1 minute because data from previous run is stored locally for comparison - only new words are being translated to save time and improve speed.
- 1.0.0: Using new backend - [deep-translator](https://github.com/nidhaloff/deep-translator). 
- 0.12.5: Bug in the API discovered.
- 0.12.4: Cleared up the code for better readability.
- 0.12.3: Fixes to `regex` formula so it also takes words with `,` & `—`.
- 0.12.2: Print which folder was created for exported files.
- 0.12.1: Renamed variables & export files' names to improve readability. 
- 0.12: Be able to select source & target languages.
- 0.11: Added input timeout.
- 0.10: Take input file directly from Kindle once drive letter is given.
- 0.9: Export files to specific folders based on today's date & ID. 
- 0.8: Add script runtime info.
- 0.7: Fixes to `regex` formula so it also takes words with `.`, `-` & `"`.
- 0.6: Print translations directly to `kindle-words_export-{DATE}.txt`.   
- 0.5: No more duplicate words.
- 0.4: Fixed `charmap' codec can't encode character (...)` problem that occured with PL characters. 
- 0.3: Translation with [googletrans](https://pypi.org/project/googletrans) lib.
-   0.2: Output list line by line + export to a `.txt.` file. 
-   0.1: Initial release. Extract single words from source file using `regex`.

## Versioning

Using [SemVer](http://semver.org/).

## License

![](https://img.shields.io/github/license/vardecab/kindle-words)
<!-- 
GNU General Public License v3.0, see [LICENSE.md](https://github.com/vardecab/umbrella/blob/master/LICENSE). -->

## Acknowledgements
### Packages
- [deep-translator](https://github.com/nidhaloff/deep-translator)
- [inputimeout](https://pypi.org/project/inputimeout/)
- [win10toast-click](https://github.com/vardecab/win10toast-click)
- [pync](https://github.com/SeTeM/pync)
- [langdetect](https://pypi.org/project/langdetect/)
### Articles
- [Text Translation with Google Translate API in Python](https://stackabuse.com/text-translation-with-google-translate-api-in-python/)
- [Change python 3.7 default encoding from cp1252 to cp65001 aka UTF-8](https://stackoverflow.com/questions/56995919/change-python-3-7-default-encoding-from-cp1252-to-cp65001-aka-utf-8)
- [Print lists in Python](https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/)
- [Writing to a File with Python's print() Function](https://stackabuse.com/writing-to-a-file-with-pythons-print-function/)
- [Python switch case](https://www.journaldev.com/15642/python-switch-case)
- [Using .write function with multiple arguments for writing to a txt file - Python](https://stackoverflow.com/questions/47425891/using-write-function-with-multiple-arguments-for-writing-to-a-txt-file-python)
### Tools
- [regex101](https://regex101.com/)
- [regexr](https://regexr.com/)
### Other
- [Flaticon / Freepik](https://www.flaticon.com/)

## Contributing

![](https://img.shields.io/github/issues/vardecab/kindle-words)

If you found a bug or want to propose a feature, feel free to visit [the Issues page](https://github.com/vardecab/kindle-words/issues).