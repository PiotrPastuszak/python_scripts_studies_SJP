#!/usr/bin/env python3
# -*- coding:utf8 -*-
import subprocess
import time


def main():
    poczatek = time.time()
    print("kod zwrotny: {}".format(subprocess.run(["gzip", "-9", "plik.txt"]).returncode))
    print("trwało to {}".format(time.time()-poczatek))


if __name__ == "__main__":
    main()
