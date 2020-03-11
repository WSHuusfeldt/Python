import string
import re

file = "./yoyo.txt"

def countWordsInFile(fileName, word):
    string = ''
    with open(fileName) as fo:
        line = fo.readline()
        while(line):
            string += line +"\n"
            line = fo.readline()
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), string))
    print(word + ' occurs ' + str(count) + ' times in file')

def countWords(word, string):
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), string))
    print(word + ' occurs ' + str(count) + ' times in string')

def countCharInFile(fileName, char):
    string = ''
    with open(fileName) as fo:
        line = fo.readline()
        while(line):
            string += line +"\n"
            line = fo.readline()
    print(char + ' occurs ' + str(string.count(char)) + ' times in string')

def countChar(char, string):
    print(char + ' occurs ' + str(string.count(char)) + ' times in string')

