#!/usr/bin/env python3
# -*- coding:utf8 -*-
import sys

linie=0
slowa=0
litery=0
zbior={}
for line in sys.stdin:
	litery+=len(line)
	slowa+=len(line.split(' '))
	linie+=1
	for slowo in line.rstrip().split(' '):
		if slowo in zbior:
			zbior[slowo]+=1
		else:
			zbior[slowo]=1

print("{} {} {}".format(linie, slowa, litery))
for slowo in zbior:
	print("{} {}".format(slowo, zbior[slowo]))
