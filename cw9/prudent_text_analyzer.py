#!/bin/python3
import sys
from typing import Dict


class EmptyFileError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)


class TextAnalyzer:
    __stat: Dict[str, int] = {}
    __file = None

    def __init__(self):
        self.__stat = {}

    def load_file(self, filepath: str):
        try:
            self.__file = open(filepath)
            try:
                msg = self.__file.read()
                if msg == "":
                    raise EmptyFileError
                msg = msg.lower()
                for w in msg.split():
                    if w in self.__stat.keys():
                        self.__stat[w] += 1
                    else:
                        self.__stat[w] = 1
            finally:
                self.__file.close()

        except FileNotFoundError:
            print("FileNotFoundError")

    def get_word_count(self, word: str) -> int:
        if word in self.__stat.keys():
            return self.__stat[word]
        return 0

    def __call__(self):
        return self.__stat


if __name__ == "__main__":
    ta = TextAnalyzer()
    ta.load_file(str(sys.argv[1]))
    print(ta.get_word_count("aa"))
    print(ta.get_word_count("ww"))
    print(ta())
