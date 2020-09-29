# kindle-words

> Do something useful with your Kindle notes :) This script extracts individual words from `My Clippings` file hidden on your Kindle e-reader, translates them using Google Translate and exports the pair "original word" → "translation" into a `.txt` file from which you can learn these words or import them into an application such as [Quizlet](https://quizlet.com/).

<!-- ## Screenshots -->

<!-- ## How to use -->

## Roadmap

- Use DeepL rather than Google Translate. 
- Dictionary definitions.
- <del>Improve regex formula to better deal with words that have special characters.</del>
- <del>Extract single words from source file.</del>
- <del>Output list line by line.</del> 
- <del>Use API to translate words.</del>
- <del>Skip the same words on subsequent imports.</del>

## Release History

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

-   https://stackabuse.com/text-translation-with-google-translate-api-in-python/
- https://pypi.org/project/googletrans
- https://regex101.com/
- https://stackoverflow.com/questions/56995919/change-python-3-7-default-encoding-from-cp1252-to-cp65001-aka-utf-8
- https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
- https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
