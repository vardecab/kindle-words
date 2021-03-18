### start + run time
import time
start_time = time.time() 
print("Starting...")

### *NOTE: fix for "'charmap' codec can't encode character (...)" problem; https://stackoverflow.com/questions/56995919/change-python-3-7-default-encoding-from-cp1252-to-cp65001-aka-utf-8
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

### notifications 
# imports
from sys import platform # check platform (Windows/macOS)
if platform == "darwin":
    import pync
elif platform == 'win32':
    import win10toast_click

### path to file: https://www.journaldev.com/15642/python-switch-case
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

### input timeout
from inputimeout import inputimeout, TimeoutOccurred # input timeout: https://pypi.org/project/inputimeout/
# timeout_time = 0 # *NOTE: test
timeout_time = 5 # *NOTE: prod
print(f'Script will wait {timeout_time} seconds for the input and then will continue with a default value.')

# select source language
try:
    select_source_language = inputimeout(prompt="Enter the source language (default: en): ", timeout=timeout_time)
except TimeoutOccurred:
    print ("Time ran out, selecting default source language (en)...")
    select_source_language = 'en'

# select target language
try:
    select_target_language = inputimeout(prompt="Enter the target language (default: pl): ", timeout=timeout_time)
except TimeoutOccurred:
    print ("Time ran out, selecting default target language (pl)...")
    select_target_language = 'pl'

# select Kindle drive letter
if platform == 'win32': # Windows
    try:
        kindle_drive_letter = inputimeout(prompt="Enter the drive letter that is assigned to your Kindle (C/D/E/F) (default: D): ", timeout=timeout_time)
        with io.open(path.get(kindle_drive_letter,r'x:\documents\My Clippings.txt'), "r", encoding="utf-8") as source_file: 
            read_source_file = source_file.readlines() # read the file to [list]
    except TimeoutOccurred:
        # print ("Time ran out.")
        # *NOTE: test
        # with io.open(r'./test/test.txt', "r", encoding="utf-8") as source_file: 
        #     print('Selecting test file...')
        #     read_source_file = source_file.readlines() # read the file to [list]
        # *NOTE: prod 
        try: 
            with io.open(r'D:\documents\My Clippings.txt', "r", encoding="utf-8") as source_file: 
                print('Time ran out, selecting default drive (D)...')
                read_source_file = source_file.readlines() # read the file to [list]
        except: 
            print('Kindle is either not connected or has a custom drive assignment. Try again. Exiting...')
            exit()
    except FileNotFoundError: 
        print ('Looks like Kindle is not assigned to this drive letter. Try a different one next time. Exiting...')
        exit() 

elif platform == "darwin": # macOS
    try: 
        kindle_name = inputimeout(prompt="Enter your Kindle's name: ", timeout=timeout_time).lower()
        with io.open(f'/Volumes/{kindle_name}/documents/My Clippings.txt', "r", encoding="utf-8") as source_file: 
            read_source_file = source_file.readlines() # read the file to [list]
    except TimeoutOccurred: 
        try: 
            with io.open('/Volumes/Kindle/documents/My Clippings.txt', "r", encoding="utf-8") as source_file: 
                print('Time ran out, choosing default name (Kindle)...')
                read_source_file = source_file.readlines() # read the file to [list]
        except: 
            print('Kindle is either not connected or it has a custom name. Try again. Exiting...')
            exit()
    except FileNotFoundError: 
        print ("Looks like this name doesn't work. Try a different one next time. Exiting...") 
        exit()

### create output & data folders
import os
if not os.path.exists('output'):
    os.makedirs('output')
if not os.path.exists('data'):
    os.makedirs('data')

### show the last word that was added on the previous run 
try: 
    with open('output/output-original_words.txt', 'r') as file:
        lines = file.read().splitlines()
        last_word = lines[-1]
    with open('output/last_word.txt', 'w') as file: 
        file.write(last_word)
except FileNotFoundError:
    print('First run - no file to load data.')

### list cleanup 
read_source_file = [x for x in read_source_file if not any(x1.isdigit() for x1 in x)] # remove numbers
read_source_file = [word.replace('\n','') for word in read_source_file] # remove character
read_source_file = [word.replace(',','') for word in read_source_file] # remove character
read_source_file = [word.replace('.','') for word in read_source_file] # remove character
read_source_file = [word.replace(';','') for word in read_source_file] # remove character
read_source_file = [word.replace('“','') for word in read_source_file] # remove character
read_source_file = [word.replace('”','') for word in read_source_file] # remove character
read_source_file = [word.replace('’','') for word in read_source_file] # remove character
read_source_file = [word.replace('—','') for word in read_source_file] # remove character
read_source_file = [word.replace('?','') for word in read_source_file] # remove character
read_source_file = [word.replace('!','') for word in read_source_file] # remove character
read_source_file = [word.replace('‘','') for word in read_source_file] # remove character
read_source_file = [word.replace('==========','') for word in read_source_file] # remove characters

