#!/usr/bin/env python3
# -*- coding:utf8 -*-
import sys

i=1
zip={}
for line in sys.stdin:
	if i>6:
		a=line.rstrip().split(',')
		if a[7] in zip:
			zip[a[7]]+=1
		else:
			zip[a[7]]=1
	i+=1

print ("Kody pocztowe z mniej niż lub dokładnie 10 wystąpieniami:")
maxkod="aaaa"
for kod in zip:
	if zip[kod]<=10:
		print (kod)
	if maxkod in zip:
		if zip[kod]>zip[maxkod]:
			maxkod=kod
	else:
		maxkod=kod

print("Kod, który wystąpił najczęściej to " + str(maxkod) + " z " + str(zip[maxkod]) + " wystąpieniami.")
