import re
import string

@outputSchema("y:bag{t:tuple(nGram:chararray)}")
def nGramsGenerate(chararray, n):
    list = []
    rplchar = '[' + string.punctuation.replace("-", "") + "0123456789" + ']'
    line = re.sub(rplchar, "", chararray, 0)
    line = (line.strip()).lower()
    line = line.replace("\\", "")
    line = line.replace("--", "")
    line = line.replace(" -", "")
    line = line.replace("- ", "")
    words = line.split()
    # build 3-grams from the list of words
    for i in range(len(words)-n+1):
        gram = ''
        for j in range(i,i+n):
            gram = gram + ' ' + words[j]
        list.append(gram.strip())
    return list

