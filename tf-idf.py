from numpy import log

def sota_tfidf(qf, df, b, dl, avdl, c, cf):
    t = (qf * (log(1+log(1+df)))*log((c+1)/cf)) / (1-b+b*(dl/avdl))
    return t

print(sota_tfidf(1.0, 4.0, 0.75, 23.0, 50.0, 100.0, 5.0) + sota_tfidf(1.0, 1.0, 0.75, 23.0, 50.0, 100.0, 3.0))