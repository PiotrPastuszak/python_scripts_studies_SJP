#!/usr/bin/env python3
# -*- coding:utf8 -*-
import sys
import getopt


def dzielniki(liczba):
    wynik = []
    for i in range(1, liczba+1):
        if liczba % i == 0:
            wynik.append(i)
    return wynik


def main():
    opts, args = getopt.getopt(sys.argv[1:], "i:h", ["input", "help"])

    wejscie = -1
    for o, a in opts:
        if o in ("-i", "--input"):
            wejscie = a
        elif o in ("-h", "--help"):
            print("-i <liczba> podanie liczby której dzielniki będą szukane")
            exit()

    if wejscie == -1:
        if len(args) > 0:
            wejscie = args[-1]

    wzakresie = False
    czyliczba = False
    if type(wejscie) == int:
        czyliczba = True
    elif wejscie.isdigit():
        wejscie = int(wejscie)
        czyliczba = True
    if czyliczba:
        if int(wejscie) in range(1, 101):
            wzakresie = True

    while (not wzakresie) or (not czyliczba):
        wejscie = input("Podana liczba jest z poza zakresu od 1 do 100 lub nie jest liczbą. Podaj liczbę:")
        wzakresie = False
        czyliczba = False
        if type(wejscie) == int:
            czyliczba = True
        elif wejscie.isdigit():
            wejscie = int(wejscie)
            czyliczba = True
        if czyliczba:
            if int(wejscie) in range(1, 101):
                wzakresie = True
    print(dzielniki(int(wejscie))[::-1])

if __name__ == "__main__":
    main()
