import sys

n = int(raw_input())
lines = sys.stdin.readlines()
l = []
for each_line in lines:
    l.append(int(each_line))

l.sort()
for i in l:
    print i


