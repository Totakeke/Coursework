#!/usr/bin/python
import sys

# input comes from STDIN (standard input)

n = 3

for each in sys.stdin:
    # remove leading and trailing whitespace, remove punctuation except hyphens, remove numbers, remove double hyphens, and convert to lowercase
    line = (((each.strip()).translate(None, '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~0123456789')).replace("--", " ")).lower()
    # split the line into words
    words = line.split()
    # build 3-grams from the list of words
    for i in range(len(words)-n+1):
        gram = ''
        for j in range(i,i+n):
            gram = gram + ' ' + words[j]
        gram = gram.strip()
        print '%s\t%s' % (gram, 1)

