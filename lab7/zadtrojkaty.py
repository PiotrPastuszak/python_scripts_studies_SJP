#!/usr/bin/env python3
# -*- coding:utf8 -*-
import math


def poleProstokata(a, b):
    return a*b


def poleTrojkata(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    p = (a+b+c)/2.0
    return math.sqrt(p*(p-a)*(p-b)*(p-c))


def main():
    ksztalt = input("Wybierz prostokąt(p) lub trójkąt(t):")
    while ksztalt not in ("p", "t"):
        ksztalt = input("Wybierz prostokąt(p) lub trójkąt(t):")

    a = 0
    b = 0
    c = 0
    czyok = False
    while not czyok:
        if ksztalt == "p":
            a = input("Podaj a:")
            b = input("Podaj b:")
        else:
            a = input("Podaj a:")
            b = input("Podaj b:")
            c = input("Podaj c:")
        try:
            a = float(a)
            b = float(b)
            c = float(c)
            if a > 0 and b > 0:
                if ksztalt == "t":
                    if c > 0:
                        czyok = True
                else:
                    czyok = True
            if not czyok:
                print("Co najmniej jedna z podanych wartości jest niewiększa od zera.")
        except ValueError:
            print("a, b lub c nie jest liczbą")

    if ksztalt == "t" and ((a > b+c) or (b > a+c) or (c > a+b)):
        print("Podane a, b i c nie spełniają warunku trójkąta.")
        exit()

    if ksztalt == "t":
        print("Pole trójkąta o podanych parametrach wynosi {}".format(poleTrojkata(a, b, c)))
    else:
        print("Pole prostokąta o podanych parametrach wynosi {}".format(poleProstokata(a, b)))


if __name__ == "__main__":
    main()
