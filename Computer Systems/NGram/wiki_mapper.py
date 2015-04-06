#!/usr/bin/python

import sys
import xml.etree.ElementTree as et
import re
import string

n = 5
data = ''

# function that returns true if the given string contains purely ascii characters
def is_ascii(string):
    return all(ord(char) < 128 for char in string)

for line in sys.stdin:
    # as ElementTree requires a root tag, parse xml by treating each <page></page> chunk as separate inputs
    if '<page>' in line:
        data = data + line
        inpage = True
    elif '</page>' in line:
        inpage = False
        data = data + line
        page = et.fromstring(data)
        title = page.find('title').text
        title = title.encode('ascii', 'ignore')
        pid = page.find('id').text
        text = page.find('revision').find('text').text
        # check if text is not empty before proceeding
        if text:
            for line in text.splitlines():
                # remove punctuation selectively 
                temp = re.sub('[' + string.punctuation.replace("-", "") + "0123456789" + ']', "", line, 0, 0)
                temp = (temp.strip()).lower()
                temp = temp.replace("\\", "")
                temp = temp.replace("--", "")
                temp = temp.replace(" -", "")
                temp = temp.replace("- ", "")
                words = temp.split()
                # check if words are purely ascii, if not, remove from the word list
                delist = []
                for i in range(len(words)):
                    if not is_ascii(words[i]):
                        delist.append(i)
                for i in range(len(delist)):
                    del words[delist[-(i+1)]]
                # build the 5-grams    
                for i in range(len(words)-n+1):
                    gram = ''
                    for j in range(i,i+n):
                        gram = gram + ' ' + words[j]
                    gram = gram.strip()
                    print '%s\t%s\t%s:%s' % (gram, 1, title, pid)
        data = ''
    elif inpage == True:
        data = data + line

