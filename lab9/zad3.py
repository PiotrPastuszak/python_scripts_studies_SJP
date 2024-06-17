#!/usr/bin/env python3
# -*- coding:utf8 -*-
import datetime


def main():
    try:
        print("Data wczesniejsza:")
        rok1 = input("Podaj rok:")
        miesiac1 = input("Podaj miesiąc:")
        dzien1 = input("Podaj dzień:")
        rok1 = int(rok1)
        miesiac1 = int(miesiac1)
        dzien1 = int(dzien1)
        print("Data późniejsza:")
        rok2 = input("Podaj rok:")
        miesiac2 = input("Podaj miesiąc:")
        dzien2 = input("Podaj dzień:")
        rok2 = int(rok2)
        miesiac2 = int(miesiac2)
        dzien2 = int(dzien2)
        data1 = datetime.date(rok1, miesiac1, dzien1)
        data2 = datetime.date(rok2, miesiac2, dzien2)
        print("Między podanymi datami minęło {} dni".format((data2-data1).days))
        czw = 0
        przest = 0
        for i in range(1, (data2-data1).days):
            if (data1+datetime.timedelta(i)).weekday() == 3:
                czw = czw + 1
            if (data1+datetime.timedelta(i)).month == 2 and (data1+datetime.timedelta(i)).day == 29:
                przest = przest + 1
        print("Pomiędzy tymi datami wystąpiło {} czwartków.".format(czw))
        print("Pomiędzy tymi datami wystąpiło {} 29. lutego.".format(przest))
    except ValueError:
        print("Podałeś nie liczby. Uruchom skrypt ponownie.")
    except IndexError:
        print("Podałeś nieistniejący dzień lub miesiąc. Uruchom skrypt ponownie.")


if __name__ == "__main__":
    main()
