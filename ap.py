import sys

s = sys.argv[1]
arr = []
for c in s:
    arr.append(c)

relevance_level = {
    # REPLACE WITH YOUR OWN RELEVANCE SETTINGS
    'a': True,
    'b': True,
    'c': False,
    'd': False,
    'e': True,
    'f': False
}

def AP(alist, aDict):
    relevance_arr = []
    for doc in alist:
        relevance_arr.append(relevance_level[doc])

    n = 0
    for key, value in aDict.iteritems():
        if value:
            n += 1
    
    ap = 0.0
    a, b = 1, 1
    for i in range(len(relevance_arr)):
        if relevance_arr[i]:
            ap += float(a)/float(b)
            a += 1
        b += 1

    return ap/float(n)

print "AP is: {0}".format(AP(arr, relevance_level))
