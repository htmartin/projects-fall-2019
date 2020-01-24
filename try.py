#!/usr/bin/env python

sum=0
s='1.23,2.4,3.123'
l=s.split(",")
for i in l:
	sum =sum +float(i)
	print(sum)