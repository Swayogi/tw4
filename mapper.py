#!/usr/bin/env python  
import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if len(line) >= 2:
        id = line[0]
        opinion = line[4]
        print '%s\t%s' % (id, opinion)  
