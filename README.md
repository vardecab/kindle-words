# kindle-words

> Do something useful with your Kindle notes :) This script extracts individual words from `My Clippings` file hidden on your Kindle e-reader, translates them using Google Translate and exports the pair "original word" → "translation" into a `.txt` file from which you can learn these words or import them into an application such as [Quizlet](https://quizlet.com/).

## Screenshots
![](https://user-images.githubusercontent.com/6877391/111391325-ac6d1f80-86b4-11eb-9816-470e442a1034.png)
![](https://user-images.githubusercontent.com/6877391/111392214-631dcf80-86b6-11eb-99c1-95ba4c997834.png)

## How to use
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
pip install deep_translator 
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

- 1.1.3: Added support for macOS.
- 1.1.2: Added `try/except` to fix a `FileNotFoundError` error.
- 1.1.1: Fixed `io.open` bug; added some `try/except` to catch more errors; re-enabled `timeout_time`; added `last_word` export so it's easy to see which words are new and which are old. Published in [Releases](https://github.com/vardecab/kindle-words/releases).
- 1.1: Quite a big re-write: it now works properly with `My Clippings.txt` file from Kindle - all bugs are fixed. Initial run takes ~ 10 minutes to complete (depending on the size of your file) but afterwards it's usually < 1 minute because data from previous run is stored locally for comparison - only new words are being translated to save time and improve speed.
- 1.0.0: Using new API - [deep-translator](https://github.com/nidhaloff/deep-translator). 
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

GNU General Public License v3.0, see [LICENSE.md](https://github.com/vardecab/umbrella/blob/master/LICENSE).

## Acknowledgements
### Packages
- [deep-translator](https://github.com/nidhaloff/deep-translator)
- [inputimeout](https://pypi.org/project/inputimeout/)
### Articles
- [Text Translation with Google Translate API in Python](https://stackabuse.com/text-translation-with-google-translate-api-in-python/)
- [Change python 3.7 default encoding from cp1252 to cp65001 aka UTF-8](https://stackoverflow.com/questions/56995919/change-python-3-7-default-encoding-from-cp1252-to-cp65001-aka-utf-8)
- [Print lists in Python](https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/)
- [Writing to a File with Python's print() Function](https://stackabuse.com/writing-to-a-file-with-pythons-print-function/)
- [Python switch case](https://www.journaldev.com/15642/python-switch-case)
- [Using .write function with multiple arguments for writing to a txt file - Python](https://stackoverflow.com/questions/47425891/using-write-function-with-multiple-arguments-for-writing-to-a-txt-file-python)
### Tools
- [regex101](https://regex101.com/)