#!/usr/bin/env python3
# -*- coding:utf8 -*-
import sys
import getopt
import string
import math


def main():
    opts, args = getopt.getopt(sys.argv[1:], "i:hrwRuUHlad:c", ["input", "help"])
    wejscie = sys.stdin
    for o, a in opts:
        if o in ("-i", "--input"):
            wejscie = open(a, "r")
    for line in wejscie:
        for o, a in opts:
            if o in ("-r"):
                line = line[::-1]
            if o in ("-w"):
                line = " ".join(line.split(" ")[::-1])
            if o in ("-R"):
                pom = line.split(" ")
                for x in pom:
                    x = x[::-1]
                line = " ".join(pom)
            if o in ("-u"):
                line = line.upper()
            if o in ("-U"):
                line = string.capwords(line, " ")
            if o in ("-H"):
                pom = line.split(" ")
                for slowo in pom:
                    slowo1 = slowo[0:math.ceil((len(pom)/2))].upper()
                    slowo2 = slowo[math.ceil((len(pom)/2)):]
                    slowo = slowo1 + slowo2
                line = " ".join(pom)
            if o in ("-l"):
                line = line.lower()
            if o in ("-a"):
                pom = line.split(" ")
                pom = sorted(pom)
                line = " ".join(pom)
            if o in ("-d"):
                for i in range(len(a)):
                    line = line.replace(a[i], "")
            if o in ("-c"):
                print(str(len(line.split(" "))) + "w, " + str(len(line)) + "c:    ")
        print(line)


if __name__ == "__main__":
    main()
