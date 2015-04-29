import sys
t =[]
if(len(sys.argv) != 2):
    print "Incorrect Number Of Arguments"
    print "Usage: duplicates.py [text-file]"
else:
    fpath = sys.argv[1]
    with open(fpath) as f:
        for line in f:
            t.append(line)
    t = list(set(t))
    with open(fpath, 'w') as f:
        for s in t:
            f.write(s)
