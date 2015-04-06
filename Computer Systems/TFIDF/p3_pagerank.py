import re
import sys
from pyspark import SparkContext
import xml.etree.ElementTree as et
from operator import add
from collections import Counter
import math
import string
import numpy as np
import copy

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

# Processing the page using Elementtree
def processPage(page):
    id = int(page.find('id').text) 
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

#part2

# Calculate the TF-IDF score
def calcTFIDF(tf,idf):
    tfidf = Counter()
    for key in tf.keys():
        tfidf[key] = tf[key] * idf[key]
    return tfidf

# Process the page, instead of returning words, return the number of words
def processPageLen(page):
    id = int(page.find('id').text)
    title = page.find('title').text 
    words = formatText(page.find('revision').find('text').text)
    return id, title, len(words)

# Calculate the similarity between two tf-idf scores, expect tfidfs to be Counter objects
def calcSim(tfidf1, tfidf2):
    # Deepcopy guarantees that the original tfidf1 will not change when temp changes
    temp = copy.deepcopy(tfidf1)
    temp.subtract(tfidf2)
    dist = (sum(np.array(temp.values())**2))**.5
    return dist

# Calculating distances for one page against all other pages, but only if id is smaller than the other
# Reduces similarity calculations by half 
def calcAdj(id, tfidf, tfidfdata, threshold):
    adj = set()
    for i in range(len(tfidfdata)):
        if id < tfidfdata[i][0]:
            if calcSim(tfidf, tfidfdata[i][2]) < threshold:
                adj.add(tfidfdata[i][0])
    return adj

# Breadth first search implementation to calculate connected components
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        page = queue.pop(0)
        if page not in visited:
            visited.add(page)
            queue.extend(graph[page] - visited)
    return visited

# Converting an "undirected" graph into a directed graph going both ways
def convAdjset(distdata):
        adjset = {}
        for line in distdata:
            adjset[line[0]] = line[2]
        for key in adjset.keys():
            for item in adjset[key]:
                adjset[item].add(key)
        return adjset

# Iterate all pages and running BFS search to generate connected components
def calcCC(adjset):
    cc = {}
    track = set()
    for key in adjset.keys():
        if key not in track:
            track.add(key)
            cc[key] = bfs(adjset, key)
            track = track.union(cc[key])
    return cc

# part 3

def computeContribs(urls, rank):
    """Calculates URL contributions to the rank of other URLs."""
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)

def parseNeighbors(urls):
    """Parses a urls pair string into urls pair."""
    parts = re.split(r'\s+', urls)
    return parts[0], parts[1]

# Generate the set of shortpages to filter the url links
def setShortpages(cc, lengths):
    shortpages = set()
    for key in cc.keys():
        if len(cc[key]) == 1:
            id = cc[key].pop()
            shortpages.add(id)
        else:
            ngh = list(cc[key])
            tpl = []
            for i in range(len(ngh)):
                tpl.append((ngh[i], lengths[ngh[i]]))
            id = sorted(tpl,key=lambda x: x[1])[-1][0]
            shortpages.add(id)
    return shortpages

def main(inc, iter):
    #inc = sc.textFile("/datasets/hw3/p3_dataset/page_files/")
    #iter = 10

    threshold = 0.2
    num_pages = inc.count()
    s1 = inc.map(lambda x: x.encode('utf-8'))
    s2 = s1.map(lambda x: et.fromstring(x))
    s3 = s2.filter(lambda x: (x.find('ns').text)=='0')
    s4 = s3.filter(lambda x: (x.find('revision').find('text').text)!='')
    tf = s4.map(lambda x: processPage(x))

    terms = Counter()
    for line in tf.collect():
            for key in line[2]:
                terms[key] += 1

    idf = calcIDF(terms, num_pages)
    tfidf = tf.map(lambda (x, y, z): (x, y, calcTFIDF(z, idf)))
    tfidfdata = tfidf.collect()
    # Calculating the tfidf of each page against all the other pages within tfidfdata
    dist = tfidf.map(lambda (x, y, z,): (x, y, calcAdj(x, z, tfidfdata, threshold)))
    distdata = dist.collect()

    adjset = convAdjset(distdata)
    cc = calcCC(adjset)
 
    # Collecting titles and lengths of each page for easier processing  
    pageData = s4.map(lambda x: processPageLen(x)).collect()
    
    titles = {}
    lengths = {}

    for line in pageData:
        titles[line[0]] = line[1]
        lengths[line[0]] = line[2]
    
    shortpages = setShortpages(cc, lengths)
    inc2 = sc.textFile("/datasets/hw3/p3_dataset/page_link.txt")

    # Loads all URLs from input file and initialize their neighbors. Filters out pairs that do not belong in the connected components set.
    links = inc2.map(lambda urls: parseNeighbors(urls)).filter(lambda (x, y): (int(x) in shortpages and int(y) in shortpages)).distinct().groupByKey().cache()

    # Loads all URLs with other URL(s) link to from input file and initialize ranks of them to one.
    ranks = links.map(lambda (url, neighbors): (url, 1.0))

    # Calculates and updates URL ranks continuously using PageRank algorithm.
    for iteration in xrange(int(iter)):
        # Calculates URL contributions to the rank of other URLs.
        contribs = links.join(ranks).flatMap(
            lambda (url, (urls, rank)): computeContribs(urls, rank))
        # Re-calculates URL ranks based on neighbor contributions.
        ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85 + 0.15)

    rankdata = ranks.collect()
    sort = sorted(rankdata, key=lambda x: x[1], reverse = True)

    f = open('p3_output.txt', 'w')
    for i in range(10):
        id = int(sort[i][0])
        rank = sort[i][1]
        title = titles[id]
        line = "%s %s %s\n" % (id, title, rank)
        if isinstance(line, unicode):
            line = line.encode('ascii','ignore')
        f.write(line)

    f.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: p3_pagerank.py <file> <iterations>"
        exit(-1)
    sc = SparkContext(appName="PageRank")
    inc = sc.textFile(sys.argv[1])
    main(inc, int(sys.argv[2]))

    sc.stop()