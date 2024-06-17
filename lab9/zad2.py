#!/usr/bin/env python3
# -*- coding:utf8 -*-
import calendar


def main():
    try:
        rok = input("Podaj rok:")
        miesiac = input("Podaj miesiąc:")
        dzien = input("Podaj dzień:")
        rok = int(rok)
        miesiac = int(miesiac)
        dzien = int(dzien)
        print("a)   {}".format(calendar.day_name[calendar.weekday(rok, miesiac, dzien)]))
        print("b)   {}".format(calendar.day_name[calendar.weekday(rok, miesiac, 1)]))
        print("c)")
        calendar.prmonth(rok, miesiac)
    except ValueError:
        print("Podałeś nie liczby. Uruchom skrypt ponownie.")
    except IndexError:
        print("Podałeś nieistniejący dzień lub miesiąc. Uruchom skrypt ponownie.")


if __name__ == "__main__":
    main()
