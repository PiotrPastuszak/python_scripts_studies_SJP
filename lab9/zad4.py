#!/usr/bin/env python3
# -*- coding:utf8 -*-
import datetime
import sys
import getopt


def main():
    try:
        rok = input("Podaj rok:")
        miesiac = input("Podaj miesiąc:")
        dzien = input("Podaj dzień:")
        godzina = input("Podaj godzinę:")
        minuta = input("Podaj minutę:")
        sekunda = input("Podaj sekundę:")
        mikrosekunda = input("Podaj mikrosekundę:")
        rok = int(rok)
        miesiac = int(miesiac)
        dzien = int(dzien)
        godzina = int(godzina)
        minuta = int(minuta)
        sekunda = int(sekunda)
        mikrosekunda = int(mikrosekunda)
        data = datetime.datetime(rok, miesiac, dzien, godzina, minuta, sekunda, mikrosekunda)
        # wczytanie pliku i dodanie delt
        opts, args = getopt.getopt(sys.argv[1:], "i:", ["input"])
        for o, a in opts:
            if o in ("-i", "--input"):
                wejscie = open(a, "r")
        for line in wejscie:
            pom = line.split("]")
            sekplus = pom[0][1:].lstrip().split(".")
            deltaplus = datetime.timedelta(seconds=int(sekplus[0]), microseconds=int(sekplus[1]))
            pompom = ""
            for i in range(1, len(pom)):
                pompom = pompom + "]" + pom[i]
            print("[{}{}".format(data+deltaplus, pompom).rstrip())
    except ValueError:
        print("Podałeś nie liczby. Uruchom skrypt ponownie.")
    except IndexError:
        print("Podałeś nieistniejący rok, miesiąc, dzień, godzinę, minutę, sekundę lub mikrosekundę. Uruchom skrypt ponownie.")


if __name__ == "__main__":
    main()
