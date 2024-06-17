#!/usr/bin/env python3
# -*- coding:utf8 -*-
import re
import sys
import getopt


def main():
    opts, args = getopt.getopt(sys.argv[1:], "i:abcde", ["input"])
    wejscie = sys.stdin
    for o, a in opts:
        if o in ("-i", "--input"):
            wejscie = open(a, "r")
    zasob = [str(line) for line in wejscie]
    numery = []
    nienumery = []
    for line in zasob:
        line = line.replace(" ", "")
        line = line.replace("-", "")
        print(line)
        if (re.search("(\+[0-9]{1,3})?[0-9]{9}", line, re.I) is not None):
            numery.append(re.search("(\+[0-9]{1,3})?[0-9]{9}", line, re.I).group())
        else:
            nienumery.append(re.search("[+]?[0-9][0-9]*", line, re.I).group())
    for o, a in opts:
        if o in ("-a"):
            print("opcja a")
            for x in nienumery:
                print(x)
        elif o in ("-b"):
            print("opcja b")
            for x in numery:
                if (re.match("\+", x, re.I) is not None):
                    print(x)
        elif o in ("-c"):
            print("opcja c")
            for x in numery:
                y = x[:-9]
                if (re.match("\+48", y, re.I) is not None):
                    print(x)
                elif (re.match("\+", y, re.I) is None):
                    print(x)
        elif o in ("-d"):
            print("opcja d")
            for x in numery:
                y = x[:-9]
                if len(x) > 0:
                    if (re.match("\+48", y, re.I) is None):
                        print(x)
        elif o in ("-e"):
            print("opcja e")
            for x in numery:
                wyjscie = "<"
                if len(x) > 9:
                    wyjscie = wyjscie + x[:-9]
                if (re.match("[34]0|5[0137]|6[069]|7[02389]|8[08]|90", x[-9:-7], re.I) is not None):
                    wyjscie = wyjscie + " " + x[-9:-6] + " " + x[-6:-3] + " " + x[-3:] + ">"
                else:
                    wyjscie = wyjscie + " " + x[-9:-7] + " " + x[-7:-4] + " " + x[-4:] + ">"
                print(wyjscie)


if __name__ == "__main__":
    main()
