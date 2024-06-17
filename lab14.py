#!/usr/bin/env python3
# -*- coding:utf8 -*-
import time
import threading
import random


def funkcjaWatka(parametr):
    global zmiennaWspolna
    for x in range(5):
        print("Wątek o numerze {}, iteracja {}, zmienna przed zmianą ma wartosc {}".format(parametr, x, zmiennaWspolna))
        zmiennaWspolna += 1
        time.sleep(random.random())


def main():
    global zmiennaWspolna
    zmiennaWspolna = 0
    for x in range(5):
        threading.Thread(target=funkcjaWatka, args=(x,)).start()
    print("koniec głównego wątku")


if __name__ == "__main__":
    main()

