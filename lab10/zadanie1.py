#!/usr/bin/env python3
# -*- coding:utf8 -*-
import re
import sys
import getopt


def main():
    opts, args = getopt.getopt(sys.argv[1:], "i:", ["input"])
    wejscie = sys.stdin
    for o, a in opts:
        if o in ("-i", "--input"):
            wejscie = open(a, "r")
    zasob = [str(line) for line in wejscie]
    print("zaczyna się na a, o, A lub O")
    wzor = re.compile("^[ao]", re.I)
    for line in zasob:
        for word in line.split(" "):
            if (wzor.match(word) is not None):
                print(word.rstrip())
    print("kończy się na ę,ó,ą,ś,ł,ż,ź,ć,ń")
    wzor = re.compile(".*[ęóąśłżźćń][.,?]?$", re.I + re.U)
    for line in zasob:
        for word in line.split(" "):
            if (wzor.match(word.rstrip()) is not None):
                print(word.rstrip())
    print("końce zdań")
    wzor = re.compile(".*[.]$", re.I)
    for line in zasob:
        for word in line.split(" "):
            if (wzor.match(word.rstrip()) is not None):
                print(word.rstrip())
    print("dwie spacje")
    for line in zasob:
        for word in re.findall("[ ][ ]\S+", line):
            print(word)
    print("3 samogłoski")
    wzor = re.compile("^[^eyuioaęóą\s]*[eyuioaęóą][^eyuioaęóą\s]*[eyuioaęóą][^eyuioaęóą\s]*[eyuioaęóą][^eyuioaęóą\s]*$", re.I)
    for line in zasob:
        for word in line.split(" "):
            if (wzor.match(word.rstrip()) is not None):
                print(word.rstrip())


if __name__ == "__main__":
    main()
