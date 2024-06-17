#!/usr/bin/env python3
# -*- coding:utf8 -*-
import subprocess


def main():
    linie = subprocess.run(["ls", "-la", "."], capture_output=True, encoding="utf8").stdout.split("\n")
    for line in linie:
        print("wysłane z Pythona:  {}".format(line))


if __name__ == "__main__":
    main()
