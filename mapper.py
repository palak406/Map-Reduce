#!/usr/bin/env python
import sys,random 
from heapq import *

#Reference: https://en.wikipedia.org/wiki/Reservoir_sampling
#Using Random Sort
cook_queue=[] #queue
parameter = int(sys.argv[1]) #length of the reservior
for x in sys.stdin:
    x= x.rstrip() #cleaning the data by removing the trailing characters
    if x == '':
        continue
    


    id_r = random.random() #making random ids 
    if len(cook_queue) < parameter: heappush(cook_queue,(id_r,x)) #checking if the length is less than the length of reservoir(parameter in this case)
    # push as (key,value) in the queue
    elif id_r > cook_queue[0][0]: heapreplace(cook_queue,(id_r,x))#if id generated randomly is larger than the minimum element then replace with the new element 

#output will be sent as input to the reducer.
for i, j in cook_queue:
    print('%f %s' %(i, j))
