#!/usr/bin/env python3
# -*- coding:utf8 -*-
import urllib.request
import sys
import getopt


def main():
    naszurl = ""

    opts, args = getopt.getopt(sys.argv[1:], "h", [])
    if len(args) != 0:
        naszurl = args[-1]
    else:
        print ("niepodano URLa")
        exit()
    for o, a in opts:
        if o in ("-h"):
            print("klient <URL> wydrukuje pierwsze 300 bajtow zdekodowanych wedlug utf-8")

    with urllib.request.urlopen(naszurl) as f:
        print(f.read(300).decode('utf-8'))


if __name__ == "__main__":
    main()

