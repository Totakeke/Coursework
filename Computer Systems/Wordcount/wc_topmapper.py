#!/usr/bin/python
import sys

# input comes from STDIN (standard input)
# for the 3-gram problem, the top-10 mapper and reducer does the same task
# taking the available input and outputting the ones with top 10 highest count

# run the script with -D mapreduce.job.reduces=1 as the final output requires all results to be on the same reducer

list = []

# split the input into the 3-gram and the count
for each in sys.stdin:
    temp = each.strip().split('\t')
    list.append((temp[0],int(temp[1])))

# sort by the second column which contains the count
list.sort(key=lambda x: x[1],reverse=True)

for i in range(10):
    print '%s\t%s' % (list[i][0], list[i][1])

