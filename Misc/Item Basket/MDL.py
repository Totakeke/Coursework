import sys
import pandas as pd
import itertools as it
import matplotlib.pyplot as plt

def plotHist(data):
    # To start association analysis, need to determine an appropriate minimum support level
    # This can be done by plotting the mean of each item
    plt.hist(data.mean())
    plt.xlabel('Mean')
    plt.ylabel('Frequency')
    plt.show()
    # Plot shows that most items appear less than 5% of the time while there are a group of items appearing more than 20%

def assocAnalysis(data, min_support, max_set = 10):
    # Candidates are sets of items to explore
    # Support stores the the mean of the set of items appearing in the dataset together
    # Itemsets are the results and the items frequently purchased together
    candidates = {}
    support = {}
    itemsets = {}

    # For item sets of size 1, iterate over all item means and extract items with mean values more than minimum support
    support[0] = {}
    itemsets[0] = []
    j = 0
    for i in list(data.mean() > min_support):
        if i == True:
            itemsets[0].append("item_" + str(j))
            support[0]["item_" + str(j)] = data.mean()[j]
        j += 1

    # Items extracts the unique list of individual item candidates
    items = itemsets[0]

    # This is the main function that iterates over to find association for item sets of size 2 and bigger
    # Indexing starts at 0, i.e. itemsets[2] would contain item sets of size 3
    for i in range(1,max_set+1):
        if len(itemsets[i-1]) != 0:
            candidates[i] = list(it.combinations(items, i+1))
            support[i] = {}
            itemsets[i] = []
            for j in candidates[i]:
                temp = data[data[j[0]] == 1]
                if i > 1:
                    for k in range(1,i):
                        temp = temp[temp[j[k]] == 1]
                if len(temp[temp[j[i]] == 1])/float(len(data)) > min_support:
                    itemsets[i].append(j)
                    support[i][j]= len(temp[temp[j[i]] ==1])/float(len(data))
            items = []
            for m in itemsets[i]:
                for n in range(0, 1+1):
                    if not m[n] in items:
                        items.append(m[n])
        # Stop the for loop if there are no viable candidates in the latest loop
        if len(itemsets[i-1]) == 0:
            break
    return itemsets, support

def printResults(itemsets, support):
    print "The largest item set size is " + str(len(itemsets)-1) + " and the item sets are:"
    for i in itemsets[len(itemsets)-2]:
        print str(i) + ": " + str(support[len(itemsets)-2][i]) + " support"

    print "The second largest item set size is " + str(len(itemsets)-2) + " and the item sets are:"
    for i in itemsets[len(itemsets)-3]:
        print str(i) + ": " + str(support[len(itemsets)-3][i]) + " support"

def fetchArgs():
    if len(sys.argv) != 3:
        print "Usage: python <source_file> <path_of_input_data_file> <min_support_level>"
        sys.exit()
    else:
        file_path = sys.argv[1]
        min_support = float(sys.argv[2])
    return file_path, min_support

def main():
    file_path, min_support = fetchArgs()
    # Read in the data into a pandas data frame
    data = pd.read_csv(file_path,sep=',',index_col='id')

    ## Plot a histogram to get an idea of the spread of each item mean
    #plotHist(data)
    # Based on plot, discover that most of items appear infrequently while a small group appear more than 20%
    # Perform association analysis using a minimum support level of 20%
    #min_support = 0.2

    # The max_set parameter determines the largest item set size to explore
    itemsets, support = assocAnalysis(data, min_support)
    printResults(itemsets, support)

if __name__ == "__main__":
    main()