from os import listdir

import mutagen as m
import sys


def __init__():
    global MUSIC_PATH_DIR
    global MUSIC_TAG
    global MUSIC_NEW_CONTENT
    try:
        MUSIC_PATH_DIR = sys.argv[1]
        MUSIC_TAG = sys.argv[2]
        MUSIC_NEW_CONTENT = sys.argv[3]
    except IndexError:
        print("Invalid arguments")
        print("Arguments required:")
        print("\t- #1: Path to directory, example: /home/user/Music")
        print("\t- #2: Music tag, example: genre, artist, album, comment, etc.")
        print("\t- #3: Music content, the text that you wish to insert into the given music tag")
        print("Example on running the program")
        print("\tpython multiple_music_tagger.py /home/user/Music genre pop")
        exit()


def start():
    __init__()
    append_metadata(MUSIC_PATH_DIR, MUSIC_TAG, MUSIC_NEW_CONTENT, directory_investigator(listdir(MUSIC_PATH_DIR)))


def directory_investigator(directory, debug=True):
    # Check which extensions are in the directory and append them to a list
    file_exts = []
    for file in directory:
        file_ext = check_filename(file)
        if file_ext is None:
            continue

        if file_ext not in file_exts:
            if debug:
                print(file_ext)
            file_exts.append(file_ext)
    return file_exts


def check_filename(file):
    file_ext = file.split('.')
    if len(file_ext) == 1:
        return None
    file_ext = file_ext[len(file_ext) - 1]
    return file_ext


def append_metadata(directory, tag, text, file_exts, debug=True):
    # Iterate through all files
    for file in directory:
        file_ext = check_filename(file)
        if file_ext is None:
            continue


start()
