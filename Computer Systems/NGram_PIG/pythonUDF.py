import re
import string

@outputSchema('ngram:chararray')
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

@outputSchema('line:chararray')
def genOutput(ngram, num, pages):
    return type(ngram), type(num), type(pages), pages
    #output = ngram + ' ' + num + '/n'
    #rplchar = '[({})]'
    #for i in range(len(pages)):
    #    pages[i]'
    #rplchar = '[({})]'
    #l1 = line.split('{')
    #l2 = l1[0].split(',')
    #output = l2[0][1:] + ' ' + l2[1] + '/n'
    #l3 = l1[1].split('),')

    #for i in range(len(l3)):
    #    l3[i] = re.sub(rplchar,"",l3[i],0)
    #for i in range(len(l3)):
    #    if l3[i]:
    #        temp = l3[i].split(',')
    #        output += '%s %s/n' % (temp[1], temp[0])
    #return output