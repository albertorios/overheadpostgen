import sys
import numpy as np
#Seed Words
s = []
#Word Weights
w = {}
#Word Count num
wc = {}

def gen(seeds,weights,low,hi,ordr):
    x = np.random.randint(len(seeds))
    y = np.random.randint(low,hi)
    r = seeds[x].split()
    for i in range(y-ordr):
        key = ' '.join(r[i:ordr+i])
        r_total = np.random.random_sample(1)[0]
        total = 0.0
        end = key[len(key)-1]
        if(key not in weights):
            break
        for v in weights[key]:
            total = total + weights[key][v]
            if(total > r_total):
                r.append(v)
                break
    return ' '.join(r)

if(len(sys.argv) != 6):
    print "Incorrect Number Of Arguments"
    print "Usage: markov.py [text-file] [order] [low] [high] [n]"
else:
    fpath = sys.argv[1]
    order = int(sys.argv[2])
    l = int(sys.argv[3])
    h = int(sys.argv[4])
    n_sentences = int(sys.argv[5])
    #Read in Text and Create Word Frequencies
    with open(fpath) as f:
        for line in f:
            x = line.split()
            if(len(x) > order):
                s.append(' '.join(x[:order]))
                for i in range(len(x) - order):
                    key = ' '.join(x[i:order+i])
                    val = x[order+i]
                    if (key not in w):
                        w[key] = {}
                        wc[key] = 0
                    wc[key] = wc[key] +1
                    if (val not in w[key]):
                        w[key][val] = 1.0
                    else:
                        w[key][val] = w[key][val] +1.0
    for k in w:
        for v in w[k]:
            w[k][v] = w[k][v] / wc[k]
    for i in range(n_sentences):
        print gen(s,w,l,h,order)
