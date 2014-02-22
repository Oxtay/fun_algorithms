#!/usr/bin/env python

# Okhtay Azarmanesh
# 02/21/2014
# As an exercise for Udacity Algorithm course
#
# Find the 2nd most popular female name among a list of names

import csv

def create_a_list():
    names = open('yob1995.txt', 'rb')
    lines = names.readlines()
    index_max = find_max(lines)
    lines.pop(index_max)
    index_2nd = find_max(lines)
    print lines[index_2nd]
    
def find_max(lines):
    maxim = ['none', 'none', '0']
    for line in lines:
        temp = line.split(',')
        if int(maxim[2]) < int(temp[2]) and temp[1]=='F':
            maxim = temp
            index = lines.index(line)
    return index

create_a_list()
    