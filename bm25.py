from numpy import log

def bm25(k, b, tf, dl, avdl, N, df):
    t = (k+1)*tf*log((N-df+0.5)/(df+0.5)) / (k*(1-b+b*((dl)/(avgl)))+tf)
    return t

print(bm25())