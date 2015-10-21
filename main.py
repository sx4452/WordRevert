__author__ = 'ben'

import time
import codecs
import sys

from CONSTANT import DICTPATH
from CONSTANT import INPUTPATH
from CONSTANT import OUTPUTPATH

def FindWord(WordsDictLines, word):
    blank = WordsDictLines[0][1]
    if(cmp(word, 'went') == 0):
        wordlist = {}
        wordlist[0] = 'go'
        wordlist[1] = 'v.'
        return True, wordlist
    if(cmp(word, 'gone') == 0):
        wordlist = {}
        wordlist[0] = 'go'
        wordlist[1] = 'v.'
        return True, wordlist
    if(cmp(word, 'sat') == 0):
        wordlist = {}
        wordlist[0] = 'sit'
        wordlist[1] = 'v.'
        return True, wordlist
    for wordline in WordsDictLines:
        wordlinelist = wordline.split(blank)
        if(cmp(word, wordlinelist[0]) == 0):
            return True, wordlinelist
        else:
            if(len(wordlinelist[0]) > 0):
                if(len(word) > 4):
                    if(cmp(word[-3:], 'ing') == 0 and cmp(wordlinelist[0][-1:], word[-5:-4]) == 0
                        and cmp(wordlinelist[0][-1:], word[-4:-3]) == 0 and cmp(wordlinelist[0][:-1], word[:-5]) == 0):
                        return True, wordlinelist
                        break
                if(len(word) > 3):
                    if(cmp(word[-2:], 'ed') == 0 and cmp(wordlinelist[0][-1:], word[-4:-3]) == 0 and
                        cmp(wordlinelist[0][-1:], word[-3:-2]) == 0 and cmp(wordlinelist[0][:-1], word[:-4]) == 0):
                        return True, wordlinelist
                        break
                if(len(word) > 2):
                    if(cmp(word[-3:], 'ies') == 0 and cmp(wordlinelist[0][:-1], word[:-3]) == 0 and cmp(wordlinelist[0][-1:], 'y') == 0):
                        return True, wordlinelist
                        break
                    if(cmp(word[-3:], 'ing') == 0 and cmp(wordlinelist[0], word[:-3]) == 0):
                        return True, wordlinelist
                        break
                    if(cmp(word[-3:], 'ing') == 0 and cmp(wordlinelist[0][:-1], word[:-3]) == 0 and cmp(wordlinelist[0][-1:], 'e') == 0):
                        return True, wordlinelist
                        break
                    if(cmp(word[-3:], 'ied') == 0 and cmp(wordlinelist[0][:-1], word[:-3]) == 0 and cmp(wordlinelist[0][-1:], 'y') == 0):
                        return True, wordlinelist
                        break
                if(len(word) > 1):
                     if(cmp(word[-2:], 'es') == 0 and cmp(wordlinelist[0], word[:-2]) == 0):
                         return True, wordlinelist
                         break
                     if(cmp(word[-2:], 'ed') == 0 and cmp(wordlinelist[0], word[:-2]) == 0):
                         return True, wordlinelist
                         break
                     if(cmp(word[-2:], 'ed') == 0 and cmp(wordlinelist[0][:-1], word[:-2]) == 0 and cmp(wordlinelist[0][-1:], 'e') == 0):
                         return True, wordlinelist
                         break
                if(len(word) > 0):
                    if(cmp(word[-1:], 's') == 0 and cmp(wordlinelist[0], word[:-1]) == 0):
                        return True, wordlinelist
                        break
            if(len(wordlinelist[0]) > 1):
                if(cmp(word[-4:], 'ying') == 0 and cmp(wordlinelist[0][:-2], word[:-4]) == 0 and cmp(wordlinelist[0][-2:], 'ie') == 0):
                    return True, wordlinelist
                    break
    return False, ''

def main():
    WordsDict = open(DICTPATH, 'r')
    outputFile = open(OUTPUTPATH, 'w+')
    inputFile = open(INPUTPATH, 'r')
    inputlines = inputFile.readlines()
    WordsDictLines = WordsDict.readlines()
    word = ''
    for word in inputlines:
        #word = raw_input("Please input a word:\n")
        [isfind, findword] = FindWord(WordsDictLines, word[:-1])
        if(isfind):
            outputStr = findword[0] + ' ' + findword[1]
            print outputStr
            outputFile.write(outputStr + '\n')
        else:
            print 'This is not in the dictionary, loading Undefined-Words-Mode......'
    WordsDict.close()
    outputFile.close()

if __name__ == "__main__":
    start = time.clock()
    main()
    end = time.clock()
    print 'runtime is '
    print end