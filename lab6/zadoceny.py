#!/usr/bin/env python3
# -*- coding:utf8 -*-
import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:], "i:o:u:", ["input", "output" "user"])
i = 1
suma = [0.0, 0.0, 0.0, 0.0, 0.0]
niepisane = [0, 0, 0, 0, 0]
wejscie = sys.stdin
wyjscie = sys.stdout
user = ""

for o, a in opts:
    if o in ("-i", "--input"):
        wejscie = open(a, "r")
    elif o in ("-o", "--output"):
        wyjscie = open(a, "w")
    elif o in ("-u", "--user"):
        user = a

if wejscie == sys.stdin:
    # print(sys.argv)
    wejscie = open(args[-1], "r")

for line in wejscie:
    if i > 1:
        a = line.rstrip().split(',')
        sumacala = 0.0
        niezdane = 0.0
        for i in range(3, 8):
            if float(a[i]) < 0:
                niezdane += 1
            else:
                sumacala += float(a[i])
                suma[i-3] += float(a[i])
        if (user == "" or user == a[2].lstrip()[1:-1]):
            wyjscie.write("{} {} {} {} {}\n".format(a[0], a[1], a[2], sumacala/5.0, sumacala/(5-niezdane)))
    i += 1

if user == "":
    wyjscie.write("jeden {} dwa {} trzy {} cztery {} final {}\n".format(suma[0]/(i-1-niepisane[0]), suma[1]/(i-1-niepisane[1]), suma[2]/(i-1-niepisane[2]), suma[3]/(i-1-niepisane[3]), suma[4]/(i-1-niepisane[4])))
if wejscie != sys.stdin:
    wejscie.close()
if wyjscie != sys.stdout:
    wyjscie.close()
