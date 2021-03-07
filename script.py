### current date & time
from datetime import datetime # have current date & time in exported files' names
this_run_datetime = datetime.strftime(datetime.now(), '%y%m%d-%H%M%S') # eg 210120-173112; https://www.w3schools.com/python/python_datetime.asp

### start + run time
import time
start_time = time.time() 
print("Starting...")

### *NOTE: fix for "'charmap' codec can't encode character (...)" problem; https://stackoverflow.com/questions/56995919/change-python-3-7-default-encoding-from-cp1252-to-cp65001-aka-utf-8
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

### path to file: https://www.journaldev.com/15642/python-switch-case
from sys import platform # check platform (Windows/Linux/macOS)
if platform == 'win32':
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
# elif platform == "darwin": # macOS
    # path = {} # TODO

### input timeout
from inputimeout import inputimeout, TimeoutOccurred # input timeout: https://pypi.org/project/inputimeout/

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

# select Kindle drive letter
try:
    kindle_drive_letter = inputimeout(prompt="Enter the drive letter that is assigned to your Kindle (C/D/E/F): ", timeout=3)
    with io.open(path.get(kindle_drive_letter,r'x:\documents\My Clippings.txt'), "r", encoding="utf-8") as source_file: 
        read_source_file = source_file.read()
except TimeoutOccurred:
    print ("Time ran out.")
    # *NOTE: test
    # with io.open(r'./_old/test.txt', "r", encoding="utf-8") as source_file: 
    #     print('Selecting test file...')
    #     read_source_file = source_file.read()
    # *NOTE: prod 
    with io.open(r'D:\documents\My Clippings.txt', "r", encoding="utf-8") as source_file: 
        print('Selecting default drive (D)...')
        read_source_file = source_file.read()

### regex formula 
import re # regex; extract words
regex_find_single_words = re.compile(r"^[\w'’“\-\.\,\—]+$", re.MULTILINE) # experiment; version to include , & —

### find single words in the source file 
print('Looking for words...')
single_words_with_special_characters = re.findall(regex_find_single_words,read_source_file)
# print ("Single words: ", single_words) # debug (with duplicates)
print ("Found", len(single_words_with_special_characters), 'words.') # debug (how many words in the list)

### remove duplicates from the list
print('Removing duplicates...')
original_words = list(dict.fromkeys(single_words_with_special_characters)) # final list of original words without duplicates etc.
print ("There are", len(original_words), 'words.') # debug (how many words in the list)

## print single words line by line & export file 
import os # create new folders
# print (*single_words_with_special_characters, sep = "\n") # debug
print('Creating a folder & exporting words to a file...')
output_lines = '\n'.join(map(str, original_words)) # https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
if not os.path.isdir("/output/" + this_run_datetime):
    os.mkdir("output/" + this_run_datetime)
    print ("Folder created: " + this_run_datetime)
with open(r"output/" + this_run_datetime + "/output-" + this_run_datetime + ".txt", "w", encoding="utf-8") as output: 
    output.write(output_lines.lower())

### take single words with special characters from the file and remove unnecessary chars (eg ".-)
print('Removing unnecessary characters...')
with io.open(r"output/" + this_run_datetime + "/output-" + this_run_datetime + ".txt", "r", encoding="utf-8") as source_file:  
    read_source_file = source_file.read()

single_words = re.findall(r"\b\w*[-'’]\w*\b|\w+",read_source_file)
output_lines = '\n'.join(map(str, single_words))
with open(r"output/" + this_run_datetime + "/output-original_words-" + this_run_datetime + ".txt", "w", encoding="utf-8") as output: 
    output.write(output_lines.lower())

### translation
from deep_translator import GoogleTranslator

print('Translating...')
translated = GoogleTranslator(source=select_source_language, target=select_target_language).translate_file(r"output/" + this_run_datetime + "/output-original_words-" + this_run_datetime + ".txt")
# print(type(translated)) # debug
with open(r"output/" + this_run_datetime + "/output-translated_words-" + this_run_datetime + ".txt", "w", encoding="utf-8") as export_translations: 
    for word in translated:
        # print(translated)
        export_translations.write(word)
print('Translated, nice!')

### export a pair: original → translated 
with open(r"output/" + this_run_datetime + "/output-translated_words-" + this_run_datetime + ".txt", "r", encoding="utf-8") as import_translations:
    translated_words = import_translations.read().splitlines()
# print(len(translated_words)) # debug; check if == 

with open(r"output/" + this_run_datetime + "/kindle-words_export-" + this_run_datetime + ".txt", "w", encoding="utf-8") as export_pairs:
    for original, translated in zip(original_words, translated_words):
        # print(str(original + " → " + translated)) # debug 
        export_pairs.write((str(original + " → " + translated + "\n"))) # write() can't take more than 1 argument so we need to str()
print('Final file exported!')

### runtime 
end_time = time.time() # run time end 
run_time = round(end_time-start_time,2)
print("Script run time:", run_time, "seconds.")
# print("Script run time:", run_time, "seconds.""with", len(single_words), "translations.") 