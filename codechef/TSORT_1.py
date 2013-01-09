import sys
l  = map(int, sys.stdin.readlines())
l.pop(0)
l.sort()
for x in l: print x

