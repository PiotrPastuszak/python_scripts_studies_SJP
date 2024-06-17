#!/usr/bin/env python3
# -*- coding:utf8 -*-
import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:], "i:o:dn:Mr:h", ["input", "output" "user", "max", "Max", "replace", "help"])
i = 1
zip = {}
wejscie = sys.stdin
wejsciedebug = "sys.stdin"
wyjscie = sys.stdout
wyjsciedebug = "sys.stdout"
debug = False
n = 10
nn = False
mmax = False
r1 = []
r2 = []

for o, a in opts:
    if o in ("-i", "--input"):
        wejscie = open(a, "r")
        wejsciedebug = a
    elif o in ("-o", "--output"):
        wyjscie = open(a, "w")
        wyjsciedebug = a
    elif o in ("-d"):
        debug = True
    elif o in ("-n", "--max"):
        n = int(a)
        nn = True
    elif o in ("-M", "--Max"):
        mmax = True
    elif o in ("-r", "--replace"):
        r1.append(a.split(',')[0])
        r2.append(a.split(',')[1])
    elif o in ("-h", "--help"):
        print("-i <plik> lub --input <plik> dla ustalenia pliku wejsciowego") #jak zacznie dzialac sam plik na koncu to dodac
        print("-o <plik> lub --output <plik> dla ustalenia pliku wyjsciowego")
        print("-d dla debugowania")
        print("-n <liczba> lub --max <liczba> aby wypisać kody które występują mniej lub dokładnie liczba razy")
        print("-M lub --Max dla znalezienia najczęściej występującego kodu")
        print("-r <kod1,kod2> lub --replace <kod1,kod2> dla traktowania kod1 jakby wystąpił kod2 (przecinek obowiązkowy) (można użyć wielokrotnie)")
        print("-h lub --help aby zobaczyć tę pomoc")
        exit()

if wejscie == sys.stdin:
    # print(sys.argv)
    wejscie = open(args[-1], "r")

if debug:
    print("uruchomiono debugowanie")
    print("wejscie: {}".format(wejsciedebug))
    print("wyjscie: {}".format(wyjsciedebug))
    print("tryb kodów z iloscią mniejsza niz {} {}".format(n, nn))
    print("szukanie maksimum {}".format(mmax))
    print("tablica zamienianych kodów (z, potem na)")
    print(r1)
    print(r2)

for line in wejscie:
    if debug:
        print("obsluga linii nr {}".format(i))
        print(line)
    if i > 6:
        a = line.rstrip().split(',')
        if a[7] in r1:
            a[7] = r2[r1.index(a[7])]
        if debug:
            print("zamieniono kod na: {}".format(a[7]))
        if a[7] in zip:
            zip[a[7]] += 1
        else:
            zip[a[7]] = 1
        if debug:
            print("aktualnie zarejestrowano kod {} {} razy".format(a[7], zip[a[7]]))
    i += 1

if nn:
    wyjscie.write("Kody pocztowe z mniej niż lub dokładnie {} wystąpieniami:\n".format(n))
if debug:
    print("szukanie max kodu i kodów <= n")
maxkod = "aaaa"
for kod in zip:
    if nn:
        if zip[kod] <= n:
            wyjscie.write(kod+"\n")
        else:
            print("{} z {} wystapieniami nie zalapal sie do trybu -n".format(kod, zip[kod]))
    if maxkod in zip:
        if zip[kod] > zip[maxkod]:
            maxkod = kod
            if debug:
                print("nowy maxkod {} ma {} wystąpień".format(maxkod, zip[maxkod]))
    else:
        maxkod = kod
        if debug:
            print("pierwszy maxkod to {}".format(maxkod))
if mmax:
    print("Kod, który wystąpił najczęściej to " + str(maxkod) + " z " + str(zip[maxkod]) + " wystąpieniami.\n")
