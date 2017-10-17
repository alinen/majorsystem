import string
def outputCards(f, prefix):
    for line in f:
        tokens = line.split(",")
        numstr = string.strip(tokens[0])
        wordstr = string.strip(tokens[1])
        print "%s (%s),%s"%(numstr, prefix, wordstr)
        print "%s, %s (%s)"%(wordstr, numstr, prefix)

adjs = open('majorsystem-adjs.csv', 'r')
nouns = open('majorsystem-nouns.csv', 'r')
verbs = open('majorsystem-verbs.csv', 'r')

outputCards(adjs, "adj")
outputCards(nouns, "nouns")
outputCards(verbs, "verbs")
