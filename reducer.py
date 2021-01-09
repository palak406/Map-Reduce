#!/usr/bin/env python
import sys 
#Reference:https://sungsoo.github.io/2015/08/21/reservoir-sampling.html

parameter = int(sys.argv[1])
count = 0

for y in sys.stdin:
	(r,x) = y.split(' ',1)
  	print(x)
  	count+=1
  	if count == parameter:break
