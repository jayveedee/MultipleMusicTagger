from os import listdir
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.oggvorbis import OggVorbis
from mutagen.m4a import M4A
from mutagen.oggopus import OggOpus

import sys
import mutagen


def errorMessage():
    print("Invalid arguments")
    print("Arguments required:")
    print("\t- #1: Path to directory, example: /home/user/Music")
    print("\t- #2: Music tag, example: genre, artist, album, comment, etc.")
    print("\t- #3: Music content, the text that you wish to insert into the given music tag")
    print("Example on running the program")
    print("\tpython tagger.py /home/user/Music genre pop")
    exit()


def check_file_ext(file):
    file_ext = file.split('.')
    if len(file_ext) == 1:
        return None
    file_ext = file_ext[len(file_ext) - 1]
    return file_ext


def directory_investigator(directory):
    # Check which extensions are in the directory and append them to a list
    file_exts = []
    for file in directory:
        file_ext = check_file_ext(file)
        if file_ext is None:
            continue
        if file_ext not in file_exts:
            print(file_ext)
            file_exts.append(file_ext)
    return file_exts


flac_dict = {"title": "TITLE", "album": "ALBUM", "comment": "COMMENT", "artist": "ARTIST", "genre": "GENRE"}
mp3_dict = {"title": "title", "album": "album", "comment": "COMM::eng", "artist": "TPE1", "genre": "TCON"}


def handleFLAC(tag, text, file_directory, debug=True):
    audio = FLAC(file_directory)
    # Removes comment
    audio[flac_dict["comment"]] = ""

    # Appends tag
    audio[flac_dict[tag]] = text
    audio.save()
    if debug:
        print(type(audio.info))
        print(type(audio.tags))
        # Prints all current file metadata entries
        for tags in audio.tags:
            print(tags)


def handleOPUS(tag, text, file_directory):
    pass


def handleMP3(tag, text, file_directory, debug=False):
    # Removes comment


    # Appends tag
    audio = MP3(file_directory, ID3=EasyID3)

    if debug:
        print(type(audio.info))
        print(type(audio.tags))
        # Prints all current file metadata entries
        for tags in audio.tags:
            print(tags)
        # Prints all current file EasyID3 metadata entries
        print(audio.pprint())
        # Prints all available EasyID3 metadata keys to edit
        print(EasyID3.valid_keys.keys())
        # Prints all current file metadata entries
        print(mutagen.File(file_directory).keys())


def handleM4A(tag, text, file_directory):
    pass


def handleOGG(tag, text, file_directory):
    pass


def tag_file(tag, text, file_ext, file_directory):
    if file_ext == "flac":
        handleFLAC(tag, text, file_directory)
    elif file_ext == "opus":
        handleOPUS(tag, text, file_directory)
    elif file_ext == "mp3":
        handleMP3(tag, text, file_directory)
    elif file_ext == "m4a":
        handleM4A(tag, text, file_directory)
    elif file_ext == "ogg":
        handleOGG(tag, text, file_directory)
    else:
        return False
    return True


def append_metadata(file_directory, music_files, tag, text):
    # Iterate through all files
    for file in music_files:
        file_ext = check_file_ext(file)
        if file_ext is None:
            continue
        if not tag_file(tag, text, file_ext, file_directory + file):
            print(f"Metadata not appended for file: {file}")


def start(debug=False):
    try:
        music_path_dir = sys.argv[1]
        music_tag = sys.argv[2]
        music_new_content = sys.argv[3]
        if debug:
            directory_investigator(listdir(music_path_dir))
        append_metadata(music_path_dir + "/", listdir(music_path_dir), music_tag, music_new_content)
    except IndexError:
        errorMessage()


start()
