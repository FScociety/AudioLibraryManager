import os
import time
import re
import config
from tinytag import TinyTag

music_files = []


class MusicFile:
    file_path = ""
    file_words = []
    file_name = ""
    file_extension = ""
    file_length = 0

    def __init__(self, file_path, file_name, file_words, file_extension):
        # save local function variables to global class variables
        self.file_path = file_path
        self.file_name = file_name
        self.file_words = file_words
        self.file_extension = file_extension

        self.audio = TinyTag.get(self.getCompletePath())

        if self.audio.duration != None:
            self.file_length = self.audio.duration / 6
            self.file_length = round(self.file_length * 10) / 100
            #self.file_length = round(self.audio.duration * 100) / 10
        else:
            self.file_length = 0

    def checkMatch(self, search_words):
        matching = 0

        for word in self.file_words:
            word = word.lower()  # make all file names LOWERCASE
            for search_word in search_words:
                search_word = search_word.lower()  # make all search names LOWECASE
                if search_word in word:
                    matching += 1
                    break
        return matching

    def getCompletePath(self):
        return self.file_path + "/" + self.file_name

    def printNames(self):
        print(self.file_words)


class Library:
    def getPath(self, index):
        return music_files[index]

    def isSupported(self, file):
        # Test if file has a supported file file_extension
        # This test is not in the file class,
        # cause you don't want to create files which aren't used afterwards
        for format in config.supported_formats:
            if file.endswith(format):
                return True
        return False

    def check_valid_element(self, element):
        print("checking:", element)
        for seperator in config.seperators_clean:
            if seperator == element:
                print("failed with:", seperator)
                return None
            else:
                print("Worked with:", seperator)
                return element

    def split_into_words(self, name):
        split = re.split(config.seperators_converted, name)
        return [string for string in split if string != ""]

    def saveFile(self, file_path, file_name_raw):
        file_name_split = os.path.splitext(file_name_raw)

        music_files.append(MusicFile(
            file_path,
            file_name_raw,
            self.split_into_words(file_name_raw),
            file_name_split[1]))

    def loadLibrary(self, path):
        for path, subdir, files in os.walk(config.music_libaries[0]):
            for name in files:
                if self.isSupported(name):
                    self.saveFile(path, name)

    def search(self, search_request):
        # Split input into different words and remove additional ""
        search_processed = search_request.split(" ")
        search_processed = [string for string in search_processed if string != ""]

        search_result = []

        for file in music_files:
            if file.checkMatch(search_processed) > 0:
                search_result.append(file)

        return search_result

    def __init__(self, path):
        self.loadLibrary(path)
