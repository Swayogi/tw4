#!/usr/bin/env python
import sys
opiniondict = {}
count = 0
for line in sys.stdin:
    line = line.strip()
    pid, opinion = line.split('\t')
    if opinion in opiniondict:
        opiniondict[opinion].append(count + 1)
    else:
        opiniondict[opinion] = []
        opiniondict[opinion].append(count + 1)
for opinion in opiniondict.keys():
    count = len(opiniondict[opinion])
    print '%s\t%s' % (opinion, count)