### add single words to the new list aka remove sentences etc.
single_words = [] # new list
for element in range(len(read_source_file)):
    if len(read_source_file[element].split()) == 1: # only single words
        if len(read_source_file[element]) != 1: # don't add single characters
            single_words.append(read_source_file[element].split())
single_words = [x for l in single_words for x in l] # remove outer list; https://blog.finxter.com/python-list-of-lists/#Convert_List_of_Lists_to_One_List-2
print ("Found", len(single_words), 'words in My Clippings file.') # debug (how many words in the list)

print('Removing duplicates...')
single_words = list(dict.fromkeys(single_words)) # remove duplicates; https://www.w3schools.com/python/python_howto_remove_duplicates.asp
print ("There are", len(single_words), 'unique words in My Clippings file.')

### open saved list
import pickle
try: 
    with open ('data/saved_location', 'rb') as file_import:
        saved_list = pickle.load(file_import)
        # print(saved_list) # debug
except FileNotFoundError:
    print('First run - no file to load data.')

### comparison 
try: 
    difference = set(single_words) - set(saved_list) # what's new in single_words[]
    if len(saved_list) == 0:
        difference = set(single_words)
except: 
    difference = set(single_words)
to_translate = list(difference) # convert set to list
print("There are", len(to_translate), "new words to translate.")

if len(to_translate) > 0:
    output_lines = '\n'.join(map(str, to_translate))
    with open(r"output/output-original_words.txt", "a", encoding="utf-8") as output: 
        output.write(output_lines.lower())

    ### translation
    # split list to smaller lists to get around 5000-character-limit of deep-translator package
    chunks = [to_translate[x:x+250] for x in range(0, len(to_translate), 250)] # split into sublists of 250 words each
    print('List of words was split into:', len(chunks), 'chunk(s) for translation.') # debug; how many sublists are in this master list

    from deep_translator import GoogleTranslator, batch_detection
    print('Translating...')

    ### export a pair: original → translated 
    counter = 0
    while counter <= len(chunks)-1: # -1 to make it work when len(chunks) == 1 and chunks[0] is the only one
        translated_list = [] # new list
        translated_list = GoogleTranslator(select_source_language, select_target_language).translate_batch(chunks[counter])
        with open(r"output/kindle-words_export.txt", "a", encoding="utf-8") as export_pairs:
            for original, translated in zip(chunks[counter], translated_list):
                # print(str(original + " → " + translated)) # debug 
                export_pairs.write((str(original + " → " + translated + "\n")).lower()) # write() can't take more than 1 argument so we need to str()
        counter += 1
    print('Words are translated & final file is exported!')

    ### notifications 
    if platform == "darwin":
        pync.notify(f'Translated {len(to_translate)} words.', title='kindle-words', contentImage="https://i.postimg.cc/3R0tLQ3H/translation.png", sound="Funk") # appIcon="" doesn't work, using contentImage instead
    elif platform == "win32":
        toaster.show_toast(msg=f'Translated {len(to_translate)} words.', title="kindle-words",  icon_path="./icons/translation.ico", duration=None, threaded=True) # duration=None - leave notification in Notification Center; threaded=True - rest of the script will be allowed to be executed while the notification is still active

    ### export list for future comparison 
    with open('data/saved_location', 'wb') as file_export:
        pickle.dump(single_words, file_export)

    ### runtime 
    end_time = time.time() # run time end 
    run_time = round(end_time-start_time,2)
    print(len(to_translate), 'words were translated in:', run_time, "seconds (" + str(round(run_time/60,2)), "minutes).")
    
else:
    ### notifications 
    if platform == "darwin":
        pync.notify(f'Nothing new to translate.', title='kindle-words', contentImage="https://i.postimg.cc/3R0tLQ3H/translation.png", sound="Funk") # appIcon="" doesn't work, using contentImage instead
    elif platform == "win32":
        toaster.show_toast(msg=f'Nothing new to translate.', title="kindle-words",  icon_path="./icons/translation.ico", duration=None, threaded=True) # duration=None - leave notification in Notification Center; threaded=True - rest of the script will be allowed to be executed while the notification is still active

    print('Nothing new to translate. Exiting...')

    ### runtime 
    end_time = time.time() # run time end 
    run_time = round(end_time-start_time,2)
    print("Script run time:", run_time, "seconds. That's", round(run_time/60,2), "minutes.")