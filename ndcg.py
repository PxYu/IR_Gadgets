import sys
import math

s = sys.argv[1]
arr = []
for c in s:
    arr.append(c)

relevance_level = {
    # REPLACE WITH YOUR OWN RELEVANCE SETTINGS
    'a': 4.0,
    'b': 2.0,
    'c': 0.0,
    'd': 0.0,
    'e': 1.0,
    'f': 0.0
}

def nDCG(alist):
    relevance_arr = []
    for doc in alist:
        relevance_arr.append(relevance_level[doc])
    
    # compute DCG
    dcg = 0.0
    print "Relevance levels: {0}".format(relevance_arr)
    for i in range(len(relevance_arr)):
        dcg += relevance_arr[i] / math.log(i+2, 2)
    
    # compute iDCG
    idcg = 0.0
    relevance_arr.sort(reverse=True)
    print "Sorted relevance levels: {0}".format(relevance_arr)
    for i in range(len(relevance_arr)):
        idcg += relevance_arr[i] / math.log(i+2, 2)

    print "nDCG is {0}".format(dcg/idcg)
        
nDCG(arr)
