import xml.etree.ElementTree as et
from operator import add
from collections import Counter
import re
import math
import sys
import string
from pyspark import SparkContext

# Function to check if the string is ascii, used for checking words in lists
def is_ascii(string):
    return all(ord(char) < 128 for char in string)

# Function to format text
def formatText(text): 
    temp = re.sub('[' + string.punctuation.replace("-", "") + "0123456789" + ']', "", text, 0, 0)
    temp = (temp.strip()).lower()
    temp = temp.replace("\\", "")
    temp = temp.replace("--", " ")
    temp = temp.replace(" -", " ")
    temp = temp.replace("- ", " ")
    words = temp.split()
    # Remove the word if it contains unicode characters
    delist = []
    for i in range(len(words)):
        if not is_ascii(words[i]):
            delist.append(i)
    for i in range(len(delist)):
        del words[delist[-(i+1)]]
    # Convert all words to string
    for i in range(len(words)):
        words[i] = words[i].encode('ascii','ignore')
    return words;

# Calculate the term frequency using Counter collections
def termFrequency(row):
    cnt = Counter()
    for word in row:
        cnt[word] += 1
    for word in cnt.keys():
        cnt[word] = cnt[word]/float(len(row))
    return cnt

# Formatting the output to the desired output
def printOut(id, title, tuple):
    if isinstance(title, unicode):
        title = title.encode('ascii', 'ignore')
    return '%s %s %s %s\n' % (id, title, tuple[0], tuple[1])

# Processing the page using Elementtree
def processPage(page):
    id = page.find('id').text 
    title = page.find('title').text 
    words = formatText(page.find('revision').find('text').text)
    tf = termFrequency(words)
    return id, title, tf

# Using a counter to generate the IDF
def calcIDF(terms, num_pages):
    cnt = Counter()
    for key in terms.keys():
        cnt[key] = math.log(num_pages/terms[key])
    return cnt

# Returns the word with the maximum tfidf
def calcMax(tf, idf):
    tfidf = Counter()
    for key in tf.keys():
        tfidf[key] = tf[key] * idf[key]
    # Ascending sort and [-1] to return the last element
    max = sorted(tfidf,key=tfidf.get)[-1]
    return max, tfidf[max]

def main(inc):
    #inc = sc.textFile("/datasets/hw3/p1_dataset/")
    num_pages = inc.count()
    s1 = inc.map(lambda x: x.encode('utf-8'))
    s2 = s1.map(lambda x: et.fromstring(x))
    s3 = s2.filter(lambda x: (x.find('ns').text)=='0')
    s4 = s3.filter(lambda x: (x.find('revision').find('text').text)!='')

    tf = s4.map(lambda x: processPage(x))

    # As keywords only appear once in the term frequency as a key value pair, use this to count if a word appear in a page or not (binary)
    terms = Counter()
    for line in tf.collect():
            for key in line[2]:
                terms[key] += 1

    idf = calcIDF(terms, num_pages)
    tfidf = tf.map(lambda (x, y, z): (x, y, calcMax(z, idf)))
    output = tfidf.map(lambda (x, y, z): printOut(x, y, z))
    outputdata = output.collect()
    f = open('p1_output.txt', 'w')
    for line in outputdata:
        f.write(line)

    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: p1_tf_idf.py <file>"
        exit(-1)
    sc = SparkContext(appName="tdidf")
    inc = sc.textFile(sys.argv[1])
    main(inc)

    sc.stop()
