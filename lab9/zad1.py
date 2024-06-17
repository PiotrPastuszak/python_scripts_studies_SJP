#!/usr/bin/env python3
# -*- coding:utf8 -*-
import datetime


def main():
    wejscie = input("Podaj ilosci dni[d], godzin[h], minut[m] i sekund[s] oddzielone spacjami np.: 2d 16h 7m 3s\n").split(" ")
    ldays = 0
    lhours = 0
    lminutes = 0
    lseconds = 0
    for w in wejscie:
        if w[-1] == "d":
            ldays = int(w[0:-1])
        if w[-1] == "h":
            lhours = int(w[0:-1])
        if w[-1] == "m":
            lminutes = int(w[0:-1])
        if w[-1] == "s":
            lseconds = int(w[0:-1])
    roznica = datetime.timedelta(days=ldays, hours=lhours, minutes=lminutes, seconds = lseconds)
    teraz = datetime.datetime.now()
    terazutc = datetime.datetime.utcnow()
    print("teraz:    {}".format(teraz))
    print("teraz UTC:    {}".format(terazutc))
    print("później:    {}".format(teraz+roznica))
    print("wcześniej:    {}".format(teraz-roznica))


if __name__ == "__main__":
    main()
