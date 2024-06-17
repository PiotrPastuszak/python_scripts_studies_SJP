#!/usr/bin/env python3
# -*- coding:utf8 -*-
import sys

i=1
suma=[0.0, 0.0, 0.0, 0.0, 0.0]
niepisane=[0, 0, 0, 0, 0]
for line in sys.stdin:
	if i>1:
		a=line.rstrip().split(',')
		sumacala=0.0
		niezdane=0.0
		for i in range(3,8):
			if float(a[i])<0:
				niezdane=+1
			else:
				sumacala+=float(a[i])
				suma[i-3]+=float(a[i])
		print("{} {} {} {} {}".format(a[0], a[1], a[2], sumacala/5.0, sumacala/(5-niezdane)))
	i+=1

print("jeden {} dwa {} trzy {} cztery {} final {}".format(suma[0]/(i-1-niepisane[0]), suma[1]/(i-1-niepisane[1]), suma[2]/(i-1-niepisane[2]), suma[3]/(i-1-niepisane[3]), suma[4]/(i-1-niepisane[4])))
