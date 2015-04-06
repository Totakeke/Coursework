#!/usr/bin/python
import sys

# input comes from STDIN (standard input)

list = []
pages = ''

for each in sys.stdin:
    temp = each.strip().split('\t')
    for i in range(len(temp[2:])):
        pages = pages + temp[2+i] + '\t'
    pages = pages.strip()
    list.append((temp[0],int(temp[1]), pages))
    pages = ''

list.sort(key=lambda x: x[1],reverse=True)

for i in range(5):
    print '%s\t%s\t%s' % (list[i][0], list[i][1], list[i][2])