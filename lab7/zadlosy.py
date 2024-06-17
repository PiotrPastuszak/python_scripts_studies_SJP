#!/usr/bin/env python3
# -*- coding:utf8 -*-
import sys
import getopt
import random


def main():
    opts, args = getopt.getopt(sys.argv[1:], "m:x:h", ["help"])
    nmax = 20
    ilerazy = 4
    for o, a in opts:
        if o in ("-m"):
            try:
                a = int(a)
                nmax = a
            except ValueError:
                print("Na argumencie -m podano nieliczbę")
                nmax = 20
        elif o in ("-x"):
            try:
                a = int(a)
                ilerazy = a
            except ValueError:
                print("Na argumencie -x podano nieliczbę")
                ilerazy = 4
        elif o in ("-h", "--help"):
            print("-m <liczba> ustawia górną granicę losowania \n-x <liczba> ustawia ilość dozwolonych prób")
            exit()

    random.seed()
    n = random.randint(1, nmax)
    print("Wylosowano liczbę od 1 do {}. Masz {} prób. Odgadnij jaka to liczba.".format(nmax, ilerazy))
    for i in range(ilerazy):
        odp = 0
        czyok = False
        while not czyok:
            odp = input("Podaj odpowiedź:   ")
            try:
                odp = int(odp)
                czyok = True
            except ValueError:
                print("Nie podałeś liczby.")
        if odp == n:
            print("Podałeś poprawną odpowiedź")
            exit()
        elif odp > n:
            print("Twoja odpowiedź była za duża.")
        else:
            print("Twoja odpowiedź była za mała.")


if __name__ == "__main__":
    main()
