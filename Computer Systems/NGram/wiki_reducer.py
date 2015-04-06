#!/usr/bin/python

from operator import itemgetter
import sys

current_gram = None
current_count = 0
gram = None
n = 5

list = {}
# input comes from STDIN
for each in sys.stdin:
    # remove leading and trailing whitespace
    line = each.strip()
    # parse the input we got from mapper.py
    temp = line.split('\t')
    gram = temp[0]
    count = temp[1]
    meta = temp[2].split(':')

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_gram == gram:
        current_count += count
        list[meta[0]] = meta[1]
    else:
        if current_gram:
            # write result to STDOUT
            for key in list.iterkeys():
                parse = parse + key + ':' + list[key] + '\t'
            parse = parse.strip()
            print '%s\t%s\t%s' % (current_gram, current_count, parse)
        current_count = count
        current_gram = gram
        list = {}
        parse = ''
        list[meta[0]] = meta[1]

# do not forget to output the last word if needed!
if current_gram == gram:
    parse = ''
    for key in list.iterkeys():
        parse = parse + key + ':' + list[key] + '\t'
    parse = parse.strip()
    print '%s\t%s\t%s' % (current_gram, current_count, parse)