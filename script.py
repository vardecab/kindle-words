# kindle-words
# 0.12.4
# !FIX: doesn't work due to https://github.com/ssut/py-googletrans/issues/264 

### import libs 
import re # regex; extract words
from googletrans import Translator # Google Translate API; https://pypi.org/project/googletrans
import os # create new folders

### current date 
from datetime import datetime # have current date in exported files' names
today_date = datetime.strftime(datetime.now(), '%y%m%d-%f') # https://www.w3schools.com/python/python_datetime.asp

### script runtime
import time
start_time = time.time() 

### fix for "'charmap' codec can't encode character (...)" problem; https://stackoverflow.com/questions/56995919/change-python-3-7-default-encoding-from-cp1252-to-cp65001-aka-utf-8
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

### path to file; https://www.journaldev.com/15642/python-switch-case
path = {
    'C' : r'C:\documents\My Clippings.txt',
    'c' : r'C:\documents\My Clippings.txt',
    'D' : r'D:\documents\My Clippings.txt',
    'd' : r'D:\documents\My Clippings.txt',
    'E' : r'E:\documents\My Clippings.txt',
    'e' : r'E:\documents\My Clippings.txt',
    'F' : r'F:\documents\My Clippings.txt',
    'f' : r'F:\documents\My Clippings.txt'
}

### input timeout
from inputimeout import inputimeout, TimeoutOccurred # input timeout; https://pypi.org/project/inputimeout/

# select source language
try:
    select_source_language = inputimeout(prompt="Enter the source language (default: en): ", timeout=3)
except TimeoutOccurred:
    print ("Time ran out, selecting default source language (en)...")
    select_source_language = 'en'

# select target language
try:
    select_target_language = inputimeout(prompt="Enter the target language (default: pl): ", timeout=3)
except TimeoutOccurred:
    print ("Time ran out, selecting default target language (pl)...")
    select_target_language = 'pl'

# select Kindle driver letter
try:
    kindle_drive_letter = inputimeout(prompt="Enter the drive letter that is assigned to your Kindle (C/D/E/F): ", timeout=3)
    with io.open(path.get(kindle_drive_letter,r'x:\documents\My Clippings.txt'), "r", encoding="utf-8") as source_file: 
        read_source_file = source_file.read()
except TimeoutOccurred:
    print ("Time ran out, selecting default drive (D)...")
    # with io.open(r'_old/test.', "r", encoding="utf-8") as source_file: # *NOTE: test
    with io.open(r'D:\documents\My Clippings.txt', "r", encoding="utf-8") as source_file: # *NOTE: prod 
        read_source_file = source_file.read()

### regex formula 
regex_find_single_words = re.compile(r"^[\w'’“\-\.\,\—]+$", re.MULTILINE) # experiment; version to include , & —

### find single words in the source file 
single_words_with_special_characters = re.findall(regex_find_single_words,read_source_file)
# print ("Single words: ", single_words) # 🐛 debug (with duplicates)
print ("With dupes: ", len(single_words_with_special_characters)) # 🐛 debug (how many words in the list)

### remove duplicates from the list
single_words_with_special_characters = list(dict.fromkeys(single_words_with_special_characters))
print ("Without dupes: ", len(single_words_with_special_characters)) # 🐛 debug (how many words in the list)

## print single words line by line & export file 
# print (*single_words_with_special_characters, sep = "\n") # 🐛 debug
output_lines = '\n'.join(map(str, single_words_with_special_characters)) # https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
if not os.path.isdir("/output/" + today_date):
    os.mkdir("output/" + today_date)
    print ("Folder created: " + today_date)
with open(r"output/" + today_date + "/output-imperfect-" + today_date + ".txt", "w", encoding="utf-8") as output: 
    output.write(output_lines.lower())

### take single words with special characters from the file and remove unnecessary chars (eg ".-)
with io.open(r"output/" + today_date + "/output-imperfect-" + today_date + ".txt", "r", encoding="utf-8") as source_file:  
    read_source_file = source_file.read()

single_words = re.findall(r"\b\w*[-'’]\w*\b|\w+",read_source_file)
output_lines = '\n'.join(map(str, single_words))
with open(r"output/" + today_date + "/output-perfect-" + today_date + ".txt", "w", encoding="utf-8") as output: 
    output.write(output_lines.lower())

### translation
Translator = Translator()

# print directly to the file: https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
original_stdout = sys.stdout # save a reference to the original standard output
# with open(r"C:\Users\x\Desktop\kindle-words_export.txt", "w", encoding="utf-8") as export_translations: # "a" → append, "w" → write
with open(r"output/" + today_date + "/kindle-words_export-" + today_date + ".txt", "w", encoding="utf-8") as export_translations: # NOTE: "a" → append, "w" → write
    translations = Translator.translate(single_words, src=select_source_language, dest=select_target_language) # NOTE: / FIXME: black box - whole thing is ran inside which means progress bar won't work
    # for translation in tqdm(translations):
    # counter = 1 # progress
    for translation in translations:
        # print ("Word:", str(counter), "/", len(single_words)) # step in the process; progress
        sys.stdout = export_translations # output to the file above
        print (translation.origin, ' -> ', translation.text)
        sys.stdout = original_stdout # reset the standard output to its original value
        # counter += 1 # progress 

### runtime 
print("Script runtime: %.2f seconds" % (time.time() - start_time), "with", len(single_words), "translations.") 