#!/usr/bin/env python

# Okhtay Azarmanesh
# 02/21/2014
# As an exercise for Udacity Algorithm course
#
# Write partition to return a new array with 
# all values less then `v` to the left 
# and all values greater then `v` to the right
#

def partition(L, v):
    P = [0 for x in range(len(L))]
    rankv = rank(L,v)
    P[rankv] = v
    lo = 0
    hi = rankv + 1
    for val in L:
        if val < v:
            P[lo]=val
            lo += 1
        elif val > v:
            P[hi]=val
            hi +=1
    return P
    
def partition_2(L, v):
    smaller = []
    bigger = []
    for val in L:
        if val < v: smaller += [val]
        if val > v: bigger += [val]
    return smaller + [v] + bigger

def rank(L, v):
    pos = 0
    for val in L:
        if val < v:
            pos += 1
    return pos